# -*- coding: utf-8 -*-
"""Southchase, FL (unincorporated Orange County). Hub + 12 city x service pages.
Research checked September 2026; see SRC below for every local citation used."""
from _helpers import page, capsule, sec, table, faq, ul, a, svc, city, post, src, ext, price
from _cityservice import cityservice_pages

SLUG = "southchase"

SRC = [
    "dep-rule", "fs125572", "fs7203045",
    ("U.S. Census Bureau — QuickFacts, Southchase CDP, Florida", "https://www.census.gov/quickfacts/fact/table/southchasecdpflorida/PST045225"),
    ("Homes.com — About Southchase, Orlando, FL neighborhood guide", "https://www.homes.com/orlando-fl/neighborhood/southchase/"),
    ("Florida-HOA.net — Southchase Community Homeowners Association directory", "https://florida-hoa.net/fhhoa_list.php?mastertable=fhtitle&masterkey1=N33740"),
    ("South Florida Water Management District — Shingle Creek", "https://www.sfwmd.gov/recreation-site/shingle-creek"),
    ("Orange County Water Atlas — Shingle Creek Watershed", "https://orange.wateratlas.usf.edu/watershed/?wshedid=10&wbodyatlas=watershed"),
    ("USDA NRCS — Official Series Description, Immokalee series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/I/IMMOKALEE.html"),
    ("USDA NRCS — Soil Survey of Orange County, Florida (1989)", "https://archive.org/details/usda-soil-survey-of-orange-county-florida-1989"),
    ("Orange County Code, Chapter 38, Zoning, Municode Library", "https://library.municode.com/fl/orange_county/codes/code_of_ordinances?nodeId=ORCOCO_CH38ZO"),
    ("BNBCalc — Orange County, Florida short-term rental regulation guide", "https://www.bnbcalc.com/blog/short-term-rental-regulation/orange-county-florida-guide"),
    ("Orange County Code, Chapter 24, Landscaping, Buffering and Open Space, Municode Library", "https://library.municode.com/fl/orange_county/codes/code_of_ordinances?nodeId=PTIIORCOCO_CH24LABUOPSP"),
    ("Orange County Utilities — watering restrictions", "https://www.orangecountyfl.net/watergarbagerecycling/wateringrestrictions.aspx"),
    ("Orange County Property Appraiser — parcel search", "https://ocpafl.org/"),
    ("Orange County Parks and Recreation — South Orange Youth Sports Complex", "https://www.orangecountyfl.net/cultureparks/parks.aspx?m=dtlvw&d=37"),
]

