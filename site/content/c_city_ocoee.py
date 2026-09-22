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
                    ["Lot type", "What's typical", "What changes in our approach"],
                    [["Starke Lake-area bungalow (1920s–1950s, oak canopy)", "Small lot, mature oaks close to downtown's lakefront park", "Drip-line check before digging; shallow excavation near root zones"],
                     ["Wesmere or a similar 1990s–early 2000s gated community", "Fountain ponds, an HOA architectural review, cul-de-sac lots", "Turf held 10 ft off pond edges, ARC packet prepared before ordering material"],
                     ["Newer growth-era subdivision off Maguire or Clarke Road", "2000s–present construction, pool cage common, compacted builder fill", "A base built for leftover fill rather than undisturbed native sand"]],
                    f"The {price('residential')} per sq ft range holds across all three; access and review change the bid, not the address.")),
        sec("Who reviews a turf permit inside Ocoee's city limits",
            f"<p>Ocoee took its own permitting fully online at permits.ocoee.org, where a resident can submit, track and pay for a permit without a trip to City Hall on Bluford Avenue, and that's the office an Ocoee lawn conversion goes through, not Orange County's. The city's code doesn't call out synthetic turf specifically, and we haven't put together our own page for Ocoee's ordinances the way we have for the unincorporated county, so 407-905-3104 is the number to call before scheduling anything ({ext(OC_PERMITTING[1], 'Ocoee Permitting')}).</p>"
            + f"<p>An address near the city's edges, particularly toward the growth corridor off Clarke Road, can still turn out to be unincorporated Orange County rather than Ocoee proper; the {ext(ORANGE_PA[1], ORANGE_PA[0])} settles it, and {a(PERMITS_ORANGE[0], PERMITS_ORANGE[1])} covers that office. Either way, the same statewide floor in {a(HB683_ROUTE, 'HB 683 and Rule 62-308.100')} applies, and a gated community's architectural review runs on the separate statute covered on {a(HOA_ROUTE, 'our HOA page')}.</p>"),
        sec("Water rules under the St. Johns River district",
            f"<p>Ocoee sets its own watering days rather than deferring to Orange County Utilities, tied to the last digit of the address: Wednesday and Saturday for odd numbers, Sunday and Thursday for even numbers, Tuesday and Friday for commercial and common-area accounts, that pattern holding through Daylight Saving Time, with irrigation shut off entirely between 10 a.m. and 4 p.m. ({ext(OC_WATER[1], 'the city’s current irrigation schedule')}). Only one of those days survives once Eastern Standard Time starts, though the city carves out an exception a lot of homeowners don't know about: a hose with an automatic shut-off nozzle attached can run on any day of the week.</p>"
            + f"<p>That local calendar sits inside the much larger St. Johns River Water Management District, which covers Ocoee along with most of Orange County outside its southeastern edge ({ext(SJRWMD_ORANGE[1], 'SJRWMD’s Orange County coverage')}). A synthetic lawn skips the calendar entirely once its old sprinkler zone is capped, which the state's standard requires regardless of which utility issued the bill, leaving the hose exemption as the only watering rule that still matters to that patch of yard.</p>"),
        sec("Ocoee's ground, from downtown's oaks to a gated pond community",
            f"<p>The USDA's official Ocoee series, first described near this city, is a poorly drained muck found in floodplains and freshwater marshes, not what sits under a typical yard here ({ext(OCOEE_OSD[1], 'USDA’s Ocoee series description')}). Most upland lots instead sit on the well-drained, sandy Candler and Apopka series common across the west Orange County ridge ({ext(CANDLER_OSD[1], 'USDA’s Candler series description')}; {ext(APOPKA_OSD[1], 'USDA’s Apopka series description')}), though a specific address is worth checking on the {src('usda-wss', 'Web Soil Survey')} rather than assuming either soil profile applies.</p>"
            + f"<p>Starke Lake's western shore anchors downtown, where the city's own park land keeps mature oak canopy close to the water and puts the state's drip-line rule in play on a fair number of jobs there ({ext(OC_DOWNTOWN[1], 'the city’s downtown page')}). South of downtown, Wesmere, a gated community built mostly between 1991 and the early 2000s around several large fountain ponds, put close to a hundred homes on waterfront lots that carry the same 10-ft setback as any other Ocoee pond ({ext(WESMERE_INFO[1], 'community details for Wesmere')}). Searching for the best artificial turf company near you in Ocoee starts with the same two questions either lot type raises: how deep does the base go, and is the crew already thinking about the pond or the oak canopy before the tape measure comes out.</p>"),
        "<!--AUTO:city-services-->",
    ])
    faqs = [
        faq("Does Ocoee require a permit for a synthetic lawn?",
            "As of September 2026 nothing in Ocoee's code names synthetic turf specifically, which means a lawn conversion falls under whatever exterior-work and drainage rules already apply to the property. The Building Division, at 407-905-3104, is the office that decides how those general rules apply to a specific scope of work."),
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
                capsule(f"Ocoee prices a residential lawn install at {price('residential')} a square foot as of September 2026, matching the rest of our service area. Ocoee runs its own Building Division and its own water utility rather than going through the county, and the USDA soil series carrying the city's own name turns out to be marsh muck, not what's under a typical upland yard. Starke Lake and the growth-era subdivisions off Maguire Road both get the same treatment."),
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
        ("Where Florida law, not the HOA, has the last word",
         f"<p>Wesmere's own review process reaches most exterior projects, but it runs up against a limit state law sets rather than the association: {a(HOA_ROUTE, 'F.S. 720.3045')} bars restricting anything that can't be seen from the street or a neighboring parcel, turf included. A dog run set behind a solid fence, out of view of both, falls on the side of that line the association doesn't get to overrule, whatever its own design guidelines say about everything else.</p>"
         f"<p>That's worth raising directly with the board before assuming a full ARC packet is required for a run nobody passing by would ever see. {city('winter-garden', 'Winter Garden')} and {city('pine-hills', 'Pine Hills')} addresses fall under that identical limit, whatever their own associations put in writing.</p>"),
    ]
    scenario = ("Say you have a 420 sq ft dog run along a fence line in Wesmere",
                f"<p>Say you have a 420 sq ft dog run planned along a side fence in a Wesmere cul-de-sac, backing one of the community's fountain ponds but staying the state's required 10 feet clear of the water. At the {price('pet', True)} per sq ft pet turf range, that run prices between $5,040 and $6,720, with a coated antimicrobial sand or zeolite adding a modest amount for the odor control a daily-use run needs.</p>"
                "<p>Because the fence blocks the view from both the street and the pond path, F.S. 720.3045 protects the run from an HOA objection even in a community that reviews most other exterior work closely. The pond-facing sprinkler zone gets capped at installation, and a hose with a shut-off nozzle, exempt from Ocoee's watering-day schedule, handles the rinsing from there.</p>")
    faqs = [
        faq("Does Ocoee's watering schedule restrict rinsing a new dog run?",
            "Not in practice. A capped pet turf area drops off the irrigation calendar entirely, and Ocoee's own hose exemption for a shut-off nozzle covers whatever rinsing still happens by hand, independent of which day the rest of the yard waters on."),
        faq("Does a Wesmere HOA need to approve a dog run it can't see from the street?",
            "Not under state law. F.S. 720.3045 strips an association's ability to restrict anything a neighbor or the street can't actually see, which covers most fenced dog runs. A courtesy heads-up to the board is still a reasonable step even when it isn't legally required."),
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
        ("Play areas across Ocoee's post-grove subdivisions",
         f"<p>Most of the swing sets and climbing structures we see in Ocoee sit in subdivisions built after the 1980s citrus freezes turned old grove land into rooftops, and growth hasn't slowed since: the city's population nearly doubled between 2000 and 2020 ({ext(OC_WIKI[1], 'Ocoee population growth')}). A {svc('playground', 'play area')} on any of those newer lots gets a shock pad matched to the equipment's actual fall height, not a stock thickness, which is what actually keeps a landing zone safe.</p>"
         "<p>Lots in these subdivisions tend to run wider than Ocoee's older lake-town blocks, which usually leaves more room to keep a play structure's footprint clear of the property line.</p>"),
        ("Staying outside the drip line near Starke Lake's oak canopy",
         "<p>Starke Lake's downtown shoreline park has kept its oak canopy intact for generations, and the older residential blocks nearby carry that same kind of long-established tree. Florida's turf rule keeps synthetic grass out of a tree's drip line, on that lot or a neighboring one, unless a certified arborist signs off that the work won't cause harm, so a play area planned near one of these mature oaks needs its canopy's actual edge marked before anything else gets measured.</p>"
         "<p>That step almost never comes up in the newer subdivisions off Maguire or Clarke Road, where the trees haven't had time to spread nearly that far.</p>"),
        ("Uneven fill under a play area on cleared grove land",
         "<p>A lot built directly on cleared citrus grove ground doesn't always compact the same way twice: some pockets carry looser, disturbed soil where a tree's root ball came out, while ground a few feet away was never touched at all. That unevenness matters more under a shock pad than under a plain lawn, since a soft pocket settles differently than the compacted rock around it and can tilt a fall zone that looked level the day it was built.</p>"
         "<p>Checking compaction across the whole footprint before turf goes down, not just at a few spot checks, is what keeps a play area flat through its first few rainy seasons.</p>"),
    ]
    scenario = ("Say a 2005 home off Clarke Road is adding a 200 sq ft play corner",
                f"<p>Say a 2005 home off Clarke Road is adding a 200 sq ft play corner for a swing set with a 5-foot fall height, on a lot cleared for the subdivision after the grove came out decades ago. At the {price('playground', True)} per sq ft playground turf range, that corner prices between $2,400 and $3,800, with the shock pad's thickness set to that fall height rather than a flat number.</p>"
                "<p>Because the lot sits well clear of any surviving canopy, the drip-line question that comes up near Starke Lake doesn't apply here, though the crew still checks compaction carefully across the pad's footprint in case the old grove clearing left an uneven pocket of fill behind. The corner's sprinkler head gets capped at installation either way.</p>")
    faqs = [
        faq("Is a permit required for a play area in Ocoee?",
            "Ocoee hasn't published a rule that treats a backyard play area any differently from other synthetic turf work, so it falls under whatever general exterior permitting already applies. Confirming a specific scope with the Building Division at 407-905-3104 beats guessing."),
        faq("How do I check whether an old oak near Starke Lake triggers the drip-line rule?",
            "A tree's canopy typically reaches well beyond its trunk, so pace off the actual branch spread rather than estimating from where the trunk sits. Without a certified arborist confirming no harm, the play area's footprint has to stay outside that measured line."),
    ]
    return {"title": "Playground Turf in Ocoee, FL", "meta": "Playground turf installation in Ocoee, FL: grove-fill compaction, Starke Lake oak drip-line rule, shock pad sizing. Market pricing checked September 2026.",
            "h1": "Playground turf for Ocoee backyards", "lede": capsule(f"Playground turf in Ocoee runs {price('playground')} per square foot as of September 2026, typically {price('playground', True)}. Post-1980s growth put most play areas on newer, grove-cleared lots rather than Starke Lake's older, oak-shaded blocks, though fill left over from clearing the original citrus grove still needs careful compaction under a shock pad."),
            "sections": sections, "scenario": scenario, "faqs": faqs, "sources": SRC}


