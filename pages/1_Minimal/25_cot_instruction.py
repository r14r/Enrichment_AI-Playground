import streamlit as st
import ollama

st.set_page_config(page_title="25 – Denkweise erklären", page_icon="🧠")

m = st.text_input("Modell", "llama3.2")
p = st.text_area("Aufgabe", "Erkläre Schritt für Schritt, wie man eine ToDo-Liste plant.")
if st.button("Run"):
    r = ollama.chat(model=m, messages=[{"role": "user", "content": p}])
    st.write(r["message"]["content"])
