---
name: documents
description: How to get and read, as text, every document land research needs: council assessments and local plans (PDF, Word, Google Docs), appeal decisions, officer and committee reports, S106 deeds, neighbourhood plans, title registers and filed deeds, Companies House records, probate records and GOV.UK property searches, including blocked portals and out of date cached pages. Use for any step that needs a document.
---

# Getting and reading documents

Rule: never read a document by taking pictures of its pages. It costs far more and misses words. Get the file, convert it to text, read the text, in full where the detail matters.

## Order of attempts (do all of these yourself before asking the user)
1. **Fetch** the web address with the fetch tool. Works for most council PDFs and GOV.UK pages. Trap: it can return a cached old copy. For anything that changes (supply statements, registers, application status), confirm the live page in the browser.
2. **Browser**: if the site refuses the fetch tool (blocked, UK only, a portal that needs scripts, council democracy sites), open it in the session's browser. Download the file there and bring it into the session; or, without saving anything, run a small script in the page that loads pdf.js from cdnjs, fetches the PDF and joins the text of every page.
3. **Another source for the same document**: planning.org.uk and plota.co.uk for applications; the Planning Inspectorate's search and richborough.co.uk for appeal decisions; the council's democracy site for committee reports; the examination library for plan documents; the Wayback Machine for pages that have moved.
4. **The user**, only if all of that fails: one plain sentence, for example "The council's website won't let me download this. Please open <address>, click Download, then type done." Then find the file in their downloads folder yourself (`profile/profile.json`, `downloads_folder`).
Never put a document on a "for later" list without trying all of the above, and never give up on a document silently: if it cannot be got, it goes in the coverage checklist as "could not check" with the plain sentence for the user.

## Google Docs links
A very large Google Doc (some councils publish appendices this way) will not export through the fetch tool. Open `https://docs.google.com/document/d/<id>/mobilebasic` in the browser, wait until the page has finished loading and its text length stops growing (this can take a minute), take `document.body.innerText` and search it for the site reference or road. Better: download it as Word and convert it, so the text is filed under `sources/`.

## Converting to text
- PDF: `python tools/pdf_to_text.py file.pdf out.txt "<source address>"` (uses pdftotext with layout when installed, otherwise PyMuPDF; puts the source and date on top). If a PDF is scanned images, run OCR first (`ocrmypdf`); signed S106 deeds are often scans.
- Word: `python tools/docx_to_text.py file.docx out.txt` (keeps tables in order).
- First lines of every text file: source address, document title, date read. File under `sources/<council>/<short-name>.txt`. Delete the PDF or Word file afterwards unless small and reused. Title registers stay as PDFs in the registers folder in the profile.
- One site's entry from an assessment: `python tools/shelaa_entry.py <text file> <site ref>`. Check the council's reference format first (some use leading zeros).
- Parsing a whole assessment into a sheet: pdftotext for the text; PyMuPDF word positions to detect tick boxes and their labels.

## Where documents live
- Applications: the council's planning portal (many use the same "online-applications" system; some show errors to automated browsers, then use SearchLand's Documents tab, planning.org.uk or plota.co.uk); committee reports and minutes on the council's democracy site.
- Appeal decisions: the Planning Inspectorate's appeals search; richborough.co.uk's appeal library.
- Local plans, assessments, supply statements, monitoring reports, call for sites registers, evidence studies: the council's planning policy pages; examination libraries for hearing statements and representations. Record every address in the council note.
- Neighbourhood plans: the council's neighbourhood planning page and the parish council's own website.
- Nutrient budgets and credit prices: the nutrient assessment in comparable applications; the council's or the credit scheme's published page.
- Sold prices and floor areas: Rightmove and Zoopla sold prices (price and date); the EPC register at find-energy-certificate.service.gov.uk (floor area). Detail pages often block the fetch tool; use the browser.

## Title registers and filed documents
- Free first: GOV.UK "Search for land and property information" (search-property-information.service.gov.uk) gives a summary (description, tenure, value stated and date, whether covenants and easements exist). It does not show notices or restrictions. "Search by map" finds land with no address (leave buildings out for a field).
- The register and plan, about £7 each, bought by the user (SearchLand or GOV.UK). Read all three parts:
  - **Property register**: address and plan; rights the land has over other land (a reserved right of way over a neighbour's strip can defeat a ransom); rights others have over it (cables, pipes, ways); mines and minerals excepted; transfers with covenants "filed under" another title (possible overage; read the filed copy before saying so).
  - **Proprietorship register**: owner names and addresses (write to each); entry date; price paid if stated (none usually means inheritance or a family transfer); restrictions (tenants in common or two trustees: every owner must sign; a company's consent restriction means a developer or lender has an interest).
  - **Charges register**: mortgages; unilateral or agreed notices (an option, promotion or sale agreement exists or existed; the register shows it exists, not its terms or whether it is still live); restrictions in favour of companies; utility deeds with covenants not to build near the apparatus; old restrictive covenants (often handled by indemnity insurance).
- A clean register: no notice, restriction or charge for a developer, promoter or lender, and no covenant forbidding building. Record "clean (read <date>)".
- Filed documents: official copy by form OC2 (about £7 online). Order before an appraisal when a deed could remove a strip or impose overage.

## Companies House
`https://find-and-update.company-information.service.gov.uk/company/<number>` and `/officers`, `/persons-with-significant-control`, `/filing-history`, `/charges`. Record status, dates, how a company closed (voluntary strike off; compulsory; members' voluntary liquidation, a planned solvent closure), officers with dates and addresses, charges. Search officers' names for successor companies.

## People
Deceased owners: public obituaries; GOV.UK Find a will (will and grant of probate, £1.50 each). Business operators: online reviews often date and name them.

## Appeal decisions and officer reports
Read in full. Record: reference, date, inspector or officer, main issues, each reason with its paragraph number, the housing supply position stated, the plan in force, nearby permissions mentioned, obligations secured, and exactly what was said about landscape value, character and the capacity to accept change.

## Learned
(Add portal quirks and better sources here as they are found, with the council and the date.)
- Some council planning registers (November 2026) only show records after the user clicks Agree on its disclaimer page in the app browser; ask them once, in plain words, and then search in the pane. Advanced search takes address, proposal and parish, and results pages after the first do not load by script, so narrow the search instead of paging. tools/pdf_to_text.py needs an output path as its second argument. Python's -I flag stops imports from the script's own folder, so run own scripts without it. planning.data.gov.uk (entity.json by point or box) is a quick, reliable check for conservation areas, listed buildings, tree zones, ancient woodland and National Landscapes; zero results is a real result once coverage is shown with a wider box.
- Sheffield documents (19 November 2026): the council's consultation site (haveyoursay) only gives a file when /download is added to the document address. The planning portal's certificate makes the fetch tool fail and it blocks with HTTP 429 after about 20 page loads in a minute: use the browser, one page at a time, read the Documents tab, and save a decision notice or officer report from the open page into the downloads folder, then convert and delete it. A pdf.js script from cdnjs may be blocked by the portal page, so do not rely on it.
