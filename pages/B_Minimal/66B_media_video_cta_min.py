import streamlit as st, ollama

st.set_page_config(page_title="66 – Media: Call-to-Action Ideen", page_icon="🎥")

m = st.text_input("Modell", "llama3.2")
t = st.text_area("Video-Transkript oder Beschreibung", "")
if st.button("Run"):
    p = "Schlage geeignete Call-to-Action-Ideen vor, die zum Inhalt des Videos passen." + "\n\nText:\n" + t
    r = ollama.chat(model=m, messages=[{"role": "user", "content": p}])
    st.write(r["message"]["content"])
