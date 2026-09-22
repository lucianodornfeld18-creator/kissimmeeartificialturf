# -*- coding: utf-8 -*-
"""Compare hub: /compare/ plus the six comparisons registered in _posts.COMPARES.
Each comparison is a head-to-head with a table, per-criterion H2s, a pick-this/pick-that
section, a worked example and its own FAQs. Does not paraphrase c_pricing.py or the
service pages; goes deeper into the specific trade-off implied by its own slug."""
from _helpers import page, capsule, sec, table, faq, ul, price, a, svc, post, src, ext

# ---------------------------------------------------------------- sources not yet in _data.SOURCES
IFAS_SELECT = ("UF/IFAS EDIS ENH04/LH005 -- Selecting a Turfgrass for Florida Lawns", "https://ask.ifas.ufl.edu/publication/LH005")
IFAS_CHINCH = ("UF/IFAS EDIS IN383 -- southern chinch bug in St. Augustinegrass", "https://edis.ifas.ufl.edu/in383")
OSCEOLA_SOD = ("Osceola Sod and Irrigation Service -- 2026 Bahia and Zoysia sod price guide", "https://www.osceolasod.com/blog/how-much-is-a-pallet-of-bahia-or-zoysia-sod-in-florida-2026-price-guide")
ZEOLITE_HOW = ("Synthetic Grass Warehouse -- Ask JW: zeolite, a complement to turf infill", "https://syntheticgrasswarehouse.com/company/ask-an-expert/ask-jw/zeolite-a-perfect-complement-to-your-infill/")
ZEOLITE_RATE = ("FlooringInc -- Zeolite Max, odor-blocking turf infill for pets and play areas", "https://www.flooringinc.com/zeolite-max-9115.html")
FIBER_SRC = ("Houston Turf -- nylon vs. polyethylene vs. polypropylene turf fiber, a comparison", "https://houstonturf.com/blog/nylon-vs-polyethylene-vs-polypropylene-turf-fiber-a-full-comparison/")
PAVER_COST = ("BuildPriced -- Florida paver patio cost, 2026", "https://buildpriced.com/cost/paver-patio")
CPSC_HANDBOOK = ("U.S. CPSC -- Public Playground Safety Handbook, Publication 325", "https://www.cpsc.gov/s3fs-public/325_PublicPlaygroundSafetyHandbook2025_7-30-25_1.pdf")
ASTM_SRC = ("Fibar -- playground safety and industry standards: ASTM F1292 and F1951", "https://www.fibar.com/industry-standards-information")
RUBBER_COST = ("Angi -- rubber playground flooring cost, 2026", "https://www.angi.com/articles/rubber-playground-flooring-cost.htm")
MULCH_COST = ("Playground Authority -- playground safety surfacing compared, 2026", "https://www.playgroundauthority.com/blog/playground-safety-surfacing-compared/")
SUNBIZ = ("Florida Division of Corporations -- Sunbiz business entity search", "https://search.sunbiz.org/")
OSCEOLA_TAX = ("Osceola County Tax Collector -- local business tax receipt", "https://osceolataxcollector.org/local-business-tax-receipt/")


def get_pages():
    pages = [
        _index(),
        _grass(),
        _infill(),
        _fiber(),
        _sideyard(),
        _installer(),
        _playground(),
    ]
    return pages


# ================================================================== /compare/ index
def _index():
    body = "".join([
        sec("How we compare turf against the alternatives",
            "<p>Every comparison on this site gets judged against the same six things, because those are what actually change on a lot around Kissimmee, not what changes in a showroom. We weigh installed and ten-year cost, how a surface handles full Florida sun, how it drains through a summer downpour, whether it fights the sandy, seasonally wet soil most yards sit on, whether it clears Florida's synthetic turf standard that took effect May 19, 2026, and whether a homeowners association is likely to sign off on it.</p>"
            + ul(["<strong>Heat.</strong> A play area or dog run gets used at 4 p.m. in July, not just in a spec sheet photo, so surface temperature matters more here than in most of the country.",
                  "<strong>Rain.</strong> Central Florida's wet season routinely drops an inch or more in an hour. A material that looks fine in a dry-climate review can pond here.",
                  "<strong>Sand.</strong> Native soil around Kissimmee is fine, fast-draining sand with a seasonally high water table, which changes how a base performs under any surface.",
                  f"<strong>The 2026 state rule.</strong> {src('dep-rule', 'Rule 62-308.100')} sets requirements for synthetic turf on single-family lots that don't apply to sod, pavers or rock, so a fair comparison has to say which side of that line each material sits on.",
                  "<strong>HOA acceptance.</strong> A material that a board approves without argument is worth more in practice than one that wins every other category and stalls in architectural review.",
                  "<strong>Ten-year cost.</strong> An installed price only tells part of the story. What a surface costs to keep up over a decade often reorders the ranking."])),
        sec("What these comparisons are not",
            f"<p>None of the six pages below name a winner for every yard, because there isn't one. A shaded side yard, a fenced dog run and a swing-set play area call for different answers even on the same lot. Each comparison ends with a plain \"pick this if / pick that if\" section instead of a single verdict, and each links back to the relevant {a('/artificial-turf-cost/', 'cost guide')} and service pages so the numbers here stay consistent with the rest of the site.</p>"),
        sec("Quick verdicts",
            table("Six comparisons, quick verdicts as of September 2026",
                  ["Comparison", "Quick verdict", "Read the full comparison"],
                  [["Turf vs. St. Augustine, Zoysia, Bahia", "Turf costs more up front; Bahia is the cheapest lawn Osceola County grows if rainfall is enough irrigation for you", a("/compare/artificial-turf-vs-st-augustine-zoysia-bahia/", "Full comparison")],
                   ["Zeolite vs. silica vs. antimicrobial infill", "Plain silica is fine without pets; a dog yard usually wants zeolite or coated sand, and both are legal under the 2026 rule", a("/compare/zeolite-vs-silica-vs-antimicrobial-infill/", "Full comparison")],
                   ["Nylon vs. polyethylene vs. polypropylene turf", "Polyethylene is the residential lawn fiber almost everywhere here; nylon shows up on putting greens, polypropylene mostly in backing", a("/compare/nylon-vs-polyethylene-vs-polypropylene-turf/", "Full comparison")],
                   ["Turf vs. pavers vs. rock, side yard", "All three work in a narrow, shaded side yard; none of them belong in the drainage swale", a("/compare/turf-vs-pavers-vs-rock-side-yard/", "Full comparison")],
                   ["Local installer vs. national franchise", "Neither model guarantees the job; what matters is who shows up and who backs the warranty", a("/compare/local-turf-installer-vs-national-franchise/", "Full comparison")],
                   ["Playground turf vs. mulch vs. poured rubber", "All three can meet federal fall-height guidance; upkeep and heat, not safety, usually decide it", a("/compare/playground-turf-vs-mulch-vs-poured-rubber/", "Full comparison")]],
                  "Verdicts are a starting point. Each linked page has the full table, sources and a worked example.")),
        sec("Turf against St. Augustine, Zoysia and Bahia",
            f"<p>Homeowners rarely ask us to compare turf against sod in the abstract; they ask because a specific lawn is failing. {a('/compare/artificial-turf-vs-st-augustine-zoysia-bahia/', 'This comparison')} lines up installed cost, shade tolerance, chinch bug exposure and irrigation need across all four surfaces, using UF/IFAS ratings rather than a sales pitch for either side. Bahia comes out looking better than most people expect.</p>"),
        sec("Zeolite, silica and antimicrobial infill",
            f"<p>Infill is the one choice on a turf quote that changes almost entirely because of pets, and {a('/compare/zeolite-vs-silica-vs-antimicrobial-infill/', 'this page')} answers the question we get asked most directly at a consultation: which of the three actually keeps a yard from smelling like a kennel. It also covers what Florida's 2026 material rule allows and where crumb rubber still legally fits.</p>"),
        sec("Nylon, polyethylene and polypropylene fiber",
            f"<p>Spec sheets throw around fiber names without explaining why one shows up on a putting green and another shows up in a backing layer you never see. {a('/compare/nylon-vs-polyethylene-vs-polypropylene-turf/', 'The fiber comparison')} covers softness, resilience and how hot each one gets before it softens, with the polymer data cited rather than asserted.</p>"),
        sec("Turf, pavers and rock for a side yard",
            f"<p>Side yards get more comparison requests than any other spot on a lot, mostly because they're narrow, shaded, and often carry an AC condensate line or a drainage swale that limits the options before price even comes up. {a('/compare/turf-vs-pavers-vs-rock-side-yard/', 'This comparison')} walks through all three surfaces against those specific constraints instead of a generic backyard.</p>"),
        sec("Local installer or national franchise",
            f"<p>This is the one comparison where we have an obvious stake, since we're a local crew ourselves, so {a('/compare/local-turf-installer-vs-national-franchise/', 'the page')} tries to stay useful to someone comparing bids rather than making a case for either model. It focuses on who actually shows up, how subcontracting works, and what happens to a warranty if a business closes.</p>"),
        sec("Playground turf, mulch and poured rubber",
            f"<p>Play-area surfacing is judged by a federal safety standard before it's judged by looks, and {a('/compare/playground-turf-vs-mulch-vs-poured-rubber/', 'this comparison')} explains what the Consumer Product Safety Commission's handbook actually asks for, what each surface costs to keep compliant over time, and where Florida's 2026 turf rule carves out an exception for rubber right under the swing set.</p>"),
        sec("Using more than one comparison at a time",
            f"<p>Most real projects touch two or three of these questions at once, not just one. A homeowner turfing a backyard for a dog usually ends up reading the {a('/compare/artificial-turf-vs-st-augustine-zoysia-bahia/', 'grass comparison')} to confirm the lawn is worth replacing at all, then the {a('/compare/zeolite-vs-silica-vs-antimicrobial-infill/', 'infill comparison')} to pick what goes between the blades, and sometimes the {a('/compare/local-turf-installer-vs-national-franchise/', 'installer comparison')} while collecting bids. Reading them in that order, problem first, then material choice, then who does the work, tends to make each one easier to act on than reading all six at once.</p>"),
    ])
    return page("/compare/", "compare",
                "Artificial Turf Comparisons for Kissimmee, FL Yards",
                "Six 2026 comparisons for Central Florida yards: turf vs. sod, infill types, fiber types, pavers, installers and playground surfacing, each with sources.",
                "How we compare turf, sod, infill, fiber and surfacing choices",
                capsule("As of September 2026, six head-to-head comparisons on this site weigh artificial turf against St. Augustine, Zoysia and Bahia sod, three infill types, three fiber types, pavers and rock, national franchise installers, and playground surfacing, each scored against the six things that actually change on a Central Florida lot: heat, rain, sandy soil, the state's May 2026 turf rule, HOA acceptance and ten-year cost."),
                body, crumb="Comparisons",
                sources=["dep-rule", "hb683"],
                related=[("/artificial-turf-cost/", "Full turf cost guide"), ("/laws/", "Florida turf laws, HOA rules and permits"), ("/faq/", "Turf FAQ, browsed by topic"), ("/blog/", "The full blog")])


