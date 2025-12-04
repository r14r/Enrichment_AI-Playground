import streamlit as st, ollama

st.set_page_config(page_title="010 – Basics: Mini-Dashboard", page_icon="📗")

m = st.text_input("Modell", "llama3.2")
t = st.text_area("Eingabe / Notizen / Beschreibung", "")
if st.button("Run"):
    p = "Skizziere ein kleines Dashboard, das Status und Schnell-Prompt kombiniert." + "\n\nText:\n" + t
    r = ollama.chat(model=m, messages=[{"role":"user","content":p}])
    st.write(r["message"]["content"])
