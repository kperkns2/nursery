# app.py
import streamlit as st
from datetime import datetime
import pandas as pd
import os
import json

# Try to import gspread; if not installed, we'll guide the user.
try:
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials
    GS_ENABLED = True
except Exception:
    GS_ENABLED = False

st.set_page_config(
    page_title="Nursery Staff Audio Training — Landing Page",
    page_icon="🌱",
    layout="centered",
)

# ---------- HERO ----------
st.title("Grow Smarter: Staff Training Audio for Missouri Nurseries 🌱")
st.subheader("Short, practical audio episodes your staff will actually listen to — and customers will benefit from.")

st.markdown(
    """
**Why this matters:** In local review analysis, roughly **40% of 5-star reviews** for independent nurseries mention *knowledgeable staff* and helpful advice.
That means better-trained staff directly correlates to reputation, repeat visits, and increased sales.  
Our audio series makes it easy to hone those skills — quick, practical lessons staff can listen to between tasks.
"""
)

st.divider()

# ---------- AUDIO PLAYER / PRODUCT PITCH ----------
st.header("Preview: Soil Types & Amendments (5-minute episode)")
st.markdown(
    """
This episode trains staff to quickly identify clay, loam, and rocky soils, recommend appropriate amendments or workarounds,
and close the conversation with clear next steps a customer can follow.  Perfect for onboarding new hires
and refreshing seasonal knowledge.
"""
)

AUDIO_FILE = "soil_amendment.mp3"  # Put your mp3 next to app.py or change this path

if os.path.exists(AUDIO_FILE):
    audio_bytes = open(AUDIO_FILE, "rb").read()
    st.audio(audio_bytes, format="audio/mp3")
else:
    st.warning(
        f"Audio file not found at `{AUDIO_FILE}`. Place `soil_amendment.mp3` in the app folder or update AUDIO_FILE path in app.py."
    )

st.markdown("---")

# ---------- BENEFITS ----------
st.header("What you get with a subscription")
st.write(
    """
- **25 concise training episodes** (~5 minutes each) that cover customer conversations, plant picks, seasonal care, and troubleshooting.
- **Staff-first design:** practical language, role-playing case studies, and pro tips to use on the sales floor.
- **Customer-facing spin-offs:** short 60–90 second audio clips you can link with QR codes to plant tags or receipts.
- **Low friction:** no app installs for staff — play in break rooms, on a POS tablet, or push to internal comms.
"""
)

st.markdown(
    """
**Business impact (how to pitch it to owners):**  
- Better-trained staff = faster service + fewer product returns.  
- Knowledgeable staff are mentioned in ~40% of five-star reviews — that’s *direct reputation value*.  
- When customers feel confident, they come back and spend more on follow-up supplies (mulch, fertilizer, tools).
"""
)

st.divider()

# ---------- LEAD FORM ----------
st.header("Request a tailored demo or pricing")
st.write("Fill out the quick form below and we'll follow up with pricing, a demo, and how we can brand the audio for your nursery.")

with st.form("lead_form", clear_on_submit=False):
    company = st.text_input("Nursery name", placeholder="e.g., Greenway Nursery")
    manager_name = st.text_input("Contact name", placeholder="e.g., Jamie Smith")
    email = st.text_input("Email", placeholder="you@nursery.com")
    phone = st.text_input("Phone (optional)")
    employees = st.number_input("Number of staff (estimate)", min_value=1, step=1, value=5)
    interest = st.selectbox("What are you most interested in?", [
        "Staff training only",
        "Customer-facing audio (QR tags)",
        "Both staff + customer audio",
        "Custom-branded episodes"
    ])
    message = st.text_area("Message / Questions (optional)")
    submit = st.form_submit_button("Send request")

def _append_to_local_csv(row_dict, csv_path="leads_local.csv"):
    df = pd.DataFrame([row_dict])
    if os.path.exists(csv_path):
        df.to_csv(csv_path, mode="a", header=False, index=False)
    else:
        df.to_csv(csv_path, index=False)

