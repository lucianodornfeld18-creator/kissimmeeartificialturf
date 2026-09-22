# -*- coding: utf-8 -*-
"""Winter Park, FL (tier 2). Researched September 2026: City of Winter Park Building & Permitting
Services, Water & Wastewater Utilities and Electric Utility (own city pages), Urban Forestry and
Historic Preservation (own city pages), the Winter Park Chain of Lakes, a secondary comparison of
Florida artificial-turf ordinances (Belle Isle, FL, already used for the Orlando permit page) for
Winter Park's own turf code, U.S. Census QuickFacts, and USDA official series descriptions for the
Candler and Apopka ridge soils. Orange County permit, water and soil facts are reused from
c_permits.py and c_counties.py (facts and URLs, not sentences)."""
from _data import CITIES
from _helpers import page, capsule, sec, table, faq, a, svc, city, post, src, ext, price
from _cityservice import cityservice_pages

SLUG = "winter-park"
MILES = CITIES[SLUG]["miles"]

WP_BUILD = ("City of Winter Park — Building & Permitting Services", "https://cityofwinterpark.org/departments/building-permitting-services/")
WP_PORTAL = ("City of Winter Park — Click2GovBP permit portal", "https://epay.cityofwinterpark.org/Click2GovBP/index.html")
WP_WATER = ("City of Winter Park — Water & Wastewater Utilities", "https://cityofwinterpark.org/departments/water-wastewater-utilities/")
WP_RESTRICT = ("City of Winter Park — current Florida water restrictions", "https://cityofwinterpark.org/docs/departments/water-wastewater-utilities/water-conservation-information/florida-water-restrictions.pdf")
WP_ELECTRIC = ("City of Winter Park — Electric Utility", "https://cityofwinterpark.org/departments/electric-utility/")
WP_FORESTRY = ("City of Winter Park — Urban Forestry", "https://cityofwinterpark.org/departments/parks-recreation/urban-forestry/")
WP_HISTORIC = ("City of Winter Park — Historic Preservation", "https://cityofwinterpark.org/departments/planning-zoning/historic-preservation/")
WP_LAKES = ("City of Winter Park — Lakes General Information", "https://cityofwinterpark.org/departments/natural-resources-sustainability/lakes/lakes-general-information/")
WP_CENSUS = ("U.S. Census Bureau QuickFacts — Winter Park city, Florida", "https://www.census.gov/quickfacts/fact/table/winterparkcityflorida")
TURF_COMPARE = ("City of Belle Isle, FL — comparison of local Florida artificial turf ordinances", "https://www.belleislefl.gov/sites/default/files/fileattachments/community/page/9922/artificial_turf_comparisons_of_local_florida_ordinances_-_sheet1.pdf")
CANDLER_OSD = ("USDA NRCS — official series description, Candler series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/C/CANDLER.html")
APOPKA_OSD = ("USDA NRCS — official series description, Apopka series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/A/APOPKA.html")
ORANGE_PA = ("Orange County Property Appraiser — parcel search", "https://ocpafl.org/")
OC_PERMIT = ("Orange County Permitting Services & Building Safety, Fast Track Online Services", "https://fasttrack.ocfl.net/OnlineServices/")
OC_CH24 = ("Orange County Code, Chapter 24, Municode Library", "https://library.municode.com/fl/orange_county/codes/code_of_ordinances?nodeId=PTIIORCOCO_CH24LABUOPSP")
SJRWMD_OC = ("St. Johns River Water Management District — Orange County", "https://www.sjrwmd.com/district-counties/orange-county/")

SRC = ["dep-rule", "fs125572", "hb683", "fs7203045", "usda-wss", "census-acs",
       WP_BUILD, WP_PORTAL, WP_WATER, WP_RESTRICT, WP_ELECTRIC, WP_FORESTRY, WP_HISTORIC, WP_LAKES, WP_CENSUS,
       TURF_COMPARE, CANDLER_OSD, APOPKA_OSD, ORANGE_PA, OC_PERMIT, OC_CH24, SJRWMD_OC]

