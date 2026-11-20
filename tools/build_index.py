"""Rebuild knowledge/index.md from the notes on disk.

Run after any change to knowledge/: python tools/build_index.py
Each note contributes one line: its file, its first heading, and its Status line if it has one.
The index is what a new session reads first, so keep headings short and keep a Status line in every site note.
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
K = os.path.join(ROOT, 'knowledge')
SECTIONS = [('councils', 'Councils'), ('sites', 'Sites (one per title or SHELAA ref)'),
            ('agents', 'Agents, promoters, developers, consultants')]


def first_heading(text):
    for line in text.splitlines():
        if line.startswith('#'):
            return line.lstrip('#').strip()
    return ''


def status(text):
    m = re.search(r'^Status:\s*(.+)$', text, re.M)
    return m.group(1).strip() if m else ''


def council_of(text):
    m = re.search(r'^Council:\s*([^\n]+?)(\s{2,}|$)', text, re.M)
    return m.group(1).strip() if m else ''


out = ['# Index', '',
       'One line per note. Read a note only when its line matches the council, title, agent or step in hand.',
       'Rebuild with `python tools/build_index.py` after editing anything under knowledge/.', '']
for folder, title in SECTIONS:
    d = os.path.join(K, folder)
    if not os.path.isdir(d):
        continue
    out.append('## ' + title)
    rows = []
    names = sorted(f for f in os.listdir(d) if f.endswith('.md'))
    work = re.compile(r'^(.+?)-(precedent|assessment|history|documents|market|owners|appraisal-inputs|appraisal-record)\.md$')
    extras = {}
    for fn in names:
        m = work.match(fn)
        if m and folder == 'sites':
            extras.setdefault(m.group(1), []).append(m.group(2))
    for fn in names:
        if folder == 'sites' and work.match(fn):
            continue
        t = open(os.path.join(d, fn), encoding='utf8').read()
        h = first_heading(t)
        extra = []
        if folder == 'sites':
            c = council_of(t)
            s = status(t)
            if c:
                extra.append(c)
            if s:
                extra.append('status: ' + s)
        stem = fn[:-3]
        if folder == 'sites' and extras.get(stem):
            extra.append('working files: ' + ', '.join(extras[stem]))
        rows.append('- `%s/%s` %s%s' % (folder, fn, h, (' (' + '; '.join(extra) + ')') if extra else ''))
    out += rows + ['']
for extra in ('contacts/log.md', 'open-items.md', 'learned-checks.md', 'timeline.md'):
    if os.path.exists(os.path.join(K, extra)):
        out.append('- `%s`' % extra)
open(os.path.join(K, 'index.md'), 'w', encoding='utf8').write('\n'.join(out) + '\n')
print('index: %d lines' % len(out))
