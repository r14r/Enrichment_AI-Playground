import streamlit as st

st.set_page_config(page_title="20 - Add a small sentiment analyzer: send a s...", page_icon="🏷️")

st.title("🏷️ Add a small sentiment analyzer: send a s...")
st.write("""Add a small sentiment analyzer: send a sentence and classify positive/neutral/negative.""")

text = st.text_area("Enter text to analyze:", height=150)

if st.button("Analyze", type="primary"):
    if text.strip():
        # Real Ollama call
        try:
            from lib.helper_ollama import get_chat_response
            import json
            response = get_chat_response(
                model="llama3.2",
                user_message=text,
                system_prompt="You are a sentiment analyzer. Analyze the sentiment of the text. Respond with a JSON object containing 'classification' (Positive, Neutral, or Negative) and 'confidence' (a number between 0.7 and 1.0). Example: {\"classification\": \"Positive\", \"confidence\": 0.95}",
                temperature=0.3,
            )
            try:
                result = json.loads(response)
                classification = result.get("classification", "Unknown")
                confidence = float(result.get("confidence", 0.85))
            except (json.JSONDecodeError, ValueError, KeyError):
                classification = response[:50] if len(response) > 50 else response
                confidence = 0.85
        except Exception as e:
            classification = f"Error: {e}"
            confidence = 0.0
        
        st.subheader("Analysis Results")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Classification", classification)
        with col2:
            st.metric("Confidence", f"{confidence:.1%}")
        
        st.progress(confidence)
    else:
        st.warning("Enter text first.")
