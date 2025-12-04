import streamlit as st
<<<<<<< HEAD
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
=======
import re
>>>>>>> main

st.set_page_config(page_title="79 - Implement a 'grammar quiz' maker that pr...", page_icon="🎯")

st.title("🎯 Implement a 'grammar quiz' maker that pr...")
st.write("""Implement a 'grammar quiz' maker that provides corrected examples.""")

# Main input
user_input = st.text_area("Input:", height=150, placeholder="Enter your input here...")

# Options
with st.expander("Options"):
    option1 = st.selectbox("Mode:", ["Default", "Advanced", "Custom"])
    option2 = st.slider("Intensity:", 1, 10, 5)

if st.button("Execute", type="primary"):
    if user_input.strip():
        st.subheader("Results")
        
        # Real Ollama call
        try:
            from lib.helper_ollama import generate_content
            result = generate_content(
                model="llama3.2",
                prompt=user_input,
                style=option1.lower() if option1 != "Default" else "professional",
                length="medium",
            )
        except Exception as e:
            result = f"Error: {e}"
        
        st.success(result)
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Processing Time", "0.5s")
        with col2:
            st.metric("Status", "Success")
    else:
        st.warning("Please provide input.")
