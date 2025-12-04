import streamlit as st

st.set_page_config(page_title="18 - Create a one-button code commenter: past...", page_icon="💻")

st.title("💻 Create a one-button code commenter: past...")
st.write("""Create a one-button code commenter: paste code, get inline explanation from the model.""")

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
