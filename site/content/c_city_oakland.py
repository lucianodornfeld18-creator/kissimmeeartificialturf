# -*- coding: utf-8 -*-
"""Oakland, FL (Orange County, tier 2). Research checked September 2026.
Primary sources: oaklandfl.gov (permitting, utility billing, history, tree city, nature preserve),
Orange County Water Atlas (Johns Lake), USDA NRCS official series descriptions (Candler, Apopka,
Basinger), brileyfarm.com and homesbymarco.com (new subdivisions), Wikipedia (West Orange Trail),
Census Reporter (2020 population). See SRC below for exact URLs."""
from _helpers import page, capsule, sec, table, faq, a, svc, city, post, src, ext, price
from _cityservice import cityservice_pages

SLUG = "oakland"

SRC = [
    "census-acs",
    ("Town of Oakland — Building & Permit Department", "https://oaklandfl.gov/1014/Building-Permit-Department"),
    ("Town of Oakland — Irrigation & Watering Restrictions", "https://oaklandfl.gov/195/Irrigation-Watering-Restrictions"),
    ("Town of Oakland — Utility Billing", "https://www.oaklandfl.gov/192/Oakland-Utility-Billing"),
    ("Town of Oakland — About the Town of Oakland", "https://oaklandfl.gov/216/About-the-Town-of-Oakland"),
    ("Town of Oakland — Oakland History", "https://oaklandfl.gov/220/Oakland-History"),
    ("Town of Oakland — Historic Town Hall", "https://www.oaklandfl.gov/217/Historic-Town-Hall"),
    ("Town of Oakland — Tree City", "https://oaklandfl.gov/223/Tree-City"),
    ("Oakland Nature Preserve", "https://oaklandnaturepreserve.wildapricot.org/"),
    ("Orange County Water Atlas — Johns Lake", "https://orange.wateratlas.usf.edu/waterbodies/lakes/7935/johns-lake"),
    ("Wikipedia — West Orange Trail", "https://en.wikipedia.org/wiki/West_Orange_Trail"),
    ("Briley Farm — official site", "https://brileyfarm.com/"),
    ("Homes by Marco — Longleaf at Oakland", "https://www.homesbymarco.com/subdivisions/longleaf-at-oakland-in-oakland-fl"),
    ("USDA NRCS — official series description, Candler series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/C/Candler.html"),
    ("USDA NRCS — official series description, Apopka series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/A/APOPKA.html"),
    ("USDA NRCS — official series description, Basinger series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/B/BASINGER.html"),
    ("Orange County Property Appraiser — parcel search", "https://ocpafl.org/"),
    ("Census Reporter — Oakland, FL profile", "http://censusreporter.org/profiles/16000US1250525-oakland-fl/"),
]

PERMITS = "/laws/permits/orange-county/"
HOA = "/laws/hoa-rules/"
HB683 = "/laws/florida-hb-683/"
COST = "/artificial-turf-cost/"

