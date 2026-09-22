# -*- coding: utf-8 -*-
"""Tier 2 city module: Apopka, FL. Incorporated city with its own Building Safety Division and its own
water utility. Facts checked September 2026; see docs/TIER2-BRIEF.md for the research assignment."""
from _helpers import page, capsule, sec, table, faq, a, svc, city, county, post, src, ext, price, note
from _cityservice import cityservice_pages

SLUG = "apopka"

APOPKA_BUILDING = ("City of Apopka -- Building Safety Division", "https://www.apopka.gov/222/Building-Safety-Division")
APOPKA_IRRIGATION = ("City of Apopka -- Landscape Irrigation Schedule", "https://www.apopka.gov/395/Landscape-Irrigation-Schedule")
APOPKA_RECLAIMED = ("City of Apopka -- Wastewater and Reclaimed Water", "https://www.apopka.gov/722/Wastewater-and-Reclaimed-Water")
DEP_WEKIVA = ("Florida DEP -- Wekiva Study Area", "https://floridadep.gov/water/onsite-sewage/content/wekiva-study-area")
WEKIVA_ACT = ("Orange County Water Atlas -- Ordinance Brief: The Wekiva Parkway and Protection Act", "https://orange.wateratlas.usf.edu/upload/documents/OrdinanceWekivaParkwayProtectionAct.pdf")
FOLIAGE_HIST = ("Islands -- Apopka, the Indoor Foliage Capital of the World", "https://www.islands.com/1930726/apopka-florida-under-radar-city-outside-orlando-indoor-foliage-capital-world/")
APOPKA_WIKI = ("Wikipedia -- Apopka, Florida", "https://en.wikipedia.org/wiki/Apopka,_Florida")
RSR_HOA = ("The Apopka Chief -- Rock Springs Ridge HOA acquires defunct golf course for $7.3M", "https://theapopkachief.com/rock-springs-ridge-hoa-acquires-defunct-golf-course-for-7-3m/")
ERROL_SALE = ("The Apopka Chief -- LLC tied to billionaire buys Errol Estate former golf course", "https://theapopkachief.com/llc-tied-to-billionaire-buys-errol-estate-former-golf-course/")
LAKE_APOPKA = ("St. Johns River Water Management District -- Lake Apopka North Shore", "https://www.sjrwmd.com/lands/recreation/lake-apopka/")
WEKIWA_PARK = ("Wikipedia -- Wekiwa Springs State Park", "https://en.wikipedia.org/wiki/Wekiwa_Springs_State_Park")
APOPKA_OSD = ("USDA NRCS -- official series description, Apopka series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/A/APOPKA.html")
CANDLER_OSD = ("USDA NRCS -- official series description, Candler series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/C/CANDLER.html")
ASTATULA_OSD = ("USDA NRCS -- official series description, Astatula series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/A/ASTATULA.html")
ORANGE_PA = ("Orange County Property Appraiser -- parcel search", "https://ocpafl.org/")

SRC = [APOPKA_BUILDING, APOPKA_IRRIGATION, APOPKA_RECLAIMED, DEP_WEKIVA, WEKIVA_ACT, FOLIAGE_HIST, APOPKA_WIKI,
       RSR_HOA, ERROL_SALE, LAKE_APOPKA, WEKIWA_PARK, APOPKA_OSD, CANDLER_OSD, ASTATULA_OSD, ORANGE_PA,
       "dep-rule", "fs125572", "fs7203045"]

PERMIT_ORANGE = ("/laws/permits/orange-county/", "Orange County permit rules for turf")
HOA_ROUTE = ("/laws/hoa-rules/", "What a Florida HOA can and can't restrict")
HB683_ROUTE = ("/laws/florida-hb-683/", "HB 683 and DEP Rule 62-308.100")


