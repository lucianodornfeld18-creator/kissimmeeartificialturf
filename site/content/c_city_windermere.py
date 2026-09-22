# -*- coding: utf-8 -*-
"""Windermere, FL: incorporated Town of Windermere plus the unincorporated 34786-mailing-address
gated communities (Isleworth, Keene's Pointe, Reserve at Lake Butler Sound and others) around the
Butler Chain of Lakes. Researched September 2026; see SRC for every local source."""
from _helpers import page, capsule, sec, table, faq, a, svc, city, post, src, ext, price
from _cityservice import cityservice_pages

SLUG = "windermere"

WIN_BUILDING = ("Town of Windermere — Building Department", "https://www.town.windermere.fl.us/page/building-department")
WIN_CANOPY = ("Town of Windermere — Canopy vs. Understory Trees", "https://www.town.windermere.fl.us/page/canopy-vs-understory-trees")
WIN_BUTLER = ("Town of Windermere — Butler Chain of Lakes", "https://www.town.windermere.fl.us/page/butler-chain-of-lakes")
WIN_WIKI = ("Wikipedia — Windermere, Florida", "https://en.wikipedia.org/wiki/Windermere,_Florida")
WIN_UTIL = ("Florida Neighborhood Realty — Windermere community contacts and utility providers", "https://www.floridaneighborhoodrealty.com/windermere-community-contacts/")
ORANGE_PA = ("Orange County Property Appraiser — parcel search", "https://ocpafl.org/")
OC_UTIL = ("Orange County Utilities — watering restrictions", "https://www.orangecountyfl.net/watergarbagerecycling/wateringrestrictions.aspx")
SFWMD_WHO = ("South Florida Water Management District — service area by county", "https://www.sfwmd.gov/who-we-are")
SFWMD_KISS = ("South Florida Water Management District — Upper Kissimmee Basin water supply plan", "https://www.sfwmd.gov/our-work/water-supply/upper-kissimmee")
BUTLER_ATLAS = ("Orange County Water Atlas — Butler Chain of Lakes", "https://orange.wateratlas.usf.edu/butler-chain/")
CANDLER_OSD = ("USDA NRCS — official series description, Candler series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/C/CANDLER.html")
PERMITS_ORANGE = ("/laws/permits/orange-county/", "Orange County turf permit rules")
HOA_ROUTE = ("/laws/hoa-rules/", "What a Florida HOA can and can't restrict")
HB683_ROUTE = ("/laws/florida-hb-683/", "HB 683 and DEP Rule 62-308.100")

SRC = [WIN_BUILDING, WIN_CANOPY, WIN_BUTLER, WIN_WIKI, WIN_UTIL, ORANGE_PA, OC_UTIL, SFWMD_WHO, SFWMD_KISS, BUTLER_ATLAS, CANDLER_OSD, "dep-rule", "fs125572", "fs7203045"]

