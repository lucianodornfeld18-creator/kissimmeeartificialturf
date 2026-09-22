# -*- coding: utf-8 -*-
"""Narcoossee, FL (tier 2, unincorporated Osceola County) — hub + six city x service pages.
Osceola County Building Department permitting, Toho Water Authority schedule and SFWMD Kissimmee
Basin facts are reused from site/content/c_permits.py and c_counties.py (same facts, fresh sentences).
Soil series, growth figures, subdivisions and the county park below were researched fresh for this
module in September 2026; sources are listed inline and in SRC."""
from _helpers import page, capsule, sec, table, faq, a, svc, city, post, src, ext, price
from _cityservice import cityservice_pages

SLUG = "narcoossee"

OSCEOLA_PERMIT_ROUTE = ("/laws/permits/osceola-county/", "Osceola County’s permit rules for turf")
HOA_ROUTE = ("/laws/hoa-rules/", "What a Florida HOA can and can’t restrict")
HB683_ROUTE = ("/laws/florida-hb-683/", "HB 683 and DEP Rule 62-308.100")
COST_ROUTE = ("/artificial-turf-cost/", "Turf cost tables for Central Florida")

TOHO_SERVICE = ("Toho Water Authority — our service area", "https://www.tohowater.com/about-us/our-service-area")
SFWMD_KISS = ("South Florida Water Management District — Upper Kissimmee Basin water supply plan", "https://www.sfwmd.gov/our-work/water-supply/upper-kissimmee")
NARCOOSSEE_OSD = ("USDA NRCS — official series description, Narcoossee series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/N/NARCOOSSEE.html")
SMYRNA_OSD = ("USDA NRCS — official series description, Smyrna series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/S/SMYRNA.html")
MYAKKA_OSD = ("USDA NRCS — official series description, Myakka series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/M/MYAKKA.html")
WIKI_NARCOOSSEE = ("Wikipedia — Narcoossee, Florida", "https://en.wikipedia.org/wiki/Narcoossee,_Florida")
WPR_OSCEOLA = ("World Population Review — Osceola County, Florida population and growth, 2026", "https://worldpopulationreview.com/us-counties/florida/osceola-county")
LAKE_AJAY = ("Florida Neighborhood Realty — Lake Ajay Village, Narcoossee", "https://www.floridaneighborhoodrealty.com/lake-ajay-village-narcoossee-homes-sale/")
GROWTHSPOTTER = ("GrowthSpotter — Central Florida’s fastest-growing neighborhoods", "https://www.growthspotter.com/2021/09/08/where-the-homes-are-a-look-at-central-floridas-fastest-growing-neighborhoods/")
EAGLE_CREEK = ("Eagle Creek Golf Club — course details", "https://www.eaglecreekorlando.com/course-details/")
NARCOOSSEE_PARK = ("Osceola County Parks — Narcoossee Community Center and Park", "https://www.osceola.org/Community/Parks-and-Public-Lands/Find-a-Park-or-Facility/Narcoossee-Community-Center-and-Park")

SRC = [("Osceola County Building Department — Online Permit Center", "https://permits.osceola.org/"),
       ("Osceola County Property Appraiser — parcel search", "https://www.property-appraiser.org/"),
       TOHO_SERVICE, SFWMD_KISS, NARCOOSSEE_OSD, SMYRNA_OSD, MYAKKA_OSD, WIKI_NARCOOSSEE, WPR_OSCEOLA,
       LAKE_AJAY, GROWTHSPOTTER, EAGLE_CREEK, NARCOOSSEE_PARK]