def _append_to_gsheet(row_list, creds_json=None, sheet_name="Nursery Leads"):
    """
    Append a single row_list to a Google Sheet.
    creds_json: path to service account json or dict of credentials (string).
    sheet_name: name of target spreadsheet (must exist and be shared with service account email).
    Returns True if success, False otherwise.
    """
    try:
        # Scope and client
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        if isinstance(creds_json, str) and os.path.exists(creds_json):
            creds = ServiceAccountCredentials.from_json_keyfile_name(creds_json, scopes=scope)
            gc = gspread.authorize(creds)
        else:
            # try reading from STREAMLIT_SECRETS if provided as JSON string
            creds_dict = None
            if isinstance(creds_json, dict):
                creds_dict = creds_json
            else:
                st.error("Invalid credentials provided for Google Sheets.")
                return False
            creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scopes=scope)
            gc = gspread.authorize(creds)

        # Open spreadsheet by title (must already exist)
        sh = gc.open(sheet_name)
        worksheet = sh.sheet1
        worksheet.append_row(row_list)
        return True
    except Exception as e:
        st.error(f"Google Sheets save failed: {e}")
        return False

if submit:
    now = datetime.now().isoformat(sep=" ", timespec="seconds")
    lead = {
        "timestamp": now,
        "nursery": company,
        "manager": manager_name,
        "email": email,
        "phone": phone,
        "employees": employees,
        "interest": interest,
        "message": message
    }

    # Try Google Sheets if credentials set in Streamlit secrets
    saved = False
    gs_reason = ""
    if GS_ENABLED:
        # Two ways to provide creds:
        # 1) Put path to service account json in STREAMLIT_SECRETS["gcloud_service_account_path"]
        # 2) Put the full json content under STREAMLIT_SECRETS["gcloud_service_account_json"]
        try:
            gpath = st.secrets.get("gcloud_service_account_path", None)
            gjson = st.secrets.get("gcloud_service_account_json", None)
            sheet_name = st.secrets.get("google_sheet_name", "Nursery Leads")

            if gpath:
                success = _append_to_gsheet(
                    [now, company, manager_name, email, phone, employees, interest, message],
                    creds_json=gpath,
                    sheet_name=sheet_name
                )
                saved = success
                if not success:
                    gs_reason = "gspread failed with file path."
            elif gjson:
                # gjson should be a dict in secrets
                success = _append_to_gsheet(
                    [now, company, manager_name, email, phone, employees, interest, message],
                    creds_json=gjson,
                    sheet_name=sheet_name
                )
                saved = success
                if not success:
                    gs_reason = "gspread failed with JSON from secrets."
            else:
                gs_reason = "No Google credentials found in Streamlit secrets."
        except Exception as e:
            gs_reason = f"Google Sheets attempt raised: {e}"
    else:
        gs_reason = "gspread not installed or available."

    if saved:
        st.success("Thanks! Your request was sent. We'll follow up by email within 2 business days.")
    else:
        # Fallback: save locally and show instructions to enable Google Sheets
        _append_to_local_csv(lead)
        st.success("Thanks — your request was saved locally. Please configure Google Sheets to save leads to the cloud.")
        st.info(
            "To enable Google Sheets saving, install `gspread` and add a Google Service Account JSON to Streamlit secrets "
            "as `gcloud_service_account_json` (or provide a path in `gcloud_service_account_path`). "
            "Also set `google_sheet_name` to the spreadsheet title and share that sheet with the service account email."
        )
        if gs_reason:
            st.write("Note:", gs_reason)

st.divider()

# ---------- FOOTER / NEXT STEPS ----------
st.markdown(
    """
### Next steps you can offer the manager
1. Ask for a 10-minute demo (we can play 2 episodes and show how QR care tips work).  
2. Offer a 30-day pilot for a single location at a reduced rate to prove ROI.  
3. Provide branded intros (nursery name and contact) on each episode for a white-label feel.

If you'd like, include a link to a PDF one-sheet, or ask us to prepare an example QR tag for a top-selling plant.
"""
)

st.caption("Built for Missouri nurseries — staff-first audio training to turn knowledge into 5-star experiences.")
