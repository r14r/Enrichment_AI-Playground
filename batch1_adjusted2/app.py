import os
import streamlit as st

st.set_page_config(page_title="Ollama + Streamlit – Batch 1 (01–30)", page_icon="🤖")

st.title("🤖 Ollama + Streamlit – Beispiele 01–30")
st.markdown(
    "Dieser Batch enthält die Grundlagen (01–10) und Prompting-Beispiele (11–30).\n\n"
    "- **Ausführlich**: Mit Erklärungen, mehr UI und Kurs-Charakter\n"
    "- **Minimal**: Nur der essenzielle Code – ideal als Referenz"
)

def load_pages(base="pages"):
    groups = {}
    if not os.path.isdir(base):
        return groups
    for grp in sorted(os.listdir(base)):
        gpath = os.path.join(base, grp)
        if not os.path.isdir(gpath):
            continue
        pages = []
        for f in sorted(os.listdir(gpath)):
            if not f.endswith(".py"):
                continue
            full = os.path.join(gpath, f).replace("\\","/")
            raw = os.path.splitext(f)[0]
            title_part = raw.split("_", 1)[1] if "_" in raw else raw
            title = title_part.replace("_", " ").title()
            url = f"{grp}_{raw}"
            pages.append(
                st.Page(
                    full,
                    title=title,
                    icon="📄",
                    url_path=url,
                )
            )
        groups[grp] = pages
    return groups

PAGES = load_pages("pages")

nav = st.navigation(PAGES)
nav.run()
