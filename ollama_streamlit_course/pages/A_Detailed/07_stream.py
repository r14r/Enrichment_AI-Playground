import streamlit as st
import ollama

st.set_page_config(page_title="07A – Streaming (Ausführlich)", page_icon="📡")
st.title("📡 07A – Streaming-Antwort (Ausführlich)")

model = st.text_input("Modellname:", value="llama3.2")
prompt = st.text_area("Prompt:", "Erzähle mir eine kurze Geschichte über eine programmierende Katze.")

if st.button("Streaming starten"):
    if not prompt.strip():
        st.warning("Bitte einen Prompt eingeben.")
    else:
        placeholder = st.empty()
        full_text = ""
        try:
            for chunk in ollama.chat(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                stream=True,
            ):
                content = chunk["message"]["content"]
                full_text += content
                placeholder.markdown(full_text)
        except Exception as e:
            st.error("Fehler beim Streaming.")
            st.exception(e)

