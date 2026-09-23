# -*- coding: utf-8 -*-
"""Frostproof, Polk County (tier 3): the farthest town on our list, between Lake Clinch and Lake Reedy on
the Lake Wales Ridge, grouped with other Polk stops rather than booked on its own. Local sources checked
September 2026: the City of Frostproof's own Building Department and Public Works pages, the Southwest
Florida Water Management District's 2026 Modified Phase III order (shared fact with c_city_lake_wales.py),
the Florida Department of Agriculture and Consumer Services' Lake Wales Ridge State Forest page, Census
Reporter's Frostproof profile, a Lake Clinch mobile-home community's own site, and the USDA official series
description for Candler sand already used for the Polk County hub (reused here as a fact and URL)."""
from _data import CITIES
from _helpers import page, capsule, sec, table, faq, a, svc, city, post, src, ext, price
from _cityservice import cityservice_pages

SLUG = "frostproof"
MI = CITIES[SLUG]["miles"]

FP_BUILDING = ("City of Frostproof — Building Department", "https://cityoffrostproof.com/departments/building/")
FP_PUBWORKS = ("City of Frostproof — Public Works Department", "https://www.cityoffrostproof.com/departments/public-works/")
SWFWMD_P3 = ("Southwest Florida Water Management District — Modified Phase III order extended through Oct. 1, 2026", "https://www.swfwmd.state.fl.us/the-newsroom/2026/district-extends-modified-phase-iii-water-shortage")
FP_FOREST = ("Florida Department of Agriculture and Consumer Services — Lake Wales Ridge State Forest", "https://www.fdacs.gov/forest-wildfire/our-forests/state-forests/lake-wales-ridge-state-forest")
FP_CENSUS = ("Census Reporter — Frostproof, FL (Census Bureau data)", "https://censusreporter.org/profiles/16000US1224900-frostproof-fl/")
FP_MOBILE = ("Frostproof Mobile Village — community on Lake Clinch", "https://www.frostproofmobilevillage.com/")
FP_HISTORY = ("Wikipedia — History of Frostproof, Florida", "https://en.wikipedia.org/wiki/History_of_Frostproof,_Florida")
CANDLER = ("USDA NRCS — official series description, Candler series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/C/CANDLER.html")

SRC = [FP_BUILDING, FP_PUBWORKS, SWFWMD_P3, FP_FOREST, FP_CENSUS, FP_MOBILE, FP_HISTORY, CANDLER, "dep-rule"]

