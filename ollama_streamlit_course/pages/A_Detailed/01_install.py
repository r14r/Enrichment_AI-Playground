import streamlit as st
import sys
import importlib
import subprocess

st.set_page_config(page_title="01A – Installationscheck (Ausführlich)", page_icon="✅")
st.title("✅ 01A – Installationscheck (Ausführlich)")

st.header("Python & Streamlit")
st.write(f"Python-Version: `{sys.version}`")

st.header("Ollama Python SDK")
ollama_spec = importlib.util.find_spec("ollama")
if ollama_spec is not None:
    st.success("Python-Paket `ollama` ist installiert.")
else:
    st.error("Python-Paket `ollama` ist NICHT installiert.")

st.header("Ollama CLI")
try:
    result = subprocess.run(
        ["ollama", "--version"],
        capture_output=True,
        text=True,
        check=True,
    )
    st.success("Ollama CLI gefunden.")
    st.write("Version:", result.stdout.strip())
except Exception as e:
    st.error("Konnte `ollama` nicht ausführen.")
    st.exception(e)