# ============================================================== hub
HUB = page(
    "/areas/southchase/", "city",
    "Artificial Turf in Southchase, FL (Orange County)",
    "Artificial turf for Southchase, an unincorporated Orange County community off South Orange Blossom Trail. Soil, water and permit facts, checked September 2026.",
    "Turf for Southchase's patio homes and pool-cage lawns",
    capsule("Southchase is an unincorporated Orange County community strung along South Orange Blossom Trail between "
            + city("hunters-creek", "Hunters Creek") + " and " + city("meadow-woods", "Meadow Woods") + ", about 7 miles from downtown Kissimmee. "
            + "Most of its patio homes and single-family lots went up in the 1990s over sandy flatwoods soil. "
            + f"Installed turf still prices at {price('residential')} a square foot here, as it does anywhere in Central Florida; a pond behind the fence, not the ZIP code, decides the layout."),
    "".join([
        sec("A racetrack grid of subdivisions off South Orange Blossom Trail",
            f"<p>Southchase sits entirely in unincorporated Orange County, wedged between {city('hunters-creek', 'Hunters Creek')} to the west and {city('meadow-woods', 'Meadow Woods')} to the north, just above the line into Osceola County. It's roughly 7 miles from downtown Kissimmee, close enough that a crew working {svc('residential', 'a lawn conversion')} in Southchase in the morning can be back in {city('kissimmee', 'Kissimmee')} by afternoon. The community grew up around South Orange Blossom Trail (US-441) through the 1990s, with builders naming several of its subdivisions after racetracks: Churchill Downs and Arlington Park are two that still show up on plat maps and HOA rosters today, alongside The Willows and the separately governed Parcel 6 (" + ext("https://www.homes.com/orlando-fl/neighborhood/southchase/", "Homes.com's Southchase neighborhood profile") + ").</p>"
            + f"<p>The 2020 Census counted 16,276 people in the Southchase census-designated place living in 5,267 housing units, a mix of detached single-family homes, townhomes and patio-style residences on lots that run smaller than a newer Osceola County subdivision (" + ext("https://www.census.gov/quickfacts/fact/table/southchasecdpflorida/PST045225", "Census QuickFacts, Southchase CDP") + "). A screened pool cage is the norm rather than the exception on the single-family side, which matters more for a turf job here than the ZIP code does.</p>"),
        sec("Five Southchase lot conditions we build around",
            table("Southchase lot conditions and how a build responds to each one",
                  ["Lot condition", "Southchase phase or feature", "How the build adapts"],
                  [["Zero-lot-line patio home", "The Willows and similar 1990s phases", "Narrow side access, hand-carried base material, tight seam layout"],
                   ["Screened pool cage", "Churchill Downs, Arlington Park and most single-family blocks", "Glue-down edges over the deck, a drainage underlay, no nail line into concrete"],
                   ["Backyard on a retention pond", "Throughout Southchase's Shingle Creek-fed drainage system", "Turf stops 10 ft short of the water's edge and never crosses the swale"],
                   ["Original 1990s St. Augustine lot", "Churchill Downs, Arlington Park, Parcel 6", "Full strip-out of 30 years of thatch before base goes in"],
                   ["Commercial frontage", "South Orange Blossom Trail parcels", "Landscape-strip and parking-island rules apply, reviewed by county staff, not an HOA board"]],
                  "Compiled from Southchase's published neighborhood profile and Orange County's zoning and water records, checked September 2026.")),
        sec("Sandy flatwoods soil and a water table that sits close to grade",
            "<p>Orange County's own soil survey maps the county's southern flatwoods, the belt Southchase sits in, to poorly drained series such as Immokalee: very deep, sandy soils that form on flat marine terraces and hold water within a foot or two of the surface for long stretches of the wet season "
            + ext("https://soilseries.sc.egov.usda.gov/OSD_Docs/I/IMMOKALEE.html", "USDA's Immokalee series description") + " and "
            + ext("https://archive.org/details/usda-soil-survey-of-orange-county-florida-1989", "the 1989 Soil Survey of Orange County") + ". "
            + "That's ordinary Central Florida flatwoods, not a defect, but it means a Southchase base can't be built at the shallow end of what the state allows and still clear the water table by much.</p>"
            + f"<p>The fix is the same one described on our {a('/artificial-turf-cost/', 'cost guide')} and on {svc('residential', 'the residential turf page')}: two to four inches of washed, open-graded crushed rock or crushed concrete, built toward the fuller end of that range and compacted in two passes rather than one, so the surface sheds a Central Florida downpour instead of sitting on top of one.</p>"),
        sec("Retention ponds, Shingle Creek and the state's 10-foot rule",
            f"<p>Southchase's drainage runs toward Shingle Creek, which starts nearby in south Orange County and carries water south into Lake Tohopekaliga and the Kissimmee Chain of Lakes, land the South Florida Water Management District manages as conservation area a few miles away in Hunters Creek ({src('dep-rule', 'the state turf rule')}; " + ext("https://www.sfwmd.gov/recreation-site/shingle-creek", "SFWMD's Shingle Creek page") + "). Orange County's own water atlas puts the Shingle Creek watershed at just over 80 square miles inside the county, dotted with 71 named lakes and ponds, several of them the stormwater ponds that back up to Southchase yards (" + ext("https://orange.wateratlas.usf.edu/watershed/?wshedid=10&wbodyatlas=watershed", "Orange County Water Atlas, Shingle Creek Watershed") + ").</p>"
            + "<p>Florida's May 19, 2026 turf standard keeps synthetic grass at least 10 feet from a natural or man-made waterbody unless a seawall separates the two, and out of any swale or a pond's littoral zone entirely. On a Southchase lot backing onto one of those ponds, that setback usually still leaves most of the yard buildable; it just isn't the strip closest to the water.</p>"),
        sec("Permits, HOA paperwork and what to line up before a crew arrives",
            f"<p>Southchase answers to Orange County's Permitting Services and Division of Building Safety, not a city hall, and the county's landscape code (Chapter 24) defines \"turf\" only as living grass species, with no section written for a synthetic product either way. See {a('/laws/permits/orange-county/', 'our Orange County permit page')} for the department's phone number and the parcel-lookup tool. That silence in the county code doesn't override {a('/laws/florida-hb-683/', 'the state standard')}, which sets the material, drainage and setback rules a Southchase installation has to meet regardless of what the county's older code says.</p>"
            + f"<p>Southchase also isn't run by one master homeowners association. County HOA filings show a string of separate parcel-level boards, several chartered around 1989 through the early 1990s as each phase was built out, plus the independently managed Parcel 6 community (" + ext("https://florida-hoa.net/fhhoa_list.php?mastertable=fhtitle&masterkey1=N33740", "Florida-HOA.net's Southchase association listings") + f"). That means the architectural-review process for a Southchase yard depends on which phase the address sits in, not a single Southchase-wide rulebook; {a('/laws/hoa-rules/', 'what Florida law lets any of them restrict')} still comes down to F.S. 720.3045, and {a('/tools/hoa-packet-checklist/', 'our HOA packet checklist')} covers what to submit either way.</p>"),
        sec("Short-term rentals in Southchase",
            f"<p>Unincorporated Orange County's zoning code permits a whole-home rental under 30 days only in its R-3 multiple-family district; every other residential district, which covers Southchase's single-family and townhome subdivisions, bars nightly or weekly turnover outright (" + ext("https://library.municode.com/fl/orange_county/codes/code_of_ordinances?nodeId=ORCOCO_CH38ZO", "Orange County Code, Chapter 38, Zoning") + "; " + ext("https://www.bnbcalc.com/blog/short-term-rental-regulation/orange-county-florida-guide", "a 2026 compliance guide summarizing the ordinance") + "). That keeps guest-turnover turf a small slice of the Southchase market compared with a Osceola tourist zone; most of the calls we'd expect here are long-term landlords and owner-occupants, not vacation-rental operators.</p>"),
        sec("How do you find the best turf installer near Southchase?",
            f"<p>Ask what goes under the grass before asking about the grass itself. A Southchase quote worth comparing states the base depth and material, the turf's face weight and pile height, the infill type and how many pounds per square foot, and how seams and the perimeter are secured, the same five numbers {post('how-to-compare-artificial-turf-quotes', 'our guide to comparing two turf quotes')} walks through. Anyone who can't answer those in writing for a flatwoods lot near Shingle Creek hasn't measured the yard yet.</p>"),
        "<!--AUTO:city-services-->",
    ]),
    faqs=[
        faq("Is Southchase in Orange County or Osceola County?", "Orange County. Southchase sits in unincorporated Orange County, just north of the Osceola line, so permitting runs through Orange County's Permitting Services rather than a city or through Osceola County."),
        faq("Does one HOA cover all of Southchase?", "No. Southchase is split among several separate parcel-level homeowners associations formed as each phase was built in the late 1980s and 1990s, plus the independently managed Parcel 6 community, so an ARC submittal depends on which subdivision the address is in."),
        faq("Can I put artificial turf next to a retention pond in Southchase?", "Only outside a 10-foot band closest to the water, unless the property already has a seawall or bulkhead between the lawn and the pond; turf can never sit inside a littoral zone or a drainage swale under the state's May 2026 standard."),
        faq("Do I need a permit for turf on an unincorporated Southchase lot?", "Orange County's landscape code doesn't name synthetic turf either way, so call Permitting Services before scheduling a crew; capping the irrigation heads under the turf can trigger its own plumbing permit even when the turf itself doesn't."),
        faq("Is Southchase zoned for a nightly vacation rental?", "Not in most of its residential districts. Orange County's zoning code limits rentals under 30 days to the R-3 district, which doesn't describe Southchase's single-family and townhome subdivisions, so a whole-home nightly rental generally isn't a permitted use there."),
    ],
    sources=SRC, city=SLUG, crumbs=[("Service areas", "/areas/")], crumb="Southchase",
    related=[("/areas/orange-county/", "Orange County service area"), ("/laws/permits/orange-county/", "Artificial turf permits in Orange County"),
             ("/areas/hunters-creek/", "Turf installers in Hunters Creek"), ("/areas/meadow-woods/", "Turf installers in Meadow Woods"),
             ("/artificial-turf-cost/", "Turf cost tables for Central Florida")],
)

# ============================================================== LOCAL
LOCAL = {}

