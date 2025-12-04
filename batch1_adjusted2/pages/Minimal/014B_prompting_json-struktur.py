import streamlit as st, ollama

st.set_page_config(page_title="014 – Prompting: JSON-Struktur", page_icon="📗")

m = st.text_input("Modell", "llama3.2")
t = st.text_area("Eingabetext / Prompt / Beispiel", "")
if st.button("Run"):
    p = "Wandle die Informationen in eine sinnvolle JSON-Struktur um." + "\n\nText:\n" + t
    r = ollama.chat(model=m, messages=[{"role":"user","content":p}])
    st.write(r["message"]["content"])
