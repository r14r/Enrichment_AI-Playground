import streamlit as st, ollama

st.set_page_config(page_title="20 – Demo Quick-Chat", page_icon="💡")

m = st.text_input("Modell", "llama3.2")
u = st.text_input("Frage", "Sag Hallo in einem Satz.")
if st.button("Go"):
    r = ollama.chat(model=m, messages=[{"role": "user", "content": u}])
    st.write(r["message"]["content"])
