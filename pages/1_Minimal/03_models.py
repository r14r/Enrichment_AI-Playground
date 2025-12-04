import streamlit as st
import ollama

st.set_page_config(page_title="03B – Modelle anzeigen (Minimal)", page_icon="📦")

st.header("Modelle")
st.write(ollama.list())

