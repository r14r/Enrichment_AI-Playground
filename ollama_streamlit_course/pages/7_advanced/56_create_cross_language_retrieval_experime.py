import streamlit as st

st.set_page_config(page_title="56 - Create cross-language retrieval experime...", page_icon="🎯")

st.title("🎯 Create cross-language retrieval experime...")
st.write("""Create cross-language retrieval experiments and evaluation.""")

query = st.text_input("Search query:")

# Mock data
documents = [
    "Document 1: Introduction to machine learning",
    "Document 2: Deep learning fundamentals",
    "Document 3: Natural language processing",
    "Document 4: Computer vision basics",
    "Document 5: Reinforcement learning overview"
]

if st.button("Search", type="primary") or query:
    if query.strip():
        st.subheader("Search Results")
        
        results = [d for d in documents if query.lower() in d.lower()]
        if not results:
            results = documents[:3]
        
        for i, doc in enumerate(results, 1):
            with st.expander(f"Result {i}: {doc[:50]}..."):
                st.write(doc)
                st.caption("Relevance: High")
        
        st.info(f"Found {len(results)} results for '{query}'")
    else:
        st.info("Enter a search query")
