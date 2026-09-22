# -*- coding: utf-8 -*-
"""Haines City, Polk County (tier 2). The city runs its own Development Services Building
Division and its own water utility, separate from Polk County's; we have not read Haines City's
own municipal code line by line, so the permit section says that honestly and points to our
Polk County (unincorporated) permit page for the state-floor baseline instead. New research for
this module, checked September 2026: Haines City's Building Division and Water Restrictions
pages, the Southwest Florida Water Management District's Modified Phase III order, Census
population for 2010/2020 and the mid-2020s, Southern Dunes and Lake Eva, the USDA Candler series
and the Lake Wales Ridge, and Haines City's citrus-belt history. Facts and county-level sourcing
for the state rule, HOA statute and general Polk soil/water picture are reused from
site/content/c_permits.py and c_counties.py (their facts and URLs, not their sentences)."""
from _helpers import page, capsule, sec, table, faq, a, svc, city, county, post, src, ext, price
from _cityservice import cityservice_pages

SLUG = "haines-city"

SRC = [
    "dep-rule", "fs125572", "fs7203045", "usda-wss",
    ("City of Haines City — Building Division", "https://hainescity.com/156/Building-Division"),
    ("City of Haines City — Water Restrictions", "https://hainescity.com/230/Water-Restrictions"),
    ("Southwest Florida Water Management District — district water shortage restrictions", "https://www.swfwmd.state.fl.us/business/epermitting/district-water-restrictions"),
    ("City of Haines City — Lake Eva Community Park", "https://hainescity.com/454/Lake-Eva-Community-Park"),
    ("USDA NRCS — official series description, Candler series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/C/CANDLER.html"),
    ("Wikipedia — Lake Wales Ridge", "https://en.wikipedia.org/wiki/Lake_Wales_Ridge"),
    ("Census Reporter — Haines City, FL profile", "https://censusreporter.org/profiles/16000US1228400-haines-city-fl/"),
    ("Southern Dunes HOA — community site", "http://www.southernduneshoa.com/home.html"),
    ("The Clio — Haines City Citrus Growers", "https://theclio.com/entry/50834"),
]

BUILDING_DIV = ("City of Haines City — Building Division", "https://hainescity.com/156/Building-Division")
WATER_PAGE = ("City of Haines City — Water Restrictions", "https://hainescity.com/230/Water-Restrictions")
CANDLER = ("USDA NRCS — official series description, Candler series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/C/CANDLER.html")
RIDGE = ("Wikipedia — Lake Wales Ridge", "https://en.wikipedia.org/wiki/Lake_Wales_Ridge")
CENSUS = ("Census Reporter — Haines City, FL profile", "https://censusreporter.org/profiles/16000US1228400-haines-city-fl/")
LAKE_EVA = ("City of Haines City — Lake Eva Community Park", "https://hainescity.com/454/Lake-Eva-Community-Park")
SOUTHERN_DUNES = ("Southern Dunes HOA — community site", "http://www.southernduneshoa.com/home.html")
CITRUS = ("The Clio — Haines City Citrus Growers", "https://theclio.com/entry/50834")


