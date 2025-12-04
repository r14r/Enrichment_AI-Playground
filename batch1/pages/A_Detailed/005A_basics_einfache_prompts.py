import streamlit as st, ollama

st.set_page_config(page_title="005 – Basics: Einfache Prompts", page_icon="💬")
st.title("005 – Basics: Einfache Prompts (Ausführlich)")

m = st.text_input("Modell", "llama3.2")
p = st.text_area("Prompt", "Erkläre kurz, was Ollama macht.", height=200)

if st.button("Antwort holen"):
    try:
        r = ollama.chat(model=m, messages=[{"role":"user","content":p}])
        st.subheader("Antwort")
        st.write(r["message"]["content"])
    except Exception as e:
        st.error("Fehler bei der Abfrage.")
        st.exception(e)
