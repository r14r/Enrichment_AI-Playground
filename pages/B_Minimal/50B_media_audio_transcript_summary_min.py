import streamlit as st, ollama

st.set_page_config(page_title="50 – Media: Audio-Zusammenfassung", page_icon="🎧")

m = st.text_input("Modell", "llama3.2")
t = st.text_area("Audio-Transkript oder Notizen", "")
if st.button("Run"):
    p = "Fasse den folgenden Transkript-Text des Audios prägnant zusammen." + "\n\nText:\n" + t
    r = ollama.chat(model=m, messages=[{"role": "user", "content": p}])
    st.write(r["message"]["content"])
