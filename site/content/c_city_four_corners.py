# -*- coding: utf-8 -*-
"""Four Corners hub + 12 city x service pages. Unincorporated quadripoint community
where Osceola, Polk, Lake and Orange counties meet along US-27 and US-192, west of
Kissimmee. Vacation-rental belt: gated resort communities, property managers, pool
cages. Researched September 2026; see SRC below for every source used."""
from _data import CITIES
from _helpers import page, capsule, sec, table, faq, a, svc, city, post, src, ext, price
from _cityservice import cityservice_pages

SLUG = "four-corners"
FC = CITIES[SLUG]

OSCEOLA_PA = ("Osceola County Property Appraiser — parcel search", "https://www.property-appraiser.org/")
ORANGE_PA = ("Orange County Property Appraiser — parcel search", "https://ocpafl.org/")
POLK_PA = ("Polk County Property Appraiser — parcel search", "https://www.polkflpa.gov/")
LAKE_PA = ("Lake County Property Appraiser — parcel search", "https://www.lakecopropappr.com/")
WIKI_FC = ("Wikipedia — Four Corners, Florida (U.S. Census population figures)", "https://en.wikipedia.org/wiki/Four_Corners,_Florida")
OSCEOLA_STRPD = ("Osceola County — Short Term Rental Planned Development (STRPD) zoning", "https://www.osceola.org/My-Property/Zoning-and-Land-Use/Zoning-Designation/STRPD")
BNBCALC_OSCEOLA = ("BNBCalc — Osceola County short-term rental regulation guide", "https://www.bnbcalc.com/blog/short-term-rental-regulation/Osceola-County-Florida-Guide")
TOHO_AREA = ("Toho Water Authority — our service area", "https://www.tohowater.com/about-us/our-service-area")
POLK_UTIL_MANUAL = ("Polk County Utilities — Administration Manual", "https://www.polkfl.gov/wp-content/uploads/2023/09/6A-Administration-Manual-03-04-2025.pdf")
SFWMD_LOCATIONS = ("South Florida Water Management District — office locations", "https://www.sfwmd.gov/doing-business-with-us/locations")
SFWMD_ERP = ("South Florida Water Management District — Environmental Resource Permits", "https://www.sfwmd.gov/doing-business-with-us/permits/environmental-resource-permits")
REEDY_CREEK = ("Polk County Water Atlas (USF) — Reedy Creek", "https://polk.wateratlas.usf.edu/waterbodies/rivers/130021/reedy-creek")
USDA_CANDLER = ("USDA NRCS — Official Series Description, Candler series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/C/Candler.html")
USDA_IMMOKALEE = ("USDA NRCS — Official Series Description, Immokalee series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/I/IMMOKALEE.html")
OSCEOLA_PERMITS = ("Osceola County Online Permit Center", "https://permits.osceola.org/")
POLK_PERMITS = ("Polk County Building permitting", "https://www.polkfl.gov/services/building/permitting/")
LAKE_PERMITS = ("Lake County Building Services — permitting information", "https://www.lakecountyfl.gov/building-services/permitting-information")
ORANGE_PERMITS = ("Orange County Fast Track Online Services", "https://fasttrack.ocfl.net/OnlineServices/")

SRC = [
    "dep-rule", "fs125572", "fs7203045", "toho-days", "osceola-water-2026", "usda-wss",
    WIKI_FC, OSCEOLA_STRPD, BNBCALC_OSCEOLA, TOHO_AREA, POLK_UTIL_MANUAL, SFWMD_LOCATIONS, SFWMD_ERP,
    REEDY_CREEK, USDA_CANDLER, USDA_IMMOKALEE, OSCEOLA_PERMITS, POLK_PERMITS, LAKE_PERMITS, ORANGE_PERMITS,
    OSCEOLA_PA, ORANGE_PA, POLK_PA, LAKE_PA,
]

PERMIT = {"osceola": "/laws/permits/osceola-county/", "polk": "/laws/permits/polk-county/",
          "lake": "/laws/permits/lake-county/", "orange": "/laws/permits/orange-county/"}


