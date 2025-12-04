import streamlit as st, ollama

st.set_page_config(page_title="05B – Prompt (Minimal)", page_icon="💬")

m = st.text_input("Modell", "llama3.2")
p = st.text_area("Prompt")
if st.button("Go"):
    r = ollama.chat(model=m, messages=[{"role": "user", "content": p}])
    st.write(r["message"]["content"])

