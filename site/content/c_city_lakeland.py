# -*- coding: utf-8 -*-
"""Lakeland, FL (tier 3, Polk County). Hub + residential/pet/putting city x service pages.
Researched September 2026: City of Lakeland Building Inspection Division and Water Utilities pages,
Lakeland Historic Preservation page, Florida Southern College's Frank Lloyd Wright campus history,
USDA official series descriptions for Candler and Basinger, and Florida Demographics for population.
County-level Polk permit/water/soil facts are reused from site/content/c_permits.py and c_counties.py
(same facts and source URLs, fresh sentences here)."""
from _data import CITIES
from _helpers import page, capsule, sec, table, faq, a, svc, city, post, src, ext, price
from _cityservice import cityservice_pages

SLUG = "lakeland"

BUILD = ("City of Lakeland - Building Inspection Division", "https://www.lakelandgov.net/departments/community-economic-development/building-inspection/")
WATER = ("City of Lakeland - Water Utilities, Phase III water shortage restrictions", "https://www.lakelandgov.net/departments/water-utilities/conservation/phase-iii-water-restrictions/")
HIST = ("City of Lakeland - Historic Preservation", "https://www.lakelandgov.net/departments/community-economic-development/historic-preservation/")
SWAN = ("City of Lakeland - 45th annual Lake Morton swan roundup", "https://www.lakelandgov.net/news/posts/2025/october/city-news-blog-city-of-lakeland-to-host-45th-annual-swan-roundup-2025/")
FLW = ("Florida Southern College - Frank Lloyd Wright campus history", "https://www.flsouthern.edu/frank-lloyd-wright-home/history")
POP = ("Florida Demographics - Lakeland population", "https://www.florida-demographics.com/lakeland-demographics")
CANDLER = ("USDA NRCS - official series description, Candler series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/C/CANDLER.html")
BASINGER = ("USDA NRCS - official series description, Basinger series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/B/BASINGER.html")
PA = ("Polk County Property Appraiser - parcel search", "https://www.polkflpa.gov/")

SRC = [BUILD, WATER, HIST, SWAN, FLW, POP, CANDLER, BASINGER, PA, "dep-rule", "fs125572", "fs7203045", "usda-wss"]