# ============================================================== HUB
_hub_body = "".join([
    sec("A town between two lakes, not a suburb of Orlando",
        "<p>Oakland runs its own town government from a former bank building on the corner of Oakland Avenue, a one-story brick structure the town still calls its "
        + ext("https://www.oaklandfl.gov/217/Historic-Town-Hall", "Historic Town Hall")
        + ", built in 1911 and standing from back when the Orange Belt Railway first brought a citrus boom through in the 1880s. The town "
        + ext("https://oaklandfl.gov/216/About-the-Town-of-Oakland", "describes itself as sitting between Lake Apopka and Johns Lake")
        + ", and that placement, plus the oak canopy the founders named the town for instead of the "
          "railroad investor's preferred choice, still shapes what a turf crew finds on a given lot: shaded, root-laced older yards near downtown, "
          "open new construction a half-mile out, and a shoreline that pulls the state's water rules into almost every estimate.</p>"),
    sec("Does Oakland review its own building permits?",
        "<p>Yes, but not with in-house staff. The Town of Oakland contracts its "
        + ext("https://oaklandfl.gov/1014/Building-Permit-Department", "Building & Permit Department")
        + " to Willdan Engineering, Inc., whose reviewers work offsite and take inspection requests by email rather than at a town counter. "
          "Oakland doesn't have its own separate law page here, so the "
        + a(PERMITS, "Orange County permit page")
        + " above covers the county's baseline code and contacts for the wider area; inside Oakland's town limits, Willdan is the office that actually reviews a job, "
          "and a call before ordering material is worth more than a guess based on a neighboring jurisdiction. Confirm which side of the town line a lot sits on with the "
        + ext("https://ocpafl.org/", "Orange County Property Appraiser")
        + "'s parcel search, since Oakland's boundary is compact and a mailing address alone won't settle it.</p>"),
    sec("HOA review and the state's turf rule",
        "<p>Newer Oakland subdivisions such as Longleaf at Oakland and Briley Farm carry an architectural review step for exterior changes, the way most deed-restricted "
          "Florida communities do; we found no published Longleaf or Briley Farm document naming turf, sod or ground cover specifically, so budget time for a design "
          "review submittal rather than assuming a fixed rule either way. Florida's "
        + a(HOA, "HOA statute")
        + " already keeps an association from reaching into a fenced Oakland backyard that a passerby on the sidewalk or a neighbor next door simply can't see, and "
        + a(HB683, "the state's May 2026 turf standard")
        + " sets the floor no association or town code can undercut on a covered single-family lot: permeable turf, natural infill, capped irrigation, and a setback from "
          "Oakland's shoreline that a stricter local rule can't beat.</p>"),
    table("Oakland yard types and what we do differently",
          ["Where in town", "What you'll typically find", "How the job changes"],
          [["Oak-shaded in-town lot", "Narrow, older lot near downtown under mature canopy", "Shallow excavation and hand digging near roots; the state's drip-line rule keeps turf clear of the canopy edge without an arborist letter"],
           ["Longleaf at Oakland", "2019–2021 Pulte homes off SR 50 with an HOA and West Orange Trail access", "An ARC submittal with a spec sheet before install; straightforward flat grading on newer soil pads"],
           ["Briley Farm", "Custom estate lots from a third of an acre to more than an acre on the old Briley family farm", "More square footage per job and room to grade a full 1–2% fall without fighting a tight side yard"],
           ["Lake Apopka or Johns Lake shoreline", "Rear lot line ending at open water or a seawall", "The 10-ft waterbody setback, staked before ordering turf, unless a seawall already separates the yard from the water"],
           ["Pool-cage home", "Screen enclosure with a lanai deck", "Glue-down edges and a drainage underlay where turf meets concrete instead of a nailed perimeter"]],
          "Prices don't change by yard type; access, grading and how much cutting the crew has to do around roots or a cage frame do. Figures are a Central Florida market range, not a quote for a specific yard."),
    sec("Water, the town's utility and its two shorelines",
        "<p>Oakland runs its own water and sewer system rather than buying through Orange County Utilities; the "
        + ext("https://www.oaklandfl.gov/192/Oakland-Utility-Billing", "Utility Billing office")
        + " takes account questions and sits inside the St. Johns River Water Management District's territory. Lawn watering follows the district's "
        + ext("https://oaklandfl.gov/195/Irrigation-Watering-Restrictions", "odd/even schedule")
        + ": odd addresses water Wednesday and Saturday, even addresses water Thursday and Sunday, dropping to one day each once standard time returns in "
          "November. None of it reaches a capped synthetic lawn, since the state's turf rule already bars watering synthetic turf from an in-ground system "
          "regardless of the day on the calendar. A yard backing onto Lake Apopka or Johns Lake keeps the same 10-ft setback the table above describes.</p>"),
    sec("What's underfoot: ridge sand or lake-margin muck",
        "<p>Away from the shoreline, Oakland's higher ground sits on the same ridge sands common across west Orange County: excessively drained "
        + src("usda-wss", "Candler")
        + ", built from thick wind-blown and marine sand with slopes up to 12%, and the deeper, well-drained "
        + ext("https://soilseries.sc.egov.usda.gov/OSD_Docs/A/APOPKA.html", "Apopka series")
        + ", which carries a clay-rich layer roughly 55 inches down that natural turf grass never reaches but a base crew doesn't need to either. Closer to Lake Apopka "
          "and Johns Lake, the ground grades into "
        + ext("https://soilseries.sc.egov.usda.gov/OSD_Docs/B/BASINGER.html", "very poorly drained soils such as Basinger")
        + ", where the seasonal high water table can sit within 18 inches of the surface. On that end of town we build the full 4 inches of washed base rather than "
          "the shallow end of the state's range, so the turf sits above ground that stays wet long after a storm passes.</p>"),
    sec("A small town that's grown fast",
        "<p>Oakland counted 3,516 residents at the 2020 Census, up 38.5% from 2,538 in 2010, and the newer end of that growth shows up as Longleaf and Briley Farm "
          "fill in around a downtown that still reads the way it did a century ago. That mix means a turf inquiry here is as likely to come from a century-old lot "
          "under a live oak as from a homesite that didn't exist five years ago, and the two jobs rarely need the same base plan.</p>"),
])

