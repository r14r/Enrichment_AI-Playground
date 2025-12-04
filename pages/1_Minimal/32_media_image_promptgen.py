import streamlit as st, ollama

st.set_page_config(page_title="32 – Media: Bild-Prompt-Generator", page_icon="🎨")

m = st.text_input("Modell", "llama3.2")
i = st.text_input("Idee", "Futuristische Stadt bei Nacht")
if st.button("Prompt"):
    p = f"Erzeuge einen kompakten Prompt für ein Text-zu-Bild-Modell zu: {i}"
    r = ollama.chat(model=m, messages=[{"role": "user", "content": p}])
    st.code(r["message"]["content"], language="text")