LOCAL["residential"] = {
    "title": "Artificial Grass Installation in Southchase, FL",
    "meta": "Artificial grass installation in Southchase, an unincorporated Orange County community built mostly in the 1990s over sandy flatwoods soil, September 2026.",
    "h1": "Turf conversions for Southchase's 1990s subdivisions",
    "lede": capsule(f"A residential lawn conversion in Southchase runs {price('residential')} a square foot installed, typically {price('residential', True)}, as of September 2026. Most of the community's single-family lots, in subdivisions such as Churchill Downs and Arlington Park, were built in the 1990s over sandy flatwoods soil that holds water close to grade, which is why the base under the turf matters as much here as the product on top of it."),
    "sections": [
        ("What's under a Southchase lawn before we touch it",
         "<p>Southchase's single-family subdivisions, Churchill Downs and Arlington Park among them, were largely built out through the 1990s on modest lots with St. Augustine sod laid straight over native sand. Three decades on, that sod is usually thin in the shady stretch behind the house and thick with old thatch everywhere the sun still reaches, and both conditions get stripped the same way: sod and several inches of the original soil come out before anything new goes in. Homes that changed hands more than once often carry a patched-together sprinkler system from more than one previous owner, which is worth mapping before demo starts rather than discovering mid-dig.</p>"),
        ("Why a flatwoods lot changes the base depth",
         "<p>The soil under most of Southchase falls into the county's mapped flatwoods series, deep sand that stays saturated within a foot or two of the surface for long stretches of a Florida wet season. On a lot like that, we build the washed crushed rock or crushed concrete base toward the top of the state's allowed two-to-four-inch range rather than the bottom, compacted in two lifts, so the turf sits far enough above a saturated water table to actually drain the way the backing is rated to. Skipping that margin is how a lawn that looked fine in November holds standing water by July.</p>"),
        ("What Orange County's code says, and doesn't, about a Southchase lawn",
         "<p>Orange County's landscape code, Chapter 24, defines turf only as a mat of living grass species and has no section written for a synthetic product, so a straightforward backyard conversion in Southchase isn't running into a named local turf rule either way. That silence doesn't mean no rules apply: capping the irrigation heads under the new lawn, required by Florida's May 2026 turf standard, can still need its own plumbing permit, and a Southchase parcel's specific homeowners association, not the county, is usually the office that reviews the design itself before a shovel goes in.</p>"),
    ],
    "scenario": ("Say you have a resale in Churchill Downs",
                 f"<p>Say you buy a resale in Churchill Downs with a 900 sq ft backyard, half of it thin St. Augustine and half bare sand where a dog used to run along the fence line. At the published range of {price('residential')} a square foot, a full conversion prices between $7,200 and $16,200, and most Southchase jobs like this land nearer the typical {price('residential', True)} band, or $9,000 to $14,400, once the base is built to the fuller depth a flatwoods lot calls for. The final number moves with fence-gate width for equipment access, how much of the old irrigation zone gets capped versus reused elsewhere, and whether the shape is a plain rectangle or works around a mature oak near the property line.</p>"),
    "faqs": [
        faq("Does Southchase's soil need a deeper base than a newer Osceola County lot?", "Often yes. Southchase's flatwoods sand holds water close to the surface longer than a well-drained ridge lot does, so we lean toward the fuller end of the state's two-to-four-inch base range rather than the minimum."),
        faq("Does the Churchill Downs or Arlington Park HOA need to approve a lawn conversion?", "Southchase doesn't have one master association, so approval depends on which phase-level HOA covers that address; check the specific community's architectural-review process before ordering material."),
    ],
    "sources": SRC,
}

LOCAL["pet"] = {
    "title": "Pet Turf & Dog Runs for Southchase, Orange County Homes",
    "meta": "Pet turf and dog runs for Southchase, FL homes on narrow patio-home lots and flatwoods sand. Local drainage notes and 2026 pricing.",
    "h1": "Dog-proof turf for Southchase's narrow side yards",
    "lede": capsule(f"Pet turf in Southchase runs {price('pet')} a square foot installed, typically {price('pet', True)}, as of September 2026. A lot of Southchase's zero-lot-line and patio-home phases, The Willows among them, leave a dog with a side strip a few feet wide rather than an open backyard, and a flatwoods water table close to grade means that strip has to drain fast or it turns into a mud lane."),
    "sections": [
        ("A dog run sized for a Southchase side yard, not a rural lot",
         "<p>Plenty of Southchase's patio-home and zero-lot-line phases, The Willows is one, put the usable outdoor space in a fenced strip three to six feet wide running along a shared property line rather than a wide-open backyard. That width dictates equipment: a run that narrow gets built with hand tools and wheelbarrow loads of base material instead of a skid steer, since there's rarely room to turn one around. It also means every inch of drainage slope matters more, because there's no wide flat area to absorb a mistake in grading.</p>"),
        ("Draining a run on soil that's already holding water",
         "<p>The sandy flatwoods soil under most of Southchase keeps a shallow water table for long stretches of the wet season, which is a bigger problem for a dog run than for an open lawn because a run gets rinsed daily and concentrates urine in a small footprint. We skip the weed barrier under pet turf here for that reason, since a fabric layer traps liquid at the surface instead of letting it filter into the rock below, and we lean on zeolite or a coated infill rather than plain silica when a Southchase yard already drains slowly on its own.</p>"),
        ("Getting a run approved when the HOA changes block by block",
         "<p>Because Southchase is split among several separate phase-level associations rather than one Southchase-wide board, what a dog run needs for sign-off, a sample swatch, a site sketch, sometimes nothing at all, depends on which subdivision the lot sits in. A fenced backyard run that no neighbor or street can see is protected from an outright HOA ban under Florida's visibility statute regardless of which association is involved, but a run along a side yard visible from the street is a different conversation worth having with that specific board first.</p>"),
    ],
    "scenario": ("Say you have a fenced strip in The Willows",
                 f"<p>Say you have a fenced side strip in The Willows, four feet wide and 100 feet long along the property line, roughly 400 sq ft, worn to dirt by a pair of dogs. At the published pet range of {price('pet')} a square foot, that run prices between $4,000 and $7,200, with the typical {price('pet', True)} band putting most quotes near $4,800 to $6,400 once odor-control infill and a flush-out zone near the gate are added. A run that narrow usually costs a little more per foot than an open backyard the same size, since a crew working in a three- or four-foot lane can't move material as fast as one working in the open.</p>"),
    "faqs": [
        faq("Should a Southchase dog run get a weed barrier?", "No, skip it under pet turf. Fabric between the base and the backing traps urine at the surface instead of letting it drain into the rock, which works against the odor control a pet system is built for."),
        faq("Does a narrow side-yard dog run in Southchase need HOA approval?", "It depends on the specific phase HOA and whether the run is visible from the street or a neighboring lot; a fully screened backyard run is generally protected from a ban under Florida's HOA visibility statute either way."),
    ],
    "sources": SRC,
}

