# -*- coding: utf-8 -*-
"""Auburndale, FL (tier 2). Researched September 2026: City of Auburndale Construction Services
(permits) and Public Utilities (water/irrigation) sites, the Southwest Florida Water Management
District's 2026 Modified Phase III order, Polk County Water Atlas lake records, USDA NRCS official
series descriptions for the Candler and Basinger soils, Wikipedia entries for Auburndale city hall
and the Auburndale TECO Trail (verified against multiple independent trail sources), and Census/Data
USA population figures. No city-specific synthetic-turf ordinance was found, so permit questions route
to the Polk County page."""
from _helpers import page, capsule, sec, table, faq, a, svc, city, county, cs, post, src, ext, price
from _cityservice import cityservice_pages

SLUG = "auburndale"

SRC = [
    "dep-rule", "fs125572",
    ("City of Auburndale — Construction Services (building permits)", "https://auburndalefl.com/construction-services/"),
    ("City of Auburndale — Public Utilities", "https://auburndalefl.com/utilities/"),
    ("Southwest Florida Water Management District — District extends Modified Phase III water shortage (2026)", "https://www.swfwmd.state.fl.us/the-newsroom/2026/district-extends-modified-phase-iii-water-shortage"),
    ("Polk County Property Appraiser — parcel search", "https://www.polkflpa.gov/"),
    ("Polk County — Building Division permitting", "https://www.polkfl.gov/services/building/permitting/"),
    ("USDA NRCS — official series description, Candler series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/C/CANDLER.html"),
    ("USDA NRCS — official series description, Basinger series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/B/BASINGER.html"),
    ("U.S. Census Bureau QuickFacts — Auburndale city, Florida", "https://www.census.gov/quickfacts/fact/table/auburndalecityflorida/PST045224"),
    ("Data USA — Auburndale, FL", "https://datausa.io/profile/geo/auburndale-fl"),
    ("Wikipedia — Auburndale City Hall (NRHP-listed, 1927)", "https://en.wikipedia.org/wiki/Auburndale_City_Hall"),
    ("Wikipedia — Auburndale, Florida", "https://en.wikipedia.org/wiki/Auburndale,_Florida"),
    ("Wikipedia — Auburndale TECO Trail", "https://en.wikipedia.org/wiki/Auburndale_TECO_Trail"),
    ("Polk County Water Atlas (USF) — Lake Ariana", "https://polk.wateratlas.usf.edu/waterbodies/lakes/160450/lake-ariana"),
    ("Polk County Water Atlas (USF) — Lake Juliana", "https://polk.wateratlas.usf.edu/waterbodies/lakes/160281/lake-juliana"),
    ("City of Auburndale — Lake Ariana Park", "https://auburndalefl.com/lake-ariana-park-2/"),
]

PERMITS_PAGE = ("/laws/permits/polk-county/", "Polk County permit rules for turf")
HOA_PAGE = ("/laws/hoa-rules/", "what a Florida HOA can and can't restrict")
HB683_PAGE = ("/laws/florida-hb-683/", "HB 683 and DEP Rule 62-308.100")

