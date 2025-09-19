import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# -------------------
# Page Config
# -------------------
st.set_page_config(
    page_title="Nursery Training Audio Series",
    page_icon="🌱",
    layout="centered"
)

# -------------------
# Header
# -------------------
st.title("🌱 Nursery Knowledge Training")
st.subheader("Turn Plant Enthusiasts Into Confident, Trusted Advisors")

st.markdown("""
When customers walk into your nursery, they’re not just buying plants —  
they’re buying **expertise**.  

In Missouri, nearly **40% of 5-star reviews for local nurseries mention “knowledgeable staff.”**  
That trust directly drives repeat business and higher sales.  

We help your team shine with **short, practical audio training episodes** —  
easy to listen to, and immediately useful with customers.
""")

# -------------------
# Demo Audio
# -------------------
st.markdown("### 🎧 Sample Episode: Soil Amendments in Missouri")
audio_file = open("soil_ammendments.mp3", "rb")
st.audio(audio_file.read(), format="audio/mp3")

st.markdown("""
This 5-minute episode helps staff explain the differences between **clay, loam, and rocky soils**,  
and how to recommend the **right amendments** with confidence.  

Every episode is:
- ✅ **Focused** on the questions real customers ask  
- ✅ **Actionable** with clear talking points staff can use right away  
- ✅ **Designed** to build trust, upsell naturally, and create loyal customers  
""")

# -------------------
# Benefits Section
# -------------------
st.markdown("### 🌟 Why Nurseries Love This Training")
st.markdown("""
- **Boost Reviews & Reputation** — Customers value knowledgeable staff more than price.  
- **Train Efficiently** — 5-minute episodes fit into daily routines.  
- **Increase Sales** — Confident recommendations lead to more purchases.  
- **Build Loyalty** — Staff sound like plant experts, customers keep coming back.  
""")

# -------------------
# Connect to Google Sheets via st.secrets
# -------------------
SCOPE = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/drive"]

creds = Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=SCOPE
)
client = gspread.authorize(creds)

SPREADSHEET_ID = st.secrets["spreadsheet_id"]
sheet = client.open_by_key(SPREADSHEET_ID).sheet1

# -------------------
# Lead Form
# -------------------
st.markdown("---")
st.markdown("## 📋 Request More Information")

st.markdown("""
Interested in bringing **expert audio training** to your nursery?  
Fill out the form below and we’ll share pricing, customization options,  
and how other nurseries are using this to **improve staff confidence**  
and **grow their bottom line**.
""")

with st.form("lead_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Work Email")
    nursery_name = st.text_input("Nursery Name")
    message = st.text_area("What would you most like to improve about staff training?")

    submitted = st.form_submit_button("Request Info")
    if submitted:
        if not name or not email:
            st.error("Please enter at least your name and email.")
        else:
            sheet.append_row([name, email, nursery_name, message])
            st.success("✅ Thank you! We’ll be in touch shortly.")

# -------------------
# Footer
# -------------------
st.markdown("---")
st.caption("Made for Missouri nurseries — empowering staff, delighting customers, and driving growth.")
