import streamlit as st, ollama

st.set_page_config(page_title="001 – Basics: Installationscheck", page_icon="✅")
st.title("001 – Basics: Installationscheck (Ausführlich)")

st.markdown("Teste, ob die Verbindung zur lokalen Ollama-Instanz funktioniert.")

if st.button("Verbindung testen"):
    try:
        info = ollama.list()
        st.success("Verbindung erfolgreich. Modelle gefunden:")
        st.json(info)
    except Exception as e:
        st.error("Fehler bei der Verbindung. Läuft `ollama serve`?")
        st.exception(e)
