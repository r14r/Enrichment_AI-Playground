"""Fill beginner stub pages with runnable Streamlit examples.
This script rewrites all .py files under ollama_streamlit_course/pages/5_beginner
with a small, self-contained Streamlit app that demonstrates the topic at a lightweight level.

The demos are mock/local implementations (no external LLM calls) chosen by keyword matching
in the filename/title so they run offline.
"""
from pathlib import Path
import re

PAGES_DIR = Path('ollama_streamlit_course/pages/5_beginner')

KEYWORD_MAP = [
    (['chat','conversation','chatbot','simple chat'], 'chat_demo'),
    (['translate','translation','translator'], 'translator_demo'),
    (['summar','summary','summarize'], 'summarizer_demo'),
    (['json','structured','schema'], 'json_demo'),
    (['fewshot','cot','chain','rAG','rag'], 'chain_demo'),
    (['roleplay','role-play'], 'roleplay_demo'),
    (['prompt','template','template'], 'prompt_demo'),
]


def humanize(slug: str) -> str:
    parts = slug.split('_')
    parts = [p.capitalize() for p in parts if p]
    return ' '.join(parts)


def pick_demo(title: str) -> str:
    t = title.lower()
    for keys, demo in KEYWORD_MAP:
        for k in keys:
            if k.lower() in t:
                return demo
    return 'generic_demo'


def make_content(num: int, title: str, demo: str) -> str:
    # Basic safe title
    title_safe = title.replace('"', '\\"')
    header = f"import streamlit as st\n\nst.set_page_config(page_title=\"{num} – {title_safe}\", page_icon=\"📄\")\n\nst.title(\"{num} – {title_safe}\")\n\n"

    if demo == 'chat_demo':
        body = """st.write('Tiny local chat demo (no external LLM). Shows session history, simple rules-based replies, and export.')

if 'history' not in st.session_state:
    st.session_state.history = []

with st.form('chat'):
    user = st.text_input('Your message', key=f'input_{num}')
    persona = st.selectbox('Persona', ['Helpful Assistant','Concise Bot','Enthusiastic Coach'])
    submitted = st.form_submit_button('Send')
    if submitted and user:
        st.session_state.history.append({'who':'User','text':user})
        # simple rule-based reply
        if 'how' in user.lower():
            reply = f"({persona}) Here's a step-by-step hint about {user.split()[0]}..."
        else:
            reply = f"({persona}) I heard: {user[::-1]}"  # playful reversed echo
        st.session_state.history.append({'who':'Bot','text':reply})

for entry in st.session_state.history:
    if entry['who']=='User':
        st.markdown(f"**You:** {entry['text']}")
    else:
        st.info(entry['text'])

if st.button('Export conversation'):
    import json
    st.download_button('Download JSON', json.dumps(st.session_state.history, ensure_ascii=False, indent=2), file_name='conversation.json')
"""
    elif demo == 'translator_demo':
        body = """st.write('Mock translator: demonstrates target languages and token-count estimation. Replace with real translator/LLM calls later.')

txt = st.text_area('Text to translate', height=150)
lang = st.selectbox('Target language', ['Spanish','German','French','Mock-Reverse'])
if st.button('Translate'):
    if not txt.strip():
        st.warning('Enter text to translate')
    else:
        if lang == 'Mock-Reverse':
            out = txt[::-1]
        else:
            out = f"[Mock {lang} translation] " + txt
        st.code(out)
        st.write('Estimated tokens (approx):', max(1, len(out.split())//1))
"""
    elif demo == 'summarizer_demo':
        body = """st.write('Naive summarizer: extractive heuristic—take the top N sentences by very simple scoring (sentence length + keyword overlap).')

text = st.text_area('Text to summarize', height=200)
num = st.slider('Sentences to return', 1, 5, 2)
if st.button('Summarize'):
    if not text.strip():
        st.warning('Paste text to summarize')
    else:
        sents = [s.strip() for s in re.split(r'(?<=[.!?])\\s+', text) if s.strip()]
        # score by length and keyword density
        keywords = set([w.lower() for w in text.split()[:10]])
        scored = []
        for s in sents:
            score = len(s)
            score += sum(1 for w in s.split() if w.lower() in keywords)
            scored.append((score,s))
        top = [s for _,s in sorted(scored, reverse=True)[:num]]
        st.write('\\n'.join(top))
"""
    elif demo == 'json_demo':
        body = """st.write('Parse simple `key:value` lines into JSON, with a small validator for required keys.')

raw = st.text_area('Enter key:value lines (one per line)', placeholder='name: Alice\\nage: 30')
required = st.text_input('Required keys (comma separated)', value='name')
if st.button('Parse'):
    out = {}
    for line in raw.splitlines():
        if ':' in line:
            k,v = line.split(':',1)
            out[k.strip()] = v.strip()
    st.json(out)
    miss = [k for k in [r.strip() for r in required.split(',') if r.strip()] if k not in out]
    if miss:
        st.error('Missing required: ' + ', '.join(miss))
    else:
        st.success('All required keys present')
"""
    elif demo == 'roleplay_demo':
        body = """st.write('Roleplay mock: pick a persona and get a persona-styled reply (canned template).')

persona = st.selectbox('Persona', ['Friendly Tutor','Dev Mentor','Strict Editor'])
inst = st.text_area('Instruction / Task')
if st.button('Act'):
    tone = {
        'Friendly Tutor': 'Sure! Let me explain that step by step...',
        'Dev Mentor': 'Focus on simplicity and tests. Consider modularizing.',
        'Strict Editor': 'Shorten this and fix grammar.'
    }
    reply = f"[{persona}] {tone.get(persona)} {inst[:200]}"
    st.write(reply)
"""
    elif demo == 'chain_demo':
        body = """st.write('Chain-of-thought mock: decompose into subtasks and show intermediate results (local heuristics).')

q = st.text_input('Question')
if st.button('Decompose') and q:
    words = q.split()
    parts = [ ' '.join(words[i:i+max(1,len(words)//3)]) for i in range(0,len(words), max(1,len(words)//3))][:3]
    for i,p in enumerate(parts):
        st.write(f"Step {i+1}: consider '{p}'")
    st.write('Intermediate conclusions:')
    for i,p in enumerate(parts):
        st.write(f"- Conclusion {i+1}: {p[::-1][:40]}")
    st.write('Final (mock) answer: ' + ' '.join(words[:7]))
"""
    else:
        # generic demo: small text toolbox
        body = """st.write('Generic text toolbox: basic operations you can apply locally.')

text = st.text_area('Input text', height=160)
op = st.selectbox('Operation', ['Echo','Reverse','Uppercase','First sentence','Word count'])
if st.button('Run'):
    if op == 'Echo':
        out = text
    elif op == 'Reverse':
        out = text[::-1]
    elif op == 'Uppercase':
        out = text.upper()
    elif op == 'Word count':
        out = f"Words: {len(text.split())}"
    else:
        out = text.split('.')[0]
    st.code(out)
"""

    return header + body


def main():
    files = sorted(PAGES_DIR.glob('*.py'))
    for f in files:
        m = re.match(r"(\d+)_([^.]*)", f.stem)
        if not m:
            continue
        num = int(m.group(1))
        slug = m.group(2)
        title = humanize(slug)
        demo = pick_demo(title)
        content = make_content(num, title, demo)
        f.write_text(content, encoding='utf-8')
    print(f'Rewrote {len(list(files))} beginner stub files in {PAGES_DIR}')


if __name__ == '__main__':
    main()
 