---
name: setup-job-search
description: Guided setup for the job search agent. Use this first, and any time the user says "set up my job search", "get started", "build my tracker", "install the job search agent", or when another job search skill cannot find job-search-config.md. Interviews the user, writes their criteria, scoring rubric and verified proof points, builds their tracker spreadsheet, checks their connections, and gets them to a first scan or practice interview. Resumable.
---

# Set up the job search agent

You are walking someone through building their own job search system: a tracker they own, criteria that describe what a good job means to them, a scoring rubric, a file of verified career proof points, and the connections that let the daily scan and interview prep do real work.

Go one step at a time. Show a draft in chat, get a yes or an edit, then write the file. Do not write a file the user has not seen. Ask at most two questions at a time. People abandon setup when it feels like a form.

This skill is a starting point. Say so once, early, and then get on with it.

## How the other skills find their files

Every file lives in one folder the user owns, called the job search folder. The skills never hardcode a path. They look for `job-search-config.md` in the working directory or the connected folder, and the config names the other files relative to itself. If a skill cannot find the config, it sends the user here.

## Step 0: Check for existing work

Look for `job-search-config.md` in the working directory or connected folders.

- Found: read its Setup progress checklist and resume at the first unchecked item. Tell the user in one line where you are picking up.
- Not found: continue to Step 1.

You need access to a folder on the user's computer or a workspace folder where files persist. If this session cannot write files at all, say so plainly. The plugin works best in Claude Code or the desktop app with a folder connected. Do not pretend to save files you cannot save.

## Step 1: Choose the job search folder

Ask where the job search folder should live. Suggest a new, empty folder with a plain name. Create it if needed. Copy `templates/job-search-config.template.md` into it as `job-search-config.md`. The templates folder sits next to this SKILL.md. Tick "Workspace folder chosen".

Never write outside this folder without asking. Never overwrite an existing file. If one exists, show a diff and ask.

## Step 2: Interview for the criteria

Ask the questions below in small groups. Push for specifics. "Good culture" gets a follow-up: what would you check from the outside to know?

Group 1, the role. What titles do you want? What level and scope? Which titles are a no? What functions do you want to own?

Group 2, the company. Stage and size, funding or ownership preferences, and how you want larger or older companies treated.

Group 3, where and how. Location rules, travel, and hours or time zone limits.

Group 4, compensation. Base floor, target total comp, equity expectations, and any exception. Tell the user this stays on their computer.

Group 5, mission and deal-breakers. Ask what they would refuse to work on or for, and what counts. Probe for indirect exposure, such as a subsidiary or a contract, because those are the ones that slip through a quick screen. Ask for a lawsuit rule that separates a company suing a competitor from a company accused of mistreating its own people.

Then draft `dream-job-criteria.md` from `templates/dream-job-criteria.template.md` in chat. Show it, take edits, and write it. Tick "Criteria written and approved".

## Step 3: Build the scoring rubric

Show the default 12 categories and weights from `templates/company-scoring-methodology.template.md`. Ask which two or three matter most to this person and which matter least. Move weights to match. They must add up to 100. Offer to rename or drop categories, and warn that the tracker headers have to match the rubric.

Confirm the score bands and the statuses they map to.

Before writing `company-scoring-methodology.md`, edit the table in it so the category names and weights are exactly what the user chose, and check that the weights total 100. The daily scan reads its weights from this file, so it has to agree with the tracker headers. If the weights or names differ from the default, also write `rubric.json` into the job search folder, a list of `{"name": ..., "weight": ...}` objects in the same order as the table. Step 5 uses it, and it lets the tracker be rebuilt later. Tick "Scoring rubric written and approved".

## Step 4: Build verified proof points

Ask for their resume or a list of roles. Read it. For each role, draft proof-point entries using `templates/proof-points.template.md`. Then go claim by claim and ask where each number came from.

