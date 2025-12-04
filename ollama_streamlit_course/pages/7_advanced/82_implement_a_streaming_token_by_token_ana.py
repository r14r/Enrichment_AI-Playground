import streamlit as st
import random

st.set_page_config(page_title="82 - Implement a streaming, token-by-token an...", page_icon="🔒")

st.title("🔒 Implement a streaming, token-by-token an...")
st.write("""Implement a streaming, token-by-token analyzer that inspects outputs live for safety.""")

text = st.text_area("Enter text to analyze:", height=150)

if st.button("Analyze", type="primary"):
    if text.strip():
        # Mock classification
        categories = ["Category A", "Category B", "Category C"]
        confidence = random.uniform(0.7, 0.99)
        
        st.subheader("Analysis Results")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Classification", random.choice(categories))
        with col2:
            st.metric("Confidence", f"{confidence:.1%}")
        
        st.progress(confidence)
    else:
        st.warning("Enter text first.")
