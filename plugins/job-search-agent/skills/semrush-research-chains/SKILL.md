---
name: semrush-research-chains
description: Chain a review-site scan (G2, Capterra, TrustRadius, Trustpilot) and Semrush MCP pulls into workflows for researching a company before an interview or a case. Review-site landscape, search competitors and keyword evidence, backlink authority evidence, and an approval-gated build sequence. Use when the user wants data behind an SEO, authority or competitor claim about a target company. Needs the Semrush connector.
---

# Semrush research chains

Four chains. Chain 0 is a free review-site scan. Chains A to C are built on the Semrush MCP (tools named `mcp__Semrush__*`). Use them when the user wants data behind an SEO, authority or competitor claim about a company they are interviewing with or sizing up. Findings stay in chat until the user agrees on content. No files, pages or publishing without a clear yes.

This is research for the user's own career decision or interview prep. The user is usually not hired yet. Frame output as how they would decide and what they would ask, not as a free engagement plan for the company. Do not suggest handing the company the full plan.

The skill stands alone. If Semrush's own skills are installed (technical-seo-audit, internal-link-audit, schema-markup, keyword-research, content-brief, serp-analysis, backlink-audit, competitor-gap), hand off to them for the detail they cover. Semrush does not cover AEO, GEO, llms.txt or answer-engine checks, so say so and keep those as a separate pass.

If `job-search-config.md` exists in the working directory, read it for the user's writing preferences. It is not required.

## Pre-flight (every run)

1. Confirm the Semrush tools are loaded. If not, say the connector is missing and stop. Do not guess metrics. The user connects it in their own settings.
2. List every host before pulling anything: root domain, www, blog, support, trust or status pages, and any other subdomain. Use `organic_research` > `domain_organic_subdomains`. Unexpected hosts matter.
3. Tell the user BEFORE the first `execute_report` that queries spend API units. Name the planned calls and a row cap of 20 to 30. After the run, report units spent per call.
4. Unit costs vary by plan and change. Record what each call costs on the first run and say so. As a rule, `backlinks_matrix` and `backlinks_refdomains` cost far more than `domain_rank`, `domain_organic_subdomains` or `backlinks_comparison`. Start small and expand only if the first batch is not enough.
5. State the time frame in the output. Semrush returns the latest month when no `display_date` is set. Traffic and keyword figures are modeled estimates for one country database (default `us`). Backlink data is current to roughly the last few days. Unix `first_seen` and `last_seen` values need converting before anyone calls a link new or old.
6. `traffic_overview` needs a Trends subscription. If it returns `no_subscription`, mark traffic comparison unavailable. Do not substitute organic estimates for total traffic. `projects`, `site_audit` and `position_tracking` are read-only here. Never promise to create a project or launch a crawl.
7. Any error object (`no_subscription`, `no_api_units`, `no_data`, `rate_limit`) is reported plainly. `no_data` is a final answer, not a failure.

Tag every finding: Verified (a source or tool output you read), Sampled (some pages checked, not all), or Inference (your read). Label Semrush numbers as estimates.

## Chain 0: review-site scan (run first, free)

Purpose: learn the competitive landscape and buyer language before spending API units, so the Semrush pulls aim at real names instead of guesses. It uses WebSearch and WebFetch, not Semrush, so it costs no units.

Sites: G2, Capterra, TrustRadius, Trustpilot. G2 pages follow `https://www.g2.com/products/<slug>/reviews` and `.../competitors/alternatives`. For the others, use the URLs the user gives or the ones WebSearch returns.

1. Find the target's listing on each site. Confirm it is the right company before using anything from it. Generic names collide (a search for a company with a common two-word name can surface unrelated products with similar names). Check vendor name, website and description, and say what you checked.
2. Per site, record: listing exists or not, rating, review count, category, and listed alternatives with rating and review count. Separate real category peers from filler (work management, chat and spreadsheet tools appear on thin listings).
3. Check the competitor side. For the top one or two named competitors, read their listings and alternatives pages and note whether the target appears as an alternative on any site. Absence is a finding. A target missing from every site, including as an alternative to its main rival, points to a weak review motion and means buyers in comparison traffic will not meet it. Label that Inference and name how you looked.
4. Read the reviews. Record themes, competitor mentions, switching triggers and price complaints. If a listing has fewer than about 10 reviews, say the sample is too small to generalize.
5. Pass the names to Chain A. Alternatives from review sites are seed names for `domain_domains` and `keyword_research`, and a cross-check against Semrush's organic competitors. Names in both are tier 1. Names in only one go on the research-gap list.

