import streamlit as st
import ollama

st.set_page_config(page_title="27 – Code-Helfer", page_icon="💻")
st.title("💻 27 – Demo: Code-Helfer (Ausführlich)")

model = st.text_input("Modell", "llama3.2")
code = st.text_area(
    "Python-Code",
    "def add(a, b):\n    return a + b",
    height=200,
)

task = st.selectbox(
    "Aufgabe",
    ["Erklären", "Verbessern", "Tests vorschlagen"],
)

if st.button("Analyse starten"):
    instr_map = {
        "Erklären": "Erkläre kurz und verständlich, was dieser Code macht.",
        "Verbessern": "Schlage Verbesserungen oder Best Practices für diesen Code vor.",
        "Tests vorschlagen": "Schlage einige einfache Unit-Tests für diesen Code vor.",
    }
    prompt = instr_map[task] + "\n\nCode:\n" + code
    with st.spinner("Frage Modell ..."):
        try:
            resp = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])
            st.subheader("Antwort")
            st.write(resp["message"]["content"])
        except Exception as e:
            st.error("Fehler bei der Code-Helfer-Demo.")
            st.exception(e)
