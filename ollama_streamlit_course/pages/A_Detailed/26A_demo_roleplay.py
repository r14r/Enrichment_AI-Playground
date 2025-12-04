import streamlit as st
import ollama

st.set_page_config(page_title="26 – Rollen & Personas", page_icon="🎭")
st.title("🎭 26 – Demo: Rollen & Personas (Ausführlich)")

model = st.text_input("Modell", "llama3.2")
persona = st.selectbox(
    "Persona",
    ["Python-Trainer", "Projektmanager", "Line-Dance-Coach", "Motivations-Coach"],
)
question = st.text_input("Frage", "Wie kann ich besser mit KI lernen?")

persona_prompts = {
    "Python-Trainer": "Du bist ein erfahrener Python-Trainer und gibst praxisnahe Tipps.",
    "Projektmanager": "Du bist ein strukturierter Projektmanager und denkst in Aufgabenpaketen.",
    "Line-Dance-Coach": "Du bist ein Line-Dance-Coach und erklärst Dinge mit Bewegungs-Analogien.",
    "Motivations-Coach": "Du bist ein Motivations-Coach und stärkst das Selbstvertrauen.",
}

if st.button("Antwort in Rolle generieren"):
    msgs = [
        {"role": "system", "content": persona_prompts[persona]},
        {"role": "user", "content": question},
    ]
    with st.spinner("Frage Modell ..."):
        try:
            resp = ollama.chat(model=model, messages=msgs)
            st.subheader("Antwort")
            st.write(resp["message"]["content"])
            st.caption(f"Persona: {persona}")
        except Exception as e:
            st.error("Fehler bei der Rollen-Demo.")
            st.exception(e)
