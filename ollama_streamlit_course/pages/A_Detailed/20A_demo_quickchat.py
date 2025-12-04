import streamlit as st
import ollama

st.set_page_config(page_title="20 – Demo Quick-Chat", page_icon="💡")
st.title("💡 20 – Demo Quick-Chat (Ausführlich)")

st.write("Kleine Demo: ein sehr einfacher Quick-Chat mit vordefiniertem Systemprompt.")

model = st.text_input("Modell", "llama3.2")
system_prompt = st.text_area(
    "System-Prompt",
    "Du bist ein freundlicher Assistent, der kurze und präzise Antworten gibt.",
)
user_msg = st.text_input("Deine Frage:", "Was kann ich heute mit Ollama üben?")

if st.button("Antwort generieren"):
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_msg},
    ]
    with st.spinner("Generiere Antwort ..."):
        try:
            resp = ollama.chat(model=model, messages=messages)
            st.subheader("Antwort")
            st.write(resp["message"]["content"])
        except Exception as e:
            st.error("Fehler beim Quick-Chat.")
            st.exception(e)
