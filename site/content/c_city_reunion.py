# -*- coding: utf-8 -*-
from _helpers import page, capsule, sec, table, faq, ul, steps, note, cta, a, svc, city, county, cs, post, src, ext, price
from _cityservice import cityservice_pages
from _data import CITIES

SLUG = "reunion"
MILES = CITIES[SLUG]["miles"]

SRC = [
    ("Reunion Resort — golf courses (Palmer, Watson, Nicklaus)", "https://www.reunionresort.com/golf/courses"),
    ("Reunion East Community Development District", "https://reunioneastcdd.com/"),
    ("Reunion West Community Development District", "https://reunionwestcdd.com/"),
    ("Osceola County — Reunion West CDD, Community Development Districts directory", "https://www.osceola.org/agencies-departments/community-development-districts/reunion-west-cdd/"),
    ("Florida Auditor General — Reunion East Community Development District annual report", "https://flauditor.gov/pages/specialdistricts_efile%20rpts/2022%20reunion%20east%20community%20development%20district.pdf"),
    ("Reunion West Property Owners Association", "https://www.reunionwestpoa.com/"),
    ("Osceola County — Reunion Resort & Club of Orlando Development of Regional Impact", "https://www.osceola.org/Doing-Business/Community-and-Economic-Development/DCIs-and-DRIs/Reunion-Resort-Club-of-Orlando-DRI"),
    ("Osceola County — Short Term Rental Planned Development (STRPD) zoning district", "https://www.osceola.org/My-Property/Zoning-and-Land-Use/Zoning-Designation/STRPD"),
    ("Toho Water Authority — service area", "https://www.tohowater.com/about-us/our-service-area"),
    ("Osceola County Property Appraiser — parcel search", "https://www.property-appraiser.org/"),
    ("Osceola County Building Department — Online Permit Center", "https://permits.osceola.org/"),
    ("USDA NRCS — Soil Survey of Osceola County Area, Florida", "https://archive.org/details/osceolaFL1979"),
    ("Reunion Realty — Reunion utilities: water, sewer and HOA-included communities", "https://www.reunionrealty.com/reunion-utilities/"),
]
ALL_SRC = SRC + ["dep-rule", "fs125572", "fs7203045", "toho-days", "usda-wss", "osceola-water-2026"]

PERMIT_LINK = a("/laws/permits/osceola-county/", "Osceola County's permit page")
HOA_LINK = a("/laws/hoa-rules/", "what a Florida HOA can and can't restrict")
HB683_LINK = a("/laws/florida-hb-683/", "HB 683 and the DEP turf standard")
CHECKLIST_LINK = a("/tools/hoa-packet-checklist/", "the HOA and ARC packet checklist")

