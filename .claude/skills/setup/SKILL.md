---
name: setup
description: First-run setup of the land engine for a new user, and the answer to "what can you do". Use when profile/profile.json does not exist, when the user says set me up, start, setup, change my details, new letterhead, or asks what this can do or how it helps.
---

# Setup

The user has just opened this folder in Claude Code, probably for the first time, and may not be technical. In about five minutes, this skill learns who they are, makes their letterhead and site map template, checks the computer has what the letter scripts need, and shows them what the engine can do. Do the work yourself; ask only for what only they know.

## 1. Welcome (one short message)
"Welcome. I'm going to set this up for you, which takes about five minutes and only happens once. I'll ask a few questions about you and your business, make your letterhead, and check your computer has what it needs. After that you can just give me a title number and I'll do the rest."

## 1a. Ask first whether their details already exist somewhere
Before any questions, ask one: "Do you already have your details somewhere I can read, such as your own letterhead, an older copy of this engine, an email signature or your website? If so, tell me where it is (for example 'my letterhead is in Documents, called Letterhead.docx'). If not, I'll just ask you."
- **An older copy of this engine** (a folder or zip with a `profile` folder): copy only `profile/` into this folder. Never copy its `knowledge/` or `sources/` unless the user asks. Read `profile.json` and `profile.md`, list what you took in a few lines, then go to step 6.
- **A Word letterhead** (.docx or .dotx): copy it to `profile/letterhead.docx`, read the name, company, company number, phone, email, website and addresses from its header and footer, and add the placeholder lines as in step 7. Their own design stays exactly as it is.
- **A PDF or picture of a letterhead**: read the details from it, take the logo out of it as an image, and build a Word letterhead in the same style with `tools/make_letterhead.py`. Tell the user in one line that you've rebuilt it in Word so letters can be filled in, and show the sample for them to compare.
- **An email signature, website or business card**: read the details from it.
- **Details typed in the chat**: take them as given.
Then ask only the questions in step 2 that are still unanswered, and show what you found so they can correct it ("I've taken these from your letterhead: ... Is anything out of date?"). Everything ends up in `profile/` the same way as for answers to the questions.

## 2. Ask for their details, in two short batches
Use the question tool if the session has one; otherwise ask in plain numbered questions. Accept short answers and fill the rest yourself. Skip any question already answered from step 1a.

Batch 1, about them:
1. Your full name, and the name you sign letters with (for example "Jane Smith").
2. Your job title on letters (for example "Land Director").
3. Your company's trading name, and its legal name and company number if it has one (this goes in the letter footer).
4. The mobile number and email address owners should use. A landline and website if you have them.
5. The return address for envelopes, if you want returned letters to come back to you.
6. The counties you work in.

