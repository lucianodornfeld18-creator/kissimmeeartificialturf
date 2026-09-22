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
                    ["Yard type", "What's typical there", "How we build it differently"],
                    [["Historic Plant Street bungalow (1900s–1950s)", "Narrow lot, mature live oaks close to the house", "Shallow excavation near root zones and a drip-line check before anyone digs"],
                     ["Stoneybrook West / Black Lake golf-community lot", "Lakefront or fairway-facing, gated, an HOA architectural review", "Turf held 10 ft off the water unless a seawall's there, plans routed through the association first"],
                     ["Subdivision south of SR-50 toward Horizon West", "2000s–present construction, pool cage common, builder fill soil", "A base built for compacted fill left over from construction, not the native sand under it"],
                     ["A lot on Lake Apopka's shoreline", "Open water on the city's northwest edge, water-level swings", "The same 10-ft state setback as any Florida lake, measured before a square foot gets quoted"]],
                    f"Access and review change the bid; the {price('residential')} per sq ft range does not move by neighborhood.")),
        sec("Who reviews a turf permit inside Winter Garden's city limits",
            f"<p>An address inside Winter Garden's city limits is reviewed by the city itself, not by Orange County: the Building Division works out of City Hall on Plant Street and takes applications through BS&A Online rather than the county's own Fast Track system. Nothing published singles out synthetic turf in the city's code, and we don't have a page written for Winter Garden's own ordinances the way we do for unincorporated Orange County, so 407-877-5136 is the fastest way to confirm what a specific lawn conversion needs before a crew shows up ({ext(WG_BUILDING[1], 'Winter Garden Building Division')}).</p>"
            + f"<p>A number of Winter Garden-adjacent addresses, especially south toward Horizon West, actually sit in unincorporated Orange County rather than inside the city; the {ext(ORANGE_PA[1], ORANGE_PA[0])} settles that in a minute, and {a(PERMITS_ORANGE[0], PERMITS_ORANGE[1])} picks up from there. Both jurisdictions answer to the same statewide floor in {a(HB683_ROUTE, 'HB 683 and Rule 62-308.100')}, and an HOA's own review runs on a separate statute, covered on {a(HOA_ROUTE, 'our HOA page')}.</p>"),
        sec("Water rules and the Lake Apopka basin",
            f"<p>Winter Garden runs its own water utility rather than buying through Orange County Utilities, and the irrigation calendar follows the address: odd numbers water Wednesday and Saturday, even numbers Thursday and Sunday, non-residential accounts Tuesday and Friday, the whole schedule running through Daylight Saving Time only, with nothing allowed from 10 in the morning to 4 in the afternoon ({ext(WG_WATER[1], 'the city’s current irrigation schedule')}). That calendar folds down to a single day once Eastern Standard Time starts, and a freshly sodded lawn gets a temporary daily watering allowance for its first month, then every other day for a second month, before dropping back onto the regular schedule.</p>"
            + f"<p>The reason that calendar exists at all traces back to Lake Apopka, which touches Winter Garden's western edge directly and sits inside the St. Johns River Water Management District's own basin planning area ({ext(SJRWMD_APOPKA[1], 'SJRWMD’s Lake Apopka basin page')}), along with every smaller pond threaded through the city's newer subdivisions. A synthetic lawn opts out of that whole calendar the moment its old sprinkler heads are capped, since the state's rule bars watering turf from an in-ground system no matter what the water bill says.</p>"),
        sec("Winter Garden's yards, from ridge sand to a golf-course lakefront",
            f"<p>The rolling ground under Winter Garden and the rest of the west Orange County ridge runs to well-drained, sandy Candler and Apopka series soils rather than the flatter, wetter sand under a Kissimmee lawn ({ext(CANDLER_OSD[1], 'USDA’s Candler series description')}; {ext(APOPKA_OSD[1], 'USDA’s Apopka series description')}); a specific lot is still worth checking on the {src('usda-wss', 'Web Soil Survey')} address by address, since the ridge and the flatter ground toward Horizon West don't always match. Stoneybrook West, a gated community of roughly 1,450 homes built between 2000 and 2011 around its own 18-hole golf course on the shore of Black Lake, is the clearest example of the newer, HOA-governed lot type south of SR-50 ({ext(SBW_INFO[1], 'community details for Stoneybrook West')}), while Independence, just southwest toward Horizon West between Lake Hancock and Lake Speer, is close enough that its homeowners often call it a Winter Garden address ({ext(INDEPENDENCE_INFO[1], 'Independence, Horizon West')}).</p>"
            + "<p>How do you find the best artificial turf contractor near you in Winter Garden? Start by asking whether the crew already knows the difference between an old Plant Street lot's root-heavy sand and a Stoneybrook West subdivision's compacted fill, since the base plan changes either way. A written quote with base depth, product name and infill type answers that question better than a sales pitch does.</p>"),
        "<!--AUTO:city-services-->",
    ])
    faqs = [
        faq("Does Winter Garden require a permit for a synthetic lawn?",
            "Nothing in Winter Garden's published code names synthetic turf as of September 2026, so a lawn conversion is measured against the city's regular exterior-work and drainage rules instead of a dedicated standard. A call to the Building Division at 407-877-5136 is the fastest way to find out how those rules apply to a specific yard."),
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
                capsule(f"A Winter Garden lawn install prices at {price('residential')} a square foot as of September 2026, no different from the rest of the towns we cover. The city keeps its own Building Division and its own water utility instead of routing either through Orange County, and its west Orange ridge soil drains faster than the flatwoods sand under a typical Osceola County lawn. Downtown's Plant Street corridor and the newer subdivisions south of SR-50 both get the same base."),
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
        ("A fenced dog run and Florida's visibility law",
         f"<p>Stoneybrook West's design review covers most exterior changes, though nothing published names turf specifically, only a general approval process for anything visible from outside the lot. Florida law settles the harder question on its own: {a(HOA_ROUTE, 'F.S. 720.3045')} keeps an association from restricting anything a neighbor or the street genuinely can't see, so a dog run tucked behind a solid privacy fence in one of these communities sits outside the association's reach even if everything else on the lot goes through review.</p>"
         f"<p>Confirming that in writing with the association before ordering material is still worth doing, since a courtesy submittal is faster than a dispute later. {city('ocoee', 'Ocoee')} and {city('clermont', 'Clermont')} homeowners get that identical protection under the same statute, whatever a given HOA's design guidelines put in writing about everything else on the lot.</p>"),
        ("Rinsing a dog run instead of watering it",
         f"<p>Winter Garden's own watering schedule limits in-ground irrigation to two mornings or evenings a week by address during Daylight Saving Time, tightening to one day in winter, with nothing allowed between 10 a.m. and 4 p.m. ({ext(WG_WATER[1], 'the city’s current schedule')}). None of that reaches a pet turf area once its old sprinkler zone is capped, since the state's rule bars an in-ground system from watering synthetic turf regardless of the day printed on a utility bill; a hose rinse settles the infill and clears odor on whatever schedule the dogs actually need.</p>"
         f"<p>{post('how-to-get-dog-urine-smell-out-of-artificial-turf', 'This article')} covers what that rinsing routine looks like week to week.</p>"),
    ]
    scenario = ("Say you have a 480 sq ft dog run behind a 2006 pool-cage home near Black Lake",
                f"<p>Say you have a 480 sq ft side-yard dog run behind a 2006 pool-cage home in a subdivision near Black Lake, fenced on both sides and never visible from the street. At the {price('pet', True)} per sq ft pet turf range, that run prices between $5,760 and $7,680, with zeolite or a coated antimicrobial sand adding a modest amount on top for the odor control a dog run actually needs.</p>"
                "<p>Because the run sits behind a privacy fence, F.S. 720.3045 protects it from an HOA objection even in a community that runs its own architectural review, though a submittal is still the faster path if the association expects one for any exterior change. The old irrigation zone that used to reach that strip gets capped rather than removed, and a hose takes over the rinsing from there.</p>")
    faqs = [
        faq("Does a Winter Garden HOA need to approve pet turf if it's not visible from the street?",
            "Not under Florida law. F.S. 720.3045 removes an association's ability to object to anything a neighbor or the street genuinely can't see, and a fenced dog run usually qualifies. Some communities still prefer a heads-up submittal even so, which can smooth things over without technically being required."),
        faq("Do I need to skip the weed barrier under a Winter Garden dog run?",
            "Most installers leave that layer out for a dog run specifically. A liner between the compacted rock and the turf's backing holds urine right where it lands rather than letting it soak down into the base, which works against what a pet area needs. A plain residential lawn can go either way on it."),
        faq("Will Winter Garden's watering restrictions slow down rinsing a new dog run?",
            "It shouldn't, since a capped pet turf area was never on the irrigation calendar to begin with once its head is removed from service. A hose handles the rinsing on whatever schedule the dogs actually need, independent of the city's odd-and-even days."),
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
        ("Play sets in the subdivisions the West Orange Trail helped build",
         f"<p>Winter Garden's growth since the trail's 1990s revival landed heaviest south of SR-50, and that's where most of the city's swing sets, trampolines and climbing structures actually sit today rather than in the older blocks near downtown. Matching a {svc('playground', 'play area')}'s shock pad to how far a child could actually fall, rather than a default thickness, is what keeps a landing zone safe instead of just green.</p>"
         "<p>A wider lot in one of these newer communities usually leaves enough room to keep the structure's footprint off the property line entirely, which takes one more variable out of the pad's layout.</p>"),
        ("The drip-line rule near Winter Garden's oldest street trees",
         "<p>The canopy along Plant Street and the blocks around it has had over a century to spread, and Florida's turf rule keeps synthetic grass out of a tree's drip line, on the lot it's growing on or the one next door, unless a certified arborist signs off that digging won't cause harm. A family adding a play area near one of these older trees needs the canopy's actual edge flagged, branch tip to branch tip, before a shock pad's outline ever gets drawn on the ground.</p>"
         "<p>That flagging step rarely comes up on a newer subdivision lot, where the landscaping hasn't had time to reach the same spread.</p>"),
        ("Shade from a golf-course tree line versus open new-construction sun",
         "<p>Lots bordering Stoneybrook West's fairways typically keep a strip of mature landscaping along the course boundary, which throws real afternoon shade onto a nearby play area in a way a freshly graded lot several streets away doesn't get for years. Less direct sun means a cooler shock pad and cooler surrounding turf, which matters most for bare feet and for younger kids who sit rather than stand.</p>"
         "<p>A play area without that kind of natural shade still benefits from a lighter-colored or cooling infill and a hose rinse before the after-school hours it usually sees the most use.</p>"),
    ]
    scenario = ("Say your family is adding a 300 sq ft play area behind a home near Stoneybrook West's tree line",
                f"<p>Say your family is adding a 300 sq ft play area behind a home near Stoneybrook West's tree-lined course boundary, sized for a swing set and a slide with a 5-foot fall height. At the {price('playground', True)} per sq ft playground turf range, that project prices between $3,600 and $5,700, with the shock pad's thickness matched to that 5-foot fall height rather than a default number.</p>"
                "<p>Because the course-side tree line already shades most of the afternoon sun off that corner, the surface stays cooler than a play area on an open, newly graded lot would, worth factoring in before paying extra for a premium cooling infill the shade may make unnecessary. The corner's old sprinkler head still gets capped at installation regardless of how much shade the spot gets.</p>")
    faqs = [
        faq("Is a permit required for a backyard play area in Winter Garden?",
            "The city hasn't published anything treating a play area differently from other synthetic turf work, so it falls under whatever exterior permitting Winter Garden already applies to yard projects. A quick call to 407-877-5136 confirms it for a specific scope before the crew arrives."),
        faq("How do I know if my Winter Garden backyard has trees close enough to trigger the drip-line rule?",
            "Walk the canopy's actual branch tips rather than eyeballing the trunk, since an old Winter Garden oak commonly reaches several feet past where it looks like the tree ends. Without a certified arborist's letter clearing the area, the play structure has to stay outside that line entirely."),
    ]
    return {"title": "Playground Turf in Winter Garden, FL", "meta": "Playground turf installation in Winter Garden, FL: golf-lot shade, oak drip-line rule near Plant Street, shock pad sizing. Market pricing checked September 2026.",
            "h1": "Playground turf for Winter Garden backyards", "lede": capsule(f"Playground turf in Winter Garden runs {price('playground')} per square foot as of September 2026, typically {price('playground', True)}. A course-side tree line near Stoneybrook West shades a play area more than an open lot elsewhere in the city does, and the state's drip-line rule still governs anything planned near an old Plant Street-area oak."),
            "sections": sections, "scenario": scenario, "faqs": faqs, "sources": SRC}


