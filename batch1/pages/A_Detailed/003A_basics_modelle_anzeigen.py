import streamlit as st, ollama

st.set_page_config(page_title="003 – Basics: Modelle anzeigen", page_icon="📦")
st.title("003 – Basics: Modelle anzeigen (Ausführlich)")

if st.button("Modelle laden"):
    try:
        data = ollama.list()
        models = data.get("models", [])
        if not models:
            st.warning("Keine Modelle gefunden. Nutze `ollama pull ...` im Terminal.")
        else:
            for m in models:
                st.write(f"• **{m.get('name')}** – {m.get('model')}")
    except Exception as e:
        st.error("Fehler beim Laden der Modelle.")
        st.exception(e)
