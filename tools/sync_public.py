"""Keep the public copy of the engine up to date automatically.

Usage: python tools/sync_public.py
Run automatically after each reply by a Stop hook in .claude/settings.local.json (private to
this computer, never copied into the public version).

What it does:
1. Reads `public_repo_folder` from profile/profile.json. If it is not set, it does nothing,
   so it is harmless in anyone else's copy of the engine.
2. Works out whether the method has changed since the last sync: CLAUDE.md, README.md,
   GUIDE.md, everything in .claude (except settings.local.json) and tools. Notes, profile
   and sources are never part of this.
3. If it has changed, builds the cleaned public copy in a temporary folder with
   tools/make_public_copy.py, which runs the leak check, and only if it is clean replaces
   the files in the public folder (keeping its .git).
4. If the leak check passes, commits the change in that folder's git clone, ready for the
   user to push. It never pushes.
5. If the leak check fails, nothing is copied or committed; the problem is written to
   profile/sync-problem.txt for the engine to report at the start of the next chat.
"""
import datetime, hashlib, io, json, os, shutil, subprocess, sys, tempfile
from contextlib import redirect_stdout

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
STATE = os.path.join(ROOT, 'profile', '.public-sync-hash')
PROBLEM = os.path.join(ROOT, 'profile', 'sync-problem.txt')
METHOD = ['CLAUDE.md', 'README.md', 'GUIDE.md', '.claude', 'tools']


def say(msg):
    # A Stop hook shows a systemMessage to the user; plain output is not shown.
    print(json.dumps({'systemMessage': msg}))


def method_hash():
    h = hashlib.sha256()
    for top in METHOD:
        p = os.path.join(ROOT, top)
        files = []
        if os.path.isfile(p):
            files = [p]
        elif os.path.isdir(p):
            for dp, dns, fs in os.walk(p):
                dns[:] = [d for d in dns if d != '__pycache__']
                files += [os.path.join(dp, f) for f in fs if f != 'settings.local.json']
        for f in sorted(files):
            h.update(os.path.relpath(f, ROOT).replace('\\', '/').encode())
            with open(f, 'rb') as fh:
                h.update(fh.read().replace(b'\r\n', b'\n'))
    return h.hexdigest()


def main():
    pj = os.path.join(ROOT, 'profile', 'profile.json')
    if not os.path.exists(pj):
        return
    repo = json.load(open(pj, encoding='utf8')).get('public_repo_folder')
    if not repo or not os.path.isdir(os.path.join(repo, '.git')):
        return
    now = method_hash()
    if os.path.exists(STATE) and open(STATE).read().strip() == now:
        return
    import make_public_copy
    out = io.StringIO()
    tmp = os.path.join(tempfile.mkdtemp(prefix='land-engine-public-'), 'copy')
    try:
        # Build and check in a temporary folder first, so a failed check never touches
        # the GitHub clone.
        with redirect_stdout(out):
            make_public_copy.main(tmp)
    except SystemExit:
        shutil.rmtree(os.path.dirname(tmp), ignore_errors=True)
        open(PROBLEM, 'w', encoding='utf8').write(
            'The public copy was NOT updated on %s, because the leak check found personal '
            'details in the method files:\n%s' % (datetime.date.today().isoformat(), out.getvalue()))
        say('The public copy was not updated: personal details were found in the method files. See profile/sync-problem.txt.')
        return
    if os.path.exists(PROBLEM):
        os.remove(PROBLEM)
    for name in os.listdir(repo):
        if name != '.git':
            p = os.path.join(repo, name)
            shutil.rmtree(p) if os.path.isdir(p) and not os.path.islink(p) else os.remove(p)
    for name in os.listdir(tmp):
        src = os.path.join(tmp, name)
        (shutil.copytree if os.path.isdir(src) else shutil.copy2)(src, os.path.join(repo, name))
    shutil.rmtree(os.path.dirname(tmp), ignore_errors=True)
    subprocess.run(['git', '-C', repo, 'add', '-A'], capture_output=True)
    st = subprocess.run(['git', '-C', repo, 'status', '--porcelain'], capture_output=True, text=True)
    if st.stdout.strip():
        msg = 'Engine update %s' % datetime.date.today().isoformat()
        r = subprocess.run(['git', '-C', repo, 'commit', '-m', msg], capture_output=True, text=True)
        if r.returncode != 0:
            say('The public copy was built, but the commit failed: ' + (r.stderr or r.stdout).strip())
            return
        say('The public copy has been updated and committed. Click Push in GitHub Desktop when you are ready.')
    open(STATE, 'w').write(now)


if __name__ == '__main__':
    main()