# ================================================================== turf vs. St. Augustine, Zoysia, Bahia
def _grass():
    body = "".join([
        table("Artificial turf vs. St. Augustine, Zoysia and Bahia sod, Central Florida",
              ["Criterion", "Artificial turf", "St. Augustine", "Zoysia", "Bahia"],
              [["Installed cost per sq ft (2026)", price("residential"), "$1-$2", "$2.00-$3.50+", "$1.00-$1.80"],
               ["Shade tolerance", "Not weather-dependent", "Good-excellent, cultivar dependent", "Good-excellent, cultivar dependent", "Fair"],
               ["Drought / irrigation need", "None once installed", "Good tolerance, still wants regular water", "Excellent tolerance", "Excellent; the least water-dependent of the three"],
               ["Wear / foot-traffic tolerance", "Built for daily use", "Poor-fair", "Good-excellent", "Poor"],
               ["Chinch bug exposure", "Not a host for the insect", "Its primary host grass statewide", "Not a preferred host", "Not a preferred host"],
               ["Establishment", "Installed once, no grow-in", "Sod or plugs only, no seed option", "Sod, sprigs, plugs, seed on some cultivars", "Seed or sod"]],
              f"Sod figures from {src('angi-turf', 'Angi')} and {ext(OSCEOLA_SOD[1], 'Osceola Sod and Irrigation Service, 2026')}; turfgrass ratings from {ext(IFAS_SELECT[1], 'UF/IFAS')}."),
        sec("Which costs less to install?",
            f"<p>Bahia, by a wide margin. An Osceola-area supplier prices installed Bahia sod at {ext(OSCEOLA_SOD[1], '$1.00 to $1.80 a square foot')}, St. Augustine typically runs {src('angi-turf', '$1 to $2')}, Zoysia runs {ext(OSCEOLA_SOD[1], '$2.00 to $3.50 or more')} because it's slower to produce and install, and {svc('residential', 'artificial turf')} runs {price('residential')} as of September 2026. On a straight installed-cost basis, every grass beats turf, and Bahia beats the other two grasses.</p>"),
        sec("Which costs less over ten years?",
            f"<p>Turf usually overtakes St. Augustine sod between year five and year eight once mowing, irrigation and pest control are added in, landing at a published {src('bearcat-10yr', '$11,500 to $23,000')} ten-year total on 1,000 sq ft against {src('attampa-sod', '$18,000 to $37,000')} for St. Augustine. Neither Bahia nor Zoysia has a published Florida ten-year model we could find, so we won't invent one. What UF/IFAS ratings do support: Bahia's lower water and wear demands should keep its running costs below St. Augustine's, while Zoysia's water need sits close to St. Augustine's even though it needs less frequent mowing at its shorter cut height.</p>"),
        sec("Which one stays coolest to walk on in a Kissimmee summer?",
            "<p>Any living grass, by a wide margin. Natural lawns stay close to air temperature because the blades are alive and transpiring, while turf in full afternoon sun commonly reaches 120 to 150 degrees and can pass 160. A hose rinse brings turf back down 30 to 50 degrees within minutes, and shade helps both surfaces, but on a bare-sun playset or a dog run, grass simply doesn't get hot the way synthetic fiber does.</p>"),
        sec("Which drains through a Central Florida downpour?",
            f"<p>Turf's backing itself drains faster than the storm can fall, {src('sgw-faq', 'over 30 inches an hour')}, but that number only matters if the base under it is graded and open. A living lawn on Kissimmee's typical sandy soil usually drains well too, once the grade slopes away from the house; the difference shows up on a compacted or poorly graded lot, where grass roots can still find a way through standing water and a badly built turf base cannot.</p>"),
        sec("Which needs the least water and pest control?",
            f"<p>Bahia, on both counts. It's the closest thing to a pasture grass among the three, tolerating drought well enough that it rarely needs supplemental irrigation once established, and it isn't the chinch bug's preferred host the way St. Augustine is. {src('toho-days', 'Toho Water Authority')} still limits most addresses here to two irrigation days a week regardless of species, which is a bigger constraint for St. Augustine's steadier water appetite than for Bahia's.</p>"),
        sec("Which holds up best under kids, dogs and shade?",
            f"<p>For wear, Zoysia rates good to excellent against St. Augustine's poor to fair and Bahia's poor, according to {ext(IFAS_SELECT[1], 'UF/IFAS turfgrass ratings')}, so a high-traffic natural lawn favors Zoysia over the other two grasses. Turf outperforms all three on pure durability since it doesn't thin or bald under a trampoline leg or a dog's regular path along the fence, though {svc('pet', 'pet-specific turf systems')} still need the right infill to stay odor-free under that traffic.</p>"),
        sec("Which will a Central Florida HOA sign off on faster?",
            f"<p>Grass, almost always, because a natural lawn is usually what the declaration already assumes and no architectural review process exists for mowing your own yard. Turf in a visible area needs an ARC application in most communities; {a('/laws/hoa-rules/', 'a fenced backyard not visible from the street or a neighbor')} is protected from that review under Florida law, but a front lawn conversion is not.</p>"),
        sec("Which one actually has to meet Florida's 2026 turf rule?",
            f"<p>Only the synthetic option. {src('dep-rule', 'Rule 62-308.100')} sets installation standards for synthetic turf on single-family lots and has nothing to say about sod, since it was written for a plastic product, not a living one. Choosing St. Augustine, Zoysia or Bahia sidesteps that rule entirely, along with the irrigation-capping and infill restrictions that come with it.</p>"),
        sec("Pick this if, pick that if",
            ul(["<strong>Pick artificial turf</strong> if the lawn has failed repeatedly, if it's under heavy shade where nothing grows well, or if daily wear from kids or dogs keeps outrunning whatever grass you plant.",
                "<strong>Pick St. Augustine</strong> if you want the thick, dense look most Central Florida subdivisions were built around and you're willing to mow, fertilize and treat for chinch bugs.",
                "<strong>Pick Zoysia</strong> if you want a natural lawn that takes more traffic than St. Augustine and are willing to pay more up front for it.",
                "<strong>Pick Bahia</strong> if the yard gets full sun, foot traffic is light, and low water and low fertilizer use matter more to you than a tight, uniform look."])),
        sec("A worked example",
            f"<p>Say you have a 1,000 sq ft front yard in a Poinciana subdivision with full sun and an HOA that requires a maintained lawn. Bahia installs for roughly $1,000 to $1,800 and, once established, needs the least water and pest spending of the three grasses; St. Augustine installs for a similar $1,000 to $2,000 but is the one most likely to need a chinch bug treatment within a summer or two here; Zoysia installs for $2,000 to $3,500 and holds up best if the family uses the front lawn heavily. Turf would run $8,000 to $18,000 for the same area and needs no HOA review at all if the front-yard turf still meets the association's design standards on color and pile height.</p>"),
    ])
    faqs = [
        faq("Does artificial turf ever make sense next to a Bahia-style yard?",
            f"Yes, on the parts of the lot Bahia struggles with. A shaded side yard or a heavily used dog run can go to turf while the rest of the lot stays in Bahia, since the two don't have to match texture the way two grass species growing next to each other would. {a('/compare/turf-vs-pavers-vs-rock-side-yard/', 'The side-yard comparison')} covers that specific situation."),
        faq("Can you mix turf in the backyard with sod in the front?",
            "Yes, and it's a common way to phase the cost. The two surfaces meet cleanly at a fence line or a change in grade, and each area is built to its own standard independently of the other."),
        faq("Is Zoysia worth the extra installed cost if you're not switching to turf at all?",
            "For a high-traffic lawn, often yes. Its wear tolerance rating beats St. Augustine's by a wide margin, and a family that uses the front or side yard heavily may spend less over time re-sodding thin St. Augustine than it would have spent on Zoysia's higher upfront price."),
        faq("Does the 2026 state turf rule affect a yard that stays natural grass?",
            "No. Rule 62-308.100 regulates synthetic turf materials, infill and installation specifically. A lawn that's never converted to turf isn't subject to it, though local watering restrictions and any HOA landscape standards still apply."),
        faq("Which of the three grasses recovers fastest after a hard freeze?",
            "Central Florida rarely sees a freeze severe enough to matter for long, and all three warm-season grasses typically green back up once temperatures return to normal. None of them compares to turf here, since synthetic fiber doesn't brown or die back at all."),
        faq("Is a mixed Bahia-and-turf yard hard to keep looking consistent?",
            "Less than you'd expect, since the two read as intentionally different surfaces rather than a patchy lawn. Keeping a clean edge, a paver strip or a bed line between them helps the transition look planned instead of accidental."),
    ]
    return page("/compare/artificial-turf-vs-st-augustine-zoysia-bahia/", "compare",
                "Artificial Turf vs. St. Augustine, Zoysia, Bahia Sod",
                "Artificial turf runs $8-$18 a sq ft against sod at $1-$3.50 in Osceola County. A UF/IFAS-sourced look at shade, chinch bugs, water and ten-year cost.",
                "Weighing Artificial Turf Against St. Augustine, Zoysia and Bahia Grass",
                capsule("As of September 2026, artificial turf costs $8 to $18 a square foot installed while St. Augustine sod runs about $1 to $2, but sod adds mowing, chinch bug spray and roughly 20,000 to 30,000 gallons of irrigation a year that turf skips; Bahia sod is the cheapest lawn Central Florida grows, at $1.00 to $1.80 a square foot installed in Osceola County."),
                body, faqs=faqs, crumbs=[("Comparisons", "/compare/")], crumb="Turf vs. natural grass",
                sources=["attampa-cost", "lbs-fl-cost", "angi-turf", "lawnstarter-cost", "bearcat-10yr", "attampa-sod", "toho-days", "dep-rule", IFAS_SELECT, IFAS_CHINCH, OSCEOLA_SOD],
                related=[("/artificial-grass-installation/", "Residential turf installation"), ("/artificial-turf-cost/", "Full turf cost guide"), ("/blog/artificial-turf-vs-sod-cost-florida/", "Turf vs. sod, the full ten-year math"), ("/blog/why-new-construction-sod-dies-in-osceola-county/", "Why builder sod struggles here")])


