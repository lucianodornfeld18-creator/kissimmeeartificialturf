# -*- coding: utf-8 -*-
"""Celebration, FL city hub + city x service pages. Celebration is an unincorporated, master-planned
community in Osceola County: Osceola County reviews permits, and the Celebration Residential Owners
Association (CROA) runs a separate architectural review on top of that."""
from _helpers import page, capsule, sec, table, faq, a, svc, city, post, src, ext, price
from _cityservice import cityservice_pages

SLUG = "celebration"

SRC = [
    ("Celebration, Florida (Wikipedia)", "https://en.wikipedia.org/wiki/Celebration,_Florida"),
    ("Osceola County - Building and Permits", "https://www.osceola.org/Doing-Business/Building-and-Permits"),
    ("Osceola County - Building Office Plan Review", "https://www.osceola.org/Doing-Business/Building-and-Permits/Building-Office-Plan-Review"),
    ("Celebration Residential Owners Association - Design Guidelines index", "https://celebration.fl.us/celebration-design-guidelines/"),
    ("CROA Design Guidelines - Lot Zone Definitions & Restrictions, effective 10/01/2009", "https://celebration.fl.us/wp-content/uploads/Guideline-References-Lots.pdf"),
    ("CROA Design Guidelines - Landscape, Plant Guide: Ground Covers, Vines, Turf, effective 10/01/2011", "https://celebration.fl.us/wp-content/uploads/ARC-Design-Guidelines-Landscape-Plant-Guide-Ground-Covers.pdf"),
    ("Celebration Community Development District - About the CDD", "https://www.celebrationcdd.org/about-the-cdd"),
    ("Celebration Community Development District - Stormwater Management", "https://www.celebrationcdd.org/stormwater-management"),
    ("Osceola County - Community Development Districts directory, Celebration CDD", "https://www.osceola.org/agencies-departments/community-development-districts/celerbation-cdd/"),
    ("Toho Water Authority - About Us", "https://www.tohowater.com/about-us"),
    ("Toho Water Authority - Reclaimed Water", "https://www.tohowater.com/reclaimedwater"),
    ("BNBCalc - Celebration, Florida short-term rental regulations", "https://www.bnbcalc.com/blog/short-term-rental-regulation/Celebration-Florida-Guide"),
    ("USDA NRCS - Official Series Description, Basinger series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/B/BASINGER.html"),
    ("Florida DEP - Soil Descriptions Appendix (Osceola County flatwoods soils)", "https://floridadep.gov/sites/default/files/Soil%20Descriptions%20Appendix_0.pdf"),
    ("Orange County Water Atlas - Reedy Creek Watershed", "https://orange.wateratlas.usf.edu/watershed/?wshedid=9&wbodyatlas=watershed"),
]

