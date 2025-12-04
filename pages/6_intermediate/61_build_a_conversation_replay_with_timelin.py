import streamlit as st

st.set_page_config(page_title="61 - Build a 'conversation replay' with timel...", page_icon="💬")

st.title("💬 Build a 'conversation replay' with timel...")
st.write("""Build a 'conversation replay' with timeline and artifacts (retrieved docs, prompts).""")

# Initialize session state
if "chat_61_messages" not in st.session_state:
    st.session_state["chat_61_messages"] = []

# Configuration sidebar
with st.sidebar:
    st.header("Settings")
    model = st.selectbox("Model:", ["llama2", "mistral", "codellama"])
    temperature = st.slider("Temperature:", 0.0, 1.0, 0.7)

# Display chat messages
for msg in st.session_state["chat_61_messages"]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Chat input
if prompt := st.chat_input("Type your message..."):
    st.session_state["chat_61_messages"].append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    # Real Ollama call
    try:
        from lib.helper_ollama import get_chat_response
        response = get_chat_response(
            model=model,
            user_message=prompt,
            history=st.session_state["chat_61_messages"][:-1] if len(st.session_state["chat_61_messages"]) > 1 else None,
            temperature=temperature,
        )
    except Exception as e:
        response = f"Error: {e}"
    st.session_state["chat_61_messages"].append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.write(response)

# Clear button
if st.button("Clear Chat"):
    st.session_state["chat_61_messages"] = []
    st.rerun()
