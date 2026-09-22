# -*- coding: utf-8 -*-
"""Winter Garden, FL (tier 2, Orange County). Building Division, water utility and history facts
researched September 2026 directly from cwgdn.com and wgfl.gov; not reused from c_permits.py or
c_counties.py, which don't cover this city individually. Soil, county-wide water-district and permit-hub
facts reuse the URLs already verified in c_permits.py / c_counties.py for Orange County."""
from _helpers import page, capsule, sec, table, faq, a, svc, city, cs, post, src, ext, price
from _cityservice import cityservice_pages

SLUG = "winter-garden"

WG_BUILDING = ("City of Winter Garden — Building Division", "https://www.cwgdn.com/291/Building")
WG_WATER = ("City of Winter Garden — Water Conservation and irrigation schedule", "https://www.cwgdn.com/351/Water-Conservation")
WG_HISTORY = ("City of Winter Garden — City History", "https://www.cwgdn.com/398/History")
WG_WIKI = ("Wikipedia — Winter Garden, Florida", "https://en.wikipedia.org/wiki/Winter_Garden,_Florida")
SJRWMD_APOPKA = ("St. Johns River Water Management District — Lake Apopka basin", "https://www.sjrwmd.com/waterways/lake-apopka/")
SBW_INFO = ("HOA Bulletin Board — community information, StoneyBrook West, Winter Garden, FL", "https://www.hoabulletinboard.com/hoa/sbwest/about_hoa/")
INDEPENDENCE_INFO = ("Florida Neighborhood Realty — Independence, Horizon West, FL", "https://www.floridaneighborhoodrealty.com/independence-horizon-west-homes-sale/")
CANDLER_OSD = ("USDA NRCS — official series description, Candler series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/C/CANDLER.html")
APOPKA_OSD = ("USDA NRCS — official series description, Apopka series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/A/APOPKA.html")
ORANGE_PA = ("Orange County Property Appraiser — parcel search", "https://ocpafl.org/")

PERMITS_ORANGE = ("/laws/permits/orange-county/", "Orange County permit rules for turf")
HOA_ROUTE = "/laws/hoa-rules/"
HB683_ROUTE = "/laws/florida-hb-683/"

SRC = [WG_BUILDING, WG_WATER, WG_HISTORY, WG_WIKI, SJRWMD_APOPKA, SBW_INFO, INDEPENDENCE_INFO, CANDLER_OSD, APOPKA_OSD, ORANGE_PA, "dep-rule", "fs125572", "fs7203045", "usda-wss"]


