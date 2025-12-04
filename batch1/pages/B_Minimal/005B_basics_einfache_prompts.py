import streamlit as st, ollama

st.set_page_config(page_title="005 – Basics: Einfache Prompts", page_icon="✅")

m = st.text_input("Modell", "llama3.2")
p = st.text_area("Eingabe", "")
if st.button("Run"):
    r = ollama.chat(model=m, messages=[{"role":"user","content":p}])
    st.write(r["message"]["content"])
