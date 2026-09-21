# Brief for content writers (internal, never rendered)

Project root: `C:\Users\luana\Projetos\kissimmeeartificialturf`. Static site generator in Python; content is Python modules that return page dicts.

## Read first, in this order

1. `docs/WRITING-GUIDE.md` — voice, the never-invent rule, verified facts and source ids, keyword and "best/near me" rules, banned phrases. **Binding.**
2. `site/_helpers.py` — the only helpers you may use to build HTML and links.
3. `site/_data.py` — services (keys, routes), cities (slugs, counties, tiers, miles from Kissimmee), prices, `SOURCES` ids.
4. `site/_posts.py` — every blog, compare, law, permit, FAQ and tool URL that exists or is being written in parallel. **Link only to routes that appear in `_data.py` or `_posts.py`** (plus `/`, `/services/`, `/areas/`, `/blog/`, `/compare/`, `/tools/`, `/about/`, `/contact/`, `/artificial-turf-cost/`). Other writers are producing those pages right now, so a link to them is fine even though the file isn't there yet.
5. `site/content/c_pricing.py` — a finished module to copy the mechanics from.

## Rules of the road

- Write only the file(s) you were assigned, in `site/content/` (or `site/bank/` if told so). Do **not** edit `_data.py`, `_helpers.py`, `_posts.py`, `templates.py`, `build.py`, anything in `qa/`, or another writer's module. Do **not** run `python site/build.py` (other writers are working at the same time and the build wipes `dist/`).
- Check your work with `python qa/check_module.py <your_module_name>` from the project root. It renders your pages in memory and prints word counts and problems. Iterate until every line says `OK`. Word-count floors are real: add substance (a table, a worked example, an exception, a local fact), never padding.
- Research on the web whenever you state something local, legal, regulatory, medical/safety or a price that isn't already in the writing guide. Cite it inline with `ext(url, "label")` and/or add `(label, url)` to `sources=[...]`. Prefer primary sources (city/county sites, flsenate.gov, floridadep.gov, UF/IFAS, USDA, Census, NOAA, ASTM/CPSC, manufacturers' spec sheets). If you can't verify it, leave it out.
- Python strings: use triple-quoted f-strings or concatenation; escape braces in f-strings; keep apostrophes safe (use double-quoted Python strings around text containing apostrophes). Use `–` for ranges and `×` sparingly. No emojis.
- Every page: unique title (≤ 60 chars if possible, 65 max), meta 120–160 chars, H1 different from the title, a 40–70 word capsule as `lede`, at least 5 internal links in running text, a `sources` list when you cite anything.
- No sentence of 8+ words may appear on two pages. Don't reuse your own paragraphs across pages, and don't paraphrase `c_pricing.py`.

## Report back (your final message)

Files written; pages and word counts (paste the final `check_module` output); sources you added; anything you could not verify and therefore left out; any route you linked to that is not in `_data.py`/`_posts.py`.
