import streamlit as st

st.set_page_config(page_title="94 – Build A Cover Letter Paragraph Generator", page_icon="📄")

st.title("94 – Build A Cover Letter Paragraph Generator")

st.write('Chain-of-thought mock: decompose into subtasks and show intermediate results (local heuristics).')

q = st.text_input('Question')
if st.button('Decompose') and q:
    words = q.split()
    parts = [ ' '.join(words[i:i+max(1,len(words)//3)]) for i in range(0,len(words), max(1,len(words)//3))][:3]
    for i,p in enumerate(parts):
        st.write(f"Step {i+1}: consider '{p}'")
    st.write('Intermediate conclusions:')
    for i,p in enumerate(parts):
        st.write(f"- Conclusion {i+1}: {p[::-1][:40]}")
    st.write('Final (mock) answer: ' + ' '.join(words[:7]))
