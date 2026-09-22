# -*- coding: utf-8 -*-
"""Union Park, FL (unincorporated Orange County CDP, tier 2). Permit, water and soil facts for
Orange County are reused from site/content/c_permits.py (orange_county()) and c_counties.py
(orange_co()) — same facts and URLs, fresh sentences. Newly researched for this module, checked
September 2026: Census 2020 figures for Union Park CDP, the Little Econlockhatchee River/Jay
Blanchard Park corridor that forms the community's west and north edge, and NRCS official series
descriptions for the flatwoods soils under it."""
from _helpers import page, capsule, sec, table, faq, a, svc, city, county, post, src, ext, price
from _cityservice import cityservice_pages

SLUG = "union-park"
SRC = [
    "dep-rule", "fs125572", "fs7203045", "usda-wss", "census-acs",
    ("Orange County Property Appraiser — parcel search", "https://ocpafl.org/"),
    ("Orange County Fast Track Online Services (Permitting Services & Division of Building Safety)", "https://fasttrack.ocfl.net/OnlineServices/"),
    ("Orange County Utilities — watering restrictions", "https://www.orangecountyfl.net/watergarbagerecycling/wateringrestrictions.aspx"),
    ("St. Johns River Water Management District — Orange County", "https://www.sjrwmd.com/district-counties/orange-county/"),
    ("U.S. Census Bureau QuickFacts — Union Park CDP, Florida", "https://www.census.gov/quickfacts/fact/table/unionparkcdpflorida/PST045223"),
    ("Wikipedia — Union Park, Florida (geography and 2020 Census demographics)", "https://en.wikipedia.org/wiki/Union_Park,_Florida"),
    ("Orange County Parks — Jay Blanchard Park", "https://www.ocfl.net/cultureparks/parks.aspx?m=dtlvw&d=8"),
    ("Orange County Parks — Little Econ Greenway", "https://www.orangecountyfl.net/CultureParks/Parks.aspx?m=dtlvw&d=25"),
    ("Wikipedia — Little Econlockhatchee River", "https://en.wikipedia.org/wiki/Little_Econlockhatchee_River"),
    ("USDA NRCS Official Series Description — Myakka series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/M/MYAKKA.html"),
    ("USDA NRCS Official Series Description — Immokalee series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/I/IMMOKALEE.html"),
    ("USDA NRCS Official Series Description — Smyrna series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/S/SMYRNA.html"),
    ("Homes.com — Union Park, FL local guide", "https://www.homes.com/local-guide/union-park-fl/"),
]

