import streamlit as st
import sys
import importlib
import subprocess

st.set_page_config(page_title="01B – Installationscheck (Minimal)", page_icon="✅")

st.write(sys.version)
st.write(importlib.util.find_spec("ollama") is not None)
st.write(subprocess.run(["ollama", "version"], capture_output=True, text=True).stdout)

