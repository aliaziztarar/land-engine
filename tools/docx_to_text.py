"""Convert a .docx (including table-heavy council assessments) to plain text in body order.
Usage: python3 docx_to_text.py in.docx out.txt ["Source URL or note"]"""
import sys, datetime
import docx
from docx.oxml.ns import qn
src, dst = sys.argv[1], sys.argv[2]
note = sys.argv[3] if len(sys.argv) > 3 else ''
d = docx.Document(src)
out = []
for el in d.element.body.iter():
    if el.tag == qn('w:p'):
        t = ''.join(x.text or '' for x in el.iter(qn('w:t')))
        if t.strip():
            out.append(t.strip())
import os
head = ['Source file: %s' % os.path.basename(src), 'Converted: %s' % datetime.date.today().isoformat()]
if note:
    head.append('Source: ' + note)
open(dst, 'w', encoding='utf8').write('\n'.join(head + [''] + out))
print(dst, len(out), 'paragraphs')
