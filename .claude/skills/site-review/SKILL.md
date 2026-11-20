---
name: site-review
description: Research a land site from every angle and give a verdict. Use whenever the user gives a title number, a SearchLand link, pasted SearchLand panel text or a SearchLand title report, a SHELAA or call for sites reference, an address, a postcode or a landowner's enquiry, or asks to look at, analyse or review a site, whether it is worth pursuing, who to approach, what the planning history means, or to screen a council's sites.
---

# Site review

The user gives one line: a title number and the SearchLand panel pasted in (or the SearchLand report). SearchLand has already given them the facts: the title, 50 or more constraint layers, the SHLAA entry, supply and delivery test, the planning history list. They can see all of that themselves in minutes. This skill's job is the layer above it, the work an experienced planning consultant does:

1. **Judgement**: read what sits behind the facts (decision notices, officer reports, appeal decisions on the site and the titles around it) and say what they mean for this site today: which refusal reasons still stand, which have fallen away and why, and how the rest could be resolved.
2. **Council memory**: read every earlier finding about this council (the council note and every earlier site note in the same council) and judge this site against all of it, then add what this site teaches, so each review in a council is sharper than the last.
3. **The documents SearchLand does not reach**: the local plan and its evidence, the neighbourhood plan, older SHLAA rounds, committee papers, parish minutes: anything about the site, its road or the area it sits in, including area-wide reasons other sites were refused that would apply here even when this site has no history of its own.

So: never restate the SearchLand panel back to the user as if it were a finding, and never spend effort re-establishing what it already shows clearly. Take its facts as given (note them in the site note), confirm only what is ambiguous or important to the verdict, and put the effort into reading, weighing and remembering. Do the work yourself; the user is asked only for what only they can do.

Read `checklist.md` (the coverage checklist), `report-template.md` (what the user receives) and `glossary.md` (plain words for every term) in this folder before starting. Read `knowledge/learned-checks.md` too.

Throughout: the advisor (this conversation) decides and judges; the worker (`.claude/agents/worker.md`, Sonnet) does the reading and fetching from written briefs. Brief templates are at the end of this file. Send independent briefs at the same time so the user is not kept waiting.

Tell the user in one plain line what you are doing as each stage starts ("I'm reading the council's assessment of this site now."), so they can follow along.

**Speed rule.** The user wants a site done in minutes, not a quarter of an hour. So:
- Never send one worker a long list of jobs. One brief, one job, a few minutes at most. Send up to four small briefs at the same time instead.
- Every brief says: "Write each finding to the file as soon as you have it, so partial work survives. Stop after 4 minutes and report what you have."
- If a worker has not reported after about 5 minutes, stop waiting. Do the quick checks yourself (Companies House pages, a web search, the council page in the browser) and mark the rest "could not check".
- If a page refuses the fetch tool, open it in the user's browser at once. If the browser is also blocked (blank map, "Access denied", a sign in page), do not retry: record "could not check", and ask the user to open that one page and paste what it shows.
- A long wait is a failure. A verdict with honest "could not check" lines delivered quickly is better than a complete one delivered late.

## 0. Before anything

1. Read the site note if one exists (`knowledge/sites/<TITLE>.md`) and start from its open items; never redo work it holds. Read the council note if one exists. If not, the worker builds it in step 5 before any judgement is made, because every judgement depends on it.
   **Council memory**: from `knowledge/index.md`, list every earlier site note in the same council and read their verdicts, precedent summaries and documents findings, and the council note's behaviour profile ("Appeal and refusal patterns", "S106 patterns seen", "Learned"). Keep them in mind for every judgement below, and say in the report where an earlier site changes the reading of this one (for example "the same local gap policy was the reason <earlier title> was refused; this site sits inside the same gap").
2. Get the starting information. The best start is SearchLand's own data for the title. If the user has given only a title number or address, ask once, plainly:
   "To start, please open the title in SearchLand, click on the land so the panel opens down the left side, then select everything in that panel (click inside it, press Ctrl and A, then Ctrl and C) and paste it here. Or click Export report and send me the PDF. Either works."
   If the session has a browser that is signed in to SearchLand, open the title yourself (`.claude/skills/searchland/SKILL.md`) and do not ask. If neither is possible, carry on from public sources and mark the SearchLand items "could not check" until the user pastes the panel.