# ------------------------------------------------------------------ HUB
HUB = page(
    "/areas/celebration/", "city",
    "Artificial Turf in Celebration, FL: Local Guide (2026)",
    "Celebration, FL artificial turf guide: Osceola County permits, CROA architectural review, alley-loaded lots, ponds and soil, updated September 2026.",
    "Artificial turf on Celebration's alley-loaded lots and golf-course edges",
    capsule(
        "Celebration sits about 8 miles west of downtown " + city("kissimmee") + ", an unincorporated Osceola "
        "County community The Walt Disney Company began building in the early 1990s around rear alleys, so "
        "garages sit off a back lane and the street-facing yard stays shallow. A lawn conversion here prices "
        "at " + price("residential") + " a square foot, the Central Florida market rate this September 2026, "
        "and clears both Osceola County's permit desk and the Celebration Residential Owners Association's "
        "own design review before work starts."
    ),
    "".join([
        sec("What makes a Celebration yard different from a typical Osceola County lot?",
            "<p>The first residents moved into Celebration in the summer of 1996, and the town's original "
            "villages, Downtown, Lake Evalyn and the neighborhoods around them, were laid out under a Pattern "
            "Book that still shapes what a homeowner can build or change today. Lots come in seven named types, "
            "Townhome, Bungalow, Garden, Cottage, Village, Manor and Estate, each with its own setback depths "
            "spelled out in " + ext("https://celebration.fl.us/wp-content/uploads/Guideline-References-Lots.pdf", "the community's own lot zone definitions")
            + ", and most of them share the same basic move: garages, meters and trash cans sit behind the "
            "house off a rear alley instead of facing the street. Artisan Park, a newer section mixing "
            "single-family homes with townhomes, follows a separate build era from those first villages. A "
            + svc("residential") + " project has to start by identifying which lot type and which zone of it, "
            "front, side, alley or private, actually holds the planned work.</p>"),
        table("How lot type changes a Celebration turf job",
              ["Lot type", "Location in Celebration", "What changes on site", "How we adjust the build"],
              [
                  ["Front yard on an alley-loaded lot", "Original villages: Downtown, Lake Evalyn and similar",
                   "Shallow, street-visible zone under the Pattern Book's front façade rules", "Treat it as a full architectural review submittal from the first sketch"],
                  ["Alley Yard behind the garage", "Same village lots, facing the rear alley",
                   "CROA's own guideline says the alley yard \"shall be fully irrigated and maintained by the owner\"", "Confirm with CROA that a capped, unirrigated turf strip still meets that upkeep duty before ordering material"],
                  ["Golf-course or pond-backing lot", "Manor and Estate lots along the fairway or a stormwater pond", "The state's 10-foot waterbody setback and pond littoral-zone limits", "Survey the shoreline or seawall before quoting the buildable turf line"],
                  ["Townhome or condo courtyard", "Georgetown-style condos and townhome clusters", "Private Zone shared with a neighbor's wall, little open soil", "A shallower base and tighter edge anchoring built for a shared party wall"],
                  ["Artisan Park lot", "Artisan Park, a newer section built after the original villages", "A different construction era than the 1996-2003 villages", "Check which Design Guidelines edition and lot type actually govern before assuming downtown's rules apply"],
              ],
              "Square-foot price holds steady across every lot type; what moves is access, base depth and which review board signs off."),
        sec("Does Osceola County or Celebration itself review a turf project?",
            "<p>Celebration has never incorporated as its own city, so there's no town hall issuing building "
            "permits here. That job belongs to Osceola County's Community Development Department at 1 "
            "Courthouse Square, Suite 1400, in Kissimmee, phone 407-742-0200, the same office that reviews "
            "work in Harmony or out toward Holopaw. Full detail on what that office asks for lives on our own "
            + a("/laws/permits/osceola-county/", "Osceola County permit page") + ". A county permit is only "
            "half the picture: nearly any exterior change a neighbor can see, a lawn conversion included, also "
            "needs a separate submittal to the Celebration Residential Owners Association's Architectural "
            "Review Committee under the community's Design Guidelines, a step the county's permit process "
            "doesn't touch at all.</p>"),
        sec("What do Celebration's own Design Guidelines say about turf?",
            "<p>CROA publishes a plant guide covering ground covers, vines and turf, "
            + ext("https://celebration.fl.us/wp-content/uploads/ARC-Design-Guidelines-Landscape-Plant-Guide-Ground-Covers.pdf", "effective since October 2011")
            + ", and its turf-grasses section lists exactly three approved species: Bermudagrass, St. Augustine "
            "'Floratam' and Zoysia. It says nothing at all about synthetic turf, so there's no published CROA "
            "rule written specifically for artificial grass to point to, favorable or not. What that means in "
            "practice is that a turf conversion goes through the same general landscape-change review as "
            "swapping a plant bed or adding a paver path, judged on what's visible rather than on the "
            "material underneath it.</p>"),
        sec("What is the Celebration Community Development District, and what does it maintain?",
            "<p>Separate from CROA, the Celebration Community Development District is a unit of local "
            "government, not a homeowners association, created under Chapter 190 of the Florida Statutes and "
            "established on March 29, 1994, with a five-member elected Board of Supervisors. Its job is public "
            "infrastructure: the Downtown lake and esplanade, common-area landscaping and the street trees "
            "lining Celebration's blocks, not the plant list on a private lot. It also plays a part in the "
            "town's stormwater ponds and lakes, which " + ext("https://www.celebrationcdd.org/stormwater-management", "the district describes as a master system")
            + " permitted through the South Florida Water Management District and the Reedy Creek Improvement "
            "District. See " + a("/laws/hoa-rules/", "what a Florida HOA can and can't restrict") + " for how "
            "that government-versus-association line matters for a homeowner.</p>"),
        sec("Where does Celebration's water come from, and where do the pond and tree rules bite hardest?",
            "<p>Toho Water Authority serves Kissimmee, St. Cloud, Poinciana and unincorporated Osceola County, "
            "Celebration included, on " + src("toho-days", "two assigned irrigation days a week by address")
            + ", with no daytime watering and the schedule under review through 2026 (" + src("osceola-water-2026", "Osceola's proposed conservation ordinance")
            + "). Some Celebration accounts carry a reclaimed line, but reclaimed customers follow the same "
            "restricted schedule as a potable account, and " + src("dep-rule", "the state's synthetic turf rule")
            + " bars in-ground irrigation, reclaimed or potable, from ever running to synthetic turf at all. "
            "The ponds ringing the golf course and the wetland-edge buffers behind many lots trigger the "
            "state's 10-foot waterbody setback unless a seawall or bulkhead already separates the yard, and "
            "the mature street trees the CDD maintains put the drip-line rule in play for almost any excavation "
            "along an alley yard.</p>"),
        sec("What's actually under a Celebration lawn?",
            "<p>Osceola County's flatwoods soil in this part of the county maps mostly to Immokalee sand, the "
            "county's most widespread series, with pockets of " + ext("https://soilseries.sc.egov.usda.gov/OSD_Docs/B/BASINGER.html", "Basinger fine sand")
            + " filling the old drainageways and sloughs the county's own soil survey traces through here. "
            "Basinger is classed very poorly drained, with a seasonal high water table sitting between zero "
            "and eighteen inches of the surface. CROA's own plant guide tells homeowners choosing anything for "
            "the yard to weigh whether it tolerates \"soggy soil (such as former swampland)\", a plain "
            "acknowledgment of the ground under a good share of this town. A base built to the state's washed, "
            "open-graded standard needs more depth on these low, marshy pockets than on the town's higher "
            "Manor and Estate sections. More on that build is in " + post("base-under-artificial-turf-florida-sandy-soil", "our guide to Central Florida's sandy base") + ".</p>"),
        sec("What can CROA actually require before turf goes in?",
            "<p>Florida's " + src("fs7203045", "F.S. 720.3045") + " keeps any homeowners association statewide "
            "from banning turf that isn't visible from the parcel's frontage or an adjacent parcel, which "
            "covers most fenced backyards in Celebration. What it doesn't do is replace CROA's own "
            "architectural review: a Design Guidelines submittal is a separate track from what a covenant can "
            "restrict, and " + src("stc-fl", "the state's turf law is aimed at city and county governments")
            + ", not at what an association's ARC asks a homeowner to file. Our " + a("/laws/florida-hb-683/", "explainer on HB 683 and Florida's turf rule")
            + " covers what the state controls, and the " + a("/tools/hoa-packet-checklist/", "HOA and ARC packet checklist")
            + " lays out what to gather before that submittal goes in, which is worth doing before ordering "
            "any material.</p>"),
        sec("Looking for a turf company that already understands Celebration's paperwork?",
            "<p>Homeowners searching for the best artificial turf installer near me in Celebration are usually "
            "after one thing: someone who can sit through an ARC review and answer the zone, setback and "
            "irrigation questions without stalling the project for a month. An installer who can name the lot "
            "type, point to the alley setback, and explain how the capped irrigation line satisfies CROA's own "
            "upkeep language has usually done this paperwork before.</p>"),
        "<!--AUTO:city-services-->",
    ]),
    faqs=[
        faq("Does Osceola County or Celebration itself issue a permit for turf work?",
            "Celebration is unincorporated, so Osceola County's Community Development Department issues the "
            "permit, at 407-742-0200. CROA's Architectural Review Committee reviews the same project "
            "separately, since a county permit doesn't cover what an association's design guidelines ask for."),
        faq("Do Celebration's Design Guidelines mention artificial turf?",
            "No. The CROA plant guide for ground covers, vines and turf lists only living grasses, "
            "Bermudagrass, St. Augustine 'Floratam' and Zoysia, and says nothing about synthetic material. A "
            "turf project still goes through the same general landscape-change review as any other yard "
            "change."),
        faq("Can CROA make a Celebration homeowner remove backyard turf?",
            "Not if it isn't visible from the street or an adjacent parcel; F.S. 720.3045 protects that "
            "regardless of the covenant. An alley-facing strip is a closer call, since alley traffic can see "
            "it, which is worth confirming with CROA before installing."),
        faq("What does the Celebration Community Development District actually control?",
            "It's a unit of local government, created under Chapter 190 in 1994, separate from CROA. It "
            "maintains the Downtown lake and esplanade, common-area landscaping and street trees; it doesn't "
            "set rules for what goes on a private lot."),
        faq("How close can turf sit to a Celebration pond or the golf course?",
            "Rule 62-308.100 sets one statewide floor no matter which town the water is in: turf stops within "
            "10 feet of a pond or lake's edge, waived only where a seawall or bulkhead already stands between "
            "the yard and the water. Celebration's stormwater ponds are permitted through the South Florida "
            "Water Management District and the Reedy Creek Improvement District."),
        faq("Is reclaimed water available for a Celebration lawn?",
            "In parts of the system, yes, but reclaimed customers follow the same restricted watering-day "
            "schedule as a potable account. Neither reclaimed nor potable in-ground irrigation can legally run "
            "to synthetic turf under the state's rule."),
    ],
    sources=SRC,
    city=SLUG,
    crumbs=[("Service areas", "/areas/")],
    crumb="Celebration",
    related=[
        ("/areas/osceola-county/", "Artificial turf in Osceola County"),
        ("/laws/permits/osceola-county/", "Osceola County permit rules"),
        ("/laws/hoa-rules/", "Can a Florida HOA ban artificial turf?"),
        ("/areas/kissimmee/", "Artificial turf in Kissimmee"),
        ("/areas/reunion/", "Artificial turf in Reunion"),
        ("/areas/championsgate/", "Artificial turf in ChampionsGate"),
        ("/artificial-turf-cost/", "Turf cost tables for Central Florida"),
    ],
)

# ------------------------------------------------------------------ LOCAL
LOCAL = {}

