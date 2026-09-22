# -*- coding: utf-8 -*-
from _helpers import page, capsule, sec, table, faq, a, svc, city, post, src, ext, price
from _cityservice import cityservice_pages

SLUG = "orlando"

ORLANDO_TURF_CODE = ("City of Orlando — Artificial Turf permit requirements (Land Development Code, Ch. 60, Sec. 60.224)", "https://www.orlando.gov/Our-Government/Departments-Offices/Economic-Development/City-Planning/Land-Development-Code-Amendments/Artificial-Turf")
ORLANDO_HISTORIC = ("City of Orlando — Historic Preservation Districts", "https://www.orlando.gov/Our-Government/History/Historic-Preservation-Districts")
ORLANDO_PERMITTING = ("City of Orlando — Permitting Services Division", "https://www.orlando.gov/Our-Government/Departments-Offices/Economic-Development/Permitting-Services")
ORLANDO_PORTAL = ("Orlando Permitting Portal", "https://digitalpermits.orlando.gov/")
ORANGE_PA = ("Orange County Property Appraiser — parcel search", "https://ocpafl.org/")
OUC_RESTRICTIONS = ("OUC — watering restrictions", "https://www.ouc.com/environment-community/high-quality-water-ouc/watering-restrictions")
OUC_SERVICES = ("OUC — water services overview", "https://www.ouc.com/about/water-services/")
ORLANDO_RECLAIMED = ("City of Orlando — Reclaimed Water Service Area", "https://www.orlando.gov/Parks-the-Environment/Get-Reclaimed-Water/Reclaimed-Water-Service-Area")
SJRWMD_MAP = ("St. Johns River Water Management District — district map", "https://www.sjrwmd.com/about/maps/")
BALDWIN_PARK_HISTORY = ("City of Orlando — Baldwin Park planning history", "https://www.orlando.gov/Our-Government/Departments-Offices/Economic-Development/City-Planning/Plans-Studies/Baldwin-Park")
ORLANDO_HOMESHARE = ("Orlando Code of Ordinances — Owner-Occupied Home Sharing, Sec. 58.989 (Municode)", "https://library.municode.com/fl/orlando/codes/code_of_ordinances?nodeId=TITIICICO_CH58ZODIUS_PT5ACUSST_5B_19_OWCUHOSH_S58.989GERE")
ORLANDO_LAKES = ("Orange County Library System — Orlando, land of 100 lakes", "https://ocls.org/ocls-blog/orlando-150-land-of-100-lakes/")

SRC = ["dep-rule", "fs125572", "fs7203045", "usda-wss", "census-acs",
       ORLANDO_TURF_CODE, ORLANDO_HISTORIC, ORLANDO_PERMITTING, ORLANDO_PORTAL, ORANGE_PA,
       OUC_RESTRICTIONS, OUC_SERVICES, ORLANDO_RECLAIMED, SJRWMD_MAP, BALDWIN_PARK_HISTORY,
       ORLANDO_HOMESHARE, ORLANDO_LAKES]

