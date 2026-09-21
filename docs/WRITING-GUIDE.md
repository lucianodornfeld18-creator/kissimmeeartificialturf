# Writing guide — kissimmeeartificialturf.com

Internal. Never rendered. Read all of it before writing a content module.

## Who is speaking

Kissimmee Artificial Turf is a **locally owned artificial turf installer in Kissimmee, Florida**. Owner: **Luis Austin**. First person plural ("we"). Service-area business: no street address, no showroom. Phone (689) 202-3710. It serves Kissimmee and towns within about 40 miles (Osceola, Orange, Polk, Lake, Seminole counties).

Public text is American English, written the way an installer who has done the work explains it to a homeowner across a driveway. Plain, specific, a little opinionated, never salesy.

## Never invent (hard rule — a page with an invented fact is deleted)

No street address, license number, insurance carrier, years in business, number of projects, reviews, star ratings, awards, staff names (other than Luis Austin, owner), brand names of turf we "carry", warranty terms, financing partners, prices presented as "our price", photos, testimonials, "as seen in", certifications, measurements we "took".

What you may say instead: market ranges with a source and date; what a good installer does and why; what we do as a method ("we compact the base in two lifts") — methods are fine, track records are not.

Do not describe the site's own production: no "keyword", "SEO", "search volume", "answer engine", "tier", "lead", "network", "sister", "partner contractors", "pipeline", "benchmark", "word count", "owner input", "pending", "TODO", "placeholder", "lorem".

## Verified facts you can use (checked 2026-09-21; cite with `src("id")` or the `sources=[...]` list)

**Prices (Central Florida market ranges, September 2026, not quotes)** — use `price("residential")` etc. from `_helpers`:
- Residential turf installed: $8–$18/sq ft, typical $10–$16 (`attampa-cost`, `lbs-fl-cost`).
- Pet turf: $10–$18, typical $12–$16 (`magnolia-pet-cost`, `installartificial-pet`).
- Putting greens: $14–$30, typical $18–$25 (`angi-putting`, `homeguide-putting`).
- Playground turf: $10–$25; small residential play areas $10–$16, school-grade with pad $15–$25 (`mightygrass-playground`).
- St. Augustine sod installed: about $1–$2/sq ft (`angi-turf`, `lawnstarter-cost`).
- Ten years on 1,000 sq ft: turf about $11,500–$23,000 vs. natural grass about $18,000–$37,000; break-even usually between year 5 and year 8 (`bearcat-10yr`, `attampa-sod`). Turf upkeep $200–$500 a year. A natural lawn that size takes roughly 20,000–30,000 gallons of irrigation a year.
- Never write a different price for a different city. Price does not change by ZIP; access, base, drainage and HOA rules do.
- For any other price (repair, cleaning, removal), research it, cite the source inline with `ext(url, text)`, and label it a market range.

**Heat**: turf in full Florida summer sun commonly reaches 120–150 °F at the surface and can pass 160 °F; a hose rinse drops it 30–50 °F within minutes; shade, light-colored/cooling infill help (`magnolia-heat`, `horsemans-heat`). Natural grass stays near air temperature. Be honest about this — it is a selling point for trust.

**Drainage**: perforated-backing turf drains at more than 30 inches per hour (`sgw-faq`); the base, not the turf, is what decides whether a yard drains. Central Florida summer storms routinely drop 1–3 inches in an hour.

**Lifespan**: 10–20 years depending on UV stabilization, traffic and infill (`stn-life`).

