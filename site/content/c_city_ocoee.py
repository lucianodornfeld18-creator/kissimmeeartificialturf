# -*- coding: utf-8 -*-
"""Ocoee, FL (tier 2, Orange County). Building Division, water utility and history facts researched
September 2026 directly from ocoee.org; not reused from c_permits.py or c_counties.py, which don't
cover this city individually. Soil, county-wide water-district and permit-hub facts reuse the URLs
already verified in c_permits.py / c_counties.py for Orange County."""
from _helpers import page, capsule, sec, table, faq, a, svc, city, cs, post, src, ext, price
from _cityservice import cityservice_pages

SLUG = "ocoee"

OC_PERMITTING = ("City of Ocoee — Permitting", "https://www.ocoee.org/169/Permitting")
OC_BUILDING = ("City of Ocoee — Building Division", "https://www.ocoee.org/163/Building-Division")
OC_WATER = ("City of Ocoee — Irrigation Schedule & New Sod", "https://www.ocoee.org/822/Irrigation-Schedule-New-Sod")
OC_HISTORY = ("City of Ocoee — City History", "https://www.ocoee.org/728/City-History")
OC_DOWNTOWN = ("City of Ocoee — Downtown", "https://www.ocoee.org/1099/Downtown")
OC_WIKI = ("Wikipedia — Ocoee, Florida", "https://en.wikipedia.org/wiki/Ocoee,_Florida")
SJRWMD_ORANGE = ("St. Johns River Water Management District — Orange County", "https://www.sjrwmd.com/district-counties/orange-county/")
WESMERE_INFO = ("Florida Neighborhood Realty — Wesmere, Ocoee, FL", "https://www.floridaneighborhoodrealty.com/wesmere-ocoee-homes-sale/")
OCOEE_OSD = ("USDA NRCS — official series description, Ocoee series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/O/OCOEE.html")
CANDLER_OSD = ("USDA NRCS — official series description, Candler series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/C/CANDLER.html")
APOPKA_OSD = ("USDA NRCS — official series description, Apopka series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/A/APOPKA.html")
ORANGE_PA = ("Orange County Property Appraiser — parcel search", "https://ocpafl.org/")

PERMITS_ORANGE = ("/laws/permits/orange-county/", "Orange County permit rules for turf")
HOA_ROUTE = "/laws/hoa-rules/"
HB683_ROUTE = "/laws/florida-hb-683/"

SRC = [OC_PERMITTING, OC_BUILDING, OC_WATER, OC_HISTORY, OC_DOWNTOWN, OC_WIKI, SJRWMD_ORANGE, WESMERE_INFO, OCOEE_OSD, CANDLER_OSD, APOPKA_OSD, ORANGE_PA, "dep-rule", "fs125572", "fs7203045", "usda-wss"]


