import streamlit as st
import ollama

st.set_page_config(page_title="24 – Few-Shot Prompting", page_icon="📚")
st.title("📚 24 – Demo: Few-Shot Prompting (Ausführlich)")

model = st.text_input("Modell", "llama3.2")

examples = [
    {"role": "user", "content": "Formuliere diese Aussage höflicher: Du bist zu spät."},
    {"role": "assistant", "content": "Entschuldige, du bist etwas später dran als geplant."},
    {"role": "user", "content": "Formuliere diese Aussage höflicher: Das ist falsch."},
    {"role": "assistant", "content": "Ich glaube, hier hat sich ein kleiner Fehler eingeschlichen."},
]

new_input = st.text_input("Neue Aussage für Höflichkeits-Umformulierung:", "Das verstehst du nicht.")

if st.button("Few-Shot anwenden"):
    messages = examples + [
        {"role": "user", "content": f"Formuliere diese Aussage höflicher: {new_input}"},
    ]
    with st.spinner("Frage Modell ..."):
        try:
            resp = ollama.chat(model=model, messages=messages)
            st.subheader("Antwort")
            st.write(resp["message"]["content"])
        except Exception as e:
            st.error("Fehler bei Few-Shot-Demo.")
            st.exception(e)
