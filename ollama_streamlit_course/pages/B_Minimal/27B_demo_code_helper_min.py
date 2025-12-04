import streamlit as st, ollama

st.set_page_config(page_title="27 – Code-Helfer", page_icon="💻")

m = st.text_input("Modell", "llama3.2")
c = st.text_area("Code", "print('Hello')")
if st.button("Explain"):
    r = ollama.chat(model=m, messages=[{"role": "user", "content": "Erkläre diesen Code:\n" + c}])
    st.write(r["message"]["content"])