LOCAL["residential"] = {
    "title": "Artificial Grass Installation in Celebration, FL",
    "meta": "Artificial grass in Celebration, FL runs $8-$18 a sq ft installed as of September 2026, on alley-loaded lots that answer to Osceola County and CROA's ARC.",
    "h1": "Artificial grass for Celebration's alley-loaded villages and newer sections",
    "lede": capsule(
        "Converting a Celebration lawn to synthetic turf runs " + price("residential") + " a square foot, the "
        "market rate everywhere else in Central Florida too as of September 2026. What sets this town apart "
        "is the paperwork and the footprint: a shallow front yard governed by CROA's Pattern Book, a rear "
        "alley yard the guidelines say the owner must keep irrigated and tidy, and an Osceola County permit "
        "desk that handles the county side no matter which village the lot sits in."
    ),
    "sections": [
        ("A front yard here answers to the Pattern Book before it answers to a shovel",
         "<p>Celebration's original villages, built starting when the first residents arrived in the summer "
         "of 1996, run on a Front Façade Zone system: the strip between the property line and the house's "
         "setback line is meant to be seen, and CROA's Architectural Review Committee reviews changes to it "
         "under the community's Design Guidelines. That review sits on top of, not instead of, whatever "
         "Osceola County's Community Development Department requires for the permit itself. A homeowner "
         "converting a front lawn should expect two separate approvals moving on two separate timelines, not "
         "one combined process.</p>"),
        ("The alley yard carries its own upkeep language worth reading first",
         "<p>Behind most Celebration houses, the rear Alley Yard sits between the alley pavement and a "
         "five-foot utility easement that doubles as the Alley Setback, and CROA's own zone definitions state "
         "that this strip \"shall be fully irrigated and maintained by the owner.\" Converting that strip to "
         "turf means capping the irrigation line entirely, since Florida's synthetic turf rule bars watering "
         "turf through an in-ground system regardless of what a guideline assumed when it was written. "
         "Confirming with CROA that a capped, well-kept turf strip still satisfies that language is worth "
         "doing before the crew shows up.</p>"),
        ("Lot type sets how much yard there actually is to work with",
         "<p>A Cottage or Bungalow lot in one of the older villages sits on a noticeably smaller footprint "
         "than a Manor or Estate lot near the golf course, and the setback depths in "
         + a("/laws/permits/osceola-county/", "the county's permit review") + " don't change that math. A "
         + svc("residential") + " quote for a compact village lot spends more time on layout, where the base "
         "meets a paver path, how close the Front Façade Zone runs to the sidewalk, than a quote for an Estate "
         "lot with room to spare on every side.</p>"),
    ],
    "scenario": (
        "Say you have a 500 sq ft village front yard",
        "<p>Say you have a 500 sq ft front yard on a Cottage lot in one of Celebration's original villages, "
        "St. Augustine that's thinned under two live oaks planted when the street was new. At "
        + price("residential", True) + " a square foot, that section runs roughly $5,000 to $8,000, with the "
        "oaks' drip lines likely trimming the buildable area before square footage does, since excavation "
        "can't enter a live oak's root zone without a certified arborist's sign-off. The project needs both "
        "an Osceola County permit and a CROA architectural review submittal before the crew arrives, and the "
        "ARC step usually takes longer to clear than the county's.</p>"
    ),
    "faqs": [
        faq("Does a Celebration turf project need two separate approvals?",
            "Usually yes: Osceola County's Community Development Department reviews the permit side, and "
            "CROA's Architectural Review Committee separately reviews anything visible from the street or an "
            "adjacent lot under the community's Design Guidelines."),
        faq("Searching for the best artificial grass installer near me in Celebration?",
            "Ask whether they've filed a CROA architectural review submittal before, not just an Osceola "
            "County permit. An installer who only knows the county side hasn't done a Celebration front yard "
            "recently."),
    ],
    "sources": SRC,
}

LOCAL["pet"] = {
    "title": "Pet Turf for Celebration's Courtyard Yards",
    "meta": "Pet turf in Celebration, FL runs $10-$18 a sq ft installed as of September 2026, sized for narrow Private Zone courtyards and alley-side dog runs.",
    "h1": "Dog runs and pet turf for Celebration's tighter yards",
    "lede": capsule(
        "Pet turf installed in Celebration, Florida runs " + price("pet") + " a square foot as of September "
        "2026, and the design has to fit a smaller footprint than most of Central Florida offers: a Private "
        "Zone courtyard behind a townhome, or a strip of Alley Yard a CROA guideline already expects to be "
        "kept irrigated and tidy. Both settings favor a compact, well-drained run over a sprawling one."
    ),
    "sections": [
        ("Private Zone courtyards leave little room for error",
         "<p>Townhomes and Garden-lot homes in Celebration often keep their outdoor space inside the Private "
         "Zone, a courtyard bounded by a garage wall, a neighbor's fence and maybe a screened porch, with "
         "square footage measured in the dozens rather than hundreds. A dog run built into a space that small "
         "needs every inch of base and drainage doing real work, since there's no larger lawn nearby to "
         "absorb an overflow the way a half-acre yard elsewhere would. Sizing the run to the actual courtyard, "
         "not a generic dog-yard template, matters more here than almost anywhere else on our service map.</p>"),
        ("An alley-side run changes what CROA's upkeep language means",
         "<p>CROA's zone definitions state that the Alley Yard behind a house \"shall be fully irrigated and "
         "maintained by the owner,\" language written with live sod in mind. A dog run built along that strip "
         "instead needs the irrigation line capped at the valve box under Florida's synthetic turf rule, which "
         "changes what \"maintained\" has to mean going forward: rinsing and brushing rather than mowing and "
         "watering. Raising that question with CROA before installation avoids a mismatch between what the "
         "guideline assumes and what a capped irrigation line actually does.</p>"),
        ("Why the fully permeable backing matters more on a small courtyard run",
         "<p>A courtyard dog run has less soil around it to disperse a rinse than an open backyard does, so "
         "the backing's ability to pass liquid straight down rather than sideways carries more weight on a "
         "tight Celebration lot than on a wide-open one. Basinger and Immokalee soils common to this part of "
         "Osceola County already hold water close to the surface in low spots, which is one more reason a "
         "shallow, undersized base shows up as odor faster on a small courtyard than it would on acreage.</p>"),
    ],
    "scenario": (
        "Say you have a 180 sq ft townhome courtyard",
        "<p>Say you have a 180 sq ft courtyard behind a Georgetown-style townhome, walled on three sides, with "
        "one medium dog wearing a bare path along the fence line. At " + price("pet", True) + " a square foot, "
        "that run costs roughly $2,160 to $2,880, built with the fully permeable backing a pet system needs "
        "since there's no surrounding lawn to help drainage along. The Private Zone location means a CROA "
        "submittal is still required, since the courtyard sits within view of a shared walkway even though "
        "it's fenced from the street.</p>"
    ),
    "faqs": [
        faq("Is a dog run in a Celebration townhome courtyard still subject to CROA review?",
            "Often yes, since a Private Zone courtyard can still be visible from a shared walkway or a "
            "neighbor's window even when it's fenced from the street. Checking sightlines before assuming "
            "F.S. 720.3045 covers it is worth the extra step."),
        faq("Can a dog run go in a Celebration alley yard?",
            "Yes, but the irrigation line has to be capped rather than left running, since the state's rule "
            "bars watering synthetic turf through an in-ground system. Confirm with CROA how that changes the "
            "alley yard's upkeep requirement before installing."),
    ],
    "sources": SRC,
}