# ============================================================== HUB
def _hub():
    body = "".join([
        sec("Turf work in Ocoee, from Starke Lake to the Maguire Road corridor",
            f"<p>An Ocoee installed lawn prices at {price('residential')} per square foot on the same Central Florida range as the rest of our area, checked in September 2026, about 21 miles from our Kissimmee base. Ocoee was platted as a subdivision in 1886 and became a city in May 1925, and its economy ran on citrus groves until hard freezes in the 1980s wiped them out; the packinghouses closed, the groves gave way to subdivisions and shopping centers, and Orlando's suburban growth pushed west into what had been farmland ({ext(OC_HISTORY[1], 'the city’s own history')}; {ext(OC_WIKI[1], 'Wikipedia’s summary of that transition')}).</p>"
            + f"<p>State Road 50 reached downtown in 1959, and a 1990 extension of State Road 408 tied Ocoee directly into Orlando's expressway grid, which is roughly when the city's population growth took off; Ocoee counted 47,295 residents in the 2020 Census, up 98.5% from 2000 ({ext(OC_WIKI[1], 'population figures')}). That growth shows up as older lake-town blocks around downtown sitting next to master-planned communities built from the 1990s forward, both served by the same {svc('residential', 'lawn conversion')}, {svc('pet', 'pet turf')} and {svc('putting', 'putting green')} work either side of town.</p>"),
        sec("Ocoee yard types and what we do differently",
            "<p>Three lot types cover most of what a crew runs into here.</p>"
            + table("Ocoee yard types and what we do differently",
                    ["Yard type", "What's typical", "What we do differently"],
                    [["Starke Lake-area bungalow (1920s–1950s, oak canopy)", "Small lot, mature oaks close to downtown's lakefront park", "Drip-line check before digging; shallow excavation near root zones"],
                     ["Wesmere or a similar 1990s–early 2000s gated community", "Fountain ponds, an HOA architectural review, cul-de-sac lots", "Turf held 10 ft off pond edges, ARC packet prepared before ordering material"],
                     ["Newer growth-era subdivision off Maguire or Clarke Road", "2000s–present construction, pool cage common, compacted builder fill", "A base built for leftover fill rather than undisturbed native sand"]],
                    f"The {price('residential')} per sq ft range holds across all three; access and review change the bid, not the address.")),
        sec("Who reviews a turf permit inside Ocoee's city limits",
            f"<p>Ocoee, like Winter Garden next door, runs its own Building Division rather than routing permits through Orange County, so an Ocoee address is reviewed at the city's own counter. We haven't built a dedicated permit page for Ocoee's own code specifically, and it's worth saying that plainly instead of guessing: the fastest path is a call to the Building Division at 407-905-3104 or a look at the city's online permitting system before scheduling a crew ({ext(OC_PERMITTING[1], 'Ocoee Permitting')}).</p>"
            + f"<p>A lot that turns out to sit outside the city limits, in unincorporated Orange County, falls under {a(PERMITS_ORANGE[0], PERMITS_ORANGE[1])} instead; the {ext(ORANGE_PA[1], ORANGE_PA[0])} settles which office actually has a given parcel. Either jurisdiction sits under the same statewide floor described at {a(HB683_ROUTE, 'HB 683 and Rule 62-308.100')}, and a gated community's own architectural review answers to a separate statute covered at {a(HOA_ROUTE, 'what a Florida HOA can and can’t restrict')}.</p>"),
        sec("Water rules under the St. Johns River district",
            f"<p>Ocoee bills and schedules its own water rather than buying through Orange County Utilities. Watering days run by the last digit of the address: during Daylight Saving Time, odd addresses water Wednesday and Saturday, even addresses water Sunday and Thursday, and non-residential properties water Tuesday and Friday, with nothing allowed between 10 a.m. and 4 p.m.; the schedule drops to one day a week once Eastern Standard Time starts ({ext(OC_WATER[1], 'the city’s current irrigation schedule')}). A hose fitted with an automatic shut-off nozzle is exempt from those days entirely, which matters more for a quick rinse than it does for a full sprinkler cycle.</p>"
            + f"<p>Ocoee sits inside the St. Johns River Water Management District, the same district covering most of Orange County outside its southeastern edge ({ext(SJRWMD_ORANGE[1], 'SJRWMD’s Orange County coverage')}). None of that watering calendar reaches a synthetic lawn once its in-ground heads are capped, which the state's turf standard requires no matter which utility sends the bill.</p>"),
        sec("Ocoee's ground, from downtown's oaks to a gated pond community",
            f"<p>The USDA's official Ocoee series, first described near this city, is a poorly drained muck found in floodplains and freshwater marshes, not what sits under a typical yard here ({ext(OCOEE_OSD[1], 'USDA’s Ocoee series description')}). Most upland lots instead sit on the well-drained, sandy Candler and Apopka series common across the west Orange County ridge ({ext(CANDLER_OSD[1], 'USDA’s Candler series description')}; {ext(APOPKA_OSD[1], 'USDA’s Apopka series description')}), though a specific address is worth checking on the {src('usda-wss', 'Web Soil Survey')} rather than assuming either soil profile applies.</p>"
            + f"<p>Starke Lake's western shore anchors downtown, where the city's own park land keeps mature oak canopy close to the water and puts the state's drip-line rule in play on a fair number of jobs there ({ext(OC_DOWNTOWN[1], 'the city’s downtown page')}). South of downtown, Wesmere, a gated community built mostly between 1991 and the early 2000s around several large fountain ponds, put close to a hundred homes on waterfront lots that carry the same 10-ft setback as any other Ocoee pond ({ext(WESMERE_INFO[1], 'community details for Wesmere')}). Searching for the best artificial turf company near you in Ocoee starts with the same two questions either lot type raises: how deep does the base go, and is the crew already thinking about the pond or the oak canopy before the tape measure comes out.</p>"),
        "<!--AUTO:city-services-->",
    ])
    faqs = [
        faq("Does Ocoee require a permit for a synthetic lawn?",
            "The city hasn't published a synthetic-turf-specific rule as of September 2026, so a residential conversion goes through Ocoee's ordinary exterior-work and drainage permitting instead. Call the Building Division at 407-905-3104 before scheduling a crew, since the scope of the job can change the answer."),
        faq("Which water management district covers Ocoee?",
            "The St. Johns River Water Management District, the same one covering most of Orange County outside its southeastern edge toward Lake Nona. Ocoee's own utility sets the day-to-day watering schedule within that district's broader rules."),
        faq("Is the USDA soil series named after Ocoee actually under most yards there?",
            "No. The official Ocoee series is a poorly drained muck found in floodplains and marshes, named for where it was first described near the city, not for what's typically under an upland residential lot. Most Ocoee yards instead sit on well-drained Candler or Apopka sand."),
        faq("Does a Wesmere HOA add anything beyond Ocoee's own permit rules?",
            "Likely yes, on top of whatever the city requires. A gated community built around shared fountain ponds typically runs an architectural review for exterior changes, and Florida's visibility statute protects a fenced backyard from that review more than it protects anything visible from the street or the water."),
        faq("How far is Ocoee from your Kissimmee crew?",
            "About 21 miles by straight line. That distance doesn't move the published per-square-foot range; an Ocoee job usually gets scheduled alongside another west Orange County stop the same day."),
    ]
    return page("/areas/ocoee/", "city",
                "Artificial Turf in Ocoee, FL (2026 Guide)",
                "Synthetic turf installation, permits, St. Johns water rules and soil facts for Ocoee, FL. Checked September 2026, about 21 miles from Kissimmee.",
                "Artificial turf and synthetic grass in Ocoee",
                capsule(f"Kissimmee Artificial Turf installs, repairs and cleans synthetic lawns in Ocoee, about 21 miles from our Kissimmee base. A residential job here prices at {price('residential')} a square foot, matching every other town we serve, checked in September 2026. The city runs its own Building Division and its own water utility, and the USDA soil series that shares Ocoee's name is a marsh muck, not what's under most upland yards."),
                body, faqs=faqs, sources=SRC, city=SLUG, crumbs=[("Service areas", "/areas/")], crumb="Ocoee",
                related=[("/areas/orange-county/", "Artificial turf across Orange County"), PERMITS_ORANGE, ("/areas/winter-garden/", "Turf in Winter Garden"), ("/areas/apopka/", "Turf in Apopka"), ("/artificial-turf-cost/", "Turf cost tables for Central Florida")])


