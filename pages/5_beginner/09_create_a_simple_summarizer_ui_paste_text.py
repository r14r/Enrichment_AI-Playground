import streamlit as st
import re

st.set_page_config(page_title="9 - Create a simple summarizer UI: paste tex...", page_icon="📝")

st.title("📝 Create a simple summarizer UI: paste tex...")
st.write("""Create a simple summarizer UI: paste text, click 'Summarize', show brief summary from Ollama.""")

# Input
text = st.text_area("Enter text to summarize:", height=200)
length = st.slider("Summary sentences:", 1, 5, 2)

if st.button("Summarize", type="primary"):
    if text.strip():
        sentences = re.split(r"(?<=[.!?])\s+", text.strip())
        keywords = set(text.lower().split()[:15])
        
        scored = []
        for s in sentences:
            score = len(s) + sum(1 for w in s.lower().split() if w in keywords) * 2
            scored.append((score, s))
        
        top = [s for _, s in sorted(scored, reverse=True)[:length]]
        
        st.subheader("Summary")
        for s in top:
            st.markdown(f"- {s}")
        
        original_words = len(text.split())
        summary_words = len(" ".join(top).split())
        if original_words > 0:
            compression = 100 - (summary_words * 100 // original_words)
            st.metric("Compression", f"{compression}%")
    else:
        st.warning("Enter text first.")