# ============================================================== pool
def _pool():
    sections = [
        ("Turf against a fairway-facing pool cage",
         f"<p>A lanai that backs Stoneybrook West's course does double duty: the screen keeps insects out the way any pool cage does, and it also stops an errant golf ball from reaching the pool or the turf around it, which is one more reason these enclosures rarely come down even as they age. {svc('pool', 'Turf built into that kind of enclosure')} still needs a drainage underlay everywhere it meets the concrete deck, since the frame blocks a share of the rain a fairway-facing yard would otherwise get in full.</p>"
         "<p>Glue-down edges against the slab outperform a nailed perimeter inside any screened enclosure, golf-course-facing or not.</p>"),
        ("Older Winter Garden pools built before the cage era",
         "<p>Pools near Plant Street's oldest blocks, put in well before Stoneybrook West or any other cage-first subdivision existed, usually never got a screen enclosure at all, since that wasn't standard practice on a Winter Garden lot that early. An open deck like that takes the sun directly, all day, in a way a caged lanai across town never does, which drives surface heat close to the upper end of what installers see in full Florida sun, worth planning for with a lighter or cooling infill right at the coping.</p>"
         f"<p>{post('how-to-make-artificial-grass-look-real', 'This article')} covers infill choices that hold up well against an uncovered pool's coping specifically.</p>"),
        ("A pool deck's turf and the 10-ft setback on a Black Lake lot",
         "<p>A handful of Black Lake-facing lots put the pool deck close enough to the shoreline that the state's 10-foot waterbody setback becomes the real limit on how far a turf border can run toward the water, not the cage's own footprint. Where a seawall already separates the yard from the lake, that setback doesn't apply the same way; where it's just a natural bank, the 10 feet gets measured before the deck's turf border is ever drawn.</p>"
         "<p>That's a different constraint than the drainage question a screened cage raises, and it's worth settling before ordering material for a lakefront pool project specifically.</p>"),
    ]
    scenario = ("Say a Stoneybrook West home is adding 500 sq ft of turf inside its screened lanai",
                f"<p>Say a Stoneybrook West home backing the course is adding 500 sq ft of turf inside its screened lanai, wrapped around a pool deck that's stayed mostly bare since sod never held up in the shade the cage throws. At the {price('residential', True)} per sq ft range this kind of project typically runs, the job prices between $5,000 and $8,000, with the total landing higher when the perimeter has to be glued to the slab rather than nailed into open ground.</p>"
                "<p>A drainage underlay goes in first everywhere the turf meets concrete, since the cage's frame blocks a share of the rain the fairway beyond it still gets in full. None of that changes because the lot backs a golf course rather than a plain backyard; the build itself is the same either way.</p>")
    faqs = [
        faq("Does turf inside a Winter Garden pool cage need a different base than an open yard?",
            "Only where the two surfaces meet. Concrete gets a drainage underlay and a glued perimeter; open ground gets a compacted rock base and a nailed or bordered edge instead. Everywhere else inside the cage, the build matches a plain lawn."),
        faq("Is pool-area turf hotter in an older, uncovered Winter Garden pool than a caged one?",
            "Usually, since a screen blocks a meaningful share of direct sun that an open deck takes all day long. A cooling or lighter-colored infill closes part of that gap, and a hose rinse closes the rest within minutes."),
        faq("Do I need a permit for turf around a pool in Winter Garden?",
            "Turf on its own doesn't trigger anything beyond the city's usual synthetic-turf permitting, though changing the cage structure itself is a separate matter. Check with the Building Division at 407-877-5136 if the scope covers both."),
    ]
    return {"title": "Pool & Lanai Turf in Winter Garden, FL", "meta": "Turf around pools and inside screened lanais in Winter Garden, FL: golf-lot cages, older uncaged pools, the 10-ft setback near Black Lake. Checked September 2026.",
            "h1": "Pool and lanai turf for Winter Garden homes", "lede": capsule(f"A screened lanai backing Stoneybrook West's course pulls double duty, blocking golf balls along with bugs, and pool-area turf built into one prices at {price('residential')} a square foot as of September 2026, typically {price('residential', True)}. An older, uncaged pool near Plant Street takes the Florida sun directly, with nothing standing in the way."),
            "sections": sections, "scenario": scenario, "faqs": faqs, "sources": SRC}


