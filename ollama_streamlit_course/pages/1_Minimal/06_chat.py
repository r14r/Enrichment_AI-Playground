import streamlit as st, ollama

st.set_page_config(page_title="06B – Chat mit Verlauf (Minimal)", page_icon="💭")

m = st.text_input("Modell", "llama3.2")
if "h" not in st.session_state:
    st.session_state.h = []
for x in st.session_state.h:
    st.write(x["role"], ":", x["content"])
u = st.text_input("Nachricht")
if st.button("Send"):
    st.session_state.h.append({"role": "user", "content": u})
    r = ollama.chat(model=m, messages=st.session_state.h)
    st.session_state.h.append(r["message"])
    st.experimental_rerun()

