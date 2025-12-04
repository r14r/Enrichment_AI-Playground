import streamlit as st

st.set_page_config(page_title="9 - Build a chat with short-term memory summ...", page_icon="💬")

st.title("💬 Build a chat with short-term memory summ...")
st.write("""Build a chat with short-term memory summarization and retrieval for context.""")

# Initialize session state
if "chat_9_messages" not in st.session_state:
    st.session_state["chat_9_messages"] = []

# Configuration sidebar
with st.sidebar:
    st.header("Settings")
    model = st.selectbox("Model:", ["llama2", "mistral", "codellama"])
    temperature = st.slider("Temperature:", 0.0, 1.0, 0.7)

# Display chat messages
for msg in st.session_state["chat_9_messages"]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Chat input
if prompt := st.chat_input("Type your message..."):
    st.session_state["chat_9_messages"].append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    # Mock response
    response = f"[{model}] Response to: {prompt[:50]}..."
    st.session_state["chat_9_messages"].append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.write(response)

# Clear button
if st.button("Clear Chat"):
    st.session_state["chat_9_messages"] = []
    st.rerun()
