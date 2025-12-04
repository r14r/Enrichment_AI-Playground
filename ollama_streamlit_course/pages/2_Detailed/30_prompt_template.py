import streamlit as st
import ollama

st.set_page_config(page_title="30 – Prompt-Templates", page_icon="📋")
st.title("📋 30 – Demo: Prompt-Templates (Ausführlich)")

model = st.text_input("Modell", "llama3.2")

template = st.selectbox(
    "Template wählen",
    ["Blog-Idee", "Lernplan", "Feedback"],
)

subject = st.text_input("Thema / Kontext", "Streamlit und Ollama lernen")

if st.button("Prompt aus Template nutzen"):
    if template == "Blog-Idee":
        prompt = f"Erzeuge 5 Blog-Ideen zum Thema '{subject}' mit kurzen Beschreibungen."
    elif template == "Lernplan":
        prompt = f"Erstelle einen 7-Tage-Lernplan für '{subject}' mit täglichen Aufgaben."
    else:
        prompt = f"Gib mir konstruktives Feedback zu folgendem Thema: '{subject}'."

    st.caption(f"Verwendeter Prompt:\n{prompt}")
    with st.spinner("Frage Modell ..."):
        try:
            resp = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])
            st.subheader("Antwort")
            st.write(resp["message"]["content"])
        except Exception as e:
            st.error("Fehler bei der Prompt-Template-Demo.")
            st.exception(e)
