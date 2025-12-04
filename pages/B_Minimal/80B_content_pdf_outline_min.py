import streamlit as st, ollama

st.set_page_config(page_title="80 – Content: PDF-Struktur skizzieren", page_icon="📄")

m = st.text_input("Modell", "llama3.2")
t = st.text_area("Dokument-Text oder Auszug", "")
if st.button("Run"):
    p = "Skizziere auf Basis des Textes die grobe Struktur (Kapitel/Abschnitte) des Dokuments." + "\n\nText:\n" + t
    r = ollama.chat(model=m, messages=[{"role": "user", "content": p}])
    st.write(r["message"]["content"])
