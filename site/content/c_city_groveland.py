# -*- coding: utf-8 -*-
"""Groveland, FL (tier 3, Lake County). Hub + residential/pet/putting city x service pages.
Researched September 2026: City of Groveland site (Building & Permitting division, water-conservation
ordinance, Green Swamp page, Chapter 4 comprehensive plan), USDA official series descriptions for
Candler and Astatula, Lake.WaterAtlas.org for Lake David/Lake Lucy/Cherry Lake, Census/Neilsberg
population figures, and public listings for Trilogy Orlando, Eagle Pointe and Green Valley."""
from _data import CITIES
from _helpers import page, capsule, sec, table, faq, a, svc, city, post, ext, price
from _cityservice import cityservice_pages

SLUG = "groveland"

GROVELAND_BUILDING = ("City of Groveland — Building Division", "https://groveland-fl.gov/130/Building-Division")
GROVELAND_CED = ("City of Groveland — Community and Economic Development Department", "https://www.groveland-fl.gov/133/Community-and-Economic-Development")
GROVELAND_PORTAL = ("City of Groveland — eTRAKiT online permit portal", "https://gvld-trk.aspgov.com/etrakit/")
GROVELAND_WATER = ("City of Groveland — Water Conservation and irrigation ordinance", "https://www.groveland-fl.gov/408/Water-Conservation")
GROVELAND_SWAMP = ("City of Groveland — The Green Swamp", "https://groveland-fl.gov/538/The-Green-Swamp")
GROVELAND_COMPPLAN = ("City of Groveland — Comprehensive Plan, Chapter 4, Public Facilities Element", "http://groveland-fl.gov/DocumentCenter/View/5523/Chapter-04---Public-Facilities")
CANDLER_OSD = ("USDA NRCS — official series description, Candler series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/C/Candler.html")
ASTATULA_OSD = ("USDA NRCS — official series description, Astatula series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/A/ASTATULA.html")
GROVELAND_POP = ("Neilsberg — Groveland, FL population by year", "https://www.neilsberg.com/insights/groveland-fl-population-by-year/")
TRILOGY_SRC = ("55places — Trilogy Orlando, a 55+ community in Groveland, FL", "https://www.55places.com/florida/communities/trilogy-orlando")
EAGLE_POINTE_SRC = ("Homes by Marco — Eagle Pointe subdivision, Groveland, FL", "https://www.homesbymarco.com/subdivisions/eagle-pointe-in-groveland-fl")
GREEN_VALLEY_SRC = ("Homes by Marco — Green Valley Townhomes, Groveland, FL", "https://www.homesbymarco.com/subdivisions/green-valley-townhomes-in-groveland-fl")
LAKE_DAVID_SRC = ("Lake.WaterAtlas.org — Lake David, Groveland", "https://lake.wateratlas.usf.edu/waterbodies/lakes/7968/lake-david")
LAKE_LUCY_SRC = ("Lake.WaterAtlas.org — Lake Lucy, Groveland", "https://lake.wateratlas.usf.edu/waterbodies/lakes/8028/lake-lucy")
CHERRY_LAKE_SRC = ("Lake.WaterAtlas.org — Cherry Lake, Groveland", "https://lake.wateratlas.usf.edu/waterbodies/lakes/7842/cherry-lake")

SRC = [GROVELAND_BUILDING, GROVELAND_CED, GROVELAND_PORTAL, GROVELAND_WATER, GROVELAND_SWAMP, GROVELAND_COMPPLAN,
       CANDLER_OSD, ASTATULA_OSD, GROVELAND_POP, TRILOGY_SRC, EAGLE_POINTE_SRC, GREEN_VALLEY_SRC,
       LAKE_DAVID_SRC, LAKE_LUCY_SRC, CHERRY_LAKE_SRC, "dep-rule", "fs125572", "fs7203045"]

MI = CITIES[SLUG]["miles"]

