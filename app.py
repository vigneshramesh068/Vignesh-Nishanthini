import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(page_title="Vignesh & Nishanthini | Wedding Invitation", page_icon="💍", layout="wide", initial_sidebar_state="collapsed")
st.markdown("""<style>[data-testid="stHeader"],[data-testid="stToolbar"],[data-testid="stDecoration"],footer{display:none!important}.block-container{padding:0!important;max-width:none!important}iframe{border:0!important;display:block}</style>""", unsafe_allow_html=True)
html=Path(__file__).with_name("invitation.html").read_text(encoding="utf-8")
raw="https://raw.githubusercontent.com/vigneshramesh068/Vignesh-Nishanthini/main/img/"
for i in range(1,7): html=html.replace(f"__PHOTO{i}__", raw+f"photo{i}.webp")
components.html(html, height=10000, scrolling=True)
