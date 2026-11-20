# Land Engine: a plain English guide

For every site you give it, Land Engine does the desk review an experienced planning consultant would do before saying whether a site is worth pursuing. That is the work most of us either do by hand over several evenings, skip because there isn't time, or leave for BuildUp's experts to pick up when they review the site. With Land Engine, a site has already been looked at from every angle before you write to the owner or send it to BuildUp. This guide shows what it does, sets it up with you in about fifteen minutes, and explains how to use it every day.

## What it goes through for each site

You give it the title number, the address SearchLand shows, and the SearchLand panel. It then works through these layers, reading the documents themselves rather than summaries:

1. **The council's land availability assessment (SHLAA).** It finds the site in every round, not only the latest, and reads the whole entry. The sentence that decides a site often sits in a small column, for example "will change to unsuitable if adjacent sites are not brought forward". It also shows how the council's view changed from one round to the next, and why.
2. **The planning history of the site and the land around it.** It reads the decision notices, officer reports and appeal decisions in full, then tests every refusal reason against today. Say a site was refused six years ago for six reasons. It might tell you:
   - three of them no longer apply, because the council has since lost its five year supply and two schemes on the same edge of the village have been approved;
   - two can be dealt with by a section 106 contribution or a survey;
   - one still stands, and here is what a scheme would have to do about it.
3. **How this council decides schemes like yours.** It finds two nearby examples, one approved and one refused, and reads why.
4. **The council's plans and papers.** It reads the adopted and emerging local plan, including its policies map, any changes made since (main modifications), the housing land supply statement and the delivery test. It also reads the studies behind the plan (landscape, Green Belt, heritage, flood, viability), the neighbourhood plan, committee papers, parish council minutes and consultation responses, looking for anything about your site, its road or its area. A local plan runs to hundreds of pages and rarely names your field, but it may put the area your site sits in inside a local gap, open countryside or a landscape area. Or a site down the road may have been refused for a reason that would apply to yours, even though yours has no history of its own.
5. **What a scheme would have to provide.** The affordable housing share and its type, the mix of homes, density, CIL, section 106, biodiversity net gain and any nutrient or water rules, so you know the shape of a scheme before any numbers are run.
6. **The owner and the market.** If SearchLand shows a company owner, it checks the company at Companies House. When you buy the title register, it reads it for the owners, any lender, and any option or developer notice. It checks whether the land is listed for sale or being promoted by someone else.
7. **Every way a site can fail.** It runs a checklist covering access, flood, heritage, landscape, ecology, ground conditions, services and policy. It marks each line checked, not relevant, or couldn't check, and tells you what would clear the ones it couldn't.

Then it gives you a plain verdict with its reasons: write to the owner, approach the agent, park it until something changes, or drop it.

## It checks for itself, whatever you paste

SearchLand puts the facts in front of you quickly: the title, the constraint layers, the SHLAA entry, the land supply, the delivery test and the planning history. Land Engine starts from the panel you paste, but it never relies on it alone. It runs its own checks on the council's assessment, the planning history, the council's documents and the market every time. So if a tab wasn't expanded, a section didn't copy, or SearchLand is out of date, nothing is missed. Where what it finds differs from SearchLand, it tells you, with the source.

That matters, because SearchLand is not always right or current. In testing on real sites, it found, for example:
- a SHLAA card that looked like the council's assessment of a whole field, but only recorded a one-house permission on a corner of the title;
- a neighbouring allocation that the council had cut by more than half in plan changes published months earlier, while SearchLand still showed the old version;
- the council's own viability study for the sites next door, which gave tested values and costs to build the appraisal on.

## It remembers every site, in every council

This is the part that grows in value the more you use it.

When you look at a hundred sites, you can't hold everything from the first ninety-nine in your head: which refusal reasons this council keeps using, which of them lose at appeal, what officers accepted on the last village edge scheme, which documents mattered. An ordinary AI chat doesn't help much either. Each new chat starts knowing nothing. And if you keep one long chat going, it fills up, slows down, uses more of your allowance and starts losing the earlier detail.

Land Engine keeps notes in your own folder instead, written as it works:
- **a note for every site:** what it found in the SHLAA, the planning history, the council's documents, the news and online searches, the verdict, and every call and letter;
- **a note for every council:** its plan and where it stands, its supply, the reasons it uses to refuse, what wins and loses at appeal, its section 106 and CIL figures, and where to find its documents;
- **a note for every agent, promoter or developer you come across.**

Every new site in a council is read against all of that. By your tenth site in a council, it reads the new one against everything learned from the first nine: the same local gap policy that sank an earlier site, an appeal down the road that changed the picture, a precedent you'd long forgotten. Nothing is lost in an old chat or to memory. Each site you analyse makes the next one sharper.

## What it does for you

