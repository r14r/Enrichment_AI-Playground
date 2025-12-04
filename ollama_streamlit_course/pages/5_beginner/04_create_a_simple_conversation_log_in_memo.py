import streamlit as st

st.set_page_config(page_title="4 - Create a simple conversation log (in-mem...", page_icon="💬")

st.title("💬 Create a simple conversation log (in-mem...")
st.write("""Create a simple conversation log (in-memory list) that shows previous user/assistant turns.""")

# Initialize session state
if "chat_4_messages" not in st.session_state:
    st.session_state["chat_4_messages"] = []

# Configuration sidebar
with st.sidebar:
    st.header("Settings")
    model = st.selectbox("Model:", ["llama2", "mistral", "codellama"])
    temperature = st.slider("Temperature:", 0.0, 1.0, 0.7)

# Display chat messages
for msg in st.session_state["chat_4_messages"]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Chat input
if prompt := st.chat_input("Type your message..."):
    st.session_state["chat_4_messages"].append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    # Mock response
    response = f"[{model}] Response to: {prompt[:50]}..."
    st.session_state["chat_4_messages"].append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.write(response)

# Clear button
if st.button("Clear Chat"):
    st.session_state["chat_4_messages"] = []
    st.rerun()
