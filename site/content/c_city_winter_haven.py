# -*- coding: utf-8 -*-
"""Winter Haven, Polk County (tier 2). The city runs its own Building & Permitting Division and
its own water utility, separate from Polk County's; we have not read Winter Haven's own
municipal code line by line, so the permit section says that honestly and points to our Polk
County (unincorporated) permit page for the state-floor baseline instead. New research for this
module, checked September 2026: Winter Haven's Building & Permitting Division and Water
Conservation pages, the Southwest Florida Water Management District's Modified Phase III order,
the Winter Haven Chain of Lakes and its canal system, the Interlaken/Lake Howard historic
district, Cypresswood as a named 55-plus community, Census population, and USDA soil mapping for
the ridge that runs through the city. Facts and county-level sourcing for the state rule, HOA
statute and general Polk soil/water picture are reused from site/content/c_permits.py and
c_counties.py (their facts and URLs, not their sentences)."""
from _helpers import page, capsule, sec, table, faq, a, svc, city, county, post, src, ext, price
from _cityservice import cityservice_pages

SLUG = "winter-haven"

SRC = [
    "dep-rule", "fs125572", "fs7203045", "usda-wss",
    ("City of Winter Haven — Building & Permitting Division", "https://www.mywinterhaven.com/342/Building-Permits-Licenses"),
    ("City of Winter Haven — Water Conservation", "https://mywinterhaven.com/367/Water-Conservation"),
    ("Southwest Florida Water Management District — district water shortage restrictions", "https://www.swfwmd.state.fl.us/business/epermitting/district-water-restrictions"),
    ("Southwest Florida Water Management District — Winter Haven Chain of Lakes", "https://www.swfwmd.state.fl.us/projects/swim/winter-haven-chain-lakes"),
    ("USDA NRCS — official series description, Candler series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/C/CANDLER.html"),
    ("Wikipedia — Lake Howard (Winter Haven, Florida)", "https://en.wikipedia.org/wiki/Lake_Howard_(Winter_Haven,_Florida)"),
    ("Census Reporter — Winter Haven, FL profile", "https://censusreporter.org/profiles/16000US1278275-winter-haven-fl/"),
    ("Top Retirements — Cypresswood, Winter Haven", "https://www.topretirements.com/reviews/Florida/Winter%20Haven/Cypresswood%20/"),
]

BUILDING_DIV = ("City of Winter Haven — Building & Permitting Division", "https://www.mywinterhaven.com/342/Building-Permits-Licenses")
WATER_PAGE = ("City of Winter Haven — Water Conservation", "https://mywinterhaven.com/367/Water-Conservation")
CHAIN = ("Southwest Florida Water Management District — Winter Haven Chain of Lakes", "https://www.swfwmd.state.fl.us/projects/swim/winter-haven-chain-lakes")
CANDLER = ("USDA NRCS — official series description, Candler series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/C/CANDLER.html")
LAKE_HOWARD = ("Wikipedia — Lake Howard (Winter Haven, Florida)", "https://en.wikipedia.org/wiki/Lake_Howard_(Winter_Haven,_Florida)")
CENSUS = ("Census Reporter — Winter Haven, FL profile", "https://censusreporter.org/profiles/16000US1278275-winter-haven-fl/")
CYPRESSWOOD = ("Top Retirements — Cypresswood, Winter Haven", "https://www.topretirements.com/reviews/Florida/Winter%20Haven/Cypresswood%20/")
SWFWMD = ("Southwest Florida Water Management District — district water shortage restrictions", "https://www.swfwmd.state.fl.us/business/epermitting/district-water-restrictions")


