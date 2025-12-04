import streamlit as st
import ollama
import json

st.set_page_config(page_title="23 – JSON-Ausgabe", page_icon="🧾")

m = st.text_input("Modell", "llama3.2")
p = st.text_area("Prompt", "Gib mir JSON mit einem Feld 'msg'.")
if st.button("Run"):
    r = ollama.chat(model=m, messages=[{"role": "user", "content": p}])
    st.write(r["message"]["content"])
