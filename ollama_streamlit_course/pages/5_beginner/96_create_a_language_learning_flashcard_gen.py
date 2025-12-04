import streamlit as st

st.set_page_config(page_title="96 - Create a 'language learning flashcard' g...", page_icon="✨")

st.title("✨ Create a 'language learning flashcard' g...")
st.write("""Create a 'language learning flashcard' generator from a vocabulary list.""")

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
        mock_output = f"[{style}, {length}] Generated content based on: {input_text[:100]}..."
        st.success(mock_output)
        
        st.download_button("Download", mock_output, file_name="generated.txt")
    else:
        st.warning("Enter input first.")
