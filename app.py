import streamlit as st

st.set_page_config(page_title="Ollama + Streamlit – Kursnavigation", page_icon="🤖")

PAGES = {
    "Ausführlich": [
        st.Page("pages/A_Detailed/01A_install_detailed.py", title="01 – Installationscheck", icon="✅"),
        st.Page("pages/A_Detailed/02A_status_detailed.py", title="02 – Status", icon="🩺"),
        st.Page("pages/A_Detailed/03A_models_detailed.py", title="03 – Modelle anzeigen", icon="📦"),
        st.Page("pages/A_Detailed/04A_pull_detailed.py", title="04 – Modell herunterladen", icon="⬇️"),
        st.Page("pages/A_Detailed/05A_prompt_detailed.py", title="05 – Prompt", icon="💬"),
        st.Page("pages/A_Detailed/06A_chat_detailed.py", title="06 – Chat mit Verlauf", icon="💭"),
        st.Page("pages/A_Detailed/07A_stream_detailed.py", title="07 – Streaming", icon="📡"),
        st.Page("pages/A_Detailed/08A_playground_detailed.py", title="08 – Playground", icon="🎯"),
        st.Page("pages/A_Detailed/09A_summary_detailed.py", title="09 – Zusammenfassung", icon="📝"),
        st.Page("pages/A_Detailed/10A_dashboard_detailed.py", title="10 – Dashboard", icon="📊"),
        st.Page("pages/A_Detailed/20A_demo_quickchat.py", title="20 – Demo Quick-Chat", icon="💡"),
        st.Page("pages/A_Detailed/21A_demo_options.py", title="21 – Demo Optionen", icon="⚙️"),
        st.Page("pages/A_Detailed/22A_demo_system_styles.py", title="22 – System-Prompt Stile", icon="🧩"),
        st.Page("pages/A_Detailed/23A_demo_json_output.py", title="23 – JSON-Ausgabe", icon="🧾"),
        st.Page("pages/A_Detailed/24A_demo_fewshot.py", title="24 – Few-Shot Prompting", icon="📚"),
        st.Page("pages/A_Detailed/25A_demo_cot_instruction.py", title="25 – Denkweise erklären", icon="🧠"),
        st.Page("pages/A_Detailed/26A_demo_roleplay.py", title="26 – Rollen & Personas", icon="🎭"),
        st.Page("pages/A_Detailed/27A_demo_code_helper.py", title="27 – Code-Helfer", icon="💻"),
        st.Page("pages/A_Detailed/28A_demo_error_explainer.py", title="28 – Fehler-Erklärer", icon="⚠️"),
        st.Page("pages/A_Detailed/29A_demo_translator.py", title="29 – Übersetzer", icon="🌐"),
        st.Page("pages/A_Detailed/30A_demo_prompt_template.py", title="30 – Prompt-Templates", icon="📋"),
    ],
    "Minimal": [
        st.Page("pages/B_Minimal/01B_install_minimal.py", title="01 – Installationscheck", icon="✅"),
        st.Page("pages/B_Minimal/02B_status_minimal.py", title="02 – Status", icon="🩺"),
        st.Page("pages/B_Minimal/03B_models_minimal.py", title="03 – Modelle anzeigen", icon="📦"),
        st.Page("pages/B_Minimal/04B_pull_minimal.py", title="04 – Modell herunterladen", icon="⬇️"),
        st.Page("pages/B_Minimal/05B_prompt_minimal.py", title="05 – Prompt", icon="💬"),
        st.Page("pages/B_Minimal/06B_chat_minimal.py", title="06 – Chat mit Verlauf", icon="💭"),
        st.Page("pages/B_Minimal/07B_stream_minimal.py", title="07 – Streaming", icon="📡"),
        st.Page("pages/B_Minimal/08B_playground_minimal.py", title="08 – Playground", icon="🎯"),
        st.Page("pages/B_Minimal/09B_summary_minimal.py", title="09 – Zusammenfassung", icon="📝"),
        st.Page("pages/B_Minimal/10B_dashboard_minimal.py", title="10 – Dashboard", icon="📊"),
        st.Page("pages/B_Minimal/20B_demo_quickchat_min.py", title="20 – Demo Quick-Chat", icon="💡"),
        st.Page("pages/B_Minimal/21B_demo_options_min.py", title="21 – Demo Optionen", icon="⚙️"),
        st.Page("pages/B_Minimal/22B_demo_system_styles_min.py", title="22 – System-Prompt Stile", icon="🧩"),
        st.Page("pages/B_Minimal/23B_demo_json_output_min.py", title="23 – JSON-Ausgabe", icon="🧾"),
        st.Page("pages/B_Minimal/24B_demo_fewshot_min.py", title="24 – Few-Shot Prompting", icon="📚"),
        st.Page("pages/B_Minimal/25B_demo_cot_instruction_min.py", title="25 – Denkweise erklären", icon="🧠"),
        st.Page("pages/B_Minimal/26B_demo_roleplay_min.py", title="26 – Rollen & Personas", icon="🎭"),
        st.Page("pages/B_Minimal/27B_demo_code_helper_min.py", title="27 – Code-Helfer", icon="💻"),
        st.Page("pages/B_Minimal/28B_demo_error_explainer_min.py", title="28 – Fehler-Erklärer", icon="⚠️"),
        st.Page("pages/B_Minimal/29B_demo_translator_min.py", title="29 – Übersetzer", icon="🌐"),
        st.Page("pages/B_Minimal/30B_demo_prompt_template_min.py", title="30 – Prompt-Templates", icon="📋"),
    ],
    "Tools": [
        st.Page("template_generator.py", title="Template Generator", icon="🛠️"),
    ],
}

nav = st.navigation(PAGES)
nav.run()