HUB = _hub()


# ============================================================== residential
def _residential():
    sections = [
        ("A lawn on Ocoee's ridge sand, not the marsh soil that shares its name",
         f"<p>The USDA's own Ocoee series, first described near this city, turns out to be a poorly drained muck that forms in floodplains and marshes, nothing like what sits under most residential lots here ({ext(OCOEE_OSD[1], 'USDA’s Ocoee series description')}). Upland yards instead run to the same well-drained Candler and Apopka sand common across the rest of the west Orange County ridge, which sheds water faster than the flatwoods sand under a typical Osceola County lawn ({ext(CANDLER_OSD[1], 'USDA’s Candler series description')}).</p>"
         f"<p>That fast drainage still needs a properly compacted rock base underneath it; loose ridge sand shifts under a plate compactor if the lifts aren't built and checked one at a time, regardless of how quickly the ground drains once turf goes down. The same ridge sand continues north through {city('winter-garden', 'Winter Garden')} and {city('apopka', 'Apopka')}.</p>"),
        ("From Starke Lake bungalows to post-freeze subdivisions",
         f"<p>Ocoee's oldest housing sits closest to Starke Lake and downtown, dating to the decades after the city's 1925 incorporation, on lots shaded by oaks that have grown for most of a century. Everything built after the 1980s citrus freezes wiped out the surrounding groves tends to sit further out, on wider lots with younger trees and, in a gated community like Wesmere, an architectural-review process that {svc('residential', 'a straightforward lawn conversion')} downtown never had to clear.</p>"
         f"<p>{post('artificial-turf-near-live-oaks-and-palms', 'This article')} goes through what a mature oak canopy actually requires before turf goes in near one.</p>"),
        ("Permits, HOA review and Ocoee's own Building Division",
         f"<p>An Ocoee address answers to the city's own Building Division, not the county's, so 407-905-3104 or the city's online permitting portal is the right first call for a lawn conversion. We haven't built our own permit page for Ocoee's code specifically; {a(PERMITS_ORANGE[0], 'our Orange County page')} covers the unincorporated pockets nearby, and both fall under the same statewide floor set by {a(HB683_ROUTE, 'the state’s May 2026 turf rule')}.</p>"
         f"<p>A Wesmere or other gated-community address adds its own architectural submittal on top of the city's process, which Florida's visibility statute limits differently than city permitting does, covered at {a(HOA_ROUTE, 'our HOA page')}.</p>"),
    ]
    scenario = ("Say you have a 950 sq ft backyard behind a 1994 home near Starke Lake",
                f"<p>Say you have a 950 sq ft backyard behind a 1994 home two streets off Starke Lake, with one corner shaded by a live oak the city's own park planted decades before the house went up next door. At the {price('residential', True)} per sq ft range most Ocoee lawns land in, that yard prices between $9,500 and $15,200, with the number leaning higher if the oak's canopy reaches far enough over the property line to trigger the state's drip-line rule.</p>"
                "<p>The sprinkler zone that used to reach that shaded corner gets capped at the valve box instead of removed, since the state standard bars an in-ground system from watering synthetic turf regardless of what day the rest of the yard waters on. A hose rinse, with or without an automatic shut-off nozzle, takes over from there.</p>")
    faqs = [
        faq("Does a lot near Starke Lake cost more to convert than one in a newer Ocoee subdivision?",
            "Sometimes, mostly because of mature oak roots and tighter access rather than the lot's size. A canopy that's had a century to grow can put more of a small yard inside the drip line than it first appears."),
        faq("Do I need Ocoee's permission before removing sod on an older lake-area lot?",
            "Nothing published treats an older Starke Lake-area lot differently from a newer Ocoee address for a straightforward sod-to-turf swap. Call the Building Division at 407-905-3104 to confirm, since the scope of the specific job can change the answer."),
    ]
    return {"title": "Artificial Grass Installation in Ocoee, FL", "meta": "Synthetic lawn installation in Ocoee, FL: ridge sand base, Starke Lake oaks, gated-community HOA review, market pricing checked September 2026.",
            "h1": "Artificial grass installation for Ocoee lawns", "lede": capsule(f"A residential lawn conversion in Ocoee prices at {price('residential')} a square foot as of September 2026, matching the rest of our Central Florida service area. Upland lots here sit on well-drained Candler and Apopka ridge sand, not the poorly drained muck that the USDA's own Ocoee soil series is named for, and lot age changes the build more than the address does."),
            "sections": sections, "scenario": scenario, "faqs": faqs, "sources": SRC}


