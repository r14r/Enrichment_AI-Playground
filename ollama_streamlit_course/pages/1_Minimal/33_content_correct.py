import streamlit as st, ollama

st.set_page_config(page_title="33 – Content: Text korrigieren", page_icon="✏️")

m = st.text_input("Modell", "llama3.2")
t = st.text_area("Text", "das ist ein kurzer text der einige fehler hat")
if st.button("Korrigieren"):
    p = "Korrigiere Rechtschreibung und Grammatik. Gib nur den korrigierten Text aus.\n\n" + t
    r = ollama.chat(model=m, messages=[{"role": "user", "content": p}])
    st.write(r["message"]["content"])
