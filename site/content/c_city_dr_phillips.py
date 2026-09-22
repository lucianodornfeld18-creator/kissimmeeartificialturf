# -*- coding: utf-8 -*-
from _helpers import page, capsule, sec, table, faq, ul, a, svc, city, cs, post, src, ext, price
from _cityservice import cityservice_pages

SLUG = "dr-phillips"

CENSUS = ("U.S. Census Bureau -- QuickFacts, Doctor Phillips CDP, Florida", "https://www.census.gov/quickfacts/fact/table/doctorphillipscdpflorida")
OC_DRP = ("Orange County Government -- Dr. Phillips, District 1 communities", "https://www.orangecountyfl.net/BoardofCommissioners/District1Commissioner/District1Communities/DrPhillips.aspx")
ORLANDO_MEMORY = ("Orlando Memory -- Dr. Philip Phillips biography", "https://orlandomemory.org/people/dr-philip-phillips/")
WATER_ATLAS = ("Orange County Water Atlas -- Butler Chain of Lakes", "https://orange.wateratlas.usf.edu/butler-chain/")
SAND_LAKE_ATLAS = ("Orange County Water Atlas -- Big Sand Lake", "https://orange.wateratlas.usf.edu/waterbodies/lakes/140008/big-sand-lake")
OFW_FACTSHEET = ("Florida DEP -- Outstanding Florida Waters fact sheet", "https://floridadep.gov/sites/default/files/ofw-factsheet.pdf")
SFWMD_WHO = ("South Florida Water Management District -- Who We Are", "https://www.sfwmd.gov/who-we-are")
OC_SETBACK = ("Orange County Code of Ordinances Sec. 38-1501 -- site and building setbacks from water bodies", "https://orangecounty-fl.elaws.us/code/cid10182/38-1501/")
OCU_WATER = ("Orange County Utilities -- watering restrictions", "https://www.orangecountyfl.net/watergarbagerecycling/wateringrestrictions.aspx")
OUC_WATER = ("OUC -- water services", "https://www.ouc.com/about/water-services/")
BAYHILL = ("Arnold Palmer's Bay Hill Club & Lodge", "https://www.bayhill.com/")
ORANGETREE = ("Orange Tree Country Club -- Our Community", "https://orangetreecc.com/about/")
PHILLIPSLANDING = ("Phillips Landing Master Community Association -- FAQs", "https://phillipslandingmaster.com/index.php/services/")
SANDLAKECOVE = ("Florida Neighborhood Realty -- Sand Lake Cove, Dr. Phillips", "https://www.floridaneighborhoodrealty.com/sand-lake-cove-dr-phillips-homes-for-sale.php")
STR_GUIDE = ("BNBCalc -- Orange County, Florida short-term rental regulation guide", "https://www.bnbcalc.com/blog/short-term-rental-regulation/orange-county-florida-guide")
SOIL_CANDLER = ("USDA NRCS -- Official Series Description, Candler series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/C/Candler.html")
SOIL_ASTATULA = ("USDA NRCS -- Official Series Description, Astatula series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/A/ASTATULA.html")
SOIL_APOPKA = ("USDA NRCS -- Official Series Description, Apopka series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/A/APOPKA.html")
ORANGE_PA = ("Orange County Property Appraiser -- parcel search", "https://ocpafl.org/")
OC_PERMIT = ("Orange County Fast Track Online Services", "https://fasttrack.ocfl.net/OnlineServices/")
RESTAURANT_ROW = ("Wheretraveler -- Restaurant Row, Orlando", "https://www.wheretraveler.com/orlando/where-eat-orlandos-famed-restaurant-row")

SRC = [CENSUS, OC_DRP, ORLANDO_MEMORY, WATER_ATLAS, SAND_LAKE_ATLAS, OFW_FACTSHEET, SFWMD_WHO, OC_SETBACK, OCU_WATER, OUC_WATER,
       BAYHILL, ORANGETREE, PHILLIPSLANDING, SANDLAKECOVE, STR_GUIDE, SOIL_CANDLER, SOIL_ASTATULA, SOIL_APOPKA, ORANGE_PA, OC_PERMIT, RESTAURANT_ROW,
       "dep-rule", "fs125572", "fs7203045"]

MILES = 12