LOCAL["putting"] = {
    "title": "Backyard Putting Greens in Celebration, FL",
    "meta": "Backyard putting greens in Celebration, FL run $14-$30 a sq ft installed as of September 2026, sized for golf-lot backyards and CROA's architectural review.",
    "h1": "Putting greens for Celebration's golf-course and Estate lots",
    "lede": capsule(
        "Building a backyard putting green in Celebration costs " + price("putting") + " a square foot, the "
        "market range this September 2026. Which lot type it goes on matters more than the price does: a "
        "Manor or Estate lot backing the golf course has room for a multi-tier layout, while a Cottage or "
        "Garden lot in one of the original villages usually calls for a single-tier green tucked into a "
        "smaller footprint."
    ),
    "sections": [
        ("Golf-adjacent lots carry the state's waterbody rule into the layout",
         "<p>A number of Celebration's Manor and Estate lots back onto the fairways and the ponds that line "
         "the town's golf course, and any green designed for one of those lots has to respect the state's "
         "10-foot setback from the pond's edge unless a seawall or bulkhead already separates the yard from "
         "the water. That setback can trim a planned green's far edge more than the lot's overall size "
         "suggests, since it's measured from the actual shoreline rather than from the house or a fence "
         "line.</p>"),
        ("CROA's architectural review comes before the base gets shaped",
         "<p>A putting green counts as a visible hardscape change under CROA's Design Guidelines the same way "
         "a paver patio does, so a submittal to the Architectural Review Committee has to clear before "
         "excavation starts, on top of whatever Osceola County's permit process requires. That review looks "
         "at how the green's shape and any retaining edge sit within the lot's Private Zone, not at the "
         "putting surface itself, since the community's own plant guide has nothing written about synthetic "
         "turf either way.</p>"),
        ("Smaller village lots call for a single tier, not a scaled-down copy",
         "<p>A green sized for a Cottage or Bungalow lot in one of the 1996-2003 villages generally works "
         "better as a single-tier design with one or two cups than as a shrunken version of a multi-tier "
         "Estate-lot layout, since the shorter sightlines and tighter Private Zone leave less room for a "
         "long fringe. Artisan Park's newer, slightly larger lots sit somewhere between the two, closer to a "
         "Garden lot's footprint than a village Cottage's.</p>"),
    ],
    "scenario": (
        "Say you have a 350 sq ft Manor-lot backyard",
        "<p>Say you have a 350 sq ft backyard on a Manor lot backing the golf course, with a pond visible "
        "past the property line and a screened lanai taking up part of the near side. At "
        + price("putting", True) + " a square foot, a single-tier green with a fringe runs roughly $6,300 to "
        "$8,750, and the layout needs to confirm the pond's 10-foot setback before finalizing how far the "
        "green can extend toward the fairway view. The project still needs a CROA architectural review "
        "submittal alongside the county permit, since the green is visible from the golf course side of the "
        "lot.</p>"
    ),
    "faqs": [
        faq("Does a putting green on a Celebration golf-lot backyard need CROA approval?",
            "Yes, the same Architectural Review Committee process that applies to any visible hardscape "
            "change applies to a putting green, separate from whatever Osceola County's permit process "
            "covers."),
        faq("What do the best putting green builders near you check on a Celebration golf-adjacent lot?",
            "Whether a pond or fairway-side water feature triggers the state's 10-foot setback, and how much "
            "of the backyard a screened lanai or golf-course sightline leaves usable for the green's shape."),
        faq("Can a smaller Celebration village lot fit a multi-tier green?",
            "Usually not comfortably. A Cottage or Bungalow lot's Private Zone tends to favor a single-tier "
            "design with a shorter fringe over a scaled-down copy of a layout built for a larger Manor or "
            "Estate lot."),
    ],
    "sources": SRC,
}

LOCAL["playground"] = {
    "title": "Playground Turf for Celebration Backyards",
    "meta": "Playground turf in Celebration, FL runs $10-$25 a sq ft installed as of September 2026, fitted into Private Zone yards under the CDD's street-tree canopy.",
    "h1": "Backyard play turf for Celebration's family neighborhoods",
    "lede": capsule(
        "Playground turf installed in Celebration, Florida runs " + price("playground") + " a square foot as "
        "of September 2026. With a 2020 population just above 11,000 spread across village lots built mostly "
        "between 1996 and the early 2000s, most backyard play-turf requests here come from a Private Zone "
        "already shaded by street trees that have had two or three decades to mature."
    ),
    "sections": [
        ("Mature street trees mean the drip-line rule shows up early",
         "<p>The Celebration Community Development District maintains the street trees lining much of the "
         "town, and many of those trees, along with ones homeowners planted in the same era, have grown large "
         "enough that their canopies reach well into a Private Zone backyard. Any play-turf layout under that "
         "canopy has to keep clear of the tree's drip line unless a certified arborist signs off that the "
         "install won't harm the roots, which can shift a swing set or climbing structure a few feet from "
         "where a family first pictured it.</p>"),
        ("A Private Zone play area is smaller than a typical suburban one",
         "<p>Because so much of a Celebration lot's outdoor space sits inside a compact Private Zone rather "
         "than a sprawling backyard, a play-turf layout usually has to share that footprint with a pool cage, "
         "a garage wall or a fence line rather than standing alone. Working the shock-pad zone around whatever "
         "else already occupies the Private Zone, instead of assuming an open rectangle, is the first step on "
         "most of these projects.</p>"),
        ("CROA review applies here the same way it does to any visible change",
         "<p>A play structure and its turf pad count as a visible addition under CROA's Design Guidelines if "
         "any part of it can be seen from the street, an adjacent lot or a shared alley, which means an "
         "Architectural Review Committee submittal often runs alongside the Osceola County permit for a "
         "larger structure. A low, ground-level play pad tucked entirely behind a privacy fence has a better "
         "chance of clearing that bar without a lengthy review.</p>"),
    ],
    "scenario": (
        "Say you have a 150 sq ft play corner",
        "<p>Say you have a 150 sq ft corner of a Private Zone backyard set aside for a swing set with a "
        "5-foot fall height, shaded by a mature oak planted when the village was new. At "
        + price("playground", True) + " a square foot, a shock-pad system sized to that fall height runs "
        "roughly $1,800 to $2,850, and the oak's canopy means the layout needs to confirm the drip line before "
        "finalizing where the equipment's footprint can sit. Because the corner is visible from a side alley, "
        "a CROA submittal is worth filing even for a modest addition like this one.</p>"
    ),
    "faqs": [
        faq("Does a Celebration backyard play area need CROA approval?",
            "If any part of it, the structure or the turf pad, is visible from the street, an adjacent lot or "
            "a shared alley, yes. A play area fully screened by a privacy fence has a better chance of "
            "clearing review without a lengthy submittal."),
        faq("Do Celebration's street trees affect where a play structure can go?",
            "They can. Trees the CDD maintains along the street, plus ones homeowners planted decades ago, "
            "often reach far enough into a Private Zone that the drip-line rule applies to part of the yard "
            "without a certified arborist's sign-off."),
    ],
    "sources": SRC,
}

