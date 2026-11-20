"""Make a new user's letterhead and site map templates from profile/profile.json and their logo.

Usage: python tools/make_letterhead.py
Run by the setup skill after profile.json is written. Writes profile/letterhead.docx and
profile/site-map-a4.docx, then records the map picture's file name in profile.json.
A user who already has a letterhead in Word can give it to the setup skill instead; the skill
adds the placeholders to it (see .claude/skills/setup/SKILL.md).
"""
import json, os, sys, tempfile, zipfile
from PIL import Image
import docx
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import user_profile as prof  # noqa: E402

FRAME = (1139, 699)


def rgb(h):
    h = (h or '1F4E3D').lstrip('#')
    return RGBColor(int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))


def no_borders(table):
    tbl = table._tbl
    pr = tbl.tblPr
    b = OxmlElement('w:tblBorders')
    for e in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
        el = OxmlElement('w:' + e)
        el.set(qn('w:val'), 'nil')
        b.append(el)
    pr.append(b)


def para(container, text='', size=11, bold=False, color=None, align=None, space_after=6):
    p = container.add_paragraph()
    if text:
        r = p.add_run(text)
        r.font.size = Pt(size)
        r.bold = bold
        if color is not None:
            r.font.color.rgb = color
    p.paragraph_format.space_after = Pt(space_after)
    if align:
        p.alignment = align
    return p


def base_doc():
    d = docx.Document()
    s = d.sections[0]
    s.page_height, s.page_width = Cm(29.7), Cm(21.0)
    s.top_margin, s.bottom_margin = Cm(1.6), Cm(1.6)
    s.left_margin, s.right_margin = Cm(2.2), Cm(2.2)
    st = d.styles['Normal']
    st.font.name = 'Calibri'
    st.font.size = Pt(11)
    st.font.color.rgb = RGBColor(0x33, 0x33, 0x33)
    return d


def letterhead(P, out):
    d = base_doc()
    s = d.sections[0]
    brand = rgb(P.get('brand_colour'))
    hdr = s.header
    t = hdr.add_table(rows=1, cols=2, width=Cm(16.6))
    no_borders(t)
    left, right = t.rows[0].cells
    lp = left.paragraphs[0]
    if P.get('logo') and os.path.exists(P['logo']):
        lp.add_run().add_picture(P['logo'], height=Cm(1.8))
    else:
        r = lp.add_run(P['company'].upper())
        r.bold = True
        r.font.size = Pt(16)
        r.font.color.rgb = brand
    lines = [l for l in (P.get('landline') and 'Tel ' + P['landline'], 'Mobile ' + P['mobile'],
                         P['email'], P.get('website'), P.get('office_address')) if l]
    rp = right.paragraphs[0]
    rp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    for i, l in enumerate(lines):
        r = rp.add_run(l + ('\n' if i < len(lines) - 1 else ''))
        r.font.size = Pt(9)
        r.font.color.rgb = brand
    legal = P.get('legal_footer') or P['company']
    fp = s.footer.paragraphs[0]
    fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = fp.add_run(legal)
    r.font.size = Pt(8)
    r.font.color.rgb = RGBColor(0x66, 0x66, 0x66)
    p = para(d, space_after=10)
    p.add_run('Our ref: [Reference]')
    p.add_run('\t[Date]')
    p.paragraph_format.tab_stops.add_tab_stop(Cm(16.6), alignment=2)
    for k in ['[Recipient name]', '[Company or organisation]', '[Address line 1]',
              '[Address line 2]', '[Town]', '[Postcode]']:
        para(d, k, space_after=0)
    para(d, space_after=6)
    para(d, 'Dear [Name],', space_after=8)
    para(d, '[Subject of the letter]', bold=True, space_after=8)
    para(d, '[Type your letter here.]', space_after=8)
    para(d, 'Yours sincerely,', space_after=36)
    para(d, '[Signature name]', bold=True, space_after=0)
    para(d, '[Signature role]', space_after=0)
    d.save(out)


def site_map(P, out):
    d = base_doc()
    brand = rgb(P.get('brand_colour'))
    tmp = tempfile.mkdtemp()
    ph = os.path.join(tmp, 'placeholder.png')
    Image.new('RGB', FRAME, (205, 210, 205)).save(ph)
    para(d, 'Land at: [Address]', size=13, bold=True, color=brand, space_after=8)
    p = d.add_paragraph()
    p.add_run().add_picture(ph, width=Cm(16.6))
    para(d, 'Indicative site boundary shown in red, for discussion only.', size=8,
         color=RGBColor(0x66, 0x66, 0x66), space_after=10)
    t = d.add_table(rows=4, cols=2)
    no_borders(t)
    t.alignment = WD_TABLE_ALIGNMENT.LEFT
    t.autofit = False
    t.columns[0].width, t.columns[1].width = Cm(3.5), Cm(13)
    grid = t._tbl.tblGrid
    for gc, w in zip(grid.findall(qn('w:gridCol')), (Cm(3.5), Cm(13))):
        gc.set(qn('w:w'), str(int(w.twips)))
    for row, (k, v) in zip(t.rows, (('Our ref', '[Ref]'), ('Title', '[Title]'), ('Area', '[Area]'),
                                     ('Enclosed with', 'our letter dated [Date]'))):
        a, b = row.cells
        a.width, b.width = Cm(3.5), Cm(13)
        ra = a.paragraphs[0].add_run(k)
        ra.bold = True
        ra.font.size = Pt(9.5)
        rb = b.paragraphs[0].add_run(v)
        rb.font.size = Pt(9.5)
    lp = para(d, space_after=0)
    lp.paragraph_format.space_before = Pt(18)
    if P.get('logo') and os.path.exists(P['logo']):
        lp.add_run().add_picture(P['logo'], height=Cm(1.4))
    else:
        r = lp.add_run(P['company'])
        r.bold = True
        r.font.color.rgb = brand
    d.save(out)
    # find the map picture inside the saved file
    with zipfile.ZipFile(out) as z:
        for n in z.namelist():
            if n.startswith('word/media/'):
                with z.open(n) as f:
                    try:
                        if Image.open(f).size == FRAME:
                            return n
                    except Exception:
                        pass
    raise SystemExit('could not locate the map picture in the template')


if __name__ == '__main__':
    P = prof.load()
    lh = os.path.join(prof.PROFILE_DIR, 'letterhead.docx')
    sm = os.path.join(prof.PROFILE_DIR, 'site-map-a4.docx')
    letterhead(P, lh)
    mi = site_map(P, sm)
    raw = json.load(open(prof.PROFILE, encoding='utf8'))
    raw.update({'letterhead': 'letterhead.docx', 'site_map_template': 'site-map-a4.docx',
                'map_image': mi, 'map_frame': list(FRAME)})
    json.dump(raw, open(prof.PROFILE, 'w', encoding='utf8'), indent=1, ensure_ascii=False)
    print('wrote', lh, 'and', sm, '(map picture', mi + ')')
