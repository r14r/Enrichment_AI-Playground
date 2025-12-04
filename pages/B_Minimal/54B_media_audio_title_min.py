import streamlit as st, ollama

st.set_page_config(page_title="54 – Media: Audio-Titel", page_icon="🎧")

m = st.text_input("Modell", "llama3.2")
t = st.text_area("Audio-Transkript oder Notizen", "")
if st.button("Run"):
    p = "Schlage auf Basis des Transkripts mehrere aussagekräftige Titel für die Audioaufnahme vor." + "\n\nText:\n" + t
    r = ollama.chat(model=m, messages=[{"role": "user", "content": p}])
    st.write(r["message"]["content"])
