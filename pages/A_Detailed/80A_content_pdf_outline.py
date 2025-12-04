import streamlit as st
import ollama

st.set_page_config(page_title="80 – Content: PDF-Struktur skizzieren", page_icon="📄")
st.title("📄 80 – Content: PDF-Struktur skizzieren (Ausführlich)")

model = st.text_input("Sprachmodell", "llama3.2")

text = st.text_area("Dokument-Text oder Auszug", "", height=260)
extra = st.text_area("Zusatzhinweise (optional)", "", height=100)

if st.button("Ausführen"):
    if not text.strip():
        st.warning("Bitte zuerst Text eingeben.")
    else:
        prompt = "Skizziere auf Basis des Textes die grobe Struktur (Kapitel/Abschnitte) des Dokuments." + "\n\nText:\n" + text.strip()
        if extra.strip():
            prompt += "\n\nZusatz:\n" + extra.strip()
        with st.spinner("Modell wird abgefragt ..."):
            try:
                resp = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])
                st.subheader("Ergebnis")
                st.write(resp["message"]["content"])
            except Exception as e:
                st.error("Fehler bei der Verarbeitung.")
                st.exception(e)
