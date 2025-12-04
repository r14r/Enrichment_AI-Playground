import streamlit as st
import ollama

st.set_page_config(page_title="08A – Playground (Ausführlich)", page_icon="🎯")
st.title("🎯 08A – Prompt Playground (Ausführlich)")

default_models = ["llama3.2", "llama3", "phi3", "mistral"]
model = st.selectbox("Modell", default_models, index=0)
temperature = st.slider("Temperatur", 0.0, 1.5, 0.7, 0.1)

prompt = st.text_area(
    "Prompt:",
    "Du bist ein hilfsbereiter Assistent. Erkläre in 3 Sätzen, wie man Ollama und Streamlit zusammen nutzt.",
    height=200,
)

if st.button("Prompt senden"):
    if not prompt.strip():
        st.warning("Bitte einen Prompt eingeben.")
    else:
        with st.spinner("LLM läuft ..."):
            try:
                response = ollama.chat(
                    model=model,
                    messages=[{"role": "user", "content": prompt}],
                    options={"temperature": temperature},
                )
                st.subheader("Antwort")
                st.write(response["message"]["content"])
            except Exception as e:
                st.error("Fehler beim Prompt-Aufruf.")
                st.exception(e)

