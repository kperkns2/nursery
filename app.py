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
# Helper for styled section
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
# Header / Hero
# -------------------
st.title("🌱 Grow Knowledge. Grow Sales.")
st.subheader("Audio Training for Nursery Staff & Customers")

styled_section(
    lambda: st.markdown(
        """
        When customers walk into your nursery, they’re not just buying plants —  
        they’re buying **expertise**.  

        In Missouri, nearly **40% of 5-star reviews for nurseries mention “knowledgeable staff.”**  
        That knowledge directly drives trust, loyalty, and repeat business.  

        Our short, practical audio series equips your staff with the right words,  
        so they can confidently guide every customer decision.
        """
    ),
    bg="#FFFFFF"
)

# -------------------
# Audio Sample Section
# -------------------
def audio_demo():
    st.markdown("### 🎧 Featured Sample Episode")
    st.markdown(
        "**Soil Amendments in Missouri** — how to explain clay, loam, and rocky soils, "
        "plus which amendments build trust with customers."
    )
    st.audio("soil_ammendments.mp3", format="audio/mp3")
    st.markdown(
        """
        👉 This 5-minute training shows how everyday questions turn into customer confidence.  
        Every episode is **practical, professional, and customer-oriented**.
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
    st.markdown("## 📋 Get More Information")
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
