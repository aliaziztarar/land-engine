---
name: letters
description: Every approach to a landowner, executor, agent, promoter or introducer: letters to owners as finished PDFs on the user's letterhead with a site map, emails to agents and promoters, phone call scripts in teleprompter form for first and follow-up calls, short follow-up texts, the polite decline, and replies to introducers. Use whenever the user says letter, write to, email, call, what do I say, they rang, or reply.
---

# Letters, emails and calls

## What this skill produces
- **Letter to an owner**: a finished PDF on the user's letterhead (and their back page, if they have one), with the site map in the form the user chose at setup (`profile/profile.json`, `map_style`): `separate` (a one page map sheet with the land outlined in red, the default), `on_letter` (the map printed on the letter itself, below the text: run `make_map.prep` on the screenshot, add `"map_png"` to the job; the script shrinks the map until the letter fits one page, and if it still does not, drop the thanks line, then shorten the conversation paragraph), or `none`. Saved to the letters folder in `profile/profile.json` as `<letters_folder>\<TITLE> - <site short name>\<TITLE> - <owner full name>.pdf` and `<TITLE> - Site map.pdf`. The letter and map carry the same reference (`ref_prefix` + title number). The user prints, signs, hand addresses the envelope and posts it. Never just text in the chat.
- **Email** to an agent, promoter, developer or introducer: drafted in the chat (a message card if the session has one) for the user to send from their business address.
- **Call script**: teleprompter form (`calls/`).
- **Short text or email to an owner** after contact: plain, one ask.

## Before drafting anything
1. Read the site note. Everything in the letter comes from the verdict and the register there. The register must have been read; the letter goes to the names on it, at the addresses on it. If it has not been bought, ask the user to buy it first (one plain sentence, see the searchland skill).
2. Read `rules.md` (all of it is binding) and `profile/profile.md` (the user's business model, deal rules and any wording rules of their own).
3. Choose the variant and read its example:
   - **Standard** (owner, clean register, no planning history): `examples/standard.md`.
   - **Owner with planning history** (an application, appeal or promotion in the past): the standard letter plus one short paragraph that shows we know the land (what went their way at appeal, what has changed since) without stating the council's current view or a number of homes.
   - **One field of a larger holding**: add "To be clear, it's only this one field I'm writing about, not the rest of your land at <name>." The map outlines that field only.
   - **Developer notice or restriction on the title**: `examples/under-option.md`. Asks whether the agreement has run its course; says plainly we are not asking them to cut across one still in force. Never held back on the assumption that the agreement is live.
   - **Executor or trustees**: `examples/executor-trustees.md`.
   - **Company owner**: to a named director (Companies House), company on the next line.
   - **Owner who lives on the land**: one line acknowledging it is their home and that anything discussed would take that fully into account.
   - **Joint owners**: a separate letter each when they live apart, each saying the other has been written to in the same terms; one joint letter when they live together.
   - **Promoter or developer holding the site; land agent acting for the owner**: email, `examples/promoter-email.md`.
   - **Decline** (a site the user cannot take): `examples/decline-email.md`.
   - **Introducer or sourcer**: `examples/introducer-reply.md`.
4. Two kinds of letter by route: a **now** letter (a site that can go to application soon) and a **pipeline** letter (land likely to be allocated in the next plan, where the interest is a long relationship). The wording rules are the same; only the one or two site specific lines differ.

## Producing the files
```
python .claude/skills/letters/scripts/make_letter.py job.json
python .claude/skills/letters/scripts/make_map.py <TITLE> "<address line>" <acres> <map png> "<site folder>" --date "<date>"
```
`job.json` is a list of letters (ref, date, outpdf, addr lines, salut, subject, body paragraphs); see `examples/job-example.json`. The script fills the letterhead, signs with the profile's name and role, refuses to make a two page letter, and adds the back page if the profile has one. The map picture comes from SearchLand's Screenshot map button (searchland skill); the script removes SearchLand's round marker, makes the outline thick and red, crops round the site and fills the map sheet. For part of a title, cover the rest of the outline and write "(this field only)" after the acreage, marked as our own measurement. Check the map before saving it: outline red and clear, no marker, site filling roughly a third to a half of the width, large sites shot wider. Save both into the site's folder on the user's computer and log the letter in `knowledge/contacts/log.md`.

If the scripts cannot run on this computer (no LibreOffice or Python), the setup skill installs them; tell the user in one line and run setup's check.

## Follow-up
Four weeks after posting, a short second letter; three contacts over three months; then stop unless something changes. A returned letter is information (the owner moved or died). Follow-ups are the user's decision; offer, don't send. Offer a SearchLand alert on parked titles.

## Messages to owners after contact
Short, plain, specific; one ask; no flowery politeness; never suggest the owner might be doubtful; never inflate the team ("the planning team we work with" is honest). After a missed call: a brief email saying you tried, then call again the next day at a different time; findings stay out of email. Never put a figure in writing before the programme has reviewed the appraisal.

## Record
Site note status: "letter written <date>, posting unconfirmed", then "letter sent <date>" when the user confirms. Contacts log row; index rebuilt; the owners' surnames and site names added to `profile/private-terms.txt`.

## Next step
After letters: "When they ring, would you like a call script ready? I can prepare it now." After an email to an agent: "Shall I note a reminder to chase in a week?" After a call: "Would you like me to update the appraisal with what they told you?"

## Learned
- A SearchLand screenshot taken while the map is still moving comes out blank; wait after zooming.
- A map showing a whole multi-parcel holding confuses owners; outline only the field being written about.
- Return addresses on envelopes help returned letters reach the user (`profile/profile.json`, `return_address`).
