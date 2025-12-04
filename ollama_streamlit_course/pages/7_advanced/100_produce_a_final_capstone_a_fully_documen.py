import streamlit as st

st.set_page_config(page_title="100 - Produce a final capstone: a fully docume...", page_icon="📁")

st.title("📁 Produce a final capstone: a fully docume...")
st.write("""Produce a final capstone: a fully documented, secured, monitored, and evaluated Ollama+Streamlit product with reproducible experiments and deployment artifacts.""")

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