# ============================================================== hub
HUB = page(
    "/areas/winter-park/", "city",
    "Artificial Turf in Winter Park, FL (2026 Guide)",
    "Synthetic turf installation, permits, the tree canopy ordinance and the Chain of Lakes setback for Winter Park, FL, checked September 2026.",
    "Turf installation and local rules for Winter Park, FL",
    capsule(f"A Winter Park lawn conversion prices the same {price('residential')} a square foot as anywhere else we work, as of September 2026, about {MILES} miles from downtown Kissimmee. What's different here is the paperwork: Winter Park's own Land Development Code reportedly already addresses synthetic turf directly, and a tree canopy ordinance shapes where a lawn can actually go."),
    "".join([
        sec("Winter Park's own turf rule, on top of the state's",
            f"<p>Winter Park's Building & Permitting Services, at 401 South Park Avenue, answers permit questions at {ext(WP_BUILD[1], '(407) 599-3237')} and takes applications through the {ext(WP_PORTAL[1], 'Click2GovBP portal')}. That much is a straightforward call. What makes Winter Park different from the rest of our service area is that its own code, not just the state's, already has language written for synthetic turf, according to {ext(TURF_COMPARE[1], 'a published comparison of Florida artificial-turf ordinances')} we checked in September 2026; a live pull of the Municode text wasn't available during this research pass, so treat the specifics below as a secondary read, not a quote of the current code.</p>"
            + "<p>That comparison describes two paths: an installation built as pervious, with a woven backing rated at 30 inches an hour of uniform permeability and an engineered layer underneath to hit that number, or one treated as impervious, which skips the permeability test but counts fully against the lot's impervious coverage and has to retain the first inch of runoff on site. Either path reportedly needs a permit, and the property owner signs a recorded agreement to keep the turf maintained, repair or replace it if it stops draining as designed, and cover the city for any drainage trouble that follows.</p>"
            + f"<p>Since May 19, 2026, {src('dep-rule', 'Rule 62-308.100')} sets a ceiling under all of this on a single-family lot of an acre or less: a local permeability standard can't ask for more than 10 inches an hour, which is looser than the 30-inch figure the comparison attributes to Winter Park's pervious path, and the state's drip-line rule carries a certified-arborist exception that the older city language, as summarized, doesn't appear to include. Which number a reviewer applies to a covered lot in September 2026 is a question for Building & Permitting Services, not something this page can settle.</p>"
            + f"<p>Not every address with a Winter Park mailing address sits inside the city limits, since a handful of surrounding pockets are unincorporated Orange County instead. The {ext(ORANGE_PA[1], 'Orange County Property Appraiser')} shows the taxing jurisdiction for a specific parcel, and our {a('/laws/permits/orange-county/', 'Orange County permit page')} covers what applies if the lot turns out to be outside city lines.</p>"),
        sec("Water and power both come from the city, not a district",
            f"<p>Winter Park runs {ext(WP_WATER[1], 'its own Water & Wastewater Utilities department')}, serving roughly 23,000 potable accounts inside the city and a few unincorporated pockets around it, plus a reclaimed-water system for irrigation. The current schedule, published on the city's own {ext(WP_RESTRICT[1], 'water restriction page')}, limits odd addresses to Saturday and even addresses to Sunday, both between 4 p.m. and 10 a.m., with non-residential properties on Tuesday; nothing waters between 10 a.m. and 4 p.m., and a new lawn gets a 30-day exemption. A synthetic lawn skips that calendar entirely the day its irrigation heads get capped, a step the state's May 2026 standard makes mandatory rather than optional.</p>"
            + f"<p>Winter Park also owns its electric grid, a setup few Florida cities still run: the city bought the system from the old investor-owned utility in 2003 and has been {ext(WP_ELECTRIC[1], 'undergrounding lines toward a citywide target of 2030')} ever since. It doesn't change a turf bid directly, but it's one more sign that permitting and utility questions here go to city hall first, not a county office or a private power company.</p>"),
        sec("A tree canopy the city tracks, and a drip line that follows it",
            f"<p>The {ext(WP_FORESTRY[1], 'Urban Forestry Division')} counts more than 75,000 trees on private land inside the city and another 25,000 in the public rights-of-way, and it runs a tree preservation ordinance alongside a tree-banking program that lets a removed canopy tree be offset with new plantings elsewhere. A canopy that tracked matters more here than in a newer subdivision: the comparison document above describes Winter Park's own turf rule as barring an install under a tree's canopy outright, a stricter starting point than the state's drip-line rule, which allows a certified arborist to sign off on turf closer to the trunk.</p>"
            + "<p>On a lot with a mature live oak, that gap between the two rules is worth raising before a crew measures anything. Whether the city still enforces the older canopy language as written, or defers to the arborist exception the state now guarantees, is exactly the kind of question Building & Permitting Services can answer for a specific address faster than a general page can.</p>"),
        sec("Historic districts built the neighborhoods, not the lawns",
            f"<p>Winter Park carries four National Register districts: the Downtown Winter Park Historic District, running along Park Avenue with buildings dated 1882 to 1965; the Interlachen Avenue Historic District; the College Quarter Historic District, designated in 2003; and Virginia Heights East, designated in 2010, plus the Hannibal Square area's own history as a historic Black neighborhood. Design review inside those boundaries, per the city's own {ext(WP_HISTORIC[1], 'Historic Preservation FAQ')}, weighs height, materials, roofline, massing and setback against the surrounding block; nothing in that published guidance addresses ground cover or a lawn's surface material, so a design-review packet isn't where a turf question gets answered here.</p>"
            + f"<p>Most of the housing near those districts predates 1965, sitting on lots narrow enough that a live oak's canopy often reaches the property line on both sides. Rollins College, on Lake Virginia's north shore, anchors a slightly younger ring of homes around it, and newer infill keeps filling gaps on streets that are otherwise a century old.</p>"),
        sec("Six lakes, one canal system, and the 10-foot line",
            f"<p>The Winter Park Chain of Lakes ties together Lake Virginia, Lake Mizell, Lake Osceola, Lake Maitland, Lake Nina and Lake Minnehaha through a set of man-made canals, {src('dep-rule', 'per the city')}'s own {ext(WP_LAKES[1], 'lakes information page')}; Lake Maitland carries the chain into {city('maitland', 'Maitland')} at its lower end. A synthetic lawn on any of those shorelines has to stay 10 feet back from open water under the state's May 2026 standard, though enough lots on the chain already carry a seawall or bulkhead that the exception ends up applying more often than the plain 10-foot rule alone would suggest.</p>"
            + "<p>A canal-front lot often stacks that setback on top of the drip-line question, since older lakefront parcels here tend to carry both a seawall and a mature oak within a few feet of each other.</p>"),
        sec("Growth on a ridge of sand that drains on its own",
            f"<p>Winter Park's population was 29,795 at the 2020 census and about 30,274 in the Census Bureau's 2019–2023 estimate, {ext(WP_CENSUS[1], 'a modest gain')} on a city that was mostly built out decades ago. The ground under it is different from the flatwoods soil that covers so much of Central Florida: USDA maps this part of the Orange County ridge to the Candler and Apopka series, {ext(CANDLER_OSD[1], 'excessively to well drained sand')} formed in thick wind-blown and marine deposits, closer to what you'd find on the Lake Wales Ridge than to the wetter Myakka and Immokalee soils common around Kissimmee.</p>"
            + "<p>Fast-draining sand doesn't excuse the base. A washed, open-graded rock layer still keeps the surface level and stops the turf from telegraphing every soft spot in the native ground beneath it, whether that ground already drains well or not.</p>"),
        "<!--AUTO:city-services-->",
    ]),
    faqs=[
        faq("Does Winter Park have its own artificial turf ordinance, separate from the state rule?",
            "As we read a secondary comparison of Florida ordinances checked September 2026, yes: Winter Park's code distinguishes a pervious install from an impervious one, sets its own permeability number for the pervious path, and requires a recorded maintenance agreement. We couldn't pull the live Municode text during this research pass, so confirm current wording with Building & Permitting Services before finalizing a design."),
        faq("Do I need a permit either way in Winter Park?",
            "Both paths described in that comparison require one. Call Building & Permitting Services at (407) 599-3237 or use the Click2GovBP portal before scheduling a crew, since the paperwork differs depending on whether the install is designed as pervious or impervious."),
        faq("What happens if a live oak's canopy covers the spot I want turfed?",
            "Two rules can apply at once. The state standard keeps turf outside a tree's drip line unless a certified arborist signs off, while the older local language described in our research bars an install under a canopy outright with no stated exception. Ask the city directly which one a reviewer is applying to a specific lot before you commit to a layout."),
        faq("What should the best artificial turf installer near you in Winter Park already know before quoting?",
            "Whether the bid accounts for the city's permeability path or the impervious one, since that changes the paperwork and possibly the base design, and whether the crew has checked your lot against both the drip-line rule and, if you're on the Chain of Lakes, the 10-foot setback. A written quote that spells out base depth, infill type and which permit path it assumes is worth more than one that doesn't mention either."),
        faq("Does the 10-foot lake setback still apply if my seawall is old or partly broken down?",
            "The state rule's exception is tied to having a seawall or bulkhead in place, not to its condition, but a wall that's failing is a separate structural problem worth a look regardless of what goes on the yard above it. If there's any doubt about whether a structure still counts, that's a question for the city rather than an assumption to build a layout around."),
    ],
    sources=SRC, crumbs=[("Service areas", "/areas/")], crumb="Winter Park", city=SLUG,
    related=[("/areas/orange-county/", "Artificial turf in Orange County"), ("/laws/permits/orange-county/", "Orange County permit rules (Winter Park runs its own code)"),
             ("/areas/maitland/", "Artificial turf in Maitland"), ("/areas/orlando/", "Artificial turf in Orlando"), ("/artificial-turf-cost/", "Full turf cost guide")])