# ============================================================== hub
def _hub():
    body = "".join([
        sec("Why one address here can answer to four different offices",
            "<p>Most of the towns covered on this site answer to a single city hall or a single county building department. Four Corners answers to whichever of four counties happens to hold the parcel, and the split is not paperwork trivia: the permit desk, the water utility, the irrigation calendar and the zoning map that governs a short-term rental all change at the county line, sometimes in the middle of the same subdivision. Add a rental-belt economy where a large share of the homes are run by a property manager rather than an owner who lives there, plus a gated HOA that reviews an exterior change before the county ever opens a file, and a plain backyard turf swap collects more approvals here than the identical job closer to downtown Kissimmee.</p>"
            + "<p>Ask a Four Corners homeowner why they searched for the best artificial turf contractor near me instead of calling the first name that came up, and the honest answer usually is not about the grass. It is that they want someone who already knows whether the lot sits in Osceola or Polk before the estimate, not an installer who has to find out on-site.</p>"),
        sec("Which of the four counties actually has your parcel",
            f"<p>Osceola, Polk, Lake and Orange counties come together at a single point near the middle of the Four Corners area, with US-27 and US-192 crossing about a mile west of that point ({ext(WIKI_FC[1], 'Wikipedia’s summary of the area')}). A subdivision that markets itself as Four Corners, or carries a Kissimmee, Davenport or Clermont mailing address, can sit in any of the four, and the mailing address never settles it. The fix is the same one used everywhere else in this service area: run the street number through the property appraiser for whichever county looks closest, and the parcel record shows the taxing jurisdiction on file. {ext(OSCEOLA_PA[1], 'Osceola')}, {ext(ORANGE_PA[1], 'Orange')}, {ext(POLK_PA[1], 'Polk')} and {ext(LAKE_PA[1], 'Lake')} counties each publish a free lookup.</p>"
            + f"<p>From there, our own permit pages cover what each office has published about synthetic turf, the phone number, and how to apply: {a(PERMIT['osceola'], 'Osceola County')}, {a(PERMIT['polk'], 'Polk County')}, {a(PERMIT['lake'], 'Lake County')} and {a(PERMIT['orange'], 'Orange County')}.</p>"),
        table("Four Corners yard types and what we do differently",
              ["Yard type", "Who usually runs it", "Where it usually sits", "What changes for us"],
              [["Gated rental-resort villa", "A property-management company on the owner's behalf", "Osceola side (communities such as Windsor Hills, Windsor Palms, Emerald Island and Windsor at Westside)", "We build around the booking calendar and the community's rental-specific design-review form"],
               ["Davenport-side resort villa", "A property-management company on the owner's behalf", "Polk side (communities such as Solterra)", "Same build, a different building department, and a Polk zoning check before we quote"],
               ["Full-time owner-occupied home", "The homeowner", "Any of the four counties", "A standard homeowner timeline with no property-manager handoff to coordinate"],
               ["Golf-course-adjacent lot", "Owner or a rental company, HOA design review", "Osceola or Polk", "A putting green or turf visible from the fairway needs the design packet before base work starts"],
               ["Pool-cage or lanai lot", "Either", "Any of the four", "Glue-down edges over the deck and a drainage underlay instead of a compacted base"],
               ["Older subdivision from the building boom", "Long-time owner or a newer rental conversion", "Any of the four", "Repair or replacement scope, plus established oaks whose drip lines now matter"]],
              "General pattern from what we see on Four Corners job sites, not a rule any HOA or county has published; a specific subdivision can differ."),
        sec("Short-term rental zoning splits at the county line too",
            f"<p>On the Osceola side, a whole-home short-term rental is not automatic just because the house next door already runs one. The county's own zoning page describes a Short Term Rental Planned Development designation created under Land Development Code Article 3.11.1, along with a mapped overlay referenced at LDC Section 3.12.2 that ties whole-property rental use to Planned Development zoning ({ext(OSCEOLA_STRPD[1], 'Osceola County’s zoning page')}). Several vacation-rental compliance guides describe that overlay as running in a band along the US-192 corridor ({ext(BNBCALC_OSCEOLA[1], 'one such compliance guide')}), which lines up with how many Four Corners resort communities operate day to day, though a specific parcel is worth confirming with Osceola's Zoning line at 407-742-0200 before anyone assumes coverage.</p>"
            + "<p>Cross into Polk County and the picture changes. As of September 2026 we found no equivalent overlay map published on the county's own site; whether a specific Davenport-side parcel's zoning district allows the use is a call to Polk's Building Division at 863-534-6080, not a published lookup.</p>"),
        sec("Which water utility and which district reaches your yard",
            f"<p>Toho Water Authority, already familiar from the rest of this site's Osceola coverage, does not stop at the county line: it serves more than 160,000 customers across St. Cloud, Kissimmee, Poinciana and unincorporated pockets of Osceola, Polk and Orange counties alike ({ext(TOHO_AREA[1], 'Toho’s own service-area page')}), which covers a meaningful share of the Osceola side of Four Corners. The Davenport side more often falls to Polk County Utilities, which runs water and wastewater to close to 68,000 accounts across the county's unincorporated communities ({ext(POLK_UTIL_MANUAL[1], 'Polk County Utilities’ own manual')}). The thin Lake County sliver near the quadripoint is small enough that a private well is at least as likely as a county connection; a seller's disclosure or Lake County Utilities settles it for a specific parcel.</p>"
            + f"<p>For anything that needs a district permit rather than a utility bill, three of the four counties share one regional office: the South Florida Water Management District's Orlando Service Center covers Orange, Osceola and Polk ({ext(SFWMD_LOCATIONS[1], 'SFWMD’s office list')}), while Lake County answers to the St. Johns River Water Management District instead. None of it changes the turf job directly, since {src('dep-rule', 'the state standard')} already bars in-ground irrigation on synthetic turf once the heads underneath are capped.</p>"),
        sec("What three decades of vacation-home building left in the ground",
            f"<p>The census counted 12,015 people in the Four Corners area in 2000, 26,116 by 2010 and 56,381 by 2020 ({ext(WIKI_FC[1], 'decennial counts cited on Wikipedia')}), and that curve is a fair proxy for when the subdivisions here went in: a wave of gated, pool-and-screen-cage vacation-home communities built from the late 1990s through the 2010s, more of them run as short-term rentals than lived in full time, plus newer construction still filling gaps along US-27.</p>"
            + f"<p>The ground under those subdivisions changes character across the same stretch. Toward the Osceola and Orange side, the flatwoods soils covered elsewhere on this site, Immokalee among them, are poorly drained Spodosols sitting on a seasonally high water table ({ext(USDA_IMMOKALEE[1], 'the official series description')}; {src('usda-wss', 'USDA Web Soil Survey')}). Moving toward the Polk side, the land climbs onto the sandier Central Florida Ridge, where the deep, excessively drained Candler series is typical ({ext(USDA_CANDLER[1], 'the official series description')}). A washed, open-graded base handles both, but a flatwoods lot needs the grade away from the house taken more seriously.</p>"
            + f"<p>Reedy Creek, a 37-mile stream that crosses both Osceola and Polk on its way through the Kissimmee Chain of Lakes system ({ext(REEDY_CREEK[1], 'the Polk Water Atlas entry')}), and the stormwater ponds nearly every one of these subdivisions was built with under a water-management-district permit ({ext(SFWMD_ERP[1], 'SFWMD’s permitting page')}), are the two features most likely to put a Four Corners lot inside the state standard's 10-foot waterbody setback or its swale exclusion.</p>"),
        sec("Two approvals, sometimes three, before a crew starts",
            f"<p>None of the four county offices above can tell a Four Corners HOA what to approve, and no HOA can override what a county permit requires. {a('/laws/florida-hb-683/', 'HB 683 and the DEP rule it produced')} set a statewide floor for material, drainage and setback rules on a covered single-family lot, and leaves ordinary permitting, plus every gated community's own architectural review, fully in place. {a('/laws/hoa-rules/', 'The statute that actually limits an association')} only protects turf that is not visible from the street or a neighboring lot, which matters more on a corner lot inside a resort community than on a quiet cul-de-sac.</p>"
            + f"<p>Bring the same packet to both approvals: a site plan, the turf and infill spec sheets, and photos of the area. {a('/tools/hoa-packet-checklist/', 'Our HOA and ARC checklist')} lays out what most Central Florida design-review forms ask for, and starting there avoids a second submission. The county side runs through whichever of {a(PERMIT['osceola'], 'Osceola')}, {a(PERMIT['polk'], 'Polk')}, {a(PERMIT['lake'], 'Lake')} or {a(PERMIT['orange'], 'Orange')} the property search above pointed to.</p>"),
        "<!--AUTO:city-services-->",
    ])
    faqs = [
        faq("How do I find out which county actually handles my Four Corners address?",
            "Run the street address through the property appraiser for whichever county looks closest; Osceola, Polk, Lake and Orange all publish a free parcel search, and the record shows the taxing jurisdiction on file. From there, our permit page for that county lists the department and phone number to call before scheduling anything."),
        faq("Can a Four Corners HOA still say no to artificial turf?",
            "For anything visible from the street or a neighboring lot, yes, since F.S. 720.3045 only protects turf that is not visible that way. A backyard behind a privacy fence is a stronger position, and most gated Four Corners communities still want a design-review submission either way."),
        faq("Does the state's May 2026 turf rule apply to a rental home here?",
            "Yes, if the lot is a single-family residence of an acre or less, which nearly every rental villa in these communities is. Being run as a short-term rental doesn't remove the protection or the material and setback rules that come with it."),
        faq("Is turf priced differently on the Polk side than the Osceola side?",
            "No. Installed turf runs the same market range across this entire service area regardless of which county line a lot falls on. What differs by side of the line is which office reviews a permit and which utility bills the water."),
        faq("My subdivision is technically in Lake County. Does anything above still apply?",
            "The state standard and the HOA statute apply the same way regardless of county. What changes is the permitting contact, Lake County Building Services, and the water district, St. Johns River rather than South Florida."),
    ]
    return page(
        "/areas/four-corners/", "city",
        "Artificial Turf in Four Corners, FL: A Four-County Yard",
        "Four Corners sits inside Osceola, Polk, Lake and Orange counties at once. What that splits between permits, HOAs and water rules for turf, as of September 2026.",
        "Turf rules change at the property line here, not the town line",
        capsule(f"Four Corners is the unincorporated stretch along US-27 and US-192, about {FC['miles']} miles west of downtown Kissimmee, where Osceola, Polk, Lake and Orange counties meet at a single point. Installed turf still runs {price('residential')} a square foot as of September 2026, but the permit desk, the water utility and the HOA that reviews the job all depend on which side of that line a lot falls on."),
        body, faqs=faqs, sources=SRC, city=SLUG, crumbs=[("Service areas", "/areas/")], crumb="Four Corners",
        related=[(PERMIT["osceola"], "Artificial turf permits in Osceola County"),
                 (PERMIT["polk"], "Artificial turf permits in Polk County"),
                 ("/areas/championsgate/", "Artificial turf in ChampionsGate"),
                 ("/areas/reunion/", "Artificial turf in Reunion"),
                 ("/areas/davenport/", "Artificial turf in Davenport"),
                 ("/artificial-turf-cost/", "Turf cost tables for Central Florida")])


