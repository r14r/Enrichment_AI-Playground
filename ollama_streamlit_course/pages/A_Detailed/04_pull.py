import streamlit as st
import ollama

st.set_page_config(page_title="04A – Modell herunterladen (Ausführlich)", page_icon="⬇️")
st.title("⬇️ 04A – Modell herunterladen (Ausführlich)")

default_models = ["llama3.2", "llama3", "phi3", "mistral", "qwen2.5"]
model_choice = st.selectbox("Modell auswählen", default_models, index=0)
custom_name = st.text_input("Oder eigener Modellname:")

model_to_pull = custom_name.strip() or model_choice

if st.button(f"Modell `{model_to_pull}` herunterladen"):
    with st.spinner(f"Lade Modell `{model_to_pull}` ..."):
        try:
            progress_box = st.empty()
            for progress in ollama.pull(model_to_pull, stream=True):
                status = progress.get("status", "")
                details = progress.get("digest", "") or progress.get("error", "") or ""
                progress_box.write(f"{status} {details}")
            st.success(f"Modell `{model_to_pull}` wurde heruntergeladen (sofern keine Fehler auftraten).")
        except Exception as e:
            st.error("Fehler beim Herunterladen des Modells.")
            st.exception(e)

