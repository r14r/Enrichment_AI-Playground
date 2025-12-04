import streamlit as st, ollama, csv, io

st.set_page_config(page_title="92 – Data: CSV-Anomalien", page_icon="📊")

m = st.text_input("Modell", "llama3.2")
f = st.file_uploader("CSV", type=["csv"])
if f and st.button("Run"):
    raw = f.read().decode("utf-8", errors="ignore")
    rows = list(csv.reader(io.StringIO(raw)))
    head = "\n".join([",".join(r) for r in rows[:50]])
    p = "Identifiziere auffällige Werte oder Zeilen, die Anomalien darstellen könnten." + "\n\nCSV-Ausschnitt:\n" + head
    r = ollama.chat(model=m, messages=[{"role": "user", "content": p}])
    st.write(r["message"]["content"])
