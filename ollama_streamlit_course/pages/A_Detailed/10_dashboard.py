import streamlit as st
import ollama

st.set_page_config(page_title="10A – Dashboard (Ausführlich)", page_icon="📊")
st.title("📊 10A – Ollama Mini-Dashboard (Ausführlich)")

tab_status, tab_models, tab_chat = st.tabs(["Status", "Modelle", "Quick-Chat"])

with tab_status:
    st.subheader("Server-Status")
    if st.button("Status prüfen", key="status_btn"):
        try:
            response = ollama.list()
            models = response.models if hasattr(response, "models") else response.get("models", [])
            st.success("Ollama läuft.")
            st.write("Installierte Modelle:", len(models))
            st.json(response)
        except Exception as e:
            st.error("Keine Verbindung zu Ollama.")
            st.exception(e)

with tab_models:
    st.subheader("Installierte Modelle")
    if st.button("Modelle laden", key="models_btn"):
        try:
            response = ollama.list()
            models = response.models if hasattr(response, "models") else response.get("models", [])
            if not models:
                st.warning("Keine Modelle installiert.")
            else:
                st.table(
                    [
                        {
                            "Name": m.get("model") or m.get("name", "Unbekannt"),
                            "Größe": m.get("size"),
                            "Geändert": m.get("modified"),
                        }
                        for m in models
                    ]
                )
        except Exception as e:
            st.error("Fehler beim Laden der Modelle.")
            st.exception(e)

with tab_chat:
    st.subheader("Quick-Chat")

    default_models = ["llama3.2", "llama3", "phi3", "mistral"]
    model = st.selectbox("Modell", default_models, index=0, key="chat_model")

    if "quick_history" not in st.session_state:
        st.session_state.quick_history = []

    for msg in st.session_state.quick_history:
        speaker = "Du" if msg["role"] == "user" else "Ollama"
        st.markdown(f"**{speaker}:** {msg['content']}")

    user_msg = st.text_input("Deine Nachricht:", key="quick_input")
    if st.button("Senden", key="quick_send") and user_msg.strip():
        st.session_state.quick_history.append({"role": "user", "content": user_msg})
        with st.spinner("Ollama denkt ..."):
            try:
                response = ollama.chat(
                    model=model,
                    messages=st.session_state.quick_history,
                )
                st.session_state.quick_history.append(response["message"])
                st.experimental_rerun()
            except Exception as e:
                st.error("Fehler beim Chat.")
                st.exception(e)