# ================================================================== zeolite vs. silica vs. antimicrobial infill
def _infill():
    body = "".join([
        table("Zeolite vs. silica vs. antimicrobial coated sand, Central Florida infill",
              ["Criterion", "Silica sand", "Zeolite", "Antimicrobial coated sand"],
              [["What it is", "Rounded, natural silica grains", "A porous volcanic mineral", "Silica sand with a bacteria-resistant coating"],
               ["How it handles pet odor", "None on its own", "Traps ammonia by ion exchange, releases it when rinsed or rained on", "Coating resists the bacteria that produce odor, doesn't absorb ammonia"],
               ["Typical application rate", "1.5-2 lb/sq ft", f"About 1 lb/sq ft as a base layer, topped with 1.5-2 lb/sq ft silica ({ext(ZEOLITE_RATE[1], 'FlooringInc')})", "1.5-2 lb/sq ft"],
               ["Added cost over plain silica", "Included in most base quotes", "Roughly $0.50-$1.00/sq ft", "Roughly $0.75-$1.50/sq ft"],
               ["Needs rinsing to keep working", "No, since it doesn't hold odor either way", "Yes; rinsing or rain recharges its trapping capacity", "Less dependent on rinsing, though any infill benefits from one"],
               ["Allowed under Rule 62-308.100 on a home lawn", "Yes, a named natural material", "Yes, a named natural material", "Yes, coated silica sand with a non-toxic coating"]],
              f"Rates from {ext(ZEOLITE_RATE[1], 'a 2026 zeolite product guide')} and {ext(ZEOLITE_HOW[1], 'a synthetic-grass supplier FAQ')}; add-on costs are typical installer differentials, not a quote."),
        sec("What is the best infill for dogs, zeolite, silica or antimicrobial sand?",
            f"<p>For a yard with dogs, zeolite or an antimicrobial coated sand beats plain silica, because silica does nothing to slow the bacteria that turn dog urine into ammonia smell. Between the two, zeolite is the natural-mineral option that needs regular rinsing to keep working, while coated sand relies on its coating rather than a rinse schedule. Neither is a wrong answer; the choice usually comes down to how consistently the yard gets hosed down and how much extra a homeowner wants to spend on infill.</p>"),
        sec("How does zeolite actually trap ammonia?",
            f"<p>Zeolite is a naturally porous mineral whose structure captures ammonium ions through a process suppliers describe as ion exchange, essentially locking odor-causing molecules inside its pores instead of letting them off-gas into the yard {ext(ZEOLITE_HOW[1], '(Synthetic Grass Warehouse)')}. That trapping capacity isn't permanent. A hose rinse, or a Central Florida downpour, flushes the captured ammonia out and effectively resets the mineral, which is why zeolite yards need a regular rinse far more than a silica-only lawn does.</p>"),
        sec("What does an antimicrobial coating actually do?",
            "<p>A coated sand starts as ordinary silica and gets a manufactured layer added that resists bacterial growth on the grain's surface. Since bacteria are what convert urine into the sharp ammonia smell, slowing their growth on the infill itself cuts down odor without relying on the mineral trapping-and-release cycle zeolite depends on. It costs more per pound than either plain silica or zeolite, and it doesn't need a rinse schedule to keep functioning, though rinsing still helps any pet yard.</p>"),
        sec("How much infill does a dog yard actually need per square foot?",
            f"<p>Most pet systems land between 1.5 and 2 pounds per square foot total, whichever infill is chosen. A zeolite build often layers roughly 1 pound of zeolite as a base with silica sand as ballast on top, while a straight zeolite or coated-sand product is typically spread at {ext(ZEOLITE_RATE[1], 'about 1.5 pounds per square foot')} on its own. Under-filling is the more common mistake we see on repair calls; a thin infill layer stands the blades up less and holds less odor-control capacity no matter which product is under it.</p>"),
        sec("Does infill choice change how hot the yard gets?",
            "<p>A little, mostly through color rather than mineral chemistry. Lighter-colored infill reflects slightly more sun than a dark one, and a damp infill layer cools the surface briefly the same way any wet surface does, whether that's plain silica, zeolite or coated sand. None of the three infills discussed here is marketed as a cooling product the way a specialty evaporative infill is, so expect ordinary turf surface temperatures, 120 to 150 degrees in full summer sun, regardless of which one is chosen.</p>"),
        sec("What does Florida's 2026 turf rule say about infill?",
            f"<p>{src('dep-rule', 'Rule 62-308.100')} narrows a home lawn's infill choices down to natural materials, plus a coated sand as long as its coating is non-toxic, which is exactly the silica, zeolite and antimicrobial family this page covers. What the rule pushes out of a home lawn entirely is crumb rubber and other synthetic infill, which it now confines to the ground directly under playground equipment.</p>"),
        sec("Is rubber or crumb infill ever legal on a residential lot?",
            f"<p>Only under playground equipment. If a backyard has a swing set or slide on it, the footprint directly beneath that equipment can use rubber infill under the state standard, but the surrounding lawn, dog run or putting green still has to use silica, zeolite, or coated sand. {a('/compare/playground-turf-vs-mulch-vs-poured-rubber/', 'The playground surfacing comparison')} covers that exception in more depth.</p>"),
        sec("Pick this if, pick that if",
            ul(["<strong>Pick plain silica</strong> if there are no pets, or only a cat that spends limited time outdoors, and budget matters more than odor insurance.",
                "<strong>Pick zeolite</strong> if you have one or two dogs, don't mind rinsing the run every few days, and want a mineral-based option over a manufactured coating.",
                "<strong>Pick antimicrobial coated sand</strong> if multiple dogs use the yard daily, rinsing happens less predictably than you'd like, and the extra cost is worth not depending on a rinse schedule."])),
        sec("A worked example",
            "<p>Say you have two Labradors on an 800 sq ft dog run behind a Hunters Creek pool cage. At 1.5 lb per square foot, that's 1,200 lb of infill either way. Plain silica costs the least but leaves you rinsing more aggressively to manage odor between two large dogs. Zeolite at roughly $0.50 to $1.00 a square foot adds about $400 to $800 to the job and works well if the run gets hosed down every couple of days. Antimicrobial coated sand at $0.75 to $1.50 a square foot adds $600 to $1,200 and is the more forgiving choice on weeks when rinsing slips.</p>"),
    ])
    faqs = [
        faq("Does zeolite infill lose its ammonia-trapping ability over time?",
            "It can slow down if it's rarely rinsed, since the pores stay loaded with trapped ammonia instead of being flushed clean. Regular hose rinsing or normal Central Florida rainfall keeps most systems working for years rather than months."),
        faq("Can silica sand alone control dog-yard odor if it's rinsed constantly?",
            "Frequent rinsing helps any infill, including plain silica, by flushing surface residue before it builds up. It still lacks the trapping or antimicrobial mechanism the other two options rely on, so a multi-dog yard on silica alone usually needs more frequent rinsing to stay comparable."),
        faq("Is antimicrobial coated sand the same thing as rubber infill?",
            "No. Antimicrobial sand is silica sand with a surface coating, and it's specifically allowed on a home lawn under Florida's 2026 rule. Rubber infill is a different material entirely, and the same rule restricts it to the footprint under playground equipment."),
        faq("Do cats need a different infill than dogs?",
            "Not usually a different product, just less of a reason to upgrade from plain silica if the cat spends little time outdoors and doesn't concentrate urine in one spot the way a fenced dog run sees daily traffic."),
        faq("Does the coating on antimicrobial sand wash off in Florida rain?",
            "Manufacturers formulate the coating to bond to the grain rather than sit on top of it, so ordinary rain and rinsing shouldn't strip it. Extremely abrasive cleaning or years of UV exposure can wear any coating down gradually, which is a maintenance question worth asking a specific product's supplier."),
        faq("Can you switch infill types without redoing the whole lawn?",
            "Often yes, by working the old infill out with a power broom or extraction and brushing in the new type at the correct rate. It's closer to a maintenance visit than a reinstall, though a heavily compacted old infill layer may need more effort to remove first."),
    ]
    return page("/compare/zeolite-vs-silica-vs-antimicrobial-infill/", "compare",
                "Zeolite vs. Silica vs. Antimicrobial Turf Infill",
                "Zeolite, silica and antimicrobial coated sand compared for dog yards: how each handles ammonia, pounds per sq ft, added cost and Florida's 2026 infill rule.",
                "Comparing Zeolite, Silica and Antimicrobial Infill for a Dog Yard",
                capsule("As of September 2026, zeolite infill runs about $0.50 to $1.00 a square foot more than plain silica sand, coated antimicrobial sand about $0.75 to $1.50 more, and Florida's Rule 62-308.100 allows all three on a home lawn at roughly 1.5 pounds per square foot, while rubber infill stays legal only under playground equipment."),
                body, faqs=faqs, crumbs=[("Comparisons", "/compare/")], crumb="Infill for dogs",
                sources=["dep-rule", "hb683", "magnolia-pet-cost", "installartificial-pet", ZEOLITE_HOW, ZEOLITE_RATE],
                related=[("/pet-turf/", "Pet turf and dog runs"), ("/artificial-turf-cost/", "Full turf cost guide"), ("/blog/how-to-get-dog-urine-smell-out-of-artificial-turf/", "Getting urine smell out of existing turf"), ("/blog/coolest-artificial-grass-and-infill-for-florida/", "The coolest turf and infill for Florida sun")])