# ============================================================== HUB
def _hub():
    body = "".join([
        sec("Turf work in Winter Garden, from Plant Street to Black Lake",
            f"<p>Winter Garden sits about {price('residential')} per square foot on the same Central Florida installed range as the rest of our service area, checked as of September 2026, roughly 22 miles from our Kissimmee base. The city grew up as a citrus and rail town after its 1908 incorporation, and its brick downtown along Plant Street stayed quiet for decades after the highway era pulled shoppers away, until the {ext('https://en.wikipedia.org/wiki/West_Orange_Trail', 'West Orange Trail')}, a 22-mile paved path that runs down the old rail bed through the middle of downtown, brought cyclists and new storefronts back starting in the 1990s ({src('census-acs', 'Census')}; {ext(WG_HISTORY[1], 'the city’s own history page')}).</p>"
            + f"<p>That history splits the city's yards into two working categories: small, oak-shaded lots near the historic core, and larger subdivision lots built from the 2000s onward south of SR-50 toward Horizon West, where {city('horizon-west', 'Horizon West')} and communities near {city('windermere', 'Windermere')} pick up where Winter Garden's own limits end. Both get {svc('residential', 'a full lawn conversion')}, a {svc('pet', 'dog run')}, or a {svc('pool', 'turf strip inside a pool cage')}, built the same way either side of town.</p>"),
        sec("Winter Garden yard types and what we do differently",
            "<p>Four lot types repeat often enough here to plan for by name.</p>"
            + table("Winter Garden yard types and what we do differently",
                    ["Yard type", "What's typical", "What we do differently"],
                    [["Historic Plant Street bungalow (1900s–1950s)", "Narrow lot, mature live oaks close to the house", "Shallow excavation near root zones and a drip-line check before anyone digs"],
                     ["Stoneybrook West / Black Lake golf-community lot", "Lakefront or fairway-facing, gated, an HOA architectural review", "Turf held 10 ft off the water unless a seawall's there, plans routed through the association first"],
                     ["Subdivision south of SR-50 toward Horizon West", "2000s–present construction, pool cage common, builder fill soil", "A base built for compacted fill left over from construction, not the native sand under it"],
                     ["A lot on Lake Apopka's shoreline", "Open water on the city's northwest edge, water-level swings", "The same 10-ft state setback as any Florida lake, measured before a square foot gets quoted"]],
                    f"Access and review change the bid; the {price('residential')} per sq ft range does not move by neighborhood.")),
        sec("Who reviews a turf permit inside Winter Garden's city limits",
            f"<p>Winter Garden runs its own Building Division rather than routing permit questions through the county, so an address inside the city limits gets reviewed at the city's own counter. We haven't built a dedicated permit page for Winter Garden's specific code the way we have for unincorporated Orange County, and that's worth saying plainly rather than guessing: call the Building Division at 407-877-5136, or start an application through the city's BS&A Online portal, before a crew is scheduled ({ext(WG_BUILDING[1], 'Winter Garden Building Division')}).</p>"
            + f"<p>If an address turns out to sit just past the city line instead, in unincorporated Orange County, {a(PERMITS_ORANGE[0], PERMITS_ORANGE[1])} covers that office instead, and a quick search on the {ext(ORANGE_PA[1], ORANGE_PA[0])} settles which one actually has a given parcel. Either way, Florida's May 19, 2026 turf standard sets the same statewide floor, described in full at {a(HB683_ROUTE, 'HB 683 and Rule 62-308.100')}, and a homeowners association answers to a separate law covered at {a(HOA_ROUTE, 'what a Florida HOA can and can’t restrict')}.</p>"),
        sec("Water rules and the Lake Apopka basin",
            f"<p>Winter Garden bills and schedules its own water rather than buying through Orange County Utilities. During Daylight Saving Time, odd-numbered addresses water Wednesday and Saturday and even-numbered addresses water Thursday and Sunday, non-residential properties water Tuesday and Friday, and nothing runs between 10 a.m. and 4 p.m.; the schedule tightens to one day a week once Eastern Standard Time starts ({ext(WG_WATER[1], 'the city’s current irrigation schedule')}). New sod gets a temporary daily allowance for its first 30 days, then every other day for 30 more, which is the schedule a lawn on the way out from under sod is still following the week before turf goes in.</p>"
            + f"<p>Winter Garden's western edge touches Lake Apopka directly, and the lake's whole basin, along with the smaller lakes threaded through the city's newer subdivisions, falls under the St. Johns River Water Management District ({ext(SJRWMD_APOPKA[1], 'SJRWMD’s Lake Apopka basin page')}). None of that watering schedule reaches a synthetic lawn once its in-ground heads are capped, which the state's turf rule requires regardless of the day printed on a utility bill.</p>"),
        sec("Winter Garden's yards, from ridge sand to a golf-course lakefront",
            f"<p>The rolling ground under Winter Garden and the rest of the west Orange County ridge runs to well-drained, sandy Candler and Apopka series soils rather than the flatter, wetter sand under a Kissimmee lawn ({ext(CANDLER_OSD[1], 'USDA’s Candler series description')}; {ext(APOPKA_OSD[1], 'USDA’s Apopka series description')}); a specific lot is still worth checking on the {src('usda-wss', 'Web Soil Survey')} address by address, since the ridge and the flatter ground toward Horizon West don't always match. Stoneybrook West, a gated community of roughly 1,450 homes built between 2000 and 2011 around its own 18-hole golf course on the shore of Black Lake, is the clearest example of the newer, HOA-governed lot type south of SR-50 ({ext(SBW_INFO[1], 'community details for Stoneybrook West')}), while Independence, just southwest toward Horizon West between Lake Hancock and Lake Speer, is close enough that its homeowners often call it a Winter Garden address ({ext(INDEPENDENCE_INFO[1], 'Independence, Horizon West')}).</p>"
            + "<p>How do you find the best artificial turf contractor near you in Winter Garden? Start by asking whether the crew already knows the difference between an old Plant Street lot's root-heavy sand and a Stoneybrook West subdivision's compacted fill, since the base plan changes either way. A written quote with base depth, product name and infill type answers that question better than a sales pitch does.</p>"),
        "<!--AUTO:city-services-->",
    ])
    faqs = [
        faq("Does Winter Garden require a permit for a synthetic lawn?",
            "The city's Building Division hasn't published a synthetic-turf-specific rule as of September 2026, so a residential conversion meets Winter Garden's ordinary exterior-work and drainage permitting rather than a dedicated turf code. Call 407-877-5136 before scheduling a crew, since the answer can depend on the scope of the job."),
        faq("Which water management district covers Winter Garden?",
            "The St. Johns River Water Management District, the same district that covers most of Orange County outside its southeastern edge. Winter Garden's northwest side borders Lake Apopka directly, which sits inside that district's Lake Apopka basin."),
        faq("Does a Stoneybrook West or Black Lake home go through extra review before turf goes in?",
            "Likely yes, on top of whatever the city requires. A gated, HOA-governed community typically expects an architectural review submittal before exterior work starts, and Florida's visibility statute protects a fenced backyard that can't be seen from the street or a neighboring lot more than it protects a front yard facing the fairway."),
        faq("Is Winter Garden's soil the same as Kissimmee's?",
            "No. Kissimmee and most of Osceola County sit on flatter, wetter flatwoods sand. Winter Garden rides the west Orange County ridge, where Candler and Apopka series soils drain fast and hold water far less than the sand under a typical Kissimmee yard."),
        faq("How far is Winter Garden from your Kissimmee crew?",
            "About 22 miles by straight line. That distance doesn't change the published per-square-foot range; it just means a Winter Garden job usually gets paired with another west Orange County stop on the same day."),
    ]
    return page("/areas/winter-garden/", "city",
                "Artificial Turf in Winter Garden, FL (2026 Guide)",
                "Synthetic turf installation, permits, Lake Apopka water rules and ridge soil facts for Winter Garden, FL. Checked September 2026, about 22 miles from Kissimmee.",
                "Artificial turf and synthetic grass in Winter Garden",
                capsule(f"Kissimmee Artificial Turf installs, repairs and cleans synthetic lawns in Winter Garden, about 22 miles from our Kissimmee base. A residential job here prices at {price('residential')} a square foot, matching every other town in our Central Florida service area, checked in September 2026. The city runs its own Building Division and its own water utility, and its west Orange ridge soil drains faster than the flatwoods sand under a typical Osceola County lawn."),
                body, faqs=faqs, sources=SRC, city=SLUG, crumbs=[("Service areas", "/areas/")], crumb="Winter Garden",
                related=[("/areas/orange-county/", "Artificial turf across Orange County"), PERMITS_ORANGE, ("/areas/ocoee/", "Turf in Ocoee"), ("/areas/oakland/", "Turf in Oakland"), ("/artificial-turf-cost/", "Turf cost tables for Central Florida")])


