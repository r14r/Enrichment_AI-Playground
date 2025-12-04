import streamlit as st
import ollama

st.set_page_config(page_title="28 – Fehler-Erklärer", page_icon="⚠️")
st.title("⚠️ 28 – Demo: Fehler-Erklärer (Ausführlich)")

model = st.text_input("Modell", "llama3.2")
error_text = st.text_area(
    "Fehlermeldung",
    "Traceback (most recent call last):\n  File 'main.py', line 1, in <module>\n    import pandas as pd\nModuleNotFoundError: No module named 'pandas'",
    height=200,
)

if st.button("Fehler erklären lassen"):
    prompt = (
        "Erkläre diesen Fehler in einfachen Worten und zeige, wie man ihn beheben kann:\n\n"
        + error_text
    )
    with st.spinner("Frage Modell ..."):
        try:
            resp = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])
            st.subheader("Erklärung")
            st.write(resp["message"]["content"])
        except Exception as e:
            st.error("Fehler bei der Fehler-Erklärer-Demo.")
            st.exception(e)