HUB = page(
    "/areas/windermere/", "city",
    "Artificial Turf in Windermere, FL: Lakefront Yards (2026)",
    "Artificial grass installation for the Town of Windermere and its gated lake communities: permits, water rules and the Butler Chain setback. September 2026.",
    "Synthetic turf for Windermere's town lots and gated lake communities",
    capsule(f"We install, repair and clean synthetic lawns across the incorporated Town of Windermere and the gated communities that share its 34786 mailing address, where turf runs {price('residential')} per square foot installed as of September 2026. Windermere sits on a narrow isthmus between Lake Down and Lake Butler, so a shoreline setback or an existing seawall often decides where a yard's turf can start."),
    "".join([
        sec("A town hall and a county office, both with jurisdiction here",
            f"<p>The incorporated Town of Windermere runs its own Building Department for the roughly 3,000 residents inside its 1.9 square miles of land, reachable at 407-876-2563 from the town hall on Main Street ({ext(WIN_BUILDING[1], 'the town’s Building Department page')}). We haven't researched Windermere's own code section by section the way we have Orlando's or the county's, so treat that phone call as the starting point for anything inside town limits, not this paragraph.</p>"
            + f"<p>Most addresses that read \"Windermere, FL 34786,\" though, sit outside those town limits. Isleworth, Keene's Pointe, the Reserve at Lake Butler Sound, Casabella, Belmere and Summerport are unincorporated Orange County, so their permits run through Orange County Permitting Services at 407-836-5550, covered in full on {a(PERMITS_ORANGE[0], PERMITS_ORANGE[1])}. The town tried annexing Isleworth in 2007; the vote failed over county and resident objections, and the boundary drawn that year still splits the map today ({ext(WIN_WIKI[1], 'per the town’s recorded history')}). {src('fs125572', 'The state turf standard')} applies the same way to a covered lot on either side of that line.</p>"),
        sec("Windermere yard types and what we do differently",
            table("Windermere yard types and what we do differently",
                  ["Yard type", "What's different", "What that changes about the job"],
                  [["In-town lake lot on Lake Down or Lake Butler", "Frontage sits inside the state's 10-ft waterbody setback", "We confirm a seawall already runs the property line before turf gets anywhere near the water"],
                   ["Golf-community lot (Isleworth, Keene's Pointe, Lake Butler Sound)", "An architectural committee reviews the yard, and a rear lawn often faces a fairway instead of a fence", f"An {a('/laws/hoa-rules/', 'ARC packet')} goes in before the crew does, with a sample and a site sketch"],
                   ["Older canopy lot near Main Street", "Live oaks planted decades ago reach well past the trunk", "A certified arborist's letter usually comes before excavation starts near the roots"],
                   ["Interior lot in Summerport, Casabella or Belmere", "No lake frontage and no separate town code to check", "Ordinary unincorporated Orange County review, without a shoreline setback to plan around"]],
                  "Every row still meets the same statewide material and drainage standard; what changes is who reviews the paperwork and what sits at the property line.")),
        sec("Water, the Butler Chain and what's under a Windermere lawn",
            f"<p>Water inside town limits comes from the Town of Windermere's own utility; step outside that boundary into Isleworth, Keene's Pointe, Summerport or the Reams Road corridor and Orange County Utilities takes over instead, on the county's seasonal odd/even schedule with no watering between 10 a.m. and 4 p.m. ({ext(WIN_UTIL[1], 'a rundown of who serves which Windermere-area address')}; {ext(OC_UTIL[1], 'Orange County’s current restrictions')}). Neither schedule reaches a synthetic yard once its heads are capped, which the state's May 19, 2026 standard already requires.</p>"
            + f"<p>The eleven interconnected lakes of the Butler Chain drain the opposite direction from most of west Orange County: instead of the St. Johns River system that serves Winter Garden and Ocoee, the chain empties south through the Cypress Creek Watershed toward Reedy Creek, the Kissimmee River and eventually Lake Okeechobee, which puts it in the South Florida Water Management District's service area rather than the district that covers the county's northern half ({ext(BUTLER_ATLAS[1], 'the Orange County Water Atlas’s Butler Chain page')}; {ext(SFWMD_WHO[1], 'SFWMD’s own list of the counties it partially covers')}). That drainage is also why the Butler Chain earned Florida's first Outstanding Florida Waters designation in 1985, a status that adds its own layer of review to any dock or seawall work near the shoreline. Inland from the water, the ground under an in-town or golf-community lot tends toward the same deep, excessively drained Candler-family sand common on Central Florida's lake ridges, not the flatter, wetter flatwoods soil under a Kissimmee or Hunters Creek yard ({ext(CANDLER_OSD[1], 'USDA’s official series description')}).</p>"),
        sec("Permits, ARC packets and the state's turf rule in Windermere",
            f"<p>Whichever office has your parcel, {a(HB683_ROUTE[0], HB683_ROUTE[1])} sets the same floor: turf permeable enough to drain, capped irrigation heads, a 10-foot buffer from the water unless a seawall already stands there, and a certified arborist's sign-off before digging inside a live oak's drip line. What the state rule doesn't touch is your association. Isleworth, Keene's Pointe and Lake Butler Sound each run an architectural review committee, and while none of the three publishes a synthetic-turf clause we could find and cite, {a(HOA_ROUTE[0], HOA_ROUTE[1])} still protects a backyard that isn't visible from the street or a neighboring lot even where the committee's own preference runs toward sod.</p>"
            + f"<p>Check which office actually has your parcel before assuming either way. The {ext(ORANGE_PA[1], ORANGE_PA[0])} shows the taxing jurisdiction for any Orange County address, and Windermere is about 16 miles from downtown Kissimmee by straight line, a distance that changes scheduling, not the price on the quote.</p>"),
        "<!--AUTO:city-services-->",
    ]),
    faqs=[
        faq("How do you find the best artificial turf installer near you in Windermere?",
            "Start with three questions: does the crew already know whether your address is inside town limits or unincorporated county, have they handled an ARC submittal for a gated community before, and will the base and infill be named in writing. An installer who asks about your lake frontage before quoting a price has done this kind of yard before."),
        faq("Does the Town of Windermere or Orange County handle my permit?",
            "It depends on the parcel, not the mailing address. Inside the town's own 1.9 square miles, the Building Department at 407-876-2563 has it; step into Isleworth, Keene's Pointe or most of the other 34786 communities and it's Orange County Permitting Services at 407-836-5550 instead. The property appraiser's site settles it either way."),
        faq("Does living on the Butler Chain add anything to the state's 10-foot setback?",
            "Nothing published sets a Windermere-specific number beyond the state's figure. What the chain's Outstanding Florida Waters status adds is a separate, stricter review for any dock, seawall or fill work at the shoreline itself, which is a different permit than the one that covers turf on the lawn above it."),
        faq("Do Isleworth or Keene's Pointe allow synthetic turf in a fairway-facing backyard?",
            "We found no published ARC document from either community that names synthetic turf one way or the other, so a submittal with a sample, a spec sheet and a site sketch is the way to find out. F.S. 720.3045 only protects turf that a neighbor or the street can't see, and a fairway view usually counts as visible."),
        faq("Is a Windermere lawn's base any different from one in Kissimmee?",
            "The build steps are identical: washed, open-graded crushed rock, compacted in two lifts, graded away from the house. What differs is the sand underneath it, since Windermere's lake-ridge terrain tends toward deep, fast-draining Candler-family soil rather than the flatter, wetter flatwoods common closer to Kissimmee."),
    ],
    sources=SRC, crumbs=[("Service areas", "/areas/")], crumb="Windermere", city=SLUG,
    related=[("/areas/orange-county/", "Artificial turf in Orange County"), PERMITS_ORANGE, ("/areas/dr-phillips/", "Turf in Dr. Phillips"), ("/areas/horizon-west/", "Turf in Horizon West"), ("/artificial-turf-cost/", "Turf cost tables for Central Florida")],
)

