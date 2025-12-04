import streamlit as st
import os
from pathlib import Path

st.set_page_config(page_title="Template Generator", page_icon="🛠️")
st.title("🛠️ Template Generator für A/B-Seiten")

st.markdown(
    """
Dieses Tool erzeugt für ein neues Thema zwei Dateien im Ordner `pages/`:

- eine **ausführliche** A-Seite
- eine **minimale** B-Seite

Du kannst den generierten Code anschließend in `app.py` in das `PAGES`-Array eintragen.
"""
)

base_dir = Path(__file__).resolve().parent
pages_dir = base_dir / "pages"

with st.form("template_form"):
    nummer = st.text_input("Nummer (z.B. 11)", value="11")
    titel = st.text_input("Titel (z.B. Dateien hochladen)", value="Dateien hochladen")
    slug = st.text_input("Slug (ohne Leerzeichen, z.B. upload)", value="upload")
    icon = st.text_input("Icon (Emoji, optional)", value="📄")
    submitted = st.form_submit_button("Templates erzeugen")

if submitted:
    if not nummer.strip() or not slug.strip() or not titel.strip():
        st.error("Bitte Nummer, Titel und Slug ausfüllen.")
    else:
        nummer_clean = "".join(c for c in nummer if c.isdigit())
        slug_clean = slug.strip().replace(" ", "_")
        prefixA = f"{nummer_clean}A_{slug_clean}_detailed"
        prefixB = f"{nummer_clean}B_{slug_clean}_minimal"

        fileA = pages_dir / f"{prefixA}.py"
        fileB = pages_dir / f"{prefixB}.py"

        titleA = f"{nummer_clean}A – {titel} (Ausführlich)"
        titleB = f"{nummer_clean}B – {titel} (Minimal)"

        codeA = f"""import streamlit as st

st.set_page_config(page_title="{titleA}", page_icon="{icon}")
st.title("{titleA}")

st.write("Dies ist ein Template für die ausführliche Version von: {titel}")
"""

        codeB = f"""import streamlit as st

st.set_page_config(page_title="{titleB}", page_icon="{icon}")

st.write("Dies ist ein Template für die minimale Version von: {titel}")
"""

        pages_dir.mkdir(parents=True, exist_ok=True)
        fileA.write_text(codeA, encoding="utf-8")
        fileB.write_text(codeB, encoding="utf-8")

        st.success("Templates erzeugt:")
        st.code(str(fileA), language="text")
        st.code(str(fileB), language="text")

        st.markdown("### Eintrag für `PAGES` in `app.py` (kopieren & einfügen)")
        st.code(
            f'st.Page("pages/{prefixA}.py", title="{nummer_clean} – {titel} (Ausführlich)", icon="{icon}", group="Ausführlich"),\n'
            f'st.Page("pages/{prefixB}.py", title="{nummer_clean} – {titel} (Minimal)", icon="{icon}", group="Minimal"),',
            language="python",
        )