You talk to it in ordinary words. One or two words is often enough.

| You type | What happens | What you get back |
|---|---|---|
| The title number, the address SearchLand shows, and the SearchLand panel pasted in | Site review: it works through every layer above | A detailed report, a plain verdict, and anything it couldn't check |
| appraisal | It works out what the land could be worth with planning | One clear set of numbers, the best mix of homes, and your BuildUp submission ready to go |
| letter | It writes to every owner on the title register, on your letterhead | Finished PDF letters ready to print, with a site map if you use one |
| call script | It prepares what to say when an owner rings | A script to read from on the call, with the questions in the right order |

When each step finishes, it offers you the next one. After a site review, for example, it asks whether you'd like the appraisal.

## Why it uses less of your Claude allowance

Every Claude plan has a usage allowance, and long documents eat into it quickly. Land Engine is built to keep that down, with three roles:
- **The lead** runs the chat: Sonnet 5.5 at high effort. It plans the work, reads what matters and writes everything you or an owner will read.
- **The Opus advisor** is a stronger model the lead consults only at the moments that decide the outcome: before settling what a site needs, before the verdict, before the appraisal figures, before anything for BuildUp, and before every letter. You switch it on with `/advisor opus`.
- **The worker** does the heavy reading on Sonnet with exact instructions: hundreds of pages of council documents, dozens of officer reports, listings and comparable sales. It brings back only the facts asked for, each with its source, so the main chat stays short.

Two more things keep usage down. It reads documents as text, never as pictures, because pictures cost far more to read. And it keeps notes, so it never reads the same document twice.

### Very important: the setup before every new chat

1. Click the model name under the message box, choose **Sonnet 5.5**, and set the effort to **High** (or type `/effort high` and press Enter).
2. Type `/advisor opus` and press Enter.
3. Check the reply says the advisor is set to Opus 5.5. You can check at any time by typing `/advisor` on its own.

If you forget, the engine reminds you in its first reply. While the advisor is working, you may see a line saying "Advising" in the chat. That is Opus checking the work.

### One site per chat

Start a new chat for every new site. The engine keeps everything in its notes, so each new chat already knows the whole story: the site, the council and what you did before. A chat with many sites in it gets longer with every message, which uses far more of your allowance and slows it down. If you bring a second site into a chat, it will save its notes and ask you to start a new chat for it. To come back to a site later, start a new chat and give its title number.

## What you need before you start