# ============================================================== hub
HUB = page(
    "/areas/winter-haven/", "city",
    "Artificial Turf in Winter Haven, FL (2026 Guide)",
    "Synthetic turf installs, permits, SWFWMD watering rules and Chain of Lakes setback facts for Winter Haven, FL, about 27 miles from Kissimmee. Checked September 2026.",
    "Artificial turf across Winter Haven",
    capsule(f"Kissimmee Artificial Turf serves Winter Haven, roughly 27 miles east of our home base, where turf installs for exactly what it costs everywhere else in our territory: {price('residential')} a square foot in 2026. Fifty lakes sit inside or against the city limits here, and Census figures put the population near 49,200 in 2020, a count that had climbed past 55,000 within the following few years."),
    "".join([
        sec("A city organized around water more than any other town we serve",
            f"<p>Winter Haven counts 50 lakes within or bordering its city limits, most of them tied together by a canal system that dates to 1915, split into a North Chain and a larger South Chain ({ext(CHAIN[1], 'SWFWMD’s Winter Haven Chain of Lakes overview')}). That geography shapes more residential lots here than in almost any other Polk County town: a meaningful share of Winter Haven addresses sit directly on a lake, a canal, or a pond feeding one, which puts the state's waterbody setback into the conversation on a routine basis rather than as an edge case. The 2020 census put the population at 49,219, and the city had grown past 55,000 by the mid-2020s ({ext(CENSUS[1], 'Census Reporter’s Winter Haven profile')}).</p>"),
        sec("The office that actually reviews a Winter Haven turf job",
            f"<p>Winter Haven runs its own Building & Permitting Division, at 490 Third Street NW, reachable at 863-291-5695, with applications filed through the city's Accela citizen portal ({ext(BUILDING_DIV[1], BUILDING_DIV[0])}). That's separate from Polk County's Building Division, which only has authority outside the city limits.</p>"
                + f"<p>Winter Haven's own code may or may not say something about synthetic turf; we genuinely can't tell you either way, since the page-by-page search behind this site covered the county's unincorporated Land Development Code and stopped there, not the city's separate set of ordinances. {a('/laws/permits/polk-county/', 'Our Polk County permit page')} covers the county's own unincorporated code instead, which is useful as a baseline even inside city limits: {a('/laws/florida-hb-683/', 'HB 683 and Rule 62-308.100')} set the same statewide floor for Winter Haven that they set for the county around it. A community's own design review, governed separately by {a('/laws/hoa-rules/', 'the state statute limiting what an association can restrict')}, is a different step entirely from either building permit.</p>"),
        sec("Winter Haven's own water, under the same shortage order as its neighbors",
            f"<p>Winter Haven bills and schedules its own water rather than buying through Polk County Utilities, and that utility sits under the Southwest Florida Water Management District along with the rest of the western half of the county ({ext(WATER_PAGE[1], 'the city’s water conservation page')}). The district's Modified Phase III order, running since April 2026, gives every address exactly one sprinkler day out of seven, with the specific day tied to the last digit on the mailbox and the actual watering squeezed into either a predawn or a late-evening stretch of a few hours ({ext(SWFWMD[1], 'SWFWMD’s district restrictions page')}). A capped synthetic lawn skips that schedule entirely, since the state's turf rule already bars watering synthetic grass from an in-ground system no matter what the shortage order allows for the lawn next to it.</p>"),
        table("Winter Haven lots and how the turf plan changes",
              ["Lake or neighborhood type", "What the lot usually looks like", "How we plan around it"],
              [["Seawalled lots on the North or South Chain", "A bulkhead already separating yard from open water", "Turf can run to the seawall itself, the one exception to the ten-foot line"],
               ["Un-walled pond and canal banks off the Chain", "A soft, sloped bank with no hard edge", "The full ten-foot setback staked before material is ordered"],
               ["Interlaken and Lake Howard's 1920s bungalows", "Narrow historic lots under mature oak canopy", "A drip-line check before any excavation near the trunk"],
               ["Newer subdivisions on the county's ridge side", "Candler sand instead of the flatwoods soil closer to Lake Hartridge", "A base built for loose, fast-draining sand rather than a high water table"],
               ["55-plus communities such as Cypresswood", "Smaller lots, golf-course frontage, an active design review", "A design-review submittal filed ahead of a compact, low-maintenance layout"]],
              "Checked against the city's own building and water pages, SWFWMD's Chain of Lakes materials and USDA soil mapping, September 2026."),
        sec("Fifty lakes and the ten-foot line, with its one exception",
            f"<p>Most of Winter Haven's lakefront and canal-front lots already carry a seawall or bulkhead, a common fix on a chain this developed and this old, and that hardware matters directly to a turf plan: Florida's rule keeps synthetic grass at least 10 feet from a natural or man-made waterbody, but a physical barrier such as a seawall removes that requirement entirely. A soft, un-walled bank on one of the smaller connecting canals doesn't get the same exception, so the first question on any Winter Haven waterfront estimate is simply which of the two a specific lot actually has, not which lake it's on.</p>"),
        sec("Oak canopy on the old lake streets, open sand on the new ridge lots",
            f"<p>Winter Haven's oldest neighborhoods, Interlaken and the streets ringing Lake Howard among them, were platted in the 1920s and still carry the oak canopy that's grown in over a century since, with more than fifty of the district's homes listed on the National Register ({ext(LAKE_HOWARD[1], 'Lake Howard’s historic-district background')}). A backyard on one of those streets plans around the state's drip-line rule almost by default. Head toward the county's ridge side instead, where newer subdivisions sit on Candler sand rather than the flatwoods soil closer to the Chain, and the challenge flips: less canopy to route around, but loose, fast-draining sand that needs its own base approach ({ext(CANDLER[1], 'USDA’s official series description')}).</p>"),
        "<!--AUTO:city-services-->",
    ]),
    faqs=[
        faq("Does a seawall really remove the ten-foot setback entirely in Winter Haven?",
            "Yes, under the state's May 2026 turf standard: the setback applies where no local buffer or physical barrier already separates the yard from the water, and a seawall or bulkhead counts as that barrier. Turf can run to the wall itself once that's confirmed, though the wall's own condition is a separate question worth checking before building against it."),
        faq("What should the best artificial turf contractor near you already know about a Winter Haven lake lot?",
            "Whether that specific address carries a seawall or not, since that single detail decides how close to the water turf can legally go. A contractor who asks about the seawall before ever quoting a lakefront job has clearly worked in Winter Haven before, rather than treating every yard the same."),
        faq("Does living in a historic district like Interlaken change what turf permit applies?",
            "We haven't found a Winter Haven turf rule specific to any historic district. What does apply on those older, oak-canopied lots is the state's drip-line rule, the same one that applies anywhere else in the city, just triggered more often because the canopy there is older and wider."),
        faq("Why do two Winter Haven addresses on the same chain sometimes get different price quotes?",
            "Because the seawall question, not the lake itself, decides how much of a waterfront yard the ten-foot setback removes from the usable turf area. A seawalled lot can turf closer to the water than an un-walled one on the exact same chain, which changes total square footage more than it changes the per-foot price."),
        faq("Are Winter Haven's 55-plus communities held to a different turf standard?",
            "No. Florida's turf rule and its HOA-visibility statute apply the same way regardless of a community's age restriction. What usually differs in a community like Cypresswood is the yard itself: smaller, golf-course-facing, and run through an active design-review process before work starts."),
    ],
    sources=SRC, city=SLUG, crumbs=[("Service areas", "/areas/")], crumb="Winter Haven",
    related=[("/areas/polk-county/", "Artificial turf in Polk County"), ("/laws/permits/polk-county/", "Polk County permit rules for turf"),
             ("/areas/auburndale/", "Turf in Auburndale"), ("/areas/haines-city/", "Turf in Haines City"),
             ("/artificial-turf-cost/", "Full turf cost guide")],
)