# ============================================================== HUB
HUB = page(
    "/areas/dr-phillips/", "city",
    "Artificial Turf in Dr. Phillips, FL: Lakefront & Gated Yards",
    "Artificial turf in Dr. Phillips, FL: unincorporated Orange County permitting, the Butler Chain's shoreline rules, gated ARC review, and 2026 price ranges.",
    "Artificial turf for Dr. Phillips, Florida yards",
    capsule(f"Dr. Phillips is an unincorporated Orange County community about {MILES} miles from downtown Kissimmee, built up mostly from the 1960s through the early 2000s around the Butler Chain of Lakes and gated golf neighborhoods such as Orange Tree. As of September 2026, artificial grass here runs {price('residential')} per square foot installed, with a lakefront setback, an architectural review committee or both usually deciding how a job gets planned."),
    "".join([
        sec("What sets a Dr. Phillips yard apart",
            f"<p>Dr. Phillips is a census-designated place in southwest Orange County, sitting between International Drive and the Butler Chain of Lakes roughly {MILES} miles southwest of downtown Kissimmee. The 2020 census counted 12,328 residents here, up from 10,981 a decade earlier ({ext(CENSUS[1], CENSUS[0])}). The name comes from Dr. Philip Phillips, a Columbia-trained physician who became one of the largest citrus growers anywhere before selling his groves to Minute Maid in the 1950s; the acreage he kept became the subdivisions and golf clubs that still carry his name, among them the Bay Hill neighborhood built on the south shore of Big Sand Lake in the 1960s ({ext(OC_DRP[1], 'Orange County’s own Dr. Phillips page')}; {ext(ORLANDO_MEMORY[1], 'Orlando Memory')}).</p>"
            + f"<p>That history leaves a turf crew reading several different rulebooks on the same afternoon: a guard-gated golf community with an architectural review committee, a 1990s subdivision with a grown-in oak canopy, a lakefront lot answering to a state water-quality designation, and a storefront on {a('/commercial-turf/', 'Sand Lake Road’s restaurant corridor')} that never qualifies for the residential exemption in {a('/laws/florida-hb-683/', 'Florida’s 2025 turf law')} at all. Pricing and planning both start with which of those a given address is.</p>"),
        sec("Which office reviews your permit: Orange County or the City of Orlando?",
            f"<p>Dr. Phillips itself is unincorporated, so a synthetic turf project here goes to the county's permitting counter, the Division of Building Safety (407-836-5550), and is filed through {ext(OC_PERMIT[1], 'Fast Track Online Services')}, rather than a city hall. The county's landscape code (Chapter 24) uses the word turf to mean live grass and nothing else, and had no synthetic-turf language on the books as of September 2026, which our {a('/laws/permits/orange-county/', 'Orange County permits page')} covers in more depth.</p>"
            + f"<p>A handful of addresses that feel like Dr. Phillips, particularly near the MetroWest line, actually sit inside Orlando city limits, and Orlando is the one jurisdiction in Central Florida with a named artificial-turf code section, covered on our {a('/laws/permits/city-of-orlando/', 'City of Orlando permits page')}. Run any address through the {ext(ORANGE_PA[1], 'Orange County Property Appraiser')} parcel search before assuming which office has it; the parcel record states the taxing jurisdiction.</p>"),
        table("Dr. Phillips yard types and what we do differently",
              ["Lot", "The complication", "Our approach"],
              [["Lakefront lot on the Butler Chain", "Property backs onto an Outstanding Florida Water", "Turf stops at least 10 ft from the ordinary water line unless a seawall or bulkhead already separates the yard from the lake"],
               ["Guard-gated golf lot (Orange Tree, Phillips Landing)", "An architectural review committee signs off before work starts", "We build the ARC packet, spec sheet and sample alongside the yard plan"],
               ["Established 1990s subdivision with grown oaks (Sand Lake Cove and similar)", "Canopies planted decades ago now shade a large share of the lot", "Excavation stays outside the drip line unless a certified arborist has cleared it"],
               ["Pool cage or lanai floor on an older pool home", "Bare concrete deck, so there is no soil underneath for a normal base", "A drainage underlay glues to the slab instead of rock going into the ground"],
               ["Storefront or patio on the Sand Lake corridor", "Commercial property, so the state's single-family exemption never applies", "Orange County's own landscape code, not the DEP rule, sets the standard we build to"]],
              "Illustrative categories built from the sources on this page, not a survey of every parcel."),
        sec("The Butler Chain of Lakes and what it means for shoreline turf",
            f"<p>Thirteen interconnected lakes make up the Butler Chain, spread across more than 5,000 surface acres along Dr. Phillips' western edge, and in 1985 the chain became the first lake system in Florida named an Outstanding Florida Water for its water quality and habitat ({ext(WATER_ATLAS[1], 'Orange County Water Atlas')}; {ext(OFW_FACTSHEET[1], 'DEP’s Outstanding Florida Waters fact sheet')}). The chain drains south through Reedy Creek toward the Kissimmee River, Lake Okeechobee and the Everglades, which puts that particular drainage basin under the South Florida Water Management District rather than the St. Johns district that covers most of the rest of Orange County ({ext(SFWMD_WHO[1], 'SFWMD’s own coverage list')}).</p>"
            + f"<p>None of that changes the state's turf rule itself: {a('/laws/florida-hb-683/', 'Rule 62-308.100')} keeps synthetic turf at least 10 feet from any natural or artificial waterbody unless a seawall already stands between the yard and the water. Big Sand Lake, where the Bay Hill section sits, belongs to a separate eleven-lake Sand Lake chain that doesn't carry the Butler Chain's Outstanding Florida Water status ({ext(SAND_LAKE_ATLAS[1], 'Big Sand Lake, Orange County Water Atlas')}), but it still counts as a waterbody for that same 10-foot rule. Orange County's zoning code sets its own 50-foot building setback from a lake's normal high water line, a number the county fixed at 99.5 feet above sea level for the Butler Chain specifically, though that figure governs structures, not landscaping ({ext(OC_SETBACK[1], 'Orange County Code Sec. 38-1501')}).</p>"),
        sec("Gated communities, HOAs and the ARC process",
            f"<p>Orange Tree Country Club is a guard-gated enclave of more than 600 custom homes built between 1976 and 1993 around a golf course laid out by Joe Lee in 1972, with a recreation center on Lake Marsha ({ext(ORANGETREE[1], 'Orange Tree Country Club')}). Phillips Landing runs its own master community association, and its published FAQ tells homeowners that material modifications to the landscape go through an architectural review process before work starts, without spelling out a turf-specific clause ({ext(PHILLIPSLANDING[1], 'Phillips Landing FAQs')}). Sand Lake Cove, by contrast, is a non-gated run of 214 homes built mostly from 1996 to 1999 off South Apopka-Vineland Road, with a mandatory HOA but no shared amenities of its own ({ext(SANDLAKECOVE[1], 'Sand Lake Cove, Dr. Phillips')}).</p>"
            + f"<p>Under {a('/laws/hoa-rules/', 'F.S. 720.3045')}, none of those associations can block turf an outsider can't see from the street or a neighboring lot, but a front yard or a lake-facing rear yard on a golf hole is a different story, and most gated Dr. Phillips communities run design review regardless. Our {a('/tools/hoa-packet-checklist/', 'HOA packet checklist')} lists what a typical ARC submittal wants before it approves anything.</p>"),
        sec("Water, soil and what's under the grass",
            f"<p>Orange County Utilities runs the water and irrigation schedule for most unincorporated Dr. Phillips addresses: two days a week from March 8 through October 31 (odd addresses Wednesday and Saturday, even Thursday and Sunday), one day a week the rest of the year, and no watering between 10 a.m. and 4 p.m. either way ({ext(OCU_WATER[1], 'Orange County Utilities watering restrictions')}). A pocket of addresses near the Orlando line can be billed by the Orlando Utilities Commission instead, which sets its own schedule, so a recent water bill settles which one applies faster than guessing ({ext(OUC_WATER[1], 'OUC water services')}).</p>"
            + f"<p>The ridge soils under most of southwest Orange County run to Candler and Apopka fine sands, excessively to well drained and rapidly permeable, with pockets of the even faster-draining Astatula series closer to the lake shores ({ext(SOIL_CANDLER[1], 'USDA Candler series')}; {ext(SOIL_APOPKA[1], 'USDA Apopka series')}; {ext(SOIL_ASTATULA[1], 'USDA Astatula series')}). That native sand already drains fast; a washed, open-graded crushed-rock base keeps it that way once turf goes on top, which our {svc('residential', 'residential installation page')} covers in more detail.</p>"),
        sec("Short-term rentals: a small slice of the Dr. Phillips market",
            f"<p>Orange County's zoning code, Chapter 38, prohibits short-term and single-family transient rental in standard R-1 and R-2 residential districts outright; legal nightly rentals concentrate instead in Planned Developments and a few commercial or R-3 parcels clustered near Walt Disney World and the US-192 corridor ({ext(STR_GUIDE[1], 'Orange County short-term rental zoning guide')}). Dr. Phillips' established subdivisions, from Orange Tree to Sand Lake Cove, sit in ordinary residential zoning rather than that overlay, so {a('/vacation-rental-turf/', 'vacation-rental turf')} is a smaller share of the work here than it is closer to the theme parks.</p>"
            + f"<p>That doesn't mean it never comes up. A long-term furnished rental near Restaurant Row still deals with guest turnover and a yard nobody's watering carefully, which is the case our {a('/vacation-rental-turf/dr-phillips/', 'vacation rental turf page')} makes.</p>"),
        sec("Getting turf approved before a crew shows up",
            f"<p>Three approvals can apply to the same Dr. Phillips project and none of them substitute for another: {a('/laws/permits/orange-county/', 'Orange County’s permitting office')} for the county's own drainage and land-alteration rules, an association's {a('/laws/hoa-rules/', 'ARC or design review')} where one exists, and the floor {a('/laws/florida-hb-683/', 'set statewide by HB 683 and Rule 62-308.100')} since May 19, 2026 for a covered single-family lot of an acre or less. Our {a('/tools/hoa-packet-checklist/', 'HOA packet checklist')} walks through what most Orange County associations ask an ARC submittal to include: a sample, a spec sheet, a site plan and a drainage note.</p>"),
    ]) + "<!--AUTO:city-services-->",
    faqs=[
        faq("What's the best artificial turf installer near me in Dr. Phillips?", "Ask three things: a written measurement of the square footage, the base depth and material spelled out (washed crushed rock or crushed concrete, not fill dirt), and whether the estimate accounts for an HOA submittal if your community requires one. Two quotes with those three answered are easy to compare; two that just say \"premium turf, installed\" aren't."),
        faq("Is Dr. Phillips in the City of Orlando or unincorporated Orange County?", "Mostly unincorporated Orange County, but a strip near the Orlando city line can go either way depending on the parcel. Run the address through the Orange County Property Appraiser's site to see the taxing jurisdiction before assuming which permitting office applies."),
        faq("Does my lot on the Butler Chain need a special permit for turf?", "The state's turf rule applies the same 10-foot waterbody setback here as anywhere else, seawall exception included; we found no Orange County ordinance that adds a stricter turf-specific buffer on top of that for the Butler Chain as of September 2026. A structure, unlike turf, does answer to the county's own 50-foot setback from the chain's normal high water line."),
        faq("Do Orange Tree or Phillips Landing require turf to be pre-approved?", "Both run an architectural review process for exterior landscape changes, based on their own published materials, though neither has posted turf-specific language we could find. Submit a sample and a site plan before ordering material, the same way you would for a fence or a paver patio."),
        faq("Is short-term rental turf a big part of the Dr. Phillips market?", "Not really. Orange County's zoning keeps nightly rentals mostly out of standard residential districts like the ones Dr. Phillips is built from, concentrating that use instead in Planned Developments near Disney and US-192, so this work is a smaller slice of what we do here than in the tourist corridor."),
    ],
    sources=SRC, city=SLUG, crumbs=[("Service areas", "/areas/")], crumb="Dr. Phillips",
    related=[("/laws/permits/orange-county/", "Orange County artificial turf permits"), ("/laws/permits/city-of-orlando/", "City of Orlando artificial turf permits"),
             ("/laws/hoa-rules/", "What a Florida HOA can and can't restrict"), ("/tools/hoa-packet-checklist/", "HOA / ARC packet checklist"),
             ("/areas/windermere/", "Turf in Windermere"), ("/areas/hunters-creek/", "Turf in Hunters Creek"), ("/areas/orlando/", "Turf installers in Orlando"), ("/areas/celebration/", "Turf in Celebration"), ("/areas/kissimmee/", "Artificial turf in Kissimmee"),
             ("/artificial-turf-cost/", "Turf cost tables for Central Florida")],
)

