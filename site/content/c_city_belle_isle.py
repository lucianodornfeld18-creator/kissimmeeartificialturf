# -*- coding: utf-8 -*-
"""Belle Isle, FL (tier 2, incorporated city in Orange County) — hub + six city x service pages.
Orange County permit-hub facts (property appraiser, permit-page routing) are reused from
site/content/c_permits.py and c_counties.py (same facts, fresh sentences). Belle Isle's own
building-official arrangement, watering ordinance, Lake Conway drainage basin, soil series and
Cornerstone Charter Academy were researched fresh for this module in September 2026."""
from _helpers import page, capsule, sec, table, faq, a, svc, city, post, src, ext, price
from _cityservice import cityservice_pages

SLUG = "belle-isle"

ORANGE_PERMIT_ROUTE = ("/laws/permits/orange-county/", "Orange County's permit rules for turf")
HOA_ROUTE = ("/laws/hoa-rules/", "What a Florida HOA can and can't restrict")
HB683_ROUTE = ("/laws/florida-hb-683/", "HB 683 and DEP Rule 62-308.100")
COST_ROUTE = ("/artificial-turf-cost/", "Turf cost tables for Central Florida")

BI_BUILDING = ("City of Belle Isle — Building and Permitting", "https://www.belleislefl.gov/building")
BI_UES = ("City of Belle Isle Permitting and Inspections Portal (Universal Engineering)", "https://www.teamues.com/city-of-belle-isle-permits-portal/")
BI_UTILITIES = ("City of Belle Isle — Utilities", "https://www.belleislefl.gov/publicworks/page/utilities")
BI_WATERING = ("City of Belle Isle — Watering Days", "https://www.belleislefl.gov/code/page/watering-days")
BI_MUNICODE_UTIL = ("Belle Isle Code of Ordinances, Chapter 32, Utilities", "https://library.municode.com/fl/belle_isle/codes/code_of_ordinances?nodeId=PTIICOOR_CH32UT_ARTIIWACOORLAIR_S32-39PE")
BI_NPDES = ("City of Belle Isle — Storm Water / NPDES", "https://www.belleislefl.gov/publicworks/page/storm-water-npdes")
BI_PARKS_LAKES = ("City of Belle Isle — Parks and Lakes", "https://www.belleislefl.gov/publicworks/page/parks-and-lakes")
BI_CORNERSTONE = ("City of Belle Isle — Cornerstone Charter Academy", "https://www.belleislefl.gov/community/page/cornerstone-charter-academy")
WIKI_BELLE_ISLE = ("Wikipedia — Belle Isle, Florida", "https://en.wikipedia.org/wiki/Belle_Isle,_Florida")
CONWAY_FACT_SHEET = ("USF Water Atlas — Lake Conway fact sheet, Orange County", "https://orange.wateratlas.usf.edu/upload/documents/Lake-Fact-Sheet_Conway.pdf")
CONWAY_LAKE_PAGE = ("Orange County Water Atlas — Lake Conway", "https://orange.wateratlas.usf.edu/waterbodies/lakes/140148/lake-conway")
ASTATULA_OSD = ("USDA NRCS — official series description, Astatula series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/A/ASTATULA.html")
ORANGE_SOIL_SURVEY = ("USDA NRCS — Soil Survey of Orange County, Florida (1989), Internet Archive", "https://archive.org/details/usda-soil-survey-of-orange-county-florida-1989")
CONWAY_MAXLIFE = ("MaxLife Realty — homes on the Conway Chain of Lakes", "https://maxliferealty.com/belle-isle")
ORANGE_PA = ("Orange County Property Appraiser — parcel search", "https://ocpafl.org/")

SRC = [BI_BUILDING, BI_UES, BI_UTILITIES, BI_WATERING, BI_MUNICODE_UTIL, BI_NPDES, BI_PARKS_LAKES,
       BI_CORNERSTONE, WIKI_BELLE_ISLE, CONWAY_FACT_SHEET, CONWAY_LAKE_PAGE, ASTATULA_OSD,
       ORANGE_SOIL_SURVEY, CONWAY_MAXLIFE, ORANGE_PA]