# ============================================================== hub
HUB = page(
    "/areas/lakeland/", "city",
    "Artificial Turf Installation in Lakeland, FL (2026)",
    "Artificial turf installers serving Lakeland, FL: the city's own permit office, its 38 lakes' 10-ft setback, and Candler ridge soil, checked September 2026.",
    "Artificial turf and synthetic grass in Lakeland, Florida",
    capsule(f"Lakeland homeowners get a measured yard, a washed-rock base and an installed synthetic lawn priced at {price('residential')} a square foot, the Central Florida range as of September 2026. What's specific to the city is the paperwork: its own Building Inspection Division, its own water utility, and 38 named lakes that each carry the state's 10-foot waterbody setback wherever a yard actually backs onto one."),
    "".join([
        sec("What makes Lakeland different for a turf crew",
            f"<p>Close to {ext(POP[1], 'an estimated 120,000 people')} live inside Lakeland's city limits, Polk County's largest city and, unlike the smaller towns closer to Kissimmee, one that runs almost everything itself: its own Building Inspection Division, its own water utility, and design review for seven local historic districts. That self-sufficiency means the code questions that come up in {city('auburndale')} or {city('lake-alfred')} don't automatically carry over here. At {CITIES['lakeland']['miles']} miles from downtown Kissimmee in a straight line, Lakeland sits at the outer rim of where we work; a job here typically gets grouped with another stop in {city('bartow')} or {city('winter-haven')}, though the price stays the same either way.</p>"),
        sec("Permits: the office that actually reviews a Lakeland yard",
            f"<p>A synthetic-turf job inside the Lakeland city limit goes through the city's own Building Inspection Division at {ext(BUILD[1], '863-834-6012')}, not a Polk County office, with permits filed through its iMS and ePlan systems rather than paper drawings. Nothing in Lakeland's own code addresses synthetic turf by name as far as we've found, which leaves {a('/laws/florida-hb-683/', "the statewide standard that took effect in 2026")} as the only turf-specific rule with real teeth here; the division can confirm that for a specific address faster than we can guess at it. A handful of parcels with a Lakeland mailing address actually sit in unincorporated Polk County, and for those, {a('/laws/permits/polk-county/', "the county's own permit page")} covers what applies, and the {ext(PA[1], "property appraiser's parcel search")} confirms it in under a minute. A subdivision under a homeowners' association layers its own review on top, and {a('/laws/hoa-rules/', 'Florida law limits what that association can restrict')} once turf sits out of view from the street.</p>"),
        sec("Lakeland yard types and what we do differently",
            "<p>Two soil types and two very different building styles make up most of Lakeland. None of it rules out turf; each just changes one detail of the build.</p>"
            + table("Lakeland yard types and what we do differently", ["Yard type", "What's around it", "What changes for the build"],
                    [["Lakefront lot on Hollingsworth, Morton or Mirror", "One of the city's 38 named lakes, sometimes a seawall", "10-ft setback from the ordinary water line, waived where a seawall already separates yard from water"],
                     ["Dixieland or South Lake Morton bungalow", "Local historic district, oak canopy over brick streets", "Base plan stops at the drip line unless a certified arborist signs off"],
                     ["Ridge-adjacent lot toward the city's east or south side", "Excessively drained Candler sand", "Standard washed-rock base, built in two firm lifts since loose sand shifts under a compactor"],
                     ["Newer subdivision near a retention pond", "Platted lot, HOA architectural review", "Turf sample and site plan filed before the crew starts"]],
                    "Every row still starts with the same call to the Building Inspection Division; what differs is what else has to happen first.")),
        sec("Water, the lakes and the setback that follows them",
            f"<p>{ext(WATER[1], "Lakeland's own Water Utilities department")} bills water separately from Lakeland Electric, and both are city-owned rather than run through the county. The Southwest Florida Water Management District has the city under a Phase III shortage order right now: a Lakeland address gets exactly one watering day out of seven, the specific weekday tied to the last digit of the address, and the clock only opens before 4 a.m. or after 8 p.m. on anything under an acre. A capped synthetic lawn skips that schedule entirely, since {src('dep-rule', "the state's turf rule")} bars watering turf through an in-ground system either way. Lakeland's 38 named lakes, including Lake Morton, home to the swans {ext(SWAN[1], 'released there since February 1957')}, Lake Mirror and Lake Hollingsworth, each carry the same 10-foot waterbody setback as a backyard retention pond, measured to the ordinary water line unless a seawall already stands between turf and open water.</p>"),
        sec("Oaks, ridge sand and Lakeland's historic core",
            f"<p>{ext(HIST[1], "Lakeland's seven local historic districts")} cover 1.42 square miles and protect more than 1,600 buildings, many shaded by live oaks that have grown for a century along brick streets in Dixieland and South Lake Morton; {a('/laws/florida-hb-683/', "the state rule")} keeps any synthetic lawn outside a canopy's drip line without a certified arborist's letter. The ground itself splits in two: toward the ridge, soil turns to Candler series, which {ext(CANDLER[1], "USDA's official description")} calls excessively drained with very rapid to rapid permeability, formed in wind-blown and marine sand on slopes mostly under 12 percent, while low ground near a lake margin trends toward the wetter profile {ext(BASINGER[1], 'USDA maps around drainageways and low flats')}. Nearby, {ext(FLW[1], "Florida Southern College's Frank Lloyd Wright campus")}, the largest single-site collection of his buildings anywhere, sits among the older, larger-lot neighborhoods on that same ridge.</p>"),
        "<!--AUTO:city-services-->",
    ]),
    faqs=[
        faq("Does the City of Lakeland require a permit for artificial turf?",
            "Call the Building Inspection Division at 863-834-6012 to confirm for a specific address; we haven't found a Lakeland code section written for synthetic turf on its own, so the state's 2026 standard is the clearest rule that applies. Permits go through the city's iMS and ePlan systems, not Polk County's portal."),
        faq("What are Lakeland's current irrigation days?",
            "One day out of seven, the specific day tied to the last digit of the address, inside the pre-dawn or late-evening windows SWFWMD's current order allows for a lot under an acre. A synthetic lawn with its heads capped skips the schedule entirely."),
        faq("Can turf go right up to Lake Hollingsworth or Lake Morton?",
            "Not inside 10 feet of the water's edge, measured to the ordinary water line, unless the yard already has a seawall or bulkhead between the turf and the lake. That distance comes from the state's 2026 turf rule and applies to any pond, lake or canal in Florida, and the same rule rules out laying turf inside a drainage swale."),
        faq("Do Lakeland's historic districts restrict artificial turf?",
            "The city's historic-district guidelines cover exterior changes visible from the street, not backyard surfaces specifically, so we haven't found a rule naming turf one way or the other. A live oak's drip line is the more common limit in these older, canopied neighborhoods."),
        faq("Searching for the best artificial turf installer near me in Lakeland? Start here.",
            "Ask whether the crew measures the yard in person before quoting a number, what depth of washed crushed rock the bid includes, and whether the answer changes if the parcel turns out to sit in unincorporated Polk County. A contractor who answers all three readily is worth a second call."),
    ],
    sources=SRC, city=SLUG, crumbs=[("Service areas", "/areas/")], crumb="Lakeland",
    related=[("/areas/polk-county/", "Turf rules for all of Polk County"), ("/laws/permits/polk-county/", "Polk County's permit page"),
             ("/areas/auburndale/", "Artificial turf in Auburndale"), ("/areas/winter-haven/", "Artificial turf in Winter Haven"),
             ("/artificial-turf-cost/", "Full turf cost guide"), ("/blog/artificial-turf-near-live-oaks-and-palms/", "Will turf hurt a live oak's roots?")],
)

# ============================================================== residential
_RES_S1 = ("A city split between two very different lots",
           f"<p>{ext(POP[1], 'Close to 120,000 people')} live inside Lakeland's city limits, spread across neighborhoods that don't have much in common with each other. A South Lake Morton or Dixieland lot tends to run narrow and alley-loaded, shaded by an oak canopy that's stood since the 1920s land boom, while a lot in a newer subdivision toward the city's edge is wider, flatter, and governed by an HOA architectural committee instead of a historic-district design review. Both kinds of yards convert to synthetic grass without trouble, but the paperwork and the base plan differ enough that a single answer doesn't cover both. A rental duplex near {ext(FLW[1], "Florida Southern College's Frank Lloyd Wright campus")} sees a foot-traffic pattern closer to what {svc('str', 'a vacation-rental yard')} takes than a quiet family lawn does, and either way {post('does-artificial-grass-increase-home-value-florida', 'the resale question comes up almost as often as the price does')}.</p>")

_RES_S2 = ("Building a base on Candler ridge sand",
           f"<p>Once the ground rises toward Lakeland's ridge neighborhoods, native soil shifts from the flatwoods sand common closer to Kissimmee to Candler series: excessively drained, with permeability {ext(CANDLER[1], "USDA's official series description")} rates as very rapid to rapid, formed in thick wind-blown and marine sand on slopes that mostly run 0 to 12 percent. Ground like that rarely holds water long enough to cause a drainage complaint, which is the opposite problem from a flatwoods lot. The complication runs the other way: loose, fast-draining sand shifts under a plate compactor before it locks into a stable base, so we build the washed crushed-rock layer in two compacted lifts rather than one, and recheck the 1 to 2 percent fall away from the foundation once the first lift is down, since a few inches of stone can flatten a subtle grade on sand this loose; {post('base-under-artificial-turf-florida-sandy-soil', 'the base guide')} goes through the same build on the flatter, wetter sand most of the region sits on instead.</p>")

_RES_S3 = ("Permits and HOA paperwork for a straightforward lawn",
           f"<p>A plain backyard conversion inside the Lakeland city limit goes through the city's own Building Inspection Division at {ext(BUILD[1], '863-834-6012')}, not a Polk County office, and small residential jobs can qualify for the city's Express Permitting track, submitted through its iMS and ePlan systems rather than paper drawings. Lakeland's code doesn't carry a section written for synthetic turf on its own, at least not one we could find, so {a('/laws/florida-hb-683/', "the rule the state adopted in May 2026")} does the real work of governing this kind of build. A call to the division with the exact address is still worth it before assuming that covers everything. A subdivision under an HOA layers its own architectural-review packet on top of that, typically a turf sample, a spec sheet and a site plan, and {a('/laws/hoa-rules/', 'Florida law limits what an HOA can restrict')} once the turf sits behind a fence line, out of view from the street.</p>")

_RES_SC = ("Say you have a 620 sq ft South Lakeland backyard",
           f"<p>Say you have a 620 sq ft backyard behind a 1978 ranch house off Lakeland Highlands Road, the kind of flat, sodded rectangle common through South Lakeland's older subdivisions. At the {price('residential', True)} typical range, that's roughly ${620 * 10:,}–${620 * 16:,} installed, or ${620 * 8:,}–${620 * 18:,} across the full published range depending on access and how much grading the yard needs. Stripping the existing St. Augustine and its root mat is usually the first day's work, then base, seams and infill follow over the next day or two. A yard this size, with no lake frontage and no HOA architectural board to satisfy, is close to the simplest version of this job we see anywhere in Polk County.</p>")

LOCAL_RESIDENTIAL = {
    "title": "Artificial Grass Installation in Lakeland: Ridge to Lake",
    "meta": "Artificial grass installation in Lakeland, FL covers ridge-sand subdivisions and historic lakefront lots alike, at $8–$18 a sq ft installed, September 2026.",
    "h1": "Installing artificial grass on Lakeland's ridge and lakefront lots",
    "lede": capsule(f"Lakeland homeowners get the same {price('residential')} per square foot artificial grass range as the rest of Central Florida, as of September 2026, whether the lot sits on a Dixieland brick street or a subdivision off County Line Road. What changes here is the ground: much of Lakeland sits on excessively drained Candler ridge sand, a sharp contrast from the flatwoods sand common in the towns closer to Kissimmee."),
    "sections": [_RES_S1, _RES_S2, _RES_S3],
    "scenario": _RES_SC,
    "faqs": [
        faq("What's the best artificial grass installer near me in Lakeland?",
            "Ask whether the crew measures the yard in person before quoting a number, what depth of washed crushed rock the bid includes, and whether the price changes if the lot turns out to sit in unincorporated Polk County. A contractor who answers all three without hesitation is worth calling back."),
        faq("Does a lawn conversion in Lakeland need a permit?",
            "Possibly, and the only way to know for a specific address is to call the city's Building Inspection Division directly, since we haven't found a Lakeland code section written for synthetic turf. If the parcel turns out to be unincorporated Polk County, the county's own permit page and Building Division apply instead."),
        faq("Is Candler sand a problem for a residential lawn?",
            "Not for drainage, since it moves water almost as fast as it falls. The tradeoff is compaction: loose ridge sand needs a firmer two-lift base than a wetter flatwoods lot closer to Kissimmee, which is a labor difference, not a design one."),
    ],
    "sources": SRC,
}

# ============================================================== pet
_PET_S1 = ("Small lots near the water, big lots away from it",
           "<p>Lakeland's older lakefront neighborhoods, the blocks ringing Lake Hollingsworth, Lake Morton and Lake Hunter, tend to run narrow and close to the water, which is exactly where a dog owner most wants a fenced run and exactly where the state's setback has the most to say. A run has to stay at least 10 feet from a lake's ordinary water line unless a seawall already separates the yard from open water, and on a lot that's maybe 60 feet wide to begin with, that strip matters. Move a few miles out to a newer subdivision and the math flips: lots run wider, there's rarely a lake in the backyard, and the limiting factor becomes the HOA's fence-and-yard rules more than any waterbody setback.</p>")

_PET_S2 = ("Why a lake-margin dog run drains differently than a ridge one",
           f"<p>Soil under a Lakeland dog run isn't one thing citywide. Up on the ridge, Candler sand drains almost as fast as a hose can fill a bucket, good for a run that gets rinsed daily, though a fully permeable backing and a firm two-lift base still matter for keeping the surface flat under a dog's repeated laps. Down near a lake margin, ground can shift toward something closer to Basinger series, which drains far more slowly, and {ext(BASINGER[1], "USDA's official description")} puts its high-water mark as shallow as 18 inches down for six to nine months of a typical year. A run built there needs its own drain point graded toward daylight, not just toward the house, since the native ground underneath won't pull water away the way ridge sand does; {post('how-to-get-dog-urine-smell-out-of-artificial-turf', 'keeping odor out of a run')} matters more on the slower-draining side of that split.</p>")

_PET_S3 = ("HOA sign-off for a fenced run",
           f"<p>Because a dog run almost always sits behind a fence, {a('/laws/hoa-rules/', "Florida's 2023 law")} covering items not visible from the street or an adjacent lot usually applies, whether the address is in a Dixieland-area historic district or a platted subdivision toward {city('polk-city')}. {ext(HIST[1], "Lakeland's design guidelines")} for its seven local districts cover paint, siding and street-facing changes; they don't call out backyard turf, so a fenced run out of street view is unlikely to trigger that review at all. An HOA-governed lot is a different story, since most architectural committees still ask for a sample and a site plan even for something a neighbor will never see from the sidewalk; {post('coolest-artificial-grass-and-infill-for-florida', 'the infill options for pets')} cover the odor-control side of that packet.</p>")

_PET_SC = ("Say you have a 260 sq ft run near Christina",
           f"<p>Say you have a 260 sq ft dog run along the side yard of a South Lakeland home near Christina, fenced off from the pool cage. At the {price('pet', True)} typical range that's about ${260 * 12:,}–${260 * 16:,} installed, or ${260 * 10:,}–${260 * 18:,} across the full published range once zeolite or an antimicrobial coated sand gets added for odor control. A run that size usually skips the weed barrier entirely, since fabric under pet turf traps urine at the surface instead of letting it filter into the rock, and the crew grades the whole run toward one corner so rinse water has somewhere to go.</p>")

LOCAL_PET = {
    "title": "Pet Turf & Dog Runs in Lakeland, FL",
    "meta": "Pet turf and dog runs in Lakeland, FL: the 10-ft lake setback near Lake Hollingsworth and Morton, and what ridge sand changes, September 2026.",
    "h1": "Pet turf and dog runs near Lakeland's lakes and ridge",
    "lede": capsule(f"A dog run in Lakeland runs the same {price('pet')} per square foot pet-turf range as the rest of Central Florida, typical jobs at {price('pet', True)}, as of September 2026. The detail that changes block to block here is how close the fence line sits to one of the city's 38 named lakes, since that distance decides whether the state's 10-foot waterbody setback comes into play at all."),
    "sections": [_PET_S1, _PET_S2, _PET_S3],
    "scenario": _PET_SC,
    "faqs": [
        faq("How close to Lake Hollingsworth can a dog run go?",
            "At least 10 feet, measured from the lake's ordinary water line to the nearest edge of the turf, unless a seawall or bulkhead already stands between the yard and open water. A property right on the water is still buildable; it just isn't buildable all the way to the shoreline."),
        faq("Does a dog run in a Lakeland historic district need special approval?",
            "The city's design guidelines for its seven historic districts focus on street-facing exterior changes, not backyard surfaces, so a fenced run that isn't visible from the street or a neighboring lot is unlikely to need historic-district sign-off. Confirming with the Building Inspection Division first costs one phone call."),
    ],
    "sources": SRC,
}

# ============================================================== putting
_PUT_S1 = ("Where a green actually fits in Lakeland",
           f"<p>Without a cluster of golf-course communities the way {city('championsgate')} or {city('reunion')} has them, Lakeland's putting greens tend to show up on bigger, older lots instead: an estate-sized property along Lake Hollingsworth Drive with room to shape two or three tiers, or a Lakeland lot from the 1980s or 1990s with a deep backyard and no pool cage eating into the usable space. {ext(FLW[1], "Florida Southern College's Frank Lloyd Wright campus")}, the largest single-site collection of his buildings anywhere, sits close enough to several of these older, larger-lot neighborhoods that a green there is often part of a bigger yard renovation rather than a standalone project. A narrower Dixieland-area lot can still take a small chipping pad; it just won't hold the multi-tier layout a wider yard allows; {post('artificial-turf-glossary', 'the glossary')} explains what a tier and a stimp reading actually mean before that conversation starts.</p>")

_PUT_S2 = ("Shaping a green on ridge sand versus lake-margin ground",
           f"<p>A green's shaped base asks more of the ground under it than a flat lawn does, and Lakeland's two soil types answer that differently. On Candler ridge sand, excavation holds its shape well once compacted, since the material barely retains water and rarely slumps back after a rain. Closer to a lake basin, where the ground trends toward the wetter profile USDA maps around low flats and drainageways, a green's lower tiers need extra attention to drainage, since that native soil holds water far longer after a storm than ridge sand does. Either way the washed-rock base still runs to the top of the state's allowed depth under a green's low points, and {a('/laws/florida-hb-683/', "the state rule")} keeps the whole build outside any live oak's drip line unless an arborist signs off.</p>")

_PUT_S3 = ("Distance, scheduling and what that means for a green",
           f"<p>At {CITIES['lakeland']['miles']} miles from downtown Kissimmee, Lakeland sits about as far out as we go, and a putting green, which takes more layout and shaping time than a flat lawn, gets scheduled with that distance in mind. We typically pair a Lakeland green with another stop the same week, in {city('bartow')} or {city('auburndale')}, rather than sending a crew out for one job alone. That doesn't change the {price('putting')} price range or the build itself; it changes the calendar, and a Lakeland green usually books a little further out than one closer to Kissimmee; {post('backyard-putting-green-cost-florida', 'the cost breakdown')} explains what fills that extra time on a bigger layout.</p>")

_PUT_SC = ("Say you have a 420 sq ft green near Lake Hollingsworth",
           f"<p>Say you have a 420 sq ft green and fringe planned for a Lake Hollingsworth-area backyard with two gentle tiers and four cups. At the {price('putting', True)} typical range that prices around ${420 * 18:,}–${420 * 25:,}, or ${420 * 14:,}–${420 * 30:,} across the full published range depending on how much contouring and fringe the layout needs. A yard that size usually keeps a strip of real lawn or pool deck around the green itself, so the putting surface and its fringe get seamed in as their own piece rather than replacing the whole backyard.</p>")

LOCAL_PUTTING = {
    "title": "Backyard Putting Greens in Lakeland, FL",
    "meta": "Backyard putting greens in Lakeland, FL fit large lake-area and ridge lots rather than golf-community subdivisions, priced $14–$30 a sq ft, 2026.",
    "h1": "Backyard putting greens for Lakeland's larger lots",
    "lede": capsule(f"A backyard putting green in Lakeland runs {price('putting')} per square foot, typical jobs at {price('putting', True)}, the same published Central Florida range as of September 2026 whether the lot backs onto Lake Hollingsworth or sits inland on ridge sand. Lakeland doesn't have Kissimmee's golf-community subdivisions; here, a green is usually a large, established lot's own addition rather than part of a planned golf corridor."),
    "sections": [_PUT_S1, _PUT_S2, _PUT_S3],
    "scenario": _PUT_SC,
    "faqs": [
        faq("Is there room for a putting green on a smaller Lakeland lot?",
            "Usually a chipping pad rather than a full multi-tier green. A narrower historic-district lot in Dixieland or South Lake Morton can still take a compact practice surface; the deeper, tiered layouts we build elsewhere in the county need the bigger backyards more common in Lakeland's newer subdivisions."),
        faq("Do Florida Southern College's oaks affect a nearby green?",
            "Only if the property itself has mature oaks close to the planned green, since the state's drip-line rule applies to any live oak on the lot or next door, not to the college campus specifically. A certified arborist's letter is the only way around it once a canopy overlaps the layout."),
    ],
    "sources": SRC,
}

LOCAL = {"residential": LOCAL_RESIDENTIAL, "pet": LOCAL_PET, "putting": LOCAL_PUTTING}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
