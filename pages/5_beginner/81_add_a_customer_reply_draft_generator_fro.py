import streamlit as st


st.set_page_config(page_title="81 - Add a 'customer reply draft' generator f...", page_icon="✨")

st.title("✨ Add a 'customer reply draft' generator f...")
st.write("""Add a 'customer reply draft' generator from an incoming support ticket.""")

# Input fields
input_text = st.text_area("Input:", height=150, placeholder="Enter your input here...")

col1, col2 = st.columns(2)
with col1:
    style = st.selectbox("Style:", ["Professional", "Casual", "Creative", "Technical"])
with col2:
    length = st.selectbox("Length:", ["Short", "Medium", "Long"])

if st.button("Generate", type="primary"):
    if input_text.strip():
        st.subheader("Generated Output")
        # Real Ollama call
        try:
            from lib.helper_ollama import generate_content
            output = generate_content(
                model="llama3.2",
                prompt=input_text,
                style=style.lower(),
                length=length.lower(),
            )
        except Exception as e:
            output = f"Error: {e}"
        st.success(output)
        
        st.download_button("Download", output, file_name="generated.txt")
    else:
        st.warning("Enter input first.")
