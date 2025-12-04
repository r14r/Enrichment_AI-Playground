import streamlit as st, ollama

st.set_page_config(page_title="36 – CreateContent: Blog & Artikel", page_icon="📰")

m = st.text_input("Modell", "llama3.2")
t = st.text_input("Thema", "Warum lokale KI-Modelle praktisch sind")
if st.button("Blog-Intro"):
    p = "Schreibe eine kurze Einleitung für einen Blogartikel zum Thema: " + t
    r = ollama.chat(model=m, messages=[{"role": "user", "content": p}])
    st.write(r["message"]["content"])
