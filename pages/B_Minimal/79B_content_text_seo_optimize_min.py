import streamlit as st, ollama

st.set_page_config(page_title="79 – Content: SEO-Optimierung", page_icon="✍️")

m = st.text_input("Modell", "llama3.2")
t = st.text_area("Eingabetext", "")
if st.button("Run"):
    p = "Optimiere den Text für SEO, indem du Keywords sinnvoll einbaust und den Aufbau verbesserst." + "\n\nText:\n" + t
    r = ollama.chat(model=m, messages=[{"role": "user", "content": p}])
    st.write(r["message"]["content"])
