# -*- coding: utf-8 -*-
from _helpers import page, capsule, sec, table, faq, a, svc, city, post, src, ext, price
from _cityservice import cityservice_pages

SLUG = "oak-ridge"

SRC = [
    "dep-rule", "fs125572", "usda-wss", "census-acs",
    ("Orange County Property Appraiser — parcel search", "https://ocpafl.org/"),
    ("Orange County Fast Track Online Services", "https://fasttrack.ocfl.net/OnlineServices/"),
    ("Orange County Code, Chapter 24, Municode Library", "https://library.municode.com/fl/orange_county/codes/code_of_ordinances?nodeId=PTIIORCOCO_CH24LABUOPSP"),
    ("Orange County Utilities — watering restrictions", "https://www.orangecountyfl.net/watergarbagerecycling/wateringrestrictions.aspx"),
    ("U.S. Census Bureau QuickFacts, Oak Ridge CDP, Florida", "https://www.census.gov/quickfacts/fact/table/oakridgecdpflorida/PST045224"),
    ("South Florida Water Management District — Shingle Creek", "https://www.sfwmd.gov/recreation-site/shingle-creek"),
    ("USDA NRCS official series description, EauGallie series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/E/EAUGALLIE.html"),
    ("USDA NRCS official series description, Immokalee series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/I/IMMOKALEE.html"),
    ("Orange County, Florida short-term rental regulation guide", "https://www.bnbcalc.com/blog/short-term-rental-regulation/orange-county-florida-guide"),
    ("The Florida Mall — company history", "https://en.wikipedia.org/wiki/The_Florida_Mall"),
    ("Central Florida's Fascinating History: Orlando's Oak Ridge", "https://citruslandfl.blogspot.com/2017/10/orlandos-oak-ridge.html"),
]

