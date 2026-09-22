# -*- coding: utf-8 -*-
"""Azalea Park, FL (unincorporated Orange County CDP, tier 2, with edges close to Orlando's city
limits). Permit, water and soil facts for Orange County are reused from site/content/c_permits.py
(orange_county()) and c_counties.py (orange_co()) — same facts and URLs, fresh sentences. Newly
researched for this module, checked September 2026: Census 2020 figures for Azalea Park CDP, the
neighborhood's 1952 Phillips Properties development history, and its Lake Underhill/Lake Barton
edge."""
from _helpers import page, capsule, sec, table, faq, a, svc, city, county, post, src, ext, price
from _cityservice import cityservice_pages

SLUG = "azalea-park"
SRC = [
    "dep-rule", "fs125572", "fs7203045", "usda-wss", "census-acs",
    ("Orange County Property Appraiser — parcel search", "https://ocpafl.org/"),
    ("Orange County Fast Track Online Services (Permitting Services & Division of Building Safety)", "https://fasttrack.ocfl.net/OnlineServices/"),
    ("Orange County Utilities — watering restrictions", "https://www.orangecountyfl.net/watergarbagerecycling/wateringrestrictions.aspx"),
    ("St. Johns River Water Management District — Orange County", "https://www.sjrwmd.com/district-counties/orange-county/"),
    ("U.S. Census Bureau QuickFacts — Azalea Park CDP, Florida", "https://www.census.gov/quickfacts/fact/table/azaleaparkcdpflorida/PST045225"),
    ("Wikipedia — Azalea Park, Florida (geography and 2020 Census demographics)", "https://en.wikipedia.org/wiki/Azalea_Park,_Florida"),
    ("Orlando Memory (Orange County Regional History Center) — Azalea Park: An Illustrated History", "https://orlandomemory.org/places/azalea-park-an-illustrated-history/"),
    ("Orange County Government Newsroom — A Neighborhood You Should Know: Azalea Park", "https://newsroom.ocfl.net/2020/02/a-neighborhood-you-should-know-old-and-new-merge-to-make-azalea-park-an-enduring-neighborhood/"),
    ("City of Orlando — Lake Underhill Park", "https://www.orlando.gov/Parks-the-Environment/Directory/Lake-Underhill-Park"),
    ("Orange County Water Atlas — Lake Underhill", "https://orange.wateratlas.usf.edu/waterbodies/lakes/140473/lake-underhill"),
    ("USDA NRCS Official Series Description — Immokalee series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/I/IMMOKALEE.html"),
    ("USDA NRCS Official Series Description — Myakka series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/M/MYAKKA.html"),
]