# ============================================================== pool
def _pool():
    sections = [
        ("Turf inside a screened cage in Wesmere and its pond-side neighbors",
         f"<p>Wesmere and the other pond-centered communities built from the 1990s forward went in almost entirely with screened cages rather than open decks, which leaves a band of turf between the enclosure's frame and the coping that sod rarely survives in the shade. {svc('pool', 'Turf built into one of these enclosures')} needs a drainage underlay everywhere it meets the concrete, since the screen keeps out a share of ordinary rain while a wind-driven storm still gets through.</p>"
         "<p>Gluing the perimeter to the slab, rather than nailing it the way an open-ground edge would be, is standard practice inside any of these cages regardless of which pond the lot backs.</p>"),
        ("Older, uncaged pools near Starke Lake",
         "<p>Pools that predate Ocoee's growth era, closer to Starke Lake and the older lake-town blocks, usually never got a screen enclosure in the first place, since cages weren't standard on the city's earliest lots. An open deck like that takes full sun for most of the day, unlike a shaded, caged lanai a few streets over in a newer subdivision, and the surface heat that builds up from it is enough to make a lighter or cooling infill worth the extra cost near the coping.</p>"
         f"<p>{post('how-to-make-artificial-grass-look-real', 'This article')} covers infill choices that read well against an open pool's coping.</p>"),
        ("A pool deck strip and Ocoee's own hose exemption",
         f"<p>A pool deck strip was rarely on a sprinkler zone to begin with, so Ocoee's odd-and-even watering calendar was mostly irrelevant to that patch of yard before turf ever entered the picture. Where a head genuinely did reach the area, capping it is required by the state's rule regardless of the day printed on a water bill, and the city's own hose exemption for a shut-off nozzle becomes the only watering rule that could still apply, though a pool deck rarely needs the extra rinse a dog run or a full lawn does.</p>"
         "<p>The pool itself ends up doing more rinsing than any hose would, since a splash after a swim reaches that strip more often than a scheduled watering day ever would.</p>"),
    ]
    scenario = ("Say a Wesmere home is adding 450 sq ft of turf around its screened pool deck",
                f"<p>Say a Wesmere home near one of the community's fountain ponds is adding 450 sq ft of turf around its screened pool deck, filling in a band that's stayed patchy since the original sod couldn't handle the cage's shade. At the {price('residential', True)} per sq ft range, the project prices between $4,500 and $7,200, with the number climbing when the crew has to glue the perimeter to the slab instead of anchoring it in open soil.</p>"
                "<p>A drainage underlay goes down first anywhere the turf meets concrete, since the screen keeps most rain out but a hard summer storm still finds its way in. Ten feet of clearance from the pond itself isn't a factor for this particular strip, since the pool deck already sits well back from the water.</p>")
    faqs = [
        faq("Does turf inside an Ocoee pool cage need a different base than an open yard?",
            "Just at the edges. Concrete gets a drainage layer underneath and a glued perimeter, while open soil elsewhere in the same yard still gets the usual compacted rock base and a nailed or bordered edge."),
        faq("Is pool-area turf hotter in an older, uncovered Ocoee pool than a caged one?",
            "Yes, in most cases, since an open deck near Starke Lake takes direct sun all day that a screened Wesmere-style cage partly blocks. A cooling infill and a regular hose rinse both help close that difference."),
        faq("Do I need a permit for turf around a pool in Ocoee?",
            "Turf itself doesn't trigger anything beyond Ocoee's usual synthetic-turf permitting, though changing the cage structure is a separate scope. Call the Building Division at 407-905-3104 if both are part of the same project."),
    ]
    return {"title": "Pool & Lanai Turf in Ocoee, FL", "meta": "Turf around pools and inside screened cages in Ocoee, FL: Wesmere pond-side cages, older uncaged pools near Starke Lake, hose rules. Checked September 2026.",
            "h1": "Pool and lanai turf for Ocoee homes", "lede": capsule(f"Pool and lanai turf in Ocoee runs the {price('residential')} per square foot residential range as of September 2026, typically {price('residential', True)}. Wesmere's pond-side screened cages need a drainage underlay at the deck the way any enclosure does, while older, uncaged pools near Starke Lake take the Florida sun with nothing blocking it."),
            "sections": sections, "scenario": scenario, "faqs": faqs, "sources": SRC}


