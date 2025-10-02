import streamlit as st
import pandas as pd
from utils import ensure_session, render_reset_button, verdict_engine, STAT_KEYS, get_block

ensure_session()
st.title("🧠 Analisi & Verdetti (Auto)")

render_reset_button()

def merge_blocks(keys):
    A = {k: None for k in STAT_KEYS}
    B = {k: None for k in STAT_KEYS}
    cA = {k:0 for k in STAT_KEYS}
    cB = {k:0 for k in STAT_KEYS}
    for sec in keys:
        blk = get_block(sec)
        for k in STAT_KEYS:
            va, vb = blk["A"][k], blk["B"][k]
            if isinstance(va, int): A[k] = (0 if A[k] is None else A[k]) + va; cA[k]+=1
            if isinstance(vb, int): B[k] = (0 if B[k] is None else B[k]) + vb; cB[k]+=1
    for k in STAT_KEYS:
        if cA[k]>0: A[k]//=cA[k]
        if cB[k]>0: B[k]//=cB[k]
    return A, B

available = []
for sec in ["general","set1","set2","set3","set4","set5"]:
    blk = get_block(sec)
    if any(isinstance(blk["A"][k], int) or isinstance(blk["B"][k], int) for k in STAT_KEYS):
        available.append(sec)

if not available:
    st.warning("Inserisci almeno un blocco (Match Generale o Set).")
    st.stop()

A, B = merge_blocks(available)
res = verdict_engine(A, B, st.session_state.context)

st.subheader("🧾 Dati usati")
st.write("Blocchi considerati:", ", ".join(available))
df = pd.DataFrame({"A": A, "B": B})
st.dataframe(df.style.format("{:.0f}%"), use_container_width=True)

st.markdown("---")
st.subheader("🏁 Verdettone")
if res["winner"] == "Equilibrio":
    st.info("Match/Set in equilibrio. Aggiorna i blocchi o attendi segnali.")
else:
    st.success(f"Favorito: **{res['winner']}** · Confidenza ~ **{res['confidence']}%**")
if res["notes"]:
    st.markdown("**Chiavi di lettura:**")
    for n in res["notes"]:
        st.markdown(f"- {n}")