# ============================================================== hub
HUB = page(
    "/areas/narcoossee/", "city",
    "Artificial Turf Installation in Narcoossee, FL (2026)",
    "Synthetic turf for Narcoossee, FL homes between East Lake Toho and Lake Nona, on wells, septic tanks and Osceola County’s flatwoods sand. Checked September 2026.",
    "Turf for Narcoossee’s acreage lots and lake edges",
    capsule(f"Kissimmee Artificial Turf installs synthetic lawns, pet turf and putting greens along the Narcoossee Road corridor in northeast Osceola County, where installed turf runs {price('residential')} per square foot as of September 2026. Narcoossee sits about 11 miles from our Kissimmee shop, on ground that ranges from quarter-acre lake lots to multi-acre parcels marketed for horses and small farms, between East Lake Tohopekaliga and the Lake Nona line."),
    "".join([
        sec("An unincorporated stretch between two lakes and a boomtown",
            f"<p>Narcoossee has never incorporated. It's a community in northeast Osceola County strung along Narcoossee Road, County Road 15, between the east shore of East Lake Tohopekaliga and the Orange County line, where the last stretch of pasture gives way to {city('lake-nona', 'Lake Nona')}'s office towers. English settlers platted the place as a citrus colony in the 1880s; hard freezes and a 1908 drought scattered most of the original families within a generation, and the grove land they left behind is what's selling as home sites today ({ext(WIKI_NARCOOSSEE[1], 'a history the town keeps on record')}).</p>"
            + f"<p>Osceola County doesn't track Narcoossee as its own census place, so there's no official population count for it the way there is for {city('st-cloud', 'St. Cloud')} or {city('kissimmee', 'Kissimmee')}. What is countable is the county around it: Osceola added roughly 15,800 residents between 2024 and 2025, one of the faster growth rates of any county in the country, and Narcoossee Road carries a fair share of that traffic toward the Lake Nona line ({ext(WPR_OSCEOLA[1], 'Osceola County’s 2026 population estimate')}).</p>"),
        sec("Wells and septic tanks outnumber Toho hookups out here",
            f"<p>Toho Water Authority's service area covers most of Osceola County and its crews maintain lines under Narcoossee Road itself, which is why the newer gated communities that sit directly on the corridor, Lake Ajay Village among them, run on Toho water and sewer ({ext(TOHO_SERVICE[1], 'Toho’s service-area page')}). Move off the paved corridor onto the larger, older parcels east of it, and a private well and a septic tank are at least as common as a utility meter; Toho doesn't publish a lot-by-lot boundary, so the honest answer for any one address is to run it through the utility's own map or call before assuming either way.</p>"
            + "<p>That mix changes a turf job less at the sprinkler than at the tank. A well-fed yard was never tied to an in-ground zone, so there's no head to cap under a new lawn there, but the state's rule still requires a septic tank's pump-out lid to stay reachable once turf and base go in, and plenty of Narcoossee's larger lots have never had that lid mapped since the day the tank was set. We locate it before rock goes into the ground, on either water source.</p>"),
        sec("East Lake Toho, Lake Ajay and the wetter edges of a lot",
            f"<p>Two named waterbodies frame the area: East Lake Tohopekaliga along the west side, inside the South Florida Water Management District's Upper Kissimmee Basin planning area, and the much smaller Lake Ajay, tucked behind the gates of Lake Ajay Village off North Narcoossee Road ({ext(SFWMD_KISS[1], 'SFWMD’s Kissimmee Basin plan')}; {ext(LAKE_AJAY[1], 'the Lake Ajay Village community')}). A lot backing onto either one carries the state's 10-foot setback from the ordinary or mean high water line, waived only where a seawall or bulkhead already separates yard from water, and the same rule keeps turf out of any drainage swale or ditch a property drains through on its way to one of the two lakes.</p>"),
        table("Narcoossee yard types and what we build differently",
              ["Lot type", "What's usually there", "What changes for the crew"],
              [["Acreage east of Narcoossee Road", "Private well, septic tank, loose cross-fencing left from a grove or pasture", "No head to cap; the septic lid gets staked before any rock goes down"],
               ["Lake Ajay Village and similar gated lake lots", "Toho water and sewer, a community dock, a fenced yard behind a newer house", "The state's 10-ft lake setback plus a gate-width check for equipment access"],
               ["New construction filling in from the Lake Nona side", "Builder sod over compacted fill, narrow side yards", "A fuller base depth, since fill packed for a foundation drains worse than the sand it replaced"],
               ["Older grove-era homesteads near the historic core", "Mature oak cover, a mix of well and county water depending on the block", "A drip-line check first, since decades-old canopy usually reaches further than it looks"]],
              "Checked against Toho's service-area map, Osceola County's Land Development Code and the developments named above, September 2026."),
        sec("Who reviews a Narcoossee permit",
            f"<p>There's no Narcoossee city hall to call, because there's no Narcoossee city. {a('/laws/permits/osceola-county/', 'Osceola County’s Building Department')} reviews a permit here the same way it would in Poinciana or Harmony, through the county's Accela-based Online Permit Center rather than a counter of its own. Osceola County's Land Development Code doesn't mention synthetic turf either way, so a Narcoossee lawn conversion answers to the county's ordinary landscape and drainage rules plus the state's May 2026 turf standard, not a local turf ordinance.</p>"
            + f"<p>An HOA is a separate matter. Lake Ajay Village and the newer gated communities filling in from the Lake Nona side run their own architectural review, and {a('/laws/hoa-rules/', 'Florida’s visibility statute')} only protects turf an ARC can't see from the street or a neighboring lot; a fenced backyard on a quarter-acre gated lot is a different case from an open acreage parcel with no fence line at all. Neither the county nor an HOA can go further than {a('/laws/florida-hb-683/', 'HB 683 and the DEP’s turf rule')} allow on a covered single-family lot.</p>"),
        "<!--AUTO:city-services-->",
    ]),
    faqs=[
        faq("What should I ask to find the best artificial turf installer near me in Narcoossee?",
            "Ask whether the crew already knows to check a well-versus-Toho address before quoting irrigation work, whether the quote names base depth and material, and whether anyone's asked where the septic tank sits. Those three questions separate an installer who's worked this corridor from one who hasn't."),
        faq("Is Narcoossee its own town, or part of unincorporated Osceola County?",
            "Unincorporated. Narcoossee has no city hall, no mayor and no city-specific code; it's part of Osceola County, and the county's Building Department handles permits the way it would for any other unincorporated address in the county."),
        faq("How do I find out if my Narcoossee address is on Toho water or a private well?",
            "Toho Water Authority's interactive service-area map is the fastest check, since the utility's lines run along parts of Narcoossee Road but stop well short of many parcels behind it. A blank result on the map usually means a well and septic system, which is worth confirming before a quote."),
        faq("How far is Narcoossee from Kissimmee and from Lake Nona?",
            "About 11 miles from our Kissimmee shop by straight line. Lake Nona sits at the other end of Narcoossee Road, close enough that its retail and apartment growth has spilled across the county line into Narcoossee's north end."),
        faq("Does the state's 10-foot water setback apply to a dock on Lake Ajay or East Lake Toho?",
            "The setback measures from the ordinary or mean high water line, not from a dock structure itself, and it doesn't apply at all where a seawall or bulkhead already separates the yard from the water. Most Lake Ajay lots have neither a seawall nor a dock footprint large enough to change that math."),
    ],
    sources=SRC, city=SLUG, crumbs=[("Service areas", "/areas/")], crumb="Narcoossee",
    related=[("/areas/osceola-county/", "Artificial turf across Osceola County"), OSCEOLA_PERMIT_ROUTE,
             ("/areas/lake-nona/", "Artificial turf in Lake Nona"), ("/areas/st-cloud/", "Artificial turf in St. Cloud"),
             COST_ROUTE],
)

