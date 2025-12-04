import streamlit as st, ollama

st.set_page_config(page_title="004 – Basics: Modell herunterladen", page_icon="⬇️")
st.title("004 – Basics: Modell herunterladen (Ausführlich)")

model = st.text_input("Modellname", "llama3.2")
out = st.empty()

if st.button("Pull starten"):
    if not model.strip():
        st.warning("Bitte einen Modellnamen angeben.")
    else:
        try:
            for status in ollama.pull(model, stream=True):
                out.write(status.get("status"))
            st.success("Pull-Vorgang abgeschlossen (oder bereits vorhanden).")
        except Exception as e:
            st.error("Fehler beim Pull.")
            st.exception(e)
