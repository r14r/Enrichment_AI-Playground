import streamlit as st, ollama

st.set_page_config(page_title="84 – Content: Quiz aus PDF-Inhalt", page_icon="📄")

m = st.text_input("Modell", "llama3.2")
t = st.text_area("Dokument-Text oder Auszug", "")
if st.button("Run"):
    p = "Erzeuge ein Quiz mit Antworten basierend auf dem Inhalt." + "\n\nText:\n" + t
    r = ollama.chat(model=m, messages=[{"role": "user", "content": p}])
    st.write(r["message"]["content"])
