import streamlit as st, ollama

st.set_page_config(page_title="59 – Media: Social-Media-Post aus Audio", page_icon="🎧")

m = st.text_input("Modell", "llama3.2")
t = st.text_area("Audio-Transkript oder Notizen", "")
if st.button("Run"):
    p = "Erzeuge aus dem Transkript einen knackigen Social-Media-Post, der den Inhalt attraktiv zusammenfasst." + "\n\nText:\n" + t
    r = ollama.chat(model=m, messages=[{"role": "user", "content": p}])
    st.write(r["message"]["content"])
