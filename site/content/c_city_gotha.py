# -*- coding: utf-8 -*-
"""Gotha, FL (tier 2, unincorporated Orange County CDP). Local research checked September 2026; see SRC
for every source used. County-level permitting, water-management-district and soil facts are reused from
site/content/c_permits.py (Orange County page) and site/content/c_counties.py (Orange County hub) --
same underlying facts and URLs already verified there, new sentences written for this module."""
from _data import CITIES
from _helpers import page, capsule, sec, table, faq, a, svc, city, cs, post, src, ext, price
from _cityservice import cityservice_pages

SLUG = "gotha"
C = CITIES[SLUG]

ORANGE_CODE = ("Orange County Code, Chapter 24, Municode Library", "https://library.municode.com/fl/orange_county/codes/code_of_ordinances?nodeId=PTIIORCOCO_CH24LABUOPSP")
ORANGE_FASTTRACK = ("Orange County Fast Track Online Services", "https://fasttrack.ocfl.net/OnlineServices/")
ORANGE_WATERING = ("Orange County Utilities -- watering restrictions", "https://www.orangecountyfl.net/watergarbagerecycling/wateringrestrictions.aspx")
ORANGE_SEPTIC = ("Orange County -- Septic Pollution Prevention", "https://www.orangecountyfl.net/environment/septicpollutionprevention.aspx")
HISTORY_CENTER = ("Orange County Regional History Center -- The Koehnes of Gotha", "https://www.thehistorycenter.org/the-koehnes-of-gotha/")
GOTHA_HISTORY = ("Nehrling Gardens -- Gotha Community history", "https://nehrlinggardens.org/history/gotha-community/")
NEHRLING_GARDENS = ("Nehrling Gardens", "https://nehrlinggardens.org/")
GOTHA_LAKES_NEWS = ("Spectrum News 13 -- Gotha's rising lakes", "https://mynews13.com/fl/orlando/news/2020/06/08/gotha-lake-nally-rising-water")
ASTATULA_OSD = ("USDA NRCS -- official series description, Astatula series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/A/ASTATULA.html")
CANDLER_OSD = ("USDA NRCS -- official series description, Candler series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/C/CANDLER.html")
ORANGE_PA = ("Orange County Property Appraiser -- parcel search", "https://ocpafl.org/")

SRC = [ORANGE_CODE, ORANGE_FASTTRACK, ORANGE_WATERING, ORANGE_SEPTIC, HISTORY_CENTER, GOTHA_HISTORY, NEHRLING_GARDENS,
       GOTHA_LAKES_NEWS, ASTATULA_OSD, CANDLER_OSD, ORANGE_PA, "dep-rule", "fs125572", "usda-wss", "census-acs"]


def nb(slug, label=None):
    return (CITIES[slug]["route"], label or f"Turf in {CITIES[slug]['name']}")