Batch 2, about how they work:
7. Are you a member of a programme such as BuildUp? (If BuildUp: their rules are filled in for you: BuildUp reviews each site before any offer; target profit 26 percent; build costs from BuildUp's costing calculator; submissions through Nexus.)
8. In a sentence, how you work with landowners (for example "we take land through planning at our own cost under an option, the owner keeps the land if planning fails"). If they are unsure, offer that example and ask if it fits.
9. Any rules about deals you will or won't do (for example faith based finance rules, no upfront fees).
10. Your logo: "Please put your logo file somewhere I can find it, such as your Downloads folder, and tell me its name. If you don't have one, I'll use your company name in your colours." Ask for a brand colour if they have one.
11. If they already have a letterhead in Word, they can give that instead and you will use it.
12. Do you send a map of the land with your letters? As a separate sheet (the usual way), printed on the letter itself, or no map? (Record as `map_style`: separate, on_letter or none.)
13. How they sign in to SearchLand (for example "Google, with my work email"), so you know which account to use in the browser.

## 3. Folders
Find the user's home and Downloads folders yourself. Create, if missing, `Documents\Land\Letters` and `Documents\Land\Title Registers` (or the Mac equivalents), and tell them where these are in one line. If they already keep letters somewhere, use that instead.

## 4. Programme files (BuildUp members)
BuildUp's Site Checks checklist and Costing Calculator come with the engine (`.claude/skills/appraisal/templates/`); copy the calculator into `profile/buildup/`. The one file each member supplies is BuildUp's Master appraisal workbook: look in their Downloads and Documents for an Excel file whose name contains "Appraisal" and copy it into `profile/buildup/`. If you cannot find them: "Please download your BuildUp Master appraisal workbook from the BuildUp resources into your Downloads folder, then type done." The engine never shares these files.

## 5. Write the profile
- `profile/profile.json` with every detail (keys as in `profile/profile.example.json`): `full_name`, `short_name`, `role`, `company`, `legal_entity`, `mobile`, `landline`, `email`, `website`, `office_address`, `return_address`, `ref_prefix` (two or three capital letters from the company name plus a slash, for example "JSL/"; tell them what it is for: the reference on every letter and map), `company_description` ("a land and development company working in {county}"), `counties`, `brand_colour`, `logo`, `searchland_login`, `letters_folder`, `registers_folder`, `downloads_folder`, `map_style`, `programme`, `target_profit_on_sale`, `buildup_workbook`, `buildup_calculator`, `plain_english_level`.
- `profile/profile.md` from `profile/profile.example.md`, in their words: who they are, their business model, their deal rules, their programme's rules, any preferences they mention.
- `profile/private-terms.txt`: their name, surname, company name, phone numbers, email, address. The engine adds owners' names and site names as it works. This list stops any of it being shared by mistake.

## 6. Check the computer (do it yourself; tell the user only what they must approve)
The letter scripts need Python with a few libraries, and LibreOffice (free) to turn letters into PDFs.
- Check: `python --version` (or `python3`), `soffice --version` (or LibreOffice in Program Files), and `python -c "import docx, pypdf, PIL, numpy, cv2, scipy, openpyxl, fitz"`.
- Install what is missing. Windows: `winget install -e --id Python.Python.3.12` and `winget install -e --id TheDocumentFoundation.LibreOffice`; Mac: Homebrew (`brew install python libreoffice`) or the installers from python.org and libreoffice.org. Then `python -m pip install python-docx pypdf pillow numpy opencv-python-headless scipy openpyxl pymupdf`.
- Before each install, tell the user in one line what it is and that Windows or Mac may ask them to click Yes: "I'm installing LibreOffice, a free office program I use to turn letters into PDFs. If a box asks for permission, please click Yes."
- If an install cannot be done from here, give them the exact link and the one button to click, then check again.

## 7. Make the letterhead and site map template
- If they gave a Word letterhead: copy it to `profile/letterhead.docx` and add the placeholder lines the scripts look for, in this order in the body: `Our ref: [Reference]` with `[Date]`, then `[Recipient name]`, `[Company or organisation]`, `[Address line 1]`, `[Address line 2]`, `[Town]`, `[Postcode]`, `Dear [Name],`, `[Subject of the letter]`, `[Type your letter here.]`, `Yours sincerely,`, `[Signature name]`, `[Signature role]`. Then run `python tools/make_letterhead.py` only for the site map, or build the map sheet the same way.
- Otherwise run `python tools/make_letterhead.py`, which makes both from the profile and logo.
- Make one sample letter to "Mr A Sample, 1 Example Road, Sampletown, AB1 2CD" with the standard wording, open it for them, and ask: "Here's how your letters will look. Is anything wrong, such as a phone number or the logo size?" Fix and repeat until they are happy. Delete the sample afterwards.

## 8. Show them what it can do (the "what can you do" answer too)
Explain in plain words, one short paragraph each, then offer to start:
1. **Site review**: "Give me the title number, the address SearchLand shows, and paste what SearchLand shows down the left side, or send its report. I'll read the council's assessment of the land, its planning history and two nearby examples (one approved, one refused), the council's other documents, and check whether it's listed for sale and every constraint I can check from my side. If SearchLand shows a company owner, I'll check the company. A private owner's name and any option on the land are only on the title register, so once you buy it (about £7), I'll read it. Then I'll tell you plainly whether it's worth pursuing and why, and what I couldn't check."
2. **Appraisal**: "Say appraisal and I'll work out what the land could be worth with planning: local sold prices, the council's affordable housing rules, building costs from your calculator, the council's charges, and the best mix of homes. Then I'll prepare your BuildUp submission."
3. **Letters and calls**: "Say letter and I'll write to the owners on your letterhead with a map of their land, ready to print. When they ring, I'll give you a script to read from."
4. **Memory**: "I keep notes on every site, council and agent in this folder, so next time I start where we stopped and get faster with each council."
Then explain how to start each session, in plain words: "Before each new chat, choose Sonnet 5.5 and High in the model menu under the message box, then type /advisor opus and check it says the advisor is set to Opus. Use one chat per site: start a new chat for each new site. I keep notes in this folder, so each new chat already knows everything we've done." Then: "Shall we start with your first site? Give me the title number, the address SearchLand shows and the SearchLand panel."

## 9. Record
Run `python tools/build_index.py`. Tell the user setup is done in one line.

## Changing details later
"Change my phone number", "new logo" and similar: update the profile, rebuild the letterhead with `tools/make_letterhead.py` (or edit their own), make a sample, and confirm.
