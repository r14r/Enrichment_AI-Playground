import streamlit as st, ollama

st.set_page_config(page_title="004 – Basics: Modell herunterladen", page_icon="📗")

m = st.text_input("Modell", "llama3.2")
t = st.text_area("Eingabe / Notizen / Beschreibung", "")
if st.button("Run"):
    p = "Beschreibe Schritt für Schritt, wie du ein neues Modell mit `ollama pull` installierst." + "\n\nText:\n" + t
    r = ollama.chat(model=m, messages=[{"role":"user","content":p}])
    st.write(r["message"]["content"])