LOCAL["pool"] = {
    "title": "Pool & Lanai Turf in Celebration, FL",
    "meta": "Pool and lanai turf in Celebration, FL prices like a residential lawn, $8-$18 a sq ft as of September 2026, sized for compact Private Zone pool cages.",
    "h1": "Turf around Celebration pool cages and screened lanais",
    "lede": capsule(
        "Turf around a Celebration pool or inside a screened lanai costs the same as a residential lawn, "
        + price("residential") + " a square foot, the market range this September 2026. What actually changes "
        "the job here is the screen mesh itself: most Celebration cages sit out of street view entirely, which "
        "shifts both whether CROA has to review the work and how the state's wind-anchoring rule applies "
        "inside an enclosure."
    ),
    "sections": [
        ("A screened cage often clears CROA's visibility test on its own",
         "<p>CROA's Design Guidelines trigger an Architectural Review Committee submittal for anything visible "
         "from the street, an adjacent lot or a shared alley, and a pool cage wrapped in mesh on every open "
         "side is frequently the one part of a Celebration lot that clears that bar without a formal filing, "
         "since the screen blocks the same sightlines a fence would. That changes on a Manor or Estate lot "
         "where the lanai opens toward the golf course or a pond instead of a backyard fence: a fairway walker "
         "or a neighbor across the water can still see into the enclosure, which puts the project back under "
         "CROA's review even though the street side never would have flagged it.</p>"),
        ("Reclaimed and potable lines under the deck get capped the same way",
         "<p>Some Celebration accounts carry a reclaimed water line alongside the potable service Toho Water "
         "Authority bills for, and an older pool deck sometimes ran a dedicated zone off either one to keep a "
         "strip of sod green right up to the screen track. The state's synthetic turf rule doesn't split the "
         "two: reclaimed or potable, an in-ground line can't legally water synthetic turf, so both kinds get "
         "capped at the valve box the same way once the ring around the cage goes in.</p>"),
        ("The state's anchoring rule carries more weight inside an enclosure",
         "<p>Rule 62-308.100 requires turf anchored at every edge and seam to withstand wind, and a screened "
         "lanai concentrates gusts against that border rather than letting them spend themselves across an "
         "open lawn. A narrow strip of turf running tight against the cage's concrete curb needs that anchoring "
         "done properly for exactly that reason, more than a wide residential yard where wind has open ground "
         "to cross before it ever reaches a seam.</p>"),
    ],
    "scenario": (
        "Say you have a 260 sq ft lanai ring on a golf-course lot",
        "<p>Say you have a Manor-lot lanai wrapping three sides of the pool cage, 260 square feet of sod "
        "squeezed between the screen and the concrete curb, thin from chlorine splash and never quite "
        "recovering between waterings. Turf for that ring costs " + price("residential", True)
        + " a square foot, so the job lands between $2,600 and $4,160, and because the open side of the lanai "
        "faces the fairway rather than the street, it still counts as visible under CROA's Guidelines even "
        "though the mesh hides it from the road. The reclaimed line that used to feed that strip gets capped "
        "at the valve box the same day the new turf goes down.</p>"
    ),
    "faqs": [
        faq("Does pool-area turf in Celebration cost more than a plain lawn?",
            "The per-square-foot range matches any residential lawn. What pushes a job toward the top of that "
            "range is the edge work: seaming tight against a concrete curb inside a screened enclosure takes "
            "longer than finishing an open stretch of yard."),
        faq("Does a fully screened pool cage still need a CROA submittal?",
            "Often not, since Design Guidelines review turns on what's visible from the street, an adjacent "
            "lot or a shared alley, and a fully screened cage on an interior lot usually clears that test. A "
            "lanai open toward the golf course or a pond is the exception, since that view counts as visible "
            "too."),
    ],
    "sources": SRC,
}

LOCAL["str"] = {
    "title": "Vacation Rental Turf in Celebration: A Tight Market",
    "meta": "Vacation rental turf in Celebration, FL is a small market: CROA's charter sets year-long minimum leases, unlike the nightly-rental corridors nearby.",
    "h1": "Turf for Celebration rental homes, where nightly stays aren't allowed",
    "lede": capsule(
        "Turf for a Celebration rental property costs the same as any residential lawn, " + price("residential")
        + " a square foot, this September's market rate, but the nightly-rental demand that drives this "
        "service closer to the theme parks barely exists here. CROA's governing charter sets a one-year "
        "minimum lease term for most homes, and Osceola County's short-term-rental overlay zoning excludes "
        "Celebration outright."
    ),
    "sections": [
        ("CROA's charter rules out the nightly-rental model most turf here would serve",
         "<p>Under a CROA charter provision approved August 28, 2024, most Celebration primary dwellings carry "
         "an initial lease term of no less than one year, and garage apartments are capped at a three-month "
         "initial term with no more than two tenants in any twelve-month stretch; single rooms can't be leased "
         "at all. Compare that with " + city("kissimmee") + "'s US-192 corridor or the whole-home rental "
         "subdivisions around " + city("four-corners") + " and " + city("championsgate")
         + ", both built around nightly stays, and it's clear Celebration was never meant to compete with "
         "them on that front.</p>"),
        ("Osceola's own overlay zoning agrees with CROA on this point",
         "<p>Osceola County's short-term-rental overlay district, the zoning tool that lets a whole-home "
         "nightly rental operate legally elsewhere in the county, doesn't extend into Celebration at all. That "
         "leaves CROA's own lease-term rules as the operative limit here rather than a county zoning fight, "
         "and a homeowner asking about a nightly Airbnb in Celebration is asking about something the "
         "association's charter already forecloses.</p>"),
        ("Where durable turf still pays off despite the smaller market",
         "<p>A furnished, legally leased property on a one-year term still turns over tenants and still shows "
         "wear between move-outs, and durable turf solves that the same way it would on an owner-occupied "
         "lawn: no mowing schedule to coordinate around a lease changeover, no dead patch from weeks a unit "
         "sat vacant. That's a longer-term rental use case, not a nightly one, and it's the honest frame for "
         "what this service actually looks like in Celebration.</p>"),
    ],
    "scenario": (
        "Say you have a furnished long-term rental yard",
        "<p>Say you have a furnished single-family rental on a one-year CROA-compliant lease, with a 400 sq "
        "ft backyard that shows bare patches between tenant turnovers. Priced at " + price("residential", True)
        + " a square foot, that backyard costs between $4,000 and $6,400 to convert, and because the property "
        "still sits inside a village lot, a CROA architectural review submittal applies the same as it would "
        "for an owner-occupied home, on top of the Osceola County permit.</p>"
    ),
    "faqs": [
        faq("Can I run a nightly Airbnb out of a Celebration house?",
            "No, in practice. CROA's charter sets a one-year minimum lease term for most homes, and Osceola "
            "County's short-term-rental overlay zoning doesn't cover Celebration, so there's no path to a "
            "legal nightly rental here the way there is closer to the parks."),
        faq("Is there a best vacation-rental turf company near me for a Celebration property?",
            "The better question is which installer understands long-term rental wear, since Celebration's "
            "lease-term rules rule out the nightly-turnover market that phrase usually assumes elsewhere."),
        faq("Do garage apartments in Celebration have different rental rules?",
            "Yes. CROA's charter allows a three-month initial lease term for a garage apartment, capped at two "
            "tenants in any twelve-month period, shorter than the one-year term set for a primary dwelling."),
    ],
    "sources": SRC,
}

