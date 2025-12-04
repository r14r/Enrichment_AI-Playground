import streamlit as st, ollama

st.set_page_config(page_title="62 – Media: Kapitel & Timestamps", page_icon="🎥")

m = st.text_input("Modell", "llama3.2")
t = st.text_area("Video-Transkript oder Beschreibung", "")
if st.button("Run"):
    p = "Schlage sinnvolle Kapitelüberschriften vor und gib geschätzte Positionen im Video (z. B. Anfang/Mitte/Ende) an." + "\n\nText:\n" + t
    r = ollama.chat(model=m, messages=[{"role": "user", "content": p}])
    st.write(r["message"]["content"])
