import streamlit as st, ollama

st.set_page_config(page_title="22 – System-Prompt Stile", page_icon="🧩")

m = st.text_input("Modell", "llama3.2")
u = st.text_input("Frage", "Erkläre kurz, was ein Prompt ist.")
if st.button("Run"):
    r = ollama.chat(model=m, messages=[
        {"role": "system", "content": "Du bist ein freundlicher Lehrer."},
        {"role": "user", "content": u},
    ])
    st.write(r["message"]["content"])
