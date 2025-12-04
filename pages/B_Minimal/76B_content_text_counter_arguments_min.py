import streamlit as st, ollama

st.set_page_config(page_title="76 – Content: Gegenargumente erzeugen", page_icon="✍️")

m = st.text_input("Modell", "llama3.2")
t = st.text_area("Eingabetext", "")
if st.button("Run"):
    p = "Formuliere passende Gegenargumente zu den Aussagen im Text." + "\n\nText:\n" + t
    r = ollama.chat(model=m, messages=[{"role": "user", "content": p}])
    st.write(r["message"]["content"])