HUB = _hub()


# ============================================================== residential
def _residential():
    sections = [
        ("Building on Winter Garden's ridge sand",
         f"<p>Winter Garden and the rest of the west Orange County ridge sit on well-drained Candler and Apopka series soils, sandier and faster-draining than the flatwoods sand under most Osceola County lawns ({src('usda-wss', 'USDA Web Soil Survey')}). That's good news for a French drain and bad news for a rushed base: sand this loose shifts under a plate compactor faster than it settles, so a two-lift compaction schedule matters here even more than it does on flatter ground, and it's worth confirming which side of the ridge a specific lot sits on before assuming either soil profile.</p>"
         f"<p>A historic Plant Street-area lot, platted when the city was still a citrus and rail town, tends to sit on shallower topsoil over that same sand than a subdivision built decades later with imported fill, which changes how much material gets removed before the rock goes in. That same ridge runs west through {city('oakland', 'Oakland')} and further south toward {city('clermont', 'Clermont')}.</p>"),
        ("Older lots downtown, newer ones south of SR-50",
         f"<p>Winter Garden's residential stock splits cleanly by era. Near downtown and the West Orange Trail, homes date to the city's early-1900s boom and sit on narrow lots shaded by decades-old live oaks, which puts the state's drip-line rule in play on a large share of jobs there. South of SR-50 toward {city('horizon-west', 'Horizon West')}, gated communities such as Stoneybrook West were built between 2000 and 2011 around a golf course on Black Lake, with wider lots, younger trees and an architectural-review process that {svc('residential', 'a downtown lawn conversion')} never had to clear.</p>"
         f"<p>Either lot type gets the same washed, compacted rock base and the same turf; what changes is how much of the job is negotiating a canopy or an HOA form before the crew shows up. {post('artificial-turf-near-live-oaks-and-palms', 'This article')} covers the drip-line question in more detail.</p>"),
        ("Permits, HOA review and Winter Garden's own Building Division",
         f"<p>An address inside Winter Garden's limits answers to the city's own Building Division, not Orange County's, so a call to 407-877-5136 or a submission through the city's BS&A portal is the right first step for a lawn conversion. We haven't built our own permit page for Winter Garden's code specifically; {a(PERMITS_ORANGE[0], 'our Orange County page')} covers the unincorporated pockets nearby, and either jurisdiction answers to the same statewide floor set by {a(HB683_ROUTE, 'the state’s May 2026 turf rule')}.</p>"
         f"<p>A Stoneybrook West or other HOA-governed address adds a separate step: an architectural submittal to the association, which Florida's visibility statute limits differently than it limits city permitting, covered at {a(HOA_ROUTE, 'our HOA page')}.</p>"),
    ]
    scenario = ("Say you have a 1,100 sq ft backyard behind a 1925 bungalow two blocks off Plant Street",
                f"<p>Say you have a 1,100 sq ft backyard behind a 1925 bungalow two blocks off Plant Street, shaded on one side by a live oak that's been there since before the house was built. At the {price('residential', True)} per sq ft range most Winter Garden yards land in, that lawn prices between $11,000 and $17,600, with the final number leaning toward the upper end if the oak's canopy reaches far enough to trigger the state's drip-line rule and slow the excavation near its roots.</p>"
                "<p>The old sprinkler zone that used to reach that corner gets capped at the valve box rather than removed, since the state standard bars watering synthetic turf from an in-ground system either way. A hose rinse takes over after that, on whatever schedule the lawn needs rather than the city's odd-and-even watering days, which stop applying to that section of yard the moment the heads are capped.</p>")
    faqs = [
        faq("Does a narrow downtown Winter Garden lot cost more to convert than a subdivision lot?",
            "Often a little, yes, mostly because of tree roots and tighter access rather than the lot itself. A mature oak's root system can extend well past its canopy, which slows excavation near the trunk regardless of how small the actual turf area is."),
        faq("Do I need Winter Garden's permission before removing sod on a historic Plant Street lot?",
            "Nothing published treats a historic-district lot differently from any other Winter Garden address for a straightforward sod-to-turf swap. Call the Building Division at 407-877-5136 to confirm before starting, since scope and location both factor into whether a permit applies."),
    ]
    return {"title": "Artificial Grass Installation in Winter Garden, FL", "meta": "Synthetic lawn installation in Winter Garden, FL: ridge sand base, Plant Street oaks, Stoneybrook West HOA review, market pricing checked September 2026.",
            "h1": "Artificial grass installation for Winter Garden lawns", "lede": capsule(f"A residential lawn conversion in Winter Garden prices at {price('residential')} a square foot, matching every other town in our Central Florida service area as of September 2026. The city's west Orange ridge soil drains faster than the flatwoods sand under a typical Osceola County lawn, and lot age, from 1900s Plant Street bungalows to post-2000 subdivisions, changes the build more than the address does."),
            "sections": sections, "scenario": scenario, "faqs": faqs, "sources": SRC}