LOCAL["putting"] = {
    "title": "Southchase, FL Backyard Putting Green Installation",
    "h1": "A putting green on a Southchase lawn, not a golf lot",
    "meta": "Backyard putting green installation in Southchase, FL, a non-golf Orange County community. Contouring, sizing and 2026 pricing for a home lot.",
    "lede": capsule(f"A backyard putting green in Southchase runs {price('putting')} a square foot installed, typically {price('putting', True)}, as of September 2026. Southchase doesn't sit on a golf course the way some newer Central Florida communities do, so a green here usually competes for space with a screened pool cage and a fenced yard rather than sitting on an oversized fairway lot."),
    "sections": [
        ("Building a green where the lot wasn't drawn for one",
         "<p>Southchase's subdivisions were platted as suburban single-family and patio-home blocks, not around a golf amenity, so a putting green here almost always shares a modest backyard with a pool cage, a shed or a play area rather than sitting alone on a half-acre fairway lot. That changes the design brief: instead of a sprawling multi-hole layout, most Southchase greens are a single contoured pad, sized to what's left after the pool deck and a side setback are subtracted, with a fringe collar doing double duty as the rest of the lawn.</p>"),
        ("Contouring on soil that already sheds water",
         "<p>The sandy flatwoods base under Southchase actually helps a putting green's foundation, since the same washed crushed rock that keeps a lawn from ponding also holds a shaped contour better than a soft, organic-rich soil would. Building the subtle breaks and tiers a true roll needs takes more shaping labor on a small urban lot than on open ground, because there's less room to blend a slope into the surrounding grade before it hits a fence line or a patio edge.</p>"),
        ("Fitting a green around a pool cage instead of a fairway",
         "<p>Where a Southchase lot already has a screened pool enclosure, which is the norm on the single-family side of the community, a putting green usually ends up in the strip between the cage and the back fence, or wrapped around the cage's outside edge. That layout puts the green closer to a shared property line than a golf-community green would sit, which is one more reason a fenced-yard green rarely runs into visibility concerns under an HOA's exterior rules the way a front-yard installation would.</p>"),
    ],
    "scenario": ("Say you have a side yard in Arlington Park",
                 f"<p>Say you have a side yard in Arlington Park, 500 sq ft between the pool cage and the fence, currently dead St. Augustine that never got enough sun to hold. At the published putting range of {price('putting')} a square foot, a single contoured green with a fringe collar and two cups prices between $7,000 and $15,000, with most jobs landing in the typical {price('putting', True)} band, or $9,000 to $12,500. A tighter footprint like this one usually pushes toward the top of that range, since contouring and fringe work don't shrink proportionally just because the pad is smaller.</p>"),
    "faqs": [
        faq("Does Southchase have a golf community with putting green amenities built in?", "No. Southchase is a suburban single-family and patio-home community without a golf course, so a putting green here is a standalone backyard build rather than an extension of an existing course."),
        faq("Can a Southchase putting green share space with a pool cage?", "Yes, and it's the common layout here; the green typically runs along the outside of the screen enclosure or in the strip left over after the cage and setbacks are subtracted from the lot."),
    ],
    "sources": SRC,
}

LOCAL["playground"] = {
    "title": "Playground Turf for Southchase Family Yards",
    "h1": "Cushioned play turf for Southchase's family-heavy blocks",
    "meta": "Playground turf for Southchase, FL backyards, an Orange County community of about 16,000 residents. Shock-pad sizing and 2026 pricing.",
    "lede": capsule(f"Backyard playground turf in Southchase runs {price('playground')} a square foot installed, typically {price('playground', True)}, as of September 2026. The 2020 Census counted 16,276 residents in Southchase across 5,267 housing units, a family-dense community where a fall-rated play surface behind the house is a more common ask than in an over-55 subdivision nearby."),
    "sections": [
        ("A census-sized family community, not a retirement pocket",
         "<p>Southchase's 2020 Census count, 16,276 residents in 5,267 housing units, points to a community built and occupied by families rather than the age-restricted developments found elsewhere in Central Florida. That shows up in what gets asked for: a play surface sized to a swing set or a trampoline rather than a low-maintenance retirement-lot lawn, and a shock pad rated to the actual equipment's fall height rather than a decorative putting-green-style build.</p>"),
        ("A county sports complex nearby, built for leagues, not backyards",
         "<p>Orange County Parks and Recreation runs the South Orange Youth Sports Complex a short drive down South Orange Blossom Trail at 11800 S. Orange Avenue, eight lighted ballfields and a playground on a 28-acre site built for organized leagues. That facility handles team practice and games; it doesn't do anything for the everyday backyard play space a Southchase family still needs between practices, which is the gap a home shock-pad system fills.</p>"),
        ("Shade, heat and where a Southchase play area goes",
         "<p>Full Florida sun pushes an unshaded synthetic surface to 120 to 150°F, occasionally higher, which matters more for a play area than a plain lawn since kids sit and kneel on it rather than just walk across it. A Southchase yard with an oak or a covered patio nearby is worth siting the play pad toward, and where there's no shade available, a lighter-colored or cooling infill and a habit of hosing it down before an afternoon session both help more than most parents expect.</p>"),
    ],
    "scenario": ("Say you have a swing set in Parcel 6",
                 f"<p>Say you have a swing set behind a Parcel 6 home, with a fall zone of about 250 sq ft that's currently bare dirt where grass never came back. At the published playground range of {price('playground')} a square foot, a shock-pad system sized to that equipment's fall height prices between $2,500 and $6,250, with most Southchase jobs landing in the typical {price('playground', True)} band, or $3,000 to $4,750. Adding a cooling or antimicrobial infill for a shaded but still humid Southchase yard pushes toward the upper part of that range without changing the footprint.</p>"),
    "faqs": [
        faq("How big is Southchase, based on the last census?", "The 2020 Census counted 16,276 residents in 5,267 housing units in the Southchase census-designated place, an unincorporated Orange County community."),
        faq("Is there a public playground near Southchase for a comparison?", "Orange County's South Orange Youth Sports Complex, off South Orange Blossom Trail, has a playground alongside its ballfields, though it's built for league use rather than everyday backyard play."),
    ],
    "sources": SRC,
}

