import streamlit as st

st.set_page_config(page_title="48 - Implement a 'translate code comment' too...", page_icon="💻")

st.title("💻 Implement a 'translate code comment' too...")
st.write("""Implement a 'translate code comment' tool: comment in English → comment in target language.""")

languages = ["English", "Spanish", "French", "German", "Italian", "Portuguese"]

col1, col2 = st.columns(2)
with col1:
    source = st.selectbox("From:", languages)
with col2:
    target = st.selectbox("To:", languages, index=1)

text = st.text_area("Enter text:", height=150)

if st.button("Translate", type="primary"):
    if text.strip():
        # Mock translation
        result = f"[Mock {target} translation of {source} text]: {text[:100]}..."
        st.subheader("Translation")
        st.info(result)
    else:
        st.warning("Enter text first.")