# ============================================================== local (city x service)
LOCAL = {
    "residential": {
        "title": "Artificial Grass Installation in Winter Park, FL",
        "meta": "Artificial grass installation in Winter Park, FL runs $8–$18 per sq ft. What the city's own turf code and tree canopy rule mean for a 1920s-to-1960s lot.",
        "h1": "Converting a Winter Park lawn to synthetic turf",
        "lede": capsule(f"A residential lawn conversion in Winter Park runs {price('residential')} per square foot installed as of September 2026, most jobs landing between {price('residential', True)}. What changes the plan here more than the price is the lot itself: a city with its own turf code, a tracked tree canopy, and, on many streets, homes built before 1965 on lots narrower than a newer subdivision's."),
        "sections": [
            ("What a pre-1965 lot changes about the layout",
             f"<p>A big share of Winter Park's housing stock sits inside or near the {a('/laws/hoa-rules/', 'Downtown Winter Park')}, Interlachen Avenue, College Quarter or Virginia Heights East historic districts, all built out mostly between the 1920s and the 1960s. Design review there looks at the house, not the yard, so a lawn conversion typically doesn't need architectural sign-off the way a new addition would. What it does run into more often than a 1990s subdivision is a mature live oak close to the house, planted decades before anyone thought about a synthetic surface underneath its branches.</p>"
             + f"<p>That combination, an old lot and an old tree, is why the drip-line question comes up on a residential job here more than it does in {city('altamonte-springs', 'Altamonte Springs')} or a newer part of the county. Working around a canopy usually means a smaller turfed footprint than the lot's total square footage suggests, with the remainder handled some other way.</p>"),
            ("Reading Winter Park's own permeability path",
             f"<p>Beyond the state's {a('/laws/florida-hb-683/', 'May 2026 turf standard')}, a secondary comparison of Florida ordinances checked this September describes Winter Park's own code as splitting a residential install into a pervious path, built to a stated 30-inch-per-hour permeability rate with an engineered layer underneath, and an impervious path that skips that rate but counts fully toward the lot's impervious coverage limit. Which path a specific quote assumes changes what gets submitted with the permit application, so it's worth asking a bidder directly rather than assuming.</p>"
             + "<p>The same source describes a recorded maintenance agreement as part of the deal here, something we haven't seen described for any other city in this network. A homeowner signing that agreement is committing to keep the lawn draining and looking as designed, not just to a one-time install.</p>"),
            ("What Candler sand means for the base under a residential yard",
             f"<p>{ext(CANDLER_OSD[1], 'USDA maps much of Winter Park')} to the Candler and Apopka series, excessively to well drained ridge sand that behaves differently than the flatwoods soil under most Central Florida yards we describe elsewhere on this site. It drains fast on its own, which sounds like an advantage, but a washed crushed-rock base still does the job of holding the surface level; loose ridge sand shifts under foot traffic in a way a compacted rock layer doesn't. {post('base-under-artificial-turf-florida-sandy-soil', 'This article')} goes through why the base matters more than the native soil's drainage rate either way.</p>"),
        ],
        "scenario": ("A Comstock-area bungalow with an oak out front",
                     f"<p>Say you have a 1948 bungalow near the Downtown district with a 620 sq ft backyard, a live oak whose canopy covers roughly a third of it, and a side yard too narrow for a wheelbarrow to pass a fence post. At {price('residential', True)} per square foot for the turfed area alone, a straightforward 400 sq ft install outside the drip line runs about $4,000 to $6,400, before the oak's canopy is factored back in as a no-turf zone unless an arborist signs off on going closer.</p>"
                     + f"<p>Getting an arborist's letter first, before ordering material, is the difference between pricing the job once and re-measuring it after a crew finds out mid-install that the layout has to shrink. The same logic applies on a lot near {city('orlando', 'Orlando')} or {city('casselberry', 'Casselberry')} with an old oak of its own, not just here.</p>"),
        "faqs": [
            faq("Does a historic district review add time to a residential turf job in Winter Park?",
                "Not usually for the turf itself, since published design review focuses on the structure, not the lawn surface. What can add time is confirming which of the city's two permeability paths applies and getting an arborist's sign-off if a canopy is close to the layout."),
            faq("Is Winter Park's sandy ridge soil actually better for a lawn conversion?",
                "It drains faster than the flatwoods soil common elsewhere in our service area, but that doesn't replace a compacted base. The rock layer is what keeps the surface flat under traffic, on any soil type."),
        ],
        "sources": SRC,
    },
    "pet": {
        "title": "Pet Turf & Dog Runs for Winter Park Yards",
        "meta": "Pet turf and dog run installation in Winter Park, FL runs $10–$18 per sq ft. Zero-lot-line side yards near Rollins College and the city's own water rules.",
        "h1": "Pet turf for narrow Winter Park yards",
        "lede": capsule(f"Pet turf in Winter Park runs {price('pet')} per square foot as of September 2026, typically {price('pet', True)}, and most jobs here go into a fenced side or back yard behind a home built before Rollins College's surrounding blocks filled in. A narrow lot changes the layout for a dog run more than the price does."),
        "sections": [
            ("Dog runs on lots that were never platted wide",
             f"<p>Streets near Rollins College and the older grid closer to Park Avenue carry some of the narrowest side yards in our service area, a legacy of lots platted for a 1920s or 1930s cottage rather than a modern setback pattern. A side-yard dog run here often has to run the full depth of the property in a strip under six feet wide, which changes how a crew stages material and where the flush-out zone for rinsing goes. A wider backyard, if the lot has one, usually takes the run instead once the side yard's width rules it out.</p>"
             + f"<p>{svc('pet', 'Pet turf systems')} built for that kind of narrow footprint lean on the same fast-draining infill choices as a wider yard, just packed into less room, which is more a layout problem than a materials one.</p>"),
            ("Why the city's own irrigation rule barely touches a dog run",
             f"<p>Winter Park runs its own water utility rather than buying through a district, and the current restriction limits odd addresses to Saturday and even addresses to Sunday, both outside the 10 a.m.-to-4 p.m. window. None of that reaches a pet turf area once the zone's heads are capped, which the state's May 2026 standard requires outright. What actually keeps a dog run working is the rinse habit that replaces irrigation: a hose pass to settle infill and clear odor, done on whatever schedule the dog's use of the yard calls for, not on the city's watering calendar.</p>"),
            ("Zeolite and coated sand near a protected canopy",
             f"<p>A pet yard shaded by a live oak, common on the older lots near the historic districts, holds odor differently than one in full sun, since shade slows how fast a hose rinse dries. Zeolite or a coated silica infill, both allowed under the state's natural-material standard, work with that shade rather than against it by trapping ammonia until the next rinse instead of relying on sun exposure to help. {post('how-to-get-dog-urine-smell-out-of-artificial-turf', 'This article')} covers what each infill choice actually does once a dog has used the yard for a season.</p>"),
        ],
        "scenario": ("A dog run behind a Virginia Heights cottage",
                     f"<p>Say you have a 200 sq ft side-yard strip behind a 1950s cottage near Virginia Heights East, five feet wide and running the depth of the lot, fenced for two dogs. At {price('pet', True)} a square foot, that comes to roughly $2,400 to $3,200 installed, with zeolite infill adding another $100 to $200 on top for a run this size. A wider lot near {city('winter-springs', 'Winter Springs')} or {city('altamonte-springs', 'Altamonte Springs')} might carry that same run in a backyard instead of a side strip, which changes the access plan more than the total.</p>"
                     + "<p>Either way, the flush-out zone at the low end of the run matters as much as the infill choice, since that's where rinse water and whatever it carries actually exits the yard.</p>"),
        "faqs": [
            faq("Can a pet turf run go inside a Winter Park historic district without design review?",
                "Published historic design review covers architectural elements, not lawn surfaces, so a pet turf run in a side or back yard typically isn't the kind of change that review addresses. Confirm with Historic Preservation if the run involves visible fencing or hardscape changes at the street."),
            faq("Does zeolite infill need more rinsing under a shaded oak canopy than in full sun?",
                "Shade slows drying, so a shaded run can hold odor a bit longer between rinses than one in full sun, though the infill itself works the same way either spot. Rinsing on a schedule tied to actual use, rather than a fixed calendar, handles both conditions."),
            faq("Is there a minimum side-yard width for a dog run in Winter Park?",
                "Nothing published sets a minimum specific to turf. A run under three feet wide gets difficult for a crew to compact and seam properly, which is a practical limit more than a coded one."),
        ],
        "sources": SRC,
    },
    "putting": {
        "title": "Backyard Putting Greens in Winter Park, FL",
        "meta": "Backyard putting green installation in Winter Park, FL runs $14–$30 per sq ft. Larger Chain of Lakes lots and the drip-line rule near mature oaks.",
        "h1": "Putting greens on larger Winter Park lots",
        "lede": capsule(f"Expect {price('putting')} a square foot for a backyard putting green in Winter Park as of September 2026, with {price('putting', True)} covering most jobs. The lots that suit a green best here tend to be the larger, older parcels near the Chain of Lakes rather than the narrower cottage lots closer to downtown."),
        "sections": [
            ("Where a green actually fits on an older Winter Park lot",
             f"<p>A putting green needs open, flat ground with room to contour a few feet of fall for the roll, which rules out most of the narrow side-yard lots near Rollins College but fits comfortably on the wider parcels around Interlachen Avenue and the lake-adjacent streets, where a backyard can run 80 feet deep or more. The Winter Park Country Club's clubhouse, a National Register building near Interlachen, sits in that same stretch of larger, older lots, a rough marker for where lot sizes open up enough for a green without crowding the rest of the yard.</p>"),
            ("Oak canopy and a contoured green don't mix well",
             f"<p>Contouring a green means shaping the subgrade with real precision, and a live oak's root flare sitting inside that footprint makes even a few inches of grading a problem for the tree. The state's drip-line rule and its certified-arborist exception apply the same way to a putting green as to a plain lawn, but a green's grading work tends to go deeper at the contours than a flat residential install, which is worth flagging to an arborist reviewing the layout rather than assuming a flat-lawn approval covers it.</p>"),
            ("Winter Park's permeability path and a green's drainage",
             f"<p>Whichever of Winter Park's two described permeability paths a green follows, pervious or impervious, the drainage plan matters more on a contoured surface than a flat one, since water moving across a slope concentrates at the low points faster than it does on level ground. A green built to the pervious standard needs that engineered layer graded to match the contours, not just laid flat underneath them, which is a detail worth asking a bidder about directly.</p>"),
        ],
        "scenario": ("A green behind an Interlachen-area estate lot",
                     f"<p>Say you have a 450 sq ft green and fringe planned for a backyard near Interlachen Avenue, with two cups and a gentle two-foot fall across the surface, clear of any canopy. At {price('putting', True)} a square foot, that lands around $8,100 to $11,250 installed, with the contouring and fringe work sitting toward the upper half of that range rather than the lower. A flatter green of the same size, without the contour work, would price closer to the low end.</p>"
                     + f"<p>{svc('putting', 'Backyard putting greens')} in {city('maitland', 'Maitland')} or {city('orlando', 'Orlando')} price on the same range; what moves the number here is the shaping, not the ZIP code.</p>"),
        "faqs": [
            faq("Are Winter Park's lakefront lots typically large enough for a putting green?",
                "Many of the older parcels around the Chain of Lakes are, especially away from the narrower cottage streets closer to downtown. A site visit is the only way to confirm a specific backyard has the flat, open run a contoured green needs."),
            faq("Does a putting green's grading trigger the drip-line rule differently than a flat lawn?",
                "The rule itself is the same, but a contoured green's excavation tends to go deeper at low points than a flat lawn's, which is worth mentioning to an arborist reviewing a layout near a live oak's root flare."),
        ],
        "sources": SRC,
    },
    "playground": {
        "title": "Playground Turf for Winter Park Families",
        "meta": "Playground turf installation in Winter Park, FL runs $10–$25 per sq ft. Shock pad sizing under a shaded canopy near Dinky Dock and Kraft Azalea parks.",
        "h1": "Shaded play areas and playground turf in Winter Park",
        "lede": capsule(f"A backyard swing set in Winter Park is more likely than not to sit under some amount of live oak canopy, which changes both the heat picture and the drip-line question. Small residential play areas here typically price at {price('playground', True)} a square foot, within the wider {price('playground')} Central Florida range as of September 2026."),
        "sections": [
            ("Shade changes the heat problem more than it solves it",
             f"<p>A residential play area under a mature oak's canopy near {a('/laws/hoa-rules/', 'a Winter Park')} historic district runs cooler on a summer afternoon than the same turf in open sun a block away, since the canopy the Urban Forestry Division tracks across more than 75,000 private trees blocks direct exposure for a good part of the day. That's real, but it's a smaller effect than a hose rinse, which drops surface temperature 30 to 50 degrees within minutes regardless of shade. {post('how-hot-does-artificial-turf-get-in-florida', 'This article')} covers the numbers behind both.</p>"),
            ("Shock pad sizing and a shaded layout's edges",
             f"<p>Fall-height cushioning under a swing set or a play structure has to match the equipment's own manufacturer rating no matter what's overhead, and a canopy doesn't change that math. What a canopy does change is the layout's edges: a shock pad footprint that would otherwise sit centered in an open yard sometimes has to shift a few feet to stay clear of a drip line, which can mean redesigning where the equipment itself goes rather than just the turf underneath it.</p>"),
            ("Leaf and acorn cleanup on a canopy lot",
             f"<p>A live oak sheds heavily in late winter, and a play area under one collects far more debris over a season than a lawn on an open lot in a newer part of the county. Left alone, that debris works down into the infill and changes drainage the same way it would on natural grass. {post('oak-leaves-and-debris-on-artificial-turf', 'This article')} covers how often that cleanup actually needs to happen on a canopy-heavy lot like the ones common here.</p>"),
        ],
        "scenario": ("A play area behind a canopy lot near Kraft Azalea Park",
                     f"<p>Picture a family a few blocks from Kraft Azalea Park wanting to turf a 300 sq ft corner of the backyard for a swing set rated to a four-foot fall height, with an adjacent live oak shading roughly a third of that footprint. Pricing the whole area at {price('playground', True)} a square foot puts the job near $3,600 to $5,700, though the shaded third can't be finalized until an arborist confirms whether the layout actually reaches into the canopy's drip line.</p>"
                     + f"<p>A comparable play area in {city('casselberry', 'Casselberry')} or {city('winter-springs', 'Winter Springs')}, without a canopy overhead, skips that step entirely and moves straight from measurement to install.</p>"),
        "faqs": [
            faq("Does oak canopy over a Winter Park play area reduce how much cooling infill is worth buying?",
                "It lowers surface temperature during the shaded hours, but a west-facing gap in the canopy can still get hot in late afternoon, so a cooling or lighter-colored infill still helps on the sunniest part of the layout even under a partial canopy."),
            faq("Do I need an arborist's letter for a shock pad under a Winter Park oak?",
                "If any part of the fall-height pad falls inside the tree's drip line, yes, under the state's May 2026 turf standard. Marking the actual canopy edge, not just the trunk, before finalizing equipment placement avoids redesigning the layout mid-project."),
        ],
        "sources": SRC,
    },
    "pool": {
        "title": "Pool and Lanai Turf in Winter Park, FL",
        "meta": "Pool and lanai turf in Winter Park, FL prices in the same range as a residential lawn, $8–$18 per sq ft. What ridge sand means for a pool-deck strip.",
        "h1": "Turf around a Winter Park pool enclosure",
        "lede": capsule(f"Most pool jobs in Winter Park go into a screen enclosure added onto an older home rather than a pool built with the house new, and the turf itself prices at the residential rate, {price('residential', True)} a square foot within the {price('residential')} Central Florida range, as of September 2026."),
        "sections": [
            ("Retrofitted enclosures on pre-1970s lots",
             f"<p>A share of Winter Park's pool cages were added years after the house itself, on lots that predate the screen-enclosure era entirely, which means the strip of ground between the pool deck and the cage frame is often narrower and more irregular in shape than a newer subdivision's factory-planned pool yard. Turf in that strip needs a drainage underlay where it meets the concrete deck, since the transition between a hard surface and turf is exactly where water tends to collect if the grading isn't right.</p>"),
            ("Fast-draining Candler sand doesn't replace the underlay",
             f"<p>The ridge sand under much of Winter Park drains quickly on its own, but a pool-deck retrofit still needs the same drainage underlay and glue-down edge treatment a slower-draining flatwoods lot would need, since the concrete slab itself, not the native soil, is what the turf actually sits against at that edge. {post('install-artificial-turf-over-concrete-pavers-or-grass', 'This article')} covers how that installation differs from a soil-based lawn.</p>"),
            ("Low-E glass near a screened lanai",
             f"<p>A screened lanai often sits close to sliding glass doors on the home's rear elevation, and low-emissivity glass, common in replacement windows installed during a remodel, can reflect enough concentrated sun to soften turf several feet away. Checking which windows face the enclosure before finalizing turf placement is a five-minute step that's cheaper than replacing a scorched section later.</p>"),
        ],
        "scenario": ("A lanai retrofit on a 1960s ranch",
                     f"<p>A 1968 ranch home near downtown wanting turf along two sides of its pool deck, inside a screen cage added years after the original build, might be turfing something closer to 340 sq ft once the deck's odd angles are measured out. Figure roughly $3,400 to $5,440 for that at {price('residential', True)} a square foot, plus a modest add for the drainage underlay wherever the turf meets the concrete edge.</p>"
                     + f"<p>The same retrofit on a home near {city('maitland', 'Maitland')} or {city('orlando', 'Orlando')} prices the same way; the enclosure's age and shape drive the number more than the town it sits in.</p>"),
        "faqs": [
            faq("Does Winter Park's fast-draining soil mean a pool-deck retrofit needs less base work?",
                "No. The turf at a pool deck bonds to the concrete slab itself at that edge, so the underlay and glue-down treatment there don't change based on what the native soil underneath the rest of the yard does."),
            faq("Should I check for low-E glass before turfing a screened lanai in an older Winter Park home?",
                "Yes, especially if the home had replacement windows installed after the original construction, since low-E coatings reflect more concentrated heat than older glass and can affect turf placed nearby."),
        ],
        "sources": SRC,
    },
    "repair": {
        "title": "Artificial Turf Repair in Winter Park, FL",
        "meta": "Artificial turf repair in Winter Park, FL is quoted after a site visit, not a per-square-foot rate. The city's own maintenance agreement raises the stakes.",
        "h1": "Fixing turf that's fallen out of compliance in Winter Park",
        "lede": capsule("A lifted seam or a matted section takes a different amount of work than a full re-lay, so Winter Park turf repairs get priced from what a visit turns up, not from a rate card. What raises the stakes here more than most towns is a maintenance agreement the city's own turf code reportedly attaches to an install."),
        "sections": [
            ("A maintenance duty most cities don't attach to turf",
             f"<p>A secondary comparison of Florida ordinances, checked in September 2026, describes Winter Park's turf code as requiring a recorded agreement between the property owner and the city: routine maintenance, including cleaning, brushing, debris removal and repair, and a code violation if the turf stops functioning as designed and permitted. We couldn't independently confirm the current Municode text during this research pass, so verify the exact terms with Building & Permitting Services, but if that description holds, a Winter Park install carries an ongoing obligation that a repair visit here answers to directly, not just a homeowner's own preference for how the yard looks.</p>"),
            ("What actually shows up first after a rushed install",
             f"<p>A corner that was stapled instead of properly bonded tends to lift at the seam first, usually after a season of rain finds the weak point. On an older Winter Park lot, that seam problem often shows up faster near a driveway or patio transition, where the edge bonds to concrete rather than anchoring into soil. {post('does-homeowners-insurance-cover-artificial-turf', 'This article')} covers what a homeowner's policy does and doesn't pick up when a repair traces back to installation quality rather than storm damage.</p>"),
            ("Matching infill and grain on a repair job",
             f"<p>A repair patch has to match the surrounding turf's pile height, infill type and grain direction, or the fix reads as a visible seam even after it's structurally sound. On a lot with a live oak overhead, matching also means accounting for however much fading or debris staining the surrounding turf has picked up since installation, since a brand-new patch next to years-old material can look mismatched even when both pieces meet spec.</p>"),
        ],
        "scenario": ("A lifted edge near a driveway transition",
                     "<p>Say you have an eight-foot seam along a driveway edge that's started to lift after three rainy seasons, on a lawn installed before the state's May 2026 base and anchoring standards existed. A site visit is what determines whether that's a simple re-bond of the existing edge or a sign the base underneath settled unevenly, which would call for pulling back a wider section than the visible lift suggests.</p>"
                     + f"<p>A settled base under that seam costs noticeably more to correct than a simple adhesive failure would, which is exactly why the number only firms up once someone's actually looked at what's underneath.</p>"),
        "faqs": [
            faq("If Winter Park's turf code requires an ongoing maintenance agreement, what happens if the turf falls out of compliance?",
                "As described in the comparison document we checked, the city can treat unmaintained turf as a code violation and the property owner is on the hook to repair or replace it. Confirm the exact remedy process with Building & Permitting Services rather than assuming."),
            faq("Searching for the best artificial turf repair company near me in Winter Park? Here's what to ask first.",
                "Ask whether the crew has seen a maintenance-agreement requirement like Winter Park's before, since that changes how a repair gets documented, and ask for a site visit rather than a phone quote. A repair priced sight unseen is a guess, not a number worth planning around."),
        ],
        "sources": SRC,
    },
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