LOCAL["pool"] = {
    "title": "Pool & Lanai Turf for Southchase Screen Cages",
    "h1": "Turf where sod never grew inside a Southchase cage",
    "meta": "Pool and lanai turf for Southchase, FL screen enclosures. Drainage, gluing and the 10-foot pond setback, checked for September 2026.",
    "lede": capsule(f"Turf around a Southchase pool or inside a lanai runs {price('residential')} a square foot installed, usually toward the upper half of that range, as of September 2026. A screened pool cage is the default on Southchase's single-family lots, and grass has never grown well on the shaded, low-airflow concrete deck most of those cages enclose."),
    "sections": [
        ("Screened pools are standard here, not the exception",
         "<p>Southchase's single-family subdivisions, built mostly in the 1990s, follow the Central Florida norm of enclosing the pool in a screened cage rather than leaving it open, and that enclosure is exactly where sod struggles most: shaded by the screen roof for part of the day, starved of airflow, and boxed in by a concrete deck that never holds soil in the first place. Turf solves the sod problem entirely, since it doesn't need sun or soil to stay green.</p>"),
        ("Gluing an edge instead of nailing one",
         "<p>Turf laid over a Southchase pool deck or lanai slab can't be anchored the way an open-lawn edge is, since there's concrete underneath instead of soil, so the perimeter gets glued down instead of nailed and the whole area sits on a drainage underlay that lets rinse water and rain move out from beneath the turf rather than pooling on the slab. Skipping that underlay is the single most common reason a pool-deck turf job smells or discolors within a year.</p>"),
        ("The 10-foot rule when the pool cage backs to a pond",
         "<p>A number of Southchase lots back onto one of the stormwater ponds that feed the Shingle Creek drainage system, and where that's true, turf inside the pool cage is unaffected by the state's waterbody setback since the cage itself sits well back from the water. It's the open lawn between the cage and the pond's edge that has to stay at least 10 feet clear unless a seawall or bulkhead already separates the two, a distinction worth walking a Southchase homeowner through before pricing the whole yard as one project.</p>"),
    ],
    "scenario": ("Say you have a pool deck in Churchill Downs",
                 f"<p>Say you have a screened pool deck in Churchill Downs, 550 sq ft of concrete around the water where sod was never even attempted. At the published residential range of {price('residential')} a square foot, and pool-area jobs usually landing in the upper half of that band because of the drainage underlay and glue-down edging, a full turf-over of the deck prices between roughly $6,600 and $9,900. If the same Southchase lot backs onto a retention pond, the open side yard leading to the water gets priced separately, since the 10-foot setback there rules out turf running all the way to the bank.</p>"),
    "faqs": [
        faq("Why does pool-deck turf cost more per square foot in Southchase than an open lawn?", "It needs a drainage underlay and glued, anchored edges instead of a soil base and nailed perimeter, which adds labor even though the area is often smaller than an open backyard."),
        faq("Does the 10-foot pond setback apply inside a screened pool cage?", "No, the setback is measured from the waterbody itself. A pool cage set well back from a Southchase retention pond isn't affected; it's an open lawn running toward the water's edge that has to stop 10 feet short."),
    ],
    "sources": SRC,
}

LOCAL["str"] = {
    "title": "Southchase Vacation Rental Turf, Orange County FL",
    "h1": "Why vacation-rental turf is a small ask in Southchase",
    "meta": "Vacation rental turf for Southchase, FL homes, where Orange County zoning limits nightly rentals outside the R-3 district. What that means for 2026.",
    "lede": capsule(f"Turf for a rental home in Southchase runs {price('residential')} a square foot installed, as of September 2026. Unlike a tourist-zoned pocket of Osceola County, most of Southchase's single-family and townhome districts don't allow a whole-home nightly rental under Orange County's zoning code, so guest-turnover turf is a small piece of demand here compared with long-term rental turnover."),
    "sections": [
        ("Orange County's zoning keeps Southchase out of the nightly-rental business",
         "<p>Orange County's zoning code permits a single-family transient rental, its term for renting a home under 30 days, only inside the R-3 multiple-family district, and bars it in every other residential zoning category. Southchase's subdivisions are platted as ordinary single-family and townhome districts, not R-3, which means a compliant nightly or weekly Airbnb-style rental generally isn't an available use for a typical Southchase address, unlike parts of Osceola County built specifically for that market.</p>"),
        ("What a long-term landlord in Southchase actually asks for",
         "<p>Because Southchase skews toward annual leases rather than weekly guest turnover, the turf requests we'd expect here look more like a landlord replacing dead sod between tenants than a property manager prepping a house for back-to-back Saturday checkouts. That's a lower-wear use case than a true vacation rental, since one household a year puts far less traffic on a lawn than a new set of renters every few days.</p>"),
        ("Guest-proofing a yard even without nightly turnover",
         "<p>A Southchase rental home still benefits from the same durability a short-term property needs elsewhere: infill that resists compaction under whatever furniture or a grill ends up on it, a seam pattern that won't open under occasional heavy use, and a base built to the fuller end of the state's depth range given the community's flatwoods soil. None of that changes because the turnover is annual instead of nightly; it just means the lawn has years, not weeks, to prove the build was right.</p>"),
    ],
    "scenario": ("Say you rent out a house in Arlington Park",
                 f"<p>Say you own a rental house in Arlington Park with a 700 sq ft backyard that a tenant's dog left bare and rutted before moving out. At the published residential range of {price('residential')} a square foot, a full turf conversion between tenants prices between $5,600 and $12,600, with the typical {price('residential', True)} band putting most quotes near $7,000 to $11,200. Since Orange County's zoning doesn't allow that Arlington Park address to operate as a nightly rental, the calculation here is annual wear and re-leasing turnaround, not weekend-to-weekend guest traffic.</p>"),
    "faqs": [
        faq("Can I list a Southchase home as a nightly Airbnb?", "Generally not under Orange County's current zoning, which limits rentals under 30 days to the R-3 multiple-family district; Southchase's single-family and townhome subdivisions fall outside that district."),
        faq("Does turf pay off differently for a long-term Southchase rental than a vacation rental?", "It's less about traffic volume and more about turnaround: an annual tenant puts steady but lower wear on a lawn than a weekly vacation guest would, so the same durable build just has to last through fewer move-outs a year."),
    ],
    "sources": SRC,
}

