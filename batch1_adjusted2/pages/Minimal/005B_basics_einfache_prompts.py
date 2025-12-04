import streamlit as st, ollama

st.set_page_config(page_title="005 – Basics: Einfache Prompts", page_icon="📗")

m = st.text_input("Modell", "llama3.2")
t = st.text_area("Eingabe / Notizen / Beschreibung", "")
if st.button("Run"):
    p = "Formuliere einen einfachen Prompt und erkläre, warum er verständlich ist." + "\n\nText:\n" + t
    r = ollama.chat(model=m, messages=[{"role":"user","content":p}])
    st.write(r["message"]["content"])