LOCAL["commercial"] = {
    "title": "Commercial Turf for Celebration's Town Center",
    "meta": "Commercial turf in Celebration, FL is quoted per job from drawings, covering Town Center storefronts, condo courtyards and CDD-maintained common areas.",
    "h1": "Commercial and common-area turf around Celebration's Town Center",
    "lede": capsule(
        "A Celebration commercial project gets priced from a site visit or a set of drawings, not a single "
        "square-foot range, because a Town Center storefront, a condo courtyard and a CDD-maintained common "
        "area each carry their own base and approval needs. A compact downtown built around a small lake "
        "means most commercial turf work here is small-footprint rather than sprawling."
    ),
    "sections": [
        ("The CDD, not a private owner, controls the Downtown common areas",
         "<p>The Celebration Community Development District maintains the Downtown lake and esplanade, "
         "including its shade structures and interactive fountain, along with common-area landscaping and "
         "street trees, as part of its role as a unit of local government rather than a private association. "
         "Any turf proposed for those shared spaces would run through the district's own process, separate "
         "from the CROA review that governs a private lot, and separate again from whatever Osceola County's "
         "permit desk requires for the parcel itself.</p>"),
        ("Condo and townhome associations run their own approval on top of that",
         "<p>Georgetown-style condo buildings and townhome clusters in Celebration typically carry their own "
         "association governance for shared courtyards and entry landscaping, on top of CROA's community-wide "
         "Design Guidelines. A board considering turf for a shared courtyard or a pet relief area should "
         "expect two layers of sign-off, its own association plus CROA, before a contractor can start, more "
         "than a single-family Village or Manor lot typically needs.</p>"),
        ("Storefronts along the Town Center sit on the same small footprint as the housing around them",
         "<p>Retail and office space near Celebration Avenue and Market Street sits close to the street with "
         "little setback, mirroring the compact village lots surrounding it rather than a suburban shopping "
         "plaza's open parking apron. A storefront's turf project, a planter strip or a small patio area, "
         "still needs Osceola County's permit review for the parcel, and coordinating that with the "
         "property's own commercial lease terms and any downtown design standards takes more lead time than a "
         "single-family job.</p>"),
    ],
    "scenario": (
        "Say you have a 900 sq ft condo courtyard",
        "<p>Say you have a 900 sq ft shared courtyard at a Georgetown-style condo building near the Town "
        "Center, currently thin St. Augustine that struggles under foot traffic between units. Pricing that "
        "job takes a walk-through rather than a flat per-square-foot figure, since shared irrigation lines, "
        "existing hardscape and the association's own approval process all weigh on labor more heavily than "
        "a private backyard ever would. The board would need its own sign-off plus a CROA review before work "
        "starts, separate from the Osceola County permit for the parcel.</p>"
    ),
    "faqs": [
        faq("How is commercial turf priced in Celebration?",
            "From a walk-through or a set of drawings, not one flat number, since a Town Center storefront, a "
            "condo courtyard and a CDD common area each carry different access, irrigation and approval "
            "requirements. There's no single per-square-foot figure that fits all three."),
        faq("Can turf go in a Celebration CDD-maintained common area?",
            "It would need to go through the district's own process, since the CDD maintains the Downtown "
            "lake, esplanade and common-area landscaping as a unit of local government, not through CROA's "
            "private-lot architectural review."),
        faq("Does a Celebration condo association need CROA approval too?",
            "Often yes, on top of its own building or association sign-off, since CROA's community-wide "
            "Design Guidelines apply broadly across Celebration regardless of whether the property is a "
            "single-family lot or a condo building."),
    ],
    "sources": SRC,
}

LOCAL["sports"] = {
    "title": "Sports & Fitness Turf in Celebration, FL Yards",
    "meta": "Sports and fitness turf in Celebration, FL is quoted per job, fitting compact bocce and putting-adjacent lanes into Manor and Estate Private Zones.",
    "h1": "Home sports turf sized for Celebration's compact lots",
    "lede": capsule(
        "Fitting a bocce lane, a small agility strip or a sled track into a Celebration yard gets priced from "
        "a site visit, not a flat square-foot number, because layout eats more of the budget than area does. "
        "Lot size here runs smaller across the board than in most towns on our service map, which decides "
        "what actually fits before price ever enters the conversation."
    ),
    "sections": [
        ("Manor and Estate lots have the only real room for a longer feature",
         "<p>Among Celebration's seven lot types, only Manor and Estate lots, generally the ones backing the "
         "golf course or a larger pond, have enough uninterrupted Private Zone space for something like a full "
         "bocce court or a sled and agility lane longer than 20 feet. Even there, the state's 10-foot "
         "waterbody setback trims the usable length on any lot backing a pond or fairway water feature, which "
         "is worth checking before a layout gets drawn.</p>"),
        ("Village and Garden lots favor a short, single-purpose feature",
         "<p>A Cottage, Bungalow or Garden lot's Private Zone rarely has room for more than a compact feature, "
         "a short putting fringe doubling as a chipping target, or a narrow sled-push lane tucked against a "
         "fence line. Fitting a sports surface into one of these smaller footprints means accepting a shorter, "
         "single-purpose design rather than scaling down a layout built for a bigger lot.</p>"),
        ("A golf-course-facing feature draws CROA's review even when a fenced one wouldn't",
         "<p>A bocce court or a sled lane tucked behind a privacy fence away from the alley can sometimes read "
         "as low-profile enough to skip a lengthy Architectural Review Committee process, but the same feature "
         "built along a Manor or Estate lot's open side toward the fairway doesn't get that pass, since a golf "
         "cart path counts as a public sightline under CROA's Design Guidelines the same as the street does. "
         "That distinction, not the sport itself, usually decides how long the paperwork takes.</p>"),
    ],
    "scenario": (
        "Say you have a 10 by 60 ft bocce lane on a golf-course Manor lot",
        "<p>Say you have a Manor lot backing the golf course with room along the side yard for a regulation-"
        "width bocce lane, 10 feet by 60 feet, sitting in view of the cart path rather than screened behind a "
        "fence. Because that side of the lot counts as visible under CROA's Design Guidelines, the "
        "Architectural Review Committee submittal has to cover the lane's retaining edge and base detail, not "
        "just the turf spec, before the county permit gets filed. Pricing the lane still takes a site visit "
        "rather than a flat number, since the base depth a true bocce surface needs under repeated play "
        "weighs on labor more than the lane's length by itself.</p>"
    ),
    "faqs": [
        faq("What sports surfaces fit on a Celebration lot?",
            "A full bocce court or a longer agility lane generally needs a Manor or Estate lot's larger "
            "Private Zone. A Cottage, Bungalow or Garden lot usually fits only a shorter, single-purpose "
            "feature."),
        faq("Does a golf-course-facing sports feature need CROA approval even if it's small?",
            "Usually yes. A cart path counts as a public sightline the same way a street does, so a compact "
            "bocce lane or agility strip facing the fairway still goes through the Architectural Review "
            "Committee even when a similar feature behind a privacy fence might not."),
    ],
    "sources": SRC,
}