**Law** (informational, never legal advice; say exactly what each law covers):
- **HB 683 (2025)**, effective July 1, 2025, created **F.S. 125.572**: Florida DEP sets minimum standards for synthetic turf on **single-family residential lots of one acre or less**, and local governments may not prohibit turf that meets them or regulate it inconsistently with them. **DEP adopted Rule 62-308.100, F.A.C., effective May 19, 2026** — so this is now in force (`hb683`, `fs125572`, `dep-rule`, `marathon-pr`). Never write that the rule is still proposed.
- **What Rule 62-308.100 requires** — we have the adopted text (saved at `research/dep-62-308.100-final.txt`; cite `dep-rule`). Quote it accurately, never embellish:
  - Scope: single-family residential properties of 1 acre or less; local governments may not regulate inconsistently; **the rule creates no new DEP permit**; it does not change easements or rights-of-way.
  - **Materials**: turf, backing and infill must contain **no heavy metals and no intentionally added PFAS**, and must be disposable at a Florida-permitted landfill. **Infill may only be clean silica sand, rock, shell or other natural material; coated silica sand is allowed if the coating is non-toxic. Rubber or any other synthetic infill is allowed only within the footprint of playground equipment.** Infill must not wash off the property. (So: on a home lawn never recommend crumb rubber or TPE; zeolite is a natural mineral and fits "other natural material"; antimicrobial/cooling products are fine only as coated silica sand.)
  - **Subgrade (base)**: natural materials such as **crushed rock or crushed concrete** that meet the permeability requirement, **washed before installation to prevent fines from binding**. The soil beneath must **not be compacted to the point that it hurts percolation**. (So: describe the base as washed, open-graded crushed rock or crushed concrete, leveled and compacted firm — never "limerock with fines", "concrete fines", "road base" or "decomposed granite", which bind into a crust.)
  - **Color**: green synthetic turf shall be allowed.
  - **Permeability**: permeable turf on permeable backing over a pervious subgrade, graded for positive drainage; a local government may set a quantifiable standard of **at most 10 inches per hour for all layers**.
  - **Stormwater**: no pooling and no increase in runoff volume, direction or rate to adjacent properties; **not within a swale, ditch, stormwater pond or a pond's littoral zone**; must not alter the permitted stormwater system.
  - **Water conservation**: **in-ground irrigation cannot be used to irrigate synthetic turf**; a local government may require existing heads removed and the pipe capped.
  - **Water quality**: where no local buffer exists, turf stays **at least 10 feet from a natural or man-made waterbody** (ordinary or mean high water line) **unless there is a physical barrier such as a seawall or bulkhead**; a local buffer can't be stricter than the one for natural turf.
  - **Trees**: not inside **tree drip lines, on the property or on adjacent properties**, unless a **certified arborist** certifies no harm (noxious-weed trees excepted).
  - **Other**: installed to the manufacturer's specifications; **anchored at all edges and seams** to withstand wind or flooding; must leave **access to the septic tank for pump-out**; landward of any dune system.
- Consequences for how we describe our work: heads under turf are **capped**; rinsing is by **hose**; base is **washed crushed rock or crushed concrete**; infill on lawns is silica, zeolite or coated sand; stay outside drip lines without an arborist letter; 10 ft from ponds/lakes/canals unless there's a seawall; never in swales; keep the septic tank lid reachable.
- HB 683 is about **local governments**. It does **not** override HOA covenants (`stc-fl`).
- **F.S. 720.3045 (2023)**: an HOA may not restrict items **not visible from the parcel's frontage or an adjacent parcel**, "including, but not limited to, artificial turf". In practice: a fenced backyard is protected, a front yard is not (`fs7203045`, `olg-720`).
- Artificial turf is **not** automatically "Florida-Friendly Landscaping" under F.S. 373.185 / 720.3075; UF/IFAS does not class it that way (`ifas-turf`, `fs7203075`).
- Florida has **no state DBPR license for landscaping or turf installation**; local business tax receipts and county rules vary (`dbpr`).
- **Toho Water Authority** (Kissimmee, most of Osceola): two irrigation days a week by address (odd: Wed/Sat; even: Thu/Sun; non-residential: Mon/Fri), no daytime watering. Rules were under review in 2026 (`toho-days`, `osceola-water-2026`).
- PFAS: since January 1, 2026 California bars intentionally added PFAS in turf, pushing national product lines PFAS-free; ask for a test report. Mount Sinai's children's environmental health center remains critical of turf for play — mention both sides (`watersavers-pfas`, `mtsinai-turf`).

Anything local you add (permit rules, HOA/ARC requirements, soil series, housing age, utilities) **must be researched on the web and cited** with `ext(url, "label")` inline or as `(label, url)` tuples in `sources=[...]`. If a jurisdiction publishes no rule, write that and give the department's phone. Never guess.

## Page mechanics

Every content module lives in `site/content/` as `c_<name>.py`, imports from `_helpers`, and exposes `get_pages()` returning a list of `page(...)` dicts. Read `site/_helpers.py` and `site/_data.py` first. A worked example is `site/content/c_pricing.py`.

```python
from _helpers import page, capsule, sec, table, faq, ul, steps, note, cta, a, svc, city, cs, post, src, ext, price, price_note, tel
```