- [ ] A Windows or Mac computer.
- [ ] A paid Claude plan that includes Claude Code (the plans are listed at [claude.com/pricing](https://claude.com/pricing)).
- [ ] The Claude desktop app, installed and signed in, from [claude.com/download](https://claude.com/download).
- [ ] Your SearchLand account.
- [ ] If you are a BuildUp member, your BuildUp Master appraisal workbook saved on your computer. BuildUp's costing calculator and Site Checks checklist already come with the engine.
- [ ] Your logo as a picture file, if you have one. If you don't, it uses your company name instead.

You don't need to know anything technical. If Land Engine needs a program installed, it installs it for you and tells you when to click Yes.

## Setting it up, step by step

Allow about fifteen minutes. You only do this once.

1. **Download the folder.** Open the GitHub link from the group post, click the green **Code** button, then **Download ZIP**. The file lands in your Downloads folder.
2. **Unzip it somewhere easy.** On Windows, right-click the file and choose **Extract All**, then pick your Documents folder. On a Mac, double-click it, then drag the folder into Documents.
3. **Open the Claude desktop app** and go to the **Code** tab.
4. **Point it at the folder.** Choose to work on your own computer, then select the Land Engine folder in Documents. If Claude asks whether you trust this folder, say yes.
5. **Set the model.** Choose Sonnet 5.5 and High under the message box, type `/advisor opus`, and check it says the advisor is set to Opus 5.5.
6. **Type: set me up** and press Enter.
7. **Answer its questions.** It first asks whether your details already exist somewhere, such as your own letterhead. Then it asks only what's missing: your name, title, company, phone, email and the counties you work in, then how you work with landowners, whether you're a BuildUp member, and where your logo is. Short answers are fine.
8. **Click Yes when asked.** It checks your computer has what it needs to make PDF letters, and installs anything missing, such as LibreOffice (a free office program). Your computer may ask permission; click Yes. The first few times Claude wants to run something, it shows you a short description and asks. Click **Allow**.
9. **Check your sample letter.** It makes your letterhead and a sample letter, and shows it to you. Tell it if anything is wrong, such as a phone number or the logo size, and it fixes it.
10. **Start.** It asks for your first site. That's it.

## Using it every day

Before each new chat, do the setup above (Sonnet 5.5, High, `/advisor opus`), and use one chat per site.

**1. Reviewing a site**

Open the title in SearchLand and click on the land so the panel opens down the left side. Copy the address it shows. Then click inside the panel, press **Ctrl and A**, then **Ctrl and C** (on a Mac, Command instead of Ctrl). In Claude, type the title number and the address, then press **Ctrl and V** to paste the panel, and press Enter. If you'd rather, export the SearchLand report as a PDF and drop it into the chat with the title number.

It tells you what it's doing as it goes. A site with a long planning history takes longer, because it reads the decisions and appeals in full. You can leave it running and come back. You get a report in this order:
1. What it found, section by section, with where each fact came from.
2. What that adds up to.
3. A plain verdict: write to the owner, approach the agent, park it until something changes, or drop it, with the reasons.
4. The checklist: what it checked, what didn't apply, and what it couldn't check.
5. What it needs from you, if anything.

**2. The appraisal**

Type **appraisal**. It uses the council's affordable housing rules and charges, local sold prices, BuildUp's costing calculator and the 26 percent profit target. It tests several mixes of homes and picks the one that gives the land the most value while staying within the rules. It fills in your BuildUp workbook. Type **Nexus** and it prepares the submission, written in your voice, with BuildUp's Site Checks filled in.

**3. Letters**

Type **letter**. You'll need to have bought the title register first (it tells you how). It writes one letter per owner, in the wording that has worked with owners, on your letterhead, with a map of their land if you use one (a separate sheet, printed on the letter itself, or none: you choose at setup). The files go into your Letters folder, ready to print, sign and post.

**4. When an owner rings or replies**

Type **they rang**, **call script** or **reply**, and tell it what they said. It prepares the call script or the reply, and records it in the notes.

## When it asks you for help

It does almost everything itself. It only asks you for things only you can do, in one plain sentence that says exactly what to click. These are the usual ones:

| It asks you to | Why |
|---|---|
| Give the title number, the address and the SearchLand panel, or send the report | SearchLand is your paid account, so you open it |
| Buy the title register (about £7) | It costs money, so you decide. It's the only source for a private owner's name and any option on the land |
| Sign in to a website | Only you know your password |
| Click Download on a page it has opened | Some council websites block automated downloads |
| Click Yes or Allow on a box | Your computer asks you before anything new is installed or run |

If it can't get something after trying every route, it doesn't quietly leave it out. It finishes everything else, then tells you what it couldn't check, why, what you can do about it, and how the verdict might change once that's done.

## Your privacy

Everything about you and your sites stays in your own folder on your own computer: your details, your letterhead, your notes on every site, owner and council, and the documents it has read. The folder you downloaded came with none of anyone else's sites or details in it, and yours stay with you in the same way.

- **Don't send anyone your Land Engine folder.** It holds your pipeline.
- If you use GitHub, the folder comes set up so that your profile, notes and documents are never uploaded.
- If you ever want to give a copy to someone else, ask Claude to **make a public copy**. It builds one without your details, and refuses to finish if it finds your name, phone number, a title number or an owner's name anywhere in it.

## Getting the most from it

- **Give it the title number, address and SearchLand panel every time.** It's the quickest start, and it tells the engine which constraints are already known, so it spends its effort where things are unclear.
- **One site per chat.** Start a new chat for each new site, with the model set up as above.
- **Let it finish.** A thorough review reads the officer reports and appeals, not just the headlines. That's where the useful detail is.
- **Read the "could not check" lines.** They are the honest edges of the verdict. Usually one click from you clears them.
- **Tell it when something changes.** "The owner rang back", "BuildUp replied with these comments", "I posted the letters today". It updates the notes, so the next step starts from the truth.
- **Ask it to explain.** If a term or a finding isn't clear, ask "what does that mean?" It explains in plain words and names the proper term, so you learn as you go.
- **It gets better with use.** When it finds a new kind of problem on one of your sites, it adds a check for it, and every site after that is checked for it too.

## If something goes wrong

In almost every case, the fix is to tell Claude what you see, in your own words.

| What you see | What to do |
|---|---|
| It doesn't seem to know about Land Engine | Check the Land Engine folder is the one selected in the Code tab, then start a new chat |
| It says the chat isn't on Sonnet or has no advisor | Choose Sonnet 5.5 and High under the message box, type `/advisor opus`, and start a new chat |
| It says you haven't been set up | Type **set me up** |
| It can't open SearchLand | Paste the SearchLand panel into the chat instead, or send the report |
| A council website won't load | It tries other routes itself; if it asks, click Download on the page it opens |
| Letters won't turn into PDFs | Type **check my computer** and it reinstalls what is missing |
| A phone number or logo on the letter is wrong | Type, for example, **change my phone number to 07000 000000** |
| You've used up your allowance for now | Wait for it to reset; your notes are safe in the folder, and the next chat carries on |

If you're still stuck, ask in the group and include a screenshot of what you see.
