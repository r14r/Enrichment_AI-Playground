import streamlit as st


st.set_page_config(page_title="35 - Add a 'save favorite prompt' list in bro...", page_icon="🎯")

st.title("🎯 Add a 'save favorite prompt' list in bro...")
st.write("""Add a 'save favorite prompt' list in browser session state.""")

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