# ============================================================== pet
def _pet():
    sections = [
        ("Dog runs in Wesmere and Ocoee's other pond communities",
         f"<p>Wesmere, built mostly between 1991 and the early 2000s around several large fountain ponds south of downtown, packed close to a hundred homes onto cul-de-sac lots with narrower side yards than an older Starke Lake bungalow gets ({ext(WESMERE_INFO[1], 'community details for Wesmere')}). That shape suits a dedicated {svc('pet', 'dog run')} well, fenced along a side property line and built with a deeper drainage base and odor-control infill a plain lawn skips.</p>"
         "<p>A run backing one of Wesmere's ponds still has to clear the state's 10-ft waterbody setback, the same as any other turf near standing water in the community.</p>"),
        ("A hose exemption Ocoee's own water rules already allow",
         f"<p>Ocoee's watering-day schedule limits in-ground irrigation by address, odd numbers on Wednesday and Saturday, even numbers on Sunday and Thursday during Daylight Saving Time, but the city explicitly exempts a hose fitted with an automatic shut-off nozzle from that calendar entirely ({ext(OC_WATER[1], 'Ocoee’s irrigation schedule')}). That's useful for a dog run specifically, since rinsing infill and clearing odor works better on an as-needed basis than on a fixed two-day schedule anyway.</p>"
         f"<p>Once the run's old sprinkler head is capped, per the state's turf standard, that hose exemption is the only watering rule that still applies to the spot at all. {post('how-to-get-dog-urine-smell-out-of-artificial-turf', 'This article')} covers a rinsing routine in more detail.</p>"),
        ("A fenced yard and Florida's visibility statute",
         f"<p>Wesmere and Ocoee's other gated communities run an architectural review for most exterior changes, though we found no published rule naming turf specifically, only a general design-approval process. {a(HOA_ROUTE, 'F.S. 720.3045')} protects an item an HOA can't see from the street or an adjacent lot, so a dog run tucked behind a privacy fence gets that protection even in a community that reviews everything else closely.</p>"
         f"<p>Raising that distinction with the association before submitting paperwork can settle whether a full ARC packet is even necessary. The same statute protects a fenced yard the same way in {city('winter-garden', 'Winter Garden')} or {city('pine-hills', 'Pine Hills')}.</p>"),
    ]
    scenario = ("Say you have a 420 sq ft dog run along a fence line in Wesmere",
                f"<p>Say you have a 420 sq ft dog run planned along a side fence in a Wesmere cul-de-sac, backing one of the community's fountain ponds but staying the state's required 10 feet clear of the water. At the {price('pet', True)} per sq ft pet turf range, that run prices between $5,040 and $6,720, with a coated antimicrobial sand or zeolite adding a modest amount for the odor control a daily-use run needs.</p>"
                "<p>Because the fence blocks the view from both the street and the pond path, F.S. 720.3045 protects the run from an HOA objection even in a community that reviews most other exterior work closely. The pond-facing sprinkler zone gets capped at installation, and a hose with a shut-off nozzle, exempt from Ocoee's watering-day schedule, handles the rinsing from there.</p>")
    faqs = [
        faq("Does Ocoee's watering schedule restrict rinsing a new dog run?",
            "No. The city's odd-and-even schedule governs in-ground irrigation, and it specifically exempts a hose with an automatic shut-off nozzle from those days. A pet turf area doesn't run on an irrigation zone once its head is capped anyway."),
        faq("Does a Wesmere HOA need to approve a dog run it can't see from the street?",
            "Florida's visibility statute doesn't require approval for something a neighbor or the street can't see, a fenced dog run included. Some associations still prefer a courtesy submittal, which can be worth the extra step even when the law doesn't require one."),
        faq("How close can a dog run sit to a Wesmere fountain pond?",
            "At least 10 feet from the ordinary water line, the same statewide setback that applies to any Florida pond or lake, unless a seawall or similar barrier already separates the yard from the water."),
    ]
    return {"title": "Pet Turf & Dog Runs in Ocoee, FL", "meta": "Pet turf and dog run installation in Ocoee, FL: Wesmere pond-community lots, hose watering exemption, HOA visibility rules. Checked September 2026.",
            "h1": "Pet turf and dog runs for Ocoee yards", "lede": capsule(f"Pet turf in Ocoee runs {price('pet')} per square foot as of September 2026, typically {price('pet', True)}. Gated pond communities such as Wesmere favor narrow, fenced side yards for a dog run, and the city's own watering rules already exempt a hose with a shut-off nozzle from its irrigation-day schedule."),
            "sections": sections, "scenario": scenario, "faqs": faqs, "sources": SRC}


