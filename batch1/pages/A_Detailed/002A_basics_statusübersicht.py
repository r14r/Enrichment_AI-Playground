import streamlit as st, ollama, math

st.set_page_config(page_title="002 – Basics: Statusübersicht", page_icon="🩺")
st.title("002 – Basics: Statusübersicht (Ausführlich)")

if st.button("Status abrufen"):
    try:
        data = ollama.list()
        models = data.get("models", [])
        st.write(f"Anzahl Modelle: {len(models)}")
        for m in models:
            size = m.get("size", 0)
            mb = round(size / (1024*1024), 1) if size else 0
            st.write(f"- {m.get('name')} ({mb} MB)")
    except Exception as e:
        st.error("Fehler beim Statusabruf.")
        st.exception(e)