# ============================================================== hub
HUB = page(
    "/areas/auburndale/", "city",
    "Artificial Turf Installation in Auburndale, FL",
    "Artificial turf installers covering Auburndale, FL, about 28 miles from Kissimmee: Polk permit rules, SWFWMD watering order and lake setbacks, this September.",
    "Turf built for Auburndale's ridge sand and lake edges",
    capsule(f"We install, repair and clean artificial turf around Auburndale's dozen-plus lakes, about 28 miles from Kissimmee. Installed synthetic grass runs {price('residential')} a square foot, the same Central Florida range quoted anywhere in Polk County this fall. Ground here splits in two: excessively drained ridge sand on one side of town, slower and wetter soil toward the lake edges on the other, and that split changes how a crew builds the base."),
    "".join([
        sec("Why Auburndale isn't one soil type to build on",
            f"<p>Toward Lake Myrtle and the ridge running north of downtown, the native ground is {ext('https://soilseries.sc.egov.usda.gov/OSD_Docs/C/CANDLER.html', 'Candler series sand')}: very deep, excessively drained, and rapid to very rapid at moving water straight down, formed from old wind-blown and marine deposits with slopes that can run from flat to a rolling 12 percent. Closer to the lower ground around Lake Ariana and the town's older lots, drainage swings the other way toward soils in the {ext('https://soilseries.sc.egov.usda.gov/OSD_Docs/B/BASINGER.html', 'Basinger series')} family, very poorly drained sand that sits in shallow flats and drainageways and can stay ponded for months under natural conditions, even though the sand itself passes water fast once it's actually saturated. A base built for one side of town rarely suits the other without adjustment.</p>"),
        table("Auburndale yard types and what we do differently",
              ["Yard type", "What's different here", "What changes in the build"],
              [["Ridge lot near Lake Myrtle Sports Park", "Excessively drained Candler sand, occasional old grove-row dips", "Grade out the dips first; the sand rarely holds a puddle on its own"],
               ["Lakefront lot on Ariana or Juliana", "Inside the state's required 10-ft buffer from open water, absent a seawall", "Flag the buffer line for the crew before material gets ordered"],
               ["In-town lot near the 1927 city hall", "Smaller, older parcel on slower-draining ground", "Grade carefully off the house; there's less room to redirect water than on a ridge lot"],
               ["Subdivision built since the 1990s off Berkley Road", "Builder sod on a shallow, code-minimum irrigation zone", "Cap the same heads the sod used rather than adding new plumbing"],
               ["Pool-cage lot in a 2000s subdivision", "Screen-track edges and a concrete deck", "Feather the base to the slab and set that edge with adhesive, not nails"]],
              "Distances and prices don't change by yard type; the base and grading plan do."),
        sec("Who reviews a turf permit in Auburndale",
            f"<p>Auburndale runs its own {ext('https://auburndalefl.com/construction-services/', 'Construction Services division')} out of 108 East Park Street, reachable at (863) 965-5530, and applications go through the city's online permitting portal rather than a paper counter form. Nothing published in the city's code singles out synthetic or artificial turf, and we don't keep a separate page here for Auburndale's own ordinance the way we do for the full county, so a call to Construction Services before work starts is worth more than a guess. The {a(*PERMITS_PAGE)} covers the state standard that reaches every Polk County address, Auburndale included, and a search on the {ext('https://www.polkflpa.gov/', 'Polk County Property Appraiser')} site confirms a specific parcel before anyone assumes which office to call. None of that touches a private HOA: {a(*HB683_PAGE)} binds Auburndale's own government, not a subdivision's covenants, so a deed-restricted street here still runs its own architectural review; {a(*HOA_PAGE)} spells out where state law limits what that review can actually forbid.</p>"),
        sec("Water and irrigation rules for an Auburndale address",
            f"<p>Auburndale bills and schedules its own water through the city's {ext('https://auburndalefl.com/utilities/', 'Public Utilities Department')} rather than buying through the county, and since April 3, 2026 every address here has followed the {ext('https://www.swfwmd.state.fl.us/the-newsroom/2026/district-extends-modified-phase-iii-water-shortage', 'Southwest Florida Water Management District Modified Phase III')} order: one watering day a week, assigned by the last digit of the house number, running through October 1, 2026. Addresses ending 0 or 1 water Monday, 2 or 3 Tuesday, 4 or 5 Wednesday, 6 or 7 Thursday, 8 or 9 Friday, inside a 12:01-to-4-a.m. or 8-p.m.-to-11:59-p.m. window on lots under an acre. A lawn that becomes synthetic turf drops off that schedule entirely once its heads are capped, which the state's own turf rule already requires.</p>"),
        sec("Lakes, a sports park and a rail trail",
            f"<p>Auburndale sits among more than a dozen named lakes; Lake Ariana runs 1,019 acres and Lake Juliana 924, sitting next to each other along State Road 559, with a city park on Ariana's shore for anyone who wants to see the setback line in person. Turf near any of these waterbodies has to hold the state's required 10-foot line back from open water, an allowance that disappears only where a seawall or bulkhead already stands between the lawn and the lake. On the north side of town, the {ext('https://en.wikipedia.org/wiki/Auburndale_TECO_Trail', 'Auburndale TECO Trail')} runs 7.3 paved, nearly flat miles past the Lake Myrtle Sports Complex, nine baseball diamonds and ten soccer fields that host county-wide tournaments, before joining the Van Fleet State Trail up in {city('polk-city')}.</p>"),
        "<!--AUTO:city-services-->",
    ]),
    faqs=[
        faq("Does Auburndale have its own rule for artificial turf, or does Polk County's apply?",
            f"Neither office has published anything specific to synthetic turf. Auburndale's Construction Services division (863-965-5530) handles the city's building permits generally, and the state's May 2026 standard, not a city or county ordinance, is what actually governs a covered residential lawn here. The {a(*PERMITS_PAGE)} walks through what that standard requires."),
        faq("How many days a week can an Auburndale address run irrigation right now?",
            "One, under the regional water shortage order in effect since April 2026, assigned by the last digit of the address. A capped, synthetic section of yard stops needing that schedule at all, since the state's turf rule already bars watering it through an in-ground system regardless of any shortage order."),
        faq("Do lakefront lots on Lake Ariana or Lake Juliana need extra clearance for turf?",
            "Yes, unless a seawall or bulkhead already stands between the lot and the water, in which case the distance rule drops away. Otherwise the ten-foot line holds, and a yard backing onto either lake typically has more usable space than that rule first suggests, just not turf running to the water's edge."),
        faq("Does the sandy ground near Lake Myrtle Sports Park need a different base than a lot near downtown?",
            "Usually a similar base depth, built differently. Ridge sand near the sports park drains almost too fast and rarely holds water during compaction, while older lots toward downtown sit on slower ground that needs the grading double-checked so a heavy storm has somewhere to go besides the foundation."),
        faq("How do you pick the best artificial turf contractor near me in Auburndale?",
            "Ask which side of town the crew is used to working, since ridge sand near Lake Myrtle and low ground near Ariana call for different grading judgment calls. Also ask for base depth and infill type in writing, and whether the quote accounts for the city's own watering-day schedule when heads get capped."),
    ],
    sources=SRC, city=SLUG,
    crumbs=[("Service areas", "/areas/")], crumb="Auburndale",
    related=[("/areas/polk-county/", "Turf across Polk County"), ("/laws/permits/polk-county/", "Polk County permit rules for turf"),
             ("/areas/lake-alfred/", "Turf in Lake Alfred"), ("/areas/winter-haven/", "Turf in Winter Haven"),
             ("/artificial-turf-cost/", "Turf cost tables for Central Florida")],
)