# ============================================================== putting
def _putting():
    sections = [
        ("A green for a lot that never had a golf-course view",
         f"<p>Ocoee's housing runs to lake-town bungalows and pond-side subdivisions more than golf-community fairways, so a {svc('putting', 'backyard putting green')} here usually gets carved out of a side yard or a corner of the lawn rather than sized to a view the lot already had. That's a different starting point from a golf-adjacent community, and it means the green's shape often follows the fence line and the sun rather than a fairway's angle.</p>"
         f"<p>A single cup and a modest fringe area cover most of what a lot like this actually needs. A similar side-yard approach fits lots we see in {city('gotha', 'Gotha')} and {city('windermere', 'Windermere')}.</p>"),
        ("Grading a green on the west Orange ridge, away from Ocoee's marsh soil",
         f"<p>The well-drained Candler and Apopka sand under most upland Ocoee lots holds a shaped subgrade better than the poorly drained muck the USDA's own Ocoee soil series describes, which only turns up in floodplain and marsh areas, not under a typical yard ({ext(OCOEE_OSD[1], 'USDA’s Ocoee series description')}; {ext(APOPKA_OSD[1], 'USDA’s Apopka series description')}). That drainage advantage still calls for a rock base compacted in lifts around whatever contour a green needs, since loose ridge sand settles unevenly if it's packed in a single pass.</p>"
         "<p>A raised collar around a cup adds one more contour to grade correctly before the green's carpet goes down.</p>"),
        ("A putting green near a Wesmere fountain pond",
         f"<p>Wesmere's cul-de-sac lots wrap around several large ponds, and a green planned for a pond-facing yard there has to clear the same 10-ft waterbody setback any other turf near standing water does. {post('artificial-turf-glossary', 'This glossary')} covers the terms, fringe, stimp, pile height, worth knowing before sizing a green for a lot with a water view rather than open lawn on every side.</p>"
         "<p>Keeping the green's footprint that far back from the pond edge usually still leaves enough room for a real chipping approach, not just a cup and a token collar.</p>"),
    ]
    scenario = ("Say you have a 280 sq ft green in a side yard backing a Wesmere pond",
                f"<p>Say you have a 280 sq ft putting and chipping green planned for the side yard of a Wesmere home, staying 10 feet clear of the fountain pond it otherwise backs onto. At the {price('putting', True)} per sq ft putting green range, that project prices between $5,040 and $7,000, with the number moving up if the green needs a raised collar and more than one break to read true.</p>"
                "<p>Because the lot sits inside a gated community, a design submittal to the association is worth starting early, even though the green itself likely faces the pond rather than the street. The 10-ft setback from the water line sets the green's back edge before any grading starts, and the existing sprinkler zone in that side yard gets capped once the green is in.</p>")
    faqs = [
        faq("Can a putting green sit right up to a Wesmere pond's edge?",
            "No. The state's 10-ft waterbody setback applies to a fountain pond in a gated community the same way it applies to a lake or canal, unless a seawall or similar barrier already separates the yard from the water."),
        faq("Is a putting green harder to build on Ocoee's ridge sand than elsewhere?",
            "Not harder, just different from flatter ground. The sand drains fast enough that a shaped subgrade holds its contour well once it's compacted in proper lifts, but loose sand packed too quickly can settle unevenly under a green's more detailed grading."),
    ]
    return {"title": "Backyard Putting Greens in Ocoee, FL", "meta": "Backyard putting green installation in Ocoee, FL: Wesmere pond-community setbacks, ridge-sand grading, market pricing checked September 2026.",
            "h1": "Backyard putting greens for Ocoee yards", "lede": capsule(f"Backyard putting greens in Ocoee run {price('putting')} per square foot as of September 2026, typically {price('putting', True)}. Most lots here face a side yard or a pond rather than a golf-course fairway, and the west Orange ridge's well-drained sand holds a contoured subgrade better than the marsh soil the USDA's own Ocoee series describes."),
            "sections": sections, "scenario": scenario, "faqs": faqs, "sources": SRC}