HUB = page(
    "/areas/azalea-park/", "city",
    "Artificial Turf Installers Serving Azalea Park, FL",
    "Artificial turf in Azalea Park, FL: a 1950s Orange County neighborhood near Lake Barton, its mixed Orlando/county permit lines, and 2026 pricing.",
    "Synthetic grass on Azalea Park's postwar streets",
    capsule(f"Azalea Park went up starting in 1952 as one of Orange County's first large tract subdivisions, and its concrete-block ranch homes on tight, established lots are about 18 miles from Kissimmee. A residential turf installation runs {price('residential')} a square foot here, {price('residential', True)} on most yards, no different from the rest of Central Florida this September. What changes block to block is which office reviews the work."),
    "".join([
        sec("Azalea Park's postwar streets, from Alder to Zinnia",
            f"<p>Phillips Properties began building Azalea Park in 1952 on the site of a former private grass airstrip, turning it into an 1,100-home subdivision with its own shopping center, a public pool and five churches inside a couple of years ({ext('https://orlandomemory.org/places/azalea-park-an-illustrated-history/', 'an illustrated history from Orlando Memory')}). Streets carry the plant names the developer gave them, Camellia, Dogwood, Lantana, Oxalis, Zinnia among others, and the concrete-block ranch construction typical of Florida tract building in that era still defines most of the neighborhood today.</p>"
            + "<p>By the 2020 Census, Azalea Park held 14,141 residents on just over 3 square miles, one of the more densely built communities in our service area, with a median age under 35 and roughly two in nine residents under 18. That's a lot of yards doing double duty as everyday play space, not just a lawn to keep green.</p>"
            + "<p>What does the best artificial turf contractor near Azalea Park actually do differently here? Mostly, size the job to a real 1950s lot rather than to a showroom photo of somebody else's quarter-acre, and check the parcel before quoting anything that touches a property line.</p>"),
        sec("Where Orange County's rule ends and Orlando's begins",
            f"<p>Azalea Park's official boundary, Colonial Drive to the north, Goldenrod Road to the east, Curry Ford Road to the south and either Semoran Boulevard or Lake Barton and Orlando Executive Airport to the west, is drawn by the Census Bureau as unincorporated territory. In practice, Orlando has annexed pieces of this same area at different points since the 1950s, so a specific parcel can sit inside city limits even on a block that otherwise reads as county. A search on the {ext('https://ocpafl.org/', 'Orange County Property Appraiser')} site settles it before anyone applies for a permit.</p>"
            + f"<p>Where a parcel comes back unincorporated, Orange County's Chapter 24 landscape code applies, the same code that defines turf only as a living grass species and says nothing about a synthetic product either way. That office, Permitting Services and Division of Building Safety, takes calls at 407-836-5550, with applications filed through {ext('https://fasttrack.ocfl.net/OnlineServices/', 'Fast Track Online Services')}; {a('/laws/permits/orange-county/', 'our Orange County permit page has the full writeup')}. A parcel that comes back inside Orlando answers to that city's own, separate turf ordinance instead.</p>"),
        sec("Water days and the district behind them",
            f"<p>Orange County Utilities holds its unincorporated customers, Azalea Park among them, to one watering day a week for most of the year and two once daylight saving time begins, with nothing permitted between 10 a.m. and 4 p.m. ({ext('https://www.orangecountyfl.net/watergarbagerecycling/wateringrestrictions.aspx', 'current restrictions')}); a parcel on the Orlando side of the boundary instead follows the Orlando Utilities Commission's own separate schedule. Either way, {a('/laws/florida-hb-683/', 'the May 2026 state turf rule')} bars watering a synthetic lawn through an in-ground system once it's capped, so the specific utility only matters for the rest of the yard.</p>"
            + f"<p>The whole neighborhood sits within the St. Johns River Water Management District's coverage of Orange County ({ext('https://www.sjrwmd.com/district-counties/orange-county/', 'SJRWMD district coverage')}), which sets watering restrictions and wetland rules separately from, and on top of, the state turf standard's own 10-foot waterbody setback.</p>"),
        sec("Azalea Park lot types and how we treat them",
            "<p>Four patterns cover most of the calls we get from this neighborhood, and the office that reviews the paperwork often matters as much as the yard itself.</p>"
            + table("Azalea Park yard types and what we do differently",
                    ["Lot", "The 1950s original", "What changes with turf", "Who signs off"],
                    [["Standard Phillips-era concrete-block ranch lot", "A narrow strip of grass tight to the neighbors on both sides", "Full or partial conversion trimmed to the property's real line", "Orange County if unincorporated; Orlando's own desk if the parcel checks out inside city limits"],
                     ["Lot along the Lake Barton edge, northwest corner of the CDP", "Grass running down toward the waterline", "Turf stops at least 10 ft back unless a seawall's already there", "State waterbody setback, DEP Rule 62-308.100"],
                     ["Interior lot two or three streets off Semoran", "A single mature oak left over from the original 1950s planting", "Turf laid up to, never under, the canopy", "Drip-line rule unless a certified arborist clears it"],
                     ["Corner lot at Colonial Drive or Curry Ford Road", "Two road frontages and older drainage", "Base graded to two exit points instead of one", "County drainage review on the second frontage too"]],
                    "Compiled from Azalea Park's published boundary description and Florida's May 2026 turf rule; a specific address can still differ, which is why we check the parcel first.")),
        sec("Lake Underhill, Lake Barton and what's under the grass",
            f"<p>Lake Barton runs along Azalea Park's northwest edge, and Lake Underhill, a separate 140-acre lake with its own city park and a 1.3-mile walking path, sits just southwest of the neighborhood along Lake Underhill Road ({ext('https://www.orlando.gov/Parks-the-Environment/Directory/Lake-Underhill-Park', 'Lake Underhill Park')}). A yard that actually backs onto either lake has to keep turf back at least 10 feet from the water under the state's rule; that distance only shrinks to nothing where a seawall or bulkhead already stands in the water's place. Most Azalea Park lots don't touch either lake directly, but the ones that do are worth checking against a map before assuming otherwise.</p>"
            + f"<p>{src('usda-wss', 'the USDA Web Soil Survey')} generally maps this stretch of Orange County as Immokalee and Myakka fine sands where seven decades of building haven't already reclassified the ground as urban land, both poorly drained flatwoods soils under whatever fill was added when the original subdivision went in during the 1950s. The compacted rock here goes in nearer the top of the state's two-to-four-inch allowance than the bottom, for the same reason it would on any flatwoods lot: slow natural drainage underneath needs the extra margin a well-drained ridge lot wouldn't.</p>"),
        "<!--AUTO:city-services-->",
    ]),
    faqs=[
        faq("Is Azalea Park inside Orlando or unincorporated Orange County?", "Both, depending on the exact parcel. The Census Bureau maps the whole community as unincorporated, but Orlando has annexed pieces of the area over the decades, so a specific address is worth checking on the county property appraiser's site before assuming either answer."),
        faq("How old are most of Azalea Park's homes?", "The neighborhood dates to 1952, when Phillips Properties built roughly 1,100 homes here as one of Orange County's first large tract subdivisions. Most of the original stock is concrete-block ranch construction typical of that era."),
        faq("Does turf near Lake Barton or Lake Underhill need a special setback?", "The same 10-foot waterbody setback applies here as anywhere else in Florida under the May 2026 turf rule, except on a lot where a seawall or bulkhead already sits between lawn and water. Most Azalea Park lots sit a block or more from either lake, so it doesn't come up on every job."),
        faq("Who handles water service in Azalea Park?", "Orange County Utilities bills unincorporated parcels on a seasonal odd/even schedule; a parcel inside Orlando's city limits instead follows the Orlando Utilities Commission. Check a recent bill if the jurisdiction isn't obvious from the address."),
        faq("Is Azalea Park within your service area?", "Yes. It's about 18 miles from Kissimmee in a straight line, well inside the roughly 40-mile radius we cover across Osceola, Orange, Polk, Lake and Seminole counties. We quote distance, not drive time, since Semoran Boulevard traffic shifts a lot by hour."),
    ],
    sources=SRC, city=SLUG, crumbs=[("Service areas", "/areas/")], crumb="Azalea Park",
    related=[("/areas/orange-county/", "Turf installation across Orange County"), ("/laws/permits/orange-county/", "Orange County's turf permit rules"), ("/areas/union-park/", "Turf in Union Park"), ("/areas/conway/", "Turf in Conway"), ("/artificial-turf-cost/", "Turf cost tables for Central Florida")],
)

