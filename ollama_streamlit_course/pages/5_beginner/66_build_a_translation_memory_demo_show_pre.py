import streamlit as st

st.set_page_config(page_title="66 – Build A Translation Memory Demo Show Pre", page_icon="📄")

st.title("66 – Build A Translation Memory Demo Show Pre")

st.write('Mock translator: demonstrates target languages and token-count estimation. Replace with real translator/LLM calls later.')

txt = st.text_area('Text to translate', height=150)
lang = st.selectbox('Target language', ['Spanish','German','French','Mock-Reverse'])
if st.button('Translate'):
    if not txt.strip():
        st.warning('Enter text to translate')
    else:
        if lang == 'Mock-Reverse':
            out = txt[::-1]
        else:
            out = f"[Mock {lang} translation] " + txt
        st.code(out)
        st.write('Estimated tokens (approx):', max(1, len(out.split())//1))