# ============================================================== playground
def _playground():
    sections = [
        ("Play areas in Ocoee's post-freeze growth subdivisions",
         f"<p>Most of Ocoee's housing stock dates to after the 1980s citrus freezes turned surrounding groves into subdivisions, and the city's population nearly doubled between 2000 and 2020, which means a large share of backyards here are young enough to carry a family with kids still using a swing set or a climbing structure ({ext(OC_WIKI[1], 'Ocoee population growth')}). A {svc('playground', 'play area')} on one of these newer lots gets a shock pad sized to the equipment's actual fall height, not a generic thickness.</p>"
         "<p>Wider, newer lots usually leave more clearance around a play structure than an older, tighter downtown yard does, which simplifies where the pad's edge lands.</p>"),
        ("Staying outside the drip line near Starke Lake's oak canopy",
         f"<p>Ocoee's own downtown park land keeps mature oak canopy close to Starke Lake's shoreline, and older residential blocks nearby carry the same kind of decades-old trees. The state's turf rule bars synthetic turf inside a tree's drip line, on that property or an adjacent one, unless a certified arborist certifies no harm, which makes marking the actual canopy edge, not just the trunk, a necessary first step for a play area planned near one of these older lots.</p>"
         f"<p>{post('is-artificial-turf-safe-for-kids-pfas-lead', 'This article')} covers infill choice for a play area, separate from the drip-line question.</p>"),
        ("Shock pad drainage on Ocoee's ridge sand",
         f"<p>Well-drained Candler and Apopka sand under most upland Ocoee lots moves water away from a shock pad faster than flatter, wetter ground would, a different profile from the poorly drained muck the USDA's own Ocoee soil series describes for floodplain areas ({ext(CANDLER_OSD[1], 'USDA’s Candler series description')}). Fast drainage doesn't excuse a loose base, though; a shock pad settles unevenly on uncompacted fill even when the soil underneath sheds water well on its own.</p>"
         f"<p>The same washed, lift-by-lift compaction a plain lawn gets still applies under a play structure's footprint. The same base rules apply to play areas we build in {city('apopka', 'Apopka')} and {city('pine-hills', 'Pine Hills')}.</p>"),
    ]
    scenario = ("Say you have a 220 sq ft play area behind a 2005 home off Clarke Road",
                f"<p>Say you have a 220 sq ft play area planned for the backyard of a 2005 home off Clarke Road, sized around a swing set and slide combination with a 5-foot fall height. At the {price('playground', True)} per sq ft playground turf range, that area prices between $2,640 and $4,180, with the shock pad's thickness set to the equipment's fall height rather than a flat default.</p>"
                "<p>Because the lot sits well clear of any mature tree canopy, the drip-line question doesn't come up the way it would on an older Starke Lake-area lot, and the crew can plan the pad's footprint around the existing fence line without worrying about root zones. The corner's old sprinkler head gets capped at installation, the same as anywhere else on the property.</p>")
    faqs = [
        faq("Does a playground turf project in Ocoee need a permit?",
            "Nothing published treats a residential play area differently from any other synthetic turf project in the city. Call the Building Division at 407-905-3104 before scheduling a crew to confirm what a specific job needs."),
        faq("How do I check whether an old oak near my Ocoee backyard triggers the drip-line rule?",
            "Measure to where the canopy's branches actually end, not the trunk, since a mature tree near Starke Lake or an older block nearby often reaches further than it looks from the yard. A certified arborist's letter is the only way around the setback if a play area has to sit inside that line."),
    ]
    return {"title": "Playground Turf in Ocoee, FL", "meta": "Playground turf installation in Ocoee, FL: shock pad sizing, Starke Lake oak drip-line rule, ridge-sand drainage. Market pricing checked September 2026.",
            "h1": "Playground turf for Ocoee backyards", "lede": capsule(f"Playground turf in Ocoee runs {price('playground')} per square foot as of September 2026, typically {price('playground', True)}. Newer subdivisions built after the 1980s citrus freezes give a play area more clearance from mature trees than an older Starke Lake-area lot does, where the state's drip-line rule comes up more often."),
            "sections": sections, "scenario": scenario, "faqs": faqs, "sources": SRC}


