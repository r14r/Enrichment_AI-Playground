import streamlit as st, ollama

st.set_page_config(page_title="58 – Media: Sprechstil analysieren", page_icon="🎧")

m = st.text_input("Modell", "llama3.2")
t = st.text_area("Audio-Transkript oder Notizen", "")
if st.button("Run"):
    p = "Beschreibe den Sprechstil (z. B. ruhig, hektisch, sachlich, motivierend) und begründe kurz deine Einschätzung." + "\n\nText:\n" + t
    r = ollama.chat(model=m, messages=[{"role": "user", "content": p}])
    st.write(r["message"]["content"])
