# -*- coding: utf-8 -*-
"""Price hub + cost calculator. Owner of questions 1, 2 (see research/questions.csv)."""
import json

from _data import PRICES, PRICE_DATE
from _helpers import page, capsule, sec, table, faq, ul, note, cta, a, svc, post, src, price, price_note

SIZES = [200, 500, 1000, 1500, 2500]


def money(n):
    return f"${n:,.0f}"


def size_rows():
    rows = []
    for s in SIZES:
        rows.append([f"{s:,} sq ft", f"{money(s * 8)}–{money(s * 11)}", f"{money(s * 11)}–{money(s * 15)}", f"{money(s * 15)}–{money(s * 18)}"])
    return rows


def get_pages():
    body = "".join([
        sec("How much does artificial turf cost in Kissimmee in 2026?",
            f"<p>Installed artificial grass in Kissimmee and the rest of Osceola County runs about <strong>{price('residential')} per square foot</strong> as of {PRICE_DATE}, and most residential yards land between {price('residential', True)}. That figure covers removing the old sod, the compacted base, the turf, seams, edging, infill and cleanup. A 1,000 sq ft backyard usually prices between $10,000 and $16,000. These are published {src('attampa-cost', 'Florida installer ranges')} cross-checked against {src('lbs-fl-cost', 'a 2026 state cost survey')}, not a quote for your yard.</p>"
            + table("Artificial turf cost per square foot by project type, Central Florida",
                    ["Project type", "Market range (installed)", "Where most jobs land", "What pushes it up"],
                    [[svc("residential", "Residential lawn"), price("residential") + " / sq ft", price("residential", True), "Tight access, heavy grading, lots of curves and cuts"],
                     [svc("pet", "Pet turf and dog runs"), price("pet") + " / sq ft", price("pet", True), "Odor-control infill, deeper drainage base, flush-out zone"],
                     [svc("putting", "Putting greens"), price("putting") + " / sq ft", price("putting", True), "Contouring, fringe turf, cups, chipping pads"],
                     [svc("playground", "Playground turf"), price("playground") + " / sq ft", price("playground", True), "Shock pad thickness for the equipment's fall height"],
                     [svc("pool", "Pool and lanai turf"), price("residential") + " / sq ft", "Upper half of the range", "Small areas, glue-down over concrete, drainage underlay"]],
                    price_note())
            + "<p>Small jobs cost more per foot. A crew, a plate compactor and a truckload of base show up whether the area is 150 sq ft or 1,500, so a side-yard strip can price at $16 to $18 a foot while a wide-open backyard of the same turf comes in near $11.</p>"),
        sec("What does it cost to turf a 500, 1,000 or 1,500 sq ft yard?",
            "<p>Multiply the area by the range for the build you want. A 500 sq ft yard runs roughly $5,500 to $7,500 at mid-grade; 1,000 sq ft runs $11,000 to $15,000; 1,500 sq ft runs $16,500 to $22,500. The table gives three build levels for five common sizes in Osceola and south Orange County yards.</p>"
            + table("Installed turf cost by yard size and build level",
                    ["Area", "Basic ($8–$11 / sq ft)", "Mid-grade ($11–$15 / sq ft)", "Premium ($15–$18 / sq ft)"], size_rows(),
                    "Basic: 1.25–1.5 in pile, standard silica infill, simple rectangle. Mid-grade: 1.6–1.9 in pile with thatch, curves, paver or bender-board edge. Premium: heavy face weight, cooling or antimicrobial infill, tight access or significant grading. " + price_note())
            + f"<p>Measuring is simple: length times width for each rectangle, added up. Pool homes in Hunters Creek or BVL often have 350 to 700 sq ft of actual grass once the deck and screen are subtracted; a quarter-acre lot in St. Cloud can carry 3,000 sq ft or more. The {a('/artificial-turf-cost/calculator/', 'turf cost calculator')} does the arithmetic and adds base and infill quantities.</p>"),
        sec("Where does the money go?",
            "<p>Turf itself is usually less than half the invoice. The base and the labor to build it are the part you never see again and the part that decides whether the lawn stays flat through a Florida rainy season.</p>"
            + table("Typical share of an installed turf price", ["Line item", "Share of total", "What it covers"],
                    [["Turf material", "30–40%", "The rolls, plus 8–12% waste on curved yards because turf comes 15 ft wide and the grain must run one way"],
                     ["Base and grading", "20–30%", "Sod and soil removal, hauling, 2–4 in of washed crushed rock or crushed concrete, leveled and compacted, slope away from the house"],
                     ["Labor", "20–30%", "Layout, seaming with tape and adhesive, trimming, edge fastening, infill, power brooming"],
                     ["Infill and edging", "5–10%", "Silica, zeolite or coated sand at 1–2 lb per sq ft; bender board, paver border or nailed perimeter"],
                     ["Disposal, irrigation capping, cleanup", "3–7%", "Dump fees, capping the sprinkler heads under the turf, final rinse"]],
                    "Shares vary by yard. A flat, open rectangle skews toward material; a tight side yard with roots skews toward labor.")
            + f"<p>That split explains most of the gap between two bids. If one quote is $3 a foot lower, ask how deep the base is, whether it's compacted in one pass or two, and how seams are joined. There's more on reading bids in {post('how-to-compare-artificial-turf-quotes', 'how to compare two turf quotes line by line')}.</p>"),
        sec("Is turf cheaper than sod over ten years?",
            f"<p>Usually, yes, but not in year one. St. Augustine sod goes in for about $1 to $2 a square foot and then costs money every week. Published ten-year comparisons for a 1,000 sq ft lawn put natural grass at $18,000 to $37,000 and artificial turf at $11,500 to $23,000, with turf catching up between year five and year eight ({src('bearcat-10yr', 'ten-year cost model')}; {src('attampa-sod', 'Florida long-term comparison')}).</p>"
            + table("Ten-year cost of 1,000 sq ft: artificial turf vs. St. Augustine sod", ["Cost", "Artificial turf", "Natural grass (St. Augustine)"],
                    [["Installation", "$10,000–$16,000", "$1,000–$2,000"], ["Mowing and edging", "$0", "$30–$50 per visit, 35–40 visits a year if hired out"],
                     ["Irrigation water", "Occasional rinse", "About 20,000–30,000 gallons a year"], ["Fertilizer, weed and pest control", "$0", "$300–$700 a year"],
                     ["Upkeep", "$200–$500 a year (brushing, infill top-up, deodorizer for pets)", "Re-sodding thin or chinch-bug areas every 5–7 years"],
                     ["Ten-year total", "<strong>$11,500–$23,000</strong>", "<strong>$18,000–$37,000</strong>"]],
                    "Published model ranges for 1,000 sq ft; your mowing and water bills decide the real number. Run your own in the " + a("/tools/turf-vs-sod/", "turf vs. sod calculator") + ".")
            + f"<p>If you mow your own lawn and irrigate from a well, grass stays cheaper for a long time, and we'll tell you so. The full argument, including what Toho's two-day watering schedule does to new sod, is in {post('artificial-turf-vs-sod-cost-florida', 'turf vs. sod in Florida over ten years')}.</p>"),
        sec("What changes the price on a Central Florida lot?",
            ul(["<strong>Access.</strong> A 36-inch side gate means wheelbarrows instead of a skid steer. On a 900 sq ft backyard that can add a full crew day.",
                "<strong>What's there now.</strong> Healthy St. Augustine has a 3–4 inch thatch and root mat that has to leave the site. Bahia on a newer St. Cloud lot strips faster.",
                "<strong>Water.</strong> Yards that hold water after an afternoon storm need the grade corrected or a drain line before any turf goes down. Turf drains faster than 30 inches an hour; the soil under it may not.",
                "<strong>Tree roots.</strong> Inside a live oak's dripline we keep excavation shallow and build up instead of down, which takes more base material.",
                "<strong>Edges and shapes.</strong> Curves, tree rings and stepping stones mean more cuts and more waste. A plain rectangle is the cheapest shape there is.",
                "<strong>Infill choice.</strong> Standard silica is the least expensive. Zeolite or antimicrobial coated sand for dogs, or a cooling infill for a full-sun play area, adds roughly $0.50 to $1.50 a foot.",
                f"<strong>HOA paperwork.</strong> An ARC submittal with a sample, a spec sheet and a site plan takes time in communities such as Celebration or Reunion. See {a('/laws/hoa-rules/', 'what Florida law lets an HOA restrict')}."])
            + "<p>What doesn't change the price: your ZIP code. We don't charge a Lake Nona rate and a Poinciana rate. The yard sets the number.</p>"),
        sec("What does the infill choice add?",
            "<p>Infill is the sand-like material brushed between the blades. It holds the turf down, keeps the fibers upright and, depending on the type, fights odor or heat. It's a small line on the quote that changes how the lawn lives.</p>"
            + table("Common infills and what they add to the price", ["Infill", "Typical use", "Effect on installed price", "Trade-off"],
                    [["Rounded silica sand", "Standard lawns", "Included in most base quotes", "No odor control; fine for yards without dogs"],
                     ["Zeolite", "Dog runs and pet yards", "Adds roughly $0.50–$1.00 per sq ft", "Traps ammonia and releases it when rinsed or rained on; needs rinsing to keep working"],
                     ["Antimicrobial coated sand", "Pets, play areas", "Adds roughly $0.75–$1.50 per sq ft", "Costs more; doesn't break down or hold moisture"],
                     ["Evaporative cooling infill", "Full-sun play areas and pool surrounds", "Adds roughly $1.00–$1.50 per sq ft", "Works while damp, so it needs a hose rinse on hot afternoons"]],
                    "Add-on figures are typical installer differentials within the published per-foot ranges above, not separate quotes.")
            + f"<p>The {a('/compare/zeolite-vs-silica-vs-antimicrobial-infill/', 'infill comparison')} goes through each one, and {post('coolest-artificial-grass-and-infill-for-florida', 'this article covers the cooling products')}. Since May 2026 the state standard limits infill on single-family lots to silica sand, rock, shell or other natural material, plus coated sand with a non-toxic coating; rubber and other synthetic infills are allowed only under playground equipment. It also requires turf, backing and infill free of heavy metals and intentionally added PFAS. Both belong on the quote in writing.</p>"),
        sec("Deposits, scheduling and what a fair payment schedule looks like",
            "<p>Turf is a materials-heavy job, so a deposit to order the rolls is normal. What's reasonable is a deposit that roughly matches material cost, a progress payment once the base is in and compacted, and the balance at the walkthrough. Be wary of anyone who wants the whole amount before a shovel goes in the ground, and of quotes that are only good \"today.\" A written scope with the five spec lines below protects both sides.</p>"
            "<p>Dry-season dates, from about October to May, fill first. Summer installs happen too; they just start earlier in the day and lose the odd afternoon to lightning.</p>"),
        sec("What do the other services cost?",
            f"<p>Repairs, cleaning and replacement are priced by the visit or the job, not the square foot, so they don't fit one table. {svc('repair', 'Seam and edge repairs')} usually carry a minimum service charge; {svc('cleaning', 'pet-odor treatments and power brooming')} are quoted by yard size and how long it's been; {svc('replacement', 'tear-out and replacement')} prices close to a new install minus whatever base can be reused. {svc('commercial', 'Commercial areas')}, {svc('sports', 'sports surfaces')} and {svc('pavers', 'turf set between pavers')} are quoted from drawings or a site walk. Each service page gives the ranges we could verify.</p>"),
        sec("How do you keep a quote honest?",
            "<p>Shorter answers to money questions live on the {a('/faq/cost/', 'cost FAQ')}, and the {a('/tools/', 'planning tools')} turn dimensions into ranges. Ask for five numbers in writing: square footage measured, base depth and material, turf product name with face weight and pile height, infill type and pounds per square foot, and how seams and edges are secured. Two bids with those five lines can be compared. Two bids that say \"premium turf, installed\" can't.</p>"
            + f"<p>Ask what happens with the irrigation zone, who handles the HOA application, and what the workmanship warranty covers separately from the manufacturer's. {post('what-does-artificial-turf-warranty-cover', 'Turf warranties')} mostly cover UV fade, not seams that open because the base settled.</p>"
            + cta("Get a measured quote", "We measure, check drainage and access, and put the five numbers in writing.")),
    ])
    faqs = [
        faq("Why is artificial grass installation so expensive?", "Because most of the price is excavation, base rock, compaction and skilled seaming, not the turf. On a typical Kissimmee yard the rolls are 30–40% of the invoice. The base is what keeps the surface flat and draining through summer storms, and it's the first thing a low bid cuts."),
        faq("Is there a minimum job size?", "Most installers, us included, have a minimum because a crew and equipment are mobilized either way. Expect small areas under about 200 sq ft to price at the top of the per-foot range or as a flat minimum."),
        faq("Does turf cost more in Celebration or Lake Nona than in Poinciana?", "No. Material and labor cost the same across the area. What differs is access, grading, tree roots and whether an architectural review application is needed."),
        faq("Can I lower the price by doing the demo myself?", "Sometimes. Removing sod and hauling it off can take $1–$2 a square foot out of a quote. The grade still has to be right before base goes in, so talk to the installer first about depth and slope."),
        faq("Do you charge for an estimate?", f"No. We measure the yard, look at drainage and access, and send a written quote. Call or text {PHONE}."),
        faq("What is the cheapest way to get turf without cutting corners?", "Keep the shape simple, because rectangles waste the least material. Choose a mid-height turf with standard silica infill, turf only the area that gives you trouble, and ask whether removing the sod yourself lowers the quote. Don't economize on the base or the seams; those are what you'd pay to redo."),
    ]
    hub = page("/artificial-turf-cost/", "price",
               "Artificial Turf Cost in Kissimmee, FL (2026): Per Sq Ft & By Yard",
               "Artificial turf in Kissimmee runs $8–$18 per sq ft installed in 2026. Tables by yard size, project type and ten-year cost vs. sod, with sources.",
               "What artificial turf costs in Kissimmee and Central Florida",
               capsule(f"Artificial turf in Kissimmee, FL costs about {price('residential')} per square foot installed as of {PRICE_DATE}, with most yards between {price('residential', True)}. A 1,000 sq ft backyard typically runs $10,000 to $16,000 including sod removal, a washed crushed-rock base, turf, infill and edging. Pet systems and putting greens cost more per foot."),
               body, faqs=faqs, crumb="Turf cost",
               sources=["attampa-cost", "lbs-fl-cost", "magnolia-pet-cost", "installartificial-pet", "angi-putting", "homeguide-putting", "mightygrass-playground", "bearcat-10yr", "attampa-sod", "sgw-faq", "toho-days"],
               related=[("/artificial-turf-cost/calculator/", "Turf cost and materials calculator"), ("/tools/turf-vs-sod/", "Turf vs. sod ten-year calculator"), ("/blog/why-is-artificial-grass-so-expensive/", "Why turf installation costs what it does"), ("/faq/cost/", "More cost questions, answered briefly")])

    rates = {k: [PRICES[k][0], PRICES[k][1]] for k in PRICES}
    calc_body = sec("Estimate your yard",
                    f"""<form id="calc" class="lead" data-rates='{json.dumps(rates)}' data-opera="skip"><div><label for="c-len">Length (ft)</label><input id="c-len" name="len" type="number" min="0" inputmode="decimal"></div><div><label for="c-wid">Width (ft)</label><input id="c-wid" name="wid" type="number" min="0" inputmode="decimal"></div><div><label for="c-area">…or total area (sq ft)</label><input id="c-area" name="area" type="number" min="0" inputmode="decimal"></div><div><label for="c-kind">Project type</label><select id="c-kind" name="kind"><option value="residential">Residential lawn</option><option value="pet">Pet turf</option><option value="putting">Putting green</option><option value="playground">Playground turf</option></select></div><div class="full"><label class="ck" for="c-rm"><input id="c-rm" type="checkbox" name="remove" checked><span>Include removing existing sod and soil (adds about $1–$2 per sq ft)</span></label></div><div class="full"><p id="calc-out" role="status" aria-live="polite">Enter a length and width, or an area.</p></div></form>"""
                    + "<p>The calculator multiplies your area by the published Central Florida range for that project type and rounds to the nearest $50. It also estimates crushed base at 3 inches deep with a 15% compaction allowance and infill at 1.5 lb per square foot, which is what you'd order for a do-it-yourself job.</p>") \
        + sec("How to measure an odd-shaped yard",
              "<p>Break it into rectangles and triangles, measure each, and add them. For a curved bed line, measure to the widest point and accept a little extra: turf comes in 15-foot-wide rolls and the blades lean one direction, so every piece has to run the same way. That's why a yard that measures 820 sq ft often needs 900 sq ft of material.</p>"
              + f"<p>Subtract the pool deck, the screen enclosure footprint, the AC pad and any planting beds you're keeping. Then read {a('/artificial-turf-cost/', 'the full cost guide')} for what moves a job toward the top or bottom of the range, or skip the math and {a('/contact/', 'ask us to measure it')}.</p>")
    calc = page("/artificial-turf-cost/calculator/", "tool", "Artificial Turf Cost Calculator – Kissimmee & Central Florida",
                "Enter your yard's size and project type to see a 2026 Central Florida installed cost range, plus base rock and infill quantities.",
                "Artificial turf cost and materials calculator",
                capsule(f"Enter the length and width of the area, pick the project type, and the calculator returns a {PRICE_DATE} Central Florida installed range along with the cubic yards of base rock and pounds of infill the job needs. It's arithmetic on published market ranges, so treat the result as a planning number."),
                calc_body, crumbs=[("Turf cost", "/artificial-turf-cost/")], crumb="Calculator", sources=["attampa-cost", "lbs-fl-cost", "angi-putting", "mightygrass-playground"],
                related=[("/artificial-turf-cost/", "Full turf cost guide with tables"), ("/tools/turf-vs-sod/", "Turf vs. sod ten-year calculator")])
    return [hub, calc]


from _data import PHONE_DISPLAY as PHONE  # noqa: E402
