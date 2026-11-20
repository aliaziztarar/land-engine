"""Convert a PDF to text, keeping the page layout as far as possible.

Usage: python tools/pdf_to_text.py input.pdf output.txt [source address]
Uses pdftotext -layout if it is installed (best for tables), otherwise PyMuPDF.
Writes the source address and today's date on the first lines when given.
"""
import datetime, shutil, subprocess, sys


def convert(src, out, source=None):
    if shutil.which('pdftotext'):
        subprocess.run(['pdftotext', '-layout', src, out], check=True)
        text = open(out, encoding='utf8', errors='ignore').read()
    else:
        import fitz
        doc = fitz.open(src)
        text = '\n'.join('[page %d]\n%s' % (i + 1, p.get_text('text', sort=True)) for i, p in enumerate(doc))
    if len(text.strip()) < 50:
        text = '[This PDF has no text layer; it is probably scanned. Run OCR (ocrmypdf) first.]\n' + text
    head = ''
    if source:
        head = 'Source: %s\nRead: %s\n\n' % (source, datetime.date.today().strftime('%d %B %Y').lstrip('0'))
    open(out, 'w', encoding='utf8').write(head + text)
    return out


if __name__ == '__main__':
    convert(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)
    print('wrote', sys.argv[2])
