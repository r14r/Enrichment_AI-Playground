import streamlit as st, ollama

st.set_page_config(page_title="35 – CreateContent: E-Mail-Generator", page_icon="📧")

m = st.text_input("Modell", "llama3.2")
c = st.text_area("Kontext", "Bewerbung als Python-Entwickler bei Firma X")
if st.button("E-Mail"):
    p = "Schreibe eine kurze, höfliche E-Mail mit Betreff zu folgendem Kontext:\n" + c
    r = ollama.chat(model=m, messages=[{"role": "user", "content": p}])
    st.write(r["message"]["content"])
