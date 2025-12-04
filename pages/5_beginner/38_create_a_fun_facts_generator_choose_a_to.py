import streamlit as st

st.set_page_config(page_title="38 - Create a 'fun facts' generator: choose a...", page_icon="✨")

st.title("✨ Create a 'fun facts' generator: choose a...")
st.write("""Create a 'fun facts' generator: choose a topic, get 3 facts.""")

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