- Accept a number only if the user can name a source: a report, dashboard, export or document.
- Ask what the number exactly measures. A rate and a count are different claims. A measured result and an estimated one are different claims.
- Ask what the number does not show. Write the limit down. An interviewer will find it.
- If the user cannot source a claim, put it under "Claims I do not make" rather than dropping it silently. They may find the source later.
- Ask for known gaps, such as industries, motions or levels they have not worked in.

Do not round up. Do not invent. Do not fill a gap with something plausible. Write `proof-points.md` and tick "Proof points written and verified". It is fine if this takes a while. It is the file that makes interview prep trustworthy.

## Step 5: Build the tracker

Run the builder from this skill's own folder, the directory that holds this SKILL.md. It is not the job search folder, so use the skill folder's full path and give the job search folder as a full path too:

```
python3 -I "<skill folder>/scripts/build_tracker.py" --out "<job search folder>/Job Search Tracker.xlsx"
```

Add `--rubric "<job search folder>/rubric.json"` if Step 3 produced one. The script needs `openpyxl` (`pip install openpyxl` if it is missing). It will not overwrite an existing tracker. Do not pass `--force` unless the user asks, and say what it will destroy first.

The tracker has three tabs.

- Tracker holds live rows: Pursue, Pursue with Diligence, Applied, Followed Up, Call Scheduled, Interview, New - Needs Scoring.
- Passed - Closed holds roles that were screened out or closed before becoming a real conversation.
- Applied and Lost holds roles the user applied to that did not work out.

Open the file after building it and confirm the tabs, headers and Status dropdown exist. Explain the three tabs in two sentences. Tick "Tracker built".

## Step 6: Check connections

Look at which tools exist in this session. Do not claim anything is connected unless you can see its tools. Tell the user, in plain words, what each connection unlocks and what the skills do without it.

- Web search. Needed for the daily scan and all research. Without it, the plugin cannot find roles.
- A browser the agent can drive (Claude in Chrome, or the built-in browser in the desktop app). Needed to confirm a posting is really open. Many job pages look live to search and fetch tools when they are closed. Without a browser, the scan marks postings as unverified instead of open.
- Gmail, read-only. Optional. Lets the scan read application confirmations, replies and job alert emails. The scan never sends, drafts, labels or deletes, and asks every run.
- A spreadsheet or file skill. Lets the scan edit the tracker while keeping formatting.
- Calendar. Optional. Useful for interview dates.

If something is missing and they want it, tell them to connect it in their own settings for connectors or tools. You cannot connect it for them. If you can search a connector registry in this session, do that and show what you find. Tick "Connections checked" and record in the config which ones are present.

## Step 7: Record alert sources

Ask which job alert emails they get. Offer the ones in the config template. Suggest setting up saved alerts on LinkedIn and one or two niche boards for their function if they have none. Update the "Job alert emails I receive" section. Tick "Alert sources recorded".

## Step 8: Prove it works

Offer one of these and run it with them.

1. A first daily scan. Run the daily-job-search-scan skill with a short scope and no email sweeps. Show how a company gets screened, scored and filed.
2. A practice interview prep. Pick a real or made-up company and run interview-prep. Show how it asks which story to use.

Tick "First scan or practice interview run".

## Step 9: Optional daily schedule

If a scheduling tool exists, offer a daily scan at a time they choose. Tell them what changes when it runs unattended: it skips every email sweep because those need a yes each run, and it may skip posting verification if no browser is available. The summary will say so. Do not create a schedule without a yes.

## Step 10: Hand over

Finish with a short summary: the folder, the files written, the tracker, which connections are live, and what to say next. Examples: "run my daily job search scan", "prep me for my interview with <name> at <company>", "research <company>".

Remind them the folder holds their real data. If they keep it in a git repo, add it to `.gitignore` or keep it out of the repo entirely.

## Rules for this skill

- Never invent a number, a title or a date for the user.
- Never write a file the user has not seen and approved in chat.
- Never overwrite an existing file or tracker.
- Never imply a connection exists that you cannot see.
- If the user wants to skip a step, let them, leave its box unticked, and say what will be thin without it.
- Keep your own messages short. Most turns should be a few sentences and one or two questions.
