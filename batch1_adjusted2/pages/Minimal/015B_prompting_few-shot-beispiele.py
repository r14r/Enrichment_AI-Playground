import streamlit as st, ollama

st.set_page_config(page_title="015 – Prompting: Few-Shot-Beispiele", page_icon="📗")

m = st.text_input("Modell", "llama3.2")
t = st.text_area("Eingabetext / Prompt / Beispiel", "")
if st.button("Run"):
    p = "Erkenne Muster in Beispielen und setze sie konsistent fort." + "\n\nText:\n" + t
    r = ollama.chat(model=m, messages=[{"role":"user","content":p}])
    st.write(r["message"]["content"])