# ============================================================== pet
def _pet():
    sections = [
        ("Dog runs behind Winter Garden's newer subdivisions",
         f"<p>South of SR-50, communities built from the 2000s onward toward {city('horizon-west', 'Horizon West')} and Independence run narrower, zero-lot-line side yards more often than the wider lots downtown, which is exactly the shape a dedicated dog run needs to work well. A run built along a side fence in one of these subdivisions gets the odor-control infill and drainage base a family lawn skips, and skipping the weed-barrier layer that a plain lawn often includes, since fabric under a pet area traps liquid instead of letting it filter through.</p>"
         f"<p>{svc('pet', 'Pet turf and dog runs')} built this way handle daily rinsing better than a lawn that was only ever meant for foot traffic a few times a week.</p>"),
        ("A fenced backyard and Florida's visibility rule",
         f"<p>Stoneybrook West and the other gated communities south of SR-50 run an architectural review before most exterior changes, dog runs included, though we found no published community rule naming turf specifically, only a general design-review process. What does apply everywhere in Florida is {a(HOA_ROUTE, 'F.S. 720.3045')}, which protects an item an HOA can't see from the street or an adjacent lot; a fenced backyard dog run in one of these communities gets that protection, while a run along a street-facing side yard doesn't.</p>"
         f"<p>That distinction is worth raising with the association before submitting paperwork, since it can change whether a full ARC packet is even required. The same statute protects a fenced yard the same way in {city('ocoee', 'Ocoee')} or {city('clermont', 'Clermont')}, not just in Winter Garden.</p>"),
        ("Rinsing a dog run instead of watering it",
         f"<p>Winter Garden's own watering schedule limits in-ground irrigation to two mornings or evenings a week by address during Daylight Saving Time, tightening to one day in winter, with nothing allowed between 10 a.m. and 4 p.m. ({ext(WG_WATER[1], 'the city’s current schedule')}). None of that reaches a pet turf area once its old sprinkler zone is capped, since the state's rule bars an in-ground system from watering synthetic turf regardless of the day printed on a utility bill; a hose rinse settles the infill and clears odor on whatever schedule the dogs actually need.</p>"
         f"<p>{post('how-to-get-dog-urine-smell-out-of-artificial-turf', 'This article')} covers what that rinsing routine looks like week to week.</p>"),
    ]
    scenario = ("Say you have a 480 sq ft dog run behind a 2006 pool-cage home near Black Lake",
                f"<p>Say you have a 480 sq ft side-yard dog run behind a 2006 pool-cage home in a subdivision near Black Lake, fenced on both sides and never visible from the street. At the {price('pet', True)} per sq ft pet turf range, that run prices between $5,760 and $7,680, with zeolite or a coated antimicrobial sand adding a modest amount on top for the odor control a dog run actually needs.</p>"
                "<p>Because the run sits behind a privacy fence, F.S. 720.3045 protects it from an HOA objection even in a community that runs its own architectural review, though a submittal is still the faster path if the association expects one for any exterior change. The old irrigation zone that used to reach that strip gets capped rather than removed, and a hose takes over the rinsing from there.</p>")
    faqs = [
        faq("Does a Winter Garden HOA need to approve pet turf if it's not visible from the street?",
            "Florida's visibility statute doesn't require approval for an item a neighbor or the street can't see, a fenced backyard dog run included. Some associations still ask for a courtesy submittal even when the law doesn't require one, so a quick check with the HOA can save a dispute later."),
        faq("Do I need to skip the weed barrier under a Winter Garden dog run?",
            "Most installers leave that layer out for a dog run specifically. A liner between the compacted rock and the turf's backing holds urine right where it lands rather than letting it soak down into the base, which works against what a pet area needs. A plain residential lawn can go either way on it."),
        faq("Will Winter Garden's watering restrictions slow down rinsing a new dog run?",
            "No. The city's odd-and-even schedule governs in-ground irrigation, and a synthetic pet area doesn't use one once its heads are capped. A hose rinse isn't tied to that calendar."),
    ]
    return {"title": "Pet Turf & Dog Runs in Winter Garden, FL", "meta": "Pet turf and dog run installation in Winter Garden, FL: zero-lot-line subdivisions, HOA visibility rules, odor-control infill. Checked September 2026.",
            "h1": "Pet turf and dog runs for Winter Garden yards", "lede": capsule(f"Pet turf in Winter Garden runs {price('pet')} per square foot as of September 2026, with most dog runs landing between {price('pet', True)}. Newer subdivisions south of SR-50 favor narrow, fenced side yards for a run, and Florida's visibility statute protects one an HOA can't see from the street."),
            "sections": sections, "scenario": scenario, "faqs": faqs, "sources": SRC}


