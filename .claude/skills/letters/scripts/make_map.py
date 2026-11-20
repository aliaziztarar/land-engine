"""Build the A4 site map PDF that goes with a landowner letter.

Usage:
  python make_map.py TITLE "Address line" ACRES map.png OUTDIR --date "16 November 2026" [--thin]

map.png is SearchLand's "Screenshot map" download (see ../../searchland/SKILL.md), taken with
a large browser window so it is sharp. The script removes SearchLand's round title marker,
recolours the title outline red and thickens it, crops around the site, drops it into the
user's site map template (profile/site-map-a4.docx, made by the setup skill) and converts to
"<TITLE> - Site map.pdf" in OUTDIR. --thin keeps the outline thin.

The template carries the placeholders [Address], [Ref], [Title], [Area] and [Date], and a
picture whose file is named in profile.json as map_image.
Needs: numpy, opencv-python, Pillow, scipy, LibreOffice.
"""
import os, re, shutil, subprocess, sys, tempfile, zipfile
import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', '..', 'tools'))
import user_profile as prof  # noqa: E402
from make_letter import soffice  # noqa: E402

RED = (228, 26, 28)


def _remove_marker(bgr, cx, cy):
    """SearchLand puts a small round red and white marker at the centre of the selected title."""
    import cv2
    h, w = bgr.shape[:2]
    y0, y1 = max(int(cy) - 45, 0), min(int(cy) + 45, h)
    x0, x1 = max(int(cx) - 45, 0), min(int(cx) + 45, w)
    sub = bgr[y0:y1, x0:x1].astype(int)
    b, g, r = sub[..., 0], sub[..., 1], sub[..., 2]
    mk = ((r > 150) & (r > g + 40) & (r > b + 40)) | ((r > 175) & (g > 175) & (b > 175))
    m = np.zeros(bgr.shape[:2], np.uint8)
    m[y0:y1, x0:x1] = mk.astype(np.uint8) * 255
    m = cv2.dilate(m, np.ones((7, 7), np.uint8))
    if m.sum() == 0:
        return bgr
    return cv2.inpaint(bgr, m, 9, cv2.INPAINT_TELEA)


def prep(src, out, frame, thicken=True):
    """Find SearchLand's blue or purple title outline, crop around it, recolour it red, remove
    the title marker, and write the picture at twice the frame size. Returns the site's share
    of the frame width (aim for roughly a third to a half)."""
    import cv2
    from scipy import ndimage
    fw, fh = frame
    AR = fw / fh
    im = Image.open(src).convert('RGB')
    a = np.array(im).astype(int)
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    strict = (r > 95) & (r < 175) & (g < 80) & (b > 140) & (b > r + 15)
    wide = (b > r + 12) & (b > g + 35) & (r > g + 15)
    lab, n = ndimage.label(ndimage.binary_dilation(strict, iterations=3))
    if n == 0:
        raise SystemExit('No title outline found in ' + src + '. Retake the screenshot with the title selected.')
    sizes = ndimage.sum(strict, lab, range(1, n + 1))
    keep = np.isin(lab, [i + 1 for i, s in enumerate(sizes) if s >= 0.05 * sizes.max()])
    m = (wide | strict) & ndimage.binary_dilation(keep, iterations=2)
    m = ndimage.binary_dilation(m, iterations=1)
    o = np.array(im)
    o[m] = RED
    ys, xs = np.nonzero(strict & keep)
    x0, x1, y0, y1 = xs.min(), xs.max(), ys.min(), ys.max()
    H, W = o.shape[:2]
    col = np.array(im)[:, 20]
    L = 135 if (np.abs(col.astype(int) - [229, 227, 223]).max(axis=1) < 6).mean() > 0.9 else 0
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    w = max((x1 - x0) * 1.8, (y1 - y0) * 1.8 * AR, 500)
    w = min(w, W - L, H * AR)
    h = w / AR
    X0 = min(max(cx - w / 2, L), W - w)
    Y0 = min(max(cy - h / 2, 0), H - h)
    c = Image.fromarray(o).crop((int(X0), int(Y0), int(X0 + w), int(Y0 + h)))
    c = c.resize((fw * 2, fh * 2), Image.LANCZOS)
    bgr = cv2.cvtColor(np.array(c), cv2.COLOR_RGB2BGR)
    sx, sy = fw * 2 / w, fh * 2 / h
    bgr = _remove_marker(bgr, (cx - X0) * sx, (cy - Y0) * sy)
    if thicken:
        red = ((bgr[..., 2] > 180) & (bgr[..., 1] < 80) & (bgr[..., 0] < 80)).astype(np.uint8)
        n2, lab2, st, _ = cv2.connectedComponentsWithStats(red, 8)
        if n2 > 1:
            big = 1 + int(np.argmax(st[1:, cv2.CC_STAT_AREA]))
            k = cv2.dilate((lab2 == big).astype(np.uint8), np.ones((7, 7), np.uint8)) > 0
            bgr[k] = (RED[2], RED[1], RED[0])
    cv2.imwrite(out, bgr)
    return (x1 - x0) / w


