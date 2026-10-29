---
name: daily-job-search-scan
description: Daily scan for new roles that match the user's criteria. Searches job boards, optionally reads job alert and application emails (read-only, asks every run), verifies postings are really open, screens deal-breakers, scores each company against the user's rubric, and files rows in their tracker. Use for "run my daily scan", "find new roles", "scan my email for applications", or as a scheduled task. Needs the setup-job-search skill to have been run once.
---

# Daily job search scan

You are running the user's daily scan. The point of the run is to surface new roles they have not seen, plus new applications and replies in their inbox. Upkeep on rows already tracked matters, but it is secondary. Spend most of the search effort on new roles.

## Start here

Find `job-search-config.md` in the working directory or a connected folder. Read it, then read the files it names: the criteria, the scoring rubric and the tracker. If the config or any of those files is missing, stop and tell the user to run the setup-job-search skill first. Do not guess at their criteria.

All file names below are relative to the folder that holds the config.

## Live run or unattended run

Work out which one you are in. A live run has the user present to answer. An unattended run is a scheduled task or has no one to ask.

Every email sweep below needs an explicit yes from the user on each run. A yes from yesterday does not carry over. In an unattended run, skip every email sweep and add one line to the summary saying so. In a live run, ask once up front for all the sweeps the config lists, for example "Want me to scan Gmail for application emails and your job alerts since yesterday?" If the user's own message already asked for the sweep ("scan my email"), that message is the yes.

## Email sweeps

Sweeps read the user's inbox. They are always read-only.

Rules that apply to every sweep:

- Only call tools that search or read mail. Never send, reply, forward, delete, archive, label, mark or create a draft. A draft is still a change. If you are unsure whether a call changes mailbox state, do not make it, and say the sweep was skipped for that reason.
- Only sweep the sources the config has checked.
- Use an overlapping window so a skipped day loses nothing. The dedup rules below stop double entries. Widen the window if the last sweep was longer ago than the window, or if the user asks for a phrase or sender to be rescanned.
- Never open or scrape linkedin.com for the LinkedIn alert sweep. Take the company and exact role title from the email text and find the real posting on the company's site or its applicant tracking system. Other alert sources can be followed directly.

### Application confirmations and replies

These are things the user already did, so the rows you add start as Applied.

Run several passes. A single narrow query misses real confirmations.

- Confirmations: `(subject:"thank you for applying" OR subject:"thanks for applying" OR subject:"thank you for your application" OR "we've received your application" OR "your application has been received" OR "thank you for your interest in") newer_than:2d`
- Indeed Easy Apply: `from:indeedapply@indeed.com newer_than:2d`. These never name the company. Resolve it by matching the job title against another confirmation from the same sweep, by searching the exact title to find the live posting, or by asking the user. If it still cannot be resolved, list the orphaned confirmation in the summary with its title and time instead of dropping it.
- Company-branded applicant systems send one email per role. Several in a row for the same company are separate applications, not duplicates.
- Replies and rejections: `(subject:"interview" OR subject:"next steps" OR subject:"update on your application" OR "unfortunately" OR "moving forward with other candidates" OR "not moving forward" OR "schedule a call" OR "schedule a time") newer_than:2d`
- If the user names companies they applied to, run a targeted search for each.

For each email, extract the company (from the sender name and the body, not only the domain), the role title (include a job or requisition number so parallel applications stay distinct), a posting link if one is present (skip tracking pixels and unsubscribe links), and the email date, which becomes Date First Seen.

Then:

1. Dedupe against all three tabs. Different roles at the same company are different rows. The same company and role is a duplicate. If a row exists and lacks a link, backfill the link and add a dated note. If the user reapplied to a company sitting in Passed - Closed or Applied and Lost, leave that row's status and score alone, add a dated note, and flag the reapplication in the summary.
2. If it is new, add a row to the Tracker tab with Status Applied and a note recording the source and subject line.
3. If you cannot extract the company, role or link with confidence, still add the row with what you know and say exactly what is missing in Notes.
4. A new Applied row has blank scores, so it enters the scoring queue. It stays Applied whatever it scores. If it fails the deal-breaker screen, call that out prominently in the summary. The user applied before any screening happened, so they need to know.
5. A rejection email, or the user telling you in chat that a company declined, sets Status to Declined with a dated note. An interview request does not change Status. Flag it in the summary so the user can update it themselves.

### Job alert emails

These are leads, not applications. Never add one as Applied. They follow the same screen, score and file path as any new find.

| Source | Query to start from | Notes |
|--------|---------------------|-------|
| LinkedIn alerts | `from:jobalerts-noreply@linkedin.com OR from:jobs-noreply@linkedin.com newer_than:3d` | Resolve each role on the company's own site. Never open linkedin.com. |
| Built In alerts | `from:support@builtin.com subject:"Job Matches" newer_than:5d` | Links can be followed directly and checked. |
| Jobright alerts | `from:noreply@jobright.ai newer_than:3d` | Its match percentage is its own algorithm. It does not replace the screen and the rubric. |
| The Ladders alerts | `from:theladders.com newer_than:3d` | Many roles are posted for unnamed clients. Keep one only if the employer can be resolved. A Ladders link is not canonical. |
| Other senders | whatever the config lists | Use a domain query rather than guessing the exact address. |

