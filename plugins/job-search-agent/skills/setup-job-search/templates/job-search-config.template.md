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

## Resume tailoring

Read by the resume-tailor skill. It writes this section with you the first time you use it.

- Master resume: <where the resume you keep up to date lives: a file in this folder, or a link to a document>
- Save tailored PDFs to: <a folder path, a folder link in a connected drive, or "chat only">
- Always keep: <items that must appear in every version, or "none">
- Cut by default: <items that should never ride along, such as old training or volunteering, or "none">
- Roles I tailor for: <two to four kinds of role, one line each>
- Approved wording changes: <rewordings you approved, with when to use each, or "none yet">

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
- Resume tailoring never changes titles, employers, dates, numbers or education, and never writes to your master resume.
- Gmail sweeps are read-only and ask permission every run.
- Rows with an in-progress pipeline status are never changed by a score.

## Job alert emails I receive

These four are examples, not requirements. Check the ones you actually get and list any other senders below. The daily scan only sweeps the ones checked here, and only after asking you each run.

- [ ] Application confirmation and response emails (any sender)
- [ ] LinkedIn job alerts
- [ ] Built In job alerts
- [ ] Jobright alerts
- [ ] The Ladders alerts
- Other senders to sweep: <sender address or domain, plus a subject line that marks a job alert, one per line, or "none">

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
