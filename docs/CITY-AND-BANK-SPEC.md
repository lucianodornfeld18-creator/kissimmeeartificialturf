# City modules and the block bank (internal, never rendered)

City × service pages (`/<service>/<city>/`, e.g. `/pet-turf/st-cloud/`) are assembled by `site/_cityservice.py` from two hand-written sources:

1. **The city module** `site/content/c_city_<slug_with_underscores>.py` — everything that is true only of that town, written for each service separately.
2. **The block bank** `site/bank/b_<service>.py` — technical blocks about the service, in five variants each, so that two towns never show the same wording on more than one block.

Read `docs/WRITING-GUIDE.md` first. Everything there applies (never invent, cite local facts, banned phrases, "best … near me" at most once per page and only as the customer's question).

## 1. City module

```python
# -*- coding: utf-8 -*-
from _helpers import page, capsule, sec, table, faq, ul, steps, note, cta, a, svc, city, county, cs, post, src, ext, price
from _cityservice import cityservice_pages

SLUG = "st-cloud"                       # must exist in _data.CITIES
SRC = [("City of St. Cloud — Building Department", "https://…"), …]   # every local source you used

HUB = page("/areas/st-cloud/", "city", "<title ≤60>", "<meta 120–160>", "<H1>", capsule("…40–70 words…"),
           "".join([sec("…", "…"), …, "<!--AUTO:city-services-->"]),
           faqs=[faq("…", "…"), …4–6…], sources=SRC, city=SLUG, crumbs=[("Service areas", "/areas/")], crumb="St. Cloud",
           related=[…county hub, permit page for the jurisdiction, 2 nearby city hubs via city("slug"), cost guide…])

LOCAL = {
  "residential": {
     "title": "Artificial Grass Installation in St. Cloud, FL – <local angle>",     # ≤ 65 chars, unique
     "meta":  "…120–160 chars with a local fact…",
     "h1":    "…different from the title…",
     "lede":  capsule("…40–70 words: what it is here, the {price('residential')} market range, one local fact, 'as of September 2026'…"),
     "sections": [("H2 …", "<p>…</p>"), ("H2 …", "<p>…</p>"), ("H2 …", "<p>…</p>")],   # three local sections, 110–170 words each
     "scenario": ("H2 …", "<p>Say you have a … sq ft … in <neighborhood type> …</p>"),      # 100–150 words, illustrative, with sq ft and the market price range arithmetic
     "faqs": [faq("…local question…", "…"), faq("…", "…")],                                # 2–3, unique to this page
     "sources": SRC,
  },
  "pet": {…}, …   # one entry per service in _data.TIER_SERVICES[tier of this city]
}

def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
```

### What "local" has to mean (the uniqueness gate)

Across the hub and the LOCAL entries, work in at least **six verifiable local facts**, each cited, and spread them so different services lean on different facts:

- which jurisdiction reviews permits (city vs. unincorporated county) with the department's name, phone and link; link our page `/laws/permits/<key>/`
- the water utility and its irrigation schedule (Toho, OUC, Orange County Utilities, Polk County Utilities, city utilities…), and the water management district (SFWMD / SJRWMD / SWFWMD)
- one or two real communities, HOAs or CDDs and what their published design guidelines say about turf, sod or ground cover — only if you can cite the document; otherwise describe the housing type without naming a rule
- the dominant soil series from USDA (Web Soil Survey / official series descriptions) and what it means for base and drainage
- when most homes were built (Census ACS "year structure built", or the city's own history page) and what that implies (pool cages, lot width, mature oaks, builder sod)
- lakes, ponds, canals, conservation areas or golf courses that trigger the 10-ft waterbody setback or the drip-line rule
- short-term-rental zoning if relevant (Osceola STR overlay, Polk/Four Corners), 55+ communities, septic prevalence
- distance from downtown Kissimmee: use `_data.CITIES[slug]["miles"]` ("about N miles") — never invent a drive time

Per service, make the local sections about *that service in that town* (dogs in narrow zero-lot-line yards; putting greens on golf-community lots; playground turf for a named city park's neighborhood type; pool turf in pool-cage subdivisions; vacation-rental turf in the STR overlay…). Never the same paragraph with the service name swapped. No sentence of 8+ words may repeat between any two of your pages.

Prices never differ by town. Use `price("<key>")` and do arithmetic inside the published range.

**Two checks, both mandatory, run from the project root:** `python qa/check_module.py c_city_<slug>` (format, word counts, banned phrases, repeats inside your file) and then `python qa/cross_check.py c_city_<slug>` (compares your rendered pages with every page already built in `site/dist`; it prints any run of 10+ shared words and fails on a pair over 12% or a shared run of 14+ words). Writers who "copied the mechanics" of an existing city module have produced 20–30% overlap; that is rejected. Write from your own research, in your own sentences, with different section angles. Check with `python qa/check_module.py c_city_<slug>` (city × service pages need ≥ 900 words including the bank blocks; if the bank for a service isn't written yet the page will be short — then aim for ≥ 520 words of your own material per page and say so in your report).

## 2. Block bank

`site/bank/b_<service>.py`:

```python
# -*- coding: utf-8 -*-
BLOCKS = {
  "base":    [("H2 variant 1", "<p>…</p>"), … five variants …],
  "product": [ … five … ],
  "process": [ … five … ],
  "risks":   [ … five … ],
  "care":    [ … five … ],
}
```

- Five variants per block, 80–120 words each, **each variant making a different point or using a different example**, not a reworded copy. H2s differ too.
- Placeholders `{city}` and `{county}` are replaced at build time; use `{city}` once or twice per variant so the sentence reads naturally ("On a typical {city} lot…").
- Block meanings for the service: **base** = what goes under it and why on Central Florida sand (washed crushed rock or crushed concrete, grade, drainage; state rule); **product** = which turf/infill/backing/pad spec suits this service; **process** = how the job runs and how long; **risks** = what goes wrong when it's done badly, and Florida-specific traps (heat, storms, low-E glass, drip lines, swales, 10-ft setback); **care** = upkeep for this service.
- Plain HTML strings (no helper calls inside the bank, so no links). Facts must come from `docs/WRITING-GUIDE.md`; no prices other than the guide's ranges; no invented numbers.
- No sentence of 8+ words may repeat anywhere in your file, or paraphrase a sentence in `site/content/c_services_*.py`.

Check with `python qa/check_bank.py b_<service>`.