LOCAL = {
    "residential": {
        "title": "Artificial Grass Installation in Windermere, FL",
        "meta": "Residential turf installation for Windermere town lots and lakefront yards, priced per square foot, with the town-vs-county permit split explained. Sept. 2026.",
        "h1": "Synthetic lawns for Windermere's town and lakefront lots",
        "lede": capsule(f"A residential lawn conversion in Windermere runs {price('residential')} per square foot installed, typically {price('residential', True)}, as of September 2026. Whether that quote answers to the Town of Windermere's own Building Department or to Orange County Permitting Services depends on which side of the 2007 annexation line your parcel sits."),
        "sections": [
            ("Why the same street can answer to two different offices",
             f"<p>Windermere's town limits cover a small isthmus between Lake Down and Lake Butler, so a lawn conversion two doors apart can fall under different rules depending on a boundary most homeowners never think about. Inside town limits, the Building Department at 407-876-2563 has the file; step across into Isleworth, Casabella or most of the rest of the 34786 area and {svc('residential', 'the lawn swap')} answers to Orange County Permitting Services at 407-836-5550 instead, the office covered on {a('/laws/permits/orange-county/', 'our Orange County permit page')}.</p>"
             "<p>Neither office has published a synthetic-turf-specific answer as of September 2026, so a residential job in either jurisdiction meets the state's May 2026 standard as its only written turf rule, plus whatever ordinary landscape or drainage review the office already runs for exterior work.</p>"),
            ("The isthmus geometry changes where turf can go",
             "<p>A lot inside the incorporated town is rarely far from Lake Down, Lake Butler or Lake Bessie, since the town's entire 1.9 square miles of land sits wedged between them. That geography means the state's 10-foot waterbody setback comes up on a much larger share of in-town jobs than it would on a typical inland Central Florida lot, and a seawall, where one already exists, is usually the detail that decides whether turf can run right up to the property line.</p>"
             "<p>A lot on Summerport's or Casabella's interior streets, by contrast, rarely touches open water at all, so that particular rule stays out of the conversation entirely on most unincorporated 34786 addresses away from the chain.</p>"),
            ("A different sand than the Kissimmee side of the service area",
             f"<p>Deep sandy ridge soil, of the same Candler-family type documented on lakefront ground across Central Florida, drains far faster than the wetter flatwoods common closer to Kissimmee, which changes how much a crew leans on compaction versus drainage when building the base ({ext(CANDLER_OSD[1], 'USDA’s official series description')}). Fast-draining sand still needs the same washed, open-graded crushed rock the state rule requires; the difference shows up in how quickly that base packs firm rather than in how deep it needs to be.</p>"
             "<p>A slope toward the water, common on an older Windermere lakefront lot, gets graded so runoff still moves away from the house before it reaches turf near the shoreline setback.</p>"
             f"<p>The same lake-ridge-to-flatwoods contrast plays out moving toward {city('dr-phillips')}, {city('winter-garden')} and {city('gotha')}, three nearby stops each with their own soil quirks, and {post('base-under-artificial-turf-florida-sandy-soil', 'this article')} goes deeper on why sandy ground changes the base recipe. Our {city('windermere', 'Windermere turf overview')} rounds up the rest of the town's permit and water rules.</p>"),
        ],
        "scenario": ("Say you have a 950 sq ft in-town backyard near Lake Butler",
                     f"<p>A 950 sq ft backyard on an in-town Windermere lot, roughly a third of it inside the state's 10-foot lake setback because there's no seawall on that stretch, prices differently depending on which part gets turfed. The 650 sq ft outside the setback, a flat rectangle behind the pool cage, runs {price('residential')} per square foot, so about $5,200 to $11,700 at the published range. The remaining 300 sq ft nearest the water stays as it is, or gets a native ground cover instead, until a seawall or a different buffer plan changes the math.</p>"
                     "<p>Add an ARC submittal if the lot sits in a community that requires one, and factor the Building Department's ordinary exterior-work permitting into the timeline even though the town hasn't published a synthetic-turf-specific rule. The setback, not the square footage, is usually what a Windermere lakefront quote has to work around first.</p>"),
        "faqs": [
            faq("Do I need a permit to convert a lawn inside the Town of Windermere?",
                "The town hasn't published a yes-or-no answer for synthetic turf specifically, so call the Building Department at 407-876-2563 before scheduling a crew. Capping the irrigation heads under the new turf, required by the state standard either way, can trigger its own review regardless of what the town says about the turf itself."),
            faq("My lot backs onto Lake Down. How close can turf come to the water?",
                "Ten feet from the ordinary or mean high water line, under the state's May 2026 standard, unless a seawall or bulkhead already separates the yard from the lake. We haven't found a Windermere-specific number that goes further than that, so plan around the state figure until the town says otherwise."),
        ],
        "sources": SRC,
    },
    "pet": {
        "title": "Pet Turf & Dog Runs in Windermere, FL",
        "meta": "Pet-friendly synthetic turf for Windermere yards and gated-community dog runs, with split water utilities and odor-control infill explained. Sept. 2026.",
        "h1": "Dog runs and pet turf built for a Windermere yard",
        "lede": capsule(f"Pet turf in Windermere runs {price('pet')} per square foot installed, typically {price('pet', True)}, as of September 2026. Rinsing a dog run in the incorporated town draws on the Town of Windermere's own water utility, while most of the surrounding 34786 gated communities buy from Orange County Utilities instead."),
        "sections": [
            ("Two water bills, one rinsing routine",
             f"<p>A pet turf area never runs on an in-ground system once its heads are capped, which the state standard requires regardless of which utility serves the address. Inside town limits, that utility is the Town of Windermere itself; in Isleworth, Keene's Pointe, Summerport and most of the rest of the 34786 mailing area, it's Orange County Utilities, running a seasonal odd/even schedule with no watering between 10 a.m. and 4 p.m. ({ext(WIN_UTIL[1], 'who actually bills which Windermere-area address')}; {ext(OC_UTIL[1], 'Orange County’s current restrictions')}). Whichever bill arrives, a hose is what keeps a dog run clean and cool from here on.</p>"
             "<p>That split matters more for a homeowner deciding on a rinse schedule than for the turf build itself, since the infill and drainage plan for a dog run stay the same on either side of the town line.</p>"),
            ("Fairway-facing runs in the golf communities",
             f"<p>A dog run in Isleworth, Keene's Pointe or Lake Butler Sound often sits closer to a fairway or a lake view than to a fence line, since those lots were platted around the golf course and the water rather than around a typical suburban backyard. That visibility is exactly what an architectural review committee weighs before approving a change, so a pet turf submittal there benefits from a tighter, more finished-looking edge, such as a paver border, than a purely functional side-yard run would need.</p>"
             f"<p>{a('/laws/hoa-rules/', 'Florida’s HOA-visibility statute')} still protects a run that's fenced and out of sight from the street or an adjacent lot, but a fairway view often removes that protection even where the fence itself is tall.</p>"),
            ("Keeping a run away from the lake setback",
             "<p>An in-town lot near Lake Down or Lake Butler that wants a dog run close to the water still answers to the state's 10-foot waterbody buffer the same way a plain lawn would, seawall exception included. Placing the run on the house side of that line, rather than fighting for the last few feet near the shoreline, is usually the simpler path, and it keeps the zeolite or coated-sand infill pet turf needs away from water it isn't supposed to reach anyway.</p>"
             f"<p>Pet owners near the water face a similar setback question in {city('dr-phillips')}, {city('horizon-west')} and {city('winter-garden')}, and {post('how-to-get-dog-urine-smell-out-of-artificial-turf', 'this guide to keeping pet infill fresh')} covers the odor-control side that matters on any of these yards. {svc('pet', 'Our full pet turf guide')} has the build spec that doesn't change from lot to lot.</p>"),
        ],
        "scenario": ("Say you have a 250 sq ft run behind a Keene's Pointe pool cage",
                     f"<p>A 250 sq ft dog run behind a screened pool cage in Keene's Pointe, tucked along a side yard rather than facing the fairway, runs {price('pet')} per square foot, or roughly $2,500 to $4,500 at the published range, with zeolite infill added for two dogs using the space daily. Because the run sits behind the screen and isn't visible from the golf course or the street, it's a stronger candidate for the HOA-visibility protection than a run facing open fairway would be.</p>"
                     "<p>An ARC submittal with the turf sample and a site sketch still goes in first if the community requires one for any exterior change, screened or not, and the irrigation head that used to water that strip gets capped at the valve box before the base goes down.</p>"),
        "faqs": [
            faq("Does Orange County Utilities' watering schedule affect a capped dog run?",
                "No. Once the irrigation heads under a pet turf area are capped, which the state standard requires, neither Orange County Utilities' schedule nor the Town of Windermere's own applies to that section of yard. A hose handles rinsing instead, on whatever routine keeps ammonia odor down."),
            faq("Do golf-community HOAs treat a pet run differently from a plain lawn?",
                "Not under any published rule we found. What changes in practice is visibility: a run facing a fairway or a lake gets more scrutiny from an architectural committee than a fenced run tucked out of sight, simply because more of the community can see it."),
        ],
        "sources": SRC,
    },
    "putting": {
        "title": "Backyard Putting Greens in Windermere, FL",
        "meta": "Putting green installation for Windermere's golf communities and in-town lots, with ARC review and contour options explained. Checked September 2026.",
        "h1": "Putting greens for Windermere's golf-community lots",
        "lede": capsule(f"A backyard putting green in Windermere runs {price('putting')} per square foot installed, typically {price('putting', True)}, as of September 2026. Isleworth, Keene's Pointe and the Reserve at Lake Butler Sound are built around golf courses, which makes a home green a natural fit, and also means an architectural committee reviews it first."),
        "sections": [
            ("Why a green fits a golf-community lot",
             "<p>Isleworth, Keene's Pointe and Lake Butler Sound were platted around golf courses from the start, so a homeowner already living beside a fairway is a more common candidate for a home putting green than someone on a standard suburban lot elsewhere in our service area. A contoured green with two or three cups and a chipping pad reads as an extension of the course view rather than an unusual addition, which is part of why the request comes up more often here than in a typical subdivision.</p>"
             "<p>That same fairway view is also what draws the closest architectural scrutiny, since a green sits in the most visible part of many of these lots.</p>"),
            ("What an ARC submittal for a green needs",
             f"<p>None of the three communities publishes a synthetic-turf clause we could find and cite, so a putting green submittal goes in as a general landscape or hardscape change: a site sketch showing the green's footprint and contours, a sample of the product, and a description of the fringe and cup placement. Because {a('/laws/hoa-rules/', 'Florida’s HOA statute')} protects a change only if it isn't visible from the street or an adjacent lot, and a fairway-facing green usually is visible from somewhere, the ARC review carries more weight here than the state's own turf standard does for this particular decision.</p>"),
            ("Base work on a lake-ridge lot",
             f"<p>The deep, fast-draining Candler-family sand common on Windermere's lake-ridge lots holds a shaped subbase well, since it doesn't stay saturated the way flatter flatwoods soil can after a summer storm ({ext(CANDLER_OSD[1], 'USDA’s official series description')}). Contouring a green into that sand still calls for the same washed, open-graded crushed rock as any other job, built up in shaped lifts rather than a flat pass, so a subtle rise-and-fall reads true when a ball rolls across it.</p>"
             f"<p>A shaped green built into ridge sand isn't unique to Windermere's golf communities; {city('dr-phillips')}, {city('winter-garden')} and {city('ocoee')} all carry lots worth the same look, and {post('backyard-putting-green-cost-florida', 'our cost breakdown for greens across Central Florida')} explains how contouring moves the price within the published range. {svc('putting', 'The putting green service page')} has more on cup and fringe options.</p>"),
        ],
        "scenario": ("Say you have an 800 sq ft green and fringe near a Keene's Pointe fairway",
                     f"<p>An 800 sq ft putting green with fringe, set back from a Keene's Pointe fairway line by the community's standard rear setback, runs {price('putting')} per square foot, or about $11,200 to $24,000 at the published range depending on contouring and cup count. A two-cup layout with modest breaks lands toward the lower half of that range; a three-cup green with a chipping pad and more elaborate shaping pushes toward the top.</p>"
                     "<p>An ARC application with the green's footprint and a turf sample goes in before the crew is scheduled, and the review typically takes longer than the install itself, since these committees weigh a fairway-facing feature more carefully than an interior side-yard change.</p>"),
        "faqs": [
            faq("Do Windermere's golf communities allow synthetic putting greens?",
                "We found no published ARC document from Isleworth, Keene's Pointe or Lake Butler Sound that names synthetic turf or putting greens specifically. A submittal with a sample and a site plan through the community's standard review process is how to find out for a given lot."),
            faq("How is the best backyard putting green near a Windermere fairway actually planned?",
                "Start with how the green will read next to the golf course itself: matching mow height and green speed to a natural look matters more here than in a yard with no course view at all. Beyond that, the same checklist applies everywhere: named base depth, product face weight, and cup placement in writing before work starts."),
        ],
        "sources": SRC,
    },
    "playground": {
        "title": "Playground Turf in Windermere, FL",
        "meta": "Cushioned playground turf for Windermere's oak-canopied lots, with the state's drip-line rule and shock-pad sizing explained. Checked September 2026.",
        "h1": "Playground turf under Windermere's oak canopy",
        "lede": capsule(f"Playground turf in Windermere runs {price('playground')} per square foot installed, typically {price('playground', True)}, as of September 2026. The town's older, tree-lined lots near Main Street put a play area inside a live oak's drip line more often than a newer subdivision would, which brings the state's arborist rule into the plan early."),
        "sections": [
            ("Why Windermere's canopy matters for a swing set",
             f"<p>The Town of Windermere publishes its own guide distinguishing canopy trees from understory planting ({ext(WIN_CANOPY[1], 'the town’s Canopy vs. Understory Trees page')}), which points to how seriously the town treats mature tree cover on its older, in-town lots. A live oak planted when a Main Street cottage went up decades ago has a canopy, and a root system, that reaches well past where a homeowner might guess, and a play structure or its surrounding turf can land inside that drip line without anyone measuring it first.</p>"
             "<p>Newer construction in the surrounding gated communities tends to carry younger trees with a smaller reach, so the drip-line question comes up less often there than on an established in-town lot.</p>"),
            ("Getting the arborist letter before the shovel",
             f"<p>{a(HB683_ROUTE[0], 'Florida’s May 2026 turf standard')} keeps synthetic grass out of a live oak's drip line, whether the canopy belongs to that lot or spills over from next door, unless a certified arborist signs off first. For a playground project specifically, that means marking where the canopy's branch tips actually end, not the trunk, before deciding where the shock pad and fall zone can go. Skipping that step risks stressing surface roots during excavation, on a tree that can take decades to replace.</p>"),
            ("Sizing the pad for the equipment, not the yard",
             "<p>A swing set or a play structure sets the shock-pad thickness a playground turf system needs, based on the equipment's fall height, not on how much space the yard has available. A small backyard swing set on a shaded in-town lot generally needs less pad depth than a taller structure with a slide platform, and getting that number from the equipment's own specification sheet is a better start than guessing from the size of the play area.</p>"
             f"<p>Shock-pad sizing doesn't change whether a lot sits here or closer to {city('gotha')}, {city('ocoee')} or {city('dr-phillips')}, and {post('is-artificial-turf-safe-for-kids-pfas-lead', 'this article on turf safety for kids')} covers the material rules the state standard also governs. {svc('playground', 'Our playground turf page')} explains pad thickness by equipment type in more detail.</p>"),
        ],
        "scenario": ("Say you have a 300 sq ft play area near a mature live oak",
                     f"<p>A 300 sq ft play area for a swing set, planned six feet clear of a mature live oak's canopy edge on an older in-town Windermere lot, runs {price('playground')} per square foot, or about $3,000 to $7,500 at the published range depending on shock-pad thickness for the equipment's fall height. Because the canopy reaches further than the trunk suggests, the actual buildable footprint sometimes comes in smaller than the homeowner first measured from the base of the tree.</p>"
                     "<p>If the canopy's drip line does cross the planned area, a certified arborist's letter comes before excavation starts, adding time to the schedule that a treeless lot elsewhere in the county wouldn't need.</p>"),
        "faqs": [
            faq("Does Windermere's tree page set a specific drip-line distance for play areas?",
                "The town's Canopy vs. Understory Trees page distinguishes tree types but we didn't find a specific numeric setback for synthetic turf published there. The state's May 2026 rule is the number to plan around: no turf inside the drip line without a certified arborist's sign-off."),
            faq("Is playground turf safe to install under a live oak's shade?",
                "Shade is an advantage for a play area, since it keeps the surface cooler on a summer afternoon than a full-sun installation would. The concern the state rule addresses is root damage during construction, not the finished turf sitting under the canopy."),
        ],
        "sources": SRC,
    },
    "pool": {
        "title": "Pool & Lanai Turf in Windermere, FL",
        "meta": "Pool-cage and lanai turf for Windermere's lakefront and golf-community homes, with the Butler Chain's 10-foot setback explained. Checked September 2026.",
        "h1": "Turf beside a Windermere pool cage or lanai",
        "lede": capsule(f"Turf around a pool or inside a screen enclosure prices at the residential range, {price('residential')} per square foot as of September 2026. On a Windermere lakefront lot, the pool deck and the state's 10-foot waterbody setback frequently sit close enough together that both get measured on the same visit."),
        "sections": [
            ("When the pool cage meets the lake setback",
             f"<p>A screened pool on an in-town lake lot, or on a golf-community lot backing up to one of the Butler Chain's connecting canals, sometimes leaves only a narrow strip of ground between the cage and the water. That strip is exactly where {a(HB683_ROUTE[0], 'the state’s 10-foot waterbody buffer')} applies, seawall exception included, so measuring the pool deck and the shoreline distance on the same visit avoids planning turf for a strip that isn't available to use.</p>"
             "<p>Where a seawall already runs the property line, which is common on older in-town lake lots, the setback doesn't apply, and turf can run to the wall itself.</p>"),
            ("Turf inside the screen, glued rather than pinned",
             "<p>Turf laid over a pool deck's existing concrete or pavers inside a screen enclosure gets glued down at the edges rather than staked, since there's no soil underneath to anchor a perimeter nail into. A drainage underlay goes between the concrete and the turf backing so water from a rinse or a storm has somewhere to go besides sitting on the slab, which matters more in a screened, lower-airflow space than it would in an open yard.</p>"),
            ("Low-E glass around a lake-view lanai",
             "<p>A lanai or pool cage with large low-emissivity windows facing it, common on newer lakefront construction that maximizes the water view, can reflect enough concentrated sun to soften a synthetic lawn several feet away, since the material starts to give in the 175 to 200°F range under that kind of focused heat. Checking which windows face the turf before installation is a cheaper step than repairing a scorched patch after the fact.</p>"
             f"<p>Low-emissivity glass near a pool cage isn't unique to this town either; it turns up on lake-view lots toward {city('winter-garden')}, {city('horizon-west')} and {city('pine-hills')} just as often, and {post('can-artificial-turf-melt', 'this piece on turf and reflected heat')} explains the mechanics behind it. {svc('pool', 'The pool and lanai turf page')} covers the glue-down build in full.</p>"),
        ],
        "scenario": ("Say you have a 400 sq ft strip between a Windermere pool cage and Lake Down",
                     f"<p>A 400 sq ft strip of turf between a screened pool cage and a Lake Down shoreline, with an existing seawall running the property line, prices at {price('residential')} per square foot, or about $3,200 to $7,200 at the published range, glued at the deck edge and pinned along the outer perimeter. Because the seawall already separates the yard from open water, the state's 10-foot setback doesn't reduce the usable strip the way it would on an unwalled shoreline.</p>"
                     "<p>Without a seawall, the same 400 sq ft strip would need roughly the first 10 feet from the water's edge left as-is, cutting the turfed area down before the per-square-foot math even starts.</p>"),
        "faqs": [
            faq("Can turf go all the way to the water on a Windermere lake lot?",
                "Only if a seawall or bulkhead already separates the yard from the lake. Without one, the state's May 2026 standard keeps synthetic turf at least 10 feet from the ordinary or mean high water line, the same rule that applies to any Florida waterfront lot."),
            faq("Does turf inside a screened lanai still need a drainage layer?",
                "Yes, when it's going over existing concrete or pavers. A screen keeps rain out but not entirely, and any rinse water needs somewhere to go besides sitting on the slab, so a drainage underlay under the turf backing is standard for that setup."),
        ],
        "sources": SRC,
    },
    "repair": {
        "title": "Turf Repair in Windermere, FL",
        "meta": "Turf repair for Windermere's lake-ridge lots, from storm-lifted edges near the Butler Chain to seams opened by fast-draining Candler sand. September 2026.",
        "h1": "Fixing turf on a Windermere lake-ridge lot",
        "lede": capsule("Turf repair is quoted after photos or a site visit, not by the square foot, since a lifted seam and a scorched patch cost different amounts to fix. On a Windermere lot, storm exposure off the open water and a fast-draining ridge sand are the two problems that show up most often."),
        "sections": [
            ("Wind off the Butler Chain and lifted edges",
             f"<p>A lakefront lot with an open view down the Butler Chain gets more direct wind during a tropical storm than an inland yard shielded by neighboring houses, and that wind is what tests whether a turf edge was anchored the way {a(HB683_ROUTE[0], 'the state’s standard')} requires. A corner that peels back after a storm usually traces to a perimeter that was stapled rather than properly fastened or bordered, and the fix is a re-anchor of that section, not a full replacement.</p>"
             "<p>Checking the perimeter after any named storm, while the lifted section is still small, keeps a repair quick rather than letting water and traffic work the gap wider.</p>"),
            ("What fast-draining sand does to a seam over time",
             f"<p>Deep, excessively drained Candler-family sand, common under Windermere's lake-ridge lots, shifts more under a base than the wetter, denser flatwoods soil closer to Kissimmee does ({ext(CANDLER_OSD[1], 'USDA’s official series description')}). A base that wasn't compacted in two full lifts on that kind of ground can settle unevenly a season or two later, opening a seam at the low point even though the turf itself is undamaged. Rebuilding just that section of base, rather than replacing the whole lawn, usually solves it.</p>"),
            ("Low-E glass damage near lake-view homes",
             "<p>Large lake-facing windows, common on newer Windermere construction built to maximize the view, can concentrate enough reflected sun to melt a patch of turf several feet from the glass, since the material softens well below the temperature a summer afternoon alone would produce. A scorched patch that doesn't match any obvious cause is worth checking against which windows face that section of yard before assuming a manufacturing defect.</p>"
             f"<p>Storm-driven edge repairs and reflected-heat damage both turn up on lake lots toward {city('dr-phillips')}, {city('gotha')} and {city('ocoee')} as well, and {post('artificial-turf-hurricane-flooding', 'this guide to turf after a storm or flood')} covers what to check first anywhere in the service area. {svc('repair', 'Our repair service page')} has more on how a visit gets priced.</p>"),
        ],
        "scenario": ("Say a storm lifts a 6 ft seam behind a Keene's Pointe fairway lot",
                     "<p>A 6 ft section of seam lifted after a tropical storm on a Keene's Pointe lot facing open fairway and lake view usually means the original bond skinned before it fully cured, or the perimeter fastener spacing was too wide for that much wind exposure. Re-bonding that seam and adding fasteners at tighter spacing along the affected edge is a same-day fix in most cases, priced by the visit rather than the square foot.</p>"
                     "<p>If the lifted section also shows a soft, uneven base underneath once the turf is pulled back, that's the ridge sand settling rather than the seam itself failing, and the repair extends to rebuilding that stretch of base before the turf goes back down.</p>"),
        "faqs": [
            faq("Why does turf near the Butler Chain seem to need more edge repairs than an inland yard?",
                "Open water means less wind shielding during a storm, which puts more stress on a turf perimeter than a fenced, tree-sheltered inland yard usually sees. The fix is the same everywhere; lakefront lots just need the perimeter checked more often after a named storm."),
            faq("Does Windermere's sandy soil make turf repairs more frequent?",
                "Not more frequent overall, but a base built at the shallow end of the state's compaction range can settle sooner on fast-draining ridge sand than on denser flatwoods soil. A repair on that kind of settling usually means rebuilding a short stretch of base, not replacing the turf."),
        ],
        "sources": SRC,
    },
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
