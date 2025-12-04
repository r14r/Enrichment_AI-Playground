import streamlit as st

st.set_page_config(page_title="32 - Implement document redaction before inge...", page_icon="📁")

st.title("📁 Implement document redaction before inge...")
st.write("""Implement document redaction before ingestion (PII removal via model prompts).""")

uploaded_file = st.file_uploader("Upload a file:", type=["txt", "csv", "json", "pdf"])

if uploaded_file:
    st.success(f"Uploaded: {uploaded_file.name}")
    st.metric("File Size", f"{uploaded_file.size} bytes")
    
    if uploaded_file.type == "text/plain":
        content = uploaded_file.read().decode()
        st.subheader("File Content")
        st.text_area("Content:", content, height=200)
        
        st.subheader("Analysis")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Lines", len(content.split("\n")))
        with col2:
            st.metric("Words", len(content.split()))
else:
    st.info("Upload a file to get started.")
