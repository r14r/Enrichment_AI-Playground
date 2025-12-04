import streamlit as st
import ollama

st.set_page_config(page_title="32 – Media: Bild-Prompt-Generator", page_icon="🎨")
st.title("🎨 32 – Media: Bild-Prompt-Generator (Ausführlich)")

st.markdown(
    "Hier erzeugst du mit einem LLM einen **Prompt für ein Bildgenerierungs-Tool** "
    "(z. B. Stable Diffusion, ComfyUI, Flux)."
)

model = st.text_input("Text-Modell", "llama3.2")
idee = st.text_area("Motiv-Idee", "Ein futuristischer Stadtpark bei Nacht")
stil = st.text_input("Stil / Look", "ultra-realistisch, Kino-Licht, 8k")
zusatz = st.text_area("Optionale Zusatzinfos (Kamera, Farbstimmung, ...)", "", height=80)

if st.button("Bild-Prompt erzeugen"):
    base_prompt = f"""
Erzeuge einen kompakten, aber detailreichen Prompt für ein Text-zu-Bild-Modell.
Motiv: {idee}
Stil: {stil}
Zusatz: {zusatz}

Formatiere den Prompt in einer Zeile ohne Erklärungen.
"""
    with st.spinner("Prompt wird generiert ..."):
        try:
            resp = ollama.chat(
                model=model,
                messages=[{"role": "user", "content": base_prompt}],
            )
            prompt = resp["message"]["content"].strip()
            st.subheader("Bild-Prompt")
            st.code(prompt, language="text")
        except Exception as e:
            st.error("Fehler beim Erzeugen des Bild-Prompts.")
            st.exception(e)
