import streamlit as st
import ollama

st.set_page_config(page_title="06A – Chat mit Verlauf (Ausführlich)", page_icon="💭")
st.title("💭 06A – Chat mit Verlauf (Ausführlich)")

model = st.text_input("Modellname:", value="llama3.2")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for msg in st.session_state.chat_history:
    role = "Du" if msg["role"] == "user" else "Ollama"
    st.markdown(f"**{role}:** {msg['content']}")

user_msg = st.text_input("Deine Nachricht:")

col1, col2 = st.columns(2)
with col1:
    send_clicked = st.button("Senden")
with col2:
    clear_clicked = st.button("Verlauf löschen")

if clear_clicked:
    st.session_state.chat_history = []
    st.experimental_rerun()

if send_clicked and user_msg.strip():
    st.session_state.chat_history.append({"role": "user", "content": user_msg})
    with st.spinner("Ollama denkt ..."):
        try:
            response = ollama.chat(
                model=model,
                messages=st.session_state.chat_history,
            )
            st.session_state.chat_history.append(response["message"])
            st.experimental_rerun()
        except Exception as e:
            st.error("Fehler beim Chat-Aufruf.")
            st.exception(e)

