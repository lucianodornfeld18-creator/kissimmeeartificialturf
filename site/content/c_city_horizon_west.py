# -*- coding: utf-8 -*-
"""Horizon West, FL: Orange County's unincorporated master-planned villages west of the theme
parks (Bridgewater, Lakeside Village, Hamlin, Waterleigh, Summerlake, Independence and others),
built out mostly 2005-2026. Researched September 2026; see SRC for every local source."""
from _helpers import page, capsule, sec, table, faq, a, svc, city, post, src, ext, price
from _cityservice import cityservice_pages

SLUG = "horizon-west"

OC_PLANNING = ("Orange County Planning Division — Horizon West Special Planning Area", "https://www.ocfl.net/PlanningDevelopment/HorizonWest.aspx")
HW_WIKI = ("Wikipedia — Horizon West, Florida", "https://en.wikipedia.org/wiki/Horizon_West,_Florida")
HW_FACILITY = ("West Orange Times & Observer — Orange County opens new water supply facility in Horizon West", "https://www.orangeobserver.com/news/2021/nov/09/orange-county-opens-new-water-supply-facility-in-horizon-west/")
HAMLIN_WRF = ("Horizon West News & Info — Hamlin Water Reclamation Facility fully operational", "https://www.horizonwestinfo.com/hamlin-water-reclamation-facility-fully-operationally/")
LAKESIDE_ARC = ("Lakeside at Hamlin HOA — Community Standards and Architectural Guidelines", "https://lakesidehamlinhoa.com/arc-standards")
NITTAW_OSD = ("USDA NRCS — official series description, Nittaw series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/N/NITTAW.html")
OC_STORMWATER = ("Orange County Code — Article VII, Stormwater Management", "https://library.municode.com/fl/orange_county/codes/code_of_ordinances?nodeId=ORCOCO_CH34SURE_ARTVIISTMA_DIV1GERE_S34-228DEWIARSPFLHA")
SUBDIVISION_WAIVER = ("West Orange Times & Observer — County OKs subdivision plan for Horizon West", "https://www.orangeobserver.com/news/2020/jul/01/county-oks-subdivision-plan-for-horizon-west/")
GROWTH_PAINS = ("ClickOrlando — A 300% population increase over 10 years causes growing pains for this Florida community", "https://www.clickorlando.com/news/local/2023/09/20/a-300-population-increase-over-10-years-causes-growing-pains-for-this-florida-community/")
ORANGE_PA = ("Orange County Property Appraiser — parcel search", "https://ocpafl.org/")
OC_UTIL = ("Orange County Utilities — watering restrictions", "https://www.orangecountyfl.net/watergarbagerecycling/wateringrestrictions.aspx")
SFWMD_KISS = ("South Florida Water Management District — Upper Kissimmee Basin water supply plan", "https://www.sfwmd.gov/our-work/water-supply/upper-kissimmee")
PERMITS_ORANGE = ("/laws/permits/orange-county/", "Orange County turf permit rules")
HOA_ROUTE = ("/laws/hoa-rules/", "What a Florida HOA can and can't restrict")
HB683_ROUTE = ("/laws/florida-hb-683/", "HB 683 and DEP Rule 62-308.100")

SRC = [OC_PLANNING, HW_WIKI, HW_FACILITY, HAMLIN_WRF, LAKESIDE_ARC, NITTAW_OSD, OC_STORMWATER, SUBDIVISION_WAIVER, GROWTH_PAINS, ORANGE_PA, OC_UTIL, SFWMD_KISS, "dep-rule", "fs125572", "fs7203045"]

