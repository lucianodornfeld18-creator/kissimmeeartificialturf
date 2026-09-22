# -*- coding: utf-8 -*-
"""Tier 2 hub + six city x service pages for Polk City, FL (Polk County). Researched September 2026:
Polk County's own Building Division (Polk City has no building department of its own), the town's
"Gateway to the Green Swamp" page, the Green Swamp Area of Critical State Concern statute, the Polk
City Chain of Lakes, Fantasy of Flight, the Auburndale TECO Trail / Van Fleet State Trail connection,
Census/Florida Demographics population figures, the SWFWMD Modified Phase III extension, and the USDA
Myakka, Basinger and Candler series descriptions (Candler already used for the Polk County ridge in
c_counties.py)."""
from _data import CITIES
from _helpers import page, capsule, sec, table, faq, a, svc, city, post, ext, price
from _cityservice import cityservice_pages

SLUG = "polk-city"
C = CITIES[SLUG]

GATEWAY = ("Town of Polk City — Gateway to the Green Swamp", "https://www.mypolkcity.org/residents-visitors/page/gateway-green-swamp")
GREEN_SWAMP_LAW = ("Florida Statutes §380.0551 — Green Swamp Area, designation as area of critical state concern", "https://law.justia.com/codes/florida/title-xxviii/chapter-380/part-i/section-380-0551/")
POLK_BUILDING = ("Polk County Building Division — permitting", "https://www.polkfl.gov/services/building/permitting/")
POLK_PA = ("Polk County Property Appraiser — parcel search", "https://www.polkflpa.gov/")
DOH_SEPTIC = ("Florida Department of Health in Polk County — septic tanks (onsite sewage treatment and disposal)", "https://polk.floridahealth.gov/programs-and-services/environmental-public-health/septic-tanks-onsite-sewage-treatment-disposal-systems/")
CANDLER_OSD = ("USDA NRCS — official series description, Candler series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/C/CANDLER.html")
MYAKKA_OSD = ("USDA NRCS — official series description, Myakka series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/M/MYAKKA.html")
BASINGER_OSD = ("USDA NRCS — official series description, Basinger series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/B/BASINGER.html")
LAKE_AGNES = ("Polk County Water Atlas — Lake Agnes", "https://polk.wateratlas.usf.edu/waterbodies/lakes/160182/lake-agnes")
FANTASY_FLIGHT = ("Visit Central Florida — Fantasy of Flight, Polk County", "https://visitcentralflorida.org/featured/fantasy-of-flight/")
TECO_TRAIL = ("Florida Hikes — Auburndale TECO Trail", "https://floridahikes.com/teco-auburndale-trail/")
POP_POLK_CITY = ("Florida Demographics — Polk City population", "https://www.florida-demographics.com/polk-city-demographics")
SWFWMD_EXT = ("Southwest Florida Water Management District — district extends Modified Phase III water shortage order", "https://www.swfwmd.state.fl.us/the-newsroom/2026/district-extends-modified-phase-iii-water-shortage")

SRC = [GATEWAY, GREEN_SWAMP_LAW, POLK_BUILDING, POLK_PA, DOH_SEPTIC, CANDLER_OSD, MYAKKA_OSD, BASINGER_OSD,
       LAKE_AGNES, FANTASY_FLIGHT, TECO_TRAIL, POP_POLK_CITY, SWFWMD_EXT, "dep-rule", "fs125572"]