HUB = _hub()

# ============================================================== local (12 services)
LOCAL = {}

# -------------------------------------------------- residential
LOCAL["residential"] = {
    "title": "Artificial Grass Installation in Four Corners, FL",
    "meta": "Artificial grass installation in Four Corners, FL runs $8–$18 a sq ft in 2026. What changes when your lot is in Osceola, Polk, Lake or Orange County.",
    "h1": "A backyard lawn swap where the county line matters more than the street",
    "lede": capsule(f"Artificial grass installed on a Four Corners lot costs about {price('residential')} a square foot, typically {price('residential', True)}, the same range as the rest of Central Florida as of September 2026. What's different here is the paperwork: a permit for the identical backyard can run through Osceola, Polk, Lake or Orange County depending on the parcel, and a full-time owner-occupied home is now the minority next to rental-run villas."),
    "sections": [
        ("How a full-time home differs from the villa next door",
         "<p>A large share of Four Corners lots are run by a property manager on behalf of an absentee owner, which makes the ordinary owner-occupied residential job something of a specialty here rather than the default. The scope is identical, sod and a few inches of soil come out, washed crushed rock goes down and compacts firm, turf gets seamed and edged, but the schedule is not built around a booking calendar or a rental company's approval chain. That usually means more flexibility on start dates and a homeowner on site to answer questions about grading, tree roots or where the irrigation heads get capped, which speeds up the parts of a job that slow down on a vacant rental.</p>"),
        ("The four-county permit question, for a plain backyard",
         f"<p>A homeowner replacing a dead lawn behind the house still has to know which building department covers the address before scheduling anything, since Four Corners can put that same project under {a(PERMIT['osceola'], 'Osceola')}, {a(PERMIT['polk'], 'Polk')}, {a(PERMIT['lake'], 'Lake')} or {a(PERMIT['orange'], 'Orange')} County depending on the parcel. None of the four has a synthetic-turf-specific ordinance published as of September 2026, so the review that applies is the county's ordinary permitting for exterior work and any plumbing permit tied to capping an irrigation head, not a turf rule written just for this project.</p>"),
        ("Soil that changes character within the same subdivision",
         f"<p>Because Four Corners straddles the edge between the flatwoods and the Central Florida Ridge, two homes a few streets apart can sit on different soil series: poorly drained Spodosols on the Osceola and Orange side, and the deeper, faster-draining Candler sand as the ground climbs toward Polk ({src('usda-wss', 'USDA Web Soil Survey')}). Either way the base is the same washed, open-graded crushed rock the state standard calls for, but a flatwoods lot needs the one-to-two-percent grade away from the house checked more carefully, since standing water has fewer places to go once it's there.</p>"),
    ],
    "scenario": ("Say you have a 950 sq ft backyard behind a full-time home",
                 f"<p>Say you have a 950 sq ft backyard behind a Four Corners home you actually live in, with the original 2005 sod thinned out by shade from a mature oak near the fence line. At the typical {price('residential', True)} range, a straightforward conversion runs roughly $9,500 to $15,200, before accounting for anything the oak's drip line adds to the layout. Because the tree sits close to the work area, the state standard's rule keeping turf out of a drip line without a certified arborist's letter applies regardless of which county the parcel falls in, and that's worth checking before a shape gets finalized. Removing the old sod and grading around the root zone rather than through it usually adds a modest amount of labor rather than changing the material cost, so the estimate mostly still comes down to square footage and access. A wider gate than the standard 36 inches, common on some of the older Four Corners lots built before golf-cart access became a selling point, can also shave a bit off the labor line since equipment moves in faster than a wheelbarrow crew.</p>"),
    "faqs": [
        faq("Does it matter which county my Four Corners lot is in if I just want a lawn swap?",
            "For price, no. For process, yes: the permit office, phone number and application portal differ by county, so confirming the parcel first saves a call to the wrong department."),
        faq("Are most Four Corners residential lots on septic or sewer?",
            "It varies by subdivision and by county; older Osceola-side communities and some rural Lake and Polk parcels run on septic, which means the state standard's requirement to keep the tank's access lid reachable applies to any turf layout near it."),
    ],
    "sources": SRC,
}

