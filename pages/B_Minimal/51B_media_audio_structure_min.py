import streamlit as st, ollama

st.set_page_config(page_title="51 – Media: Struktur aus Audio", page_icon="🎧")

m = st.text_input("Modell", "llama3.2")
t = st.text_area("Audio-Transkript oder Notizen", "")
if st.button("Run"):
    p = "Extrahiere aus dem Transkript die Hauptpunkte und strukturiere sie in einer übersichtlichen Liste." + "\n\nText:\n" + t
    r = ollama.chat(model=m, messages=[{"role": "user", "content": p}])
    st.write(r["message"]["content"])