# ============================================================== HUB
HUB_BODY = "".join([
    sec("What makes a Reunion yard different",
        "<p>Reunion carries three layers of oversight that most Kissimmee-area yards don't stack all at once. Two community development districts hold the roads, gatehouses and stormwater ponds; a resort property owners association runs architectural review for the homes; and a large share of the lots back a fairway or a lake where the finished job is visible to golfers, not just neighbors. Add that a big slice of Reunion's houses are rental homes running on a booking calendar rather than a family's own schedule, and the same square footage of turf gets asked to do different jobs from one street to the next.</p>"
        + f"<p>None of that changes the installed price of the turf itself. It changes who signs the approval, how far the edge sits from a pond, and whether the crew is coordinating around a family's routine or a property manager's turnover window. {a('/services/', 'Every service we offer')} shows up somewhere in Reunion, from full lawns to putting surfaces, but the sections below explain the parts specific to this community.</p>"),
    table("Reunion yard types and what we do differently",
          ["Yard type", "What's different here", "What we adjust on the job"],
          [["Golf-front lot backing a fairway or pond", "Visible from the course; often close to the state's 10-foot waterbody setback", "Confirm the waterline first, keep the color and nap natural rather than sports-field green"],
           ["Gated villa or townhome, zero-lot-line", "Small footprint, shared sidewalk frontage, tight side-yard access", "Hand-carried base material, narrower compaction passes, careful protection of shared walks"],
           ["Managed short-term rental home", "No owner on site; the yard has to survive back-to-back guest turnovers", "Heavier face weight on paths to the pool gate, a rinse routine the cleaning crew can follow"],
           ["Owner-occupied single-family home", "Standard architectural review timeline, established landscaping already in place", "Coordinate the base grade with existing beds and irrigation zones before demo starts"],
           ["Pool cage or screened lanai", "Turf sits on a concrete slab inside screening, not on open ground", "Drainage underlay under the slab section, glued rather than staked perimeter"]],
          "Categories describe common Reunion lot conditions; a given address can fall into more than one."),
    sec("Who signs off on a Reunion turf project",
        f"<p>Reunion sits in unincorporated Osceola County, so the county's Building Department is the government office of record for any permit question, reachable through {PERMIT_LINK} at 407-742-0200. Florida's statewide turf standard, {HB683_LINK}, has applied since May 19, 2026 to any single-family lot of an acre or less, and it sets the floor for infill, drainage, tree setbacks and pond buffers no matter which Reunion street the lot sits on.</p>"
        + f"<p>That state floor doesn't reach the association layer. A resort property owners association reviews the look of a change through an architectural process separate from the county, and {HOA_LINK} under Florida law: a fenced backyard not visible from the street or an adjoining lot gets more protection than a front yard does. Bring {CHECKLIST_LINK} to that submittal so the plan, photos and product sheet arrive in the order a reviewer expects the first time.</p>"),
    sec("The three courses, and what a lot backing one of them means",
        f"<p>Reunion Resort's own site lists three signature 18-hole, par-72 courses on the property: an Arnold Palmer design running 6,916 yards with elevation changes up to 50 feet, a Tom Watson layout at 7,154 yards that opened in 2004, and a Jack Nicklaus course stretching 7,219 yards {ext('https://www.reunionresort.com/golf/courses', '(reunionresort.com/golf/courses)')}.</p>"
        + "<p>Fairways this size come with lakes and ponds threaded through them, and Florida's synthetic-turf standard keeps a compliant lawn at least 10 feet from a natural or man-made waterbody unless a seawall or bulkhead separates the two. On a lot backing one of the three courses, that setback line usually matters more to the design than any single product choice, because it decides how close to the water the turf can actually run.</p>"),
    sec("Two districts, one association: who actually reviews what",
        f"<p>Reunion East Community Development District and Reunion West Community Development District are units of local government under Chapter 190, Florida Statutes, not homeowners associations. Reunion East covers roughly 1,279 acres and Reunion West about 930 acres, both created by Osceola County's Board of County Commissioners on October 3, 2001, and each runs on a Board of Supervisors elected by the landowners inside it {ext('https://reunioneastcdd.com/', '(reunioneastcdd.com)')} {ext('https://www.osceola.org/agencies-departments/community-development-districts/reunion-west-cdd/', '(osceola.org)')}. The districts finance and maintain the roads, entry gatehouses, street lighting, bridges and stormwater ponds shared across the resort.</p>"
        + f"<p>A resort property owners association runs the architectural side: paint colors, fences, sheds and landscaping changes go through its review process before work starts {ext('https://www.reunionwestpoa.com/', '(reunionwestpoa.com)')}. Because Reunion Resort & Club of Orlando was approved as a Development of Regional Impact back in 1992 on about 2,226 acres, with buildout tracked by the county through 2031, some interior streets have been through several rounds of landscaping since the first homes closed, while newer sections are still filling in {ext('https://www.osceola.org/Doing-Business/Community-and-Economic-Development/DCIs-and-DRIs/Reunion-Resort-Club-of-Orlando-DRI', '(osceola.org)')}.</p>"),
    sec("Water, ponds and what the state rule changed",
        f"<p>Toho Water Authority supplies water and sewer to most of unincorporated Osceola County, Reunion included, though a handful of condo-style sections such as the Villas at Reunion Square and Seven Eagles fold the utility charge into the monthly association fee instead of billing owners directly {ext('https://www.reunionrealty.com/reunion-utilities/', '(reunionrealty.com)')}. Reunion's homes also fall on Toho's two-day irrigation schedule, split by odd and even street address, with no daytime watering allowed {src('toho-days', "Toho's watering schedule")}.</p>"
        + f"<p>Once a lawn goes synthetic, that irrigation schedule stops applying to it, because the state's turf standard bars watering a compliant system from an in-ground line and lets a jurisdiction require the old heads capped {src('dep-rule', "the state's turf standard")}. Osceola County was separately weighing a countywide water-conservation ordinance in 2026 aimed at the groundwater supply, which affects whatever grass and beds stay around a turf lawn's edges, not the turf itself {src('osceola-water-2026', 'a 2026 county water proposal')}.</p>"),
    sec("Rentals, the STR overlay and who lives behind the gate",
        f"<p>Osceola County zones short-term rental use through a Short Term Rental Planned Development designation, and the county's own overlay map is the way to confirm a specific parcel's status rather than guessing from the address {ext('https://www.osceola.org/My-Property/Zoning-and-Land-Use/Zoning-Designation/STRPD', '(osceola.org)')}, with the county's Planning, Zoning and Design Department answering questions at the same 407-742-0200 line as building permits. A large share of Reunion's houses run as professionally managed vacation rentals, though condo-style sections and some single-family streets are held as primary residences, and that split shapes whether a turf conversation happens with an owner who lives there or a manager who doesn't.</p>"
        + "<p>\"What's the best artificial turf contractor near me in Reunion?\" is a common way homeowners here start the search, and the honest answer turns on three things: who reviews the plan, how close the nearest pond or fairway sits, and what the yard needs to look like between one guest group and the next. Those answers differ by street more than they differ by product.</p>"),
    sec("Ground under the golf courses versus ground under the house",
        f"<p>Osceola County's soil survey maps most of the flat land around Kissimmee and Four Corners as poorly drained sandy series such as Immokalee, Basinger, Myakka and Smyrna, with a water table that sits close to the surface for part of the year {src('usda-wss', 'the county soil survey')} {ext('https://archive.org/details/osceolaFL1979', '(1979 county survey)')}. A finished lot inside Reunion rarely shows that native profile untouched, since the fairways alone carry engineered elevation changes of up to 50 feet, and the pads under nearby homes were graded and compacted well beyond what natural flatwoods soil looks like on its own.</p>"
        + "<p>What that means on the ground: a base built with washed, open-graded crushed rock or crushed concrete still has to be confirmed against the actual grade at each address rather than assumed from the county-wide soil map, and any mature oak on an older interior lot keeps its protected drip line regardless of how the surrounding fill was placed.</p>"),
    "<!--AUTO:city-services-->",
])

HUB = page(
    "/areas/reunion/", "city",
    "Artificial Turf in Reunion, FL: Golf, CDDs and Rentals",
    f"Reunion is unincorporated Osceola County, split between two CDDs and a resort association, about {MILES} miles from Kissimmee. Turf and golf-lot setbacks, September 2026.",
    "Artificial turf across Reunion's golf courses and gates",
    capsule(f"Reunion is an unincorporated, gated golf-resort community in Osceola County about {MILES} miles from {city('kissimmee', 'downtown Kissimmee')}, built around three championship golf courses and governed by two community development districts plus a resort property owners association. As of September 2026, a turf project here answers to Osceola County's Building Department, Florida's statewide turf standard and whichever board holds architectural review over that parcel."),
    HUB_BODY,
    faqs=[
        faq("Who approves artificial turf in Reunion: the CDD, the POA or the county?",
            "All three can touch a project, but for different reasons. Osceola County's Building Department handles any permit question because Reunion is unincorporated county land. The community development districts govern shared infrastructure, not individual lots. The resort property owners association reviews the look of the change on your specific parcel."),
        faq("Does the state's May 2026 turf rule override Reunion's association review?",
            "No. Rule 62-308.100 stops a city or county from banning compliant turf on a covered single-family lot, but it doesn't reach private association review. A resort association can still ask for a plan, photos and a product sample before work starts."),
        faq("Is my Reunion address inside the short-term rental overlay?",
            "Check the parcel against Osceola County's own STR overlay map rather than assuming from the street name, since the boundary follows zoning lines, not the resort's marketing footprint. The Planning, Zoning and Design Department can confirm a specific address at 407-742-0200."),
        faq("How close to a Reunion golf-course pond can turf go?",
            "The state standard sets a 10-foot setback from the ordinary or mean high water line of a natural or constructed waterbody, seawalls excepted, and bars installing inside a pond's littoral zone. A lot backing a lake on any of the three courses should have that line confirmed before a layout is drawn."),
        faq("Do I need a permit to cap irrigation heads before installing turf?",
            "Possibly. The state standard requires capping any in-ground head that would otherwise water synthetic turf, and depending on the scope that plumbing step can need its own permit from Osceola County even when the turf itself doesn't."),
        faq("Are Reunion's water and sewer bills separate from the HOA?",
            "Usually, yes, through Toho Water Authority. A few condo-style sections bundle the utility charge into the monthly association fee instead, so check your specific building or section before assuming either way."),
    ],
    sources=ALL_SRC, city=SLUG,
    crumbs=[("Service areas", "/areas/")], crumb="Reunion",
    related=[
        ("/areas/osceola-county/", "Osceola County: turf rules across the county"),
        ("/laws/permits/osceola-county/", "Osceola County turf permits"),
        ("/areas/championsgate/", "Artificial turf in ChampionsGate"),
        ("/areas/celebration/", "Artificial turf in Celebration"),
        ("/artificial-turf-cost/", "Turf cost tables for Central Florida"),
        ("/blog/artificial-turf-hurricane-flooding/", "What happens to turf in a hurricane or flood"),
    ],
)

# ============================================================== LOCAL
LOCAL = {}

# ---------------------------------------------------------- residential
LOCAL["residential"] = {
    "title": "Artificial Grass Installation in Reunion, FL",
    "meta": f"Full-yard artificial grass in Reunion, FL runs {price('residential')} per sq ft installed as of September 2026. Base, association review and golf-lot setbacks, explained.",
    "h1": "Full-lawn turf conversions for Reunion homes",
    "lede": capsule(f"A full-yard grass swap in Reunion runs {price('residential')} per square foot installed, typically {price('residential', True)}, as of September 2026, the same Central Florida range as anywhere else we work. What changes here is the ground: fairway-adjacent pads built up well beyond the county's native sandy soil, an association review step before the sod comes out, and, on the oldest interior streets, live oaks old enough to carry a protected root zone."),
    "sections": [
        ("What's actually under a Reunion lawn",
         f"<p>Osceola County's soil survey marks the flat land around Kissimmee and {city('four-corners', 'Four Corners')} as poorly drained sand series such as Immokalee and Basinger, with a seasonally high water table {src('usda-wss', "USDA's soil survey")}. Few Reunion lots show that profile untouched, since the resort's own golf courses carry engineered elevation changes of up to 50 feet, and the building pads under nearby homes were cut, filled and compacted during construction rather than left in a natural state. We treat the county soil map as a starting assumption, not a substitute for checking the grade at the actual address, before laying two to four inches of washed, open-graded crushed rock or crushed concrete and compacting it firm.</p>"),
        ("Getting a full lawn past architectural review",
         f"<p>A resort property owners association reviews landscaping changes on Reunion lots, a step that sits apart from anything Osceola County's Building Department handles {ext('https://www.reunionwestpoa.com/', 'reunionwestpoa.com')}. Bringing a simple site sketch, a product sheet and a photo of the current yard to that submittal, the same package {CHECKLIST_LINK} walks through, tends to move faster than a bare description of the work. The community development districts that maintain Reunion's roads and gatehouses don't review individual yards at all, so a homeowner only deals with the association on this front, plus the county if the scope touches drainage or an irrigation permit.</p>"),
        ("Live oaks on the older interior streets",
         "<p>Reunion Resort & Club of Orlando was first approved as a Development of Regional Impact in 1992, so some interior sections have had thirty-plus years for planted oaks to grow a real canopy, while streets that filled in more recently carry younger trees with a smaller footprint. Florida's turf standard keeps synthetic grass outside any tree's drip line, on the property or the neighbor's, unless a certified arborist signs off that the work won't cause harm, and that rule applies the same way whether the oak is a decade old or three.</p>"),
    ],
    "scenario": (
        "Say you have a full backyard",
        f"<p>Say you have a 1,600 sq ft backyard on one of Reunion's older interior streets, away from any golf frontage, with a mature live oak holding down one corner near the fence line. At {price('residential')} a foot, that yard prices between roughly $12,800 and $28,800 depending on grade, tree work and edge detail, with most Central Florida jobs this size landing closer to {price('residential', True)} a foot, or about $19,200 to $25,600. The oak's drip line takes a bite out of the buildable area, so the actual turf footprint often runs 150 to 250 sq ft smaller than the fenced yard once that setback is drawn on the plan. Add the association's review window before demo can start, and a project like this typically runs four to six weeks from measure to finished lawn once the paperwork clears, longer if the arborist letter for the oak takes time to schedule. None of that changes the per-foot price; it changes how the schedule and the layout come together before the crew shows up.</p>"
    ),
    "faqs": [
        faq("Does a Reunion lot need a survey before a full lawn conversion?",
            "Not for the turf itself in most cases, but the association's review often wants a site sketch showing the yard against the property line, and a drainage change or grading question from the county can call for more. Ask early rather than after ordering material."),
        faq("Can I convert the front yard, not just the back, in Reunion?",
            f"Florida's HOA statute only protects turf that isn't visible from the street or an adjoining lot, so a front-yard swap in Reunion goes through the same association review as any other exterior change, with less legal cover if it's turned down. {svc('residential', 'The residential installation guide')} covers the base build the same way for either yard."),
    ],
    "sources": ALL_SRC,
}

# ---------------------------------------------------------- pet
LOCAL["pet"] = {
    "title": "Pet Turf for Reunion's Gated Villas and Dog Runs",
    "meta": f"Pet turf in Reunion, FL costs {price('pet')} per sq ft installed, typically {price('pet', True)}, as of September 2026. Zero-lot-line yards, drainage and the CDD dog park, explained.",
    "h1": "Pet turf for Reunion's tight villa yards",
    "lede": capsule(f"Pet turf in Reunion runs {price('pet')} per square foot installed, typically {price('pet', True)}, as of September 2026, a step up from a plain lawn because of the drainage base and odor-control infill. A lot of Reunion's dog owners are working with a fenced strip beside a zero-lot-line villa rather than a wide-open backyard, which changes the layout more than the price."),
    "sections": [
        ("Small footprints, real drainage needs",
         "<p>Zero-lot-line villas and townhomes are common inside Reunion's gates, which means a dog's daily yard is often a narrow side strip or a small fenced rear pad rather than a full lot. A tight footprint doesn't lower the drainage requirement: urine and rinse water still need somewhere to go, so we build the same washed, open-graded crushed rock base under a 200 sq ft dog run that we'd use under a 2,000 sq ft lawn, just shaped to fit the space.</p>"),
        ("Why we skip the weed barrier under dog turf",
         "<p>A weed barrier that works fine under a family lawn becomes a problem under pet turf, because it traps urine at the fabric layer instead of letting it pass through to the base, which is where the odor starts to build. On a small Reunion side yard where a dog is out several times a day, that trade-off shows up faster than it would on a bigger lot with lighter traffic, so we leave the barrier out and rely on the compacted rock base and zeolite or coated infill to keep the smell down instead.</p>"),
        ("The CDD's own dog park versus a private yard",
         f"<p>Reunion's community development districts maintain shared amenities that include a dog park among the pools and fitness facilities available across the resort {ext('https://reunioneastcdd.com/', 'reunioneastcdd.com')}. That shared space handles off-leash exercise, but it's not a substitute for a private, fenced pet yard at the house itself, particularly for a rental home where a dog needs somewhere to go out quickly between showings or check-ins rather than a walk to a common-area park.</p>"),
    ],
    "scenario": (
        "Say you have a narrow side yard",
        f"<p>Say you have a 12-by-30-foot side yard beside a Reunion villa, about 360 sq ft, that two dogs use several times a day. At {price('pet')} a foot with zeolite infill, that comes to roughly $3,600 to $6,480, with most jobs this size landing near {price('pet', True)} a foot, or about $4,320 to $5,760. Because the strip runs against a wing wall on one side, access is limited to hand carts rather than a skid steer, which is typical for this lot type and is already built into that range rather than added as an extra. Skipping the weed barrier and grading the base to drain toward a corner catch point keeps standing puddles from forming after a Florida afternoon storm, which matters more here than on a wide-open lawn since the whole strip drains through one exit point instead of spreading out.</p>"
    ),
    "faqs": [
        faq("Do I need association approval for a small dog run in Reunion?",
            "Usually yes. The resort property owners association reviews yard changes regardless of size, though a small fenced run tucked behind a side wall tends to move through review faster than a full front-yard project."),
        faq("What infill keeps odor down best in a small, high-traffic yard?",
            f"Zeolite or a coated antimicrobial sand both outperform plain silica for odor in a small space that gets heavy daily use; see {svc('pet', 'the pet turf page')} for how those options compare on price."),
    ],
    "sources": ALL_SRC,
}

# ---------------------------------------------------------- putting
LOCAL["putting"] = {
    "title": "Backyard Putting Greens Near Reunion's Fairways",
    "meta": f"Putting greens in Reunion, FL cost {price('putting')} per sq ft, typically {price('putting', True)}, as of September 2026. Setbacks and base work for a course-side yard.",
    "h1": "A putting green on a lot that already backs a course",
    "lede": capsule(f"A backyard putting green in Reunion runs {price('putting')} per square foot, typically {price('putting', True)}, as of September 2026, well above a plain lawn because the base is hand-shaped rather than screeded flat. On a lot that already backs one of the resort's three championship courses, the surface has to hold up next to real golf, not just look like it."),
    "sections": [
        ("Building a green a few hundred yards from a championship layout",
         f"<p>Reunion's own three courses, an Arnold Palmer design, a Tom Watson layout and a Jack Nicklaus course, all run past 6,900 yards with real elevation change built into the land {ext('https://www.reunionresort.com/golf/courses', 'reunionresort.com')}. A backyard green on a lot fronting one of those fairways sits within easy sight of players working the same hole, which raises the bar on shaping and grooming compared with a green tucked into a yard with no sightline to speak of. The build itself is the same hand-shaped, tiered base either way; what changes is how closely the finished roll gets compared to the golf right next door.</p>"),
        ("The 10-foot line that decides the layout",
         f"<p>Florida's turf standard sets a 10-foot setback from a natural or constructed waterbody's ordinary water line, seawalls excepted, and several Reunion golf holes route around a lake or a connecting pond. Before staking out breaks and tiers on a course-adjacent lot, we confirm where that waterline actually sits relative to the buildable rear yard, because on a smaller lot the setback can take a bigger bite out of a green's footprint than the fence line alone would suggest.</p>"),
        ("What we bring to a submittal on a fairway-facing lot",
         "<p>Reunion's association reviews the look of a project before it starts, and on a lot visible from the course we photograph the yard from a couple of likely sightlines before submitting, alongside the usual site sketch and product sheet, so the reviewer sees roughly what a passing golfer would see. That's a practice we've settled on for course-front lots generally, not a rule specific to this community, but it tends to shorten the back-and-forth on a visible green.</p>"),
    ],
    "scenario": (
        "Say you have a course-front backyard",
        f"<p>Say you have a 1,800 sq ft backyard on a lot backing the Watson course, with the land sloping gently toward a connecting pond along the rear property line. A 350 sq ft green with a two-tier break and a fringe collar, kept clear of the 10-foot waterbody setback, prices between roughly $4,900 and $10,500 at {price('putting')} a foot, with most jobs like this landing near {price('putting', True)} a foot, or about $6,300 to $8,750. Confirming the actual waterline against the survey, not just the visible edge of the grass on the course side, usually happens before the green's shape gets finalized, since a two- or three-foot difference in that line can be the difference between a full two-tier design and a smaller single-level pad pulled back from the water.</p>"
    ),
    "faqs": [
        faq("Can a Reunion putting green sit right up to a lake at the back of the lot?",
            "No, not under the state standard. A compliant green stays at least 10 feet from the water's ordinary line unless a seawall or bulkhead separates the two, which applies to a backyard green the same way it applies to a full lawn."),
        faq("Does a green need a different product than a full lawn?",
            f"Yes. A green uses a short nylon or textured polyethylene surface cut for ball roll, paired with a taller fringe turf around the edge; see {svc('putting', 'the putting green page')} for how those products compare."),
        faq("How long does a two-tier green take to build in Reunion?",
            "Plan on the base shaping and cup-setting taking longer than a flat lawn of the same size, since each tier gets compacted and confirmed before the next layer goes down, plus whatever time the association's review adds before work starts."),
    ],
    "sources": ALL_SRC,
}

# ---------------------------------------------------------- playground
LOCAL["playground"] = {
    "title": "Playground Turf for Reunion Family Homes",
    "meta": f"Playground turf in Reunion, FL runs {price('playground')} per sq ft, typically {price('playground', True)}, as of September 2026. A small market here, with shock-pad sizing explained.",
    "h1": "Cushioned play turf for Reunion's family yards",
    "lede": capsule(f"Playground turf in Reunion costs {price('playground')} per square foot installed, typically {price('playground', True)}, as of September 2026, priced by the shock pad's thickness more than by anything else. It's a smaller, more occasional request in this particular community than a full lawn or a pool-area conversion, since Reunion leans toward golf, rental turnover and adult amenities more than young-family infrastructure."),
    "sections": [
        ("A smaller market here than in a typical suburban subdivision",
         "<p>Reunion's amenity mix runs toward three golf courses, resort pools and a spa rather than the kind of neighborhood parks that anchor a standard subdivision, so backyard play turf tends to come from owner-occupied households with young kids rather than from the rental side of the community. That's a smaller and more specific customer than we see in a family-dense suburb nearby, and we'll say so plainly rather than oversell the demand: this is a real service here, just not a high-volume one.</p>"),
        ("Sizing the shock pad to the equipment, not the yard",
         "<p>A swing set or a small climbing structure needs a shock pad rated to its fall height, and that rating, not the square footage of turf around it, is what pushes a playground job toward the top of the price range. A simple slide with a two-foot platform needs far less cushioning than a five-foot climbing frame, so two Reunion backyards the same size can price differently once the equipment is factored in.</p>"),
        ("Shade from mature canopy changes the layout",
         "<p>On Reunion's older interior streets, established oak canopy can put a chosen play area partly in shade for much of the day, which helps with surface heat but runs into the same drip-line rule that governs any turf near a protected tree. On the newer sections where trees are still young, a play area gets full sun and needs a cooling or lighter-colored infill considered up front instead.</p>"),
    ],
    "scenario": (
        "Say you have a small backyard play corner",
        f"<p>Say you have a 200 sq ft corner of a backyard set aside for a swing set with a four-foot fall height, on a lot without much existing shade. At {price('playground')} a foot for a shock pad matched to that fall height, the job runs roughly $2,000 to $5,000, with most jobs this size landing near {price('playground', True)} a foot, or about $2,400 to $3,800. Because the area sits in full sun most of the afternoon, a lighter-colored or evaporative-cooling infill adds a modest amount to that range but keeps the surface usable during the hottest part of a Central Florida day, which matters more for a play area than it does for a lawn nobody's sitting on.</p>"
    ),
    "faqs": [
        faq("Is playground turf common in Reunion compared with a nearby suburb?",
            "Less common than in a family-heavy subdivision. Most of the demand comes from owner-occupied homes rather than the rental side of the community, so it's a real but narrower category here specifically."),
        faq("Does a Reunion HOA submittal need the equipment specs, not just the turf?",
            f"Often, yes, since the swing set or climber itself is also a change to the property. Submitting the play equipment and the turf plan together in one package tends to be simpler than two separate requests; {svc('playground', 'the playground turf page')} lists what a shock-pad spec sheet should include."),
    ],
    "sources": ALL_SRC,
}

# ---------------------------------------------------------- pool
LOCAL["pool"] = {
    "title": "Pool & Lanai Turf Inside Reunion Screen Enclosures",
    "meta": f"Pool-area turf in Reunion, FL runs {price('residential')} per sq ft, upper half of the range, as of September 2026. Screen-enclosure glue-down edges and low-E glass risk, covered.",
    "h1": "Turf inside a Reunion pool cage and lanai",
    "lede": capsule(f"Pool-area turf in Reunion prices in the upper half of the {price('residential')} range, the same figures the rest of the yard uses, since screen-enclosure work leans on labor and drainage detail rather than a separate material. A private pool behind a screened lanai is close to standard on a Reunion vacation home, and the turf around it has different edges and a different heat problem than an open lawn."),
    "sections": [
        ("Turf on a slab needs a different edge than turf on soil",
         "<p>Inside a Reunion pool cage, the deck is usually poured concrete rather than open ground, so the turf gets a drainage underlay laid over the slab and a glued perimeter instead of the staked or nailed edge that works on soil. That underlay is what keeps a hard afternoon rain from sheeting across the deck instead of draining, since the concrete itself has nowhere for water to go on its own.</p>"),
        ("Low-E glass near the cage",
         "<p>A west-facing sliding door or a low-emissivity window near a Reunion pool enclosure can reflect enough concentrated sunlight to soften nearby turf, since polyethylene starts to give in the 175 to 200°F range that reflected glare can reach on a bright afternoon. Checking the glass on the house side of the lanai before finalizing the turf layout catches this before a scorched patch shows up months later rather than after.</p>"),
        ("Turf that survives a rental home's pool traffic",
         "<p>On a Reunion vacation home, the pool deck sees a different pattern of use than a family's own backyard: several groups of guests a month, wet feet, pool floats dragged across the turf, and no single person keeping an eye on wear day to day. A heavier face weight and a secured, glued edge hold up better under that kind of rotating traffic than a lighter residential-grade product would, even though the base construction underneath is the same either way.</p>"),
    ],
    "scenario": (
        "Say you have a screened pool deck",
        f"<p>Say you have a 450 sq ft strip of turf planned around a pool inside a screened Reunion lanai, on a concrete deck that needs the drainage underlay and a fully glued perimeter. At the upper half of the {price('residential')} range, that runs roughly $6,800 to $8,100, close to $15 to $18 a foot once the underlay and glue-down labor are figured in versus the $11 to $16 a plain open-ground lawn would run. A west-facing slider two rooms over gets checked for glare before the layout is set, since a scorched strip near that kind of glass would otherwise show up as a surprise the first hot week after installation rather than during the walkthrough. For a home running as a managed rental, we also plan the seam layout to keep the highest-traffic path from the door to the pool ladder on a single, well-secured piece rather than a seam that sees the most foot traffic of any spot in the yard.</p>"
    ),
    "faqs": [
        faq("Does turf around a Reunion pool need a permit separate from the lawn?",
            "Not typically for the turf itself, though work touching the pool enclosure, drainage or an irrigation head can trigger its own review from Osceola County depending on scope. Ask the Building Department for a specific address."),
        faq("Can I install turf on the outside of the pool cage in Reunion too?",
            f"Yes, and that section behaves like a standard lawn on soil rather than the on-slab build inside the cage; see {svc('pool', 'the pool and lanai turf page')} for how the two areas differ."),
    ],
    "sources": ALL_SRC,
}

# ---------------------------------------------------------- str
LOCAL["str"] = {
    "title": "Vacation Rental Turf for Reunion Short-Term Homes",
    "meta": f"Vacation-rental turf in Reunion, FL runs {price('residential')} per sq ft installed, as of September 2026. STRPD zoning and turnover-proof product choices for managed homes.",
    "h1": "Turf built for Reunion's guest turnover",
    "lede": capsule(f"Turf for a Reunion vacation rental prices at the standard {price('residential')} per square foot, typically {price('residential', True)}, as of September 2026, since the material and base don't change for a managed home. What changes is the spec: a lawn that has to photograph well and hold up between one guest group checking out and the next one checking in, usually with nobody local watching it in between."),
    "sections": [
        ("Zoning that already expects rental use",
         f"<p>Osceola County zones short-term rental activity through a Short Term Rental Planned Development designation, and a large share of Reunion sits inside that framework, which is part of why so much of the resort's housing stock runs as managed rentals rather than year-round residences {ext('https://www.osceola.org/My-Property/Zoning-and-Land-Use/Zoning-Designation/STRPD', 'osceola.org')}. That zoning status doesn't change anything about the turf standard itself; it just means the property manager, not necessarily the owner, is often the one coordinating the install and the review submittal.</p>"),
        ("Choosing a product that survives a booking calendar",
         "<p>A rental home's yard sees a rotating set of guests who didn't pick the landscaping and won't be the ones dealing with a worn patch six months later, so we lean toward a heavier face weight and a denser stitch on the paths guests actually walk, from the driveway to the pool gate, rather than spreading the same light-duty product evenly across the whole lot. A photo-ready lawn that stays flat and green between cleanings matters more for a listing's reviews than it does for most owner-occupied yards.</p>"),
        ("One less thing for a manager to schedule",
         f"<p>Once a Reunion rental's lawn goes synthetic, the in-ground irrigation heads under it get capped under the state's turf standard, which means the watering schedule Toho assigns by address no longer applies to that section of the yard at all {src('dep-rule', "the state's capping requirement")}. For a property manager juggling turnover across several Reunion addresses, one less irrigation zone to track between guest stays is a real, if small, operational win, on top of the yard simply not going brown during a slow booking week.</p>"),
    ],
    "scenario": (
        "Say you manage a rental with a 900 sq ft backyard",
        f"<p>Say you manage a Reunion rental with a 900 sq ft backyard that currently turns brown between waterings when the booking calendar is light and nobody's requesting extra irrigation. At {price('residential')} a foot, converting it runs roughly $7,200 to $16,200, with most jobs this size landing near {price('residential', True)} a foot, or about $9,000 to $14,400, plus a modest premium for the heavier-duty product on the main walking path from the gate to the pool deck. Once the heads are capped, that yard no longer depends on someone remembering to run a hose or request a mid-stay watering visit, and the association submittal for a rental home follows the same review process as an owner-occupied one, just routed through whoever holds power of attorney or management authority for the account.</p>"
    ),
    "faqs": [
        faq("Can a property manager submit the ARC application instead of the owner?",
            "Usually, if the manager has documented authority on file with the association. Check with the resort's property owners association about what paperwork it needs before assuming a manager can submit on the owner's behalf."),
        faq("Does turf reduce water bills on a Reunion rental with bundled utilities?",
            f"For sections where water and sewer are folded into the association fee rather than billed by usage, the savings show up as reduced irrigation demand on the shared system rather than a lower individual bill, which still matters for a community managing water costs overall. {svc('str', 'The vacation rental turf page')} covers product choices for a high-turnover yard."),
    ],
    "sources": ALL_SRC,
}

# ---------------------------------------------------------- commercial
LOCAL["commercial"] = {
    "title": "Commercial Turf for Reunion Clubhouses & Amenities",
    "meta": "Commercial turf around Reunion's clubhouse and amenity grounds is quoted per job as of September 2026, routed through the CDDs rather than the county.",
    "h1": "Turf for Reunion's shared clubhouse and amenity grounds",
    "lede": capsule("Commercial turf around a Reunion clubhouse, pool deck or amenity building is quoted per job rather than off a single per-foot range, since scope varies with drawings and site access. It's a narrower market for us here than a typical strip mall or apartment complex, because most of Reunion's shared grounds already answer to the community development districts or the resort association's own landscaping contracts."),
    "sections": [
        ("Who actually commissions commercial turf in Reunion",
         "<p>Reunion East and Reunion West Community Development Districts, not individual homeowners, hold and maintain the roads, entry gatehouses and shared recreational facilities that make up the resort's common ground, so a commercial turf project around one of those amenity areas typically starts with the district's facilities staff rather than a homeowner's request. That's a different intake path than a residential job, and it usually means drawings, a bid process and a district board sign-off before any turf goes down.</p>"),
        ("Where turf fits around a clubhouse or pool deck",
         "<p>Low-traffic strips around a clubhouse entrance, shaded patio seating and narrow planting borders that natural grass struggles to hold under heavy foot and cart traffic are where commercial turf tends to make sense on a resort property, more than as a wholesale replacement for open lawn areas that golfers and guests cross regularly. Product choice for those areas leans toward a denser, heavier turf built for continuous foot traffic rather than the residential blends used in a backyard.</p>"),
        ("A small but real corner of this market",
         "<p>Compared with the volume of residential and rental-home jobs we see across Reunion, commercial work tied to the clubhouse or amenity grounds is a smaller, more occasional category in this particular community, usually a single larger project rather than a recurring stream of small jobs. We'll say that plainly rather than suggest otherwise: it's a real service here, just not the one Reunion calls us about most often.</p>"),
    ],
    "scenario": (
        "Say a district asks for a bid on a shaded courtyard",
        f"<p>Say a Reunion community development district asks for a bid on a 2,200 sq ft shaded courtyard between a clubhouse and a fitness building, where grass has struggled under constant foot traffic and afternoon shade from the structure. Because the job runs through a district procurement process rather than a homeowner's request, the quote covers drawings review, a heavier-duty commercial-grade turf spec, and site logistics around active amenity hours, none of which fit neatly into a per-square-foot residential number. A project like this usually takes longer to move from bid to installation than a backyard job simply because of the approval steps involved, even though the physical work itself, once scheduled, follows the same base-and-turf sequence as any other job.</p>"
    ),
    "faqs": [
        faq("Do individual Reunion homeowners ever need commercial-grade turf?",
            f"Occasionally, for a heavily trafficked side path or a rental home's pool deck that sees constant guest turnover, though most residential jobs use standard residential-grade product rather than the commercial spec described on {svc('commercial', 'the commercial turf page')}."),
        faq("Who pays for turf around a Reunion CDD amenity area?",
            "That's a district budget decision, funded through the assessments the community development district levies on property within its boundaries, not something an individual homeowner is billed for directly."),
    ],
    "sources": ALL_SRC,
}

# ---------------------------------------------------------- sports
LOCAL["sports"] = {
    "title": "Sports & Fitness Turf in Reunion, FL",
    "meta": "Sports and fitness turf in Reunion, FL is quoted per job, September 2026: a niche market next to three championship courses, from sled tracks to bocce.",
    "h1": "Backyard sports turf beside three golf courses",
    "lede": capsule("Sports and fitness turf in Reunion, a bocce court, a home-gym sled track or a small fitness pad, is quoted per job rather than a single price range, since layout and product vary more than a lawn does. It's a genuinely small market in a community where golf already dominates the athletic identity of the place."),
    "sections": [
        ("Golf already owns the sports conversation here",
         f"<p>With three championship courses running past 6,900 yards each on the same property {ext('https://www.reunionresort.com/golf/courses', 'reunionresort.com')}, a Reunion homeowner looking for a competitive outlet in the yard is a rarer request than in a community without that kind of golf already built in. The backyard sports turf we do install in Reunion tends to be a fitness accessory, a sled track for a home gym or a small putting-adjacent chipping pad, rather than a full court or field.</p>"),
        ("What actually gets built when it does",
         "<p>A home-gym sled track needs a firm, low-pile turf glued or nailed flat over a compacted base, built to handle a weighted sled dragged repeatedly across the same strip rather than foot traffic alone, which is a different wear pattern than any lawn sees. A backyard bocce court, less common but not unheard of on a larger Reunion lot, needs a level, contained bed with edging tight enough to keep the playing surface true.</p>"),
        ("Space is the real constraint on a Reunion lot",
         "<p>Between the pool, the screened lanai and whatever landscaping the association expects to see, many Reunion backyards simply don't have the open run of flat ground a sports surface needs, which is the practical reason this stays a small category here regardless of interest. A sled track fits into a narrow side strip where a bocce court usually can't.</p>"),
    ],
    "scenario": (
        "Say you want a sled track along a side yard",
        f"<p>Say you have a 6-by-40-foot side strip beside a Reunion home, about 240 sq ft, that isn't wide enough for much else and gets quoted for a home-gym sled track. Because the base needs to handle a loaded sled dragged back and forth rather than just foot traffic, the build uses a denser compaction pass and a low-pile, high-durability turf glued at the edges rather than staked, and the whole job is priced from a site visit rather than a published per-foot number given how specialized the wear pattern is. A strip this size and shape usually clears association review faster than a highly visible backyard project, since it sits along a side fence line rather than facing the street or a golf course.</p>"
    ),
    "faqs": [
        faq("Is a backyard sports court realistic on a typical Reunion lot?",
            "Rarely for a full court. Most Reunion lots are sized around the pool, lanai and landscaping the association expects, leaving room for a narrow feature like a sled track more often than a full-size court or field."),
        faq("Does sports turf need a different base than a lawn?",
            f"Usually a denser compaction and sometimes a firmer product, since it's built to handle repeated, concentrated wear in one spot rather than distributed foot traffic; see {svc('sports', 'the sports and fitness turf page')} for the range of builds we quote."),
    ],
    "sources": ALL_SRC,
}

# ---------------------------------------------------------- pavers
LOCAL["pavers"] = {
    "title": "Turf & Pavers for Reunion Driveways and Pool Decks",
    "meta": "Turf-between-pavers work in Reunion, FL is quoted per job as of September 2026. Ribbon strips and paths for the resort's paver-heavy driveways and pool decks.",
    "h1": "Turf ribbons for Reunion's paver driveways and decks",
    "lede": capsule("Turf set between pavers in Reunion, a driveway ribbon, a stepping-stone path or a border strip around a pool deck, is quoted per job rather than a per-foot lawn price, since the paver layout drives most of the cost. Paver hardscape is close to standard across Reunion's builder-grade driveways and pool surrounds, which makes this a regular finishing request rather than an unusual one."),
    "sections": [
        ("Why paver-heavy yards are common here",
         f"<p>Reunion's builder palette leans on paver driveways, walkways and pool-deck borders more than poured concrete, a choice shared with vacation-home builders in nearby {city('davenport', 'Davenport')}, which means a lot of the outdoor square footage on a given lot is hardscape rather than open ground before any turf conversation even starts. Turf ribbons between those pavers soften the look without pulling out material that's already there.</p>"),
        ("Narrow strips need a different base approach",
         "<p>A ribbon of turf running between paver rows on a driveway is rarely wider than a foot or two, which means the base underneath gets built and compacted in a much narrower channel than a lawn would, often by hand rather than machine. Getting the finished turf height to sit flush with the surrounding paver surface, not proud of it or sunk below it, matters more on a narrow strip than it does across an open lawn, since a small height mismatch is far more visible in a tight ribbon.</p>"),
        ("Edging that holds up against paver joints",
         "<p>Where turf meets a paver edge, the seam has to resist the paver's polymeric sand or mortar joint shifting over time, which is a different edge condition than turf meeting soil or a bender board. We secure that edge with an approach built for the paver's own joint material rather than the standard staked perimeter used on an open lawn, so the ribbon doesn't work loose as the pavers settle.</p>"),
    ],
    "scenario": (
        "Say you have a paver driveway with bare joints",
        f"<p>Say you have a Reunion driveway with two 18-inch-wide paver borders running alongside the main drive, currently bare polymeric sand that's washed out in spots after repeated Florida storms, totaling about 140 sq ft between both strips. Because the work is narrow-channel base prep and edge-matched turf rather than an open lawn build, it's priced from a site visit that accounts for the paver height, the joint condition and how much hand labor the access requires, not from a per-square-foot lawn number. A project like this usually takes less than a day for a crew already familiar with paver-adjacent turf work, since the footprint is small even though the detailing is more careful than a wide-open yard.</p>"
    ),
    "faqs": [
        faq("Does turf between pavers need association approval in Reunion?",
            "Often yes, since it changes the visible finish of the driveway or walkway, which is exactly the kind of exterior change the resort's architectural review process covers."),
        faq("Can turf ribbons replace polymeric sand joints entirely?",
            f"For wider borders, yes; for the narrow joint lines between individual pavers, sand or mortar usually stays the practical choice. See {svc('pavers', 'the turf and pavers page')} for where the line falls."),
    ],
    "sources": ALL_SRC,
}

# ---------------------------------------------------------- repair
LOCAL["repair"] = {
    "title": "Turf Repair in Reunion: Seams, Edges and Golf-Ball Dents",
    "meta": "Turf repair in Reunion, FL is quoted per visit as of September 2026: open seams, lifted edges and the occasional golf-ball dent on fairway-backing lots.",
    "h1": "Fixing turf on Reunion's fairway-adjacent yards",
    "lede": capsule("Turf repair in Reunion, open seams, lifted edges, a melted spot near reflective glass, is quoted per visit as of September 2026 rather than a flat rate, since the fix depends on what's actually wrong. One repair call we get here that's less common elsewhere: turf dented or scuffed by an errant golf shot on a lot backing one of the resort's three fairways."),
    "sections": [
        ("Golf-ball impact on fairway-backing lots",
         "<p>A lot that backs any of Reunion's three courses occasionally takes a stray shot into the yard, and turf can show a compressed dent or a scuffed patch where a ball lands hard on a section without much give underneath. That's a narrower, more local repair reason than the seam and edge failures we see everywhere, and fixing it usually means working infill back into the compressed spot and brushing the pile upright rather than replacing the section outright, unless the impact tore the backing.</p>"),
        ("Screen-enclosure edges that work loose",
         "<p>Turf glued along a pool cage's concrete perimeter, common across Reunion's screened lanais, can start to lift at the edge as the adhesive ages or as the concrete itself shifts slightly with seasonal temperature swings. That lifted edge is a different repair than a staked lawn perimeter coming loose in soil, since it calls for re-gluing to a clean, dry slab rather than resetting a stake, and it's worth catching early before foot traffic near the pool works the gap wider.</p>"),
        ("Seams that open under rental-home traffic",
         "<p>On a managed rental with steady guest turnover, the seam along a well-worn path, from a patio door to a pool gate, sees more repeated foot traffic than the same seam would in an owner-occupied yard used more lightly, which can open a taped seam faster than it would elsewhere. Reinforcing that specific seam with a stronger adhesive method during a repair visit, rather than just re-taping it the way it was originally done, tends to hold up better against the same traffic pattern going forward.</p>"),
    ],
    "scenario": (
        "Say a stray shot leaves a compressed patch",
        f"<p>Say a Reunion homeowner backing the Nicklaus course finds a roughly 8-inch compressed patch in the backyard turf after a ball lands hard during weekend play, along with a seam nearby that's started to peel back about a foot. A repair visit for both issues together, brushing infill back into the compressed spot and re-securing the peeling seam with fresh adhesive, is quoted from photos or a short site visit rather than a fixed menu price, since the seam condition varies more than the golf-ball dent does. Most calls like this get scheduled within the week, faster than a full installation, since the crew is working on an existing base rather than building one from scratch.</p>"
    ),
    "faqs": [
        faq("Can a golf-ball dent in turf be fixed without replacing the section?",
            "Usually yes, if the backing itself isn't torn. Working infill back into the compressed area and brushing the pile upright resolves most impact dents without cutting out and reseaming a patch."),
        faq("How fast can a Reunion repair be scheduled?",
            f"Faster than a new install in most cases, since there's no base or drainage work involved, though the exact timeline depends on the scope; see {svc('repair', 'the turf repair page')} for what we look at during a repair visit."),
    ],
    "sources": ALL_SRC,
}

# ---------------------------------------------------------- cleaning
LOCAL["cleaning"] = {
    "title": "Turf Cleaning for Reunion Rental Turnovers",
    "meta": "Turf cleaning in Reunion, FL is quoted per visit as of September 2026. Power brooming and pet-odor treatment timed to a rental home's turnover schedule.",
    "h1": "Turf cleaning built around a rental's turnover schedule",
    "lede": capsule("Turf cleaning in Reunion, power brooming, pet-odor treatment, infill top-ups, is quoted per visit as of September 2026 based on yard size and how long it's been since the last service. A lot of that work here runs on a rental home's booking calendar rather than a homeowner's own schedule, which changes when the visit needs to happen more than what the visit involves."),
    "sections": [
        ("Cleaning that fits between guest stays",
         "<p>A Reunion rental's turf often needs attention timed to a gap between bookings rather than a fixed monthly schedule, since a yard that looked fine after the last guest checked out can pick up sand, leaves or pet hair from a group with a dog before the next arrival. Coordinating a cleaning visit with a property manager's turnover window, rather than a standing calendar date, is common for this community in a way it isn't for most owner-occupied streets.</p>"),
        ("Pet-odor treatment for a rotating cast of guest dogs",
         "<p>Pet-friendly rental listings bring a rotation of different dogs through the same yard month to month, which builds up odor differently than a single household pet using the same turf every day. A deeper flush-and-treat pass, working an enzymatic cleaner down through the infill rather than a surface rinse alone, tends to hold up better between one guest's dog and the next than a quick hose-down does.</p>"),
        ("Debris under mature canopy on the older streets",
         f"<p>On Reunion's older interior sections where oak canopy has had decades to fill in, turf collects leaf litter and acorns faster than it does on the newer, more open streets, and that debris breaking down into the infill can slow drainage right where a Central Florida storm needs it working fastest. A regular power-broom pass clears that buildup before it compacts; {post('oak-leaves-and-debris-on-artificial-turf', 'more on managing leaf and pine debris on turf')} covers the seasonal pattern in more detail.</p>"),
    ],
    "scenario": (
        "Say a rental needs a quick turnover clean",
        f"<p>Say a Reunion rental has a two-day gap between a guest group that brought a dog and the next family checking in, and the 700 sq ft backyard needs a fast pet-odor treatment and power broom before the next arrival. That kind of quick-turnaround visit is quoted and scheduled around the specific gap rather than a standing monthly plan, since rental turnover windows vary week to week depending on the booking calendar. A yard this size with moderate pet traffic typically takes a couple of hours for a thorough pass, brushing the infill, treating any odor spots and clearing loose debris, well within a same-day or next-day turnaround most managers need between bookings.</p>"
    ),
    "faqs": [
        faq("Can turf cleaning be scheduled around a specific checkout date?",
            "Yes, and for Reunion rentals that's often the most practical way to book it, coordinating the visit to land in the gap between one guest's departure and the next arrival rather than a fixed calendar date."),
        faq("How often does rental turf need a deeper pet-odor treatment?",
            f"More often than an owner-occupied pet yard, typically, since a rotating set of dogs uses the same turf month to month; see {svc('cleaning', 'the turf cleaning page')} for how that schedule compares to a standard household visit."),
    ],
    "sources": ALL_SRC,
}

# ---------------------------------------------------------- replacement
LOCAL["replacement"] = {
    "title": "Turf Replacement for Reunion's Older Phases",
    "meta": "Turf replacement in Reunion, FL is quoted per job as of September 2026, close to a new install minus reusable base. Early-phase lawns are reaching end of life.",
    "h1": "Replacing first-generation turf in Reunion's earliest phases",
    "lede": capsule("Turf replacement in Reunion, tearing out a worn system and correcting the base before laying new material, prices close to a new install minus whatever base can be reused, quoted per job as of September 2026. Reunion's earliest phases, approved as a Development of Regional Impact back in 1992, are old enough now that some of the first turf lawns installed on those streets are reaching the end of a normal service life."),
    "sections": [
        ("Housing age tells you where to look first",
         f"<p>Osceola County has tracked Reunion Resort & Club of Orlando's buildout against a 2031 deadline since the county approved it as a Development of Regional Impact in 1992 {ext('https://www.osceola.org/Doing-Business/Community-and-Economic-Development/DCIs-and-DRIs/Reunion-Resort-Club-of-Orlando-DRI', 'osceola.org')}. That long a build-out window means Reunion's housing stock spans three decades of construction on the same property, and a turf system installed on one of the earliest streets not long after those first homes closed is a different replacement conversation than one installed five years ago on a newer section.</p>"),
        ("Why rental wear shortens the replacement clock",
         "<p>A turf lawn on a managed rental sees more concentrated foot traffic over its life than the same product would on an owner-occupied home used more lightly, simply because of how many different guest groups pass through a season, so the fiber can mat down and lose its upright look faster than the manufacturer's general lifespan estimate would suggest. That doesn't mean the base underneath needs rebuilding at the same pace; often the existing rock layer is still sound and only the surface and infill need replacing.</p>"),
        ("What gets reused and what doesn't",
         "<p>A replacement job starts with checking whether the existing washed crushed-rock base is still compacted, draining and free of the fines that would have bound it into a crust over time; if it's holding up, we build the new turf on top of it rather than tearing the base out along with the old surface, which is what keeps replacement priced below a full ground-up install. Irrigation heads capped under an older system usually stay capped, since the reason they were capped in the first place, the state's restriction on watering synthetic turf, hasn't changed.</p>"),
    ],
    "scenario": (
        "Say you have a first-generation lawn from an early phase",
        f"<p>Say you have a 1,200 sq ft Reunion backyard on one of the resort's earliest streets, with turf that's showing matted, flattened fiber and a couple of lifted seams after years of use as part of a managed rental. Because the existing base checks out as still compacted and draining well, the replacement quote covers tearing out and disposing of the old surface, adjusting the base where it's settled unevenly, and laying new turf and infill, typically pricing at or slightly below what a ground-up install on the same footprint would run since the rock layer doesn't need rebuilding from scratch. A job like this usually finishes faster than a first-time install for the same reason, since a full day of demo, base repair and new turf replaces what would otherwise be a two-stage excavation and build process.</p>"
    ),
    "faqs": [
        faq("How do I know if my Reunion turf needs full replacement or just a repair?",
            f"A few loose seams or a small worn patch usually points to a repair visit; widespread matting, a base that's stopped draining, or fiber that's lost its upright feel across most of the yard points to replacement. See {svc('replacement', 'the turf replacement page')} for the signs we look for."),
        faq("Does replacing turf on an older Reunion lot need a new association submittal?",
            "Often a lighter one than a first-time install, since the yard's overall look isn't changing, but it's worth checking with the resort's property owners association before assuming a straightforward swap needs no paperwork at all."),
    ],
    "sources": ALL_SRC,
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