# ================================================================== nylon vs. polyethylene vs. polypropylene
def _fiber():
    body = "".join([
        table("Nylon vs. polyethylene vs. polypropylene turf fiber",
              ["Property", "Nylon", "Polyethylene", "Polypropylene"],
              [["Feel underfoot", "Coarser, stiffer", "Softest of the three", "Moderately soft, less durable feel"],
               ["Resilience after crushing", f"Highest; roughly 40% more resilient than polyethylene ({ext(FIBER_SRC[1], 'Houston Turf')})", "Good, the standard for residential lawns", "Lowest; mats down soonest under repeat weight"],
               ["Softening point", "Roughly 350-400°F, well above the others", "Roughly 200-230°F", "Roughly 190-210°F, softens first"],
               ["Melting point", f"Roughly 450-500°F ({ext(FIBER_SRC[1], 'Houston Turf')})", "Roughly 260-320°F", "Roughly 240-270°F"],
               ["Typical cost tier", "Highest per square yard", "Mid-range, most residential lawns", "Lowest; common in backing and thatch, not the visible pile"],
               ["Where it shows up", "Putting and chipping surfaces, sports turf", "Residential and pet lawns, most of a Kissimmee yard", "Thatch layer, backing fabric, budget products"]],
              f"Thermal and resilience figures from {ext(FIBER_SRC[1], 'a 2026 fiber comparison')}; individual products vary by resin grade and additive package."),
        sec("Which turf fiber makes the better everyday lawn: nylon, polyethylene or polypropylene?",
            f"<p>Polyethylene, for nearly every residential lawn in Central Florida. It balances a soft, grass-like feel with enough UV stability and heat tolerance for daily use, which is why {svc('residential', 'the standard lawn products')} we install are polyethylene rather than nylon or polypropylene. Nylon's extra resilience matters more on a surface that has to roll a golf ball true than on a lawn a family walks across barefoot, and polypropylene's low cost comes with the fastest matting of the three.</p>"),
        sec("Why do putting greens use nylon instead of polyethylene?",
            f"<p>Ball roll punishes any fiber that doesn't spring back upright between shots, and nylon recovers its shape after compression better than polyethylene or polypropylene, which keeps a green rolling consistently over years of foot and ball traffic {ext(FIBER_SRC[1], '(Houston Turf)')}. {svc('putting', 'A backyard putting green')} typically pairs a short nylon putting surface with a taller polyethylene fringe around it, since the fringe doesn't need nylon's stiffness and reads more like a natural lawn edge.</p>"),
        sec("Where does polypropylene actually show up in a turf system?",
            "<p>Rarely as the visible pile on a Central Florida lawn. Its low cost and resistance to absorbing moisture make it a common choice for backing fabric and the tan thatch fibers woven in at the base of the blades, where it never takes direct foot traffic or sun exposure the way the pile does. Where it does appear as the surface fiber, usually on the least expensive turf products, expect it to flatten sooner under regular use than a polyethylene lawn would.</p>"),
        sec("How hot does each fiber get in a Kissimmee summer, and which softens first?",
            f"<p>Polypropylene has the lowest softening point of the three, around 190 to 210 degrees, with polyethylene close behind and nylon well clear of both at roughly 350 to 400 degrees before it starts to give {ext(FIBER_SRC[1], '(polymer data)')}. In practice, ordinary Florida sun rarely pushes any of them that far; the failures we see trace back to a concentrated heat source such as sunlight reflected off a low-emissivity window, not ambient summer heat alone.</p>"),
        sec("Does fiber type change the price per square foot?",
            f"<p>Yes, though it's rarely the only factor on a quote. Polypropylene lawns price at the low end because the fiber itself is inexpensive to produce; polyethylene sits in the middle and covers most of the {price('residential')} residential range; nylon adds a premium most often seen on putting surfaces rather than full lawns, where its extra durability is worth paying for.</p>"),
        sec("Which fiber lasts longest under Florida's UV exposure?",
            "<p>All three fade somewhat over years of direct sun, and manufacturers add UV stabilizers to slow that regardless of which polymer is used. Nylon's resilience advantage shows up more in resisting matting and crushing than in resisting color fade specifically. A shaded lawn of any fiber type will hold its color longer than the same product installed in full, unbroken sun.</p>"),
        sec("Pick this if, pick that if",
            ul(["<strong>Pick polyethylene</strong> for almost any residential lawn, pet yard or pool surround, since it balances softness, heat tolerance and cost better than the other two for everyday use.",
                "<strong>Pick nylon</strong> for a putting or chipping surface, or any spot that takes concentrated, repeated impact where a softer fiber would mat down.",
                "<strong>Pick polypropylene</strong> only where cost is the deciding factor and the area sees light use, or accept it as the backing and thatch layer under a polyethylene or nylon pile, which is where it usually belongs anyway."])),
        sec("A worked example",
            f"<p>Say you want a 450 sq ft backyard putting green in a Celebration yard with an 80 sq ft chipping pad off to the side. The putting surface itself would specify nylon for roll consistency; the fringe around it and the surrounding lawn would specify polyethylene; and the backing fabric under all of it, which nobody sees or touches, is likely polypropylene regardless of which fiber sits on top. A quote that names all three by zone, rather than one blanket \"synthetic grass,\" is the more complete document. {a('/artificial-turf-cost/', 'The cost guide')} covers what that specification adds to the price.</p>"),
    ])
    faqs = [
        faq("Does a nylon lawn feel as soft underfoot as polyethylene?",
            "No, and that's the trade-off. Nylon's coarser texture is part of what gives it superior resilience, which matters on a putting surface but feels less like a natural lawn to bare feet than polyethylene does."),
        faq("Can polypropylene turf cover a whole backyard?",
            "It can, and some budget products are built that way, but expect it to mat down under regular foot traffic sooner than a polyethylene lawn built for the same use. It's a reasonable choice for a low-traffic accent area, less so for a yard kids and dogs use daily."),
        faq("Does fiber type affect how fast a lawn drains?",
            "Not directly. Drainage depends on the backing's perforation and the base underneath, which is independent of whether the pile itself is nylon, polyethylene or polypropylene."),
        faq("Will a nylon lawn actually outlast a polyethylene one in the same yard?",
            "Likely yes on pure wear resistance, but polyethylene's UV stability and lower heat retention make it the more practical choice for most residential settings, so the trade rarely favors nylon outside specialty surfaces like greens."),
        faq("Is checking fiber type on a spec sheet worth the trouble?",
            f"Yes, since a vague quote that only says \"premium synthetic grass\" can hide a polypropylene product priced like a polyethylene one. {post('artificial-turf-glossary', 'The turf glossary')} explains the other spec-sheet terms worth asking about at the same time."),
        faq("Does Florida's 2026 turf rule regulate which fiber a lawn uses?",
            f"No. {src('dep-rule', 'Rule 62-308.100')} addresses heavy metals, added PFAS, infill material and installation details, not the specific polymer family of the pile. A nylon, polyethylene or polypropylene lawn all have to meet the same PFAS and heavy-metal standard regardless of fiber choice."),
    ]
    return page("/compare/nylon-vs-polyethylene-vs-polypropylene-turf/", "compare",
                "Nylon vs. Polyethylene vs. Polypropylene Turf",
                "Nylon, polyethylene and polypropylene turf fiber compared on softness, resilience, softening point and where each belongs, with 2026 polymer data cited.",
                "Comparing Turf Fiber: Nylon, Polyethylene and Polypropylene",
                capsule("As of September 2026, nylon turf fiber resists crushing roughly 40 percent better than polyethylene but doesn't start to soften until around 350 degrees Fahrenheit, well above polyethylene's 200 to 230, which is why almost every Central Florida lawn is polyethylene, nylon shows up mainly on putting greens, and polypropylene stays a budget backing or thatch layer rather than a lawn's visible fiber."),
                body, faqs=faqs, crumbs=[("Comparisons", "/compare/")], crumb="Turf fiber compared",
                sources=["stn-life", "dep-rule", FIBER_SRC],
                related=[("/putting-greens/", "Backyard putting green installation"), ("/artificial-grass-installation/", "Residential turf installation"), ("/blog/artificial-turf-glossary/", "Turf terms explained"), ("/blog/can-artificial-turf-melt/", "Can artificial turf melt?")])


