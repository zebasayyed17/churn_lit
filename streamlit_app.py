from pathlib import Path

import streamlit as st


APP_DIR = Path(__file__).resolve().parent
HTML_FILE = APP_DIR / "customer_churn_prediction.html"

st.set_page_config(
    page_title="CHURN//LAB · Customer Retention Console",
    page_icon="C",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# The visible frame belongs to Streamlit, not the HTML application.
# Remove its border and the extra element spacing so the cream Xscel-style
# surface sits directly on the Streamlit page.
st.markdown(
    """
    <style>
    /* Remove the host iframe border */
    div[data-testid="stIFrame"],
    div[data-testid="stIFrame"] iframe,
    iframe[title="st.iframe"] {
        border: 0 !important;
        outline: 0 !important;
        box-shadow: none !important;
    }

    /* Remove Streamlit spacing around the iframe */
    div[data-testid="stIFrame"] {
        margin: 0 !important;
        padding: 0 !important;
    }

    /* Keep the main Streamlit canvas clean */
    section.main > div.block-container {
        padding-top: 0.75rem;
        padding-bottom: 0 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

if not HTML_FILE.exists():
    st.error("customer_churn_prediction.html is missing from the app package.")
    st.stop()

# Streamlit 1.56+ supports local HTML files directly through st.iframe.
# JavaScript in the local HTML continues to run inside the iframe.
st.iframe(
    HTML_FILE,
    height=1280,
    width="stretch",
)
