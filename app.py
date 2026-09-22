import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Vignesh & Nishanthini — Wedding Invitation",
    page_icon="💍",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Make Streamlit itself disappear so the invitation behaves like a normal website.
st.markdown("""
<style>
[data-testid="stHeader"] {display:none !important;}
[data-testid="stToolbar"] {display:none !important;}
[data-testid="stDecoration"] {display:none !important;}
footer {display:none !important;}
.block-container {padding:0 !important; max-width:none !important;}
[data-testid="stAppViewContainer"] {padding:0 !important;}
</style>
""", unsafe_allow_html=True)

html_path = Path(__file__).parent / "invitation.html"

# Use Streamlit's current iframe API. This loads the complete local HTML page
# (including its JavaScript) instead of passing a large HTML string through the
# legacy components.v1.html API.
st.iframe(html_path, height=10000)
