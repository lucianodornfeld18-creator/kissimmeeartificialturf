# -*- coding: utf-8 -*-
"""Montverde, FL (Lake County, tier 2). Research checked September 2026.
Primary sources: mymontverde.com (permitting, water/irrigation schedule, Lake Florence Park),
Wikipedia (population, area), montverde.org (Montverde Academy), bellacollina.com (Bella Collina,
Lake Siena), USDA NRCS official series descriptions (Astatula, Candler), PermitHunt (inspection
routing). See SRC below for exact URLs."""
from _helpers import page, capsule, sec, table, faq, a, svc, city, post, src, ext, price
from _cityservice import cityservice_pages

SLUG = "montverde"

SRC = [
    "census-acs",
    ("Town of Montverde — official website", "https://mymontverde.com/"),
    ("Town of Montverde — Water Conservation & Irrigation Schedule", "https://mymontverde.com/water-conservation-irrigation-schedule/"),
    ("Town of Montverde — Lake Florence Park", "https://mymontverde.com/lake-florence-park-montverde-fl/"),
    ("PermitHunt — Town of Montverde building permits", "https://permithunt.com/directory/state/florida/municipality/montverde"),
    ("Wikipedia — Montverde, Florida", "https://en.wikipedia.org/wiki/Montverde,_Florida"),
    ("Montverde Academy — the boarding experience", "https://montverde.org/boarding-school/"),
    ("Bella Collina — community overview", "https://www.bellacollina.com/community-overview"),
    ("Bella Collina — Siena luxury lakefront condos", "https://www.bellacollina.com/siena-luxury-lakefront-condos"),
    ("USDA NRCS — official series description, Astatula series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/A/ASTATULA.html"),
    ("USDA NRCS — official series description, Candler series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/C/Candler.html"),
    ("Lake County Property Appraiser — parcel search", "https://www.lakecopropappr.com/"),
    ("GrowthSpotter, September 2026 — Bella Collina annexation coverage confirming its unincorporated Lake County status",
     "https://www.growthspotter.com/2026/09/01/bella-collina-developer-is-adding-more-than-100-new-homesites-to-the-luxury-residential-community-in-montverde/"),
]

PERMITS = "/laws/permits/lake-county/"
HOA = "/laws/hoa-rules/"
HB683 = "/laws/florida-hb-683/"
COST = "/artificial-turf-cost/"

