import os, streamlit as st

st.set_page_config(page_title="Ollama + Streamlit – Beispiele", page_icon="🤖")

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
            title = raw.split("_",1)[-1].replace("_"," ").title()
            url = f"{grp}_{raw}"
            pages.append(st.Page(full, title=title, icon="📄", url_path=url))
        groups[grp] = pages
    return groups

PAGES = load_pages()
nav = st.navigation(PAGES)
nav.run()
