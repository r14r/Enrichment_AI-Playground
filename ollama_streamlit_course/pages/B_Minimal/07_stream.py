import streamlit as st, ollama

st.set_page_config(page_title="07B – Streaming (Minimal)", page_icon="📡")

m = st.text_input("Modell", "llama3.2")
p = st.text_area("Prompt")
if st.button("Stream"):
    t = ""
    ph = st.empty()
    for c in ollama.chat(model=m, messages=[{"role": "user", "content": p}], stream=True):
        t += c["message"]["content"]
        ph.write(t)

