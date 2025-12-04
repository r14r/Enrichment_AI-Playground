import streamlit as st
import ollama

st.set_page_config(page_title="33 – Content: Text korrigieren", page_icon="✏️")
st.title("✏️ 33 – Content: Text korrigieren (Ausführlich)")

st.markdown(
    "Nutze das Modell, um Rechtschreibung, Grammatik und Stil eines Textes zu verbessern."
)

model = st.text_input("Sprachmodell", "llama3.2")
lang = st.selectbox("Sprache des Textes", ["Deutsch", "Englisch"], index=0)

text = st.text_area(
    "Originaltext",
    "das ist ein kurzer text der einige fehler hat und nich sehr gut klingt",
    height=200,
)

modus = st.radio(
    "Ausgabe",
    ["Nur korrigierter Text", "Korrigierter Text + Erklärungen"],
    index=0,
)

if st.button("Text korrigieren"):
    if not text.strip():
        st.warning("Bitte zuerst einen Text eingeben.")
    else:
        instruction = (
            "Korrigiere Rechtschreibung, Grammatik und Stil. "
            "Verbessere die Lesbarkeit, aber verändere den Inhalt nicht."
        )
        if modus == "Nur korrigierter Text":
            instruction += " Gib ausschließlich den korrigierten Text zurück, ohne Erklärungen."
        else:
            instruction += " Gib zuerst den korrigierten Text und danach eine kurze Liste der wichtigsten Änderungen."

        prompt = f"""{instruction}

Sprache: {lang}

Text:
{text}"""

        with st.spinner("Text wird korrigiert ..."):
            try:
                resp = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])
                st.subheader("Ergebnis")
                st.write(resp["message"]["content"])
            except Exception as e:
                st.error("Fehler bei der Textkorrektur.")
                st.exception(e)
