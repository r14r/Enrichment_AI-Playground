import streamlit as st, ollama

st.set_page_config(page_title="019 – Prompting: Antwort bewerten", page_icon="📗")
m = st.text_input("Modell", "llama3.2")
t = st.text_area("Eingabetext / Prompt / Beispiele", "")
if st.button("Run"):
    p = "Bewerte die Qualität des Textes entlang sinnvoller Kriterien." + "\n\nText:\n" + t
    r = ollama.chat(model=m, messages=[{"role":"user","content":p}])
    st.write(r["message"]["content"])
