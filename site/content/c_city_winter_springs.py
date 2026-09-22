# -*- coding: utf-8 -*-
"""Winter Springs, FL (tier 2, Seminole County). Researched September 2026: Winter Springs Building
Division and its Civic Access/EnerGov portal; Public Works & Utilities irrigation schedule; the
Tuscawilla Homeowners Association and Tuscawilla Country Club; Lake Jesup and the Cross Seminole
Trail; Census population; USDA flatwoods soils already verified for Seminole County in c_counties.py."""
from _helpers import page, capsule, sec, table, faq, a, svc, city, county, src, ext, price, post
from _cityservice import cityservice_pages

SLUG = "winter-springs"

BUILDING = ("Winter Springs Building Division — Building & Permits", "https://www.winterspringsfl.org/cd/page/building-permits")
UTIL = ("City of Winter Springs — Public Works & Utilities", "https://www.winterspringsfl.org/publicworks")
WATERING = ("City of Winter Springs — Watering Restrictions", "https://www.winterspringsfl.org/publicworks/page/watering-restrictions")
RECLAIMED = ("City of Winter Springs — Reclaimed Water", "https://www.winterspringsfl.org/publicworks/page/reclaimed-water")
TUSCAWILLA_HOA = ("Tuscawilla Homeowners Association — about the community", "https://tuscawilla.org/about-tuscawilla")
TUSCAWILLA_CC = ("Tuscawilla Country Club", "https://www.tuscawillacc.com/course/")
HISTORY = ("City of Winter Springs — The History of Winter Springs", "https://www.winterspringsfl.org/166/The-History-of-Winter-Springs")
LAKE_JESUP = ("Wikipedia — Lake Jesup", "https://en.wikipedia.org/wiki/Lake_Jesup")
CROSS_SEM_TRAIL = ("Seminole County — Cross Seminole Trail", "https://www.seminolecountyfl.gov/departments-services/parks-recreation/parks-trails-and-natural-lands/trails/cross-seminole-trail")
CENTRAL_WINDS = ("Winter Springs Parks Department — Central Winds Park", "https://www.winterspringsfl.org/parksrec/page/parks-department-central-winds-park")
CENSUS_WS = ("U.S. Census Bureau QuickFacts — Winter Springs city, Florida", "https://www.census.gov/quickfacts/fact/table/winterspringscityflorida/PST045225")
SJRWMD = ("St. Johns River Water Management District — watering restrictions", "https://www.sjrwmd.com/wateringrestrictions/")

SRC = [BUILDING, UTIL, WATERING, RECLAIMED, TUSCAWILLA_HOA, TUSCAWILLA_CC, HISTORY, LAKE_JESUP,
       CROSS_SEM_TRAIL, CENTRAL_WINDS, CENSUS_WS, SJRWMD, "usda-wss", "dep-rule", "fs125572", "fs7203045"]

PERMITS_SEM = ("/laws/permits/seminole-county/", "Seminole County permit rules for turf")
HB683 = ("/laws/florida-hb-683/", "HB 683 and DEP Rule 62-308.100")
HOA = ("/laws/hoa-rules/", "What a Florida HOA can and can't restrict")