LOCAL = {
    "residential": {
        "title": "Artificial Grass Installation in Azalea Park, FL",
        "meta": "Turf for Azalea Park's 1950s concrete-block ranch homes: tight in-town lots, mixed Orlando/county permitting, and 2026 pricing.",
        "h1": "Turf for Azalea Park's postwar ranch homes",
        "lede": capsule(f"Installed turf in Azalea Park runs {price('residential')} a square foot, {price('residential', True)} on most yards, unchanged from the rest of Central Florida heading into fall 2026. The neighborhood's 1952 concrete-block ranch homes sit on some of the tighter lots we work on, which shapes a conversion here more than the price ever does."),
        "sections": [
            ("A tight in-town lot changes the job before turf is even ordered",
             "<p>Azalea Park's original 1,100 homes were built close together on modest lots by Central Florida standards, which means a front yard here is often a narrow strip rather than the wide setback a 1990s subdivision would give the same square footage. That geometry pushes more of the visible lawn to the front of the house than we see in newer, larger-lot communities, which matters because a front yard doesn't get the same HOA-visibility protection a fenced backyard does if a deed restriction happens to apply.</p>"
             + "<p>We haven't found a recorded homeowners' association covering the original subdivision, so most jobs here proceed as a straightforward county or city permitting question rather than an added architectural review. The civic association that organizes the neighborhood's anniversary events isn't the same thing as a deed-enforced HOA.</p>"),
            ("Checking which office actually reviews the work",
             f"<p>Because Orlando has annexed parts of Azalea Park at different points over the decades, the same street can have county-permitted and city-permitted homes next to each other. A search on the {ext('https://ocpafl.org/', 'Orange County Property Appraiser')} site shows which one has a given parcel before any paperwork goes in. An unincorporated lot follows {a('/laws/permits/orange-county/', 'the Orange County Chapter 24 process')}, which stays silent on synthetic turf specifically; an Orlando parcel follows that city's own written turf rule instead.</p>"),
            ("What seven decades of settling does to a base here",
             "<p>A concrete-block home built in 1952 has had a lot longer to settle than a 1990s tract house, and the yard around it often shows the same history: old fill from additions, a driveway extension, or a long-gone above-ground pool can all sit under a few inches of topsoil without being obvious until excavation starts. We check for that kind of buried inconsistency before grading, since building a uniform crushed-rock base over uneven old fill is how a flat-looking lawn ends up with a low spot two summers later.</p>"),
        ],
        "scenario": ("A typical Azalea Park front-and-back conversion",
                     f"<p>Say a 1952 concrete-block ranch on a standard Azalea Park lot has 700 sq ft of combined front and back lawn, thin in the back where a camellia hedge shades it most of the day. At {price('residential')} a square foot installed, that runs roughly $5,600 to $12,600, with most quotes closer to {price('residential', True)} a foot, or about $7,000 to $11,200. Splitting the job between a visible front strip and a private back yard sometimes means two different turf specs, a denser blend up front where it's seen from the street, and a simpler build in back, both priced inside the same per-foot range rather than as separate line items.</p>"),
        "faqs": [
            faq("Does a 1950s Azalea Park home need special prep for turf?", "Not usually because of its age specifically, though older lots sometimes have buried fill from past additions or driveway work that needs checking before grading. Otherwise a conversion here follows the same washed-rock base as any Central Florida lawn."),
            faq("Is there an HOA I need to submit turf plans to in Azalea Park?", "We haven't found a recorded deed-restricted HOA for the original subdivision. The neighborhood has an active civic association, but that's a different thing from an architectural review board with turf authority."),
            faq("How do I know if my Azalea Park address is in Orlando or the county?", "Search the parcel on the Orange County Property Appraiser's site. Azalea Park's boundary has been annexed into Orlando in pieces over the decades, so an address alone doesn't settle it."),
        ],
        "sources": SRC,
    },
    "pet": {
        "title": "Pet Turf & Dog Runs in Azalea Park, FL",
        "meta": "Pet turf for Azalea Park's narrow side yards between 1950s ranch homes: fast drainage, odor control, and 2026 Central Florida pricing.",
        "h1": "Pet turf between Azalea Park's ranch homes",
        "lede": capsule(f"Pet turf in Azalea Park runs {price('pet')} a square foot installed, typically {price('pet', True)}, covering the deeper drainage base and odor-control infill a dog run needs. Lots here sit closer together than in a newer subdivision, so a side-yard dog run in Azalea Park is often narrower than the same run would be in a 1990s community with wider setbacks."),
        "sections": [
            ("Fitting a dog run into a Phillips-era side yard",
             "<p>The gap between two Azalea Park homes is frequently narrower than a modern lot's side setback, sometimes not much more than the width of a single-car driveway, and that squeezed strip is exactly where a dog spends most of its outdoor time on these lots. Grass in a space that tight rarely survives more than a season of daily traffic, especially with a concrete-block wall or a wood fence radiating heat back into the strip on a summer afternoon.</p>"
             + "<p>A pet-turf run suits that footprint precisely because it doesn't need mowing access a narrow strip can't provide anyway, and the fast-draining backing handles daily use a lawnmower-width space never could.</p>"),
            ("No ARC packet, but still a parcel to check first",
             f"<p>Azalea Park's original subdivision carries no recorded architectural review board that we've found, so a pet-turf job here generally clears whichever general permitting process applies to that specific parcel rather than an added design submittal. The catch is confirming that process in the first place: a search on the {ext('https://ocpafl.org/', 'Orange County Property Appraiser')} site shows whether a given address answers to the county or to Orlando before work starts, since the two offices have different written positions on synthetic turf.</p>"),
            ("Keeping odor and drainage under control on a tight lot",
             f"<p>A side-yard run this narrow concentrates dog waste in a small footprint, which makes infill choice matter more here than on a wide-open backyard. Zeolite or a coated antimicrobial sand both work by trapping and later releasing ammonia when rinsed, and {post('how-to-get-dog-urine-smell-out-of-artificial-turf', 'a consistent rinse schedule')} does more for odor control on a run this size than infill choice alone.</p>"),
        ],
        "scenario": ("A dog run in a narrow Azalea Park side yard",
                     f"<p>Say an Azalea Park side yard measures 6 feet wide by 20 feet long between a driveway and a wood fence, for 120 sq ft of usable ground, tight even by this neighborhood's standards. At {price('pet')} a square foot installed, that runs roughly $1,200 to $2,160, with most jobs closer to {price('pet', True)} a foot, or about $1,440 to $1,920 total. A run this narrow sometimes carries a small minimum charge on top of the per-foot rate, since a crew and equipment mobilize for a 120 sq ft job the same way they would for one four times the size. A single flush point at the low end keeps rinse water moving toward the back rather than pooling against the driveway.</p>"),
        "faqs": [
            faq("Is a narrow Azalea Park side yard big enough for pet turf?", "Yes. A dog run doesn't need mowing clearance, so a strip as narrow as five or six feet works, though a job this small sometimes carries a minimum charge since a crew mobilizes the same way for a small area as a large one."),
            faq("Do I need Orlando's or Orange County's permit for a pet run here?", "It depends on the parcel. Check the address on the county property appraiser's site first, since Azalea Park has both county and city-annexed lots on the same streets."),
        ],
        "sources": SRC,
    },
    "putting": {
        "title": "Backyard Putting Greens in Azalea Park, FL",
        "meta": "Compact putting greens sized to Azalea Park's smaller 1950s lots, with cup and fringe options and 2026 Central Florida pricing.",
        "h1": "Compact putting greens for Azalea Park yards",
        "lede": capsule(f"A backyard putting green in Azalea Park runs {price('putting')} a square foot installed, typically {price('putting', True)}, covering contouring, fringe and a cup. Lots in this 1952 subdivision run smaller than in most of the newer communities we serve, so a green here is usually sized to fit a compact backyard rather than built as the yard's centerpiece feature."),
        "sections": [
            ("Designing around Azalea Park's smaller footprint",
             "<p>A standard Azalea Park backyard leaves less open ground than a 1990s subdivision lot of the same era's larger-lot competitors, so a putting green here typically takes the form of a single compact contour with one cup rather than a multi-hole layout. That's less a limitation than a design starting point: a smaller green built to fill the actual space reads as intentional, where an oversized one crammed into a tight yard usually doesn't leave room for anything else, including the dog run or patio a lot of the same homeowners also want.</p>"),
            ("Working around a mature oak left from the original planting",
             f"<p>Some of Azalea Park's original 1950s trees, oaks planted when the subdivision first went in, have grown large enough that their canopy now shades a meaningful share of a small backyard. {a('/laws/florida-hb-683/', 'the state turf rule')} keeps a green from extending under that drip line without a certified arborist's sign-off, which on a lot this size can determine whether a green fits at all or has to shift toward whichever corner still gets full sun.</p>"),
            ("Why a smaller green still needs a full-depth base",
             "<p>Compact doesn't mean simple where the base is concerned. Azalea Park's ground is generally mapped as Immokalee and Myakka fine sand under decades of added fill, both slow-draining flatwoods soils, and an uneven base under a small green shows up in the roll just as fast as it would on a large one. We build to the same compacted, washed-rock standard regardless of the green's footprint, since cutting corners on a small job doesn't actually save meaningful time.</p>"),
        ],
        "scenario": ("A single-cup green on a compact Azalea Park lot",
                     f"<p>Say an Azalea Park backyard has 250 sq ft of open, sunny ground once the shade from a corner oak is subtracted, enough for one cup, a simple contour and a modest fringe. At {price('putting')} a square foot installed, that runs roughly $3,500 to $7,500, with most jobs closer to {price('putting', True)} a foot, or about $4,500 to $6,250 total. On a lot this size, the fringe often borders a patio or a fence line directly rather than open lawn, which changes how the edge gets trimmed and anchored but not the underlying price range.</p>"),
        "faqs": [
            faq("Is Azalea Park too small a lot for a putting green?", "Not usually. A compact single-cup green with a modest fringe fits most standard Azalea Park backyards once the shaded area under any mature trees is accounted for; it just won't be a multi-hole layout the way a larger lot elsewhere might support."),
            faq("Does an oak on my Azalea Park lot limit where a green can go?", "Yes, if the tree is inside or near the planned footprint. The state's drip-line rule keeps turf from extending under the canopy without a certified arborist's approval, which on a small lot often decides the green's shape more than the design itself does."),
        ],
        "sources": SRC,
    },
    "playground": {
        "title": "Playground Turf Installation in Azalea Park, FL",
        "meta": "Cushioned playground turf for Azalea Park's family-heavy blocks near the neighborhood's own namesake park, with 2026 pricing and sources.",
        "h1": "Backyard play turf for Azalea Park's youngest residents",
        "lede": capsule(f"Playground turf in Azalea Park runs {price('playground')} a square foot installed, typically {price('playground', True)}, with a shock pad sized to the equipment on top of it. Roughly 22 percent of Azalea Park's 14,141 residents were under 18 in the 2020 Census, one of the younger age profiles in our service area, and the neighborhood's own namesake park on Oxalis Drive gets more use than its size would suggest."),
        "sections": [
            ("A neighborhood built around its own park since the 1950s",
             f"<p>Azalea Park has run its own community pool and park on Oxalis Drive since not long after the subdivision was built, a rarity for a neighborhood this size, and it remains a gathering point today. A backyard play surface doesn't compete with that; it covers the daily version of the same need, somewhere safe for a toddler to fall or a swing set to stand, on the mornings a trip to the park isn't practical.</p>"),
            ("The infill line the state draws around play equipment",
             f"<p>Florida's May 2026 turf standard limits rubber or other synthetic infill strictly to the ground directly under playground equipment, never across a residential lawn generally. On an Azalea Park lot that usually means a smaller, defined zone under a swing set or slide built to the equipment's fall-height spec, bordered by ordinary silica-infilled turf everywhere else the family actually walks. {post('is-artificial-turf-safe-for-kids-pfas-lead', 'Material safety questions')} come up often enough on these jobs that we keep a page just on that.</p>"),
            ("Small lots mean the play zone often replaces, not adds to, lawn",
             "<p>Because Azalea Park's backyards run smaller than a newer subdivision's, a play area here more often replaces a struggling patch of shaded lawn than gets carved out of an otherwise healthy one. That's usually a straightforward trade: the spot under a camellia or oak where grass barely grows anyway is frequently the same spot that makes sense for a swing set, since neither one needs full sun to work.</p>"),
        ],
        "scenario": ("A play area replacing thin lawn near Azalea Park's own park",
                     f"<p>Say an Azalea Park family a few blocks from the Oxalis Drive park wants a 350 sq ft play zone in a shaded back corner where grass has never done well, covering a swing set and a soft landing area for a young child. At {price('playground')} a square foot installed, that runs roughly $3,500 to $8,750, with most jobs closer to {price('playground', True)} a foot, or about $4,200 to $6,650. Shock-pad depth under the swing set's fall zone drives most of that range, and because the area replaces bare or thinning ground rather than healthy lawn, there's no sod-removal cost eating into the budget the way a full-yard conversion would carry.</p>"),
        "faqs": [
            faq("Can I put rubber mulch-style infill across the whole play area?", "Only the footprint directly under the equipment can use rubber or another synthetic infill under Florida's May 2026 rule. Turf outside that footprint, even within the same play zone, uses silica sand, rock, shell or a coated natural-material infill instead."),
            faq("Does Azalea Park's own park change what a backyard play area needs?", "No, the public park doesn't affect permitting or design for a private yard. It does mean a lot of nearby families already think in terms of a swing set or slide, which is part of why the shock-pad spec question comes up early in these conversations."),
        ],
        "sources": SRC,
    },
    "pool": {
        "title": "Pool & Lanai Turf in Azalea Park, FL",
        "meta": "Turf for Azalea Park's smaller pool decks and patios on tight 1950s lots, with drainage details and 2026 Central Florida pricing.",
        "h1": "Turf for Azalea Park pool decks and patios",
        "lede": capsule(f"Turf beside a pool or patio in Azalea Park runs {price('residential')} a square foot installed, generally toward {price('residential', True)}, since small, tightly bordered areas take more labor per foot than an open lawn does. Pools on these 1950s lots tend to sit closer to the property line than a newer home's would, which changes how much room a turf border actually has to work with."),
        "sections": [
            ("A smaller pool footprint on an older Azalea Park lot",
             "<p>A pool added to a 1950s Azalea Park lot, whether original to the home or retrofitted later, usually leaves a tighter band of surrounding ground than a pool built into a larger modern lot from the start. That band often runs directly against a property-line fence rather than another section of open yard, which limits where a turf edge can be nailed into soil versus where it has to bond to an existing paved or block surface instead.</p>"
             + "<p>Because the usable strip is narrow, we frequently price these jobs at the higher end of the range even though the total cost stays modest, simply because a crew and base materials mobilize for a small area the same way they would for a larger one.</p>"),
            ("Where the state's waterbody setback comes up here",
             f"<p>Most Azalea Park pool lots don't back directly onto Lake Barton or Lake Underhill, but the handful that do still have to keep turf at least 10 feet from the water under {a('/laws/florida-hb-683/', 'the state turf rule')}, regardless of how close the pool deck itself sits to the property's rear line. A seawall or bulkhead, where one already exists, removes that specific requirement, but nothing about having a pool changes the underlying setback.</p>"),
            ("Drainage on a patio that predates the pool cage",
             f"<p>Some Azalea Park patios were poured well before a screen enclosure went up later, which means the concrete's original grade doesn't always match what a modern cage would specify. Turf laid over that older concrete still needs a drainage underlay regardless of the slab's age, since a rinse or a storm has to go somewhere once it hits a solid, non-percolating surface. {post('can-artificial-turf-melt', 'Reflected heat from nearby glass or a pool cage panel')} is also worth checking before installation, not after.</p>"),
        ],
        "scenario": ("A narrow pool-border strip on an older Azalea Park lot",
                     f"<p>Say a 1950s Azalea Park pool sits close to the rear property line, leaving a 200 sq ft band of turf between the pool deck and a wood fence, currently patchy grass that gets scorched by heat reflecting off the deck. At {price('residential')} a square foot installed, that runs roughly $1,600 to $3,600, landing nearer {price('residential', True)} a foot for a job this size, or about $2,000 to $3,200. A glue-down edge where the turf meets the pool deck's concrete sits inside that figure, as does the drainage underlay the deck's non-percolating surface requires.</p>"),
        "faqs": [
            faq("Does a small Azalea Park pool border cost more per square foot?", "Often, yes. A narrow, tightly bordered area takes close to the same labor and material mobilization as a larger one, so the per-foot rate tends to land toward the upper half of the published range even though the total job cost stays modest."),
            faq("Do I need a drainage layer under turf on an old Azalea Park patio?", "Yes, whenever turf goes directly over existing concrete, regardless of the slab's age. Concrete doesn't drain the way soil does, so a rinse or a storm needs somewhere to go once it reaches that surface."),
        ],
        "sources": SRC,
    },
    "repair": {
        "title": "Artificial Turf Repair in Azalea Park, FL",
        "meta": "Repairing older turf installations in Azalea Park, from seam failures to drainage problems, priced after photos or a site visit.",
        "h1": "Repairing older turf on an Azalea Park lot",
        "lede": capsule("A repair estimate in Azalea Park waits on photos or a look at the yard in person, since a torn seam, a scorched patch and a failed base each call for different fixes that a flat per-foot rate can't reflect. Homes here date to 1952, so some of the turf we're asked to fix was installed years before the state's current standard existed."),
        "sections": [
            ("Repair work on a resale home's existing turf",
             "<p>Azalea Park changes hands often enough, like any established neighborhood this age, that a fair share of our repair calls involve turf a previous owner installed rather than a job we're seeing for the first time. What that turf sits on varies widely: some bases were built properly, and some used whatever fill was on hand at the time, which is why a repair estimate here starts with pulling back a section to see what's actually underneath rather than guessing from the surface.</p>"
             + "<p>An unwashed or under-compacted base shows the same symptoms as a bad seam bond from the outside, a lifted edge, a soggy low spot, so telling the two apart before quoting anything saves a homeowner from paying for the wrong fix.</p>"),
            ("Heat damage near reflective glass or a pool cage",
             f"<p>A newer low-emissivity window, increasingly common as Azalea Park homeowners replace 1950s originals, can bounce enough focused sunlight onto nearby turf to leave a soft, discolored patch, since the fiber itself is polyethylene, a material that starts to distort somewhere around 175 to 200 degrees under that kind of concentrated heat. {post('can-artificial-turf-melt', 'A scorched patch with no obvious cause')} is one of the more common repair calls we get from older homes mid-renovation, and the fix is usually a window film or repositioning the affected turf section rather than a full replacement.</p>"),
            ("What decades of settling near Lake Barton does to drainage",
             "<p>Lots closer to Azalea Park's Lake Barton edge sit on the same slow-draining flatwoods sand as the rest of the neighborhood, and decades of settling around an older home's foundation can shift the grade a lawn was originally built to shed water toward. A repair here sometimes involves correcting that drift in grade rather than just re-anchoring an edge, since turf laid over a base that no longer slopes the way it did in 1952 will pool water regardless of how well the seams are bonded.</p>"),
        ],
        "scenario": ("A scorched patch traced back to a window, not the turf",
                     "<p>Say an Azalea Park homeowner notices a roughly 3-square-foot discolored, slightly melted patch of turf that appears each afternoon near a west-facing window replaced the previous year. A site visit would trace the sun's path from that window across the yard at the time the damage seems to appear, since low-emissivity glass reflecting concentrated light is a common and easily missed cause that has nothing to do with how the turf itself was installed. Photos taken at different times of day help narrow down the timing before a visit, though confirming the actual cause still means seeing both the window and the patch in person.</p>"),
        "faqs": [
            faq("Can you tell if turf damage is from the base or the original installation?", "Usually, yes, after pulling back the affected section. A failed seam bond and a settled or unwashed base look similar from the surface but need different fixes, which is why we check in person before quoting."),
            faq("Why does a patch of my Azalea Park turf look scorched?", "Check nearby windows first. Low-emissivity glass on a newer replacement window can reflect enough concentrated sunlight to soften or scorch turf several feet away, a pattern we see often enough on Azalea Park's older homes mid-renovation."),
        ],
        "sources": SRC,
    },
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