# ============================================================== hub
HUB = page(
    "/areas/belle-isle/", "city",
    "Artificial Turf Installation in Belle Isle, FL (2026)",
    "Synthetic turf for Belle Isle, FL homes on the Lake Conway chain, from seawalled lots to shaded 1960s ranch yards. Permits, water rules, checked September 2026.",
    "Turf for Belle Isle's Conway shoreline and shaded ranch lots",
    capsule(f"Kissimmee Artificial Turf installs synthetic lawns, pet turf and putting greens in Belle Isle, the small incorporated city wrapped around Lake Conway in south Orange County, where installed turf runs {price('residential')} per square foot as of September 2026. Belle Isle sits about 12 miles from our Kissimmee shop and counted 7,032 residents at the 2020 Census, most of them on lots that back onto some part of the Conway chain."),
    "".join([
        sec("A city built around a lake chain, not a grid",
            f"<p>Belle Isle incorporated in 1924, briefly dissolved in 1928, and came back for good in 1954; today it runs a council-manager government from a small city hall on Nela Avenue. What sets the map apart from a typical Orange County suburb is how much of it is water: Lake Conway alone covers 1,771 acres, with Little Lake Conway and a string of smaller connected lakes, Pineloch and Gatlin among them, filling in the rest of the city's shoreline ({ext(BI_PARKS_LAKES[1], 'the city’s own parks and lakes page')}; {ext(CONWAY_LAKE_PAGE[1], 'Orange County’s Water Atlas entry for Lake Conway')}).</p>"
            + f"<p>The 2020 Census counted 7,032 residents across 2,746 households, up from 5,988 in 2010 ({ext(WIKI_BELLE_ISLE[1], 'Census figures compiled for Belle Isle')}). A large share of the housing stock dates to the 1950s through the 1970s, concrete-block ranch and split-level homes on generous lots with decades-old oak canopy, built when a lakefront lot on the Conway chain was still an affordable proposition rather than a premium one ({ext(CONWAY_MAXLIFE[1], 'a real-estate profile of the Conway Chain’s housing stock')}).</p>"),
        sec("Who actually reviews a Belle Isle building permit",
            f"<p>Belle Isle has its own city hall, but not its own building department. The city contracts plan review and inspections to Universal Engineering, a private consultant, rather than routing permits through Orange County's Permitting Services; applications go in through Universal Engineering's own online portal, not the county's Fast Track system ({ext(BI_BUILDING[1], 'the city’s Building and Permitting page')}; {ext(BI_UES[1], 'the Universal Engineering permit portal')}). That's a different setup from the {a('/laws/permits/orange-county/', 'unincorporated county')}, which reviews its own permits directly, so a Belle Isle project follows the city's process even though the parcel sits inside Orange County for tax and property-appraiser purposes.</p>"),
        sec("Water: a city utility bill, but two possible suppliers",
            f"<p>Belle Isle bills its own residents for water rather than folding utility service into a county bill, but the water itself comes from one of two sources depending on the account: Orange County Utilities or Orlando Utilities Commission, the same split that shows up in a few other unincorporated Orange County pockets ({ext(BI_UTILITIES[1], 'the city’s utilities page')}). The city sets its own watering-day ordinance on top of whichever supplier serves a given address: during daylight saving time, odd addresses water Wednesday and Saturday and even addresses Thursday and Sunday, tightening to a single weekend day per parity group in the winter months, all under Chapter 32 of the city code ({ext(BI_WATERING[1], 'Belle Isle’s watering-days page')}; {ext(BI_MUNICODE_UTIL[1], 'Chapter 32, Utilities')}).</p>"
            + f"<p>Lake Conway itself drains through the Boggy Creek watershed under the St. Johns River Water Management District, and the city is a co-permittee with Orange County on the federal stormwater discharge permit that governs what runs off a Belle Isle yard into that system ({ext(CONWAY_FACT_SHEET[1], 'the Lake Conway fact sheet')}; {ext(BI_NPDES[1], 'the city’s stormwater program page')}).</p>"),
        table("Belle Isle lot types and how a turf job changes",
              ["Lot type", "What's typically on it", "What we plan around"],
              [["Seawalled Main Conway lakefront", "A bulkhead, a private dock, an open lawn to the water's edge", "The seawall exception lets turf run to the wall instead of stopping 10 ft short"],
               ["Smaller connected lakes (Pineloch, Gatlin)", "Older, unwalled shoreline, narrower lots", "The full 10-ft setback applies where there's no seawall or bulkhead"],
               ["1950s-1970s inland ranch homes", "Concrete-block construction, decades-old live oaks, wide side yards", "A drip-line check before excavation, since the canopy usually outreaches the trunk"],
               ["Newer family streets near Cornerstone Charter Academy", "Smaller, fenced backyards, younger landscaping", "Less canopy to work around, more emphasis on a defined play or pet area"]],
              "Checked against the city's own site, Orange County's Water Atlas and Chapter 32 of the Belle Isle Code, September 2026."),
        sec("Permits, the county line and your association",
            f"<p>Because Belle Isle is incorporated, {a('/laws/permits/orange-county/', 'the unincorporated Orange County office')} isn't who reviews a turf permit here, even though the Orange County Property Appraiser still carries the parcel record; Universal Engineering, under contract to the city, is the office to call. Neither Belle Isle's code nor Orange County's addresses synthetic turf by name, so a project answers to ordinary landscape and drainage review plus {a('/laws/florida-hb-683/', 'the state’s May 2026 turf standard')}, not a local turf ordinance.</p>"
            + f"<p>A homeowners association is a separate step again. Several of Belle Isle's older platted subdivisions carry deed restrictions from the 1960s and 1970s, and {a('/laws/hoa-rules/', 'Florida’s HOA-visibility statute')} only protects turf that a covenant committee can't see from the street or a neighboring lot, regardless of how old the covenant is.</p>"),
        "<!--AUTO:city-services-->",
    ]),
    faqs=[
        faq("Does Belle Isle have its own building department for a turf permit?",
            "No. The city contracts building permit review and inspections to Universal Engineering rather than staffing its own department, and applications go through that contractor's online portal rather than Orange County's system, even though Belle Isle sits inside Orange County."),
        faq("Is Belle Isle's water managed by the St. Johns or South Florida water district?",
            "St. Johns River Water Management District. Lake Conway drains through the Boggy Creek watershed toward that district's jurisdiction, which is why Belle Isle's watering-day ordinance and any shortage restrictions track SJRWMD's rules rather than the South Florida district that covers parts of southeast Orange County near Lake Nona."),
        faq("Can turf run all the way to the water on a seawalled Lake Conway lot?",
            "The state's rule sets its 10-foot waterbody setback aside specifically where a seawall or bulkhead already separates the yard from the water, which describes most of the premium lots directly on Main Conway. A lake lot without a wall, on one of the smaller connected lakes, still needs the full 10 feet."),
        faq("How far is Belle Isle from your Kissimmee shop?",
            "About 12 miles by straight line, which puts it comfortably inside the roughly 40-mile radius we cover. Most Belle Isle jobs get scheduled alongside other south Orange County stops on the same route."),
        faq("What should I check before hiring the best turf installer near me in Belle Isle?",
            "Ask whether the crew already knows the seawall exception applies to Main Conway lots but not to every connected lake, whether they've planned for a decades-old oak's drip line on an older ranch lot, and whether the quote spells out base depth and infill type in writing. Those three answers say more than a sales pitch."),
    ],
    sources=SRC, city=SLUG, crumbs=[("Service areas", "/areas/")], crumb="Belle Isle",
    related=[("/areas/orange-county/", "Artificial turf across Orange County"), ORANGE_PERMIT_ROUTE,
             ("/areas/hunters-creek/", "Artificial turf in Hunters Creek"), ("/areas/orlando/", "Artificial turf in Orlando"),
             COST_ROUTE],
)

