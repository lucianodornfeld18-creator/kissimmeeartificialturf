# -*- coding: utf-8 -*-
"""Conway, FL (tier 2): unincorporated CDP in Orange County between Lake Conway and Orlando
International Airport. Researched September 2026; see docs/TIER2-BRIEF.md."""
from _helpers import page, capsule, sec, table, faq, a, svc, city, county, src, ext, price
from _cityservice import cityservice_pages

SLUG = "conway"

SRC = [
    ("Orange County Water Atlas — Boggy Creek Watershed", "https://orange.wateratlas.usf.edu/watershed/?wshedid=2"),
    ("Orange County Water Atlas — Boggy Creek", "https://orange.wateratlas.usf.edu/waterbodies/rivers/130001/boggy-creek"),
    ("Orange County Water Atlas — Lake Conway", "https://orange.wateratlas.usf.edu/waterbodies/lakes/140148/lake-conway"),
    ("South Florida Water Management District — Upper Kissimmee Basin water supply plan", "https://www.sfwmd.gov/our-work/water-supply/upper-kissimmee"),
    ("U.S. Census Bureau QuickFacts — Conway CDP, Florida", "https://www.census.gov/quickfacts/conwaycdpflorida"),
    ("Wikipedia — Conway, Florida", "https://en.wikipedia.org/wiki/Conway,_Florida"),
    ("Wikipedia — List of neighborhoods in Orlando, Florida", "https://en.wikipedia.org/wiki/List_of_neighborhoods_in_Orlando,_Florida"),
    ("Orange County Utilities — water service", "https://www.orangecountyfl.net/watergarbagerecycling/waterservice.aspx"),
    ("OUC — water services", "https://www.ouc.com/about/water-services/"),
    ("Orange County Code, Chapter 24, Municode Library", "https://library.municode.com/fl/orange_county/codes/code_of_ordinances?nodeId=PTIIORCOCO_CH24LABUOPSP"),
    ("Orange County Fast Track Online Services", "https://fasttrack.ocfl.net/OnlineServices/"),
    ("Orange County Property Appraiser — parcel search", "https://ocpafl.org/"),
    ("USDA NRCS — official series description, Candler series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/C/CANDLER.html"),
    ("USDA NRCS — official series description, Astatula series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/A/ASTATULA.html"),
    ("Ben Laube Homes — Conway homes for sale and neighborhood guide", "https://www.benlaubehomes.com/central-florida-communities/conway"),
    ("ClickOrlando (WKMG), April 18, 2019 — flight-path relief sought for Conway and Belle Isle residents", "https://www.clickorlando.com/news/2019/04/18/relief-possibly-coming-for-residents-living-under-orlando-international-flight-path/"),
    "dep-rule", "fs125572", "hb683", "fs7203045",
]

CANDLER = ("USDA NRCS — official series description, Candler series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/C/CANDLER.html")
ASTATULA = ("USDA NRCS — official series description, Astatula series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/A/ASTATULA.html")
LAKE_ATLAS = ("Orange County Water Atlas — Lake Conway", "https://orange.wateratlas.usf.edu/waterbodies/lakes/140148/lake-conway")
BOGGY_WSHED = ("Orange County Water Atlas — Boggy Creek Watershed", "https://orange.wateratlas.usf.edu/watershed/?wshedid=2")
BOGGY_CREEK = ("Orange County Water Atlas — Boggy Creek", "https://orange.wateratlas.usf.edu/waterbodies/rivers/130001/boggy-creek")
SFWMD_KISS = ("South Florida Water Management District — Upper Kissimmee Basin water supply plan", "https://www.sfwmd.gov/our-work/water-supply/upper-kissimmee")
OC_UTIL = ("Orange County Utilities — water service", "https://www.orangecountyfl.net/watergarbagerecycling/waterservice.aspx")
OUC = ("OUC — water services", "https://www.ouc.com/about/water-services/")
CH24 = ("Orange County Code, Chapter 24, Municode Library", "https://library.municode.com/fl/orange_county/codes/code_of_ordinances?nodeId=PTIIORCOCO_CH24LABUOPSP")
FASTTRACK = ("Orange County Fast Track Online Services", "https://fasttrack.ocfl.net/OnlineServices/")
ORANGE_PA = ("Orange County Property Appraiser — parcel search", "https://ocpafl.org/")
CENSUS = ("U.S. Census Bureau QuickFacts — Conway CDP, Florida", "https://www.census.gov/quickfacts/conwaycdpflorida")
WIKI_CONWAY = ("Wikipedia — Conway, Florida", "https://en.wikipedia.org/wiki/Conway,_Florida")
WIKI_ANNEX = ("Wikipedia — List of neighborhoods in Orlando, Florida", "https://en.wikipedia.org/wiki/List_of_neighborhoods_in_Orlando,_Florida")
BENLAUBE = ("Ben Laube Homes — Conway homes for sale and neighborhood guide", "https://www.benlaubehomes.com/central-florida-communities/conway")
AIRPORT = ("ClickOrlando (WKMG), April 18, 2019 — flight-path relief sought for Conway and Belle Isle residents", "https://www.clickorlando.com/news/2019/04/18/relief-possibly-coming-for-residents-living-under-orlando-international-flight-path/")