# ================================================================== turf vs. pavers vs. rock, side yard
def _sideyard():
    body = "".join([
        table("Turf vs. pavers vs. rock for a Central Florida side yard",
              ["Criterion", "Turf", "Pavers", "Rock / gravel"],
              [["Installed cost per sq ft (2026)", price("residential"), f"{ext(PAVER_COST[1], '$12-$32')}", "Priced by the yard of material and delivery, not a fixed per-square-foot rate"],
               ["Drains a heavy storm", f"Backing alone drains {src('sgw-faq', 'over 30 in/hr')}; depends on the base beneath it", "Depends on joint sand and base; permeable pavers exist, standard ones can pond", "Drains well loosely laid, but migrates without an edge to hold it"],
               ["Handles shade and dampness", "Fine if the base is graded; can stay damp longer under a dense canopy", "Can grow algae or moss in a shaded, damp strip", "Same algae risk as pavers in a shaded, damp strip"],
               ["Surface heat in full sun", "120-150°F, similar to dark hardscape", "Gets hot too, especially dark pavers", "Can get hot and shift underfoot when it does"],
               ["Dogs", "Best footing for daily running", "Fine, though a determined digger can work at joint sand", "Paws pick up loose stone, tracked indoors"],
               ["Upkeep", "Infill top-up, occasional rinse", "Joint sand refresh, periodic pressure washing", "Weed control, periodic topping off as it settles or scatters"]],
              f"Paver range from {ext(PAVER_COST[1], 'a 2026 Florida paver cost guide')}; drainage rate for turf backing from {src('sgw-faq', 'a manufacturer FAQ')}."),
        sec("Which drains best down a narrow, shaded side yard?",
            f"<p>Turf, if the base underneath is built right, since its {src('sgw-faq', 'perforated backing drains faster than a Central Florida storm falls')}. That advantage disappears on a poorly graded base, which is the more common failure point than the turf itself. Pavers with proper joint sand and a compacted aggregate base drain reasonably well too, and loose rock over landscape fabric drains fastest of all but has nothing holding it in place once water starts moving.</p>"),
        sec("What happens if any of the three run through the drainage swale?",
            f"<p>Turf specifically can't. {src('dep-rule', "Florida's synthetic turf standard")} keeps synthetic turf out of a swale, ditch or stormwater pond entirely, since covering the flow line defeats the reason the swale exists. The rule doesn't name pavers or rock because it only regulates synthetic turf, but we treat the swale the same regardless of material: none of the three belongs on the flow line, because blocking it usually just moves the water problem to wherever the swale was supposed to carry it.</p>"),
        sec("Does shade change which material makes sense?",
            "<p>Somewhat. A side yard shaded most of the day by the neighboring roofline or a fence line often already has damp, compacted soil where grass never took hold, which is exactly the condition a well-drained turf or paver base corrects. Rock in deep, permanent shade tends to collect leaf litter and stay damp longer than the other two, which can show up as algae or moss faster than on turf or pavers.</p>"),
        sec("Which costs less to install in a typical Kissimmee side yard?",
            f"<p>Rock, usually, since it's sold and delivered by the yard rather than installed as a finished system, though it comes with the least polished look and the most long-term drift. Pavers run {ext(PAVER_COST[1], '$12 to $32 a square foot')} depending on the material, with concrete pavers at the low end of that range. Turf runs {price('residential')}. A narrow strip of any of the three often prices at the top of its range, since a crew and equipment show up regardless of the area's size.</p>"),
        sec("Which stands up best to a dog running the fence line?",
            f"<p>Turf, for a side yard that doubles as a dog's regular path. {svc('pet', 'Pet-specific turf builds')} handle repeated running better than pavers, which can loosen at the joints under a dog wearing a groove along one edge, or rock, which shifts and scatters under the same repeated traffic and tends to get tracked into the house on wet paws.</p>"),
        sec("Does an AC condensate line change the recommendation?",
            "<p>It's worth planning around rather than avoiding outright. A condensate line drips steadily in a small, wet path, and turf handles that fine as long as the base grades that moisture away instead of trapping it against the backing. Pavers and rock can develop a stain or a mossy patch right at the drip point if that specific spot doesn't get the same drainage attention as the rest of the run.</p>"),
        sec("Which needs the least upkeep over ten years?",
            "<p>Turf edges out pavers here, mostly because pavers need their joint sand refreshed periodically and benefit from an occasional pressure wash to stay looking new, while turf mainly needs infill topped up and a rinse now and then. Loose rock asks for the most ongoing attention of the three, since it migrates, collects debris, and needs weed control unless a fabric barrier and edge restraint are both done correctly at installation.</p>"),
        sec("Pick this if, pick that if",
            ul([f"<strong>Pick turf</strong> if the side yard sees regular dog traffic, if you want the lowest long-term upkeep, or if you're tying it visually into {post('artificial-grass-for-shady-side-yards', 'a backyard lawn')} you're also converting.",
                "<strong>Pick pavers</strong> if the side yard doubles as a walkway between the front and back, since a firm, level surface matters more there than in a strip nobody walks.",
                "<strong>Pick rock or gravel</strong> if budget is the main driver, the area is small, and you're comfortable with occasional top-offs and a less finished look."])),
        sec("A worked example",
            f"<p>Say you have a 4-foot-wide, 40-foot-long side yard in Hunters Creek, 160 sq ft total, shaded most of the day by the neighbor's roofline. An AC condenser and its drain line sit halfway down, and a shallow swale runs along the fence for the first 15 feet. The swale section stays open regardless of material, per the state rule if turf is chosen there and as ordinary drainage practice either way. The remaining 100 or so sq ft could take turf at roughly $1,400 to $2,400 for the strip, pavers at $1,700 to $4,600, or a gravel bed for meaningfully less, with the condensate line's drip path graded to shed water away from the base no matter which surface goes down.</p>"),
    ])
    faqs = [
        faq("Can turf go right up to an AC condensate line?",
            "Yes, as long as the base under that section is graded so the drip path sheds water away rather than pooling against the turf's backing. Leaving a small gravel or splash-block area right at the drip point is a common way installers handle it."),
        faq("Does a paver side yard need the same washed base a turf side yard does?",
            "A similar principle, different material. Pavers sit on a compacted aggregate base rather than the specific washed, open-graded rock Florida's turf rule requires, but both approaches share the same goal of a stable, well-draining foundation under the finished surface."),
        faq("Will loose rock stay in place in a Central Florida downpour?",
            "Reasonably well if it's contained by an edge restraint and laid over landscape fabric, though a hard, fast storm can still wash smaller stone toward the low point of a slope. Larger decorative stone holds its place better than fine gravel in heavy runoff."),
        faq("Can you mix turf and pavers in the same side yard?",
            f"Yes, and it's a common layout: a paver walkway strip flanked by narrow turf borders, or turf as the main surface with a paver stepping path. {svc('pavers', 'Turf set between pavers')} covers that specific combination."),
        faq("Does a side yard need its own permit if it includes a swale?",
            f"It depends on the jurisdiction and whether the work touches the swale's grading. {a('/laws/permits/', 'The permit guide for your city or county')} lists what each office requires before digging near a drainage feature."),
        faq("Which option is easiest to change your mind about later?",
            "Rock, since it can be raked out and replaced without demolition. Turf comes out in sections without disturbing a compliant base underneath it, which can often be reused. Pavers are the most labor-intensive to remove and are usually the final word on a side yard's surface once installed."),
    ]
    return page("/compare/turf-vs-pavers-vs-rock-side-yard/", "compare",
                "Turf vs. Pavers vs. Rock for a Side Yard",
                "Turf, pavers and loose rock compared for a shady Central Florida side yard: drainage, AC condensate, dogs, heat, cost and the state rule's swale exclusion.",
                "Turf, Pavers or Rock: What Actually Works in a Shady Side Yard",
                capsule("As of September 2026, a Central Florida side-yard job runs about $8 to $18 a square foot for turf, $12 to $32 for pavers and considerably less for loose rock delivered by the yard, but Florida's Rule 62-308.100 keeps turf out of the drainage swale that usually runs down the middle, which decides the layout before price does."),
                body, faqs=faqs, crumbs=[("Comparisons", "/compare/")], crumb="Turf vs. pavers vs. rock",
                sources=["attampa-cost", "lbs-fl-cost", "sgw-faq", "magnolia-drain", "dep-rule", PAVER_COST],
                related=[("/turf-and-pavers/", "Turf between pavers"), ("/artificial-grass-installation/", "Residential turf installation"), ("/blog/artificial-grass-for-shady-side-yards/", "Artificial grass for shady side yards"), ("/artificial-turf-cost/", "Full turf cost guide")])


# ================================================================== local installer vs. national franchise
def _installer():
    body = "".join([
        table("What to check: local installer vs. national franchise",
              ["What to check", "Often true of a small local installer", "Often true of a national franchise brand"],
              [["Who shows up on installation day", "The owner or a small, fixed crew you can usually name in advance", "A local dealer licensed to use the brand, staffed by that dealer's own crew, not corporate employees"],
               ["Subcontracting", "Direct-hire in most cases, since there's little layer to subcontract through", "The \"franchise\" is itself an independently owned local business, so a second layer of subcontracting is uncommon but worth asking about"],
               ["Warranty backing", "A workmanship warranty tied to that specific business's continued operation", "Product warranty is sometimes centralized with the manufacturer; workmanship warranty still rests on the local dealer"],
               ["Response after a storm", "Depends on that business's current workload, not on its size", "Depends on the local dealer's workload; a national name doesn't guarantee faster local service"],
               ["How you find them", "Word of mouth, local search, neighborhood recommendations", "National advertising and a review base aggregated across many locations"],
               ["What to verify either way", f"{ext(SUNBIZ[1], 'Sunbiz registration')}, {ext(OSCEOLA_TAX[1], 'a local business tax receipt')}, insurance, a written scope", "Same four items, checked against the specific local dealer, not the national brand name"]],
              "General patterns, not a rule that holds for every company on either side."),
        sec("Who actually shows up to do the work?",
            "<p>With a small local crew, it's usually the same one or two people from the estimate through the walkthrough, which makes it easier to hold someone specific accountable for the finished job. A national franchise brand almost always operates through independently owned local dealers, so the crew on your yard works for that dealer, not for a corporate office, even though the truck and the paperwork carry the national name.</p>"),
        sec("What does subcontracting mean for a turf job, and does it matter which model you pick?",
            "<p>Subcontracting means the company that sold you the job isn't the company whose employees install it. It happens on both sides of this comparison, and the model itself, local or franchise, doesn't predict it reliably. The more useful question at the estimate is direct: who is actually digging up the yard, and does that crew work for the person standing in front of you.</p>"),
        sec("Whose warranty are you really relying on?",
            f"<p>Two separate documents apply either way: a manufacturer's product warranty on the turf itself, and a workmanship warranty from whoever installed it. {post('what-does-artificial-turf-warranty-cover', 'What a turf warranty actually covers')} explains the difference in more depth. A franchise's product warranty is sometimes backed at the manufacturer level regardless of which dealer sold it, while the workmanship portion, the part that covers a seam opening or a base settling, almost always rests on that specific local business staying open.</p>"),
        sec("Which one responds faster after a hurricane or a failed seam?",
            "<p>Neither model has a built-in advantage here. A busy local crew with a backlog after a named storm responds just as slowly as a busy franchise dealer would, and a slow season helps either one respond faster. What predicts response time better than company size is how that specific business currently balances new installs against warranty and repair calls.</p>"),
        sec("Does a national name mean more reviews you can trust?",
            "<p>More reviews, not necessarily more trustworthy ones. A national brand's review count is often aggregated across dozens of independently run locations, so a strong national average can mask a weak local dealer, and a thin local review count for a small company isn't automatically a red flag if the work you can see locally holds up. Read reviews from the specific location or crew doing your job, not the brand's national total.</p>"),
        sec("What should you verify no matter which one you're calling?",
            f"<p>Florida doesn't license turf installation as a trade {src('dbpr', "(there's no state landscaping or turf license to look up)")}, so verification means checking business fundamentals instead: an active {ext(SUNBIZ[1], 'Sunbiz')} registration, a current {ext(OSCEOLA_TAX[1], 'local business tax receipt')} for wherever the business operates, proof of insurance, and a written scope with the specifics {post('how-to-compare-artificial-turf-quotes', 'a complete quote should name')}. {post('do-turf-installers-need-a-license-in-florida', 'This page')} goes through what Florida does and doesn't require of anyone in this trade.</p>"),
        sec("Pick this if, pick that if",
            ul(["<strong>Consider a local installer</strong> if direct contact with the person doing the work matters to you, or if you'd rather support a business based in the county where you live.",
                "<strong>Consider a national franchise</strong> if a recognized brand name and a manufacturer-backed product warranty independent of any single local dealer matter more to you than who specifically shows up.",
                "<strong>Either way</strong>, get the same five specifics in writing and check the same four verification items before signing, since the model itself predicts less about the outcome than the specific business does."])),
        sec("A worked example",
            "<p>Say you get two bids for the same 900 sq ft backyard in St. Cloud: one from a two-truck local crew, one from a dealer operating under a national franchise brand. Both quote a similar turf product at a similar price. The local bid comes with the owner's cell number and a handshake on the workmanship warranty; the franchise bid comes with a printed manufacturer warranty card and a dealer's business card with the brand's logo on it. Neither detail tells you which crew compacts a base better. Asking each one the same five spec questions, and checking each one's Sunbiz and insurance status independently of what name is on the truck, tells you more than the logo does.</p>"),
    ])
    faqs = [
        faq("Is a franchise's turf actually a different product than a local installer's?",
            "Not necessarily. Many local and franchise installers alike buy from the same handful of national turf manufacturers, so the product itself may be identical while the installation crew, warranty structure and price differ by company, not by model."),
        faq("What happens to a warranty if a franchise dealer goes out of business?",
            "It depends on whether the product warranty is backed by the manufacturer directly or by the closed dealer. A manufacturer-backed product warranty typically survives a dealer closing; a workmanship warranty tied only to that dealer usually doesn't. Ask this question before signing, for a franchise or a local company alike."),
        faq("Do national brands carry better insurance than local companies?",
            "Not automatically. Insurance requirements vary by individual business, not by whether it operates under a national name. Ask to see a certificate of insurance rather than assuming size or brand recognition implies coverage."),
        faq("Is it fair to assume a local company will be around longer than a franchise dealer?",
            "No, longevity varies business to business on both sides. A well-run franchise dealer can operate in the same county for decades, and a small local company can close after one bad season. Years in a specific location, which you can check independently, tells you more than the business model."),
        faq("Does either model handle HOA paperwork differently?",
            f"Not structurally. {a('/laws/hoa-rules/', 'An ARC application')} needs the same sample, spec sheet and site plan regardless of who submits it. Some installers, local or franchise, offer to assemble that packet as part of the quote; others leave it to the homeowner, so ask either one directly."),
        faq("Should the size of the company change how many bids you get?",
            "Not really. Two or three bids that name the same five specifics let you compare fairly whether the businesses behind them are large franchise operations or two-person local crews."),
    ]
    return page("/compare/local-turf-installer-vs-national-franchise/", "compare",
                "Local Turf Installer or National Franchise?",
                "Choosing between a local turf installer and a national franchise dealer in Central Florida: who shows up, subcontracting, warranty backing and storm response.",
                "Choosing Between a Local Turf Installer and a National Franchise",
                capsule("As of September 2026, Central Florida homeowners weighing a turf bid choose between small local crews working within roughly 40 miles of home and national franchise brands operating through independent local dealers; neither model guarantees the outcome by itself, and what actually predicts it is who shows up on installation day, how subcontracting works, and what stands behind the warranty after a storm."),
                body, faqs=faqs, crumbs=[("Comparisons", "/compare/")], crumb="Local vs. franchise",
                sources=["dbpr", SUNBIZ, OSCEOLA_TAX],
                related=[("/blog/do-turf-installers-need-a-license-in-florida/", "Does a turf installer need a license?"), ("/blog/how-to-compare-artificial-turf-quotes/", "How to compare two turf quotes"), ("/blog/what-does-artificial-turf-warranty-cover/", "What a turf warranty covers"), ("/artificial-turf-cost/", "Full turf cost guide")])


# ================================================================== playground turf vs. mulch vs. poured rubber
def _playground():
    body = "".join([
        table("Playground turf vs. engineered wood mulch vs. poured-in-place rubber",
              ["Criterion", "Playground turf", "Engineered wood mulch", "Poured-in-place rubber"],
              [["Installed cost per sq ft (2026)", price("playground"), f"{ext(MULCH_COST[1], '$6-$12')}", f"{ext(RUBBER_COST[1], '$10-$18')}"],
               ["Impact attenuation (fall cushioning)", "Depends on shock pad thickness matched to equipment fall height", "Depends on maintained loose-fill depth, which settles and needs topping off", "Engineered per pour thickness; consistent as long as it isn't worn through"],
               ["Wheelchair / stroller accessibility", "Firm, stable surface once installed", "Loose fill is the hardest of the three to keep compliant without added routes or mats", "Firm, stable, unitary surface, generally the easiest to keep accessible"],
               ["Surface heat in full sun", "120-150°F, similar to a home lawn", "Stays closest to air temperature of the three", "Can run as hot as or hotter than turf in direct sun, especially dark colors"],
               ["Upkeep", "Infill top-up, occasional cleaning", "Annual replenishment as it compacts, blows and washes away", "Lowest routine upkeep; a worn or torn section needs a specialized patch"],
               ["Typical lifespan", f"{src('stn-life', '10-20 years')}, shorter under heavy public use", "Needs partial replenishment yearly; a full refresh every few years", f"Roughly {ext(RUBBER_COST[1], '10-15 years')} before a full resurfacing"]],
              f"Mulch and rubber costs from {ext(MULCH_COST[1], 'a 2026 surfacing cost comparison')} and {ext(RUBBER_COST[1], 'a 2026 rubber flooring cost guide')}; turf cost from {src('mightygrass-playground', 'a 2026 playground turf cost guide')}."),
        sec("What does the CPSC actually require for playground surfacing?",
            f"<p>The {ext(CPSC_HANDBOOK[1], "U.S. Consumer Product Safety Commission's Public Playground Safety Handbook")} sets fall-height and cushioning guidance so a child falling from equipment lands on a surface that absorbs enough impact to reduce injury, tested in the lab under {ext(ASTM_SRC[1], 'ASTM F1292')}. None of the three surfaces here is inherently compliant or non-compliant; each has to be built or maintained to the depth or pad thickness that matches the specific equipment's fall height, which is a design number, not a property of the material alone.</p>"),
        sec("Which surface is easiest to keep wheelchair-accessible?",
            f"<p>A firm, stable, unitary surface tests more consistently for accessibility, and {ext(ASTM_SRC[1], 'ASTM F1951')} is the specific standard that measures it. Poured-in-place rubber and properly installed turf both behave as a continuous, stable surface. Loose-fill mulch can meet the same standard, but keeping it firm and stable at accessible routes takes more consistent maintenance than a unitary surface does, since raked or displaced mulch changes the surface's stability day to day.</p>"),
        sec("Which gets hottest in a Florida summer?",
            "<p>Poured rubber and turf both run hot in direct sun, commonly 120 to 150 degrees or more, with dark-colored rubber sometimes running hotter than turf in the same exposure. Mulch stays noticeably closer to air temperature since wood doesn't retain heat the way a synthetic surface does. On an unshaded public playground in July, that difference is worth weighing alongside safety and upkeep, not instead of them.</p>"),
        sec("Which needs the most year-round upkeep?",
            f"<p>Mulch, by a clear margin. Loose fill compacts, blows and washes toward low spots, so keeping its depth even across the whole use zone takes regular raking and periodic replenishment, a detail the {ext(CPSC_HANDBOOK[1], 'CPSC handbook')} flags directly since a thinned-out spot loses cushioning exactly where a fall is likely. Turf needs infill topped up occasionally; poured rubber needs the least routine attention but is the hardest and most specialized of the three to patch once it tears or wears through.</p>"),
        sec("What does Florida's 2026 turf rule allow under a backyard swing set?",
            f"<p>An exception most homeowners don't expect. {src('dep-rule', 'Rule 62-308.100')} bars rubber and other synthetic infill everywhere else on a single-family lot, but it specifically allows that infill within the footprint of playground equipment. In practice, that means a backyard swing set can sit on turf with rubber infill directly under the swings and slide, while the surrounding play lawn and the rest of the yard stay on silica, zeolite or coated sand.</p>"),
        sec("Which costs the least to install, and which costs the least over ten years?",
            f"<p>Mulch installs cheapest, at {ext(MULCH_COST[1], '$6 to $12 a square foot')}, against {price('playground')} for turf and {ext(RUBBER_COST[1], '$10 to $18')} for poured rubber. Mulch's annual replenishment cost adds up over a decade, though, while turf and rubber both spread their higher upfront price over ten to twenty years and roughly ten to fifteen years respectively before needing a full redo.</p>"),
        sec("Pick this if, pick that if",
            ul(["<strong>Pick playground turf</strong> for a residential backyard play area where you want a lawn-like look between visits to the equipment itself, and don't mind an occasional infill top-up.",
                "<strong>Pick engineered wood mulch</strong> for a budget-conscious install, public or private, where regular raking and replenishment are realistically going to happen.",
                "<strong>Pick poured-in-place rubber</strong> for a public playground or high-traffic community play area where accessibility and minimal routine upkeep matter more than upfront cost or surface heat."])),
        sec("A worked example",
            f"<p>Say you have a 200 sq ft play area under a swing set in a Celebration backyard, with a 6-foot fall height from the top of the swing seat. Engineered wood mulch at a compliant depth for that fall height would run roughly $1,200 to $2,400 installed and need yearly topping off. {svc('playground', 'Playground turf')} with a shock pad sized to that same fall height runs {price('playground')}, or $2,400 to $5,000 for 200 sq ft, with rubber infill allowed specifically under the swing's footprint per the state rule. Poured-in-place rubber at $10 to $18 a square foot runs $2,000 to $3,600 and needs the least ongoing attention of the three, though it's the least common choice for a residential backyard given the cost and the specialized install.</p>"),
    ])
    faqs = [
        faq("Does a backyard swing set need the same surfacing as a public park?",
            f"The same safety principles apply, fall height and adequate cushioning matter regardless of who owns the equipment, but a public playground typically has to document compliance with {ext(ASTM_SRC[1], 'ASTM standards')} in a way a private backyard doesn't. Building a home play area to the same fall-height guidance is still the responsible choice even without that documentation requirement."),
        faq("Can turf go under a trampoline the same way it goes under a swing set?",
            f"Turf can go under a trampoline, but a trampoline's fall risk and required clearance differ from a swing set's, so the surfacing depth and infill choice should be sized to the specific equipment rather than assumed to carry over. {post('is-artificial-turf-safe-for-kids-pfas-lead', 'This page')} covers infill safety more broadly."),
        faq("How deep does mulch need to be to cushion a fall?",
            f"Depth requirements scale with the equipment's fall height rather than a single fixed number, which is why the {ext(CPSC_HANDBOOK[1], 'CPSC handbook')} ties surfacing depth to fall height tables instead of a flat recommendation. A qualified installer or playground safety inspector can match depth to your specific equipment."),
        faq("Does poured rubber ever crack or lift in Florida heat and humidity?",
            "It can over years of UV exposure and temperature swings, particularly at seams or edges, which is part of why its routine upkeep is low but a needed repair is more specialized than patching turf or adding mulch."),
        faq("Is playground turf infill the same as lawn infill?",
            f"Not always. A play area under equipment can use rubber infill within that specific footprint under Florida's 2026 rule, while a lawn elsewhere on the property is limited to silica, zeolite or coated sand. {a('/compare/zeolite-vs-silica-vs-antimicrobial-infill/', 'The infill comparison')} covers the natural-material options in more depth."),
        faq("Does homeowners insurance care which surface sits under a backyard play set?",
            "Insurers generally underwrite the property and its features broadly rather than certifying a specific playground surface, so ask your carrier directly if a swing set or trampoline is part of the policy discussion, separate from the surfacing choice itself."),
    ]
    return page("/compare/playground-turf-vs-mulch-vs-poured-rubber/", "compare",
                "Playground Turf vs. Mulch vs. Poured Rubber",
                "Playground turf, engineered wood mulch and poured-in-place rubber compared on CPSC fall-height guidance, ASTM accessibility, heat, upkeep and 2026 cost.",
                "Playground Surfacing Compared: Turf, Mulch and Poured-in-Place Rubber",
                capsule("As of September 2026, poured-in-place rubber runs about $10 to $18 a square foot installed, engineered wood mulch $6 to $12, and playground turf with a shock pad $10 to $25, and all three can meet the fall-height cushioning the Consumer Product Safety Commission's playground handbook calls for when built to the right depth or pad thickness."),
                body, faqs=faqs, crumbs=[("Comparisons", "/compare/")], crumb="Playground surfacing",
                sources=["mightygrass-playground", "dep-rule", "stn-life", CPSC_HANDBOOK, ASTM_SRC, RUBBER_COST, MULCH_COST],
                related=[("/playground-turf/", "Playground turf installation"), ("/artificial-turf-cost/", "Full turf cost guide"), ("/blog/is-artificial-turf-safe-for-kids-pfas-lead/", "PFAS, lead and infill safety"), ("/blog/how-hot-does-artificial-turf-get-in-florida/", "How hot artificial turf gets in Florida")])
