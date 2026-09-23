# -*- coding: utf-8 -*-
"""Sanford, FL (tier 3, Seminole County). Permit-office, water, historic-district, soil and Census
facts researched September 2026; see report for sources. Reuses the Seminole County permit/water/soil
facts already established in c_permits.py and c_counties.py (facts and URLs only, fresh sentences)."""
from _data import CITIES
from _helpers import page, capsule, sec, table, faq, a, svc, city, post, ext, price
from _cityservice import cityservice_pages

SLUG = "sanford"
SAN = CITIES[SLUG]

SRC = [
    ("City of Sanford — Building Division", "https://sanfordfl.gov/government/development-services/building-division/"),
    ("City of Sanford — Water Conservation and watering restrictions", "https://sanfordfl.gov/government/public-works-utilities/water_and_sewer/water-conservation/"),
    ("Sanford Residential Historic District — Wikipedia", "https://en.wikipedia.org/wiki/Sanford_Residential_Historic_District"),
    ("Sanford, Florida — Wikipedia", "https://en.wikipedia.org/wiki/Sanford,_Florida"),
    ("USDA NRCS — official series description, EauGallie series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/E/EAUGALLIE.html"),
    ("USDA NRCS — official series description, St. Johns series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/S/ST._JOHNS.html"),
    ("Seminole County Property Appraiser — parcel search", "https://www.scpafl.org/"),
    "dep-rule", "fs125572", "fs7203045", "usda-wss",
]