# ============================================================== hub
HUB_BODY = "".join([
    sec("A rural corner of Orange County, not a town hall",
        f"<p>Gotha has never incorporated, so there's no city hall, no council and no city code to check for a turf rule, only the Orange County Division of Building Safety, which reviews the parcel the same way it reviews any other unincorporated address between {city('windermere', 'Windermere')} and {city('ocoee', 'Ocoee')}. Permitting Services takes calls at 407-836-5550 and runs applications through the county's Fast Track Online Services rather than a local counter of its own.</p>"
        + f"<p>Chapter 24 of Orange County's own code, the section covering landscaping and open space, only recognizes living grass species, Bahia, Bermuda, Centipede and St. Augustine among them, when it defines what counts as turf, and it has nothing written for a manufactured version either way. That gap means a Gotha lawn conversion isn't colliding with a written county turf rule, but it still meets the county's ordinary landscape and drainage permitting, plus whatever {src('dep-rule', 'the Florida turf standard')} adds on top: turf stays legal on a covered acre-or-less lot no matter what the county might prefer, the permeability ask tops out at 10 inches an hour, and the waterbody buffer can't outdo the one grass already lives with. {a('/laws/permits/orange-county/', 'Our Orange County permit page')} has the fuller code write-up.</p>"),
    sec("Gotha yard types and what we do differently",
        "<p>Four property types cover most of what a crew runs into on a Gotha street, and each one changes the plan before the first shovel of sod comes up.</p>"
        + table("Gotha yard types and what we do differently",
                ["Property type", "Typical lot", "What changes for turf"],
                [["Legacy citrus-era homesteads", "Half an acre to several acres", "A septic system is common, so the tank's pump-out lid gets mapped before any base goes down"],
                 ["Lake Fischer and Lake Nally waterfront", "Around the community's closed-basin lakes", "No storm drain to fall back on, so the state's setback and swale rules carry more weight than usual"],
                 ["Newer estate infill near the Windermere line", "West and south edges of the community", "Larger, flatter pads that sit closer to a standard county water hookup than the older lots do"],
                 ["In-town lots near the Hempel Avenue crossroads", "The historic center of the community", "Smaller yards platted before modern setback rules, worth a parcel check ahead of a quote"]],
                "Every lot still gets the same washed-rock base and published price range; what changes is drainage, septic access and how much land actually surrounds the house.")),
    sec("Water, wells and a county that counts its septic tanks",
        f"<p>Gotha's water carries the same seasonal limit Orange County Utilities sets for the rest of the unincorporated county: a separate day for odd- and even-numbered addresses, that allowance dropping from two of those days to one once daylight saving time ends, and nothing running between 10 a.m. and 4 p.m. regardless of the season ({ext(ORANGE_WATERING[1], 'current county restrictions')}). Orange County doesn't publish a water-customer map down to the neighborhood level, and Gotha's half-acre-and-up lots are exactly the kind of larger, older parcel where a private well is at least as likely as a county meter, so that's worth confirming with Orange County Utilities before a bid assumes either one.</p>"
        + f"<p>The county counts more than 85,000 septic tanks countywide, concentrated in older, larger-lot subdivisions like this one, and new rules effective March 2025 require enhanced, nitrogen-reducing systems on repairs and new installs on lots of an acre or less ({ext(ORANGE_SEPTIC[1], 'the Orange County septic program')}). None of that changes the turf job directly, beyond the state rule's own requirement that a septic tank's access stay reachable once the lawn around it is finished.</p>"),
    sec("Ground shaped by citrus rows and closed-basin lakes",
        f"<p>West Orange County's ridge carries Astatula and Candler fine sands, excessively drained soils built from thick wind-blown and marine sand deposits on the South-Central Florida Ridge ({ext(ASTATULA_OSD[1], 'the USDA official series description')}; {ext(CANDLER_OSD[1], 'the Candler series description')}). Ground like that sheds water almost immediately, which sounds convenient until a crew tries to lock a level base into sand loose enough to shift under a plate compactor mid-pass, the reverse of the slow-draining flatwoods problem under {city('hunters-creek', 'east Orange County')} lots.</p>"
        + f"<p>Fast-draining sand hasn't stopped Gotha's own lakes from causing trouble: Lake Fischer, Lake Nally, Lake Hugh, Mills Pond and Gotha Pond are landlocked, with no natural drainage outlet, and Lake Nally's level climbed roughly 15 feet over several wet years before Orange County commissioned a $200,000 engineering study into the cause ({ext(GOTHA_LAKES_NEWS[1], 'Spectrum News 13 coverage')}). A lot near any of those five bodies of water answers to the state's 10-foot setback and its littoral-zone ban the same way any lakefront lot would, worth double-checking given this particular lake system's history.</p>"),
    sec("A German colony, Henry Nehrling's gardens and how fast the place has grown",
        f"<p>Henry Hempel platted Gotha in 1885 as a colony for German immigrants, built around a sawmill, a general store, a post office, a school and a community hall, with the Turnverein's hall hosting gymnastics, dances and minstrel shows for the settlers who followed him here ({ext(HISTORY_CENTER[1], 'the Orange County Regional History Center')}). Horticulturist Henry Nehrling started buying land nearby the same year, and the tropical and experimental garden he built, tested with the USDA and known today as {ext(NEHRLING_GARDENS[1], 'Nehrling Gardens')}, earned a spot on the National Register of Historic Places in 2000.</p>"
        + f"<p>The Census counted 731 residents in Gotha in 2000, 1,915 in 2010 and 2,217 in 2020 ({src('census-acs', 'Census Bureau figures')}), which is a faster three-decade climb than the citrus-and-Turnverein settlement's founders would likely have pictured. The growth shows up as infill on larger lots rather than a wholesale subdivision buildout, which is part of why Gotha still reads as rural compared with {city('winter-garden', 'Winter Garden')} or {city('horizon-west', 'Horizon West')} next door.</p>"),
    "<!--AUTO:city-services-->",
])