HUB = page("/areas/oakland/", "city",
           "Artificial Turf Installation in Oakland, FL",
           "Artificial turf installers serving the Town of Oakland, FL, between Lake Apopka and Johns Lake. Permits, HOA review, soil and pricing, checked September 2026.",
           "Artificial turf in Oakland, between two lakes in west Orange County",
           capsule(f"We install and repair artificial turf in Oakland, FL, where installed lawns run {price('residential')} a square foot as of September 2026. "
                   "The town sits between Lake Apopka and Johns Lake and contracts its own building permits to an outside engineering firm rather than reviewing "
                   "them in house, which changes who you call before a crew shows up."),
           _hub_body,
           faqs=[
               faq("Is Oakland its own permitting authority?",
                   "Yes, but the review itself is outsourced. The Town of Oakland contracts building permits and inspections to Willdan Engineering, Inc., which works offsite, rather than keeping a building official on town staff."),
               faq("Does Oakland's tree canopy limit where turf can go?",
                   "The town's Tree City USA status commits it to an ordinance covering trees on streets and in parks; we found nothing published that sets a private-lot trunk rule. What does apply everywhere is the state's turf standard, which keeps synthetic grass out of a live oak's drip line unless a certified arborist signs off."),
               faq("Which water management district covers Oakland?",
                   "The St. Johns River Water Management District. Oakland runs its own water utility inside that district's boundary, and its two-lake geography is why the 10-ft waterbody setback comes up on more estimates here than in a landlocked subdivision."),
               faq("What separates the best artificial turf installers near Oakland from an average one?",
                   "Ask for a written scope with square footage, base depth and material, turf product and infill named specifically, and how the perimeter is anchored. A contractor who can answer all four without hedging is worth more than one who only quotes a price per foot."),
               faq("Is Oakland split between more than one soil type?",
                   "In practice, yes. Ridge sand such as Candler and Apopka covers most of the higher ground, while the strip closest to Lake Apopka and Johns Lake grades into much wetter, poorly drained soil, which is why we check a specific address before quoting base depth."),
           ],
           sources=SRC, city=SLUG, crumbs=[("Service areas", "/areas/")], crumb="Oakland",
           related=[("/areas/orange-county/", "Turf installers across Orange County"), (PERMITS, "Artificial turf permits in Orange County"),
                    ("/areas/winter-garden/", "Turf in Winter Garden"), ("/areas/montverde/", "Turf in Montverde"),
                    (COST, "Turf cost tables for Central Florida")])


