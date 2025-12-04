import streamlit as st
import ollama
import csv
import io

st.set_page_config(page_title="89 – Content: PDF → Titel & Abstract", page_icon="📄")
st.title("📄 89 – Content: PDF → Titel & Abstract (Ausführlich)")

model = st.text_input("Sprachmodell", "llama3.2")

file = st.file_uploader("CSV-Datei hochladen", type=["csv"])

max_rows = st.slider("Maximale Anzahl Zeilen, die ans Modell geschickt werden", 10, 200, 50, 10)

if st.button("CSV analysieren"):
    if not file:
        st.warning("Bitte zuerst eine CSV-Datei hochladen.")
    else:
        raw = file.read().decode("utf-8", errors="ignore")
        reader = csv.reader(io.StringIO(raw))
        rows = list(reader)
        head = rows[:max_rows]
        csv_preview = "\n".join([",".join(r) for r in head])

        prompt = "Schlage einen passenden Titel und einen kurzen Abstract für das Dokument vor." + "\n\nHier sind die ersten Zeilen der CSV-Datei:\n" + csv_preview

        with st.spinner("Modell wird abgefragt ..."):
            try:
                resp = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])
                st.subheader("Ergebnis")
                st.write(resp["message"]["content"])
            except Exception as e:
                st.error("Fehler bei der CSV-Verarbeitung.")
                st.exception(e)
