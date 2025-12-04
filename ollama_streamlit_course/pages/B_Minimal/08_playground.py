import streamlit as st, ollama

st.set_page_config(page_title="08B – Playground (Minimal)", page_icon="🎯")

m = st.text_input("Modell", "llama3.2")
t = st.slider("Temp", 0.0, 1.5, 0.7)
p = st.text_area("Prompt")
if st.button("Run"):
    r = ollama.chat(model=m, messages=[{"role": "user", "content": p}], options={"temperature": t})
    st.write(r["message"]["content"])

