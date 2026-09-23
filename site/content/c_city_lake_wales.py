# -*- coding: utf-8 -*-
"""Lake Wales, Polk County (tier 3): a ridge town at the outer edge of our range, grouped with other
Polk stops rather than booked on its own. Local sources checked September 2026: the City of Lake Wales'
own Building Division and Utilities Department pages, the Southwest Florida Water Management District's
2026 Modified Phase III order and Lake Wales News' coverage of it, the city's own Bok Tower page, Lake
Ashton's HOA governance page, U.S. Census Bureau QuickFacts, the Florida Fish and Wildlife Conservation
Commission's Lake Wales Ridge history page, and the USDA official series description for Candler sand
already used for the Polk County hub (reused here as a fact and URL, not a sentence)."""
from _data import CITIES
from _helpers import page, capsule, sec, table, faq, a, svc, city, post, src, ext, price
from _cityservice import cityservice_pages

SLUG = "lake-wales"
MI = CITIES[SLUG]["miles"]

BUILDING = ("City of Lake Wales — Building Division", "https://lakewalesfl.gov/241/Building-Division")
PORTAL = ("City of Lake Wales — Contractor Online Portal", "https://www.lakewalesfl.gov/909/Contractor-Online-Portal")
UTILITIES = ("City of Lake Wales — Utilities Department", "https://www.lakewalesfl.gov/256/Utilities-Department")
SWFWMD_P3 = ("Southwest Florida Water Management District — Modified Phase III order extended through Oct. 1, 2026", "https://www.swfwmd.state.fl.us/the-newsroom/2026/district-extends-modified-phase-iii-water-shortage")
LWNEWS = ("Lake Wales News, July 2026 — watering restrictions and citations", "https://www.lakewalesnews.net/story/2026/07/08/news/watering-restrictions-remain-in-place-citations-may-be-on-tap/5094.html")
BOKTOWER = ("City of Lake Wales — Bok Tower", "https://www.lakewalesfl.gov/497/Bok-Tower")
LAKEASHTON = ("Lake Ashton Living — Lake Ashton HOA governance (Lake Wales side)", "https://lakeashtonliving.com/governance/la-hoa")
CENSUS_LW = ("U.S. Census Bureau QuickFacts — Lake Wales city, Florida", "https://www.census.gov/quickfacts/fact/table/lakewalescityflorida/RHI225223")
CANDLER = ("USDA NRCS — official series description, Candler series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/C/CANDLER.html")
RIDGE_HIST = ("Florida Fish and Wildlife Conservation Commission — Lake Wales Ridge history", "https://myfwc.com/recreation/lead/lake-wales-ridge/history/")

SRC = [BUILDING, PORTAL, UTILITIES, SWFWMD_P3, LWNEWS, BOKTOWER, LAKEASHTON, CENSUS_LW, CANDLER, RIDGE_HIST, "dep-rule"]

