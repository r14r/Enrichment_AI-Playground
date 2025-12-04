import streamlit as st

st.set_page_config(page_title="7 - Build a 'Clear chat' button that resets ...", page_icon="💬")

st.title("💬 Build a 'Clear chat' button that resets ...")
st.write("""Build a 'Clear chat' button that resets conversation state.""")

# Initialize session state
if "chat_7_messages" not in st.session_state:
    st.session_state["chat_7_messages"] = []

# Configuration sidebar
with st.sidebar:
    st.header("Settings")
    model = st.selectbox("Model:", ["llama2", "mistral", "codellama"])
    temperature = st.slider("Temperature:", 0.0, 1.0, 0.7)

# Display chat messages
for msg in st.session_state["chat_7_messages"]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Chat input
if prompt := st.chat_input("Type your message..."):
    st.session_state["chat_7_messages"].append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    # Mock response
    response = f"[{model}] Response to: {prompt[:50]}..."
    st.session_state["chat_7_messages"].append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.write(response)

# Clear button
if st.button("Clear Chat"):
    st.session_state["chat_7_messages"] = []
    st.rerun()
