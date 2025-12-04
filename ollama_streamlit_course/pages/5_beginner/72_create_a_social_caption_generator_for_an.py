import streamlit as st

st.set_page_config(page_title="72 – Create A Social Caption Generator For An", page_icon="📄")

st.title("72 – Create A Social Caption Generator For An")

st.write('Generic text toolbox: basic operations you can apply locally.')

text = st.text_area('Input text', height=160)
op = st.selectbox('Operation', ['Echo','Reverse','Uppercase','First sentence','Word count'])
if st.button('Run'):
    if op == 'Echo':
        out = text
    elif op == 'Reverse':
        out = text[::-1]
    elif op == 'Uppercase':
        out = text.upper()
    elif op == 'Word count':
        out = f"Words: {len(text.split())}"
    else:
        out = text.split('.')[0]
    st.code(out)