3. Two screening questions before deep work, answered from the SearchLand data or the map: does the land have its own frontage to a public road (if not, who owns the strip between), and is it over about half an acre (under that it is a plot, not strategic land; say so and stop unless the user wants it anyway). A hard constraint over the whole site (functional flood plain, SSSI, ancient woodland, a live allocation already built out) can also end the review early, with the reason recorded.
4. Decide the route the site is on, because it sets what matters most:
   - **Application now**: the council is short of housing land, the site is small to medium with its own access; planning history, precedent and constraints decide.
   - **Pipeline**: land likely to be allocated in the next local plan; the plan stage, the council's evidence and competing promoters decide.
   - **Enquiry**: an owner came to the user; identify the land first, then the owner's history and what they want.

## 1. Identify the land

### From SearchLand data (pasted panel or report)
Extract: title number, address, area in acres and hectares, tenure, ownership type (private, or company name and number), the Considerations list, every constraint layer the report covers, the SHLAA panel entries, call for sites entries, planning applications count and list, local plan status (adopted and emerging, five year supply, Housing Delivery Test), local plan policies, neighbourhood plans, charges and mortgages, leasehold, nearby sales.

Traps:
- The SHLAA panel's "units" figure is the council's modelled **delivery rate per year**, not the capacity. The capacity is in the council's own assessment (step 4). Never appraise on the units figure.
- The SHLAA reference may drop leading zeros (84 for 084).
- A SHELAA site is often bigger than one title. Compare the council's site area with the title area; if they differ, find the other titles and record every title in the site.
- "Ownership" shows the freeholder; "Leasehold info" shows a tenant. A long lease gives the tenant possession and the freeholder can only sell the reversion; if the lease covers the whole field, park unless both can be brought together.
- Several neighbouring titles with identical planning history usually means one old parcel later split, not one owner.

### From an enquiry (postcode, address, screenshot, house name)
1. Fix obvious postcode typos. Check a named house on listing sites and whether it is listed (Historic England, British Listed Buildings).
2. Find the title free: SearchLand by postcode and click the parcel; or GOV.UK "Search for land and property information" (search-property-information.service.gov.uk), "Search by map", clicking inside the parcel, choosing not to include buildings for a field (including buildings returns the house title first). A postcode search lists only titles with an address. A UPRN is an address id, not a title number.
3. Compare the registered owner with the enquirer's name. A mismatch is common (family land, an estate, let property). Do not name the registered owner to the enquirer; ask them for the title number.

### From a SHELAA or call for sites reference
SHELAA sites have no address. Search the village in SearchLand, turn on the SHLAA layer, use "More info" on the site so its outline highlights, then click the land inside the outline: the panel switches to that title. Repeat for every part of the outline. Sum the title areas against the council's hectares. Check the planning list before buying registers.

### Batch screening a whole council
When the start is a council, not a site: the worker parses the assessment appendix into a sheet, one row per site (name, ref, settlement, parish, area, developable area, use, every constraint tick, greenfield or brownfield, promoted by owner or developer, developer interest, available now, could commence in five years, phasing, council summary). Filter: promoted by the landowner, not by a developer, no developer interest, available now, greenfield or mixed. Major flags: conservation area, listed building, historic park, National Landscape, SSSI, SINC, ancient woodland, flood zone, public open space, local gap, covenants or tenants, access or ransom, ownership issue, contamination, employment land. Minor flags: TPO, SPA or SAC payment, pollution, minerals, infrastructure. Grades: A clean and next to a main town or key service centre or inside the boundary; B clean and next to a rural village; B+ passes with only a conservation area or listed building flag, inside or partly inside the boundary; C passes with a serious flag; Out fails. Meanings to explain: "phasing if permitted" is a build-out guess, not a waiting period; "unlikely to commence in five years" is the council's view, not a bar, and a good sign that nobody has picked it up; "no developer interest" was true only on the date of the call for sites. Keep a tracker (title, address, acres, refs, homes in any draft allocation, assessment verdict, owner, register bought, route, earliest application, letter angle, what is still needed); prioritise by homes and by what is missing.

## 2. Who owns it, and is anyone already in