LOCAL = {}

# ---------------------------------------------------------------- residential
LOCAL["residential"] = {
    "title": "Artificial Grass Installation in Dr. Phillips, FL",
    "meta": "Artificial grass installation in Dr. Phillips, FL: ARC review at Orange Tree and Phillips Landing, oak drip lines, and sandy ridge soil, priced for 2026.",
    "h1": "Artificial grass for Dr. Phillips lawns",
    "lede": capsule(f"A Dr. Phillips lawn conversion runs {price('residential')} per square foot installed as of September 2026, typically {price('residential', True)}, with most of that range set by lot size and access rather than which subdivision the house sits in. Gated communities such as Orange Tree add an architectural review step; older lots under grown oaks add a drip-line boundary to work around."),
    "sections": [
        ("Getting a lawn past Orange Tree or Phillips Landing's design review",
         f"<p>Orange Tree Country Club has run guard-gated architectural review since its first phase went in during 1976, and Phillips Landing's master association tells homeowners that material landscape changes go through an ARC process before anyone breaks ground. Neither community has posted a turf-specific clause we could find, which means a submittal package does the talking: a physical sample, the product's spec sheet, and a site plan showing where the new surface replaces sod.</p>"
         + f"<p>That review adds a week or two to the schedule on top of the install itself, so a homeowner in either community is better off submitting before ordering material than after. See {a('/tools/hoa-packet-checklist/', 'what a typical Orange County ARC packet wants')} for the checklist we work from.</p>"),
        ("Working around oaks planted when these lots were new",
         f"<p>Orange Tree's original phase is nearly 50 years old and Sand Lake Cove's homes went up mostly between 1996 and 1999, long enough for the live oaks planted with those subdivisions to reach full canopy over a meaningful share of the lot. Florida's turf standard keeps installation outside a tree's drip line, whether the trunk stands on your side of the fence or the neighbor's, until a certified arborist puts in writing that the work won't hurt the root system.</p>"
         + f"<p>On a lot where the shade already keeps grass thin, that boundary usually still leaves plenty of sunnier lawn to convert. {post('artificial-turf-near-live-oaks-and-palms', 'This article walks through how we map a drip line before digging')}.</p>"),
        ("What the ridge sand under a Dr. Phillips lawn is doing",
         f"<p>Southwest Orange County sits on Candler and Apopka fine sands, both excessively to well drained and fast-percolating on their own, the same ridge soil that made this corridor good citrus ground before it was residential. A washed, open-graded crushed-rock base doesn't need to fight standing water here the way it might on flatter, tighter clay; it mostly needs to stay level and compacted so the lawn doesn't develop low spots after a summer storm.</p>"
         + f"<p>Near the lake shore the soil shifts toward the even sandier Astatula series, which drains faster still. Either way, capping the irrigation heads under the new turf, required by the state standard, matters more for the water bill than for drainage on this ground.</p>"),
    ],
    "scenario": ("A typical Dr. Phillips lawn conversion, worked out",
                 f"<p>Say a homeowner off Apopka-Vineland Road has an 1,100 sq ft front and side yard, mostly thinned-out St. Augustine under a stand of oaks planted when the subdivision was new in the late 1990s. Roughly 150 sq ft of that sits inside the canopy's drip line, so the plan turfs the remaining 950 sq ft and leaves mulch under the trees rather than pursuing an arborist letter for a small gain.</p>"
                 + f"<p>At the typical {price('residential', True)} range, 950 sq ft runs about $9,500 to $15,200 installed, including sod removal, a compacted rock base, turf, seams and edging. Because the lot sits inside a gated community, the schedule also has to account for an ARC submittal before the crew is booked, which the homeowner starts the same week as getting the quote rather than after.</p>"),
    "faqs": [
        faq("How do I find the best artificial grass installer near Orange Tree or Phillips Landing?", "Ask whether the quote already accounts for a design-review submittal and how long that adds to the schedule. An installer who's done work inside a Dr. Phillips ARC community before can usually estimate the review timeline; one who hasn't should still budget the extra week or two rather than promise a start date that skips it."),
        faq("Do I need a permit from Orange County for a backyard lawn swap in Dr. Phillips?", "As of September 2026, Orange County's landscape code doesn't name synthetic turf specifically, and the county hasn't published a stated permit answer for a residential lawn conversion. Capping irrigation heads can trigger its own plumbing review; call Permitting Services at 407-836-5550 to confirm for your address."),
        faq("Does a Dr. Phillips lawn cost more than one in Kissimmee?", "No. Material and labor price the same across Central Florida; what changes here is gate access for equipment, an ARC submittal in some communities, and whether oak roots limit how much of the lot qualifies."),
    ],
    "sources": [CENSUS, ORANGETREE, PHILLIPSLANDING, SANDLAKECOVE, SOIL_CANDLER, SOIL_APOPKA, "dep-rule"],
}

# ---------------------------------------------------------------- pet
LOCAL["pet"] = {
    "title": "Pet Turf & Dog Runs in Dr. Phillips, FL",
    "meta": "Pet turf and dog runs in Dr. Phillips, FL: fast-draining ridge sand, side-yard layouts near Sand Lake Cove, and 2026 market pricing by square foot.",
    "h1": "Pet turf for Dr. Phillips dog owners",
    "lede": capsule(f"Pet turf in Dr. Phillips runs {price('pet')} per square foot installed as of September 2026, typically {price('pet', True)}, and the sandy ridge ground under most of the community already drains faster than the turf sitting on top of it. The main local variables are lot width in the older non-gated subdivisions and how close a run sits to a lake's 10-foot setback."),
    "sections": [
        ("Why Astatula and Candler sand help a dog run more than it hurts",
         f"<p>The USDA describes the Astatula series, common closer to the Butler and Sand Lake shorelines, as excessively drained and very rapidly permeable, while the Candler series that covers most of the higher ground runs nearly as fast. For a dog run, where urine and rinse water need somewhere to go quickly, that native sand is doing half the work before any rock base goes down.</p>"
         + f"<p>The trade-off is that a weed barrier under pet turf, which holds odor against the fibers, matters more here than the base depth does. We skip the barrier on pet installs and let the sand keep draining the way it already does.</p>"),
        ("Side-yard runs in Sand Lake Cove and similar 1990s subdivisions",
         f"<p>Sand Lake Cove's 214 homes, built mostly from 1996 to 1999 off South Apopka-Vineland Road, sit on standard suburban lots rather than a golf-course footprint, which usually means a side yard 8 to 12 feet wide between the house and a privacy fence. That width is enough for a dog run without eating into the main lawn, and it's narrow enough that wheelbarrow access, not a skid steer, is how material gets back there.</p>"
         + f"<p>{post('pet-turf-vs-regular-artificial-grass', 'What separates pet turf from a standard lawn product')} matters more in a run this size, since every square foot of it takes daily traffic rather than the occasional path across a bigger yard.</p>"),
        ("Keeping a run outside the Butler Chain's 10-foot line",
         f"<p>A handful of Dr. Phillips lots back directly onto Butler Chain water, and a dog run tucked along the rear property line has to respect the same 10-foot setback from the ordinary water line that applies to any turf on the lot, seawall exception included. That's rarely a real constraint on a standard-depth lot, but on a narrower waterfront parcel it can push a run toward the side yard instead of straight back toward the water.</p>"
         + f"<p>Where the setback does bite, zeolite or a coated-sand infill closer to the fence line still keeps odor down without needing extra footage near the shoreline.</p>"),
    ],
    "scenario": ("Sizing a dog run off Apopka-Vineland Road",
                 f"<p>Say a couple near Sand Lake Cove has two mid-size dogs and wants a 350 sq ft run down the side yard, from the gate to the back corner, replacing a strip of St. Augustine that never fully recovers between rinses. At the typical {price('pet', True)} range, that run prices around $4,200 to $5,600 installed, including a zeolite or coated-sand infill sized for daily use.</p>"
                 + f"<p>Because the lot sits well back from any lake, there's no setback math to do; the limiting factor is the side yard's actual width, measured gate to fence, which usually comes in a foot or two narrower than a homeowner expects once the AC pad and a hose bib are subtracted.</p>"),
    "faqs": [
        faq("What should I ask to find the best pet turf company near Sand Lake Cove?", "Ask what infill they use and why. Standard silica doesn't fight odor; zeolite or a coated antimicrobial sand does, and either is the difference between a run that smells fine after a hose-down and one that doesn't."),
        faq("Does pet turf need a deeper base than a regular lawn in Dr. Phillips?", "Not on this ground. The ridge sand already drains fast, so the base depth for pet turf matches a standard lawn; what changes is skipping the weed barrier and choosing an odor-control infill."),
        faq("Can I put a dog run right up to a Butler Chain lake?", "Not quite to the water. The state's synthetic turf standard keeps any turf, including a pet run, at least 10 feet from the ordinary water line unless a seawall already separates the yard from the lake."),
    ],
    "sources": [SOIL_ASTATULA, SOIL_CANDLER, SANDLAKECOVE, WATER_ATLAS, "dep-rule"],
}

