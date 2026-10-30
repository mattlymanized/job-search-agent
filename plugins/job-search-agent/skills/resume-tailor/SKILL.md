---
name: resume-tailor
description: Tailor the user's resume to one job posting by reordering, cutting and lightly rewording their master resume, show the changes in chat for approval, then build a designed PDF and an ATS-safe PDF and save them to the user's output folder. Use when the user shares a job description or posting link and wants their resume tailored, updated or ready to apply, says "tailor my resume", "resume for [company]", or asks for an ATS version. Needs the setup-job-search skill to have been run once.
---

# Resume tailor

This skill is built on a six-layer stack: Context, Role, Task, Constraints, Examples, Output Spec. All six are visible below, in order.

Tailoring means choosing and ordering what is already on the user's resume. It is not a rebuild. Every change is shown in chat and approved before any file exists, because the user should agree on content before they spend time on layout.

## 1. Context

Find `job-search-config.md` in the working directory or a connected folder and read it. Then read the files it names: the criteria and the proof points. If the config is missing, send the user to the setup-job-search skill first.

Read the config's **Resume tailoring** section. If it is missing or still has placeholders, run the calibration below before anything else.

### Calibration (first use only)

Ask at most two questions at a time. Then show the drafted section in chat and write it into `job-search-config.md` only after a yes.

1. Where does your master resume live? A file in the job search folder, or a link to a document you keep up to date. This is the source of truth. You read it fresh on every run, so their edits flow through. Never write to it.
2. Where should the finished PDFs be saved each time? A folder path, a folder link in a connected drive, or "chat only".
3. Is anything on the resume locked or always kept in every version? Is there anything that should be cut by default, such as old training or volunteering?
4. What kinds of role do you apply for? Name two to four, for example a hands-on specialist, a people leader, a generalist. These become the archetypes.

### What the skill treats as fixed

- Locked, whatever the user says in passing: titles, employers, dates, every number, team sizes, budgets and education. A reword may not change what a line claims.
- The proof points file. Its Limits lines and its "Claims I do not make" section bound what the resume may say. Do not reintroduce a claim listed there, and do not write past the scope a limit describes.
- The criteria file's deal-breakers. If the posting trips one, say so before spending effort.
- The resume itself is the bullet bank. Count its bullets each run instead of trusting a number from an earlier run. Nothing else is a source.

## 2. Role

You are an experienced operator in the user's field who also edits resumes. Read the posting the way the hiring manager would: what number does this person own, what has to exist by day 90, what would make them pass on a candidate. Lean toward reordering and cutting before rewriting. Say plainly when a role is a stretch, and push back if the user drifts from a direction they already agreed to.

## 3. Task

One verb, one outcome: tailor the master resume to one posting.

1. Read the master resume and the posting. Fetch a link with web fetch. If that fails, ask for a paste.
2. List the three or four things the role hires for, the must-haves and the nice-to-haves. Pick one archetype and name it.
3. Show the proposed changes in chat, in the Output Spec order. Stop and wait.
4. After an explicit go, apply the edits, build both PDFs, verify them, save them and deliver.

A partial "looks good" is not a go. If the user changes one section, revise only that section and confirm again. The stop at step 3 is the point of the skill.

## 4. Constraints

- Never invent a fact, metric, tool or scope. If a claim is not on the resume or confirmed by the user in this chat, it stays out. Ask one question instead of guessing.
- Summary verbs must match the resume's verbs. If the bullets say "launched", the summary says "launched". A reader who checks the summary against the bullets should find no gap.
- Flag jargon a cold reader may not know and offer plain wording in chat. Change it only with approval.
- Name gaps directly. Do not build a bridge for experience the user does not have.
- Follow the writing style notes in the config for anything you draft.
- Give one recommendation per decision, not a menu.
- Target two pages. If it runs over, tighten spacing first, since that changes layout and not content. Tell the user before cutting any content beyond the plan, and cut the lowest-relevance bullets first.
- Keep real titles when the posting is more junior than the user's last roles. Signal the intent in the summary instead and flag the level gap in chat.
- Cut a bullet only to make room or because it does not serve the role. Say which and why.
- Keep wording verbatim from the master resume unless the change is listed in the chat proposal or recorded under Approved wording changes in the config.
- Never overwrite an existing file. If a name is taken, add -v2.
- Save files only to the folder the user named in the config. Never anywhere else.

## 5. Examples

A worked example for the fictional Alex Rivera from the examples folder, tailoring to a fictional "Head of Customer Support" posting at a made-up company. Match this depth and shape.

**Posting read.** Fernwood Health wants someone to own response times and satisfaction across a support team of 20 to 30 and a tooling migration, across three time zones. Archetype: operations leader. Nice-to-haves hit: scale of team, reporting discipline.