# -------------------------------------------------- pet
LOCAL["pet"] = {
    "title": "Pet Turf for Four Corners Rentals and Homes",
    "meta": "Pet turf in Four Corners, FL costs $10–$18 a sq ft in 2026. How odor-control infill works differently for a pet-friendly rental than for one household's dog.",
    "h1": "Pet turf that has to work for a rotating set of dogs, not just one",
    "lede": capsule(f"Pet turf in Four Corners runs about {price('pet')} a square foot installed, typically {price('pet', True)}, as of September 2026. A meaningful share of the area's gated communities market specific villas as pet-friendly to guests, which changes what the infill and the dog-run layout need to survive compared with a single family's yard."),
    "sections": [
        ("A pet-friendly listing puts different demands on the yard",
         f"<p>A resort villa advertised as pet-friendly sees a rotating set of guest dogs rather than one household's pet, so the {svc('pet', 'pet turf build')} has to assume unfamiliar animals with no established habits rather than a dog whose owner already knows where it likes to dig or pace the fence line. Zeolite or a coated silica sand for odor control makes more sense here than plain silica, since a listing that turns over every few days doesn't get the daily rinsing routine a resident dog owner would keep up on their own.</p>"),
        ("Dog runs in a zero-lot-line resort subdivision",
         "<p>Many Four Corners gated communities were built with narrow side yards and screened pool cages taking up most of the usable backyard, which leaves a strip along the fence line as the only realistic dog-run location. That strip often backs directly onto a neighbor's identical strip, so keeping infill and drainage contained matters more here than on a wide-open half-acre lot elsewhere in the service area. Skipping a weed barrier under pet turf, standard practice since it traps urine instead of letting it drain, applies the same way whether the yard belongs to a full-time resident or a rental company.</p>"),
        ("HOA sign-off works differently when a rental company applies",
         f"<p>A property-management company submitting a dog-run request on an absentee owner's behalf typically works from a standard packet rather than a homeowner's personal preference, which can speed up the architectural review in communities that already see similar applications often. {a('/tools/hoa-packet-checklist/', 'The same checklist')} that helps an owner-occupied application works just as well when a management company is the one filing it, since the design-review board asks the same questions either way.</p>"),
    ],
    "scenario": ("Say a pet-friendly rental needs a 240 sq ft dog run",
                 f"<p>Say a Four Corners villa marketed as pet-friendly needs a 240 sq ft strip along the side fence turned into a dedicated dog run, since the current grass has gone to bare dirt from guest dogs pacing the same path all season. At the typical {price('pet', True)} range, that comes out to roughly $2,880 to $3,840 installed, including zeolite infill for odor control and a flush-out area near the hose bib. Because the run sits inside a screened side yard shared with a neighbor's fence, drainage gets planned to keep water and infill on the property rather than sheeting toward the adjoining lot, which the state standard requires regardless of which county the villa sits in. A property manager overseeing several nearby units often bundles a request like this with routine turnover work, which is worth mentioning when scheduling since it can shift the install date around an existing service window rather than a single owner's calendar.</p>"),
    "faqs": [
        faq("Should a pet-friendly rental use different infill than a family's own dog run?",
            "Not necessarily a different type, but a rotating set of guest dogs argues for zeolite or coated sand over plain silica more often, since odor control matters more without one owner's consistent rinsing habit."),
        faq("Do Four Corners HOAs treat a dog run differently from ordinary turf?",
            "Most design-review boards ask the same questions regardless of use: material, visibility from the street, and drainage. A run tucked behind a pool cage rarely draws extra scrutiny beyond the standard application."),
    ],
    "sources": SRC,
}

# -------------------------------------------------- putting
LOCAL["putting"] = {
    "title": "Backyard Putting Greens in Four Corners, FL",
    "meta": "A putting green in Four Corners, FL runs $14–$30 a sq ft in 2026. Why contour and fringe matter more on a lot that doubles as a rental listing photo.",
    "h1": "A green that has to read well in a listing photo, not just roll true",
    "lede": capsule(f"A backyard putting green in Four Corners costs about {price('putting')} a square foot installed, typically {price('putting', True)}, as of September 2026. On a lot run as a short-term rental, the green is as much a marketing photo as a golf feature, which changes what contour, fringe and placement need to accomplish."),
    "sections": [
        ("What the best putting-green installer near you does differently for a listing",
         f"<p>What the best putting-green installer near you in Four Corners does differently on a rental property comes down to two things: contour and fringe that photograph well from the patio slider, and cups placed where they show up in a wide shot rather than tucked in a corner. A {svc('putting', 'flat, technically sound green')} can still look unremarkable in a listing photo if the fringe transition is a straight line instead of a soft curve, and on a property competing with dozens of similar rentals for a booking, that photo does real work.</p>"),
        ("Golf-adjacent lots and what the HOA wants to see",
         "<p>A number of Four Corners subdivisions were built around or near a golf course, and lots backing onto a fairway often carry design-review language about anything visible from that side of the property, greens included. A submission that shows the green's footprint, height and color, plus how it reads from the course side rather than just the street side, tends to move through review faster in these communities than a bare site plan.</p>"),
        ("Contour built for a rotating set of guests, not one golfer's habits",
         "<p>A green built for one household's owner can be shaped around that person's preferred shots; a rental-property green gets used by guests with a wide range of skill levels, most of them casual, over a single weekend. A gentler break and a slightly larger cup radius hold up better across that kind of turnover than a green designed for a single serious golfer's practice routine, and the fringe still needs the same true-roll backing and pile height regardless of who's using it that week.</p>"),
    ],
    "scenario": ("Say you have a 420 sq ft green and fringe combination",
                 f"<p>Say a Four Corners rental wants a 420 sq ft putting green with fringe added behind the pool cage, replacing a plain grass strip that never got much use. At the typical {price('putting', True)} range, that prices out to roughly $7,560 to $10,500 installed, covering the contoured green, two cups, fringe turf and edging. Because the lot backs onto a community pond, the state standard's 10-foot waterbody setback factors into how close the contouring can run to the rear property line, which is worth confirming before the layout is finalized rather than after. A property manager listing the home would typically want the green visible from the lanai in exterior photos, so placement gets planned around the camera angle a listing photographer is likely to use as much as around the terrain itself.</p>"),
    "faqs": [
        faq("Does a putting green need HOA approval on a Four Corners golf-course lot?",
            "Most golf-adjacent communities require design review for anything visible from the course or the street, greens included. A submission with the footprint, height and color usually covers what the board asks for."),
        faq("Is a smaller green worth it just for listing photos?",
            "Often yes. A modest green with clean contour and fringe photographs better than a larger one with a plain rectangular edge, and it costs less to install and maintain."),
    ],
    "sources": SRC,
}

# -------------------------------------------------- playground
LOCAL["playground"] = {
    "title": "Playground Turf for Four Corners Backyards",
    "meta": "Playground turf in Four Corners, FL costs $10–$25 a sq ft in 2026. Shock-pad sizing for a backyard play set on a rental-heavy lot, explained.",
    "h1": "A play area sized for whichever family is staying that week",
    "lede": capsule(f"Playground turf in Four Corners runs about {price('playground')} a square foot installed, typically {price('playground', True)}, as of September 2026. On a rental-run lot the play area sees children of different ages every booking, which argues for a shock pad sized to the tallest piece of equipment rather than one family's kids."),
    "sections": [
        ("Sizing the shock pad for equipment nobody chose personally",
         "<p>A backyard swing set or small climbing structure on an owner-occupied lot usually gets sized to the household's own kids, and the shock pad underneath can be sized the same way. A furnished rental typically leaves equipment in place for years across dozens of different families, so the pad thickness gets planned around the tallest reasonable fall height a listing might attract rather than the current occupant's age group, since nobody is swapping out the swing set between summer bookings.</p>"),
        ("Full Florida sun on a yard nobody's watching daily",
         "<p>A vacant rental between bookings means nobody notices right away if a play surface starts holding heat differently than expected, and Four Corners' open, low-tree-canopy subdivisions put a lot of these play areas in full sun most of the day. A cooling or lighter-toned infill matters more here than in a shaded, mature-oak neighborhood, since the first person to test the surface temperature is often a guest's child rather than someone who lives there and already knows to check.</p>"),
        ("Where a play area fits on a pool-cage lot",
         "<p>Many Four Corners lots put the pool and screen cage in the center of the usable yard, leaving a narrow strip on one side for anything else, including a play set. Fitting a play area into that leftover space usually means a smaller footprint than a standalone backyard would allow, which keeps the shock-pad calculation simple even as it limits how much equipment fits comfortably next to the cage.</p>"),
    ],
    "scenario": ("Say you have a 260 sq ft play area beside the pool cage",
                 f"<p>Say a Four Corners rental has a 260 sq ft strip beside the screen enclosure holding a small swing set with a five-foot fall height. At the typical {price('playground', True)} range, a shock-pad build for that fall height prices around $3,120 to $4,940 installed, toward the upper half of the range because the pad thickness scales with fall height rather than square footage alone. Since the strip sits in full sun most of the afternoon, a cooling infill adds a modest amount to the total but keeps the surface more usable during a Florida summer than standard silica alone. A property manager overseeing the listing would want the equipment's fall height documented alongside the shock-pad spec, since that's the number a liability question would come back to later.</p>"),
    "faqs": [
        faq("Does a rental home's play area need a bigger shock pad than a family home's?",
            "Not automatically bigger, but it's worth sizing to the tallest equipment a listing might reasonably add later rather than only what's there now, since a rental's equipment tends to stay put across many different guests."),
        faq("Does the state's turf rule limit infill on a backyard play area?",
            "Yes: rubber or other synthetic infill is allowed only within the footprint of the playground equipment itself. Everywhere else on a single-family lot, infill has to be silica, zeolite or other natural material."),
    ],
    "sources": SRC,
}

