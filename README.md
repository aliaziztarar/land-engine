# Land Engine

A Claude Code folder that does the desk analysis of a site you have already found. It does not find sites for you; you find them in SearchLand as you do now. Give it the title number, the address SearchLand shows for it, and what SearchLand shows in its left-hand panel, and it analyses the site from every angle:

- the council's assessment of the land, and every land availability (SHLAA) round it appears in;
- its planning history, with every refusal reason tested against today, and two nearby examples (one approved, one refused);
- the council's other documents: local plan, neighbourhood plan, evidence studies, committee papers and parish minutes;
- whether it is listed for sale or being promoted by someone else;
- the owner: if SearchLand shows a company, it checks the company at Companies House (status, directors, charges). A private owner's name, any lender, and any option or developer notice are only on the title register, so it reads those once you buy the register (about £7) and give it;
- every constraint, from what SearchLand shows and its own online checks, weighed together.

It then gives you a plain verdict, and lists anything it could not check. Say "appraisal" and it works out what the land could be worth with planning. Say "letter" and it writes to the owners on your letterhead with a map, ready to print.

## Getting started
1. Install the Claude desktop app and sign in.
2. Download this folder (green **Code** button, then **Download ZIP**), extract it and put it somewhere easy, such as Documents.
3. In the Claude app, open the Code tab, choose this folder, and set the model (see below).
4. Type: **set me up**. Claude asks a few questions, makes your letterhead (or uses your own, if you tell it where it is) and checks your computer has what it needs.
5. After that, give it the title number, the address SearchLand shows, and the SearchLand left-hand panel pasted in.

## Very important: the setup for every new chat
This is what keeps your Claude allowance down. Before you start each new chat:
1. Click the model name under the message box, choose **Sonnet 5.5**, and set the effort to **High** (or type `/effort high` and press Enter).
2. Type `/advisor opus` and press Enter.
3. Check the reply says the advisor is set to Opus 5.5. To check at any time, type `/advisor` on its own.

Sonnet does the work, Opus is consulted at the moments that decide the outcome (the verdict, the appraisal, submissions and letters), and a worker on Sonnet does the heavy reading.

## One site per chat
Start a new chat for every new site. The engine keeps notes in this folder, so each new chat already knows everything learned before. A long chat with many sites in it uses far more of your allowance and gets slower. To come back to a site, start a new chat and give its title number.

## The full guide
Read [GUIDE.md](GUIDE.md) for the step by step guide.

## What is in the folder
- `CLAUDE.md`: the instructions Claude reads first.
- `GUIDE.md`: the full plain English guide.
- `.claude/`: the skills (site review, appraisal, letters, SearchLand, documents, setup), the worker, and the settings.
- `profile/`, `knowledge/`, `sources/`: your own details, notes and documents. These stay on your computer and are never shared or uploaded.
- `tools/`: small helper scripts Claude runs for you.
