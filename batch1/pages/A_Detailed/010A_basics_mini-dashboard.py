import streamlit as st, ollama

st.set_page_config(page_title="010 – Basics: Mini-Dashboard", page_icon="📊")
st.title("010 – Basics: Mini-Dashboard (Ausführlich)")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Status")
    if st.button("Ollama Status"):
        try:
            data = ollama.list()
            st.success(f"Modelle: {len(data.get('models', []))}")
            st.json(data)
        except Exception as e:
            st.error("Fehler beim Statusabruf.")
            st.exception(e)

with col2:
    st.subheader("Schnell-Prompt")
    m = st.text_input("Modell", "llama3.2")
    p = st.text_input("Prompt", "Sag Hallo! 👋")
    if st.button("Senden"):
        try:
            r = ollama.chat(model=m, messages=[{"role":"user","content":p}])
            st.write(r["message"]["content"])
        except Exception as e:
            st.error("Fehler beim Prompt.")
            st.exception(e)