HUB = page(
    "/areas/frostproof/", "city",
    "Artificial Turf in Frostproof, FL (2026 Guide)",
    "Synthetic turf installation, permits and soil facts for Frostproof, FL, between Lake Clinch and Lake Reedy, from a Kissimmee-based crew. Checked Sept. 2026.",
    "Artificial grass installation for Frostproof yards",
    capsule(f"Frostproof, the farthest town on our list at about {MI} miles from downtown Kissimmee, still gets the identical synthetic lawns, pet turf and putting greens we build closer to home, at the {price('residential')} figure we checked this September. The city sits between two lakes on the Lake Wales Ridge and runs its own small building department. A visit here rides along with whatever else is already booked in Polk County that day."),
    "".join([
        sec("The farthest stop on a Kissimmee crew's map",
            f"<p>Frostproof sits about {MI} miles from downtown Kissimmee, the longest distance on our whole service list, in a small city squeezed onto Wall Street between Lake Clinch and Lake Reedy. Settlers first tried a fort here in 1850, and the town later took its current name after riding out the freeze of December 1894 better than most of the state's citrus belt, only to lose most of its own groves to the harder freeze that followed in 1895 ({ext(FP_HISTORY[1], 'the city’s documented history')}). None of that history moves the number on a quote: a Frostproof lawn prices exactly like a Kissimmee one, {price('residential')} a square foot. Ask five installers who all call themselves the best artificial turf company near Frostproof, and the honest tell is whether they've actually driven the {MI} miles out before, not just how confidently the ad reads.</p>"),
        sec("Citrus country, lake shores and a slow, steady population",
            f"<p>Frostproof's historic downtown runs east to west on Wall Street, wedged between the two lakes that give the city its shape, with citrus groves stretching from both shores since the first commercial planting here in 1886. Growth has stayed modest: 2,877 residents at the 2020 census, an estimate near 3,346 by 2024 ({ext(FP_CENSUS[1], 'Census Reporter’s profile')}). Manufactured-home and 55-plus communities line Lake Clinch's shore, including a resident-owned, adult-only co-op and a lakefront community with its own marina ({ext(FP_MOBILE[1], 'Frostproof Mobile Village')}), together a good share of the smaller, lower-maintenance yards a synthetic lawn suits well.</p>"),
        sec("Frostproof yard types and what we do differently",
            "<p>A Frostproof address usually falls into one of three patterns.</p>"
            + table("Frostproof yard types and what we do differently",
                    ["Where it sits", "What the lot looks like", "What changes for the crew"],
                    [["Between the two lakes on Wall Street", "Small, established, citrus or shade trees nearby", "Water buffer and tree canopy checked first"],
                     ["Bordering a grove outside downtown", "More acreage, straighter property lines", "Fewer access problems than a tight in-town lot brings"],
                     ["Inside a lakeside or 55-plus park", "Compact lot, low-maintenance expectations", "A quicker job, cleared with the park office more often than city hall"]],
                    "Price per square foot doesn't move between these three. Proximity to a lake, a grove line or a fence is what moves a Frostproof bid."),
        ),
        sec("Frostproof's own Building Department, not a contractor or the county",
            f"<p>Frostproof runs its own Building Department rather than contracting the work out or routing it to Polk County: Bob Lane, the city's Building Official, takes applications by email or fax and can be reached at 863-635-7854, with permit fees payable through an online link on the department's page ({ext(FP_BUILDING[1], 'City of Frostproof Building Department')}). Nothing published there addresses synthetic turf, so a lawn conversion gets treated as ordinary landscaping and irrigation work, with {a('/laws/florida-hb-683/', 'Florida’s 2026 turf standard')} filling the gap the city's own code leaves (see also {a('/laws/hoa-rules/', 'what a Florida HOA can restrict')}, if a property answers to one). For anyone just outside city limits, {a('/laws/permits/polk-county/', 'our Polk County permit page')} covers what the county told us, and a Frostproof stop typically shares a route toward {city('lake-wales', 'Lake Wales')} or {city('winter-haven', 'Winter Haven')} that day.</p>"),
        sec("Water rules that may be stricter than the city's own page",
            f"<p>The city's Public Works Department posts a twice-a-week irrigation schedule, odd addresses Wednesday and Saturday, even addresses Thursday and Sunday, both before 10 a.m. or after 4 p.m. ({ext(FP_PUBWORKS[1], 'City of Frostproof Public Works')}), the page most residents find first. It's also out of date: emergency footing from the district covering this part of Polk County has trimmed every customer inside its lines, Frostproof included, to a single day a week since early 2026, a cut running through October 1 ({ext(SWFWMD_P3[1], 'SWFWMD’s order')}). Watering on the printed schedule instead of the emergency one risks a citation, so a call to city hall settles which day applies. A capped synthetic lawn sidesteps the question, since {src('dep-rule', 'Florida’s turf rule')} already forbids an in-ground system on turf regardless of the day.</p>"),
        sec("Ridge sand, scrub habitat and the trees next door",
            f"<p>Frostproof sits on the same Candler ridge sand as the rest of the Lake Wales Ridge, excessively drained ground built from old wind-blown dune deposits ({ext(CANDLER[1], 'USDA’s official series description')}), and the {ext(FP_FOREST[1], 'Lake Wales Ridge State Forest')} just outside town protects some of the last scrub habitat this soil supported, home to scrub oaks, gopher tortoises and the Florida scrub-jay. That protected scrub matters for a yard here in one practical way: the drip-line rule keeps turf out from under a tree's canopy whether the tree sits on the property being turfed or the lot next door, so a yard backing onto a scrub-oak thicket needs the same arborist sign-off as one under a live oak downtown. The water side of that rule book applies to either shoreline: a Lake Clinch or Lake Reedy yard keeps turf clear of the first 10 feet of open water unless a seawall already stands at that line.</p>"),
        "<!--AUTO:city-services-->",
    ]),
    faqs=[
        faq("Does Frostproof have its own rule for synthetic turf?", "No. The city's Building Department reviews a lawn conversion as ordinary landscaping work and hasn't published anything turf-specific. Florida's statewide standard, in force since May 2026, is the only turf rule reaching a Frostproof property."),
        faq("How many days a week can I water in Frostproof right now?", "A single day, even though the city's own posted page still shows a twice-a-week pattern. The district's emergency order supersedes that page through October 1, 2026; check with city hall for the day that currently applies."),
        faq("Does the Lake Wales Ridge State Forest affect what I can install?", "Only indirectly, through the same drip-line rule that applies everywhere: turf can't go under a tree's canopy, including a neighbor's, without a certified arborist's sign-off, which matters more here given how much scrub oak grows nearby."),
        faq("Can turf go right up to Lake Clinch or Lake Reedy?", "Not usually. Both lakes fall under Florida's standard buffer, 10 feet of clearance from the shoreline, erased only where a seawall or bulkhead already forms the edge between lawn and lake."),
    ],
    sources=SRC, city=SLUG, crumbs=[("Service areas", "/areas/")], crumb="Frostproof",
    related=[("/areas/polk-county/", "Artificial turf across Polk County"), ("/laws/permits/polk-county/", "Polk County permit findings for turf"),
             ("/areas/lake-wales/", "Turf installers in Lake Wales"), ("/areas/bartow/", "Turf installers in Bartow"),
             ("/artificial-turf-cost/", "Full turf cost guide")],
)

