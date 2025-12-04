import streamlit as st, ollama

st.set_page_config(page_title="02B – Status (Minimal)", page_icon="🩺")

if st.button("Status"):
    st.write(ollama.list())

