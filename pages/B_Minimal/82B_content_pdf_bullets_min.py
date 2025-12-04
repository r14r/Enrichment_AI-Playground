import streamlit as st, ollama

st.set_page_config(page_title="82 – Content: PDF → Bullet Points", page_icon="📄")

m = st.text_input("Modell", "llama3.2")
t = st.text_area("Dokument-Text oder Auszug", "")
if st.button("Run"):
    p = "Erstelle stichpunktartige Zusammenfassungen der wichtigsten Inhalte." + "\n\nText:\n" + t
    r = ollama.chat(model=m, messages=[{"role": "user", "content": p}])
    st.write(r["message"]["content"])
