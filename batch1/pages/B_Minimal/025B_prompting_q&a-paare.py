import streamlit as st, ollama

st.set_page_config(page_title="025 – Prompting: Q&A-Paare", page_icon="📗")
m = st.text_input("Modell", "llama3.2")
t = st.text_area("Eingabetext / Prompt / Beispiele", "")
if st.button("Run"):
    p = "Erzeuge Frage-Antwort-Paare, die den Inhalt prüfen." + "\n\nText:\n" + t
    r = ollama.chat(model=m, messages=[{"role":"user","content":p}])
    st.write(r["message"]["content"])