HUB = page(
    "/areas/sanford/", "city",
    "Artificial Turf Installation in Sanford, FL (2026)",
    "Synthetic grass for Sanford, FL yards, from the Historic District's oak canopy to Lake Monroe's seawalled riverfront. Local rules, checked September 2026.",
    "Artificial turf for Sanford yards, from the Historic District to Lake Monroe",
    capsule(f"Sanford's yards split between Craftsman bungalows on the Historic District's brick streets and new construction toward the Lake Mary line, with synthetic lawns, pet turf and putting greens fitting either kind. Residential turf runs {price('residential')} per square foot as of September 2026. Sanford sits about {SAN['miles']} miles from our Kissimmee base, near the outer edge of where we schedule regular work."),
    "".join([
        sec("A Seminole County stop at the edge of our map",
            f"<p>Sanford sits about {SAN['miles']} miles from our Kissimmee crew's home base, near the far edge of the roughly 40-mile radius we work inside, on the north shore of Lake Monroe where the St. Johns River opens into open water. A Sanford date on our schedule usually rides alongside another stop in Seminole County rather than standing on its own, since the drive alone is close to an hour each way. That scheduling reality does not change the {price('residential')} per square foot range a Sanford lawn costs to install as of September 2026, or how the base underneath it gets built; it changes which day of the week we can offer. Orlando Sanford International Airport sits on the city's east side, and the yards in town range from a downtown platted before 1900 to subdivisions still being framed near the Lake Mary line.</p>"),
        sec("The Historic District, the RiverWalk and what came after",
            f"<p>Downtown Sanford's Residential Historic District joined the National Register of Historic Places in 1989, and its roughly 430 contributing homes, mostly built from the 1880s into the 1920s, stand under a live oak canopy along brick-paved streets laid out when the city was still shipping celery by rail. A yard in that district falls inside more tree drip lines than almost anywhere else we work, which is where {a('/laws/florida-hb-683/', 'the certified-arborist exception in the 2026 state rule')} does the most work before a shovel goes in. Where downtown meets the water, the city's RiverWalk trail runs along a seawalled stretch of Lake Monroe, and that seawall is exactly what lets a lawn sit closer than the standard's usual 10-foot waterbody setback would otherwise allow. Away from the river, Sanford's growth shows up in the gap between a 2020 census count of 61,051 and an estimate closer to 66,900 for 2024, most of it in newer subdivisions toward the Lake Mary line, with 1950s-1970s ranch homes still filling out the east side.</p>"),
        sec("Water, irrigation days and reclaimed water",
            f"<p>The city runs its own water and sewer utility rather than buying through Seminole County: odd addresses water Wednesday and Saturday, even addresses Thursday and Sunday, both during daylight saving time, dropping to a single weekend day once clocks fall back, with no watering between 10 a.m. and 4 p.m. Sanford is also one of the few cities in our service area that sells reclaimed water on its own schedule, three days a week year-round, which matters for whatever bed or side strip stays planted next to a new lawn. None of it reaches the turf itself, since {a('/laws/florida-hb-683/', 'the 2026 state standard')} already bars an in-ground system from watering synthetic turf once the heads under it are capped.</p>"),
        sec("What a Sanford permit covers, and what we have not researched",
            f"<p>Sanford runs its own Building Division, separate from the county office that handles unincorporated land, reachable at (407) 688-5150 or through the city's Citizenserve portal. We have not gone through the city's own code the way {a('/laws/permits/seminole-county/', 'our Seminole County permit page')} does for unincorporated land nearby, so we will not attribute a rule to Sanford's ordinance we have not verified. What carries over regardless is the floor set by Florida Rule 62-308.100. A search on the {ext('https://www.scpafl.org/', 'Seminole County Property Appraiser')} site settles whether an address is actually inside city limits, and where a subdivision has its own association, {a('/laws/hoa-rules/', 'the HOA visibility law')} is what limits an architectural review, not either government permit counter.</p>"),
        sec("Picking who does the work",
            "<p>Ask how a company handles Sanford specifically: whether it knows the Historic District's drip-line issue, whether it treats a RiverWalk-adjacent lot's setback correctly, and whether the quote lists base depth and infill by name rather than the phrase premium turf installed. That test beats searching for the best artificial turf company near you in Sanford and picking whoever ranks first.</p>"
            + table("Sanford yard types and what we do differently",
                    ["Yard type", "What we typically find", "How the build changes"],
                    [["Historic District bungalow lot", "Live oak canopy over a brick street, narrow side yards", "Shallow excavation inside the drip line unless an arborist signs off; base built up, not down"],
                     ["Lake Monroe / RiverWalk waterfront", "A seawalled riverfront lot along the RiverWalk corridor", "The seawall lets turf sit closer than the standard 10-ft waterbody setback allows"],
                     [f"Newer subdivision toward {city('lake-mary', 'Lake Mary')}", "2000s-2020s builder-graded lot, compacted fill", "Washed crushed rock in place of compacted fill so storms drain instead of pooling"],
                     ["1950s-1970s east-side ranch home", "Established St. Augustine, mature landscaping, older irrigation", "Locating and capping legacy sprinkler zones under the new turf footprint"]],
                    f"Base and grading are the constant across every row above, washed crushed rock graded away from the house; what shifts is where the crew slows down for a tree, a seawall or a hidden zone valve. Turf itself still prices at {price('residential')} a square foot installed, unchanged since this page was last checked in September 2026.")),
        "<!--AUTO:city-services-->",
    ]),
    faqs=[
        faq("Does the City of Sanford have a synthetic turf permit rule we can quote?",
            "We have not researched Sanford's own code the way we have for the eight offices on our permit hub, so we will not quote a city-specific rule here. Call the Building Division at (407) 688-5150 before scheduling a crew, and bring up Florida Rule 62-308.100 if synthetic turf comes up."),
        faq("Is Sanford too far from Kissimmee for a quote to make sense?",
            "Not usually, though it sits close to where our range runs out. A straight-line 36 miles puts Sanford at the outer edge of the towns we schedule regularly, and a crew heading that way typically adds a second Seminole County stop to the trip."),
        faq("Will turf under an oak in the Historic District need anything special?",
            "Likely yes. The state rule keeps synthetic turf out of a live oak's drip line unless a certified arborist certifies no harm, and a canopy this old usually reaches further than it looks."),
        faq("Does Sanford's reclaimed water change anything for a synthetic lawn?",
            "No. A synthetic lawn stops needing either the potable or the reclaimed schedule the moment its irrigation heads are capped, which the 2026 state standard requires regardless of which utility served that part of the yard before."),
    ],
    sources=SRC, city=SLUG, crumbs=[("Service areas", "/areas/")], crumb="Sanford",
    related=[("/areas/seminole-county/", "Artificial turf in Seminole County"), ("/laws/permits/seminole-county/", "Seminole County permit rules for turf"),
             ("/areas/lake-mary/", "Artificial turf in Lake Mary"), ("/areas/longwood/", "Artificial turf in Longwood"),
             ("/artificial-turf-cost/", "Full turf cost guide")],
)