# ---------------------------------------------------------------- putting
LOCAL["putting"] = {
    "title": "Backyard Putting Greens Near Bay Hill, Dr. Phillips",
    "meta": "Backyard putting greens in Dr. Phillips, FL near Bay Hill and Orange Tree: contouring, chipping pads and 2026 pricing by square foot.",
    "h1": "Putting greens for Dr. Phillips golf-community lots",
    "lede": capsule(f"A backyard putting green in Dr. Phillips costs {price('putting')} per square foot installed as of September 2026, typically {price('putting', True)}, depending on contouring, fringe and how many cups the design carries. Living near Bay Hill and Orange Tree means plenty of golfers asking for one, on lots that usually have the room a real green needs."),
    "sections": [
        ("What Bay Hill's golf heritage means for demand here, not price",
         f"<p>Bay Hill Club & Lodge sits on the south shore of Big Sand Lake in the neighborhood that gave the area its name, and Arnold Palmer owned the club from the mid-1970s until his death in 2016; it still hosts the PGA Tour's Arnold Palmer Invitational each spring. None of that changes what a backyard green costs, since the market range holds the same whether a lot is three minutes from the course or across the county, but it does mean a lot of Dr. Phillips homeowners already know exactly what a good roll feels like before they call.</p>"
         + f"<p>That familiarity shows up as more specific requests: a particular stimp speed, a false-front contour, a chipping pad at a set distance, rather than a general request for something for the backyard.</p>"),
        ("Building a green on an Orange Tree golf-course lot",
         f"<p>Orange Tree's golf course, designed by Joe Lee in 1972, borders many of the community's more than 600 homes directly, and a lot backing onto a fairway usually has the open, level rear yard a contoured green needs without much regrading. The main design question on those lots is sightlines: keeping a green's slope and cup placement from putting a stray shot toward the course itself.</p>"
         + f"<p>{post('backyard-putting-green-cost-florida', 'What drives the price of a green up or down')} applies here the same as anywhere, with fringe turf, cup count and contouring doing most of the work.</p>"),
        ("Sizing a green on a standard, non-golf lot",
         f"<p>Not every Dr. Phillips putting green sits on a golf-course lot. Sand Lake Cove and similar subdivisions built through the late 1990s have deeper backyards than a zero-lot-line home, typically enough for a modest green with a short chipping approach even without course frontage. The build itself doesn't change: contoured shaping under the turf, a firmer, lower-nap product than a residential lawn, and real cups rather than a flat mat.</p>"
         + f"<p>{svc('putting', 'The putting green service page')} covers the shaping and product choice in more detail than fits here.</p>"),
    ],
    "scenario": ("A green sized for a fairway-facing yard",
                 f"<p>Say a homeowner on an Orange Tree golf lot wants a 500 sq ft green with two cups, a false-front slope and a small chipping pad off to one side, replacing a flat stretch of Bahia that never held up to foot traffic anyway. At the typical {price('putting', True)} range, that project runs roughly $9,000 to $12,500 installed, with the contouring and fringe turf accounting for most of the gap above a flat lawn's per-foot price.</p>"
                 + f"<p>Because the lot backs the course, no ARC-adjacent sightline issue applies here beyond the usual submittal; the design just keeps the slope facing the house rather than the fairway.</p>"),
    "faqs": [
        faq("Do I need a bigger budget for a green near Bay Hill than elsewhere in Florida?", "No, the market range doesn't change by neighborhood. A Dr. Phillips green costs the same per square foot as one in Kissimmee; what changes the total is size, contouring and how many cups the design carries."),
        faq("Can a putting green go right up to an Orange Tree fairway?", "There's no state or county setback between residential turf and a golf course itself, unlike the 10-foot lake rule. The practical limit is usually the community's own rear-yard setback for the house lot, not anything specific to turf."),
        faq("Does a putting green need the same base as a regular lawn?", "The excavation goes deeper in spots to build the contours, but the underlying principle is the same washed, open-graded crushed rock the state standard requires everywhere else, just shaped rather than left flat."),
    ],
    "sources": [BAYHILL, ORANGETREE, SANDLAKECOVE],
}

# ---------------------------------------------------------------- playground
LOCAL["playground"] = {
    "title": "Playground Turf for Dr. Phillips Families",
    "meta": "Playground turf in Dr. Phillips, FL: shock pad sizing for swing sets and play structures near Dr. P. Phillips Community Park, priced for 2026.",
    "h1": "Playground turf for Dr. Phillips backyards",
    "lede": capsule(f"Playground turf in Dr. Phillips runs {price('playground')} per square foot installed as of September 2026, typically {price('playground', True)}, with the shock pad thickness set by the fall height of whatever equipment sits on top. Families here often measure a home swing set against the county park nearby, which sets expectations for how soft the surface ought to feel."),
    "sections": [
        ("A 43-acre county park as the local reference point",
         f"<p>Dr. Phillips Community Park, a 43-acre county facility on Big Sand Lake, gives the area a public playground most families already know, complete with a splash pad and play structures on cushioned surfacing. Homeowners bringing that expectation to a backyard install usually want a similar fall-height-rated shock pad under a home swing set or slide, not the thinner cushioning that works fine under an open lawn.</p>"
         + f"<p>{post('is-artificial-turf-safe-for-kids-pfas-lead', 'What the state material standard actually requires for a play surface')} is worth reading before comparing quotes, since infill choice under equipment is more tightly regulated than it is on the rest of the lawn.</p>"),
        ("Fitting a play area into a 1990s-subdivision backyard",
         f"<p>Sand Lake Cove's homes, built mostly between 1996 and 1999, sit on lots sized for a family yard rather than a golf frontage, which usually leaves enough flat rear lawn for a play structure without crowding a pool cage or a fence line. Where an oak canopy from the same era shades part of the yard, keeping the play area outside the drip line, the same rule that applies to any turf near a mature tree, is worth settling before ordering equipment.</p>"
         + f"<p>A shaded play area also runs cooler underfoot in summer, which matters more for bare feet on a swing-set surface than it does on a lawn nobody sits on.</p>"),
        ("Why infill under the swing set is a separate decision from the rest of the yard",
         f"<p>Florida's turf standard limits infill on a single-family lot to clean silica sand, zeolite, coated sand or other natural material everywhere except directly under playground equipment, where a rubber or synthetic fill is allowed within that footprint specifically. That line matters on a Dr. Phillips lot that's turfing both a play area and the surrounding lawn in one job, since the two zones can legally carry different infill even though they're one continuous surface to the eye.</p>"
         + f"<p>{svc('playground', 'The playground turf service page')} breaks down shock-pad sizing by fall height in more detail.</p>"),
    ],
    "scenario": ("Sizing a play area behind a Sand Lake Cove home",
                 f"<p>Say a family off South Apopka-Vineland Road wants 300 sq ft of playground turf under a swing set and a small slide, with a shock pad rated for a 6-foot fall height, plus another 200 sq ft of standard lawn turf around it to tie the yard together. At the typical {price('playground', True)} range for the play area, that portion runs about $3,600 to $5,700 installed, with the surrounding lawn priced separately at the standard residential range.</p>"
                 + f"<p>Because the oaks on this particular lot sit along the side property line rather than over the play area, no drip-line adjustment is needed here, though that's worth checking on any lot with a mature canopy before finalizing equipment placement.</p>"),
    "faqs": [
        faq("Does Dr. Phillips Community Park set the standard for a home play surface?", "Not officially, but it's the reference point a lot of local families use. A backyard shock pad sized to the actual equipment's fall height, the same principle the park's own surfacing follows, is what the state material standard expects regardless."),
        faq("Can I use rubber infill under a swing set but sand everywhere else in the yard?", "Yes. The state standard allows rubber or another synthetic infill only within the footprint of playground equipment; the rest of a single-family lot stays limited to silica sand, zeolite, or coated sand with a non-toxic coating."),
        faq("Does a shaded play area near an oak need special permission?", "Only if the equipment or excavation falls inside the tree's drip line. A play area positioned outside that boundary doesn't need an arborist's letter; one that overlaps it does."),
    ],
    "sources": [OC_DRP, SANDLAKECOVE, "dep-rule"],
}