LOCAL["commercial"] = {
    "title": "Commercial Turf for Southchase & the OBT Corridor",
    "h1": "Turf for the storefronts along South Orange Blossom Trail",
    "meta": "Commercial artificial turf for Southchase, FL properties along South Orange Blossom Trail, plus HOA common areas. Local code notes for September 2026.",
    "lede": capsule("Commercial turf in Southchase is quoted per job after a site visit, not a flat per-foot rate, since a retail pad along South Orange Blossom Trail and a phase HOA's entrance island call for different drainage, edging and traffic-rated builds. Both fall under Orange County's landscape code, reviewed by county staff rather than any one Southchase association."),
    "sections": [
        ("What actually counts as commercial in Southchase",
         f"<p>Southchase itself is almost entirely residential, but its edge along South Orange Blossom Trail carries the retail plazas, offices and drive-through pads that serve the surrounding neighborhoods, plus the clubhouses and entrance features several of Southchase's phase HOAs maintain as shared property. Both types of site answer to Orange County's commercial permitting rather than a residential process, which is a different office than the one that handles {svc('residential', 'a homeowner\'s backyard conversion')}.</p>"),
        ("Orange County's landscape-strip rule and where synthetic turf fits",
         "<p>Chapter 24 of Orange County's code bars natural turf grass from landscape strips under 7 feet wide and from interior vehicle-use areas, a rule written entirely around living grass species with no synthetic-turf section alongside it. That gap means a parking-island or narrow-strip synthetic installation on an OBT-facing Southchase property isn't clearly covered either way, which is exactly the kind of question worth routing through Permitting Services before a design gets finalized rather than assuming either answer.</p>"),
        ("Common areas run by a dozen different Southchase HOAs",
         "<p>Because Southchase is split among several separate parcel-level associations instead of one master board, a shared entrance median or clubhouse lawn in Churchill Downs answers to a different HOA than the same kind of common area in Arlington Park, and each board sets its own bid process and appearance standard. Coordinating with property management on scheduling and access matters more for this kind of job than for a single homeowner's backyard, since a common area often stays in use while work happens around it.</p>"),
    ],
    "scenario": ("Say you manage a small plaza on South Orange Blossom Trail",
                 "<p>Say you manage a small retail plaza fronting South Orange Blossom Trail near Southchase, with a 600 sq ft landscape island between two rows of parking that's struggled to hold sod under constant car exhaust and foot traffic. A commercial turf build for that island needs a heavier-duty backing rated for occasional vehicle overrun and a drainage plan tied into the lot's existing stormwater system, which is why a job like this gets priced from a site walk and a set of drawings rather than a published per-foot number. The same applies to a Southchase HOA's entrance median down the street, sized and quoted the same way.</p>"),
    "faqs": [
        faq("Does Orange County's 7-foot landscape strip rule apply to synthetic turf?", "That rule names natural grass species specifically and doesn't address a synthetic product, so it's worth confirming with the county's Zoning division before assuming either way for a narrow commercial strip."),
        faq("Who approves a common-area turf job for a Southchase HOA?", "Whichever phase-level association owns that common area, since Southchase doesn't have one master board; check with that HOA's property manager for its own bid and approval process before scheduling work."),
    ],
    "sources": SRC,
}

LOCAL["sports"] = {
    "title": "Sports & Fitness Turf, Southchase FL Backyards",
    "h1": "Home sports turf on Southchase's flat, sandy lots",
    "meta": "Sports and fitness turf for Southchase, FL backyards: bocce, batting cages and agility lanes on flatwoods sand. Quoted per job for 2026.",
    "lede": capsule("Home sports turf in Southchase, a batting cage lane, a bocce court or a sled track, is quoted per job after a site visit rather than a flat per-foot rate, since each build has its own backing spec and base depth. Southchase's flat, sandy lots make leveling straightforward; the limiting factor is usually how much yard is left once a pool cage and setbacks are subtracted."),
    "sections": [
        ("A youth sports complex nearby, built for leagues, not home training",
         "<p>Orange County Parks and Recreation's South Orange Youth Sports Complex sits a short drive from Southchase at 11800 S. Orange Avenue, eight lighted fields on a 28-acre site built for organized baseball and softball leagues. That's useful for league play, but it does nothing for the daily agility drills, batting practice or fitness routine a Southchase family wants to run without a drive and a scheduled field, which is the gap a home sports surface fills.</p>"),
        ("Leveling a lane or court on flat sand instead of a slope",
         "<p>Southchase's lots sit on flat marine-terrace flatwoods sand, mapped by the county's own soil survey, which makes grading a straight lane for a batting cage track or a bocce court more straightforward than it would be on a hillier Central Florida site. The tradeoff is drainage: the same flat sand holds water close to grade, so a base built for a home sports surface still needs the fuller-depth washed rock treatment any Southchase lawn does, just shaped level rather than sloped for a pool cage or a putting green.</p>"),
        ("Fitting a build into what's left of a modest lot",
         "<p>After a screened pool cage, a shed and the setbacks from a fence line are subtracted, a Southchase backyard often leaves a strip rather than an open field for a sports surface, which is why a batting cage lane or an agility strip is a more common ask here than a full bocce court. Sizing the build to that leftover space, rather than a standard dimension, is usually the first design conversation on a Southchase sports-turf job.</p>"),
    ],
    "scenario": ("Say you have a side yard in Churchill Downs",
                 "<p>Say you have a side yard in Churchill Downs, 12 feet wide and 40 feet long, about 480 sq ft, currently unused grass between the house and the fence. A batting-cage lane or an agility track sized to that strip needs a level, well-drained base built the same way a Southchase lawn's base is, plus a heavier-duty backing where a net anchor or agility markers get staked into the turf. Because the spec depends on which equipment goes in, pricing for a build like this comes from a site visit rather than a published square-foot range, the same way it would for a batting cage anywhere else in Central Florida.</p>"),
    "faqs": [
        faq("Is Southchase's soil good for a level sports surface?", "Yes for grading, since the flatwoods sand under most Southchase lots is flat with few slopes to correct; the base still has to be built deep enough to drain given how close the water table sits to the surface."),
        faq("Is there room in a typical Southchase yard for a full sports court?", "Often not a full-size one. Most Southchase lots have a pool cage and modest side yards, so a batting-cage lane or a narrow agility strip is more realistic than a full bocce court on a typical lot.")
    ],
    "sources": SRC,
}

