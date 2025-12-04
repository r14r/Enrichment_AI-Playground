import streamlit as st, ollama

st.set_page_config(page_title="002 – Basics: Statusübersicht", page_icon="📘")
st.title("002 – Basics: Statusübersicht (Ausführlich)")

st.markdown("**Lernziel:** Beschreibe, wie du herausfindest, welche Modelle lokal installiert sind.")

model = st.text_input("Modell", "llama3.2")
txt = st.text_area("Eingabe / Notizen / Beschreibung", "", height=260)
extra = st.text_area("Zusatz (optional)", "", height=120)

if st.button("Ausführen"):
    if not txt.strip():
        st.warning("Bitte zuerst Text eingeben.")
    else:
        prompt = "Beschreibe, wie du herausfindest, welche Modelle lokal installiert sind." + "\n\nText:\n" + txt.strip()
        if extra.strip():
            prompt += "\n\nZusatz:\n" + extra.strip()
        with st.spinner("Modell wird abgefragt ..."):
            try:
                resp = ollama.chat(model=model, messages=[{"role":"user","content":prompt}])
                st.subheader("Ergebnis")
                st.write(resp["message"]["content"])
            except Exception as e:
                st.error("Fehler bei der Verarbeitung.")
                st.exception(e)