HUB = page(
    "/areas/union-park/", "city",
    "Artificial Turf in Union Park, FL: An Orange County Guide",
    "Turf installation in Union Park, FL: Orange County permitting, the Little Econ setback, flatwoods soil, and September 2026 Central Florida pricing.",
    "Synthetic grass for Union Park's ranch-home streets",
    capsule(f"We install, repair and clean synthetic turf in Union Park, an unincorporated Orange County community strung along East Colonial Drive between Orlando and UCF. A residential lawn conversion runs {price('residential')} a square foot installed, {price('residential', True)} on most yards, the same Central Florida range every town in our area sees this September. Union Park's ranch-home lots back up to the Little Econlockhatchee River more often than most places we work."),
    "".join([
        sec("Turf on a Union Park ranch-home lot",
            "<p>Union Park runs along East Colonial Drive (SR 50) roughly midway between downtown Orlando and the University of Central Florida, about 22 miles from Kissimmee as the crow flies. Homeowners here search for the best artificial turf contractor near Union Park once a section of St. Augustine has thinned out under decades of oak canopy and stopped being worth mowing, or once a neighbor's yard has stayed green through a summer that turned theirs to dirt.</p>"
            + "<p>Most of the community's housing stock is 1960s-to-1980s ranch construction on modest, tree-shaded lots, the pattern behind subdivisions such as Huntridge. Grass struggles in permanent shade on one side of the house and bakes on the other, which is usually why the call starts, rather than any wish for a wholesale style change. A fenced side yard for a dog, or a compact putting green tucked between the oaks, comes up almost as often as a full backyard swap.</p>"),
        sec("Reading a Union Park yard before we quote it",
            "<p>Four situations cover most of what we run into on a Union Park property, and each one changes what the finished lawn is allowed to look like before it changes what it costs.</p>"
            + table("Union Park yard types and what we do differently",
                    ["The situation", "What's on the lot today", "How we handle the turf", "Rule in play"],
                    [["1960s-80s ranch backyard under live oaks", "St. Augustine thinning in permanent shade", "Full conversion, kept outside the canopy's drip line", "State drip-line rule unless a certified arborist signs off"],
                     ["Lot backing the Little Econlockhatchee or a retention pond", "A mowed strip down to the bank", "Turf stops at least 10 ft from the water", "DEP Rule 62-308.100 waterbody setback (seawall exception)"],
                     ["Narrow side yard between two houses", "Bare dirt or a thin, trampled strip", "Pet turf, or turf run between paving stones", "No recorded HOA design review on most of these streets"],
                     ["Corner lot on a street feeding Colonial Drive", "Two frontages, two roadside swales", "Base graded to two low points instead of one", "County drainage review; the swales themselves stay untouched"]],
                    "Compiled from our reading of Orange County's code and Florida's May 2026 turf rule; call before assuming a specific lot fits one row exactly.")),
        sec("Who signs off on a Union Park lawn",
            f"<p>There's no Union Park town hall to call: the community is unincorporated Orange County, so a residential turf job here goes through the county's Permitting Services and Division of Building Safety rather than a local office. Chapter 24 of the county code defines turf only as a living grass species and, as of September 2026, says nothing about a synthetic product either way, which means a phone call settles more than the ordinance does. Applications run through {ext('https://fasttrack.ocfl.net/OnlineServices/', 'Fast Track Online Services')}, and 407-836-5550 reaches a person directly; {a('/laws/permits/orange-county/', 'our Orange County permit page')} lays out everything else we found there.</p>"
            + f"<p>Orlando's own city limits run in an irregular checkerboard through this part of the county, and a few streets near Union Park's western edge sit close enough to that line that an address alone won't settle which office has a given parcel. A search on the {ext('https://ocpafl.org/', 'Orange County Property Appraiser')} site shows the taxing jurisdiction on file before anyone applies for anything.</p>"
            + f"<p>We haven't found a recorded homeowners' association or architectural review document covering turf on Union Park's older platted streets, unlike some of the newer planned communities we also serve. Where a deed restriction does apply, {src('fs7203045', 'F.S. 720.3045')} keeps an HOA from reaching a fenced backyard hidden from the road and from every next-door view, a protection {a('/laws/hoa-rules/', 'explained in full here')}. {a('/laws/florida-hb-683/', 'The state turf standard')} sets the floor everywhere in the county regardless of what a given subdivision does or doesn't have on paper.</p>"),
        sec("Water rules and the district behind them",
            f"<p>Sprinklers across Orange County Utilities' territory, Union Park included, stay off between 10 a.m. and 4 p.m. every day of the year, and the utility allows just one watering day outside daylight saving time, stepping up to two once clocks spring forward each spring ({ext('https://www.orangecountyfl.net/watergarbagerecycling/wateringrestrictions.aspx', 'the current watering restrictions')}). A few unincorporated pockets elsewhere in the county answer to the Orlando Utilities Commission instead, so a specific bill is worth a glance before assuming which one applies here. Whichever schedule governs, {a('/laws/florida-hb-683/', 'the state standard')} still bars pointing an in-ground system at synthetic turf once the heads underneath it are capped.</p>"
            + f"<p>Union Park sits inside the St. Johns River Water Management District's share of Orange County, in the planning area built around the Econlockhatchee River and its Little Econlockhatchee tributary ({ext('https://www.sjrwmd.com/district-counties/orange-county/', 'SJRWMD coverage of Orange County')}). The district's own rules on lakes and wetlands run alongside the state turf standard's separate 10-foot waterbody setback, not in place of it.</p>"),
        sec("The Little Econ, retention ponds and Union Park's oaks",
            f"<p>The Little Econlockhatchee River runs along Union Park's western and northern edge on its way to the main Econlockhatchee River, a state-designated Outstanding Florida Water ({ext('https://en.wikipedia.org/wiki/Little_Econlockhatchee_River', 'about 18 miles long')}). {ext('https://www.ocfl.net/cultureparks/parks.aspx?m=dtlvw&d=8', 'Jay Blanchard Park')}, off Dean Road, and the paved Little Econ Greenway running through it are the stretch most residents actually see; a backyard that backs onto that same corridor has to keep turf at least 10 feet from the water under the state's rule, unless the yard already ends at a seawall or bulkhead instead of open bank.</p>"
            + "<p>Retention ponds inside the subdivisions carry the same setback, and neither a pond bank nor a roadside swale is a legal spot for turf at all, no matter how convenient the slope looks. Where a lot backs onto open drainage instead of a fenced yard, we stake the setback before ordering material rather than guessing from the property line.</p>"
            + f"<p>Web Soil Survey maps most of the ground under Union Park's yards as flatwoods soil, principally Immokalee, Myakka and Smyrna fine sands, all poorly to very poorly drained, where groundwater can rise to within a foot or two of the surface for weeks on end after a wet summer ({ext('https://soilseries.sc.egov.usda.gov/OSD_Docs/M/MYAKKA.html', 'the Myakka series description')}; {ext('https://soilseries.sc.egov.usda.gov/OSD_Docs/I/IMMOKALEE.html', 'the Immokalee series')}). That's the reason the crushed-rock layer on a Union Park lot goes in closer to four inches than two, well past the state's minimum, and it's also why mature oaks along these streets keep turf outside the drip line unless a certified arborist clears going closer.</p>"),
        "<!--AUTO:city-services-->",
    ]),
    faqs=[
        faq("Does Union Park have its own building department for turf permits?", "No town office exists here to call. Because Union Park is unincorporated, Orange County's Permitting Services and Division of Building Safety reviews the work, reachable at 407-836-5550 or through Fast Track Online Services. Chapter 24 doesn't mention synthetic turf by name, so confirming by phone is worth the five minutes."),
        faq("Is Union Park billed by Orange County Utilities or by OUC?", "Most of unincorporated Orange County, including Union Park, is billed by Orange County Utilities on its seasonal odd/even schedule. A handful of unincorporated pockets elsewhere in the county are OUC customers instead, so check a recent bill rather than assume."),
        faq("How close can turf come to the Little Econlockhatchee River?", "At least 10 feet, under Florida's May 2026 turf rule. A property with an existing seawall or bulkhead is the one exception to that distance. The same setback applies to a subdivision retention pond, and turf can't go inside a drainage swale at all."),
        faq("Do Union Park's older subdivisions have an HOA that reviews turf?", "We haven't found a recorded design-review document for turf on these streets, unlike some newer planned communities nearby. Where a deed restriction does exist, Florida law still protects a yard that can't be seen from the street or an adjacent lot."),
        faq("How far is Union Park from your Kissimmee crew?", "About 22 miles in a straight line. Actual drive time depends on traffic on Colonial Drive or the East-West Expressway, so we don't quote one."),
    ],
    sources=SRC, city=SLUG, crumbs=[("Service areas", "/areas/")], crumb="Union Park",
    related=[("/areas/orange-county/", "Turf installation across Orange County"), ("/laws/permits/orange-county/", "Orange County's turf permit rules"), ("/areas/azalea-park/", "Turf in Azalea Park"), ("/areas/oviedo/", "Turf in Oviedo"), ("/artificial-turf-cost/", "Turf cost tables for Central Florida")],
)

