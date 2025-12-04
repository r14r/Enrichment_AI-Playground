import streamlit as st
import ollama

st.set_page_config(page_title="25 – Denkweise erklären", page_icon="🧠")
st.title("🧠 25 – Demo: Denkweise erklären (Ausführlich)")

model = st.text_input("Modell", "llama3.2")
prompt = st.text_area(
    "Aufgabe",
    "Erkläre Schritt für Schritt, wie man eine einfache Streamlit-App baut.",
    height=200,
)

if st.button("Antwort generieren"):
    instruction = (
        "Löse die Aufgabe strukturiert in nummerierten Schritten und erkläre "
        "kurz, warum jeder Schritt wichtig ist. Am Ende fasse alles in 2 Sätzen zusammen."
    )
    full_prompt = instruction + "\n\nAufgabe: " + prompt
    with st.spinner("Frage Modell ..."):
        try:
            resp = ollama.chat(
                model=model,
                messages=[{"role": "user", "content": full_prompt}],
            )
            st.subheader("Antwort")
            st.write(resp["message"]["content"])
        except Exception as e:
            st.error("Fehler bei der Denkweise-Demo.")
            st.exception(e)
