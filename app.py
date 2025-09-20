import streamlit as st

st.set_page_config(
    page_title="Nursery Training Audio Series",
    page_icon="🌱",
    layout="wide"
)

# Full HTML Template
html_code = """
<style>
/* Reset spacing for Streamlit */
.main .block-container {
    padding-top: 0rem;
    padding-bottom: 0rem;
    padding-left: 0rem;
    padding-right: 0rem;
    max-width: 100% !important;
}

body {
    margin: 0;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

/* Banner */
.banner {
    background: linear-gradient(135deg, #2d6a4f, #95d5b2);
    color: white;
    text-align: center;
    padding: 4rem 2rem;
}
.banner h1 {
    font-size: 2.5rem;
    margin-bottom: 0.5rem;
}
.banner p {
    font-size: 1.2rem;
}

/* Section styling */
.section {
    padding: 3rem 2rem;
    max-width: 1000px;
    margin: auto;
}
.section h2 {
    font-size: 1.8rem;
    margin-bottom: 1rem;
    color: #004F71;
}

/* Highlight blocks */
.highlight-blue {
    background-color: #E8F4FA;
    color: #004F71;
    padding: 1.5rem;
    border-radius: 12px;
    text-align: center;
    font-size: 1.2rem;
    font-weight: 600;
    margin: 2rem 0;
}
.highlight-gray {
    background-color: #f5f5f5;
    color: #333;
    padding: 1.5rem;
    border-radius: 12px;
    margin: 2rem 0;
}

/* Audio demo */
.audio-demo {
    margin-top: 1rem;
}

/* Footer */
footer {
    background-color: #f9f9f9;
    text-align: center;
    padding: 1.5rem;
    font-size: 0.9rem;
    color: #666;
    margin-top: 3rem;
}
</style>

<div class="banner">
    <h1>Grow Knowledge. Grow Sales.</h1>
    <p>Audio Training for Nursery Staff & Customers</p>
</div>

<div class="section">
    <p>
        When customers walk into your nursery, they’re not just buying plants — they’re buying <b>expertise</b>.
    </p>
    <p>
        Our short, practical audio series equips your staff with the right words, so they can confidently guide every customer decision.
    </p>
</div>

<div class="section">
    <div class="highlight-blue">
        In Missouri, nearly <b>40% of 5-star reviews for nurseries mention “knowledgeable staff.”</b><br>
        That knowledge directly drives trust, loyalty, and repeat business.
    </div>
</div>

<div class="section">
    <h2>Featured Sample Episode</h2>
    <p><b>Soil Amendments in Missouri</b> — how to explain clay, loam, and rocky soils, plus which amendments build trust with customers.</p>
    <div class="audio-demo">
        <audio controls>
            <source src="soil_ammendments.mp3" type="audio/mp3">
            Your browser does not support the audio element.
        </audio>
    </div>
    <p>👉 This 5-minute training shows how everyday questions turn into customer confidence. Every episode is <b>practical, professional, and customer-oriented</b>.</p>
</div>

<div class="section">
    <h2>The 25-Episode Training Series</h2>
    <p>
        Each episode is short, focused, and designed to help staff handle real customer scenarios.
    </p>
    <ul>
        <li>Missouri soil types & amendments</li>
        <li>Choosing trees & shrubs for local climates</li>
        <li>Seasonal care & maintenance tips</li>
        <li>Explaining native vs. exotic plants</li>
        <li>Watering, fertilizing, and pest prevention</li>
        <li>Common customer questions — answered with confidence</li>
    </ul>
    <p>
        Together, the series builds a foundation of <b>expert communication</b> that keeps your staff sharp and customers coming back.
    </p>
</div>

<footer>
    Made for Missouri nurseries — empowering staff, delighting customers.
</footer>
"""

st.components.v1.html(html_code, height=2000, scrolling=True)