HUB = page(
    "/areas/lake-wales/", "city",
    "Artificial Turf in Lake Wales, FL (2026 Guide)",
    "Synthetic turf installation, permits and Lake Wales Ridge soil facts for Lake Wales, FL, from a Kissimmee-based crew. Checked September 2026.",
    "Artificial grass installation for Lake Wales yards",
    capsule(f"Lake Wales, a ridge town about {MI} miles from our Kissimmee base, gets the same synthetic lawns, pet turf and putting greens we build everywhere else, priced at the identical {price('residential')} checked this September. A visit here rides with other Polk County stops rather than running on its own. Ridge sand changes how the base gets built."),
    "".join([
        sec("A ridge town on the far edge of a Kissimmee route",
            f"<p>Lake Wales sits close to {MI} miles from downtown Kissimmee, near the outer rim of where we work, and a crew usually reaches it on a day that covers other ridge towns too, rather than driving out for one yard. The town's claims to fame sit on high ground: Bok Tower, a 1920s landmark on Iron Mountain, sits at one of the higher points on the Florida peninsula ({ext(BOKTOWER[1], 'the city’s own page on the tower')}), and 1920s brick storefronts still line a historic downtown near the optical illusion at Spook Hill. None of that changes the price: a full backyard, {svc('pet', 'a pet run')} or {svc('putting', 'a chipping green')} here costs whatever it would in Kissimmee, since {price('residential')} doesn't move with the address. Comparing the best artificial turf companies near Lake Wales comes down to one question: has the crew worked this far out before, or only closer to home?</p>"),
        sec("From citrus rows to a golf-course retirement community",
            f"<p>The city began as a 1911 land purchase around Lake Wailes, incorporated in 1917, and has grown since: 16,361 at the 2020 census, an estimated 17,798 by 2024 ({ext(CENSUS_LW[1], 'Census Bureau figures')}). Freezes through the 1980s pushed citrus south and left grove ground open for the subdivisions that followed, documented by the state's own wildlife agency on this stretch of the {ext(RIDGE_HIST[1], 'Lake Wales Ridge')}. Lake Ashton, the 55-plus golf community straddling the Lake Wales and Winter Haven line, is one result: its HOA runs {a('/laws/hoa-rules/', 'an architectural review')} for exterior changes, though nothing published spells out a turf rule, so a resident files plans like any other landscaping change ({ext(LAKEASHTON[1], 'Lake Ashton’s own governance page')}).</p>"),
        sec("Lake Wales yard types and what we do differently",
            "<p>The ridge itself sorts Lake Wales into four recurring yard types, and which one a lot falls into says more about the build than its street name does.</p>"
            + table("Lake Wales yard types and what we do differently",
                    ["Type of yard", "What's common there", "How we adjust the job"],
                    [["A 1920s bungalow lot near downtown", "Narrow, established, mature shade trees", "Base sized for fast drainage, with a drip-line check before digging near any oak"],
                     ["A home in Lake Ashton or another golf community", "Architectural review, low-maintenance expectations", "Filed through the community's review process, the same paperwork a fence or paint color would need"],
                     ["A newer subdivision on former grove land", "Wider lots, younger trees, straighter grade", "A simpler layout on the same loose Candler sand underneath"],
                     ["A lakefront lot on Lake Wailes or a smaller ridge lake", "Waterfront setback applies", "Held to the state's water buffer unless an existing seawall already marks the shoreline"]],
                    "Every row sits on the same statewide price range. Slope, trees and water move a bid here, not the neighborhood."),
        ),
        sec("Permits for a synthetic lawn in Lake Wales",
            f"<p>Lake Wales runs its own Building Division rather than routing permits through the county: reach it at 863-676-5115, extension 9201, and track a filed permit through its contractor portal ({ext(BUILDING[1], 'Building Division')}; {ext(PORTAL[1], 'Contractor Online Portal')}). Nothing published there addresses synthetic turf, so a lawn conversion gets reviewed like any landscaping or irrigation-capping work, with {a('/laws/florida-hb-683/', 'Florida’s statewide turf standard')} the only turf-specific rule reaching the property. For pockets just outside the city line, {a('/laws/permits/polk-county/', 'our Polk County permit page')} covers what that office told us, and either job typically shares a route toward {city('dundee', 'Dundee')} or {city('haines-city', 'Haines City')} that week.</p>"),
        sec("Water, irrigation days and the ridge lakes",
            f"<p>The city's own Utilities Department, not the county, draws Lake Wales' water from three wells into the Floridan aquifer ({ext(UTILITIES[1], 'Lake Wales Utilities')}). Its posted schedule still shows two days a week, but that page hasn't caught up with the district's emergency footing: since early 2026 the Southwest Florida Water Management District has cut every customer in its territory, Lake Wales included, to one watering day through October 1, 2026, with citations now replacing courtesy letters ({ext(SWFWMD_P3[1], 'SWFWMD’s extension order')}). A capped synthetic lawn skips the question, since {src('dep-rule', 'the state turf rule')} already bars in-ground irrigation on turf. Confirming the day that applies is worth a call to city hall rather than trusting either page ({ext(LWNEWS[1], 'reporting from July 2026')}).</p>"),
        sec("Ridge sand, real slope and staying inside the lines",
            f"<p>Once the ground rises into the ridge, the soil shifts to Candler series sand: excessively drained, built from wind-deposited dunes, with grades running from flat to a real, walkable slope where a subdivision was cut into old grove land ({ext(CANDLER[1], 'USDA’s official series description')}). Ground like that barely holds a shape on its own, so anchoring every edge matters more here than on a flat Osceola lot, and {a('/laws/florida-hb-683/', 'the state’s own turf standard')} requires infill heavy enough to stay put rather than migrate toward a fence line. Lake Wailes downtown and the smaller ridge lakes near Lake Ashton fall under that standard's other half: no turf within 10 feet of open water, gone only where a seawall or bulkhead already does that job.</p>"),
        "<!--AUTO:city-services-->",
    ]),
    faqs=[
        faq("Does Lake Wales have its own rule for synthetic turf?", "No. The city's Building Division reviews a lawn conversion like any landscaping or irrigation change and hasn't published anything turf-specific. Florida's 2026 statewide standard is the only turf-specific rule reaching a Lake Wales property."),
        faq("How many days a week can I run irrigation in Lake Wales right now?", "Just one. The district's Modified Phase III order overrides the city's older two-day notice through October 1, 2026, so call city hall before assuming which schedule applies to a specific address."),
        faq("What does the Lake Wales Ridge's sandy soil mean for a new lawn?", "Candler sand drains fast and holds its shape poorly, so a base still needs careful compaction and anchored edges, especially on a real slope. Fast drainage doesn't remove the need for a proper washed-rock base."),
        faq("Can turf go right up to Lake Wailes or another ridge lake?", "Not usually. State rule holds any Florida lake or canal lot to the same line, 10 feet of clearance from open water, gone only where a seawall or bulkhead already forms that edge."),
    ],
    sources=SRC, city=SLUG, crumbs=[("Service areas", "/areas/")], crumb="Lake Wales",
    related=[("/areas/polk-county/", "Artificial turf across Polk County"), ("/laws/permits/polk-county/", "Polk County permit findings for turf"),
             ("/areas/dundee/", "Turf installers in Dundee"), ("/areas/frostproof/", "Turf installers in Frostproof"),
             ("/artificial-turf-cost/", "Full turf cost guide")],
)

