import streamlit as st

st.set_page_config(page_title="15 – Add An Option To Switch Between Chat And", page_icon="📄")

st.title("15 – Add An Option To Switch Between Chat And")

st.write('Tiny local chat demo (no external LLM). Shows session history, simple rules-based replies, and export.')

if 'history' not in st.session_state:
    st.session_state.history = []

with st.form('chat'):
    user = st.text_input('Your message', key=f'input_{num}')
    persona = st.selectbox('Persona', ['Helpful Assistant','Concise Bot','Enthusiastic Coach'])
    submitted = st.form_submit_button('Send')
    if submitted and user:
        st.session_state.history.append({'who':'User','text':user})
        # simple rule-based reply
        if 'how' in user.lower():
            reply = f"({persona}) Here's a step-by-step hint about {user.split()[0]}..."
        else:
            reply = f"({persona}) I heard: {user[::-1]}"  # playful reversed echo
        st.session_state.history.append({'who':'Bot','text':reply})

for entry in st.session_state.history:
    if entry['who']=='User':
        st.markdown(f"**You:** {entry['text']}")
    else:
        st.info(entry['text'])

if st.button('Export conversation'):
    import json
    st.download_button('Download JSON', json.dumps(st.session_state.history, ensure_ascii=False, indent=2), file_name='conversation.json')
