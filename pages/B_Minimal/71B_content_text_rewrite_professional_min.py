import streamlit as st, ollama

st.set_page_config(page_title="71 – Content: Text professionalisieren", page_icon="✍️")

m = st.text_input("Modell", "llama3.2")
t = st.text_area("Eingabetext", "")
if st.button("Run"):
    p = "Formuliere den folgenden Text professioneller, ohne den Inhalt zu verändern." + "\n\nText:\n" + t
    r = ollama.chat(model=m, messages=[{"role": "user", "content": p}])
    st.write(r["message"]["content"])