# ============================================================== hub
HUB = page(
    "/areas/haines-city/", "city",
    "Artificial Turf in Haines City, FL (2026 Guide)",
    "Synthetic turf installs, permits, SWFWMD watering rules and Lake Wales Ridge soil facts for Haines City, FL, about 18 miles from Kissimmee. Checked September 2026.",
    "Artificial turf across Haines City",
    capsule(f"Kissimmee Artificial Turf serves Haines City, about 18 miles up US-27 from our home base, where a residential lawn conversion installs for {price('residential')} a square foot in 2026, no different from anywhere else we work. The city sits on the Lake Wales Ridge and has nearly tripled in population since the 2010 census, with much of that new construction going up on land that grew citrus within living memory."),
    "".join([
        sec("Why a Haines City yard isn't built like a Kissimmee one",
            f"<p>{ext(RIDGE[1], 'The Lake Wales Ridge')} runs the length of Central Florida, and Haines City sits on its northern hump, which puts the city on drier, faster-draining ground than the flatwoods towns closer to Kissimmee. Where a Kissimmee yard usually fights a shallow water table, a Haines City yard is more likely to fight loose sand that won't hold a level, compacted shape on its own, especially on a lot cut from what used to be a grove row. The 2020 census counted 26,669 residents here, up from 20,535 in 2010, and the city had grown to roughly 34,000 by the mid-2020s, one of the faster climbs anywhere in Polk County ({src('usda-wss', 'confirmed against USDA soil mapping')}; {ext(CENSUS[1], 'Census Reporter’s Haines City profile')}). A good share of that new rooftop count sits on former citrus ground.</p>"),
        sec("Who actually reviews a turf permit here",
            f"<p>Haines City runs its own permitting, separate from the county. The Building Division, part of the city's Development Services Department at 620 E. Main Street, takes calls at 863-421-3600 and posts applications through its {ext('https://haines.portal.iworq.net/portalhome/haines', 'online Contractor Portal')} ({ext(BUILDING_DIV[1], BUILDING_DIV[0])}). That's a different office, with a different code, from Polk County's Building Division, which only reaches land outside the city limits.</p>"
                + f"<p>Whether Haines City's own ordinances say anything about synthetic turf is a question we can't answer with confidence yet. Our clause-by-clause search covered the county's unincorporated Land Development Code, not the city's separate book of rules, so the honest answer is that we don't know. {a('/laws/permits/polk-county/', 'Our Polk County permit page')} is offered as a baseline instead: {a('/laws/florida-hb-683/', 'HB 683 and Rule 62-308.100')} set the same statewide floor inside Haines City that they set everywhere else, whatever the city's own code turns out to say. An architectural review, where {a('/laws/hoa-rules/', 'a separate state statute limits what an association can restrict')}, is its own step on top of either permitting path.</p>"),
        sec("Haines City's own water, and one day a week",
            f"<p>Haines City bills its own water instead of buying through Polk County Utilities, and that utility answers to the Southwest Florida Water Management District, not the district that covers Kissimmee and most of Osceola County ({ext(WATER_PAGE[1], 'the city’s water restrictions page')}). Under a Modified Phase III shortage order in force since April 2026, a resident here gets exactly one lawn-watering slot a week, chosen by the street address's last digit, inside a roughly 3.5-hour window that falls either just after midnight or just after 8 p.m. ({ext(SRC[6][1], 'SWFWMD’s district restrictions page')}). None of that touches a capped synthetic lawn, since the state's turf rule already rules out an in-ground system on synthetic turf no matter what the shortage order allows for the grass next to it.</p>"),
        table("Haines City yard types and what we do differently",
              ["Where in Haines City", "What the lot usually has", "What changes in the build"],
              [["Southern Dunes and other US-27 golf communities", "Gated entry, an ARC review, mowed golf-course frontage", "A design-review submittal with a sample and spec sheet before the crew shows up"],
               ["Vacation-rental homes off US-27 and I-4", "New construction, a small yard, a new set of guests most weeks", "Heavier face weight and a rinse plan built for turnover, not for one owner's routine"],
               ["In-town lots near Lake Eva", "Older homes, some inside the ten-foot waterbody line", "The setback staked before we ever order material"],
               ["New subdivisions on former grove rows", "Fill left by grading equipment rather than native ridge sand", "A fuller base depth wherever that fill drains worse than the sand it replaced"],
               ["Oak-shaded streets near the old downtown", "Established canopy over narrow, older lots", "A drip-line check before any excavation starts"]],
              "Checked against Haines City's own building, water and parks pages, plus USDA soil mapping, September 2026."),
        sec("Lake Eva, the ridge lakes and the ten-foot line",
            f"<p>Lake Eva, a 151-acre lake at the center of the city's namesake park, is one of several ridge lakes Haines City is built around, alongside the smaller ponds tucked into subdivisions on former grove land ({ext(LAKE_EVA[1], 'the city’s Lake Eva park page')}). Florida's turf rule keeps synthetic grass at least 10 feet back from any of them, natural or built, unless a seawall or bulkhead already separates the yard from the water, and that line gets staked before turf is ever ordered for a lakefront lot. A ridge lake tends to sit low against the surrounding sand hills rather than the other way around, so a yard that reads flat from the street can still carry enough slope toward the water to need its own drainage plan on top of the setback itself.</p>"),
        sec("Building a base on Lake Wales Ridge sand",
            f"<p>The Candler series, the sand that defines most of the ridge, is excessively drained with very rapid to rapid permeability, built from thick windblown and marine deposits, and it carries real slope: 0 to 12 percent through most of Haines City, steeper on the more cut-up ground near old grove edges ({ext(CANDLER[1], 'USDA’s official series description')}). That's close to the opposite problem from a flatwoods lawn in Kissimmee. A Haines City base usually isn't fighting a high water table; it's fighting sand loose enough to shift under a plate compactor before the layer above it settles. On a lot regraded for a subdivision built into former citrus ground, we also check whether the fill a builder left behind is native ridge sand or something trucked in and compacted differently, since the two drain at different rates under the same two lifts of washed rock ({ext(CITRUS[1], 'Haines City’s citrus-belt history')}).</p>"),
        "<!--AUTO:city-services-->",
    ]),
    faqs=[
        faq("Ridge sand, a fast-growing city: what should the best artificial turf installer near you already know about Haines City?",
            "Ask three things before signing: how the base handles ridge sand instead of flatwoods soil, whether the quote lists face weight and infill by name, and whether the crew already knows Haines City runs its own water utility separate from the county. A written answer to all three beats a sales pitch."),
        faq("Does Haines City require a separate permit just to cap irrigation heads under new turf?",
            "We couldn't find a published answer either way in the city's code, which is a plumbing question as much as a landscaping one. The Building Division at 863-421-3600 is the office to ask before a crew caps anything under a Haines City yard."),
        faq("Does a Southern Dunes HOA approval replace a city permit, or the other way around?",
            "Neither replaces the other. A gated community's design review and Haines City's own building permit are two separate approvals, and a turf project inside Southern Dunes or a similar community can need one, both or neither depending on the scope of the work."),
        faq("Is every Haines City lake close enough to trigger the ten-foot setback?",
            "Only a yard that actually borders a pond, lake or canal, not every yard in a lake-named subdivision. A parcel that doesn't touch water directly has no setback to plan around, though a ridge lake's low-lying edge is worth checking even on a lot that looks flat."),
        faq("Why does a newer Haines City subdivision sometimes need a deeper base than an older one?",
            "Because a lot regraded during construction on former grove land can carry compacted fill instead of the ridge's naturally loose sand, and that fill doesn't always drain the way undisturbed Candler sand does. We check which one a specific lot has before setting base depth."),
    ],
    sources=SRC, city=SLUG, crumbs=[("Service areas", "/areas/")], crumb="Haines City",
    related=[("/areas/polk-county/", "Artificial turf in Polk County"), ("/laws/permits/polk-county/", "Polk County permit rules for turf"),
             ("/areas/davenport/", "Turf in Davenport"), ("/areas/winter-haven/", "Turf in Winter Haven"),
             ("/artificial-turf-cost/", "Full turf cost guide")],
)