# ============================================================== HUB
_hub_body = "".join([
    sec("A ridge-top town between two lakes",
        "<p>Montverde covers just 1.88 square miles on the west shore of Lake Apopka, wedged between that lake and the smaller, "
        + ext("https://mymontverde.com/lake-florence-park-montverde-fl/", "131-acre Lake Florence")
        + " at its center, with "
        + ext("https://montverde.org/boarding-school/", "Montverde Academy")
        + "'s campus occupying a chunk of the shoreline in between. The town "
        + src("census-acs", "counted 1,655 residents at the 2020 Census")
        + ", small enough that a single golf-community development on its edge, Bella Collina, can shift what a typical turf inquiry looks like from one year to "
          "the next. What sits under the yard changes fast here too: the same short drive that takes you from a ridge-top lot to the lake's edge can take you "
          "from sand that never holds a drop of rain to ground that barely lets go of it.</p>"),
    sec("Who reviews a building permit in Montverde?",
        "<p>Town Hall handles intake itself rather than sending residents to the county counter: a "
        + ext("https://mymontverde.com/", "Permitting Clerk on Montverde's own staff")
        + " takes applications through the town's own CitizenServe portal, separate from Lake County's system. Inspections on a good share of permits still run "
          "through a contracted outside firm, "
        + ext("https://permithunt.com/directory/state/florida/municipality/montverde", "Alpha Inspections")
        + ", reached by email rather than a town inspector knocking on the door. Montverde doesn't have its own dedicated law page here, so the "
        + a(PERMITS, "Lake County permit page")
        + " above is background on the county's own code, and it's more than background for one well-known Montverde-addressed community: Bella Collina, "
          "despite carrying the town's ZIP code, sits in unincorporated Lake County, not inside the 1.88-square-mile town limits, so a Bella Collina permit "
          "goes through the county rather than Town Hall. A parcel search on the "
        + ext("https://www.lakecopropappr.com/", "Lake County Property Appraiser")
        + "'s site is the fastest way to confirm which side of that line a specific address falls on.</p>"),
    sec("HOA review, Bella Collina, and the state's turf rule",
        "<p>Bella Collina, the 1,900-acre gated golf community on Lake Apopka's south shore that most people associate with Montverde, runs its own "
          "architectural approval for exterior work the way any HOA-governed community does, county land or not; we found no published Bella Collina design "
          "guideline naming synthetic turf specifically, so the honest answer is that a submittal goes through review without a pre-set rule either way. "
          "Florida's "
        + a(HOA, "HOA statute")
        + " already protects a yard that a street or a neighboring lot can't see, and "
        + a(HB683, "the state's turf standard")
        + " sets a floor that applies at Bella Collina exactly as it does on an in-town Montverde lot: permeable turf, natural infill, capped irrigation "
          "heads, and a setback from the shoreline that no HOA document, county code or town ordinance can shrink.</p>"),
    table("Montverde yard types and what we do differently",
          ["Part of town", "What's common on the lot", "What we adjust for it"],
          [["Ridge-top lot away from the lakes", "Elevated, excessively drained Astatula or Candler sand", "Base compacts fast; the main risk is infill sliding downhill on a steep grade rather than drainage"],
           ["In-town cottage near Lake Florence Park", "Older, smaller lot close to the town center", "Tighter access and more hand work; often a shorter, simpler run of turf"],
           ["Bella Collina golf-community estate", "Larger lakefront or golf-frontage lot with an HOA, in unincorporated Lake County despite the Montverde address", "An ARC submittal ahead of time plus a county rather than town permit; more room to grade than an in-town lot"],
           ["Lake Apopka or Lake Florence shoreline", "Rear lot line ending at open water", "The state's 10-ft waterbody setback, staked before turf is ordered, seawall lots excepted"],
           ["Steep ridge slope", "Grade change of several feet across a single yard", "Heavier edge anchoring and a coarser infill grain so material doesn't migrate to the low corner"]],
          "The range doesn't shift by yard type. What moves a quote is slope, access and how much hand-grading a lot needs, not its street."),
    sec("Water: the town's own utility, and a shortage order that reaches every lawn",
        "<p>Montverde draws its drinking water from the Floridan Aquifer through its own utility rather than a county system, and the "
        + ext("https://mymontverde.com/water-conservation-irrigation-schedule/", "St. Johns River Water Management District")
        + " placed the town under a Phase III Extreme Water Shortage Order effective May 11, 2026, tightening what was already a two-day-a-week limit. Under "
          "daylight saving time, even house numbers keep Thursday and Sunday, odd numbers keep Wednesday and Saturday, both outside the 10-to-4 midday window; "
          "once Eastern Standard Time returns each side drops to a single day, Sunday for even addresses and Saturday for odd ones. A capped synthetic lawn "
          "sidesteps the order entirely, since the state's turf standard already forbids watering synthetic turf from an in-ground system regardless of what "
          "the district allows that week.</p>"),
    sec("Excessively drained ridge sand, and where it isn't",
        "<p>Most of Montverde sits on the South-Central Florida Ridge, where "
        + ext("https://soilseries.sc.egov.usda.gov/OSD_Docs/A/ASTATULA.html", "Astatula")
        + ", a very deep, excessively drained sand built from windblown and marine deposits, dominates the higher ground; water passes through it almost as "
          "fast as a hose can put it down. Candler turns up across the same ridge and was originally classified as a variant of Astatula itself, distinguished "
          "mostly by thin, broken bands of finer material starting around 40 inches down that a shallow turf base never reaches anyway. Both soils compact into "
          "a firm, stable base quickly, which is an advantage almost everywhere except on a steep slope, where that same fast drainage does nothing to stop "
          "loose infill from creeping downhill after a hard rain if the edge isn't anchored well.</p>"),
    sec("A small town shaped by a school and a golf gate",
        "<p>With under two thousand residents across less than two square miles, Montverde punches above its size for name recognition, mostly because of "
          "Montverde Academy's boarding students and athletes and Bella Collina's golf membership drawing people from well outside town limits. That mix means "
          "a turf estimate here swings between a modest in-town cottage lot and a multi-acre golf-frontage estate more often than in a town of similar "
          "population without either draw.</p>"),
])