def _xml_escape(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def build(title, addr, acres, png, outdir, date, thin=False, P=None, tenure=''):
    P = P or prof.load()
    d = tempfile.mkdtemp(prefix='map_')
    x = os.path.join(d, 'x')
    with zipfile.ZipFile(P['site_map_template']) as z:
        z.extractall(x)
    frac = prep(png, os.path.join(x, *P['map_image'].split('/')), P['map_frame'], thicken=not thin)
    p = os.path.join(x, 'word', 'document.xml')
    s = open(p, encoding='utf8').read()
    area = acres if str(acres).startswith('approx') else 'approximately %s acres' % acres
    title_line = title + (', ' + tenure if tenure else '')
    for k, v in (('[Address]', addr), ('[Ref]', P['ref_prefix'] + title), ('[Title]', title_line),
                 ('[Area]', area), ('[Date]', date)):
        assert k in s, 'template placeholder %s missing' % k
        s = s.replace(k, _xml_escape(v))
    # the template's hidden "paste the map here" prompt sits behind the picture and pushes the caption down
    # keep the caption at the top of its cell so it clears the logo beneath it
    _i = s.find('Indicative site boundary')
    _j = s.rfind('<w:vAlign w:val="center"/>', 0, _i)
    if _i > 0 and _j > 0:
        s = s[:_j] + '<w:vAlign w:val="top"/>' + s[_j + len('<w:vAlign w:val="center"/>'):]
    for frag in ('Paste the map here (', 'Ctrl+V', '), then drag a corner until it fills this box.'):
        s = s.replace('>' + frag + '</w:t>', '></w:t>')
    open(p, 'w', encoding='utf8').write(s)
    docx_path = os.path.join(d, title + ' - Site map.docx')
    with zipfile.ZipFile(docx_path, 'w', zipfile.ZIP_DEFLATED) as z:
        for root, _, files in os.walk(x):
            for f in files:
                full = os.path.join(root, f)
                z.write(full, os.path.relpath(full, x))
    subprocess.run([soffice(), '--headless', '--convert-to', 'pdf', '--outdir', d, docx_path],
                   capture_output=True, check=True)
    pdf = docx_path[:-5] + '.pdf'
    from pypdf import PdfReader
    n = len(PdfReader(pdf).pages)
    assert n == 1, 'site map ran to %d pages' % n
    os.makedirs(outdir, exist_ok=True)
    shutil.copy(pdf, outdir)
    shutil.rmtree(d, ignore_errors=True)
    return os.path.join(outdir, os.path.basename(pdf)), frac


if __name__ == '__main__':
    args = sys.argv[1:]
    date = ''
    if '--date' in args:
        i = args.index('--date')
        date = args[i + 1]
        del args[i:i + 2]
    tenure = ''
    if '--tenure' in args:
        i = args.index('--tenure')
        tenure = args[i + 1]
        del args[i:i + 2]
    thin = '--thin' in args
    args = [a for a in args if not a.startswith('--')]
    t, addr, ac, png, od = args[:5]
    out, frac = build(t, addr, ac, png, od, date, thin=thin, tenure=tenure)
    print(out, 'site fills %.0f%% of the frame width' % (frac * 100))
