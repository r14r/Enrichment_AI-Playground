import streamlit as st
import ollama
import base64

st.set_page_config(page_title="31 – Media: Bildanalyse", page_icon="🖼️")

m = st.text_input("Modell", "llama3.2-vision")
q = st.text_input("Frage", "Was ist auf diesem Bild?")
f = st.file_uploader("Bild", type=["png", "jpg", "jpeg", "webp"])
if f and st.button("Analyse"):
    b = base64.b64encode(f.read()).decode("utf-8")
    r = ollama.chat(model=m, messages=[{"role": "user", "content": q, "images": [b]}])
    st.write(r["message"]["content"])
