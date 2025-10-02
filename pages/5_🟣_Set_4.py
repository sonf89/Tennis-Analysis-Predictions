import streamlit as st
from utils import ensure_session, render_reset_button, render_stats_editor

ensure_session()
st.title("🟣 Set 4")

render_reset_button()

render_stats_editor("set4", "Set 4")
