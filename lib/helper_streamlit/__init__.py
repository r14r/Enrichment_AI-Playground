import os
import streamlit as st

def load_pages(base_path="pages", icons=None):
    groups = {}

    for group_name in sorted(os.listdir(base_path)):
        group_path = os.path.join(base_path, group_name)
        if not os.path.isdir(group_path):
            continue

        pages = []

        for file in sorted(os.listdir(group_path)):
            if not file.endswith(".py"):
                continue

            # skip legacy demo filenames that still contain A_demo / B_demo
            if "A_demo" in file or "B_demo" in file:
                continue

            file_path = os.path.join(group_path, file).replace("\\", "/")

            # Remove extension
            raw = os.path.splitext(file)[0]

            # Title: split prefix “01A_…” → take second part
            if "_" in raw:
                title = raw.split("_", 1)[1].replace("_", " ").title()
            else:
                title = raw.replace("_", " ").title()

            # URL path: <group>_<basename>
            url_path = f"{group_name}_{raw}"

            if icons and raw in icons:
                icon = icons.get(raw, "📄")
            else:
                icon="📄"
            
            pages.append(
                st.Page(
                    file_path,
                    title=title,
                    icon=icon,
                    url_path=url_path,
                )
            )

        groups[group_name] = pages

    return groups
