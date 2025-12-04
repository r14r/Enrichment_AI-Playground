import streamlit as st, ollama

st.set_page_config(page_title="56 – Media: Action Items", page_icon="🎧")

m = st.text_input("Modell", "llama3.2")
t = st.text_area("Audio-Transkript oder Notizen", "")
if st.button("Run"):
    p = "Liste alle konkreten Aufgaben und Action Items auf, die sich aus dem Transkript ergeben." + "\n\nText:\n" + t
    r = ollama.chat(model=m, messages=[{"role": "user", "content": p}])
    st.write(r["message"]["content"])
