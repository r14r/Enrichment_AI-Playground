import streamlit as st, ollama

st.set_page_config(page_title="04B – Modell herunterladen (Minimal)", page_icon="⬇️")

model = st.text_input("Modell", "llama3.2")
if st.button("Pull"):
    for _ in ollama.pull(model, stream=True):
        pass
    st.write("fertig")

