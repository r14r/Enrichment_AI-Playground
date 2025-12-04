import os
import streamlit as st

from lib.helper_streamlit import load_pages

st.set_page_config(page_title="Ollama + Streamlit – Kursnavigation", page_icon="🤖")

FOLDER = os.path.join(os.path.dirname(__file__), "pages")

ICONS = {
    "01_install": "✅",
    "02_status": "🩺",
    "03_models": "📦",
    "04_pull": "⬇️",
    "05_prompt": "💬",
    "06_chat": "💭",
    "07_stream": "📡",
    "08_playground": "🎯",
    "09_summary": "📝",
    "10_dashboard": "📊",
    "20_quickchat": "💡",
    "21_options": "⚙️",
    "22_system_styles": "🧩",
    "23_json_output": "🧾",
    "24_fewshot": "📚",
    "25_cot_instruction": "🧠",
    "26_roleplay": "🎭",
    "27_code_helper": "💻",
    "28_error_explainer": "⚠️",
    "29_translator": "🌐",
    "30_prompt_template": "📋",
    "31_media_image_analyze": "🖼️",
    "32_media_image_promptgen": "🎨",
    "33_content_correct": "✏️",
    "34_content_summarize": "📑",
    "35_create_email": "📧",
    "36_create_blog": "📰",
}

PAGES = load_pages(FOLDER, ICONS)
PAGES["Tools"] = [
    st.Page(
        "template_generator.py",
        title="Template Generator",
        icon="🛠️",
        url_path="tools_template_generator",
    )
]

nav = st.navigation(PAGES)
nav.run()