- `lede` is the **answer capsule**: 40–70 words, stands alone if quoted, contains a number with a unit, a date ("as of September 2026") and the place ("in Kissimmee and Osceola County").
- Body is HTML built with `sec("H2", "<p>…</p>")`. H2s that answer a question are written as the literal question and open with a 40–70 word direct answer paragraph, then detail, then a table or list where it helps.
- Tables: use `table(caption, headers, rows, note)`. AI systems quote tables — give them clear headers and units.
- FAQs: `faqs=[faq("Question?", "Answer.")]` — 4–8 per commercial page, each answer 35–80 words, never repeating a question owned by another page (see `research/questions.csv`).
- Links: only with the helpers (`svc("pet")`, `city("st-cloud")`, `post("slug", "anchor")`, `a("/artificial-turf-cost/", "anchor")`). Anchors are descriptive and varied; the same anchor text at most twice per page. Link to the commercial page of the cluster in the first two paragraphs of a post. Every page links to at least 5 other internal pages in running text.
- Titles ≤ 60 characters where possible (65 max), keyword first, no "Best" on commercial pages. Meta 120–160 characters with a concrete fact. H1 differs from the title.
- `sources=[...]` takes ids from `_data.SOURCES` and `(label, url)` tuples.

## Word counts (visible main text)

Home 3,800–5,000 · service 1,800–2,600 · city×service 900–1,500 · city hub T1 1,200–1,800 · city hub T2/T3 700–1,100 · county hub 1,200–1,800 · price hub 2,000–3,200 · law/permit 900–1,800 · post 1,200–2,500 · compare 1,000–1,600 · FAQ page 1,200+.

## Keywords without stuffing

"artificial turf", "artificial grass", "synthetic turf", "synthetic grass" and "fake grass" are the same thing: **rotate them naturally**. The page's primary phrase goes in the title, H1, first 100 words, one H2 and the meta — then stop counting and write. Hard limits checked by QA: exact primary phrase ≤ 1.2% of words; no phrase more than twice in one paragraph; no sentence of 8+ words repeated anywhere else on the site.

### "best … contractor" / "near me" (the owner wants these used, sparingly)

Never as a claim about ourselves ("we are the best", "#1", "top-rated"). Always as the customer's question or as criteria: *"How do you pick the best artificial turf contractor in Kissimmee?"*, *"What the best turf installers near you do differently on sandy soil"*, *"Searching for the best artificial grass contractor near me? Check these five things first."* Frequency: home 2; service page 1 (its own variant: "best pet turf installer near me"); city hub 1 with the city name; city×service at most 1, worded differently each time; FAQ hub 3. Rotate "turf contractor" / "grass contractor" / "turf installer" / "turf company". Prefer "near you in St. Cloud" in our own voice; "near me" only inside the customer's literal question.

## Style (QA fails the build on the banned list)

Banned: in today's, whether you're, look no further, it's important to note, it's worth noting, in conclusion, ultimately, at the end of the day, when it comes to, elevate, seamless, seamlessly, unlock, delve, robust, leverage, game-changer, transform your, dream yard, dream backyard, oasis, paradise, lush, pristine, we understand that, our team of experts, top-notch, state-of-the-art, cutting-edge, meticulous, comprehensive, hassle-free, peace of mind, stand the test of time, a testament to, nestled, vibrant, boasts, tapestry, one-stop shop, we've got you covered, utilize, in order to, let's dive in, here's the thing, say goodbye to, curb appeal (max once per page), "ensure" more than once per page. No emojis. No exclamation marks. No "Conclusion" or generic "Why choose us" sections. Em dashes: at most two per page. No rhetorical-question openers. No triads of adjectives. Not every section ends with a call to action.

Required: contractions; sentence and paragraph lengths that vary; one specific checkable fact (number with unit, ordinance, community name, soil series, temperature, depth, date) every 120–150 words; concrete examples ("a 640 sq ft backyard behind a 2006 pool home in Hunters Creek") — examples are illustrations, write them as "a typical…" or "say you have…", never as a job we completed; installer opinions with a reason ("we don't glue seams over a damp base because the adhesive skins before it bonds").

## Florida installation facts worth using

Native soil around Kissimmee is fine sand with a seasonally high water table (Smyrna, Myakka, Immokalee, Basinger series; Candler sand on the Polk/Lake ridge — verify per city on USDA Web Soil Survey). Standard build: remove sod and 3–4 in of soil, grade 1–2% away from the house, 2–4 in of washed, open-graded crushed rock or crushed concrete (the state rule requires washed material so fines don't bind) leveled and compacted firm, optional weed barrier (skip under pet turf — it holds urine), turf seamed with tape and adhesive, perimeter secured with 5–6 in nails or a bender-board/paver edge, infill brushed in at roughly 1–2 lb per sq ft. Irrigation heads under the turf are capped (Rule 62-308.100 bars using in-ground irrigation on synthetic turf); rinsing is by hose. Rainy season runs June–September with afternoon storms; dry season installs book faster. Low-E window reflection can melt turf (polyethylene softens around 175–200 °F) — check west- and south-facing glass. Live oaks: the state rule keeps turf outside the drip line unless a certified arborist certifies no harm. Screen enclosures and lanais: turf over concrete needs a drainage underlay and glue-down edges.
