import streamlit as st, ollama

st.set_page_config(page_title="55 – Media: Kapitel aus Audio", page_icon="🎧")

m = st.text_input("Modell", "llama3.2")
t = st.text_area("Audio-Transkript oder Notizen", "")
if st.button("Run"):
    p = "Teile den Inhalt in sinnvolle Kapitel oder Abschnitte ein und gib jedem einen kurzen Titel." + "\n\nText:\n" + t
    r = ollama.chat(model=m, messages=[{"role": "user", "content": p}])
    st.write(r["message"]["content"])
