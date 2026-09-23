# -*- coding: utf-8 -*-
"""Mount Dora (tier 3, Lake County). Hub + residential/pet/putting only, per docs/TIER2-BRIEF.md.
Researched September 2026: city building department, city irrigation ordinance, Lake County
Property Appraiser, USDA official series descriptions (Apopka, Tavares, Candler), Mount Dora
Area Chamber of Commerce history, city National Register and arbor-permit pages, Census 2020,
and a 55+ community directory listing for Lakes of Mount Dora. No published HOA/ARC document
naming synthetic turf was found for any Mount Dora community, so none is quoted."""
from _helpers import page, capsule, sec, table, faq, note, a, svc, city, post, src, ext, price
from _cityservice import cityservice_pages
from _data import CITIES

SLUG = "mount-dora"
MI = CITIES[SLUG]["miles"]

MD_BUILD = ("City of Mount Dora — Online Permitting (Building Department)", "https://www.mountdora.gov/1246/Online-Permitting")
MD_WATER = ("City of Mount Dora — Irrigation, Variances & Exclusions", "https://www.mountdora.gov/511/Irrigation-Variances-Exclusions")
MD_NRHP = ("City of Mount Dora — National Register of Historic Places", "https://www.mountdora.gov/447/National-Register-of-Historic-Places")
MD_CHAMBER = ("Mount Dora Area Chamber of Commerce — city history", "https://www.mountdora.com/mount-dora-history/")
MD_TREE = ("City of Mount Dora — Arbor Permits and Landscaping", "https://mountdora.gov/1539/Arbor-Permits-and-Landscaping")
LAKE_PA = ("Lake County Property Appraiser — parcel search", "https://www.lakecopropappr.com/")
APOPKA_OSD = ("USDA NRCS — official series description, Apopka series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/A/APOPKA.html")
TAVARES_OSD = ("USDA NRCS — official series description, Tavares series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/T/TAVARES.html")
CANDLER_OSD = ("USDA NRCS — official series description, Candler series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/C/CANDLER.html")
LOMD = ("55places — Lakes of Mount Dora, a 55+ community", "https://www.55places.com/florida/communities/lakes-of-mount-dora")

SRC = ["dep-rule", "fs125572", "fs7203045", "census-acs", "usda-wss",
       MD_BUILD, MD_WATER, MD_NRHP, MD_CHAMBER, MD_TREE, LAKE_PA, APOPKA_OSD, TAVARES_OSD, CANDLER_OSD, LOMD]


