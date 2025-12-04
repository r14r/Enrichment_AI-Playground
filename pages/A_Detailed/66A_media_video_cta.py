import streamlit as st
import ollama

st.set_page_config(page_title="66 – Media: Call-to-Action Ideen", page_icon="🎥")
st.title("🎥 66 – Media: Call-to-Action Ideen (Ausführlich)")

model = st.text_input("Sprachmodell", "llama3.2")

text = st.text_area("Video-Transkript oder Beschreibung", "", height=260)
extra = st.text_area("Zusatzhinweise (optional)", "", height=100)

if st.button("Ausführen"):
    if not text.strip():
        st.warning("Bitte zuerst Text eingeben.")
    else:
        prompt = "Schlage geeignete Call-to-Action-Ideen vor, die zum Inhalt des Videos passen." + "\n\nText:\n" + text.strip()
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
