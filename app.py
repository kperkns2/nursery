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


st.markdown(
    """
    <style>
    /* Remove default top padding/whitespace */
    .block-container {
        padding-top: 1rem;
    }
    
    /* Optionally also remove default header space */
    header[data-testid="stHeader"] {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    /* Hide the Streamlit 'Manage app' button */
    div[data-testid="stStatusWidget"] {display: none;}
    iframe[title="streamlitShareMenu"] {display: none;}
    </style>
    """,
    unsafe_allow_html=True
)



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
        padding: 10rem 1rem 6rem;
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

      .audio-wrapper {
        position: relative;
        display: block;
        margin: 2rem auto;
        max-width: 700px;
        border-radius: 15px;
        padding: 10px;
        background: linear-gradient(270deg, #8bc34a, #c5e1a5, #aed581, #dce775, #c8e6c9, #dcedc8);
        background-size: 1200% 1200%;
        animation: gradientBorder 7s ease infinite;
      }

      audio {
        width: 100%;
        border-radius: 10px;
        display: block;
      }

      @keyframes gradientBorder {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
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
        border-radius: 50px !important;
        padding: 0.8rem 2rem !important;
        font-size: 1.1rem !important;
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
      <p>This 5-minute training shows how everyday questions turn into customer confidence. Every episode is <strong>practical, professional, and customer-oriented</strong>.</p>
      <div class="audio-wrapper">
        <audio controls>
          <source src="https://raw.githubusercontent.com/kperkns2/nursery/main/cedar_ammendments5.mp3" type='audio/mp3'>
          Your browser does not support the audio element.
        </audio>
      </div>
    </section>
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
    </section>
    """,
    unsafe_allow_html=True,
)

# -------------------
# Lead Capture Form
# -------------------
st.markdown(
    """
    <section class='section alt'>
      <h2>Get More Information</h2>
      <p>Fill out the form below to receive up to <strong>5 additional free sample episodes</strong> directly to your inbox.</p>
    </section>
    """,
    unsafe_allow_html=True,
)

with st.form("lead_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Work Email")
    nursery = st.text_input("Nursery Name")
    episodes = st.multiselect(
        "Which episodes are you most interested in? (Select up to 5)",
             [
              "Soil Amendments in Missouri",
              "Drainage Detectives: Fixing Wet & Soggy Spots",
              "pH Plain-Talk: What to Test and What to Tell",
              "Mulch Matters: Types, Thickness & Timing",
              "Compost Confidence: Building Better Garden Soil",
              "Raised Beds & Mixes That Actually Work",
              "Quick Soil Tests for the Sales Floor",
              "Right Tree, Right Place: Matching Trees to Missouri Yards",
              "Small-Space Shade Trees: Big Impact, Low Fuss",
              "Shrubs for Sun & Shade: Clear Customer Scripts",
              "Black Walnut Basics: What Every Customer Should Know",
              "Fruit Tree Fundamentals: Pollination & Pruning 101",
              "Evergreen Selection for Year-Round Appeal",
              "Fast Wins: Shrubs That Establish Quickly",
              "Perennials That Keep Coming Back",
              "Annuals for Maximum Wow",
              "Pollinator Picks: Plants that Attract Bees & Butterflies",
              "Shade Garden Color: Designing Where the Sun Doesn’t Reach",
              "Cut Flower Favorites: Grow to Sell, Sell to Grow",
              "Seasonal Display Planning: Spring to Fall",
              "Low-Maintenance Borders: Beauty Without the Backache",
              "Watering for Results: Frequency, Depth & Timing",
              "Drip & Soaker Basics: When to Recommend",
              "Rain Gardens & Erosion Fixes",
              "Drought Response: Quick Advice When the Heat Hits",
              "Soggy Lawn? Alternatives & Fixes",
              "Insect ID in 60 Seconds: Friend vs Foe",
              "Fungal Flags: Spotting & Stopping Common Diseases",
              "IPM for the Sales Floor: Integrated Pest Management Made Simple",
              "Deer & Rabbit Defense: Practical Deterrents",
              "Diagnosing Yellow Leaves: Fast Troubleshooting",
              "Safe Product Conversations: What to Recommend & When",
              "Why Natives Win: Selling the Show-Me State Story",
              "Missouri Prairie Picks: Grasses & Meadow Plants",
              "Native Trees with Big Payoffs",
              "Backyard Habitat: Small Steps for Big Wildlife Benefits",
              "Controlling Invasives: What Homeowners Should Know",
              "Spring Prep: Getting Your Yard Ready to Grow",
              "Summer Watch: Heat, Water & Pest Signals",
              "Fall Tasks That Save Next Year’s Work",
              "Winter Care & Salt-Safe Plants",
              "Turn Questions into Sales: Friendly Scripts That Work",
              "Listening to Reviews: Train from Customer Feedback",
              "Handling Returns & Tough Conversations",
              "Merchandise That Sells: Plant Pairings & Display Tips",
              "Value Bundles: Packages that Customers Actually Buy",
              "Quick Product Demos: Teach Staff to Demo with Confidence",
              "Container Combinations that Convert",
              "Houseplant Rescue: Common Issues & Fast Fixes",
              "Pollinator Pots & Small-Space Edibles"
            ]

    )
    message = st.text_area("What would you like to improve about your staff training?")

    submit = st.form_submit_button("🌿 Request Free Samples")
    if submit:
        if not name or not email or '@' not in email:
            st.error("Please enter at least your name and email.")
        else:
            sheet.append_row([name, email, nursery, ", ".join(episodes), message])
            st.success("✅ Thank you! We’ll send your free episodes shortly.")

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
