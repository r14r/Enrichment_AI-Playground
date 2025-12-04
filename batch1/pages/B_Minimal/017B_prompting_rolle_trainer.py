import streamlit as st, ollama

st.set_page_config(page_title="017 – Prompting: Rolle Trainer", page_icon="📗")
m = st.text_input("Modell", "llama3.2")
t = st.text_area("Eingabetext / Prompt / Beispiele", "")
if st.button("Run"):
    p = "Erkläre das Thema für Anfänger in einem Kurs." + "\n\nText:\n" + t
    r = ollama.chat(model=m, messages=[{"role":"user","content":p}])
    st.write(r["message"]["content"])