# ---------------------------------------------------------------- pool
LOCAL["pool"] = {
    "title": "Pool & Lanai Turf on Dr. Phillips Lakefront Estates",
    "meta": "Pool and lanai turf in Dr. Phillips, FL: the Butler Chain's 10-ft setback, Orange County's 50-ft structure line, and 2026 pricing by square foot.",
    "h1": "Pool and lanai turf for Dr. Phillips lake homes",
    "lede": capsule(f"Pool and lanai turf in Dr. Phillips prices in the {price('residential')} residential range, typically the upper half of {price('residential', True)}, as of September 2026. Lakefront pool cages here carry an extra wrinkle most yards don't: a state 10-foot waterline setback that runs alongside, not instead of, Orange County's own 50-foot building line from the shore."),
    "sections": [
        ("Two different setbacks on the same Butler Chain lot",
         f"<p>Orange County's zoning code sets a 50-foot minimum setback for a principal structure from a lake's normal high water line, a figure the county fixed at 99.5 feet above sea level for the Butler Chain specifically. That number governs where the pool cage itself can sit, decided when the house and screen enclosure were permitted. The state's synthetic turf standard is a separate, later rule: it keeps turf at least 10 feet from the ordinary water line, seawall or bulkhead excepted, and it applies to landscaping inside that structure setback, not to the building itself.</p>"
         + f"<p>In practice, a pool cage already sitting inside the 50-foot structure line rarely leaves much yard between the enclosure and the water anyway, so the 10-foot turf setback usually applies to whatever open border sits between the cage and the seawall, not the screened area itself.</p>"),
        ("Where a seawall changes the math",
         f"<p>A fair share of Butler Chain lots, particularly on Lake Down, Lake Tibet-Butler and Lake Chase, have a seawall or bulkhead already separating the yard from open water, which is exactly the exception the state rule carves out: turf can run to a hard shoreline barrier with no 10-foot buffer required. A lot without one, backing onto a natural sand or vegetated shoreline instead, keeps the full setback.</p>"
         + f"<p>Either way, {post('install-artificial-turf-over-concrete-pavers-or-grass', 'turf over an existing pool deck or paver border')} still needs to drain toward whatever outlet the deck already uses, seawall or not.</p>"),
        ("Big Sand Lake homes near Bay Hill answer to the same 10-foot rule, minus the OFW label",
         f"<p>The Bay Hill neighborhood sits on Big Sand Lake, part of a separate Sand Lake chain that doesn't carry the Butler Chain's Outstanding Florida Water designation. That distinction affects water-quality oversight generally, not the turf setback specifically: a pool-area yard on Big Sand Lake still keeps turf 10 feet from the water absent a seawall, the identical number that applies on Lake Down or Lake Sheen.</p>"
         + f"<p>{svc('pool', 'The pool and lanai turf service page')} covers the drainage underlay a glued lanai floor needs, separate from an open border's rock base.</p>"),
    ],
    "scenario": ("Turfing a lakefront pool deck border",
                 f"<p>Say a home on Lake Tibet-Butler has a screened pool cage with a seawall already at the property line, plus a 260 sq ft open border between the cage and a side fence that isn't screened. Because the seawall separates the yard from the water, no 10-foot setback applies to that border strip; at the upper end of the typical {price('residential', True)} range for pool-area turf, 260 sq ft runs roughly $3,900 to $4,700 installed.</p>"
                 + f"<p>If the same lot had no seawall, the open border would need to start at least 10 feet back from the ordinary water line instead, which on a narrower lot can shrink the turfed area meaningfully before pricing even comes into it.</p>"),
    "faqs": [
        faq("How do you choose the best pool turf contractor near the Butler Chain?", "Ask whether they measure the setback from the actual ordinary water line or just eyeball it, and whether they check for a seawall before quoting the layout. That single check changes how much of a lakefront border can legally be turfed."),
        faq("Does Orange County's 50-foot lake setback apply to turf itself?", "No. That figure governs where a principal structure like the pool cage sits; it isn't a landscaping rule. The turf-specific setback is the state's separate 10-foot rule, measured from the water line to the edge of the synthetic surface."),
        faq("Is Big Sand Lake regulated the same as the Butler Chain for turf?", "For the turf setback, yes; both are waterbodies under the state's 10-foot rule. Big Sand Lake just doesn't carry the Outstanding Florida Water designation the Butler Chain has held since 1985, which is a separate water-quality classification."),
    ],
    "sources": [OC_SETBACK, WATER_ATLAS, SAND_LAKE_ATLAS, OFW_FACTSHEET, BAYHILL, "dep-rule"],
}

# ---------------------------------------------------------------- str
LOCAL["str"] = {
    "title": "Vacation Rental Turf in Dr. Phillips, FL",
    "meta": "Vacation rental turf in Dr. Phillips, FL: Orange County zoning limits on short-term rentals and 2026 pricing for guest-proof yards between bookings.",
    "h1": "Turf for Dr. Phillips vacation rentals",
    "lede": capsule(f"Vacation rental turf in Dr. Phillips prices in the {price('residential')} residential range as of September 2026. Because Orange County's zoning keeps whole-home nightly rental out of the standard subdivisions Dr. Phillips is built from, this is a smaller part of the local market than it is in the resort corridor closer to Disney."),
    "sections": [
        ("Why Dr. Phillips sees less nightly-rental turf than nearby corridors",
         f"<p>Orange County's zoning code, Chapter 38, prohibits short-term and single-family transient rental outright in standard R-1 and R-2 residential districts, which is what most of Dr. Phillips, from Orange Tree to Sand Lake Cove, is zoned. Legal nightly rentals concentrate instead in Planned Developments and a narrow band of commercial and R-3 parcels clustered near Walt Disney World and the US-192 corridor, well south of here.</p>"
         + f"<p>That doesn't eliminate demand entirely. Furnished, longer-stay rentals and corporate housing near Restaurant Row still turn over between tenants, and a yard that needs to look presentable without weekly mowing fits that pattern even outside a licensed nightly-rental zone.</p>"),
        ("What guest turnover does to a yard even without nightly stays",
         f"<p>A furnished rental near the Sand Lake Road corridor, leased by the month rather than the night, still sees a different pattern of yard use than an owner-occupied home: nobody's watering on a fixed schedule, and a landscaper hired between tenants doesn't always match the last one's care. Turf removes the two things that suffer most from that gap, mowing and irrigation, without requiring the property to sit in a zoning district built for nightly turnover.</p>"
         + f"<p>{post('artificial-turf-vs-sod-cost-florida', 'The ten-year cost comparison against sod')} matters more for a rental than an owner-occupied home, since a rental's upkeep budget usually has to be predictable rather than flexible.</p>"),
        ("If a property does sit in a rental-zoned pocket",
         f"<p>A small number of parcels at the edges of Dr. Phillips' broader zip codes fall inside Orange County's vacation-home zoning rather than standard residential, and a nightly rental there deals with faster turf wear from back-to-back guest turnover than an owner-occupied yard ever would. {post('best-time-of-year-to-install-artificial-turf-florida', 'Scheduling installation around the booking calendar')}, rather than during a run of reservations, avoids losing rental days to construction.</p>"
         + f"<p>{svc('str', 'The vacation rental turf service page')} covers the guest-proofing details, from infill choice to edge anchoring, that matter most for a property that turns over often.</p>"),
    ],
    "scenario": ("Turfing a furnished rental's backyard between tenants",
                 f"<p>Say a furnished monthly rental near Restaurant Row has a 280 sq ft backyard that's gone patchy from irregular watering between tenants and an HOA notice about the lawn's condition. At the typical {price('residential', True)} range, that job runs about $2,800 to $4,500 installed, a cost the owner can weigh against a landscaper's monthly bill and the risk of another HOA letter.</p>"
                 + f"<p>Because the property sits in standard residential zoning rather than a nightly-rental district, there's no additional zoning review tied to the turf itself, just the same permitting questions any Dr. Phillips lawn conversion runs into.</p>"),
    "faqs": [
        faq("Can I run a nightly Airbnb from a house in Dr. Phillips?", "Generally not under Orange County's current zoning, which reserves nightly and short-term rental for Planned Developments and a few commercial or R-3 parcels near Disney and US-192. Standard Dr. Phillips subdivisions are zoned R-1 or R-2, where that use is prohibited."),
        faq("Does turf help a monthly furnished rental even without nightly guests?", "Yes. The upkeep problem, irregular mowing and watering between tenants, isn't specific to nightly stays. A monthly or corporate rental sees the same pattern and gets the same benefit from removing the lawn-care variable."),
        faq("Is vacation rental turf priced differently than a regular lawn?", "No, it uses the same residential market range. What changes for a rental is how the job gets scheduled, usually between bookings or tenants, not the per-square-foot price."),
    ],
    "sources": [STR_GUIDE, RESTAURANT_ROW],
}