LOCAL["pavers"] = {
    "title": "Turf & Pavers in Southchase, Florida",
    "h1": "Turf ribbons between Southchase's paver driveways",
    "meta": "Turf between pavers for Southchase, FL driveways and walkways, common across the community's 1990s subdivisions. Quoted per job for September 2026.",
    "lede": capsule("Turf set between pavers in Southchase, a driveway ribbon, a stepping-stone path or an edging strip, is quoted per job rather than a flat per-foot rate, since the layout and how much cutting a curved paver pattern needs both change the labor. Paver driveways and walkways are common across Southchase's 1990s and early-2000s subdivisions, and a turf strip between them beats bare sand or a gravel fill that migrates."),
    "sections": [
        ("Paver driveways are common across Southchase's older subdivisions",
         "<p>A share of Southchase's homes, built through the 1990s and into the early 2000s, use paver driveways and walkways rather than plain poured concrete, a detail found in several of the community's neighborhood real-estate profiles alongside its stucco-and-arch architectural style. Wherever pavers meet a planting bed or a driveway edge, a thin strip of exposed sand or crushed base is common, and that strip is exactly what turf ribbons are built to replace.</p>"),
        ("Why turf beats loose rock between pavers on flatwoods sand",
         "<p>Loose gravel or shell fill between pavers migrates into the joints and onto the driveway itself after a Southchase wet season, and bare sand in that same strip washes out during a heavy summer storm. A narrow turf ribbon, bonded to a compacted base the same way a full lawn is, stays put through both problems and gives the strip a finished edge without adding a mowing task to a space too narrow for a mower anyway.</p>"),
        ("Matching what a Southchase HOA already expects at the curb",
         "<p>Because paver driveways are already the norm in several Southchase phases, a turf ribbon between them tends to read as consistent with the street rather than as a change that draws HOA attention, though the specific phase association covering that address still sets its own review process for any exterior work. A sample swatch and a simple sketch showing where the ribbon runs is usually enough for that conversation.</p>"),
    ],
    "scenario": ("Say you have a paver walkway in Parcel 6",
                 "<p>Say you have a paver walkway in Parcel 6 running from the driveway to the front door, with an 18-inch-wide strip of bare, weedy sand on either side, about 120 sq ft combined. A turf ribbon along both sides of that walkway replaces the bare strip with a finished edge and stops weeds from pushing up between the paver joints from the side. Because the job is mostly cutting turf to a narrow, curved shape rather than covering open ground, pricing comes from a measured site visit rather than the same per-square-foot number a wide-open lawn would use.</p>"),
    "faqs": [
        faq("Do most Southchase homes have paver or concrete driveways?", "Paver driveways and walkways are common across several of Southchase's 1990s and early-2000s subdivisions, based on the community's own real-estate profiles, though concrete drives exist too depending on the phase and builder."),
        faq("Does a narrow turf ribbon between pavers need its own base?", "Yes, the same compacted, washed-rock base a full lawn needs, just built in a narrower trench sized to the strip between the pavers and the bed or driveway edge."),
    ],
    "sources": SRC,
}

LOCAL["repair"] = {
    "title": "Southchase Artificial Turf Repair, Orange County",
    "h1": "Fixing turf and old sprinkler conflicts in Southchase",
    "meta": "Artificial turf repair for Southchase, FL homes, where original 1990s subdivisions often carry decades-old irrigation and drainage quirks. Quoted per job.",
    "lede": capsule("Turf repair in Southchase, an open seam, a lifted edge or a section that settled, is quoted per visit rather than a flat rate, since the fix depends on what's under the surface. Southchase's oldest subdivisions date to 1989, which means irrigation systems in the 30-plus-year range are common under a lawn that's due for its first repair or its first turf conversion."),
    "sections": [
        ("Irrigation systems old enough to complicate a repair",
         f"<p>Southchase's earliest phases, chartered around 1989 by county HOA filings, put the community's oldest irrigation systems well past the 25-to-35-year mark most sprinkler lines are rated for. A repair call on an existing Southchase turf area sometimes turns up a head that was never properly capped at the original install, still connected to a zone valve that's leaking underground, which shows up as a soft, sunken patch that looks like a base failure but is actually a plumbing one. {a('/laws/florida-hb-683/', 'the state turf standard')} requires those heads capped, not just turned off, which is the fix either way once one turns up.</p>"),
        ("What a saturated water table does to a neglected seam",
         "<p>On Southchase's flatwoods soil, a seam that was taped and glued correctly holds up fine, but one that was rushed, nailed instead of properly bonded, tends to open faster here than on a well-drained ridge lot, because the base underneath stays damp longer after a storm and gives adhesive less of a chance to fully cure between rain events during a repair. That's a reason to schedule seam repairs for a dry stretch rather than the middle of a wet-season week whenever the calendar allows it.</p>"),
        ("Storm damage along a pond-fed Southchase yard",
         "<p>A Southchase lot backing onto one of the retention ponds feeding the Shingle Creek drainage system sees more standing water pressure during a tropical storm than a lot away from the water, which is where a lifted edge or a corner that pulled free of its anchoring shows up first after a hard blow. Walking that edge after a major storm and catching a lifted section early keeps the fix to a quick re-anchor instead of a wider tear-out later.</p>"),
    ],
    "scenario": ("Say you have a lifted edge in The Willows",
                 "<p>Say you have a turf lawn in The Willows, installed a decade ago, with a 6-foot section of edge that pulled loose along the back fence after a summer storm and a corner seam nearby that's started to gap. A repair visit for damage that size usually involves re-anchoring the loose edge and re-bonding the open seam rather than tearing out the whole lawn, and because the scope depends on what's found once the turf is pulled back, a repair like this is priced from that inspection rather than a published per-foot rate. Catching it within a season or two of the storm, rather than after another year of foot traffic works the gap wider, keeps the job small.</p>"),
    "faqs": [
        faq("Why do Southchase repair calls sometimes turn up an old irrigation head?", "Because many of Southchase's subdivisions date to 1989 and the early 1990s, some existing turf areas were installed before capping standards tightened, so a repair visit occasionally finds a head that was only turned off, not sealed, still leaking underground."),
        faq("Does a pond-backed Southchase lot need extra anchoring?", "It's worth checking after any tropical storm regardless of the lot, but a yard backing onto one of Southchase's retention ponds sees more standing water pressure during heavy rain, which is exactly where a loose edge tends to show up first."),
    ],
    "sources": SRC,
}

