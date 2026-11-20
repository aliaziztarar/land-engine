# Land Engine

A Claude Code folder that does the desk work of land sourcing for you. Give it a title number (and what SearchLand shows for it) and it researches the site from every angle: the council's assessment of the land, its planning history, two nearby examples (one approved, one refused), the council's other documents, whether it is for sale, who owns it and whether anyone already has an option, and every constraint it can check. It then gives you a plain verdict. Say "appraisal" and it works out what the land could be worth with planning. Say "letter" and it writes to the owners on your letterhead with a map, ready to print.

## Getting started
1. Install the Claude desktop app and sign in.
2. Download this folder and put it somewhere easy, such as Documents.
3. In the Claude app, open the Code tab, choose this folder, and type: **set me up**
Claude asks a few questions, makes your letterhead (or uses your own, if you tell it where it is) and checks your computer has what it needs. After that, just give it a title number.

The full step by step guide is linked from the group post.

## What is in the folder
- `CLAUDE.md`: the instructions Claude reads first.
- `.claude/`: the skills (site review, appraisal, letters, SearchLand, documents, setup), the worker that does the heavy reading on a cheaper model, and the setting that starts every chat on the stronger model.
- `profile/`, `knowledge/`, `sources/`: your own details, notes and documents. These stay on your computer and are never shared or uploaded.
- `tools/`: small helper scripts Claude runs for you.