HUB = page("/areas/montverde/", "city",
           "Artificial Turf Installation in Montverde, FL",
           "Artificial turf installers serving Montverde, FL, on the ridge between Lake Apopka and Lake Florence. Permits, water rules and soil, checked 2026.",
           "Artificial turf in Montverde, on the ridge above two lakes",
           capsule(f"Ask what a lawn costs in Montverde and the answer starts with the region's published range, {price('residential')} a square foot "
                   "installed, before slope enters the conversation. September 2026 pricing doesn't move for a ridge-top address near Town Hall or a "
                   "lakefront one on Lake Apopka; what moves is the base plan each lot actually needs."),
           _hub_body,
           faqs=[
               faq("Does Montverde have its own building department?",
                   "Town Hall takes permit applications itself through a Permitting Clerk and its own online portal, rather than routing homeowners to Lake County first, though inspections on many jobs are contracted out to a private firm."),
               faq("Is Bella Collina actually inside the Town of Montverde?",
                   "No, despite the shared ZIP code. Bella Collina sits in unincorporated Lake County, so its permits go through the county rather than Town Hall, though the state's turf standard applies there exactly as it does on a lot inside town limits."),
               faq("Which water management district covers Montverde?",
                   "The St. Johns River Water Management District, which placed the town under a Phase III shortage order in 2026. Montverde's own utility bills separately, but the watering-day restriction still follows the district's schedule."),
               faq("Comparing artificial turf installers near Montverde? The slope plan is the detail worth asking about first.",
                   "Ask each one how they'd anchor the edge on a sloped lot specifically, since that detail separates an installer who's worked the ridge from one who hasn't. A vague answer on slope is a bigger red flag here than anywhere flat."),
               faq("Is Montverde's soil the same as Kissimmee's?",
                   "No. Kissimmee sits on flatwoods sand that holds water near the surface; Montverde's ridge soil, Astatula and Candler, drains almost immediately, which is close to the opposite problem for a base crew to plan around."),
           ],
           sources=SRC, city=SLUG, crumbs=[("Service areas", "/areas/")], crumb="Montverde",
           related=[("/areas/lake-county/", "Turf installers across Lake County"), (PERMITS, "Artificial turf permits in Lake County"),
                    ("/areas/oakland/", "Turf in Oakland"), ("/areas/clermont/", "Turf in Clermont"),
                    (COST, "Turf cost tables for Central Florida")])


