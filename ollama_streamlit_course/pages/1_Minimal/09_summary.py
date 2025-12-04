import streamlit as st, ollama

st.set_page_config(page_title="09B – Zusammenfassung (Minimal)", page_icon="📝")

m = st.text_input("Modell", "llama3.2")
f = st.file_uploader("Datei", type=["txt"])
if f and st.button("Zusammenfassen"):
    t = f.read().decode("utf-8", errors="ignore")
    r = ollama.chat(model=m, messages=[{"role": "user", "content": "Fasse zusammen:\n" + t}])
    st.write(r["message"]["content"])

