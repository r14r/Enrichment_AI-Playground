import streamlit as st, ollama

st.set_page_config(page_title="61 – Media: Szenenübersicht", page_icon="🎥")

m = st.text_input("Modell", "llama3.2")
t = st.text_area("Video-Transkript oder Beschreibung", "")
if st.button("Run"):
    p = "Erstelle aus dem Transkript eine Liste von Szenen oder Abschnitten mit kurzen Beschreibungen." + "\n\nText:\n" + t
    r = ollama.chat(model=m, messages=[{"role": "user", "content": p}])
    st.write(r["message"]["content"])