# -------------------------------------------------- pool
LOCAL["pool"] = {
    "title": "Pool & Lanai Turf in Four Corners, FL",
    "meta": "Pool and lanai turf in Four Corners, FL runs $8–$18 a sq ft in 2026. Why glue-down turf inside a screen cage is almost the standard build here.",
    "h1": "The pool-cage lot is the default here, not the exception",
    "lede": capsule(f"Turf around a Four Corners pool or inside a screened lanai costs about {price('residential')} a square foot installed, typically {price('residential', True)}, as of September 2026. Screen-enclosed pools cover most of the usable yard in these subdivisions, which makes glue-down turf over concrete closer to the standard job here than the exception it is elsewhere."),
    "sections": [
        ("Why nearly every Four Corners lot has this exact problem",
         f"<p>The gated resort communities built across Four Corners since the late 1990s were built around the pool cage, not the lawn, so the space where {svc('pool', 'turf around a pool')} usually goes is the narrow strip inside or beside the screen enclosure rather than an open backyard. Sod struggles in that strip anyway, shaded by the cage's own frame for part of the day and starved of rain the screen keeps out, which is exactly the situation this service exists for.</p>"),
        ("Glue-down edges on a lanai deck, not a compacted base",
         "<p>Concrete inside the screen enclosure needs a different build than the washed-rock base under an open-yard lawn: a drainage underlay and glued, mechanically fastened edges instead of nailed perimeter and compacted crushed rock. That distinction matters more here than in most of this service area, since a large share of the actual jobs on a Four Corners lot happen inside a cage rather than on open ground.</p>"),
        ("Reflection off the cage frame and the neighbor's slider",
         "<p>Screen cages sit close enough together in some of these denser subdivisions that a low-emissivity window on a two-story neighbor's rear wall can reflect concentrated sun onto a pool deck below, on top of whatever the cage's own aluminum frame reflects. Checking the full height of nearby glass during a site visit, not just the ground-floor sliders, catches a heat source that's easy to miss on a lot this tightly packed.</p>"),
    ],
    "scenario": ("Say you have a 380 sq ft lanai deck inside the screen cage",
                 f"<p>Say a Four Corners pool home has a 380 sq ft strip of cracked, algae-stained concrete inside the lanai between the pool and the cage wall. At the typical {price('residential', True)} range, a glue-down turf build for that area runs roughly $3,800 to $6,080, with the underlay and edge fastening making up a larger share of the labor than a comparable open-yard job of the same size would need. Because the deck sits under full screen coverage, heat is less of a concern here than on an open pool surround, though a west-facing slider on the house itself is still worth checking before the layout is finalized. Most jobs like this finish in a single day once the old concrete surface is cleaned and any low spots are shimmed level.</p>"),
    "faqs": [
        faq("Does turf inside a screen cage need the same base as an open backyard?",
            "No. Turf over existing concrete uses a drainage underlay and glued or mechanically fastened edges rather than the washed-rock base and nailed perimeter an open-ground lawn needs."),
        faq("Do Four Corners HOAs review turf inside a screen cage the same way as a front yard?",
            "Usually with less scrutiny, since a screened lanai is rarely visible from the street. F.S. 720.3045 protects anything not visible from the frontage or a neighboring parcel, which covers most enclosed pool areas."),
    ],
    "sources": SRC,
}

# -------------------------------------------------- str
LOCAL["str"] = {
    "title": "Vacation Rental Turf in Four Corners: A Property Manager's Guide",
    "meta": "Vacation rental turf in Four Corners, FL: how Osceola's rental zoning, Polk's silence and property-manager scheduling change a $8–$18/sq ft turf job.",
    "h1": "Rental turf that answers to a management company, not a resident",
    "lede": capsule(f"Turf for a Four Corners short-term rental prices the same {price('residential')} a square foot as any single-family lot, since the state's rule protects a rental home the same way it protects an owner-occupied one. What changes is who signs off: a property manager, a rental-specific HOA form, and, on the Osceola side, a zoning overlay that decides whether whole-home rental is even allowed."),
    "sections": [
        ("Ask what the best turf company near you does differently for a rental",
         f"<p>Ask what the best artificial turf company near you does differently for a Four Corners rental, and the answer usually starts with the turnover calendar, not the {svc('str', 'turf')} itself. A crew that can work inside a two-day gap between checkout and the next arrival, and coordinate a lockbox code with a property manager instead of a homeowner, fits the way most of these properties actually operate. The build underneath is the same washed-rock, capped-irrigation job as any other Four Corners lot.</p>"),
        ("Zoning decides whether the rental is legal before turf is even a question",
         f"<p>On the Osceola side, whole-home short-term rental only works inside a mapped Short Term Rental Overlay tied to Planned Development zoning, created under the county's Land Development Code ({ext(OSCEOLA_STRPD[1], 'Osceola County’s own zoning page')}). Several compliance guides describe that overlay running along the US-192 corridor ({ext(BNBCALC_OSCEOLA[1], 'one such guide')}), which covers many established resort communities but is worth confirming for a specific parcel with the county's Zoning line before assuming coverage. Cross into Polk County and there's no equivalent published overlay map as of September 2026, so a Davenport-side rental's zoning gets checked with Polk's Building Division directly.</p>"),
        ("Working through a management company instead of an owner",
         f"<p>Most Four Corners rental jobs get scheduled through a property-management company holding the calendar for several units at once, rather than an owner who lives nearby. That company usually wants the state's irrigation-capping requirement documented in writing for whoever maintains the yard afterward, and often bundles the turf work into a maintenance window that already has a cleaning crew or a pool-cage repair scheduled, similar to how {city('davenport', 'Davenport')} and {city('championsgate', 'ChampionsGate')} rentals nearby tend to be run.</p>"),
    ],
    "scenario": ("Say a management company wants an 820 sq ft rental yard converted",
                 f"<p>Say a property-management company overseeing a Windsor Palms-area rental wants the full 820 sq ft backyard converted before the next high-season booking window. At the typical {price('residential', True)} range, that prices out to roughly $8,200 to $13,120 installed. Because the home operates as a licensed short-term rental, the manager will likely ask for the capped-irrigation note and the manufacturer's material statement filed with the property records rather than handed to whoever happens to be on-site that day, since the person checking on the yard next season may not be the same person who signed off on the job. Scheduling around a vacancy gap during rainy season usually means building in a day or two of slack for storms, the same buffer any Four Corners rental install needs regardless of which county the parcel sits in.</p>"),
    "faqs": [
        faq("Can any Four Corners home legally operate as a short-term rental?",
            "Not automatically. On the Osceola side, whole-home rental requires the parcel to fall inside a mapped overlay tied to Planned Development zoning; on the Polk side, it depends on the parcel's zoning district since no published overlay map exists as of September 2026."),
        faq("Who handles the HOA paperwork for a rental turf job, the owner or the property manager?",
            f"Either can, and most gated communities accept a submission from a management company acting on the owner's behalf. {a('/tools/hoa-packet-checklist/', 'The same checklist')} applies regardless of who files it."),
        faq("Does a rental home get a different price than an owner-occupied home for the same yard?",
            "No. The market range is the same regardless of how the property is used; what changes is scheduling around bookings and who signs the paperwork."),
    ],
    "sources": SRC,
}