# ============================================================== putting
def _putting():
    sections = [
        ("Putting greens behind a golf-community fairway",
         f"<p>Stoneybrook West's own 18-hole course, designed by Arthur Hills and built into the community between 2000 and 2011, put a fairway or a green within view of a large share of its roughly 1,450 homes ({src('census-acs', 'ACS community data')}; {ext(SBW_INFO[1], 'community details for Stoneybrook West')}). A homeowner backing that kind of view is a natural candidate for {svc('putting', 'a backyard putting or chipping green')} of their own, sized to the side yard or a corner of the lot that never got real use as lawn.</p>"
         "<p>The pitch matters more here than on a plain residential job, since a green has to read true regardless of which way the yard happens to slope toward the golf course drainage behind it.</p>"),
        ("Grading a green on the west Orange ridge",
         f"<p>The well-drained Candler and Apopka sand common on Winter Garden's side of the county holds a shaped subgrade better than wetter flatwoods sand does, which helps when a green needs multiple breaks and a raised collar rather than a flat rectangle ({ext(CANDLER_OSD[1], 'USDA’s Candler series description')}). That doesn't remove the need for an engineered base; contouring still happens in the rock layer before the green's carpet ever goes down, compacted in lifts around each shaped feature rather than smoothed over the top afterward.</p>"
         "<p>A cup or two set into the green adds drainage detail a flat lawn never needs, since water has to clear the hole itself, not just the surrounding turf.</p>"),
        ("A chipping pad on a smaller downtown lot",
         f"<p>Not every Winter Garden green backs a fairway. A narrower lot near downtown and the West Orange Trail more often fits a compact chipping pad with a single cup than a full contoured green, tucked into whatever corner of the yard gets the most sun once the live oaks are accounted for. {post('artificial-turf-glossary', 'This glossary')} covers the terms, fringe, stimp, pile height, that come up when sizing a green for a specific lot rather than a golf-course backdrop.</p>"
         f"<p>Either version uses the same fringe-and-green turf combination, just at a different scale. A similar chipping-pad approach fits smaller lots we see in {city('windermere', 'Windermere')} and {city('oakland', 'Oakland')}.</p>"),
    ]
    scenario = ("Say you have a 320 sq ft green tucked behind a Stoneybrook West home backing the fairway",
                f"<p>Say you have a 320 sq ft putting and chipping green planned for the side yard of a Stoneybrook West home that backs the golf course's 14th fairway. At the {price('putting', True)} per sq ft putting green range, that project prices between $5,760 and $8,000, with the number moving toward the top if the green needs more than one break and a raised collar around the cup.</p>"
                "<p>Because the lot sits inside a gated, HOA-governed community, a design submittal to the association is worth starting before ordering turf, even though the green itself likely sits behind a privacy hedge rather than facing the street. The existing sprinkler zone in that side yard gets capped once the green goes in, and any grading needed to keep water moving toward the golf course's own drainage happens in the rock base, not after the fact.</p>")
    faqs = [
        faq("Does a putting green need HOA approval in a Stoneybrook West-type community?",
            "Likely yes, since exterior changes in a gated, association-governed community typically go through an architectural review regardless of how visible the project actually is. Submitting a sample, a sketch and the turf spec ahead of time is faster than starting the conversation after the crew is scheduled."),
        faq("Is a putting green harder to build on Winter Garden's ridge sand than on flatter ground?",
            "Not harder, just different. Fast-draining sand holds a shaped subgrade well once it's compacted in lifts, which suits a contoured green, but it also means the crew has to work more carefully to keep loose sand from shifting under the plate compactor before the rock is fully packed."),
    ]
    return {"title": "Backyard Putting Greens in Winter Garden, FL", "meta": "Backyard putting green installation in Winter Garden, FL: golf-community lots near Stoneybrook West, ridge-sand grading, market pricing checked September 2026.",
            "h1": "Backyard putting greens for Winter Garden yards", "lede": capsule(f"Backyard putting greens in Winter Garden run {price('putting')} per square foot as of September 2026, typically {price('putting', True)}. Golf-community lots such as those backing Stoneybrook West's course are natural candidates, and the west Orange ridge's well-drained sand holds a contoured subgrade better than flatter Osceola County ground."),
            "sections": sections, "scenario": scenario, "faqs": faqs, "sources": SRC}