# ============================================================== pool
def _pool():
    sections = [
        ("Turf inside a screened cage in a newer Ocoee subdivision",
         f"<p>Subdivisions built from the 1990s forward, Wesmere and the growth-era neighborhoods off Maguire and Clarke Road included, favor a screened pool cage over an open deck, which leaves a ring of shaded turf between the cage frame and the pool coping that sod rarely holds up in. {svc('pool', 'Turf in that enclosure')} needs a drainage underlay wherever it meets the concrete deck, since the screen blocks some rain while wind-driven storms still reach the area a few times a season.</p>"
         "<p>Glue-down edges against the slab hold up better than a nailed perimeter would inside any screen enclosure, regardless of which Ocoee neighborhood the pool sits in.</p>"),
        ("Older, uncaged pools near Starke Lake",
         f"<p>Closer to downtown, pools built before Ocoee's growth era often went in without a screen enclosure, since cages weren't standard practice on the city's older lake-town lots. Turf around an uncovered pool takes full sun in a way a shaded, caged one never does, pushing the surface toward the upper end of the 120 to 150 degree range and making a lighter-colored or cooling infill worth the added cost right along the deck.</p>"
         f"<p>{post('how-to-make-artificial-grass-look-real', 'This article')} covers product and infill choices that hold up well against pool coping specifically. Older, uncaged pools turn up just as often in {city('winter-garden', 'Winter Garden')} and {city('gotha', 'Gotha')}.</p>"),
        ("Why Ocoee's watering-day rules skip a pool deck",
         f"<p>Ocoee's odd-and-even irrigation schedule governs sprinkler zones, and a pool deck strip usually was never on one of those zones to begin with ({ext(OC_WATER[1], 'the city’s watering schedule')}). Where a head did reach that area, capping it is required under the state's turf standard regardless of the day printed on a water bill, and the pool itself becomes the closest thing to a scheduled rinse the turf gets, since a quick hose-off after a swim covers the same job.</p>"
         "<p>That's one less watering zone to plan around than a full front-yard conversion, where grass on either side of the driveway often still needs its own schedule.</p>"),
    ]
    scenario = ("Say you have a 520 sq ft turf strip inside a screened cage in a 2008 Ocoee home",
                f"<p>Say you have a 520 sq ft strip of turf planned inside the screened pool cage of a 2008 home off Maguire Road, running along two sides of the deck where sod never fully took hold in the shade cast by the enclosure's frame. At the {price('residential', True)} per sq ft range pool-area turf typically lands in, that project prices between $5,200 and $8,320, usually toward the upper half because glue-down edges over concrete take more labor than a nailed perimeter in open ground.</p>"
                "<p>A drainage underlay goes down first wherever the turf meets the slab, since the screen keeps most rain off but a wind-driven storm still reaches that strip a few times a year. Once that layer is in, the rest of the build looks like any other turf job, just anchored to concrete rather than soil at the edges.</p>")
    faqs = [
        faq("Does turf inside an Ocoee pool cage need a different base than an open yard?",
            "Yes, where it meets the concrete deck. A drainage underlay handles water the screen doesn't fully block, and the perimeter gets glued to the slab instead of nailed the way an open-ground edge would be."),
        faq("Is pool-area turf hotter in an older, uncovered Ocoee pool than a caged one?",
            "Generally yes, since a screen enclosure blocks some direct sun an open deck gets all day. A lighter-colored or cooling infill, along with hosing the area down on hot afternoons, both help close that gap."),
        faq("Do I need a permit for turf around a pool in Ocoee?",
            "Nothing published singles out pool-area turf from any other synthetic turf project in the city. Call the Building Division at 407-905-3104 if the pool cage itself is part of the scope, since a structural change can trigger its own review."),
    ]
    return {"title": "Pool & Lanai Turf in Ocoee, FL", "meta": "Turf around pools and inside screened cages in Ocoee, FL: drainage underlay, older uncaged pools near Starke Lake, heat and infill. Checked September 2026.",
            "h1": "Pool and lanai turf for Ocoee homes", "lede": capsule(f"Pool and lanai turf in Ocoee runs the {price('residential')} per square foot residential range as of September 2026, typically {price('residential', True)}. Subdivisions built from the 1990s forward favor a screened cage that needs a drainage underlay at the deck, while older, uncaged pools near Starke Lake take more direct sun."),
            "sections": sections, "scenario": scenario, "faqs": faqs, "sources": SRC}


