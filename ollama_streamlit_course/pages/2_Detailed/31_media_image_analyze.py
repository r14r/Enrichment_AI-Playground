import streamlit as st
import ollama
import base64

st.set_page_config(page_title="31 – Media: Bildanalyse", page_icon="🖼️")
st.title("🖼️ 31 – Media: Bildanalyse (Ausführlich)")

st.markdown(
    "Lade ein Bild hoch und lass ein Vision-Modell (z. B. `llama3.2-vision` oder `llava`) "
    "eine Beschreibung oder Analyse erstellen."
)

model = st.text_input("Vision-Modell", "llama3.2-vision")
question = st.text_area("Frage an das Bild", "Was ist auf diesem Bild zu sehen?")

uploaded = st.file_uploader("Bild hochladen", type=["png", "jpg", "jpeg", "webp"])

if uploaded is not None:
    st.image(uploaded, caption="Hochgeladenes Bild", use_column_width=True)

if st.button("Bild analysieren"):
    if uploaded is None:
        st.warning("Bitte zuerst ein Bild hochladen.")
    else:
        img_bytes = uploaded.read()
        b64 = base64.b64encode(img_bytes).decode("utf-8")
        messages = [
            {
                "role": "user",
                "content": question,
                "images": [b64],
            }
        ]
        with st.spinner("Vision-Modell wird abgefragt ..."):
            try:
                resp = ollama.chat(model=model, messages=messages)
                st.subheader("Analyse")
                st.write(resp["message"]["content"])
            except Exception as e:
                st.error("Fehler bei der Bildanalyse.")
                st.exception(e)
