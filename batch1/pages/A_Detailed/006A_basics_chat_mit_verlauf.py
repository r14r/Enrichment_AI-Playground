import streamlit as st, ollama

st.set_page_config(page_title="006 – Basics: Chat mit Verlauf", page_icon="💭")
st.title("006 – Basics: Chat mit Verlauf (Ausführlich)")

m = st.text_input("Modell", "llama3.2")

if "msgs" not in st.session_state:
    st.session_state.msgs = []

for msg in st.session_state.msgs:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user = st.chat_input("Frage an das Modell")
if user:
    st.session_state.msgs.append({"role":"user","content":user})
    try:
        r = ollama.chat(model=m, messages=st.session_state.msgs)
        ans = r["message"]["content"]
        st.session_state.msgs.append({"role":"assistant","content":ans})
        with st.chat_message("assistant"):
            st.markdown(ans)
    except Exception as e:
        st.error("Fehler im Chat.")
        st.exception(e)
