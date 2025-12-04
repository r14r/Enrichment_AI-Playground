import streamlit as st, ollama, base64

st.set_page_config(page_title="44 – Media: Prompt-Optimierung", page_icon="🖼️")

m = st.text_input("Modell", "llama3.2-vision")
q = st.text_area("Aufgabe", "Formuliere einen optimierten Prompt für ein Text-zu-Bild-Modell, um ein Bild zu erzeugen, das dem hochgeladenen Bild möglichst ähnlich ist.")
f = st.file_uploader("Bild", type=["png", "jpg", "jpeg", "webp"])
if f and st.button("Run"):
    b = base64.b64encode(f.read()).decode("utf-8")
    r = ollama.chat(model=m, messages=[{"role": "user", "content": q, "images": [b]}])
    st.write(r["message"]["content"])
