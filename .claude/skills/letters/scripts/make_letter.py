"""Build landowner letters as PDFs on the user's letterhead.

Usage: python make_letter.py job.json
job.json is a list of letters, each with: ref, date, outpdf, addr (list of lines),
salut, subject, body (list of paragraphs), and map_png (optional, used when the profile's
map_style is on_letter). See ../examples/job-example.json.

The letterhead, signature name and role, and optional back page come from profile/profile.json
(built by the setup skill). The letter must fit one page; the script refuses a two page front.
Needs: python-docx, pypdf, LibreOffice (soffice) on the path.
"""
import copy, json, os, shutil, subprocess, sys
import docx
from pypdf import PdfReader, PdfWriter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', '..', 'tools'))
import user_profile as prof  # noqa: E402


def soffice():
    for c in ('soffice', 'libreoffice',
              r'C:\Program Files\LibreOffice\program\soffice.exe',
              r'C:\Program Files (x86)\LibreOffice\program\soffice.exe',
              '/Applications/LibreOffice.app/Contents/MacOS/soffice'):
        if shutil.which(c) or os.path.exists(c):
            return shutil.which(c) or c
    raise SystemExit('LibreOffice is not installed. The setup skill installs it.')


def _settext(p, t):
    if not p.runs:
        p.add_run(t)
        return
    p.runs[0].text = t
    for r in p.runs[1:]:
        r.text = ''


def _document(P, ref, date, addr, salut, subject, body, map_png, map_cm):
    d = docx.Document(P['letterhead'])

    def find(s):
        return next(p for p in d.paragraphs if p.text.startswith(s))

    p = find('Our ref:')
    for r in p.runs:
        r.text = r.text.replace('[Reference]', ref).replace('[Date]', date)
    keys = ['[Recipient name]', '[Company or organisation]', '[Address line 1]',
            '[Address line 2]', '[Town]', '[Postcode]']
    for i, k in enumerate(keys):
        _settext(find(k), addr[i] if i < len(addr) else '__DEL__')
    _settext(find('Dear [Name]'), salut)
    _settext(find('[Subject'), subject)
    ph = [p for p in d.paragraphs
          if p.text.startswith(('[Type your letter', '[When the letter', '[To reuse'))]
    tm = ph[0]
    _settext(tm, body[0])
    last = tm
    for t in body[1:]:
        n = copy.deepcopy(tm._p)
        last._p.addnext(n)
        np_ = docx.text.paragraph.Paragraph(n, tm._parent)
        _settext(np_, t)
        last = np_
    for p in ph[1:]:
        p._p.getparent().remove(p._p)
    if map_png and map_cm:
        from docx.shared import Cm
        n = copy.deepcopy(tm._p)
        last._p.addnext(n)
        mp = docx.text.paragraph.Paragraph(n, tm._parent)
        _settext(mp, '')
        mp.runs[0].add_picture(map_png, width=Cm(map_cm))
    _settext(find('[Signature name]'), P['full_name'])
    _settext(find('[Signature role]'), P['role'])
    for p in list(d.paragraphs):
        if p.text == '__DEL__':
            p._p.getparent().remove(p._p)
    left = [p.text for p in d.paragraphs if '[' in p.text]
    assert not left, 'placeholders left: %s' % left
    return d


def build(ref, date, addr, salut, subject, body, outpdf, P=None, map_png=None):
    """Make one letter. With map_style on_letter and a map_png (prepared by make_map.prep),
    the map goes under the body, shrunk step by step until the letter fits one page."""
    P = P or prof.load()
    od = os.path.dirname(os.path.abspath(outpdf))
    os.makedirs(od, exist_ok=True)
    tmp = os.path.splitext(outpdf)[0] + '.docx'
    sizes = [None]
    if map_png and P.get('map_style') == 'on_letter':
        sizes = [12, 10, 8.5, 7, 6]
    for cm in sizes:
        _document(P, ref, date, addr, salut, subject, body, map_png, cm).save(tmp)
        subprocess.run([soffice(), '--headless', '--convert-to', 'pdf', '--outdir', od, tmp],
                       capture_output=True, check=True)
        r = PdfReader(outpdf)
        n = len(r.pages)
        if n == 1:
            break
    assert n == 1, '%s runs to %d pages: shorten the body' % (outpdf, n)
    w = PdfWriter()
    w.add_page(r.pages[0])
    back = P.get('back_page')
    if back and os.path.exists(back):
        w.add_page(PdfReader(back).pages[0])
    w.write(outpdf)
    os.remove(tmp)
    return outpdf


if __name__ == '__main__':
    P = prof.load()
    for j in json.load(open(sys.argv[1], encoding='utf8')):
        print('built', build(P=P, **j))