# ============================================================== HUB
HUB = page(
    "/areas/winter-springs/", "city",
    "Synthetic Turf Installers in Winter Springs, FL",
    "Artificial turf work in Winter Springs, FL: the Building Division, Tuscawilla's golf-community lots, watering rules and soil facts, checked September 2026.",
    "Artificial grass and synthetic turf work in Winter Springs, Florida",
    capsule(f"Installed synthetic lawns in Winter Springs cost {price('residential')} per square foot as of September 2026, the same Central Florida range whether the address sits inside Tuscawilla or one of the older streets that came before it. The city grew up around Tuscawilla, a roughly 3,500-acre planned golf community whose homeowners' association has run its own architectural review since 1977, layered on top of whatever the city's own Building Division already requires."),
    "".join([
        sec("A city built in two distinct waves",
            f"<p>Winter Springs sits about 29 miles from downtown Kissimmee and incorporated in 1959, but stayed a small crossroads town for more than a decade before Tuscawilla's golf-course development took hold and the population climbed toward its current size ({ext(HISTORY[1], 'The History of Winter Springs')}). That leaves two housing eras inside the same city limits: modest homes from the years right after incorporation, and the planned streets built around Tuscawilla Country Club's 18-hole course from the late 1970s onward.</p>"
            + f"<p>Nearly all of Seminole County's second-smallest-by-area footprint already sits inside a city limit, and Winter Springs is no exception: there's little unincorporated land nearby, so almost every address here answers to the city's own {ext(BUILDING[1], 'Building Division')} rather than the county. That, and Tuscawilla's homeowners' association, are the two local layers that shape how a job gets planned.</p>"),
        table("Winter Springs neighborhoods and how we plan around them",
              ["Where in town", "What the yard looks like", "How the plan changes"],
              [["Tuscawilla fairway lots", "Curved, larger, backing the golf course", "HOA architectural submittal; layout often works around a view corridor"],
               ["Tuscawilla interior streets, off the course", "1980s-90s family lots, fenced", "Same association review; fewer sightline constraints"],
               ["Pre-Tuscawilla neighborhoods near the city center", "Smaller, older, built soon after 1959", "Often no HOA at all; more straightforward permitting"],
               ["Lots along the Cross Seminole Trail corridor", "Backing a shared-use path rather than a street", "Rear-yard visibility from the trail is worth checking against HOA rules"],
               ["Lower ground toward Lake Jesup", "Flatter, closer to the water table", "Extra attention to base depth and the state's 10-ft waterbody setback"]],
              "The neighborhood changes the plan, not the price; every row above still quotes inside the same Central Florida range."),
        sec("Does Winter Springs require a permit for synthetic turf?",
            f"<p>We searched Winter Springs' code for a synthetic-turf section and came up empty, and the city hasn't published a stated permit answer for a residential lawn conversion, at least as of September 2026. {ext(BUILDING[1], 'The Winter Springs Building Division')}, at 1126 East State Road 434, takes questions at 407-327-5963 through a Civic Access portal built on Tyler's EnerGov system rather than a paper counter. Worth confirming anyway: the lawn's old irrigation heads still need capping, something {a(HB683[0], HB683[1])} requires outright even where the code says nothing about turf.</p>"
            + f"<p>Because so little of {county('seminole', 'Seminole County')} sits outside a city boundary, the county's own building department rarely has jurisdiction over a Winter Springs address, and we don't have a page written for the city's code the way we do for {a(PERMITS_SEM[0], 'the county')}. An unincorporated result on a parcel search reads that county page instead. A Tuscawilla ARC approval, discussed below, is a separate step that doesn't substitute for either permit.</p>"),
        sec("Water rules and the district behind them",
            f"<p>Winter Springs runs its own water utility through Public Works & Utilities rather than buying through the county, and its schedule follows the season: one watering day a week during Eastern Standard Time and two days a week once daylight saving time starts, with no watering between 10 a.m. and 4 p.m. ({ext(WATERING[1], 'Winter Springs watering restrictions')}). Reclaimed-water customers get a better deal, two days a week year-round, and Utility Billing at 407-327-5996 has the specific day assignments by address ({ext(RECLAIMED[1], 'Winter Springs Reclaimed Water')}). The city, like the rest of {county('seminole')}, sits under the St. Johns River Water Management District, which kept a tightened Phase III shortage order running through 2026 ({ext(SJRWMD[1], 'SJRWMD watering restrictions')}).</p>"
            + f"<p>A converted lawn stops caring which of those days applies the moment its old sprinkler heads are capped, a step {src('dep-rule', 'the state standard')} requires regardless of the season or the district in force. What's left of the schedule still governs whatever grass, mulch beds or golf-course rough stays around the edges of that yard.</p>"),
        sec("Tuscawilla: a golf community with its own review, not its own turf rule",
            f"<p>Tuscawilla is the defining feature of Winter Springs: a roughly 3,500-acre planned community built around an 18-hole course at {ext(TUSCAWILLA_CC[1], 'Tuscawilla Country Club')}, with its own homeowners' association running architectural review since 1977 ({ext(TUSCAWILLA_HOA[1], 'Tuscawilla Homeowners Association')}). We looked for a published governing document naming sod, ground cover or synthetic turf directly and didn't find one posted as of September 2026, so a turf application goes in as a general exterior-change submittal rather than a pre-cleared category.</p>"
            + f"<p>What the association can and can't restrict still runs through the same statute as any other Florida HOA: a backyard invisible from the street or an adjacent lot is outside what an architectural committee can weigh in on, fairway frontage or not ({a(HOA[0], HOA[1])}). A synthetic green on the fairway-facing side of a lot is the one layout where visibility genuinely comes up, since the course counts as an adjoining view the way a neighbor's yard would.</p>"),
        sec("Lake Jesup, the Cross Seminole Trail and Winter Springs' soil",
            f"<p>Lake Jesup, Seminole County's largest lake, named in 1837 for General Thomas Jesup, forms part of the city's northern edge, and the Cross Seminole Trail runs along State Road 434 through town on its way from Oviedo to Sanford, with a 2007 overpass that let the path finally cross SR 434 inside Winter Springs itself ({ext(LAKE_JESUP[1], 'Lake Jesup')}; {ext(CROSS_SEM_TRAIL[1], 'Cross Seminole Trail')}). Ground closer to the shoreline is mapped mostly to Myakka and Basinger, both poorly drained and both prone to pooling in a low spot for days after a hard rain, part of the same flatwoods family that covers the rest of {county('seminole', 'Seminole County')} ({src('usda-wss', 'USDA Web Soil Survey')}).</p>"
            + f"<p>That geography doesn't change the published price, but it does change base planning: a lawn on the lower ground toward Lake Jesup gets built at the fuller end of the state's washed-rock depth range, and a lot inside the state's 10-foot waterbody setback plans its layout around that line first. The city's population has grown to roughly 39,822 as of the Census Bureau's 2024 estimate ({ext(CENSUS_WS[1], 'Census QuickFacts')}).</p>"),
        "<!--AUTO:city-services-->",
    ]),
    faqs=[
        faq("Does the Tuscawilla Homeowners Association have a written rule on artificial turf?",
            "We looked for one and didn't find a published governing document that names synthetic turf, sod or ground cover specifically as of September 2026. A submittal there goes in as an ordinary exterior-change request, with a product sample and a site plan, rather than against a known clause."),
        faq("What do the best turf installers near you in Winter Springs check before quoting a Tuscawilla lot?",
            "Whether the yard faces the golf course, since that changes the HOA-visibility question, and whether the ground sits on the lower, lake-facing side of town, since that changes how deep the base needs to run. A contractor who asks both has actually looked at the lot rather than quoting off an address alone."),
        faq("How far is Winter Springs from your Kissimmee base, and does that change the price?",
            "About 29 miles by straight line, the same distance as Oviedo next door. Distance changes scheduling, not the published Central Florida price range."),
        faq("Which water management district covers Winter Springs?",
            "The St. Johns River Water Management District, the same one that covers most of Seminole County. The city bills its own water separately from the district, so the specific watering days come from the city's utility rather than the district's regional number alone."),
    ],
    sources=SRC, city=SLUG, crumbs=[("Service areas", "/areas/")], crumb="Winter Springs",
    related=[("/areas/seminole-county/", "Turf across Seminole County"), PERMITS_SEM,
             ("/areas/oviedo/", "Turf in Oviedo"), ("/areas/longwood/", "Turf in Longwood"),
             ("/artificial-turf-cost/", "Turf cost tables for Central Florida")])

