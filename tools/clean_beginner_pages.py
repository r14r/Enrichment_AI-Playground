"""Clean beginner page files: remove markdown code fences and ensure `import re` present when needed."""
from pathlib import Path
import re

PAGES = Path('ollama_streamlit_course/pages/5_beginner')
count=0
for p in sorted(PAGES.glob('*.py')):
    txt = p.read_text(encoding='utf-8')
    orig = txt
    # If file contains markdown code fence, extract inner content
    if '```' in txt:
        # find first fence and last fence
        first = txt.find('```')
        last = txt.rfind('```')
        if first != -1 and last != -1 and last>first:
            inner = txt[first+3:last]
            # strip leading language marker like 'python' on first line
            if inner.lstrip().startswith('python'):
                inner = inner.lstrip()[6:]
            txt = inner.strip('\n') + '\n'
    # ensure import streamlit at top
    if not re.search(r'^import\s+streamlit', txt, flags=re.M):
        txt = 'import streamlit as st\n' + txt
    # ensure import re if regex used
    if 're.' in txt and not re.search(r'^import\s+re', txt, flags=re.M):
        # insert after import streamlit
        txt = txt.replace('import streamlit as st\n', 'import streamlit as st\nimport re\n', 1)
    if txt!=orig:
        p.write_text(txt, encoding='utf-8')
        count+=1
print(f'Cleaned {count} files under {PAGES}')
