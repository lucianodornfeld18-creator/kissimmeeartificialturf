# Tier 2 / Tier 3 city brief (internal, never rendered)

You are researching and writing the local pages for one or two towns on the website of a local artificial turf installer based in Kissimmee, Florida. Read, in this order: `docs/AGENT-BRIEF.md` and everything it points to (`docs/WRITING-GUIDE.md` is binding; it carries the ADOPTED text of Florida DEP Rule 62-308.100, effective May 19, 2026), `docs/CITY-AND-BANK-SPEC.md` section 1 (the contract for your file, including the TWO mandatory checks), and `site/_cityservice.py`. Do NOT open other city modules (`c_city_*.py`). Skim one bank file (`site/bank/b_residential.py`) so your local sections don't repeat what the bank already says. Read `site/content/c_permits.py` and `site/content/c_counties.py` only for the county permit, water and soil facts already verified for your county; reuse those facts and URLs, not the sentences. Never write anything about our track record ("most of our jobs", "our customers", "we've installed…") — the checker fails on it.

## What a tier 2 town gets

`_data.CITIES[slug]["tier"]` is 2: one hub `/areas/<slug>/` (kind="city", city=slug, 900–1,300 words) plus the SIX city × service pages allowed by `_data.TIER_SERVICES[2]` — residential, pet, putting, playground, pool, repair — built with `cityservice_pages(SLUG, LOCAL)` with one LOCAL entry for each of those six keys only. A tier 3 town (`tier` 3) gets a hub of 800–1,100 words plus THREE pages: residential, pet, putting.

Each module is one file `site/content/c_city_<slug_with_underscores>.py` exposing `get_pages()` returning `[HUB] + cityservice_pages(SLUG, LOCAL)`. If you were assigned two towns, write two separate files and run the checks on both (you may pass both module names to each checker in one command).

## Research (budget: about 8 web searches/fetches per town; primary sources; cite everything local in `SRC` and inline with `ext(url, "label")`)

1. Jurisdiction: is the town its own permitting authority (city building department: name, phone, portal) or unincorporated county? Link the county permit page (`/laws/permits/<key>/`, keys in `_posts.PERMIT_PAGES`); for a city without its own permit page, name the city office honestly and say we don't have a separate page for its code. The county property appraiser for the parcel check.
2. Water: the utility that serves the town, its irrigation days (cite), and the water management district (SFWMD / SJRWMD / SWFWMD — Polk and Lake are split; the county hubs already say which).
3. Housing and history: when it grew, typical lots (pool cages, oaks, lakefront, ridge slopes, 55+ communities, golf), Census population, and any PUBLISHED HOA/ARC document mentioning sod, ground cover or synthetic turf — quote only what you can cite; otherwise describe the review process without attributing a rule.
4. Ground: USDA soil series (official series descriptions), lakes/ponds/canals → the state rule's 10-ft waterbody setback (seawall exception) and swale/pond-bank exclusion; mature trees → drip-line rule; septic areas → septic-tank access.
5. Short-term rentals only where relevant. Distance: `_data.CITIES[slug]["miles"]` ("about N miles" straight-line from downtown Kissimmee); never a drive time.

## Writing

Hub: capsule (what we do there, `price("residential")`, one local fact, "as of September 2026"); what's different about turf in this town; a `table(...)` of "<Town> yard types and what we do differently"; permits/HOA paragraph linking the county permit page, `/laws/hoa-rules/`, `/laws/florida-hb-683/`; one "best … near me" sentence with the town name as the customer's question — exactly once; the token `<!--AUTO:city-services-->`; 4–5 FAQs; `related` as (route, label) tuples with plain route strings (county hub, permit page, 2 nearby hubs via their `/areas/<slug>/` routes, the cost guide).

Each LOCAL entry: unique title (≤ 65 chars, vary the pattern), meta 120–160, H1 different from title, a 40–70 word capsule with the market range via `price("<key>")` (residential, pet, putting, playground have keys; pool uses `price("residential")`; repair says quoted after photos or a site visit), three local sections of 110–170 words each about THAT service in THAT town from a different angle per service, a "say you have…" scenario of 100–150 words with square footage and range arithmetic, 2–3 local FAQs, `sources`. At most 2 of the 6 pages (1 of 3 for tier 3) may use a "best/near me" customer question, each worded differently. Link in running text to the parent service (`svc`), the hub (`city(slug)`), law/permit pages, 1–2 posts from `_posts.py`, and 3–4 nearby hubs (`city("slug")` for any slug in `_data.CITIES`).

No sentence of 8+ words may repeat between any two of your pages, nor with any existing page. Prices never differ by town. No invented facts.

## Verify, from the project root

`python qa/check_module.py c_city_<slug>` — every line OK (hub floor 700 words, city × service floor 900).
`python qa/cross_check.py c_city_<slug>` — "no cross-module duplication found".

Report briefly: facts verified with sources, anything you could not verify and left out, final output of both checks.