LOCAL["pavers"] = {
    "title": "Turf & Pavers Along Celebration's Alleys",
    "meta": "Turf between pavers in Celebration, FL is quoted per job, from alley-side paver strips to front-loaded driveways on newer Artisan Park lots.",
    "h1": "Turf ribbons and paver paths for Celebration's alleys and driveways",
    "lede": capsule(
        "Pricing turf between pavers in Celebration takes a site visit rather than one square-foot figure, "
        "because an alley-side apron, a driveway ribbon and a stepping-stone path each call for a different "
        "split of paver and turf across the same footprint. Most driveways here connect to a rear alley "
        "rather than the front street, which changes where this kind of project actually goes.</p>"
    ),
    "sections": [
        ("Alley-side aprons see more traffic than a front driveway would",
         "<p>Because garages in most Celebration villages open onto the rear alley rather than the street, "
         "the paver apron connecting a garage to the alley cartway carries daily car and trash-pickup traffic "
         "that a front-facing driveway elsewhere wouldn't. A turf ribbon set into that apron needs a firmer, "
         "better-anchored edge than a purely decorative front-yard strip, since the alley's 12-foot cartway and "
         "the vehicles using it put real load close to the turf's border.</p>"),
        ("Artisan Park's front-loaded driveways work more like a typical Florida subdivision",
         "<p>Artisan Park, built after Celebration's original alley-loaded villages, mixes some front-loaded "
         "garages and driveways into its layout, closer to what a Windermere or Winter Garden subdivision "
         "looks like than to downtown Celebration's alley system. A turf ribbon down the center of one of "
         "those driveways behaves the same way it would anywhere else in Central Florida, without the alley "
         "cartway's added traffic load to plan around.</p>"),
        ("Stepping-stone paths fit the smaller Private Zones village lots have",
         "<p>A worn dirt track between a Cottage lot's back door and its Alley Yard gate is a common enough "
         "sight in Celebration's older villages, and a stepping-stone path with turf between the pavers "
         "replaces it without paving the whole strip. On a lot this size, the shallower footprint of stepping "
         "stones disturbs less of an already tight Private Zone than a continuous paver walkway would.</p>"),
    ],
    "scenario": (
        "Say you have a 25 ft alley apron",
        "<p>Say you have a 25 ft by 10 ft paver apron connecting a village lot's garage to the alley, with a "
        "narrow turf ribbon planned along one edge to soften the hardscape. Sizing that job means walking the "
        "apron first, not quoting from a per-square-foot chart, since the paver base has to carry regular "
        "vehicle and trash-service loads while the turf strip beside it needs a drainage path of its own, and "
        "the two crews have to work off one shared grade rather than two separate ones.</p>"
    ),
    "faqs": [
        faq("Does an alley apron need a sturdier build than a front driveway strip?",
            "Yes, generally. Regular vehicle and trash-pickup traffic along the alley cartway puts more load "
            "near the turf's edge than a purely decorative front-yard ribbon would ever see."),
        faq("Are Artisan Park driveways different from the rest of Celebration?",
            "Some are front-loaded rather than alley-loaded, closer to a standard Central Florida subdivision "
            "layout, which simplifies turf-and-paver planning since there's no alley cartway traffic to design "
            "around."),
    ],
    "sources": SRC,
}

LOCAL["repair"] = {
    "title": "Turf Repair in Celebration, FL: Alley Yards & Ponds",
    "meta": "Turf repair in Celebration, FL is quoted per visit, covering alley-yard edges worn by daily traffic and pond-backing lots near the golf course.",
    "h1": "Fixing turf on Celebration's alley yards and pond-backing lots",
    "lede": capsule(
        "A repair visit in Celebration gets priced after a walk of the yard, not from a flat square-foot "
        "rate, because what's actually wrong, a lifted seam, a settled corner, infill that's washed thin, "
        "changes the labor more than the size of the area does. Two things draw more repair calls here than "
        "the rest of the lot: the alley-facing edge, and turf old enough to predate the state's current "
        "infill rule."
    ),
    "sections": [
        ("Alley-yard edges take more day-to-day wear than a front lawn",
         "<p>An Alley Yard sees garbage trucks, delivery traffic and daily foot traffic along the cartway in a "
         "way a shallow front yard behind the Front Façade Zone never does, and turf installed along that edge "
         "can loosen at the border faster than the same product would in a quieter setting. A lifted alley-side "
         "edge is worth checking against the five-foot utility easement too, since older installs sometimes "
         "encroach on that easement without anyone noticing until a repair visit.</p>"),
        ("Pond-backing lots need the setback re-checked at every repair",
         "<p>An older turf install on a Manor or Estate lot backing a pond or the golf course sometimes "
         "predates the current version of the state's 10-foot waterbody setback, and a repair visit is a "
         "natural point to confirm the existing footprint still meets that distance rather than simply "
         "patching the same layout back into place. Wind and water exposure at an open pond edge also works "
         "at a seam or a nailed border harder over the years than a lawn set back from any water feature.</p>"),
        ("A repair is the point to swap out infill the state no longer allows on a lawn",
         "<p>Turf installed in Celebration before Rule 62-308.100 took effect on May 19, 2026 sometimes carries "
         "a crumb rubber infill that was ordinary practice at the time, and a repair visit that involves "
         "topping up or replacing infill is a natural point to change that out, since the rule now keeps "
         "rubber or any other synthetic infill to the footprint of playground equipment and limits a plain "
         "lawn to silica sand, zeolite or a coated sand product instead. Putting off that swap at a repair "
         "just means doing it again at the next one.</p>"),
    ],
    "scenario": (
        "Say you have a lifted corner in a 10-year-old alley yard",
        "<p>Say you have a turf strip along a village lot's alley yard, installed about ten years ago with a "
        "crumb rubber infill that was standard then, now lifting at one corner after last season's storms. "
        "Because the fix stays inside the same footprint as the original install, CROA generally treats it as "
        "maintenance rather than a new architectural change, so the visit itself doesn't need a fresh Design "
        "Guidelines submittal the way a resized or relocated strip would. While the crew is already at that "
        "corner, the crumb rubber washing out of it gets swapped for silica sand, since rubber infill on a "
        "plain lawn isn't what the state allows today.</p>"
    ),
    "faqs": [
        faq("Why does alley-yard turf need more repair than a front lawn in Celebration?",
            "Daily traffic along the alley cartway, garbage trucks, deliveries and foot traffic, wears at an "
            "edge harder over time than a shallow, quieter front yard ever experiences, which is why "
            "alley-side borders get checked first on a repair visit."),
        faq("Does a repair visit change what infill is used?",
            "It can. If the original install used crumb rubber, common before May 2026, a repair is a "
            "practical point to switch to silica sand, zeolite or coated sand, since the rule now keeps "
            "rubber infill to the footprint of playground equipment on a residential lot."),
        faq("Does repairing pond-lot turf change how close it sits to the water?",
            "Sometimes. An install older than Rule 62-308.100 can sit closer to a pond than a new project "
            "could today, so a repair is a fair point to re-measure the edge, with a seawall or bulkhead "
            "counting as the only exception to that 10-foot floor."),
    ],
    "sources": SRC,
}