# ============================================================== hub
HUB = page(
    "/areas/oak-ridge/", "city",
    "Artificial Turf in Oak Ridge, FL: Permits & Rental Yards",
    "Turf installers serving unincorporated Oak Ridge, FL: Orange County permitting, watering days, short-term rental zoning, and 2026 pricing.",
    "Installing artificial grass along Oak Ridge's Orange Blossom Trail corridor",
    capsule(
        "Oak Ridge counted 25,062 residents at the 2020 Census, more people than several incorporated Florida cities, and about half "
        f"identify as Hispanic or Latino. We install and repair synthetic grass here at Central Florida's standard {price('residential')} "
        "a square foot, unchanged since our September 2026 check, on lots ranging from a 1950s single-family house to a duplex held as a "
        "long-term rental."
    ),
    "".join([
        sec("Who reviews a turf permit in unincorporated Oak Ridge?",
            "<p>Oak Ridge has no city hall of its own, so Orange County's Permitting Services and Division of Building Safety handles "
            f"every turf permit here, with status checks running through {ext('https://fasttrack.ocfl.net/OnlineServices/', 'Fast Track Online Services')} "
            "and questions going to 407-836-5550. It is easy to assume this stretch of Orange Blossom Trail belongs to Orlando, since the "
            "Mall at Millenia and the tourist corridor along International Drive both sit close by, but Oak Ridge itself remains unincorporated "
            f"county land, so there is no separate city code to consult. A search on the {ext('https://ocpafl.org/', 'Orange County Property Appraiser')} "
            "site confirms the taxing jurisdiction for any specific address. County Code Chapter 24 limits its definition of \"turf\" to living "
            "grass species and, checked as of September 2026, has no section written for synthetic turf, which leaves the state's own standard "
            f"as the operative rule. {a('/laws/permits/orange-county/', 'Our Orange County permit page')} has the department's full contact "
            f"details, and {a('/laws/florida-hb-683/', 'the state rule itself')} sets the material and setback requirements either way.</p>"),
        sec("What kinds of Oak Ridge properties do we see, and how does the plan change?",
            "<p>Oak Ridge's housing stock runs from single-family houses built before Disney opened to duplexes and small rental "
            "properties, and what a crew finds at the address usually says more about the job than the neighborhood name does.</p>"
            + table("Oak Ridge property types and how the plan differs",
                    ["Property type", "What we typically find", "How the plan changes"],
                    [["A 1950s-60s single-family house off the Trail", "An older slab with no irrigation zone map on file", "Heads are traced and capped by hand before base material goes down"],
                     ["A duplex or side-by-side rental", "One shared property line, sometimes two separate water meters", "Seams and edging are kept clear of the line the two units share"],
                     ["A 1980s subdivision backing a retention pond", "A mowed pond bank a few feet from the patio slab", "Turf stops 10 ft from the bank unless a seawall is already there"],
                     ["A lot fronting Orange Blossom Trail or a signal", "Reflective glass off nearby commercial storefronts or signage", "Infill color gets checked against that reflection before ordering"]])
            + "<p>The published price per square foot does not move between these four. Labor hours and what has to be traced or protected first do.</p>"),
        sec("Which water utility and schedule cover Oak Ridge?",
            "<p>Call 407-254-9850 and Orange County Utilities will confirm the watering day for a given Oak Ridge address: two days a week "
            "while daylight saving time is in effect, one day a week the rest of the year, with a 10 a.m. to 4 p.m. no-water window that holds "
            "year-round regardless of the day count. A block or two close enough to the Orlando line can end up billed by the Orlando Utilities "
            "Commission instead, so a recent water bill settles it faster than guessing from a map. Either utility's schedule stops applying to "
            f"a turf area the day its irrigation heads are capped, which {src('dep-rule', 'the May 2026 state rule')} requires outright.</p>"),
        sec("Why Shingle Creek matters for drainage here",
            f"<p>The headwaters of {ext('https://www.sfwmd.gov/recreation-site/shingle-creek', 'Shingle Creek')}, recognized as the northernmost "
            "source water of the Everglades, rise in the southwest stretch of Orange County near the airport and Orange Blossom Trail corridor "
            "before running about 23 miles south through Kissimmee to Lake Tohopekaliga. Oak Ridge sits close enough to that corridor that "
            "drainage from a meaningful share of the area routes toward Shingle Creek and, from there, into the South Florida Water Management "
            "District's Kissimmee Basin rather than the district that manages Orlando proper. The exact line between the two districts runs "
            "address by address, so a homeowner near the edge is better off checking the county's own water atlas than assuming either way. "
            "A retention pond at the back of a newer subdivision is usually part of that same drainage picture, which is why turf near one still "
            "has to respect the state's 10-ft waterbody setback.</p>"),
        sec("What Oak Ridge's zoning says about a nightly rental",
            "<p>Orange County's zoning code keeps short-term and nightly rentals out of standard R-1 and R-2 residential districts, which cover "
            "most of Oak Ridge, allowing that use mainly in commercial, industrial or specifically approved planned developments instead. What "
            "the area has in abundance is the other kind of rental: long-term leases in single-family houses and duplexes, often turning over "
            "tenants every year or two. A synthetic lawn that does not need reseeding or a new irrigation controller between leases is a "
            "different pitch for a landlord than for an owner-occupant, even though the install itself, and the price per square foot, do not "
            "change based on who signs the check.</p>"),
    ]) + "<!--AUTO:city-services-->",
    faqs=[
        faq("Is Oak Ridge part of the City of Orlando?",
            "No. Oak Ridge is unincorporated Orange County, even though it borders Orlando and sits close to Mall at Millenia and the "
            "International Drive tourist corridor. Permits go through the county's Permitting Services, not Orlando's."),
        faq("Can I rent my Oak Ridge house out nightly on a booking app?",
            "Not in a standard residential zone. Orange County's code reserves short-term, nightly rental for commercial, industrial and "
            "specifically approved planned-development districts, which most Oak Ridge subdivisions are not."),
        faq("Which water utility bills my Oak Ridge address?",
            "Usually Orange County Utilities, though a pocket near the Orlando line may be billed by the Orlando Utilities Commission instead. "
            "A recent bill will say which one, and either way a capped turf area stops needing that schedule."),
        faq("How do you pick the best artificial turf company near Oak Ridge when half the block rents long-term?",
            "Ask whether the crew has priced a job around a shared duplex property line before, and get the same five written specs from every "
            "bidder regardless of whether the buyer is an owner-occupant or a landlord."),
        faq("How far is Oak Ridge from your Kissimmee base?",
            "About 12 miles by road. That is well inside the roughly 40-mile radius we cover, and it does not change the per-square-foot price."),
    ],
    sources=SRC, city=SLUG, crumbs=[("Service areas", "/areas/")], crumb="Oak Ridge",
    related=[("/areas/orange-county/", "Orange County: permits, water and soil"),
             ("/laws/permits/orange-county/", "Orange County permit rules for turf"),
             ("/areas/pine-castle/", "Artificial turf in Pine Castle"),
             ("/areas/dr-phillips/", "Artificial turf in Dr. Phillips"),
             ("/areas/southchase/", "Artificial turf in Southchase"),
             ("/artificial-turf-cost/", "Full turf cost guide for Central Florida")],
)

