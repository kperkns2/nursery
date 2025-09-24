import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# -------------------
# Page Config
# -------------------
st.set_page_config(page_title="Nursery Training Audio Series", layout="wide")

# -------------------
# Google Sheets Setup
# -------------------
SCOPE = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]
creds = Credentials.from_service_account_info(
    st.secrets["gcp_service_account"], scopes=SCOPE
)
client = gspread.authorize(creds)
SPREADSHEET_ID = st.secrets["spreadsheet_id"]
sheet = client.open_by_key(SPREADSHEET_ID).sheet1

# -------------------
# Custom Styles
# -------------------
st.markdown(
    """
    <style>
      body {
        margin: 0;
        font-family: 'Poppins', sans-serif;
        line-height: 1.6;
        color: #2d2d2d;
        background-color: #fdfdfd;
      }

      header {
        background: linear-gradient(rgba(0, 70, 40, 0.7), rgba(0, 70, 40, 0.7)),
        url('https://images.unsplash.com/photo-1501004318641-b39e6451bec6?auto=format&fit=crop&w=1600&q=80') no-repeat center center/cover;
        color: white;
        text-align: center;
        padding: 12rem 1rem 8rem;
      }

      header h1 {
        font-size: 3.5rem;
        margin: 0;
        font-weight: 700;
      }

      header p {
        font-size: 1.4rem;
        margin-top: 1rem;
        font-weight: 400;
      }

      .section {
        max-width: 950px;
        margin: auto;
        padding: 4rem 2rem;
      }

      .section.alt {
        background-color: #f9f9f9;
      }

      .highlight.blue {
        background: linear-gradient(135deg, #e8f4fa, #cfe6f3);
        color: #004f71;
        padding: 2.5rem;
        border-radius: 16px;
        text-align: center;
        font-size: 1.4rem;
        font-weight: 600;
        margin: 3rem auto;
        box-shadow: 0 6px 20px rgba(0,0,0,0.12);
        max-width: 850px;
      }

      .highlight.gray {
        background: #f2f2f2;
        color: #333;
        padding: 2rem;
        border-radius: 12px;
        text-align: center;
        font-size: 1.2rem;
        font-weight: 500;
        margin: 2rem auto;
        max-width: 800px;
      }

      h2 {
        font-size: 2rem;
        margin-bottom: 1rem;
        color: #002b45;
        text-align: center;
      }

      audio {
        display: block;
        margin: 1.5rem auto;
        width: 100%;
        max-width: 650px;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
      }

      ul li {
        margin: 0.6rem 0;
      }

      form label {
        font-weight: 600;
        display: block;
        margin-top: 1rem;
        color: #002b45;
      }

      input, textarea {
        border: 1px solid #ccc;
        border-radius: 8px;
        font-size: 1rem;
        padding: 0.75rem;
        width: 100%;
        margin-top: 0.3rem;
        font-family: 'Poppins', sans-serif;
      }

      .cta {
        text-align: center;
        margin-top: 2rem;
      }

      .cta button {
        background: linear-gradient(135deg, #0077b6, #004f71);
        color: white;
        border: none;
        padding: 1rem 2.5rem;
        border-radius: 50px;
        font-size: 1.2rem;
        cursor: pointer;
        transition: transform 0.2s, box-shadow 0.3s;
        box-shadow: 0 6px 15px rgba(0,0,0,0.15);
        font-weight: 600;
      }

      footer {
        text-align: center;
        background: #002b45;
        color: white;
        padding: 2rem;
        margin-top: 2rem;
      }
    </style>

    <header>
      <h1>Grow Knowledge. Grow Sales.</h1>
      <p>Audio Training for Nursery Staff & Customers in Missouri</p>
    </header>
    """,
    unsafe_allow_html=True,
)

# -------------------
# Intro Section
# -------------------
st.markdown(
    """
    <section class="section">
      <p>When customers walk into your nursery, they’re not just buying plants — they’re buying <strong>expertise</strong>. Our short, practical audio series equips your staff with the right words, so they can confidently guide every customer decision.</p>
    </section>
    <div class="highlight blue">
      In Missouri, nearly <strong>40% of 5-star reviews for nurseries mention “knowledgeable staff.”</strong><br>
      That knowledge directly drives trust, loyalty, and repeat business.
    </div>
    """,
    unsafe_allow_html=True,
)

# -------------------
# Audio Sample Section
# -------------------
st.markdown(
    """
    <section class="section alt">
      <h2>Featured Sample Episode</h2>
      <p><strong>Soil Amendments in Missouri</strong> — how to explain clay, loam, and rocky soils, plus which amendments build trust with customers.</p>
    </section>
    """,
    unsafe_allow_html=True,
)
st.audio("soil_ammendments.mp3", format="audio/mp3")
st.markdown(
    """
    <div class="highlight gray">
      This 5-minute training shows how everyday questions turn into customer confidence. Every episode is <strong>practical, professional, and customer-oriented</strong>.
    </div>
    """,
    unsafe_allow_html=True,
)

# -------------------
# Series Overview
# -------------------
st.markdown(
    """
    <section class="section">
      <h2>The 25-Episode Training Series</h2>
      <p>Each episode is short, focused, and designed to help staff handle real customer scenarios.</p>
      <ul>
        <li>Missouri soil types & amendments</li>
        <li>Choosing trees & shrubs for local climates</li>
        <li>Seasonal care & maintenance tips</li>
        <li>Explaining native vs. exotic plants</li>
        <li>Watering, fertilizing, and pest prevention</li>
        <li>Common customer questions — answered with confidence</li>
        <li>And much more…</li>
      </ul>
      <div class="highlight gray">
        Together, the series builds a foundation of <strong>expert communication</strong> that keeps your staff sharp and customers coming back.
      </div>
    </section>
    """,
    unsafe_allow_html=True,
)

# -------------------
# Lead Capture Form
# -------------------
st.markdown("<section class='section alt'><h2>Get More Information</h2></section>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div style='max-width:800px;margin:auto;'>", unsafe_allow_html=True)
    with st.form("lead_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Work Email")
        nursery = st.text_input("Nursery Name")
        message = st.text_area("What would you like to improve about your staff training?")

        if st.form_submit_button("🚀 Request Info"):
            if not name or not email:
                st.error("Please enter at least your name and email.")
            else:
                sheet.append_row([name, email, nursery, message])
                st.success("✅ Thank you! We’ll be in touch shortly.")
    st.markdown("</div>", unsafe_allow_html=True)

# -------------------
# Footer
# -------------------
st.markdown(
    """
    <footer>
      <small>Made for Missouri nurseries — empowering staff, delighting customers.</small>
    </footer>
    """,
    unsafe_allow_html=True,
)
