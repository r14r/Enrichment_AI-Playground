import streamlit as st

from lib.helper_ollama import generate

st.set_page_config(page_title="3 - Create a streaming chat UI", page_icon="💬")

st.title("💬 Create a streaming chat UI")
st.write("""Create a streaming chat UI that displays partial responses as the model streams.""")

# Initialize session state
if "chat_3_messages" not in st.session_state:
    st.session_state["chat_3_messages"] = []

# Configuration sidebar
with st.sidebar:
    st.header("Settings")
    model = st.selectbox("Model:", ["llama3.2", "mistral", "codellama"])
    temperature = st.slider("Temperature:", 0.0, 1.0, 0.7)

# Display chat messages
for msg in st.session_state["chat_3_messages"]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Chat input
if prompt := st.chat_input("Type your message..."):
    st.session_state["chat_3_messages"].append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    # response
    response = generate(model=model,prompt=prompt)
    
    st.session_state["chat_3_messages"].append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.write(response)

# Clear button
if st.button("Clear Chat"):
    st.session_state["chat_3_messages"] = []
    st.rerun()