# ============================================================== LOCAL
LOCAL = {
    "residential": {
        "title": "Artificial Grass Installation in Montverde, FL",
        "meta": "Artificial grass installation in Montverde, FL: ridge-top Astatula sand, Lake Florence cottages and Bella Collina, priced for 2026.",
        "h1": "Grass installation for Montverde's ridge and lakefront lots",
        "lede": capsule(f"A Montverde lawn conversion runs {price('residential')} a square foot installed, typically {price('residential', True)}, as of "
                        "September 2026. The deciding factor on a given quote is usually slope: a level lot near Lake Florence Park costs less to prep than "
                        "a ridge-top yard with several feet of grade change across it."),
        "sections": [
            ("A ridge lot changes the anchoring plan, not the base recipe",
             "<p>Excessively drained Astatula and Candler sand cover most of "
             + city("montverde", "Montverde")
             + "'s higher ground, and both compact into a firm base quickly once graded. The complication on a sloped lot isn't drainage, since this sand "
             "barely holds water even in a downpour, it's keeping infill from creeping toward the low corner over time. On anything with a real grade change "
             "we run a heavier perimeter anchor at the downhill edge and choose a coarser infill grain, since the state's rule already requires that infill "
             "not wash off the property, and a fine, light sand is the material most likely to migrate first.</p>"),
            ("An in-town cottage near Lake Florence Park is a smaller, faster job",
             "<p>Montverde's older lots near the town center and Lake Florence Park tend to be modest in size, often with a shorter run of lawn than a golf-"
             "community estate and less grading to do overall. Access is the bigger factor here: a narrow side gate or a mature tree close to the house can add "
             "a day to a job that would otherwise be quick, and we walk the route in before quoting rather than assuming a small lot means a small crew.</p>"),
            ("Bella Collina's review process, honestly described",
             "<p>A home at Bella Collina goes through the community's own architectural approval before exterior work starts, on top of the Lake County "
             "permit its unincorporated address actually requires rather than a Town Hall one. We haven't found a published Bella Collina design document "
             "that names turf, sod or ground cover specifically, so we treat a submittal there as a normal review rather than promise a rule that isn't "
             "written down anywhere we could verify. The "
             + svc("residential", "residential installation guide")
             + " covers the base and product side of a job like this in more depth than fits on one town page.</p>"),
        ],
        "scenario": ("Say you have an 850 sq ft lot with a slope",
                     "<p>Say you have an 850 sq ft backyard on a ridge-top Montverde street, with about four feet of fall from the back fence down to the "
                     "patio. At the typical rate of $10 to $16 a square foot, that prices between $8,500 and $13,600, with the upper end reflecting the extra "
                     "anchoring and coarser infill a graded slope calls for rather than any change in the base recipe itself. A similarly sized, flat lot near "
                     + city("clermont", "Clermont")
                     + " or Lake Florence Park would land closer to the lower end of that same range. "
                     + post("artificial-turf-on-a-slope", "The full slope-installation guide")
                     + " goes through the anchoring detail further.</p>"),
        "faqs": [
            faq("Does a steep Montverde lot cost more per square foot?",
                "It can push a quote toward the upper end of the published range because of extra anchoring and grading work, but the per-square-foot figures themselves stay the same everywhere in Central Florida."),
            faq("Do I need Town Hall's approval for a straightforward lawn conversion?",
                "Confirm with Montverde's Permitting Clerk before starting, particularly if the job involves any regrading, since that crosses into work the town reviews even on a routine residential lot."),
        ],
        "sources": SRC,
    },
    "pet": {
        "title": "Pet Turf & Dog Runs in Montverde, FL",
        "meta": "Pet turf for Montverde, FL dog runs on sloped ridge lots: infill choice, anchoring and drainage, with 2026 pricing and sources.",
        "h1": "Dog runs built for Montverde's sloped lots",
        "lede": capsule(f"Pet turf in Montverde runs {price('pet')} a square foot installed, typically {price('pet', True)}, as of September 2026. A dog run "
                        "on a ridge-top lot has the opposite drainage problem most Florida yards have: the ground here lets go of water so fast that keeping "
                        "infill in place, not moving it out, is the real design question."),
        "sections": [
            ("Excessively drained sand means the run never puddles",
             "<p>Astatula and Candler sand pass water fast enough that a dog run built on either one is unlikely to hold standing urine or rainwater the way "
             "a run on Osceola County's flatwoods sand might. That's good news for odor control, but it means zeolite or a coated infill still earns its keep "
             "for ammonia release rather than drainage, since the sand underneath was never the bottleneck to begin with.</p>"),
            ("A sloped run needs a harder edge than a flat one",
             "<p>A dog run angled down a Montverde ridge lot loses infill to gravity faster than one on level ground, especially once a dog's regular running "
             "path packs the surface and gives loose material an easier route downhill. We anchor the downhill perimeter more heavily on these runs and pick "
             "a coarser grain of infill, since Florida's rule requires infill to stay on the property and a fine sand migrates first on a real grade.</p>"),
            ("Staying clear of Lake Apopka's edge on a shoreline lot",
             "<p>A handful of Montverde lots run down to Lake Apopka itself, and a dog run planned near that edge still needs the state's 10-ft waterbody "
             "setback measured in before layout, seawall lots excepted. Combined with a slope, that setback can eat more of the usable yard than a homeowner "
             "expects, which is worth confirming before ordering material rather than after.</p>"),
        ],
        "scenario": ("Say you have a 300 sq ft run on a graded slope",
                     "<p>Say you have a 300 sq ft dog run planned down a side yard that drops nearly three feet from top to bottom, typical of a ridge lot "
                     "away from the two lakes. At the typical pet-turf rate of $12 to $16 a square foot, that runs about $3,600 to $4,800, with the coarser "
                     "infill grain and reinforced downhill edge included in that figure rather than billed as an add-on. A flat run of the same size near "
                     + city("oakland", "Oakland")
                     + " or "
                     + city("winter-garden", "Winter Garden")
                     + " would use the same range without the extra anchoring step.</p>"),
        "faqs": [
            faq("Does a sloped yard change which infill works best for dogs?",
                "It changes the grain size more than the material. Zeolite and coated sand both still work for odor control; we lean toward a coarser grade of whichever one you choose so it resists sliding downhill."),
            faq("Can a dog run in Montverde go right up to Lake Apopka's shoreline?",
                "Not without a seawall or bulkhead already in place. Otherwise the state's 10-ft setback from the water's edge applies the same as it would on any other Central Florida lake lot."),
        ],
        "sources": SRC,
    },
    "putting": {
        "title": "Backyard Putting Greens in Montverde, FL",
        "meta": "Backyard putting greens in Montverde, FL near Bella Collina's golf course: ridge-sand base, contouring and 2026 pricing.",
        "h1": "A home practice green next door to Bella Collina's course",
        "lede": capsule(f"Putting greens in Montverde run {price('putting')} a square foot installed, typically {price('putting', True)}, as of September "
                        "2026. Living a short drive from Bella Collina's Nick Faldo-designed golf course means more residents here ask about a home practice "
                        "green than in a town without a golf address nearby."),
        "sections": [
            ("Astatula sand is close to an ideal green subgrade already",
             "<p>A backyard putting green in "
             + city("montverde", "Montverde")
             + " needs a subgrade that won't shift or hold water under a compacted foam base, and this town's excessively drained "
             "Astatula sand starts closer to that requirement than the flatwoods sand under most of Osceola County. We still shape and compact the contours "
             "in lifts rather than trusting the native sand alone, since a green's subtle breaks have to hold their shape for years, but the starting material "
             "does less fighting against the design here than it does elsewhere.</p>"),
            ("A golf-adjacent lot often has room Bella Collina residents actually use",
             "<p>Homes near or inside Bella Collina tend to sit on larger lots than Montverde's older in-town parcels, which leaves room for a multi-cup green "
             "with a real chipping approach rather than a single flat target squeezed against a fence. The community's own architectural review applies to a "
             "green the same as any other exterior addition, and submitting a footprint drawing and product spec ahead of the meeting tends to move faster than "
             "explaining the project after the fact.</p>"),
            ("Grading a green on a slope takes more planning, not more base",
             "<p>A green built on a ridge lot with any natural fall has to be leveled independently of the yard's overall grade, which sometimes means building "
             "up on the downhill side rather than cutting into the uphill side to keep the putting surface itself flat and true. That's a layout decision made "
             "before any base goes down, not a fix applied afterward. The same ridge terrain reaches into "
             + city("minneola", "Minneola")
             + " and "
             + city("groveland", "Groveland")
             + " just down the road, so a homeowner comparing quotes across those towns should expect the same contouring approach.</p>"),
        ],
        "scenario": ("Say you have a 450 sq ft two-cup green",
                     "<p>Say you have a 450 sq ft area at a golf-community lot near Bella Collina set aside for a two-cup green with a short fringe border, "
                     "on a lot with enough width that the green doesn't compete with the pool or the side setback. At the typical putting-green rate of $18 to "
                     "$25 a square foot, that runs about $8,100 to $11,250, with the leveling work on a naturally sloped pad included rather than priced "
                     "separately. "
                     + post("artificial-turf-glossary", "The turf glossary")
                     + " is a useful reference if terms like stimp or fringe come up during a design conversation, and the "
                     + svc("putting", "putting green guide")
                     + " covers cup placement and contouring beyond what fits here.</p>"),
        "faqs": [
            faq("What do the best putting green installers near Montverde get right that a flatland crew might miss?",
                "Ask to see how they've handled a green on a naturally sloped lot specifically, since leveling a putting surface on ridge ground is a different problem than building one on a flat Central Florida yard."),
            faq("Does living near Bella Collina's course affect the price of a home green?",
                "No. Proximity to a golf course doesn't change the published per-square-foot range; lot size, contouring and cup count are what move the number."),
        ],
        "sources": SRC,
    },
    "playground": {
        "title": "Playground Turf Installation in Montverde, FL",
        "meta": "Playground turf for Montverde, FL families near Lake Florence Park and Montverde Academy: shock pads, shade and 2026 pricing.",
        "h1": "Play surfaces for Montverde's smallest yards",
        "lede": capsule(f"Playground turf in Montverde runs {price('playground')} a square foot installed, typically {price('playground', True)}, as of "
                        "September 2026. With Montverde Academy's campus and athletic fields anchoring one edge of a town of under two thousand people, a "
                        "fair number of local families are already used to organized play space and want something similar, scaled down, at home."),
        "sections": [
            ("Sizing the pad to the equipment, not the town",
             "<p>A shock pad under a home swing set or climbing structure in "
             + city("montverde", "Montverde")
             + " is sized to that equipment's fall height using the same standard as "
             "anywhere else in Florida; nothing about the town changes that calculation. What does vary locally is available yard space, since an older cottage "
             "lot near the town center often has less room for a play area than a larger parcel farther from downtown, which sometimes means a compact "
             "climbing structure instead of a full swing set and slide combination.</p>"),
            ("Ridge lots drain fast, but shade still matters",
             "<p>Because Astatula and Candler sand drain almost immediately, a play surface here is rarely fighting standing water the way one on flatwoods "
             "soil might. Heat is the bigger consideration: a play area in full sun on an open ridge lot gets just as hot as one anywhere else in Central "
             "Florida, so we still recommend shade, whether from a planted tree, an existing structure, or a shade sail, over any full-sun play surface.</p>"),
            ("Lake Florence Park sets a nearby comparison point",
             "<p>"
             + ext("https://mymontverde.com/lake-florence-park-montverde-fl/", "Lake Florence Park")
             + ", tucked at the north end of Porter Avenue on the edge of Montverde Academy's campus, is the town's main public green space, and it gives "
             "local families a sense of what a well-kept play surface should feel like underfoot. A home play area won't match a public park's scale, but the "
             "same attention to a cushioned, well-drained surface applies at any size. The "
             + svc("playground", "playground turf guide")
             + " covers pad thickness by fall height in more detail, and "
             + post("is-artificial-turf-safe-for-kids-pfas-lead", "the safety questions parents ask most")
             + " is worth reading alongside it, whether the yard is in Montverde or nearby "
             + city("clermont", "Clermont")
             + ".</p>"),
        ],
        "scenario": ("Say you have a 250 sq ft play corner",
                     "<p>Say you have a 250 sq ft corner of a Montverde backyard set aside for a small swing set, on a lot too tight for anything larger once "
                     "the pool and a side setback are accounted for. At the typical playground rate of $12 to $19 a square foot, that prices between $3,000 "
                     "and $4,750, with shock-pad thickness under the swing set itself driving most of the difference. Adding a shade sail over the equipment "
                     "would price separately once we've seen how much sun the corner actually gets.</p>"),
        "faqs": [
            faq("Is playground turf worth it on such a small lot?",
                "Often, yes, since a small area is exactly where synthetic turf's low upkeep matters most: there's no room for a mower to maneuver comfortably, and a compact patch of real grass tends to wear out fastest under repeated play."),
            faq("Does Montverde Academy's presence affect turf pricing nearby?",
                "No. The school doesn't change the published per-square-foot range for a residential yard; it's just one reason play-focused installs come up more often in a town this size."),
        ],
        "sources": SRC,
    },
    "pool": {
        "title": "Pool & Lanai Turf in Montverde, FL",
        "meta": "Turf around a pool or lanai in Montverde, FL, from Lake Apopka lots to Bella Collina estates. Drainage, edges and 2026 pricing.",
        "h1": "Pool-deck turf for Montverde's lake and ridge lots",
        "lede": capsule(f"Turf beside a pool or inside a lanai in Montverde prices at the residential rate, {price('residential')} a square foot, typically "
                        f"{price('residential', True)}, as of September 2026. A Bella Collina estate pool facing Lake Apopka and a modest in-town lanai near "
                        "Lake Florence Park share the same price range but rarely the same grading problem."),
        "sections": [
            ("A sloped lot moves water toward the pool cage, not away from it",
             "<p>On a ridge-top lot in "
             + city("montverde", "Montverde")
             + ", the natural fall of the land can run straight toward a pool enclosure instead of away from it, which is the "
             "opposite of what a level Central Florida yard usually deals with. Before any turf goes down around the cage, we check where that grade actually "
             "sends water and correct it if needed, since Astatula and Candler sand drain fast once water reaches them, but only after it gets there.</p>"),
            ("Glue-down edges at the deck, regardless of elevation",
             "<p>Wherever turf meets a pool deck's concrete, on a flat in-town lanai or a stepped, multi-level deck at a Bella Collina estate, that seam bonds "
             "with adhesive rather than nails, since there's no soil at that specific edge to anchor into. A drainage underlay beneath the turf keeps splash-"
             "out and hosed-off water moving rather than pooling against the slab.</p>"),
            ("A lakefront pool still respects the state's setback",
             "<p>A pool cage itself isn't subject to the 10-ft waterbody setback, but the open turf beyond the cage on a Lake Apopka-facing lot is, so a "
             "lanai that opens onto a long lawn running toward the water needs that boundary staked before the layout is finalized, not assumed from the "
             "property line alone. "
             + post("can-artificial-turf-melt", "The melting question")
             + " comes up often near a pool cage's glass too, and the "
             + svc("pool", "pool and lanai turf guide")
             + " covers that risk alongside the edge details above. The same drainage-direction check applies on a sloped lot in "
             + city("oakland", "Oakland")
             + " as well.</p>"),
        ],
        "scenario": ("Say you have a 400 sq ft lanai border",
                     "<p>Say you have a 400 sq ft strip of turf planned around a screened pool at a golf-community home, where the builder left bare dirt "
                     "between the cage and the property's side setback. At the typical residential rate of $10 to $16 a square foot, that comes to about "
                     "$4,000 to $6,400, with the glue-down edge and drainage underlay included in that figure. A similar strip on a sloped lot needing the "
                     "grade corrected first would price toward the upper end for the added grading time.</p>"),
        "faqs": [
            faq("Does a lakefront lot at Bella Collina need extra drainage work for pool turf?",
                "Sometimes, if the grade already runs toward the water rather than away from the pool cage. We check that direction before quoting rather than assuming it based on the lot's general slope."),
            faq("Can turf go over an existing paver deck at a Montverde pool?",
                "Yes, with a drainage layer and glued edges instead of a nailed perimeter, the same approach used anywhere pavers already cover the ground."),
        ],
        "sources": SRC,
    },
    "repair": {
        "title": "Artificial Turf Repair in Montverde, FL",
        "meta": "Artificial turf repair in Montverde, FL: slope-related infill loss, edge lifting and drainage fixes. Quoted after a site visit.",
        "h1": "Repairing turf that's slipped or lifted in Montverde",
        "lede": capsule("Turf repair in Montverde is quoted after photos or a short site visit rather than a flat per-square-foot rate, since a repair job "
                        "here ranges from topping off infill that's crept downhill to rebuilding an edge that never anchored properly on a graded lot."),
        "sections": [
            ("Infill migration is the repair we see most on ridge lots",
             "<p>A "
             + city("montverde", "Montverde")
             + " lawn built on a slope without a heavy enough downhill anchor tends to show thinning infill at the top of the grade and a buildup at the "
             "bottom within a season or two, especially after a hard summer storm. The fix usually means redistributing what's already there and topping off "
             "with a coarser grain rather than a full tear-out, provided the backing and seams underneath are still sound.</p>"),
            ("A lifted edge near a pool deck or driveway tells its own story",
             "<p>Turf that meets concrete, a driveway apron or a pool deck bonds with adhesive rather than nails, and that bond is usually the first thing to "
             "fail on an older install, especially on a stepped or multi-level deck common at larger Montverde estates. A lifted corner there is a faster and "
             "cheaper fix caught early than after months of foot traffic work it loose further.</p>"),
            ("An older base sometimes can't be patched around",
             "<p>Turf installed before the state's washed-rock standard took hold in 2026 sometimes sits on a base with fines that bind into a hard layer over "
             "time, and on a sloped Montverde lot that crust can direct water sideways instead of letting it pass through, showing up as an odd damp strip "
             "partway down the yard. When that's the underlying issue, we say so plainly rather than patch a symptom that will reappear. The "
             + svc("repair", "turf repair guide")
             + " covers base-related failures beyond what's specific to a ridge lot, and "
             + post("artificial-turf-hurricane-flooding", "what a storm can do to an already marginal base")
             + " is a useful read after a bad season. The same diagnose-first approach applies whether the lawn sits in Montverde, "
             + city("groveland", "Groveland")
             + " or "
             + city("minneola", "Minneola")
             + ".</p>"),
        ],
        "scenario": ("Say you have a 60 sq ft strip low on the slope",
                     "<p>Say you have a 60 sq ft strip at the bottom of a graded Montverde backyard where infill has visibly piled up against the rear fence "
                     "after two rainy seasons, thinning the turf higher up the grade in the process. That's a small fraction of a typical 850 sq ft ridge-lot "
                     "lawn, which would cost roughly $8,500 to $13,600 to replace whole at the town's residential range, so redistributing infill and "
                     "reinforcing the downhill anchor rather than a full replacement is the right scope for a strip this size. We'd confirm the exact fix "
                     "after seeing the slope and how the infill settled.</p>"),
        "faqs": [
            faq("Vetting a turf repair company near Montverde? Ask how they'd anchor a downhill edge before anything else.",
                "Ask directly how they'd re-anchor a downhill edge and whether they'd change the infill grain. An installer without a ready answer likely hasn't dealt with a ridge-lot repair before."),
            faq("Does a slope-related repair need Town Hall's approval?",
                "A straightforward infill top-up and re-anchor typically doesn't, but a repair that involves rebuilding the base or changing the grade is worth confirming with Montverde's Permitting Clerk first."),
        ],
        "sources": SRC,
    },
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