HUB_FAQS = [
    faq("Is Gotha its own town, or part of Orange County?",
        "Gotha has never incorporated. It's a census-designated place inside unincorporated Orange County, so a permit question goes to the county's Division of Building Safety at 407-836-5550, not to a city hall, since Gotha doesn't have one."),
    faq("How do you find the best artificial turf company near you in Gotha?",
        "Ask whether the crew already treats a septic-served, half-acre lot differently from a standard subdivision yard, since that changes base planning and access. Beyond that, the usual checklist applies: named base material and depth, infill type and rate, and a written measurement rather than a guess off a listing photo."),
    faq("Do Gotha's flooding lakes affect where turf can go?",
        "Only in the way any lakefront lot works: the state's 10-foot setback from the ordinary water line applies to Lake Fischer, Lake Nally and the community's other closed-basin lakes, and turf can't go inside a pond's littoral zone regardless of how that specific lake has behaved in recent years."),
    faq("Does a septic system change how a Gotha lawn gets built?",
        "It changes one specific step: the tank's pump-out lid gets located and kept clear before the base goes in, since the state's turf rule requires that access stay reachable once the lawn is finished, not buried under compacted rock and turf like the rest of the yard."),
    faq("Which water management district covers Gotha?",
        "Gotha sits in west Orange County near Windermere and Ocoee, both of which fall under the St. Johns River Water Management District rather than the South Florida district, whose Orange County territory only reaches the county's southeastern corner near Lake Nona and the Osceola line."),
]

HUB = page("/areas/gotha/", "city",
           "Artificial Turf Installation in Gotha, FL (2026)",
           "Synthetic turf installed in Gotha, FL, between Windermere and Ocoee, priced $8-$18 a sq ft. Septic, wells and closed-basin lakes covered. Sept. 2026.",
           "Artificial turf across Gotha",
           capsule(f"Kissimmee Artificial Turf installs and repairs synthetic lawns in Gotha, an unincorporated Orange County community platted in 1885, at {price('residential')} a square foot as of September 2026. Half-acre-and-up lots, working septic systems and a cluster of closed-basin lakes change the base plan here more than the turf choice does."),
           HUB_BODY, faqs=HUB_FAQS, sources=SRC, city=SLUG,
           crumbs=[("Service areas", "/areas/")], crumb="Gotha",
           related=[("/areas/orange-county/", "Artificial turf in Orange County"),
                    ("/laws/permits/orange-county/", "Orange County permit rules for turf"),
                    nb("windermere", "Turf in Windermere"),
                    nb("winter-garden", "Turf in Winter Garden"),
                    ("/artificial-turf-cost/", "Full turf cost guide")])

