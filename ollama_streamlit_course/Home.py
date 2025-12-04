import streamlit as st

st.set_page_config(page_title="Ollama + Streamlit – Kursnavigation", page_icon="🤖")

PAGES = {
    "Ausführlich": [
        st.Page("pages/A_Detailed/01_install.py", title="01 – Installationscheck", icon="✅", url_path="A01"),
        st.Page("pages/A_Detailed/02_status.py", title="02 – Status", icon="🩺", url_path="A02"),
        st.Page("pages/A_Detailed/03_models.py", title="03 – Modelle anzeigen", icon="📦", url_path="A03"),
        st.Page("pages/A_Detailed/04_pull.py", title="04 – Modell herunterladen", icon="⬇️", url_path="A04"),
        st.Page("pages/A_Detailed/05_prompt.py", title="05 – Prompt", icon="💬", url_path="A05"),
        st.Page("pages/A_Detailed/06_chat.py", title="06 – Chat mit Verlauf", icon="💭", url_path="A06"),
        st.Page("pages/A_Detailed/07_stream.py", title="07 – Streaming", icon="📡", url_path="A07"),
        st.Page("pages/A_Detailed/08_playground.py", title="08 – Playground", icon="🎯", url_path="A08"),
        st.Page("pages/A_Detailed/09_summary.py", title="09 – Zusammenfassung", icon="📝", url_path="A09"),
        st.Page("pages/A_Detailed/10_dashboard.py", title="10 – Dashboard", icon="📊", url_path="A10"),
        st.Page("pages/A_Detailed/20A_demo_quickchat.py", title="20 – Demo Quickchat", icon="🧪", url_path="A20"),
        st.Page("pages/A_Detailed/21A_demo_options.py", title="21 – Demo Options", icon="⚙️", url_path="A21"),
        st.Page("pages/A_Detailed/22A_demo_system_styles.py", title="22 – System Styles", icon="🎨", url_path="A22"),
        st.Page("pages/A_Detailed/23A_demo_json_output.py", title="23 – JSON Output Demo", icon="🗂️", url_path="A23"),
        st.Page("pages/A_Detailed/24A_demo_fewshot.py", title="24 – Few-shot Demo", icon="✳️", url_path="A24"),
        st.Page("pages/A_Detailed/25A_demo_cot_instruction.py", title="25 – CoT Instruction", icon="🧭", url_path="A25"),
        st.Page("pages/A_Detailed/26A_demo_roleplay.py", title="26 – Roleplay Demo", icon="🎭", url_path="A26"),
        st.Page("pages/A_Detailed/27A_demo_code_helper.py", title="27 – Code Helper", icon="💻", url_path="A27"),
        st.Page("pages/A_Detailed/28A_demo_error_explainer.py", title="28 – Error Explainer", icon="🛠️", url_path="A28"),
        st.Page("pages/A_Detailed/29A_demo_translator.py", title="29 – Translator Demo", icon="🌐", url_path="A29"),
        st.Page("pages/A_Detailed/30A_demo_prompt_template.py", title="30 – Prompt Template", icon="📑", url_path="A30"),
    ],
    "Minimal": [
        st.Page("pages/B_Minimal/01_install.py", title="01 – Installationscheck", icon="✅", url_path="B01"),
        st.Page("pages/B_Minimal/02_status.py", title="02 – Status", icon="🩺", url_path="B02"),
        st.Page("pages/B_Minimal/03_models.py", title="03 – Modelle anzeigen", icon="📦", url_path="B03"),
        st.Page("pages/B_Minimal/04_pull.py", title="04 – Modell herunterladen", icon="⬇️", url_path="B04"),
        st.Page("pages/B_Minimal/05_prompt.py", title="05 – Prompt", icon="💬", url_path="B05"),
        st.Page("pages/B_Minimal/06_chat.py", title="06 – Chat mit Verlauf", icon="💭", url_path="B06"),
        st.Page("pages/B_Minimal/07_stream.py", title="07 – Streaming", icon="📡", url_path="B07"),
        st.Page("pages/B_Minimal/08_playground.py", title="08 – Playground", icon="🎯", url_path="B08"),
        st.Page("pages/B_Minimal/09_summary.py", title="09 – Zusammenfassung", icon="📝", url_path="B09"),
        st.Page("pages/B_Minimal/10_dashboard.py", title="10 – Dashboard", icon="📊", url_path="B10"),
        st.Page("pages/B_Minimal/20B_demo_quickchat_min.py", title="20 – Demo Quickchat (Min)", icon="🧪", url_path="B20"),
        st.Page("pages/B_Minimal/21B_demo_options_min.py", title="21 – Demo Options (Min)", icon="⚙️", url_path="B21"),
        st.Page("pages/B_Minimal/22B_demo_system_styles_min.py", title="22 – System Styles (Min)", icon="🎨", url_path="B22"),
        st.Page("pages/B_Minimal/23B_demo_json_output_min.py", title="23 – JSON Output Demo (Min)", icon="🗂️", url_path="B23"),
        st.Page("pages/B_Minimal/24B_demo_fewshot_min.py", title="24 – Few-shot Demo (Min)", icon="✳️", url_path="B24"),
        st.Page("pages/B_Minimal/25B_demo_cot_instruction_min.py", title="25 – CoT Instruction (Min)", icon="🧭", url_path="B25"),
        st.Page("pages/B_Minimal/26B_demo_roleplay_min.py", title="26 – Roleplay Demo (Min)", icon="🎭", url_path="B26"),
        st.Page("pages/B_Minimal/27B_demo_code_helper_min.py", title="27 – Code Helper (Min)", icon="💻", url_path="B27"),
        st.Page("pages/B_Minimal/28B_demo_error_explainer_min.py", title="28 – Error Explainer (Min)", icon="🛠️", url_path="B28"),
        st.Page("pages/B_Minimal/29B_demo_translator_min.py", title="29 – Translator Demo (Min)", icon="🌐", url_path="B29"),
        st.Page("pages/B_Minimal/30B_demo_prompt_template_min.py", title="30 – Prompt Template (Min)", icon="📑", url_path="B30"),
    ],
    "Tools": [
    st.Page("template_generator.py", title="Template Generator", icon="🛠️", url_path="tools_template_generator"),
    ]
}

nav = st.navigation(PAGES)
nav.run()
