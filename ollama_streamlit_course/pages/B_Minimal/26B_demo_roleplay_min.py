import streamlit as st, ollama

st.set_page_config(page_title="26 – Rollen & Personas", page_icon="🎭")

m = st.text_input("Modell", "llama3.2")
u = st.text_input("Frage", "Gib mir einen Lern-Tipp.")
if st.button("Run"):
    r = ollama.chat(model=m, messages=[
        {"role": "system", "content": "Du bist ein freundlicher Python-Trainer."},
        {"role": "user", "content": u},
    ])
    st.write(r["message"]["content"])