Rules:
- The fetch tool has a domain allowlist and may refuse URLs you construct yourself (a direct Trustpilot or TrustRadius profile URL was refused in practice). Fetch URLs the user gave or WebSearch returned. If a page is refused or returns an error, try the built-in browser pane read as text. If that fails too, mark the site not reachable and move on. Do not sign in, create an account, solve a CAPTCHA or work around a block.
- WebFetch summarizes and can miscount. Treat ratings and review counts as approximate and re-fetch before a number goes into a decision. Two fetches of the same page can disagree by a few reviews.
- Not appearing in WebSearch results is sampled evidence, not proof of no listing. Say which queries you ran.
- Review-site alternatives lists are the site's own matching, not proof of who buyers compare. Label them Inference when used to name competitors.
- Ratings across sites are not comparable. Volumes and scales differ. Trustpilot skews consumer and is thin for B2B infrastructure, so say so rather than reading much into it.
- Quote at most one short review line, in quotation marks, with attribution. Summarize the rest. Review sites are not a backlink or authority source. Use Semrush for links.

Output: a table per site (listing, rating, reviews, category, alternatives, peer or filler), the review themes, whether the target appears as an alternative to its main competitor, and the names carried into Chain A.

## Chain A: search competitors, keywords, SERPs

Purpose: replace a competitor list built from a job dossier or forum threads with search evidence, and test whether category terms and comparison pages have real demand.

1. `competitors_research` > `domain_organic_organic` for the target. Note who appears that the user has not named, and compare against the Chain 0 review-site names. Tier them: direct, platform, status quo, watch list. Mark which names came from review sites, Semrush or both.
2. `competitors_research` > `domain_domains` for the target plus up to four competitors (five domains max). Pull missing and weak keywords. Cap 30 rows.
3. `keyword_research` for 6 to 10 head terms: the category term, competitor plus "alternative", target vs competitor, and the main use case. Pull volume, difficulty and intent. Report unknown, never guess.
4. `keyword_research` > `phrase_organic` for the top 3 or 4 head queries. Record who owns the top 10 and whether any result is competitor-authored. A competitor-written page about the target gets flagged. Check its claims against the target's own pricing and product pages before calling them wrong.
5. Output: competitor tiers, a keyword table (term, volume, difficulty, intent, who ranks), and a page decision list (build, improve, skip), each tied to evidence. No page recommendation without volume or SERP evidence.

Hand off: `competitive-research` and `product-research` for profiles.

## Chain B: authority evidence

Purpose: show where authority sits, where it leaks, and whether consolidating hosts is worth it.

1. `competitors_research` > `backlinks_comparison` for the root domain, each host (domain type) and 2 or 3 competitors (root_domain type). The `targets` and `target_types` arrays must match in length.
2. Judge by referring domains and Authority Score, not raw backlinks. Flag any single domain holding more than half of total backlinks and check its `first_seen`. Call it suspect only with a stated reason, and label that as judgment.
3. `backlinks_research` > `backlinks_anchors`, `backlinks_pages` and `backlinks_historical` (12 months) for the target. Anchors show branded versus descriptive. Pages show which content earns links. History shows direction.
4. `backlinks_research` > `backlinks_refdomains` for the target, sorted by authority, 30 rows. Note which partner and press domains send only one link.
5. `competitors_research` > `backlinks_matrix` with the target as the first target, filter `backlinks_bucket_0` equals 0, sort `matchesnum_desc`, 30 rows. Classify gap domains: press and PR, partners and storage or platform vendors, directories and aggregators (do not chase), job boards, communities.
6. Internal links and structure, no Semrush project needed. Use a browser the agent can drive to read each host's sitemap, count articles, and fetch article pages to count links pointing to the main host. Read competitors' sitemaps to see whether they run blog, customers, newsroom, events and compare pages as folders on one domain.
7. Output: an authority scorecard (target versus competitors), where links sit by host, a leak list, a gap list with classes, and a consolidation decision marked OPEN. Say honestly that Google allows both subdomains and subfolders and that the evidence for consolidation gains is mixed.

Hand off: `backlink-audit` and `internal-link-audit` if installed.

## Chain C: build sequence (only after the user approves)

Run only when the user has agreed the findings and asks to build, for example for a case study or working session. Order matters.

1. Brief: a content brief for the pillar or comparison page from the Chain A evidence (intent, angle, outline, FAQ, linking plan). A brief only, not the article.
2. Page: hand to a comparison-page skill if the user has one, otherwise draft in chat in the user's writing style.
3. Markup: draft JSON-LD from verified facts only. Never invent entity facts, ratings or reviews. Validate with the Rich Results Test and the Schema validator, and say what was not validated.
4. Links: list internal link targets from Chain B and the outside targets worth pursuing.

Nothing is published or sent. Show each step in chat first.

## Output rules

- Chat first. Compact tables. Point first, support second.
- Keep Semrush estimates, first-party checks and inference separate.
- End with API units spent, what was not covered, and one next step.