HUB = page(
    "/areas/horizon-west/", "city",
    "Artificial Turf in Horizon West, FL: New-Build Yards (2026)",
    "Artificial grass installation for Horizon West's master-planned villages, from builder sod that won't take to the stormwater-pond setback. Checked September 2026.",
    "Synthetic turf for Horizon West's new-build villages",
    capsule(f"We install, repair and clean synthetic lawns across Horizon West's master-planned villages, unincorporated Orange County land built out mostly since 2005, where turf runs {price('residential')} per square foot installed as of September 2026. Nearly every yard here sits within sight of a stormwater pond or a builder's original sod, and both of those change the plan before the turf choice does."),
    "".join([
        sec("Five villages, one building department",
            f"<p>Orange County's Horizon West Special Planning Area covers roughly 20,700 gross acres organized into five mixed-use villages and a town center, a plan the county adopted in 1995 and has been filling in ever since ({ext(OC_PLANNING[1], 'the county’s own Horizon West planning page')}). Bridgewater is one of the five formal villages; Hamlin, Waterleigh, Summerlake, Independence and Lakes of Windermere are the named communities most homeowners actually recognize, spread across those villages and the town center between them ({ext(HW_WIKI[1], 'a fuller rundown of the villages and their boundaries')}).</p>"
            + f"<p>All of it is unincorporated Orange County, so there's no separate Horizon West town hall the way there is a few miles east in Windermere. Permits run through Orange County Permitting Services at 407-836-5550, covered on {a(PERMITS_ORANGE[0], PERMITS_ORANGE[1])}, on top of the villages' own architectural-review layer, which most other unincorporated parts of the county don't carry.</p>"),
        sec("Horizon West yard types and what we do differently",
            table("Horizon West yard types and what we do differently",
                  ["Yard type", "What's different", "What that changes about the job"],
                  [["New-construction lot, first year or two", "Builder sod is thin and often stressed before closing", "We strip what's left rather than build turf on top of a root mat that never established"],
                   ["Alley-loaded small lot", "Narrow side access and a garage that faces the alley, not the street", "Material moves in by hand or wheelbarrow more often than by skid steer"],
                   ["Lot backing a stormwater pond", "The state's 10-ft waterbody setback applies at the pond's edge", "We hold turf back from the bank and never inside the littoral shelf"],
                   ["Village HOA lot under architectural review", "A committee reviews exterior changes against a published community standard", "A submittal with a sample and site plan goes in before the crew is scheduled"]],
                  "Every row still meets the same statewide material and drainage standard; what changes is the lot's age, its access and who signs off on the paperwork.")),
        sec("Water, reclaimed lines and what sits under a new pad",
            f"<p>Orange County Utilities serves Horizon West's villages, and the county backed that growth with a dedicated Hamlin Water Reclamation Facility, permitted under the St. Johns River Water Management District, that came online with 5 million gallons a day of reclaimed-water capacity for the area's newer subdivisions ({ext(HW_FACILITY[1], 'the water supply facility’s opening coverage')}; {ext(HAMLIN_WRF[1], 'the reclamation facility’s own capacity figures')}). A reclaimed line irrigates the sod that's still there; once a section converts to synthetic turf, the state's May 2026 standard bars using either a potable or a reclaimed in-ground system on it, and the head simply gets capped.</p>"
            + f"<p>Horizon West also sits near the point where three water management districts coordinate under the Central Florida Water Initiative, since the Kissimmee Basin's planning area reaches into southwest Orange County not far from here ({ext(SFWMD_KISS[1], 'SFWMD’s Upper Kissimmee Basin plan')}). Underfoot, the villages were built around a deliberate network of greenbelts and stormwater ponds, and the low, poorly drained pockets inside that network often map to Nittaw-type soil, a very slowly permeable series found in Florida's swamps and marshes, standing water and all, for months at a time ({ext(NITTAW_OSD[1], 'USDA’s official series description')}). The buildable pad on most lots sits above that on trucked-in fill, graded to keep the house dry.</p>"),
        sec("Village HOAs, the pond setback and the state's turf rule",
            f"<p>Horizon West's villages are thick with homeowners associations layered on top of the county's own review, and at least one of them publishes exactly what it expects a lawn to look like: Lakeside at Hamlin's community standards call for \"grassed front, side, and rear lawns\" of \"St. Augustine or other approved Florida-Friendly grass,\" ban \"gravel or similar type lawns,\" and set minimum sod-band widths along the sidewalk, the driveway and the side property line, all reviewed by an architectural board with up to 45 days to answer a submittal ({ext(LAKESIDE_ARC[1], 'Lakeside at Hamlin’s published architectural guidelines')}). That document doesn't mention synthetic turf either way, so a homeowner there is submitting into a covenant written for live sod, not against a stated turf ban.</p>"
            + f"<p>{a(HB683_ROUTE[0], HB683_ROUTE[1])} sets the floor under all of that: no waterbody buffer stricter than natural grass gets, no permeability rule tighter than 10 inches an hour, and the same 10-foot pond setback that shows up on nearly every Horizon West lot with a water view. {a(HOA_ROUTE[0], HOA_ROUTE[1])} still leaves the front-yard visibility question to the association, which is where a covenant like Lakeside at Hamlin's keeps its say.</p>"),
        "<!--AUTO:city-services-->",
    ]),
    faqs=[
        faq("How do you pick the best artificial turf company near you in Horizon West?",
            "Ask whether the crew already treats a first-year builder lot differently from an established one, since thin, stressed sod comes out differently than an older, rooted lawn. Beyond that, the same checklist applies here as anywhere: base depth and material, product face weight, and infill type in writing before a deposit changes hands."),
        faq("Is Horizon West one village or several?",
            "Several. Orange County's plan organizes it into five formal villages and a town center, though most residents know the area by community names like Hamlin, Waterleigh, Summerlake and Independence rather than by the village boundaries themselves."),
        faq("Does a Horizon West HOA's sod requirement rule out synthetic turf?",
            "Not automatically. The one published guideline we found, from Lakeside at Hamlin, requires a grassed lawn and specific sod-band widths but doesn't name synthetic turf as prohibited or approved. A submittal through the architectural review process, with a sample and a site plan, is how a specific community answers that question."),
        faq("Why do so many Horizon West lots back up to a pond?",
            "The villages were designed around a network of stormwater ponds and greenbelts rather than a single retention area, which is part of the master plan's own drainage design. That layout means the state's 10-foot waterbody setback comes up on a large share of backyards here, more than in an older subdivision built around one central pond."),
        faq("How far is Horizon West from downtown Kissimmee?",
            "About 16 miles by straight line, similar to Windermere just to its north. That figure is for scheduling, not price, since turf costs the same per square foot everywhere in our service area."),
    ],
    sources=SRC, crumbs=[("Service areas", "/areas/")], crumb="Horizon West", city=SLUG,
    related=[("/areas/orange-county/", "Artificial turf in Orange County"), PERMITS_ORANGE, ("/areas/windermere/", "Turf in Windermere"), ("/areas/winter-garden/", "Turf in Winter Garden"), ("/artificial-turf-cost/", "Turf cost tables for Central Florida")],
)

