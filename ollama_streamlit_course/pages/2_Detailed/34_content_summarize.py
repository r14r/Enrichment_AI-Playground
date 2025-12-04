import streamlit as st
import ollama

st.set_page_config(page_title="34 – Content: Text analysieren & zusammenfassen", page_icon="📑")
st.title("📑 34 – Content: Text analysieren & zusammenfassen (Ausführlich)")

model = st.text_input("Sprachmodell", "llama3.2")

text = st.text_area(
    "Eingabetext",
    "Hier könntest du einen längeren Abschnitt aus einem Blog oder Artikel einfügen ...",
    height=260,
)

if st.button("Analysieren & zusammenfassen"):
    if not text.strip():
        st.warning("Bitte einen Text einfügen.")
    else:
        prompt = f"""
Analysiere den folgenden Text und liefere:

1. Eine Kurz-Zusammenfassung in 2–3 Sätzen.
2. Die wichtigsten Stichpunkte (Bullet Points).
3. Die Zielgruppe, für die der Text am sinnvollsten ist.
4. Einen Vorschlag für einen prägnanten Titel.

Text:
{text}
"""
        with st.spinner("Analysiere Text ..."):
            try:
                resp = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])
                st.subheader("Analyse-Ergebnis")
                st.write(resp["message"]["content"])
            except Exception as e:
                st.error("Fehler bei der Textanalyse.")
                st.exception(e)
