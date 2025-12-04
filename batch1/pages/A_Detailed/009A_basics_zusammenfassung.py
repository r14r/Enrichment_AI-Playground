import streamlit as st, ollama

st.set_page_config(page_title="009 – Basics: Zusammenfassung", page_icon="📝")
st.title("009 – Basics: Zusammenfassung (Ausführlich)")

m = st.text_input("Modell", "llama3.2")
t = st.text_area("Langer Text", "Füge hier einen längeren Text ein.", height=260)

if st.button("Zusammenfassen"):
    if not t.strip():
        st.warning("Bitte Text eingeben.")
    else:
        p = "Fasse den folgenden Text in 5 Sätzen zusammen:\n\n" + t
        try:
            r = ollama.chat(model=m, messages=[{"role":"user","content":p}])
            st.subheader("Zusammenfassung")
            st.write(r["message"]["content"])
        except Exception as e:
            st.error("Fehler bei der Zusammenfassung.")
            st.exception(e)
