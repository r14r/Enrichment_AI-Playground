import streamlit as st, ollama

st.set_page_config(page_title="57 – Media: Schlüsselbegriffe", page_icon="🎧")

m = st.text_input("Modell", "llama3.2")
t = st.text_area("Audio-Transkript oder Notizen", "")
if st.button("Run"):
    p = "Extrahiere die wichtigsten Schlüsselbegriffe und Konzepte aus dem Transkript." + "\n\nText:\n" + t
    r = ollama.chat(model=m, messages=[{"role": "user", "content": p}])
    st.write(r["message"]["content"])
