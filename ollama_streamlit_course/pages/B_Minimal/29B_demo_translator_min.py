import streamlit as st, ollama

st.set_page_config(page_title="29 – Übersetzer", page_icon="🌐")

m = st.text_input("Modell", "llama3.2")
t = st.text_area("Text", "Hello, how are you?")
if st.button("DE"):
    p = "Übersetze ins Deutsche:\n" + t
    r = ollama.chat(model=m, messages=[{"role": "user", "content": p}])
    st.write(r["message"]["content"])
