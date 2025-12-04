import streamlit as st, ollama

st.set_page_config(page_title="008 – Basics: Prompt-Playground", page_icon="🎯")
st.title("008 – Basics: Prompt-Playground (Ausführlich)")

m = st.text_input("Modell", "llama3.2")
system = st.text_area("System-Prompt", "Du bist ein hilfsbereiter KI-Assistent.", height=100)
user = st.text_area("User-Prompt", "Gib mir 3 Ideen für eine kleine KI-App.", height=200)
temp = st.slider("Temperatur", 0.0, 1.5, 0.7, 0.1)

if st.button("Ausführen"):
    msgs = [
        {"role":"system","content":system},
        {"role":"user","content":user},
    ]
    try:
        r = ollama.chat(model=m, messages=msgs, options={"temperature":temp})
        st.subheader("Antwort")
        st.write(r["message"]["content"])
    except Exception as e:
        st.error("Fehler im Playground.")
        st.exception(e)
