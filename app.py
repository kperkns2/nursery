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

st.title("🌱 Grow Knowledge. Grow Sales.")
st.subheader("Audio Training for Nursery Staff & Customers")

# -------------------
# Hero Section
# -------------------
st.markdown("""
Boost your nursery’s reputation with staff who **sound like experts**.  
In Missouri, nearly **40% of 5-star nursery reviews mention “knowledgeable staff.”**  
Our short, practical audio episodes sharpen your team’s plant knowledge —  
so they can deliver the confident advice customers love.
""")

# -------------------
# Demo Audio
# -------------------
st.markdown("### 🎧 Sample Episode: Soil Amendments in Missouri")
audio_file = open("soil_episode.mp3", "rb")
st.audio(audio_file.read(), format="audio/mp3")

st.markdown("""
This 5-minute episode trains staff how to explain clay, loam, and rocky soils —  
plus what amendments work best. Every episode is **practical, customer-oriented,  
and designed to increase customer trust**.
""")

# -------------------
# Connect to Google Sheets via st.secrets
# -------------------
SCOPE = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/drive"]

# Read the service account JSON from secrets
creds = Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=SCOPE
)
client = gspread.authorize(creds)

# Open your sheet (replace with your actual Spreadsheet ID)
SPREADSHEET_ID = st.secrets["spreadsheet_id"]
sheet = client.open_by_key(SPREADSHEET_ID).sheet1

# -------------------
# Lead Form
# -------------------
st.markdown("---")
st.markdown("## 📋 Get More Information")

with st.form("lead_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Work Email")
    nursery_name = st.text_input("Nursery Name")
    message = st.text_area("What would you like to improve about your staff training?")

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
st.caption("Made for Missouri nurseries — empowering staff, delighting customers.")
