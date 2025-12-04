import streamlit as st, ollama

st.set_page_config(page_title="24 – Few-Shot Prompting", page_icon="📚")

m = st.text_input("Modell", "llama3.2")
u = st.text_input("Satz", "Das verstehst du nicht.")
if st.button("Run"):
    msgs = [
        {"role": "user", "content": "Formuliere höflicher: Du bist zu spät."},
        {"role": "assistant", "content": "Entschuldige, du bist etwas später dran als geplant."},
        {"role": "user", "content": f"Formuliere höflicher: {u}"},
    ]
    r = ollama.chat(model=m, messages=msgs)
    st.write(r["message"]["content"])
