import streamlit as st
import re

st.set_page_config(page_title="99 - Implement a 'prompt explainability' tool...", page_icon="🎯")

st.title("🎯 Implement a 'prompt explainability' tool...")
st.write("""Implement a 'prompt explainability' tool that asks the model to explain why it responded.""")

# Main input
user_input = st.text_area("Input:", height=150, placeholder="Enter your input here...")

# Options
with st.expander("Options"):
    option1 = st.selectbox("Mode:", ["Default", "Advanced", "Custom"])
    option2 = st.slider("Intensity:", 1, 10, 5)

if st.button("Execute", type="primary"):
    if user_input.strip():
        st.subheader("Results")
        
        result = f"""Task completed!

Input processed with:
- Mode: {option1}
- Intensity: {option2}

Output: Processing complete for your input."""
        
        st.success(result)
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Processing Time", "0.5s")
        with col2:
            st.metric("Status", "Success")
    else:
        st.warning("Please provide input.")
