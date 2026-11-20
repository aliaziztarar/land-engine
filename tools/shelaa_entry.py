"""Print one site's entry from an extracted land availability assessment text.
Usage: python tools/shelaa_entry.py sources/<council>/<assessment>.txt <site ref>
Matches "Site Ref: <ref>" and prints to the next "Site Ref:". Tries the ref with and without leading zeros."""
import re, sys
path, ref = sys.argv[1], sys.argv[2]
t = open(path, encoding='utf8').read()
for r in (ref, ref.zfill(3), ref.lstrip('0')):
    m = re.search(r'Site Ref:\s*' + re.escape(r) + r'\s*\n', t)
    if m:
        j = t.find('Site Ref:', m.end())
        print(t[m.start(): j if j > 0 else len(t)])
        break
else:
    sys.exit('no entry for ' + ref)