# ============================================================== LOCAL
LOCAL = {
    "residential": {
        "title": "Artificial Grass Installation in Oakland, FL Yards",
        "meta": "Artificial grass installation in Oakland, FL: what changes between an oak-shaded in-town lot and new construction at Longleaf or Briley Farm.",
        "h1": "Turf for Oakland's oak-shaded lots and new-build yards",
        "lede": capsule(f"Installed artificial grass in Oakland runs {price('residential')} a square foot, typically {price('residential', True)}, as of September 2026. "
                        "The number that actually moves on a given quote here is root work: a lot under a mature oak near downtown costs more to prep than a "
                        "flat, sod-pad lawn at Longleaf or Briley Farm a few blocks away."),
        "sections": [
            ("An in-town lot's roots decide the schedule",
             "<p>Oakland's oldest blocks sit under the oak canopy the town was named for, a detail that shapes more of "
             + city("oakland", "how we plan turf work here")
             + " than any single ordinance does. A lawn conversion there starts with a walk around the yard to map "
             "surface roots before any sod comes up. Excavation stays shallow near a trunk and the crew builds up with base rather than cutting down through roots "
             "that a live oak needs to breathe. Getting closer to that trunk than the canopy's own drip line takes a certified arborist's written sign-off "
             "under the state's rule, and on a tight in-town lot that boundary can swallow more of the usable yard than a homeowner expects before the tape measure "
             "comes out.</p>"),
            ("Grading a Longleaf or Briley Farm lot is a different job",
             "<p>Longleaf at Oakland's Pulte-built lots and Briley Farm's larger custom homesites sit on graded pads with builder sod already established, so the "
             "excavation phase is faster: strip four inches, shape the fall away from the foundation, and move straight to base. Both communities carry an "
             "architectural review step for exterior work, and neither publishes a turf-specific clause as of this research pass, so a spec sheet and site plan "
             "submitted ahead of the ARC meeting saves a redo. Briley Farm's larger lots, some over an acre, also mean more room to run the 1–2% grade to a single "
             "low point instead of splitting it toward two fence lines.</p>"),
            ("Building on Candler and Apopka sand",
             "<p>Away from the two lakes, Oakland's ground is the same excessively drained Candler and well-drained Apopka ridge sand common across west Orange "
             "County, both of which barely hold water even after a hard rain. That's an advantage for a base crew: compaction firms up quickly and there's little "
             "risk of trapped moisture softening the rock later. It also means watering a newly seeded strip of remaining sod dries out fast, which is one more "
             "reason a full turf conversion appeals to an Oakland homeowner tired of a sprinkler running against sandy ground that won't hold it. The broader "
             + svc("residential", "residential installation guide")
             + " covers the base and product choices that hold everywhere in Central Florida, not just here; "
             + post("artificial-turf-near-live-oaks-and-palms", "the drip-line question specifically")
             + " is worth reading first if a live oak sits anywhere near the planned turf line.</p>"),
        ],
        "scenario": ("Say you have a 900 sq ft in-town lot",
                     "<p>Say you have a 900 sq ft backyard on one of Oakland's older streets, half of it shaded by a live oak close enough that its drip line "
                     "clips the back corner. We'd fence off that corner from the turfed area rather than pull a permission letter for a small strip, leaving "
                     "roughly 760 sq ft to convert. At Oakland's typical range of $10 to $16 a square foot, that prices between about $7,600 and $12,200, with the "
                     "root work near the trunk pushing toward the upper end even though the square footage shrank. A same-sized lot at Longleaf with no mature "
                     "trees to route around would land closer to the lower end of that same range for the full 900 sq ft, closer to what a "
                     + city("winter-garden", "Winter Garden")
                     + " or "
                     + city("horizon-west", "Horizon West")
                     + " lot without mature trees typically prices at, since the range itself doesn't change with the address, only with what's on the lot.</p>"),
        "faqs": [
            faq("Do I need Willdan's approval for a straightforward turf conversion in Oakland?",
                "A residential lawn swap is a smaller scope than most permitted work, but confirm with the contracted Building & Permit Department before starting, especially if you're also regrading or adding a drain line."),
            faq("Does Briley Farm's larger lot size change the price per square foot?",
                "No. A bigger, open lot is usually easier to grade, which can push a quote toward the lower end of the range, but the published per-square-foot figures stay the same regardless of lot size or address."),
        ],
        "sources": SRC,
    },
    "pet": {
        "title": "Pet Turf & Dog Runs in Oakland, FL",
        "meta": "Pet turf installation in Oakland, FL near Lake Apopka and Johns Lake: drainage, odor control and the state's infill rule for dog yards.",
        "h1": "Dog turf built for Oakland's lake-edge yards",
        "lede": capsule(f"Pet turf in Oakland runs {price('pet')} a square foot installed, typically {price('pet', True)}, as of September 2026. Dogs and standing water "
                        "don't mix, and on the stretch of town closest to Lake Apopka and Johns Lake, drainage does more work than infill choice to keep a run from "
                        "smelling by August."),
        "sections": [
            ("Lake-margin lots need a deeper flush zone",
             "<p>A dog run near "
             + city("oakland", "Oakland")
             + "'s two shorelines, Lake Apopka or Johns Lake, often sits on the wetter, poorly drained ground the county's soil survey maps toward the shoreline, "
             "where the seasonal high water table can sit close to the surface for months. We build the base at the full 4 inches on these lots rather than "
             "splitting the difference, and skip the weed barrier entirely under a pet area since fabric traps urine at the surface instead of letting it filter "
             "down. Zeolite or a coated sand infill goes on top, both allowed under the state's natural-material rule, chosen for how well they release trapped "
             "ammonia when rinsed rather than for looks.</p>"),
            ("Fencing a run inside the drip line without losing the shade",
             "<p>Plenty of Oakland's older lots have a live oak positioned right where a dog naturally wants to run, in the shade along a fence line. Rather than "
             "clear the canopy, we route the run around the drip line and rely on the tree's own shade to keep the surface cooler during the hottest part of the "
             "day, since pet turf without any shade at all can get hot enough to bother bare paws faster than a person walking across it barefoot notices.</p>"),
            ("What the state's turf rule means for a dog yard here",
             "<p>Rubber infill is a common question from dog owners who've read about it elsewhere, but Florida's rule reserves rubber and other synthetic infill "
             "for the footprint under playground equipment only; a dog run gets silica, zeolite or a coated sand instead. On an Oakland lot that slopes toward "
             "Johns Lake or a rear swale, we also grade the run so infill doesn't wash toward the water line during a summer storm, since the same rule requires "
             "infill to stay on the property it was installed on. The "
             + svc("pet", "pet turf and dog run guide")
             + " covers infill choice in more depth, and "
             + post("pet-turf-vs-regular-artificial-grass", "what actually differs between pet turf and a standard lawn")
             + " is a good next read for a homeowner comparing the two systems. The same drainage logic applies whether the run sits in Oakland, "
             + city("winter-garden", "Winter Garden")
             + " or "
             + city("ocoee", "Ocoee")
             + ", since the flatwoods-to-ridge soil pattern runs across all three.</p>"),
        ],
        "scenario": ("Say you have a 350 sq ft run along a side fence",
                     "<p>Say you have a 350 sq ft dog run down the side yard of a home a few blocks from Johns Lake, an area the previous owner never got sod to "
                     "hold in because of the standing water after storms. At Oakland's typical pet-turf range of $12 to $16 a square foot, that runs about $4,200 "
                     "to $5,600, with zeolite infill and a full-depth base built into that figure rather than added on top. Because the lot sits close to the "
                     "lake's edge, we'd also confirm the run doesn't cross into the 10-ft waterbody setback before locking in the layout.</p>"),
        "faqs": [
            faq("Which questions single out the best pet turf installer near Oakland before you sign anything?",
                "Ask specifically what infill they use for dogs and why. An installer who names zeolite or coated sand and explains the ammonia-release reasoning knows the state's material rule; one who suggests rubber for an open yard doesn't."),
            faq("Will pet turf smell worse near Johns Lake's humidity?",
                "Humidity alone doesn't cause odor; standing water in a base that can't drain does. That's why lake-margin lots here get the fuller base depth and no weed barrier under the pet area specifically."),
        ],
        "sources": SRC,
    },
    "putting": {
        "title": "Backyard Putting Greens in Oakland, FL",
        "meta": "Backyard putting green installation in Oakland, FL: how Briley Farm and Longleaf lot sizes shape a contoured green, with pricing and base notes.",
        "h1": "A practice green sized to an Oakland backyard",
        "lede": capsule(f"Putting greens in Oakland run {price('putting')} a square foot installed, typically {price('putting', True)}, as of September 2026. Contouring "
                        "and fringe turf drive most of that range, and how much room a lot has to work with, tight in-town or wide open at Briley Farm, decides "
                        "how ambitious the design can get."),
        "sections": [
            ("Room to build depends on which part of town",
             "<p>An older in-town lot near downtown "
             + city("oakland", "Oakland")
             + " rarely has more than a modest rectangle of open yard once a live oak's canopy and a shed or pool "
             "cage take their share, which keeps a green small: a single cup, a short chip pad, fringe on two sides. Out at Briley Farm, where custom lots run "
             "from a third of an acre past a full acre, there's room for a contoured multi-cup green with a proper chipping approach, since the grading crew "
             "isn't fighting a fence line eight feet from where the green needs to break.</p>"),
            ("Ridge sand makes a stable base easier",
             "<p>Candler and Apopka, the excessively to well drained sands under most of Oakland's higher ground, compact predictably once graded, which matters "
             "more for a putting green than a flat lawn because a green's contours have to hold their shape for years without a low spot developing where a "
             "ball collects water. We build the subgrade contours first, compact in lifts, then lay the green's foam or foam-and-rock base on top rather than "
             "trying to shape the final break in the turf itself.</p>"),
            ("Fringe and cups fit the same review process as any other exterior change",
             "<p>Longleaf at Oakland and other HOA-governed sections of town treat a putting green as an exterior improvement subject to the same architectural "
             "review as a patio or a fence, even though no published guideline mentions synthetic turf by name. Submitting a drawing that shows the green's "
             "footprint, height of any mounding and cup locations ahead of time tends to move faster than waiting for a question after installation starts. "
             "The full "
             + svc("putting", "putting green installation guide")
             + " goes through contouring and fringe choices in more detail, and "
             + post("backyard-putting-green-cost-florida", "how Florida green costs typically break down")
             + " is useful background before a design call. A homeowner comparing options against "
             + city("montverde", "Montverde")
             + "'s golf-community lots or "
             + city("clermont", "Clermont")
             + "'s larger yards will find the same per-square-foot range applies across all three towns.</p>"),
        ],
        "scenario": ("Say you have a 500 sq ft green and fringe at Briley Farm",
                     "<p>Say you have a 500 sq ft area at a Briley Farm homesite set aside for a two-cup green with fringe on three sides, a project the acre-plus "
                     "lot has room for without crowding the pool or the property line. At Oakland's typical putting-green range of $18 to $25 a square foot, that "
                     "runs about $9,000 to $12,500, with the higher end reflecting a second cup and a chipping pad rather than a single flat target. A same-sized "
                     "green squeezed onto an in-town lot would likely drop a cup to fit the space rather than push the price further.</p>"),
        "faqs": [
            faq("Can a putting green go inside a live oak's drip line at an Oakland home?",
                "Only with a certified arborist's letter confirming no harm to the tree, the same rule that applies to any other synthetic turf. Most Oakland greens we'd plan route around the drip line instead of pursuing that letter."),
            faq("Does Briley Farm's HOA require a specific turf brand for a green?",
                "We found no published brand requirement. The review process asks for a site plan and product spec sheet, not a named manufacturer, based on what's publicly available as of this research."),
        ],
        "sources": SRC,
    },
    "playground": {
        "title": "Playground Turf Installation in Oakland, FL",
        "meta": "Playground turf for Oakland, FL homes near the Oakland Nature Preserve: shock pad sizing, shade under oaks, and 2026 pricing.",
        "h1": "Safer play surfaces for Oakland's growing families",
        "lede": capsule(f"Playground turf in Oakland runs {price('playground')} a square foot installed, typically {price('playground', True)}, as of September 2026. "
                        "The town's population grew 38.5% between the 2010 and 2020 Census counts, and a good share of that growth is families whose kids already "
                        "spend weekends on the boardwalk at the nature preserve down the road."),
        "sections": [
            ("Shock pad thickness follows the equipment, not the town",
             "<p>A swing set or a small climbing structure in an "
             + city("oakland", "Oakland")
             + " backyard needs a shock pad sized to its fall height the same way it would anywhere else "
             "in Central Florida; the town doesn't publish a different standard. What changes locally is what sits around that equipment: an in-town yard often "
             "has a live oak close enough to help with shade, while a Longleaf or Briley Farm yard on a newer, more open lot may need a shade sail or a "
             "positioned tree planting instead, since full sun pushes a play surface's temperature well past what a natural lawn nearby would reach.</p>"),
            ("Rubber infill stops at the edge of the equipment",
             "<p>Florida's turf rule allows rubber or another synthetic infill only within the footprint of playground equipment itself, not across the rest of "
             "a residential yard. On an Oakland lot that means a clearly defined play zone with its own infill and pad, bordered by ordinary silica-infilled "
             "lawn turf everywhere else, rather than one uniform surface stretching from the swing set to the fence.</p>"),
            ("A family day at the nature preserve sets local expectations",
             "<p>The Oakland Nature Preserve, roughly 130 wetland and upland acres on Lake Apopka's south shore with more than 13 miles of trails, is the kind "
             "of free, walkable destination that shapes what families here expect from their own yard: someplace a kid can be barefoot and muddy without a "
             "parent worrying about fire ants or a bare dirt patch. A cushioned, well-drained play surface at home extends that expectation past the preserve's "
             "gate. The "
             + svc("playground", "playground turf guide")
             + " covers shock-pad sizing by fall height in full, and "
             + post("is-artificial-turf-safe-for-kids-pfas-lead", "the safety questions parents usually ask first")
             + " is worth reading alongside it. Families cross-shopping "
             + city("winter-garden", "Winter Garden")
             + " or "
             + city("clermont", "Clermont")
             + " will find the same shock-pad math applies regardless of which town the play set ends up in.</p>"),
        ],
        "scenario": ("Say you have a 300 sq ft play area under partial shade",
                     "<p>Say you have a 300 sq ft corner of a Longleaf backyard set aside for a swing set and a small climbing dome, with a young live oak nearby "
                     "that won't offer real shade for another decade. At Oakland's typical playground range of $12 to $19 a square foot, that prices between "
                     "$3,600 and $5,700, with the shock pad thickness under the equipment itself, not the open turf around it, driving most of that spread. "
                     "Adding a shade sail over the equipment is a separate line item we'd price after seeing the yard's sun exposure.</p>"),
        "faqs": [
            faq("Is playground turf safe under a live oak that drops acorns and leaves?",
                "Yes, but debris needs clearing before it breaks down into the infill layer. A live oak's late-winter leaf drop is the heaviest period, and blowing the surface clear during that stretch matters more than any other time of year."),
            faq("Does Oakland require a permit for a swing set or play structure itself?",
                "That's a separate question from the turf underneath it and depends on the structure's size and anchoring; ask Willdan Engineering, the town's contracted Building & Permit Department, before installing anchored equipment."),
        ],
        "sources": SRC,
    },
    "pool": {
        "title": "Pool & Lanai Turf in Oakland, FL",
        "meta": "Turf around a pool cage or lanai in Oakland, FL: drainage underlay, glue-down edges and pricing for 2026, near Lake Apopka and Johns Lake.",
        "h1": "Turf around an Oakland pool cage",
        "lede": capsule(f"Turf beside a pool or inside a screen enclosure in Oakland is priced at the residential range, {price('residential')} a square foot, "
                        f"typically {price('residential', True)}, as of September 2026. Newer pool-cage homes at Longleaf and Briley Farm and older lanais closer "
                        "to downtown need different edge details even though the price range is identical."),
        "sections": [
            ("Glue-down edges where turf meets a pool deck",
             "<p>Inside a screen enclosure on an "
             + city("oakland", "Oakland")
             + " lot, turf meets the pool deck's concrete directly, with no soil to anchor a nailed perimeter into. That edge gets bonded "
             "with adhesive instead, and a thin drainage underlay goes beneath the turf so water from pool splash-out or a hosed-off deck has somewhere to go "
             "rather than sitting against the concrete. This detail is the same whether the cage is a decade old near downtown Oakland or finished last year "
             "at Briley Farm.</p>"),
            ("Newer construction changes the surrounding grade, not the edge detail",
             "<p>A Longleaf or Briley Farm pool-cage home usually has the lanai poured level with a clean grade already sloping away from the house, so the turf "
             "portion outside the cage is typically a straightforward strip rather than a project needing much regrading. An older in-town lot with a lanai "
             "added years after the original house sometimes has a deck that settled slightly, which we check with a level before assuming the drainage still "
             "falls the right direction.</p>"),
            ("Low-E glass near a pool cage is worth a look either way",
             "<p>Pool cages sit close to the house, and a west- or south-facing window with low-emissivity glass can reflect enough concentrated sun to soften "
             "turf several feet away, regardless of which Oakland neighborhood the home is in. Checking that reflection path before installation is a five-minute "
             "step that avoids a scorched patch showing up in the first full summer. "
             + post("can-artificial-turf-melt", "How a melted patch actually happens")
             + " goes through the low-E glass problem in more detail, and the "
             + svc("pool", "pool and lanai turf guide")
             + " covers glue-down edge work beyond what fits on this page. The same reflection check applies equally on a screen enclosure in "
             + city("horizon-west", "Horizon West")
             + " or "
             + city("winter-garden", "Winter Garden")
             + ".</p>"),
        ],
        "scenario": ("Say you have a 450 sq ft lanai surround",
                     "<p>Say you have a 450 sq ft strip of turf planned around a screened pool at a Briley Farm home, replacing a paver border the builder left "
                     "as dirt. At Oakland's typical residential range of $10 to $16 a square foot, that comes to about $4,500 to $7,200, with the glue-down "
                     "edge along the pool deck and the drainage underlay both included in that figure rather than billed separately. An older in-town lanai "
                     "needing the deck releveled first would price toward the higher end for the extra prep.</p>"),
        "faqs": [
            faq("Does turf inside a screen enclosure still need the 10-ft waterbody setback?",
                "No. That setback applies to a natural or man-made waterbody like Lake Apopka or Johns Lake, not to a swimming pool, so a pool-cage lanai isn't affected by it."),
            faq("Can turf go directly over an existing paver pool deck?",
                "Usually yes, with a drainage layer and glue-down edges rather than nails, since pavers don't need to be removed first. We'd still check the paver base isn't already holding water before installing over it."),
        ],
        "sources": SRC,
    },
    "repair": {
        "title": "Artificial Turf Repair in Oakland, FL",
        "meta": "Artificial turf repair in Oakland, FL: seams, oak-debris wear and storm damage. Quoted after photos or a site visit, checked September 2026.",
        "h1": "Fixing tired turf on an Oakland lot",
        "lede": capsule("Turf repair in Oakland is quoted after photos or a short site visit rather than by the square foot, since a lifted seam, a melted patch "
                        "and a drainage fix take different time and materials. What we see most often here traces back to either oak debris or a base that "
                        "was never built to the state's current standard."),
        "sections": [
            ("Oak debris ages a lawn faster than sun does",
             "<p>An in-town "
             + city("oakland", "Oakland")
             + " lawn under a live oak deals with acorns, leaf drop and Spanish moss falling year-round, and left long enough, that organic "
             "material works down into the infill layer and starts holding moisture the way mulch does. The fix is usually a deep clean and infill top-up "
             "rather than replacing turf outright, but a lawn that's gone several years without clearing debris can mat enough that brushing alone won't "
             "restore it, especially right after the heaviest late-winter leaf drop.</p>"),
            ("A driveway or pool-deck edge is the first place to check",
             "<p>Wherever turf meets a hard edge, a Longleaf driveway apron or a Briley Farm pool deck, that seam bonds with adhesive rather than nails into "
             "soil, and it takes more foot and wheel traffic than any other point on the lawn. A lifted corner there after a season of use almost always traces "
             "back to that one bond rather than a problem with the rest of the lawn, and it's a faster, cheaper fix caught early than after it's peeled back "
             "another six inches.</p>"),
            ("An older base sometimes needs more than a patch",
             "<p>Turf installed years ago in Oakland, before the state's washed-rock standard took effect in 2026, sometimes sits on a base that used unwashed "
             "fill, which binds into a crust over time and stops draining the way it should. A patch on top of that base fixes the visible seam but not the "
             "puddling underneath, so we'll say plainly when a repair is a stopgap and when the honest answer is pulling a section back to rebuild the base "
             "correctly. The "
             + svc("repair", "turf repair guide")
             + " lists the most common failure points beyond what's specific to Oakland, and "
             + post("artificial-turf-hurricane-flooding", "what a storm can do to an otherwise sound lawn")
             + " covers the wind and flooding angle. The same diagnosis-before-patch approach holds whether the lawn is in Oakland, "
             + city("montverde", "Montverde")
             + " or "
             + city("clermont", "Clermont")
             + ".</p>"),
        ],
        "scenario": ("Say you have a 40 sq ft trouble spot",
                     "<p>Say you have a 40 sq ft corner of an in-town lawn where the perimeter nails pulled loose after a summer storm and infill washed toward "
                     "a side swale. That's a small fraction of a typical 900 sq ft Oakland lawn, the kind that costs roughly $9,000 to $14,400 to replace whole "
                     "at the town's residential range of $10 to $16 a square foot, which is exactly why a repair, re-anchoring the edge and topping off infill "
                     "rather than tearing out the lawn, is the right call here. We'd quote that after seeing photos of the lifted section and the direction "
                     "water moves across the yard.</p>"),
        "faqs": [
            faq("Comparing turf repair companies near Oakland? What actually separates the best from a quick patch job.",
                "Ask whether they'll diagnose the base before quoting a fix. A repair that only addresses the visible seam without checking what's underneath tends to come back within a year or two."),
            faq("Does a repair need Willdan's sign-off the way a new install might?",
                "A small seam or edge repair typically doesn't trigger a permit, but a repair that involves rebuilding the base or regrading a section is worth a call to the town's contracted Building & Permit Department first."),
        ],
        "sources": SRC,
    },
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
