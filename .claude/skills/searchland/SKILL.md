---
name: searchland
description: How to use SearchLand (app.searchland.co.uk) for a site, either by asking the user to paste the title panel or send the title report, or by working it in the session's browser when one is signed in: reading a title's panels, finding the titles under a SHELAA outline, the call for sites layer, planning searches for precedent and S106 evidence, planning documents, alerts, and a sharp map screenshot for letters.
---

# SearchLand

SearchLand is a paid tool on the user's own account. It is used one title at a time, as a person would. Never bulk scrape it, never store its data in bulk, never share a session.

## The easy way: the user pastes the panel or sends the report
Most users are not technical. The quickest start, which works on any computer, is to ask:
"Please open the title in SearchLand and click on the land so the panel opens down the left side. Then click anywhere inside that panel, press Ctrl and A, then Ctrl and C, and paste it here. If you'd rather, click Export report and send me the PDF."
(On a Mac: Command instead of Ctrl.) If they say the panel will not select, ask for the report. If they send screenshots instead, thank them, read what is visible, and ask for the paste or the report for the rest, because pictures cost more to read and miss text.

Read the paste in full. It carries: ownership, considerations and constraint layers, title metrics (area), planning applications, local plan status (supply and delivery test), local plan policies, neighbourhood plans, SHLAA and call for sites entries, charges for company titles, nearby sales.

## When the session has a browser signed in to SearchLand
Use the browser tool the session has (the Claude desktop app's built-in browser, or Claude in Chrome). Sign in with the method in `profile/profile.json` (`searchland_login`); if the sign in page appears and needs the user, ask them in one line to sign in and say done.

Open a title directly: `https://app.searchland.co.uk/?titleNo=<TITLE>&custom=false` (add `&lat=<lat>&lng=<lng>&zoom=18` to position the map). Wait about eight seconds. Read the panel as text (the page text tool or `document.body.innerText`), never by screenshot. Collapsed headers open by clicking their label text. A page left open for hours drops to the login page; check before reading.

## SHLAA panel and layer
- An entry reads like "Ref: 84 | Published: <date> | <name> | 16 units | 1 to 5 years". The ref may lack leading zeros; "units" is the modelled delivery rate per year, not the capacity.
- Turn on the SHLAA layer in the Control centre. "More info" on a site highlights its outline; clicking the land inside the outline switches the panel to that title (the address bar shows `titleNo=`). Repeat for each part; one site often spans several titles.
- Colours: green positive, orange neutral, red negative; blue is the current call for sites (submitted, not yet assessed).
- The "Call for sites" tab in the same panel lists submissions with the council's reference and name; the council's own register usually gives the area and uses.

## Planning searches (precedent and S106 evidence)
- Location: a radius or drawn area around the site if the tool offers it; otherwise select the council or the parishes and wards within the distance wanted, and check the selection covers nothing extra.
- Decision: for precedent, every decision type including refused, withdrawn and undetermined; for S106 evidence, "is one of" Approved.
- Dates: decision date (not received date) for S106 evidence; for precedent, both lodged and decided within the period.
- Type: "is one of" or "contains any" Full, Outline, Reserved Matters, Permission in Principle. Never "contains all" (it needs one application to be every type and returns nothing).
- Size: for precedent, schemes of about the same number of homes as the subject (two examples only, one approved, one refused); greater than 9 for S106 evidence. If there is no dwellings filter, search "dwellings" and pick by hand.
- List view gives reference, address, homes and decision; open each on the council portal for the documents.
- Alerts can be set on a title (a notice removed, a new application). Offer one when a site is parked.

## Planning documents
From a title's planning list, open an application; its Documents tab lists files in pages of 10. Do not read a document in SearchLand's viewer. Use the viewer's download button (top right); the file lands in the user's downloads folder (`profile/profile.json`, `downloads_folder`). Bring it into the session, convert it to text (`.claude/skills/documents/SKILL.md`) and read the text. If downloading is not possible, the viewer's text is in `document.body.textContent` once loaded.

## Buying a title register
The register is HM Land Registry's own document; SearchLand only resells it, and the user decides whether to buy. Never assume the user will buy it, and never buy it yourself. Use the free GOV.UK property summary first (see the site-review skill, step 2). If the user chooses to buy through SearchLand, ask: "Please buy the title register for <TITLE> in SearchLand (about £7, the Land Registry button on the title) and tell me when it has downloaded." Then find it in their downloads folder yourself. If SearchLand says the Land Registry download failed, the same register can be bought on GOV.UK's "Search for land and property information".

## Map screenshot for a letter
The "Screenshot map" button (right hand toolbar, camera icon) saves `map-screenshot-<timestamp>.png` to the downloads folder (first as a `.tmp`; wait a few seconds). Its sharpness depends on the window size, so:
1. Make the browser window large first (about 2400 by 1600 if the browser tool can resize it).
2. Open the title with lat, lng and zoom (18 for sites over about 5 acres, 19 for small ones; large multi-parcel titles need a wider shot). The map recentres on the whole title after loading, so zoom in after it settles and wait about seven seconds.
3. Turn off the coloured layers ("Layers on map" On/Off) so only the title outline shows; close the legend.
4. Click "Screenshot map" with a real click; wait six seconds. A shot taken while the map is moving comes out blank; retake it.
5. Put the window size back. Bring the PNG into the session and tidy up the downloads folder (delete the leftover .tmp and PNG), telling the user what was removed.
If there is no browser, ask: "Please click the camera icon on the right of the SearchLand map (Screenshot map) with only the title outlined, then tell me when it has downloaded." Never print SearchLand's own PDF export as the map; it carries their branding.

## Learned
- `?titleNo=` opens a title directly; no search needed.
- SearchLand's planning list can lag the council portal; cross-check references.
- The area for the map sheet is in the panel text "Title metrics Area N acre".
- Green Belt parcel and scores (19 November 2026): Control centre, Strategic land, tick Green Belt Review. A Green Belt Review tab appears; choose Overall, then click the land. The popup gives the council's parcel reference and the score for each Green Belt purpose (a sprawl, b merging, c countryside, d setting, e regeneration), which is the evidence for a grey belt argument. The same click lists the SHLAA entry and any allocation on that spot, which shows whether a title is inside a proposed allocation.
- A SHLAA card with no Suitable, Available or Achievable lines, a name like "within the curtilage of <house>" and one unit is usually a small permission record, not an assessment of the land around it, and SearchLand draws its outline over the whole title. The Source button may open a window that closes at once; do not rely on it.
- The browser pane is shared with any worker running at the same time: workers can change the active tab, so name the tab id when reading SearchLand.