# -------------------------------------------------- commercial
LOCAL["commercial"] = {
    "title": "Commercial Turf for Four Corners Clubhouses",
    "meta": "Commercial turf for Four Corners resort clubhouses and amenity centers, priced per job after a site visit. What HOAs and property managers ask for.",
    "h1": "Amenity centers built to look good in a rental brochure",
    "lede": capsule("Commercial turf for a Four Corners clubhouse, amenity center or gated entrance is priced per job after a site visit rather than a flat rate per square foot, since scope varies with drainage, hardscape and how much of the area guests actually see. Nearly every resort community in the area maintains at least one shared amenity building that turf can serve."),
    "sections": [
        ("Clubhouse grounds that dozens of rental owners share",
         f"<p>A Four Corners resort community's clubhouse, pool deck and entrance sign typically serve every unit in the subdivision at once, which puts commercial turf here in a different category from a single homeowner's backyard: the {svc('commercial', 'HOA or its management company')} is the client, not one resident, and the decision usually goes through a board vote rather than an individual application. Wear patterns concentrate around high-traffic paths, the walk from the parking area to the pool gate especially, more predictably than on a residential lot with one household's habits.</p>"),
        ("Entrance features and gatehouse landscaping",
         "<p>Many of these communities put real effort into the guard gate and entrance monument, since that's the first thing an arriving guest photographs for a group chat before checking into the rental. Turf around a gatehouse or entrance feature answers to the same state material and drainage standard as a residential lawn once the area is a covered use, but a formal geometric layout around signage or fountains often calls for more precise cutting and seaming than an open lawn does.</p>"),
        ("Coordinating with an HOA's existing landscape contractor",
         "<p>A resort community usually already has a landscape crew on a standing contract for the mowed common areas, and a commercial turf project has to work around that crew's schedule rather than replace it outright, since turf typically covers specific features, not the entire property. Confirming who maintains what after installation, the landscape contractor or a separate turf-care visit, avoids a gap where nobody is responsible for brushing or infill top-ups on a shared amenity area.</p>"),
    ],
    "scenario": ("Say an HOA wants turf around a 1,600 sq ft clubhouse pool deck",
                 f"<p>Say a Four Corners HOA wants the 1,600 sq ft perimeter around its clubhouse pool deck converted from thinning sod that never recovers from foot traffic between pool parties. Because this is a shared amenity rather than a single-family lot, pricing comes from a site walk and drawings rather than the residential per-square-foot range, and the board typically wants a formal quote with material specs attached to its meeting minutes before approving the expense. The state's turf standard's single-family, one-acre-or-less scope doesn't cover this kind of common-area project the way it covers a resident's backyard, so the HOA's own governing documents and whichever county's land-development code applies carry more weight here than on a residential job. A phased approach, doing the highest-traffic section first and the rest the following season, is common when a board is managing the cost against dues.</p>"),
    "faqs": [
        faq("Does the state's turf standard cover an HOA clubhouse or amenity center?",
            "No. Rule 62-308.100 applies to single-family residential lots of an acre or less. A shared clubhouse or common area answers to the county's ordinary land-development code and the HOA's own governing documents instead."),
        faq("Who approves a commercial turf project at a Four Corners resort community?",
            "Typically the HOA board or its property-management company, often after a vote at a board meeting, rather than an individual resident application."),
    ],
    "sources": SRC,
}

# -------------------------------------------------- sports
LOCAL["sports"] = {
    "title": "Sports & Fitness Turf in Four Corners, FL",
    "meta": "Sports and fitness turf in Four Corners, FL is priced per job after a site visit. Bocce courts, agility lanes and sled tracks on larger, non-rental lots.",
    "h1": "Sports turf for the lots that aren't run as a listing",
    "lede": capsule("Sports and fitness turf, a bocce court, an agility lane or a home-gym sled track, is quoted per job in Four Corners rather than a flat per-square-foot rate, since layout and base work vary with the feature. This service tends to land on larger, owner-occupied lots away from the densest rental clusters, where there's room for a dedicated feature beyond the pool cage."),
    "sections": [
        ("Where a sports feature actually fits here",
         f"<p>The tightest Four Corners resort subdivisions leave little yard beyond the pool cage, which pushes most requests for a {svc('sports', 'dedicated sports surface')} toward the larger residential lots scattered through the area's non-gated or lower-density pockets, closer to how a lot in {city('clermont', 'Clermont')} or a spread-out rural parcel would be laid out. An agility lane or a short bocce court needs a rectangle of open ground that a zero-lot-line rental villa simply doesn't have.</p>"),
        ("A home-gym sled track on a lot with mixed soil",
         "<p>A straight-line sled track or turf lane for resistance work needs a firm, flat base more than it needs drainage speed, which matters on the Osceola and Orange side of Four Corners where the native soil holds water longer than the sandier ground toward Polk. Building the base slightly higher than grade on the flatwoods side keeps the lane usable the morning after a summer storm instead of soft underfoot.</p>"),
        ("Bocce and other shared-yard features on a full-time home",
         "<p>Unlike a rental property where every square foot of yard gets weighed against booking appeal, an owner-occupied Four Corners lot can dedicate a corner to a feature the household actually uses regularly, a bocce court along a side fence or an agility lane for a dog, without worrying about how it photographs for guests. That changes the design conversation from what looks good in a listing to what holds up under the same few people using it often.</p>"),
    ],
    "scenario": ("Say you have room for a 300 sq ft bocce court",
                 "<p>Say a Four Corners homeowner on a larger, non-rental lot has a flat side yard with room for a 300 sq ft bocce court, currently unused St. Augustine that struggles in partial shade anyway. Because this service is priced per job, the estimate depends on whether the court needs a contained sand-and-turf bocce surface with edging or a simpler open lane, plus how much grading the existing slope needs to get level. A site visit and a drawing showing the court's exact footprint and orientation relative to the house give a firmer number than a square-footage guess would, since a dedicated sports surface carries more spec variation than a plain residential lawn of the same size.</p>"),
    "faqs": [
        faq("Is sports turf common on Four Corners rental properties?",
            "Less common than on owner-occupied lots, since most rental villas use every available yard square foot for pool, lanai or listing photos rather than a dedicated sports feature."),
        faq("Does a bocce court or agility lane need HOA approval?",
            "Usually yes if it's visible from the street or a neighboring lot, following the same design-review process as any other yard feature in a Four Corners gated community."),
    ],
    "sources": SRC,
}

