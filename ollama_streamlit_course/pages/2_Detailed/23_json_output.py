import streamlit as st
import ollama
import json

st.set_page_config(page_title="23 – JSON-Ausgabe", page_icon="🧾")
st.title("🧾 23 – Demo: JSON-Ausgabe (Ausführlich)")

model = st.text_input("Modell", "llama3.2")
prompt = st.text_area(
    "Prompt",
    "Erzeuge eine Liste von 3 Aufgaben für einen Prompt-Engineering-Workshop als JSON mit den Schlüsseln 'title' und 'description'.",
    height=200,
)

if st.button("JSON generieren"):
    with st.spinner("Frage Modell ..."):
        try:
            resp = ollama.chat(
                model=model,
                messages=[{"role": "user", "content": prompt}],
            )
            raw = resp["message"]["content"]
            st.subheader("Roh-Antwort")
            st.write(raw)
            st.subheader("Versuch, JSON zu parsen")
            try:
                data = json.loads(raw)
                st.json(data)
            except Exception as parse_err:
                st.warning("Konnte Antwort nicht direkt als JSON parsen.")
                st.exception(parse_err)
        except Exception as e:
            st.error("Fehler bei der JSON-Demo.")
            st.exception(e)
