import streamlit as st

st.set_page_config(page_title="93 - Add a 'small code generator' for basic f...", page_icon="💻")

st.title("💻 Add a 'small code generator' for basic f...")
st.write("""Add a 'small code generator' for basic functions like factorial, fibonacci.""")

language = st.selectbox("Language:", ["Python", "JavaScript", "Java", "C++", "Go"])

code = st.text_area(
    f"Enter {language} code:",
    height=200,
    placeholder="# Paste your code here..."
)

action = st.selectbox("Action:", ["Explain", "Review", "Optimize", "Add Comments", "Find Bugs"])

if st.button("Process", type="primary"):
    if code.strip():
        st.subheader(f"{action} Results")
        
        # Real Ollama call
        try:
            from lib.helper_ollama import get_chat_response
            result = get_chat_response(
                model="llama3.2",
                user_message=f"{action} this {language} code:\n\n{code}",
                system_prompt=f"You are a code analysis expert. {action} the provided {language} code. Be concise and helpful.",
                temperature=0.5,
            )
        except Exception as e:
            result = f"Error: {e}"
        
        st.code(result)
    else:
        st.warning("Enter code first.")