# -------------------------------------------------- pavers
LOCAL["pavers"] = {
    "title": "Turf Between Pavers in Four Corners, FL",
    "meta": "Turf between pavers in Four Corners, FL is priced per job. Why paver driveways and walkways are nearly universal across the area's resort subdivisions.",
    "h1": "Paver ribbons are the rule here, not an upgrade",
    "lede": capsule("Turf set between pavers, driveway ribbons, stepping-stone paths or a paver-and-grass border, is priced per job in Four Corners rather than a flat rate, since the layout depends on the paver pattern already in place. Paver driveways and walkways are close to standard across the area's resort-built subdivisions, which makes this pairing more common here than in an older, plain-concrete neighborhood."),
    "sections": [
        ("Why nearly every Four Corners driveway already has pavers",
         f"<p>The gated resort communities built across Four Corners from the late 1990s onward were laid out with paver driveways and walkways as a standard feature rather than an upgrade, which means the question for {svc('pavers', 'turf between pavers')} here is usually how to fill an existing joint pattern rather than whether to install pavers in the first place. A narrow turf ribbon down the center of a paver driveway, or along its edges where grass used to struggle against the hardscape, is a common request precisely because the pavers were already there.</p>"),
        ("Stepping-stone paths in a pool-cage side yard",
         "<p>The same narrow side yards that push pool cages into most of the usable backyard also leave a stepping-stone path as the most practical way to get from the driveway gate to the lanai door. Turf filled between those stones drains faster than the bare sand or mulch that's often there instead, and it holds up better underfoot than loose gravel when guests are wheeling luggage through on a check-in day.</p>"),
        ("Matching turf color and grain to an existing paver tone",
         f"<p>Because so many Four Corners homes already have a specific paver color, tan, gray or a red-brown blend, chosen when the subdivision was built, matching turf shade and grain direction to what's already there matters more for how the finished job looks than it would on a blank-slate yard. A community such as {city('celebration', 'Celebration')}, built with its own strict paver and hardscape palette, shows how much a mismatched turf tone can stand out against an established streetscape.</p>"),
    ],
    "scenario": ("Say you have a 110 sq ft ribbon down a paver driveway",
                 "<p>Say a Four Corners driveway has a 4-foot-wide, roughly 110 sq ft strip of dead grass running down its center between two paver borders, a common layout in the area's older resort-built subdivisions. Because this service is priced per job rather than a flat per-square-foot rate, the estimate depends mainly on how the strip ties into the existing paver edge, whether a bender-board or a mow-strip transition is needed, and how much of the strip needs new base material versus a simple turf-over-sand fill. A narrow ribbon like this usually finishes in well under a day once the paver edges are cleaned and squared, since the footprint is small even though the detail work at the border takes more care than an open lawn would.</p>"),
    "faqs": [
        faq("Do paver driveways need a different turf backing than a lawn?",
            "The turf itself is the same permeable-backed product either way; what changes is the edge detail, since a paver border needs a clean, secured transition rather than a nailed perimeter into open ground."),
        faq("Does the state's turf rule apply to a small paver-ribbon project?",
            "Yes, if it's part of a single-family residential lot of an acre or less. The material, infill and drainage standards apply the same way to a 100 sq ft ribbon as to a full backyard."),
    ],
    "sources": SRC,
}

# -------------------------------------------------- repair
LOCAL["repair"] = {
    "title": "Artificial Turf Repair in Four Corners, FL",
    "meta": "Artificial turf repair in Four Corners, FL is priced per visit with a minimum charge. Common failures on rental-run yards, from lifted seams to melted patches.",
    "h1": "Repairs that show up in a guest review before an owner sees them",
    "lede": capsule("Turf repair in Four Corners, lifted edges, open seams, a melted patch or a low spot that holds water, is priced per visit with a typical minimum service charge, the same as anywhere else in this service area. What's different is how the damage gets noticed: on a rental-run lot, the first sign is often a guest's comment rather than an owner walking the yard."),
    "sections": [
        ("Wear patterns from turnover, not one family's habits",
         f"<p>A yard used by a rotating set of vacationing guests wears differently than one used by a single household: heavier traffic on the direct path between the driveway and the pool gate, occasional damage from rolling luggage or a dropped grill, and less consistency in who reports a problem right away. That makes {svc('repair', 'seam and edge repair')} on a Four Corners rental more often reactive to a specific complaint than scheduled around a homeowner's own observation, which is why a property manager's response time to a guest report matters as much as the repair itself.</p>"),
        ("Reflection damage in a densely built resort subdivision",
         f"<p>Some of the more tightly packed Four Corners communities, similar to what shows up in {city('championsgate', 'ChampionsGate')}'s newer construction, put two-story homes close enough together that a low-emissivity window on one house can melt a patch of turf on the neighboring lot's pool deck, not just its own. Tracing a melted spot back to a reflection source sometimes means checking a different property's windows than the one the turf sits on, which is a step easy to skip on a routine repair call.</p>"),
        ("Base failures that go unnoticed on a vacant week",
         "<p>A base that settles unevenly or drains too slowly shows the same symptoms anywhere, standing water and a soft spot underfoot, but a Four Corners rental sitting empty between bookings can go a week or two before anyone notices. By the time it shows up as a guest complaint, the problem has usually been developing quietly for a while, which argues for catching it at a scheduled turnover cleaning rather than waiting for a report.</p>"),
    ],
    "scenario": ("Say a guest reports a lifted seam and a small melted patch",
                 "<p>Say a Four Corners rental's cleaning crew flags a 6-foot lifted seam near the pool cage door and a roughly 8 sq ft melted patch on the deck after a guest mentions both in a checkout note. Repair pricing here runs per visit with a minimum charge rather than a per-square-foot rate, since remobilizing a crew for a small job costs largely the same regardless of the exact footage involved. The melted patch is worth tracing to its heat source, a low-e window on the house itself or a neighboring two-story unit, before patching, since fixing the turf without addressing the reflection just invites the same damage again next summer. Scheduling around an existing vacancy gap keeps the fix from cutting into the next booking, which a property manager will usually want built into the timeline from the first call.</p>"),
    "faqs": [
        faq("Why do Four Corners rentals seem to need more repairs than owner-occupied homes?",
            "Not necessarily more, but issues get reported differently: a rotating set of guests notices and mentions problems a resident might live with longer, which can make repair requests feel more frequent even when total wear is similar."),
        faq("Is there a minimum charge for a small repair visit?",
            "Yes, most installers, including us, charge a minimum service fee since a crew and a trip out are the same cost whether the fix takes ten minutes or an hour."),
    ],
    "sources": SRC,
}

