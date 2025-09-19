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
# Highlight Section
# -------------------
def highlight_section(text, bg="#E8F4FA", color="#004F71"):
    st.markdown(
        f"""
        <div style="
            background-color:{bg};
            color:{color};
            padding:2rem;
            border-radius:12px;
            margin:2rem 0;
            text-align:center;
            font-size:1.3rem;
            font-weight:600;
            line-height:1.6;
        ">
            {text}
        </div>
        """,
        unsafe_allow_html=True,
    )

# -------------------
# Styled Section
# -------------------
def styled_section(content_func, bg="#FFFFFF"):
    with st.container():
        st.markdown(
            f"""
            <div style="background-color:{bg}; padding:2rem; border-radius:10px; margin:1rem 0;">
            """,
            unsafe_allow_html=True,
        )
        content_func()
        st.markdown("</div>", unsafe_allow_html=True)

# -------------------
# Hero Section
# -------------------
st.title("🌱 Grow Knowledge. Grow Sales.")
st.subheader("Audio Training for Nursery Staff & Customers")

styled_section(
    lambda: st.markdown(
        """
        When customers walk into your nursery, they’re not just buying plants —  
        they’re buying **expertise**.  

        Our short, practical audio series equips your staff with the right words,  
        so they can confidently guide every customer decision.
        """
    ),
    bg="#FFFFFF"
)

highlight_section(
    "🌟 In Missouri, nearly **40% of 5-star nursery reviews** mention *knowledgeable staff*.\n\n"
    "Ensure your team earns that praise — every customer, every visit."
)

# -------------------
# Audio Sample Section
# -------------------
def audio_demo():
    st.markdown("### 🎧 Click to Listen: Soil Amendments in Missouri")
    st.markdown(
        "**This 5-minute episode shows staff how to explain clay, loam, and rocky soils,** "
        "and recommend the right amendments to customers with confidence."
    )
    st.audio("soil_ammendments.mp3", format="audio/mp3")
    st.markdown(
        """
        ✅ Practical, professional, and customer-oriented  
        ✅ Builds staff confidence and customer trust  
        ✅ Fits easily into daily routines
        """
    )

styled_section(audio_demo, bg="#F9F9F9")

# -------------------
# Series Overview
# -------------------
def overview():
    st.markdown("### 📚 The 25-Episode Training Series")
    st.markdown(
        """
        Each episode is short, focused, and designed to help staff handle real customer scenarios.

        **Topics include:**
        - Missouri soil types & amendments  
        - Choosing trees & shrubs for local climates  
        - Seasonal care & maintenance tips  
        - Explaining native vs. exotic plants  
        - Watering, fertilizing, and pest prevention  
        - Common customer questions — answered with confidence  
        - And much more…
        """
    )
    st.markdown(
        "Together, the series builds a foundation of **expert communication** "
        "that keeps your staff sharp and customers coming back."
    )

styled_section(overview, bg="#FFFFFF")

# -------------------
# Google Sheets Setup
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
# Lead Capture Form
# -------------------
def lead_form():
    st.markdown("## 📋 Ready to Bring Expert Training to Your Nursery?")
    st.markdown(
        "Fill out the form below to receive pricing, customization options, "
        "and see how Missouri nurseries are already benefiting."
    )
    with st.form("lead_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Work Email")
        nursery_name = st.text_input("Nursery Name")
        message = st.text_area(
            "What would you like to improve about your staff training?"
        )

        submitted = st.form_submit_button("🚀 Request Info")
        if submitted:
            if not name or not email:
                st.error("Please enter at least your name and email.")
            else:
                sheet.append_row([name, email, nursery_name, message])
                st.success("✅ Thank you! We’ll be in touch shortly.")

styled_section(lead_form, bg="#F9F9F9")

# -------------------
# Footer
# -------------------
st.markdown("---")
st.caption("Made for Missouri nurseries — empowering staff, delighting customers.")