# ============================================================== hub
HUB = page(
    C["route"], "city",
    "Artificial Turf in Polk City, FL (2026)",
    f"Synthetic turf installation in Polk City, FL: Green Swamp drainage rules, well-and-septic lots, Polk County permits and the {price('residential')} market range, September 2026.",
    "Artificial turf at the Green Swamp's edge, from acreage lots to the chain of lakes",
    capsule(f"Kissimmee Artificial Turf installs and repairs synthetic lawns in Polk City, the self-described “Gateway to the Green Swamp,” at the same {price('residential')} range as the rest of Central Florida, roughly {C['miles']} miles out from our Kissimmee base. Polk County, not a Polk City building department, reviews the permit here. As of September 2026, enough of the city's outlying lots sit on a well and septic system to change how a base gets planned."),
    "".join([
        sec("Gateway to the Green Swamp, not just a name",
            f"<p>Polk City sits in north Polk County between {city('lakeland', 'Lakeland')} and I-4, and it calls itself the “Gateway to the Green Swamp” on its own website, a description that's more than a slogan ({ext(GATEWAY[1], "the city's own Green Swamp page")}). The Green Swamp Area of Critical State Concern, designated under state law since 1974, holds the headwaters of four rivers, the Withlacoochee, Oklawaha, Hillsborough and Peace, and sits over some of the highest groundwater in the Florida peninsula, which is part of why the area matters so much to the Floridan Aquifer that the whole state draws on ({ext(GREEN_SWAMP_LAW[1], "Florida's Green Swamp statute")}). The same protected wetland reaches west into Lake County, past {city('groveland', 'Groveland')}, so a mis-graded yard here drains toward the same system, which is part of why the state turf rule is so strict about installing inside a drainage swale, ditch or a stormwater pond's littoral zone.</p>"),
        sec("City water in town, wells and septic on the outskirts",
            f"<p>Polk City's own Water Department supplies drinking water and fire protection inside city limits, but plenty of lots on the city's rural edges, especially toward the Green Swamp side, sit on a private well with a septic system instead of city service. The Florida Department of Health in Polk County permits every new or repaired septic system in the county, including these ({ext(DOH_SEPTIC[1], 'Florida DOH in Polk County')}). A seasonally high water table near the swamp's edge is common enough that a septic permit often calls for a mound-style drainfield, built up in fill rather than dug into the ground, to keep the required separation from groundwater. Either way, Florida's turf rule requires that a septic tank's pump-out lid stay reachable once a lawn is finished, which matters on a well-and-septic lot here more often than it does on a city-sewer block downtown.</p>"),
        sec("Two lake chains, a museum and a rail-trail",
            f"<p>The Polk City Chain of Lakes, Agnes, Mattie, Martha and Juliana among them, wraps the town's south and west sides and puts a working share of Polk City yards behind the state's 10-foot buffer from open water, a line that only moves closer to shore where a seawall already stands in for it ({ext(LAKE_AGNES[1], 'Polk County Water Atlas records')}). Kermit Weeks' Fantasy of Flight, a vintage-aircraft museum that has drawn visitors to a Polk City address since 1995, sits a short drive from downtown ({ext(FANTASY_FLIGHT[1], 'Visit Central Florida')}), and the paved Auburndale TECO Trail rolls into town from the east to meet the 29-mile Van Fleet State Trail at the Polk City trailhead ({ext(TECO_TRAIL[1], "Florida Hikes' trail guide")}). The city itself stayed small through most of that: 2,713 residents at the 2020 Census, an estimated 2,974 by 2024, growth that's real but still small enough that a Polk County reviewer, not a city building department, handles the paperwork ({ext(POP_POLK_CITY[1], "Florida Demographics' Polk City page")}).</p>"),
        table("Polk City yard types and what we do differently",
              ["Yard type", "What changes here", "How we handle it"],
              [["Rural acreage lot on well and septic", "No city water; a septic pump-out lid to keep clear", "Map the septic lid before grading; cap only what's on the well-fed irrigation zone"],
               ["Lot on the Chain of Lakes (Agnes, Mattie, Martha, Juliana)", "A 10-foot buffer from the water applies unless a seawall is already doing that job", "Stake the buffer before ordering material, same as any Florida lake lot"],
               ["In-town lot on a city water line", "Regular city service, smaller platted lot", "Standard washed-rock base, no septic or well complications"],
               ["Newer subdivision lot away from downtown", "Younger landscaping, fewer mature trees", "Straightforward base and drainage plan, full-sun infill choice"]],
              "Compiled from the Polk County Water Atlas, Polk City's own utility and Green Swamp pages and Florida DOH septic guidance, checked September 2026."),
        sec("Polk County, not Polk City, reviews the permit",
            f"<p>Polk City has no building department of its own; Polk County's Building Division, at 330 W. Church Street in Bartow, reviews permits for the city the same way it does for the unincorporated county around it, and a call to 863-534-6080 reaches the office directly ({a('/laws/permits/polk-county/', 'our Polk County permit page')} covers what the county's code does and doesn't say about synthetic turf). Applications run through the county's Accela-based Citizen Access portal rather than a separate Polk City system ({ext(POLK_BUILDING[1], "Polk County's own permitting page")}). As of September 2026 that code has no line naming synthetic turf, so {a('/laws/florida-hb-683/', "the state's May 2026 standard")} is the only turf-specific rule reaching a Polk City lot, on top of whatever the county's ordinary drainage and land-alteration review already requires. Checking a specific address against {ext(POLK_PA[1], "the county property appraiser's parcel records")} confirms it's inside city limits before that call, since Polk City's boundary runs an irregular line through otherwise rural county land.</p>"),
        "<!--AUTO:city-services-->",
    ]),
    faqs=[
        faq("What should the best synthetic turf installer near me in Polk City ask before quoting a well-and-septic lot?", "Whether they'll map the septic drainfield and pump-out lid, and confirm the irrigation zone's water source, before laying out a job, rather than treating every acreage lot like a standard city-water yard. An installer who asks about well versus city service unprompted has actually thought about the address."),
        faq("Does Polk City or Polk County issue the turf permit?", "Polk County does. Polk City has no building department of its own, so the county's Building Division in Bartow reviews permits inside city limits the same way it reviews the surrounding unincorporated county."),
        faq("Which lakes trigger the 10-ft setback in Polk City?", "The Polk City Chain of Lakes, Agnes, Mattie, Martha and Juliana, wraps much of the town's south and west sides, and Florida's rule holds any lawn on them back 10 feet from the ordinary shoreline, closer only where a seawall or bulkhead already does that separating."),
        faq("Is Polk City really inside the Green Swamp?", "Polk City brands itself the “Gateway to the Green Swamp” on its own website, and the Green Swamp Area of Critical State Concern, in state law since 1974, does reach the town's edges. That designation is mainly about wetlands, floodplain and aquifer recharge rather than a separate turf rule."),
        faq("What's the current watering schedule for a Polk City address?", "September 2026 finds every address in the district, Polk City's included, down to one watering night a week under an extreme-shortage order from Southwest Florida's water managers, a restriction running through October 1. None of that reaches a synthetic lawn once its irrigation heads are capped."),
    ],
    sources=SRC, city=SLUG, crumbs=[("Service areas", "/areas/")], crumb="Polk City",
    related=[("/areas/polk-county/", "Artificial turf across Polk County"), ("/laws/permits/polk-county/", "Polk County permit rules for turf"),
             ("/areas/auburndale/", "Turf in Auburndale"), ("/areas/davenport/", "Turf in Davenport"), ("/artificial-turf-cost/", "Turf cost tables for Central Florida")])

# ============================================================== local
LOCAL = {
    "residential": {
        "title": "Artificial Grass Installation in Polk City, FL – Well Lots",
        "meta": f"Synthetic lawn installation in Polk City, FL: well-and-septic lots, Green Swamp drainage rules and the {price('residential')} market range, September 2026.",
        "h1": "Artificial Grass for Polk City's Well, Septic and City-Water Lots",
        "lede": capsule(f"A Polk City homeowner converting a lawn pays {price('residential')} a square foot as of September 2026, the market range that holds from the Green Swamp's edge to a city-water block downtown. What changes lot to lot here is what surrounds the yard: a septic tank's pump-out lid to keep clear, a well-fed irrigation zone to cap, or a lake chain close enough to trigger the state's 10-ft setback."),
        "sections": [
            ("Mapping the septic lid before the base goes in",
             f"<p>Enough Polk City lots outside the city-water grid run on a private well and septic system that mapping the tank's pump-out lid is a standard early step here, more than it is on a typical in-town Central Florida lot. The Florida Department of Health in Polk County permits every new or repaired septic system in the county, including these ({ext(DOH_SEPTIC[1], 'Florida DOH in Polk County')}), and Florida's synthetic turf rule separately requires that a tank's access stay reachable once a lawn is finished, not buried under compacted base and turf like the rest of the yard. The base gets built up to the lid's edge rather than over it, and that edge gets checked again once the surrounding grade is finished, before turf goes down anywhere nearby.</p>"),
            ("Why the Green Swamp's edge matters for grading",
             f"<p>Polk City calls itself the “Gateway to the Green Swamp,” and that isn't just a slogan for a homeowner grading a lawn near the edge of it. The Green Swamp Area of Critical State Concern holds some of the highest groundwater in the Florida peninsula and feeds four rivers ({ext(GREEN_SWAMP_LAW[1], "Florida's Green Swamp statute")}), which is part of why the state's turf rule is strict about keeping synthetic grass out of a drainage swale, ditch or a stormwater pond's littoral zone. A yard that slopes toward a roadside ditch on a swamp-adjacent lot needs that grading confirmed before any rock goes down, since the standard 1 to 2 percent fall away from the house still has to land somewhere that isn't one of those excluded features.</p>"),
            ("A city-water block downtown still gets the same base",
             "<p>Not every Polk City lot deals with a well or a swamp-edge drainage question. Blocks close to downtown and the city's own water lines look like a typical small Central Florida neighborhood: smaller platted lots, ordinary city sewer or septic within city limits, and no particular wetlands complication to plan around. The base underneath still runs the same two to four inches of washed, open-graded crushed rock either way, since the state's material standard doesn't have a separate rule for a city-water block versus a rural acre; what differs between the two is everything around the base, not the base itself.</p>"),
        ],
        "scenario": ("Say you have a 900 sq ft lawn on a well-and-septic acre",
                     f"<p>Say a Polk City acre lot on a private well has a 900 sq ft front yard where St. Augustine has struggled for years against sandy soil and inconsistent well-fed irrigation. At {price('residential')} a square foot, that yard prices between $7,200 and $16,200 installed, with the septic tank's location and how far the crew has to run to cap the well-fed irrigation zone both moving a specific quote inside that range. A similarly sized yard on a city-water block downtown prices the same per square foot, minus the septic mapping step this lot needs first.</p>"),
        "faqs": [
            faq("Does a Polk City septic system limit where turf can go?", "Not where it can go so much as what has to stay accessible. The state's turf rule requires a septic tank's pump-out lid to remain reachable once a lawn is finished, so the base gets built around that spot rather than over it; the rest of the yard can be turfed the same as any other lot."),
            faq("Is Polk City's Green Swamp location a flood risk for a new lawn?", "The Green Swamp raises the stakes on drainage rather than flooding a typical upland lot directly. Grading a yard to fall away from the house and never into a swale or ditch matters more here than on a lot farther from the swamp's edge, since runoff eventually reaches wetlands the state regulates closely."),
        ],
        "sources": SRC,
    },
    "pet": {
        "title": "Pet Turf & Dog Runs in Polk City, FL – Acre Lots",
        "meta": f"Pet turf and dog runs in Polk City, FL: capped well irrigation, septic-safe layouts and the {price('pet')} market range, September 2026.",
        "h1": "Dog Runs for Polk City's Acreage and In-Town Lots",
        "lede": capsule(f"Dog owners on a Polk City acreage lot pay {price('pet')} a square foot for pet turf, the Central Florida figure that doesn't move whether the run sits on city water or a private well. A bigger rural lot usually means more room for a run than a tighter in-town yard, but the septic tank's location and the state's capped-irrigation rule matter on both."),
        "sections": [
            ("Sizing a run on open acreage versus a tight in-town yard",
             "<p>A Polk City acre lot toward the Green Swamp side of town often has room for a dog run several times the size of anything possible on a smaller in-town parcel, and that extra space changes the layout question more than the construction method. A bigger run still needs the same washed-rock base and silica or zeolite infill as a small one; what a bigger footprint actually buys is room to route the run around a septic drainfield or a well's protective radius instead of running tight against a fence line the way a small in-town yard has to.</p>"),
            ("Capping irrigation that draws from a well instead of a meter",
             "<p>A dog run's old sprinkler zone gets capped at the valve box before turf goes down the same way anywhere in Florida, but on a Polk City lot fed by a private well rather than a city meter, that valve box sits closer to the well's own pressure tank than a typical suburban setup does. The capping itself doesn't change: the state's rule bars an in-ground system from watering synthetic turf regardless of what supplies the water, and the old zone for that section of yard just gets left capped once the pet turf is down. What's worth confirming first on a well-fed system is that capping one zone doesn't affect pressure to the rest of the property's irrigation.</p>"),
            ("Keeping a run clear of the septic drainfield",
             "<p>A septic drainfield needs airflow and unobstructed soil to work correctly, which makes it one of the few spots on a Polk City acre lot where a dog run genuinely shouldn't go, turf or not. Mapping the drainfield's footprint against the proposed run happens before any digging starts, not as an afterthought, since compacting rock and turf over an active drainfield can shorten its working life. Most Polk City lots large enough to consider a serious dog run also have enough room to route around the drainfield entirely, which is more often a layout adjustment than a real limit on run size.</p>"),
        ],
        "scenario": ("Say you have a 20×30 dog run on a Polk City acre",
                     f"<p>Say a Polk City acre lot fences off a 20-by-30 dog run along the side yard, away from the drainfield and clear of the well's own service radius, 600 sq ft in total. At {price('pet')} a square foot, that run prices between $6,000 and $10,800 installed, with the well-capping step and however far the crew has to carry material from the driveway both nudging a specific quote inside that range. A run half that size on a smaller in-town Polk City lot scales the same way per square foot, minus any septic or well planning if that lot happens to be on city service instead.</p>"),
        "faqs": [
            faq("Does well water change the infill choice for Polk City pet turf?", "No. Silica sand, coated sand and zeolite all work the same regardless of whether the yard's hose bib draws from a well or city service; infill choice depends on odor-control preference, not water source."),
            faq("How close can a Polk City dog run sit to a septic drainfield?", "There's no single statewide number for turf specifically, but Florida's septic rules already require setbacks between a drainfield and any structure or heavily compacted surface. Mapping the drainfield against the health department's permit record before laying out a run is the safest starting point."),
            faq("What should the best pet turf installer near me in Polk City know about an acreage lot?", "Whether they'll map a septic drainfield and a well's service area before laying out a run, not just measure the fence line. An installer used to Polk City's mix of acreage and in-town lots asks about water source and septic before quoting, not after."),
        ],
        "sources": SRC,
    },
    "putting": {
        "title": "Backyard Putting Greens in Polk City, FL – Rural Acres",
        "meta": f"Backyard putting greens in Polk City, FL: flat rural acreage, Green Swamp-edge drainage and the {price('putting')} market range, September 2026.",
        "h1": "Putting Greens for Polk City's Rural and In-Town Lots",
        "lede": capsule(f"A putting green built in Polk City runs {price('putting')} a square foot, the published Central Florida band, and the town's mix of flat rural acreage and tighter in-town lots changes the layout more than it changes the price. A green near the Green Swamp's edge needs the same drainage discipline as any lawn there; one on a smaller downtown lot has to work harder for its square footage."),
        "sections": [
            ("Flat acreage gives a green room, not automatic drainage",
             "<p>A flat rural acre toward the edge of the Green Swamp gives a putting green plenty of room to work with, more than most in-town Polk City lots offer, but flat ground doesn't drain itself the way a ridge lot's slope would. The green's own engineered base, compacted aggregate under a permeable backing, still has to be built to shed water on its own, since a swamp-adjacent lot's already-high water table gives a poorly built base nowhere to send water that doesn't drain through it fast enough. Space is the advantage here; the drainage work is not optional just because the lot is generous.</p>"),
            ("Fitting a green onto a smaller in-town Polk City lot",
             f"<p>Closer to downtown, where {city('auburndale', 'Auburndale')} sits within easy reach, Polk City's older platted lots run smaller than the acreage on the swamp side of town, which usually means a shorter green with fewer cups rather than a full practice layout. A two-cup green with a modest fringe fits comfortably on a lot that couldn't support a longer run, and the same washed-rock base and {svc('putting', 'synthetic surface')} go into it regardless of size. What a smaller lot loses in length, careful contouring on the cups that do fit can partly make up for.</p>"),
            ("Soil under a green on the swamp side of town",
             f"<p>Ground on Polk City's lower, swamp-facing side tends toward Myakka and Basinger series soils, very poorly to poorly drained sands with a water table that can sit close to the surface for weeks after a wet summer, according to the USDA's official series descriptions ({ext(MYAKKA_OSD[1], 'Myakka series')}; {ext(BASINGER_OSD[1], 'Basinger series')}). Higher ground elsewhere in town, more toward the ridge country shared with {city('lake-alfred', 'Lake Alfred')}, runs closer to excessively drained Candler sand instead ({ext(CANDLER_OSD[1], 'Candler series')}). A green's base recipe doesn't change between the two, washed, open-graded rock either way, but a crew treats a Myakka-series lot with more caution about building the base up rather than trusting the ground underneath to help it drain, the same principle {post('base-under-artificial-turf-florida-sandy-soil', 'laid out here')} for Central Florida's sandy soils broadly.</p>"),
        ],
        "scenario": ("Say you have a 450 sq ft green on a rural Polk City acre",
                     f"<p>Say a rural Polk City acre near the Green Swamp's edge has room for a 450 sq ft green with three cups and a wraparound fringe, well clear of any wetland boundary. At {price('putting')} a square foot, that green prices between $6,300 and $13,500 installed, with cup count and fringe width doing most of the work of setting where in that range a specific quote lands. A shorter, two-cup version on a smaller in-town lot runs toward the lower end of the same per-square-foot range, simply because there's less total area to build.</p>"),
        "faqs": [
            faq("Does a wetter Myakka-series lot need a different putting-green base than Candler sand?", "The base material is the same washed, open-graded rock either way, but a crew builds it with more attention to compaction and depth on a Myakka or Basinger-series lot, since that soil holds water near the surface longer than the excessively drained Candler sand on higher ground."),
            faq("Can a putting green go near a Polk City lake without an issue?", "Only behind the state's 10-foot buffer from open water, the same rule that applies on any Florida lake or pond, closer only where a seawall already does the separating. Most lots on the Polk City chain of lakes still have room for a green outside that strip."),
            faq("How do you find the best putting green builder near me in Polk City?", "Ask whether they've priced a job on both sides of town: a flat, well-drained rural acre and a smaller in-town lot with less room to work with. A builder who asks about soil and lot size before naming cup count has actually thought about the specific yard."),
        ],
        "sources": SRC,
    },
    "playground": {
        "title": "Playground Turf in Polk City, FL – Rural and In-Town",
        "meta": f"Playground turf in Polk City, FL: shock-pad sizing, oak and cypress shade near the swamp edge and the {price('playground')} market range, September 2026.",
        "h1": "Playground Turf for Polk City's Acreage and Subdivision Lots",
        "lede": capsule(f"Play-area turf in Polk City costs {price('playground')} a square foot, holding steady whether the yard sits on a wooded acre near the Green Swamp's edge or a tighter lot in a newer subdivision. Fall height from the actual equipment sets shock-pad thickness either way, and a swamp-edge lot's mature oak or cypress cover usually does more to keep a play area cool than anything built into the turf itself."),
        "sections": [
            ("Shade from swamp-edge oaks and cypress heads",
             f"<p>Lots toward the Green Swamp side of Polk City sometimes back up to a cypress head or carry an old live oak that's shaded the same corner of yard for decades, and that natural cover does real work keeping a play area's surface temperature down compared with open sun. The state's turf rule still keeps synthetic grass out of any tree's drip line without a certified arborist's sign-off, which means the shadiest, most comfortable spot for a play structure is sometimes also the spot the rule limits the most. Marking the actual canopy edge, not just the trunk, before finalizing where the turf and its shock pad go avoids planning a layout that has to shrink later, and {post('artificial-turf-near-live-oaks-and-palms', 'our piece on turf near live oaks and palms')} covers the drip-line rule in more depth.</p>"),
            ("Fall height on a subdivision lot without mature trees",
             "<p>A newer subdivision lot away from the swamp side of town usually starts with young landscaping instead of established shade, which puts a play area in full sun for most of the day until the trees planted with the house actually grow in. Shock-pad thickness there still comes from the equipment's fall height, not the amount of sun, but the hose-rinse habit that keeps surface temperature manageable matters more on an unshaded lot than a shaded one. A lighter infill color is a small, one-time choice at installation that keeps paying off every summer afternoon on a lot like this.</p>"),
            ("Building a play area's base on a well-and-septic lot",
             "<p>On a Polk City acre without city sewer, the same septic-access rule that applies to the rest of the yard applies to a play area too: if a tank's pump-out lid sits anywhere near the planned layout, the base gets built around it rather than over it. A play area's base otherwise looks like any other turf base, two to four inches of washed, open-graded rock under the shock pad, sized to the fall height rather than to whether the lot is on a well or a city meter. The septic question is a layout detail, not a different construction method.</p>"),
        ],
        "scenario": ("Say you have a 200 sq ft play area under a swamp-edge oak",
                     f"<p>Say a Polk City acre near the Green Swamp's edge has a 200 sq ft play area planned under the shade of an old live oak, just outside the mapped drip line, for a swing set with a five-foot fall height. At {price('playground')} a square foot, that area prices between $2,000 and $5,000 installed, with shock-pad thickness sized to the five-foot fall height setting most of where in that range the job lands. The same area on a sunny new subdivision lot prices the same per square foot, with a lighter infill color doing the work the oak's shade would otherwise provide.</p>"),
        "faqs": [
            faq("Does a Green Swamp-edge lot's shade change shock-pad thickness?", "No. Shade affects surface temperature and comfort, not the shock rating a specific fall height requires. A play area under a swamp-edge oak and one in full sun on a new subdivision lot use the same pad thickness if the equipment's fall height matches."),
            faq("Can playground turf go near a septic drainfield on a Polk City lot?", "It depends on the drainfield's mapped location relative to the equipment and its fall zone. Keeping compacted base and turf off an active drainfield protects both the septic system and the play area's long-term drainage, so mapping it first is worth the extra step."),
        ],
        "sources": SRC,
    },
    "pool": {
        "title": "Pool & Lanai Turf in Polk City, FL – Deck Strips",
        "meta": f"Turf around a Polk City pool cage or lanai: drainage underlay over concrete and the {price('residential')} market range, checked September 2026.",
        "h1": "Turf for Polk City Pool Decks and Screened Lanais",
        "lede": capsule(f"A screened pool deck in Polk City takes the same turf as any lawn, {price('residential')} a square foot, and it's usually the deck's own concrete, not the well water or the lake nearby, that decides how the edges get set. A lanai strip needs a drainage layer under it; the surrounding yard, on well or city water, still gets the standard washed-rock base."),
        "sections": [
            ("The deck's drainage layer doesn't care about the water source",
             "<p>A screened enclosure's floor is poured concrete, not soil, and concrete doesn't pass water the way a compacted rock base does, which is why turf going down inside a lanai needs its own drainage layer between the slab and the backing no matter what feeds the house's taps. The perimeter bonds to that concrete with adhesive instead of nails, since there's no ground at the edge for a fastener to bite into, and whichever irrigation zone used to reach that side of the pool cage gets capped at the valve box the same as any other, well pump or metered line alike.</p>"),
            ("A lake-view lanai and the state's setback",
             "<p>A handful of Polk City pool homes sit on the chain of lakes, Agnes, Mattie, Martha and Juliana, closely enough that the screen enclosure itself sits well within what would otherwise be the state's required buffer from open water. That buffer is about turf, not the structure, so an existing lanai isn't affected, but yard turf outside the cage that continues toward the water still has to clear the same 10-foot line the state sets for any shoreline, unless a seawall already stands in the way. Staking that boundary before extending turf past the pool cage's own footprint keeps a straightforward job from running into a setback question late.</p>"),
            ("Heat on an open acreage pool deck",
             "<p>A pool deck on an open rural acre without much surrounding shade can run hotter underfoot than one tucked closer to town under established trees, and a hose rinse before anyone walks the deck barefoot drops that surface temperature 30 to 50 degrees within minutes. The fix costs nothing beyond the water itself, which matters on a well-fed property where a homeowner might otherwise hesitate to run a hose for a reason that feels cosmetic rather than necessary. A lighter-colored infill is a one-time choice at installation that reduces how often that rinse is needed. Either way, the deck's concrete and its drainage layer, not the water source, decide how the job gets built.</p>"),
        ],
        "scenario": ("Say you have a 350 sq ft lanai strip on a Polk City lake lot",
                     f"<p>Say a screened lanai on a Polk City lake lot has a 350 sq ft strip of turf planned between the pool deck and the enclosure's frame, comfortably inside the cage and nowhere near the required lake setback. At {price('residential')} a square foot, that strip prices between $2,800 and $6,300 installed, with the deck's drainage underlay accounting for most of the difference between the low and high end. A similar strip on a rural acre without a pool cage at all, just turf around an open deck, prices the same per square foot without that underlay cost.</p>"),
        "faqs": [
            faq("Does a Polk City lanai on well water need different turf than one on city water?", "No. Turf and infill choice don't depend on water source; a hose rinse works the same either way. What matters for a lanai is the concrete deck underneath, which needs a drainage layer regardless of where the water comes from."),
            faq("Is a pool screen enclosure itself affected by the state's 10-ft lake setback?", "No, the setback applies to turf, not to an existing structure. A screen enclosure already built close to the water stays as it is; it's any new turf extending past the cage toward the lake that has to respect the 10-ft line."),
        ],
        "sources": SRC,
    },
    "repair": {
        "title": "Artificial Turf Repair in Polk City, FL – Well & Deck Fixes",
        "meta": "Turf repair in Polk City, FL: capped-well irrigation fixes, driveway-edge repairs and swamp-edge base checks, quoted after photos or a visit.",
        "h1": "Fixing Polk City Turf: Wells, Edges and Rushed Bases",
        "lede": capsule("Fixing a seam or a bare patch on a Polk City lawn is priced from photos or a short visit rather than a flat number, since a well-and-septic lot's access and an older in-town driveway edge fail for different reasons. Polk County's Building Division, not a Polk City department, is still the office that would review any repair large enough to need a permit."),
        "sections": [
            ("When a repair traces back to a well pump, not the turf",
             "<p>A Polk City lawn on a private well sometimes develops a soggy, discolored patch that looks like a drainage failure in the turf itself but actually traces back to a leaking well line or a pressure tank cycling more than it should underneath that section of yard. Ruling that out before pulling up turf to rebuild a base that was never the problem saves a callback and a second bill. A city-water lot doesn't have this specific failure mode, since a metered line rarely leaks underground the way an older well system's fittings can. A quick check of the meter or the well pump's cycling pattern before any turf comes up is worth the ten minutes it takes.</p>"),
            ("Driveway-edge repairs on Polk City's older platted lots",
             "<p>An older platted lot closer to downtown Polk City often backs turf up to a driveway poured well before synthetic turf was part of the plan, and that edge, glued rather than staked since there's no soil to anchor into, is usually the first place a repair call comes from. A slab that's settled unevenly over the years leaves a gap or a ridge at the transition that a freshly poured driveway on a newer lot hasn't had time to develop yet. Re-trimming and re-gluing that one edge is typically a smaller job than a homeowner expects once photos show exactly where the slab has moved.</p>"),
            ("Base checks on the Green Swamp side of town",
             f"<p>A rushed or thin base on a lot toward the Green Swamp's edge tends to show trouble sooner than the same shortcut would on higher, better-drained ground, since the wetter Myakka and Basinger-series soils there give a struggling base less room for error ({ext(MYAKKA_OSD[1], 'Myakka series')}). A section that holds water for days after a storm, rather than draining within hours, usually points to a base that was never built to the fuller end of the state's two-to-four-inch range, or to unwashed fill that's crusted over underneath. Photos of standing water and how long it's been there help narrow that down before a crew ever gets on site, alongside the general drainage principles {post('does-artificial-turf-drain-in-heavy-rain', 'covered here')}.</p>"),
        ],
        "scenario": ("Say you have a soggy patch that won't drain after storms",
                     "<p>Say a Polk City lawn near the Green Swamp's edge has a roughly 4-by-6-ft patch that holds visible water for two full days after a normal summer storm, while the rest of the yard drains within hours. That could mean the base under just that section was compacted too tight, or that unwashed fill snuck into an otherwise correct rock layer during the original build. Either fix means pulling back turf over that specific patch rather than the whole lawn, but knowing which one it is, and how deep the problem runs, takes a look at the base itself, not a guess based on the patch's size alone.</p>"),
        "faqs": [
            faq("Does a well-related soggy patch mean the turf itself failed?", "Not usually. Turf and its backing rarely fail on their own; a soggy patch more often points to something underneath, a leaking well line, a pressure tank issue, or a base that was compacted too tight in that one spot, rather than a problem with the turf material."),
            faq("Do driveway-edge repairs need Polk County's permit process?", "Rarely, for a simple re-glue or re-trim of an existing edge. A repair that involves regrading a larger section or changing drainage near the driveway is worth a call to Polk County's Building Division first, since that's the office that reviews permits for Polk City addresses."),
        ],
        "sources": SRC,
    },
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