# ============================================================== hub
HUB = page(
    "/areas/groveland/", "city",
    "Artificial Turf Installation in Groveland, FL (2026)",
    "Synthetic grass installed on Groveland's ridge lots, resort subdivisions and lakefront yards. Permits, water rules and pricing, checked September 2026.",
    "Synthetic grass for Groveland's ridge lots and new subdivisions",
    capsule(f"Groveland's population more than doubled between 2010 and 2020 and kept climbing toward 25,000 by 2024, and we install and repair synthetic turf across the ridge lots and resort subdivisions that growth left behind. September 2026's installed price for a Central Florida lawn runs {price('residential')} a square foot, the same figure whether the yard sits on Groveland's sand or closer to Kissimmee."),
    "".join([
        sec("Ridge sand, a resort community and a fast-growing skyline",
            "<p>Groveland sits on the northeastern edge of the sand ridge running through south Lake County, and the ground under a typical yard shows it. The Candler and Astatula series the USDA maps here are excessively drained fine sands with a water table more than 80 inches down, the opposite problem from the flatwoods soil that holds water near the surface closer to Kissimmee. A base built into ground like this isn't fighting rain with nowhere to go; it's holding a stable surface on sand that already drains faster than the state's permeability standard asks for.</p>"
            + f"<p>What has reshaped Groveland's yards more than the soil is how fast the city has grown. {ext('https://www.55places.com/florida/communities/trilogy-orlando', 'Trilogy Orlando')}, a Shea Homes 55+ community, added 1,500 houses on the north side alone, and newer subdivisions such as {ext('https://www.homesbymarco.com/subdivisions/eagle-pointe-in-groveland-fl', 'Eagle Pointe')} and {ext('https://www.homesbymarco.com/subdivisions/green-valley-townhomes-in-groveland-fl', 'Green Valley')} have filled the gaps around older lake lots downtown. A lawn conversion looks different on each: a compact resort villa, a builder-grade quarter acre, or a shoreline yard older than most of the growth around it.</p>"),
        table("Groveland yard types and what we do differently",
              ["Yard type", "What changes for the crew"],
              [["Trilogy Orlando and other 55+ resort lots", "Front yards are mowed under the community fee, so requests concentrate on the fenced backyard the association never touches"],
               ["Ridge subdivisions like Eagle Pointe and Green Valley", "Base depth targets a firm, level surface on fast-draining Candler and Astatula sand rather than fighting a high water table"],
               ["Older lots on Lake David, Lake Lucy or Cherry Lake", "10-ft waterbody setback from the shoreline, waived only where a seawall or bulkhead already stands"],
               ["Rural acreage toward the Green Swamp edge", "No turf inside a swale, ditch or wetland buffer; well and septic access gets mapped before any rock goes down"]],
              "Checked against the city's own site and USDA soil data, September 2026."),
        sec("Permits and the state standard in Groveland",
            f"<p>Groveland runs its own permitting rather than routing applications through Lake County, so {a('/laws/permits/lake-county/', 'the Lake County turf permit page we maintain')} is written for unincorporated pockets of the county, not an address inside city limits. We don't have a page breaking down Groveland's own code the way we do for a few larger cities, so here's what we found directly: Building & Permitting, under the city's Community and Economic Development Department at 6825 SR 50, takes applications at 352-429-2141 (option 2) and online through its {ext('https://gvld-trk.aspgov.com/etrakit/', 'eTRAKiT portal')}. Nothing published names synthetic turf specifically in the city's code as of September 2026, a reason to call ahead, not a signal either way.</p>"
            + f"<p>An HOA is a separate question from a city permit. {a('/laws/hoa-rules/', 'what a Florida HOA can and cannot restrict')} turns mostly on visibility: whatever a fence hides from the street or a neighbor's lot gets more latitude than a front yard, reaching a subdivision like Eagle Pointe the same way it reaches a resort community. {a('/laws/florida-hb-683/', 'the statewide May 2026 turf rule')} sets the floor everywhere in Groveland regardless of which side of the ridge a lot sits on: capped irrigation heads, a washed-rock subgrade, turf held back from the waterbody setback and any drip line.</p>"),
        sec("Water rules, and the swamp at the edge of town",
            f"<p>Groveland's irrigation ordinance, adopted as {ext('https://www.groveland-fl.gov/408/Water-Conservation', 'City Ordinance 2009-03-09')}, runs under the St. Johns River Water Management District's governing board rather than the Southwest Florida district that manages the Green Swamp preserve a few miles south. During daylight saving time, odd-addressed lots water Wednesday and Saturday and even-addressed lots water Thursday and Sunday; once clocks fall back, each address gets a single day. None of that applies once a synthetic lawn's heads are capped, which the state's turf rule already requires.</p>"
            + f"<p>The swamp itself is a land-use question more than a water-utility one. Groveland's {ext('https://groveland-fl.gov/538/The-Green-Swamp', 'own Green Swamp page')} describes a 50-ft upland buffer required around wetlands and two Green Swamp-specific future land use categories created to keep construction out of the floodplain. That protective status sits closest to the rural, low-lying acreage on the city's western side, the same stretch where a turf layout has to route around a swale rather than cross it.</p>"),
        sec("Groveland sits near the edge of our range",
            f"<p>Groveland is about {MI} miles from downtown Kissimmee by straight line, close to the outer rim of the roughly 40-mile radius we cover. A job here isn't scheduled as a special trip; it rides along with other {a('/areas/lake-county/', 'Lake County')} stops the same day a crew is already headed toward {city('clermont')} or {city('minneola')}.</p>"),
        "<!--AUTO:city-services-->",
    ]),
    faqs=[
        faq("How do you find the best artificial turf installer near me in Groveland?",
            "Ask whether the crew has actually built a base on ridge sand before, since Candler and Astatula soils drain almost immediately and change the plan compared with flatwoods sand closer to Kissimmee. Past that, the usual checklist applies anywhere: measured square footage, named base depth, and infill type written into the quote."),
        faq("Does Trilogy Orlando allow artificial turf in the backyard?",
            "We haven't found a published design guideline from the community naming synthetic turf either way, so checking the current architectural packet before ordering anything is the honest step. Florida's HOA-visibility law still applies underneath whatever the community's review asks for."),
        faq("Is Groveland in a different water management district than Kissimmee?",
            "Groveland's own irrigation ordinance answers to the St. Johns River Water Management District's governing board, the same district Kissimmee falls under, even though part of the city sits inside the Green Swamp Area of Critical State Concern that the Southwest Florida district helps manage as protected land. Water-bill regulation and swamp preservation turn out to be two separate questions here."),
        faq("What's different about the soil in Groveland compared with Kissimmee?",
            "Groveland sits mostly on the Candler and Astatula ridge series, excessively drained fine sand with a water table more than 80 inches down. Kissimmee and most of Osceola County sit on flatwoods soil that holds water within a few feet of the surface for weeks after a storm, which is close to the opposite problem for a base to manage."),
        faq("Can turf go inside the 10-foot setback on a Lake David or Cherry Lake lot?",
            "Only where a seawall or bulkhead already separates the yard from the water. Without one, the state's rule keeps synthetic turf at least 10 feet back from the shoreline on a Groveland lake lot the same way it would anywhere else in Florida."),
    ],
    sources=SRC, city=SLUG,
    crumbs=[("Service areas", "/areas/")], crumb="Groveland",
    related=[("/areas/lake-county/", "Artificial turf across Lake County"),
             ("/laws/permits/lake-county/", "Lake County turf permit rules"),
             ("/areas/mascotte/", "Artificial turf in Mascotte"),
             ("/areas/clermont/", "Artificial turf in Clermont"),
             ("/artificial-turf-cost/", "Full turf cost guide")])

