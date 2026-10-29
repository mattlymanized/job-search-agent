---
name: competitive-research
description: Fast, honest read on where a company sits in its market, for the user's own career decisions. Use when the user names a company and says "research this company", "who are they up against", "is this a good bet", or before an interview or networking conversation. Produces one research brief in chat with sourced claims, talking points and open questions. Offers the product-research deep dive afterward. Needs the setup-job-search skill to have been run once.
---

# Competitive research

This is research for the user's own career decision, not a battlecard for an employer. Work like an analyst who has to brief an executive in twenty minutes. Use live web search. This is not a job for memory.

## Start here

Find `job-search-config.md` in the working directory or a connected folder and read it, then the criteria file it names. If they are missing, tell the user to run the setup-job-search skill first. The criteria feed the decision lens at the end.

## Step 1: Get the target

Ask which company, and whether the user already has a short list of competitors or wants you to identify the set. Do not guess the company unless the user named it in the same message.

## Step 2: Research

Prefer primary sources: the company's own site, press releases, filings and funding data. Then named secondary sources: analyst commentary, trade press, and review sites or forums for real user sentiment. Skip aggregator filler.

Cover:

1. Company snapshot. What they do, size and stage, funding or revenue signal, and recent trajectory such as growth, layoffs, a pivot, an acquisition or leadership changes.
2. Market position. Who they actually compete against, named specifically, and how they are perceived next to those competitors: leader, challenger, niche or losing ground.
3. Where they are winning. Real, specific strengths. If a competitor beats them somewhere, say where.
4. Where they are exposed. Product gaps, perception problems, themes in reviews, analyst notes or news. Do not strawman and do not soften.
5. Trajectory. Hiring patterns, executive departures and arrivals, funding or layoff news, product direction. Is this company scaling or coasting?
6. Talking points. Three or four sharp, specific things the user could say that show they understand the market better than someone who read the About page. Each one must rest on a fact from the research.
7. Decision lens. Using the criteria file, say which criteria the company meets, which it misses, and which cannot be told from the outside. This part is inference. Label it as a read, not a fact. Run the deal-breaker screen here too, including subsidiaries and the company's own careers page.
8. Open questions. What the user should ask the company, because the research could not answer it.

## Sourcing

Tag every factual claim.

- Verified: traced to a specific, checkable source. Name it and link it if you can.
- Inference: a reasonable read, not a confirmed fact. Say so.

If something central cannot be confirmed, such as funding status, a key competitor's positioning or whether the company is really growing, say so under Open Questions. Do not smooth it into vague language that still implies certainty.

## Step 3: Offer the product deep dive

When the pass is done, ask: "Want me to run the full product research deep dive on <company>?" Do not run it automatically. It is a heavier pass. If the user says yes, hand off to the product-research skill with the company already named.

## Output

A structured brief in chat, about 600 words, with a header for each section. Talking points and open questions as short lists. Cut anything the user would not say out loud or ask in the room. If a section has nothing sourced, write one line saying so. Do not make a file unless the user asks, and use the format in the config if they do.

Say what you found, plainly. No market-report filler. If a claim would not survive a follow-up question, it does not belong in the talking points.
