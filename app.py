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

# Section helper for alternating backgrounds
def section(content, bg="#FFFFFF"):
    st.markdown(
        f"""
        <div style="background-color:{bg}; padding:2rem; border-radius:10px; margin-bottom:1.5rem;">
            {content}
        </div>
        """,
        unsafe_allow_html=True,
    )

# -------------------
# Header
# -------------------
st.title("🌱 Nursery Knowledge Training")
st.subheader("Turn Plant Enthusiasts Into Confident, Trusted Advisors")

section("""
When customers walk into your nursery, they’re not just buying plants —  
they’re buying **expertise**.  

In Missouri, nearly **40% of 5-star reviews for local nurseries mention “knowledgeable staff.”**  
That trust directly drives repeat business and higher sales.
""", bg="#f9f9f9")

# -------------------
# Audio Sample
# -------------------
audio_html = """
<h3>🎧 Sample Training Episode</h3>
<p><b>Soil Amendments in Missouri</b> (5 minutes)</p>
"""
st.markdown(audio_html, unsafe_allow_html=True)

audio_file = open("soil_ammendments.mp3", "rb")
st.audio(audio_file.read(), format="audio/mp3")

section("""
This short episode helps staff explain the differences between **clay, loam, and rocky soils**,  
and how to recommend the **right amendments** with confidence.  

✅ **Focused** on the questions real customers ask  
✅ **Actionable** with clear talking points staff can use right away  
✅ **Designed** to build trust, upsell naturally, and create loyal customers  
""", bg="#eef6f0")

# -------------------
# Benefits
# -------------------
section("""
### 🌟 Why Nurseries Love This Training

- **Boost Reviews & Reputation** — Customers value knowledgeable staff more than price.  
- **Train Efficiently** — 5-minute episodes fit into daily routines.  
- **Increase Sales** — Confident recommendations lead to more purchases.  
- **Build Loyalty** — Staff sound like experts, customers keep coming back.  
""", bg="#f9f9f9")

# -------------------
# Series Overview
# -------------------
with st.expander("📚 Full Training Series Overview (25 Episodes)"):
    st.markdown("""
    Each episode is **5 minutes or less** and covers **real-world customer conversations**:

    1. Greeting customers & making a great first impression  
    2. Missouri soil types & simple amendment tips  
    3. Choosing the right mulch for different plants  
    4. Explaining fertilizer basics (NPK made simple)  
    5. Watering: how much is too much?  
    6. Shade vs. sun plants: helping customers choose  
    7. How to recommend native plants customers will love  
    8. Annuals vs. perennials: easy explanations  
    9. Handling “why is my plant dying?” conversations  
    10. Container gardening basics  
    11. Seasonal color recommendations customers appreciate  
    12. Pollinator-friendly plants (bees, butterflies, birds)  
    13. Explaining drought-tolerant plants  
    14. Low-maintenance landscaping ideas  
    15. Trees for Missouri yards (small, medium, large)  
    16. Shrubs for privacy, beauty, and low care  
    17. Explaining fruit trees & edible landscaping  
    18. Helping customers pick houseplants  
    19. How to guide beginners without overwhelming them  
    20. Upselling: soil, pots, and fertilizers naturally  
    21. Seasonal sales tips: spring, summer, fall, winter  
    22. Spotting and solving common pest problems  
    23. Lawn basics: cool season grasses in Missouri  
    24. Handling complaints with confidence  
    25. Leaving a lasting impression: turning first-time buyers into regulars  
    """)
    st.info("Each episode is crafted to **train staff in real customer interactions** — not theory, just practical knowledge.")

# -------------------
# Connect to Google Sheets
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
# Lead Form CTA
# -------------------
section("""
## 📋 Bring Expert Training to Your Nursery

**Ready to grow staff knowledge and customer trust?**  
Fill out the form below to get pricing, customization options,  
and examples of how Missouri nurseries are already benefiting.
""", bg="#eef6f0")

with st.form("lead_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Work Email")
    nursery_name = st.text_input("Nursery Name")
    message = st.text_area("What would you most like to improve about staff training?")

    submitted = st.form_submit_button("📨 Request Info")
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
