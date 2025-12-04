import streamlit as st, ollama

st.set_page_config(page_title="74 – Content: Text erweitern", page_icon="✍️")

m = st.text_input("Modell", "llama3.2")
t = st.text_area("Eingabetext", "")
if st.button("Run"):
    p = "Erweitere den Text, verdopple ungefähr die Länge und füge passende Details hinzu." + "\n\nText:\n" + t
    r = ollama.chat(model=m, messages=[{"role": "user", "content": p}])
    st.write(r["message"]["content"])