# ============================================================== local
LOCAL = {
    "residential": {
        "title": "Artificial Grass Installation in Auburndale, FL – Ridge to Lake",
        "meta": "Auburndale artificial grass installers building for both sides of town: excessively drained Candler ridge sand and slower ground near Lake Ariana.",
        "h1": "Installing artificial grass across Auburndale's ridge and lake sides",
        "lede": capsule(f"Auburndale runs the same {price('residential')} a square foot Central Florida installed range quoted anywhere in Polk County, current this fall. What changes here is the ground: Candler sand on the ridge toward Lake Myrtle drains almost too well, while older lots down toward Lake Ariana sit on slower, wetter soil that wants a fuller compacted base."),
        "sections": [
            ("Candler sand on the ridge side of town",
             f"<p>Subdivisions built off Berkley Road and out toward {city('polk-city', 'Polk City')} generally sit on Candler series sand, excessively drained and rapid to very rapid at moving water down and away, the kind of ground that rarely gives a crew standing water to work around during a build. That drainage speed cuts the other way once turf goes in: a base compacted at the shallow end of the state's allowed range settles faster on Candler sand than on a loamier soil, so we lean toward the fuller two-to-four-inch depth on a ridge lot rather than the minimum. Old citrus-grove rows sometimes leave a shallow dip across a yard that was platted over former grove land, and that gets graded out before rock goes down, not covered over.</p>"),
            ("Older lots near downtown sit on different ground",
             "<p>Closer to the 1927 city hall and Auburndale's older residential blocks, lots run smaller and the native ground drains more slowly, closer to the Basinger family of soils that dominate low, flat ground around the lakes than to the ridge sand a mile or two north. A front yard here often has less room to redirect a downpour than a wide ridge-subdivision lot does, so the one-to-two-percent fall away from the house gets checked twice, once on bare soil and again after the first lift of rock, since two to four inches of stone can flatten a subtle grade if nobody rechecks it. These smaller lots are also where a side-yard conversion comes up most, since sod rarely holds up in the narrow gap between an older home and its fence line.</p>"),
            ("What Construction Services expects on a lawn conversion",
             f"<p>Auburndale's Construction Services division doesn't have a published rule specific to synthetic turf, so a residential conversion here follows whatever a specific scope actually requires, which is often just a plumbing step for capping the irrigation heads a new lawn no longer uses. That capping matters beyond paperwork: the city's own watering schedule, currently one day a week under the regional shortage order, stops applying to a section of yard entirely once its heads are capped and the state's rule against irrigating turf takes over. Homeowners converting only part of a Candler-sand front yard, keeping a shade bed or a specimen oak in sod, should flag that split scope before a {svc('residential', 'residential turf conversion')} gets scheduled, not after. Our {post('base-under-artificial-turf-florida-sandy-soil', 'base guide for Central Florida sandy soil')} covers the compaction question in more depth than a permit call ever will.</p>"),
        ],
        "scenario": ("Say you're converting a ridge-subdivision front yard",
                     f"<p>Say a 2005-built home off Berkley Road has a 720 sq ft front lawn on Candler sand, builder sod that's thinned out under full afternoon sun for years. At {price('residential')} installed, that lawn lands between roughly $5,760 and $12,960 depending on backing weight and infill; most jobs on a straightforward, flat ridge lot like this one land inside the {price('residential', typical=True)} typical band, or about $7,200 to $11,520. The existing sprinkler zone gets capped at the valve rather than removed, the crew grades a gentle fall toward the driveway apron, and the whole 720 sq ft gets a base at the fuller end of the state's allowed depth given how fast this sand already drains.</p>"),
        "faqs": [
            faq("Does Candler sand mean a ridge-lot lawn skips the compacted base?",
                "No. Fast drainage keeps water from pooling, but it does nothing for holding a flat, stable surface, which is what the compacted rock layer is actually for. A ridge lot in Auburndale still gets the same two to four inches of washed crushed rock as anywhere else, just with more attention to keeping loose native sand from working up through it later."),
            faq("Who do I call about a residential turf permit in Auburndale?",
                f"Construction Services at (863) 965-5530, since nothing published carves out a synthetic-turf exception from the city's general permitting. The {a(*PERMITS_PAGE)} covers the state standard that applies regardless of which office in Polk County reviews the paperwork."),
        ],
        "sources": SRC,
    },
    "pet": {
        "title": "Pet Turf & Dog Runs in Auburndale, FL – Lakefront Lots",
        "meta": "Pet turf for Auburndale yards near Lake Ariana and older in-town lots, with the state's waterbody setback and Auburndale's own water rules explained.",
        "h1": "Dog-friendly turf for Auburndale's lakefront and older lots",
        "lede": capsule(f"Pet turf in Auburndale runs {price('pet')} a square foot installed, unchanged from the rest of Central Florida this fall. A dog run behind a lakefront lot on Ariana or Juliana has to answer to the state's 10-foot waterbody setback, while a run on one of Auburndale's smaller in-town lots is mostly a question of fitting a narrow side yard."),
        "sections": [
            ("A dog run near Lake Ariana or Lake Juliana",
             f"<p>A yard backing onto {ext('https://polk.wateratlas.usf.edu/waterbodies/lakes/160450/lake-ariana', 'Lake Ariana')} or Lake Juliana has to keep any new turf, dog run included, ten feet clear of open water under the same rule an ordinary residential lawn follows, an allowance that only lifts where a seawall or bulkhead already sits between the yard and the lake. What changes for a dog run specifically is drainage direction: infill has to stay on the property under the state's rule, and a run graded toward open water rather than toward a swale or the street risks carrying sand or zeolite into the lake during a hard rain. Keeping the run's low point pointed away from Ariana or Juliana, not just outside the ten-foot line, is the safer plan on these lots.</p>"),
            ("Narrow side yards near the older part of town",
             "<p>Auburndale's older lots, platted well before the subdivisions that followed decades later out toward the edges of town, tend to run narrow between the house and the property line, which is exactly where a dog often ends up running laps along a fence. Whether a weed barrier goes in is a pet-turf question everywhere, not just here, so what actually changes on one of these narrow lots is edge treatment: there's less width to give up to a paver or bender-board border, which pushes more of these runs toward a simple nailed perimeter instead. Measuring the actual usable width before ordering material matters more on a lot like this than on a wide-open ridge subdivision, where an inch or two lost to an edge treatment barely registers.</p>"),
            ("Rinsing a pet run under Auburndale's own watering schedule",
             f"<p>Auburndale's Public Utilities Department currently limits every address to one irrigation day a week under the regional shortage order, but that schedule governs sprinklers, not the hose rinsing a pet run actually needs, a distinction our post on {post('how-to-get-dog-urine-smell-out-of-artificial-turf', 'clearing dog odor from artificial turf')} explains in more depth. A dog run gets rinsed on whatever day it needs it, heat, odor or a heavy-use afternoon, since the state's own turf rule already keeps synthetic sections off the in-ground system regardless of the city's watering calendar. That's one less schedule to track for a household that's also watching which day its remaining sod is allowed to run, the same order neighboring {city('winter-haven', 'Winter Haven')} households follow under the same regional restriction.</p>"),
        ],
        "scenario": ("Say you have a dog run behind a lake-area ranch home",
                     f"<p>Say a single-story home two streets back from Lake Ariana has a fenced 340 sq ft side yard where a Labrador has worn the sod down to sand along the fence line. At {price('pet')} installed, that run costs roughly $3,400 to $6,120, with most pet-turf jobs this size landing in the {price('pet', typical=True)} typical range, or about $4,080 to $5,440. Since the yard sits well outside the lake's ten-foot setback already, the only site-specific step is grading the run's low point toward the front yard's storm inlet instead of back toward the fence and the lake beyond it, a five-minute planning decision that costs nothing extra either way.</p>"),
        "faqs": [
            faq("Can a dog run go inside the ten-foot setback from Lake Ariana if it's fenced?",
                "Fencing doesn't change it; only a physical barrier like a seawall or bulkhead between the yard and the lake does. Without one already in place, a fenced run still has to sit ten feet clear of the water the same as an open lawn would."),
            faq("How do you find the best pet turf installer near me in Auburndale?",
                "Ask specifically about infill choice for a dog run, since coated silica sand or zeolite are the odor-control options the state's material rule actually allows, not rubber crumb. Also ask how the crew plans to grade the run's low point if the yard sits anywhere near Ariana, Juliana or one of Auburndale's other lakes."),
        ],
        "sources": SRC,
    },
    "putting": {
        "title": "Backyard Putting Greens in Auburndale, FL – Ridge Lots",
        "meta": "Backyard putting greens for Auburndale's rolling ridge lots and older lake-area properties, with contouring notes and the state's waterbody setback.",
        "h1": "Putting greens for Auburndale's ridge slopes and lake-area lots",
        "lede": capsule(f"A backyard putting green in Auburndale runs {price('putting')} a square foot installed, the same range as everywhere in Central Florida heading into fall. What's local here is the ground a green sits on: rolling ridge terrain near Lake Myrtle Sports Park gives a green real contour to work with, while flatter lake-area lots near Ariana and Juliana need the state's setback worked into the layout instead."),
        "sections": [
            ("A sports-minded town with room to build a green",
             f"<p>Auburndale already centers a fair amount of its recreation around the Lake Myrtle Sports Complex and the {ext('https://en.wikipedia.org/wiki/Auburndale_TECO_Trail', 'TECO Trail')} that runs past it, nine baseball diamonds and ten soccer fields on one side of town and 7.3 miles of paved path connecting to Polk City on the other. A backyard putting green fits that same pattern on a smaller scale, and a lot near the sports complex or the trail corridor often has the flatter, more open backyard that makes laying out cups, a fringe and a chipping approach straightforward without cutting into mature landscaping, more so than the tighter in-town lots closer to {city('haines-city', 'Haines City')} tend to allow on a comparable budget.</p>"),
            ("Working with the ridge's natural roll instead of against it",
             f"<p>Where the ground rises toward the ridge running through town, ordinary yard grading already carries some slope, since a subdivision built into former citrus-grove land can hold several feet of elevation change across one backyard, the kind of terrain our post on {post('artificial-turf-on-a-slope', 'installing artificial turf on a slope')} addresses generally. Rather than grading that away, a green built on a ridge lot can use a gentle existing slope as the start of a break, shaping the subgrade to exaggerate or soften it before turf goes down, which is a different design conversation than the flat pad a lake-bottom lot usually starts from. The excessively drained sand under most ridge lots also means the green's subgrade rarely fights standing water during shaping.</p>"),
            ("Setback and space near Lake Ariana and Lake Juliana",
             f"<p>An older, larger lot near {ext('https://polk.wateratlas.usf.edu/waterbodies/lakes/160281/lake-juliana', 'Lake Juliana')} or Lake Ariana often has more backyard than a newer subdivision parcel, which sounds like an advantage for a full green with a chipping approach until the state's ten-foot waterbody setback gets measured in. A green laid out to end well short of that line, using the rest of the yard for the approach and fringe, avoids designing around a setback that gets discovered only after cups are already staked. A seawall or bulkhead along the shoreline removes that specific ten-foot requirement, but the point still needs confirming lot by lot rather than assumed, since two neighboring properties on the same stretch of shoreline can end up with different answers depending on what each one built decades ago.</p>"),
        ],
        "scenario": ("Say you're adding a green on a ridge-subdivision lot",
                     f"<p>Say a home near the sports complex has a 480 sq ft backyard with about eighteen inches of natural fall from back porch to rear fence, left over from the citrus grove the subdivision replaced. At {price('putting')} installed, a green sized to that yard runs roughly $6,720 to $14,400, with most jobs this size landing in the {price('putting', typical=True)} typical band, about $8,640 to $12,000. The crew shapes that existing fall into two gentle breaks rather than grading the yard flat first, since the ridge sand underneath already drains fast enough that the slope isn't fighting standing water the way it might on lower ground.</p>"),
        "faqs": [
            faq("Does a putting green need a different base on Auburndale's ridge sand?",
                "The base depth stays the same as any other yard, but shaping is different, since Candler sand holds a contour without the water-related settling risk that a wetter soil closer to the lakes can bring. That makes a ridge lot a reasonably forgiving place to build a green with real breaks rather than a flat practice pad."),
            faq("What should the best backyard putting green contractor near you in Auburndale get right before anyone signs anything?",
                "Ask how the design uses or avoids the lot's natural slope, since a ridge-adjacent yard often already has contour worth building around rather than erasing. Also confirm the layout keeps clear of the ten-foot lake setback on any lot near Ariana or Juliana before cups and fringe get placed."),
        ],
        "sources": SRC,
    },
    "playground": {
        "title": "Playground Turf in Auburndale, FL – Family Subdivisions",
        "meta": "Playground turf for Auburndale's newer family subdivisions and older shaded lots, covering heat, shade and the drip-line rule for mature oaks, checked this fall.",
        "h1": "Cushioned play turf for Auburndale's newer and older neighborhoods",
        "lede": capsule(f"Playground turf in Auburndale runs {price('playground')} a square foot installed, holding steady with the rest of Central Florida this fall. Full-sun backyards in the subdivisions built since the 1990s need a heat plan a shaded, older in-town lot with mature oaks doesn't, while that same older lot brings the state's drip-line rule into the layout instead."),
        "sections": [
            ("Full-sun play areas in newer subdivisions",
             f"<p>Most of Auburndale's growth since the 1990s has filled in subdivisions with young trees and wide-open backyards, which means a swing set or a trampoline in one of these newer neighborhoods usually sits in full afternoon sun with little canopy to break it up. Surface temperature on unshaded synthetic turf can reach 120 to 150°F in Florida summer sun, so a playground build here leans on lighter-colored fiber or a cooling infill rather than counting on shade that won't exist for another decade of tree growth. A hose rinse before after-school play drops that surface temperature fast, and it's worth building into a family's afternoon routine on these lots specifically.</p>"),
            ("Mature oaks on older, shadier lots",
             f"<p>Closer to Auburndale's original neighborhoods, decades-old oaks throw real shade over a backyard, which solves the heat problem a newer subdivision doesn't have but introduces the state's drip-line rule instead, covered at length in our post on {post('artificial-turf-near-live-oaks-and-palms', 'artificial turf near live oaks and palms')}: synthetic turf can't go inside a live oak's drip line, on that property or a neighboring one, unless a certified arborist signs off that the install won't harm the tree. A play area planned under or near an old oak's canopy on one of these lots needs that arborist step built into the timeline before equipment gets ordered, not worked around after a crew shows up ready to dig.</p>"),
            ("Lake Myrtle Sports Park as a family-recreation reference point",
             f"<p>Families already headed to the Lake Myrtle Sports Complex or walking the {ext('https://en.wikipedia.org/wiki/Auburndale_TECO_Trail', 'TECO Trail')} on weekends are the same households asking about play turf at home, usually looking for the same cushioned, shock-absorbing surface under a swing set or slide that a public playground uses, sized to a backyard instead of a park. A shock pad specified to the equipment's actual fall height matters more here than infill color, since a home play area doesn't get the same daily inspection a county park surface does, whether the yard sits in Auburndale proper or out toward {city('lakeland', 'Lakeland')} on the same ridge. Asking for that fall-height number in writing, rather than a generic pad thickness, is a small step that pays off the first time a child jumps off the swing instead of sliding down it.</p>"),
        ],
        "scenario": ("Say you're building a play area in a newer subdivision",
                     f"<p>Say a family in a 2015-built subdivision off SR 559 wants a 260 sq ft play area around a swing set, currently bare dirt in full afternoon sun since the builder's sod never took there. At {price('playground')} installed, that area runs roughly $2,600 to $6,500 depending on pad thickness and infill, with most small residential play areas landing in the {price('playground', typical=True)} typical band, about $3,120 to $4,940. Given the lack of shade, the crew specs a lighter-colored fiber and confirms the shock pad matches the swing set's actual fall height rather than a generic thickness, and the family plans to add a shade tree nearby over the next year or two.</p>"),
        "faqs": [
            faq("Does a play area near an old oak in Auburndale need special permission?",
                "If the equipment or turf falls inside the tree's drip line, yes, a certified arborist has to certify the install won't harm the tree, since the state's turf rule bars synthetic grass inside a drip line otherwise. Measuring the canopy's actual spread before ordering material avoids finding this out mid-project."),
            faq("Is rubber infill an option for a backyard swing set in Auburndale?",
                "Yes, rubber or another synthetic infill is allowed specifically within the footprint of playground equipment under the state's material rule, unlike the rest of a residential lawn where it isn't. Outside that equipment footprint, infill has to switch back to silica sand, rock, shell or a coated natural material."),
        ],
        "sources": SRC,
    },
    "pool": {
        "title": "Pool & Lanai Turf in Auburndale, FL – Screen-Cage Lots",
        "meta": "Pool and lanai turf for Auburndale's screen-cage subdivisions and lakefront pool decks, covering deck drainage and the state's waterbody setback.",
        "h1": "Turf for Auburndale pool cages and lakefront decks",
        "lede": capsule(f"Pool-area turf in Auburndale is priced from the same {price('residential')} range as a residential lawn, unchanged across Central Florida this fall. A screen-cage lot in one of Auburndale's newer subdivisions is mostly a deck-drainage question, while a lakefront pool near Ariana or Juliana adds the state's waterbody setback on top of that."),
        "sections": [
            ("Screen-cage subdivisions built since the growth years",
             f"<p>Pool cages became close to standard on new Auburndale homes through the subdivisions built from the 1990s into the 2020s, and turf around one of these pools has to meet a concrete deck at a clean, feathered edge rather than trailing off into loose rock the way an open-yard lawn can, a transition our post on {post('install-artificial-turf-over-concrete-pavers-or-grass', 'installing turf over concrete, pavers or grass')} covers for any hardscape edge. That edge typically bonds with adhesive instead of nails, since there's no soil at the transition to anchor into, and getting that bond right matters more here than almost anywhere else on the property, since a pool deck edge takes bare feet and pool furniture dragging across it daily, far more wear than a fence-line edge out in the open yard ever sees over the same number of years.</p>"),
            ("Ridge sand under a pool-cage lot's base",
             f"<p>On the ridge side of town, the excessively drained Candler sand under a pool-cage lot means water rarely lingers under the base during construction, which simplifies compaction but doesn't remove the need for it. The base still gets built to the same two-to-four-inch washed-rock depth as anywhere else, graded to carry rinse water and rain away from the pool's overflow drain rather than back toward the cage's screen track, where standing water tends to work its way into the track hardware over time, the same base logic that applies whether the cage sits in Auburndale or out toward the vacation-home corridor near {city('davenport', 'Davenport')}.</p>"),
            ("Lakefront pool lots near Ariana or Juliana",
             f"<p>A pool cage on a lot backing onto Lake Ariana or Lake Juliana sits inside a yard that also has to respect the state's ten-foot waterbody setback for any turf outside the cage itself, even though the pool and screen enclosure aren't turf and aren't subject to that particular rule. Turf laid between the cage and the property's rear lake frontage, a common layout on these lots, needs that ten-foot line measured and staked the same way a lawn conversion would, seawall exception included where one already exists. Pricing that strip before the setback is confirmed tends to overstate how much of it can actually be turfed, which makes for an awkward conversation later if the number has to come back down.</p>"),
        ],
        "scenario": ("Say you're finishing a pool cage in a 2000s subdivision",
                     f"<p>Say a 2008-built home has a 520 sq ft pool cage with bare, weedy dirt around the pool deck and along the screen track, never landscaped since the builder poured the deck. At the {price('residential')} residential range, that area runs roughly $4,160 to $9,360 installed, with most pool-cage jobs this size landing in the {price('residential', typical=True)} typical band, about $5,200 to $8,320. The crew feathers the base to the existing deck height, sets the screen-track edge with adhesive, and grades the narrow strip along the track away from the hardware rather than toward it, a detail that matters more here than the color of the infill ever will.</p>"),
        "faqs": [
            faq("Does turf inside an Auburndale pool cage need the ten-foot lake setback?",
                "Only if that same yard also runs turf outside the cage toward a lake frontage; the cage and pool themselves aren't turf and aren't subject to the setback. A lot backing onto Ariana or Juliana still needs the ten-foot line respected for any lawn or lanai turf beyond the enclosure."),
            faq("Why does the screen-track edge matter more than the rest of a pool-cage lawn?",
                "Because it bonds to the track with adhesive rather than anchoring into soil, and that transition takes constant foot traffic and dragged furniture. A rushed bond at that one edge tends to show lifting well before the rest of the turf does."),
        ],
        "sources": SRC,
    },
    "repair": {
        "title": "Turf Repair in Auburndale, FL – Ridge and Lake-Area Lots",
        "meta": "Artificial turf repair in Auburndale for lifted seams, capped-head retrofits and ridge-lot edge failures, quoted after photos or a site visit.",
        "h1": "Fixing artificial turf on Auburndale's ridge and lake-area lots",
        "lede": capsule("Turf repair in Auburndale is quoted after photos or a site visit, since a lifted seam, a shrunken infill layer and a capped-head retrofit all cost differently to fix. Two problems show up more here than elsewhere: heads that were never properly capped when the state's turf rule took effect, and perimeter edges that lift faster on excessively drained ridge sand than on heavier ground."),
        "sections": [
            ("Irrigation heads that were capped incorrectly",
             f"<p>Some Auburndale lawns installed before the state's turf rule reached full effect still have irrigation heads under them that were shut off at the timer rather than physically capped at the valve, which technically leaves an active line under the turf even though nothing sprays. That matters for two reasons: the state's rule requires those heads capped, not just turned off, and a line left pressurized under turf can eventually fail and surface as a soggy patch with no obvious cause. Checking valve boxes against what's actually capped is a quick first step on an older Auburndale lawn before diagnosing anything else, and it's a five-minute check compared with tracking down a soggy patch after the fact.</p>"),
            ("Why ridge-lot edges lift before lake-area ones do",
             f"<p>On excessively drained Candler sand, a perimeter edge that was under-compacted or nailed too far apart tends to show movement sooner than the same mistake would on heavier, wetter ground, since loose ridge sand shifts under a lifted edge rather than holding it in place by sheer weight, the kind of storm-driven failure our post on {post('artificial-turf-hurricane-flooding', 'artificial turf in a hurricane or flood')} walks through. A lifted corner on one of these ridge lots is usually a re-anchoring job rather than evidence the whole lawn failed, but it's worth checking the rest of the perimeter at the same visit, since one weak stretch of edge often isn't the only one.</p>"),
            ("Driveway and hardscape edges near the older part of town",
             f"<p>On Auburndale's smaller, older in-town lots, a turf lawn often runs right up against a driveway, walkway or patio slab with little room to spare, and that adhesive-bonded transition is one of the most common repair calls on these properties specifically, whether the home sits here or in an equally old block of {city('winter-haven', 'Winter Haven')}. A lifted strip right at a hardscape edge usually traces back to that one bond rather than a problem with the lawn generally, and fixing just that section, rather than re-doing the whole perimeter, is typically enough on an otherwise sound older lot with no other signs of trouble anywhere along the rest of the perimeter.</p>"),
        ],
        "scenario": ("Say you have a lifted seam along a driveway",
                     "<p>Say a home near downtown has about 45 sq ft of turf lifting along the driveway edge where the original adhesive bond failed after several years, while the rest of a roughly 600 sq ft front lawn still looks fine. A repair like that is priced after a site visit rather than off a square-foot table, since the fix is mostly labor to lift, clean and re-bond that one edge rather than materials for a full section. Photos of the lifted strip and the driveway transition, sent ahead of a visit, usually let a crew scope the job before arriving.</p>"),
        "faqs": [
            faq("How do I know if my Auburndale lawn's irrigation heads are actually capped?",
                "Check the valve box for that zone; a head that's simply turned off at the controller still has a pressurized line running to it, while a properly capped one has the line sealed at the valve itself. If that's unclear from the box alone, it's worth having it checked before assuming a soggy patch is a turf problem rather than a plumbing one."),
            faq("Why did the edge of my ridge-lot lawn lift after only a couple of years?",
                "Fast-draining Candler sand doesn't hold a poorly anchored edge in place the way heavier soil can, so an under-compacted or under-nailed perimeter tends to show movement sooner on ridge lots than on lower, wetter ground. It's usually a re-anchoring fix rather than a sign the whole lawn needs replacing."),
        ],
        "sources": SRC,
    },
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
