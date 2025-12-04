import streamlit as st, ollama

st.set_page_config(page_title="64 – Media: Titel & Beschreibung", page_icon="🎥")

m = st.text_input("Modell", "llama3.2")
t = st.text_area("Video-Transkript oder Beschreibung", "")
if st.button("Run"):
    p = "Schlage einen YouTube-Titel und eine passende Beschreibung für das Video vor." + "\n\nText:\n" + t
    r = ollama.chat(model=m, messages=[{"role": "user", "content": p}])
    st.write(r["message"]["content"])
