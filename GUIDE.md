# Land Engine: a plain English guide

Land Engine works alongside SearchLand as a senior adviser. It does not find sites for you: you find them in SearchLand as you do now. You give it the title number, the address and what SearchLand shows for the site, and it reads everything behind it, tells you what it means for the site today, and remembers what it learns about each council. This guide shows you what it does, sets it up with you in about fifteen minutes, and explains how to use it every day.

## Why this matters

SearchLand already puts the facts in front of you: the title, the constraint layers, the SHLAA entry (usually one click to the right page of the source document), the housing land supply and delivery test, and the planning history. Looking a site up takes minutes. Land Engine doesn't replace any of that. It starts from the SearchLand panel you paste in and works from there.

What SearchLand can't do is tell you what it all means for this site, today. That is where Land Engine helps, in three ways.

**1. A senior adviser at your side.** It reads what sits behind the facts: the full decision notices, officer reports and appeal decisions on the site and on the titles around it. Then it weighs each refusal reason against today. Say a site was refused six years ago for six reasons. It might tell you:
- three of them no longer apply, because the council has since lost its five year supply and two schemes on the same edge of the village have been approved;
- two can be dealt with by a section 106 contribution or a survey;
- one still stands, and here is what a scheme would have to do about it.

That is the judgement an experienced planning consultant brings, applied to every site you look at.

**2. A memory of each council that builds up.** When you look at site after site, nobody holds everything from the last ten in their head: which refusal reasons this council keeps using, which of them lose at appeal, what officers accepted on the last village edge scheme. Land Engine writes it all down as it goes. By your tenth site in a council, it reads the new site against everything learned from the first nine.

**3. The documents nobody has time to search.** A local plan runs to hundreds of pages and rarely names your field. But it may cover the area your site sits in: open countryside, a local gap, a landscape or character area, or a place where another site was refused for a reason that would apply to yours. Land Engine searches the adopted and emerging local plan, the neighbourhood plan, the studies behind them (landscape, Green Belt, heritage, flood), committee papers and parish minutes for anything about your site, its road or its area. It also finds the site in older SHLAA rounds that SearchLand doesn't show, and fetches the SHLAA document itself when SearchLand's source link doesn't open the page.

In short, it is a second pair of eyes that goes deeper than the panel, explains what it finds in plain words, and remembers.

## What it does for you

You talk to it in ordinary words. One or two words is often enough.

| You type | What happens | What you get back |
|---|---|---|
| The title number, the address SearchLand shows, and the SearchLand panel pasted in | Site review: it reads beyond the panel and weighs everything up (list below) | A detailed report, a plain verdict, and anything it couldn't check |
| appraisal | It works out what the land could be worth with planning | One clear set of numbers, the best mix of homes, and your BuildUp submission ready to go |
| letter | It writes to every owner on the title register, on your letterhead | Finished PDF letters ready to print, with a site map if you use one |
| call script | It prepares what to say when an owner rings | A script to read from on the call, with the questions in the right order |

**What the site review adds to the SearchLand panel**
- It reads every refusal, officer report and appeal on the site and its neighbours, and says which reasons still stand today, which have fallen away, and how the rest could be resolved.
- It finds two nearby examples of how this council decides schemes like yours: one approved and one refused, with the reasons read.
- It searches the local plan, neighbourhood plan, evidence studies, committee papers and parish minutes for your site, its road and its area.
- It finds every SHLAA round the site appears in, including older ones, and fetches the document when SearchLand's source link doesn't work.
- It works out what a scheme would have to provide: the share of affordable homes and their type, the mix of homes, and density.
- It checks whether the land is listed for sale or being promoted by someone else.
- It checks the owner as far as it honestly can. If SearchLand shows a company, it looks the company up at Companies House (status, directors, charges). A private owner's name, any lender, and any option or developer notice are only on the title register. Once you buy the register (about £7) and give it, it reads it; until then it marks those lines "could not check".
- It runs a checklist of every way a site can fail, from what SearchLand shows and its own online checks, and marks each one checked, not relevant, or couldn't check. Some checks need you, such as buying the register or clicking Download on a council page.
- It compares the site with everything it has learned from your earlier sites in the same council.

**It remembers.** It keeps notes on every site, council and agent in your folder. The second site in a council is quicker and sharper than the first, and nothing you've found is ever lost.

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