# ---------------------------------------------------------------- commercial
LOCAL["commercial"] = {
    "title": "Commercial Turf Along Dr. Phillips' Sand Lake Corridor",
    "meta": "Commercial artificial turf in Dr. Phillips, FL along Sand Lake Road's Restaurant Row: patios, storefronts and Orange County's landscape code, 2026.",
    "h1": "Commercial turf for the Sand Lake corridor",
    "lede": capsule("Commercial turf in Dr. Phillips gets priced after we walk the site or read the drawings; there's no flat per-foot rate for it. Sand Lake Road's restaurant and office corridor, known locally as Restaurant Row, is the busiest stretch of commercial property in the area, and it answers to Orange County's landscape code rather than the state's single-family turf exemption."),
    "sections": [
        ("Why Restaurant Row doesn't get the residential exemption",
         f"<p>West Sand Lake Road between Dr. Phillips Boulevard and International Drive carries more than 150 restaurants and a run of offices and retail, the stretch everyone in the area calls Restaurant Row. Florida's HB 683 and Rule 62-308.100 apply only to single-family residential lots of one acre or less, so a restaurant patio, an office courtyard or a shopping-center island along this corridor never qualifies; Orange County's own landscape code, {a('/laws/permits/orange-county/', 'Chapter 24')}, is the only standard that applies, and it defines turf as living grass species without a synthetic-turf section.</p>"
         + f"<p>That gap cuts both ways: no state floor protects a commercial turf installation from a stricter local requirement, but there's also no named local ban to work around, just the county's ordinary permitting for the property.</p>"),
        ("Patios, entries and pet-relief areas on a busy retail street",
         f"<p>A restaurant patio or a retail entry along Sand Lake Road gets more foot traffic in an evening than most residential lawns see in a month, which changes the product spec more than the base underneath it: a tighter, denser face weight holds up to that traffic better than a residential-grade blade. Office parks along the corridor increasingly add a small pet-relief turf area near the parking structure, a use {a('/commercial-turf/', 'commercial properties')} ask for more often than a homeowner does.</p>"
         + f"<p>{post('how-to-compare-artificial-turf-quotes', 'Comparing commercial quotes')} works the same way it does for a residential job: base depth, product spec and anchoring method, spelled out rather than assumed.</p>"),
        ("Parking islands and landscape strips under the county's grass-species rule",
         f"<p>Orange County Chapter 24 requires landscape strips of a minimum width and interior vehicle-use-area buffers to carry living plant material, defined by species list, not a manufactured surface. Because the code's definition of turf doesn't include synthetic products either way, a property considering turf in one of those required strips needs a direct answer from Orange County Zoning before committing to the design, not an assumption either direction.</p>"
         + f"<p>Outside those specific buffer requirements, an entry courtyard or a non-vehicle-use patio has more flexibility, which is where most commercial turf on this corridor actually goes in.</p>"),
    ],
    "scenario": ("Turfing a restaurant's outdoor seating area",
                 f"<p>Say a restaurant along Sand Lake Road wants 900 sq ft of turf for an outdoor seating extension, replacing a gravel patch that tracks dust into the dining room on windy afternoons. Because commercial work is quoted from a site walk and a drawing set rather than a flat per-foot rate, pricing depends on the base condition under the gravel, the anchoring method for a high-traffic surface, and any drainage tie-in to the property's existing stormwater system.</p>"
                 + f"<p>A project like this usually needs a scaled site plan submitted with the Orange County application, since it touches an existing commercial site plan rather than a simple residential lawn swap.</p>"),
    "faqs": [
        faq("Who's the best commercial turf contractor near Restaurant Row on Sand Lake Road?", "Look for one who can point to the specific Orange County code section their design follows, since Chapter 24's landscape strip and buffer rules apply to commercial sites in a way the state's residential turf rule never does."),
        faq("Does the state's 2026 turf standard cover a Dr. Phillips restaurant patio?", "No. Rule 62-308.100 is limited to single-family residential lots of one acre or less. A commercial property along Sand Lake Road answers only to Orange County's own landscape code."),
        faq("Can turf go inside a required landscape buffer on a commercial lot?", "Orange County's Chapter 24 defines the required buffer plantings as living grass species by name, so a synthetic product's status there isn't addressed either way in the published code. Confirm directly with Orange County Zoning before designing around one."),
    ],
    "sources": [RESTAURANT_ROW, OC_DRP],
}

# ---------------------------------------------------------------- sports
LOCAL["sports"] = {
    "title": "Sports & Fitness Turf for Dr. Phillips Estate Lots",
    "meta": "Sports and fitness turf in Dr. Phillips, FL: bocce courts, batting cages and home-gym sled tracks sized for larger golf-community lots, 2026.",
    "h1": "Sports turf for Dr. Phillips backyards",
    "lede": capsule("Sports and fitness turf in Dr. Phillips is quoted per job rather than a flat per-square-foot rate, since a bocce court, a batting cage and a sled track each need a different build. The larger lots common in gated golf communities here usually have room for a dedicated sports surface that a tighter subdivision lot doesn't."),
    "sections": [
        ("Room to build on a golf-community lot",
         f"<p>Homes in Orange Tree and similar Dr. Phillips gated communities tend to sit on larger parcels than a standard subdivision, a legacy of being platted around golf-course frontage rather than maximizing density. That extra depth is what makes a dedicated sports surface practical: a 12-by-60-foot bocce court or a batting cage needs a long, narrow run of flat ground that a smaller zero-lot-line yard often can't spare without giving up the rest of the lawn.</p>"
         + f"<p>{svc('sports', 'The sports and fitness turf service page')} covers face-weight and infill choices by sport in more detail than fits here.</p>"),
        ("Building a home-gym sled track on sand instead of clay",
         f"<p>A sled push track or agility lane needs a firm, even surface more than a soft one, which the excessively drained Candler and Apopka sands under most of Dr. Phillips make easier to build correctly than a heavier clay soil would. The base still needs the same washed, open-graded crushed rock as any other turf project; on this ground it mostly needs to stay level rather than fight standing water.</p>"
         + f"<p>{post('artificial-turf-on-a-slope', 'A sloped or uneven yard')} needs grading before a track goes in regardless of soil type, since a sled track that isn't flat throws off every rep.</p>"),
        ("Keeping a batting cage or court inside the property line",
         f"<p>A batting cage or bocce court long enough to be useful can run close to a rear or side property line on some Dr. Phillips lots, which raises the same drip-line question any excavation near a mature oak does, and the same 10-foot waterbody setback on a lot backing the Butler Chain. Laying the surface out on paper against both boundaries before ordering material avoids a rebuild.</p>"
         + f"<p>Netting posts and cage framing for a batting setup typically need their own footing, separate from the turf install itself.</p>"),
    ],
    "scenario": ("Sizing a bocce court on a golf-community lot",
                 f"<p>Say a homeowner in a gated Dr. Phillips community wants a regulation-length bocce court, roughly 12 by 60 feet, or 720 sq ft, built along a side yard that currently holds nothing but St. Augustine. Because sports surfaces are quoted per job rather than by a flat per-foot rate, pricing depends on the specific product (a tighter, lower-nap turf than a residential lawn), the sub-base leveling required for consistent ball roll, and any edging that separates the court from the surrounding lawn.</p>"
                 + f"<p>On a lot with the room to spare, laying the court along the side yard rather than centered in the backyard usually keeps the main lawn intact for everything else the family uses it for.</p>"),
    "faqs": [
        faq("Do larger Dr. Phillips lots make a sports court cheaper per square foot?", "Not directly, since sports surfaces are priced per job rather than a flat rate. What a larger lot does is make certain builds, a long bocce court or batting cage in particular, practical to fit without sacrificing the rest of the yard."),
        faq("Does a bocce court need the same base as a regular lawn?", "The washed crushed-rock base is the same material, but a sports surface needs tighter leveling tolerances for consistent play, which usually means more compaction passes than a standard lawn install."),
        faq("Can a batting cage go right up to the property line?", "Nothing in the state turf standard sets a property-line setback beyond the waterbody and drip-line rules that apply to any turf. A local setback for structures like cage framing and posts is a separate question worth checking with Orange County before finalizing placement."),
    ],
    "sources": [SOIL_CANDLER, SOIL_APOPKA, ORANGETREE],
}