# ============================================================== playground
def _playground():
    sections = [
        ("Play areas near the West Orange Trail's family subdivisions",
         f"<p>The trail's 1990s revival pulled families as well as cyclists into Winter Garden, and the subdivisions built south of SR-50 in the decades since carry more young households than the older downtown core does. A backyard {svc('playground', 'play set or climbing structure')} on one of those newer lots gets a shock pad sized to the equipment's fall height, not a generic thickness, which is the detail that separates a safe landing zone from one that only looks finished.</p>"
         f"<p>A wider, newer lot usually has room to keep the play area clear of a fence line, which simplifies the shock-pad edge compared with a tighter downtown yard. The same shock-pad approach applies to family subdivisions we see in {city('ocoee', 'Ocoee')} and {city('windermere', 'Windermere')}.</p>"),
        ("Keeping a swing set outside an oak's drip line",
         f"<p>Winter Garden's historic core carries decades-old live oaks close to the house, and the state's turf rule bars installing synthetic turf inside a tree's drip line, on that property or an adjacent one, unless a certified arborist certifies no harm. A play area planned for a downtown-area backyard needs that drip line marked before the shock pad's footprint gets finalized, since a canopy's reach is usually wider than it looks from the ground.</p>"
         f"<p>{post('is-artificial-turf-safe-for-kids-pfas-lead', 'This article')} covers what infill choice matters most under a play structure, separate from the drip-line question.</p>"),
        ("Shock pad drainage on fast-draining ridge sand",
         f"<p>Well-drained Candler and Apopka sand under a Winter Garden lot moves water away from a shock pad faster than the flatter, wetter ground under a Kissimmee playground turf job, which sounds like an advantage until the pad itself is built without matching attention to compaction ({ext(APOPKA_OSD[1], 'USDA’s Apopka series description')}). A loose, uncompacted layer under a fall-height pad can settle unevenly even on soil that drains well, so the base still gets built in the same washed, compacted lifts a plain lawn does.</p>"
         "<p>What changes on this soil is how quickly the pad dries after a storm, not whether it needs a proper base to begin with.</p>"),
    ]
    scenario = ("Say you have a 250 sq ft play area behind a 1998 two-story home near a subdivision park",
                f"<p>Say you have a 250 sq ft play area planned for the backyard of a 1998 two-story home in a subdivision south of SR-50, built around a small swing set and a slide combo with a 6-foot fall height. At the {price('playground', True)} per sq ft playground turf range, that area prices between $3,000 and $4,750, with the shock pad's thickness set to the equipment's actual fall height rather than a flat default.</p>"
                "<p>Because the lot sits well clear of any mature tree canopy, the drip-line question doesn't come up the way it would on an older downtown lot, and the crew can plan the pad's edges around the existing fence line instead of working around root zones. The old irrigation head that used to reach that corner gets capped at installation, the same as anywhere else in the yard.</p>")
    faqs = [
        faq("Does a Winter Garden playground turf project need a permit?",
            "Nothing published treats a residential play area differently from any other synthetic turf project in the city. Winter Garden's Building Division, at 407-877-5136, is the office to confirm with before scheduling a crew."),
        faq("How do I know if my Winter Garden backyard has trees close enough to trigger the drip-line rule?",
            "Measure to the actual edge of the canopy, not the trunk, since a mature oak's branches and roots both extend well past where the tree appears to end from a distance. A certified arborist's letter is the only way around the setback if a play area has to sit inside that line."),
    ]
    return {"title": "Playground Turf in Winter Garden, FL", "meta": "Playground turf installation in Winter Garden, FL: shock pad sizing, oak drip-line rule, ridge-sand drainage. Market pricing checked September 2026.",
            "h1": "Playground turf for Winter Garden backyards", "lede": capsule(f"Playground turf in Winter Garden runs {price('playground')} per square foot as of September 2026, typically {price('playground', True)}. Newer subdivisions south of SR-50 give a play area more clearance from mature trees than a historic downtown lot does, where the state's drip-line rule comes up more often."),
            "sections": sections, "scenario": scenario, "faqs": faqs, "sources": SRC}