# ============================================================== hub
HUB = page(
    f"/areas/{SLUG}/", "city",
    "Artificial Turf in Mount Dora, FL: Hills, Lakes, Permits",
    "Synthetic turf installers covering Mount Dora, FL: hillside grading, Lake Dora and Lake Gertrude setbacks, the city permit office and 2026 pricing.",
    "Artificial turf installers for Mount Dora's hills and lakefronts",
    capsule(f"Mount Dora's hillside lots and two in-town lakes make it a different kind of job than the flat subdivisions we usually turf, though we price it the same as anywhere in Central Florida, {price('residential')} a square foot, current for September 2026. At about {MI} miles north of Kissimmee, a Mount Dora install typically rides along with other Lake County stops rather than a trip on its own."),
    "".join([
        sec("Turf on a hill, not a flat lot",
            f"<p>Nearly every yard we quote sits on flat, sandy ground. Mount Dora breaks that pattern: the historic core rises on real elevation above Lake Dora, brick streets and century-old homes built into a slope no Kissimmee or St. Cloud subdivision presents us with, where a base that gets screeded level everywhere else sometimes needs a terraced step or a heavier anchor edge instead. Mature live oaks line most of the older streets, so staying outside a canopy's drip line, or getting a certified arborist's letter first, often decides where turf can go before grading starts. Lots backing onto Lake Dora or Lake Gertrude bring the state's 10-foot waterbody setback into the mix too, a buffer that only lifts once a seawall already stands between lawn and lake.</p>"),
        table("Mount Dora yard types and what we do differently",
              ["Lot type", "Where it sits in town", "What we adjust for it"],
              [["Historic hillside lots", "The brick-street core around downtown and Lake Dora", "A terraced or stepped base instead of one flat screed; oak drip lines to route around first"],
               ["Lake Dora and Lake Gertrude lakefront", "Lots backing directly onto either lake", "A 10-ft setback from the shoreline, gone only where a seawall already stands in the way"],
               ["Newer east-side subdivisions", f"Growth along the Wekiva Parkway corridor toward {city('apopka')}", "Flatter, younger lots closer to a typical Kissimmee-area build"],
               ["Lakes of Mount Dora and other 55+ sections", "Gated communities built around interconnected lakes off Highway 44", "Smaller lawns, an ARC submittal, and a review process with no published turf rule we could find"],
               ["Rural ridge edges", "Where city limits give way to Lake County's citrus ridge", "Fast-draining Candler or Tavares sand that still needs a properly compacted base"]],
              f"Every row still prices at {price('residential')} a square foot; access and paperwork change, not the rate."),
        sec("Permits, HOA review and checking a parcel",
            f"<p>Mount Dora runs its own Building Department at 308 E. 5th Avenue, phone 352-735-7115, filing through the city's {ext(MD_BUILD[1], 'BS&A Online permitting portal')}. We have not written a page for the city's own municipal code the way we have for the five counties in our service area, so we say that plainly rather than link somewhere that does not exist: call the Building Department with a code-specific question. A few edge parcels sit in unincorporated Lake County instead, where {a('/laws/permits/lake-county/', 'our Lake County permit page')} applies; the {ext(LAKE_PA[1], 'county Property Appraiser’s parcel search')} shows which side of the line an address falls on. {a('/laws/florida-hb-683/', 'The state’s May 2026 turf standard')} sets the same floor here as anywhere in Lake County, and an association review under {a('/laws/hoa-rules/', 'Florida’s HOA visibility statute')} is a separate step from the city's permit.</p>"),
        sec("Water and irrigation days",
            f"<p>Mount Dora runs its own Public Works & Water Utilities department rather than buying through a county authority, on a St. Johns River Water Management District schedule: one day a week from the first Sunday in November to the second Sunday in March, two days the rest of the year, odd addresses Wednesday and Saturday, even addresses Thursday and Sunday, none of it between 10 a.m. and 4 p.m. ({ext(MD_WATER[1], 'the city’s irrigation page')}). A capped synthetic lawn stops needing any of those days, since the state standard already forbids an in-ground system on turf regardless of the utility.</p>"),
        sec("A hill town with a real history",
            f"<p>Mount Dora traces to an 1880s settlement renamed for early resident Dora Ann Drawdy and incorporated in 1910, growing into a downtown the Chamber of Commerce still calls “the New England of the South” for its hilly streets and Colonial-style storefronts ({ext(MD_CHAMBER[1], 'the Chamber’s history page')}). Its 35-foot lighthouse at Gilbert Park, dedicated in 1988, is one of only three freshwater lighthouses in Florida, and the downtown core made the National Register of Historic Places in 2009 ({ext(MD_NRHP[1], 'the city’s National Register page')}). The city keeps an approved canopy-tree list and a removal permit for a protected tree ({ext(MD_TREE[1], 'the city’s arbor permit page')}). The 2020 Census counted 16,341 residents ({src('census-acs', 'U.S. Census Bureau')}).</p>"),
        sec("Growth on the east side, and an honest word on distance",
            f"<p>The Wekiva Parkway extension opened Mount Dora's east side to growth the hillside core never had room for; Lakes of Mount Dora, a gated 55+ community built around connected lakes off Highway 44, is the clearest example, roughly 950 homesites with a review committee for anything visible from the street ({ext(LOMD[1], 'a 55+ community directory listing')}). We found no published design-review document naming synthetic turf, so we describe the process, a sample and a site plan, rather than a rule. A homeowner searching “best artificial turf installer near me in Mount Dora” is usually asking whether a Kissimmee crew reaches this far north at all; the honest answer is yes, on a schedule shared with other Lake County stops.</p>"),
        "<!--AUTO:city-services-->",
    ]),
    faqs=[
        faq("Is Mount Dora too far out for a Kissimmee-based turf crew?",
            f"It sits close to the edge of our range, about {MI} miles from Kissimmee by straight line. We still take the jobs; they get grouped with other Lake County stops rather than scheduled on their own, so lead time can run a little longer than for a job closer to home."),
        faq("Does the 10-foot waterbody setback change on Lake Dora or Lake Gertrude?",
            "No. One number applies statewide: turf stops 10 feet short of a lake, pond or canal's normal water line, and that distance closes to nothing only once a bulkhead or seawall takes over the job of separating land from water. Neither Lake Dora nor Lake Gertrude carries a published local rule pushing that number higher, checked September 2026."),
        faq("Do I need an arborist before turfing near one of Mount Dora's oaks?",
            "Only if the planned turf falls inside a live oak's drip line, which is common on the hillside streets. The state rule bars turf there unless a certified arborist certifies the install will not harm the tree; the city's own arbor permit applies separately to removing a protected tree."),
        faq("Who do I actually call about a permit in Mount Dora?",
            "The city's Building Department at 352-735-7115, filed through its BS&A Online portal. If a parcel search shows the address as unincorporated Lake County instead, our Lake County permit page has the office to call."),
    ],
    sources=SRC, city=SLUG, crumbs=[("Service areas", "/areas/")], crumb="Mount Dora",
    related=[("/areas/lake-county/", "Artificial turf in Lake County"), ("/laws/permits/lake-county/", "Lake County permit rules for turf"),
             ("/areas/clermont/", "Artificial turf in Clermont"), ("/areas/montverde/", "Artificial turf in Montverde"),
             ("/artificial-turf-cost/", "Turf cost tables for Central Florida")],
)