# ---------------------------------------------------------------- pavers
LOCAL["pavers"] = {
    "title": "Turf & Pavers for Dr. Phillips Entries and Walks",
    "meta": "Turf between pavers in Dr. Phillips, FL: entry drives, stepping-stone paths and driveway strips on fast-draining ridge sand, priced for 2026.",
    "h1": "Turf and pavers for Dr. Phillips walkways",
    "lede": capsule("Turf set between pavers in Dr. Phillips is quoted per job rather than a flat per-square-foot rate, since the design depends on paver layout more than square footage. Paver entries and driveway strips are common across the gated communities here, and the sandy ridge ground underneath makes the joints easier to keep draining than tighter soil would."),
    "sections": [
        ("Why paver entries are common in Dr. Phillips gated communities",
         f"<p>Guard-gated communities like Orange Tree and Phillips Landing favor paver driveways and entry walks over plain concrete, both for the look their architectural guidelines expect and for how well pavers handle Central Florida's rainy season without cracking the way a poured slab can. A turf ribbon set into the joints between paver bands, or along a stepping-stone path through a side yard, is a common request in these communities specifically because the hardscape is already there.</p>"
         + f"<p>{svc('pavers', 'The turf and pavers service page')} covers how a joint strip differs from a full-yard install in more detail.</p>"),
        ("What Candler sand does for a paver joint's drainage",
         f"<p>A turf strip between pavers doesn't sit on the two to four inches of rock a full lawn gets; it gets a thin leveling layer of sand in the joint instead, and that sand needs to drain rather than trap water against the paver edges. The excessively drained Candler sand common across the higher ground in Dr. Phillips is naturally suited to that job, since it percolates faster on its own than most fill material would even before any base work happens.</p>"
         + f"<p>Near a lake shore, where the soil shifts toward the faster-draining Astatula series, that advantage is even more pronounced, though joint width still matters more than soil type for how well a strip actually drains.</p>"),
        ("Driveway strips on wider golf-community lots",
         f"<p>A center strip of turf between two paver wheel tracks, replacing what used to be a full-width driveway, is a request that comes up more often on wider Dr. Phillips lots than on a standard subdivision's narrower frontage, simply because there's more driveway to work with. The strip needs the same firm, level joint sand as a smaller paver-border project, sized to the vehicle's actual wheelbase rather than a generic width.</p>"
         + f"<p>{post('artificial-grass-for-shady-side-yards', 'A shaded side path where sod never grew')} often pairs with the same paver-and-turf approach used on a driveway strip.</p>"),
    ],
    "scenario": ("Turfing a stepping-stone path through a side yard",
                 f"<p>Say a Phillips Landing homeowner has a 40-foot stepping-stone path connecting the driveway to a side gate, currently bordered by bare dirt that turns muddy after every storm. Because paver-and-turf work is quoted per job, not a flat per-foot rate, pricing depends on the paver spacing, the joint width being turfed, and whether the existing stones need releveling before the turf goes in.</p>"
                 + f"<p>A path this size is a small enough job that it often gets bundled with a larger lawn project on the same visit, since the crew and base material are already on site either way.</p>"),
    "faqs": [
        faq("Does turf between pavers need HOA approval in Dr. Phillips like a full lawn does?", "Most gated communities' architectural review covers hardscape and landscape changes generally, so a paver-and-turf entry redesign likely needs the same submittal a full lawn conversion would, even though the footprint is smaller."),
        faq("Can turf go into paver joints on a driveway without regrading it?", "Usually yes, since the joint gets a thin sand leveling layer rather than a full rock base, but the existing pavers need to already drain correctly. A driveway with a low spot needs that fixed before turf goes into the joints, not after."),
        faq("Does the sandy Dr. Phillips soil make paver joints drain better than elsewhere?", "It helps. The Candler and Astatula series common here are naturally fast-draining, which gives a joint strip a head start over the same design on tighter clay soil, though joint width and sand quality still matter more."),
    ],
    "sources": [SOIL_CANDLER, SOIL_ASTATULA, ORANGETREE, PHILLIPSLANDING],
}

# ---------------------------------------------------------------- repair
LOCAL["repair"] = {
    "title": "Artificial Turf Repair for Dr. Phillips Homes",
    "meta": "Artificial turf repair in Dr. Phillips, FL: low-E glass scorch marks on lakefront homes, storm-lifted edges, and open-seam fixes, priced per visit.",
    "h1": "Turf repair for Dr. Phillips yards",
    "lede": capsule("Turf repair in Dr. Phillips is priced by the visit, not by the square foot, since an open seam and a melted patch call for different fixes. Large lakefront windows on Butler Chain homes are a repair trigger specific to this area, on top of the wind and storm exposure any open water frontage brings."),
    "sections": [
        ("Low-E glass on lakefront homes is a Dr. Phillips-specific repair cause",
         f"<p>Lakefront homes along the Butler Chain and Big Sand Lake tend to carry more glass than an inland house, expansive sliders and picture windows built to frame the water view, and a low-emissivity coating on that much glass can reflect enough concentrated sunlight to soften turf in its path. Polyethylene blades start to give around 175 to 200 degrees Fahrenheit under that kind of focused heat, and the damage shows up as a scorched patch shaped by the reflection angle rather than ordinary wear.</p>"
         + f"<p>{post('can-artificial-turf-melt', 'How to tell reflection damage from a different problem')} covers what that patch looks like compared with a burn from a grill or a discarded cigarette.</p>"),
        ("Open water frontage means more wind exposure at the edges",
         f"<p>A yard that backs directly onto open lake water, without a fence or another structure breaking the wind, takes a stronger gust during a summer storm than a yard tucked between houses does. That extra load shows up first at the perimeter, where a nailed or bender-board edge can lift if it wasn't anchored to the standard the state requires. {post('artificial-turf-hurricane-flooding', 'What a named storm can do to turf on an exposed lot')} is worth reading before hurricane season if your yard backs open water.</p>"
         + f"<p>A seawall doesn't change the wind exposure, only the water setback, so a lot with one still needs the same edge-anchoring attention as one without.</p>"),
        ("Open seams on older Orange Tree and Bay Hill installs",
         f"<p>Turf installed years ago in the area's oldest sections, Orange Tree's original 1970s and 1980s phases or the Bay Hill neighborhood built in the 1960s, is old enough on some lots that the original adhesive has had decades to age, even accounting for later turf replacements. A seam that's started to separate rarely fails all at once; catching it while it's a few inches of lift is a shorter repair than waiting for a wider gap to open under foot traffic.</p>"
         + f"<p>{svc('repair', 'The turf repair service page')} covers what a seam repair visit typically involves.</p>"),
    ],
    "scenario": ("Diagnosing a scorched patch on a lakefront lawn",
                 f"<p>Say a home on Lake Chase has a roughly 4-by-6-foot discolored patch of turf near a bank of west-facing sliding glass doors, noticed after a stretch of clear afternoons. Because repair work is priced by the visit rather than the square foot, the first step is confirming the cause, checking the reflection angle off the glass against the patch's shape and timing, before quoting a fix.</p>"
                 + f"<p>If it's reflection damage, as the shape and location suggest, the repair replaces the affected turf section and the conversation shifts to whether film on the glass or a change in furniture placement prevents a repeat.</p>"),
    "faqs": [
        faq("How do I know if my lakefront home's windows are melting the turf?", "Look for a scorched or discolored patch shaped like a beam rather than a random burn, usually on the side of the yard facing a large west- or south-facing window. That pattern points to low-E glass reflection rather than ordinary wear."),
        faq("Does an open lake frontage need stronger edge anchoring than a fenced yard?", "It's worth the extra attention. A yard with nothing breaking the wind off open water takes more load at the perimeter during a storm, so confirming the edge is anchored to the state's wind-and-flood standard matters more there than on a sheltered lot."),
        faq("Is repair pricing different for an older Orange Tree or Bay Hill install than a newer one?", "Not by neighborhood. What matters is the turf's age and condition, not which decade the community itself was built, since most lawns have been replaced at least once since these areas were originally developed."),
    ],
    "sources": [BAYHILL, ORANGETREE, WATER_ATLAS],
}