LOCAL = {
    "residential": {
        "title": "Artificial Grass Installation in Lake Wales, FL",
        "meta": "Artificial grass installed on Lake Wales' ridge-sand lots runs $8–$18 a sq ft. Slope, HOA review and the 2026 state turf rule, checked for this city.",
        "h1": "A synthetic lawn built for Lake Wales' sandy slopes",
        "lede": capsule(f"A Lake Wales {svc('residential', 'lawn conversion')} prices the same as anywhere in Central Florida, {price('residential')} per square foot installed, with most yards landing at {price('residential', True)} once the crew measures for slope and access. What changes here is the ground: Candler ridge sand drains fast but holds a compacted shape poorly, so September 2026's checked range still depends on getting the base right first."),
        "sections": [
            ("Grading a sloped lot near downtown",
             f"<p>A lot near downtown {city('lake-wales', 'Lake Wales')} often carries more real grade change than a same-size yard back in Kissimmee, since this part of the city sits on the shoulder of the ridge rather than flat ground. Where a flatwoods lawn just needs its subgrade sloped one to two percent toward a rear low point, a sloped Lake Wales yard sometimes needs a shaped, terraced subbase or extra anchoring along the downhill edge so the compacted rock doesn't creep before turf ever goes down. Mature oaks are common on these older lots too, planted when the brick storefronts a few blocks away were new, and the state's drip-line rule keeps installation outside a tree's root zone unless a certified arborist signs off. None of that changes the price range; it changes how many hours the base takes before turf ever goes down, which is a big part of why {post('artificial-turf-on-a-slope', 'installing turf on a real slope')} takes longer than the same square footage on flat ground.</p>"),
            ("A citrus-grove subdivision or a golf-course lot",
             "<p>Plenty of Lake Wales' newer streets sit on ground that grew oranges before it grew houses, since freezes through the 1980s pushed commercial citrus south and left grove land open for the subdivisions that followed across the ridge. A lot built this way is usually wider and straighter than a downtown lot, with a shallower grade, which keeps the base simpler even though it's still Candler sand underneath. Lake Ashton, the 55-plus golf community that spans the Lake Wales and Winter Haven line, is a good example of the type: its homeowners association reviews landscaping changes through an architectural process, so a turf submittal there goes in with a product spec sheet and a site sketch like any other exterior change, the same file a paint color or a fence would need. "
             + f"{post('artificial-turf-for-55-plus-communities', 'What changes, and what doesn’t, in a 55-plus community')} covers the rest of that process.</p>"),
            ("A lakefront yard on the ridge",
             f"<p>A handful of Lake Wales lots back onto Lake Wailes itself or one of the smaller lakes threaded through the ridge, and Florida holds those yards to the same line as any lake or canal lot in the state: no turf in the first 10 feet of open water, a distance that closes to zero only where a seawall or bulkhead already stands there. Because Lake Wales sits about {MI} miles out, close to the edge of where a Kissimmee crew works, a lakefront measure-and-quote visit here usually gets scheduled for a day that already includes a stop in {city('winter-haven', 'Winter Haven')} or {city('bartow', 'Bartow')}, not as a one-off trip. Sequence matters more than anything else on a lot like this: mark the buildable line first, then build the usual washed-rock base inside it, sized for however much slope the lot carries down toward the water.</p>"),
        ],
        "scenario": ("What a 1,050 sq ft Lake Wales backyard runs",
                     f"<p>Say you have a 1,050 sq ft backyard on a Lake Ashton lot, flat enough that the crew doesn't need to terrace anything, with the old St. Augustine already dying back in the shadier corners. At {price('residential', True)} a square foot, the typical Central Florida range, that yard prices between $10,500 and $16,800 once sod removal, the washed-rock base, turf and infill are all in the same number. A steeper downtown lot of the same size, with a terraced subbase and extra anchoring along the low edge, would land closer to the top of the full {price('residential')} range instead. Either way, the HOA paperwork for a golf-community lot like this one is usually the slower part of the schedule, not the install itself.</p>"),
        "faqs": [
            faq("Does a sloped Lake Wales lot cost more to turf?", "Sometimes. A lot with real grade change needs a shaped or terraced base and extra anchoring along the downhill edge, which adds labor time even though the price per square foot comes from the same statewide range as a flat yard."),
            faq("Do I need Lake Ashton's HOA approval before installing turf?", "Almost certainly, the same as for any exterior landscaping change there. Submit a product spec sheet and a site sketch through the community's architectural review process before scheduling an install date."),
            faq("Is my Lake Wales yard inside the state's waterbody setback?", "If it backs onto Lake Wailes or another lake or canal, probably. That 10-foot buffer goes away only on a lot where a seawall or bulkhead already marks the water's edge, and a measure visit confirms the buildable area before anything is quoted."),
        ],
        "sources": SRC,
    },
    "pet": {
        "title": "Pet Turf & Dog Runs in Lake Wales, FL",
        "meta": "Pet turf for Lake Wales dog runs drains fast through ridge sand but still needs its own base. Zeolite infill, fencing and setbacks, checked September 2026.",
        "h1": "Dog-run turf built for Lake Wales' fast-draining sand",
        "lede": capsule(f"{svc('pet', 'Pet turf')} for a Lake Wales dog run costs {price('pet')} per square foot installed, typically {price('pet', True)}, the same Central Florida range checked in September 2026 regardless of address. Ridge sand under the yard drains fast on its own, but a run still needs its own deeper base and a fully permeable backing, not just fast native soil."),
        "sections": [
            ("Fast sand, but still a deeper base",
             f"<p>Candler sand under {city('lake-wales', 'Lake Wales')} is excessively drained on its own, among the fastest-draining ground in Central Florida, which sometimes leads a homeowner to assume a dog run here needs less base than one back in flatter Osceola County. It doesn't work that way: a run still needs three to four inches of washed, open-graded rock rather than a plain lawn's two to four, because the volume from daily rinsing and a determined pacer's traffic is higher than what fast native sand alone can absorb at the surface. The sand's speed helps the base clear a rinse quickly once it's built correctly; it doesn't replace the base itself.</p>"),
            ("A fenced yard the neighbors can't see into",
             "<p>"
             + a("/laws/hoa-rules/", "Florida’s HOA visibility rule")
             + " protects a fenced backyard that can't be seen from the street or from an adjacent lot, which covers most dog runs built on the wider, straighter lots common in Lake Wales' newer subdivisions on former grove ground. A front-yard run, or one visible from a neighbor's window, doesn't get that same protection and is more likely to need architectural review first. Either way, the fence itself and the gate threshold matter as much as the turf choice, since a bored dog tests a loose corner far more than foot traffic on a family lawn ever does.</p>"),
            ("Keeping a run back from the ridge lakes",
             f"<p>A dog run planned for a lot backing onto Lake Wailes or one of the ridge's smaller lakes still has to keep the same clearance from open water that any turf near a Florida lake, canal or pond has to keep, 10 feet, gone only where a seawall or bulkhead already stands at that shoreline. Lake Wales sits about {MI} miles from our Kissimmee base, near the outer edge of the area we cover, so a pet-turf measure visit out this way typically lines up with another stop toward {city('haines-city', 'Haines City')} rather than running as its own trip. Staking that 10-foot line before ordering material keeps a run's fenced footprint from creeping into ground the state rule doesn't allow turfing at all.</p>"),
        ],
        "scenario": ("Pricing a 420 sq ft dog run behind a Lake Wales home",
                     f"<p>Say you have a 420 sq ft side yard fenced off for two dogs behind a newer Lake Wales subdivision home, currently bare dirt where grass never took hold under the shade of a young oak. At {price('pet', True)} a square foot, the typical range for pet turf, that run prices between $5,040 and $6,720 once the deeper rock base, permeable backing, zeolite infill and fencing tie-ins are all figured in. Add a wider gate or a poured threshold pad for double-dog traffic and the number moves toward the top of the full {price('pet')} range instead. Either way, the fence goes up before the base does, so the crew can grade toward a single drain point from the start.</p>"),
        "faqs": [
            faq("Does Lake Wales' fast-draining sand mean a dog run needs less base?", "No. A run still needs three to four inches of washed rock, deeper than a plain lawn's base, because daily rinsing and traffic add more liquid than even fast-draining Candler sand can handle at the surface alone."),
            faq("Does a backyard dog run need Lake Wales' Building Division involved?", "Usually only if the fencing itself needs a permit; the city hasn't published anything specific to turf, so a run gets reviewed like any other landscaping or fencing project. Call the Building Division to confirm for a specific address."),
            faq("Can a dog run go closer than 10 feet to a ridge lake?", "Only on a lot where a seawall or bulkhead already stands between the fence line and open water. Otherwise a fenced pet area keeps the same distance from a lake or canal that any other turf would."),
        ],
        "sources": SRC,
    },
    "putting": {
        "title": "Backyard Putting Greens in Lake Wales, FL",
        "meta": "Backyard putting greens in Lake Wales, home to a golf-course retirement community on the ridge, run $14–$30 a sq ft installed. Checked September 2026.",
        "h1": "A putting green shaped for Lake Wales' real slope",
        "lede": capsule(f"Building a backyard {svc('putting', 'putting green')} in Lake Wales costs {price('putting')} per square foot, typically {price('putting', True)}, matching what a green runs anywhere else we work this September. What's different here is real ridge slope, which changes how a green gets shaped far more than it changes what the job costs, especially near the golf-course lots the ridge is known for."),
        "sections": [
            ("Shaping tiers into an actual ridge slope",
             "<p>A flat lawn base just needs a gentle one to two percent fall toward a drain point, but a putting green's tiers have to hold a specific, designed shape on top of Lake Wales' loose Candler sand, which doesn't pack as predictably as heavier soil once a plate compactor runs over it. On a ridge lot with real grade change, that usually means hand-shaping the rock in smaller lifts and checking each tier against the break plan before the next layer goes down, rather than screeding one flat pad the way a lawn's base gets built. Skipping that extra care on sandy, sloped ground is how a green loses its break within a season instead of holding it for years.</p>"),
            ("A green that fits a golf-community lifestyle",
             f"<p>{city('lake-wales', 'Lake Wales')} is home to Lake Ashton, a 55-plus community built around its own golf course, and a backyard putting green is a natural fit for a homeowner there who wants to keep practicing without a cart ride to the first tee. The community's architectural review covers a green the same way it covers any other exterior addition, so a design gets submitted with a layout sketch and a product spec sheet before a crew breaks ground. {post('artificial-turf-for-55-plus-communities', 'What a 55-plus community typically asks for')} walks through what that packet usually includes, separate from anything the city itself requires.</p>"),
            ("Room enough near a former grove or a downtown lot",
             "<p>A newer subdivision built across former grove land typically leaves far more open space for a green's design than a compact lot near Lake Wales' 1920s downtown offers, where a chipping pad and a short fringe might be all that fits beside the house. Either lot sits on the same ridge soil, so the shaping principle doesn't change, only the scale of the design: a bigger, multi-tier green with two or three cups on a wider lot, or a single small green sized to whatever strip of yard is left once a garage and a driveway are accounted for.</p>"),
        ],
        "scenario": ("A 380 sq ft green on a Lake Wales golf-community lot",
                     f"<p>Say you have a 380 sq ft L-shaped area behind a Lake Ashton home, enough for a two-tier green with a short fringe and a couple of cups. Figured at {price('putting', True)} a square foot, the usual range for a backyard green, the project totals $6,840 to $9,500 once the hand-shaped base, putting surface, fringe turf and cup hardware are all included. A simpler, single-tier design of the same size would land closer to the bottom of the full {price('putting')} range instead, since less shaping labor goes into a flat pad than into two distinct breaks.</p>"),
        "faqs": [
            faq("Does a putting green need Lake Ashton's HOA approval separately from the city?", "Yes, in addition to whatever Lake Wales itself would require for the work. Submit the green's layout and product spec sheet through the community's architectural review before scheduling an install date."),
            faq("Why does a green cost more to build on ridge sand than flat ground?", "Because loose Candler sand doesn't hold a shaped tier as predictably as denser soil, so the base gets built in smaller, hand-checked lifts. The turf and hardware cost the same either way; the extra labor is in the shaping."),
            faq("Is there room for a putting green on a small downtown Lake Wales lot?", "Often, just at a smaller scale, a single tier with a short fringe rather than a multi-cup layout. The same ridge soil and shaping approach apply regardless of lot size."),
        ],
        "sources": SRC,
    },
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
