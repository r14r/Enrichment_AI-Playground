import streamlit as st, ollama

st.set_page_config(page_title="28 – Fehler-Erklärer", page_icon="⚠️")

m = st.text_input("Modell", "llama3.2")
e = st.text_area("Fehler", "ModuleNotFoundError: No module named 'pandas'")
if st.button("Explain"):
    r = ollama.chat(model=m, messages=[{"role": "user", "content": "Erkläre diesen Fehler:\n" + e}])
    st.write(r["message"]["content"])
