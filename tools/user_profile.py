"""Read the user's profile (profile/profile.json) for the scripts.

Every script that needs the user's name, company, contact details, letterhead or folders
calls load(). Nothing personal is ever written into a skill or a script.
"""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILE_DIR = os.path.join(ROOT, 'profile')
PROFILE = os.path.join(PROFILE_DIR, 'profile.json')

REQUIRED = ['full_name', 'role', 'company', 'mobile', 'email', 'ref_prefix', 'letters_folder']


def load():
    if not os.path.exists(PROFILE):
        raise SystemExit('No profile yet. Run the setup skill first ("set me up").')
    p = json.load(open(PROFILE, encoding='utf8'))
    missing = [k for k in REQUIRED if not p.get(k)]
    if missing:
        raise SystemExit('Profile is missing: ' + ', '.join(missing) + '. Run the setup skill again.')
    for k in ('letterhead', 'site_map_template', 'back_page', 'logo'):
        if p.get(k) and not os.path.isabs(p[k]):
            p[k] = os.path.join(PROFILE_DIR, p[k])
    p.setdefault('letterhead', os.path.join(PROFILE_DIR, 'letterhead.docx'))
    p.setdefault('site_map_template', os.path.join(PROFILE_DIR, 'site-map-a4.docx'))
    p.setdefault('map_image', 'word/media/image2.png')
    p.setdefault('map_frame', [1139, 699])
    return p
