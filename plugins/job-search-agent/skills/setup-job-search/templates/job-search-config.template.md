---
name: job-search-config
description: Settings every job search skill reads first. Lives in the user's job search folder.
---

# Job Search Config

Written by the setup-job-search skill. Every skill in this plugin reads this file before it does anything else. Edit it by hand whenever your search changes.

## Who

- Name: <fill in>
- Roles I am targeting: <titles and variants>
- Level band: <for example "Director through VP; a Head-of title counts if scope and comp match">
- Titles I do not want: <titles to exclude>

## Files in this folder

These names are relative to the folder that holds this config file.

- Criteria: dream-job-criteria.md
- Scoring rubric: company-scoring-methodology.md
- Proof points: proof-points.md
- Tracker: Job Search Tracker.xlsx

## Output preferences

- Default: answers and briefings stay in chat
- If I ask for a file: <.docx, .pdf, or .md>
- Writing style notes: <anything you want applied to drafts, or "none">

## Coaching style for interview prep

These are defaults. Change them to fit how you talk.

- Open with the strongest verified number, then wait to be asked for the detail
- Give a point of view before the story
- Match the framing to the interviewer: lead with business results for a commercial interviewer, and with craft and approach for a functional one
- Ask questions throughout the call, not only at the end
- Close every interview by agreeing a next step and a date

## Locked rules

The skills enforce these whatever this file says. They exist to protect you.

- Interview prep only uses claims written in proof-points.md. No number or outcome is ever invented or rounded up.
- If no real story exists for a topic, the skill says so instead of stretching a weak one.
- Gmail sweeps are read-only and ask permission every run.
- Rows with an in-progress pipeline status are never changed by a score.

## Job alert emails I receive

Check the ones you actually get. The daily scan only sweeps the ones checked here, and only after asking you each run.

- [ ] Application confirmation and response emails (any sender)
- [ ] LinkedIn job alerts
- [ ] Built In job alerts
- [ ] Jobright alerts
- [ ] The Ladders alerts
- Other senders to sweep: <sender or domain, one per line, or "none">

## Where I search

List any boards, communities or investor job boards you want checked in addition to the defaults in the daily scan skill.

- Extra sources: <for example your professional community's job board, or "none">

## Setup progress

setup-job-search ticks these off so it can pick up where it stopped.

- [ ] Workspace folder chosen
- [ ] Criteria written and approved
- [ ] Scoring rubric written and approved
- [ ] Proof points written and verified
- [ ] Tracker built
- [ ] Connections checked
- [ ] Alert sources recorded
- [ ] First scan or practice interview run