# -------------------------------------------------- cleaning
LOCAL["cleaning"] = {
    "title": "Turf Cleaning for Four Corners Rental Turnovers",
    "meta": "Turf cleaning and maintenance in Four Corners, FL is priced by visit and yard size. How rental turnovers change the cleaning schedule versus a family lawn.",
    "h1": "Cleaning scheduled around checkout, not the calendar",
    "lede": capsule("Turf cleaning in Four Corners, power brooming, pet-odor treatment and infill top-ups, is priced by yard size and how long it's been since the last visit, the same as elsewhere in this service area. On a rental-run property, the natural trigger for a cleaning visit is the turnover schedule rather than a fixed monthly date."),
    "sections": [
        ("Turnover cleaning as the built-in maintenance check",
         f"<p>Most Four Corners rentals already have a cleaning crew coming through between every guest stay, which makes that turnover the most reliable moment to catch a flattened path or debris buildup before it becomes a bigger {svc('cleaning', 'turf-cleaning')} job. A quick blower pass and a look at infill depth during a routine turnover costs far less than letting the same issue sit through several bookings unnoticed on a property nobody visits between guests.</p>"),
        ("Debris load in a growing resort corridor",
         "<p>Ongoing construction along the US-27 and US-192 corridors, still adding new resort phases and retail in parts of Four Corners, tracks more dust and debris onto nearby yards than a fully built-out, established neighborhood would see. A yard near an active construction zone benefits from a closer look at infill and drainage than one further from the current building activity, since dust settling into infill over time changes how the surface drains.</p>"),
        ("Scheduling around booking size, not a fixed date",
         "<p>A property that just hosted a large group, a family reunion or several couples sharing a big villa, is worth a closer inspection than one coming off a quiet weekend for two, since more people moving through the yard puts more stress on infill and edges in a few days than routine use does over weeks. Tying a deeper cleaning to booking size rather than a flat quarterly schedule catches the wear that actually happened.</p>"),
    ],
    "scenario": ("Say a rental needs cleaning after a slow month, then a big group",
                 "<p>Say a Four Corners rental's 700 sq ft yard has gone a slow month with light bookings, then suddenly hosts a 12-guest group over a holiday week. Pricing for this service runs by yard size and time since the last visit rather than a flat per-square-foot number, so the slow month likely calls for a light standard visit, while the post-group cleaning afterward is a heavier job: brushing down flattened paths, checking infill depth near the pool gate where most of the foot traffic concentrated, and treating any pet odor if the group brought a dog. A property manager scheduling both visits around the actual booking pattern, rather than a fixed monthly date, gets more value from the same number of cleanings over a season.</p>"),
    "faqs": [
        faq("Should cleaning be scheduled with every guest turnover or on a fixed schedule?",
            "A fixed schedule works for a steady-occupancy property, but tying at least a quick inspection to every turnover catches problems faster on a Four Corners rental with variable booking patterns."),
        faq("Does nearby construction really affect how often turf needs cleaning?",
            "It can. A yard close to an active building site tends to collect more dust in its infill than one in a fully built-out area, which shows up as slower drainage if it's not addressed."),
    ],
    "sources": SRC,
}

# -------------------------------------------------- replacement
LOCAL["replacement"] = {
    "title": "Turf Removal & Replacement in Four Corners, FL",
    "meta": "Turf removal and replacement in Four Corners, FL prices close to a new install minus reusable base. What to expect on a lawn from the 1990s–2000s boom.",
    "h1": "Replacing turf and sod that are both original to the boom years",
    "lede": capsule("Replacing worn turf or an old, thinning lawn in Four Corners prices close to a new installation minus whatever base can be reused, the same rule that applies across this service area. Many of the area's homes date to the vacation-home building wave of the late 1990s through the 2010s, which means original turf or builder sod alike is often past due."),
    "sections": [
        ("Original turf from the early resort-building years",
         f"<p>A subdivision built during Four Corners' fastest growth years, the population here roughly doubled twice between 2000 and 2020, sometimes had turf or sod installed as part of the original build rather than added later, and that first-generation product is now old enough on many lots to be past its expected life. {svc('replacement', 'Replacing it')} means checking whether the original base is still sound before assuming a full rebuild is needed, since a well-built base from even 15 or 20 years ago can sometimes stay in place under new turf.</p>"),
        ("What years of guest traffic did that a family lawn wouldn't see",
         f"<p>A lawn or turf area that's spent most of its life on a rental property has absorbed a different kind of wear than the same age of turf on an owner-occupied home in {city('reunion', 'Reunion')} or a similar community: heavier concentrated traffic on guest paths, more exposure to rolling luggage and pool gear, and less consistent care between different management companies over the years. That uneven wear pattern often means one section of the yard needs full replacement while the rest of the same-age turf still has useful life left.</p>"),
        ("Drip lines and setbacks that weren't a factor when it went in originally",
         "<p>A tree planted small when a subdivision was new has often grown enough by now that its drip line reaches into an area the original turf or sod never had to account for. A replacement project is the natural point to correct that, keeping the new turf outside the tree's current root zone rather than repeating whatever the original 1990s or 2000s layout got away with before the rule existed.</p>"),
    ],
    "scenario": ("Say you have 1,100 sq ft of original turf from a 2007 build",
                 f"<p>Say a Four Corners rental still has roughly 1,100 sq ft of its original 2007 turf, now matted flat, faded and pulling loose at several seams after nearly two decades of guest traffic. Replacement here prices close to a new {price('residential')} installation minus whatever the existing base turns out to be worth reusing, so the first step is checking whether that base has held its grade and compaction or whether water has been getting underneath it for years. If the original base is sound, the job skips most of the excavation and grading that a first-time install needs; if it's settled or holding water, that part gets rebuilt before new turf goes down, which changes the total more than the turf itself does.</p>"),
    "faqs": [
        faq("Is replacing old turf cheaper than a first-time installation?",
            "Sometimes, if the original base is still sound and just needs new turf on top. If the base has failed, replacement costs close to the same as starting from bare ground, since the base work gets redone either way."),
        faq("Do older Four Corners subdivisions have turf rules that changed since they were built?",
            "The state standard adopted in 2026 applies to any covered lot regardless of when the subdivision was built, so a replacement project is a natural point to bring an older layout in line with today's drip-line and setback rules."),
    ],
    "sources": SRC,
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
