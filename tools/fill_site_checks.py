"""Fill BuildUp's Site Checks checklist (the member's own Word copy, kept at
profile/buildup/site-checks-checklist.docx by the setup skill) from a small JSON file, and make a PDF.

Usage:
  python tools/fill_site_checks.py answers.json "<output folder>" ["<file name without extension>"]

answers.json holds one key per line of the checklist, in plain English, for example:
  {"Title number": "ABC123456",
   "Access": "Frontage on an adopted road; ...",
   "Flood Zone": "...",
   ...
   "Additional notes": "..."}
Keys are matched to the start of each line of the checklist, ignoring case and punctuation, so
"Access" fills the line "Access- Is there adequate access for the site?". Every line in the checklist must
have an answer; the tool stops and lists any that are missing, so nothing is left blank.
The answer is added after the line's own words, in plain (not bold) text. Writes <name>.docx and, when
LibreOffice is installed, <name>.pdf in the output folder. Run without -I so it can import python-docx."""
import sys, os, json, re, copy, subprocess, shutil
import docx

HERE = os.path.dirname(os.path.abspath(__file__))
_CANDIDATES = [os.path.join(HERE, '..', 'profile', 'buildup', 'site-checks-checklist.docx'),
               os.path.join(HERE, '..', '.claude', 'skills', 'appraisal', 'templates', 'buildup-site-checks-checklist.docx')]
TEMPLATE = next((c for c in _CANDIDATES if os.path.exists(c)), _CANDIDATES[0])

# lines that are headings, not items to answer
HEADINGS = ('site checks:', '1st site checks', '2nd site checks', '3rd site checks', '4th site checks')


def norm(s):
    return re.sub(r'[^a-z0-9 ]', '', s.lower()).strip()


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    answers = json.load(open(sys.argv[1], encoding='utf8'))
    out_dir = sys.argv[2]
    name = sys.argv[3] if len(sys.argv) > 3 else 'Site Checks'
    os.makedirs(out_dir, exist_ok=True)
    d = docx.Document(TEMPLATE)
    keys = {norm(k): v for k, v in answers.items()}
    used, missing = set(), []
    for p in d.paragraphs:
        text = p.text.strip()
        if not text:
            continue
        low = text.lower()
        if low.startswith(HEADINGS):
            continue
        label = None
        if 'title number' in low:
            label = 'title number'
        elif low.startswith('additional notes'):
            label = 'additional notes'
        else:
            n = norm(text)
            for k in keys:
                if n.startswith(k):
                    label = k
                    break
        if label is None:
            missing.append(text)
            continue
        used.add(label)
        r = p.add_run('  ' + keys[label])
        r.bold = False
        r.italic = False
        # copy the font of the existing text so the answer looks part of the line
        src = p.runs[0] if p.runs else None
        if src is not None and src.font.name:
            r.font.name = src.font.name
        if src is not None and src.font.size:
            r.font.size = src.font.size
    unanswered = [t for t in missing]
    unused = [k for k in keys if k not in used]
    if unanswered:
        print('LINES WITH NO ANSWER (add a key for each):')
        for t in unanswered:
            print('  -', t)
        sys.exit(2)
    if unused:
        print('Keys that matched no line (check spelling):', unused)
    docx_path = os.path.join(out_dir, name + '.docx')
    d.save(docx_path)
    print('wrote', docx_path)
    soffice = shutil.which('soffice') or r'C:\Program Files\LibreOffice\program\soffice.exe'
    if os.path.exists(soffice) or shutil.which('soffice'):
        subprocess.run([soffice, '--headless', '--convert-to', 'pdf', '--outdir', out_dir, docx_path],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=180)
        pdf = os.path.join(out_dir, name + '.pdf')
        print('wrote', pdf if os.path.exists(pdf) else '(PDF not made; open the Word file and save as PDF)')
    else:
        print('LibreOffice not found; open the Word file and save as PDF')


if __name__ == '__main__':
    main()
