import streamlit as st
import ollama

st.set_page_config(page_title="21 – Demo Optionen", page_icon="⚙️")
st.title("⚙️ 21 – Demo: Modell-Optionen (Ausführlich)")

st.write("Spiele mit Temperatur und Kontextlänge, um unterschiedliche Antworten zu erzeugen.")

model = st.text_input("Modell", "llama3.2")
temperature = st.slider("Temperatur (0 = deterministisch, 1+ = kreativ)", 0.0, 2.0, 0.7, 0.1)
num_ctx = st.slider("Kontext-Länge (num_ctx)", 256, 4096, 1024, 256)

prompt = st.text_area(
    "Prompt",
    "Schreibe zwei Sätze darüber, warum lokale LLMs praktisch sind.",
)

if st.button("Antwort generieren"):
    opts = {"temperature": temperature, "num_ctx": num_ctx}
    with st.spinner(f"Frage Modell mit Optionen: {opts}"):
        try:
            resp = ollama.chat(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                options=opts,
            )
            st.subheader("Antwort")
            st.write(resp["message"]["content"])
            st.caption(f"Verwendete Optionen: {opts}")
        except Exception as e:
            st.error("Fehler beim Aufruf mit Optionen.")
            st.exception(e)
