import streamlit as st
import ollama

st.set_page_config(page_title="02A – Status (Ausführlich)", page_icon="🩺")
st.title("🩺 02A – Status der Ollama-Instanz (Ausführlich)")

st.write("Prüfe, ob deine lokale Ollama-Instanz erreichbar ist.")

if st.button("Status prüfen"):
    try:
        response = ollama.list()
        models = response.models if hasattr(response, "models") else response.get("models", [])
        st.success("Verbindung zu Ollama hergestellt.")
        st.write("Anzahl installierter Modelle:", len(models))
        st.json(response)
    except Exception as e:
        st.error("Konnte keine Verbindung zu Ollama herstellen.")
        st.exception(e)

