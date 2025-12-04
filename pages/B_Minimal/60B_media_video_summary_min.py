import streamlit as st, ollama

st.set_page_config(page_title="60 – Media: Video-Zusammenfassung", page_icon="🎥")

m = st.text_input("Modell", "llama3.2")
t = st.text_area("Video-Transkript oder Beschreibung", "")
if st.button("Run"):
    p = "Fasse die Video-Inhalte (basierend auf dem Transkript oder einer Beschreibung) in wenigen Sätzen zusammen." + "\n\nText:\n" + t
    r = ollama.chat(model=m, messages=[{"role": "user", "content": p}])
    st.write(r["message"]["content"])
