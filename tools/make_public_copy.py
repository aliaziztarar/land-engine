"""Build the shareable copy of the engine, with nothing personal in it.

Usage: python tools/make_public_copy.py <output folder>
(The output folder can be a GitHub clone: its .git folder is kept, everything else is replaced.)

Copies CLAUDE.md, README.md, .claude/ (settings, worker, skills), tools/, and the empty
knowledge/, sources/ and profile/ scaffolding. Leaves out profile/ contents (except the
example), every note under knowledge/, every text under sources/, and anything listed in
profile/private-terms.txt. Then scans every copied file for: the words in
profile/private-terms.txt, the values in profile/profile.json, and every Land Registry title
number found in the private knowledge notes. If anything is found, the copy is deleted and the
script stops with the file and line, so nothing personal can leave by accident.
"""
import json, os, re, shutil, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KEEP_TOP = ['CLAUDE.md', 'README.md', 'GUIDE.md', '.claude', 'tools']
PUBLIC_GITIGNORE = '''# Your own details and notes stay on your computer and are never uploaded.
profile/*
!profile/README.md
!profile/profile.example.json
!profile/profile.example.md
knowledge/**/*.md
!knowledge/README.md
sources/**
!sources/README.md
__pycache__/
*.tmp
.claude/settings.local.json
'''
SCAFFOLD = {
    'knowledge/README.md', 'knowledge/learned-checks.md', 'knowledge/index.md',
    'knowledge/contacts/log.md', 'knowledge/open-items.md',
    'sources/README.md', 'profile/README.md', 'profile/profile.example.json',
    'profile/profile.example.md',
}
TEXT_EXT = ('.md', '.py', '.json', '.txt', '.sh', '.xml', '.gitignore')


def private_words():
    words = set()
    f = os.path.join(ROOT, 'profile', 'private-terms.txt')
    if os.path.exists(f):
        for line in open(f, encoding='utf8'):
            line = line.strip()
            if line and not line.startswith('#'):
                words.add(line)
    pj = os.path.join(ROOT, 'profile', 'profile.json')
    if os.path.exists(pj):
        personal = ('full_name', 'short_name', 'company', 'legal_entity', 'mobile', 'landline', 'email',
                    'website', 'office_address', 'return_address', 'searchland_login', 'letters_folder',
                    'registers_folder', 'downloads_folder')
        for k, v in json.load(open(pj, encoding='utf8')).items():
            if k in personal and isinstance(v, str) and len(v) >= 4:
                words.add(v)
    titles = set()
    kd = os.path.join(ROOT, 'knowledge')
    for dp, _, fs in os.walk(kd):
        for fn in fs:
            if fn.endswith('.md'):
                titles |= set(re.findall(r'\b(?:[A-Z]{1,3}\d{4,7})\b', open(os.path.join(dp, fn), encoding='utf8').read()))
    return words, titles


def main(out):
    out = os.path.abspath(out)
    # If the output folder is a git clone (for example the GitHub copy), keep its .git
    # folder so the clone stays connected; replace everything else.
    if os.path.exists(out):
        for name in os.listdir(out):
            if name == '.git':
                continue
            p = os.path.join(out, name)
            shutil.rmtree(p) if os.path.isdir(p) and not os.path.islink(p) else os.remove(p)
    else:
        os.makedirs(out)
    for name in KEEP_TOP:
        src = os.path.join(ROOT, name)
        if os.path.isdir(src):
            shutil.copytree(src, os.path.join(out, name),
                            ignore=shutil.ignore_patterns('__pycache__', 'settings.local.json'))
        elif os.path.exists(src):
            shutil.copy(src, os.path.join(out, name))
    for rel in SCAFFOLD:
        src = os.path.join(ROOT, rel)
        dst = os.path.join(out, rel)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        if rel.startswith('knowledge/') and rel != 'knowledge/README.md':
            # empty versions for a new user
            empty = {'knowledge/learned-checks.md': '# Learned checks\n\nChecks this engine has learned on your own sites, added by the site review. Read with the coverage checklist.\n',
                     'knowledge/index.md': '# Index\n\nEmpty. Rebuilt by `python tools/build_index.py` as notes are written.\n',
                     'knowledge/contacts/log.md': '# Contact log\n\n| Date | Title | Recipient | What | Status | File |\n|---|---|---|---|---|---|\n',
                     'knowledge/open-items.md': '# Open items\n\nNone yet.\n'}
            open(dst, 'w', encoding='utf8').write(empty[rel])
        elif os.path.exists(src):
            shutil.copy(src, dst)
    open(os.path.join(out, '.gitignore'), 'w', encoding='utf8').write(PUBLIC_GITIGNORE)
    for sub in ('knowledge/councils', 'knowledge/sites', 'knowledge/agents'):
        os.makedirs(os.path.join(out, sub), exist_ok=True)
        open(os.path.join(out, sub, '.keep'), 'w').close()
    words, titles = private_words()
    problems = []
    for dp, _, fs in os.walk(out):
        for fn in fs:
            p = os.path.join(dp, fn)
            if not fn.endswith(TEXT_EXT):
                continue
            for i, line in enumerate(open(p, encoding='utf8', errors='ignore'), 1):
                for w in words:
                    if re.search(r'(?<![A-Za-z0-9])' + re.escape(w) + r'(?![A-Za-z0-9])', line, re.I):
                        problems.append('%s:%d contains "%s"' % (os.path.relpath(p, out), i, w))
                for t in re.findall(r'\b[A-Z]{1,3}\d{4,7}\b', line):
                    if t in titles:
                        problems.append('%s:%d contains title %s' % (os.path.relpath(p, out), i, t))
    if problems:
        for name in os.listdir(out):
            if name == '.git':
                continue
            p = os.path.join(out, name)
            shutil.rmtree(p) if os.path.isdir(p) and not os.path.islink(p) else os.remove(p)
        print('NOT BUILT. Personal details found:')
        print('\n'.join(problems))
        sys.exit(1)
    print('Public copy built at', out, 'and checked clean.')


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, '..', 'land-engine-public'))
