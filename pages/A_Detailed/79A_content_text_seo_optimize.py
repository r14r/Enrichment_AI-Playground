import streamlit as st
import ollama

st.set_page_config(page_title="79 – Content: SEO-Optimierung", page_icon="✍️")
st.title("✍️ 79 – Content: SEO-Optimierung (Ausführlich)")

model = st.text_input("Sprachmodell", "llama3.2")

text = st.text_area("Eingabetext", "", height=260)
extra = st.text_area("Zusatzhinweise (optional)", "", height=100)

if st.button("Ausführen"):
    if not text.strip():
        st.warning("Bitte zuerst Text eingeben.")
    else:
        prompt = "Optimiere den Text für SEO, indem du Keywords sinnvoll einbaust und den Aufbau verbesserst." + "\n\nText:\n" + text.strip()
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