# ============================================================== local
LOCAL = {
    "residential": {
        "title": "Artificial Grass Installation in Groveland, FL — Ridge Lots",
        "meta": "Artificial grass installed on Groveland's fast-draining ridge sand and resort subdivisions. Base method, pricing and local rules, checked September 2026.",
        "h1": "Backyard turf built for Groveland's ridge sand",
        "lede": capsule(f"Most calls for artificial grass in Groveland come from the ridge subdivisions north of SR 50, where excessively drained Candler and Astatula sand changes the base plan more than it changes the finished lawn. Expect to pay {price('residential')} a square foot installed, September 2026's Central Florida figure, regardless of which side of the ridge a lot sits on."),
        "sections": [
            ("Why a Groveland lawn's base is about stability, not drainage",
             "<p>A residential base anywhere in Central Florida starts with the same washed, open-graded crushed rock the state's turf rule requires, but what that rock is fighting changes by soil. On the flatwoods sand around Kissimmee, the job is keeping a lawn above a water table that can sit within a couple of feet of grade for weeks. On Groveland's ridge, the Candler and Astatula series the USDA maps here are excessively drained, with a water table more than 80 inches down and low water-holding capacity even in the wet season.</p>"
             f"<p>That means a ridge lot rarely holds standing water after a storm, but it does shift underfoot more than flatter ground, especially on the steeper end of the zero-to-40-percent slope range these soils can carry. The same sand ridge continues south through {city('clermont')} and {city('minneola')}, so a base built here answers to the same drainage math a crew would use on either side of Groveland. The base still runs two to four inches deep and gets compacted in lifts; the reason for doing it carefully here is holding a level, stable surface on loose sand rather than lifting the lawn above a rising water table.</p>"),
            ("What a Trilogy Orlando or other 55+ lot changes",
             f"<p>{ext('https://www.55places.com/florida/communities/trilogy-orlando', 'Trilogy Orlando')} put 1,500 homes on Groveland's north side, and its monthly association fee covers front-yard lawn care along with internet, cable and access to the community's resort club, according to the community's own published pricing. That leaves the fenced backyard as the part of a resort lot most homeowners actually ask about turfing, since it's the one patch of ground the association fee never touches.</p>"
             f"<p>A resort villa's backyard also tends to be smaller and more uniform in shape than an older Groveland lot, which usually means less cutting and fewer seams. What it doesn't mean is a different rule: Florida's visibility statute for HOAs, covered in full at {a('/laws/hoa-rules/', 'what a Florida HOA can and cannot restrict')}, still applies to a resort community's design review the same way it would anywhere else.</p>"),
            ("Newer subdivisions and the older lake lots they surround",
             f"<p>{ext('https://www.homesbymarco.com/subdivisions/eagle-pointe-in-groveland-fl', 'Eagle Pointe')}, built out between 2006 and 2020, and the newer {ext('https://www.homesbymarco.com/subdivisions/green-valley-townhomes-in-groveland-fl', 'Green Valley')} townhomes sit on graded, builder-compacted lots where the native ridge sand has already been disturbed once by construction equipment. That compaction doesn't behave like undisturbed Candler sand, so a crew treats a five-year-old subdivision lot as its own case rather than assuming it drains exactly like the surrounding ridge.</p>"
             f"<p>Older lots ringing {city('groveland', 'downtown Groveland')} near Lake David or Cherry Lake carry decades of landscaping and mature trees that a newer subdivision hasn't grown into yet, which shifts the conversation toward drip-line clearance and shade rather than base compaction alone.</p>")],
        "scenario": ("A worked example: a Trilogy Orlando backyard",
                     f"<p>Say you have a 1,200 sq ft backyard behind a Trilogy Orlando villa, fenced on all four sides and currently the only square footage on the lot the community's landscaping fee doesn't cover. At Groveland's {price('residential')} range, that yard prices between roughly $9,600 and $21,600 depending on base depth and how the crew gets equipment through a villa's side gate; most jobs this size land closer to $12,000–$19,200 at the typical grade.</p>"
                     "<p>Because the lot sits on excessively drained ridge sand, the base leans toward the fuller end of the state's two-to-four-inch range less for drainage than for a firm, settled surface under a decade of foot traffic. Removing existing sod, correcting any low spot near the lanai, and capping the irrigation heads that used to reach that section all happen before turf goes down, and infill goes in last at roughly one to two pounds per square foot.</p>"),
        "faqs": [
            faq("Does a resort villa in Groveland need a different turf product than a full-size lot?",
                "Not a different product, just a smaller order. A villa backyard usually runs a few hundred square feet, which pushes the per-foot price toward the top of the range since a crew and compactor show up regardless of lot size, but the turf, base and infill specs stay identical to a larger Groveland yard."),
            faq("Will a new Groveland subdivision lot need extra base work because of construction fill?",
                "Sometimes. A lot graded within the last few years can carry compacted fill from construction traffic that behaves differently than the undisturbed ridge sand around it, so a crew checks drainage and grade on site rather than assuming a new subdivision lot matches its older neighbors."),
        ],
        "sources": SRC,
    },
    "pet": {
        "title": "Pet Turf & Dog Runs in Groveland, FL",
        "meta": "Pet turf and dog runs for Groveland yards near the Green Swamp edge and newer ridge subdivisions. Setbacks, drainage and pricing, checked September 2026.",
        "h1": "Dog runs built for Groveland's sand and setbacks",
        "lede": capsule(f"A dog run in Groveland often sits closer to a swale, a wetland buffer or a lake edge than a plain lawn would, since owners tend to carve the run along a property line, which puts the state's setback rules in play more than they would on a simple backyard job. Pet turf here prices at {price('pet')} a square foot installed, September 2026's Central Florida figure."),
        "sections": [
            ("Dog runs on rural acreage near the Green Swamp",
             f"<p>Larger, rural-feeling lots toward Groveland's western edge back up against the Green Swamp Area of Critical State Concern, and the state's turf rule draws a hard line there: synthetic turf can't go inside a drainage swale, a ditch or a wetland buffer no matter how convenient that strip looks for a dog run. A property with a septic system also needs its tank's pump-out lid mapped before any base goes in, since that access has to stay reachable once the run is finished, not buried under compacted rock.</p>"
             f"<p>None of that rules out a dog run on acreage like this; it just moves the layout a few feet in from where an owner might first picture it. {post('artificial-turf-hurricane-flooding', 'This post')} covers what a heavy storm does to a run built too close to a swale, which is the failure mode this setback is meant to prevent.</p>"),
            ("Odor control on excessively drained sand",
             "<p>Candler and Astatula soils under a Groveland yard already drain faster than almost anywhere else in Central Florida, so the argument for zeolite or a coated antimicrobial infill over plain silica in a dog run here is less about standing liquid and more about ammonia smell lingering in loose, dry sand between rinses. Skipping the weed barrier under a pet area still applies on ridge sand the same way it does anywhere else, since fabric traps urine at the surface instead of letting the base carry it away.</p>"
             f"<p>A run built without that barrier, on a base compacted the same two to four inches deep as the rest of a Groveland yard, rinses clean with a hose in a way that dense native sand alone would not. {city('montverde')} and the hillier lots toward {city('four-corners')} share enough of this ridge that the same odor-control logic carries over to both.</p>"),
            ("Fenced runs in Eagle Pointe and Green Valley",
             f"<p>A side-yard dog run in a newer subdivision like Eagle Pointe or {city('groveland', 'Groveland')}'s Green Valley townhomes usually sits behind a privacy fence, which is exactly the condition Florida's HOA-visibility statute protects: a run that can't be seen from the street or an adjacent lot gets more latitude from an association's design review than a front-yard project would. {a('/laws/hoa-rules/', 'What a Florida HOA can and cannot restrict')} goes through the statute in full.</p>"
             "<p>A narrower side yard between two townhomes also means less room to grade a fall line away from a shared fence, so a crew routes drainage toward the street or a rear common area instead of a neighbor's foundation.</p>")],
        "scenario": ("A worked example: a fenced side-yard run",
                     f"<p>Say you have a 300 sq ft side-yard dog run along an Eagle Pointe fence line, currently bare dirt because grass never held up to daily traffic there. At Groveland's {price('pet')} range, that run prices between about $3,000 and $5,400, with most owners landing near $3,600 to $4,800 once zeolite or an antimicrobial coated sand is added for odor control.</p>"
                     "<p>Because the lot sits on fast-draining ridge sand rather than flatwoods soil, the base doesn't need extra depth to handle a high water table the way a similar run might closer to Kissimmee. The weed barrier gets skipped, the base is compacted the same two to four inches deep as the rest of the yard, and the run gets graded to drain toward the side yard's low point rather than back toward the house.</p>"),
        "faqs": [
            faq("Can a dog run go inside a swale on a rural Groveland lot?",
                "No. The state's turf rule bars synthetic turf inside a drainage swale, ditch or wetland buffer regardless of how the rest of the yard is used, and that applies to a dog run the same way it applies to a full lawn. The run has to sit outside that strip even if it means a shorter run than the property line would otherwise allow."),
            faq("Does a septic system change where a dog run can go in Groveland?",
                "It changes where the run's edge lands, not whether one can be built. The tank's pump-out lid has to stay reachable once the run is finished, so the base gets built up to that spot rather than over it, and the surrounding grade gets checked separately during layout."),
        ],
        "sources": SRC,
    },
    "putting": {
        "title": "Backyard Putting Greens in Groveland, FL",
        "meta": "Backyard and chipping greens shaped into Groveland's ridge lots and resort-community yards. Contouring, setbacks and pricing, checked September 2026.",
        "h1": "Putting greens shaped into Groveland's rolling ground",
        "lede": capsule(f"The ridge terrain across this part of Lake County already carries more natural grade change than a flat Osceola County lot, which can work in a green's favor once contouring enters the plan. A backyard putting green in Groveland prices at {price('putting')} a square foot installed as of September 2026."),
        "sections": [
            ("Turning the ridge's natural slope into a green's contour",
             "<p>Most putting-green work starts by building slope into an otherwise flat yard, shaping a subbase into rolls and tiers that read as a natural green rather than a tabletop. A Groveland backyard on the sand ridge often starts with some of that grade already there, since the same rolling terrain that runs through this stretch of Lake County shows up at yard scale, not just on the road driving in.</p>"
             f"<p>That head start still needs engineering rather than a shovel and a guess: a green built straight onto an existing slope without a compacted, shaped subbase underneath will hold water in the low cups and dry out on the high side, which defeats the point of a true roll. The same terrain runs on toward {city('clermont')}, so the shaping approach that works on a Groveland lot generally transfers to a ridge yard there too. The ridge's excessively drained sand at least means the subbase isn't fighting a rising water table while that shaping happens.</p>"),
            ("Greens on 55+ resort lots and golf-adjacent living",
             f"<p>{ext('https://www.55places.com/florida/communities/trilogy-orlando', 'Trilogy Orlando')}'s clubhouse includes a golf simulator among its amenities, which points to the kind of buyer a 55+ resort community in Groveland tends to attract: someone who wants golf in daily life without necessarily wanting a full course membership. A small backyard green on a resort lot fits that pattern, sized to the villa's fenced yard rather than to a full three-hole layout.</p>"
             f"<p>{svc('putting', 'A contoured green')} on a lot this size usually gives up square footage for fringe and a chipping pad instead of a longer roll, since the whole point on a compact resort lot is fitting real practice into limited space rather than replicating a course green at scale.</p>"),
            ("Waterfront lots near Lake David and Cherry Lake",
             f"<p>A green planned for a lot backing onto {ext('https://lake.wateratlas.usf.edu/waterbodies/lakes/7968/lake-david', 'Lake David')} or {ext('https://lake.wateratlas.usf.edu/waterbodies/lakes/7842/cherry-lake', 'Cherry Lake')} has to stake the state's 10-ft waterbody setback before laying out cups or fringe, the same way a lawn conversion would, unless a seawall or bulkhead already separates the yard from the water. That staking happens first, before ordering turf, so pricing and cup placement follow the actual usable ground instead of the lot's full run to the water.</p>"
             f"<p>A shoreline lot that clears the setback often has room left for a real green despite it, since Groveland's older lake lots tend to run deep even where they're narrow at the water's edge. {post('artificial-turf-glossary', 'This glossary')} covers stimp, fringe and the other terms that come up once a green's actual dimensions get discussed.</p>")],
        "scenario": ("A worked example: a green near Cherry Lake",
                     f"<p>Say you have a 450 sq ft area at the back of a Cherry Lake lot, set at least 10 feet from the shoreline with room left over after the setback is staked. At Groveland's {price('putting')} range, a contoured green with fringe and two cups prices between about $6,300 and $13,500, with most builds landing near $8,100 to $11,250 once chipping-pad turf and cup hardware are added to the base green.</p>"
                     "<p>The subbase for a green this size takes more shaping time than a flat lawn of the same area, since rolls and a slightly raised collar around each cup have to hold their shape under years of foot traffic and Central Florida rain. On ridge sand, that shaping doesn't have to fight a rising water table the way it might closer to Kissimmee, which is one less variable in an already detailed build.</p>"),
        "faqs": [
            faq("Does Groveland's ridge terrain make a putting green cheaper to build?",
                "Not necessarily cheaper, but sometimes less invasive. A yard that already has mild grade can need less added fill to create contour than a dead-flat lot would, though the subbase still has to be shaped and compacted with the same care either way. Price depends more on green size, cup count and fringe detail than on the starting slope."),
            faq("How close to Lake David or Cherry Lake can a putting green sit?",
                "The same 10 feet the state's rule sets for any synthetic turf near a natural or man-made waterbody, unless a seawall or bulkhead already stands between the yard and the water. That line gets staked before a green's layout is finalized, not adjusted afterward."),
            faq("Do 55+ communities in Groveland allow backyard putting greens?",
                "We haven't seen a published design guideline from a specific Groveland resort community addressing synthetic greens either way, so checking the current architectural review packet before ordering one is the honest first step. Florida's HOA-visibility statute still applies underneath whatever that review asks for."),
        ],
        "sources": SRC,
    },
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
