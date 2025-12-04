import streamlit as st

st.set_page_config(page_title="74 – Build A Short Survey Summarizer That Tur", page_icon="📄")

st.title("74 – Build A Short Survey Summarizer That Tur")

st.write('Naive summarizer: extractive heuristic—take the top N sentences by very simple scoring (sentence length + keyword overlap).')

text = st.text_area('Text to summarize', height=200)
num = st.slider('Sentences to return', 1, 5, 2)
if st.button('Summarize'):
    if not text.strip():
        st.warning('Paste text to summarize')
    else:
        sents = [s.strip() for s in re.split(r'(?<=[.!?])\s+', text) if s.strip()]
        # score by length and keyword density
        keywords = set([w.lower() for w in text.split()[:10]])
        scored = []
        for s in sents:
            score = len(s)
            score += sum(1 for w in s.split() if w.lower() in keywords)
            scored.append((score,s))
        top = [s for _,s in sorted(scored, reverse=True)[:num]]
        st.write('
'.join(top))