# ============================================================== local
LOCAL = {
    "residential": {
        "title": "Artificial Grass Installation in Oak Ridge, FL Rentals",
        "meta": "Artificial grass installation in Oak Ridge, FL: turf for long-term rental turnover, duplex lots, and 2026 pricing per square foot.",
        "h1": "Low-upkeep turf for Oak Ridge's rental-heavy blocks",
        "lede": capsule(
            f"Long-term landlords and homeowners across Oak Ridge's 1950s through 1980s subdivisions pay the same {price('residential')} a "
            f"square foot as the rest of Central Florida for a turf conversion, a range that has not moved since our September 2026 check, "
            f"typically settling at {price('residential', True)}. What differs block to block is whether the lot is owner-occupied or a "
            "rental turning over every lease term."
        ),
        "sections": [
            ("A yard that survives one tenant after another",
             "<p>A rental lawn takes a different kind of wear than an owner-occupied one: irregular mowing between leases, a moving truck "
             "parked on the grass, a tenant's dog that the lease did not mention. Synthetic turf does not care about any of that in the way "
             "St. Augustine does, since there is no mowing schedule to fall behind on and no root system to compact under a truck's tires. For "
             "a landlord holding a house or a duplex unit long-term, that translates to one line item that stops recurring between tenants "
             f"rather than a lawn that needs re-sodding every time a lease ends badly. {svc('residential', 'The full installation breakdown')} "
             "covers what the base and turf actually consist of, regardless of who ends up living behind it.</p>"),
            ("Duplex and side-by-side lots split the job, not the price",
             "<p>A duplex or a side-by-side rental shares one property line down the middle, which changes how a crew lays out seams and "
             "edging more than it changes the total cost. Turf on both sides usually gets run as one continuous job rather than two separate "
             "small ones, with the dividing seam kept a foot or two off the actual property line so a future dispute over lawn care never "
             "becomes a boundary argument. Where two units carry separate water meters, capping irrigation heads on each side still happens "
             "independently, since the state's rule against watering synthetic turf applies meter by meter, not lot by lot.</p>"),
            ("What Oak Ridge Road's history says about how old this ground is",
             "<p>Local records place the name Oak Ridge on this stretch of the county at least as far back as 1903, when a parcel became the "
             "cemetery that still sits at the northwest corner of Sand Lake Road and Orange Blossom Trail; county commissioners renamed several "
             "streets here in the mid-1950s, turning Macy Street into today's Oak Ridge Road. Ground that has been platted and built on that "
             "long has usually been through at least one prior landscaping cycle, sod pulled and replaced, a bed dug and filled in, which "
             "means a crew occasionally finds old irrigation line or buried debris a newer subdivision would not have. None of that changes "
             "the published price; it can add an hour or two to the strip-out on an older lot.</p>"),
        ],
        "scenario": ("A 520 sq ft yard behind a rental duplex",
                     "<p>Say you have a 520 sq ft yard behind one side of a 1962 duplex held as a long-term rental, with the other unit's "
                     "tenant sharing the driveway but not the backyard. At the published range that prices between $4,160 and $9,360, with "
                     "most jobs this size landing near $5,200 to $8,320. For a landlord, the calculation usually weighs that cost against "
                     "several years of re-sodding a lawn that a rotating set of tenants never waters on schedule, rather than against a "
                     "single season's water bill the way an owner-occupant might.</p>"),
        "faqs": [
            faq("Does turf make sense for a rental property in Oak Ridge?",
                f"For a lease that turns over every year or two, often yes: there is no mowing schedule for a tenant to skip and no sod to "
                f"replace between leases. {post('is-artificial-turf-worth-it-in-florida', 'The broader cost comparison')} lays out the ten-year "
                "math either way."),
            faq("How do you price a duplex with two separate yards?",
                "Usually as one job with a shared seam kept off the property line, not two separate quotes. Two water meters just mean heads "
                "on each side get capped independently."),
        ],
        "sources": SRC,
    },
    "pet": {
        "title": "Pet Turf & Dog Runs for Oak Ridge Duplex Yards",
        "meta": "Pet turf and dog runs in Oak Ridge, FL: odor-control infill for rental turnover, flatwoods soil, and 2026 installed pricing.",
        "h1": "Pet turf sized for Oak Ridge's smaller rental yards",
        "lede": capsule(
            f"A pet-ready turf system for an Oak Ridge side yard costs {price('pet')} a square foot, September 2026 pricing that leans "
            f"toward {price('pet', True)} once odor-control infill is added. On a block where dogs come and go with each new tenant, the "
            "infill choice matters as much as the turf itself."
        ),
        "sections": [
            ("Odor control that outlasts a single tenant",
             "<p>A dog run on a rental lot has to handle more than one dog's habits over its lifespan, and zeolite or antimicrobial-coated "
             "sand infill, both allowed as natural material under the state's turf standard, are built for exactly that kind of repeat use "
             "rather than a single pet's schedule. Plain silica costs less upfront but does nothing for odor, which shows up fastest on a "
             "smaller lot where the run sits close to a bedroom window or a shared fence. For a landlord weighing the two, the incremental cost "
             "of zeolite over silica is small next to the cost of a full re-infill after an odor complaint from either side of a duplex.</p>"),
            ("Flatwoods sand under a narrow duplex side yard",
             "<p>Much of Oak Ridge sits on the same Immokalee and EauGallie flatwoods soils common across this part of Orange County, both "
             "poorly drained series with a seasonal high water table that can sit within 6 to 18 inches of the surface for a few months most "
             "years. A duplex side yard, often the narrowest strip on the whole lot, has less room to grade a fall away from the fence than an "
             "open backyard does, so the base leans on the fuller washed-rock depth to keep a dog run from holding water after a summer storm "
             "rather than trying to out-grade a tight space.</p>"),
            ("Why a shared fence line changes the layout",
             "<p>Where a dog run backs onto a fence shared with a duplex neighbor or an adjacent rental, keeping the turf's edge a few inches "
             "off that fence rather than running flush to it avoids infill and debris piling against a shared structure that is not the "
             "installer's to repair. It also gives a hose enough clearance to rinse the full width of the run without spraying directly onto "
             f"the neighbor's side. {svc('pet', 'The pet turf infill and drainage guide')} goes through the zeolite-versus-silica trade-off in "
             "more depth than one fence line's layout can cover.</p>"),
        ],
        "scenario": ("A 180 sq ft run on a duplex side yard",
                     "<p>Say you have a 180 sq ft strip along one side of a rental duplex, fenced from the shared driveway but open to the "
                     "backyard, for a tenant's dog. At the published pet range that prices between $1,800 and $3,240, with most jobs this size "
                     "landing near $2,160 to $2,880 once zeolite infill is included. Because the strip is narrow, expect the base and edging "
                     "labor to make up a larger share of that total than the turf material itself, which is typical on any run this size "
                     "regardless of the neighborhood.</p>"),
        "faqs": [
            faq("Should a landlord pay extra for odor-control infill?",
                "Usually yes, if the property is expected to house a dog again after the current tenant leaves. The cost difference over "
                "plain silica is modest next to a full infill replacement later."),
            faq("Does a shared duplex fence change how the run is built?",
                "Mainly the edge placement: keeping turf a few inches off a shared fence avoids debris and infill piling against a structure "
                "that belongs to both units rather than just one."),
        ],
        "sources": SRC,
    },
    "putting": {
        "title": "Backyard Putting Greens in Oak Ridge's Smaller Yards",
        "meta": "Backyard putting greens in Oak Ridge, FL: fitting a green into a compact lot near a retention pond, plus 2026 installed pricing.",
        "h1": "Compact putting greens for Oak Ridge backyards",
        "lede": capsule(
            f"Fitting a putting green into one of Oak Ridge's smaller backyards costs {price('putting')} a square foot; as of September "
            f"2026 the number tracks the tightness of the space more closely than the green's shape, with most builds landing at "
            f"{price('putting', True)}. A retention pond at the back of the lot is the other detail that shapes the design here."
        ),
        "sections": [
            ("Designing around a compact 1970s or 80s lot",
             "<p>Many of Oak Ridge's subdivisions were built on lots smaller than what came later further from the city, which means a "
             "putting green here usually has to share space with a patio, a shed or a narrow side yard rather than claim an entire open "
             "backyard. A compact green with a single contour and a small fringe apron fits that footprint better than an ambitious multi-tier "
             "design, and it keeps the fringe close enough to the green itself that both surfaces can share one drainage layout instead of two "
             "separate ones competing for the same small lot.</p>"),
            ("Staying off the pond bank",
             "<p>A subdivision backing a retention pond, common in Oak Ridge's 1980s-era development, means the green's edge has to respect "
             "the same 10-ft waterbody setback as any other synthetic turf, measured from the pond's ordinary edge rather than from a property "
             "line that might sit further back. That setback usually still leaves enough room for a modest green, but it rules out the kind of "
             "green that runs turf right down to the water's edge for a view, which is a request that comes up more near a pond than it does "
             "on a landlocked interior lot.</p>"),
            ("Fringe turf that matches a small yard's traffic",
             "<p>A fringe apron on a compact green takes more foot traffic per square foot than the same product would on a larger layout, "
             "simply because there is less green to walk around before reaching it. A heavier-face-weight fringe product holds up better under "
             "that concentrated use than the lighter option that might be fine on a spacious lot, which is a spec worth asking about on a "
             f"smaller Oak Ridge yard specifically. {svc('putting', 'The full putting green guide')} covers fringe specs and contouring "
             "options in more depth.</p>"),
        ],
        "scenario": ("A 260 sq ft green on a pond-adjacent lot",
                     "<p>Say you have a 260 sq ft area at the back of an 1980s-subdivision lot, with a retention pond bank about 15 feet from "
                     "the patio. At the published range that prices between $3,640 and $7,800, with most builds this size landing near $4,680 "
                     "to $6,500. Because the pond sits close by, the design keeps the green and fringe a full 10 ft back from the water's edge, "
                     "which on a lot this size still leaves comfortable room for two cups and a short chipping approach.</p>"),
        "faqs": [
            faq("Is it worth calling around for the best putting green builder near Oak Ridge for a yard this size?",
                "Yes, since a compact lot benefits from a design that shares drainage between the green and fringe rather than treating them "
                "separately. Compare how each bidder proposes to lay out contour and fringe before comparing price alone."),
            faq("Can a green run right up to a retention pond?",
                "No. The state's turf standard keeps synthetic grass at least 10 ft from a pond's edge unless a seawall already separates the "
                "two, which most residential retention ponds do not have."),
            faq("Does a small lot limit the green to one cup?",
                "Not usually. A 250 to 300 sq ft green can typically fit two cups and a short fringe approach; it is the setback and the "
                "patio's footprint that limit the layout more than the cup count does."),
        ],
        "sources": SRC,
    },
    "playground": {
        "title": "Playground Turf in Oak Ridge Near the Trail Corridor",
        "meta": "Playground turf in Oak Ridge, FL: shock-pad sizing for family backyards near the tourist corridor, and 2026 pricing per square foot.",
        "h1": "Play-area turf for Oak Ridge's family blocks",
        "lede": capsule(
            f"September 2026 pricing puts playground-grade turf in Oak Ridge at {price('playground')} a square foot, with the shock pad "
            f"underneath doing more to move that number than the surface itself, and most home play areas landing at "
            f"{price('playground', True)}. Census figures show 43.2% of Oak Ridge households include a child under 18, well above a lot of "
            "Central Florida suburbs."
        ),
        "sections": [
            ("A young population on smaller lots",
             "<p>With more than four in ten Oak Ridge households raising a child under 18, a compact backyard play area comes up here more "
             "often than in an area with an older population, even though the lots themselves tend to run smaller than in newer subdivisions "
             "further from the city. That combination, young families and modest yard space, tends to favor a single well-built play surface "
             "over a sprawling one, since the shock pad and fall-height math matter more on a tight footprint where the equipment sits close "
             "to a fence or a patio edge.</p>"),
            ("Fall height still sets the pad, regardless of lot size",
             "<p>A shock pad's thickness is set by the play equipment's fall height, not by how much of the yard is left over after the "
             "structure is placed, so a small backyard set squeezed against a fence needs the same pad spec as a larger one with the same fall "
             "height. Skipping that step to save money on a smaller job is the same mistake regardless of yard size, and it is the difference "
             "between a play surface that meets the state's installation standard and one that just looks like it does.</p>"),
            ("Reflected heat near the commercial corridor",
             "<p>Lots closer to Orange Blossom Trail's commercial strip, including some backing onto retail parking or signage, can pick up "
             "more reflected heat and glare through the afternoon than a lot deeper in a residential subdivision. That does not change the "
             "shock pad or infill spec, but it is worth factoring into where on the lot a play area goes if there is a choice, since a shaded "
             f"corner will stay noticeably cooler underfoot on a July afternoon than one facing open pavement. {post('how-hot-does-artificial-turf-get-in-florida', 'How hot turf actually gets')} "
             "covers the numbers behind that difference.</p>"),
        ],
        "scenario": ("A 230 sq ft play area behind a family home",
                     "<p>Say you have a 230 sq ft corner of a backyard set aside for a play structure with a 6-foot fall height, on a lot two "
                     "blocks off Orange Blossom Trail. At the published range that prices between $2,300 and $5,750, with most jobs this size "
                     "landing near $2,760 to $4,370 once a shock pad sized to that fall height is included. A taller structure than a basic "
                     "swing set pushes the pad spec up, which is usually the bigger factor in the final number, not the 230 sq ft footprint "
                     "itself.</p>"),
        "faqs": [
            faq("Does a smaller Oak Ridge lot limit playground turf options?",
                "Not for a typical residential play structure. The shock pad is sized to the equipment's fall height regardless of how much "
                "yard surrounds it, so a compact lot works the same way a larger one does."),
            faq("Is playground turf here safe near a commercial corridor's heat?",
                "Yes, with the same care any Florida install needs: a hose rinse on hot afternoons and, where possible, siting the area away "
                "from direct afternoon glare off nearby pavement or signage."),
        ],
        "sources": SRC,
    },
    "pool": {
        "title": "Pool & Lanai Turf in Oak Ridge's Screened Lanais",
        "meta": "Pool and lanai turf in Oak Ridge, FL: glue-down turf over concrete decks, shade from nearby buildings, and 2026 installed pricing.",
        "h1": "Turf for Oak Ridge's screened pool decks",
        "lede": capsule(
            f"A pool deck or lanai conversion in Oak Ridge prices like any other residential lawn, {price('residential')} a square foot as "
            "of September 2026, since the turf does not know it is next to water. Several of the area's older screened pools sit close enough "
            "to a neighboring structure that shade, not the pool itself, is what killed the sod there first."
        ),
        "sections": [
            ("Shade from a duplex or an adjacent building",
             "<p>A pool lanai wedged between a house and a neighboring duplex or apartment building loses direct sun for a larger part of the "
             "day than a freestanding pool cage on an open lot, which is a common enough layout on Oak Ridge's older, tighter subdivisions. "
             "St. Augustine sod thins out fast under that kind of shade, leaving bare concrete-adjacent dirt that tracks into the pool. Turf "
             "does not need the light, so the specific problem that made the lanai strip look bad for years stops being a factor the day "
             "installation finishes.</p>"),
            ("Glue-down edges on a concrete deck",
             "<p>Where a lanai floor is poured concrete rather than soil, turf bonds to the slab with adhesive at the edges instead of "
             "anchoring with nails, and a drainage underlay goes beneath it so water from a screen-filtered rain has somewhere to go besides "
             "pooling against the pool's coping. That underlay matters more on a shaded, tightly enclosed lanai than on an open lawn, since "
             "there is less air movement to help anything dry between rains during a Central Florida wet season.</p>"),
            ("Checking glass and signage reflection before ordering",
             "<p>A pool area near Oak Ridge's commercial-adjacent blocks occasionally sits within reflection range of a storefront window or "
             "an illuminated sign rather than a neighbor's house window, and either can concentrate enough sun to soften turf the same way "
             "residential low-E glass does, since polyethylene blades begin to give around 175 to 200°F under focused heat. A short check of "
             "the pool area in the late afternoon, looking for a bright glare on the spot where turf will go, catches this before it becomes a "
             "repair instead of a layout adjustment.</p>"),
        ],
        "scenario": ("A 380 sq ft strip around a shaded lanai",
                     "<p>Say you have a 380 sq ft ring of turf planned around a screened pool wedged between an Oak Ridge house and a "
                     "neighboring duplex, where sod has struggled in the shade for years. At the residential range that prices between $3,040 "
                     "and $6,840, with most lanai jobs this size landing near $3,800 to $6,080 once the drainage underlay and glued edging are "
                     "included. Because the space runs narrow along a shared property line, expect labor to account for more of that total than "
                     "it would on an open backyard rectangle the same size.</p>"),
        "faqs": [
            faq("Will turf fix a lanai where sod never grew in the shade?",
                "Yes. Turf does not need sunlight to stay green, so a shaded strip between two buildings that never held sod works the same "
                "as a sunny one once turf replaces it."),
            faq("Does nearby commercial signage pose a melting risk?",
                "Only if it reflects concentrated sun directly onto the turf, which is uncommon but worth a quick check before installation, "
                "the same way we would check a neighbor's low-E window."),
        ],
        "sources": SRC,
    },
    "repair": {
        "title": "Artificial Turf Repair in Oak Ridge, FL",
        "meta": "Artificial turf repair in Oak Ridge, FL: diagnosing heat-scorched turf near reflective glass, storm damage, and how repair pricing works.",
        "h1": "Repairing turf along a busy commercial corridor",
        "lede": capsule(
            "An open seam or a scorched patch on an Oak Ridge lawn does not get a per-foot number over the phone; repair is priced after "
            "we have looked at it, whether that is photos texted over or a short visit. As of September 2026, a scorch mark near a nearby "
            "storefront's glass is one of the more distinctive problems this corridor produces."
        ),
        "sections": [
            ("Diagnosing a scorch mark near reflective glass",
             "<p>A patch of turf that has softened or discolored in an odd, sharply bordered shape usually traces back to concentrated "
             "sunlight reflecting off glass somewhere nearby, whether that is a neighbor's low-E window or, in parts of Oak Ridge close to "
             "Orange Blossom Trail's storefronts, a commercial building's windows or signage. The fix depends on tracing the sun's path back "
             "to its source at the right time of day, since the damage itself looks similar to a defect but is not one. Once the source is "
             "found, a repair usually means replacing the affected patch and adjusting the layout or adding a window film rather than any "
             "change to the surrounding turf.</p>"),
            ("A seam that opens on a shared duplex property line",
             "<p>Where turf runs across a duplex's shared property line, a seam there sometimes gets more foot traffic, and more disagreement "
             "over whose responsibility a repair is, than a seam in the middle of a single-family yard. Confirming who installed the original "
             "job and whether it was quoted as one continuous lawn or two separate ones is usually the first question worth answering, since "
             "that shapes whether a repair is one job or a conversation between two tenants or owners first.</p>"),
            ("Storm-driven damage near a retention pond",
             "<p>A lawn backing onto one of Oak Ridge's retention ponds sees the same storm-driven risk as any waterside yard: an edge that "
             "was never properly bonded lifts first, and infill can wash toward the pond bank if the original grade sent water that direction "
             f"instead of toward a proper drain. {post('does-artificial-turf-drain-in-heavy-rain', 'How turf is supposed to handle a heavy summer storm')} "
             "covers the base mechanics; a pond-adjacent lot here just shows a bad grade sooner than an interior lot would.</p>"),
        ],
        "scenario": ("Diagnosing a 50 sq ft scorched patch",
                     "<p>Say you have a 50 sq ft discolored patch near a side fence shared with a commercial parking lot, on a lawn installed "
                     "several years ago by a company no longer in business. As of September 2026 we would not price that sight unseen; a repair "
                     "visit starts with checking the angle of any nearby glass or signage in the late afternoon, since a scorch pattern that "
                     "sharp rarely comes from anything else. If the source is confirmed, the fix is usually a patch and a small layout shift "
                     "rather than replacing the whole lawn.</p>"),
        "faqs": [
            faq("What causes a sharply bordered burn mark on artificial turf?",
                "Almost always reflected sunlight off nearby glass, concentrated enough to soften the turf's polyethylene fibers. It is worth "
                "checking any windows or reflective signage near the affected spot before assuming a material defect."),
            faq("Who pays for a repair on a shared duplex seam?",
                "That depends on how the original job was quoted and who owns each side. Confirming the original scope is usually the first "
                "step before assigning cost between two owners or tenants."),
            faq("Does a pond-adjacent lawn need different repair methods?",
                "Not different methods, just more attention to grade and edge bonding, since that is where storm-driven lifting and infill "
                "loss tend to start on a waterside lot."),
        ],
        "sources": SRC,
    },
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
