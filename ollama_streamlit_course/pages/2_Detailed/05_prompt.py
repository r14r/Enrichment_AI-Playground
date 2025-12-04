import streamlit as st
import ollama

st.set_page_config(page_title="05A – Prompt (Ausführlich)", page_icon="💬")
st.title("💬 05A – Einfacher Prompt (Ausführlich)")

model = st.text_input("Modellname:", value="llama3.2")
prompt = st.text_area("Prompt:", "Erkläre kurz, was Ollama ist.")

if st.button("Senden"):
    if not prompt.strip():
        st.warning("Bitte einen Prompt eingeben.")
    else:
        with st.spinner("Frage Modell ..."):
            try:
                response = ollama.chat(
                    model=model,
                    messages=[{"role": "user", "content": prompt}],
                )
                st.subheader("Antwort")
                st.write(response["message"]["content"])
            except Exception as e:
                st.error("Fehler beim Aufruf von `ollama.chat`.")
                st.exception(e)