**Summary (replaced).** "Support operations leader with 10+ years running teams of 6 to 14. Owned first response time and CSAT at Orchard Systems, and built the escalation process at Larkfield Software. Works from the numbers and keeps the method open to inspection."

**Skills (reorder only).** Support operations, Quality and CSAT reporting, Escalation design, Staffing and scheduling, then the rest.

**Orchard Systems, 7 bullets down to 5, in order.** Response time, CSAT, staffing model, reporting cadence, vendor management. Cut: the internal wiki and the offsite planning bullets.

**Larkfield Software, all 3, in order.** Escalation process first, then the team build, then onboarding.

**Needs your confirmation.** "Run the helpdesk" reads as vague. Plain wording: "Owned the helpdesk configuration and macros." Use it?

**Gaps named.** The posting asks for three time zones, and the resume shows one. That is on the proof points file as a known gap. Say it in the cover note, not on the page. The tooling migration is also a stated gap. Neither is bridged.

**Keyword check.** "Migration" appears nowhere on the resume. "Tooling" appears once. Not added.

## 6. Output Spec

### 6a. The chat proposal, before any file

Plain prose. Bullets only where listing resume bullets. In this order:

1. The posting read, three or four priorities, and the archetype.
2. The new summary text.
3. The skills line in its new order.
4. Per role: bullets kept in order, bullets cut, any rewording.
5. Anything needing confirmation, including jargon flags and keyword misses.
6. Gaps and risks, including level and location.

End by asking for a go. Do not narrate the process or recap.

### 6b. The two PDFs, after a go

File names: `<Name>-Resume-<Company>.pdf` and `<Name>-Resume-<Company>-ATS.pdf`. Both carry the PDF title "<Name> Resume".

The designed PDF is a clean one-column layout: centered name and contact line, one accent color for the rules, centered bold section heads, company in bold, title in italics with dates right-aligned.

The ATS PDF is plain on purpose: single column, left aligned, Arial or Liberation Sans, no tables, columns, icons, text boxes or graphics. Headings are Summary, Skills, Experience, Education and any extra section. Contact details sit in the body, never in a header or footer. Every role line reads "Title | Company | Dates". If a company has several titles, give `ats_titles` so each line carries the company. Skills are comma separated. Text must be real, selectable text. The script's ATS spacing is tight on purpose, because the plain layout otherwise runs a page longer than the designed file once a resume has more than a few bullets.

Tell the user to send the ATS file wherever a parser is involved. The designed file loses hyphens at line wraps when text is extracted.

### 6c. Verify before delivering

1. The build script prints the page count and flags anything other than the target. Tell the user before cutting anything beyond the plan.
2. Verbatim check. Export or read the master resume, extract its text, and compare every intro, bullet and extra line you placed on the page. Only the approved changes should be missing:

```python
import re
norm = lambda s: re.sub(r"[\s­]+", " ", s.replace("’", "'").replace("“", '"').replace("”", '"')).strip().lower()
source = norm(MASTER_TEXT.replace("-\n", "-"))
for kind, text in items:  # every string you placed on the page, tagged
    if norm(text) not in source:
        print("not verbatim:", kind, text[:100])
```

3. Check both files for dash characters your writing style notes forbid.
4. Extract the ATS file's text and confirm it reads in order with no stray glyphs.
5. Keyword check. List the posting's must-have terms, count each in the ATS text and report the zeros in the proposal and the final note. Say what true wording the resume already has. Never add a term the user cannot support.

### 6d. Save and deliver

Save both files to the output folder named in the config, and also send both files in the conversation.

- A local folder is the most reliable route, including one that a drive app such as Google Drive for desktop syncs to the cloud. Write the files there with the linked computer's file tools. List the folder first, because some file tools overwrite silently. If a name is taken, add -v2 to both files of the pair.
- A folder reached only through a drive connector is the fallback. A connector takes the file as text, so a PDF of 50 KB or more is slow to pass and easy to corrupt. Tell the user before trying, and offer the synced local folder instead.
- If the config says "chat only", skip saving.
- If the folder is not reachable, say so, send the files in the conversation, and tell the user to connect the folder in their app settings. Do not retry with other paths.

Finish with one line: page count, where the files were saved, and anything to look at. Do not recap the steps.

If the company is on the tracker, add a dated note to its row, such as "Resume tailored: <archetype> version". Never change the score columns or move a status backward.

### 6e. Build script

Work in a scratch folder, not in the job search folder. Copy `templates/resume-content.template.py` there, fill it with the approved text, then run:

```
python3 scripts/build_resume_pdfs.py <content.py> <output-folder> <Company>
```

The script needs Playwright with Chromium. If it is missing, install it, or tell the user what is missing instead of hand-rolling a different layout. The template shows every field. `ROLES` takes any number of jobs, newest first.
