import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# -------------------
# Page Config
# -------------------
st.set_page_config(
    page_title="Nursery Training Audio Series",
    page_icon="🌱",
    layout="wide"
)

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
        font-family: 'Poppins', sans-serif;
        color: #2d2d2d;
        background-color: #fdfdfd;
      }

      header {
        background: linear-gradient(rgba(0, 70, 40, 0.8), rgba(0, 70, 40, 0.8)),
        url('https://images.unsplash.com/photo-1501004318641-b39e6451bec6?auto=format&fit=crop&w=1600&q=80') no-repeat center center/cover;
        color: white;
        text-align: center;
        padding: 8rem 1rem 6rem;
      }

      header h1 {
        font-size: 3rem;
        font-weight: 700;
        margin: 0;
      }

      header p {
        font-size: 1.3rem;
        margin-top: 1rem;
      }

      .section {
        max-width: 1200px;
        margin: auto;
        padding: 3rem 2rem;
      }

      .section.alt {
        background-color: #f9f9f9;
      }

      .highlight.blue {
        background: linear-gradient(135deg, #e8f4fa, #cfe6f3);
        color: #004f71;
        padding: 2rem;
        border-radius: 14px;
        text-align: center;
        font-size: 1.3rem;
        font-weight: 600;
        margin: 2.5rem auto;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        max-width: 1100px;
      }

      .highlight.gray {
        background: #f2f2f2;
        color: #333;
        padding: 1.8rem;
        border-radius: 12px;
        text-align: center;
        font-size: 1.1rem;
        margin: 2rem auto;
        max-width: 1050px;
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
        max-width: 700px;
        border-radius: 10px;
        box-shadow: 0 3px 8px rgba(0,0,0,0.1);
      }

      .form-container {
        max-width: 1000px;
        margin: auto;
        background: #fff;
        padding: 2.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
      }

      .submit-btn button {
        background-color: #006644 !important;
        color: white !important;
        font-weight: 600 !important;
        border-radius: 8px !important;
        padding: 0.6rem 1.2rem !important;
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
      <p>This 5-minute training shows how everyday questions turn into customer confidence. Every episode is <strong>practical, professional, and customer-oriented</strong>. </p>
    </section>
    """,
    unsafe_allow_html=True,
)
col1, col2, col3 = st.columns([1,1,1])
col2.audio("soil_ammendments.mp3", format="audio/mp3")

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
st.markdown("<section class='section alt'><h2>Get More Information</h2><p>Fill out the form below to receive up to <strong>5 additional free sample episodes</strong> directly to your inbox.</p></section>", unsafe_allow_html=True)

with st.form("lead_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Work Email")
    nursery = st.text_input("Nursery Name")
    episodes = st.multiselect(
        "Which episodes are you most interested in? (Select up to 5)",
        [
            "Soil Amendments in Missouri",
            "Trees & Shrubs for Local Climates",
            "Seasonal Care & Maintenance",
            "Native vs. Exotic Plants",
            "Watering & Fertilizing Basics",
            "Pest Prevention Techniques",
            "Handling Common Customer Questions"
        ]
    )
    message = st.text_area("What would you like to improve about your staff training?")

    submit = st.form_submit_button("🌿 Request Free Samples", help="Submit to receive sample episodes")
    if submit:
        if not name or not email:
            st.error("Please enter at least your name and email.")
        else:
            sheet.append_row([name, email, nursery, ", ".join(episodes), message])
            st.success("✅ Thank you! We’ll send your free episodes shortly.")

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
