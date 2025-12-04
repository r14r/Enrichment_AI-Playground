import streamlit as st, ollama

st.set_page_config(page_title="007 – Basics: Streaming", page_icon="📡")
st.title("007 – Basics: Streaming (Ausführlich)")

m = st.text_input("Modell", "llama3.2")
p = st.text_area("Prompt", "Schreibe einen motivierenden Text über das Lernen mit KI.", height=200)

if st.button("Stream starten"):
    ph = st.empty()
    out = ""
    try:
        for c in ollama.chat(model=m, messages=[{"role":"user","content":p}], stream=True):
            out += c["message"]["content"]
            ph.markdown(out)
    except Exception as e:
        st.error("Fehler beim Streaming.")
        st.exception(e)