# ============================================================== local, per service
LOCAL = {
    "residential": {
        "title": "Artificial Grass Installation in Mount Dora, FL",
        "meta": "Artificial grass installed on Mount Dora's hillside and lakefront lots: grading, setbacks and the 2026 Central Florida price range.",
        "h1": "Artificial grass for Mount Dora's hills and lakefronts",
        "lede": capsule(f"The ground changes more than the price does. A Mount Dora lawn still prices at {price('residential')} a square foot, tracked this September, but real hillside grade through the historic core and two in-town lakes bring the state's waterbody setback into play far more often than on a flat inland lot."),
        "sections": [
            ("Grading a hillside yard in the historic core",
             f"<p>A lot near downtown Mount Dora can drop several feet from the back porch to the rear fence line, which is not something a crew working mostly flat Osceola County ground deals with every day. Rather than screeding one flat plane, we shape the compacted rock base in a step or a gentle terrace, so the finished lawn reads level in sections instead of tilted end to end. {post('artificial-turf-on-a-slope', 'A slope changes the layout more than the material')}, and a yard on Mount Dora's hillside is a good example of why: the anchor edge at the low end of a run carries more of the job than it would on a flat lot, since that is where a poorly secured perimeter would show movement first. Candler and Tavares sand, the {ext(CANDLER_OSD[1], 'excessively drained ridge series')} common on this side of Lake County, drains quickly on its own, which helps once the grade is right but does nothing to fix a base that was never properly stepped.</p>"),
            ("Working around Mount Dora's oak canopy",
             f"<p>Streets in the older part of town carry oak canopy old enough to shade both sides at once, and a live oak's root system reaches well past where its branches end. The state standard keeps synthetic turf outside that drip line, on the property it grows on or a neighboring one, unless a certified arborist signs off that the work will not harm the tree. On a historic-core lot that can mean less usable lawn than the fence line suggests, since a canopy from a neighbor's yard often reaches across the property line too. {post('artificial-turf-near-live-oaks-and-palms', 'Marking where a canopy actually ends')}, not just where the trunk sits, is the first step on a job like this, well before anyone talks about turf color or infill.</p>"),
            ("Flatter ground on the east side, near the Wekiva Parkway",
             f"<p>Growth along the Wekiva Parkway corridor has filled in Mount Dora's east side with subdivisions built on ground closer to what we see every day near {city('minneola')} or {city('clermont')}: modest grade, younger sod, and a builder's compacted fill instead of a century of undisturbed hillside soil. That fill drains worse than it looks, since construction traffic packs it tighter than the native sand underneath ever was on its own, so we still build up with washed, open-graded rock rather than assuming a newer lot needs less base than an older one. The upside on this side of town is a straightforward, mostly flat layout, closer to a standard Kissimmee-area job than anything the hillside core requires.</p>"),
        ],
        "scenario": ("What a hillside Mount Dora yard actually costs",
                     f"<p>Say you have a 1,050 sq ft backyard behind a 1920s bungalow a few blocks off the downtown hill, with close to three feet of fall from the patio to the back fence. At {price('residential')} a square foot, that lawn prices between $8,400 and $18,900 before anyone talks about the slope specifically, since the rate does not change for a hillside lot. What does move within that range is labor: stepping the base down the grade instead of screeding one flat plane, and building a heavier anchor edge at the low end, both take more crew time than the same square footage on a level Osceola County yard, which is usually what pushes a job like this toward the upper half of the published range rather than past it.</p>"),
        "faqs": [
            faq("Does a sloped lot cost more than a flat one in Mount Dora?",
                "The published rate does not change for slope. What changes is where a job lands inside that rate: extra time to step the base and anchor the low edge properly usually pushes a hillside lawn toward the upper half of the range rather than adding a separate line item."),
            faq("Can I turf all the way to my property line if my neighbor's oak hangs over it?",
                "Not if the canopy's drip line reaches your side of the fence. The setback follows the tree's roots, not the property boundary, so a neighbor's oak can limit your yard the same way one of your own would, unless an arborist certifies the work as safe."),
        ],
        "sources": SRC,
    },
    "pet": {
        "title": "Pet Turf & Dog Runs in Mount Dora, FL",
        "meta": "Pet turf and dog runs built for Mount Dora's narrow hillside lots and 55+ communities, with 2026 Central Florida pricing.",
        "h1": "Pet turf for Mount Dora's tighter, older yards",
        "lede": capsule(f"Older homes near downtown Mount Dora tend to sit on narrower lots than a newer Kissimmee-area subdivision, which changes where a dog run's drain point can go more than it changes the price: pet turf here still runs {price('pet')} a square foot, the same figure we quote everywhere, current this September."),
        "sections": [
            ("Dog runs on a narrow historic-core lot",
             "<p>Homes built into Mount Dora's hillside in the early 1900s often sit on lots narrower than anything platted in the last thirty years, which leaves a dog run competing for space with a driveway, a fence line and whatever grade the house itself sits on. Fitting a run into that footprint usually means picking the flattest available strip first and working the drainage direction around it, rather than starting from an ideal rectangle the way a wide-open Osceola County backyard allows. A narrow run still needs the same fully permeable backing and deeper base a wider one would, just fit into less room. A run squeezed against a shared driveway or a neighbor's fence line also needs its gate placed where a trash can or a parked car will not block daily access, a detail that matters less on a wider suburban lot with room to spare.</p>"),
            ("Pet yards inside a 55+ section",
             f"<p>Lakes of Mount Dora and similar 55+ sections on the city's east side tend to have smaller, tidier lots than the historic core, with a single companion dog more common than a multi-dog household. A fenced pet run here usually sits closer to the patio than a run on a larger family lot would, and a design-review submittal, sample and site plan included, is part of the process the same way it would be for a lawn. We have not found a published rule from any Mount Dora 55+ association addressing turf specifically, so we treat the review as a step to plan for rather than a fixed standard to quote.</p>"),
            ("Grading a run on a slope instead of flat ground",
             f"<p>A dog run on one of Mount Dora's graded lots still needs its drain point chosen deliberately, but a hillside adds a second consideration a flat {city('montverde')} or Osceola County yard does not: which direction the natural slope already wants water to go. Fighting that slope with a drain point aimed uphill costs more base work than routing the run's grade to match the land's own fall, so the layout conversation on a hillside property usually starts with where the ground already drains before anything about fencing or infill comes up. On a lot that drops toward the street rather than the backyard, that can mean routing the run's low corner toward the front instead of the rear, which changes where a fence gate and a rinse hose bib make the most sense before anything about turf color comes up.</p>"),
        ],
        "scenario": ("Sizing a dog run on a Lake Gertrude-area lot",
                     f"<p>Say you have a 380 sq ft side yard behind a home near Lake Gertrude, fenced off for one mid-sized dog that already has a worn path along the property line. At {price('pet')} a square foot, a run that size prices between $3,800 and $6,840 installed, covering the deeper three- to four-inch base, the fully permeable backing and zeolite or coated-sand infill a pet system needs over a plain lawn build. On a lot with any real grade, plan on the drain point sitting at whichever corner the land already slopes toward rather than the corner that happens to be closest to a hose bib.</p>"),
        "faqs": [
            faq("Is a dog run harder to fit on an older Mount Dora lot?",
                "Often the limiting factor is width, not the build itself. A narrow historic-core side yard still gets the same permeable backing and deeper base as a wider one; there is just less flexibility in where the fenced footprint can go."),
            faq("Do 55+ communities in Mount Dora allow pet turf?",
                "We have not found a published rule against it from any Mount Dora 55+ association, and none naming turf specifically either. Expect the same design-review submittal, a sample and a site plan, that any Florida association typically asks for."),
        ],
        "sources": SRC,
    },
    "putting": {
        "title": "Backyard Putting Greens in Mount Dora, FL",
        "meta": "Putting greens shaped for Mount Dora's hillside and lakefront lots, with 55+ community options and 2026 Central Florida pricing.",
        "h1": "Putting greens built for Mount Dora's real elevation",
        "lede": capsule(f"Few towns in our area hand us actual elevation to design around, and Mount Dora's hillside lots are the exception worth planning for. A backyard green here still costs {price('putting')} a square foot, the figure we quote across Central Florida, checked this September, whatever the view looks like from the tee."),
        "sections": [
            ("Using a hillside lot's own elevation",
             "<p>Most putting greens we build start from flat ground and get their breaks shaped entirely into the base. A hillside lot near downtown Mount Dora sometimes hands us a head start: real existing grade that a design can lean into rather than fight, so long as the base underneath is still built to hold that shape through a rainy season rather than sliding back toward flat. The trade-off is drainage planning, since a green tucked into a natural slope needs its lowest tier engineered to move water through just as fast as one built on level ground, or the same storm that looks scenic from the porch leaves a puddle exactly where the cup sits.</p>"),
            ("Lakefront estate lots on Lake Dora and Lake Gertrude",
             f"<p>Larger, older lots backing onto Lake Dora or Lake Gertrude tend to have more open backyard than a historic-core property squeezed onto a narrow street, which is where a full-size green with a fringe and a couple of tiers actually fits. A green still has to stay 10 feet clear of the shoreline the way any turf does, a line that disappears only where a seawall already runs between yard and lake, worth confirming against the actual water's edge before a design gets drawn up rather than after. These older lakefront parcels often carry mature oak canopy of their own, planted decades before anyone thought about a putting surface, so the same drip-line check that applies to a lawn applies here too, sometimes limiting a green to a smaller footprint than the open yard first suggests.</p>"),
            ("A smaller green as a 55+ amenity",
             f"<p>Lakes of Mount Dora and comparable 55+ sections on the east side tend to favor a compact green over a full-size one, often as a low-maintenance stand-in for the trips a homeowner used to make to a course. A design-review submittal applies here the same way it does for a lawn or a pet run, sample and site plan included, and we have not found a published association rule addressing synthetic turf specifically to quote either way. Compared with {city('longwood')} or another flatter Seminole County lot, the main difference on a Mount Dora 55+ lot is usually less square footage to design around, not a different build, since the same base, fiber and cup-setting process applies whatever the lot size.</p>"),
        ],
        "scenario": ("What a lakefront green costs near Lake Dora",
                     f"<p>Say you have a 600 sq ft area behind a lakefront home on Lake Dora, set back well past the required 10 feet from the water, and you want a two-tier green with a fringe collar. At {price('putting')} a square foot, that project prices between $8,400 and $18,000 installed, with the final number driven more by how many tiers and cups the design calls for than by the lake view next to it. A simple single-level green at that size lands toward the lower part of the range; add a second tier and hand-set cups, and the shaping labor alone can carry it past the middle.</p>"),
        "faqs": [
            faq("Does Mount Dora's hilly terrain make a putting green cheaper to build?",
                "Not usually cheaper, though an existing slope can mean less earth needs to move to create interesting breaks. The base still has to be shaped and compacted to hold that contour through a rainy season, which is the same labor-heavy step as building breaks from scratch on flat ground."),
            faq("How do you find the best putting green installer near you in Mount Dora?",
                "Ask whether the quote breaks out shaping labor, cup hardware and fiber type separately from a flat per-square-foot number, and whether the installer has already checked your lot's setback from Lake Dora or Lake Gertrude before pricing it. A quote that skips both usually has not planned the job in enough detail yet."),
        ],
        "sources": SRC,
    },
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