PERMIT_ROUTE = ("/laws/permits/orange-county/", "Orange County turf permit rules")

# ============================================================== HUB
HUB = page(
    "/areas/conway/", "city",
    "Artificial Turf in Conway, FL: Unincorporated Orange County",
    "Synthetic turf installation for Conway, an unincorporated Orange County community between Lake Conway and Orlando International Airport. Checked September 2026.",
    "Turf work on Conway's lake chain and airport-side streets",
    capsule(f"Conway has no city hall of its own: it is an unincorporated community, so a permit question goes to Orange County rather than a Conway building department. Kissimmee Artificial Turf installs synthetic lawns, pet turf and putting greens here at {price('residential')} per square foot as of September 2026, on 1950s-era ranch lots between Lake Conway and Orlando International Airport, about 15 miles from our Kissimmee base."),
    "".join([
        sec("Conway has no building department, and that changes who you call",
            f"<p>Conway is a census-designated place, not a city, which means every permit question routes to {a('/laws/permits/orange-county/', 'the Orange County Division of Building Safety')} rather than a Conway city hall that doesn't exist. The county's landscaping ordinance never even reaches the synthetic question: Chapter 24 limits its definition of the word to Bahia, St. Augustine and other living species, leaving nothing on the books for a manufactured surface one way or the other ({src('dep-rule', 'a gap the state rule now caps regardless')}; {ext(CH24[1], 'Chapter 24')}). Permitting Services takes calls at 407-836-5550 and applications through {ext(FASTTRACK[1], 'Fast Track Online Services')}.</p>"
            + f"<p>One wrinkle worth checking before assuming that: part of Conway was annexed into the City of Orlando between 1964 and 1973, and the community today sits only partly inside Orlando's limits ({ext(WIKI_ANNEX[1], 'Orlando’s own neighborhood list')}). A lot on that edge can answer to Orlando's building code, which does name artificial turf, instead of the county's silence. A quick search on the {ext(ORANGE_PA[1], 'Orange County Property Appraiser')} site settles which office actually has a given address before anyone applies for anything.</p>"),
        table("Conway yard types and what we do differently",
              ["Yard type", "What we see", "What changes about the install"],
              [["Lake Conway chain frontage", "Boat docks, screened lanais, older seawalls", "State's 10-ft waterbody setback, waived where a seawall already separates yard from water"],
               ["Inland 1950s–70s ranch lot", "8,000–12,000 sq ft, oak canopy from decades of growth", "Drip-line rule; base often runs the fuller 4 in where roots have loosened the sand"],
               ["Airport-corridor infill and newer builds", "Rebuilt or expanded homes near the MCO approach path", "No turf-specific change, just a hotter, noisier jobsite most afternoons"],
               ["Orlando-annexed edge parcel", "Same architecture, different building department", "Permit goes through Orlando's engineering process, not the county's quiet code"]],
              "Yard types as observed on Conway jobs; permit column reflects each office's published rule as of September 2026, not a guarantee for a specific parcel."),
        sec("Which agency actually manages Conway's water",
            f"<p>Two different offices can appear on a Conway water bill. Orange County Utilities bills most of the unincorporated community, while a strip closer to the Orlando line can instead be billed by the Orlando Utilities Commission (OUC), which serves the city plus adjoining county pockets ({ext(OC_UTIL[1], 'Orange County’s water service page')}; {ext(OUC[1], 'OUC’s water services page')}). Either way, the state's May 2026 rule already bars watering a synthetic lawn from an in-ground system once the heads underneath are capped, so the specific utility only matters for whatever lawn or bed stays natural.</p>"
            + f"<p>The lake chain itself answers to a district most of Orange County doesn't. Most of the county drains north toward the St. Johns River, but the county's own water atlas maps Lake Conway into the Boggy Creek Watershed, whose namesake stream runs south into East Lake Tohopekaliga ({ext(BOGGY_WSHED[1], 'Boggy Creek Watershed, general information')}; {ext(BOGGY_CREEK[1], 'the Boggy Creek entry itself')}). That puts Conway's chain under the South Florida Water Management District's Upper Kissimmee Basin planning umbrella, the same district that covers most of neighboring Osceola County, rather than the St. Johns district that serves Orlando just to the north ({ext(SFWMD_KISS[1], 'SFWMD’s Upper Kissimmee Basin plan')}).</p>"),
        sec("Ranch homes, a lake chain and the ground under both",
            f"<p>Conway's housing stock is mostly 1950s–1970s ranch-style homes on lots running 8,000 to 12,000 square feet, with a mix of 1980s–90s builder product and newer custom lakefront construction filling the gaps ({ext(BENLAUBE[1], 'a Conway neighborhood profile')}). The 2020 Census counted 13,596 residents in the CDP ({ext(CENSUS[1], 'Census QuickFacts, Conway CDP')}), and decades of that growth means most lots now carry oak canopy old enough to trigger the state's drip-line rule on any job that gets close to a trunk.</p>"
            + f"<p>The Water Atlas puts the Conway chain, Lake Conway itself plus its connected waters, at 1,771 surface acres ({ext(LAKE_ATLAS[1], 'the Lake Conway entry')}), which is why lakefront turf work here runs into the 10-ft waterbody setback more often than in a landlocked neighborhood, waived only where a seawall already stands between yard and water. Away from the shoreline, Orange County's soil survey maps the community's higher ground to Candler and Astatula fine sands, excessively drained ridge soils built from wind-blown and marine deposits rather than the flatter, wetter flatwoods sand common in most of Osceola County next door ({ext(CANDLER[1], 'Candler series description')}; {ext(ASTATULA[1], 'Astatula series description')}).</p>"),
        sec("Permits, HOA paperwork and the state's May 2026 floor",
            f"<p>Nothing above changes what {a('/laws/florida-hb-683/', 'HB 683 and Rule 62-308.100')} already requires on a covered single-family lot: turf on permeable backing over a washed, open-graded base, irrigation heads capped rather than watering the turf, and infill limited to silica, zeolite or another natural material. A Conway HOA is a separate question again; {a('/laws/hoa-rules/', 'F.S. 720.3045')} protects turf an association can't see from the street or a neighboring lot, not a front yard.</p>"
            + "<p>Searching for the best artificial turf contractor near you in Conway usually comes down to three checks: does the crew already know which building department has your specific parcel, does the quote name base depth and infill by product, and does it account for a lakefront lot's setback before pricing the job.</p>"),
        "<!--AUTO:city-services-->",
    ]),
    faqs=[
        faq("Is my Conway address inside Orlando or unincorporated Orange County?",
            "It depends on the parcel. Conway was annexed into Orlando in pieces between 1964 and 1973 and today sits only partly within the city, so two houses a block apart can answer to different building departments. A search on the Orange County Property Appraiser's site shows the taxing jurisdiction for a specific address."),
        faq("Does Orange County Utilities or OUC serve my street in Conway?",
            "Either can, depending on how close the address sits to the Orlando line. Orange County Utilities bills most of unincorporated Conway; the Orlando Utilities Commission bills the city plus some adjoining county pockets. Checking a recent bill is faster than guessing, and it stops mattering for turf itself once the irrigation heads are capped."),
        faq("Does living on the Lake Conway chain change the setback for turf?",
            "A shoreline lot still has to keep synthetic turf ten feet back from the water, the same figure that applies statewide, and the only way around it is an existing seawall or bulkhead standing between the yard and the lake. We found no Conway-specific buffer published beyond that state number as of September 2026."),
        faq("Does Orlando International Airport's flight path affect a turf installation in Conway?",
            "Not the build itself. Conway sits close enough to the airport that residents have asked the FAA for relief from arrival and departure noise in the past, which is worth knowing before scheduling an outdoor walkthrough, but it has no bearing on base depth, drainage or the state's material standard."),
        faq("How far is Conway from your Kissimmee crew?",
            "About 15 miles by straight line, which keeps it well inside the roughly 40-mile radius we work within. The published Central Florida price range doesn't change with that distance."),
    ],
    sources=SRC, city=SLUG, crumbs=[("Service areas", "/areas/")], crumb="Conway",
    related=[("/areas/orange-county/", "Artificial turf in Orange County"), PERMIT_ROUTE, ("/areas/edgewood/", "Turf in Edgewood"), ("/areas/pine-castle/", "Turf in Pine Castle"), ("/artificial-turf-cost/", "Full turf cost guide")],
)

