import streamlit as st
from utils import ensure_session, render_reset_button, render_stats_editor

ensure_session()
st.title("🟠 Set 2")

render_reset_button()

render_stats_editor("set2", "Set 2")