LOCAL = {
    "residential": {
        "title": "Artificial Grass for Sanford's Historic District and New Lots",
        "meta": "Synthetic lawns for Sanford yards, from 1900s Historic District bungalows to new construction near Lake Mary, at Central Florida prices, checked September 2026.",
        "h1": "Installing artificial grass on a Sanford lot, old or new",
        "lede": capsule(f"A synthetic lawn on a Sanford lot runs {price('residential')} per square foot installed as of September 2026, whether the address is a Craftsman bungalow inside the Historic District or a two-year-old build off US 17-92. What changes between the two is tree canopy, lot shape and how much of the existing yard is compacted builder fill rather than native ground."),
        "sections": [
            ("Turf inside Sanford's Historic District",
             f"<p>A bungalow lot inside the Residential Historic District rarely measures more than a small in-town parcel, and most of what grass exists sits in the shade of a live oak that has been growing since before the district's 1989 listing. The state rule keeps synthetic turf out of a tree's drip line on that lot or the one next door unless a certified arborist signs off, and {post('artificial-turf-near-live-oaks-and-palms', 'a canopy this mature')} usually reaches further than a homeowner expects, often past the porch steps. Where the yard opens up past the canopy, a narrow side strip toward the brick street is a common candidate for {svc('residential', 'a full turf conversion')}, since St. Augustine rarely holds up in that much shade anyway. Working near a brick street also means protecting the pavers themselves during base work, since a skid steer that would be routine on a wider modern lot is not always practical on a street this old.</p>"),
            ("New construction toward Lake Mary versus the older east side",
             f"<p>Homes going up between Sanford and {city('lake-mary', 'Lake Mary')} sit on lots graded and compacted during construction, and that compacted fill drains slower than the native sand it replaced, so a base built from washed, open-graded crushed rock has to correct for it more than it would on undisturbed ground. On the city's older east side, ranch homes from the 1950s through the 1970s carry decades of established landscaping and, often, an irrigation system with zones nobody has mapped in years. Converting one of those older yards means locating and capping every head that used to reach the new turf footprint, not just the obvious ones near the patio. Either way the {price('residential')} range holds, since it is the access, the fill and the number of heads to cap that move a bid, not which side of town the lot sits on.</p>"),
            ("Permits, the parcel record and what we have not verified",
             f"<p>Sanford runs its own Building Division, separate from the Seminole County office that handles unincorporated land, and we have not reviewed the city's code the way {a('/laws/permits/seminole-county/', 'our county permit page')} does for unincorporated Seminole County. A call to the Building Division before scheduling a crew is the honest answer, not a guess dressed up as one. Before that call, a quick search on the county property appraiser's site settles whether a specific Sanford-area address is actually inside city limits, since the postal address alone does not always match the taxing jurisdiction. An architectural review from a subdivision association, where one exists, is a separate step again, governed by {a('/laws/hoa-rules/', 'the HOA visibility law')} rather than by either building department.</p>"),
        ],
        "scenario": ("Say you have a quarter-acre lot on Sanford's east side",
                     f"<p>Say you have a 1962 ranch home on Sanford's east side with a 1,400 sq ft front and back lawn, four sprinkler heads to cap, and a St. Augustine lawn that has thinned out under a pair of mature oaks near the property line. At {price('residential')} per square foot, a mid-grade install on that footprint runs roughly ${1400 * 10:,}–${1400 * 16:,}, depending on how much of the yard falls inside the oaks' drip lines and needs an arborist's letter before it gets turfed. Skipping the shaded strip and turfing only the sunnier 1,000 sq ft in front brings that down to about ${1000 * 10:,}–${1000 * 16:,}, with the oak-shaded back left as mulch instead of grass that was already struggling before turf ever entered the conversation.</p>"),
        "faqs": [
            faq("Does the Historic District have its own review for exterior changes like turf?",
                "We have not found a published Sanford ordinance that names synthetic turf specifically, historic district or not, so the same state standard applies to a bungalow lot as it does anywhere else in the city. A historic district often adds a design-review step for anything visible from the street, which is a question for the city's planning staff rather than the Building Division's permit counter."),
            faq("How do you handle capping old irrigation on an east-side Sanford lot?",
                "The same way anywhere else: every head that used to reach the new turf footprint gets capped at the valve, not just cut at the surface, since a buried line left live can push water up through a seam later. On an older system, tracing zones that were never labeled takes a few extra minutes before the base goes in."),
            faq("Is a Sanford address always inside the city, or could it be unincorporated Seminole County?",
                "Not always. Some Sanford-area mailing addresses sit in unincorporated county land rather than inside the city limits, and the two answer to different building departments. A parcel search on the county property appraiser's site is the fastest way to check before assuming which office applies."),
        ],
        "sources": SRC,
    },
    "pet": {
        "title": "Pet Turf Installation for Sanford, FL Dog Runs",
        "meta": "Fast-draining pet turf for Sanford yards, from downtown dog runs to new subdivisions, priced for Central Florida, checked September 2026.",
        "h1": "Pet turf for a Sanford backyard, checked against local watering rules",
        "lede": capsule(f"A Sanford dog run gets a faster-draining base and an odor-control infill that a plain lawn skips, priced at {price('pet')} per square foot installed as of September 2026. Sanford also sells its own reclaimed water on top of the usual potable schedule, which matters for whatever planted ground still surrounds the run."),
        "sections": [
            ("Rinsing a dog run against Sanford's watering calendar",
             "<p>Sanford's irrigation ordinance limits potable water to two mornings or evenings a week during daylight saving time, one day once clocks fall back, with a hard stop between 10 a.m. and 4 p.m. every day of the year. None of that reaches a capped pet turf area, since the state standard already keeps an in-ground system off synthetic turf regardless of the calendar, so a quick hose-down after a Sanford dog has been out in July heat is never the scheduling problem that watering the rest of the yard can be. The city's own reclaimed water service, sold on a separate three-day, year-round schedule, is the more useful fact for whatever St. Augustine or bedding plants stay around the edges of the run once the turf itself goes in.</p>"),
            ("Dog runs on Sanford's older, fenced lots",
             f"<p>The city's east side carries block after block of fenced backyards built in the decades before HOAs became standard in Central Florida, which is exactly the kind of lot a dog run fits without an architectural review to clear first. A narrow side yard behind a chain-link fence, common on these older parcels, drains slower than a wide-open modern lot because there is less room to grade a fall toward one low point, so the crew often adds a shallow collector strip along the fence line rather than relying on the general slope alone. Newer fenced yards toward the Lake Mary side of town tend to be wider and already graded correctly by the builder, which is the main reason two dog runs of the same size can price differently even inside the same {price('pet')} range.</p>"),
            ("Scheduling a Sanford pet turf job",
             f"<p>A pet turf call in Sanford almost always lands on the same visit as another Seminole County stop, since the drive from our Kissimmee base runs close to {SAN['miles']} miles each way and rarely justifies a trip for one dog run alone. That mostly affects which day of the week is open, not the work itself: the base still runs deeper under a pet system than a plain lawn, and the infill choice, zeolite or a coated sand rather than plain silica, stays the same whether the address sits ten minutes from our shop or forty. Booking a Sanford date a little further out than a Kissimmee one is normal, not a sign the job gets treated differently.</p>"),
        ],
        "scenario": ("Say a Sanford dog run needs to replace a bare side yard",
                     f"<p>Say you have a 12-by-20-foot side yard, 240 sq ft, worn to bare sand by two dogs on the east side of Sanford, with one sprinkler head to cap near the gate. At {price('pet')} per square foot, that run prices around ${240 * 12:,}–${240 * 16:,}, infill included. Add a second run behind the garage, another 150 sq ft, and the combined job runs about ${390 * 12:,}–${390 * 16:,} total, still priced the same whether the address sits downtown or out past the airport, since the range moves with square footage and how much base work the yard needs, never with the ZIP code.</p>"),
        "faqs": [
            faq("Does Sanford's reclaimed water schedule apply to a pet turf area?",
                "No. Reclaimed water and the city's regular potable-water days both stop applying to synthetic turf once the irrigation heads underneath it are capped, which the 2026 state standard requires regardless of which utility served that part of the yard before."),
            faq("Is there a faster way to control odor between visits in Sanford's heat?",
                f"A hose rinse is the tool that actually works, since it flushes the infill rather than masking a smell sitting on top of it. {post('how-to-get-dog-urine-smell-out-of-artificial-turf', 'This article')} covers the rinse-and-infill routine in more detail than one paragraph can.")             ,
            faq("Why would a Sanford pet turf job get scheduled later than one closer to Kissimmee?",
                "Distance, not priority. Sanford sits near the edge of where we work, so a crew heading that way usually pairs the visit with another Seminole County stop, which can push the date out compared with a yard fifteen minutes from our shop."),
        ],
        "sources": SRC,
    },
    "putting": {
        "title": "Backyard Putting Greens for Sanford, FL and Riverfront Lots",
        "meta": "Contoured backyard putting greens for Sanford lots, from riverfront yards near Lake Monroe to growing subdivisions, priced for Central Florida, September 2026.",
        "h1": "Building a putting green on a Sanford lot, riverfront or not",
        "lede": capsule(f"A backyard putting green in Sanford runs {price('putting')} per square foot as of September 2026, with the contouring and fringe turf that a flat lawn install does not need. Sanford's population has grown past 66,000 in a city of just under 24 square miles, and the newer, larger lots behind that growth are where most putting-green calls come from."),
        "sections": [
            ("Riverfront lots and the 10-foot setback",
             "<p>A handful of Sanford properties back directly onto Lake Monroe or a canal feeding it, some behind a seawall along the RiverWalk corridor and some without one. A putting green near that water answers to the same rule as a plain lawn: nothing synthetic within 10 feet of a lake, pond or canal edge unless a seawall or bulkhead already stands in the way, and a contoured design earns no exception just for being a specialty surface. Staking that line before ordering turf or fringe material matters more on a green than on a rectangle of lawn, since pulling a finished contour back after the fact costs more than a straight edge would.</p>"),
            ("Sandy river-terrace ground near Lake Monroe versus flatwoods further inland",
             "<p>Soil maps for the area shift as the ground drops toward Lake Monroe: away from the river, Sanford sits mostly on the same Myakka and Basinger fine sands found across the rest of Seminole County, while low ground closer to the water trades over to poorly drained series such as EauGallie and St. Johns fine sand. A putting green cares about this more than a lawn does, since an uneven cup-to-cup roll shows up the moment the compacted rock beneath it settles unevenly. On the wetter, river-terrace ground, that argues for building the base toward the fuller end of the state rule's two-to-four-inch range rather than the shallow end, so the green has more separation from soil that can stay saturated for weeks after a summer storm.</p>"),
            ("Bigger lots, and three questions worth asking before you hire",
             "<p>Sanford's growth toward roughly 66,900 residents has come mostly in subdivisions built since 2000, and those newer lots tend to run wider than anything platted downtown a century ago, which is where a full green with a chipping pad and multiple cups actually fits. Finding the best putting green builder near you in Sanford comes down to fewer questions than the search suggests: ask whether the quote separates fringe turf from the green surface itself, whether cups are set into a real subgrade rather than just cut into the base rock, and whether the crew has already asked about a lot's distance from Lake Monroe before pricing the job.</p>"),
        ],
        "scenario": ("Say a newer Sanford lot has room for a full green",
                     f"<p>Say you have a newer home near the edge of town with a 500 sq ft backyard set aside for a green, contoured with two cups and a small chipping pad, fringe turf running the perimeter. At {price('putting')} per square foot, that project runs roughly ${500 * 18:,}–${500 * 25:,} depending on how much contouring and how many cups the design calls for. A simpler 300 sq ft green with one cup and no chipping pad, better suited to an older, narrower lot closer to downtown, comes in around ${300 * 18:,}–${300 * 25:,}, proof that lot age and shape move this number more than which part of Sanford the address sits in.</p>"),
        "faqs": [
            faq("Do all Sanford lots near the water need the full 10-foot setback?",
                "Not if a seawall or bulkhead already stands between the yard and the water, which several RiverWalk-adjacent lots have. Where there is no seawall, the 10-foot figure is the number to design around, and it applies to a putting green exactly the way it applies to a plain lawn."),
            faq("Does a putting green need a deeper base than a lawn on the same Sanford lot?",
                "Often yes, especially on ground closer to Lake Monroe where the soil drains slower. Building toward the top of the state rule's two-to-four-inch range keeps a contoured surface from settling unevenly the way a shallow base can once the ground beneath it stays wet for a while."),
            faq("Is Sanford's population growth actually changing what kind of greens get requested?",
                "Some. Newer subdivisions built on wider lots since 2000 have room for a chipping pad and multiple cups that an older, narrower in-town lot usually cannot fit, so the design conversation starts differently depending on when the neighborhood was platted."),
        ],
        "sources": SRC,
    },
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