LOCAL = {
    "residential": {
        "title": "Artificial Grass Installation in Horizon West, FL",
        "meta": "Residential turf installation for Horizon West's new-build villages, priced per square foot, with builder sod and the stormwater-pond setback explained.",
        "h1": "Synthetic lawns for Horizon West's new-build villages",
        "lede": capsule(f"A residential lawn conversion in Horizon West runs {price('residential')} per square foot installed, typically {price('residential', True)}, as of September 2026. Most lots here were built since 2005 on a small footprint next to a stormwater pond, which shapes the job more than the age of the neighborhood does."),
        "sections": [
            ("Why builder sod struggles here specifically",
             "<p>A production builder lays sod on a lot that was graded and compacted weeks earlier, often over subsoil that never had time to recover its structure before the pallets arrived. On a small Horizon West lot with a short window between the final grade and closing, that sod frequently arrives thin and under-rooted, and a homeowner who's fought a patchy lawn for a year or two is a common candidate for a full conversion rather than another reseed.</p>"
             "<p>Stripping that root mat and the compacted layer under it, rather than laying turf over what's there, is the difference between a lawn that holds up and one that repeats the same drainage problem under a new surface.</p>"),
            ("Small lots, alleys and how material actually gets in",
             f"<p>A meaningful share of Horizon West's newer sections use an alley-loaded layout, where the garage faces a rear alley instead of the street, freeing the front yard for a porch and a narrow lawn instead of a driveway ({ext(SUBDIVISION_WAIVER[1], 'a 2020 county approval describing that lot layout')}). That design usually means a tighter side-yard gate than a conventional driveway-front lot, so base material and turf rolls move in by wheelbarrow rather than skid steer, which is worth factoring into a bid on a lot under about 65 feet wide.</p>"
             "<p>The upside of a small lot is a shorter timeline: less square footage means less base to compact and fewer seams to run.</p>"),
            ("Grading a lawn that backs up to a pond",
             f"<p>A backyard that ends at a stormwater pond, common across Horizon West's greenbelt-and-pond layout, still needs to fall away from the house the same way any yard does, but the last several feet before the water are off-limits under {a(HB683_ROUTE[0], 'the state’s waterbody setback')}. Grading the usable turf area to drain toward that buffer strip, rather than pooling against the house, keeps the yard dry without pushing water where the rule says it can't go.</p>"
             f"<p>The same pond-and-fill combination shows up moving toward {city('windermere')}, {city('winter-garden')} and {city('four-corners')}, three nearby stops with their own take on new-construction ground, and {post('artificial-turf-vs-sod-cost-florida', 'our ten-year cost comparison')} covers why builder sod rarely wins that race long-term. {svc('residential', 'The residential turf page')} and our {city('horizon-west', 'Horizon West turf overview')} round out the rest.</p>"),
        ],
        "scenario": ("Say you have a 600 sq ft alley-loaded backyard against a retention pond",
                     f"<p>A 600 sq ft backyard on an alley-loaded Horizon West lot, with the rear 80 sq ft inside the state's 10-foot setback from a retention pond, leaves about 520 sq ft available to turf. At {price('residential')} per square foot, that runs roughly $4,160 to $9,360 depending on access and how much of the original builder sod has to come out first. The buffer strip stays as low ground cover or mulch rather than turf.</p>"
                     "<p>Because the side gate on an alley-loaded lot is often narrower than a standard driveway-front layout, moving several yards of base material in by wheelbarrow can add a half day to the schedule compared with a lot a truck can back straight into.</p>"),
        "faqs": [
            faq("Is it worth replacing builder sod that's only a year or two old?",
                "Often, yes, if it's already patchy despite regular watering, since thin sod on compacted new-construction fill rarely recovers on its own. A conversion at that point avoids paying to re-sod a second time before eventually turfing anyway."),
            faq("Does Orange County require anything extra for a new-construction lot?",
                "Nothing published specific to synthetic turf beyond the state's May 2026 standard. What a newer lot does add is a village HOA's own architectural review on top of the county's ordinary permitting, which an older unincorporated lot without that layer wouldn't have."),
        ],
        "sources": SRC,
    },
    "pet": {
        "title": "Pet Turf & Dog Runs in Horizon West, FL",
        "meta": "Pet-friendly synthetic turf for Horizon West's small fenced yards, with reclaimed-water irrigation and odor-control infill for new-build lots explained.",
        "h1": "Dog runs built for Horizon West's small fenced yards",
        "lede": capsule(f"Pet turf in Horizon West runs {price('pet')} per square foot installed, typically {price('pet', True)}, as of September 2026. A fenced side or rear yard on a new-build lot here is usually small enough that a dog run and the whole usable lawn are close to the same thing."),
        "sections": [
            ("A small yard means the run is the yard",
             "<p>On a typical Horizon West lot, the fenced area behind the house rarely exceeds a few hundred square feet once the patio and any pool cage are subtracted, so a dedicated pet turf zone often ends up covering most of the usable lawn rather than one corner of it. That changes the infill decision: since dogs use nearly the whole space rather than a defined strip, a full-yard zeolite or coated-sand infill makes more sense here than it would on a larger inland lot where only part of the grass sees daily traffic.</p>"),
            ("Reclaimed water doesn't reach a capped run",
             f"<p>Orange County Utilities pushes reclaimed water to a share of Horizon West's newer sections specifically for irrigation, drawn from the Hamlin Water Reclamation Facility that came online to serve the area's growth ({ext(HAMLIN_WRF[1], 'the reclamation facility’s service figures')}). That line keeps the remaining sod green on a schedule separate from the county's potable-water restrictions, but it stops mattering the moment a section converts to turf, since {a(HB683_ROUTE[0], 'the state standard')} bars watering synthetic turf from any in-ground system, reclaimed or not. A hose rinse takes over from there.</p>"),
            ("Getting a run past the architectural committee",
             f"<p>A village HOA that requires a grassed lawn, the way Lakeside at Hamlin's published standard does, is describing live sod, not ruling out synthetic turf by name, so a pet turf submittal there goes in as a landscape change with a sample and a site plan rather than as a request for an exception ({ext(LAKESIDE_ARC[1], 'Lakeside at Hamlin’s architectural guidelines')}). A neat edge, such as a paver or bender-board border matching the community's driveway sod-band style, tends to read as more finished to a reviewer than a plain nailed perimeter.</p>"
             f"<p>A similar HOA-versus-turf question comes up in {city('celebration')}, {city('dr-phillips')} and {city('windermere')}, and {post('pet-turf-vs-regular-artificial-grass', 'this comparison of pet turf and standard lawns')} explains why the infill choice matters more for dogs than the grass type does. {svc('pet', 'Our pet turf page')} has the full build spec.</p>"),
        ],
        "scenario": ("Say you have a 350 sq ft fenced yard for two dogs in Hamlin",
                     f"<p>A 350 sq ft fenced backyard in Hamlin, entirely converted to pet turf for two dogs, runs {price('pet')} per square foot, or about $3,500 to $6,300 at the published range with zeolite infill throughout rather than confined to one zone. Because the fence line is the property line here, there's no separate \"pet area\" to carve out. the whole space gets the same drainage-focused base and infill treatment.</p>"
                     "<p>An architectural review submittal goes in first if the HOA requires one for exterior changes, with a sample and a site sketch showing the fenced footprint, before the crew schedules the strip-out.</p>"),
        "faqs": [
            faq("Does a Horizon West HOA that requires sod also require live grass in a fenced backyard?",
                "The one published example we found, Lakeside at Hamlin, requires grassed front, side and rear lawns generally, without carving out an exception for a fenced area a neighbor can't see. Florida's HOA-visibility statute protects turf that isn't visible from the street or an adjacent lot, but it doesn't override an association's own landscape standard on its own."),
            faq("Is reclaimed water ever used to rinse a dog run instead of a hose?",
                "No. Reclaimed water in Horizon West runs through a separate irrigation system for sod and beds, not a hose bib, and the state standard bars using any in-ground system, potable or reclaimed, on synthetic turf once it's installed."),
        ],
        "sources": SRC,
    },
    "putting": {
        "title": "Backyard Putting Greens in Horizon West, FL",
        "meta": "Putting green installation for Horizon West's village lots, with architectural-review submittals and small-lot contouring for new construction explained.",
        "h1": "Putting greens for Horizon West's small village lots",
        "lede": capsule(f"A backyard putting green in Horizon West runs {price('putting')} per square foot installed, typically {price('putting', True)}, as of September 2026. A green here usually competes for space with a pool cage or a patio on a lot smaller than an older Central Florida subdivision would offer, so sizing it right matters more than the contouring does."),
        "sections": [
            ("Fitting a green onto a builder-sized lot",
             "<p>A Horizon West backyard rarely runs past a few hundred square feet once the patio, the pool cage where there is one, and the required side setbacks are subtracted, so a putting green here tends toward a compact single-cup or two-cup layout rather than the larger multi-hole greens that fit an older, wider lot elsewhere in our service area. A tighter footprint doesn't mean a lower-quality build; it just means the fringe and collar take up a bigger share of the total relative to the putting surface itself.</p>"),
            ("Submitting a green through a village's architectural review",
             f"<p>None of the published Horizon West HOA material we found addresses putting greens directly, so a submittal goes in as a general hardscape or landscape change: a site plan showing the green's footprint against the setbacks, a turf sample, and a description of any cup or fringe detail. Where a community's own standard calls for a grassed lawn, as Lakeside at Hamlin's does, showing that the green sits inside a fenced, non-visible portion of the yard, the kind {a(HOA_ROUTE[0], 'Florida’s HOA-visibility statute')} protects, is usually the stronger argument than arguing the covenant doesn't apply ({ext(LAKESIDE_ARC[1], 'Lakeside at Hamlin’s published guidelines')}).</p>"),
            ("Building a stable base on fill, not native ground",
             f"<p>Most Horizon West lots sit on pad fill trucked in and compacted during construction, above the naturally poorly drained, Nittaw-type soil found in the low pockets of the villages' preserved wetlands and pond edges ({ext(NITTAW_OSD[1], 'USDA’s official series description')}). That fill generally compacts more predictably than the wetter native ground underneath it, which helps a shaped putting surface hold its contour, provided the crushed-rock base still goes in washed and compacted in separate lifts rather than dumped and packed once.</p>"
             f"<p>Compact greens on fill soil aren't unique to Horizon West either; {city('winter-garden')}, {city('four-corners')} and {city('celebration')} all carry similarly sized lots worth their own look, and {post('artificial-turf-glossary', 'our glossary of putting-green terms')} explains stimp, fringe and pile height in plain language. {svc('putting', 'The putting green service page')} covers cup and contour options in more depth.</p>"),
        ],
        "scenario": ("Say you have a 400 sq ft green fitted beside a Summerlake pool cage",
                     f"<p>A 400 sq ft single-cup putting green squeezed into the side yard beside a pool cage on a Summerlake lot runs {price('putting')} per square foot, or about $5,600 to $12,000 at the published range, with a compact fringe rather than a wide collar to make the most of a narrow footprint. A second cup usually isn't practical at that size without crowding the fringe past a usable width.</p>"
                     "<p>An architectural review submittal, with the green's footprint measured against the lot's side setback, goes in before scheduling, and the base still gets built in two compacted lifts even though the green competes for space with the pool equipment pad next to it.</p>"),
        "faqs": [
            faq("Is there room for a putting green on a typical Horizon West lot?",
                "Usually a compact one. A single-cup green in the 300 to 500 sq ft range fits most fenced backyards here once the patio and any pool cage are accounted for; a full multi-hole green typically needs more room than a standard village lot has to spare."),
            faq("Do Horizon West village HOAs treat a putting green differently from a pool or a patio?",
                "Not under any published rule we found. It goes through the same architectural review as any exterior landscape or hardscape change, with a site plan and a sample, rather than a separate process specific to putting greens."),
        ],
        "sources": SRC,
    },
    "playground": {
        "title": "Playground Turf in Horizon West, FL",
        "meta": "Playground turf for Horizon West's young family neighborhoods, with shock-pad sizing for new equipment and the state's material rule explained.",
        "h1": "Cushioned play surfaces for Horizon West's newer yards",
        "lede": capsule(f"Playground turf in Horizon West runs {price('playground')} per square foot installed, typically {price('playground', True)}, as of September 2026. The villages have grown mostly since 2005 around young families, which is why a swing set or a play structure comes up more often here than the drip-line question a mature canopy would raise elsewhere."),
        "sections": [
            ("A community built around young families, not old oaks",
             f"<p>Horizon West's population grew more than 300 percent between 2010 and 2020, driven largely by families buying into new schools and new neighborhoods rather than moving into an established one ({ext(GROWTH_PAINS[1], 'coverage of that growth and its strain on infrastructure')}). That demographic is exactly who asks about backyard playground turf, and because most lots were cleared and rebuilt within the last two decades, a live oak old enough to cast the wide canopy that triggers the state's drip-line setback is still the exception here rather than the rule.</p>"),
            ("Sizing the shock pad to the equipment, not the yard",
             "<p>A play structure's fall height, not the size of the yard around it, sets how thick the shock pad under playground turf needs to be, and that number comes from the equipment's own specification sheet. A simple swing set on a Horizon West patio-adjacent lawn generally calls for less pad than a taller structure with a slide platform and a climbing wall, so ordering pad depth off the play set's own rating avoids over- or under-building the base.</p>"),
            ("Working around a pond view instead of a tree canopy",
             f"<p>Where a Horizon West lot's play area sits close to one of the villages' many stormwater ponds rather than under mature trees, {a(HB683_ROUTE[0], 'the state’s 10-foot waterbody setback')} is the rule that governs the layout instead of the drip-line rule that would apply on an older, oak-covered lot. Keeping the play structure and its turf pad set back from the pond bank, with a fence between the two if the association requires one, is the more common planning question on this kind of lot than tree-root protection ever is.</p>"
             f"<p>Pond-adjacent play areas come up just as often toward {city('dr-phillips')}, {city('windermere')} and {city('four-corners')}, and {post('coolest-artificial-grass-and-infill-for-florida', 'this rundown of cooler infill options')} is worth a look for a full-sun play area near open water. {svc('playground', 'Our playground turf page')} has the shock-pad specifics.</p>"),
        ],
        "scenario": ("Say you have a 250 sq ft play area between a patio and a pond-view fence",
                     f"<p>A 250 sq ft play area for a swing set, set between a Horizon West patio and a fence roughly 12 feet from a retention pond, runs {price('playground')} per square foot, or about $2,500 to $6,250 at the published range depending on the pad thickness the equipment's fall height requires. Because the fence already sits outside the state's 10-foot pond setback, the play area itself doesn't need to be measured against the water separately.</p>"
                     "<p>An architectural review submittal, if the village HOA requires one, typically moves faster for a play structure than for a more visible feature like a green, since a swing set behind a privacy fence usually isn't visible from the street either.</p>"),
        "faqs": [
            faq("Do Horizon West's newer trees ever trigger the drip-line rule for a play area?",
                "Occasionally, on the oldest sections built in the mid-2000s where street trees have had two decades to grow, but it's far less common than in an established town with mature oaks. Most Horizon West play-area layouts are governed by the pond setback instead."),
            faq("Does a Horizon West HOA require a specific playground turf color or product?",
                "Nothing published sets that requirement in the material we reviewed. What a committee typically asks for is a sample and a site plan showing the equipment and turf footprint relative to the fence and any setback, the same as for other exterior changes."),
        ],
        "sources": SRC,
    },
    "pool": {
        "title": "Pool & Lanai Turf in Horizon West, FL",
        "meta": "Pool-cage and lanai turf for Horizon West's compact new-build lots, with alley-loaded access and the stormwater-pond setback explained.",
        "h1": "Turf beside a Horizon West pool cage or lanai",
        "lede": capsule(f"Turf around a pool or inside a screen enclosure prices at the residential range, {price('residential')} per square foot as of September 2026. On a compact Horizon West lot, the strip between the pool cage and the property line, or a pond behind it, is often the entire yard rather than one section of it."),
        "sections": [
            ("A narrow strip is the whole job here",
             "<p>Where an older, wider Central Florida lot might have a broad lawn beside the pool cage, a newer Horizon West lot often leaves only a three- to six-foot strip between the screen and the fence, since the builder maximized the pool deck against a smaller overall footprint. That strip still needs the same glued, drainage-underlaid treatment as a larger pool-area job; there's simply less of it, which is the main reason a small Horizon West pool job can price near the top of the per-square-foot range even at a modest total cost.</p>"),
            ("Getting equipment past an alley-loaded garage",
             f"<p>On an alley-loaded lot, where the garage and driveway sit off the rear alley rather than the front street, reaching a pool-cage side yard sometimes means routing material through a narrower front gate instead of straight through the garage the way a conventional lot allows ({ext(SUBDIVISION_WAIVER[1], 'a 2020 county approval describing this Horizon West lot layout')}). That routing question is worth settling on the first site visit, since it changes how material gets staged more than it changes the turf itself.</p>"),
            ("When the lanai backs onto a stormwater pond",
             f"<p>A lanai or pool cage that backs onto one of Horizon West's stormwater ponds sits close enough to the water that {a(HB683_ROUTE[0], 'the state’s 10-foot setback')} often overlaps with the pool deck's own footprint. Where that's the case, turf runs from the cage to the setback line and stops there, leaving the final feet before the bank as mulch, rock or a low ground cover rather than turf, since the rule doesn't carve out an exception for a pool view.</p>"
             f"<p>A narrow pool-side strip against a pond shows up on lots toward {city('celebration')}, {city('winter-garden')} and {city('dr-phillips')} too, and {post('install-artificial-turf-over-concrete-pavers-or-grass', 'this guide to turf over an existing pool deck')} covers the glue-down details that carry over from lot to lot. {svc('pool', 'The pool and lanai turf page')} has the rest.</p>"),
        ],
        "scenario": ("Say you have a 300 sq ft strip between a Waterleigh pool cage and a pond",
                     f"<p>A 300 sq ft strip of turf between a screened pool cage and a stormwater pond on a Waterleigh lot, with roughly 60 sq ft of that falling inside the state's 10-foot setback, leaves about 240 sq ft to turf. At {price('residential')} per square foot, that runs roughly $1,920 to $4,320, glued at the deck edge with a drainage underlay and pinned along the outer, non-setback perimeter.</p>"
                     "<p>Because the strip is narrow, the crew's biggest time cost is precise cutting and seaming rather than base work, which is the opposite of a wide-open backyard job where the base is what takes the time.</p>"),
        "faqs": [
            faq("Does a small Horizon West lot cost more per square foot for pool turf?",
                "Sometimes, yes, since a crew and equipment mobilize for a job whether the strip is 100 sq ft or 1,000, and cutting turf tightly around a narrow pool-cage strip takes more labor per foot than an open lawn does."),
            faq("Can turf run all the way to a stormwater pond behind a Horizon West lanai?",
                "No, not without a seawall or similar barrier, which most Horizon West retention ponds don't have. The state's 10-foot setback applies the same way it would on a natural lake, leaving the last stretch before the bank outside the turfed area."),
        ],
        "sources": SRC,
    },
    "repair": {
        "title": "Turf Repair in Horizon West, FL",
        "meta": "Turf repair for Horizon West's pond-backed lots, from bank erosion near the setback line to seams strained by young, still-settling fill soil.",
        "h1": "Fixing turf on a Horizon West pond-backed lot",
        "lede": capsule("Turf repair is quoted after photos or a site visit, not by the square foot, since a lifted seam and a washed-out edge cost different amounts to fix. On a Horizon West lot, a stormwater pond at the back fence and fill that's still settling under a newer lawn are the two problems that come up most."),
        "sections": [
            ("When the setback line itself starts eroding",
             f"<p>A turf edge that sits right at {a(HB683_ROUTE[0], 'the state’s 10-foot pond setback')} takes more water stress than one set well back from any bank, since runoff crossing that buffer strip during a hard summer storm can undercut an improperly anchored edge over a season or two. A repair there usually means re-anchoring the affected section with fasteners spaced tighter than the original install, plus checking whether the buffer strip itself needs regrading so water sheets across it instead of channeling along the turf's edge.</p>"),
            ("Settling fill under a lawn that's only a few years old",
             f"<p>Pad fill brought in during construction keeps settling for a year or more after a Horizon West home is finished, more than native, undisturbed ground would, and a base built on top of it before that settling finished can develop a soft spot that opens a seam later even though the original installation was done correctly ({ext(NITTAW_OSD[1], 'background on the poorly drained native soil the fill typically sits above')}). Rebuilding just the settled section, rather than the whole lawn, is usually enough once the fill has finished moving.</p>"),
            ("Alley-loaded access complicates a repair visit, too",
             "<p>The same narrow side gates and rear-alley garages that slow down a first install also affect a repair call, since a plate compactor or a wheelbarrow load of replacement base still has to reach the same tight entry point. Scheduling a repair with that access noted up front, rather than discovering the gate width on arrival, keeps a same-day fix from turning into a return visit.</p>"
             f"<p>Settling fill and pond-edge wear both turn up on newer lots toward {city('windermere')}, {city('four-corners')} and {city('celebration')} as well, and {post('what-does-artificial-turf-warranty-cover', 'this article on what a workmanship warranty actually covers')} is worth reading before assuming a repair falls outside it. {svc('repair', 'Our repair service page')} explains how a visit gets priced.</p>"),
        ],
        "scenario": ("Say a 5 ft section pulls loose along a Waterleigh pond-setback line",
                     "<p>A 5 ft stretch of turf edge pulling loose along the pond-setback buffer on a Waterleigh lot, after a summer of heavy afternoon storms, usually means water crossing that strip found a low point in the original grading rather than a defect in the turf itself. Re-anchoring the edge with closer fastener spacing and correcting the grade of the buffer strip so runoff sheets across it evenly is a same-day fix in most cases.</p>"
                     "<p>If pulling the edge back reveals a soft, still-settling patch of fill underneath, the repair extends to rebuilding that section of base before the turf goes back down, which adds a day rather than an hour to the job.</p>"),
        "faqs": [
            faq("Why does turf near a Horizon West retention pond need more edge repairs than an inland lawn?",
                "Runoff crossing the state's mandatory buffer strip during a hard rain puts more stress on that section of turf than on an edge set well away from any water, especially if the original grading left a low spot. Checking that specific stretch after a heavy storm season catches a problem early."),
            faq("Does new-construction fill ever cause turf problems years after installation?",
                "Occasionally. Fill soil under a Horizon West lawn can keep settling for a year or more past the home's completion, and a base built before that settling finished can develop an uneven spot later. It's a base issue, not a defect in the turf, and it's fixed by rebuilding the affected section."),
        ],
        "sources": SRC,
    },
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
