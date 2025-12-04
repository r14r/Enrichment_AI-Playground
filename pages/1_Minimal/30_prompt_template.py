import streamlit as st
import ollama

st.set_page_config(page_title="30 – Prompt-Templates", page_icon="📋")

m = st.text_input("Modell", "llama3.2")
s = st.text_input("Thema", "Streamlit Kurs")
if st.button("Run"):
    p = "Erzeuge 3 Ideen zu: " + s
    r = ollama.chat(model=m, messages=[{"role": "user", "content": p}])
    st.write(r["message"]["content"])
