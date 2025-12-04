import streamlit as st
import ollama

st.set_page_config(page_title="03A – Modelle anzeigen (Ausführlich)", page_icon="📦")
st.title("📦 03A – Installierte Modelle (Ausführlich)")

if st.button("Modelle laden"):
    try:
        response = ollama.list()
        models = response.models if hasattr(response, "models") else response.get("models", [])
        if not models:
            st.warning("Keine Modelle installiert.")
        else:
            for m in models:
                name = m.get("model") or m.get("name", "Unbekanntes Modell")
                with st.expander(name):
                    st.write(m)
    except Exception as e:
        st.error("Fehler beim Laden der Modelle.")
        st.exception(e)