For every alert source:

1. Extract each distinct company and role pair. Alerts repeat across days, so collapse to one candidate per pair before doing any work.
2. Dedupe against all three tabs. A company already tracked gets skipped with a note if it is a live pipeline company.
3. Triage before spending search effort. Skip companies and titles the criteria rule out, such as mega-caps when the criteria prefer growth-stage, and titles below the user's level. Compensation bands in the alert are a useful early filter. Name skipped roles in the summary by company and role only.
4. Resolve each remaining candidate to the canonical posting. Search `"<company>" "<exact role title>"` and use the company's own careers page or its applicant tracking system. If you cannot find a live posting, do not add a row. Say it could not be resolved.
5. Verify the posting is open, screen it, score it and file it.

## Posting verification

Search results and plain page fetches are not proof that a posting is open. Many applicant systems return the same empty page whether the job exists or not, and aggregator pages stay up for weeks after a role closes. Verify by rendering the page in a browser tool and reading what comes back. If no browser tool is available, do not mark a row as confirmed open. Say it is unverified.

What a closed posting tends to look like:

- Ashby: "Job not found". The page is rendered by script, so a blank first read is common. Read the page text again before concluding anything.
- Greenhouse: the board says it is no longer active, or the job URL redirects to the general board without the role in it.
- Lever: a 404 page.
- Company career pages: the job URL redirects to a generic careers page. Use the on-page search box to look for the exact title before deciding. Dismiss cookie banners that block the search button.
- Heavy enterprise portals (Workday, Oracle and similar): the same, search the title.
- ZipRecruiter and Indeed: a "page not found" shell, or only similar-jobs cards with no description. These sites keep dead roles live for a long time, so treat their render as weak and cross-check the original system.
- Built In: "this job was removed". These can flip between open and closed. Be careful with a single open read against several recent closed reads.
- Investor portfolio boards: "no longer accepting applications" shown on the page, even though the full description may still display below it. A large share of postings found through search on these boards are closed.
- Executive networks that hide the employer name behind a paywall: low yield. Mention them to the user as a source for their own account rather than expecting leads from search.
- Sites behind a bot check that does not clear: find the same posting on its original applicant system and verify there.
- LinkedIn, for a role the user already tracks: an invalid job id redirects to an unrelated search page. Treat that as closed. A tracking-link format may bounce to a login wall either way. Retry the plain job URL first.

Only record Date Last Confirmed Open as today when you have a rendered-page confirmation.

## Freshness cadence

Checking every tracked posting every day wastes the run. For each row on the Tracker tab, find its last-checked date: the later of Date Last Confirmed Open and the most recent dated note. If neither exists, use Date First Seen.

- 7 or more days ago, or no date at all: due. Check it this run.
- Fewer than 7 days: not due. Leave it alone.

New finds are always checked, whatever the cadence. A user asking for a full sweep ("check everything today") makes every row due. Rows on Passed - Closed and Applied and Lost are never rechecked.

## Tracker structure

Three tabs with identical columns:

- Tracker: live rows. Statuses Pursue, Pursue with Diligence, Applied, Followed Up, Call Scheduled, Interview, New - Needs Scoring.
- Passed - Closed: roles that were screened out or closed before becoming a real conversation. Statuses Pass, Deal-Breaker, Closed.
- Applied and Lost: roles the user applied to that did not work out. Status Declined.

Columns A to L: Company, Score, Score Band, Status, Role/Title, Posting Link, Date First Seen, Date Last Confirmed Open, Criteria Met (Summary), Criteria Gaps (Summary), Sources, Notes. The remaining columns, one per category in the rubric, hold the 0 to 10 category scores in the rubric's order.

Notes entries start with a date in brackets, for example `[2026-03-14: note]`, so the freshness cadence can read them.

## Where to search

Cover as much of this as the run allows, plus any extra sources the config lists.

- Applicant systems and general boards: Ashby, Greenhouse, Lever, Workable, SmartRecruiters, LinkedIn.
- Aggregators: Indeed, ZipRecruiter, Glassdoor, The Ladders. Run a dedicated site-specific search for each, for example `site:ziprecruiter.com "<job title>" remote`, because they rarely surface in general searches. Cross-check against the original system before scoring anything from them.
- Remote-focused boards: Wellfound, Built In, Himalayas, Remotive, We Work Remotely, Otta or Welcome to the Jungle, RemoteOK.
- Community and function boards, where the user has access, and any mission-aligned boards if the criteria include a mission.
- Investor portfolio boards. Many run on the same client-rendered platform, so do not fetch them directly. Search them with a `site:` query against each board's domain, then verify each hit in a browser.

Search for the titles and phrases in the criteria's search terms. Score a "Head of" title at the same level on scope and compensation, not on the title alone.

## Triage

Before spending effort on a company you do not already know, check headcount, funding stage and ownership. A newly acquired company, or one that raised a very large late-stage round, can carry the same drag on autonomy and stage as a mega-cap even when the brand still reads as a startup. A quick look at recent culture and management themes on a review site is worth doing too. A repeated theme about a toxic culture or a bad management pattern is a real drag on the culture and management categories even when pay and scope look strong.

