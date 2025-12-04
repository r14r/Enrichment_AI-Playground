#!/usr/bin/env python3
"""Generate Streamlit page stubs from CONTENT.md tasks.

Creates pages under:
- ollama_streamlit_course/pages/5_beginner
- ollama_streamlit_course/pages/6_intermediate
- ollama_streamlit_course/pages/7_advanced

Usage: python3 scripts/generate_pages_from_content.py
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "CONTENT.md"
OUT_BASE = ROOT / "ollama_streamlit_course" / "pages"

SECTIONS = {
    "Beginner": ("## Beginner apps", OUT_BASE / "5_beginner"),
    "Intermediate": ("## Intermediate apps", OUT_BASE / "6_intermediate"),
    "Advanced": ("## Advanced apps", OUT_BASE / "7_advanced"),
}


def slugify(text, maxlen=40):
    s = re.sub(r"[^a-z0-9]+", "_", text.lower())
    s = re.sub(r"_+", "_", s).strip("_")
    return s[:maxlen].strip("_") or "task"


def parse_tasks(md_text, section_header):
    # find section header
    idx = md_text.find(section_header)
    if idx == -1:
        return []
    tail = md_text[idx:]
    # collect lines starting with 'number.' until the next '---' or next section
    tasks = []
    for line in tail.splitlines()[1:]:
        m = re.match(r"\s*(\d+)\.\s+(.*)", line)
        if m:
            tasks.append((int(m.group(1)), m.group(2).strip()))
        # stop if next section header
        if line.startswith("## ") and not line.startswith(section_header):
            break
    return tasks


def make_stub(path: Path, number: int, title: str):
    path.mkdir(parents=True, exist_ok=True)
        slug = slugify(title)
        filename = path / f"{number:02d}_{slug}.py"
        if filename.exists():
            return filename
        # escape double quotes for safe insertion into double-quoted Python string
        title_escaped = title.replace('"', '\\"')
        content = f"""import streamlit as st

    st.set_page_config(page_title="{number} – {title_escaped}", page_icon="📄")

    st.title("{number} – {title_escaped}")

    st.write("This is a stub page for the task: {title_escaped}")
    """
        filename.write_text(content, encoding='utf-8')
        return filename


def main():
    md = CONTENT.read_text(encoding="utf-8")

    created = 0
    for sec_name, (header, out_dir) in SECTIONS.items():
        tasks = parse_tasks(md, header)
        if not tasks:
            print(f"No tasks found for {sec_name}")
            continue
        print(f"Creating {len(tasks)} stubs for {sec_name} in {out_dir}")
        for num, text in tasks:
            make_stub(out_dir, num, text)
            created += 1

    print(f"Created {created} page stubs")


if __name__ == '__main__':
    main()