# ============================================================== LOCAL
LOCAL = {
    "residential": {
        "title": "Artificial Grass Installation in Winter Haven, FL",
        "meta": "Artificial grass installation in Winter Haven, FL: the city's own permitting office, Chain of Lakes setback rules and 2026 market pricing per sq ft.",
        "h1": "A lawn conversion built around Winter Haven's fifty lakes",
        "lede": capsule(f"A Winter Haven lawn conversion carries the same {price('residential')} a square foot price tag we quote anywhere in the territory. What sets a Winter Haven job apart isn't the number on the invoice; it's how often a residential lot here actually touches one of the city's 50 lakes or their connecting canals, far more common than in a landlocked Polk County subdivision."),
        "sections": [
            ("Filing through Winter Haven's own Building & Permitting Division",
             f"<p>A residential lawn conversion inside Winter Haven answers to the city's own Building & Permitting Division at 490 Third Street NW, reachable at 863-291-5695, not Polk County's Building Division, which has no authority once an address falls inside the city limits. A direct call beats a guess here: our research for this site covered the county's unincorporated code, not the city's own ordinance book, so a homeowner planning a full conversion is better off asking the division outright than reading anything into its published silence. {a('/laws/permits/polk-county/', 'Our Polk County permit page')} is the closest published reference point we have while that city-specific answer remains unconfirmed.</p>"),
            ("Why so many residential quotes here start with a lake question",
             "<p>A large share of Winter Haven's residential lots sit on the Chain of Lakes or one of the canals connecting it, which means the first question on many estimates isn't square footage, it's whether the property has a seawall. A seawalled lot lets turf run to the water's edge; a soft, un-walled bank keeps the state's ten-foot setback in force, which can shrink the actually turfable area on two otherwise similar lakefront lots by a meaningful margin. That single detail changes total material more than any other variable on a typical Winter Haven residential job.</p>"),
            ("A lawn's age tells you more here than its ZIP code does",
             f"<p>Winter Haven's population moved from 49,219 at the 2020 census past 55,000 by the mid-2020s, and that growth splits fairly cleanly between two kinds of lots: a 1920s bungalow near Lake Howard on undisturbed sand under a full oak canopy, and a newer home on the county's ridge side built on looser Candler sand with little shade at all. Both convert to turf, but the older lot plans first around the state's drip-line rule while the newer one plans first around a base that has to hold its shape on sand that wants to shift.</p>"),
        ],
        "scenario": ("Pricing a seawalled backyard against an un-walled one",
                     f"<p>Say you have two 950 sq ft backyards on the same canal, one behind a home with an existing seawall and one without. At the full {price('residential')} range, turfing the seawalled yard's entire 950 sq ft prices between $7,600 and $17,100, typically {price('residential', True)} per foot or $9,500 to $15,200. The un-walled neighbor loses roughly the strip within ten feet of the bank to the state setback, which can trim actual turfable area by 150 sq ft or more on a narrow canal lot, bringing that job down closer to 800 sq ft of material even though the two lots measure the same on a survey. The per-foot price doesn't change between them; the billable square footage does.</p>"),
        "faqs": [
            faq("Does Winter Haven require a survey to confirm a lakefront setback before permitting turf?",
                "Nothing published says so specifically for turf. A recent survey or a plat showing the ordinary or mean high water line is worth having on hand regardless, since it settles the ten-foot question before material gets ordered rather than after."),
            faq("Is a Winter Haven lawn on Candler ridge sand harder to convert than one near the Chain?",
                "Different, not harder. Ridge sand drains fast enough that the base fights loose material rather than standing water, while a lawn closer to the Chain sits on flatter, slower-draining ground where the base's job is closer to what a Kissimmee yard needs."),
        ],
        "sources": SRC,
    },
    "pet": {
        "title": "Pet Turf & Dog Runs in Winter Haven, FL",
        "meta": "Pet turf and dog run installation in Winter Haven, FL, for canal-lot yards and older lake neighborhoods. Odor-control infill and 2026 pricing per sq ft.",
        "h1": "A dog run that respects Winter Haven's canal lines",
        "lede": capsule(f"A Winter Haven dog run prices out at {price('pet')} a square foot, with most jobs settling into {price('pet', True)} once the infill is chosen. A fenced run on a canal lot has to respect the same waterbody setback a full lawn does, which matters more here than in a town without two dozen connected lakes running through it."),
        "sections": [
            ("A dog run on a canal doesn't get to ignore the ten-foot line",
             "<p>A fenced pet area is still turf under the state's rule, and a dog run planned for the strip of yard between a house and a canal bank has to respect the same ten-foot setback a full lawn would, unless that bank already carries a seawall. Homeowners sometimes assume a small, fenced run is exempt because it reads as a specialty project rather than a lawn conversion, but the rule doesn't distinguish by purpose, only by distance from the water and whether a physical barrier already stands between the two.</p>"),
            ("Rinsing instead of watering on a one-day-a-week schedule",
             "<p>The district's shortage order has boxed Winter Haven residents into a single sprinkler day since April 2026, keyed off the last digit of the street number. A pet run stands entirely outside that box: a hose, not a zone valve, is what keeps a synthetic run clean, so a dog overheating on a July afternoon gets rinsed off regardless of whether that particular Tuesday happens to be the yard's assigned watering day.</p>"),
            ("Older lake-street yards versus newer ridge-side yards for a run",
             f"<p>A dog run behind one of Winter Haven's 1920s lake-street homes usually goes in on undisturbed native sand that's held its shape for a century, with mature oak roots nearby to route around; a run on the newer ridge side deals with looser, faster-draining Candler sand that compacts less predictably under a plate tamper ({ext(CANDLER[1], 'USDA’s Candler series description')}). Neither version gets the fabric layer a standard lawn build sometimes adds, because trapping waste at the surface is exactly what a run's fast-draining design is meant to avoid.</p>"),
        ],
        "scenario": ("Sizing a run on a canal lot with no seawall",
                     f"<p>Say you have a 220 sq ft fenced run planned for the side yard of a canal-front home with no seawall in place. At the full {price('pet')} range, that run prices between $2,200 and $3,960 if the full 220 sq ft can be used, with a job this size more often coming in near {price('pet', True)}, or $2,640 to $3,520. If part of that side yard falls within the ten-foot setback from the canal bank, the usable footprint shrinks and the run gets redrawn around the line rather than the property's actual fence posts, which is worth settling on the initial site visit rather than after ordering material.</p>"),
        "faqs": [
            faq("Does a covered or shaded dog run change the ten-foot canal setback in Winter Haven?",
                "No. The setback measures distance from the water's edge, not whether the run has a roof or shade cloth over it. A covered run still has to sit outside the setback the same way an open one does, unless a seawall already applies."),
            faq("What breed or size restrictions should I check before building a run in a Winter Haven HOA?",
                "That depends entirely on the specific association, and we haven't found a published document covering every Winter Haven community's pet policy. Checking directly with the HOA before finalizing a run's size and fencing avoids a design-review surprise later."),
        ],
        "sources": SRC,
    },
    "putting": {
        "title": "Backyard Putting Greens in Winter Haven, FL",
        "meta": "Backyard putting green installation in Winter Haven, FL, including 55-plus golf communities like Cypresswood. Contouring notes and 2026 pricing per sq ft.",
        "h1": "A putting green sized for Winter Haven's 55-plus lots",
        "lede": capsule(f"Backyard putting greens in Winter Haven run {price('putting')} per square foot as of September 2026, typically {price('putting', True)}. A green built for a smaller lot in a 55-plus community like Cypresswood answers to a different set of constraints than one built for a full-size lakefront yard on the Chain."),
        "sections": [
            ("Fitting a green onto a smaller 55-plus lot",
             f"<p>Cypresswood and Winter Haven's other 55-plus communities tend to sit on smaller, more tightly platted lots than the city's older lake neighborhoods, which changes how a green gets designed more than it changes the build itself: a compact two- or three-cup layout with a shorter fringe collar fits where a full contoured green with multiple tiers simply wouldn't. These communities generally run an active design review for anything visible from a shared street or the community's own course, so a green submittal usually goes in alongside the same paperwork a patio or a fence extension would need ({ext(CYPRESSWOOD[1], 'a description of Cypresswood’s layout and amenities')}).</p>"),
            ("Building contours where the Chain's flatter soil sits underneath",
             "<p>A green planned for a lot closer to the Chain of Lakes, rather than the county's ridge side, usually sits over flatter, slower-draining ground than a ridge lot would, which actually simplifies part of the build: the compacted aggregate base under a green's contours doesn't fight the same loose, shifting sand a Lake Wales Ridge site does. What it does have to answer for instead is proximity to water on a narrow lake lot, where the green's footprint sometimes has to work around the same ten-foot setback a full lawn would face on the same property.</p>"),
            ("Why an older Interlaken-area yard rarely gets a full green",
             "<p>A backyard in Interlaken or along Lake Howard, shaded by decades of oak canopy and often narrower than a newer subdivision lot, usually has less open, sunlit ground than a putting green's turf actually needs to hold color and stand up to regular play. A single practice pad tucked into whatever sun the yard does get is a more realistic fit on one of these historic lots than a full contoured green with a fringe collar, which needs more unbroken open space than most century-old lake streets were platted to provide.</p>"),
        ],
        "scenario": ("Sizing a compact green for a 55-plus lot",
                     f"<p>Say you have a 260 sq ft two-cup green planned for a Cypresswood-style backyard, sized to fit a lot noticeably smaller than a full-size lakefront property elsewhere in the city. At the full {price('putting')} range, that green prices between $3,640 and $7,800; most compact builds its size land in the {price('putting', True)} typical band, $4,680 to $6,500, since a shorter fringe collar and a simpler two-cup layout keep the contouring labor lower than a larger, multi-tier green would need. The community's own design-review process typically adds a few weeks to scheduling, which is worth building into a timeline before ordering material.</p>"),
        "faqs": [
            faq("How do you find the best putting green company near you in a Winter Haven 55-plus community?",
                "Ask whether they've built for a smaller, tightly platted lot before, not just whether they've built a green at all. A contractor who brings up the community's design-review process without being asked has clearly worked in a 55-plus neighborhood already."),
            faq("Can a putting green go inside the ten-foot setback on a Winter Haven lake lot?",
                "No, unless a seawall or bulkhead already separates the yard from the water. A green's footprint on a narrow lake lot sometimes has to shrink or shift closer to the house to stay outside that line, which is worth confirming before finalizing the layout."),
        ],
        "sources": SRC,
    },
    "playground": {
        "title": "Playground Turf in Winter Haven, FL",
        "meta": "Playground turf installation in Winter Haven, FL, for shaded lake-street yards and newer ridge-side subdivisions. Shock pad notes and 2026 pricing.",
        "h1": "Play-area turf for both sides of Winter Haven",
        "lede": capsule(f"A backyard play surface in Winter Haven prices between {price('playground')} a square foot, with the typical small job settling around {price('playground', True)}. A shaded backyard near Lake Howard's oak canopy and an open lot on the county's ridge side call for the same shock-pad math but a different drip-line conversation first."),
        "sections": [
            ("Planning a play area under a century-old canopy",
             f"<p>Interlaken and the streets around Lake Howard carry oak canopy that predates most of Winter Haven's current housing stock by decades, with more than fifty homes in the district on the National Register ({ext(LAKE_HOWARD[1], 'Lake Howard’s historic-district background')}). A backyard play area on one of these lots almost always has to work around a drip line somewhere in the yard, since branches from a mature specimen tend to reach further than a homeowner expects until they're actually measured. Mapping that line before sketching where a swing set or climbing structure will sit avoids redrawing the layout mid-project.</p>"),
            ("Open, sun-exposed lots on the ridge side need a different plan",
             "<p>A newer subdivision on Winter Haven's ridge side typically has far less canopy than an old lake street, which removes the drip-line question but adds a heat one instead: a play surface with no shade at all reaches the higher end of what synthetic turf gets on a Florida afternoon, and a rinse habit or a shaded structure over part of the equipment matters more here than it would under an old oak's canopy a mile away.</p>"),
            ("Sizing a shock pad the same way regardless of neighborhood",
             "<p>Wherever a Winter Haven play area sits, the shock pad underneath answers to the same rule: thickness scales to the specific equipment's fall height, not to the neighborhood or the size of the yard around it. A taller climbing structure needs a thicker pad than a low toddler swing does, which is a spec that doesn't change whether the yard sits under a century of oak growth or on a ridge lot with no mature trees at all.</p>"),
        ],
        "scenario": ("Sizing a shaded play area near Lake Howard",
                     f"<p>Say you have a 280 sq ft play area planned for a backyard near Lake Howard, most of it under an oak canopy but kept clear of the tree's actual drip line once branches are measured out. At the full {price('playground')} range, that area prices between $2,800 and $7,000, though a job this modest usually settles closer to {price('playground', True)}, meaning $3,360 to $5,320 once the shock pad is sized to whatever swing set or slide is going in. Staying outside the drip line on a historic lot this size sometimes trims a few feet off one edge of the layout, which is worth settling with a certified arborist's input before ordering material rather than after.</p>"),
        "faqs": [
            faq("Does a Winter Haven historic district add its own review for a backyard play structure?",
                "We haven't found a turf-specific rule tied to Interlaken or any other Winter Haven historic district. What does apply on those lots is the state's drip-line rule, triggered more often there because the canopy is older and wider than on a newer subdivision lot."),
            faq("Why would a ridge-side Winter Haven play area need more rinsing than one near the Chain?",
                "Because a ridge-side lot typically carries less shade, and an unshaded synthetic surface reaches a higher afternoon temperature than one under an old oak's canopy. A quick hose rinse before play time matters more on the open, sunnier lot."),
        ],
        "sources": SRC,
    },
    "pool": {
        "title": "Pool & Lanai Turf in Winter Haven, FL",
        "meta": "Turf around a Winter Haven pool cage or lanai, including seawalled lakefront lots and the ten-foot setback exception. 2026 installed pricing per sq ft.",
        "h1": "Turf around a Winter Haven pool enclosure",
        "lede": capsule(f"Turf around a Winter Haven pool cage isn't its own price category; it borrows the residential figure, {price('residential')} a square foot, and typically sits in the upper part of that band once deck edges and drainage are counted in. A screen enclosure on a seawalled lake lot can turf right up to the wall; the same enclosure on an un-walled canal bank still answers to the state's ten-foot line."),
        "sections": [
            ("A pool cage that already sits past the setback question",
             "<p>A pool enclosure built on a Winter Haven lot with an existing seawall doesn't have to work around the state's ten-foot waterbody line inside that enclosure, since the wall itself satisfies the exception the rule allows for a physical barrier. That simplifies layout on a chain this developed, since most of the older lakefront lots we see already carry a seawall installed decades ago, well before synthetic turf became part of the conversation.</p>"),
            ("The same enclosure without a seawall plans differently",
             "<p>A newer canal-adjacent lot without an existing seawall keeps the full setback in force even once a screen enclosure goes up around the pool, so the open strip of yard between the cage and the water still has to stay clear of turf within ten feet of the bank. That distinction, seawall or no seawall, matters more to a Winter Haven pool quote than almost any other single detail, since it decides how much of the yard around the enclosure can actually be turfed at all.</p>"),
            ("Feathering a deck edge on ridge-side pool lots",
             f"<p>A pool built on Winter Haven's ridge side, away from the Chain, sits over looser Candler sand that doesn't hold a graded slope as predictably as the flatter ground near the lakes does ({ext(CANDLER[1], 'USDA’s official series description')}). Wherever the lawn meets the deck's poured edge, the crew tapers the base down to match the slab exactly, then switches to glue instead of fasteners for that last few inches, since concrete leaves nothing underneath for a nail to grab.</p>"),
        ],
        "scenario": ("Turfing a lanai strip against a seawall",
                     f"<p>Picture a 240 sq ft band of grass lining a screen enclosure on a lakefront lot with an existing seawall, stretching the full width of the pool deck's outer edge. Multiplying by the residential range, {price('residential')} a square foot, lands the job somewhere between $1,920 and $4,320, and a tight enclosure job like this one tends to run closer to $3,840 than to the low end, since the glue-down deck edge takes labor a wide-open lawn skips entirely. The seawall itself isn't what drives that number up; it's what keeps the full width of the deck turfable instead of losing several feet to the state's setback.</p>"),
        "faqs": [
            faq("Does an older Winter Haven seawall need to be inspected before turf goes in against it?",
                "We'd recommend it as good practice, though it's not a state turf-rule requirement. A deteriorating seawall is a structural and cost question on its own, separate from whether the setback exception applies once the wall is confirmed to be standing and functional."),
            faq("Is pool-area turf priced differently on the Chain than on a ridge-side lot in Winter Haven?",
                "The per-square-foot range is the same everywhere in Winter Haven. What differs is how much of the enclosure's footprint can actually be turfed, since a seawalled Chain lot often has more usable area than an un-walled canal lot of the same size."),
        ],
        "sources": SRC,
    },
    "repair": {
        "title": "Artificial Turf Repair in Winter Haven, FL",
        "meta": "Artificial turf repair in Winter Haven, FL: seawall-edge, canal-bank and historic-lot fixes. Priced after photos or a site visit. Checked September 2026.",
        "h1": "Repairing turf on Winter Haven's lake and canal lots",
        "lede": capsule("Turf repair in Winter Haven is priced after photos or a site visit, since a lifted seawall-side edge, a root-heaved section near an old oak, and a settled patch on ridge-side fill all need different fixes. What we see most in this city traces back to its water, more than its soil or its age."),
        "sections": [
            ("Why a seawall-adjacent edge is often the first to move",
             "<p>Turf running right up to a Winter Haven seawall takes wave action and boat wake against that edge in a way an interior lawn seam never experiences, and a nailed or adhered border along that specific line tends to show wear before the rest of a lakefront lawn does. A repair that keeps reopening at that same seawall edge usually points to the joint itself needing a sturdier anchor method, not a defect spreading through the rest of the installation.</p>"),
            ("Root damage under a century-old Interlaken oak",
             "<p>A live oak that's been growing since the 1920s on a Lake Howard or Interlaken lot has root structure that can heave a narrow ridge in nearby turf years after installation, well after the original drip-line planning was done correctly. That kind of damage looks different from a broad, settled dip: it tracks in a fairly straight line back toward the trunk, and it usually needs an arborist's input on the root itself before deciding whether to reroute the edge or accept that the same spot will need attention again as the tree keeps growing.</p>"),
            ("Fill that settles unevenly on the ridge side",
             "<p>A repair on Winter Haven's newer ridge-side subdivisions more often traces back to grading fill that never compacted quite as evenly as the loose native Candler sand around it, producing a soft spot months or years after installation rather than immediately. That's a different repair than the seawall-edge or root-heave problems we see closer to the Chain, which is part of why a photo or a site visit, not a phone estimate, decides what a specific Winter Haven repair actually needs.</p>"),
        ],
        "scenario": ("Weighing a canal-edge repair against full replacement",
                     f"<p>Say you have a 70 sq ft section along a canal-front seawall where the turf has lifted and pulled away from its anchor after a season of wave action. A full replacement of that same 70 sq ft at the residential range, {price('residential')} per square foot, would run $560 to $1,260 before any premium for matching the surrounding lawn's grain and fade; a targeted edge repair typically prices well under that figure, since it reuses the existing turf field and base and only rebuilds the anchor at the wall itself. The exact number depends on what a site visit shows once the seawall's own condition and the anchor method are checked.</p>"),
        "faqs": [
            faq("Can a lifted seawall-edge repair be diagnosed from photos alone?",
                "Sometimes, if the anchor failure is clearly visible and the seawall itself looks sound. A repair that keeps recurring at the same spot, or where the wall's own condition is in question, usually needs an in-person visit before we can say what the actual fix requires."),
            faq("Does an oak root repair near Lake Howard cost more than a standard patch?",
                "It can, since a root-heaved section sometimes needs an arborist's assessment before the turf work itself starts, which adds a step a simple worn-patch repair doesn't need. We'd rather quote that accurately after a visit than guess at a number over the phone."),
        ],
        "sources": SRC,
    },
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
