# -*- coding: utf-8 -*-
"""Kenansville (tier 3, unincorporated Osceola County). Hub + residential/pet/putting only,
per docs/TIER2-BRIEF.md. Researched September 2026: Osceola County Building Department (facts
reused from c_permits.py), Florida Department of Health in Osceola County (onsite sewage program,
now under FDEP since July 1, 2021), Toho Water Authority's own service-area description, South
Florida Water Management District's Kissimmee River overview, FWC's Three Lakes Wildlife
Management Area page, USDA official series description for the Felda series, and Florida Memory's
record of the Heartbreak Hotel. The U.S. Census Bureau has never designated Kenansville its own
place, so no population figure is used or invented."""
from _helpers import page, capsule, sec, table, faq, note, a, svc, city, post, src, ext, price
from _cityservice import cityservice_pages
from _data import CITIES

SLUG = "kenansville"
MI = CITIES[SLUG]["miles"]

OSCEOLA_PERMITS = ("Osceola County Online Permit Center", "https://permits.osceola.org/")
OSCEOLA_PA = ("Osceola County Property Appraiser — parcel search", "https://www.property-appraiser.org/")
DOH_OSCEOLA = ("Florida Department of Health in Osceola County — onsite sewage disposal", "https://osceola.floridahealth.gov/programs-and-services/environmental-health/onsite-sewage-disposal/")
OSCEOLA_SEPTIC = ("Osceola County — septic and well permit requirements", "https://www.osceola.org/files/assets/county/v/1/doing-business/building-amp-permits/documents/buildercontractor-requirements-and-information/dept-of-health-septic-well-permit-requirements.pdf")
TOHO_AREA = ("Toho Water Authority — our service area", "https://www.tohowater.com/about-us/our-service-area")
SFWMD_KISS = ("South Florida Water Management District — Kissimmee River", "https://www.sfwmd.gov/our-work/kissimmee-river")
FWC_3LAKES = ("Florida Fish and Wildlife Conservation Commission — Three Lakes Wildlife Management Area", "https://myfwc.com/recreation/lead/three-lakes/")
FELDA_OSD = ("USDA NRCS — official series description, Felda series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/F/FELDA.html")
FL_MEMORY = ("Florida Memory — Webb's Heartbreak Hotel, Kenansville, Florida", "https://www.floridamemory.com/items/show/142791")

SRC = ["dep-rule", "fs125572", "fs7203045", "usda-wss",
       OSCEOLA_PERMITS, OSCEOLA_PA, DOH_OSCEOLA, OSCEOLA_SEPTIC, TOHO_AREA, SFWMD_KISS, FWC_3LAKES, FELDA_OSD, FL_MEMORY]


