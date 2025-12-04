import streamlit as st
import ollama

st.set_page_config(page_title="09A – Zusammenfassung (Ausführlich)", page_icon="📝")
st.title("📝 09A – Textzusammenfassung (Ausführlich)")

model = st.text_input("Modellname:", value="llama3.2")
uploaded_file = st.file_uploader("Textdatei hochladen (.txt)", type=["txt"])

if uploaded_file is not None:
    raw_text = uploaded_file.read().decode("utf-8", errors="ignore")
    st.subheader("Originaltext (Ausschnitt)")
    st.write(raw_text[:1000] + ("..." if len(raw_text) > 1000 else ""))

    if st.button("Text zusammenfassen"):
        prompt = "Fasse den folgenden Text in 5 Sätzen zusammen.\n\n" + raw_text
        with st.spinner("Fasse zusammen ..."):
            try:
                response = ollama.chat(
                    model=model,
                    messages=[{"role": "user", "content": prompt}],
                )
                st.subheader("Zusammenfassung")
                st.write(response["message"]["content"])
            except Exception as e:
                st.error("Fehler beim Zusammenfassen.")
                st.exception(e)
else:
    st.info("Bitte zuerst eine .txt-Datei hochladen.")