# ============================================================== repair
def _repair():
    sections = [
        ("Oak roots along Starke Lake's downtown shoreline",
         f"<p>Starke Lake's downtown shoreline park has carried the same mature oak canopy for generations, and the residential blocks nearby inherited trees old enough that a root can still be pushing toward the surface years after a lawn was installed. {svc('repair', 'A repair')} in one of these spots usually starts with tracing the root back far enough to cut it cleanly, then rebuilding the short stretch of base it disturbed before re-seaming.</p>"
         "<p>Catching a small lift near one of these oaks early keeps the fix to a single section rather than a running seam problem the length of the yard.</p>"),
        ("Uneven settling on lots cleared from old citrus groves",
         "<p>A subdivision built directly on cleared grove land, common across Ocoee from the 1980s freezes onward, doesn't always compact evenly: a spot where a mature citrus tree's root ball was pulled can settle differently for years afterward than ground nearby that was never disturbed. A section of lawn that develops a shallow dip with no storm or obvious cause to explain it is worth checking against that history before assuming a base failure elsewhere in the yard.</p>"
         "<p>The fix is usually limited to re-leveling that one pocket rather than reworking the whole lawn's base.</p>"),
        ("Low-E glass in the growth-era subdivisions off Maguire and Clarke Road",
         f"<p>Homes built during Ocoee's growth era are more likely to carry low-emissivity replacement windows than an older lake-town bungalow, and that glass can concentrate enough reflected sun to soften synthetic turf several feet from the house. A scorched patch with an odd, sharp-edged shape and no other explanation is worth checking against a nearby south- or west-facing window before assuming a product defect.</p>"
         f"<p>{svc('repair', 'Fixing')} that kind of damage means cutting out the affected section and patching in matched material, and a window film afterward keeps the same spot from failing a second time.</p>"),
    ]
    scenario = ("Say a 1994 Ocoee lawn has a shallow settled dip and a scorched patch near a window",
                "<p>Say a 1994 lawn near Starke Lake has developed a shallow, 15 sq ft dip where an old grove tree once stood, plus a 5 sq ft scorched patch near a west-facing window added during a later renovation. Both get priced after the crew looks at the site, since a settled dip calls for re-leveling the base while a scorched patch calls for cutting out and replacing turf, two different scopes with two different costs.</p>"
                f"<p>Replacing that combined 20 sq ft outright, instead of repairing either issue, would run somewhere between $160 and $360 at the {price('residential')} residential range, a useful reference point even though neither repair here is actually priced by the square foot. Most jobs this size stay well under a full lawn's worth of work either way.</p>")
    faqs = [
        faq("Does homeowners insurance cover turf damage in Ocoee?",
            f"Coverage depends on the carrier and the cause more than the city. {post('does-homeowners-insurance-cover-artificial-turf', 'This article')} breaks down how a policy typically treats sudden damage, like wind, against gradual issues like root intrusion or ground settling."),
        faq("Do I need a permit to repair turf in Ocoee?",
            "A standard seam, patch or re-leveling job doesn't usually require its own permit, though nothing published states that outright. Work that involves regrading a larger area is the kind worth a call to 407-905-3104 before starting."),
    ]
    return {"title": "Turf Repair in Ocoee, FL", "meta": "Artificial turf repair in Ocoee, FL: oak-root lifts near Starke Lake, grove-fill settling, low-E window melt off Maguire and Clarke Road. Checked September 2026.",
            "h1": "Turf repair for Ocoee lawns", "lede": capsule("An oak-root lift near Starke Lake and a settled dip on old grove land need two different fixes in Ocoee, so pricing follows a look at the site rather than a flat per-square-foot number. Both problems come up often enough here to plan for, and the number on a quote tracks the visit, not a published range."),
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