# ============================================================== LOCAL
LOCAL = {
    "residential": {
        "title": "Artificial Grass Installation in Gotha, FL",
        "meta": "Synthetic lawn installation on Gotha, FL's rural-residential lots, from septic-tank access to Orange County permitting, priced $8-$18 a sq ft. Sept. 2026.",
        "h1": "Installing artificial grass on a Gotha lot",
        "lede": capsule(f"In Gotha, installed synthetic grass runs {price('residential')} a square foot, typically {price('residential', True)}, as of September 2026, the same published range as everywhere else. A half-acre or larger lot here is common enough that a residential quote often covers more square footage, more septic-tank planning and more open sun than a standard Orange County subdivision job does."),
        "sections": [
            ("Orange County's office, and what its code actually says",
             f"<p>Gotha has no city government of its own, so a lawn conversion answers to Orange County's Division of Building Safety, reachable at 407-836-5550, with applications filed through the county's Fast Track Online Services. The county's Chapter 24 defines \"turf\" only as a list of living grass species, with no section written for a synthetic product, which leaves the county's ordinary landscape and drainage permitting, plus {src('dep-rule', 'the state turf standard')}, as the written rules that actually apply.</p>"
             + f"<p>A parcel search on the {ext(ORANGE_PA[1], ORANGE_PA[0])} confirms the taxing jurisdiction before a call goes out, since a Gotha-area mailing address can sit close enough to {city('ocoee', 'Ocoee')} or {city('windermere', 'Windermere')} that the county line isn't always where a homeowner expects it.</p>"),
            ("Sizing a lot that's closer to an acre than a quarter of one",
             f"<p>Where a standard {city('winter-garden', 'Winter Garden')} subdivision lot might run a fifth of an acre, plenty of Gotha addresses sit on a half-acre or more, a holdover from the community's citrus-grove past. A bigger lot changes the math on a full-yard conversion more than it changes the method: more square footage at the same {price('residential')} range, more grading to plan across a larger fall, and often more existing shade from mature trees that were left standing when the grove around them was subdivided. The install method itself is no different from {svc('residential', 'our standard residential process')}; Gotha just asks more of the grading step because of the acreage.</p>"),
            ("Septic-tank access on an older Gotha parcel",
             f"<p>A number of Gotha's older, larger lots run on septic rather than a county sewer connection, which means the tank's pump-out lid has to stay reachable once turf and base material go down around it, a requirement that comes from {src('dep-rule', 'the state turf rule')} itself rather than from any county add-on. {post('how-artificial-turf-is-installed-step-by-step', 'Mapping that lid during layout')}, before the base gets built up around it, is a faster fix than relocating compacted rock later.</p>"),
        ],
        "scenario": ("Say you have a half-acre former citrus lot",
                     f"<p>Say you have a 2,000 sq ft front and back yard on a half-acre Gotha lot where the grove that once stood there gave way to a house decades ago, and a septic tank sits near the side yard. At {price('residential')} a square foot, a full conversion runs $16,000 to $36,000, and at the more typical {price('residential', True)}, most quotes land between $20,000 and $32,000. Locating the septic lid during the initial walk keeps the base plan from having to shift later, and the extra square footage compared with a standard subdivision lot is the main reason a Gotha quote often lands higher in total than a same-priced job on a smaller lot nearby.</p>"),
        "faqs": [
            faq("Does Gotha have its own building department, separate from Orange County?",
                "No. Gotha has never incorporated, so Orange County's Division of Building Safety handles permitting for the entire community at 407-836-5550, the same office that covers the rest of unincorporated Orange County."),
            faq("Do all Gotha homes have septic systems?",
                "Not all, but enough of the older, larger lots do that it's worth checking before a quote assumes a county sewer connection. Newer estate infill closer to the Windermere line is more likely to run on county utilities."),
        ],
        "sources": SRC,
    },
    "pet": {
        "title": "Pet Turf and Dog Runs in Gotha, FL",
        "meta": "Pet turf and dog runs in Gotha, FL, planned around the community's closed-basin lakes and drainage history, priced $10-$18 a sq ft. Checked Sept. 2026.",
        "h1": "Pet turf built for Gotha's drainage",
        "lede": capsule(f"Expect to pay {price('pet')} a square foot for pet turf in Gotha, typically {price('pet', True)}, as of September 2026. A dog run near Lake Fischer, Lake Nally or one of the community's other closed-basin lakes gets planned around drainage more carefully than a run on higher, better-drained ground a few streets away."),
        "sections": [
            ("Why a landlocked lake changes a drainage conversation",
             f"<p>Lake Fischer, Lake Nally, Lake Hugh, Mills Pond and Gotha Pond have no natural outlet, and Lake Nally's water level rose roughly 15 feet over a run of wet years before the county funded a study into why ({ext(GOTHA_LAKES_NEWS[1], 'Spectrum News 13 reporting')}). A dog run near any of those five bodies of water sits on ground that's already prone to holding water longer than a typical yard, which is exactly the situation where washed, open-graded rock earns its keep over compacted fill that would trap moisture at the surface instead of letting it pass through.</p>"),
            ("Skipping the weed barrier where dogs actually run",
             "<p>Skipping the weed-fabric layer is one of the few build differences between a Gotha dog run and a standard lawn: with fabric in place, urine pools right at the surface instead of passing down into the rock the way the infill is meant to handle it, so pet areas go without it while a plain lawn usually gets it. That trade-off carries more weight on a low, poorly draining Gotha lot near one of the community's lakes than it would on a well-drained parcel up on the ridge.</p>"),
            ("A run sized for a half-acre lot, not a zero-lot-line yard",
             f"<p>Where a dog run on a tight subdivision lot often gets squeezed into a narrow side yard, Gotha's larger citrus-legacy parcels usually have room for a run set well away from the house and any septic field, which gives a crew more flexibility on shape and orientation than a {city('dr-phillips', 'Dr. Phillips')}-style zero-lot-line yard would allow. That extra space is also useful for keeping the run clear of a property's septic drain field, which shouldn't carry the extra saturation a heavily used pet area can add. Infill and backing choices follow {svc('pet', 'the same pet-turf specifics')} used on a tighter lot; extra space changes layout, not materials.</p>"),
        ],
        "scenario": ("Say you have a run near the back property line",
                     f"<p>Say you have a 350 sq ft dog run along the back of a Gotha lot, roughly 200 feet from the edge of Lake Fischer, on ground that stays damp longer than the front yard after a hard rain. At {price('pet')} a square foot, that run costs $3,500 to $6,300, and at the more typical {price('pet', True)}, most quotes fall between $4,200 and $5,600. Because the lot sits near a closed-basin lake with a documented history of rising water, the base goes in at the fuller end of the state's two-to-four-inch rock depth rather than the shallow end, and the layout keeps clear of the 10-foot setback from the lake's ordinary water line.</p>"),
        "faqs": [
            faq("Does a dog run near Lake Fischer or Lake Nally need a bigger setback than the state's 10 feet?",
                "Nothing published sets a Gotha-specific number beyond the state standard. The 10-foot setback from the ordinary or mean high water line applies the way it would on any other Florida lake, unless a seawall already separates the yard from the water."),
            faq("Should a Gotha dog run go in before or after a septic inspection?",
                "Before, if the run's location is anywhere near the drain field. Confirming the field's boundaries first avoids compacting soil the septic system needs to stay permeable."),
        ],
        "sources": SRC,
    },
    "putting": {
        "title": "Backyard Putting Greens, Gotha FL",
        "meta": "Backyard putting greens on Gotha, FL's larger citrus-legacy lots, priced $14-$30 a sq ft, with room the average subdivision yard doesn't have. Sept. 2026.",
        "h1": "Backyard putting greens on Gotha's larger lots",
        "lede": capsule(f"A Gotha putting green costs {price('putting')} a square foot as of September 2026, typically {price('putting', True)}. The half-acre-and-up lots common on this community's old citrus ground give a green more room to work with than a standard subdivision yard, closer in spirit to the private gardens Henry Nehrling once tended nearby."),
        "sections": [
            ("Room to build a real contour, not a compromise",
             f"<p>Gotha's legacy citrus-grove lots, often a half-acre or more, give a putting green designer space a standard {city('winter-garden', 'Winter Garden')} lot rarely offers: room for a multi-tier green with a real fringe width, set back far enough from the house that a mis-hit chip isn't a daily concern. That extra land is also useful for routing the green around any remaining mature oaks left standing when the surrounding grove was cleared for houses. {svc('putting', 'Our putting-green page')} covers contour shaping and cup placement in more depth than a single Gotha lot needs repeated here.</p>"),
            ("A neighbor to Nehrling's own experimental gardens",
             f"<p>Henry Nehrling built his tropical and experimental garden nearby starting in 1885, testing thousands of plant species on land not far from where a modern Gotha putting green might go in today ({ext(NEHRLING_GARDENS[1], 'Nehrling Gardens')}). The connection is more historical color than a technical one, since a synthetic green doesn't answer to the same soil and irrigation questions Nehrling's live plantings did, but it's a reminder that this ground has supported ambitious landscaping projects for well over a century.</p>"),
            ("Grading a green on excessively drained ridge sand",
             f"<p>West Orange County's Astatula and Candler fine sands drain almost as fast as the turf that would sit on top of them ({src('usda-wss', 'the USDA soil data')}), which is unusual for Central Florida and changes what a green's base has to solve. Instead of fighting a high water table the way a build near {city('ocoee', 'Ocoee')}'s flatter, wetter ground might, the base here focuses on holding a stable, level contour on sand that wants to shift before compaction locks it in place.</p>"),
        ],
        "scenario": ("Say you have room for a real multi-tier green",
                     f"<p>Say you have a 600 sq ft green with fringe planned for a half-acre Gotha lot, tucked into a back corner shaded by two oaks left standing from the property's citrus-grove days. At {price('putting')} a square foot, that runs $8,400 to $18,000, and at the more typical {price('putting', True)}, most quotes land between $10,800 and $15,000. The extra lot size means the green can sit more than 20 feet from the house, far enough that a mis-hit rarely reaches a window, and the fast-draining ridge sand underneath means the base work focuses on stability rather than fighting standing water.</p>"),
        "faqs": [
            faq("Do Gotha's bigger lots cost more to build a putting green on?",
                "Not per square foot; the published range doesn't change with lot size. A larger lot just means more room to design a bigger or more contoured green if the owner wants one, not a higher price for the same footprint."),
            faq("Does the fast-draining ridge sand near Gotha mean a green needs less base?",
                "No. Fast drainage keeps water from pooling, but it doesn't hold a level, stable contour on its own, which is what the compacted base actually does. A Gotha green still gets the same two to four inches of washed rock as anywhere else."),
        ],
        "sources": SRC,
    },
    "playground": {
        "title": "Playground Turf for Gotha Families",
        "meta": "Playground turf for Gotha, FL families on larger lots, priced $10-$25 a sq ft, sized to fall height, as the community's population keeps climbing. Sept 2026.",
        "h1": "Playground turf for Gotha's growing families",
        "lede": capsule(f"Budget {price('playground')} a square foot for playground turf in Gotha, typically {price('playground', True)}, as of September 2026. The Census counted 731 residents here in 2000 and 2,217 by 2020, and a fair share of that growth has been young families moving onto lots with enough room for a real play area, not just a corner of a small yard."),
        "sections": [
            ("A community that once built a hall for exactly this",
             f"<p>Gotha's German settlers organized a Turnverein in the 1880s, building a hall for gymnastics instruction, dances and community events almost as soon as the colony was platted ({ext(HISTORY_CENTER[1], 'the Orange County Regional History Center')}). A backyard play area is a much smaller version of the same instinct, giving kids a dedicated, safer space to be active, and the state's rule for what that surface can be made of, permeable turf with synthetic infill limited to the equipment's own footprint, is a much newer answer to an old idea.</p>"),
            ("Padding a play structure to its actual fall height",
             "<p>A shock pad under playground turf is specified to the height a child could fall from, not to the size of the yard around it, so a taller climbing structure needs a thicker pad than a low slide does even on the same square footage. Pulling that number from the equipment's own manufacturer specification, rather than assuming a default thickness, avoids both an underbuilt pad and unnecessary cost from over-padding a low piece of equipment.</p>"),
            ("Space that a citrus-grove lot still has to offer",
             f"<p>A Gotha lot with room left over from its citrus-grove past can usually separate a play area from the rest of the yard by more distance than a standard {city('horizon-west', 'Horizon West')} subdivision allows, which matters for keeping a ball in play clear of a septic drain field or a mature tree's drip line. That separation is a planning advantage newer, tighter-lotted communities nearby don't have as often. Pad thickness and infill rules stay identical to {svc('playground', 'the citywide playground-turf guide')}; a Gotha lot mostly just has more room to place it.</p>"),
        ],
        "scenario": ("Say you have a swing set going in past the patio",
                     f"<p>Say you have a 300 sq ft play area planned well past the patio on a Gotha lot, around a swing set with a 7-foot fall height, with enough side yard to keep it clear of the property's septic field. At {price('playground')} a square foot, that runs $3,000 to $7,500, and at the more typical {price('playground', True)}, most quotes land between $3,600 and $5,700, with the shock pad sized to the 7-foot fall height. The extra distance from the drain field, easier to maintain on a larger lot than a small one, is confirmed before layout rather than assumed from a property survey alone.</p>"),
        "faqs": [
            faq("Does playground turf need to stay a set distance from a Gotha septic field?",
                "Nothing published sets a turf-specific distance, but keeping heavy foot traffic and any added soil compaction away from a drain field is standard practice regardless of what surface goes down, and a septic contractor can confirm the field's exact boundary."),
            faq("Can playground turf go near one of Gotha's oaks left from the grove era?",
                "Only outside that tree's drip line, unless a certified arborist certifies the installation won't cause harm. Older oaks left standing from a cleared citrus grove often have wider root spreads than their canopy suggests."),
        ],
        "sources": SRC,
    },
    "pool": {
        "title": "Pool and Lanai Turf in Gotha, FL",
        "meta": "Turf around Gotha, FL pool cages and lanais, priced with the $8-$18 residential range, built for ridge sand and closed-basin lake setbacks. Sept. 2026.",
        "h1": "Turf around Gotha pool cages and lanais",
        "lede": capsule(f"Excessively drained ridge sand under most of Gotha changes how a pool-deck or lanai strip gets built more than it changes what goes on top, and it prices the same as any residential job: {price('residential')} a square foot, typically {price('residential', True)}, as of September 2026."),
        "sections": [
            ("Ridge sand that drains almost too well",
             f"<p>Astatula and Candler fine sands, the excessively drained soils common on west Orange County's ridge, pass water so fast that the usual concern with a high water table barely applies here ({ext(CANDLER_OSD[1], 'the USDA Candler series description')}). Against a pool deck, that means the base's job shifts from moving water away quickly to holding a stable, compacted surface on sand that shifts underfoot before a plate compactor locks it down, a different failure mode than the soggy flatwoods sand under a lot closer to {city('ocoee', 'Ocoee')}. {svc('pool', 'Our pool and lanai turf page')} covers the drainage-underlay and low-E glass questions in more depth than this section alone.</p>"),
            ("A pool cage close enough to a closed-basin lake",
             f"<p>A pool enclosure on a Lake Fischer or Lake Nally lot sits inside a community where those closed-basin lakes have a documented history of rising several feet over consecutive wet years ({ext(GOTHA_LAKES_NEWS[1], 'coverage of the county-commissioned engineering study')}). {src('dep-rule', 'The state-mandated 10-foot setback')} from the ordinary water line still governs how close turf can go, waived only where a seawall or bulkhead separates yard from water, and on a lake this changeable, staying well inside that line rather than right at its edge is worth the extra buildable-area math.</p>"),
            ("Low-E glass on a screened enclosure's own doors",
             f"<p>A screened lanai facing west or south toward open, sunny acreage, common on Gotha's larger lots, is exactly the orientation where low-emissivity glass can reflect enough concentrated light to soften turf several feet away, since {post('how-to-make-artificial-grass-look-real', 'the fiber itself')} starts to give around 175 to 200°F under that kind of focused heat. Checking the lanai's own sliding-door glass, not just the front of the house, is worth doing before or right after installation.</p>"),
        ],
        "scenario": ("Say you have a strip inside a screened enclosure",
                     f"<p>Say you have a 190 sq ft strip of turf planned along the edges of a screened pool deck on a Gotha lot roughly 300 feet from Lake Nally's shoreline. At {price('residential')} a square foot, that runs $1,520 to $3,420, and at the more typical {price('residential', True)}, most quotes land between $1,900 and $3,040. Because the strip sits well outside the state's 10-foot lake setback, the layout isn't constrained by that line, but the base still gets a drainage underlay where turf meets the pool deck's concrete edge, the same as it would on any screened enclosure regardless of how far the water sits.</p>"),
        "faqs": [
            faq("Does Gotha's ridge sand drain too well for a pool-deck base?",
                "Fast drainage doesn't replace the compacted base; it changes what the base has to fight. On loose ridge sand, the priority shifts from moving water away to holding a level, stable surface, which still means two to four inches of washed rock either way."),
            faq("How close can a Gotha pool cage sit to Lake Fischer or Lake Nally?",
                "The state's 10-foot setback from the ordinary water line applies unless a seawall or bulkhead already separates the property from the lake, the same rule that governs any other Florida waterfront lot."),
        ],
        "sources": SRC,
    },
    "repair": {
        "title": "Artificial Turf Repair Serving Gotha, FL",
        "meta": "Artificial turf repair in Gotha, FL: seams, drainage and septic-lid access on older rural lots, quoted after a site visit. Checked September 2026.",
        "h1": "Fixing artificial turf on a Gotha lot",
        "lede": capsule("A flat rate doesn't work for turf repair in Gotha, since pricing a fix takes photos or a walk of the property: a lawn near one of the community's closed-basin lakes fails differently than one on a dry ridge-sand lot near Hempel Avenue. As of September 2026, the calls that come in most often involve a buried septic lid, a low spot that won't drain, and an edge a summer storm worked loose."),
        "sections": [
            ("Finding a septic lid that's been covered for years",
             f"<p>On an older Gotha lot, a repair call sometimes starts with locating a septic tank's pump-out lid that was never mapped clearly when the lawn went in, since {src('dep-rule', 'the state turf rule')} requires that access stay reachable rather than buried under settled infill and turf. A repair crew checks septic records or probes the likely area before pulling any turf, since guessing wrong means disturbing more of the lawn than the fix actually needs. {svc('repair', 'Our turf-repair page')} runs through the seam, edge and drainage failures that show up most often statewide; Gotha's septic step is the local add-on.</p>"),
            ("Drainage repairs near a closed-basin lake",
             f"<p>A lot near Lake Fischer, Lake Nally or one of the community's other landlocked lakes can develop a soggy low spot faster than a lot on higher ground, especially after the kind of multi-year wet stretch that pushed Lake Nally up roughly 15 feet in recent years ({ext(GOTHA_LAKES_NEWS[1], 'Spectrum News 13 coverage')}). A repair there often means correcting the base's grade rather than just re-securing the turf on top of it, since a symptom at the surface usually traces back to what's happening underneath.</p>"),
            ("Storm-loosened edges on the historic crossroads lots",
             f"<p>The older, smaller lots near the Hempel Avenue crossroads were platted well before {a('/laws/florida-hb-683/', 'the current state anchoring standard')} existed, so a repair visit there sometimes finds a perimeter that was never nailed or bonded to withstand a tropical-storm-strength wind in the first place. {post('artificial-turf-hurricane-flooding', 'What a storm actually does to an under-anchored edge')} explains why that specific failure shows up after a system passes through rather than on an ordinary rainy afternoon.</p>"),
        ],
        "scenario": ("Say a low spot showed up after a wet summer",
                     "<p>Say you have a 25 sq ft depression that's developed in the middle of an otherwise flat lawn on a Gotha lot near one of the community's closed-basin lakes, holding water for a day or two after a normal afternoon storm. A repair visit checks whether the base settled unevenly under that spot or whether a nearby drainage path changed after work on a neighboring property, since a lake with a documented history of rising water makes the second explanation worth ruling out specifically. The fix, pulling back the turf, correcting the grade and recompacting before relaying it, gets quoted once the cause is confirmed rather than assumed from the symptom alone.</p>"),
        "faqs": [
            faq("Why would a Gotha lawn develop a low spot years after installation?",
                "Usually uneven settling in the base, sometimes worsened by a lot's proximity to one of the community's closed-basin lakes, which can raise the surrounding water table during a wet stretch. A repair visit checks the grade before assuming the turf itself is at fault."),
            faq("Does a septic system make Gotha turf repairs more expensive?",
                "Not automatically, but locating and clearing a pump-out lid before working nearby adds a step a subdivision repair on county sewer wouldn't need, which a technician accounts for once they see the lot."),
        ],
        "sources": SRC,
    },
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
