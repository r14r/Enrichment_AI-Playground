import streamlit as st
import ollama

st.set_page_config(page_title="Simple Chat — Starter", page_icon="💬")

st.title("Simple Chat — Ollama + Streamlit (Starter)")

model = st.selectbox("Model", ["llama3.2", "alpaca-mini"], index=0)
user_input = st.text_input("Your message", "Hello, how are you?")

if "history" not in st.session_state:
    st.session_state.history = []

def send_message():
    if not user_input.strip():
        st.warning("Please enter a message.")
        return
    st.session_state.history.append({"role": "user", "content": user_input})
    try:
        # Basic single-turn chat — build messages from history if desired
        resp = ollama.chat(model=model, messages=st.session_state.history)
        assistant = resp.get("message", {}).get("content")
        st.session_state.history.append({"role": "assistant", "content": assistant})
    except Exception as e:
        st.error("Request failed: " + str(e))

if st.button("Send"):
    send_message()

if st.session_state.history:
    st.subheader("Conversation")
    for m in st.session_state.history:
        role = m.get("role", "user").capitalize()
        st.markdown(f"**{role}:** {m.get('content', '')}")
