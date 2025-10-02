import streamlit as st
from utils import ensure_session, render_reset_button, render_stats_editor

ensure_session()
st.title("🏟️ Match Generale")

render_reset_button()

render_stats_editor("general", "Match Generale")