LOCAL = {
    "residential": {
        "title": "Artificial Grass Installation in Frostproof, FL",
        "meta": "Installed artificial grass for a Frostproof yard between Lake Clinch and Lake Reedy runs $8–$18 a sq ft. Permits, soil and setbacks, checked Sept. 2026.",
        "h1": "A synthetic lawn for a citrus-country Frostproof lot",
        "lede": capsule(f"Installed {svc('residential', 'artificial grass')} for a Frostproof yard runs {price('residential')} per square foot, typically {price('residential', True)}, the same Central Florida range we checked in September 2026. Between Lake Clinch and Lake Reedy the ground is the same fast-draining ridge sand as the rest of the county, and the town's own Building Department, not a contracted firm, signs off on the work."),
        "sections": [
            ("A permit from the city's own small office",
             "<p>A residential lawn conversion in Frostproof goes through the city's own Building Department rather than a contracted review firm or Polk County directly, with Bob Lane, the Building Official, taking applications by email or fax rather than through an online system. Nothing in that office's published requirements addresses synthetic turf by name, so a straightforward sod-to-turf swap on an existing lawn typically moves through the same channel as a landscaping change, though a homeowner capping irrigation heads as part of the job should confirm with the department whether that specific step needs its own sign-off. Keeping the manufacturer's spec sheet on hand for the crew's chosen product is worth doing regardless, since it documents that the installation meets the state's own material standard if anyone ever asks.</p>"),
            ("Grove-adjacent ground versus a Wall Street lot",
             f"<p>A property just outside {city('frostproof', 'Frostproof')}'s small downtown tends to sit on more open ground than a lot right on Wall Street, often bordering what used to be, or still is, a citrus grove, which means fewer mature trees to route a base around and a straighter, simpler grade. A Wall Street lot, by contrast, sits close enough to both Lake Clinch and Lake Reedy that the required clearance from open water is worth checking before finalizing a layout, on top of whatever shade a citrus tree or an old oak throws over the yard. Either way, the same Candler ridge sand sits underneath, so the base recipe doesn't change, only how much of the lot the crew can actually use.</p>"),
            ("A smaller lawn in a lakeside 55-plus park",
             f"<p>Several manufactured-home and 55-plus communities line Lake Clinch's shore on the edge of town, and the lots inside them run smaller than a typical single-family yard, which actually suits a synthetic lawn well: less square footage to install, and no mowing for a resident who chose a low-maintenance park specifically to avoid yard work. Review inside these communities usually runs through the park's own office rather than a city process, so confirming what a specific park expects before ordering material saves a return trip. {post('artificial-turf-for-55-plus-communities', 'What changes in a 55-plus setting')} covers the broader pattern, which applies here as much as it does anywhere else on the ridge.</p>"),
        ],
        "scenario": ("Turfing a 900 sq ft yard near downtown Frostproof",
                     f"<p>Say you have a 900 sq ft yard on a Wall Street-area lot, roughly half in the shade of a mature oak and close enough to Lake Reedy that the setback needs checking before anything gets ordered. At {price('residential', True)} a square foot, the typical range, that yard prices between $9,000 and $14,400 once the shaded and sunny sections, the washed-rock base and the usual edging are all included. A same-size lot on more open ground near a grove, with no drip-line or setback to work around, would likely land closer to the bottom of that same range instead, since the layout itself is simpler to build.</p>"),
        "faqs": [
            faq("Does Frostproof require a permit for a sod-to-turf conversion?", "The city's Building Department reviews it as ordinary landscaping work, since nothing published addresses synthetic turf specifically. Call 863-635-7854 to confirm what a specific address needs before scheduling."),
            faq("How close to Lake Clinch or Lake Reedy can a Frostproof lawn go?", "Not within the first 10 feet of either shoreline, the same statewide line that applies to any Florida lake or canal lot, unless a seawall or bulkhead already marks that edge."),
            faq("Is a 55-plus park lawn in Frostproof cheaper to turf than a house?", "Usually only because it's smaller. The price per square foot is the same statewide range either way; a compact park lot simply needs less material and less labor to finish."),
        ],
        "sources": SRC,
    },
    "pet": {
        "title": "Pet Turf & Dog Runs in Frostproof, FL",
        "meta": "Pet turf for a Frostproof dog run, from a lakeside mobile-home park to a scrub-edge lot near the state forest, checked for this city in Sept. 2026.",
        "h1": "Dog-run turf for Frostproof's lake and scrub lots",
        "lede": capsule(f"{svc('pet', 'Pet turf')} for a Frostproof dog run costs {price('pet')} per square foot installed, typically {price('pet', True)}, whether the yard sits beside Lake Clinch or backs onto scrub ground near the state forest. September 2026's range hasn't moved for any Florida city; what changes here is how close a run sits to water, a grove line or a neighbor's tree canopy."),
        "sections": [
            ("A run in a lakeside mobile-home park",
             f"<p>Several of the manufactured-home and 55-plus communities along Lake Clinch, on {city('frostproof', 'Frostproof')}'s edge, welcome dogs, and a compact lot in one of these parks often means a dog run has to share space with a carport, a shed and a small patio rather than spreading across an open backyard. A run this size still needs the full three to four inches of washed rock a pet system calls for, not a scaled-down version, since liquid volume from daily use doesn't shrink just because the fenced area does. Checking the specific park's own pet and fencing rules before laying out the run avoids a conflict that has nothing to do with the turf itself.</p>"),
            ("Staying clear of a scrub-oak canopy",
             f"<p>Scrub oaks are shorter and scrappier than a live oak, but the state's drip-line rule treats them the same way: no turf under the canopy, on the property or a neighbor's, without a certified arborist's sign-off. A property backing onto scrub ground near the {ext(FP_FOREST[1], 'Lake Wales Ridge State Forest')} is more likely to have this kind of tree along a rear fence line than a yard closer to downtown, which matters for a dog run's layout specifically since a run's fixed fence posts are harder to shift later than an open lawn's edge would be. Planning the fence a few feet clear of any canopy from the start avoids relocating the whole run.</p>"),
            ("Grading a run away from a grove line",
             "<p>A dog run built next to an active or former citrus grove needs its drain point aimed away from the grove line rather than toward it, since the state's no-added-runoff rule applies to a neighbor's grove exactly as it would to a residential yard next door. That's usually a simple fix on Frostproof's open, grove-adjacent lots, where there's more room to route a grade than on a tight in-town lot, but it has to be planned before the fence goes up, not adjusted afterward once posts are already set in the ground.</p>"),
        ],
        "scenario": ("A 300 sq ft run for a Frostproof park home",
                     f"<p>Say you have a 300 sq ft fenced side yard behind a manufactured home in one of Frostproof's lakeside communities, currently patchy grass that never fully filled in under a carport's shade. At {price('pet', True)} a square foot, the typical pet turf range, that run prices between $3,600 and $4,800 once the deeper base, permeable backing and odor-control infill are figured in. A run twice that size for a multi-dog household on a grove-adjacent lot outside town would scale up proportionally, though the per-foot number wouldn't change just because the lot has more room to work with.</p>"),
        "faqs": [
            faq("Do Frostproof's lakeside parks allow dog runs on manufactured-home lots?", "Most do, though the park's own office sets the specific pet and fencing rules rather than the city. Check with park management before finalizing a run's layout."),
            faq("Does a Frostproof dog run need to stay clear of scrub oaks?", "Yes, the same drip-line rule that protects a live oak covers a scrub oak too, including one on a neighboring property, unless a certified arborist confirms the install won't cause harm."),
            faq("Can a dog run's drainage point face a neighbor's citrus grove?", "No. The state's rule against added runoff applies to a grove next door the same way it applies to a residential neighbor, so the run's grade has to be planned away from that line."),
        ],
        "sources": SRC,
    },
    "putting": {
        "title": "Backyard Putting Greens in Frostproof, FL",
        "meta": "Backyard putting greens for a Frostproof lot, from a grove-sized yard to a retirement-park patio, run $14–$30 a sq ft installed. Checked Sept. 2026.",
        "h1": "A putting green built for Frostproof's bigger lots",
        "lede": capsule(f"A Frostproof backyard {svc('putting', 'putting green')} costs {price('putting')} a square foot to build, typically {price('putting', True)}, matching the number a green would run anywhere in the territory this September. Acreage is the real variable here: a grove-sized lot outside downtown gives a design far more to work with than a tight Wall Street yard does, even though both sit on the same ridge sand."),
        "sections": [
            ("More room on a grove-sized lot",
             f"<p>Property outside {city('frostproof', 'Frostproof')} typically runs bigger than a standard subdivision parcel, a holdover from the town's farming layout, and that changes what a green's design can include more than almost anything else does. A multi-tier layout with more than one cup and a long approach off the fringe needs the kind of footprint only a grove-adjacent lot usually has; a compact Wall Street yard does better with a single, simpler tier sized to whatever space remains once the house and driveway are accounted for. The base recipe underneath doesn't change either way; only the scale of what gets built on top of it does.</p>"),
            ("Shaping breaks into loose ridge sand",
             "<p>Candler sand under a Frostproof yard is so loose and excessively drained that it barely resists a footstep, let alone the pressure of a plate compactor trying to lock a designed tier in place, and ground that shifts this easily wants to creep back toward flat the moment a crew stops watching it. A green shaped in a single pass on sand like this tends to lose its break within a season as the loose grains keep migrating under rain and foot traffic; one built in checked, compacted layers holds that same break for years instead. The turf and the cups look identical either way on installation day, which is exactly why asking how the base was built matters more than judging a green by its finish.</p>"),
            ("A green near the lake, set back from the water",
             "<p>A property backing onto Lake Clinch or Lake Reedy can still fit a putting green, just set back the required distance from the shoreline unless an existing seawall or bulkhead already marks that edge. That line matters more for a green than for open lawn, since a design built around specific cup placements and break angles is harder to shrink after the fact than a plain rectangle of turf would be. Staking the setback before finalizing the layout, not after, keeps a two-tier design from needing a last-minute redraw.</p>"),
        ],
        "scenario": ("A 500 sq ft green on a Frostproof grove lot",
                     f"<p>Say you have a 500 sq ft L-shaped area on a grove-adjacent Frostproof property, flat enough overall but with a gentle three-foot rise across the back third where old grove rows once ran. The typical range for a backyard green, {price('putting', True)} a square foot, puts the total between $9,000 and $12,500 once the hand-shaped base, putting surface, fringe and two cups are included. A smaller, single-tier green closer to downtown, sized to fit beside a Wall Street lot's house and driveway, would land nearer the bottom of that same range instead, simply because there's less shaping and less turf involved.</p>"),
        "faqs": [
            faq("Does a grove-adjacent Frostproof lot cost less to turf for a green?", "Not per square foot. The extra acreage just means room for a bigger design; the statewide price range per square foot stays the same whether the lot is a quarter acre downtown or several acres near a grove."),
            faq("How close to Lake Clinch can a putting green sit?", "Not within 10 feet of the water's edge, the same distance any Florida waterbody requires, unless a seawall or bulkhead already stands at that edge."),
            faq("Why does ridge sand make a green harder to build correctly?", "Because loose Candler sand shifts under a compactor more than denser soil does, so holding a designed break takes shaping the base in smaller, checked layers rather than one flat pass."),
        ],
        "sources": SRC,
    },
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