## Deal-breaker screen

Run the deal-breakers from the criteria on every company before scoring, whatever its size or fame. A well-known employer is not exempt.

Many deal-breakers do not show up in a company's pitch. For each one, check beyond the marketing:

- Search the company name with the relevant term, for example `"<company>" <the sector or activity you rule out>`.
- Read the company's own careers page for adjacent roles in the same department, such as a sales role aimed at a sector you rule out. A news search can come back clean when the jobs page gives it away.
- Check for a named subsidiary or division in the sector, even when the main brand looks unrelated.

For legal deal-breakers, judge whose conduct is in question. A company suing a competitor is a routine commercial dispute. A suit from a former employee alleging the company retaliated against them is the kind of signal the screen exists to catch.

If a company fails, leave its category scores blank, note the reason, and set Status to Deal-Breaker, unless the row is already Applied, Followed Up, Call Scheduled or Interview. In that case leave the status alone, add a clear warning in Notes and flag it in the summary.

## Status rules

Applied, Followed Up, Call Scheduled and Interview reflect the user's real progress. Never change one of them because of a score, a deal-breaker result or a posting check. For those rows, only update Date Last Confirmed Open if the posting is still live, and append `[POSTING CLOSED]` to Notes if it is gone. The one thing that moves a row out of those statuses is a confirmed rejection, which sets Declined. Declined then triggers archiving to Applied and Lost on the same run.

## Scoring queue

On every run, find Tracker rows that need scoring:

- Status is New - Needs Scoring.
- Any category score is blank, except rows deliberately left blank because they failed the deal-breaker screen. Check Notes for a deal-breaker flag before treating a blank row as unscored.
- A category was a placeholder and new research has confirmed or contradicted it. Rescore that category, recompute the total and note what changed.

For each one:

1. Research the company and role with the checklist in the rubric file. Use the posting link if there is one. If not, search the company and title to find the description.
2. Run the deal-breaker screen first.
3. If it passes, score every category from 0 to 10 using the rubric's anchors. Compute the weighted total on the 0 to 100 scale, set Score and Score Band, and fill Criteria Met, Criteria Gaps and Sources with cited evidence. Label inferences as inferences. If a category cannot be told from the outside, score it 5 and say it is a placeholder.
4. Set Status from the band table in the rubric file, unless the row is already in an in-progress status.

## Archiving

After scoring and checks are done:

- Move rows whose Status is Pass, Deal-Breaker or Closed to Passed - Closed.
- Move rows whose Status is Declined to Applied and Lost. Do this every run, including any left behind earlier.
- Before appending, check whether the company is already on the destination tab. If it is, fold the new information into the existing row's Notes and delete the Tracker row instead of adding a second entry.
- Copy the row with its formatting. After every deletion, recheck row numbers, because a stale row number writes to the wrong row.
- New finds that fail the screen, or score below the pursue threshold, go straight to Passed - Closed and never touch the Tracker tab. Rows with an in-progress status always stay on Tracker.
- Archived rows are reference only. Do not rescore or recheck them unless the user asks.

## Deduplication

Before adding any row, check all three tabs for the same company and the same role. The user may apply to several roles at one company, and each is its own row, told apart by Role/Title with the requisition number where there is one. For job-board and alert finds, the company name alone is the dedup key, because the scan is deciding whether to research a company at all. If a company is already on any tab, do not add a duplicate. Recheck immediately before every row write, not once at the start.

## Steps

1. Open the tracker and read every row on the Tracker tab, including rows the user added by hand.
2. Decide live or unattended, and run the sweeps that are allowed.
3. Recheck postings that are due under the freshness cadence. Keep this short.
4. Work the scoring queue.
5. Search for new roles across the search scope. This and the sweeps are the main event. Dedupe, screen, verify, score and add.
6. Archive to Passed - Closed.
7. Archive to Applied and Lost.
8. Save the tracker back to its own path. Keep the formatting on all three tabs: header styling, column widths, frozen panes, the filter range and the Status dropdown on the Tracker tab. Extend the filter range on any tab where rows were added or removed. If a spreadsheet skill is available, use it. Never save over the user's tracker without keeping what was already in it.

## Output

Keep the summary to about 150 words, longer only when a deal-breaker or a reapplication needs the space. In this order:

- New companies added that scored at or above the pursue threshold: name, score, status. Lead with this. If there were none across all sources, say so in the first line instead of padding with upkeep.
- New rows from each email sweep that ran, kept separate from board finds, with how many alerts were reviewed, deduped, skipped and unresolvable. If a sweep was skipped, say so in one line.
- Deal-breaker failures among email-sweep rows, named specifically.
- Reapplications to companies already in an archive tab.
- Manually added rows that were newly scored, with their score and the main drivers.
- Postings that closed, including any in the active pipeline.
- Rows moved to Applied and Lost, kept brief.
- Rejection emails and interview requests spotted. Interview requests need the user's own follow-up, so say so clearly.

Be direct. Cite sources for factual claims and label inferences.
