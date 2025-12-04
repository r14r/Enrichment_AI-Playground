import streamlit as st
import ollama

st.set_page_config(page_title="02B – Status (Minimal)", page_icon="🩺")

st.header("Status")
st.write(ollama.list())

