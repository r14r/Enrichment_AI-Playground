import streamlit as st
import ollama

st.set_page_config(page_title="35 – CreateContent: E-Mail-Generator", page_icon="📧")
st.title("📧 35 – CreateContent: E-Mail-Generator (Ausführlich)")

model = st.text_input("Sprachmodell", "llama3.2")

typ = st.selectbox(
    "E-Mail-Typ",
    ["Anfrage", "Bewerbung", "Dankesmail", "Beschwerde"],
)

ansprache = st.selectbox("Anrede-Stil", ["formell", "locker"], index=0)

ziel = st.text_input("Empfänger / Kontext", "Personalabteilung eines IT-Unternehmens")
punkte = st.text_area(
    "Stichpunkte / Inhalt",
    """- Ich interessiere mich für die ausgeschriebene Stelle
- Erfahrung mit Python und Streamlit
- Bitte um Rückmeldung""",
    height=200,
)

if st.button("E-Mail erzeugen"):
    prompt = f"""
Schreibe eine {typ}-E-Mail auf Deutsch im Stil: {ansprache}.
Empfänger / Kontext: {ziel}
Nutze diese Stichpunkte als Grundlage:
{punkte}

Struktur:
- Sinnvolle Betreffzeile
- Anrede
- 2–4 kurze Absätze
- höflicher Abschluss mit Grußformel

Gib nur die E-Mail mit Betreff zurück.
"""
    with st.spinner("E-Mail wird erstellt ..."):
        try:
            resp = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])
            st.subheader("E-Mail")
            st.write(resp["message"]["content"])
        except Exception as e:
            st.error("Fehler beim Erzeugen der E-Mail.")
            st.exception(e)