# ============================================================== hub
HUB = page(
    "/areas/apopka/", "city",
    "Artificial Turf Installation in Apopka, FL",
    "Synthetic grass installation in Apopka, Florida: permits, the city's own water rules, golf-community lots and ridge soil, checked September 2026.",
    "Turf work across Apopka, from ridge lots to Lake Apopka's shore",
    capsule(f"We install and repair artificial grass across Apopka, Florida, where a residential lawn runs {price('residential')} per square foot as of September 2026. Apopka runs its own water utility rather than Toho's or Orange County's, and its reclaimed-water customers keep a two-day watering schedule year-round. About 29 miles from downtown Kissimmee, Apopka sits at the edge of our Central Florida service area."),
    "".join([
        sec("An Apopka yard sits somewhere between a ridge and a lake",
            f"<p>Apopka grew from 41,542 residents at the 2010 census to 54,873 in 2020, a 32 percent jump in one decade, and the city's own estimate put it near 65,000 by the middle of this decade ({ext(APOPKA_WIKI[1], 'Census figures summarized by Wikipedia')}). Some of that growth sits on ground that used to grow something else entirely: a fern industry that took root here in the 1920s expanded into more than 400 acres of shade-house nurseries within a few decades, and Apopka carried the nickname Indoor Foliage Capital of the World by the mid-1960s ({ext(FOLIAGE_HIST[1], 'the city’s foliage history')}). A share of that acreage is subdivisions now rather than greenhouses.</p>"
            + f"<p>The terrain splits the city. West and north of downtown, the ground rises onto the same sandy ridge system that continues into Lake and Polk counties. East and south, lots run down toward Lake Apopka, Florida's fourth-largest lake at roughly 30,800 acres and the subject of a four-decade restoration effort by the water district ({ext(LAKE_APOPKA[1], 'SJRWMD’s Lake Apopka restoration page')}). A single {a('/artificial-grass-installation/', 'lawn conversion')} can answer to either soil type depending on which side of town it falls on.</p>"),
        sec("Who reviews a permit here, since Apopka runs its own code office",
            f"<p>Apopka is incorporated and keeps its own Building Safety Division, reached at 407-703-1713 out of City Hall at 120 East Main Street, with applications filed through the city's OpenGov permitting portal rather than the EnerGov system a few neighboring offices use ({ext(APOPKA_BUILDING[1], 'Apopka’s Building Safety Division')}). We don't have a page written for Apopka's own code the way we do for the county's, and a search of the city's ordinances turns up nothing that names synthetic turf directly, so a homeowner inside city limits should call the Building Safety Division before scheduling a crew rather than assume the answer either way.</p>"
            + f"<p>A lot just outside the city line answers to a different office entirely. {a(PERMIT_ORANGE[0], 'Our Orange County permit page')} covers the unincorporated pockets that still carry an Apopka mailing address, and the {ext(ORANGE_PA[1], ORANGE_PA[0])} settles which office actually has a specific parcel. Either way, {src('dep-rule', "the state's turf standard")} sets the same material and setback floor no matter which office stamps the permit.</p>"),
        sec("Apopka yard types and what changes for turf",
            "<p>The table below is the short version; the six city-times-service pages linked from this one go deeper on each.</p>"
            + table("Apopka yard types and what changes for turf",
                    ["Yard type", "What's typical", "What changes for the turf job"],
                    [["Golf-community lot (Rock Springs Ridge, Errol Estate)", "Larger lot, often backing a fairway or a closed course", "More open square footage to plan around; check the community's own ARC process before ordering material"],
                     ["Lake Apopka shoreline or canal lot", "Backs directly onto the lake or a connecting waterway", "The state's 10-foot waterbody setback applies unless a seawall already separates yard from water"],
                     ["West-side ridge subdivision", "Newer construction on Candler- or Apopka-series sand", "Fast-draining native soil still needs a washed-rock base; the sand alone won't hold a level surface"],
                     ["Older in-town lot on septic", "Built before city sewer reached that block", "The base plan leaves the tank's pump-out lid exposed, not buried under compacted rock"],
                     ["Former nursery ground", "Mature shade trees left over from decades of shade-house growing", "The drip-line rule applies to established canopy unless a certified arborist signs off"]],
                    "Checked against the city's published record and the sources listed below, September 2026.")),
        sec("Water in Apopka: a city utility, reclaimed lines and the Wekiva basin behind it",
            f"<p>Apopka runs its own water utility rather than buying through Toho or Orange County Utilities. Its {ext(APOPKA_IRRIGATION[1], 'landscape irrigation schedule')} assigns two watering days during daylight saving time, odd addresses Wednesday and Saturday and even addresses Thursday and Sunday, tightening to one day each during the winter months. A reclaimed-water line reaches a meaningful share of Apopka neighborhoods and runs on that same two-day schedule year-round ({ext(APOPKA_RECLAIMED[1], 'the city’s reclaimed-water program')}), but {src('dep-rule', 'the state standard')} bars watering synthetic turf from either supply, potable or reclaimed, once the heads underneath it are capped, so a reclaimed hookup at the curb doesn't change how the lawn itself gets built.</p>"
            + f"<p>Most of Apopka sits in the St. Johns River Water Management District, inside what the state designates the Wekiva Study Area. The Wekiva Parkway and Protection Act layers extra stormwater and septic requirements onto new development here, including a nitrogen-reducing upgrade standard for septic systems on lots under an acre within the basin's priority focus area ({ext(WEKIVA_ACT[1], 'the Wekiva Parkway and Protection Act summary')}; {ext(DEP_WEKIVA[1], 'Florida DEP’s Wekiva Study Area page')}). None of that changes how a turf lawn is built, but it's why a drainage or septic question on an Apopka lot tends to get closer scrutiny than the same question two towns over.</p>"),
        sec("HOAs, golf communities and the Florida law that limits both",
            f"<p>Two of Apopka's better-known subdivisions were built around a golf course, and both have spent the last few years figuring out what comes after golf. Rock Springs Ridge's 1,320 homes went without a working course for roughly a decade after it closed in 2014, until the community's own homeowners association agreed to a $7.3 million lease-purchase in 2026 to bring the land back under its control ({ext(RSR_HOA[1], 'coverage of the Rock Springs Ridge purchase')}). Errol Estate's course closed and its clubhouse came down in 2021, and the land changed hands again in 2025 under a development-linked buyer rather than the neighborhood itself ({ext(ERROL_SALE[1], 'coverage of the Errol Estate sale')}).</p>"
            + f"<p>Neither community has a published rule about synthetic turf that we could find, so an ARC submittal in either one runs on the same {a(HOA_ROUTE[0], 'visibility standard every Florida HOA answers to')}: a fenced backyard is protected from an outright ban, a front yard generally is not. {a(HB683_ROUTE[0], 'The state’s May 2026 turf standard')} sets the material and setback floor underneath whatever the ARC ultimately decides.</p>"),
        "<!--AUTO:city-services-->",
    ]),
    faqs=[
        faq("What should you ask before hiring the best turf installer in Apopka?",
            "Ask whether the crew already knows Apopka runs its own water utility rather than Toho's, whether the base plan changes between the ridge sand on the west side and the flatter ground near Lake Apopka, and whether the quote lists base depth, product face weight and infill by name. A written answer to all three is worth more than a sales pitch."),
        faq("Does the Wekiva Study Area add a rule for synthetic turf specifically?",
            "Not by itself. The Wekiva Parkway and Protection Act adds stormwater standards and, on older septic lots under an acre, a nitrogen-reducing upgrade requirement for new development in the basin, but neither names synthetic turf. Florida's May 2026 turf rule, not the Wekiva Act, sets the material and setback standard for a lawn conversion here."),
        faq("Is Rock Springs Ridge's golf course open again?",
            "Not as of September 2026. The homeowners association agreed to buy the closed course back that year after roughly a decade without one, financed through a dues increase, with reopening plans still ahead of it. Errol Estate's former course took a different path, selling in 2025 to a development-linked buyer rather than to its own community."),
        faq("Does a lot on Lake Apopka get a different setback than one on a small pond?",
            "No. The state's 10-foot setback from the ordinary or mean high water line applies the same way whether the water is Florida's fourth-largest lake or a small retention pond, unless a seawall or bulkhead already separates the yard from the water."),
        faq("I have a reclaimed-water hookup. Can I run it to new turf?",
            "No. Florida's turf standard bars watering synthetic turf from any in-ground system, potable or reclaimed, once the heads under it are capped, so a reclaimed line at the curb doesn't change how the lawn gets built. A hose handles rinsing afterward instead."),
    ],
    sources=SRC, city=SLUG, crumbs=[("Service areas", "/areas/")], crumb="Apopka",
    related=[("/areas/orange-county/", "Artificial turf in Orange County"), PERMIT_ORANGE, ("/areas/ocoee/", "Turf in Ocoee"), ("/areas/winter-garden/", "Turf in Winter Garden"), ("/artificial-turf-cost/", "Full turf cost guide")],
)


# ============================================================== local service content
LOCAL = {
    "residential": {
        "title": "Artificial Grass Installation in Apopka's Ridge Neighborhoods",
        "meta": "Synthetic lawn installation in Apopka, Florida, built for Candler- and Apopka-series ridge sand, from " + price("residential") + " per sq ft as of September 2026.",
        "h1": "Turf for Apopka's sandy ridge lots",
        "lede": capsule(f"A residential lawn conversion in Apopka runs {price('residential')} per square foot as of September 2026, whether the lot sits on the sandy ridge west of downtown or the flatter ground closer to Lake Apopka. The Apopka soil series, a well-drained upland sand, is actually named for this city, which says something about what a base has to handle here."),
        "sections": [
            ("Building on ground the USDA named after this city",
             f"<p>The Apopka series, official series description on file with the USDA, consists of very deep, well-drained soils with moderately slow permeability on upland ridges, side slopes and knolls ({ext(APOPKA_OSD[1], 'USDA’s official series description')}). Drive further west toward Rock Springs Ridge and the ground shifts to Candler and Astatula, both excessively drained and rapidly permeable sand that barely holds water at all ({ext(CANDLER_OSD[1], 'the Candler series description')}; {ext(ASTATULA_OSD[1], 'the Astatula series description')}). Neither soil holds a flat surface on its own.</p>"
             + f"<p>That's why the base under an Apopka lawn is washed, open-graded crushed rock or crushed concrete, not the native sand, compacted in two lifts regardless of which side of the ridge line a lot sits on. {post('base-under-artificial-turf-florida-sandy-soil', 'This article')} goes through why that specific mix matters more here than the brand of turf on top of it.</p>"),
            ("A city adding rooftops faster than it's replacing nursery ground",
             "<p>Apopka's population climbed 32 percent between the 2010 and 2020 census counts, and growth since has kept pace, which shows up on the ground as new-construction subdivisions built over what used to be shade-house nursery land. A yard on recently graded fill drains differently than an established one nearby: compacted construction fill packs tighter than undisturbed native sand, so water that should pass through the base instead rides on top of it after a summer storm.</p>"
             + f"<p>An older section of the city, closer to downtown or south toward {city('winter-garden', 'Winter Garden')}, is more likely to sit on undisturbed ridge sand under a mature yard, which drains faster but needs the same washed-rock base to stay level under foot traffic over a decade.</p>"),
            ("What Apopka's Building Safety Division actually reviews",
             f"<p>Apopka's own Land Development Code doesn't name synthetic turf, so a straightforward lawn conversion inside city limits isn't running into a written turf rule either way; it's running into the city's ordinary permitting for exterior work and irrigation. The {a('/laws/permits/orange-county/', 'unincorporated Orange County office')} handles the pockets just outside the line that still carry an Apopka address, which is worth checking on a lot near the edge of town.</p>"
             + f"<p>{city('apopka', 'Our Apopka hub page')} lists the Building Safety Division's phone and portal for a specific question. One item on the checklist doesn't wait on that answer either way: the state's material rule forces every in-ground sprinkler head under the new lawn to be capped at the valve, a plumbing detail worth scheduling into the same visit instead of treating as an afterthought once the turf is already down.</p>"),
        ],
        "scenario": ("Say you have a 1,100 sq ft ridge-lot backyard",
                     f"<p>Say you have a 1,100 sq ft backyard on a west-Apopka lot built on Candler sand, with a straightforward rectangle and a gate wide enough for equipment. At the published {price('residential')} range, that lawn prices between $8,800 and $19,800, and a straightforward yard like this one usually lands closer to the {price('residential', True)} typical band, or roughly $11,000 to $17,600. The fast-draining ridge sand doesn't change the base recipe: two to four inches of washed crushed rock still goes down and gets compacted in two passes, since the point of the base is holding a level surface, not fighting a high water table the way a flatwoods lot would.</p>"
                     + "<p>If the same yard backs onto a retained portion of an old grove line with a mature oak at the corner, the crew stakes the drip line before ordering material, since that's the boundary the state's rule protects unless an arborist signs off, and it can trim a modest amount of square footage off the quote.</p>"),
        "faqs": [
            faq("Does Apopka's ridge soil mean a cheaper base?",
                "No. Fast-draining sand keeps water from pooling, but it doesn't hold a flat, stable surface by itself, which is the base's real job. A ridge lot still gets the full two to four inches of washed crushed rock, the same as a flatwoods lot near Lake Apopka."),
            faq("Is a new-construction lawn in Apopka different from an older one?",
                "Often, yes, and not in the new lot's favor. Compacted fill left behind by a builder can drain worse than the undisturbed native sand under an older Apopka yard, since the compaction process itself packs out the pore space that let water pass through."),
        ],
        "sources": SRC,
    },
    "pet": {
        "title": "Pet Turf and Dog Runs for Apopka Yards",
        "meta": "Fast-draining pet turf for Apopka dog runs, priced " + price("pet") + " per sq ft as of September 2026, with notes on septic lots and reclaimed water.",
        "h1": "Turf built for dogs on an Apopka lot",
        "lede": capsule(f"A dog run built in pet turf costs Apopka homeowners {price('pet')} a square foot, current as of September 2026, and most jobs finish out around {price('pet', True)} once odor-control infill is added. In the city's older, in-town sections, where a meaningful share of lots still run on septic, that drainage plan has to work around the tank instead of through it."),
        "sections": [
            ("Dog runs on a golf-community lot",
             f"<p>Rock Springs Ridge and other Apopka subdivisions built around a golf course tend to carry larger backyards than a standard subdivision lot, since the original layout left room next to a fairway or a common area. That extra width is useful for a dog run specifically: a longer, narrower turf strip along a side fence gives a dog room to move without turning the whole backyard into a bathroom.</p>"
             + f"<p>{city('altamonte-springs', 'Altamonte Springs')} and other older Seminole County communities show the same pattern on a smaller scale, but Apopka's golf-community lots are usually the widest ones in our northwest Orange County service area.</p>"),
            ("Septic tanks and where a dog run's drainage can go",
             "<p>An Apopka lot built before city sewer reached that block still runs on a septic system, and the state's turf standard requires the tank's pump-out lid stay reachable once any part of the yard, dog run included, is finished. That matters more for a dog run than a plain lawn, since a run often gets built with a slight extra pitch toward one corner for rinse water to drain, and that corner can't be the one sitting over the drain field or the lid itself.</p>"
             + "<p>Mapping the septic system's layout before staking a dog run's footprint is a five-minute step that avoids redesigning the run later.</p>"),
            ("What Apopka's reclaimed water does and doesn't change for a pet yard",
             f"<p>A reclaimed-water hookup, common in a meaningful share of Apopka neighborhoods, keeps the rest of the lawn green without pulling from the potable system, but it has no bearing on a turf dog run once it's installed: {src('dep-rule', "the state's rule")} bars using either potable or reclaimed irrigation on synthetic turf, so the run gets rinsed by hose the same way it would on a lot with no reclaimed line at all. What reclaimed water does change is the price of keeping natural grass around the run's edges, which is one more reason some Apopka owners turf the whole backyard instead of just the run.</p>"),
        ],
        "scenario": ("Say you have a 320 sq ft side-yard dog run",
                     f"<p>Say you have a 320 sq ft dog run along a side fence on an older, in-town Apopka lot that's still on septic. At {price('pet')} per square foot, that run prices between $3,200 and $5,760, with most jobs like it landing in the {price('pet', True)} typical band, or $3,840 to $5,120. Zeolite or a coated antimicrobial sand goes in as infill instead of plain silica, since odor control matters more on a run than a lawn a family only walks across.</p>"
                     + "<p>Because the lot is on septic, the crew maps the tank and drain field before staking the run, keeping the pump-out lid clear and pitching drainage away from the field rather than toward it, which doesn't change the price but does change where the run's corners land.</p>"),
        "faqs": [
            faq("Should a weed barrier go under an Apopka dog run?",
                "No, skip it under a pet area specifically. A layer of fabric between the base and the backing holds waste right where it lands instead of letting it pass down into the rock, working against the fast drainage a dog run needs most. The same fabric is fine, and optional, under a plain lawn elsewhere on the property."),
            faq("Does a golf-community HOA in Apopka review a dog run differently than a full lawn?",
                "Not usually as a separate category. Rock Springs Ridge and similar communities review an ARC submittal on visibility from the street or an adjacent lot, the same standard Florida law sets for any synthetic turf project, whether it covers a dog run or the whole yard."),
        ],
        "sources": SRC,
    },
    "putting": {
        "title": "Backyard Putting Greens in Apopka, FL",
        "meta": "Contoured putting greens for Apopka backyards, priced " + price("putting") + " per sq ft as of September 2026, including golf-community lots.",
        "h1": "A private green for an Apopka backyard",
        "lede": capsule(f"Contouring and a cup or two put most Apopka putting greens in the {price('putting', True)} typical band, inside the wider {price('putting')}-a-square-foot range published for September 2026. With two of the city's own golf courses in flux, a private green lets a homeowner keep practicing no matter what happens to the shared course next door."),
        "sections": [
            ("Two closed courses and what that means for a private green",
             f"<p>Rock Springs Ridge's 39-hole course sat closed for roughly a decade before the community's homeowners association agreed to a $7.3 million buyback in 2026, and Errol Estate's course, demolished clubhouse and all in 2021, sold again in 2025 to a buyer with no announced plan to reopen it as golf ({ext(RSR_HOA[1], 'coverage of the Rock Springs Ridge purchase')}; {ext(ERROL_SALE[1], 'coverage of the Errol Estate sale')}). A homeowner in either community who wants somewhere to practice a short game doesn't have to wait on either outcome.</p>"
             + f"<p>A backyard {svc('putting', 'putting green')} sits entirely on private property and answers to the same ARC review as any other yard feature, not to whatever happens with the community's shared course.</p>"),
            ("Building a green on ridge sand instead of flatwoods soil",
             "<p>A putting green's base has less margin for error than a plain lawn, since an uneven subgrade shows up in every missed putt rather than just an occasional low spot. Apopka's ridge-sand lots, fast-draining and prone to shifting under a compactor if it's rushed, need extra attention to a stable, well-compacted foundation before contouring goes in, more so than a flatwoods lot where the sand itself holds together better under a plate compactor.</p>"
             + f"<p>{post('artificial-turf-glossary', 'This glossary')} covers stimp rating and the other spec terms worth asking about on a green-specific quote.</p>"),
            ("Sizing a green to fit a golf-community lot",
             f"<p>Rock Springs Ridge and Errol Estate lots tend to run wider than a standard Apopka subdivision parcel, which gives a green more room to include a real chipping pad alongside the putting surface itself rather than squeezing both into a cramped footprint. A lot near {city('ocoee', 'Ocoee')} or a newer, tighter subdivision elsewhere in the city usually calls for a smaller, single-purpose green instead.</p>"),
        ],
        "scenario": ("Say you have a 450 sq ft green with a chipping pad",
                     f"<p>Say you have a 450 sq ft putting green with an attached 150 sq ft chipping pad planned for a Rock Springs Ridge backyard, 600 sq ft total. At the published {price('putting')} range, that project prices between $8,400 and $18,000, with most jobs like it landing in the {price('putting', True)} typical band, or $10,800 to $15,000. Two cups and moderate contouring sit inside that range; a third cup or a false-front slope pushes it toward the upper end.</p>"
                     + "<p>Because the lot sits on fast-draining ridge sand, the crew spends extra time compacting the subgrade in thin lifts before shaping the contours, since a green built too quickly on this soil can settle unevenly within its first year.</p>"),
        "faqs": [
            faq("Will Rock Springs Ridge's golf course reopening change what I can put in my own backyard?",
                "No. A private putting green sits entirely on the homeowner's lot and goes through the community's ordinary ARC process, unrelated to whatever the HOA decides about the shared course it now owns."),
            faq("Does a putting green need a deeper base than a regular Apopka lawn?",
                "The depth range is the same, two to four inches of washed crushed rock, but a green needs tighter compaction control and shaping since even a small dip changes how a ball rolls, unlike a lawn where a minor low spot just looks slightly different."),
            faq("Can a green go in near one of Apopka's remaining live oaks?",
                "Only outside the tree's drip line unless a certified arborist signs off, the same rule that applies to any turf project. A green's contouring work also disturbs more subgrade than a flat lawn does, which is one more reason to keep it clear of root zones."),
        ],
        "sources": SRC,
    },
    "playground": {
        "title": "Playground Turf Near Wekiwa Springs, Apopka",
        "meta": "Cushioned playground turf for Apopka backyards, priced " + price("playground") + " per sq ft as of September 2026, sized to the equipment's fall height.",
        "h1": "Play-area turf for Apopka families",
        "lede": capsule(f"A shock pad sized to the equipment's fall height sits under most backyard play turf in Apopka, priced inside the {price('playground')} range published for September 2026. The city borders Wekiwa Springs State Park, 7,000 acres that draw families outdoors, and a home play area near the same kind of mature oak canopy has to work around the state's drip-line rule just as the park's own trails do."),
        "sections": [
            ("A play area near a 7,000-acre state park",
             f"<p>Wekiwa Springs State Park sits inside Apopka's city limits, 7,000 acres of spring-fed river and oak hammock that draws families outdoors on weekends ({ext(WEKIWA_PARK[1], 'Wekiwa Springs State Park')}). A backyard play structure a few minutes from the park doesn't answer to the park's own rules, but the same mature oak canopy common near it shows up in nearby subdivisions too, which is where the state's turf standard's drip-line exclusion comes into play before a shock pad and turf go down near a trunk.</p>"),
            ("Shade from decades of nursery growing",
             "<p>Apopka's history as a fern and foliage nursery hub left more mature shade trees standing in older neighborhoods than a typical newer Central Florida subdivision carries, since growers planted windbreaks and shade cover that outlasted the nurseries themselves. A play area under that kind of canopy gets real afternoon shade, which helps with surface heat, but the trade-off is a wider drip-line boundary to work around when siting a swing set or a climbing structure.</p>"
             + f"<p>{post('is-artificial-turf-safe-for-kids-pfas-lead', 'This article')} covers what the state's material rule requires for a surface kids play on directly.</p>"),
            ("How the equipment, not the acreage, sets the pad",
             "<p>A backyard climbing tower with an eight-foot deck needs a thicker shock-absorbing layer underneath it than a low platform swing set does, since the pad's job is cushioning a specific fall height, not covering a fixed area regardless of what sits on it. Florida's material rule keeps rubber and other synthetic infill limited strictly to that equipment footprint, so a wide Apopka backyard with room to spare around a single swing set still only carries that infill directly under it, with silica, rock, shell or coated sand everywhere else the turf reaches.</p>"),
        ],
        "scenario": ("Say you have a 280 sq ft play area under an oak's edge",
                     f"<p>Say you have a 280 sq ft play area planned for a swing set and a small climbing structure in an older Apopka neighborhood, with a mature oak's canopy reaching partway across the space. At the published {price('playground')} range, that job prices between $2,800 and $7,000, with most projects like it landing in the {price('playground', True)} typical band, or $3,360 to $5,320, depending on fall-height pad thickness.</p>"
                     + "<p>Because part of the planned area falls inside the oak's drip line, the crew stakes that boundary first and shifts the layout to keep excavation outside it, which can trim the play area by 40 to 60 sq ft compared with the original sketch, without an arborist's letter to clear the difference.</p>"),
        "faqs": [
            faq("Does living near Wekiwa Springs State Park change playground turf rules for a home?",
                "No. The park's own rules apply to park property, not to a private backyard nearby. A home play area answers to the state's May 2026 turf standard and Apopka's ordinary permitting, the same as anywhere else in the city."),
            faq("Can rubber infill go under an Apopka backyard swing set?",
                "Yes, but only within the equipment's own footprint. The state's material rule limits rubber and other synthetic infill to that specific area; the rest of the yard's turf uses silica sand, rock, shell or a coated sand instead."),
        ],
        "sources": SRC,
    },
    "pool": {
        "title": "Pool and Lanai Turf for Apopka Homes",
        "meta": "Turf beside pools and inside screen cages in Apopka, Florida, priced like a residential lawn at " + price("residential") + " per sq ft, September 2026.",
        "h1": "Turf around an Apopka pool cage",
        "lede": capsule(f"Because pool-area turf uses the identical base and product as a full lawn, just less of it, an Apopka pool deck or screen cage prices out at the residential span, {price('residential')} a square foot, current as of September 2026. A lot near Lake Apopka's shore layers the state's 10-foot waterbody setback on top of the ordinary cage planning."),
        "sections": [
            ("Turf strips inside a screen enclosure",
             "<p>A screened pool cage on an Apopka lot leaves narrow strips of ground on either side of the pool deck, too shaded by the cage's own frame and too awkward in shape for sod to hold up. Turf inside the enclosure needs a drainage underlay where it meets the concrete deck, since the deck itself sheds rainwater differently than open ground does, and a glued, not nailed, edge where turf meets the slab.</p>"),
            ("Pool lots near Lake Apopka's shore",
             f"<p>A pool home backing onto Lake Apopka or one of its connecting canals adds the state's 10-foot waterbody setback to the ordinary pool-cage layout, measured from the ordinary or mean high water line unless a seawall already separates the yard from the water. {ext(LAKE_APOPKA[1], "SJRWMD's restoration work on the lake")} has pushed water clarity up substantially over the past few years, which is part of why more of these shoreline lots have become renovation targets rather than being left as-is.</p>"),
            ("Reclaimed water and a pool-cage lawn's edges",
             f"<p>Where turf stops and natural grass starts at a pool cage's outer edge, Apopka's reclaimed-water service, on the same schedule as potable water, keeps that remaining lawn green without pulling from the drinking-water system. {a('/areas/apopka/', "Our Apopka hub page")} has the exact watering days; none of it applies to the turfed section itself once its heads are capped, which is required either way under the state's rule.</p>"),
        ],
        "scenario": ("Say you have 480 sq ft of turf inside a pool cage",
                     f"<p>Say you have a screened pool cage on an Apopka lot with 480 sq ft of usable ground around the pool deck, split between two side strips and a narrow run behind the shallow end. At the residential range of {price('residential')} per square foot, that job prices between $3,840 and $8,640, with most cage jobs like it landing in the {price('residential', True)} typical band, or $4,800 to $7,680, since the drainage underlay and glue-down edge work add labor that a flat, open lawn doesn't need.</p>"
                     + "<p>If the same lot backs onto a canal feeding Lake Apopka, the crew confirms the 10-foot setback line before finalizing the layout, which on a narrow lot can mean the turf strip runs shorter than the screen cage itself.</p>"),
        "faqs": [
            faq("Does turf inside a pool cage need a different base than an open Apopka lawn?",
                "The rock depth is the same, but a cage installation usually adds a drainage underlay where turf meets the concrete deck and an adhesive-set edge instead of nailed anchoring, since there's no soil at that specific joint to nail into."),
            faq("Does Lake Apopka's ongoing restoration change the setback for a shoreline pool lot?",
                "No. The 10-foot setback is a state standard tied to the water's ordinary or mean high water line, not to water quality, so it applies the same way whether the lake is mid-restoration or fully recovered."),
        ],
        "sources": SRC,
    },
    "repair": {
        "title": "Artificial Turf Repair in Apopka, FL",
        "meta": "Seam, edge and drainage repairs for artificial turf in Apopka, Florida, quoted after photos or a site visit, checked September 2026.",
        "h1": "Fixing worn turf on an Apopka lawn",
        "lede": capsule("A lifted seam and a settled low spot rarely cost the same to fix, so Apopka turf repair gets quoted from photos or a site visit instead of a posted flat rate. A lawn approaching a decade old on the city's fast-draining ridge sand tends to fail differently than one on the flatter ground closer to Lake Apopka."),
        "sections": [
            ("Why a ridge-sand lawn and a lakefront lawn fail differently",
             f"<p>A turf lawn on Apopka's excessively drained Candler or Astatula sand rarely holds standing water, so when it fails, the more common cause is a base that shifted under the turf during a rushed installation rather than a base that was overwhelmed by rain. Closer to Lake Apopka, on the moderately permeable Apopka series or flatter ground, a failed section is more often a drainage problem: a low spot that never had enough compacted rock underneath it to move a Central Florida storm through fast enough.</p>"
             + f"<p>{post('what-does-artificial-turf-warranty-cover', 'This article')} explains what a manufacturer's warranty is likely to cover in either case, and what falls to the installer instead.</p>"),
            ("Repairing a septic-lot lawn without losing pump-out access",
             "<p>An older, in-town Apopka lot still on septic sometimes has turf that was installed years ago without leaving the tank's pump-out lid clear, since that requirement is part of the state's 2026 standard rather than something builders always accounted for earlier. A repair visit on a lot like this is a chance to correct that access point at the same time as fixing whatever brought the crew out in the first place, rather than treating it as a separate job later.</p>"),
            ("What a golf-community ARC wants to see before a repair starts",
             f"<p>A repair inside {city('apopka', "Apopka")}'s golf-community subdivisions, Rock Springs Ridge included, sometimes needs the same architectural sign-off as a fresh installation if the fix changes the turf's visible footprint or color, though a like-for-like seam or edge repair rarely triggers that review at all. Checking with the community's management before a crew shows up avoids a redo over paperwork rather than workmanship.</p>"),
        ],
        "scenario": ("Say you have a 60 sq ft low spot after a rainy season",
                     "<p>Say you have a 60 sq ft section of an Apopka backyard lawn that's held standing water after every storm this past rainy season, in a corner that never drained the way the rest of the yard does. A repair like this usually means pulling that section of turf, checking the base underneath for compaction or a fines problem, correcting the grade, and reinstalling, rather than anything wrong with the turf itself.</p>"
                     + "<p>What that inspection finds sets the price, not a phone call: a straightforward regrade costs far less than discovering the original base was never washed rock in the first place."),
        "faqs": [
            faq("Why does a lawn on Apopka's ridge sand rarely need a drainage repair?",
                "The native sand there drains so fast on its own that pooling is uncommon even with a marginal base. When a ridge-sand lawn fails, it's more often a shifted or unevenly compacted base showing up as a soft or uneven spot, not standing water."),
            faq("Does a turf repair need a new permit from Apopka's Building Safety Division?",
                "Usually not for a like-for-like seam, edge or drainage fix, since that falls under routine maintenance rather than new construction. A repair that changes drainage patterns or footprint is worth a call to the division first."),
        ],
        "sources": SRC,
    },
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