LOCAL = {
    "residential": {
        "title": "Artificial Grass Installation in Union Park, FL",
        "meta": "Sod-to-turf conversions for Union Park's 1960s-80s ranch homes: oak drip lines, Orange County permitting, and 2026 Central Florida pricing.",
        "h1": "Turf conversions for Union Park's ranch-home yards",
        "lede": capsule(f"A sod-to-turf conversion in Union Park runs {price('residential')} a square foot installed, {price('residential', True)} on most yards, a range that's held across Central Florida since September 2026. Many of Union Park's ranch homes went up between the 1960s and 1980s, so the lawn underneath is often original builder sod struggling under decades of oak canopy the first owners never planned for."),
        "sections": [
            ("Why builder sod struggles on a 1970s Union Park lot",
             "<p>A lot of Union Park's residential streets went in during the 1960s through the 1980s, and the St. Augustine or Bahia the builder laid back then is often still the lawn a homeowner is standing on, thinner every year as the oaks planted alongside the houses have grown into a full canopy. Grass that once had six hours of sun now gets two, and the shaded side of the house is usually the first section that gives out entirely.</p>"
             + "<p>Underneath that struggling lawn, Web Soil Survey generally maps this part of Orange County as Immokalee and Myakka fine sands, both poorly drained flatwoods soils where the ground stays waterlogged not far beneath the surface for weeks after a wet summer. Shade above and slow-draining sand below is a hard combination for natural grass and a fairly ordinary one for turf, once the base is built to the state's washed-rock specification rather than whatever fill went in with the original driveway.</p>"),
            ("What Orange County's silence on synthetic turf means here",
             f"<p>Orange County's landscaping code defines turf only as a living grass species, so a synthetic lawn in Union Park isn't named in Chapter 24 one way or the other, unlike Orlando's code a few miles west, which spells out an engineering permit for the same product. In practice, a call to Permitting Services at 407-836-5550, or a look at {ext('https://fasttrack.ocfl.net/OnlineServices/', 'Fast Track Online Services')}, settles a specific job faster than reading the ordinance does. {a('/laws/permits/orange-county/', 'Our Orange County permit page')} covers the rest of what we found.</p>"
             + "<p>A handful of streets near Union Park's western edge sit close enough to Orlando's irregular city line that the same block can straddle two jurisdictions. Checking the parcel first, rather than assuming from the address, keeps paperwork from going to the wrong office.</p>"),
            ("Capping irrigation and reading the water rules",
             f"<p>Orange County Utilities meters most Union Park homes and runs a seasonal odd/even watering schedule, two days a week in daylight saving time and one day the rest of the year, with nothing running between 10 a.m. and 4 p.m. Once turf goes down, {a('/laws/florida-hb-683/', 'the May 2026 state turf standard')} bars using that same in-ground system to water it, so we cap the heads under the new lawn at the valve and leave the rest of the zone serving whatever beds stay planted. A hose rinse takes over from there, which also happens to be the only legal way to cool the surface on an August afternoon.</p>"),
        ],
        "scenario": ("A typical Union Park sod-to-turf conversion",
                     f"<p>Say a Union Park homeowner two streets off the Little Econ Greenway has an 800 sq ft backyard behind a 1974 ranch home, roughly a hundred square feet of it shaded inside a live oak's drip line, which the state's rule keeps off-limits, leaving about 700 sq ft to actually turf. At {price('residential')} a square foot installed, that works out to roughly $5,600 to $12,600, with most quotes landing near {price('residential', True)} a foot, or about $7,000 to $11,200 total. The spread between low and high usually comes down to access: a 36-inch side gate means wheelbarrows instead of a machine, which adds labor time material cost alone doesn't show. The oak stays untouched, drainage still has to clear the yard toward the back fence, and the irrigation zone that used to cover that section gets capped rather than removed.</p>"),
        "faqs": [
            faq("Does Union Park need an Orange County permit for a residential turf conversion?", "Orange County's code doesn't mention synthetic turf, so nothing published requires a dedicated permit for an ordinary lawn swap. Call Permitting Services at 407-836-5550 to confirm for a specific job, especially one that also touches drainage or a retaining edge."),
            faq("Can turf go under a live oak in Union Park?", "Not inside the drip line, unless a certified arborist certifies the work won't harm the tree. That limit applies statewide as of May 2026, and it's usually the single biggest factor in how much of a shaded Union Park backyard ends up turfed."),
            faq("Will my irrigation zone still work after turf goes in?", "The section under turf gets capped at the valve, since state rule bars watering synthetic turf with an in-ground system. Zones still covering planting beds or a remaining strip of lawn keep running on Orange County Utilities' normal schedule."),
        ],
        "sources": SRC,
    },
    "pet": {
        "title": "Pet Turf & Dog Runs in Union Park, FL",
        "meta": "Fast-draining pet turf for Union Park's narrow side yards: odor-control infill, no HOA paperwork on most streets, and 2026 pricing.",
        "h1": "Pet turf for Union Park's narrow side yards",
        "lede": capsule(f"Pet turf in Union Park runs {price('pet')} a square foot installed, typically {price('pet', True)}, reflecting the deeper drainage and odor-control infill a dog run needs over a plain lawn. Union Park's older platted lots often leave a narrow strip between two houses rather than a wide fenced backyard, and that strip is usually where a pet-turf conversation in Union Park starts."),
        "sections": [
            ("The narrow-lot dog run, Union Park's most common layout",
             "<p>A lot of Union Park's houses sit closer to their side property line than a newer subdivision would allow, leaving a run of ground four to eight feet wide between one house and the neighbor's fence. That strip gets hard use from a dog going in and out all day, and it's usually the first patch of grass on the property to turn to mud or bare dirt, since foot traffic there is constant in a spot that natural grass in full or partial shade already has a hard time holding.</p>"
             + "<p>Turf suits that footprint well because the whole point of a dog run is a surface that drains fast and doesn't hold odor, not one that needs mowing in a four-foot-wide space a mower can barely enter anyway. We skip the weed barrier under a pet run specifically, since fabric there traps liquid at the surface instead of letting it filter through the base.</p>"),
            ("Why most Union Park streets skip the HOA paperwork entirely",
             f"<p>Unlike some of the newer planned communities in our service area, we haven't found a recorded homeowners' association or architectural review document governing Union Park's older platted subdivisions, which means a pet-turf job here usually clears Orange County's general permitting question rather than an ARC packet on top of it. {a('/laws/hoa-rules/', 'Florida law on HOA restrictions')} still applies if a specific street does carry a deed restriction, protecting a fenced yard that isn't visible from the road.</p>"
             + f"<p>{post('how-to-get-dog-urine-smell-out-of-artificial-turf', 'Odor control')} comes down mostly to infill choice and rinsing habits rather than paperwork, which is one reason a pet-turf quote here tends to move faster than a full lawn conversion.</p>"),
            ("Rinsing a Union Park dog run on Orange County's schedule",
             "<p>A pet run needs more frequent rinsing than a plain lawn regardless of what the irrigation calendar allows, since Orange County Utilities' odd/even watering days govern in-ground sprinklers, not a hose. A quick rinse a few times a week clears waste and resets odor-control infill such as zeolite, which absorbs ammonia and releases it again once flushed. None of that rinsing counts against the county's restricted watering hours, since a hose bib isn't the irrigation system the schedule is written for.</p>"),
        ],
        "scenario": ("A dog run between two Union Park houses",
                     f"<p>Say a Union Park side yard runs 10 feet wide by 15 feet deep between a driveway and the fence line, a common footprint on these older lots, for 150 sq ft of usable ground. At {price('pet')} a square foot installed, that space runs roughly $1,500 to $2,700, with most jobs landing near {price('pet', True)} a foot, or about $1,800 to $2,400. Zeolite infill adds a modest amount on top of that base figure for the odor control a daily-use run needs. A flush-out point at one end, tied into an existing hose bib, keeps waste moving toward the yard's low corner instead of sitting against the fence, and skipping the weed barrier here is deliberate rather than a shortcut.</p>"),
        "faqs": [
            faq("Do I need a permit for a small pet-turf run in Union Park?", "Nothing in Orange County's code singles out a synthetic dog run for separate review, so most jobs proceed under the same general understanding as a residential lawn conversion. A call to Permitting Services confirms it for anything larger than a simple side-yard strip."),
            faq("Does a Union Park HOA need to approve a fenced dog run?", "We haven't found a recorded design-review document requiring that on these older streets. Where a deed restriction does exist elsewhere in our service area, a fenced yard not visible from the street or a neighboring lot is protected under Florida law regardless."),
        ],
        "sources": SRC,
    },
    "putting": {
        "title": "Backyard Putting Greens in Union Park, FL",
        "meta": "Putting greens sized to fit Union Park's oak-shaded ranch lots, built outside the drip line, with 2026 Central Florida pricing and sources.",
        "h1": "Putting greens under Union Park's oak canopy",
        "lede": capsule(f"A backyard putting green in Union Park runs {price('putting')} a square foot installed, typically {price('putting', True)}, covering contouring, fringe turf and cups. The limiting factor on most of these ranch lots isn't budget so much as finding a clear, sunny footprint outside a mature oak's drip line, since the state's rule keeps turf from going underneath one without an arborist's sign-off."),
        "sections": [
            ("Sizing a green to what a Union Park lot actually offers",
             "<p>Union Park's 1960s-to-1980s lots are generous enough for a modest green, typically a quarter-acre or so, but mature oaks planted when the houses went up now shade a good share of that ground and put a chunk of the backyard off-limits under the drip-line rule. The workable footprint is usually a corner of the yard that gets several hours of open sun, often nearer the property's back edge than its center, which shapes the green into an L or a simple oval rather than a large formal contour.</p>"
             + "<p>That constraint isn't unique to golf; it's the same reason a lot of Union Park landscaping already avoids the space directly under these trees. A green built around it, rather than fighting it, tends to look more deliberate than one that was simply squeezed into whatever flat ground was left over.</p>"),
            ("What a Union Park green sits on, and why that matters here",
             "<p>Flatwoods soils under most Union Park yards, Immokalee and Myakka fine sands among them, drain slowly and hold a seasonally high water table, which makes base depth more important on a putting green than on an ordinary lawn since an uneven base telegraphs straight into an uneven roll. We lean toward the deeper end of the state's allowed base depth on a green specifically, rather than splitting the difference, and we check the contour with a level at each compaction pass instead of only at the finish.</p>"),
            ("Where a chipping pad and fringe actually fit",
             f"<p>A short-game setup, cup, fringe and a small chipping pad, generally needs less continuous open ground than the green surface itself suggests, since the fringe can wrap a tighter curve than a true putting surface can. On a Union Park lot where the sunny footprint is narrow, that often means one full-size cup with a compact fringe rather than multiple holes. {svc('putting', 'Our putting green page')} goes through fringe and cup options in more depth.</p>"),
        ],
        "scenario": ("A compact green on a shaded Union Park lot",
                     f"<p>Say a Union Park backyard has a 400 sq ft sunny corner clear of the property's live oaks, enough for a single-cup green with a modest fringe. At {price('putting')} a square foot installed, that runs roughly $5,600 to $12,000, with most jobs closer to {price('putting', True)} a foot, or about $7,200 to $10,000 total. Contouring and a cup or two sit inside that per-foot range rather than as add-ons. Because the green has to clear the drip line of a nearby oak by design, the actual footprint sometimes ends up an irregular shape rather than the rectangle a homeowner first pictured, which is normal on a lot this shaded.</p>"),
        "faqs": [
            faq("Can a putting green go under an oak tree in Union Park?", "Not inside the drip line, unless a certified arborist signs off on it first. On most Union Park lots that rule is what decides the green's shape and location more than anything else in the design."),
            faq("Does a small Union Park lot limit putting green size?", "It limits the sunny, unobstructed footprint more than the lot size itself. A quarter-acre ranch lot usually has enough open ground for a modest single-cup green once the shaded area under mature trees is subtracted."),
            faq("How does Union Park's sandy soil affect a putting green's roll?", "The flatwoods sand underneath drains slowly, so an unevenly compacted base can settle over time and throw off the roll. Building the base in full compacted lifts matters more here than on a plain lawn, where a small dip is far less noticeable."),
        ],
        "sources": SRC,
    },
    "playground": {
        "title": "Playground Turf Installation in Union Park, FL",
        "meta": "Cushioned playground turf for Union Park backyards near Jay Blanchard Park, sized to equipment fall height, with 2026 pricing and sources.",
        "h1": "Backyard play turf for Union Park families",
        "lede": capsule(f"Playground turf in Union Park runs {price('playground')} a square foot installed, typically {price('playground', True)}, with the shock pad sized to whatever equipment sits on top of it. About half of Union Park's roughly 10,450 residents identify as Hispanic or Latino in the 2020 Census, and this is one of the more family-heavy communities we work in, which is exactly the mix that keeps backyard play turf on our schedule here."),
        "sections": [
            ("Why families here often build rather than drive to the park",
             f"<p>Jay Blanchard Park, off Dean Road, and the paved Little Econ Greenway running through it are Union Park's main public green space, and both see heavy use on weekends. A backyard play surface doesn't replace a public trail or a ball field, but it does cover the smaller, everyday need, a swing set, a trampoline, a spot for a toddler to fall safely, without loading kids into a car first. {post('is-artificial-turf-safe-for-kids-pfas-lead', 'Material safety for a play surface')} is worth reading alongside this page.</p>"),
            ("The infill rule that actually governs a Union Park play area",
             f"<p>Florida's May 2026 turf standard allows rubber or other synthetic infill only inside the footprint of playground equipment itself, never across the rest of a residential lawn. In practice that means a Union Park backyard often carries two different builds side by side: a rubber or engineered infill zone sized to the equipment's fall height directly under a swing set or slide, and ordinary silica-infilled turf everywhere else in the yard. {a('/laws/florida-hb-683/', 'the exact rule wording')} is on our HB 683 page.</p>"),
            ("Building a play area over Union Park's flatwoods sand",
             "<p>The same Immokalee and Myakka fine sands that sit under most Union Park lawns also sit under a backyard play area, and a seasonally high water table means the base has to work harder here than it would on a better-draining ridge lot elsewhere in Central Florida. We build toward the deeper end of the state's crushed-rock range under a play zone specifically, since standing water under a shock pad defeats the point of the pad faster than under open lawn.</p>"),
        ],
        "scenario": ("A backyard play area near Jay Blanchard Park",
                     f"<p>Say a Union Park family a few blocks from Jay Blanchard Park wants a 300 sq ft play area for a swing set and a trampoline, on a lot where the rest of the backyard stays open lawn. At {price('playground')} a square foot installed, that runs roughly $3,000 to $7,500, with most jobs closer to {price('playground', True)} a foot, or about $3,600 to $5,700. Shock-pad thickness under the swing set's fall zone accounts for most of the spread within that range, since a taller structure needs a deeper pad than a low trampoline does. The rest of the yard, turfed separately in ordinary silica-infill turf, prices at the standard residential range rather than the play-area rate.</p>"),
        "faqs": [
            faq("Can rubber infill go anywhere in a Union Park backyard?", "Only inside the footprint of playground equipment, under Florida's May 2026 turf rule. The rest of the yard has to use silica sand, rock, shell or a coated natural-material infill instead."),
            faq("Does Jay Blanchard Park count toward what a Union Park yard needs?", "No, a public park doesn't change any permitting or setback rule for a private backyard project. It's simply the community's main open space, which is part of why backyard play turf tends to serve as a supplement rather than a replacement here."),
        ],
        "sources": SRC,
    },
    "pool": {
        "title": "Pool & Lanai Turf in Union Park, FL",
        "meta": "Turf around Union Park pool decks and screen enclosures, kept clear of the Little Econ setback, with drainage details and 2026 pricing.",
        "h1": "Turf for Union Park pool decks and lanais",
        "lede": capsule(f"A turf strip beside a pool or inside a screen enclosure in Union Park tends to price near the top of the residential range, {price('residential')} a square foot installed, since a small, tightly bordered area takes more edging and labor per foot than an open lawn. On the older ranch lots here, that strip sometimes runs the last few feet toward a retention pond or the Little Econlockhatchee corridor rather than stopping at a fence."),
        "sections": [
            ("Screen enclosures on a 1970s Union Park pool home",
             "<p>A pool cage added onto an older Union Park ranch home usually leaves a narrow band of ground between the enclosure's edge and the property line, too tight and too shaded by the structure itself for grass to hold on consistently. That band takes a glue-down or nailed edge where it meets the concrete pool deck, since there's no soil at that exact seam to anchor into the way the rest of a lawn's perimeter does.</p>"
             + "<p>Because the space is small, per-foot pricing runs higher than an open backyard would, even though the total job cost is often lower simply because there's less area to cover.</p>"),
            ("When a pool lot backs onto the Little Econ setback",
             f"<p>Some Union Park pool homes back directly onto a retention pond or the Little Econlockhatchee corridor, and where that's the case, turf still has to stop at least 10 feet from the water under {a('/laws/florida-hb-683/', 'the state turf rule')}. Only an existing seawall or bulkhead changes that math; a pool cage itself doesn't, since the rule measures from the water's edge, not from any structure standing between the two.</p>"),
            ("Drainage underneath turf on a concrete pool deck",
             f"<p>Turf laid directly over an existing concrete pool deck needs a drainage underlay beneath it, since concrete itself doesn't perc the way Union Park's native flatwoods sand does, and without that layer, water from a rinse or a storm has nowhere to go but sideways under the turf. {post('install-artificial-turf-over-concrete-pavers-or-grass', 'Installing over concrete, pavers or existing grass')} covers that underlay in more detail than fits on this page.</p>"),
        ],
        "scenario": ("A pool-cage turf strip on an older Union Park lot",
                     f"<p>Say a 1978 Union Park pool home has a 250 sq ft band of ground inside the screen enclosure, between the concrete deck and the cage's edge, currently bare dirt where grass never took in the shade. At {price('residential')} a square foot installed, that runs roughly $2,000 to $4,500 for the strip, landing nearer {price('residential', True)} a foot for a job this size, or about $2,500 to $4,000. A drainage underlay where the turf meets the concrete deck, and a glue-down bond at that same seam, both sit inside that per-foot figure rather than pricing as extras.</p>"),
        "faqs": [
            faq("Does turf near a Union Park retention pond need a permit?", "Nothing published singles out a permit for that specifically, but the 10-foot waterbody setback in the state's May 2026 rule still applies regardless of whether a permit is required. Check the setback before finalizing a layout on any pond-adjacent lot."),
            faq("Can turf go all the way to a pool cage's edge in Union Park?", "Yes, turf can run up to the enclosure's edge; it just needs a glue-down or nailed bond at that seam rather than the nail-and-soil anchor used on an open lawn's perimeter, since there's no soil right at that line."),
        ],
        "sources": SRC,
    },
    "repair": {
        "title": "Artificial Turf Repair in Union Park, FL",
        "meta": "Repairing lifted seams, wrinkles and drainage failures on Union Park turf, priced after photos or a site visit rather than by the foot.",
        "h1": "Fixing tired turf on a Union Park lot",
        "lede": capsule("Turf repair in Union Park is quoted after photos or a site visit rather than by the square foot, since a lifted seam, a wrinkled panel and a drainage failure each take different work to fix. About 22 miles from Kissimmee, Union Park has enough older turf installations, some original to a resale home, that repair calls here are as common as new installs."),
        "sections": [
            ("Why an older Union Park lawn needs more than a re-glue",
             "<p>A fair number of Union Park's turf repair calls involve a lawn installed years ago by a previous owner or a different contractor, on a base that may never have matched the washed, open-graded crushed rock the state's rule now specifies. Unwashed fill clogs with fine particles over time and stops draining, so a seam that keeps lifting in the same spot after every fix is often a base problem wearing a seam problem's clothes.</p>"
             + "<p>Diagnosing that difference before quoting anything is the point of a site visit rather than a phone estimate, since pulling back a corner to check the base underneath tells us more in five minutes than a description ever could.</p>"),
            ("Union Park's water table and what it does to a bad base",
             f"<p>Immokalee and Myakka fine sands, the flatwoods soils under most Union Park yards, run a seasonally high water table, one that can stay just beneath the surface for weeks once summer rains set in. A base that was compacted too thin, or built from fill that later crusted over, can't move that groundwater fast enough once heavy rain adds to it, and the result is a lawn that holds standing water for days rather than draining the 30-plus inches an hour turf backing itself is built for. {post('does-artificial-turf-drain-in-heavy-rain', 'Drainage failures like this')} usually trace back to the base, not the turf.</p>"),
            ("Storm damage and the drip-line rule during a repair",
             f"<p>A tropical storm or a summer downpour tends to expose whatever was already marginal on an older Union Park lawn, a corner nailed instead of properly bonded, an edge that was never anchored to withstand wind. Where a repair also involves excavating near a mature oak, the same drip-line rule that governs a new install applies to the fix, so a certified arborist's sign-off is still required before digging closer than the canopy allows. {post('artificial-turf-hurricane-flooding', 'What happens to turf in a storm or flood')} covers the broader pattern.</p>"),
        ],
        "scenario": ("A lifted seam after a decade on a Union Park lawn",
                     "<p>Say a Union Park homeowner in a resale ranch home notices a 12-foot seam along the yard's low side has started lifting after every hard rain, with water pooling nearby for a day or two afterward. A site visit would check whether the seam bond itself failed or whether the base beneath it settled unevenly, since those two problems look identical from the surface but call for different fixes, a re-seam versus pulling back that section to rebuild the base underneath. Photos of the lifted area and how long water sits after a storm help us scope the visit before anyone drives out, though a firm number still waits until we've seen the base in person.</p>"),
        "faqs": [
            faq("Why does my Union Park turf hold water after storms?", "Usually the base, not the turf. Backing drains at over 30 inches an hour on its own, so standing water almost always means the crushed-rock layer underneath was built too thin, compacted too tight, or made from fill that crusted over."),
            faq("Can you repair turf that was installed by someone else in Union Park?", "Yes. Most repair calls here involve turf from a previous owner or another contractor. A site visit tells us what base is actually underneath, which matters more for pricing than who originally installed it."),
        ],
        "sources": SRC,
    },
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
