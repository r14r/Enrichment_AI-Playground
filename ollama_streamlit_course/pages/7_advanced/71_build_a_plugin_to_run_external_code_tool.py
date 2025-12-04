import streamlit as st

st.set_page_config(page_title="71 - Build a plugin to run external code tool...", page_icon="💻")

st.title("💻 Build a plugin to run external code tool...")
st.write("""Build a plugin to run external code tools safely (e.g., calculators, DB queries).""")

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