LOCAL["cleaning"] = {
    "title": "Turf Cleaning & Maintenance in Southchase, FL",
    "h1": "Keeping a Southchase lawn clean under mature oak canopy",
    "meta": "Turf cleaning and maintenance for Southchase, FL yards under decades-old oak canopy and humid flatwoods conditions. Quoted per visit, September 2026.",
    "lede": capsule("Turf cleaning in Southchase, pet-odor treatment, power brooming or an infill top-up, is quoted by yard size and condition rather than a flat rate. Southchase's oldest subdivisions have had 30-plus years to grow a full oak canopy, and a flatwoods lot that already holds humidity close to the ground gives fallen leaves and pollen more time to work into a lawn's infill before anyone notices."),
    "sections": [
        ("Three decades of oak canopy over Southchase's older blocks",
         "<p>Subdivisions chartered around 1989, Southchase's earliest phases among them, have had enough time for young landscape trees to grow into a full oak canopy, which sheds leaves and pollen onto a lawn on a schedule that a newer, less-treed subdivision doesn't deal with yet. Left alone for a season, that organic matter works its way past the fiber and starts to compost inside the infill itself, slowing the same drainage a flatwoods lot already struggles with, so a blow-off or rake-through timed to the heaviest leaf drop matters more on an older Southchase block than on a freshly built one.</p>"),
        ("Pet odor that lingers longer in humid, low-lying air",
         "<p>The sandy flatwoods ground under most of Southchase holds humidity close to the surface for longer stretches than a well-drained lot would, and that same damp air slows how fast a rinse or a treatment actually dries out of the infill after cleaning. A pet-odor treatment scheduled here benefits from a follow-up rinse timed for a dry, breezy stretch rather than the muggiest week of a Central Florida summer, since the product needs the surface to actually dry to finish working.</p>"),
        ("A rinse schedule built around a Southchase summer",
         "<p>Full sun pushes an unshaded Southchase lawn's surface into the 120-to-150°F range through summer, and a quick hose rinse drops that 30 to 50 degrees within minutes while also settling infill and clearing pollen that's built up since the last rain. There's no fixed calendar for it beyond doing it more often in July and August than in a mild spring, and doing it whenever the lawn looks dusty or starts to smell faintly of the season's pollen.</p>"),
    ],
    "scenario": ("Say you have an oak-shaded lawn in Arlington Park",
                 "<p>Say you have a turf lawn in Arlington Park, installed a few years ago under a mature oak that's grown large enough to drop a heavy layer of leaves and acorns each winter, covering roughly 1,200 sq ft of the backyard. A seasonal cleaning visit for a lawn that size typically covers a full leaf and debris clearing, a power-broom pass to lift matted fiber, and an infill top-up where years of rinsing and rain have thinned it out. Because the scope depends on how much debris has built up and how compacted the infill has gotten, a visit like this is quoted after a look at the yard rather than from a flat per-square-foot number.</p>"),
    "faqs": [
        faq("Why does an older Southchase lawn need more leaf clearing than a new one?", "Southchase's earliest subdivisions date to 1989, giving landscape trees decades to grow into a full canopy that a newer, less-treed lawn elsewhere doesn't have to deal with yet, so leaf and debris buildup happens on a faster schedule here."),
        faq("Does Southchase's humid, low-lying soil affect how a pet-odor treatment works?", "It can slow drying time, since the flatwoods ground holds moisture close to the surface, so timing a treatment and its follow-up rinse for a drier, breezy stretch helps the product finish working properly."),
    ],
    "sources": SRC,
}

LOCAL["replacement"] = {
    "title": "Turf Removal & Replacement, Southchase FL",
    "h1": "Replacing worn sod or worn turf in Southchase",
    "meta": "Turf removal and replacement for Southchase, FL lots where original 1990s St. Augustine sod has thinned under decades of shade. Quoted per job.",
    "lede": capsule("Turf removal and replacement in Southchase, whether it's decades-old St. Augustine finally giving up or an older synthetic lawn nearing the end of its life, is quoted per job after a measured site visit rather than a flat rate. Southchase's original subdivisions are old enough now that both situations show up regularly."),
    "sections": [
        ("Why original St. Augustine struggles on a 30-year-old Southchase lot",
         "<p>Sod planted when Southchase's subdivisions were first built, back through the 1990s, has spent three decades competing with landscape trees that have since grown into full shade over parts of nearly every lot, and St. Augustine thins fast once daily direct sun drops below what it needs. Add the flatwoods soil's tendency to stay damp, which favors fungus and weeds over healthy turfgrass, and a lot of Southchase's original lawns are down to bare patches and weeds in the shadier third of the yard well before the rest of the sod looks worn.</p>"),
        ("What's different when synthetic turf installed years ago gets replaced",
         "<p>A synthetic lawn installed in Southchase a decade or more ago, before the state's May 2026 material and drainage standard existed, sometimes used an infill or a backing that wouldn't meet today's rule, silica sand is still fine, but an older unwashed base underneath is a more common find on a replacement job than on a fresh install. Replacing that turf is a chance to correct the base at the same time, since tearing out the old surface already exposes whatever's underneath.</p>"),
        ("Coordinating a Southchase HOA's approval around the timeline",
         "<p>Because Southchase runs on several separate phase associations rather than one board, a replacement project's paperwork, if the specific HOA requires any for a like-for-like swap, needs to be sorted with that community's own management before demo starts, not worked out mid-project. Building in that lead time matters more here than on a first-time install, since a homeowner replacing an existing lawn is often working around a deadline, a sale, a move-in date, that a first conversion isn't.</p>"),
    ],
    "scenario": ("Say you have a failing lawn in Churchill Downs",
                 "<p>Say you have a Churchill Downs lawn where the original 1990s St. Augustine has thinned to bare dirt and weeds under a canopy that's grown in over the years, roughly 1,000 sq ft of backyard that no longer holds sod no matter how it's treated. Replacing that lawn with turf means the same base-and-turf process as a first-time conversion, sod and soil removal, a washed-rock base built to the fuller depth this flatwoods lot needs, then turf, seams and infill, which prices the same way a fresh install would rather than at a discount just because grass used to be there. The shade that killed the sod isn't a problem for turf, since it doesn't need sunlight to survive.</p>"),
    "faqs": [
        faq("Why does St. Augustine sod fail faster in older, shadier parts of Southchase?", "Landscape trees planted when Southchase's subdivisions went in during the 1990s have grown into full canopy over parts of many lots, and St. Augustine thins quickly once it loses the direct sun it needs, especially on soil that already stays damp."),
        faq("Does replacing an old synthetic lawn in Southchase cost less than a first install?", "Not usually. The base and turf both still need to be built correctly, so removing old material adds a step rather than removing one, even though the yard already had grass of some kind on it before."),
    ],
    "sources": SRC,
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
