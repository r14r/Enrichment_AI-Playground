import streamlit as st, ollama

st.set_page_config(page_title="016 – Prompting: Chain-of-Thought", page_icon="📗")

m = st.text_input("Modell", "llama3.2")
t = st.text_area("Eingabetext / Prompt / Beispiel", "")
if st.button("Run"):
    p = "Löse die Aufgabe Schritt für Schritt mit Zwischenerklärungen." + "\n\nText:\n" + t
    r = ollama.chat(model=m, messages=[{"role":"user","content":p}])
    st.write(r["message"]["content"])
