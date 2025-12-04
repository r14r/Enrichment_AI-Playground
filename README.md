# Ollama + Streamlit – Kurs mit Navigation & Template Generator

Dieses Projekt enthält:

- `app.py` – zentrale Navigation mit `st.navigation(PAGES)` und Gruppen:
  - **Ausführlich**
  - **Minimal**
  - **Tools**
- 10 Themen, jeweils als A/B-Seiten:
  - A = ausführlich
  - B = minimal
- `template_generator.py` – Streamlit-Tool zum Erzeugen neuer A/B-Templates im Ordner `pages/`.

## Installation

```bash
pip install -r requirements.txt

## Start

```bash
streamlit run app.py

Voraussetzung: Lokale Ollama-Installation und laufender Dienst:

```bash
ollama serve
