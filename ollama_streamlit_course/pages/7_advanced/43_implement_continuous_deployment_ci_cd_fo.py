import streamlit as st
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

st.set_page_config(page_title="43 - Implement continuous deployment (CI/CD) ...", page_icon="💻")

st.title("💻 Implement continuous deployment (CI/CD) ...")
st.write("""Implement continuous deployment (CI/CD) for models and app code.""")

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