# ============================================================== pool
def _pool():
    sections = [
        ("Turf inside a screened lanai south of SR-50",
         f"<p>Subdivisions built from the 2000s onward south of SR-50, Stoneybrook West and the communities around it included, favor a screened pool cage over an open deck, which leaves a ring of turf between the cage's frame and the pool's coping that sod almost never survives in shade. {svc('pool', 'Turf inside that enclosure')} needs a drainage underlay wherever it meets the concrete deck, since the screen keeps rain off part of the area while the rest gets a normal downpour.</p>"
         "<p>Glue-down edges hold better than nailed ones against a slab, which is standard practice inside any screen enclosure regardless of the neighborhood.</p>"),
        ("Older Winter Garden pools without a cage",
         f"<p>Closer to downtown, pools built in the 1950s through the 1970s often went in without a screen enclosure at all, since cages weren't standard practice on Winter Garden lots that early. Turf around an uncovered pool takes full sun the way a shaded, caged one never does, which pushes the surface temperature toward the upper end of the 120 to 150 degree range the guide describes and makes a light-colored or cooling infill worth the extra cost near the deck.</p>"
         f"<p>{post('how-to-make-artificial-grass-look-real', 'This article')} covers infill and product choices that read well next to pool coping specifically. Older, uncaged pools show up just as often in {city('oakland', 'Oakland')} and {city('clermont', 'Clermont')}.</p>"),
        ("Watering rules that never reach a pool deck",
         f"<p>Winter Garden's odd-and-even irrigation schedule governs sprinkler zones, not a pool deck strip that was never on an irrigation head to begin with in most cases ({ext(WG_WATER[1], 'the city’s watering schedule')}). Where a head did used to reach that area, capping it is required by the state's turf rule regardless of the day printed on a utility bill, and the pool itself becomes the closest thing to a rinse station the turf gets, since a quick hose-off after a swim does the same job a scheduled watering day would.</p>"
         "<p>That's one less thing to coordinate around than a full front-yard conversion, where the irrigation zone often still serves grass on either side.</p>"),
    ]
    scenario = ("Say you have a 600 sq ft turf strip inside a 2003 screened cage south of SR-50",
                f"<p>Say you have a 600 sq ft strip of turf planned inside the screened pool cage of a 2003 home in a subdivision south of SR-50, running along two sides of the pool deck where sod never fully took in the shade cast by the enclosure's frame. At the {price('residential', True)} per sq ft range pool-area turf typically lands in, that project prices between $6,000 and $9,600, usually toward the upper half because glue-down edges over concrete take more labor than a nailed perimeter in open ground.</p>"
                "<p>A drainage underlay goes down first wherever the turf meets the deck, since the screen keeps most rain off but a wind-driven storm still reaches that strip a few times a season. Once that layer's in, the build looks like any other turf job, just anchored to concrete instead of soil at the edges.</p>")
    faqs = [
        faq("Does turf inside a Winter Garden pool cage need a different base than an open yard?",
            "Yes, where it meets the concrete deck. A drainage underlay handles water that the screen doesn't fully block, and the perimeter gets glued to the slab rather than nailed the way an open-ground edge would be."),
        faq("Is pool-area turf hotter in an older, uncovered Winter Garden pool than a caged one?",
            "Generally yes, since a screen enclosure blocks some direct sun that an open deck gets all day. A lighter-colored or cooling infill and a habit of hosing the area down on hot afternoons both help close that gap."),
        faq("Do I need a permit for turf around a pool in Winter Garden?",
            "Nothing published singles out pool-area turf from any other synthetic turf project in the city. Call the Building Division at 407-877-5136 if the pool cage itself is also part of the scope, since a structural change can carry its own review separate from the turf."),
    ]
    return {"title": "Pool & Lanai Turf in Winter Garden, FL", "meta": "Turf around pools and inside screened lanais in Winter Garden, FL: drainage underlay, older uncaged pools, heat and infill. Checked September 2026.",
            "h1": "Pool and lanai turf for Winter Garden homes", "lede": capsule(f"Pool and lanai turf in Winter Garden runs the {price('residential')} per square foot residential range as of September 2026, typically {price('residential', True)}. Newer subdivisions south of SR-50 favor a screened cage that needs a drainage underlay at the deck, while older, uncaged downtown pools take more direct sun."),
            "sections": sections, "scenario": scenario, "faqs": faqs, "sources": SRC}


