import streamlit as st
from utils import ensure_session, render_reset_button

ensure_session()
st.title("🥎 Contesto Live")

render_reset_button()

ctx = st.session_state.context
ctx["playerA"]    = st.text_input("Nome Giocatore A", value=ctx.get("playerA",""))
ctx["playerB"]    = st.text_input("Nome Giocatore B", value=ctx.get("playerB",""))
ctx["format"]     = st.selectbox("Formato", ["BO3","BO5"], index=0 if ctx.get("format","BO3")=="BO3" else 1)
ctx["set_focus"]  = st.number_input("Set in focus (1–5)", 1, 5, value=int(ctx.get("set_focus",1)), step=1)
ctx["score_sets"] = st.text_input("Score set (es. 7-6, 2-2)", value=ctx.get("score_sets",""))
ctx["game_score"] = st.text_input("Game corrente (es. 40-30)", value=ctx.get("game_score",""))
ctx["server"]     = st.selectbox("Chi serve ora?", ["A","B"], index=0 if ctx.get("server","A")=="A" else 1)

st.success("Contesto aggiornato ✅")