# ---------------------------------------------------------------- cleaning
LOCAL["cleaning"] = {
    "title": "Turf Cleaning & Maintenance in Dr. Phillips, FL",
    "meta": "Turf cleaning and maintenance in Dr. Phillips, FL: oak-canopy leaf litter, lakefront pollen and pet-odor service for established yards, priced per visit.",
    "h1": "Turf cleaning for Dr. Phillips yards",
    "lede": capsule("Turf cleaning and maintenance in Dr. Phillips is priced per visit, and the two things that move it are the size of the lawn and how long it's gone untouched. Decades-old oak canopies in the area's older subdivisions and pollen off the Butler Chain both add to what a maintenance visit here typically clears."),
    "sections": [
        ("Oak litter in communities planted decades ago",
         f"<p>Orange Tree's original phases date to the late 1970s and Bay Hill's to the 1960s, long enough for the oaks planted with those subdivisions to drop a steady mix of leaves, acorns and pollen catkins through the fall and spring. That litter settles into turf fibers differently than grass clippings would on a natural lawn, since it doesn't decompose in place the way it would in soil; it needs to be swept or blown off before it works down toward the backing.</p>"
         + f"<p>{post('oak-leaves-and-debris-on-artificial-turf', 'How oak debris affects synthetic turf differently than a natural lawn')} covers the seasonal pattern in more detail.</p>"),
        ("Pollen and algae near the Butler Chain shoreline",
         f"<p>A lakefront lot on the Butler Chain or Big Sand Lake picks up more airborne pollen off the surrounding tree canopy and, occasionally, algae residue carried by a lake breeze during a bloom, on top of whatever a standard yard collects. A power-broom and rinse cycle timed to spring pollen season keeps that from building up in the pile the way it would on a yard set back from the water.</p>"
         + f"<p>None of that changes the base cleaning routine, just how often it's worth doing on a lot that sits right at the shoreline.</p>"),
        ("Pet-odor service in narrower Sand Lake Cove side yards",
         f"<p>A side-yard dog run in a subdivision like Sand Lake Cove, tighter than an open backyard, concentrates pet traffic onto a smaller footprint, which means odor and infill depletion both show up faster there than on a wide-open lawn. {post('how-to-get-dog-urine-smell-out-of-artificial-turf', 'A deeper rinse-and-treat routine')} in that specific strip, rather than treating the whole yard on the same schedule, is usually the more efficient fix.</p>"
         + f"<p>{svc('cleaning', 'The turf cleaning service page')} covers infill top-ups and deodorizing treatments by use case.</p>"),
    ],
    "scenario": ("Scheduling a fall maintenance visit under mature oaks",
                 f"<p>Say a home in an older section of Orange Tree has roughly 1,800 sq ft of lawn turf under a heavy oak canopy that's dropped several inches of leaf litter and acorns since the last service. Because maintenance is priced by the visit rather than the square foot, the quote depends on how much debris has to come out, whether infill needs topping off underneath it, and whether a power broom alone handles it or a rinse cycle is needed too.</p>"
                 + f"<p>A yard like this one usually needs two seasonal visits a year, once after the fall leaf drop and once after spring pollen, rather than a single annual cleaning.</p>"),
    "faqs": [
        faq("How often does turf under Dr. Phillips oak canopies need cleaning?", "Twice a year is typical for a lot with heavy oak cover, once after fall leaf and acorn drop and once after spring pollen, compared with once a year for an open lawn without mature trees."),
        faq("Does lakefront turf near the Butler Chain need different cleaning than an inland yard?", "Mostly the same routine, just on a shorter interval during pollen season and after any algae bloom on the lake, since both settle onto turf closer to the shoreline faster than they would further back."),
        faq("Is pet-odor treatment priced differently for a narrow side-yard run?", "It's priced by the job rather than a flat rate either way, but a concentrated run typically needs infill checked and topped off more often than the same square footage spread across an open lawn."),
    ],
    "sources": [ORANGETREE, BAYHILL, WATER_ATLAS, SANDLAKECOVE],
}

# ---------------------------------------------------------------- replacement
LOCAL["replacement"] = {
    "title": "Turf Removal & Replacement in Dr. Phillips, FL",
    "meta": "Turf removal and replacement in Dr. Phillips, FL: swapping out original-era installs from Orange Tree and Bay Hill's oldest sections, priced per job.",
    "h1": "Turf replacement for Dr. Phillips homes",
    "lede": capsule("Turf removal and replacement in Dr. Phillips is priced close to a new install minus whatever base material can be reused, not a flat per-square-foot rate. The area's oldest sections, developed from the 1960s through the 1990s, are reaching the age where a first-generation lawn or an early turf conversion is due for a full swap."),
    "sections": [
        ("Replacing turf that's outlived its original base",
         f"<p>A synthetic lawn's working life runs somewhere between ten and twenty years, set by how well the yarn resists UV, how hard it's used and what infill it carries, which means a lawn installed in Dr. Phillips' earlier wave of turf adoption, anywhere from the mid-2000s on, is now old enough in some cases to need a full swap rather than a patch repair. Whether the existing rock base is worth keeping depends on how it was built originally; a base that was washed and properly compacted holds up far longer than turf's own service life, while one built with unwashed fill often needs to come out along with the old surface.</p>"
         + f"<p>{post('how-long-does-artificial-turf-last-in-florida', 'What actually shortens a turf lawn’s lifespan here')} covers the traffic and UV factors in more detail.</p>"),
        ("What changed in the rules since the original install went in",
         f"<p>A homeowner replacing turf installed before May 19, 2026 is working under a different, now-tighter material standard than whatever was originally used: infill on a single-family lot is now limited to silica sand, zeolite, rock, shell or coated sand outside a playground footprint, and the turf, backing and infill can't contain intentionally added PFAS or heavy metals. A replacement job is a natural point to bring an older lawn up to that current standard, even though the rule doesn't require retrofitting an existing, already-installed lawn.</p>"
         + f"<p>{a('/laws/florida-hb-683/', 'What Rule 62-308.100 requires')} is worth a read before choosing a replacement product.</p>"),
        ("Coordinating replacement with an HOA's design review",
         f"<p>In a gated community running architectural review, like Orange Tree or Phillips Landing, a full turf replacement can trigger the same ARC submittal a first-time installation would, particularly if the product or color is changing from what was originally approved. Confirming that upfront avoids a mismatch between a signed contract and a design-review answer that comes back after material is already ordered.</p>"
         + f"<p>{svc('replacement', 'The turf removal and replacement service page')} covers how much of an old base typically gets reused versus rebuilt.</p>"),
    ],
    "scenario": ("Replacing a first-generation lawn from the mid-2000s",
                 f"<p>Say a home in one of Dr. Phillips' older sections has 1,200 sq ft of turf installed around 2008 that's gone matted and faded, with the original base still reasonably intact under it. Because replacement pricing runs close to a new install minus whatever base can be reused, a job like this typically lands somewhat below the full {price('residential', True)} new-install range, with the exact number depending on how much of the existing rock survives inspection once the old turf comes up.</p>"
                 + f"<p>If the community requires design review for the new product, that submittal runs in parallel with the tear-out rather than delaying it, since removal doesn't usually need ARC approval the way the finished surface does.</p>"),
    "faqs": [
        faq("How do I know if my Dr. Phillips lawn needs replacement instead of repair?", "Widespread matting, faded color across the whole lawn rather than one patch, and infill that's worn thin everywhere point to replacement. A single open seam or one damaged section is usually a repair instead."),
        faq("Does a turf replacement need to meet the new 2026 state standard?", "The rule doesn't require retrofitting an existing lawn, but since a replacement is starting fresh anyway, most homeowners choose infill and materials that already meet the current standard rather than matching an older, now-outdated spec."),
        faq("Will my HOA make me resubmit for a like-for-like turf replacement?", "Depends on the community. Some architectural review processes only care about a visible change in product or color; others want any exterior work resubmitted. Ask before assuming a straight swap doesn't need paperwork."),
    ],
    "sources": ["dep-rule", "stn-life", ORANGETREE, PHILLIPSLANDING],
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
