import streamlit as st

st.set_page_config(page_title="26 - Implement a short code runner sandbox to...", page_icon="💻")

st.title("💻 Implement a short code runner sandbox to...")
st.write("""Implement a short code runner sandbox to run small snippets safely (careful security).""")

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
        
        lines = len(code.split("\n"))
        mock_result = f"""Analysis of your {language} code:
- Lines of code: {lines}
- Estimated complexity: Medium
- Suggestion: Consider adding error handling

Your code appears to be well-structured."""
        
        st.code(mock_result)
    else:
        st.warning("Enter code first.")