# ============================================================== hub
HUB = page(
    "/areas/orlando/", "city",
    "Artificial Turf in Orlando, FL: Permits, OUC and Oaks",
    "Orlando is the only city near Kissimmee with its own artificial turf code: an Engineering Permit, a 50-foot water setback and six historic districts, as of 2026.",
    "Why Orlando has its own rules for synthetic turf",
    capsule("Orlando sits about 17 miles north of Kissimmee in Orange County, and it is the only city in our area with a code section written just for synthetic turf: an Engineering Permit, a 50-foot water setback and separate rules inside six historic districts, as of September 2026. Yards here range from 1920s bungalows under oak canopy to 2000s planned communities like Baldwin Park."),
    "".join([
        sec("The one Central Florida code written for synthetic turf",
            f"<p>Orlando's Land Development Code names synthetic turf directly, in Chapter 60, Section 60.224, something Kissimmee, Osceola County and every other office we deal with has not done ({ext(ORLANDO_TURF_CODE[1], "the city's own summary")}). The section treats turf as impervious surface, requires an Engineering Permit with a signed survey and an Impervious Surface Ratio worksheet, and keeps installed turf at least 50 feet from a pond, lake or other water body.</p>"
            + f"<p>Florida's own turf standard, Rule 62-308.100, took effect May 19, 2026 and caps what a city can enforce on a single-family lot of an acre or less: no ban on compliant turf, no drainage standard stricter than 10 inches an hour across the layers, and no shoreline buffer for turf that's wider than the one for sod ({src('dep-rule', 'the adopted rule text')}; {src('fs125572', 'F.S. 125.572')}). Orlando's 50-foot rule is five times the state's 10-foot floor, and whether the city has narrowed that gap since May 2026 is a question for {ext(ORLANDO_PERMITTING[1], 'Permitting Services')} at 407-246-2121, not something a published page can settle on its own.</p>"),
        sec("Orlando yard types and what we do differently",
            "<p>Orlando runs from 1920s bungalow blocks to 2003-built Baldwin Park, and the code, the soil and the water table shift block to block. This table lines up five common Orlando yard types against what actually changes about the turf job.</p>"
            + table("Orlando yard types and what changes about the turf job",
                    ["Yard type", "What's typically there", "What changes about the job"],
                    [["Historic bungalow (Lake Eola Heights, Lake Cherokee, Colonialtown South)", "1905–1925 Craftsman and Mediterranean Revival homes under mature live oak canopy", "A district design review and the state's drip-line rule both apply before turf goes down"],
                     ["Mid-century ranch (SoDo, Delaney Park-adjacent, Conway-adjacent blocks)", "1950s–70s slab-on-grade ranches, many with a screened pool cage added later", "Narrow side yards and an older irrigation zone where the heads need pulling, not just capping"],
                     ["Baldwin Park and other 2000s planned communities", "Traditional-neighborhood lots built from 2003 on the former Naval Training Center site, alley-loaded garages", "An HOA design packet on top of the city permit, plus the mow-strip edge the code calls out by name"],
                     ["A lot backing to a lake or retention pond", "One of the city's roughly 100-plus lakes, or a stormwater pond in a newer subdivision", "Orlando's own 50-foot water setback, five times the state's 10-foot floor, with no in-ground irrigation left running"],
                     ["Small urban lot or townhome (Thornton Park, Millenia-area condos)", "A narrow footprint where the driveway and the unit already use most of the impervious budget", "The Impervious Surface Ratio worksheet decides how much turf fits before a variance conversation starts"]],
                    "Checked against Orlando's Land Development Code and Historic Preservation Districts page, September 2026; confirm a specific parcel with Permitting Services.")),
        sec("OUC, reclaimed water and a hundred lakes",
            f"<p>Orlando Utilities Commission supplies water to most of the city and a slice of unincorporated Orange County around it, and its lawn-watering schedule allows two irrigation days a week while Daylight Saving Time is in effect, drops to a single day in the cooler months, and closes the 10 a.m. to 4 p.m. window year-round ({ext(OUC_RESTRICTIONS[1], "OUC's current schedule")}). None of that applies to a turf area once its irrigation heads are capped, which the state standard requires ({src('dep-rule', 'Rule 62-308.100')}).</p>"
            + f"<p>The city runs a separate reclaimed water system in limited neighborhoods, exempt from the watering schedule entirely, so a capped turf zone next to a reclaimed-water lawn shows up on the same block more than once ({ext(ORLANDO_RECLAIMED[1], 'the service area map')}). Orlando counts more than 100 lakes inside its limits ({ext(ORLANDO_LAKES[1], 'a local library system count')}), and nearly all of the city sits inside the St. Johns River Water Management District, with a slice of southern and western Orange County answering to the South Florida district instead ({ext(SJRWMD_MAP[1], "SJRWMD's boundary map")}).</p>"),
        sec("Historic districts, oak canopy and the drip line",
            f"<p>Orlando has designated six historic preservation districts since 1980: Downtown, Lake Cherokee, Lake Copeland, Lake Eola Heights, Lake Lawsona and Colonialtown South, the newest of the six added in 2000 ({ext(ORLANDO_HISTORIC[1], "the city's district list")}). Homes in Lake Eola Heights alone date mostly to 1905–1925, and the live oaks planted alongside them now carry canopies that reach well past the average backyard's edge.</p>"
            + f"<p>The state's drip-line rule lets a certified arborist clear turf under an oak that would otherwise be off-limits; a historic district's design review is a different process the state rule does not reach, so an arborist's letter answers the tree question without answering the district question ({a('/laws/florida-hb-683/', 'what the state rule does and does not preempt')}).</p>"),
        sec("Checking whether an address is really inside Orlando",
            f"<p>Not every Orlando-sounding address sits inside the city limits. Pockets near {city('lake-nona', 'Lake Nona')} and {city('dr-phillips', 'Dr. Phillips')}, along with parts of MetroWest, sit in unincorporated Orange County rather than the city, and the fastest way to check a specific parcel is the {ext(ORANGE_PA[1], "Orange County Property Appraiser's parcel search")}. If the home is short-term rented, {ext(ORLANDO_HOMESHARE[1], "the city's owner-occupied home-sharing rule")} caps a whole-home stay at 30 nights or more outside a designated vacation-home zone, a separate question from what the yard is allowed to be.</p>"),
        sec("Three approvals for one backyard",
            f"<p>A synthetic turf project inside Orlando answers to the city's Engineering Permit process first, {a('/laws/hoa-rules/', 'a homeowners association second where the lot has one')}, and the state floor under {a('/laws/florida-hb-683/', 'HB 683 and Rule 62-308.100')} underneath both. {a('/laws/permits/city-of-orlando/', 'Our permit page for the City of Orlando')} walks through the Engineering Permit paperwork line by line; this page is about the yard itself.</p>"
            + "<p>“What's the best artificial turf installer near me in Orlando?” usually turns into a second question once the historic-district and lake-setback answers are in: which approval has to happen first.</p>"),
    ]),
    faqs=[
        faq("Does Orlando require a permit for artificial turf?", "Yes. Chapter 60, Section 60.224 of the city's Land Development Code requires an Engineering Permit with a signed survey and an Impervious Surface Ratio worksheet, whether the project is a backyard lawn or a larger commercial area. Permitting Services takes questions at 407-246-2121."),
        faq("Is turf really barred within 50 feet of a lake in Orlando?", "That is what the city's own code says, and it is stricter than the state's 10-foot floor under Rule 62-308.100. The state rule caps how tight a local buffer can get on a covered single-family lot; it does not force a city to loosen a buffer that is already looser than the cap, so 50 feet is likely to hold until Orlando says otherwise."),
        faq("Can I install turf in a district like Lake Eola Heights?", "Only after the district's design review, and only if it is not a kind of installation the city's rule bars outright. That review sits outside what the state's May 2026 turf standard preempts, since it is a design process rather than a material, drainage or setback rule."),
        faq("How do I find out if my Orlando-area address is really inside the city?", "Search the address on the Orange County Property Appraiser's site. The parcel record shows the taxing jurisdiction, and stretches near Lake Nona, Dr. Phillips and MetroWest sit in unincorporated Orange County rather than the city."),
        faq("Which water utility serves Orlando, and does it change a turf job?", "Orlando Utilities Commission serves most of the city on a two-day or one-day watering schedule depending on the season. A turf area skips that schedule once its in-ground heads are capped, which the state standard requires either way."),
    ],
    sources=SRC, city=SLUG, crumbs=[("Service areas", "/areas/")], crumb="Orlando",
    related=[("/laws/permits/city-of-orlando/", "Artificial turf permits in the City of Orlando"),
             ("/laws/hoa-rules/", "What a Florida HOA can and can't restrict"),
             ("/laws/florida-hb-683/", "HB 683 and DEP Rule 62-308.100, explained"),
             ("/areas/winter-park/", "Artificial turf in Winter Park"),
             ("/areas/hunters-creek/", "Artificial turf in Hunters Creek"),
             ("/artificial-turf-cost/", "Turf cost tables for Central Florida")],
)
HUB["body"] += "<!--AUTO:city-services-->"

# ============================================================== city x service local content
LOCAL = {
    "residential": {
        "title": "Artificial Grass Installation in Orlando, FL: Oaks & ARC",
        "meta": "Artificial grass in Orlando runs $10–$16 a sq ft typical, but a historic-district review and a live oak's drip line usually decide the design first, as of 2026.",
        "h1": "Installing artificial grass under Orlando's live oaks",
        "lede": capsule(f"Artificial grass installed in Orlando runs {price('residential')} a square foot, typically {price('residential', True)}, the same range we quote {city('kissimmee', 'back in Kissimmee')} or anywhere else in Central Florida. What changes here is the paperwork: a lot inside one of the city's six historic districts needs a design review before turf goes down, and a lot under a live oak has to clear the drip line, as of September 2026."),
        "sections": [
            ("Turf and the drip line in Orlando's oak-canopy neighborhoods",
             f"<p>Lake Eola Heights, Lake Cherokee and the blocks around them carry some of Orlando's oldest tree canopy, planted alongside bungalows going up between 1905 and 1925. A live oak in one of those yards can spread a drip line that covers a third of a small backyard, and the state's synthetic-turf standard keeps installed turf outside that line unless a certified arborist signs off that the root zone won't be harmed. On a typical {city('kissimmee', 'Kissimmee')}-area lot with younger trees this rarely comes up; on an Orlando lot with a hundred-year-old oak, it is usually the first measurement we take. {post('artificial-turf-near-live-oaks-and-palms', "What a live oak's root zone actually needs")} goes through the arborist-letter process in more detail.</p>"),
            ("What a historic district's design review adds to the job",
             "<p>A lot inside Downtown, Lake Cherokee, Lake Copeland, Lake Eola Heights, Lake Lawsona or Colonialtown South answers to the district's design review before a shovel moves, on top of the Engineering Permit every Orlando turf job needs. Our read of the published rule is that turf visible from the street inside those six districts faces a tighter standard than turf tucked behind a fence line, though the state's 2026 preemption doesn't reach that review at all, since it covers materials, drainage and setbacks rather than architectural character. A front lawn swap and a fenced backyard conversion are not the same conversation with the district's reviewer, and it's worth having that conversation before ordering material.</p>"),
            ("Baldwin Park and the newer end of Orlando's lots",
             f"<p>{ext(BALDWIN_PARK_HISTORY[1], 'Baldwin Park')} went up starting in 2001 on the former Naval Training Center site, with the first residents moving in by 2003, and its traditional-neighborhood lots run narrower than a 1970s ranch subdivision but skip the century-old canopy that drives the drip-line conversation elsewhere in the city. The Land Development Code calls for a solid edge, typically a mow strip, separating turf from any planted bed, a detail worth pricing into a Baldwin Park bid alongside the community's own architectural review. {city('winter-park', 'Winter Park')}, just north, has a similar mix of older canopy streets and newer infill.</p>"),
        ],
        "scenario": ("A bungalow backyard near Lake Cherokee",
                     f"<p>Say you have a 950 sq ft backyard behind a 1920s bungalow a few blocks from Lake Cherokee, with a live oak covering roughly a quarter of the yard along the back fence. At {price('residential')} a square foot the full 950 sq ft would run $7,600 to $17,100, but the portion inside the oak's drip line stays out unless an arborist letter clears it, which trims the workable area to something closer to 700 sq ft, or $5,600 to $12,600 at the same per-foot range. Because the lot sits in a historic district, the design review runs in parallel with, not after, the Engineering Permit application, so the arborist letter and the district submittal are worth starting the same week.</p>"),
        "faqs": [
            faq("Does an Orlando historic district review a backyard the same as a front yard?", "The published rule focuses on what's visible from the street, so a fenced backyard installation generally draws less scrutiny than a front lawn, though the district still reviews the application either way. Ask the district's staff before assuming a backyard is automatically exempt."),
            faq("What if the oak's drip line covers most of the yard?", "Then the workable turf area shrinks to whatever sits outside the drip line, unless a certified arborist certifies that turf under the canopy won't harm the root zone. That letter is a real cost and a real delay, so it's worth getting early rather than after a bid is written."),
            faq("Is a 100-year-old Orlando bungalow lot more expensive to turf than a newer one?", "Not on the material and labor side; the price per square foot is the same range everywhere we work. The added cost is usually the arborist letter and the district paperwork, not the installation itself."),
        ],
        "sources": SRC,
    },
    "pet": {
        "title": "Dog-Friendly Artificial Turf for Orlando, FL Yards",
        "meta": "Pet turf in Orlando runs $12–$16 a sq ft typical on narrow mid-century side yards, with capped irrigation and a fenced run behind the historic-district line.",
        "h1": "Dog runs that fit Orlando's narrow side yards",
        "lede": capsule(f"Pet turf installed in Orlando runs {price('pet')} a square foot, typically {price('pet', True)}, for fast-draining backing and odor-control infill. The question comes up most on the mid-century ranch lots around SoDo and the Conway-adjacent blocks, where a dog run has to fit a side yard built for a single 1960s car, not a modern setup, as of September 2026."),
        "sections": [
            ("Dog runs on Orlando's narrow, zero-lot-line lots",
             "<p>Ranch subdivisions built through the 1950s, 60s and 70s around SoDo and the blocks toward Conway often left a side yard just wide enough for a single car and a trash can, four to six feet in most cases. A dog run in that footprint needs a flush-out slope built in from day one, since there's no room to widen a drainage path later if the first grade doesn't carry water away fast enough. We build these runs with a slightly steeper pitch than a typical backyard, closer to 2 percent than 1, because a narrow channel concentrates runoff instead of spreading it.</p>"),
            ("Rinsing a pet run without in-ground irrigation",
             f"<p>The state's synthetic-turf standard bars using an in-ground irrigation system to water synthetic turf, which means the heads in a pet run get capped at the lateral line, not just plugged at the surface, and rinsing goes back to a hose. Orlando Utilities Commission's watering schedule stops mattering for that zone entirely once the capping is done ({ext(OUC_RESTRICTIONS[1], "OUC's schedule")}), which is one less thing to track for a household already managing two dogs and a rinse routine. Zeolite or a coated sand infill still needs that rinse to keep working the way it's supposed to.</p>"),
            ("A fenced run inside one of Orlando's historic districts",
             f"<p>A backyard dog run tucked behind a fence and not visible from the street generally clears the visibility standard that governs synthetic turf inside Orlando's historic districts, separate from {a('/laws/hoa-rules/', "the state statute that protects turf an HOA can't see from the frontage")}. The two rules solve different problems, one about a city design review and one about an association's authority, so meeting one doesn't automatically satisfy the other, and both are worth confirming before a fenced run near Lake Copeland or Lake Lawsona gets built.</p>"),
        ],
        "scenario": ("A dog run behind a Conway-adjacent ranch",
                     f"<p>Say you have a 12 by 40 ft side yard, 480 sq ft, behind a 1965 ranch near the Conway-adjacent blocks of south Orlando, with two dogs using it daily. At {price('pet')} a square foot the job runs $4,800 to $8,640, and most jobs like this land near the typical range of {price('pet', True)}, or roughly $5,760 to $7,680 for 480 sq ft. That figure includes the deeper drainage base a narrow zero-lot-line channel needs, plus zeolite or antimicrobial infill; it doesn't include capping the two heads that used to water that strip, which a plumber typically prices separately.</p>"),
        "faqs": [
            faq("Can I keep one irrigation head running in a pet turf area for rinsing?", "No. The state standard bars in-ground irrigation on synthetic turf outright, so every head in that zone gets capped at the line. A hose or a low-flow bib nearby is the standard workaround."),
            faq("Does a narrow Orlando side yard cost more per square foot for pet turf?", "The per-square-foot price doesn't change, but a small, narrow area often prices at the top of the range because a crew and equipment mobilize the same way for 480 sq ft as for 1,500."),
            faq("Is a fenced dog run in a historic district treated differently than an open one?", "Generally yes, since Orlando's rule is built around what's visible from the street. A fenced run out of street view usually has an easier path than an open front-yard installation in the same district."),
        ],
        "sources": SRC,
    },
    "putting": {
        "title": "Backyard Putting Greens in Orlando, FL: Lakes & ISR",
        "meta": "Putting greens in Orlando run $18–$25 a sq ft typical, but a big green eats into the Impervious Surface Ratio and the city's 50-foot water setback, as of 2026.",
        "h1": "Where a putting green actually fits on an Orlando lot",
        "lede": capsule(f"A backyard putting green in Orlando runs {price('putting')} a square foot, typically {price('putting', True)}, for contouring, fringe turf and cups. The harder question on many Orlando lots isn't the price, it's the math: Chapter 60 counts a green as impervious surface, and a lot that backs to one of the city's lakes carries its own 50-foot setback, as of September 2026."),
        "sections": [
            ("Where a green fits on an Orlando lot",
             "<p>Baldwin Park and other 2000s planned communities generally carry more usable lot depth than a 1920s bungalow block, which is why a full contoured green with fringe shows up there more often than in Colonialtown or Thornton Park's smaller footprints. On the sandier, better-draining ground toward the ridge, base work for a contoured green moves faster, since excessively drained sand holds a shaped subgrade without the standing water that a flatter, tighter soil can trap after a summer storm. A smaller chipping pad, rather than a full green, is usually the better fit on a compact urban lot.</p>"),
            ("The Impervious Surface Ratio math on a big green",
             f"<p>Orlando's own turf code, Section 60.224, counts synthetic turf as impervious surface and ties a permit to an Impervious Surface Ratio worksheet, so a 600 sq ft green isn't a free addition on a lot that already carries a pool deck, a driveway and a lanai near its zoning cap ({ext(ORLANDO_TURF_CODE[1], "the city's permit page")}). We run that math with a client before finalizing a green's footprint, because a design that looks fine on paper can trip the ratio once the pool deck is added back in. {svc('putting', 'The full putting green guide')} covers contour, fringe and cup specs in more depth.</p>"),
            ("Building a green near one of Orlando's lakes",
             f"<p>A lot backing to one of Orlando's roughly 100-plus lakes carries the city's 50-foot water-body setback for synthetic turf, five times the state's 10-foot floor under Rule 62-308.100 ({src('dep-rule', 'the adopted rule')}), and that buffer applies to a putting green the same way it applies to a lawn. A green designed to hug a lake view often has to shrink or shift closer to the house, which is a conversation worth having before fringe turf and cups get specified rather than after.</p>"),
        ],
        "scenario": ("A green and fringe in a Baldwin Park backyard",
                     f"<p>Say you have a 600 sq ft green with fringe planned for a Baldwin Park backyard that already has a 400 sq ft pool deck and a two-car driveway. At {price('putting')} a square foot the green itself runs $8,400 to $18,000, with most jobs landing in the typical {price('putting', True)} band, or $10,800 to $15,000 for 600 sq ft. Before ordering material, the Impervious Surface Ratio worksheet needs the pool deck and driveway numbers added in, since a lot that's already near its zoning cap may need the green trimmed by 50 to 100 sq ft to clear the permit.</p>"),
        "faqs": [
            faq("Does a putting green count fully against Orlando's impervious limit?", "Yes. Section 60.224 treats synthetic turf as impervious surface for permitting purposes, so a green's full footprint counts in the Impervious Surface Ratio worksheet along with the driveway, pool deck and roof."),
            faq("Can I build a green within 50 feet of a retention pond in Orlando?", "Not under the city's own code, which sets that buffer specifically for synthetic turf. The state's 2026 standard only guarantees a 10-foot floor and doesn't force a city to shrink a buffer that's already stricter than that."),
            faq("Is Orlando's sandier soil actually better for a contoured green?", "Where the ground is excessively drained upland sand, yes, it moves water through the base faster during shaping. Where a lot sits on flatter, more poorly drained ground, the base needs more attention to hold the same contours."),
        ],
        "sources": SRC,
    },
    "playground": {
        "title": "Playground Turf for Orlando, FL Family Yards",
        "meta": "Playground turf in Orlando runs $12–$19 a sq ft typical, sized to fall height, with the base built differently on the city's sandy ridge than its flatwoods pockets.",
        "h1": "Cushioned play turf for Orlando's family neighborhoods",
        "lede": capsule(f"Playground turf installed in Orlando runs {price('playground')} a square foot, typically {price('playground', True)}, with a shock pad sized to the equipment's fall height. Which base spec that takes depends on where the lot sits: the city's sandy ridge soil drains differently than its flatwoods pockets, and a Baldwin Park alley lot has different access than a bungalow yard under an oak, as of September 2026."),
        "sections": [
            ("Play areas on Baldwin Park's compact lots",
             f"<p>{ext(BALDWIN_PARK_HISTORY[1], 'Baldwin Park')}'s traditional-neighborhood layout puts garages on rear alleys, which usually gives a crew a clean path to the backyard without crossing a front lawn or a driveway, a real advantage when a shock pad and drainage stone need to come in by wheelbarrow. Lots here run narrower than a 1970s ranch subdivision, so a play area often shares space with a small patio rather than sitting in an open corner, and the code's mow-strip edge requirement matters as much around a swing set's footing as anywhere else on the lot.</p>"),
            ("Soil under a play surface: ridge sand versus flatwoods",
             f"<p>Orlando's higher ground carries excessively drained sandy soils similar to the Astatula series, with a water table more than six feet down, while lower-lying pockets closer to the city's lakes and flatwoods sit on more poorly drained ground with a seasonally high water table, closer to what the Immokalee series describes ({src('usda-wss', 'USDA Web Soil Survey')}). A shock pad and drainage layer on the sandier ground moves water through fast; on the flatwoods side, the base needs a slightly deeper stone layer so a rainy-season storm doesn't leave standing water under a fall zone a child is playing on within the hour.</p>"),
            ("Historic-district backyards and a swing set",
             "<p>A 1920s bungalow lot near Lake Eola Heights or Lake Cherokee often has the exact oak canopy that makes a shaded play area appealing, and the same drip-line rule that governs a lawn conversion governs a play surface under that canopy. A swing set's footing and fall zone have to clear the drip line the same way turf does, unless an arborist has cleared the specific root zone, which means the play layout sometimes gets designed around the tree rather than the other way around.</p>"),
        ],
        "scenario": ("A play area behind a Baldwin Park home",
                     f"<p>Say you have a 300 sq ft play area planned behind a Baldwin Park home, for a swing set with an 8 ft fall height on three sides. At {price('playground')} a square foot the job runs $3,000 to $7,500, with most similar jobs landing in the typical {price('playground', True)} band, or $3,600 to $5,700 for 300 sq ft. An 8 ft fall height needs a thicker shock pad than a low toddler slide would, which is what tends to push a Baldwin Park play area toward the upper half of that range rather than the lower one.</p>"),
        "faqs": [
            faq("Does Orlando's Engineering Permit apply to a backyard play area?", "Yes, the same way it applies to a lawn conversion, since the code counts any synthetic turf installation, including a play surface, as impervious area under Section 60.224."),
            faq("Is playground turf allowed under a live oak's canopy in Orlando?", "Only outside the drip line, unless a certified arborist certifies that the specific installation won't harm the root zone. That's the same standard that applies to a residential lawn."),
            faq("Does the base really need to be different on Orlando's flatwoods soil?", "Generally yes. A seasonally high water table needs a deeper, more open-graded stone layer to keep a fall zone draining the way it's supposed to after a storm; excessively drained sand needs less correction to do the same job."),
        ],
        "sources": SRC,
    },
    "pool": {
        "title": "Pool and Lanai Turf in Orlando, FL Screen Cages",
        "meta": "Pool and lanai turf in Orlando runs $10–$16 a sq ft typical, capped to Orlando's 50-foot pond setback and OUC's reclaimed-water map, as of September 2026.",
        "h1": "Turf beside an Orlando pool cage or lanai",
        "lede": capsule(f"Turf installed beside an Orlando pool or inside a screened lanai runs {price('residential')} a square foot, typically {price('residential', True)}, priced the same as a residential lawn. A mid-century pool cage on a SoDo or Conway-adjacent ranch calls for a different install than a newer lanai backing to a retention pond, where the city's 50-foot water setback comes into play, as of September 2026."),
        "sections": [
            ("Screen cages on Orlando's mid-century pool lots",
             "<p>Plenty of ranch homes around SoDo and the Conway-adjacent blocks added a screened pool cage well after the house itself went up in the 1950s or 60s, which usually left a narrow grass strip inside the enclosure that never drained well once foot traffic wore it down. Turf inside a screen cage on one of these lots typically goes down glue-down over the existing concrete deck border, with a drainage underlay under the turf itself, since there's no room to build a full aggregate base the way an open lawn gets.</p>"),
            ("When the pool backs to a retention pond",
             f"<p>Newer subdivisions built around a stormwater pond, common in the planned communities on Orlando's edges, put a screened lanai within sight of the water more often than an older inner-city lot does, and Orlando's own code keeps synthetic turf at least 50 feet from that pond, five times the state's 10-foot floor ({src('fs125572', 'F.S. 125.572')}). A lanai footprint itself usually sits well inside that buffer, but a homeowner adding turf along the back fence line toward the water needs the setback checked before ordering material, not after.</p>"),
            ("OUC, reclaimed water and a pool-deck rinse",
             f"<p>Heads that used to water the grass strip inside or around a screen cage get capped once turf goes in, and {ext(OUC_RESTRICTIONS[1], "OUC's watering schedule")} stops applying to that zone entirely from that point. In the limited Orlando neighborhoods on the city's reclaimed water system, the rest of the yard may keep irrigating on a separate reclaimed line even after the pool-area turf is capped, since reclaimed water runs outside the potable watering schedule ({ext(ORLANDO_RECLAIMED[1], 'the reclaimed service map')}).</p>"),
        ],
        "scenario": ("A lanai strip on a 1962 SoDo-area ranch",
                     f"<p>Say you have a 380 sq ft strip inside a screened pool cage on a 1962 ranch near SoDo, glued down over an existing concrete border with grass only in the open center section. At {price('residential')} a square foot the job runs $3,040 to $6,840, and most lanai jobs like this land in the typical {price('residential', True)} band, or $3,800 to $6,080 for 380 sq ft. Glue-down edges over concrete and a drainage underlay push a job like this toward the upper part of that range compared with an open backyard the same size.</p>"),
        "faqs": [
            faq("Can turf run right up to a retention pond behind an Orlando lanai?", "Not under the city's own rule, which keeps synthetic turf 50 feet back from a pond or lake. The state's 2026 standard only guarantees a 10-foot floor and doesn't override a stricter local buffer."),
            faq("Does capping irrigation inside a screened pool cage need its own permit?", "Often yes, since disconnecting an in-ground head is plumbing work in most jurisdictions. Ask Permitting Services when you apply for the Engineering Permit so both go through together."),
            faq("Is reclaimed water available for the lawn around an Orlando pool?", "Only in the limited neighborhoods on the city's reclaimed water system. Check the service area map for a specific address before assuming it's available."),
        ],
        "sources": SRC,
    },
    "repair": {
        "title": "Artificial Turf Repair in Orlando, FL: Root Heave",
        "meta": "Turf repair in Orlando is quoted after photos or a visit, not a flat rate, and older lawns near the city's live oaks fail differently than newer Baldwin Park turf.",
        "h1": "Fixing turf problems on Orlando's older lots",
        "lede": capsule("Turf repair in Orlando is quoted after photos or a site visit, not from a published per-square-foot range, because a seam, a wrinkle and a root-heaved section each take a different amount of work. What's specific to Orlando is the cause: a lawn near one of the city's six historic districts is more likely dealing with a live oak root than a lawn on a newer planned-community lot, as of September 2026."),
        "sections": [
            ("Root heave under Orlando's mature live oaks",
             f"<p>A live oak old enough to shade a Lake Eola Heights or Lake Cherokee bungalow has roots that keep growing whether or not turf sits above them, and a root working toward the surface tends to heave a narrow ridge that tracks back toward the trunk, different from the broad, shallow dip a settled base produces. On these century-old lots we check for that pattern first, since a repair that reseams over an active root without addressing it usually needs a second visit within a year or two. {post('artificial-turf-near-live-oaks-and-palms', 'How a live oak root actually interacts with turf')} covers the arborist question that sometimes follows.</p>"),
            ("When a repair crosses into Engineering Permit territory",
             f"<p>A simple reseam or a patched corner generally stays outside Orlando's permitting process, but a repair that expands the turf's footprint, regrades a low spot near a retention pond, or moves the edge closer to the city's 50-foot water setback can trigger the same Section 60.224 review a new installation needs ({ext(ORLANDO_TURF_CODE[1], "the city's turf permit page")}). Knowing that distinction before quoting a job matters more in Orlando than in a jurisdiction with no turf-specific code at all.</p>"),
            ("Older ranch turf and newer Baldwin Park turf failing on different clocks",
             "<p>A mid-century ranch lot around SoDo that had turf installed a decade or more ago is more likely showing a fines-crusted base from before Florida's current subgrade standard, while a Baldwin Park yard turfed more recently is more likely dealing with an edge that lifted after a storm or a seam that opened under normal wear. Telling those apart on a phone call is hard, which is why photos of the affected area, taken close and from a few feet back, usually shape the first estimate more than the neighborhood does.</p>"),
        ],
        "scenario": ("A wrinkled seam near Delaney Park",
                     "<p>Say you have a 900 sq ft backyard near Delaney Park with a 40 ft seam that's started to wrinkle along one edge, and a live oak stands about 15 feet from the affected section. A close-up photo and a wider shot of the seam are usually enough for a first read on scope, but confirming whether a root is involved means lifting the corner on site, since a photo can't show what's happening under the turf. If a root is the cause, the fix may mean rerouting that section of edge rather than a straight reseam, which changes the scope from what a phone estimate alone would suggest.</p>"),
        "faqs": [
            faq("Does a small reseam need Orlando's Engineering Permit?", "Usually not. A repair that stays within the turf's existing footprint and doesn't touch grading near a water body generally falls outside the permit process that a new installation needs."),
            faq("How do you tell root heave from a settled base on an older Orlando lawn?", "A settled base tends to produce a broad, shallow dip, while a root heaves a narrower ridge that often points back toward a nearby tree's trunk. Lifting the corner and checking underneath is the only reliable way to confirm which one is happening."),
            faq("Why doesn't Orlando turf repair have a published price range like a new install?", "Because the work varies too much by cause. A reglued seam, a rebuilt base section and a root-related edge reroute take different time and material, so a firm number follows photos or a visit rather than a flat per-square-foot rate."),
        ],
        "sources": SRC,
    },
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