# ============================================================== hub
HUB = page(
    f"/areas/{SLUG}/", "city",
    "Artificial Turf in Kenansville, FL: Ranch Country Guide",
    "Synthetic turf for Kenansville, FL ranch and lake properties: well-and-septic lots, Osceola County permits and 2026 Central Florida pricing.",
    "Artificial turf out in Kenansville's ranch country",
    capsule(f"Kenansville sits about {MI} miles southeast of our Kissimmee base, on US-441 in the cattle country at the far end of Osceola County. We take turf jobs out here, priced the same {price('residential')} a square foot as anywhere else we work as of September 2026, though a well-and-septic ranch lot is a rarer call for us than a subdivision closer to town."),
    "".join([
        sec("Ranch country at the edge of where we work",
            f"<p>Everywhere else in Osceola County, we are working a subdivision lot with municipal water and a neighbor within shouting distance. Kenansville is different: an unincorporated ranching community strung along US-441, closer to Lake Kissimmee and the Kissimmee Prairie than to another rooftop. Lots here commonly run well past the one-acre ceiling the state's synthetic-turf standard actually covers, which means a lot of what applies automatically on a quarter-acre Kissimmee yard, the preemption against a local turf ban, the capped local permeability number, simply is not in play on a bigger parcel out here. We are honest that jobs this far out are occasional rather than routine, and a Kenansville install typically gets scheduled around other far-south Osceola stops rather than as a standalone trip.</p>"),
        table("Kenansville yard types and what we do differently",
              ["Yard type", "What it looks like", "What changes for us"],
              [["Cattle-ranch homesteads", "House and yard on a multi-acre working parcel", "Often over the state rule's one-acre ceiling, so only Osceola County's own code, silent on turf, applies"],
               ["Lake Marian and canal fish camps", "Waterfront lots along Lake Marian or a connecting canal", "The state's 10-ft waterbody setback, no exception without a seawall"],
               ["US-441 roadside homes", "Older homes near the Heartbreak Hotel and the town's small core", "Smaller, more typical lots; well and septic instead of a municipal utility"],
               ["New rural homesites near Three Lakes WMA", "Acreage bordering the wildlife management area", "Fencing planned around a shared boundary with conservation land, not a neighbor's yard"]],
              f"The rate does not change out here either: {price('residential')} a square foot, same as a Kissimmee subdivision."),
        sec("Permits: Osceola County, not a city hall",
            f"<p>Kenansville has no city government of its own, so every permit question runs through the Osceola County Building Department at 407-742-0200, with applications filed through the county's {ext(OSCEOLA_PERMITS[1], 'Online Permit Center')}. As of September 2026 the county's Land Development Code does not mention synthetic turf, the same silence that applies countywide, so {a('/laws/permits/osceola-county/', 'our Osceola County permit page')} covers this address as well as it covers a lot inside the Kissimmee city limits. A parcel search on the {ext(OSCEOLA_PA[1], 'Osceola County Property Appraiser’s site')} confirms boundaries and acreage before a permit conversation starts, and acreage is the number that matters most here: {a('/laws/florida-hb-683/', 'the state’s May 2026 turf standard')} only reaches a single-family lot of one acre or less, so a bigger ranch parcel answers to the county's ordinary code alone. We found no CDD or HOA covering this part of the county, so {a('/laws/hoa-rules/', 'Florida’s association visibility statute')} rarely comes up, though it would still apply to any property that does carry a recorded association.</p>"),
        sec("No city water out here: wells, septic and a state rule that follows",
            f"<p>{ext(TOHO_AREA[1], 'Toho Water Authority’s own service-area description')} centers on Kissimmee, St. Cloud, Poinciana and the unincorporated areas close to them; we found no utility, Toho or otherwise, that lists Kenansville or the ranch country around it as served territory. A home out here typically supplies its own water from a private well and treats wastewater with a septic system, permitted through the {ext(DOH_OSCEOLA[1], 'Florida Department of Health in Osceola County')}, whose onsite-sewage program moved under the Florida Department of Environmental Protection on July 1, 2021 ({ext(OSCEOLA_SEPTIC[1], 'the county’s septic and well permit checklist')}). That changes the turf checklist more than a municipal-water lot ever would: the state standard's requirement to keep a septic tank's pump-out lid reachable actually matters here, on nearly every job, instead of coming up only on the rare Kissimmee lot that never connected to Toho.</p>"),
        sec("Lakes, prairie and a river basin, not a subdivision pond",
            f"<p>Kenansville sits inside the South Florida Water Management District's Kissimmee Basin, the same broad district that drains the chain of lakes running south from Kissimmee toward the Kissimmee River and, eventually, Lake Okeechobee ({ext(SFWMD_KISS[1], 'SFWMD’s Kissimmee River overview')}). Lake Marian runs right up to the edge of town, and Lake Kissimmee and Lake Jackson sit a short drive away inside the {ext(FWC_3LAKES[1], 'nearly 64,000-acre Three Lakes Wildlife Management Area')}, one of the largest remaining stretches of dry prairie in Florida. Any turf near that shoreline still keeps the state's 10-foot waterbody setback, seawall or nothing. The ground underneath is flatwoods and prairie country: the Felda series common to this part of the county is a poorly to very poorly drained soil that {ext(FELDA_OSD[1], 'USDA’s official series description')} puts within a foot of the surface for two to six months of the year, a higher water table than the sand under most Kissimmee-area lots.</p>"),
        sec("A cattle-town history, and no Census count of its own",
            f"<p>Kenansville grew up around the Okeechobee spur of the Florida East Coast Railway and took its name in 1914, honoring Mary Lily Kenan, Henry Flagler's third wife. The building known today as the Heartbreak Hotel opened in 1915 as the Piney Woods Inn and was renamed in 1955 ({ext(FL_MEMORY[1], 'Florida Memory’s photographic record of the building')}); the railroad closed in the 1950s and the Turnpike later routed traffic away from US-441 altogether, leaving a small, working ranching community rather than a town that grew into a city. The U.S. Census Bureau has never designated Kenansville its own place, so unlike Mount Dora or St. Cloud it carries no separate population count of its own; the closest anyone searching “best artificial turf installer near me” gets out here is confirming a Kissimmee-based crew still makes the drive, and we do.</p>"),
        "<!--AUTO:city-services-->",
    ]),
    faqs=[
        faq("Do you actually take jobs as far out as Kenansville?",
            f"Yes, though not often. At about {MI} miles from Kissimmee, it sits near the outer edge of our range, and a job here typically gets grouped with other far-south Osceola County stops rather than scheduled on its own, so plan on a little more lead time than a job closer to town."),
        faq("Does the state's turf standard even apply on a big ranch lot?",
            "Only up to one acre. Rule 62-308.100 covers a single-family residential lot of one acre or less; a larger parcel, common out here, falls outside it entirely, and Osceola County's own code, which does not mention synthetic turf either way, is what applies instead."),
        faq("How does a well-and-septic property change a turf job?",
            "Mainly around the septic tank. The state standard requires keeping the pump-out lid reachable once turf is down, which we plan around on nearly every Kenansville job. A private well changes little else, since the rule against watering turf with an in-ground system applies whether the water comes from a well or a utility."),
        faq("Is there an HOA or CDD in Kenansville that reviews turf?",
            "We found no recorded homeowners association or community development district covering this part of the county. Osceola County's Building Department is the only office that reviews a permit here, and there is no architectural committee to submit a design to."),
        faq("Why doesn't your site list a population number for Kenansville?",
            "Because there is not an official one. The Census Bureau counts population for designated places, and Kenansville has never been one; the Bureau's figures for this address only go as granular as Osceola County as a whole."),
    ],
    sources=SRC, city=SLUG, crumbs=[("Service areas", "/areas/")], crumb="Kenansville",
    related=[("/areas/osceola-county/", "Artificial turf in Osceola County"), ("/laws/permits/osceola-county/", "Osceola County permit rules for turf"),
             ("/areas/st-cloud/", "Artificial turf in St. Cloud"), ("/areas/harmony/", "Artificial turf in Harmony"),
             ("/artificial-turf-cost/", "Turf cost tables for Central Florida")],
)