# ============================================================== repair
def _repair():
    sections = [
        ("What breaks first on a lawn near Winter Garden's old oaks",
         f"<p>A live oak's roots keep growing years after a lawn goes in, and near downtown Winter Garden's older canopy, a root working its way toward the surface is one of the more common reasons a seam or an edge lifts on an otherwise sound install. {svc('repair', 'A repair')} in that spot usually means cutting back the offending root, rebuilding a short stretch of base, and re-seaming rather than replacing the whole lawn.</p>"
         "<p>Catching it early, while the lift is still an inch or two, keeps the fix small; left alone through a rainy season, the same root can work a much longer seam loose.</p>"),
        ("Storm damage on a Black Lake-area lawn",
         "<p>Lakefront and fairway-facing lots near Stoneybrook West and Black Lake take more direct wind than a sheltered downtown yard does, which shows up after a tropical storm as a lifted corner where an edge was anchored lightly the first time around. The fix is usually a re-anchor along that section rather than a full edge replacement, provided the original nailing or bender-board work was otherwise sound.</p>"
         f"<p>{post('artificial-turf-hurricane-flooding', 'This article')} covers what a harder storm, not just a windy afternoon, can do to a synthetic lawn.</p>"),
        ("Low-E glass melting a patch on a newer subdivision lawn",
         f"<p>Newer homes south of SR-50 are more likely to carry low-emissivity replacement windows than an older downtown bungalow, and that glass can reflect enough concentrated sun to soften a synthetic lawn several feet away. A scorched, oddly shaped patch that doesn't trace back to any other obvious cause is worth checking against a nearby south- or west-facing window before assuming a product defect. {svc('repair', 'Repairing')} that kind of damage means cutting out the affected turf and patching in a matched piece, not replacing the whole lawn.</p>"
         f"<p>A window film or a repositioned section of turf afterward keeps the same spot from failing twice. The same low-E risk turns up in newer subdivisions around {city('ocoee', 'Ocoee')} and {city('horizon-west', 'Horizon West')}.</p>"),
    ]
    scenario = ("Say you have 40 linear feet of open seam and a small melted patch on a 2015 Winter Garden lawn",
                f"<p>Say you have 40 linear feet of open seam along one edge and a 6 sq ft melted patch near a west-facing window on a 2015 lawn in a subdivision south of SR-50. That combination gets quoted after photos or a site visit, not a flat per-square-foot rate, since a repair's price depends on how much base work the seam needs and whether the melted section can be patched or has to be cut out and replaced.</p>"
                f"<p>For comparison, replacing that same 46 sq ft of turf outright, rather than repairing it, would run roughly $370 to $830 at the {price('residential')} residential range, which is useful context even though the repair itself is priced as a visit rather than a per-foot number. Whichever the crew recommends, the fix stops at the damaged sections; a sound lawn elsewhere in the yard doesn't need to come up.</p>")
    faqs = [
        faq("Does homeowners insurance cover turf repair after a Winter Garden storm?",
            f"Sometimes, depending on the policy and the cause. {post('does-homeowners-insurance-cover-artificial-turf', 'This article')} covers what's typically covered and what isn't, since wind damage and gradual root intrusion are treated differently by most carriers."),
        faq("Do I need a permit to repair a section of turf in Winter Garden?",
            "Nothing published requires one for a straightforward seam or patch repair, since that scope of work doesn't usually rise to the level of a building permit. A larger repair that involves regrading or reworking drainage is worth a call to the Building Division at 407-877-5136 first."),
    ]
    return {"title": "Turf Repair in Winter Garden, FL", "meta": "Artificial turf repair in Winter Garden, FL: oak-root seam lifts, storm-damaged edges near Black Lake, low-E window melt. Checked September 2026.",
            "h1": "Turf repair for Winter Garden lawns", "lede": capsule("Turf repair in Winter Garden is quoted after photos or a site visit, not a flat per-square-foot rate, since seam, edge and heat-damage fixes each need a different amount of work. Older lots near live oaks and newer lawns near low-E replacement windows fail in different ways, and both are common enough here to plan for."),
            "sections": sections, "scenario": scenario, "faqs": faqs, "sources": SRC}


LOCAL = {
    "residential": _residential(),
    "pet": _pet(),
    "putting": _putting(),
    "playground": _playground(),
    "pool": _pool(),
    "repair": _repair(),
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