# ============================================================== LOCAL
LOCAL = {
    "residential": {
        "title": "Artificial Grass Installation in Haines City's Ridge Yards",
        "meta": "Artificial grass installation in Haines City, FL: ridge-sand base work, the city's own Building Division and 2026 market pricing. Checked September 2026.",
        "h1": "What a Haines City lawn conversion actually involves",
        "lede": capsule(f"A Haines City lawn conversion prices at {price('residential')} a square foot, the standard 2026 Central Florida figure we quote anywhere in our territory. What actually changes here is the ground underneath: Haines City rides the Lake Wales Ridge, so a base plan built for a flatwoods yard in Kissimmee doesn't automatically carry over to loose ridge sand."),
        "sections": [
            ("Starting with the city's own Building Division, not the county's",
             f"<p>A residential lawn swap in Haines City answers to the city's Development Services Building Division, not Polk County's Building Division, and the two run separate applications under separate codes. Nobody on our end has combed Haines City's municipal code page by page for a turf clause, so we're not the source for whether one exists there; a homeowner planning a full front-and-back conversion gets a faster, more reliable answer from a direct call to 863-421-3600 than from guessing at what the city's silence might mean. {a('/laws/permits/polk-county/', 'Our Polk County permit page')} walks through what we could confirm about the county's own code, which is the closest published reference point until Haines City's own rule, if one exists, turns up.</p>"),
            ("Grading a lawn out of an old citrus row",
             "<p>A fair share of Haines City's residential lots were graded out of grove land within the last two decades, and that history shows up under the sod more than most homeowners expect. A row that once grew citrus was often bedded up slightly above grade for drainage, and a builder leveling that same ground for a subdivision can leave compacted fill sitting differently than the loose native ridge sand around it. Before setting base depth on a residential job here, we check whether a specific yard is graded fill or undisturbed ridge sand, since a base built for one drains differently than the same depth built for the other, even on two lots a block apart.</p>"),
            ("A city that grew by roughly a third since 2020",
             "<p>Haines City's population climbed from 26,669 at the 2020 census toward roughly 34,000 by the mid-2020s, and that growth shows up as a real mix of lot ages within a few miles of each other. A downtown lot near the original grid can carry a St. Augustine lawn on undisturbed native sand that's never been touched by heavy equipment, while a subdivision finished five years ago sits on regraded ground that settles on its own separate timeline. Both convert to turf the same way in the end, but the base crew treats the two differently going in, not after a problem shows up.</p>"),
        ],
        "scenario": ("Pricing a 1,100 sq ft backyard on a former grove lot",
                     f"<p>Say you have a 1,100 sq ft backyard behind a home built around 2016 on what county records still list as former grove acreage off the US-27 corridor. At the full {price('residential')} per square foot range, that yard prices between $8,800 and $19,800 depending on access, shape and how much the compacted fill under it changes the base plan; most jobs like it land inside the {price('residential', True)} typical band, or $11,000 to $17,600. A flat, rectangular backyard with easy truck access and fill that already drains reasonably well tends to land toward the lower end; a yard with curves around a pool cage, tight side-gate access, or fill that needs the fuller base depth pushes it higher. The number doesn't move because of the ZIP code or how new the subdivision is, only because of what the crew actually finds once digging starts.</p>"),
        "faqs": [
            faq("Does a newer Haines City subdivision need less prep work than an older lot?",
                "Not necessarily. A newer lot often has fill soil left by construction grading instead of undisturbed native sand, and fill can drain worse than the ridge sand it replaced, so a newer address isn't automatically the easier job."),
            faq("Is St. Augustine sod common on Haines City lots before a turf conversion?",
                "Yes, on most of the older, in-town lots we see. A yard that's carried St. Augustine for years usually has a thicker root mat to strip than a builder-sodded new-construction lawn does, which is one more variable in how long removal takes."),
        ],
        "sources": SRC,
    },
    "pet": {
        "title": "Pet Turf & Dog Runs in Haines City, FL",
        "meta": "Pet turf and dog run installation in Haines City, FL: gated-community rules, ridge-sand drainage and 2026 pricing for odor-control infill. Checked September 2026.",
        "h1": "Dog runs for Haines City's gated and older yards alike",
        "lede": capsule(f"A Haines City dog run installs for {price('pet')} a square foot, with most jobs settling into the {price('pet', True)} band once odor-control infill is picked out. It isn't watered on the city's one-day-a-week schedule at all; it's rinsed by hose, which matters more in a gated community where a sprinkler zone can't just be turned back on for a patch of grass a dog has already worn out."),
        "sections": [
            ("A dog run doesn't care what day the city assigns for watering",
             "<p>A Southwest Florida Water Management District shortage order has capped Haines City residents at a single sprinkler slot a week since April 2026, picked by the street address. None of that governs a pet run, though, because a synthetic run was never going anywhere near a sprinkler zone to begin with: it gets a hose rinse whenever a dog and the Florida heat actually call for one, which in July can mean daily and in January can mean hardly at all. Once the run is in, a Haines City pet owner can stop tracking which day the city's shortage order allows for the rest of the yard.</p>"),
            ("Fenced runs in Southern Dunes and other gated communities",
             "<p>Southern Dunes and the handful of other gated, golf-adjacent communities along the US-27 corridor run their own design review for anything visible from a shared street or a fairway, and a fenced dog run tucked behind a house is usually the easiest version of that submittal to get through, since it sits behind a fence line most reviewers never have to weigh against the neighborhood's front-yard look. We don't have a published design document from any specific Haines City association naming synthetic turf directly, so we describe the review step itself rather than promise a specific outcome: a sample, a spec sheet and a site sketch submitted ahead of the crew's arrival is the safest way to handle it.</p>"),
            ("Why ridge sand handles a dog run differently than flatwoods soil",
             f"<p>The same Candler sand that defines most of Haines City drains rapidly on its own, which sounds like an advantage for a pet run until the crew is trying to compact a stable base on ground that shifts before a plate compactor finishes a pass. A flatwoods pet run in Kissimmee is usually built to get water away from a slow-draining base; a Haines City pet run is more often built to keep loose ridge sand from settling unevenly under a base that otherwise drains fine on its own. Either way, the backing under a dog run stays fully permeable, and the fabric layer a residential lawn sometimes gets left out entirely, since it would only hold urine right where the dog stands instead of passing it down into the rock.</p>"),
        ],
        "scenario": ("Sizing a run behind a gated-community townhome",
                     f"<p>Say you have a 260 sq ft side-yard run behind a townhome inside one of the US-27 golf communities, fenced on three sides with the house forming the fourth. At the full {price('pet')} range, that run prices between $2,600 and $4,680. Odor-control infill and a fully permeable backing tend to push a job like this toward {price('pet', True)}, or $3,120 to $4,160, rather than the bottom of the published range. A narrow side-yard footprint like this one usually means wheelbarrow access instead of equipment driving straight in, which is the kind of access detail that pushes a small job toward the upper half of its range regardless of the neighborhood it sits in.</p>"),
        "faqs": [
            faq("Do I need the association's sign-off before installing a dog run in a gated Haines City community?",
                "Likely yes, though the exact process depends on the specific association. A fenced run tucked behind the house is usually a straightforward submittal, but we'd rather a homeowner confirm with their own HOA or management company than assume based on what another Haines City community requires."),
            faq("Does capping a sprinkler zone for a pet run need its own permit in Haines City?",
                "Possibly, since that's a plumbing question the city's Building Division would need to answer for a specific address. It's worth a call to 863-421-3600 alongside any other permit question for the same job."),
            faq("Why skip the weed barrier under a Haines City pet run when it's standard on a regular lawn?",
                "A layer of fabric there would hold liquid right at the surface rather than letting it pass down into the rock, which defeats the entire purpose of grading a run for fast drainage in the first place. That holds whether the ground below is flatwoods soil or Candler ridge sand."),
        ],
        "sources": SRC,
    },
    "putting": {
        "title": "Backyard Putting Greens in Haines City, FL",
        "meta": "Backyard putting green installation in Haines City, FL, near Southern Dunes and other US-27 golf communities. Ridge-sand base notes and 2026 pricing.",
        "h1": "A practice green built for Haines City's golf-course lots",
        "lede": capsule(f"Backyard putting greens in Haines City run {price('putting')} per square foot as of September 2026, typically {price('putting', True)}. A yard backing onto a course at Southern Dunes gives a green a real fairway view, but the contouring and the base underneath it come from a built-up aggregate pad, not from shaping the loose ridge sand already on the lot."),
        "sections": [
            ("Building a green where the fairway is already the view",
             "<p>A backyard that already backs onto a Southern Dunes fairway doesn't need the green to fake a golf setting; it needs the green to look like it belongs next to a real one, which raises the bar on contouring and edge detail more than it would on a lot with no course view at all. A community like this typically runs its own architectural review for anything visible from the course or a shared street, and a putting green submittal usually goes in alongside the same paperwork a pool cage or a fence would need, a sample, a sketch of the contours and a spec sheet, rather than a separate process of its own.</p>"),
            ("Why ridge sand isn't the base a green gets built on",
             f"<p>Candler sand drains almost as fast as the turf that eventually sits on top of it, which is the opposite of what a putting green's contours need to hold their shape through a season of rain. Unlike a residential lawn, which can be built directly over a compacted layer of that same native sand, a green's mounds and breaks are shaped in a stabilized aggregate base engineered to keep its form, then capped with a pad and a short, dense pile suited to true ball roll. The ridge's fast-draining ground works in the green's favor once it's built, since water clears the surrounding lawn quickly, but it isn't the material the contours themselves are built from.</p>"),
            ("A green as a rental amenity along the US-27 corridor",
             "<p>Vacation-rental owners along US-27 increasingly list a backyard putting green as a booking amenity alongside a pool, since a green photographs well and gives a group of golfing guests something to do between tee times at a nearby course. That use changes the spec more than the neighborhood does: a rental green sees more different feet and more inconsistent care between bookings than a homeowner's private green ever would, which argues for a denser pile and a slightly larger fringe collar than the tightest, most tournament-accurate build a private owner might choose for a green nobody else ever touches.</p>"),
        ],
        "scenario": ("Sizing a two-hole green behind a course-view lot",
                     f"<p>Say you have a 480 sq ft two-hole green planned for a backyard that backs directly onto a Southern Dunes fairway, with a fringe collar built into that same footprint. At the full {price('putting')} range, that green prices between $6,720 and $14,400; most jobs its size land in the {price('putting', True)} typical band, $8,640 to $12,000, since contouring, a built-up aggregate base and two cups push the price above a flat single-pad green of the same size. A course-view lot doesn't change that math on its own, but the architectural review it usually requires can add a few weeks to scheduling before the crew ever breaks ground.</p>"),
        "faqs": [
            faq("Does a green count as impervious surface under a Haines City review, the way a patio might?",
                "We haven't found a published answer specific to Haines City's own code. A compliant system sits on a permeable backing over a pervious, graded base under the state's May 2026 turf standard, which is the number to raise if a reviewer's older worksheet assumes otherwise."),
            faq("How do you find the best putting green installer near you in Haines City if you live on a golf lot?",
                "Ask specifically how they'd shape contours next to a real fairway view, not just whether they've built a green before. A contractor who talks through the aggregate base and the architectural-review paperwork unprompted has clearly built one near a course before."),
        ],
        "sources": SRC,
    },
    "playground": {
        "title": "Playground Turf in Haines City, FL",
        "meta": "Playground turf installation in Haines City, FL, for backyards near Lake Eva and the city's newer subdivisions. Shock pad and infill notes, 2026 pricing.",
        "h1": "Play-area turf for Haines City's growing family subdivisions",
        "lede": capsule(f"A backyard play area in Haines City installs for {price('playground')} a square foot, with a typical small residential build settling into {price('playground', True)}. Lake Eva Community Park is the city's own example of a cushioned, shaded play surface, and a private version at home answers to the same shock-pad math, sized to whatever equipment sits on top of it."),
        "sections": [
            ("What Lake Eva's own play areas set as the local standard",
             "<p>Lake Eva Community Park, built around the 151-acre lake at the city's center, gives Haines City families a public reference point for what a well-built play surface looks like: several separate play areas sized to different ages, shaded seating nearby, and a surface that drains fast enough to be usable again shortly after a summer storm. A private backyard version borrows that same logic rather than the same materials, sizing a shock pad's thickness to the specific equipment going on top of it instead of the taller commercial-grade structures a city park installs.</p>"),
            ("A city adding young families faster than most of the county",
             "<p>Haines City's population climbed from 20,535 in 2010 to roughly 34,000 by the mid-2020s, and a meaningful share of that growth is families moving into newer subdivisions built where citrus groves used to stand. A play area in one of those newer yards usually sits on regraded fill rather than undisturbed ridge sand, which changes how the base under a shock pad gets built more than it changes the pad itself: fill that drains a little slower than native Candler sand argues for the fuller end of the base depth range before the pad and turf go down on top of it.</p>"),
            ("Keeping play turf out from under an old downtown oak",
             "<p>Haines City's older, in-town streets carry real canopy, oaks that have been growing since well before the current subdivisions existed, and a backyard play area on one of those lots has to plan around a drip line the way a newer, treeless lot never has to. The state's turf rule bars installing synthetic grass inside a live oak's drip line, on the property it sits on or the one next door, unless a certified arborist signs off that the work won't cause harm, so mapping where branches actually end matters before a shock pad's footprint gets drawn on paper.</p>"),
        ],
        "scenario": ("Sizing a shaded play area on an older in-town lot",
                     f"<p>Say you have a 300 sq ft play area planned for a backyard on one of Haines City's older streets, most of it inside the shade of a mature oak but outside its actual drip line once branches are measured. At the full {price('playground')} range, that area prices between $3,000 and $7,500; figure {price('playground', True)}, or $3,600 to $5,700, for the typical small residential job, with pad thickness keyed to whichever swing set or climbing structure ends up on top of it. Staying clear of the drip line on a lot this size sometimes means shrinking the footprint slightly from what was first sketched, which is worth settling before ordering material rather than after.</p>"),
        "faqs": [
            faq("Does Lake Eva Community Park use the same turf products a backyard install would?",
                "We don't know what the city's own park uses and won't guess. What we can say is that a private backyard play area is built around the specific equipment going on it, with a shock pad sized to that equipment's fall height rather than to a public park's larger-scale structures."),
            faq("How close can playground turf go to an old oak on a Haines City lot?",
                "No closer than the tree's drip line, measured from where branches actually end rather than the trunk, unless a certified arborist certifies the work won't harm the tree. That rule applies the same way on an older in-town lot as it does on a newer subdivision lot with younger trees."),
        ],
        "sources": SRC,
    },
    "pool": {
        "title": "Pool & Lanai Turf in Haines City, FL",
        "meta": "Turf around a Haines City pool cage or lanai: ridge-lot grading, ten-foot setback near ridge lakes, and 2026 installed pricing. Checked September 2026.",
        "h1": "Turf around a Haines City pool cage",
        "lede": capsule(f"There's no separate price key for pool turf: a Haines City lanai job falls under the residential range, {price('residential')} a square foot, generally toward the top half once glue-down edges and drainage are factored in. A screen enclosure built on regraded ridge ground needs a drainage underlay where turf meets the deck, and a lot near one of the city's ridge lakes may also sit inside the state's ten-foot waterbody line."),
        "sections": [
            ("A pool cage backing onto a ridge lake",
             "<p>A pool enclosure on a Haines City lot that backs onto Lake Eva or one of the smaller ridge lakes nearby sits closer to the state's ten-foot waterbody setback than most homeowners expect, since a screened lanai's outer edge can run surprisingly close to a property's water frontage on a narrower ridge lot. Turf inside the enclosure itself is unaffected by that setback, which only governs the strip of yard actually within ten feet of the water; it's the open ground between the cage and the lake, if there is any left to turf, that has to respect the line unless a seawall already separates the two.</p>"),
            ("Grading a pool deck on sloped ridge ground",
             "<p>A pool built on a lot regraded from former grove land doesn't always sit on perfectly level ridge sand the way an older, undisturbed lot might, and a deck feathered against a slight grade change needs the turf's base built to match that same taper rather than assuming a flat plane. Right where the lawn stops and the pool deck's slab starts, glue takes over from nails, simply because there's no dirt left at that exact line for a fastener to bite into once the concrete begins.</p>"),
            ("Why a newer enclosure lot needs a different underlay plan",
             "<p>Haines City's newer pool-home subdivisions, many of them built where citrus rows used to run, sit on fill rather than native ridge sand inside the screen enclosure, and that fill can hold water against the concrete deck differently than undisturbed Candler sand would. A drainage underlay beneath the turf gives that trapped moisture somewhere to go besides sitting against the slab, which matters more on a recently graded lot than on an older enclosure built directly over sand that's been settling for decades already.</p>"),
        ],
        "scenario": ("Turfing a narrow strip inside a screen enclosure",
                     f"<p>Picture a 210 sq ft ribbon of grass wrapping the inside of a screen enclosure on a lot backing onto one of Haines City's smaller ridge lakes, with the deck itself taking up most of the remaining pad. Multiplying that footprint by the residential range, {price('residential')} a square foot, puts the job somewhere between $1,680 and $3,780, though a cramped enclosure job like this one usually settles closer to $3,360 than to the bottom of that span, since a glue-down deck edge and a drainage underlay both add labor a wide-open lawn never needs. The lake behind the cage only changes that math if turf is also going into the open yard beyond the screen, inside the ten-foot line.</p>"),
        "faqs": [
            faq("Does the ten-foot waterbody setback apply inside a screened pool cage?",
                "No. The setback governs open yard within ten feet of a pond, lake or canal; turf inside an already-screened enclosure isn't the part of the property the rule is written for, since the enclosure itself isn't waterfront ground being newly turfed."),
            faq("Why does turf near a Haines City pool sometimes cost more per square foot than a plain backyard?",
                "Small, enclosed areas take proportionally more labor for the same crew and equipment mobilization, and a glue-down edge against a concrete deck plus a drainage underlay both add steps a flat, open backyard skips entirely."),
        ],
        "sources": SRC,
    },
    "repair": {
        "title": "Artificial Turf Repair in Haines City, FL",
        "meta": "Artificial turf repair in Haines City, FL: seam, edge and drainage fixes for rental-home and ridge-lot lawns. Priced after photos or a site visit.",
        "h1": "Fixing turf problems on a Haines City lawn",
        "lede": capsule("Turf repair in Haines City is priced after photos or a site visit, since a lifted seam, a worn patch and a settled base all call for different fixes and different materials. What we see most here traces back to one of two things: a vacation-rental lawn worn hard by constant guest turnover, or an older installation built before the ridge's loose sand got the base depth it actually needed."),
        "sections": [
            ("What constant guest turnover does to a rental lawn's seams",
             "<p>A vacation-rental yard along the US-27 corridor sees a different group of guests most weeks, rolling suitcases across the same strip of turf between a driveway and a front door far more often than a family home's lawn ever gets crossed. Repeated traffic concentrated on one narrow path wears differently than the same total foot traffic spread evenly across a whole yard, and a seam or edge sitting directly on that path is usually the first thing to show it, well before the rest of the lawn looks anything but new.</p>"),
            ("Telling an older Haines City lawn's problem from a newer one's",
             "<p>A lawn installed before Haines City's building stock grew as fast as it has since 2020 sometimes predates the base standard a crew would use today, and a recurring low spot on one of those older installs often traces back to a base that was never built to the current two-lift, washed-rock depth in the first place. A newer lawn's problems tend to run the other way: a base built correctly but over compacted grove fill that settled unevenly in its first year or two, which looks similar on the surface but calls for a different fix underneath it.</p>"),
            ("When the setback strip near a ridge lake is the actual cause",
             "<p>Ground within ten feet of one of Haines City's ridge lakes can shift a little faster than the rest of a yard, particularly where there's no seawall absorbing wave action or holding a bank in place through a wet season. A repair that keeps reopening in roughly the same spot along that strip, rather than somewhere different each time, often points to the location itself rather than a flaw in the original installation, since that specific edge deals with water-driven movement the rest of a lawn's base never has to handle.</p>"),
        ],
        "scenario": ("What a small worn patch costs against a full section replacement",
                     f"<p>Say you have a 90 sq ft worn patch along a rental home's main walkway, the turf flattened and the backing starting to show through after two seasons of steady guest traffic. A full replacement of that same 90 sq ft at the residential range, {price('residential')} per square foot, would run $720 to $1,620 before any labor premium for matching the surrounding lawn's grain and infill; a targeted repair typically prices well under that full-replacement figure because it reuses the existing base rather than rebuilding it, though the exact number depends on what a site visit or a set of clear photos actually shows once we look at it.</p>"),
        "faqs": [
            faq("Can a turf repair be quoted from photos alone for a Haines City vacation rental?",
                "Often, yes, for a straightforward worn patch or a lifted seam where the cause is visible in a clear photo. A recurring problem, or one near a ridge lake's setback strip, usually needs an in-person look before we can say what's actually causing it."),
            faq("Is a repaired section of turf noticeably different in color from the rest of a Haines City lawn?",
                "Sometimes, since sun exposure fades installed turf faster than a stored patch of the same product, and Haines City's mostly open, ridge-top lots see more direct sun than a shaded flatwoods yard would. Scheduling a repair soon after a problem shows up keeps that color gap smaller than waiting another season or two would."),
        ],
        "sources": SRC,
    },
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
