import streamlit as st

st.set_page_config(page_title="10 - Build a translator UI: source text + tar...", page_icon="🌐")

st.title("🌐 Build a translator UI: source text + tar...")
st.write("""Build a translator UI: source text + target language selector → show translated text.""")

languages = ["English", "Spanish", "French", "German", "Italian", "Portuguese"]

col1, col2 = st.columns(2)
with col1:
    source = st.selectbox("From:", languages)
with col2:
    target = st.selectbox("To:", languages, index=1)

text = st.text_area("Enter text:", height=150)

if st.button("Translate", type="primary"):
    if text.strip():
        # Real Ollama call
        try:
            from lib.helper_ollama import translate_text
            result = translate_text(
                model="llama3.2",
                text=text,
                source_language=source,
                target_language=target,
            )
        except Exception as e:
            result = f"Error: {e}"
        st.subheader("Translation")
        st.info(result)
    else:
        st.warning("Enter text first.")
