import streamlit as st, ollama

st.set_page_config(page_title="72 – Content: Social-Media-Varianten", page_icon="✍️")

m = st.text_input("Modell", "llama3.2")
t = st.text_area("Eingabetext", "")
if st.button("Run"):
    p = "Erzeuge mehrere Social-Media-Varianten (Tweet, LinkedIn-Post, Instagram-Caption) aus dem Text." + "\n\nText:\n" + t
    r = ollama.chat(model=m, messages=[{"role": "user", "content": p}])
    st.write(r["message"]["content"])