# ============================================================== local, per service
LOCAL = {
    "residential": {
        "title": "Artificial Grass Installation in Kenansville, FL",
        "meta": "Artificial grass for Kenansville ranch properties: acreage, wells and septic, high water table, and 2026 Central Florida pricing.",
        "h1": "Artificial grass for a Kenansville ranch lot",
        "lede": capsule(f"Installed artificial grass around Kenansville prices the same as anywhere else we work, {price('residential')} a square foot as of September 2026. What is different is the lot: acreage instead of a platted subdivision, a well and a septic tank instead of city utilities, and a water table that sits closer to the surface than it does on higher Kissimmee-area ground."),
        "sections": [
            ("When the state's one-acre rule does not reach the property",
             f"<p>Florida's synthetic-turf standard only preempts local rules on a single-family lot of one acre or less. A working cattle property out here routinely runs well past that, which means the state's floor, no local ban, a capped permeability number, a guaranteed 10-foot waterbody setback, simply does not extend to the yard around the house the way it would on a smaller platted lot. In practice that changes less than it sounds like, since {a('/laws/permits/osceola-county/', 'Osceola County’s own Land Development Code')} does not mention synthetic turf either way, acreage or not. It is still worth knowing before assuming a rule from a Kissimmee job carries over automatically to a Kenansville ranch.</p>"),
            ("Building around a well and a septic system",
             f"<p>Almost every home out here supplies its own water and treats its own wastewater, which is close to the exception on a Toho-served Kissimmee lot. The state standard's requirement to keep a septic tank's pump-out lid reachable is not a rare footnote here; it is a step we plan on nearly every job, mapping the drainfield and lid location before any rock goes down. A private well changes less than people expect about the turf itself: the rule against using an in-ground irrigation system on synthetic turf applies the same way whether the water comes from a well pump or a municipal main, so heads still get capped either way.</p>"),
            ("A higher water table than the sand up in town",
             f"<p>{ext(FELDA_OSD[1], 'The Felda series')} common to this stretch of flatwoods and prairie country is poorly to very poorly drained, with a water table that can sit within a foot of the surface for two to six months most years, wetter than the sand under a typical Kissimmee subdivision lot. That pushes us toward the fuller end of the state's two-to-four-inch washed-rock range rather than the shallow end, since a base built at the minimum depth barely clears ground that is already holding water for a good part of the summer. Compared with the citrus-ridge sand under a {city('harmony')} or Lake County lot, which drains almost too well, a Kenansville yard is the opposite problem to solve.</p>"),
        ],
        "scenario": ("Pricing a yard behind a ranch house near US-441",
                     f"<p>Say you have a 900 sq ft yard behind a single-story ranch house a few miles off US-441, on a five-acre parcel with a well and a septic drainfield mapped along the east side. At {price('residential')} a square foot, that lawn prices between $7,200 and $16,200 installed, the same range as a quarter-acre Kissimmee lot, since the five acres around the house do not change the per-foot rate for the turfed area itself. What it does change is the checklist: confirming the drainfield and pump-out lid location before staking anything, and budgeting the fuller base depth this soil generally calls for, both settled before a shovel goes in the ground.</p>"),
        "faqs": [
            faq("Does having five or ten acres make my Kenansville quote higher?",
                "No. The per-square-foot rate only applies to the area actually being turfed, typically a yard around the house, not the acreage around it. A five-acre lot with a 900 sq ft lawn prices the same as a smaller lot with the same 900 sq ft lawn."),
            faq("Do I need a permit for a lawn conversion on unincorporated land out here?",
                "Osceola County's Building Department reviews it the same way it would inside Kissimmee's growth area, since Kenansville has no city government of its own. The county's code does not mention synthetic turf specifically, so ordinary landscape and drainage permitting rules are what apply."),
        ],
        "sources": SRC,
    },
    "pet": {
        "title": "Pet Turf & Dog Runs Near Kenansville, FL",
        "meta": "Pet turf for Kenansville ranch dogs: a contained yard near the house, septic-lid planning, and 2026 Central Florida pricing.",
        "h1": "Pet turf for a Kenansville ranch dog",
        "lede": capsule(f"Pet turf near Kenansville runs {price('pet')} a square foot as of September 2026, the same as anywhere else in our area. A ranch dog usually has the run of the property already; what a turf yard adds is one contained, mud-free, easy-to-rinse area close to the house instead of a whole acreage to keep clean.</p>".replace("</p>", "")),
        "sections": [
            ("A contained yard for a dog that otherwise roams",
             "<p>Most dogs on a working property out here are not confined to a small fenced run the way a subdivision dog is; they have the yard, the barn, sometimes the whole fence line. A turf area near Kenansville usually is not about replacing that freedom, it is about giving one dog, or a pair, a mud-free spot close to the back door for the muddiest months, or a place that is easy to hose down after a day spent everywhere else on the property. That changes the design conversation: the run's size and shape follow where the house's shade and doors are, not property lines the way it might on a tighter suburban lot.</p>"),
            ("More room to route around the septic drainfield",
             f"<p>Planning a dog run's fence line around a septic drainfield and pump-out lid is a step on nearly every rural Osceola County job, but a multi-acre Kenansville property usually gives us more options for where the run can sit relative to that infrastructure than a quarter-acre lot ever would. Instead of squeezing a run's footprint into whatever space is left after the drainfield, house and driveway are accounted for, there is often room to simply place the run somewhere else entirely and leave a wide, unambiguous buffer around the septic system, which is the simpler way to satisfy the state's pump-out-access requirement.</p>"),
            ("Fencing a run near the Three Lakes boundary",
             f"<p>Properties toward the edge of town, closer to the Three Lakes Wildlife Management Area, back up to conservation land rather than another homeowner's fence. A dog run's perimeter fencing matters more here for keeping a pet contained near that boundary than it does on a lot backing onto a neighbor's yard, since there is no second fence on the other side doing any of that work. That is a fencing and layout conversation more than a turf one, but it shapes where a run's gate and boundary end up before base material ever gets ordered.</p>"),
        ],
        "scenario": ("Sizing a run behind a house off Canoe Creek Road",
                     f"<p>Say you have a 300 sq ft area behind a ranch house off Canoe Creek Road, fenced for two dogs that otherwise have the run of a fenced pasture. At {price('pet')} a square foot, that run prices between $3,000 and $5,400 installed, covering the deeper base, fully permeable backing and odor-control infill a pet system needs. With acreage to work with, the fence line usually gets planned to leave a wide, unambiguous gap around the septic drainfield rather than squeezing the run's footprint against it the way a smaller in-town lot might have to.</p>"),
        "faqs": [
            faq("What's the best pet turf installer near me going to ask about, on a Kenansville ranch, that a subdivision quote would not?",
                "Where the septic drainfield and pump-out lid sit relative to the run, and whether the water comes from a private well. Both come up on nearly every rural Osceola County job and rarely on a Toho-served Kissimmee lot, so an installer who asks about them unprompted has done this kind of job before."),
            faq("Do ranch dogs even need a turf run if they already roam the property?",
                "Plenty of owners still want one contained area near the house that stays mud-free and rinses clean in a couple of minutes, even for a dog that otherwise has the run of a pasture. It is a convenience yard next to the house, not a replacement for the rest of the property."),
        ],
        "sources": SRC,
    },
    "putting": {
        "title": "Backyard Putting Greens in Kenansville, FL",
        "meta": "Backyard putting greens for Kenansville ranch and lake properties, an occasional job out here, priced at 2026 Central Florida rates.",
        "h1": "A putting green on a Kenansville ranch lot",
        "lede": capsule(f"A backyard putting green near Kenansville runs {price('putting')} a square foot as of September 2026, the published Central Florida range. It is a rarer request out here than a lawn or a dog run, but the acreage common to this part of the county gives a green more open ground to work with than most in-town lots do."),
        "sections": [
            ("An unusual request, priced the same as anywhere else",
             f"<p>We get far fewer putting-green calls out toward Kenansville than we do closer to Kissimmee, simply because full-time ranch and rural households ask for one less often than a subdivision homeowner does. When the request does come in, the price and the build are identical to a green in town: the same {price('putting')} a square foot, the same hand-shaped base and cup-setting process. What is different is scheduling, since a job this far out usually rides along with another rural Osceola County stop rather than a standalone visit.</p>"),
            ("A green near a Lake Marian fish camp",
             f"<p>A handful of properties near town sit along Lake Marian or a connecting canal, more oriented around a dock and a boat than a manicured lawn. A green on one of these lots still keeps the state's 10-foot waterbody setback, the same as any turf near the water, and the flatter ground right along the shoreline sometimes makes for an easier build than a lot with more grade change, so long as the buildable area is confirmed against the actual shoreline first.</p>"),
            ("Excavating a green above a shallow water table",
             f"<p>The flatwoods and prairie soil under most Kenansville-area lots holds water closer to the surface than the sand under a Lake County ridge lot does, which matters more on a green than on a flat lawn since a green's shaped base runs four to six inches deep instead of two to four. Building the lowest tier with extra drainage capacity, rather than assuming the surrounding ground will simply carry water away on its own the way faster-draining ridge sand would, keeps a shaped green from holding water in its low corner after a summer storm.</p>"),
        ],
        "scenario": ("A small green behind a lake-adjacent home",
                     f"<p>Say you have a 500 sq ft area behind a home near Lake Marian, set back well past the state's 10-foot line, and want a single-tier green with a fringe collar rather than anything elaborate. At {price('putting')} a square foot, that project prices between $7,000 and $15,000 installed. Because the surrounding soil holds water longer than ridge sand does, part of that price covers building the low tier's drainage capacity a touch deeper than the same design would need on higher, faster-draining ground.</p>"),
        "faqs": [
            faq("Is it worth installing a putting green this far from Kissimmee?",
                "It is workable, though we see far fewer requests for one out here than for a lawn or a dog run. Pricing and the build are identical to a green closer to town; the main difference is that a Kenansville job typically gets scheduled alongside another rural stop rather than on its own."),
            faq("Does a lakefront lot near Lake Marian limit where a green can go?",
                "Yes, the same way it would on any Florida lake. The state's 10-foot setback from the water's edge applies unless a seawall already separates the yard from the lake, so the buildable area for a green starts at that line, not at the property boundary."),
        ],
        "sources": SRC,
    },
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
