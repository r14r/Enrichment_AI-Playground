import streamlit as st, ollama

st.set_page_config(page_title="34 – Content: Text analysieren & zusammenfassen", page_icon="📑")

m = st.text_input("Modell", "llama3.2")
t = st.text_area("Text", "Ein kurzer Beispieltext ...")
if st.button("Zusammenfassen"):
    p = "Fasse diesen Text in 3 Sätzen zusammen:\n\n" + t
    r = ollama.chat(model=m, messages=[{"role": "user", "content": p}])
    st.write(r["message"]["content"])