# ============================================================== LOCAL
LOCAL = {
    "residential": {
        "title": "Artificial Grass Installation in Belle Isle, FL",
        "meta": "Synthetic lawn installation for Belle Isle homes on the Conway chain, from seawalled lakefronts to shaded 1960s ranch yards. Checked September 2026.",
        "h1": "Lawns built for Belle Isle's lake edges and oak canopy",
        "lede": capsule(f"Installed artificial grass runs {price('residential')} per square foot in Belle Isle as of September 2026, the same Central Florida range on a seawalled Main Conway lot or an inland ranch lot two streets back. Belle Isle's soil survey maps most of the city to Astatula fine sand, an excessively drained upland soil unlike the wet flatwoods common elsewhere in our service area."),
        "sections": [
            ("A seawall changes where turf is allowed to end",
             f"<p>The state's 10-foot waterbody setback has a specific carve-out for a lot where a seawall or bulkhead already separates yard from water, and that exception covers a real share of Belle Isle's Main Conway frontage, where private docks and bulkheaded shorelines are standard rather than the exception. On a wall like that, turf can run to the property's edge instead of stopping short of the water, which changes the usable square footage on a waterfront lot more than almost any other single rule.</p>"
             + "<p>A lot on one of the smaller connected lakes, Pineloch or Gatlin among them, often lacks that wall, since older, unwalled shoreline is more common on the chain's smaller lakes than on Main Conway itself, and the full 10-foot setback applies there instead.</p>"),
            ("Excavating under a canopy that's been growing since the 1960s",
             f"<p>A ranch or split-level home built in Belle Isle's main growth years carries oak canopy that's had sixty-plus years to spread well past the trunk, and the state's drip-line rule bars turf under that reach on either the property it grows on or a neighbor's, unless a certified arborist signs off. On an older Belle Isle lot, the canopy from a single mature oak can shade and root through more of a yard than a homeowner expects walking the property before work starts.</p>"
             + f"<p>We mark actual branch tips rather than eyeballing the trunk before laying out where {svc('residential', 'a lawn conversion')} can go, since guessing short on an oak this size is an easy way to plan a yard that has to be redrawn mid-project.</p>"),
            ("Fast-draining sand, not a high water table, is the local quirk",
             f"<p>Orange County's own soil survey maps Belle Isle and the rest of the Conway shoreline mostly to Astatula fine sand, an excessively drained series with the water table sitting more than five feet down in most spots ({ext(ASTATULA_OSD[1], 'the Astatula series description')}; {ext(ORANGE_SOIL_SURVEY[1], 'the 1989 Orange County soil survey')}). That's close to the opposite problem a base has to solve compared with the flatwoods sand under {city('narcoossee', 'a Narcoossee')} or Osceola County yard: instead of fighting a water table that climbs every summer, the base here mostly has to hold a stable, level surface on sand that drains almost as fast as the turf sitting on top of it.</p>"),
        ],
        "scenario": ("Say you have a 1,100 sq ft backyard on a Pineloch canal",
                     f"<p>Say a 1,100 sq ft backyard on one of the smaller lakes off the Conway chain, unwalled, backs onto a canal connecting to Pineloch. Multiplying that by the published {price('residential')} per square foot figure puts the job between roughly $8,800 and $19,800, with typical Belle Isle estimates settling closer to $11,000-$17,600.</p>"
                     + "<p>Because there's no seawall, the crew stakes the state's 10-foot setback from the canal's ordinary water line before ordering material, which trims the buildable yard slightly from what the property line alone would suggest. A mature oak near the property's north corner also gets its drip line marked, since its canopy reaches into what would otherwise be turf area.</p>"),
        "faqs": [
            faq("Does every Lake Conway lot in Belle Isle have a seawall?",
                "No. Seawalls and bulkheads are common on Main Conway's higher-value frontage, but several of the smaller connected lakes and older, unwalled stretches of shoreline don't have one, which means the full 10-foot setback from the water still applies on those lots."),
            faq("Who reviews a Belle Isle residential turf permit?",
                f"Universal Engineering, under contract to the city, not {a('/laws/permits/orange-county/', 'Orange County’s own permitting office')}. Belle Isle's own code doesn't name synthetic turf specifically, so the application goes through the contractor's standard building-permit review."),
        ],
        "sources": SRC,
    },
    "pet": {
        "title": "Belle Isle Pet Turf: Dog Runs Under Oak Canopy",
        "meta": "Pet turf and dog runs for Belle Isle backyards, from oak-shaded ranch lots to fenced yards near Cornerstone Charter Academy. Checked September 2026.",
        "h1": "Dog runs for Belle Isle's shaded, fenced backyards",
        "lede": capsule(f"Pet turf in Belle Isle runs {price('pet')} per square foot installed as of September 2026, whether the yard sits under sixty-year-old oaks near Lake Conway or in a newer, tighter subdivision near Cornerstone Charter Academy. Fast-draining Astatula sand under most of the city means a dog run here rarely fights standing water the way one on flatwoods soil does."),
        "sections": [
            ("A shaded backyard is a mud problem grass never solves",
             "<p>Mature oak canopy over a Belle Isle backyard keeps a dog run cooler on a summer afternoon, but it also keeps the ground under it damp and thin on sunlight, which is exactly the combination that turns a grassed dog path into a bare, muddy track within a season. Pet turf's drainage backing solves the mud without needing the sun grass does, and the shade that would kill a lawn is actually an advantage for a dog run, since it keeps the surface cooler underfoot on the hottest afternoons.</p>"
             + "<p>What the canopy does add is more leaf and acorn debris to clear from the infill through the fall than a full-sun yard would ever see.</p>"),
            ("Setting a run back from a canal or lake edge",
             f"<p>On a waterfront Belle Isle lot, a dog run built close to a canal or a stretch of unwalled shoreline still falls inside the same 10-foot setback that governs the rest of a lawn, since the rule doesn't distinguish a lawn from a fenced pet area. A run planned right up to the water's edge on one of the chain's smaller, unwalled lakes needs to shift back from that line the same way {svc('residential', 'a plain lawn')} would; a seawalled Main Conway lot has more flexibility, since the wall itself satisfies the setback's exception.</p>"),
            ("Smaller, fenced yards near Cornerstone Charter Academy",
             f"<p>The newer, tighter subdivisions on Belle Isle's streets near {ext(BI_CORNERSTONE[1], 'Cornerstone Charter Academy')} run closer to a standard zero-lot-line footprint than the city's older ranch lots do, with less canopy and a fully fenced backyard as the default rather than the exception. A dog run on a lot like this is usually the whole backyard rather than a carved-out section, which simplifies layout but puts more weight on getting the perimeter anchoring right, since there's no open field around it to absorb a mistake.</p>"),
        ],
        "scenario": ("Say you have a 350 sq ft shaded run under an oak canopy",
                     f"<p>Say a 350 sq ft backyard dog run sits under decades-old oak canopy on an inland Belle Isle ranch lot, currently more dirt than grass. Multiplying that by the published {price('pet')} per square foot figure puts the job between roughly $3,500 and $6,300, with typical Belle Isle estimates settling closer to $4,200-$5,600.</p>"
                     + "<p>Because the canopy shades most of the run, no weed barrier goes under the turf, since a barrier traps moisture that direct sun would otherwise dry out. Zeolite infill goes in at the standard rate, and the crew maps the oak's drip line first to confirm the run's footprint doesn't need to shrink to stay clear of it.</p>"),
        "faqs": [
            faq("Does a dog run need to stay outside a live oak's drip line the same way a lawn does?",
                "Yes. The state's rule doesn't carve out an exception for a fenced pet area, so a run planned under a mature oak's canopy needs the same certified-arborist sign-off a full lawn would, unless it's sited outside the drip line entirely."),
            faq("Is Astatula sand good or bad for a dog run's drainage?",
                "Good, generally. Astatula is an excessively drained series, so a run built on it drains fast on its own; the base still needs to be compacted properly so it holds a stable surface, since fast-draining sand shifts more easily under a plate compactor than denser soil does."),
        ],
        "sources": SRC,
    },
    "putting": {
        "title": "Backyard Putting Greens on Belle Isle Ranch Lots",
        "meta": "Backyard putting greens for Belle Isle's wide 1960s ranch lots, built on the city's fast-draining Astatula sand near Lake Conway. Checked September 2026.",
        "h1": "Putting greens on Belle Isle's wide, sandy ranch lots",
        "lede": capsule(f"A backyard putting green in Belle Isle runs {price('putting')} per square foot as of September 2026. The city's wide, flat 1950s-and-1960s ranch lots and its fast-draining Astatula sand base give a green here two advantages a tighter, wetter lot elsewhere in Central Florida usually doesn't have."),
        "sections": [
            ("Wide ranch-era side yards were made for a real layout",
             "<p>A ranch or split-level home built during Belle Isle's main growth decades typically sits on a wider, shallower lot than a newer subdivision home does, with a side yard that runs long rather than narrow. That shape suits a putting green better than a deep, boxy backyard does, since a long, flat run gives a green room for two cups and a real fringe transition instead of squeezing everything into one corner.</p>"
             + "<p>The tradeoff on an older lot is usually a mature tree somewhere along that side yard, which shapes the green's exact footprint more than the lot's overall size does.</p>"),
            ("Why Astatula sand holds a truer roll",
             f"<p>Astatula's excessively drained profile, confirmed for the area in the county's own soil survey, means a green's subbase here compacts and stays flat with less fighting against trapped moisture than a green built on Osceola County's wetter flatwoods sand ({ext(ASTATULA_OSD[1], 'the Astatula series description')}). A stable, evenly compacted subbase is what keeps a ball rolling true months after installation, and sand this well-drained gives that subbase a head start that wetter Central Florida soil doesn't offer.</p>"
             + "<p>The same fast drainage means less waiting for the ground to dry out between a rainy summer week and the next install date, which is a scheduling advantage more than a build-quality one.</p>"),
            ("Reading shade before ordering the turf",
             "<p>A green needs consistent sun to read a true, predictable speed, and a Belle Isle lot with heavy inherited oak canopy can shade half a proposed green through the afternoon while leaving the other half in full sun, which shows up later as an uneven roll between the shaded and lit sections. Walking the site at the time of day the green will actually get used, not just at midday, catches that problem before the subbase goes in rather than after.</p>"),
        ],
        "scenario": ("Say you have a 450 sq ft green on a wide side yard",
                     f"<p>Say a Belle Isle ranch home's side yard runs 450 sq ft, flat and mostly clear of canopy, and the owner wants a two-cup green with a chipping approach at one end. Multiplying that by the published {price('putting')} per square foot figure puts the job between roughly $6,300 and $13,500, with typical Belle Isle estimates settling closer to $8,100-$11,250.</p>"
                     + "<p>Because the site maps to Astatula sand, the subbase compacts in fewer passes than a wetter-soil green would need, and the crew still lasers the surface level before the carpet goes down. A young oak at the yard's edge stays outside the green's footprint entirely rather than needing an arborist review.</p>"),
        "faqs": [
            faq("Does Belle Isle's sandy soil mean a putting green needs less base material?",
                "Not less material, but an easier compaction. The same two-to-four-inch washed crushed-rock depth applies regardless of what's underneath it; Astatula's fast drainage just means the crew spends less time fighting trapped moisture while compacting it."),
            faq("Can a putting green go on a lot with heavy oak canopy?",
                "It can, as long as the green's footprint stays outside the canopy's drip line or a certified arborist signs off on the exception. Shade also affects how evenly a green plays, which is a performance question separate from the legal one."),
            faq("Do I need HOA approval for a putting green in an older Belle Isle subdivision?",
                f"Some of the city's older platted subdivisions carry deed restrictions from the 1960s and 1970s, so it's worth checking a specific covenant before building. {a('/laws/hoa-rules/', 'Florida’s HOA-visibility statute')} protects a green that isn't visible from the street or a neighboring lot regardless of how old the restriction is."),
        ],
        "sources": SRC,
    },
    "playground": {
        "title": "Belle Isle Playground Turf Near Cornerstone Charter",
        "meta": "Playground turf for Belle Isle backyards near Cornerstone Charter Academy and under mature oak canopy on older ranch lots. Checked September 2026.",
        "h1": "Play surfaces for Belle Isle's family backyards",
        "lede": capsule(f"Playground turf in Belle Isle runs {price('playground')} per square foot as of September 2026. Families near Cornerstone Charter Academy and on the city's older, oak-shaded ranch lots both ask for it, and the two situations call for different siting decisions before the shock pad ever goes in."),
        "sections": [
            ("Siting a play area away from the water",
             "<p>A Belle Isle backyard that backs onto Lake Conway or one of its connected lakes often has more usable yard away from the shoreline than an owner first assumes, since the state's setback pulls turf back from the water's edge on any lot without a seawall. Putting a play structure in that setback zone isn't an option regardless of the surface underneath it, so on a waterfront lot we plan the play area's location before the rest of the yard's layout, closer to the house than the water.</p>"
             + "<p>A seawalled lot has more flexibility here too, the same way it does for a plain lawn, since the wall satisfies the setback exception.</p>"),
            ("Retrofitting under a swing set that's already there",
             f"<p>A fair number of calls in Belle Isle's older neighborhoods are a retrofit: a swing set or a play structure that's been sitting on bare, worn grass for years, under oak canopy that keeps the spot shaded and cool but never lets grass fill back in. Shade that kills a lawn is neutral for {svc('playground', 'playground turf')}, since the surface doesn't need sun to survive the way sod does, and the same canopy keeps the surface a little cooler on a summer afternoon than an open, full-sun play area would run.</p>"
             + "<p>The shock pad still gets sized to the existing equipment's actual fall height rather than a standard depth, whether the structure is new or has been in the yard for a decade.</p>"),
            ("Newer, smaller family lots near the school",
             f"<p>Streets built up more recently near {ext(BI_CORNERSTONE[1], 'Cornerstone Charter Academy')} carry smaller, fenced backyards with less inherited canopy than Belle Isle's older sections, which usually means a play area competes for space with a patio, a shed or a dog run rather than sharing a wide-open yard. On a lot this size, a defined pad under one piece of equipment, bordered by regular lawn turf, is the more common build than a full-yard play surface.</p>"),
        ],
        "scenario": ("Say you have a 280 sq ft play area near the school",
                     f"<p>Say a family on a newer street near Cornerstone Charter Academy wants a 280 sq ft play pad under a swing set with a 7-ft fall height, set into a corner otherwise covered in regular sod. Multiplying that by the published {price('playground')} per square foot figure puts the job between roughly $2,800 and $7,000, with typical Belle Isle estimates settling closer to $3,360-$5,320.</p>"
                     + "<p>The shock pad depth is set for the 7-ft fall height rather than a generic residential number, and the pad's border meets the surrounding lawn turf at a trimmed, glued seam. No canopy sits close enough to the site to raise a drip-line question on this particular lot.</p>"),
        "faqs": [
            faq("Can a play structure go inside the state's 10-foot lake setback in Belle Isle?",
                "No, not on a lot without a seawall or bulkhead. The setback restricts any synthetic turf, including a play surface, from that strip regardless of what sits on top of it, so a waterfront lot needs its play area sited farther back from the shoreline than the property line alone might suggest."),
            faq("Is Cornerstone Charter Academy connected to this playground turf work?",
                "No. Cornerstone Charter Academy is a public charter school, and we have no relationship with it; it's referenced here only because several of the family neighborhoods that ask for playground turf sit on streets near the school."),
        ],
        "sources": SRC,
    },
    "pool": {
        "title": "Pool & Lanai Turf in Belle Isle, FL",
        "meta": "Turf around Belle Isle pool decks, from oak-shaded 1960s lanais to newer screened enclosures near Lake Conway. Checked September 2026.",
        "h1": "Pool-deck turf for Belle Isle's shaded, older lots",
        "lede": capsule(f"Belle Isle pool-deck turf costs whatever a plain lawn would, {price('residential')} installed per square foot as of September 2026, since pool surrounds don't get their own price key. Decades-old oak canopy over many of the city's ranch-era pool decks brings more leaf litter than heat, which changes the upkeep conversation more than the install itself."),
        "sections": [
            ("Oak litter is the bigger issue than sun on an older deck",
             "<p>A pool deck shaded by a mature Belle Isle oak avoids the worst of the summer surface-heat problem full-sun turf runs into elsewhere, but it trades that for a steady drop of leaves, acorns and pollen that settles into the infill and needs clearing more often than a sun-exposed, treeless deck would. Left alone through a fall drop, that debris works down into the backing and changes how the surface drains, the same way it would on a plain lawn.</p>"
             + "<p>The trade generally favors the shaded deck anyway, since the alternative on a full-sun Belle Isle lanai is a surface hot enough to need a hose rinse before bare feet cross it on a July afternoon.</p>"),
            ("A canal or lake view doesn't change the pool deck's base",
             f"<p>Several Belle Isle pool decks sit close enough to a canal or the lake itself that the state's 10-foot waterbody setback and the pool layout end up sharing the same stretch of yard. Where a lot has a seawall, that overlap mostly disappears, since the wall satisfies the setback and turf can run to the pool cage's edge; without one, the crew checks both the pool deck's dimensions and the water setback before finalizing where {svc('pool', 'pool-area turf')} can go.</p>"),
            ("Retrofitting a screen enclosure onto an older lanai",
             "<p>A number of Belle Isle's original 1960s and 1970s pools were built before screen enclosures were standard, and some have since had a cage added around an existing deck rather than built with the house. Turf going in during that kind of retrofit needs the same drainage underlay at the deck's edge a new-construction cage would need, but the crew is often working around an existing pool finish and older deck expansion joints that a from-scratch install wouldn't have to account for.</p>"),
        ],
        "scenario": ("Say you have a 200 sq ft shaded lanai strip",
                     f"<p>Say a 200 sq ft strip of grass runs along one side of a screened pool lanai on an older Belle Isle lot, thin and patchy from decades of oak shade overhead. Multiplying that by the published {price('residential')} per square foot figure puts the job between roughly $1,600 and $3,600, with typical Belle Isle estimates settling closer to $2,000-$3,200.</p>"
                     + "<p>Because the canopy overhead sheds through the fall, the infill choice leans toward a slightly heavier grain that resists washing toward the deck drain during a hard rinse. The base is feathered to the deck's existing height, matching the older concrete's slight settle rather than assuming a perfectly level slab.</p>"),
        "faqs": [
            faq("Does oak-shaded pool turf need less maintenance than full-sun turf in Belle Isle?",
                "Less heat management, more debris management. A shaded deck rarely gets hot enough to need a cooling rinse, but it collects leaves and pollen that a full-sun deck doesn't, so the maintenance shifts from a heat problem to a clearing-and-brushing one rather than disappearing."),
            faq("Can turf run to the edge of a pool cage on a seawalled Belle Isle lot?",
                "Yes, in most cases, since a seawall or bulkhead satisfies the state's water setback exception and the pool cage's own footprint becomes the limiting boundary instead. A lot without a seawall needs both the cage layout and the 10-foot water setback checked together."),
        ],
        "sources": SRC,
    },
    "repair": {
        "title": "Turf Repair in Belle Isle: Lakefront & Oak-Root Fixes",
        "meta": "Turf repair for Belle Isle lawns and pool decks, from wind-lifted lakefront edges to oak-root heave on older ranch lots. Checked September 2026.",
        "h1": "Fixing turf on Belle Isle's lakefront and older lots",
        "lede": capsule("Turf repair in Belle Isle is quoted after photos or a site visit, since a wind-lifted lakefront edge, a root-heaved seam under an old oak and a washed-out infill strip near a seawall each need a different fix. Open water frontage and decades-old canopy both show up in repair calls here more than they would on a younger, inland subdivision lot."),
        "sections": [
            ("Open water off Main Conway lifting an unsheltered edge",
             "<p>A turf edge facing open water on Main Conway takes a steadier, less-blocked wind than one tucked into a canal or shaded by neighboring homes, and a lifted corner after a windy stretch traces back to that exposure more often than to a workmanship problem. The fix usually means re-anchoring the affected stretch and, where the budget allows, upgrading a nailed-only edge to a paver or bender-board border that holds up better against repeat wind off the open lake.</p>"),
            ("Root heave from an oak that's been growing since before the turf went in",
             "<p>A live oak on an older Belle Isle lot keeps growing long after a lawn conversion is finished, and a root that was several feet from the surface at installation can work its way up and lift a seam or a whole section years later, especially along the edge closest to the trunk. That's a different repair than a storm-related lift: the fix usually means pulling back the affected turf, addressing the root without cutting into it carelessly, and rebuilding the base over the new grade rather than just re-anchoring an edge.</p>"
             + "<p>Checking for early lifting near mature trees every couple of years catches this before a small ridge becomes a trip hazard.</p>"),
            ("Infill drifting toward a seawall after a hard rain",
             f"<p>A lawn graded toward a seawalled edge on {city('conway', 'the Conway chain')} can lose a visible amount of infill over the wall during a heavy storm if the grade or the edge anchoring at that specific point isn't quite right, the same problem that shows up at any low corner elsewhere in our service area. The fix there isn't a different infill, it's correcting the grade and the edge at the exit point so water, and the sand riding with it, doesn't concentrate at the wall.</p>"),
        ],
        "scenario": ("Say wind off the lake lifted a 150 sq ft edge",
                     "<p>Say a stretch of wind off open water on Main Conway lifted about 150 sq ft of turf along a lakefront lawn's unsheltered edge, where the original border was nailed rather than set into a paver edge. A site visit would check whether the base underneath shifted or the fastening alone gave way, since the two problems call for different repairs.</p>"
                     + "<p>If the base held, the fix is usually a re-anchored edge with a heavier border added along that exposed stretch. If the wind also drove water under the turf and washed base material out, that section needs to come up, get re-based and get reseamed before the edge goes back down.</p>"),
        "faqs": [
            faq("Why do lakefront Belle Isle lots seem to need more edge repairs than inland lots?",
                "Mostly wind exposure. An inland lot has houses, fences and trees breaking wind before it reaches a turf edge; a lot facing open water on Main Conway doesn't have that shelter, so a nailed-only border there takes more direct load during a windy stretch."),
            faq("Can an oak's roots actually push up an existing turf install years later?",
                "Yes, and it's a slower, quieter failure than a storm-related lift. A root that was safely below grade at installation can rise enough over several years to tent a seam or a section, which is why checking the ground near mature trees periodically catches it while the fix is still a small one."),
        ],
        "sources": SRC,
    },
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
