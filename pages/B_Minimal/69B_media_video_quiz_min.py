import streamlit as st, ollama

st.set_page_config(page_title="69 – Media: Quiz aus Video", page_icon="🎥")

m = st.text_input("Modell", "llama3.2")
t = st.text_area("Video-Transkript oder Beschreibung", "")
if st.button("Run"):
    p = "Erzeuge ein kurzes Quiz (Fragen & Antworten) basierend auf dem beschriebenen Videoinhalt." + "\n\nText:\n" + t
    r = ollama.chat(model=m, messages=[{"role": "user", "content": p}])
    st.write(r["message"]["content"])