# ============================================================== repair
def _repair():
    sections = [
        ("Wind and open sightlines on Stoneybrook West's golf-facing lots",
         f"<p>An HOA that keeps clear sightlines to the fairway also keeps windbreak landscaping to a minimum, which means a golf-facing backyard in Stoneybrook West takes a storm's wind more directly than a lot boxed in by mature trees and privacy fencing elsewhere in the city. {svc('repair', 'A repair')} on one of these lots is more often an edge that lifted at a corner than a seam that failed in the middle, since wind works at the perimeter first.</p>"
         "<p>Re-anchoring that corner, rather than pulling the whole edge, is usually enough if the rest of the perimeter held through the same storm.</p>"),
        ("Wear where a backyard meets the West Orange Trail",
         "<p>A handful of Winter Garden yards back directly onto the Trail's paved surface, and that edge sees more casual foot and bike traffic brushing against the property line than an interior lot ever does. A seam or a border nearest that line is worth anchoring a little heavier than the rest of the yard for exactly that reason, and it's the first spot worth checking if a trail-side lawn ever develops a lifted edge with no storm or root to explain it.</p>"
         "<p>None of that changes the turf itself, only where a crew looks first when a repair call comes in from a Trail-adjacent address.</p>"),
        ("Why humidity near Black Lake changes seam timing, not the seam itself",
         "<p>Seam tape and adhesive need a dry base to bond properly, and a lakefront lot near Black Lake holds ambient humidity a little longer after a storm than a yard several blocks inland does, which is a reason to schedule a seam repair for a clear stretch rather than the day right after a downpour. Rushing that step is how a repaired seam ends up failing again within a season, not because the materials were wrong but because the base underneath hadn't actually dried.</p>"
         "<p>Waiting an extra day or two near the lake costs nothing next to redoing the same seam twice.</p>"),
    ]
    scenario = ("Say a golf-facing Stoneybrook West lot has 25 linear feet of lifted edge after a windy afternoon",
                "<p>Say a golf-facing Stoneybrook West lot has 25 linear feet of lifted edge along the fairway side after a windy afternoon storm, with the rest of the perimeter still holding tight. A repair like that gets priced after a look at the site, not by the square foot, since the fix might be a straightforward re-anchor or might mean pulling back turf to check whether the original fastening was light to begin with.</p>"
                f"<p>If it turns out the edge needs full replacement rather than a re-anchor, that stretch works out to roughly 40 sq ft once the adjoining turf is factored in, which at the {price('residential')} residential range would run somewhere between $320 and $720 as a rough materials-and-labor reference, not a quote. Most repairs on a single lifted edge don't get anywhere near that scope.</p>")
    faqs = [
        faq("Does homeowners insurance cover storm damage to Winter Garden turf?",
            f"It depends on the policy more than the location. {post('does-homeowners-insurance-cover-artificial-turf', 'This article')} walks through what a typical policy treats as wind damage versus normal wear, and a lifted edge can fall into either bucket depending on the cause."),
        faq("Do I need a permit to repair a section of turf in Winter Garden?",
            "A routine seam or edge fix doesn't typically rise to the level of a building permit, though nothing published carves out an explicit exception either way. A repair involving regrading or new drainage work is the kind worth a call to 407-877-5136 first."),
    ]
    return {"title": "Turf Repair in Winter Garden, FL", "meta": "Artificial turf repair in Winter Garden, FL: wind-lifted edges on golf-facing lots, trail-side wear, seam timing near Black Lake. Checked September 2026.",
            "h1": "Turf repair for Winter Garden lawns", "lede": capsule("Turf repair in Winter Garden is quoted after photos or a site visit, not a flat per-square-foot rate, since a wind-lifted golf-lot edge and a worn seam along the West Orange Trail call for different fixes. Both come up often enough in this city to plan for, and pricing follows the visit rather than a published range."),
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