# ============================================================== LOCAL
LOCAL = {
    "residential": {
        "title": "Artificial Grass Installation in Conway, FL – No City Hall",
        "meta": "Synthetic lawn installs for unincorporated Conway, FL, where Orange County, not a city office, reviews the permit. Prices and rules checked September 2026.",
        "h1": "A synthetic lawn on an unincorporated Conway lot",
        "lede": capsule(f"Conway has no municipal building office, so a lawn conversion here answers to Orange County's permitting rules rather than a city code. A synthetic lawn prices at {price('residential')} a square foot as of September 2026 whether it goes in on the lake chain or a block inland, on ranch homes that mostly date to the 1950s and 1960s."),
        "sections": [
            ("What Orange County's silence on turf actually means here",
             f"<p>Orange County Code Chapter 24 spells out landscaping rules in terms of living grass species and never uses the words synthetic or artificial turf, so a Conway lawn swap isn't tripping a written local ban ({ext(CH24[1], 'Chapter 24, Municode')}). That's not the same as a stated exemption from ordinary permitting, and capping the irrigation heads under the new lawn, required by the state's May 2026 standard, can still call for its own review. Permitting Services takes that question at 407-836-5550, and applications run through {ext(FASTTRACK[1], 'Fast Track Online Services')}, the same portal every unincorporated Orange County project uses.</p>"),
            ("Checking whether a specific Conway lot is even in the county",
             f"<p>Part of the Conway area became Orlando between 1964 and 1973, and the community today is only partly inside the city ({ext(WIKI_ANNEX[1], 'Orlando’s neighborhood annexation list')}). That distinction is worth more than a formality for a lawn conversion, since Orlando's own landscape code names artificial turf specifically, with a different permit process than the county's quiet chapter. A search on the {ext(ORANGE_PA[1], 'Orange County Property Appraiser')} site shows which office holds a given parcel before anyone files anything, and settling that first avoids applying to the wrong department entirely.</p>"),
            ("Ranch-era lots and the oaks that came with them",
             f"<p>Conway's housing stock leans heavily toward 1950s and 1960s ranch homes on lots between 8,000 and 12,000 square feet, mixed with later builder product and newer lakefront construction ({ext(BENLAUBE[1], 'a Conway housing profile')}). Decades of growth on those lots means a live oak's canopy, and its drip line, comes up on a large share of Conway lawn jobs, more than on a newer subdivision built with saplings. The state's certified-arborist exception is the only way around that line once a canopy actually reaches into the planned turf area.</p>"
             + f"<p>{a('/blog/artificial-turf-near-live-oaks-and-palms/', 'Our guide to turf near live oaks and palms')} goes deeper on what that arborist's letter needs to say, and the {svc('residential', 'general residential installation guide')} covers the base and product choices behind the price range above. See the {city('conway', 'Conway turf guide')} for how the rest of the community compares, or {city('pine-castle', 'Pine Castle')}, {city('hunters-creek', 'Hunters Creek')} and {city('belle-isle', 'Belle Isle')} for nearby lots with their own version of the same oak canopy.</p>"),
        ],
        "scenario": ("Say you have an 1,100 sq ft backyard behind a 1962 ranch home",
                     f"<p>A typical Conway backyard behind a 1960s ranch runs 1,100 square feet once the patio slab and a side path are subtracted, with a live oak holding down one back corner. At the published {price('residential', True)} typical range, that lawn prices between $11,000 and $17,600 before any drip-line work near the oak changes the shape of the buildable area. If the lot backs onto one of the Conway chain's canals rather than a neighbor's fence, the crew also stakes the state's 10-foot waterbody line during layout, before ordering material, so the quote reflects the actual turf footprint rather than the property line on a survey. None of that changes the per-square-foot range itself; it changes how much of the 1,100 square feet ends up buildable once the oak and the water both get their own setback.</p>"),
        "faqs": [
            faq("How do you find the best artificial grass installer near you in Conway?",
                "Ask whether the crew already knows Conway is unincorporated, since that changes which office reviews a permit question, and whether the quote separates base depth from turf product rather than quoting one lump number. A contractor who raises the annexation question unprompted has clearly worked here before."),
            faq("Does a 1960s Conway home need a different base than a newer build?",
                "The base recipe is the same, washed crushed rock or crushed concrete two to four inches deep, but an older lot's soil has usually settled and compacted on its own over sixty-plus years, which can make excavation slower without changing the finished depth the state rule requires."),
        ],
        "sources": SRC,
    },
    "pet": {
        "title": "Pet Turf & Dog Runs in Conway, FL Near the Lake Chain",
        "meta": "Dog-run turf for Conway, FL homes on the Lake Conway chain, with the state's waterbody setback and capped irrigation explained. Checked September 2026.",
        "h1": "Dog runs on Conway's lakefront and inland lots alike",
        "lede": capsule(f"A dog run on the Lake Conway chain has to answer to the state's 10-foot waterbody setback before anything else; one three blocks inland usually doesn't. Pet turf here runs {price('pet')} per square foot as of September 2026, drains fast enough for daily rinsing, and skips the weed barrier a plain lawn often gets."),
        "sections": [
            ("Where a fenced yard meets 1,771 acres of connected lake",
             f"<p>The Conway chain, Lake Conway and the smaller waters tied to it by canal, covers 1,771 surface acres according to the county's own water atlas ({ext(LAKE_ATLAS[1], 'the Lake Conway entry')}), and a dog run on that shoreline sits inside the state's 10-foot setback zone unless a seawall or bulkhead already separates the yard from the water. Older Conway seawalls, some dating to the same 1950s and 60s wave of construction as the homes behind them, usually qualify for that exception, but a dock or a rock revetment alone does not. Staking the actual buildable line before ordering material keeps a dog-run quote honest about how much of a waterfront yard the rule allows to be turfed.</p>"),
            ("Grading a run toward Boggy Creek's own drainage, not away from it",
             f"<p>Conway's chain drains south into the Boggy Creek Watershed, whose namesake stream feeds East Lake Tohopekaliga and puts the community under the South Florida Water Management District's Kissimmee Basin planning area rather than the St. Johns district that covers most of Orange County ({ext(BOGGY_WSHED[1], 'Boggy Creek Watershed, general information')}). A dog run's own grading has nothing to do with that district line directly, but it matters for the irrigation question: whichever utility bills a specific Conway address, Orange County Utilities or OUC, its schedule stops applying to synthetic turf the moment the zone's heads are capped, which the state standard already requires.</p>"),
            ("Odor control on an older ranch lot's fenced side yard",
             f"<p>Conway's ranch homes typically carry a fenced side or back yard sized for a family dog rather than a purpose-built kennel run, and on an 8,000 to 12,000 square foot lot that fenced area is usually a modest slice of the total ({ext(BENLAUBE[1], 'a Conway lot-size profile')}). Zeolite or coated-sand infill fits that scale well, since a smaller area means rinsing takes less water and less time even on a hot Conway afternoon, and neither infill choice conflicts with the state's natural-material rule the way rubber crumb would.</p>"
             + f"<p>{a('/blog/how-to-get-dog-urine-smell-out-of-artificial-turf/', 'Our piece on clearing dog urine odor from turf')} covers the rinsing routine behind that infill choice, and the {svc('pet', 'pet turf and dog run guide')} goes through backing and drainage specs in more depth. The {city('conway', 'Conway turf guide')} above has the lake chain's setback figures; {city('belle-isle', 'Belle Isle')}, {city('orlando', 'Orlando')} and {city('edgewood', 'Edgewood')} all border the same water system from a different side.</p>"),
        ],
        "scenario": ("Say you have a 240 sq ft dog run along a lakefront fence line",
                     f"<p>A 240 square foot run along a Conway lakefront fence, common on an older lot where the dog yard sits between the house and the seawall, prices between $2,880 and $3,840 at the published {price('pet', True)} typical range. If that fence line sits within ten feet of the water and there's no seawall to claim the exception, the buildable run shrinks and the price follows the smaller footprint rather than the fence's actual length. On an inland Conway lot with no waterbody nearby, the same 240 square feet turfs at the identical rate, since the price range itself never changes; only the buildable area does.</p>"),
        "faqs": [
            faq("Does an older Conway seawall automatically qualify for the setback exception?",
                "Usually, if it's an intact seawall or bulkhead separating the yard from the water. A dock, a wood bulkhead in poor repair, or a rock revetment alone doesn't automatically qualify, so it's worth pointing the seawall out to the crew during the site visit rather than assuming."),
            faq("Which water utility do I check before scheduling irrigation capping in Conway?",
                "Look at a recent bill. Orange County Utilities serves most of the unincorporated community, and the Orlando Utilities Commission bills some addresses closer to the city line, but the capping step and its timing in the build don't change based on which one appears on the bill."),
        ],
        "sources": SRC,
    },
    "putting": {
        "title": "Backyard Putting Greens in Conway, FL Ranch Yards",
        "meta": "Putting green installation for Conway, FL's 1950s–70s ranch lots, with oak drip lines and lot size explained. Prices checked September 2026.",
        "h1": "A putting green on a Conway ranch lot's back forty feet",
        "lede": capsule(f"Conway's ranch lots run 8,000 to 12,000 square feet, big enough for a modest green without crowding the rest of the yard. Backyard putting greens here run {price('putting')} per square foot as of September 2026, and the census-counted 13,596 residents of the CDP live mostly on lots old enough to carry real oak canopy."),
        "sections": [
            ("Fitting a green onto an 8,000 to 12,000 sq ft ranch lot",
             f"<p>A Conway lot in that size range usually leaves a rear yard wide enough for a contoured green plus fringe without the retaining walls or terracing a much smaller urban lot would need ({ext(BENLAUBE[1], 'lot-size figures for the Conway area')}). The 2020 Census counted 13,596 residents across the CDP ({ext(CENSUS[1], 'Census QuickFacts')}), a population built up mostly on that same ranch-era lot pattern rather than newer, narrower subdivision frontages, which is part of why a green here tends to sit comfortably rather than fighting the yard's shape.</p>"),
            ("Oak canopy old enough to reach into the layout",
             f"<p>A canopy that's had sixty or seventy years to grow, common on Conway's original ranch lots, often reaches further into a backyard than a homeowner expects, and the state's turf rule keeps synthetic surfaces out of that drip line without a certified arborist's letter. Designing a green's breaks and tiers around an oak's actual canopy edge, not just its trunk, usually means shaping the layout before excavation starts rather than adjusting cups after a root gets found mid-dig.</p>"),
            ("A green on the chain's edge answers to the same setback as any other turf",
             f"<p>A putting green built on a lot backing onto the Conway chain still has to clear the state's 10-foot waterbody setback the same way a lawn or dog run does, waived only where a seawall already stands between the green and the water ({ext(LAKE_ATLAS[1], 'the Lake Conway entry, 1,771 surface acres')}). That line gets staked during layout on a waterfront green specifically because losing ten feet off one edge can force the whole design, cups included, several feet inland from an original plan.</p>"
             + f"<p>{a('/blog/artificial-turf-glossary/', 'Our glossary of turf terms')} explains stimp speed and break design in more depth than a city page needs, and the {svc('putting', 'putting green guide')} covers fringe and cup specs. {city('pine-castle', 'Pine Castle')}, {city('edgewood', 'Edgewood')} and {city('hunters-creek', 'Hunters Creek')} all carry a similar ranch-era lot pattern a few minutes from the {city('conway', 'Conway hub')}.</p>"),
        ],
        "scenario": ("Say you have a 320 sq ft green tucked under live oak shade",
                     f"<p>A 320 square foot green fit into the shadier half of a Conway ranch backyard, common where an old oak already shades the spot a homeowner wants to putt, prices between $5,760 and $8,000 at the published {price('putting', True)} typical range. If the oak's canopy actually overlaps part of that footprint, the arborist letter and the resulting layout change come before a number gets finalized, since the buildable shape can shift once the drip line is marked. A flatter, sunnier 320 square feet elsewhere on the same lot would price identically; shade changes contour planning and grooming, not the per-square-foot rate.</p>"),
        "faqs": [
            faq("Do Conway's older oaks make a putting green harder to design than a newer subdivision's?",
                "Sometimes. A decades-old canopy usually reaches further than a young tree's, which can eat into a planned green's footprint once the actual drip line gets marked, so it helps to walk the layout with the oak's real canopy edge in mind rather than a rough guess from the trunk."),
            faq("Can a putting green go on a Conway lot that backs onto the lake chain?",
                "Yes, outside the state's 10-foot waterbody setback unless a seawall already separates the lot from the water. That strip usually still leaves enough of an 8,000 to 12,000 square foot lot for a modest green once the buildable line is confirmed."),
        ],
        "sources": SRC,
    },
    "playground": {
        "title": "Playground Turf for Conway, FL Backyards",
        "meta": "Play-area turf for Conway, FL families near Orlando International Airport, with shock pad and shade notes. Prices checked September 2026.",
        "h1": "Play surfaces for Conway's ranch-lot backyards",
        "lede": capsule(f"Conway sits close enough to Orlando International Airport that overhead traffic is part of the neighborhood's background, which is worth knowing before scheduling an outdoor play-area walkthrough. Playground turf here runs {price('playground')} per square foot as of September 2026, cushioned with a shock pad sized to the equipment's fall height."),
        "sections": [
            ("A jobsite under a flight path, not a technical complication",
             f"<p>Conway sits close enough to Orlando International Airport that residents have petitioned the FAA in the past over arrival and departure noise from nearby flight paths ({ext(AIRPORT[1], 'ClickOrlando’s 2019 report on the complaints')}). None of that changes how a shock pad gets bonded or how deep the base runs under a play area, but it's worth building extra time into a walkthrough or a client conversation on an afternoon when departures are stacking up overhead, since a site visit near the corridor can simply be louder than one three miles further from the runways.</p>"),
            ("Why the ridge sand under Conway's higher ground behaves differently",
             f"<p>Conway's higher ground maps to Candler and Astatula fine sands on the county's own soil survey, excessively drained ridge soils that barely hold water at all ({ext(CANDLER[1], 'Candler series description')}; {ext(ASTATULA[1], 'Astatula series description')}). That's the opposite problem from the flatwoods sand common in most of Osceola County: a play area's shock pad here needs a stable, level base more than a fast-draining one, since the sand underneath already drains almost as quickly as the pad sitting on top of it.</p>"),
            ("Sizing a play surface to a ranch lot's actual yard",
             f"<p>On an 8,000 to 12,000 square foot Conway lot, a play area usually claims a defined corner rather than the whole backyard, leaving room for the rest of the family's lawn or a dog run on the same property ({ext(BENLAUBE[1], 'Conway lot-size figures')}). Containment edging around that corner, staked or a bender-board border, keeps rubber infill inside the equipment's own footprint, since the state's rule allows that material only directly under playground equipment, never spilling onto the surrounding lawn turf.</p>"
             + f"<p>{a('/blog/how-hot-does-artificial-turf-get-in-florida/', 'Our article on how hot turf gets in Florida')} explains the shock pad's own heat behavior in more depth, and the {svc('playground', 'playground turf guide')} covers ASTM fall-height ratings. The {city('conway', 'Conway turf guide')} above has the airport-corridor context; {city('hunters-creek', 'Hunters Creek')}, {city('orlando', 'Orlando')} and {city('belle-isle', 'Belle Isle')} handle similar play-area jobs near their own busy roads.</p>"),
        ],
        "scenario": ("Say you have a 380 sq ft play corner behind a ranch home",
                     f"<p>A 380 square foot play corner sized for a swing set and a small climbing structure, tucked into one side of a Conway backyard, prices between $4,560 and $7,220 at the published {price('playground', True)} typical range, with the shock pad thickness set by the tallest piece of equipment's fall height rather than a flat guess. If the corner sits near a live oak's edge, the state's drip-line rule applies to a play surface the same as any other turf, so the equipment layout gets checked against the canopy before the pad goes in. The lawn on the rest of the same 8,000 to 12,000 square foot lot prices separately, at the residential range rather than the playground one.</p>"),
        "faqs": [
            faq("Does living near Orlando International Airport affect how playground turf performs in Conway?",
                "No. Aircraft noise is an environmental fact of the neighborhood, not something that changes a shock pad's thickness, a base's drainage, or the turf's heat behavior, which follow the same state standard and product specs anywhere in Central Florida."),
            faq("Searching for the best playground turf installer near me in Conway? What should change your answer?",
                "Whether the crew asks about the specific play equipment's fall height before quoting a pad thickness, rather than offering one generic depth for every yard. That single question separates a spec-driven quote from a guess."),
        ],
        "sources": SRC,
    },
    "pool": {
        "title": "Pool & Lanai Turf in Conway, FL Screen Enclosures",
        "meta": "Turf around Conway, FL pool cages and lanais, including which building office reviews the permit depending on the parcel. Checked September 2026.",
        "h1": "Turf beside a Conway pool cage, whichever office reviews it",
        "lede": capsule(f"Whether a Conway pool project needs Orlando's permit process or the county's quieter one depends on the parcel, since part of the community was annexed into the city decades ago. Pool and lanai turf here runs {price('residential')} per square foot as of September 2026, glued at hardscape edges and drainage-backed under a screen enclosure."),
        "sections": [
            ("The annexation line that decides which permit a pool project follows",
             f"<p>Conway became part of Orlando in stages between 1964 and 1973, and the community today sits only partly inside the city's limits ({ext(WIKI_ANNEX[1], 'Orlando’s own annexed-neighborhoods list')}). That line matters more for a pool-area turf project than for most other jobs, since Orlando's landscape code names artificial turf specifically and calls for an engineering permit, while the county's Chapter 24 stays silent on the subject entirely. A parcel search on the {ext(ORANGE_PA[1], 'Orange County Property Appraiser')} site is worth doing before pricing a pool-cage job on an address near that boundary.</p>"),
            ("Drainage inside a screen enclosure built decades ago",
             f"<p>A lanai turf strip inside an older Conway pool cage needs a drainage underlay where the turf meets the existing deck, since the concrete slab underneath doesn't pass water the way soil does, and the state's permeability standard for anything on natural ground doesn't apply the same way over a hard surface. Many of Conway's enclosures date to the same 1950s–70s building wave as the ranch homes they're attached to, so a deck's control joints and slight settling over that span are worth checking before turf goes down tight to the concrete.</p>"),
            ("Capped irrigation around a pool deck, whichever utility bills the address",
             f"<p>Whether a Conway address is billed by Orange County Utilities or the Orlando Utilities Commission ({ext(OC_UTIL[1], 'Orange County’s water service page')}; {ext(OUC[1], 'OUC’s water services page')}), any spray head that used to reach the pool deck's border gets capped at installation, because neither utility's schedule can override a standard that keeps in-ground irrigation off synthetic turf entirely. That step happens early in a pool-area build, before the drainage underlay and turf go down.</p>"
             + f"<p>{a('/blog/install-artificial-turf-over-concrete-pavers-or-grass/', 'Our guide to installing turf over concrete, pavers or grass')} covers the same slab-adhesion question from the product side, and the {svc('pool', 'pool and lanai turf guide')} goes through backing choices for a glued edge. See the {city('conway', 'Conway turf guide')} for the annexation map, or {city('belle-isle', 'Belle Isle')}, {city('pine-castle', 'Pine Castle')} and {city('orlando', 'Orlando')} for more Orlando-adjacent pool-cage neighborhoods.</p>"),
        ],
        "scenario": ("Say you have a 260 sq ft border inside a screened pool cage",
                     f"<p>A 260 square foot strip of turf bordering a screened pool deck on a Conway lot, replacing a bare or gravel edge that never grew grass in the shade of the cage, prices between $2,600 and $4,160 at the published {price('residential', True)} typical range. If that specific address falls inside Orlando's annexed portion of Conway rather than the unincorporated county, the same job needs an engineering permit application before work starts, which adds paperwork and lead time without changing the per-square-foot price. Either way, the drainage underlay where turf meets the existing deck is the same regardless of which office signs off on the permit.</p>"),
        "faqs": [
            faq("Does a Conway pool project need Orlando's engineering permit or the county's process?",
                "It depends on whether the parcel sits inside Orlando's annexed portion of Conway or the unincorporated county around it. A property appraiser search settles that before applying, since the two offices review pool-area turf differently."),
            faq("Does an older Conway pool cage need extra prep before turf goes in?",
                "Often, yes. Enclosures built alongside 1950s–70s ranch homes have had decades to settle, so checking the deck's control joints and slab condition before installing a drainage underlay catches problems a newer cage usually doesn't have."),
        ],
        "sources": SRC,
    },
    "repair": {
        "title": "Turf Repair in Conway, FL Older Installations",
        "meta": "Turf repair for Conway, FL yards, from lakefront seams to ridge-sand base issues, priced after a site visit. Checked September 2026.",
        "h1": "Fixing turf on Conway's older lots and lakefront edges",
        "lede": capsule("Turf repair is priced after photos or a short site visit, not a published per-square-foot range, since the fix depends on what actually failed. In Conway, that's most often a lakefront seam, a driveway edge on a decades-old lot, or a base that was never washed rock in the first place."),
        "sections": [
            ("Reading a lifted seam near the Conway chain",
             f"<p>A seam or edge that lifts on a lot backing onto Lake Conway or one of its connected waters often traces back to the state's 10-foot setback line rather than a bonding mistake: turf installed too close to the water, or inside a swale carrying runoff toward it, sheds infill and stresses edges every time a storm pushes water across that strip ({ext(LAKE_ATLAS[1], 'the Lake Conway entry')}). A repair there usually means re-staking the actual setback line before patching, not just re-gluing the same edge in the same spot.</p>"),
            ("What an unwashed, pre-standard base looks like years later",
             f"<p>Conway's older installations, some predating the state's May 2026 material rule entirely, sometimes sit on a base that was never washed crushed rock, and Candler and Astatula's excessively drained ridge sand hides that problem differently than flatwoods soil would ({ext(CANDLER[1], 'Candler series description')}). Fines that bind into a crust show up less as standing water here and more as an uneven, slightly spongy surface that never quite firms back up after a reseam, since the ridge sand around the crust still drains even when the crust itself doesn't.</p>"),
            ("Matching a patch to a lawn that's been down for decades",
             f"<p>A repair on a Conway lawn installed years or even a decade ago has to account for UV fade and infill loss that a brand-new patch won't match on day one, since sun exposure on a ranch-lot's mostly unshaded front yard changes color faster than a shaded side yard's turf does. Cutting the patch to follow an existing seam or panel line, rather than just the visible damage, is what keeps a repair from reading as an obvious rectangle for its first year or two.</p>"
             + f"<p>{a('/blog/artificial-turf-hurricane-flooding/', 'Our article on turf after a hurricane or flood')} covers storm damage beyond a single lifted seam, and the {svc('repair', 'turf repair guide')} explains how a patch gets matched to existing product. The {city('conway', 'Conway turf guide')} above has the lake chain's setback figures; {city('edgewood', 'Edgewood')}, {city('orlando', 'Orlando')} and {city('pine-castle', 'Pine Castle')} face similar repair calls on their own older lots.</p>"),
        ],
        "scenario": ("Say a storm lifts an 8-ft seam along your lakefront fence",
                     "<p>An eight-foot section of lifted seam along a Conway lakefront fence line, the kind that shows up after a summer storm pushes water across a yard that sits close to the state's 10-foot setback, gets assessed on site rather than priced from a photo alone, since the fix depends on whether the original edge was ever properly bonded and whether the setback line itself was respected at installation. A crew checks the base underneath the lifted section for the telltale crust of an unwashed subgrade before quoting a reseam, because patching over a bad base just moves the same failure a few feet down the fence line at the next storm. The photo is useful for scheduling; the site visit is what sets the number.</p>"),
        "faqs": [
            faq("Why does turf near Conway's lake chain fail more often than an inland lawn?",
                "It's usually the setback and swale rules doing the work they're meant to do: turf installed too close to the water or inside a drainage path takes more direct water pressure during a storm than turf set back the required ten feet, which shows up as lifted edges and washed infill over time."),
            faq("Can you tell if my Conway lawn's base was ever washed rock without digging it up?",
                "Often, yes, from how the surface behaves. A spot that stays slightly spongy or uneven long after a storm passes, on Candler or Astatula sand that otherwise drains fast, is a common sign of fines that bound together under the turf rather than a drainage problem with the sand itself."),
        ],
        "sources": SRC,
    },
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