### The register comes first
Rule: on any site with a developer application, appeal, promotion or recorded developer interest in about the last seven years, the register (about £7 from SearchLand or GOV.UK) is read before any planning document; on every other site, before any letter. The register belongs to HM Land Registry (SearchLand and GOV.UK only resell it), and buying it is the user's decision and money; never buy it, never assume they will, and never describe a title as owned by a named company unless a register or a document says so. First use the free GOV.UK property summary (search-property-information.service.gov.uk): it shows the price paid and its date, whether restrictive covenants and easements exist, and the description. A recent price paid means the land has been sold, so the owner named in an older council assessment is probably out of date (the assessment's owner is the owner at the call for sites date). Then say plainly what the register would add and what is unknown without it, and ask once: "The register for <TITLE> costs about £7 from GOV.UK. It would show the current owner, any lender, and any developer notice. Would you like to buy it? If so, tell me where it saved." If they decline, finish the review and mark every title and ownership line "could not check". Reading method: `.claude/skills/documents/SKILL.md`. What decides the site:
- A unilateral or agreed notice, or a restriction, in favour of a developer, promoter or their lender: an option, promotion or sale agreement exists or existed. A restriction is stronger than a notice. Do not try to option the land. Options often run five years plus extensions, so a notice can outlive a dead agreement; only the owner knows. The free GOV.UK summary does not show notices.
- Routine restrictions (tenants in common, two trustees, a family member's consent): every owner or trustee must sign; each gets their own letter.
- A lender's charge (an equity release lender suggests older owners; lender consent needed later).
- "Transfer contains positive and/or indemnity covenants, copy filed under <title>": possible overage owed to a previous seller. Do not state it as fact until the filed document is read (official copy, form OC2).
- A utility deed: usually an easement for a cable or pipe plus a covenant not to build over it; order the filed copy before any layout, because it can remove a strip.
- Rights reserved over a neighbour's strip ("at all times and for all purposes") can defeat a ransom; rights others hold over this land constrain the layout.
- "No price stated" on the entry: inheritance or a family transfer. An assent is executors passing land to the heir. A newly created title number means the land was unregistered until then. Check whether an owner's address is the site itself (someone lives there).
- Many owners of small plots suggests a land banking scheme; hard to deal with.

### Owner research (worker)
- Elderly or possibly deceased owner: public obituaries; GOV.UK Find a will (will and grant of probate, £1.50 each); write to the executors (all must sign; they need the grant before they can sell).
- Company owner: open the company's Companies House pages yourself (overview, people, charges, filing history; the adviser can do this in a few minutes). Then do a plain web search of the company name, the registered address and its postcode, and the directors' names, because the family or the same address often runs a separate trading business (haulage, farming, building) that shows how they work and who they deal with. Say exactly what was found and what was not; "no promoter found" must never read as "nothing found on the owner". A trading business at the same postcode is a lead, not proof of the link: confirm it at Companies House before calling it the same family. A dissolved company's land passes to the Crown (bona vacantia) and can be bought from the Government Legal Department. A members' voluntary liquidation is a planned closure; search the former directors for a successor company. A property holding SIC code does not mean developer interest.
- Business tenants on the land: security of tenure under the Landlord and Tenant Act 1954 unless contracted out; redevelopment can end it with notice and compensation.

### Promoters, agents and developers
- Any agent named in the council's assessment or on applications: check `knowledge/agents/` first, then their website and Companies House. Classify: planning consultant acting for the owner (owner still free); land promoter or housebuilder (agreement likely; check the register); the owner's own company; a land agent (surveyors acting for the owner).
- "Developer interest: yes" in an assessment means someone had spoken to the owner on that date; it does not say who or whether anything was signed.
- Resubmitted in the latest call for sites: someone is paying to promote it now. Assessed positive before and absent from the latest call for sites: the promotion has probably stalled, often the best target.
- Examination representations name promoters and show how hard they pushed (step 8).

### Existing agreements: never induce a breach
A contract for land binds only if written, containing all terms and signed by both sides; registering it does not make it binding. An owner who walks away from a signed option can be sued, and a second party who knew of the first contract can be sued for inducing the breach. The owner is free only where nothing binding was signed, the agreement expired, a break clause was used, the agreement covers only part of the land, or the contract fails the writing rules; only the owner's solicitor can say. Write to the owner as to anyone, ask whether anything is signed and when it ends, and never make an offer conditional on them breaking an agreement.

## 3. Constraints baseline and depth of research

Start from the SearchLand data. For each category in `checklist.md`, decide:
- **Clear**: SearchLand and the council's assessment both show nothing, and nothing in the site's history suggests otherwise. A light confirmation is enough (one official map or document per category).
- **Ambiguous or present**: anything flagged, partly covering the site, close to the boundary, or where SearchLand and the council disagree. Full research on that category: the official source, the council's own evidence document, and how the council has treated the same constraint in decisions (step 7).
- **Always researched in full, whatever SearchLand says**: designations and local character protections (conservation area and its appraisal, listed buildings and their setting, National Landscape, Green Belt and its review, local gaps and important open areas, landscape character and sensitivity, local green space in a neighbourhood plan, tree preservation orders, locally listed heritage assets), because these decide most refusals at village edges and are often missing from automated layers.
Record each finding with its source and date in the site note.

## 4. The council's assessment of the site (worker)

Brief the worker to find the site's entry in the council's land availability assessment (SHLAA, SHELAA, HELAA and SLAA are the same kind of document) and in every earlier round, using the council note for the document and the reference format. If the text is not in `sources/`, the worker fetches, converts and files it, then extracts the entry with `tools/shelaa_entry.py`.

Fields, verbatim where the document gives them: name and address; parish; landowner; consent; legal constraints; agent; developer interest; nominated capacity; modelled capacity; current use; availability date; site area; brownfield or greenfield; description; surrounding uses; planning history; every constraint row with its mitigation and impact text; the suitable, available and achievable conclusions; the modelled schedule (net developable area, homes, density, delivery rate, years). Earlier rounds: the reference and verdict in each, and whether the verdict changed and why.

SearchLand's "source" link often opens the assessment at the right page; when the user has pasted that entry, use it and only fetch the document for the earlier rounds. When the source link does not work (roughly four times in ten), the worker fetches the document. Earlier rounds matter: a site assessed negative in 2016 and positive in 2020 tells you what the council changed its mind about.

The advisor reads the whole entry. The sentence that decides a site is usually in a mitigation or impact column ("will change to unsuitable if adjacent sites are not brought forward"; "mitigation unfeasible for this site in isolation"; "nearby clustered sites could provide sufficient massing"). Reconcile nominated capacity, modelled capacity, net area and density with SearchLand's units figure and the title area.

## 5. Where the council stands (worker builds the council note; advisor reads it)

If the council note is missing or older than three months, the worker builds it (brief template B). The advisor then records for the site:
- **The plan ladder**: call for sites (nothing judged; no planning weight) > land availability assessment (positive, neutral or negative) > draft plan, Regulation 18 (preferred sites) > submission plan, Regulation 19 (proposed allocations) > examination > adopted plan (allocations, the only stage at which the council has decided to build there). Names vary; the process does not. Where the site sits on it.
- **SearchLand colours**: the coloured SHLAA layer is the last assessment (green positive, orange neutral, red negative); blue is the current call for sites. Green only: assessed positive and not resubmitted, often the best target. Blue only: new land someone is working on. Green and blue: still being pushed, expect competition. Red and blue: rejected and resubmitted, a long shot.
- **Five year housing land supply** from the council's live statement (open it in the browser; cached copies can be a year old) and the **Housing Delivery Test**. Below five years, or a test result below 75 percent, the tilted balance applies: permission should be granted unless the harm significantly and demonstrably outweighs the benefits. Supply looks forward; the test looks back; a council can pass one and fail the other.
- **Settlement hierarchy**: the tier of the nearest settlement; a place not named in the hierarchy is countryside in policy terms. The settlement boundary, adopted and emerging.
- **Now or wait**: a council can refuse as premature only where the scale would undermine plan making. Small sites beside a draft allocation can go in now under the tilted balance; a site that is the allocation itself waits for the plan.
- Where a small operator can realistically get in: positive in the assessment but not allocated, with an owner or small agent behind it; allocated but stalled (the monitoring report and supply statement list every allocation's progress; "not started" is a lead); preferred sites at Regulation 18 before anyone has tied them up. Allocated sites in an adopted plan are usually already under option.

## 6. What the site could carry (advisor, from the council note and policy)

So the review already knows the shape of a scheme before any appraisal:
- **Affordable housing**: the policy percentage (and any different rate by area or for rural exception sites), the size of scheme at which it starts to apply (often 10 homes or 0.5 hectares, lower in some rural areas), the tenure split (for example social rent, affordable rent, First Homes, shared ownership), and whether a commuted sum is taken on small schemes. Quote the policy number and document.
- **Housing mix**: any policy or evidence (housing needs assessment) on sizes and types; bungalows, older people's housing, self and custom build percentages; accessible homes (M4(2) and M4(3)); nationally described space standard.
- **Density**: the council's expected density for the location, the density in the assessment's modelling, and what nearby approved schemes achieved (step 7).
- **Other policy obligations**: open space and play, biodiversity net gain (10 percent), nutrient or water neutrality, CIL rates, typical S106 items.
- **A first scheme range**: from the net developable area after constraints, a low and high home count with the affordable number at each, stated as a range with its assumptions. The appraisal skill turns this into numbers and the best mix.

## 7. Planning history of the site and its neighbours (worker, then advisor)

Worker (brief C): every application on the title and on every adjoining title, all decisions and dates, applicant and agent; for any refusal, withdrawal or appeal of any size on the title, and any of five or more homes next door, the decision notice, officer or committee report and appeal decision, converted to text. Search the council portal, SearchLand's planning list and Documents tab, plota.co.uk and planning.org.uk, because any one list can lag.

Advisor: read every appeal decision and every refusal report on the site in full. Then test **every reason, one by one**, against today, and write the result as a short table in the report: the reason as the council or inspector worded it; **still stands**, **no longer stands** or **stands but resolvable**; and why, with evidence (the supply position then and now, the plan then and now, a designation added or dropped, neighbouring approvals since, with references). For a resolvable reason, say how (a section 106 contribution, an affordable housing offer, a survey, a design change such as fewer homes or a landscaped frontage). This test is the most valuable thing the review gives the user. Sort the reasons into (a) real planning objections (character, landscape, sustainability, heritage, flood, access), (b) fixable omissions (no affordable offer, unsigned undertaking, missing survey, no viability evidence), (c) the policy context at the time (supply position, plan in force, any designation). Then say what has changed since. Refusal reasons age differently: "countryside, no need for housing" reasons fall away when supply is short; character, gap, heritage and landscape reasons persist. A refusal on principle is no to the land; a refusal on detail is no to that drawing. An undecided application usually waits on neutrality, S106, the plan, or an applicant who stopped pushing; read the latest documents before assuming.

## 8. Precedent review: how this council actually behaves (worker, then advisor)

Policy says what a council should do; decisions show what it does. This step is often the most valuable in the review.

**Scope (two examples only, no more)**: find exactly **two** planning applications near the site for the kind of scheme the site could carry (about the same number of homes, same kind of setting such as village edge or countryside): **one approved and one refused**. Start with the most recent decisions and work back; only go back as far as **10 years** if recent ones do not give a pair. Prefer the nearest to the site; if none within about 3 miles, take the nearest equivalent anywhere in the council area and say so. Do not list or read every scheme. Never more than two examples, whatever the council.

**Worker** (brief D): search SearchLand's planning search, the council portal and planning.org.uk for recent decisions near the site, newest first, until there is one approved and one refused example that fit the scope. For each of the two, give: reference, address, distance and direction from the site, homes, type, applicant and agent, date lodged, decision and date, officer or committee, appeal reference and outcome. Then read in full the officer or committee report (and the appeal decision if there was one) and extract: the reasons, the policies cited, the weight given to housing supply, what was said about character, landscape, gaps, sustainability, access and heritage, the S106 and affordable housing secured, and density. Write to `knowledge/sites/<TITLE>-precedent.md`.

**Advisor**: from the two examples (and the council note's earlier patterns), write a short behaviour profile for this kind of site. Say plainly that it rests on two examples and is a pointer, not a statistical pattern:
- What gets approved at the edge of settlements of this tier, at what size and density, and why.
- Which refusal reasons recur, and which of them the council wins or loses at appeal.
- How much weight officers and inspectors give the housing shortfall (tilted balance) against character and landscape.
- Whether committee overturns officers, in which direction, and on what.
- What S106 and affordable housing is routinely secured (feed to the appraisal).
- What each pattern means for this site: the arguments that will work, the objections to design out, and the size of scheme the council has shown it will accept.
Copy the reusable parts of the profile (not the site specific parts) into the council note under "Appeal and refusal patterns" and "S106 patterns seen", with references and dates, so the next site in that council starts with it.

## 9. Council document sweep (worker, then advisor)

The local plan comes first and matters most. Most local plans never name a small site, so searching for the site's name is not enough: identify every policy and map designation that covers the site's **location** (open countryside, settlement boundaries, local gaps, landscape or character areas, conservation areas, green infrastructure, minerals) from the policies map and the plan text, read those policies in full, and find the other sites in the same area the council refused or rejected under them, because a reason that defeated a neighbour defeats this site too even when this site has no planning history. Then look for the site, its field or farm name, its road, its SHELAA references and its parish in every council and parish document where a council writes about land in passing (brief E):
- every round of the land availability assessment and call for sites registers;
- local plan Regulation 18 and 19 documents, the consultation responses that name the site, the examination library (hearing statements, matters and issues, the inspector's report);
- the neighbourhood plan (made or emerging), its site assessment, housing needs survey, local green space and views evidence, and the examiner's report;
- conservation area appraisals and management plans; the local list of heritage assets; heritage impact assessments for allocations;
- landscape character assessment, landscape sensitivity and capacity studies; Green Belt, gap and settlement boundary reviews;
- the strategic flood risk assessment, water cycle study, surface water management plan;
- the infrastructure delivery plan, transport evidence, school place planning;
- the annual monitoring report and five year supply statement with its trajectory;
- open space, playing pitch and green infrastructure studies; ecological network maps;
- the county minerals and waste plan and safeguarding maps;
- planning committee papers and minutes, and parish council minutes, for the last three years.
For each mention: document, date, page, the exact words. For designations: whether the site is inside, adjoining or affected, and what the policy says. The advisor reads every mention and decides what it means.

## 10. Market and intelligence: is anyone already moving (worker, then advisor)

Brief F: search for the site and its owners in:
- property listings: Rightmove, Zoopla and OnTheMarket (land and farms for sale, and sold history near the postcode), landsale.co.uk, UK Land and Farms, the websites of local land agents and national ones (Savills, Strutt and Parker, Knight Frank, Carter Jonas, and the county's chartered surveyors);
- auctions: the main auction houses and the county's local auctioneers, and their past lots (legal packs often hold overage clauses and searches);
- news and the web: local news, parish newsletters and minutes, community groups' public pages, campaign groups opposing development, promoters' and housebuilders' "our land" or "current promotions" pages, planning consultants' case studies, and any public consultation website for a scheme on the land;
- company filings that name the land (charges, accounts of a promoter);
- the council's pre-application or consultation registers where public.
Record every hit with date and link. The advisor decides what it means: already on the market (someone has set a price; an agent is involved), sold recently (a new owner with a fresh plan, or a land banker), a promoter publicly working it (do not write to the owner over their head), local opposition (a planning risk to name), or nothing at all (the quiet site that is often the best target).

## 11. Closing the coverage checklist and hunting blind spots (advisor)

Go through `checklist.md` and `knowledge/learned-checks.md` line by line. Every line ends in one of: **checked** (finding and source), **not relevant** (one line of reason), or **could not check** (what was tried, why it failed, and one plain sentence of what the user can do). Then ask, deliberately, what a hostile planning officer, a neighbour, a highways engineer, an ecologist and a solicitor would each raise that is not on the list; research anything new; and if it turned up something real, add a one line check to `knowledge/learned-checks.md` (category, what to look for, where), so every future site is checked for it.

Always name the risks the user has not raised: ransom strips and landlocked parcels (the holder of the only access can take about a third of the uplift, Stokes v Cambridge; a council holder must get best consideration and is slow); easements and utility deeds; occupiers living on the land; every owner having to sign; income the owner already gets from the land; overage owed to a previous seller; minerals safeguarding; best and most versatile farmland; surface water and flood zones clipping a corner; listed buildings and their setting; neutrality costs and delay; the cost of the next planning step against the likely number of homes; a promoter or opposition already active.

**A council as landowner.** When a title in the site belongs to the council, keep its two roles apart: as planning authority it wrote the policy, as landowner it decides what to sell or allow. Never state that the council refuses, blocks or holds a ransom position unless a council paper, minute or reply says so; until then it is "an open question to check", with the evidence (policy wording, the inspector's words, the title plan) set out neutrally. Check which parcel holds the road frontage and whether a neighbouring permitted site gives another route before calling access a problem. A policy that "allows a possible access road" across protected land is a limit on how, not a refusal.

## 12. Verdict and approach (advisor)

One of:
- **Approach the owner**: register clean or no live interest; a credible route (application now, allocation in the next plan, or both); the precedent supports a scheme of this kind. Next step: the letters skill.
- **Approach the agent or promoter**: a promoter demonstrably holds the land (register, examination statements, current call for sites, their own website). A joint venture email (letters skill): we fund and run planning at our own cost and risk; they share in the value on sale; no upfront sum; no figures until the programme has reviewed the appraisal; never mention other sites.
- **Park, with a reason and a trigger**: for example "promotion notice dated 2024; set a SearchLand alert on the title; revisit if the notice comes off or at Regulation 19".
- **Drop, with a reason**: hard constraint; landlocked; precedent shows the council and inspectors consistently refuse this kind of site for reasons that still apply; plot too small for the model.

Order of approach: owners first, agents and promoters second. A developer's notice is not by itself a reason to hold a letter (the agreement may have ended, and the letter asks), but when a promoter demonstrably controls the land, do not write to the owner over their head. Viability screen: the model works only when the planning uplift is large compared with the planning cost; a small urban plot with a long refusal history is a job for a local planning consultant, and the decline email says so kindly.

Cluster versus assembly: **land assembly** is control of adjoining plots so they become one site with one entrance and one application; the plots must touch. A **cluster** is separate sites in the same area that come forward together and share the cost of something none could afford alone (a footway, a bus extension, a junction). A cluster is moderately strong through the local plan (one allocation policy can make each pay its share) and weak through applications (each judged alone unless one application covers all, or a section 106 pools the money). Approach all owners in a cluster in the same week, never tell one what another is offered, and take a proposed cluster or assembly to the programme before approaching a connecting plot.

## 13. Report to the user

Use `report-template.md`: detailed findings first, section by section, each finding with its source; then what they add up to; then the verdict in a few plain lines; then the coverage checklist; then "What I need from you" (only things only the user can do, each in one plain sentence); then the offer of the next step. Explain every planning term the first time it appears. Never assume something "goes without saying"; if it mattered to the verdict, it is written down.

## 14. Record

Update `knowledge/sites/<TITLE>.md` (template below), the precedent file, the council note, any agent note, `knowledge/learned-checks.md` if a new check was found, the contacts log if anything was sent, and `profile/private-terms.txt` with the site's place names and the owners' surnames. Run `python tools/build_index.py`. Facts only, in the template headings; no chat narrative; inference marked as inference.

## 15. Offer the next step

End with one line offering what naturally comes next, for example: "Would you like me to prepare the appraisal for this site now, so we know what it could be worth?" or "Shall I write to both owners now? I'll need about two minutes per letter." If the verdict is park or drop, offer to set a reminder or to look at the next site.

## Learned

- A council's call for sites list is often an interactive map from a consultation supplier (for example oc2.uk). It can load blank or return "Access denied" to automated browsing. Try it once; if blocked, ask the user to open the council's link and read what it shows for the site, and record "could not check" meanwhile.
- A SHLAA "developer interest: No" is a snapshot at the call for sites date. Later council monitoring reports can say more ("previous discussions with promoter"); read the council's latest housing delivery report for every allocation. Allocated, stalled and unapplied is a lead, but expect the owner to have advisers.
- A site that is an adopted allocation is a different job from a positive assessment: read the allocation policy in full for access, buffers, open space and contamination requirements before anything else, and say so in the first reply.
- Do not send one worker eight jobs (one such brief ran 13 minutes, then was lost when the session restarted).

## Worker brief templates

Fill every angle bracket. Keep each brief to one job. Always name the output file and say: "Write findings to the file as you go. Stop after 4 minutes and report what you have." Also say: "If a step fails, write what you tried and why it failed, then carry on."

**A. Assessment entry**: "Council <name>. Find site <ref> (<name>) in the land availability assessment <document name, URL, year> and in every earlier round. If the text is not in sources/<council>/, fetch it, convert it to text, save it there with the URL and date on the first line. Extract the fields listed in step 4 of the site-review skill, verbatim. Write to knowledge/sites/<TITLE>-assessment.md."

**B. Council note**: "Build knowledge/councils/<council>.md in the council note template in the site-review skill: adopted plan and date; emerging plan stage and dates; call for sites dates and register URL; five year supply figure, base date and source URL (from the live page); Housing Delivery Test result and year; settlement hierarchy tiers; the tier of <settlement>; land availability assessment documents (names, URLs, years, reference format, definitions); affordable housing policy (percentage, threshold, tenure split, policy number); housing mix and space standard policies; density policy; CIL charging schedule rates or 'no CIL' with the source; nutrient or water neutrality; landscape designations used; county council for roads, minerals and schools; planning portal URL and any errors seen; pre-application fees."

**C. Site and neighbour history**: "List every planning application on title <TITLE> and on every adjoining title (use SearchLand's planning list, the council portal at <URL>, plota.co.uk and planning.org.uk). For each: reference, date, applicant, agent, description, decision and date, appeal reference and outcome. Download and convert to text the decision notice, the officer or committee report and any appeal decision for every refusal, withdrawal or appeal on the title, and for any application of 5 or more homes on an adjoining title. Write the list and the texts' locations to knowledge/sites/<TITLE>-history.md."

**D. Precedent**: "Find exactly two planning applications near <site, postcode, grid or coordinates> for about <n> homes in a similar setting: one approved and one refused, taking the most recent decisions first and going back no further than ten years (<date ten years ago>). Use SearchLand's planning search, the council portal and planning.org.uk. If none within about 3 miles, take the nearest equivalent anywhere in <council> and label it. Give the fields in step 8 of the site-review skill for each, then read each officer or committee report (and appeal decision) in full and extract as step 8 says. Never more than two. Write to knowledge/sites/<TITLE>-precedent.md."

**E. Document sweep**: "Search the documents listed in step 9 of the site-review skill, for <council> and <parish>, for these terms: <site name>, <field or farm name>, <road>, <SHELAA refs>, <title number>, <parish>. For each mention give document, date, page and the exact words. Also record whether the site is inside, adjoining or affected by each designation those documents define, with the policy. Write to knowledge/sites/<TITLE>-documents.md."

**F. Market and intelligence**: "Search the sources in step 10 of the site-review skill for <address>, <postcode>, <field or farm name>, <owner names>, <title number>, <SHELAA ref>. Record every listing (live or past), auction lot, news item, promoter or developer page, consultation website, campaign page and filing, with date and link. Write to knowledge/sites/<TITLE>-market.md."

**G. Owner research**: "For the owners on title <TITLE> (<names, addresses from the register>): check Companies House for any company and its officers and filings; search public obituaries and GOV.UK Find a will for <names> if the register suggests an older or deceased owner; record any address change. Write to knowledge/sites/<TITLE>-owners.md." (Private data: these files stay in knowledge/.)

## Site note template

```
# <TITLE>  <address as on the register>

Status: approach owner | approach agent | letter sent <date> | emailed <date> | in talks | parked | dropped | enquiry | appraisal in progress
Council: <name>   Parish or settlement: <name>   Tier: <hierarchy tier>
Area: <acres> acres (<ha> ha)   Grade: <farmland grade>   Titles in the site: <list>
SHELAA or HELAA ref: <ref(s)>   Route: application now | pipeline | enquiry

## Owner and interests
## Council assessment
## Policy position and what the site could carry
## Planning history
## Precedent (summary; full table in <TITLE>-precedent.md)
## Council documents
## Market and intelligence
## Constraints (coverage checklist results)
## Verdict (<date>)
## Actions and contact
## Open items
```

## Council note template

```
# <Council>

Adopted plan: <name>, adopted <date>. Period <years>. Allocation policy prefix: <...>.
Emerging plan: <stage>, <dates>. Call for sites: <dates>, register <URL>, submitter names <published or not>.
Five year supply: <x> years at <base date> (<source URL>, read <date>). Housing Delivery Test: <%> (<year>).
Settlement hierarchy: <tiers and examples>.
Land availability assessment: <name, year, URL>; reference format <...>; definitions <...>; text filed at sources/<council>/<file>.
Affordable housing: <percentage, threshold, tenure split, policy>. Mix, space and accessibility: <...>. Density: <...>.
County matters: <county council for roads, minerals, schools>.
CIL: <rates by zone, schedule date | no CIL (source)>.
Nutrient or water neutrality: <catchments, rule, credit source and price with date>.
Landscape and heritage designations in use: <names, studies>.
Planning portal: <URL>; quirks: <...>. Pre-application fees: <...>.
S106 patterns seen: <per home figures with the applications they came from>.
Appeal and refusal patterns: <behaviour profile: what is approved, what is refused, appeal outcomes, committee behaviour, with references>.
Learned: <anything reusable about this council>.
```
