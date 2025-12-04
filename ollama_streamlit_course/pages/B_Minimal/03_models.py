import streamlit as st, ollama

st.set_page_config(page_title="03B – Modelle anzeigen (Minimal)", page_icon="📦")

if st.button("Modelle"):
    st.write(ollama.list())

