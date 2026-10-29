# Job Search Agent

A set of Claude skills for running a structured job search. It builds a tracker you own, scores companies against criteria you write, scans for new roles every day, preps you for specific interviews, and researches companies before you talk to them.

I built the original version for my own search. This repo is that system with my data and my paths taken out, so you can build your own version of it. It is a v0.1 starter kit. It was shaped around one person's search, so expect to edit it.

Built by Matt Lyman, with Claude.

## What you get

| Skill | What it does |
|-------|--------------|
| `setup-job-search` | Walks you through the whole build. Interviews you, writes your criteria, scoring rubric and proof points, builds the tracker spreadsheet, checks your connections. Run this first. |
| `daily-job-search-scan` | Searches boards for new roles, optionally reads your job alert and application emails (read-only, asks every run), checks postings are really open, screens deal-breakers, scores each company and files it in your tracker. |
| `interview-prep` | Researches the interviewer, predicts what they will probe, asks which of your verified stories to use for each topic, checks honest gaps, and builds a briefing in chat. |
| `competitive-research` | A sourced, 600-word read on where a company sits in its market, with talking points and open questions. |
| `product-research` | A deeper pass on what a company actually sells and whether its differentiation holds up against customer reviews. |

## Download and install

You need Claude Code or the Claude desktop app, with a folder on your computer you can give it access to. Pick one of the three routes below.

### Route 1: let Claude Code pull it from GitHub

No separate download. Claude Code fetches the repo for you. In your terminal:

```
claude plugin marketplace add mattlymanized/job-search-agent
claude plugin install job-search-agent@job-search-agent
```

Inside a Claude Code session, `/plugin marketplace add mattlymanized/job-search-agent` does the same first step.

### Route 2: download a copy, then install from the folder

Use this if you want the files on your machine first, or you want to read and edit them before installing.

Get the files one of two ways:

- With git: `git clone https://github.com/mattlymanized/job-search-agent`
- Without git: on the repo page on GitHub, click the green Code button, choose Download ZIP, and unzip it. The unzipped folder is named `job-search-agent-main`.

Then, from the folder that contains the download, run:

```
claude plugin marketplace add ./job-search-agent
claude plugin install job-search-agent@job-search-agent
```

If you used the ZIP, swap in `./job-search-agent-main` for the first path. The install name stays `job-search-agent@job-search-agent`. After a local install, edits you make to the files take effect the next time you start a session.

### Route 3: single skills in claude.ai or the desktop app

Download the repo as in Route 2. Then zip a skill folder from `plugins/job-search-agent/skills/` and add it in your skills settings. Zip the whole `setup-job-search` folder, because it carries the templates and the tracker builder. I have not tested this route.

### Start setup

Make an empty folder for your job search, start a Claude session in it, and run:

```
/job-search-agent:setup-job-search
```

If you used Route 3, ask Claude to run the setup-job-search skill instead.

## How setup works

Setup is a conversation, not a form. It asks a few questions at a time and shows you each file before it writes it.

1. You pick a folder. Everything the system makes lives there.
2. It interviews you about the role, the company, location, pay, mission and deal-breakers, and writes `dream-job-criteria.md`.
3. It shows you a 12-category scoring rubric and moves the weights to match what you care about.
4. It reads your resume and builds `proof-points.md`, one claim at a time. For every number it asks where the number came from, what it exactly measures and what it does not show.
5. It builds `Job Search Tracker.xlsx` with three tabs.
6. It checks which connections you have and tells you what each one unlocks.
7. It records which job alert emails you receive.
8. It runs a first scan or a practice interview prep so you see it work.

If you stop halfway, run it again. It reads its own checklist and picks up where it stopped.

## What the pieces are

Everything lives in one folder you choose. The skills never hardcode a path. They find `job-search-config.md` in the working directory and read the other file names from it.

| File | What it holds |
|------|---------------|
| `job-search-config.md` | Your settings, the alert emails you receive, your coaching style, setup progress |
| `dream-job-criteria.md` | What a good job means to you, written as things a researcher can check, plus deal-breakers |
| `company-scoring-methodology.md` | The weighted rubric, score bands and the research checklist |
| `proof-points.md` | Your verified claims, each with its source, exact definition and limits |
| `Job Search Tracker.xlsx` | Tracker, Passed - Closed, and Applied and Lost |

## Rules the skills hold themselves to

A few of these are not editable.

- Interview prep only uses claims in your proof points file. It never invents or rounds up a number, and it says so when you have no real story for a topic.
- Email sweeps are read-only. They never send, draft, label or delete. They ask your permission every run, and a scheduled run skips them.
- A posting only counts as open when a browser has rendered the page. Search results and cached pages lie about this constantly.
- A score never changes a status you set yourself. If you marked a role Applied, it stays Applied.
- The tracker builder will not overwrite an existing file.

## Connections

Web search is required. A browser the agent can drive is strongly recommended. Gmail is optional. Details in [docs/connectors.md](docs/connectors.md).

## Your data stays yours

Nothing in this repo is personal. Your criteria, pay floor, proof points and tracker live in the folder you pick on your own computer. If that folder is inside a git repo, ignore it. The `.gitignore` here already covers the file names setup creates.

The [examples](examples/) folder has a filled-in criteria file and proof points file for a made-up person, so you can see what good looks like. The person and every number in them are fictional.

## Known limits

- It was built around one person's search for a senior role at a technology company, so the default job boards and alert senders lean that way. Edit the criteria and the search scope for your field.
- The default rubric weights are a starting point. Move them.
- Posting verification depends on how job sites render today. They change. If a check starts giving wrong answers, open an issue.
- The plugin passes Claude Code's own validator, and installing from a downloaded folder (Route 2) loads all five skills. Nobody has run setup end to end on a fresh machine yet, so expect rough edges.
- Sourcing rules make the research slower than a plain chat answer. That is on purpose.

## Contributing

Issues and pull requests are welcome. If you adapt it for a different function, a PR with your criteria template is the most useful thing you can send.

## License

MIT. See [LICENSE](LICENSE). Copyright (c) 2026 Matt Lyman.
