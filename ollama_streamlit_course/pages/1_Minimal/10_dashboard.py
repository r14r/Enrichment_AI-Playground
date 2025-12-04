import streamlit as st, ollama

st.set_page_config(page_title="10B – Dashboard (Minimal)", page_icon="📊")

t1, t2, t3 = st.tabs(["Status", "Modelle", "Chat"])

with t1:
    if st.button("Status"):
        st.write(ollama.list())
with t2:
    if st.button("Modelle"):
        st.write(ollama.list())
with t3:
    if "h" not in st.session_state:
        st.session_state.h = []
    for x in st.session_state.h:
        st.write(x["role"], ":", x["content"])
    m = st.text_input("Modell", "llama3.2")
    u = st.text_input("Msg")
    if st.button("Send"):
        st.session_state.h.append({"role": "user", "content": u})
        r = ollama.chat(model=m, messages=st.session_state.h)
        st.session_state.h.append(r["message"])
        st.experimental_rerun()

