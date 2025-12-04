import streamlit as st
import ollama
import base64

st.set_page_config(page_title="48 – Media: Bildstil", page_icon="🖼️")
st.title("🖼️ 48 – Media: Bildstil (Ausführlich)")

st.markdown("Diese Seite demonstriert eine Medienaufgabe im Bereich **Bilder** mit Ollama.")

model = st.text_input("Vision-/Text-Modell", "llama3.2-vision")
task_note = st.text_area("Zusatzhinweise oder Kontext", "", height=80)
question = st.text_area("Aufgabe an das Modell", "Analysiere den visuellen Stil des Bildes (z. B. realistisch, cartoonhaft, minimalistisch) und nenne passende Stilbegriffe.", height=150)

uploaded = st.file_uploader("Bild hochladen", type=["png", "jpg", "jpeg", "webp"])

if uploaded is not None:
    st.image(uploaded, caption="Hochgeladenes Bild", use_column_width=True)

if st.button("Analyse starten"):
    if uploaded is None:
        st.warning("Bitte zuerst ein Bild hochladen.")
    else:
        img_bytes = uploaded.read()
        b64 = base64.b64encode(img_bytes).decode("utf-8")
        content = question
        if task_note.strip():
            content += "\n\nZusatz: " + task_note.strip()
        messages = [{"role": "user", "content": content, "images": [b64]}]
        with st.spinner("Modell wird abgefragt ..."):
            try:
                resp = ollama.chat(model=model, messages=messages)
                st.subheader("Antwort")
                st.write(resp["message"]["content"])
            except Exception as e:
                st.error("Fehler bei der Bildanalyse.")
                st.exception(e)