LOCAL["cleaning"] = {
    "title": "Turf Cleaning & Maintenance in Celebration, FL",
    "meta": "Turf cleaning in Celebration, FL is quoted by yard size and visit, timed around CDD street-tree leaf drop and moisture near ponds and the golf course.",
    "h1": "Keeping Celebration turf clean, from shaded alleys to pond-adjacent lawns",
    "lede": capsule(
        "Pricing a cleaning visit in Celebration comes down to yard size and time since the last one, not a "
        "flat rate, since brushing infill upright, clearing debris and rinsing off haze take different time "
        "depending on recent use. Two things move that schedule more than size does: how much canopy from "
        "the CDD's street trees hangs over the yard, and how close the lot sits to a pond or the golf course."
    ),
    "sections": [
        ("An Alley Yard still has to look kept, even without irrigation running",
         "<p>CROA's own guideline holds the owner responsible for keeping the Alley Yard \"fully irrigated and "
         "maintained,\" language written before synthetic turf was a live option back there. A capped Alley "
         "Yard can't meet the irrigated half of that anymore, so the maintained half carries more weight: "
         "brushing the pile upright and clearing leaf litter before it flattens into the infill is what keeps "
         "a strip along the alley reading as kept, to a CROA inspection walk or a neighbor passing on the "
         "cartway.</p>"),
        ("Lower ground near a pond holds moisture longer between visits",
         "<p>A lawn on a Manor or Estate lot backing a pond or the golf course sits where Basinger soil's "
         "water table runs closer to the surface than it does on higher village ground, and that extra "
         "moisture under the base can leave infill damp well after a storm has passed elsewhere in town. "
         "Checking for standing water at the infill layer during a visit catches that early, before a slow-"
         "draining patch turns into a smell.</p>"),
        ("A small Private Zone concentrates wear a bigger yard would spread out",
         "<p>Because most of a Celebration lot's outdoor space sits inside a compact Private Zone rather than "
         "a sprawling half-acre yard, foot traffic, pet use and falling debris all land on the same few "
         "hundred square feet instead of spreading across an open lawn. A courtyard or alley-strip visit "
         "usually covers less ground than one at a larger suburban home, but the concentrated wear still "
         "calls for the same careful pass.</p>"),
    ],
    "scenario": (
        "Say you have a 250 sq ft Alley Yard strip going unbrushed",
        "<p>Say you have a 250 sq ft strip of turf along a village lot's Alley Yard, capped since it went in "
        "and now matting down at the high-traffic spot by the gate, with a neighbor's oak dropping enough "
        "litter to start working into the pile. Pricing that visit depends on how long it's been since the "
        "last brushing and rinse, not a flat per-square-foot figure, and the work does double duty: restoring "
        "the pile also keeps the strip reading as \"maintained\" the way CROA's own Alley Yard language still "
        "expects, even though nothing about it gets watered anymore.</p>"
    ),
    "faqs": [
        faq("Does an Alley Yard still need to look maintained once turf goes in?",
            "Yes, in CROA's own terms. The guideline requiring the Alley Yard to stay maintained predates "
            "synthetic turf, and with irrigation capped, brushing and clearing debris is what keeps that strip "
            "reading as kept rather than neglected."),
        faq("Does turf near a Celebration pond need cleaning more often than an inland lot?",
            "It can. Lots closer to a pond or the golf course sit nearer Basinger soil's seasonal high water "
            "table, and that extra ground moisture can call for a tighter schedule during the wettest "
            "months."),
    ],
    "sources": SRC,
}

LOCAL["replacement"] = {
    "title": "Turf Removal & Replacement in Celebration, FL",
    "meta": "Turf replacement in Celebration, FL is quoted per job, for lawns installed in the town's first villages that are nearing the end of a typical service life.",
    "h1": "Replacing worn turf in Celebration's original villages and newer sections",
    "lede": capsule(
        "Replacing worn-out turf in Celebration gets priced from what the tear-out finds, not a flat "
        "square-foot rate, since the base underneath and, on an older lawn, what infill comes out of it both "
        "weigh on labor more than area alone. The town's original villages go back to 1996, so a meaningful "
        "share of that turf now predates the state's infill rule and is old enough that replacement, not "
        "another repair, is the honest call."
    ),
    "sections": [
        ("Pre-2026 lawns sometimes carry an infill the state no longer allows",
         "<p>A lawn converted in one of Celebration's original villages before Rule 62-308.100 took effect on "
         "May 19, 2026 may have gone in with a rubber crumb infill, an ordinary choice at the time and now "
         "allowed only within the footprint of playground equipment. A full replacement is the point to "
         "correct that: pulling the old turf out takes the infill with it, and the new lawn goes back down "
         "with silica sand, zeolite or a coated sand product instead, while the base underneath gets rebuilt "
         "to the state's current washed, open-graded standard at the same time.</p>"),
        ("Re-checking the pond setback on an older golf-lot or waterfront replacement",
         "<p>An older turf install on a Manor or Estate lot backing a pond or the golf course can predate the "
         "state's current 10-foot waterbody setback, and a full replacement is the point to bring the layout "
         "in line with that distance instead of relaying the same footprint that was there before. A seawall "
         "or bulkhead already standing between the yard and the water is the one case where that distance "
         "doesn't move the new edge.</p>"),
        ("A like-for-like replacement clears CROA faster than a resized one",
         "<p>Because a full tear-out and relay counts as new construction under CROA's Design Guidelines, even "
         "a straightforward like-for-like replacement still goes to the Architectural Review Committee, unlike "
         "a small repair that stays inside an already-approved footprint. What changes is how quickly that "
         "submittal moves: reproducing the same shape, edge and lot line the earlier approval covered "
         "typically clears faster than a project that also grows the footprint toward the Front Façade Zone "
         "or the alley.</p>"),
    ],
    "scenario": (
        "Say you have a 2013-installed village front yard with rubber infill",
        "<p>Say you have a front lawn converted to turf in 2013 in one of Celebration's original villages, put "
        "in with a rubber crumb infill that was ordinary practice then, now matted near the walkway with a "
        "base that holds water after storms in a way it never used to. At roughly 13 years old the turf "
        "itself sits within a typical service life, but the infill doesn't belong on a plain lawn anymore "
        "under the state's rule, so a full replacement swaps it for silica sand or zeolite while the base "
        "gets rebuilt. Because the new lawn keeps the footprint CROA already approved, the Architectural "
        "Review Committee process for it tends to move faster than a first-time submittal would.</p>"
    ),
    "faqs": [
        faq("How do I know if Celebration turf needs replacing instead of repairing?",
            "It comes down to what a tear-out would find. Turf that's just matted on a base that still drains "
            "can often be repaired in place; a base that's crusted or holding water, or a rubber infill on a "
            "plain lawn, points toward a full replacement instead."),
        faq("Does replacing older turf near a Celebration pond change the setback?",
            "It can. An install that predates the state's current 10-foot setback gets brought in line with "
            "it during a full replacement, with a seawall or bulkhead as the one exception that keeps the "
            "edge where it already sits."),
        faq("Does a like-for-like turf replacement still need CROA approval?",
            "Yes, since a full tear-out and relay counts as new construction under the Design Guidelines. It "
            "typically clears the Architectural Review Committee faster than a first-time submittal, though, "
            "when the new lawn reproduces the shape and edge the earlier approval covered."),
    ],
    "sources": SRC,
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
