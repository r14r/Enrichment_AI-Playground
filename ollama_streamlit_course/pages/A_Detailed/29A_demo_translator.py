import streamlit as st
import ollama

st.set_page_config(page_title="29 – Übersetzer", page_icon="🌐")
st.title("🌐 29 – Demo: Übersetzer (Ausführlich)")

model = st.text_input("Modell", "llama3.2")
text = st.text_area("Text", "Hello, how are you today?", height=150)
target_lang = st.selectbox("Zielsprache", ["Deutsch", "Englisch", "Spanisch", "Französisch"])

if st.button("Übersetzen"):
    prompt = f"Übersetze den folgenden Text ins {target_lang} und gib nur die Übersetzung zurück:\n\n{text}"
    with st.spinner("Frage Modell ..."):
        try:
            resp = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])
            st.subheader("Übersetzung")
            st.write(resp["message"]["content"])
        except Exception as e:
            st.error("Fehler bei der Übersetzer-Demo.")
            st.exception(e)
