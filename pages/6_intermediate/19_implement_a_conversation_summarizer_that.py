import streamlit as st

st.set_page_config(page_title="19 - Implement a conversation summarizer that...", page_icon="💬")

st.title("💬 Implement a conversation summarizer that...")
st.write("""Implement a conversation summarizer that creates short transcripts for long chats.""")

# Initialize session state
if "chat_19_messages" not in st.session_state:
    st.session_state["chat_19_messages"] = []

# Configuration sidebar
with st.sidebar:
    st.header("Settings")
    model = st.selectbox("Model:", ["llama2", "mistral", "codellama"])
    temperature = st.slider("Temperature:", 0.0, 1.0, 0.7)

# Display chat messages
for msg in st.session_state["chat_19_messages"]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Chat input
if prompt := st.chat_input("Type your message..."):
    st.session_state["chat_19_messages"].append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    # Real Ollama call
    try:
        from lib.helper_ollama import get_chat_response
        response = get_chat_response(
            model=model,
            user_message=prompt,
            history=st.session_state["chat_19_messages"][:-1] if len(st.session_state["chat_19_messages"]) > 1 else None,
            temperature=temperature,
        )
    except Exception as e:
        response = f"Error: {e}"
    st.session_state["chat_19_messages"].append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.write(response)

# Clear button
if st.button("Clear Chat"):
    st.session_state["chat_19_messages"] = []
    st.rerun()
