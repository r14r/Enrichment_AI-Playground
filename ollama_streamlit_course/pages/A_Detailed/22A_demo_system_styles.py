import streamlit as st
import ollama

st.set_page_config(page_title="22 – System-Prompt Stile", page_icon="🧩")
st.title("🧩 22 – Demo: System-Prompt Stile (Ausführlich)")

model = st.text_input("Modell", "llama3.2")
style = st.selectbox(
    "Stil wählen",
    ["Lehrer", "Coach", "Experte", "Kindgerecht"],
)

user_msg = st.text_input("Frage", "Erkläre mir kurz, was ein Prompt ist.")

system_map = {
    "Lehrer": "Du bist ein geduldiger Lehrer und erklärst klar und strukturiert.",
    "Coach": "Du bist ein motivierender Coach und sprichst den Nutzer direkt an.",
    "Experte": "Du bist Fachexperte und antwortest präzise und knapp.",
    "Kindgerecht": "Du erklärst alle Dinge einfach, als würdest du mit einem Kind sprechen.",
}
system_prompt = system_map[style]

if st.button("Antwort generieren"):
    msgs = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_msg},
    ]
    with st.spinner("Frage Modell ..."):
        try:
            resp = ollama.chat(model=model, messages=msgs)
            st.subheader("Antwort")
            st.write(resp["message"]["content"])
            st.caption(f"System-Prompt: {system_prompt}")
        except Exception as e:
            st.error("Fehler bei der System-Prompt-Demo.")
            st.exception(e)