# ============================================================== LOCAL
LOCAL = {
    "residential": {
        "title": "Artificial Grass Installation in Winter Springs, FL",
        "meta": "Synthetic lawn installation in Winter Springs, FL: Building Division permits, Tuscawilla's architectural review and flatwoods soil, checked 2026.",
        "h1": "Synthetic lawns for Winter Springs, from Tuscawilla to the city center",
        "lede": capsule(f"A residential synthetic lawn in Winter Springs runs {price('residential')} per square foot installed, typically {price('residential', True)}, as of September 2026. Almost every address here falls under the city's own Building Division rather than the county, and a lawn inside Tuscawilla goes through the community's architectural review before the crew ever measures the yard."),
        "sections": [
            ("The Building Division handles almost the whole city",
             f"<p>Because so little of Seminole County sits outside an incorporated city, a Winter Springs address almost never routes through the county's own permitting office. {ext(BUILDING[1], 'The Winter Springs Building Division')} takes calls at 407-327-5963 from 1126 East State Road 434, and applications go through a Civic Access portal rather than a walk-in counter for most of the process. We didn't find a code section naming synthetic turf directly, so a lawn swap gets reviewed against the city's general exterior-work rules rather than a dedicated turf ordinance.</p>"),
            ("What a Tuscawilla submittal actually looks like",
             f"<p>Tuscawilla's homeowners' association has run architectural review since 1977 across the community's roughly 3,500 acres, but we couldn't find a published governing document naming sod, ground cover or synthetic turf as its own category. In practice that means a homeowner submits the same packet any exterior change would need: a product sample, a spec sheet and a simple drawing of where the lawn goes, reviewed under the general standards the association already applies to landscaping changes. A lawn tucked behind a fence and away from the golf course's sightlines is the most straightforward version of that submittal.</p>"),
            ("Building on the flatwoods sand near Lake Jesup",
             f"<p>Ground on the lower, lake-facing side of Winter Springs maps mostly to Myakka and Basinger, part of the same poorly drained flatwoods family found across {county('seminole', 'Seminole County')}, where standing water can linger at grade for days after a summer downpour ({src('usda-wss', 'USDA')}). A lot higher up, away from the lake, still sits on related sand but drains a little faster, which is the kind of difference worth checking address by address rather than assuming one answer covers the whole city.</p>"),
        ],
        "scenario": ("What a 1,100 sq ft yard near the Cross Seminole Trail runs",
                     f"<p>Say a home backing the Cross Seminole Trail corridor has an L-shaped 1,100 sq ft side and back yard, split between a shaded strip along the trail fence and an open section facing the house. At the typical {price('residential', True)} range, that prices between $11,000 and $17,600, with the trail-facing section needing a slightly heavier product since it's the part of the yard visible to trail users rather than just the household. Because the lot sits outside Tuscawilla, there's no association submittal to file, only the city's own permit question if the scope reaches beyond a straightforward lawn swap.</p>"
                     + "<p>A similarly sized yard inside Tuscawilla would add one more step before ordering material: a quick architectural submittal showing the layout, reviewed under the community's general exterior-change standards rather than a rule written for turf specifically.</p>"),
        "faqs": [
            faq("Does a Winter Springs home outside Tuscawilla need any association approval?",
                "Only if that specific neighborhood has its own homeowners' association separate from Tuscawilla's; the pre-1980s neighborhoods near the city center often don't, which simplifies the paperwork to the city permit question alone."),
            faq("Is the flatwoods soil the same everywhere in Winter Springs?",
                "Close, but not identical. Ground closer to Lake Jesup drains more slowly than higher ground elsewhere in the city, which is why a base plan gets checked against the specific address rather than assumed from one description of the city as a whole."),
        ],
        "sources": SRC,
    },
    "pet": {
        "title": "Pet Turf Installation in Winter Springs, FL",
        "meta": "Pet-friendly synthetic turf in Winter Springs, FL for established fenced backyards and Tuscawilla lots, checked September 2026.",
        "h1": "Dog-run turf for Winter Springs' established backyards",
        "lede": capsule(f"Pet turf in Winter Springs runs {price('pet')} per square foot installed, typically {price('pet', True)}, as of September 2026. The city's older, pre-Tuscawilla neighborhoods carry some of the most fully grown-in, fenced backyards on this list, which is exactly the setting a dog run does best in."),
        "sections": [
            ("Dog runs behind decades-old fence lines",
             "<p>Neighborhoods built in the years right after Winter Springs incorporated in 1959 have had six decades for their fencing, hedges and shade trees to mature, and a dog run installed today usually goes into a backyard that's already fully enclosed and screened from the street. That maturity works in a run's favor for the state's HOA-visibility rule, since a yard that's been fenced and landscaped for decades is rarely visible from anywhere but inside the property itself, and it also means the base plan has to route around root systems a newer subdivision wouldn't have yet.</p>"),
            ("Tuscawilla's fenced lots and the fairway exception",
             "<p>Inside Tuscawilla, a dog run on the side or rear of a lot away from the golf course sits behind the same kind of privacy fencing that protects it from an HOA's visibility standard, association review aside. A run that opens toward the fairway is the one layout worth double-checking first, since the golf course counts as a sightline the way a neighboring yard would, and a design kept off that side of the property avoids the question rather than needing an answer to it.</p>"),
            ("Keeping infill working on slow-draining ground",
             f"<p>Winter Springs' lower ground toward Lake Jesup shares the same poorly drained Myakka and Basinger sand as the rest of the lake's shoreline, soil that holds water near the surface longer than higher ground elsewhere in the city ({src('usda-wss', 'USDA')}). A dog run there gets a more open, slightly deeper base than a plain lawn would, since urine and rinse water both need a clear path down through the rock rather than sitting against ground that's already close to saturated for weeks after a summer storm.</p>"),
        ],
        "scenario": ("A 350 sq ft run behind a 1970s Winter Springs home",
                     f"<p>Say a home from the years soon after incorporation has a fully fenced 350 sq ft backyard, shaded by decades-old trees and used daily by one large dog. At the typical {price('pet', True)} range, that prices between $4,200 and $5,600, with root systems from the mature landscaping adding some hand-digging time a newer yard wouldn't need. Because the property predates any homeowners' association in that part of town, there's no architectural submittal to file, only the city's own permit question if the scope goes beyond a straightforward run.</p>"
                     + "<p>The same size run inside Tuscawilla, kept on the side of the lot away from the golf course, would add a quick HOA submittal but otherwise follow the identical base and infill plan.</p>"),
        "faqs": [
            faq("Do older Winter Springs neighborhoods have any HOA at all?",
                "Some do and some don't; it depends on the specific subdivision rather than the city as a whole. A property predating Tuscawilla's 1970s development is the one most likely to have no association layered on top of the city permit."),
            faq("Does a Tuscawilla dog run near the golf course need special sign-off?",
                "It's the layout most worth asking the association about directly, since a run visible from the fairway falls under the same visibility standard a street-facing yard would, while one screened from that view typically doesn't."),
        ],
        "sources": SRC,
    },
    "putting": {
        "title": "Backyard Putting Greens in Winter Springs, FL",
        "meta": "Backyard putting greens in Winter Springs, FL for Tuscawilla fairway lots and flat interior yards, checked September 2026.",
        "h1": "Putting greens for a golf-community backyard in Winter Springs",
        "lede": capsule(f"A backyard putting green in Winter Springs runs {price('putting')} per square foot installed, typically {price('putting', True)}, as of September 2026. Tuscawilla's fairways are real grass the club maintains, not something a homeowner touches, but plenty of the community's own backyards have room for a private green built the same way any Central Florida yard's would be."),
        "sections": [
            ("A private green is a different surface than the fairway next door",
             f"<p>A house backing {ext(TUSCAWILLA_CC[1], "Tuscawilla Country Club's")} course sits beside real turfgrass the club maintains on its own schedule, which has nothing to do with a synthetic green built inside the homeowner's own fence line. The two surfaces meet only at the property boundary, and a backyard green there gets built exactly the way one would anywhere else: a shaped, compacted base with a deliberate pitch, then contoured cuts and fringe turf laid on top of it. The fairway view is a backdrop, not a design constraint on the green itself.</p>"),
            ("Where the HOA's review actually applies",
             "<p>Tuscawilla's association reviews exterior changes generally, and we didn't find a published clause treating a putting green differently from any other landscaping request. What does matter is visibility: a green built on the side of a lot facing the golf course is visible the way a front yard would be under Florida's HOA statute, since the fairway counts as an adjoining view, while a green tucked toward the house or behind existing landscaping usually isn't reviewed on those grounds at all.</p>"),
            ("Grading a flat Winter Springs lot for contour",
             "<p>Most residential lots in Winter Springs, fairway-adjacent or not, are flat enough that a green's rolls and breaks have to be built rather than found in the existing grade. The base still gets a deliberate pitch toward one edge before any contouring goes on top, the same drainage-first sequence any flat Central Florida lot needs, so a green that looks dramatic in its breaks doesn't end up holding water in its low spots after the first real storm.</p>"),
        ],
        "scenario": ("A 600 sq ft green on a Tuscawilla side yard",
                     f"<p>Say a Tuscawilla home has a 600 sq ft side yard that doesn't face the fairway, screened by an existing hedge, and wants a two-tier green with a chipping pad. At the typical {price('putting', True)} range, that prices between $10,800 and $15,000, with the two-tier design adding grading time beyond a single flat surface. Because the layout sits screened from the golf course and the street both, it's unlikely to draw scrutiny under the state's HOA-visibility rule even though the community's own architectural review still applies as a general exterior-change submittal.</p>"
                     + "<p>Moving the same green to the fairway-facing side of the lot wouldn't change the price, but it would put the layout squarely inside what the association can review for visibility, which is worth settling before ordering turf rather than after.</p>"),
        "faqs": [
            faq("Can a Winter Springs homeowner get in trouble for a green that faces the golf course?",
                "Not from the club or the course itself, since a private backyard green doesn't touch the fairway grass at all. The relevant question is only whether Tuscawilla's association, if the community has one over that lot, treats a fairway-facing green as visible under its general review standards."),
            faq("Does a putting green need a different water setback near Lake Jesup?",
                "Only on a lot that's actually near the lake or a connected pond. The state's 10-foot waterbody setback applies to a green the same way it would to any turf area, regardless of whether the lot is inside Tuscawilla."),
            faq("Is Winter Springs' ground too flat for a green with real contour?",
                "No. Contour on a flat lot gets built into the base rather than found in the existing grade, so a flat starting point doesn't limit how much roll or break the finished green can have."),
        ],
        "sources": SRC,
    },
    "playground": {
        "title": "Playground Turf Installation in Winter Springs, FL",
        "meta": "Playground turf for Winter Springs, FL backyards near Central Winds Park, with the state's swing-set infill rule, checked September 2026.",
        "h1": "Backyard play turf for Winter Springs families",
        "lede": capsule(f"Cushioned playground turf in Winter Springs runs {price('playground')} per square foot installed, typically {price('playground', True)}, as of September 2026. Families near the city's 103-acre Central Winds Park still ask for a home play area sized to a specific swing set or trampoline, since a public park across town doesn't cover daily backyard use."),
        "sections": [
            ("Central Winds Park sets the local standard for play surfaces",
             f"<p>{ext(CENTRAL_WINDS[1], 'Central Winds Park')}, Winter Springs' 103-acre flagship park along the Cross Seminole Trail, is the play area most families here already know, even though its own playground surface isn't synthetic turf. A backyard version scaled to one swing set or a small climbing structure is a different project entirely, sized to a specific footprint rather than a park's worth of equipment, and priced accordingly by the square foot rather than by acreage.</p>"),
            ("The infill line between the swing set and the rest of the lawn",
             "<p>Florida's turf standard keeps rubber and other synthetic infill inside the footprint of the playground equipment itself, so a Winter Springs backyard with a swing set gets one infill directly under the frame's fall zone and silica, zeolite or coated sand everywhere else the family walks or sits. A contractor should mark that boundary against the equipment's actual required fall zone before ordering material, not guess at it once installation is underway, since moving the line afterward means pulling turf back up.</p>"),
            ("Play areas on established, shaded Winter Springs lots",
             "<p>A number of the city's older neighborhoods, built up in the decades after 1959, carry mature shade trees that a newer subdivision elsewhere wouldn't have yet, which keeps a play area cooler through a Florida afternoon but also means checking a live oak's drip line before finalizing where a swing set's turf footprint goes. Newer sections built up around Tuscawilla generally have younger trees and more open sun, trading that shade for fewer layout restrictions.</p>"),
        ],
        "scenario": ("A 250 sq ft play area near Central Winds Park",
                     f"<p>Say a family living a short distance from Central Winds Park has a swing set and a sandbox taking up roughly 250 sq ft of their fenced backyard. At the typical {price('playground', True)} range, that prices between $3,000 and $4,750, with the swing set's fall zone, about a third of the total area, getting rubber infill under the equipment and the rest finished in standard silica or coated sand. Because the home sits outside Tuscawilla, there's no architectural submittal ahead of the city's own permit question.</p>"
                     + "<p>The same layout inside Tuscawilla would need a quick HOA submittal first, though the base, pad and infill specification would stay identical either way.</p>"),
        "faqs": [
            faq("Does Central Winds Park's playground use the same turf we install?",
                "We don't know what surface the park itself uses and aren't speaking for the city's own facilities; what we install is a private backyard system built to the state's residential material and infill standards, a separate question from a public park's equipment."),
            faq("Can a Winter Springs HOA require a specific playground turf color or brand?",
                "Florida's turf rule requires green synthetic turf be allowed and leaves brand choice to the homeowner and installer; an HOA in a community with an architectural review, Tuscawilla included, can still ask for a sample as part of that general review process."),
        ],
        "sources": SRC,
    },
    "pool": {
        "title": "Pool & Lanai Turf in Winter Springs, FL",
        "meta": "Turf beside pools and inside screen enclosures in Winter Springs, FL, built for Tuscawilla-era lots and flatwoods drainage, checked 2026.",
        "h1": "Lanai and pool-deck turf for Winter Springs screen enclosures",
        "lede": capsule(f"A lanai or pool-deck turf job in Winter Springs falls in the upper half of the {price('residential')} residential range as of September 2026, since a screened enclosure's small area and narrow doorway access cost more per foot than an open yard. The screened lanai is a fixture of the Tuscawilla-era subdivisions built through the 1980s and 1990s, and the strips of grass around those enclosures are some of the toughest spots on a Winter Springs lot to keep alive."),
        "sections": [
            ("Screened lanais from Winter Springs' Tuscawilla-era growth",
             "<p>Homes built through Tuscawilla's main construction years in the 1980s and 1990s commonly carry a screened pool enclosure with a narrow strip of grass along one or two sides of the deck, shaded enough by the cage that St. Augustine rarely holds up there for long. Turf installed inside that enclosure ties directly into the deck's slab edge, so the crew works the base right up to the concrete's own height rather than leaving a lip or a gap anywhere along it.</p>"),
            ("Drainage where the pool deck meets the base",
             "<p>A screened enclosure sheds water toward a specific low point on its slab, and turf butting up against that edge needs its own drainage underlay so the water leaving the deck doesn't just collect against the new turf instead of passing through it. On the lower ground toward Lake Jesup, where the native soil already holds water closer to the surface, that underlay carries more of the drainage load than it would on a higher, faster-draining lot elsewhere in the city.</p>"),
            ("Anchoring an enclosure's turf against wind and storms",
             "<p>A screened enclosure changes wind behavior around its own edges compared with an open backyard, funneling gusts along the cage's structure in a way that can work at a loosely anchored turf edge faster than it would on an unenclosed lawn. The state's anchoring standard, meant to withstand wind and standing water at every seam and edge, matters as much inside a lanai as it does anywhere else on the property, even though the cage itself offers some shelter from direct rain.</p>"),
        ],
        "scenario": ("A 480 sq ft lanai strip on a 1990s Tuscawilla-area home",
                     f"<p>Say a 1994-built home near Tuscawilla has a screened pool enclosure with a 480 sq ft strip of thin, shaded grass running along two sides of the deck. At the typical {price('residential', True)} range, that prices between $4,800 and $7,680, landing toward the upper end because the crew works through the enclosure's screen door rather than a wide gate, and because the deck-edge drainage underlay adds a line item a plain backyard lawn doesn't carry. Since the strips sit fully inside the fenced, screened enclosure, they're unlikely to draw HOA scrutiny under the visibility standard even where an association's general review still technically applies.</p>"
                     + "<p>A comparable strip on a pre-1970s home near the city center, without a screen enclosure at all, would skip the drainage-underlay step entirely and price toward the lower end of the same range instead.</p>"),
        "faqs": [
            faq("Do Tuscawilla's older screened enclosures need a different base than a newer one?",
                "Not for the base itself; the two-to-four-inch washed crushed rock specification is the same regardless of the enclosure's age. What can differ is the condition of the existing slab edge, which an older enclosure is more likely to need repaired before turf ties into it cleanly."),
            faq("Does turf around a Winter Springs pool need a permit separate from the enclosure itself?",
                "The turf installation itself follows the same permit question as any other lawn project in the city; the screen enclosure, if it needs work of its own, is a separate structure with its own permitting history worth checking before starting."),
        ],
        "sources": SRC,
    },
    "repair": {
        "title": "Artificial Turf Repair in Winter Springs, FL",
        "meta": "Turf repair in Winter Springs, FL for storm-lifted edges near Lake Jesup and Tuscawilla lots, quoted after a site visit, checked 2026.",
        "h1": "Repairing synthetic turf near Tuscawilla and Lake Jesup",
        "lede": capsule("Fixing synthetic turf in Winter Springs comes down to photos or a visit first, never a flat per-foot rate, because a lifted seam, a settled base and washed-out infill each call for a different repair. Lots near Lake Jesup and older Tuscawilla-era enclosures tend to fail in different ways from each other, which is exactly why one number can't cover both."),
        "sections": [
            ("Storm-lifted edges on lower ground toward Lake Jesup",
             "<p>A lawn on the lower, lake-facing side of Winter Springs sees more standing water after a heavy storm than higher ground elsewhere in the city, and an edge that was anchored lightly at installation is usually the first thing to show it. Fixing that means re-anchoring with the fastener spacing the state's wind and flood standard actually calls for, not simply re-gluing the same seam, and checking nearby infill for signs it migrated toward the property's low point during the same event, since both problems often turn up on the same visit.</p>"),
            ("Irrigation retrofits gone wrong on older Tuscawilla systems",
             "<p>A home built during Tuscawilla's main development years often had an elaborate, zoned irrigation system installed with the original landscaping, and capping every head that used to reach a converted turf area correctly, rather than leaving one live by mistake, is a common source of callbacks on older conversions. A repair visit checks the capped zones against the turf's actual footprint before touching anything else, since a single missed head can undo the point of the capping requirement entirely.</p>"),
            ("Base settling under a screened enclosure's turf",
             "<p>Turf laid inside an older screened lanai without enough base depth, or on ground that wasn't fully dry when it was compacted, can develop a visible dip near the deck's edge after a couple of rainy seasons, especially on the flatter, slower-draining ground toward Lake Jesup. Correcting it means pulling the affected section back, adding washed crushed rock to bring the low spot level, and recompacting the layer properly instead of laying fresh turf over ground that's already given way.</p>"),
        ],
        "scenario": ("Re-anchoring a lifted edge after a storm near Lake Jesup",
                     "<p>Say a home on the lower ground toward Lake Jesup has an 18-foot stretch of turf edge that lifted along the back property line after a summer storm, with some infill visibly missing from that same corner. A repair visit checks whether the anchoring simply failed or whether the grade is sending water toward that corner in the first place, since fixing only the edge without correcting the grade means the same failure returns after the next heavy rain. The quote reflects whichever of those two problems the visit finds, which is why an 18-foot lift can cost noticeably more or less to fix depending on the cause.</p>"
                     + "<p>A homeowner who catches the lift right after the storm, before more infill washes out, typically has the less expensive repair path still available.</p>"),
        "faqs": [
            faq("Why does turf repair near Lake Jesup cost more than a repair elsewhere in Winter Springs?",
                "It doesn't automatically; cost follows the cause, not the neighborhood. A storm-related edge failure on lower ground can need more grading correction than the same length of lifted edge on a higher, faster-draining lot, which is what a site visit is for."),
            faq("Can a missed irrigation cap under Tuscawilla turf be fixed without pulling up the whole lawn?",
                "Usually yes. A repair crew can typically access a single missed head through a small cut in the turf near that specific spot rather than removing the entire installation, then reseal the area once the cap is confirmed."),
            faq("Does a homeowners' association need to approve a turf repair the way it would a new installation?",
                "Generally no, since a repair restores an already-approved lawn rather than changing its appearance or footprint, though it's worth a quick check with the association if the repair changes the turf's visible extent."),
        ],
        "sources": SRC,
    },
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
