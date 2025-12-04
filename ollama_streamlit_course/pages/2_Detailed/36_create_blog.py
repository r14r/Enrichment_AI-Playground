import streamlit as st
import ollama

st.set_page_config(page_title="36 – CreateContent: Blog & Artikel", page_icon="📰")
st.title("📰 36 – CreateContent: Blog & Artikel (Ausführlich)")

model = st.text_input("Sprachmodell", "llama3.2")

thema = st.text_input("Thema", "Mit Streamlit und Ollama lokale KI-Tools bauen")
zielgruppe = st.text_input("Zielgruppe", "Einsteiger mit etwas Python-Erfahrung")
laenge = st.selectbox("Gewünschte Länge", ["Kurz (ca. 500 Wörter)", "Mittel (ca. 1000 Wörter)", "Lang (ca. 1500+ Wörter)"])

outline_first = st.checkbox("Zuerst nur Gliederung erzeugen", value=True)

if st.button("Blog-Inhalt erzeugen"):
    if outline_first:
        prompt = f"""
Erstelle eine detaillierte Gliederung für einen Blogartikel.

Thema: {thema}
Zielgruppe: {zielgruppe}
Länge: {laenge}

Gib nur Überschriften (H1/H2/H3) mit kurzen Stichpunkten aus.
"""
    else:
        prompt = f"""
Schreibe einen Blogartikel.

Thema: {thema}
Zielgruppe: {zielgruppe}
Länge: {laenge}

Struktur:
- Einleitung mit Hook
- Hauptteil in klaren Abschnitten
- Fazit mit Call-to-Action

Schreibe in lockerer, aber professioneller Sprache auf Deutsch.
"""
    with st.spinner("Blog-Inhalt wird erstellt ..."):
        try:
            resp = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])
            st.subheader("Ergebnis")
            st.write(resp["message"]["content"])
        except Exception as e:
            st.error("Fehler beim Erzeugen des Blog-Inhalts.")
            st.exception(e)