# ============================================================== LOCAL
LOCAL = {
    "residential": {
        "title": "Artificial Grass Installation in Narcoossee, FL",
        "meta": "Synthetic lawn installation for Narcoossee's half-acre-to-multi-acre lots, on well water, septic tanks and Osceola County's flatwoods sand. Checked September 2026.",
        "h1": "Turf built for Narcoossee's wells, septic tanks and big yards",
        "lede": capsule(f"Installed artificial grass runs {price('residential')} per square foot in Narcoossee as of September 2026, the same Central Florida range whether the lot is a quarter acre in Lake Ajay Village or several acres of former grove land off Narcoossee Road. Most of the ground here maps to the Narcoossee, Smyrna or Myakka soil series, all of it slow to drain once the summer water table climbs."),
        "sections": [
            ("Grading for a water table that climbs every summer",
             f"<p>Two named soil series cover most of the area: the Narcoossee series itself, established here in 1976 and mapped on the low sandy knolls threaded through the flatwoods, and Smyrna sand in the lower ground between them, also first classified in Osceola County that same year ({ext(NARCOOSSEE_OSD[1], 'the Narcoossee series description')}; {ext(SMYRNA_OSD[1], 'the Smyrna series description')}). Both hold a water table that climbs to within two or three feet of the surface for months at a stretch, and Smyrna's lower pockets sit wetter still.</p>"
             + f"<p>That's shallow enough that a thin four-inch rock layer only just clears the wet season's high point, which is why crews working this ground lean toward the deeper end of what the state allows rather than splitting the difference, especially at a yard's low corner, where Myakka sand, the true depression soil in the mix, tends to take over ({ext(MYAKKA_OSD[1], 'the Myakka series description')}).</p>"),
            ("A well and a septic tank change the install, not the price",
             "<p>A house on a private well was never tied to an in-ground zone the way a Toho-fed subdivision lot is, so there's no sprinkler head to cap before turf goes down on most of Narcoossee's larger parcels. What doesn't change is the septic side of the state's rule: the tank's pump-out lid has to stay reachable once the lawn is finished, and on an older acreage lot that lid was often never marked after the original install, buried since under decades of mowing.</p>"
             + f"<p>We ask for a pump-out receipt or a call to whoever last serviced the tank before laying out where turf can go, and build the base up to the lid's edge rather than over it. A newer, {a('/laws/hoa-rules/', 'HOA-governed')} lot in a community such as Lake Ajay Village skips this step but adds the irrigation-capping one instead.</p>"),
            ("Why an acreage lot usually turfs a yard, not a property",
             f"<p>A multi-acre parcel off Narcoossee Road isn't priced or built as though the whole property needs to be lawn. Most owners define a yard close to the house, porch to fence line or porch to the first line of old grove trees, and leave the rest as pasture, mowed field or native scrub. That decision changes the math more than the soil does: a defined yard costs the same per square foot whether the surrounding parcel runs a fifth of an acre or five, and the crew still measures, grades and bases only the section that gets turfed.</p>"
             + f"<p>Open acreage does add one detail a tighter {city('buenaventura-lakes', 'Buenaventura Lakes')} lot skips: without a next-door fence line a few feet away, edge anchoring along an open pasture boundary has to hold against wind with nothing nearby to break it.</p>"),
        ],
        "scenario": ("Say you have a 2.5-acre lot off Narcoossee Road",
                     f"<p>Say a 2.5-acre property off Narcoossee Road carries a 1980s home, a detached barn and a septic tank whose lid nobody's seen in a decade. The owner wants a defined 1,400 sq ft yard between the back porch and an existing wood fence, leaving the rest as mowed field. At the published {price('residential')} per square foot range, that prices between roughly $11,200 and $25,200, with most bids on ground like this landing near $14,000 to $22,400.</p>"
                     + "<p>Getting there means locating the septic lid first, building the base to the fuller four-inch depth for the site's Myakka-adjacent low corner, and using the existing fence line as the turf's edge anchor instead of a fresh paver border. The barn and the rest of the field stay exactly as they are.</p>"),
        "faqs": [
            faq("Do I need a permit to convert a Narcoossee lawn to turf?",
                f"{a('/laws/permits/osceola-county/', 'Osceola County’s Building Department')} reviews it, since Narcoossee has no city hall of its own. Its Land Development Code doesn't name synthetic turf, so the application goes through ordinary landscape and drainage review plus the state's rule rather than a local turf-specific standard."),
            faq("Does a five-acre lot cost more to turf than a quarter-acre one?",
                "Not if the finished yard is the same size. Price follows the square footage that actually gets turfed, not the acreage around it, so a 1,200 sq ft yard prices the same whether it sits on a fifth of an acre in Lake Ajay Village or in the middle of five acres of former grove land."),
        ],
        "sources": SRC,
    },
    "pet": {
        "title": "Narcoossee Pet Turf: Dog Runs for Wells & Gated Lots",
        "meta": "Pet turf and dog runs for Narcoossee, from fenced Lake Ajay Village yards to multi-acre paddocks on slow-draining flatwoods sand. Checked September 2026.",
        "h1": "Dog runs for Narcoossee's paddocks and gated backyards",
        "lede": capsule(f"Pet turf in Narcoossee runs {price('pet')} per square foot installed as of September 2026, the same whether it's a small fenced yard in a gated lake community or a working dog run on a multi-acre property off Narcoossee Road. The area's flatwoods soil holds water long after a storm, which is exactly the problem pet turf's drainage backing is built to solve."),
        "sections": [
            ("A paddock-sized run on an open Narcoossee lot",
             "<p>A property with an existing horse paddock or a fenced pasture corner already has the perimeter a dog run needs, and reusing that fence line instead of building a new one is the first cost a bigger Narcoossee lot can save on a pet project. What it can't skip is the base: an open run this size sees more standing water after a storm than a small backyard patch does, simply because there's more roof and ground draining toward it, so the crew grades a fall line out of the run before rock or turf go in.</p>"
             + "<p>Owners with working or hunting dogs on acreage properties also ask about a flush-out zone near the gate, a section built with extra drainage so a daily hose-down doesn't pond at the entrance the way it would on plain grass.</p>"),
            ("Small, fenced backyards behind a Lake Ajay Village gate",
             f"<p>Newer gated lots along the Narcoossee Road corridor run smaller and tighter than the acreage behind them, with a fenced backyard closer to {city('lake-nona', 'Lake Nona')}-style subdivision proportions than to open pasture. That's a better fit for standard pet turf than it sounds: a small, shaded, mostly-mud strip behind a screen door is the classic case where zoysia or Bahia can't keep up with a dog's traffic pattern, while a fast-draining pet system handles daily use without the bare patches.</p>"
             + f"<p>{svc('pet', 'Pet turf')} in a gated community still answers to that community's own architectural review, separate from the county, so we send the infill spec sheet along with the permit paperwork when a submittal is required.</p>"),
            ("Keeping the run clear of the septic drain field",
             "<p>On a well-and-septic property, the drain field is often the flattest, most convenient-looking stretch of yard, which makes it a tempting spot for a dog run and the wrong one to dig into without checking first. The state's turf rule requires keeping the septic tank's own pump-out lid reachable, and a run built over or right up against the drain field itself risks compacting ground that needs to stay permeable for the system to keep working.</p>"
             + "<p>We map both the tank and the field before laying out a run, and shift the footprint rather than build over either one, even when that means a slightly narrower or offset shape than the owner first pictured.</p>"),
        ],
        "scenario": ("Say you have a 900 sq ft run on a well-and-septic property",
                     f"<p>Say a 3-acre homestead off Narcoossee Road has an existing 40-by-60-ft fenced paddock the owner wants to convert into a 900 sq ft dog run near the gate, keeping the rest as open pasture. At the published {price('pet')} per square foot range, that prices between about $9,000 and $16,200, with most bids landing near $10,800 to $14,400.</p>"
                     + "<p>Before laying out the run, the crew maps the septic tank and drain field, which sit about 30 ft from the fence line, and shifts the run's footprint slightly to stay clear of both. Zeolite infill goes in at the upper end of the standard rate, since a working dog on a rural lot tracks more debris into a run than a backyard pet does.</p>"),
        "faqs": [
            faq("Can pet turf handle Narcoossee's wet flatwoods soil better than grass does?",
                "Usually, yes, once the base is built to drain. Perforated pet-turf backing moves water at over 30 inches an hour, but on Narcoossee's Myakka and Smyrna soils the base underneath still needs the fuller depth and a positive grade, or a run built on a low corner will hold water the same way a bare dirt one would."),
            faq("Does a dog run need its own fence, or can we reuse an existing paddock fence?",
                "An existing paddock or pasture fence works fine as the run's perimeter as long as it's tight to the ground, since the fence itself isn't part of what the turf install has to meet a standard for. What matters more is where the fence line sits relative to the septic system before any digging starts."),
        ],
        "sources": SRC,
    },
    "putting": {
        "title": "Backyard Putting Greens Near Eagle Creek, Narcoossee",
        "meta": "Backyard putting and chipping greens for Narcoossee's larger lots near Eagle Creek Golf Club, built on the area's flatwoods sand. Checked September 2026.",
        "h1": "Putting greens for Narcoossee's golfers and big side yards",
        "lede": capsule(f"A backyard putting green in Narcoossee runs {price('putting')} per square foot as of September 2026. The area sits minutes from Eagle Creek Golf Club off Narcoossee Road, and the multi-acre lots common east of the corridor leave room for a full green with a chipping pad that a standard subdivision yard usually can't fit."),
        "sections": [
            ("Room to build a real green, not a putting strip",
             f"<p>A quarter-acre subdivision lot usually limits a green to a single contour and a couple of cups tucked against a fence line. A multi-acre Narcoossee property removes that ceiling: with side yard and open field to work with, a green can carry two or three pin positions, a proper fringe transition and a chipping pad set back far enough to actually swing into it, rather than the compressed layout {svc('putting', 'a tight urban yard')} forces.</p>"
             + "<p>The tradeoff is that a bigger green needs a bigger, flatter subbase, and on ground with any natural roll to it, that means more grading before rock goes down than the green itself will ever show once it's finished.</p>"),
            ("Golfers near Eagle Creek asking for a practice green at home",
             f"<p>Eagle Creek Golf Club sits off Narcoossee Road, and its membership base is part of why putting greens come up more often here than in a non-golfing part of the county ({ext(EAGLE_CREEK[1], 'Eagle Creek’s course details')}). A member who plays a course with fast, true greens usually wants the same speed at home, which is less about turf brand and more about how flat and firm the subbase compacts before the carpet ever goes down.</p>"
             + "<p>We ask about stimp speed preference and slope reading before ordering material, since a green built for casual chipping and one built to mimic tournament-speed greens use different pile heights and the same base method underneath either way.</p>"),
            ("Building a stable green on ground with a seasonal high water table",
             f"<p>Narcoossee's flatwoods soil holds a water table that can sit within two to three feet of the surface for months, which is a problem for a putting green in a way it isn't for a plain lawn: a green that settles unevenly reads false, and a homeowner notices a bad roll long before they'd notice a lawn's minor dip. We compact the rock base in two full passes rather than one on any Narcoossee green, and check level with a laser rather than eyeballing it, since the margin for error on a green is a fraction of what it is on a residential lawn.</p>"),
        ],
        "scenario": ("Say you belong to Eagle Creek and want a green at home",
                     f"<p>Say a homeowner who plays Eagle Creek most weekends wants a 500 sq ft green with a two-cup layout and a small fringe apron, sited on the flat side yard of a two-acre Narcoossee lot. At the published {price('putting')} per square foot range, that prices between about $7,000 and $15,000, with most builds like this landing near $9,000 to $12,500.</p>"
                     + "<p>Because the lot's soil maps to Smyrna sand with a high seasonal water table, the crew builds the subbase four inches deep in two compacted lifts instead of one, and lasers the surface level before the carpet goes down. The result holds a truer, more predictable roll through a full rainy season than a shallower build would.</p>"),
        "faqs": [
            faq("Does a Narcoossee putting green need a permit separate from a lawn?",
                "No. Osceola County reviews a putting green the same general way it reviews any other synthetic turf project, through ordinary landscape and drainage permitting rather than a golf-specific rule, since the county's code doesn't single out putting greens."),
            faq("How much bigger can a green be on an acreage lot than in a typical subdivision?",
                "There's no fixed limit, since price scales with square footage rather than lot size. What acreage actually buys is layout freedom: room for multiple cups, a real chipping approach and a fringe transition that a standard quarter-acre backyard usually has to compress or skip."),
            faq("Do I need a well-water hookup to rinse a putting green?",
                "A hose bib is all rinsing requires, and a private well feeds one exactly the way a Toho meter does. The green's irrigation heads, if any existed before, get capped the same as they would on a Toho-served lot."),
        ],
        "sources": SRC,
    },
    "playground": {
        "title": "Narcoossee Playground Turf for Acreage & New-Build Yards",
        "meta": "Playground turf for Narcoossee families, from acreage lots near the county park to new construction off Narcoossee Road. Checked September 2026.",
        "h1": "Play surfaces for Narcoossee yards, on any lot size",
        "lede": capsule(f"Playground turf in Narcoossee runs {price('playground')} per square foot as of September 2026. Osceola County's own Narcoossee Community Center and Park, off Rambling Road, gives families here a public playground to compare a home surface against, though our work only covers the equipment and infill on private property."),
        "sections": [
            ("What the county park does that a backyard doesn't have to",
             f"<p>Narcoossee Community Center and Park, run by Osceola County off Rambling Road, has its own playground, courts and open field for the neighborhood ({ext(NARCOOSSEE_PARK[1], 'the county’s park page')}). A public park's surface answers to playground-equipment codes and maintenance schedules a private backyard never has to meet, so a home installation is simpler by design: it's sized to one family's equipment, not a rotation of park visitors, and the fall-height math only has to cover whatever swing set or slide actually sits on the property.</p>"
             + "<p>What carries over from the public standard is the idea itself, a shock-absorbing surface under the equipment rather than bare sand or mulch that compacts and washes out.</p>"),
            ("Where the equipment can go on an open Narcoossee lot",
             "<p>A multi-acre property gives a family more choice in where a swing set or a play structure lands than a subdivision yard does, but that freedom comes with more things to check first: a well head, a septic tank and drain field, and any live oak's drip line all rule out a spot before the fun part of picking a location starts. The state's rule that keeps synthetic infill out from under a mature canopy without an arborist's letter applies here exactly as it would on a smaller lot.</p>"
             + "<p>Once a clear spot is confirmed, the shock pad gets sized to the equipment's actual fall height, not a generic depth, since a taller slide or swing set needs more cushioning than a toddler-scale climber does.</p>"),
            ("Newer family lots filling in from the Lake Nona side",
             f"<p>The newer construction spreading into Narcoossee's north end from the {city('lake-nona', 'Lake Nona')} side tends to bring young families with it, and those lots come with smaller, fenced backyards where a play area has to share space with a patio and whatever else the builder's landscape plan already covers. On a lot this size, playground turf usually means a defined pad under one or two pieces of equipment rather than a full-yard surface, bordered by regular {svc('residential', 'residential turf')} for the rest of the lawn.</p>"),
        ],
        "scenario": ("Say you have a 300 sq ft play area under a swing set",
                     f"<p>Say a family on a newer Narcoossee lot near the Lake Nona line wants a 300 sq ft play area under a swing set with an 8-ft fall height, bordered by a paver edge separating it from the rest of the backyard lawn. At the published {price('playground')} per square foot range, that prices between about $3,000 and $7,500, with most jobs like this landing near $3,600 to $5,700.</p>"
                     + "<p>The shock pad underneath gets sized to that 8-ft fall height rather than a standard residential depth, and the pad's edge meets the paver border with a glued, trimmed seam so the two surfaces sit flush. The rest of the yard turfs separately at the residential rate.</p>"),
        "faqs": [
            faq("Is the Narcoossee Community Center and Park's playground surface the same product we'd install at home?",
                "No, and it doesn't need to be. A county park's playground surface answers to public-facility standards and heavier daily traffic; a home installation is sized to a family's own equipment and fall heights, which is a smaller and simpler build even though the underlying idea, a shock pad under the equipment, is the same."),
            faq("Can playground turf go near a well or septic system on an acreage lot?",
                "It can, once the well head and the septic tank and drain field are mapped and the equipment is sited clear of them. We check both before laying out a play area on any well-and-septic property, the same way we would before a lawn or a dog run."),
        ],
        "sources": SRC,
    },
    "pool": {
        "title": "Pool & Lanai Turf in Narcoossee, FL",
        "meta": "Turf for Narcoossee pool cages and open pool decks, from new construction near Lake Nona to older acreage homes. Checked September 2026.",
        "h1": "Pool-area turf for Narcoossee's cages and open decks",
        "lede": capsule(f"A Narcoossee pool surround bills out under the same {price('residential')} per square foot figure as a plain lawn, as of September 2026. Newer screened lanais on the Lake Nona side of Narcoossee and older, uncaged pool decks on acreage lots both show up here, and each needs a different drainage detail at the deck edge."),
        "sections": [
            ("Screened pool cages on newer Narcoossee lots",
             f"<p>New construction filling in toward the {city('lake-nona', 'Lake Nona')} line brings the same pool-cage layout common across Central Florida subdivisions: a narrow, shaded strip of grass between the pool deck and the screen wall that struggles for sun and drainage in equal measure. Turf inside a cage like this needs a drainage underlay where it meets the concrete deck, since that transition is where water collects if the base isn't feathered to the slab's exact height.</p>"
             + f"<p>{svc('pool', 'Pool-area turf')} in one of these communities usually pairs with an HOA architectural submittal, the same review any other exterior change in a gated Narcoossee subdivision would need.</p>"),
            ("Open, uncaged pool decks on acreage properties",
             "<p>A lot of Narcoossee's older or larger properties never had a screen enclosure built over the pool, which means the deck sits exposed to full sun, wind and whatever debris blows in from a nearby grove or pasture edge. Turf around an open deck takes more direct sun exposure than a caged one, and it also collects more leaf litter and grass clippings from the surrounding open field, so the infill needs a periodic rinse and brush more often than a shaded, enclosed lanai would.</p>"
             + "<p>The base build itself doesn't change with the cage or without it; what changes is how often an owner needs to hose the surface down to keep it looking and draining the way it did on install day.</p>"),
            ("Grading the deck edge on Narcoossee's flat, wet ground",
             f"<p>Because so much of the area sits on Narcoossee and Smyrna sand with a high seasonal water table, positive drainage away from a pool deck matters more here than on a well-drained ridge lot. The crew grades the turf strip to fall away from both the house and the pool deck itself, toward whatever low point the property already drains to, rather than assuming the sand underneath will carry water away on its own the way it might on {city('winter-garden', 'a west Orange County ridge lot')}.</p>"),
        ],
        "scenario": ("Say you have a 250 sq ft pool-cage strip",
                     f"<p>Say a newer Narcoossee home near the Lake Nona line has a 250 sq ft strip of grass inside its pool cage, currently struggling under the screen's shade. At the published {price('residential')} per square foot range, that prices between about $2,000 and $4,500, with most jobs like this landing near $2,500 to $4,000.</p>"
                     + "<p>The base gets feathered to match the pool deck's exact height at the transition, with a drainage underlay set in at that seam so water doesn't pool where turf meets concrete. The HOA submittal for the gated community goes in alongside the county paperwork, since both approvals are needed before the crew starts.</p>"),
        "faqs": [
            faq("Does an open, uncaged pool deck in Narcoossee need different turf than a screened one?",
                "The turf product and base are the same either way. What changes is upkeep: an uncaged deck takes more direct sun and more debris from a nearby field or grove edge, so the infill and surface need a hose rinse more often than a shaded, screened lanai would."),
            faq("Can turf go right up to a pool's coping on an acreage lot?",
                "Yes, the same way it would on any other pool deck, with the base feathered to the coping's height and the edge trimmed tight. What differs on an open deck is that there's no screen wall to anchor turf against, so the perimeter relies on the pool deck itself and a nailed or glued edge instead."),
        ],
        "sources": SRC,
    },
    "repair": {
        "title": "Turf Repair in Narcoossee: Storm & Septic-Area Fixes",
        "meta": "Turf repair for Narcoossee lawns, dog runs and putting greens, from storm-lifted edges on open lots to septic-adjacent seam fixes. Checked September 2026.",
        "h1": "Fixing turf on Narcoossee's open, wind-exposed lots",
        "lede": capsule("Turf repair in Narcoossee is quoted after photos or a site visit, the same as anywhere else in our service area, since a lifted edge, a wrinkle and a wind-torn seam each call for a different fix. Open acreage lots without a neighboring fence line to break the wind account for more of the storm-related calls we'd expect here than in a tighter subdivision."),
        "sections": [
            ("Wind lifting an edge with nothing nearby to block it",
             "<p>A turf edge anchored along an open pasture boundary has less shelter from wind than one tucked against a fence, a hedge or a neighboring house, and a summer storm crossing open Narcoossee farmland can catch a corner that was nailed rather than properly bonded. The fix depends on how the edge was built originally: a nailed perimeter usually just needs to be re-set and, where the ground allows, upgraded to a paver or bender-board border that holds better against repeat wind than fasteners alone.</p>"
             + "<p>Checking the full perimeter after a named storm, not just the corner that visibly lifted, catches a second weak spot before it becomes its own call a season later.</p>"),
            ("Repairing near a septic tank or a well head",
             "<p>A repair on an acreage lot sometimes means reopening ground close to a septic tank or a well casing, especially if the original install didn't map either one precisely. Before cutting into an existing seam near either feature, we confirm the tank lid and any wellhead clearance again, since a repair crew working from an old memory of where things sit runs the same risk a first-time install would.</p>"
             + "<p>That extra step adds a little time to a repair near either feature, but it's cheaper than damaging a septic line or a well casing that a shortcut would have avoided.</p>"),
            ("What a rushed subdivision install shows up as later",
             f"<p>Turf installed quickly on the newer lots filling in from the {city('lake-nona', 'Lake Nona')} side sometimes skipped a full two-pass compaction to meet a builder's closing schedule, and that shortcut tends to show up as a shallow settling dip near a corner or a seam a year or two later rather than on day one. A repair in that case usually means pulling back the affected section, adding and recompacting base material, and reseaming rather than patching over a dip that will only return.</p>"),
        ],
        "scenario": ("Say a summer storm lifted a 200 sq ft section",
                     "<p>Say a summer storm crossing an open Narcoossee lot lifted about 200 sq ft of turf along a pasture-facing edge that had been nailed rather than bonded with a paver border. A site visit would check whether the base underneath moved or just the edge fastening failed, since those two problems call for different fixes and different pricing.</p>"
                     + "<p>If the base held and only the perimeter lifted, the fix is usually a re-anchored edge with an upgraded border added at the weak stretch. If storm water also washed base material out from under the turf itself, that section needs to come up, get re-based and get reseamed, which is a larger job than an edge fix alone.</p>"),
        "faqs": [
            faq("Why do open Narcoossee lots seem to need more storm repairs than gated subdivisions?",
                "Mostly exposure. A fence, a hedge or a neighboring house breaks wind before it reaches a turf edge in a tighter subdivision lot; an open pasture boundary on an acreage property doesn't offer that shelter, so a nailed-only edge there takes more direct wind load during a named storm."),
            faq("Can a repair crew accidentally damage a septic system on an acreage lot?",
                "It's avoidable, which is why we re-confirm the tank lid and any well clearance before cutting into an existing seam near either one, rather than relying on notes from the original install. That check adds a little time but protects a system that's expensive to repair on its own."),
        ],
        "sources": SRC,
    },
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