# ============================================================== repair
def _repair():
    sections = [
        ("What breaks first near Ocoee's oldest oak canopy",
         f"<p>A live oak keeps growing for decades after a lawn goes in, and near Starke Lake's downtown shoreline, a root working its way toward the surface is one of the more common reasons an otherwise sound seam lifts years later. {svc('repair', 'A repair')} in that spot usually means cutting back the offending root, rebuilding a short stretch of base, and re-seaming rather than replacing the whole lawn.</p>"
         "<p>Catching the lift early, while it's still an inch or two, keeps the fix small; left through another rainy season, the same root can work a much longer seam loose.</p>"),
        ("Storm damage along a Wesmere pond edge",
         "<p>Pond-facing lots in Wesmere and other gated communities built around open water take more direct wind than a sheltered downtown block does, which shows up after a tropical storm as a lifted corner where an edge was anchored lightly the first time. The fix is usually a re-anchor along that section rather than a full edge replacement, provided the original nailing or bender-board work held up everywhere else.</p>"
         f"<p>{post('artificial-turf-hurricane-flooding', 'This article')} covers what a harder storm can do beyond a routine windy afternoon.</p>"),
        ("Low-E glass melting a patch on a newer Ocoee lawn",
         f"<p>Homes built during Ocoee's growth era off Maguire and Clarke Road are more likely to carry low-emissivity replacement windows than an older lake-town bungalow, and that glass can reflect enough concentrated sun to soften synthetic turf several feet away. A scorched, oddly shaped patch that doesn't trace back to any obvious cause is worth checking against a nearby south- or west-facing window before assuming a product defect. {svc('repair', 'Repairing')} that kind of damage means cutting out the affected section and patching in a matched piece, not replacing the whole lawn.</p>"
         f"<p>A window film or a repositioned section of turf afterward keeps the same spot from failing twice. The same low-E risk shows up in newer subdivisions around {city('windermere', 'Windermere')} and {city('apopka', 'Apopka')}.</p>"),
    ]
    scenario = ("Say you have 30 linear feet of lifted edge and a scorched patch on a 2010 Ocoee lawn",
                f"<p>Say you have 30 linear feet of lifted edge along a pond-facing fence line and a 5 sq ft scorched patch near a west-facing window on a 2010 Wesmere lawn. That combination gets quoted after photos or a site visit, not a flat per-square-foot rate, since the price depends on how much of the anchoring needs redoing and whether the scorched section can be patched or has to be cut out and replaced.</p>"
                f"<p>For comparison, replacing that same 35 sq ft of turf outright, rather than repairing it, would run roughly $280 to $630 at the {price('residential')} residential range, which is useful context even though the repair itself is priced as a visit rather than a per-foot number. Whichever the crew recommends, the fix stays limited to the damaged sections; the rest of a sound lawn doesn't need to come up at all.</p>")
    faqs = [
        faq("Does homeowners insurance cover turf repair after an Ocoee storm?",
            f"Sometimes, depending on the policy and the cause. {post('does-homeowners-insurance-cover-artificial-turf', 'This article')} covers what's typically included, since wind damage and gradual root intrusion are often treated differently by a carrier."),
        faq("Do I need a permit to repair a section of turf in Ocoee?",
            "Nothing published requires one for a straightforward seam or patch repair, since that scope doesn't usually rise to a building permit. A larger repair involving regrading or drainage work is worth a call to the Building Division at 407-905-3104 first."),
    ]
    return {"title": "Turf Repair in Ocoee, FL", "meta": "Artificial turf repair in Ocoee, FL: oak-root seam lifts near Starke Lake, storm-damaged edges in Wesmere, low-E window melt. Checked September 2026.",
            "h1": "Turf repair for Ocoee lawns", "lede": capsule("Turf repair in Ocoee is quoted after photos or a site visit, not a flat per-square-foot rate, since seam, edge and heat-damage fixes each take a different amount of work. Older lots near Starke Lake's oaks and newer pond-community lawns near low-E windows fail in different ways, and both come up often enough here to plan for."),
            "sections": sections, "scenario": scenario, "faqs": faqs, "sources": SRC}


LOCAL = {
    "residential": _residential(),
    "pet": _pet(),
    "putting": _putting(),
    "playground": _playground(),
    "pool": _pool(),
    "repair": _repair(),
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
