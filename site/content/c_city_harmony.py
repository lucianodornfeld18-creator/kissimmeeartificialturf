# -*- coding: utf-8 -*-
from _helpers import page, capsule, sec, table, faq, ul, steps, note, cta, a, svc, city, county, cs, post, src, ext, price
from _cityservice import cityservice_pages

SLUG = "harmony"

SRC = [
    "dep-rule", "fs125572", "fs7203045", "toho-days", "ifas-turf", "fs7203075", "sgw-faq", "stn-life",
    "magnolia-heat", "horsemans-heat", "usda-wss", "attampa-cost", "lbs-fl-cost", "magnolia-pet-cost",
    "installartificial-pet", "angi-putting", "homeguide-putting", "mightygrass-playground", "bearcat-10yr",
    "attampa-sod", "watersavers-pfas", "mtsinai-turf",
    ("Osceola County — Harmony DRI history", "https://www.osceola.org/Doing-Business/Community-and-Economic-Development/DCIs-and-DRIs/Harmony-DRI"),
    ("Osceola County — Harmony West Community Development District", "https://www.osceola.org/agencies-departments/community-development-districts/harmony-west-cdd/"),
    ("Wikipedia — Harmony, Florida", "https://en.wikipedia.org/wiki/Harmony,_Florida"),
    ("Wikipedia — Sunbridge, Florida", "https://en.wikipedia.org/wiki/Sunbridge,_Florida"),
    ("Harmony Golf Preserve — course overview", "https://harmonygolfpreserve.com/"),
    ("Toho Water Authority — Harmony Water Treatment Plant upgrade and expansion", "https://www.tohowater.com/news/harmony-water-treatment-plant-upgrades-expansion"),
    ("South Florida Water Management District — Upper Kissimmee Basin planning area", "https://www.sfwmd.gov/our-work/water-supply/upper-kissimmee"),
    ("Osceola County — short-term rental listing, revised May 2022", "https://www.osceola.org/files/assets/county/v/1/doing-business/applications/documents/060122_short-term-rental-listing.pdf"),
    ("USDA NRCS — official series description, Myakka series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/M/MYAKKA.html"),
    ("USDA NRCS — official series description, Basinger series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/B/BASINGER.html"),
    ("USDA NRCS — official series description, EauGallie series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/E/EAUGALLIE.html"),
    ("Centrel Services — septic and sewer service area, Harmony, FL", "https://www.centrelservices.com/service-areas/harmony.html"),
    ("Corcoran Connect — Buck Lake in Harmony, FL", "https://www.corcoranconnect.com/blog/buck-lake-in-harmony-fl-another-episode-in-the-love-harmony-florida-series"),
    ("55places.com — The Lakes at Harmony, a 55+ community", "https://www.55places.com/florida/communities/the-lakes-at-harmony"),
    ("Moving to Saint Cloud FL — Harmony neighborhood guide", "https://movingtosaintcloudfl.com/saint-cloud-neighborhoods/harmony/"),
    ("GrowthSpotter — Harmony Central vertical construction", "https://www.growthspotter.com/2022/01/06/vertical-construction-set-to-take-off-in-harmony-central/"),
]

# ============================================================== hub
HUB_BODY = "".join([
    sec("What makes a Harmony yard different",
        "<p>Harmony sits about 17 miles east of downtown Kissimmee on US-192, built as a walkable town rather than a subdivision carved out of a grid. That shapes the turf work three ways: an architectural review step most Osceola towns don't have, a wetter native soil than the ridge country west of St. Cloud, and more lakes, ponds and preserved buffers per acre than almost anywhere else in the county. None of that rules turf out. It changes where the crew starts measuring and which questions get answered before a shovel touches the ground.</p>"
        + f"<p>Central Florida's synthetic turf standard, {src('dep-rule', 'Rule 62-308.100')}, sets the same statewide floor here as it does in Orlando or Poinciana: permeable turf over a washed rock base, capped irrigation heads, and setbacks from trees and water. Harmony layers its own community review on top of that floor, which is the part a homeowner three towns over doesn't have to plan around.</p>"),
    sec("A conservation town built in three waves",
        f"<p>Osceola County's commissioners first approved the land under a different name entirely: the project that became Harmony was cleared for development on October 5, 1992 as \"Birchwood,\" a Development of Regional Impact allowing up to 7,200 residential units {ext('https://www.osceola.org/Doing-Business/Community-and-Economic-Development/DCIs-and-DRIs/Harmony-DRI', 'alongside commercial, office and light-industrial space')}. The Harmony Community Development District organized in March 2000, homes opened for occupancy around 2003, and the Harmony Residential Owners Association followed on October 8, 2002 to run architectural review for the neighborhood {ext('https://en.wikipedia.org/wiki/Harmony,_Florida', 'once residents moved in')}. Starwood Capital Group took over ownership of the unsold land in 2005.</p>"
        + f"<p>That original wave earned Harmony Florida Green Building Coalition certification and a standing research partnership with the University of Florida's Department of Wildlife Ecology and Conservation, begun in 2001 {ext('https://en.wikipedia.org/wiki/Harmony,_Florida', 'to study people and wildlife sharing the same ground')}. Osceola County rescinded the old DRI order on October 17, 2016 and reapproved the property as a standard Planned Development in 2021, which is the paperwork a county reviewer pulls up today rather than the 1992 file.</p>"),
    sec("Buck Lake, Cat Lake and the golf preserve",
        f"<p>Buck Lake, the larger of Harmony's two namesake lakes, runs to roughly 511 acres, with a community park on Panther Lane offering trails, picnic areas and hand-launched kayak or canoe access rather than a public boat ramp {ext('https://www.corcoranconnect.com/blog/buck-lake-in-harmony-fl-another-episode-in-the-love-harmony-florida-series', 'and a low-speed-only rule')}. Cat Lake feeds a chain running through Lake Conlin and Lake Lizzie before reaching Alligator Lake, part of the upper Kissimmee lake system, and isn't open to the public at all.</p>"
        + f"<p>Harmony Golf Preserve wraps 260 acres of existing wetlands, pine flatwoods and natural ponds, and the course was laid out so no home sites front directly onto the fairways {ext('https://harmonygolfpreserve.com/', 'the way many Florida golf communities are built')}. A handful of yards still back up to the preserve's buffer rather than a mowed rough, which matters more for excavation than for the view.</p>"),
    sec("Harmony West, Sunbridge and the town's newest corner",
        f"<p>The original village kept growing: Harmony West's Community Development District organized in 2017 to carry utilities and roads into the next phase {ext('https://www.osceola.org/agencies-departments/community-development-districts/harmony-west-cdd/', 'west of the founding neighborhoods')}, and a 268-acre tract called Harmony Central, bought by developer FMDC in 2019, is filling in with 522 more single-family lots across three phases {ext('https://www.growthspotter.com/2022/01/06/vertical-construction-set-to-take-off-in-harmony-central/', 'built out by Adams Homes and connected to the town center by trail')}.</p>"
        + f"<p>Just north, Tavistock Development Company opened Sunbridge in 2020, a separate master plan spanning more than 27,000 acres across Orange and Osceola counties, with Weslyn Park as its first finished village {ext('https://en.wikipedia.org/wiki/Sunbridge,_Florida', 'and more neighborhoods following')}. None of that is Harmony proper, but it's the new construction a Harmony-area crew runs into most weeks, and it comes with builder-graded lots rather than twenty-year-old sod.</p>"),
    sec("What changes across Harmony's yard types",
        "<p>Six lot types cover most of what a crew finds between the original town square and the newest phases. The table gives the short version; the service pages below go deeper on each one.</p>"
        + table("Harmony yard types and what we do differently",
                ["Where in Harmony", "Why it's different", "How the job changes"],
                [["Original village lots (built roughly 2003–12)", "Narrow New Urbanism lots, alley-loaded garages, mandatory design review for any exterior change", "File the plan with the Residential Owners Association before ordering material, not after"],
                 ["Lots backing Buck Lake, Cat Lake or a stormwater pond", "State rule keeps synthetic turf at least 10 feet from the water's edge and out of any swale", "Hold that 10-foot line and fill the gap with planting bed instead of guessing at a shorter setback"],
                 ["Lots near Harmony Golf Preserve's buffer", "The course wraps wetlands and ponds, so a buffer line can sit closer than the property survey suggests", "Check the preserve's edge on site before excavation begins, not just the plat"],
                 ["The Lakes at Harmony, a 55+ neighborhood built from 2016", "Smaller lots, an HOA-run clubhouse and trail system, owners who want less mowing without a lawn crew", "Size the job to a compact lot and skip retrofits a small yard doesn't need"],
                 ["New construction in Harmony West, Harmony Central and neighboring Sunbridge", "Builder-graded lots on trucked-in fill, sod that's rarely more than a season old", "Test how the yard already drains before deciding whether the base needs extra depth"],
                 ["Larger, rural-edge parcels along US-192 outside the CDD boundary", "Some run on septic rather than a central sewer connection", "Build a hinged or removable panel over the tank's access lid instead of covering it for good"]],
                "Based on our own review of each area's public records and plats, September 2026.")),
    sec("Water, soil and why the base still decides the outcome",
        f"<p>Toho Water Authority serves the Harmony area and is currently doubling the Harmony Water Treatment Plant's capacity to 2.6 million gallons a day to keep pace with the newer phases {ext('https://www.tohowater.com/news/harmony-water-treatment-plant-upgrades-expansion', 'as the community fills in')}. Toho's countywide watering schedule, odd-numbered addresses on Wednesday and Saturday and even-numbered addresses on Thursday and Sunday with no daytime hours, stops applying to a section of yard once its irrigation heads are capped {src('toho-days', 'under the state standard')}. Eastern Osceola County sits inside the Central Florida Water Initiative area, where the South Florida, St. Johns River and Southwest Florida water districts all meet, and Harmony's own chain of lakes drains toward the upper Kissimmee basin that {ext('https://www.sfwmd.gov/our-work/water-supply/upper-kissimmee', 'the South Florida district manages')}.</p>"
        + f"<p>Underneath that water sits flatwoods soil that stays wet longer than the sandy ridge on the Polk County line. Federal soil surveys classify the poorly to very poorly drained series common in this part of the county, Myakka, Basinger and EauGallie among them, with a seasonal water table that can sit within 18 inches of the surface for one to four months a year {ext('https://soilseries.sc.egov.usda.gov/OSD_Docs/M/MYAKKA.html', 'and even longer in low spots')}. A base built at the shallow end of the state's two-to-four-inch range barely clears that, so most Harmony installs lean toward the fuller depth.</p>"),
    sec("Permits, the Residential Owners Association and your paperwork",
        f"<p>Harmony has never been annexed by a city, so a Building Department review runs through {a('/laws/permits/osceola-county/', 'unincorporated Osceola County, not St. Cloud or Kissimmee')}. On top of that, every exterior change in Harmony, turf included, goes through the Residential Owners Association's design review before work starts. We could not find the association's guidelines published with specific wording about synthetic turf as of September 2026, which means the safest path is a plan submitted ahead of the truck showing up, not an assumption either way.</p>"
        + f"<p>{a('/laws/hoa-rules/', 'Florida law limits what any homeowners association can restrict')}, and a fenced backyard not visible from the street or a neighboring lot gets the strongest protection under that statute. {a('/laws/florida-hb-683/', 'The state turf rule')} sets the material and drainage floor no local board can undercut. Our {a('/tools/hoa-packet-checklist/', 'HOA packet checklist')} lists what to hand the review committee in one submission instead of three.</p>"),
    sec("Vacation rentals and the golf-course lots",
        f"<p>Osceola County's own list of neighborhoods zoned for short-term rental, more than 240 subdivisions clustered around the theme-park corridor and Poinciana, doesn't include Harmony {ext('https://www.osceola.org/files/assets/county/v/1/doing-business/applications/documents/060122_short-term-rental-listing.pdf', 'as of its most recent revision')}. Most Harmony homes are owner-occupied or long-term rentals rather than nightly stays, so turf sized for a vacation-rental turnover schedule is a small slice of the work here compared with the resort corridor closer to the parks.</p>"
        + "<p>Homeowners searching for the best artificial turf installer near Harmony usually start with the same short list of questions: who has actually measured a lot against the golf preserve's buffer, who knows the Residential Owners Association's submission process, and who will hold the ten-foot lake line without being asked twice.</p>"),
    "<!--AUTO:city-services-->",
])

HUB = page(
    "/areas/harmony/", "city",
    "Artificial Turf in Harmony, FL: Lakes, ROA Review, Wet Soil",
    "Artificial turf in Harmony, FL works around the ROA's design review, a 10-ft lake setback and wet flatwoods soil. Local facts, rules and pricing, September 2026.",
    "Turf built for Harmony's lakes, review board and soil",
    capsule("Harmony is an unincorporated conservation community in eastern Osceola County, about 17 miles from downtown Kissimmee, built around Buck Lake, Cat Lake and a 260-acre golf preserve. Installed turf here runs " + price("residential") + " per square foot as of September 2026. What changes the job is the Residential Owners Association's design review, the 10-foot waterbody setback and flatwoods soil with a high seasonal water table."),
    HUB_BODY,
    faqs=[
        faq("Does Harmony's homeowners association have to approve artificial turf?",
            "Every exterior change in Harmony goes through the Residential Owners Association's design review, and turf should go through the same process as a fence or a paint color. We haven't found the association's written guidelines addressing turf specifically, so submit a plan before ordering material rather than assuming approval either way."),
        faq("Who handles building permits for a Harmony address?",
            "Harmony has never been part of a city, so unincorporated Osceola County's Building Department reviews the permit, separate from the Residential Owners Association's design approval. Our Osceola County permit page has the department's contact information and what's published about synthetic turf."),
        faq("Does Toho Water Authority serve Harmony, and does that change the job?",
            "Yes. Toho is currently expanding the Harmony Water Treatment Plant to keep pace with growth. A turf area's irrigation heads get capped regardless of the utility, since the state standard bars watering synthetic turf from an in-ground system."),
        faq("Can turf go right up to Buck Lake or Cat Lake?",
            "No. State rule keeps synthetic turf at least 10 feet back from a lake, pond or canal's edge unless a seawall already separates the two, and bars turf inside a drainage swale entirely. Buck Lake's shoreline and any stormwater pond in the community follow the same setback."),
        faq("Is Harmony zoned for short-term vacation rentals?",
            "Osceola County's list of neighborhoods approved for short-term rental doesn't include Harmony as of our September 2026 check, unlike much of the corridor closer to the theme parks. Most Harmony properties operate as long-term or owner-occupied homes instead."),
    ],
    sources=SRC, city=SLUG,
    crumbs=[("Service areas", "/areas/")], crumb="Harmony",
    related=[
        ("/laws/permits/osceola-county/", "Artificial turf permits in Osceola County"),
        ("/laws/hoa-rules/", "What a Florida HOA can and can't restrict"),
        ("/laws/florida-hb-683/", "Florida HB 683 and the DEP synthetic turf rule"),
        ("/tools/hoa-packet-checklist/", "HOA / ARC application checklist for artificial turf"),
        ("/areas/st-cloud/", "Artificial turf in St. Cloud"),
        ("/areas/narcoossee/", "Artificial turf in Narcoossee"),
        ("/areas/kissimmee/", "Artificial turf in Kissimmee"),
        ("/areas/lake-nona/", "Artificial turf in Lake Nona"),
        ("/artificial-turf-cost/", "Turf cost tables for Central Florida"),
        ("/blog/artificial-turf-near-live-oaks-and-palms/", "Will artificial turf hurt live oaks or palm roots?"),
    ],
)

# ============================================================== local
LOCAL = {}

LOCAL["residential"] = {
    "title": "Artificial Grass Installation in Harmony, FL: ROA Review",
    "meta": "Artificial grass in Harmony, FL means clearing the ROA's design review on a New Urbanism lot over wet flatwoods soil. Local facts and pricing, September 2026.",
    "h1": "A residential lawn built for Harmony's review board and soil",
    "lede": capsule("A residential lawn in Harmony runs " + price("residential") + " per square foot installed as of September 2026, the same range as anywhere else in Central Florida. What's local is the process: a Residential Owners Association design review on a narrow, alley-loaded lot, plus EauGallie or Myakka soil that holds water within 18 inches of the surface for months at a stretch."),
    "sections": [
        ("How the original village lots are built",
         f"<p>Harmony's founding neighborhoods were laid out as a walkable town, not a standard subdivision: short front setbacks, porches close to the sidewalk, and garages fed from a rear alley rather than the street {ext('https://movingtosaintcloudfl.com/saint-cloud-neighborhoods/harmony/', 'so the front yard reads as part of the streetscape')}. That design squeezes the usable lawn into a smaller footprint than a typical suburban lot carries, and it puts a fence line and a neighbor's window within easy sightline of almost any yard. Practically, that means more of a Harmony Main lawn counts as visible from the street or an adjacent parcel than would on a wider, deeper lot, which changes how {a('/laws/hoa-rules/', "the state's HOA-visibility statute")} applies to a front-yard project here versus a fenced backyard three towns over.</p>"),
        ("Reading the ROA's design review before ordering material",
         f"<p>Every exterior change to a Harmony home, turf included, needs sign-off from the Residential Owners Association before work begins. We searched for the association's published landscape standards and could not confirm specific wording on synthetic turf as of September 2026, so treat the review as a real step rather than a formality: submit a simple plan showing the turf area, the product and the edging before a crew is scheduled. {a('/tools/hoa-packet-checklist/', 'A one-page packet')} with those three items tends to move faster than a phone call asking permission after the fact.</p>"),
        ("Building the base over EauGallie and Myakka soil",
         f"<p>Federal soil surveys map EauGallie and Myakka series soil under much of Harmony, both poorly to very poorly drained, with a water table federal researchers describe as sitting within {ext('https://soilseries.sc.egov.usda.gov/OSD_Docs/E/EAUGALLIE.html', 'six to eighteen inches of the surface for one to four months a year')}. A base at the thin end of the state's two-to-four-inch washed-rock range barely clears that saturation zone during a wet summer, so a Harmony lawn usually gets built toward the fuller depth rather than the minimum. {svc('residential', 'The residential turf guide')} covers what goes into that base on any Central Florida lot, not just here.</p>"),
    ],
    "scenario": ("What a typical Harmony Main backyard runs",
                 f"<p>Say a 1,150 sq ft backyard behind a two-story New Urbanism home near the town square is losing grass along the alley fence where the garage blocks afternoon sun. At {price('residential')} a square foot, that's roughly $9,200 to $20,700 for the full yard, with most jobs at this size landing between $11,500 and $18,400 using the typical $10–$16 band. Because the lot backs a shared alley rather than a private rear yard, the fence line sits close enough to a neighbor's sightline that the project counts as visible under {a('/laws/hoa-rules/', "the state's HOA statute")}, so the Residential Owners Association's design review applies the same as it would to a front porch repaint, not just a fenced-in backyard out of view.</p>"),
    "faqs": [
        faq("Does a Harmony ROA design review cost anything?",
            "Nothing published suggests a review fee specific to landscaping changes, but confirm directly with the association since fee schedules can change; the bigger cost is time if a plan isn't submitted before material is ordered."),
        faq("Is a Harmony lawn's soil worse than St. Cloud's for turf?",
            "Not worse, just wetter. Myakka and EauGallie hold water closer to the surface for longer stretches than the sandier ridge soils west of town, which is a base-depth decision, not a reason to skip turf."),
    ],
    "sources": SRC,
}

LOCAL["pet"] = {
    "title": "Pet Turf & Dog Runs in Harmony, FL",
    "meta": "Pet turf in Harmony, FL fits narrow alley-loaded lots and the community's wildlife-coexistence rules. Local facts, drainage notes and pricing, September 2026.",
    "h1": "Dog runs sized for Harmony's narrow lots",
    "lede": capsule("Pet turf in Harmony runs " + price("pet") + " per square foot installed as of September 2026. Harmony's Residential Owners Association wrote wildlife coexistence into its founding documents back in 2002, and its narrow, alley-loaded lots leave less room for a dog run than a standard suburban yard, so drainage and placement matter more here than the infill choice."),
    "sections": [
        ("A community that wrote wildlife coexistence into its rules",
         f"<p>Harmony's Residential Owners Association is unusual among Florida HOAs for building guidelines about living alongside local wildlife into its founding paperwork back in 2002 {ext('https://en.wikipedia.org/wiki/Harmony,_Florida', 'rather than treating it as an afterthought')}. That doesn't change anything about how a dog run gets installed, but it does mean a fenced pet area backing a preserve buffer or a lake edge is worth keeping tidy and odor-controlled, since Harmony residents notice a yard that draws raccoons or attracts flies more than most.</p>"),
        ("Fitting a run into an alley-loaded lot",
         f"<p>Harmony's original streets were platted with rear alleys feeding the garages, which leaves a narrower side or back strip for a dog run than a conventional subdivision lot offers {ext('https://movingtosaintcloudfl.com/saint-cloud-neighborhoods/harmony/', 'built around front-loaded driveways instead')}. A run along that alley fence usually measures under 300 square feet, tight enough that drainage at the low end matters more than it would on a wide-open lawn, since there's less soil area to absorb a fast rinse-down after a dog uses it.</p>"),
        ("Skipping the weed barrier, adding the right infill",
         "<p>A pet area skips the optional weed-fabric layer a plain lawn might use, since fabric under a dog run traps urine at the surface instead of letting it filter into the base rock below. Zeolite or coated silica sand handles odor control within the state's material rule, which limits infill on any residential lot, dog runs included, to sand, rock, shell or a non-toxic coated product. Rubber crumb, sometimes marketed for pet areas elsewhere, isn't an option on an open Harmony yard under that same rule.</p>"),
    ],
    "scenario": ("Say you have a 260 sq ft alley-side run",
                 "<p>A 260 sq ft strip along the garage alley, fenced for two dogs, prices between $2,600 and $4,680 at the published " + price("pet") + " range, with most jobs this size landing near $3,120 to $4,160 using the typical $12–$16 band. That figure includes the deeper drainage base a run this size needs and zeolite infill brushed in at roughly a pound and a half per square foot. Because the alley sits behind the garage rather than facing the street, the run is unlikely to be visible from the front, which usually simplifies the Residential Owners Association's design review compared with a front-yard project.</p>"),
    "faqs": [
        faq("Will a dog run near Harmony's conservation areas need extra approval?",
            "If the run backs a preserve buffer or the golf course edge rather than another yard, mention that in the design review submission; the association's own review covers placement, and the state's drip-line rule can apply separately if mature oaks sit nearby."),
        faq("Does Harmony's wildlife-coexistence guidance restrict fencing for a dog run?",
            "We found no published fencing restriction tied specifically to wildlife coexistence, only the general architectural review every fence goes through regardless of purpose. Confirm fence height and material with the association before building the run's enclosure."),
    ],
    "sources": SRC,
}

LOCAL["putting"] = {
    "title": "Backyard Putting Greens in Harmony, FL",
    "meta": "A backyard putting green in Harmony, FL suits lots near the 260-acre golf preserve or The Lakes at Harmony's 55+ section. Pricing and local facts, Sept. 2026.",
    "h1": "A putting green for a Harmony golf-community lot",
    "lede": capsule("A backyard putting green in Harmony runs " + price("putting") + " per square foot installed as of September 2026. Harmony Golf Preserve's 260 acres of wetlands and ponds shape which lots back the course, and The Lakes at Harmony, a 55+ neighborhood built since 2016, adds owners who want a green without a membership."),
    "sections": [
        ("Building near a course laid out around wetlands, not homes",
         f"<p>Harmony Golf Preserve was routed through 260 acres of existing wetlands, pine flatwoods and natural ponds with no home sites built directly against the fairways {ext('https://harmonygolfpreserve.com/', 'unlike many Florida golf communities')}. That means a putting green project here is rarely about matching a literal fairway view; it's about a lot that sits near the preserve's buffer rather than on top of it. Checking that buffer line on the ground, not just on the plat, is worth doing before excavation starts on any lot within a few hundred feet of the course.</p>"),
        ("A green built for The Lakes at Harmony's 55+ lots",
         f"<p>The Lakes at Harmony, a 55-and-over section with roughly 400 planned homes built since 2016, sits on smaller lots than Harmony's original village and gives residents access to the community's 18-hole course along with its own clubhouse and trail network {ext('https://www.55places.com/florida/communities/the-lakes-at-harmony', 'without requiring a membership for every household')}. A compact green with a chipping pad fits that lot size well, giving an owner practice space without hauling clubs to the course for every short session.</p>"),
        ("Contouring and drainage on flatwoods ground",
         "<p>A true-roll green needs a shaped subsurface, not a flat pad, and on Harmony's poorly drained flatwoods soil that shaping has to move water off the contours rather than let it pool in a low cup placement. Fringe turf around the putting surface uses a shorter, denser product than the green itself, and both sit on the same washed-rock base as a residential lawn, just built with tighter grading tolerances to hold a consistent stimp.</p>"),
    ],
    "scenario": ("Say you have a 420 sq ft green with a 150 sq ft fringe",
                 f"<p>A 420 sq ft contoured green with a 150 sq ft fringe, 570 sq ft total, on a Lakes at Harmony lot prices between $7,980 and $17,100 at the published {price('putting')} range, with most jobs this size landing near $10,260 to $14,250 using the typical $18–$25 band. The wider spread reflects how much the number of cups, contour breaks and chipping-pad grading change the labor, more than it reflects the turf itself. Homeowners asking who installs the best putting green near Harmony usually mean someone who has actually graded a green on this soil, not just a flat lawn.</p>"),
    "faqs": [
        faq("Does a putting green near Harmony Golf Preserve need the course's approval?",
            "The course itself doesn't review private yard projects; the Residential Owners Association's design review does, the same as for any other exterior change. If the lot borders the preserve's own buffer, plan on that distance being checked before any excavation."),
        faq("Can The Lakes at Harmony's smaller lots fit a full-size green?",
            "Most can fit a compact contoured green with two or three cups rather than a full-scale layout; a site visit settles the actual usable footprint once the pool cage, AC pad and setbacks are subtracted."),
        faq("Do putting greens in Harmony use different infill than a lawn?",
            "Yes. A green typically uses a finer, more consistent silica sand than a residential lawn's infill, brushed in to a tighter tolerance so ball roll stays predictable across the surface."),
    ],
    "sources": SRC,
}

LOCAL["playground"] = {
    "title": "Playground Turf for Harmony, FL Backyards",
    "meta": "Playground turf in Harmony, FL fits new Harmony Central and Weslyn Park backyards and older village lots alike. Pricing, safety notes and local facts, Sept. 2026.",
    "h1": "Play surfaces for Harmony's newest family neighborhoods",
    "lede": capsule("Playground turf in Harmony runs " + price("playground") + " per square foot installed as of September 2026. Harmony Central's 522 new lots and Weslyn Park next door in Sunbridge are filling with young families, and a shock-pad play surface suits those backyards as well as it does an older lot near Buck Lake Park."),
    "sections": [
        ("New lots filling with families in Harmony Central",
         f"<p>Developer FMDC bought 268 acres in 2019 to build Harmony Central's 522 single-family lots across three phases, with Adams Homes as the first builder and a trail connecting the new section back to the original town center {ext('https://www.growthspotter.com/2022/01/06/vertical-construction-set-to-take-off-in-harmony-central/', 'and its golf clubhouse')}. Backyards here arrive with builder sod on freshly graded fill, which looks fine the first season and then struggles once the lot settles, a common reason families in a section this new start asking about a play surface within a year or two of moving in.</p>"),
        ("Weslyn Park and Sunbridge next door",
         f"<p>Just north of Harmony, Tavistock's Sunbridge opened in 2020 across more than 27,000 acres in Orange and Osceola counties, with Weslyn Park as its first completed neighborhood {ext('https://en.wikipedia.org/wiki/Sunbridge,_Florida', 'and more villages following behind it')}. It isn't Harmony proper, but it's close enough that a Harmony-area crew installs there routinely, and the backyards run the same builder-grade sod and drainage questions a new Harmony Central lot does.</p>"),
        ("Sizing the shock pad to the equipment",
         "<p>A play structure's fall height sets the shock-pad thickness underneath it, not the other way around, so the pad spec has to match whatever swing set or climbing structure is going in before the turf gets ordered. A backyard set with a five-foot platform needs a thicker pad than a toddler-height slide, and skimping on that thickness to save on the job is the kind of shortcut that shows up as a hard landing rather than a bad-looking lawn.</p>"),
    ],
    "scenario": ("Say you have a 300 sq ft play area in Harmony Central",
                 f"<p>A 300 sq ft play area behind a new Harmony Central home, sized for a swing set with a four-foot fall height, prices between $3,000 and $7,500 at the published {price('playground')} range, with most jobs this size landing near $3,600 to $5,700 using the typical $12–$19 band. That range covers a shock pad matched to the equipment's fall height along with the turf and edging. Because the lot is new construction, there's no old sod to strip first, which is one less step than a play-area conversion on an older Harmony Main lawn.</p>"),
    "faqs": [
        faq("Does builder sod in Harmony Central need to be removed before playground turf goes in?",
            "Yes, the same as any sod, though on a lot graded within the past year or two the strip-out is usually faster since the root mat hasn't had time to establish as deeply as older grass."),
        faq("Is playground turf near Buck Lake Park subject to the lake setback?",
            "Only if the play area itself sits within 10 feet of the water's edge or another waterbody on the property; a backyard play surface away from any lake or pond isn't affected by that rule."),
    ],
    "sources": SRC,
}

LOCAL["pool"] = {
    "title": "Pool & Lanai Turf for Harmony, FL Screen Enclosures",
    "meta": "Pool and lanai turf in Harmony, FL handles screen enclosures near lake lots and Basinger soil that ponds after rain. Local facts and pricing, September 2026.",
    "h1": "Turf for a Harmony pool cage on wet ground",
    "lede": capsule("Turf around a Harmony pool or inside a screen lanai runs " + price("residential") + " per square foot installed as of September 2026, toward the higher end of that range for tight, glue-down work. Basinger soil under much of the community ponds for months after a wet season, and lots backing Buck Lake, Cat Lake or a stormwater pond carry the state's 10-foot waterbody setback on top of that."),
    "sections": [
        ("Basinger soil and a pool deck that never quite dries",
         f"<p>Basinger series soil, mapped in low flats and poorly defined drainageways around Harmony, is rated very poorly drained, with a seasonal water table federal surveys place within {ext('https://soilseries.sc.egov.usda.gov/OSD_Docs/B/BASINGER.html', 'zero to eighteen inches of the surface and standing water for six to nine months in a typical year')} in the lowest spots. A pool deck built on that ground without enough fall away from the cage can hold water along the screen track long after a storm passes, which is worth checking before turf goes down around the perimeter, not after.</p>"),
        ("Working inside the screen without disturbing the frame",
         "<p>Turf laid inside an existing pool cage has to work around the aluminum frame's footers and the screen track without cutting into either, which usually means hand tools instead of a compactor for the last foot or two along every wall. A drainage underlay under the turf where it meets the pool deck keeps splash-out water moving instead of pooling against the screen frame, a detail that matters more on Harmony's flatter, wetter lots than it would on a well-drained ridge lot.</p>"),
        ("The 10-foot rule on a lake or pond lot",
         f"<p>A lot backing Buck Lake, Cat Lake or one of Harmony's many stormwater ponds carries the same 10-foot waterbody setback as anywhere else in Florida under {src('dep-rule', 'the state standard')}, measured from the ordinary water line unless a seawall separates the two. Pool and lanai turf rarely reaches that far toward the water on its own, but a broader backyard renovation that ties the pool deck into a rear lawn near the water needs that line held the same as a lawn-only project would.</p>"),
    ],
    "scenario": ("Say you have a 480 sq ft lanai ring in Harmony West",
                 f"<p>A 480 sq ft ring of turf inside a screened lanai on a Harmony West pool home, tight against the cage frame on three sides, prices near the top of the {price('residential')} range given the hand-work involved, roughly $7,200 to $8,640 at $15–$18 a square foot. That's higher per foot than an open backyard of the same size would run, because the glue-down edges along the screen track and the drainage underlay both add labor a wide-open lawn doesn't need. The pool itself and the paved deck aren't part of that square footage.</p>"),
    "faqs": [
        faq("Does a pool cage in Harmony need its own drainage plan for turf?",
            "Not a formal plan, but the installer should grade the small strip of turf around the deck so water moves away from the screen frame, especially on Basinger soil that already holds water longer than sandier ground nearby."),
        faq("Can turf inside a Harmony lanai touch the pool deck's expansion joint?",
            "It's better to stop turf at the joint with a clean edge rather than glue across it, since the joint is there to let the deck and the cage's footers move independently during ground settling."),
    ],
    "sources": SRC,
}

LOCAL["str"] = {
    "title": "Vacation Rental Turf: Harmony, FL's Small Market",
    "meta": "Vacation rental turf in Harmony, FL is a small market since the county's short-term rental overlay doesn't reach this far east. What that means, Sept. 2026.",
    "h1": "Why vacation-rental turf is rare in Harmony",
    "lede": capsule("Turf for a vacation-rental yard in Harmony runs " + price("residential") + " per square foot installed as of September 2026. Osceola County's list of neighborhoods zoned for short-term rental doesn't reach this far east of St. Cloud, so most Harmony homes function as long-term or owner-occupied properties rather than nightly rentals."),
    "sections": [
        ("Checking the county's own list",
         f"<p>Osceola County keeps a running list of subdivisions approved for short-term rental use, more than 240 of them as of its most recent revision, clustered around the theme-park corridor west of Kissimmee and the Poinciana area {ext('https://www.osceola.org/files/assets/county/v/1/doing-business/applications/documents/060122_short-term-rental-listing.pdf', "not the town's eastern half")}. Harmony doesn't appear anywhere on that list, which means a Harmony property operating as a nightly rental would be doing so outside the county's designated overlay rather than inside it, a zoning question worth running past the county directly before marketing a home that way.</p>"),
        ("Who's actually asking for it here",
         "<p>The handful of Harmony requests for rental-ready turf tend to come from owners renting a home for weeks or months at a time, not nightly guests, since Harmony's draw is the town itself rather than proximity to the parks. That changes the priority list: durability under a rotating cast of tenants and pets matters more than surviving back-to-back weekend turnovers, so the infill and product choice can lean toward standard residential grade instead of the heavier-traffic spec a nightly rental near the resort corridor typically needs.</p>"),
        ("Toho service for a rental property",
         f"<p>Toho Water Authority serves rental and owner-occupied homes in Harmony the same way, and the utility is mid-expansion on the Harmony Water Treatment Plant to keep pace with the area's growth {ext('https://www.tohowater.com/news/harmony-water-treatment-plant-upgrades-expansion', 'as more phases fill in')}. For a rental property, that mainly matters at turnover: a capped irrigation zone under turf means no sprinkler timer for a property manager to reset between guests, one less thing to go wrong on a fast changeover.</p>"),
    ],
    "scenario": ("Say you have a 900 sq ft yard on a long-term rental",
                 f"<p>A 900 sq ft yard behind a Harmony home rented on a months-long lease rather than nightly stays prices between $7,200 and $16,200 at the published {price('residential')} range, with most jobs landing near $9,000 and $14,400 using the typical $10–$16 band. Because the property isn't inside the county's short-term rental overlay, there's no separate rental-zoning review layered on top of the usual permit and Residential Owners Association steps; the same process applies as it would for an owner-occupied home on the same street.</p>"),
    "faqs": [
        faq("Can a Harmony homeowner apply for short-term rental status even though it's not on the county's list?",
            "That's a zoning question for Osceola County's Planning department, not something turf installation changes either way; confirm with the county before marketing a Harmony property for nightly stays."),
        faq("Does turf help a long-term rental in Harmony more than a short-term one?",
            "It tends to, since a long-term or owner-occupied yard in Harmony sees steadier, lower-intensity use than a nightly-turnover property near the parks would, so the upkeep savings show up more evenly over the year."),
    ],
    "sources": SRC,
}

LOCAL["commercial"] = {
    "title": "Commercial Turf for Harmony, FL's Town Center",
    "meta": "Commercial turf in Harmony, FL fits CDD common areas and the town center's apartment and retail expansion. Local facts and how pricing works, September 2026.",
    "h1": "Turf for Harmony's town center and HOA common ground",
    "lede": capsule("Commercial turf in Harmony is quoted per job from a site visit and drawings rather than a flat per-square-foot rate. Between the Community Development District's common areas, a reported $65 million apartment and retail expansion at the town center, and clubhouse grounds at The Lakes at Harmony, most of the work here isn't a single-family lawn at all."),
    "sections": [
        ("A town center mid-transformation",
         f"<p>Harmony's original town square, built around shops and a golf clubhouse when the community opened, is under new ownership pursuing a reported $65 million apartment and retail expansion {ext('https://www.growthspotter.com/2022/01/06/vertical-construction-set-to-take-off-in-harmony-central/', 'separate from the newer Harmony Central housing phases nearby')}. A project at that scale typically brings turf into the picture for courtyards, dog-relief areas built into a multifamily podium, and street-facing planters where live grass would need a maintenance crew the property doesn't want to carry.</p>"),
        ("What the CDD and HOA common areas need",
         f"<p>Harmony's Community Development District organized in 2000 to maintain the town's shared infrastructure, and Harmony West's district followed in 2017 as the community grew {ext('https://www.osceola.org/agencies-departments/community-development-districts/harmony-west-cdd/', 'to cover the newer phase separately')}. Entry medians, clubhouse lawns and the common-area strips between a sidewalk and a preserve buffer are exactly the kind of ground where a district board weighs turf against a mowing contract, since the math on either changes with acreage rather than staying fixed the way a homeowner's yard does.</p>"),
        ("Why commercial jobs get quoted, not priced per foot",
         "<p>A single-family lawn's per-square-foot range assumes straightforward access and a residential base spec; a commercial site rarely offers either. Drainage plans, ADA-compliant surfacing around a pool deck, and a property manager's own maintenance schedule all change the bid more than square footage alone does, which is why commercial work gets quoted from drawings and a site walk instead of a published rate.</p>"),
    ],
    "scenario": ("Say a clubhouse courtyard needs 1,100 sq ft of low-maintenance ground",
                 "<p>A 1,100 sq ft courtyard at an HOA clubhouse, framed by a walkway on two sides and a retention pond edge on the third, needs the same 10-foot waterbody setback a residential yard would if any section runs close to the pond. Because the area mixes hardscape, planting beds and turf rather than one continuous lawn, the actual turf footprint often comes in under the full 1,100 sq ft once beds and pavers are subtracted, which is part of why a walkthrough measurement matters more here than an estimate from a site plan alone.</p>"),
    "faqs": [
        faq("Does Harmony's CDD install turf itself or hire out the work?",
            "That's a decision for the district's own board and budget process, not something a private installer can answer generally; a district considering turf for common areas would typically solicit bids the same way it would for any capital project."),
        faq("Is commercial turf near Harmony's town center subject to the same state rule as a residential lawn?",
            "The state's synthetic turf standard specifically covers single-family residential lots of an acre or less, so a commercial or multifamily site like the town center expansion falls outside that particular rule and answers to the county's ordinary commercial permitting instead."),
    ],
    "sources": SRC,
}

LOCAL["sports"] = {
    "title": "Sports & Fitness Turf in Harmony, FL",
    "meta": "Sports and fitness turf in Harmony, FL adds a private practice lane alongside the community's own tennis, pickleball and bocce courts. Facts and pricing, Sept. 2026.",
    "h1": "A private practice lane beside Harmony's own courts",
    "lede": capsule("Sports and fitness turf in Harmony is quoted per job once the lane's length, width and intended use are set. The Lakes at Harmony already runs its own tennis, pickleball and bocce courts along 12.6 miles of trail, and homeowners who want to train at home rather than walk to the clubhouse are the ones who typically ask about this."),
    "sections": [
        ("Community courts already exist, so why build a private lane",
         f"<p>The Lakes at Harmony's clubhouse grounds include tennis, pickleball and bocce courts connected by 12.6 miles of walking and biking trail, all part of the HOA-maintained common areas that come with the neighborhood {ext('https://www.55places.com/florida/communities/the-lakes-at-harmony', 'rather than something an individual owner installs')}. A private backyard sports surface isn't competing with that; it's for daily reps that don't require getting in the car, a batting tee session before dinner or an agility drill with the dog that doesn't need a reserved court time.</p>"),
        ("Sizing a lane to Harmony's narrower lots",
         "<p>A batting cage lane or an agility course has to fit inside whatever strip of yard a Harmony lot actually offers, which on the original village's alley-loaded lots is often a side yard rather than a wide-open backyard. A lane 8 to 10 feet wide and 30 to 40 feet long fits most of those side strips without crowding the fence, and the turf spec for that use runs a shorter, denser pile than a residential lawn so footing stays consistent under repeated sprints.</p>"),
        ("Base work for repeated impact, not foot traffic alone",
         "<p>A sports surface takes more concentrated, repeated impact in one direction than a lawn does, which is why the base under a batting lane or an agility strip usually gets compacted with less tolerance for settling than a plain backyard would need. Skipping that extra compaction pass to save a day on the schedule is the kind of shortcut that shows up as a soft spot exactly where a batter's back foot lands every swing.</p>"),
    ],
    "scenario": ("Say you have a 320 sq ft side-yard lane",
                 "<p>An 8-by-40-foot side-yard lane, 320 sq ft, along an alley-loaded Harmony lot leaves roughly 60 percent of a typical 800 sq ft side strip still open for storage or a gate path once the lane itself is laid out. Because the lane runs narrower than a standard lawn project, quoting it per job accounts for the extra compaction and the denser turf spec rather than trying to force a square-footage rate meant for an open backyard onto a use case built around repeated impact in one direction.</p>"),
    "faqs": [
        faq("Does a home batting cage in Harmony need Residential Owners Association approval?",
            "Any structure or surface change visible from the street or a neighboring lot, netting included, should go through the association's design review before installation, the same as a fence or a shed would."),
        faq("Can sports turf go inside an alley-loaded lot's rear setback?",
            "That depends on the specific lot's setback lines, which vary by phase and plat; check the survey before finalizing a lane's length near the alley or rear property line."),
    ],
    "sources": SRC,
}

LOCAL["pavers"] = {
    "title": "Turf Between Pavers on a Harmony, FL Lot",
    "meta": "Turf between pavers in Harmony, FL suits the town's front-porch walkways and alley-loaded paths. What it costs and how it's built, September 2026.",
    "h1": "Turf ribbons for a New Urbanism front walk",
    "lede": capsule("Turf set between pavers in Harmony is quoted per job based on the pattern and total run of joints rather than a flat rate. Harmony's front-porch walkways and alley-loaded paver paths, part of the town's original New Urbanism design, give this combination more use here than a typical cul-de-sac subdivision would."),
    "sections": [
        ("Why paver-and-turf shows up more in Harmony's original design",
         f"<p>Harmony's founding neighborhoods were built with short front setbacks, porches near the sidewalk and a paver or stamped-concrete path often running from the sidewalk to the porch steps {ext('https://movingtosaintcloudfl.com/saint-cloud-neighborhoods/harmony/', 'as part of the walkable street design')}. A narrow turf ribbon running between paver courses on that kind of path softens the hardscape without competing with the porch planting beds most owners keep along the front of the house, and it holds up better than mulch does against foot traffic to the front door.</p>"),
        ("Where the alley changes the layout",
         "<p>Because garages sit off a rear alley on most original Harmony lots, the paved path most owners actually walk daily runs from the alley to a side or back door, not from the street. Turf between pavers along that alley path takes more regular foot and occasionally vehicle-adjacent traffic than a front walkway would, so the joints need a slightly firmer base and a lower-profile turf than a decorative front-walk strip calls for.</p>"),
        ("Cutting turf to a paver pattern without wasted material",
         "<p>Turf comes in rolls with the grain running one direction, which means a herringbone or basket-weave paver pattern generates more offcuts than a simple running-bond layout does, since each joint segment has to be cut to match the angle of the pattern around it. Planning the cuts against a single roll's width before installation starts keeps the grain consistent across every joint, which matters more visually on a paver ribbon than it would across an open lawn where the eye doesn't track a straight edge as closely.</p>"),
    ],
    "scenario": ("Say you have a 90 sq ft alley path in turf ribbons",
                 "<p>A 90 sq ft alley path, roughly 3 feet wide by 30 feet long, laid with pavers and 18-inch turf ribbons between courses, uses about one-third the turf a comparable open strip that size would need, since the pavers themselves cover most of the footprint. That smaller turf quantity is part of why the job gets quoted rather than priced by the square foot of the whole path: the labor is mostly in cutting and fitting narrow strips precisely, not in covering open ground the way a lawn install does.</p>"),
    "faqs": [
        faq("Does turf between pavers need the same base as a lawn in Harmony?",
            "It needs a compacted base under the pavers themselves, with the turf strips set into a narrower prepared channel rather than the full washed-rock depth a lawn requires across its whole footprint."),
        faq("Can paver-and-turf paths handle Harmony's wet season?",
            "Yes, as long as the joints are graded to drain rather than trap water; a path that pools between pavers after a storm usually has a base problem, not a turf problem."),
    ],
    "sources": SRC,
}

LOCAL["repair"] = {
    "title": "Artificial Turf Repair in Harmony, FL",
    "meta": "Artificial turf repair in Harmony, FL covers original-village lawns installed since the early 2000s and newer storm-related fixes. Local facts, September 2026.",
    "h1": "Fixing turf that's aged with Harmony's original village",
    "lede": capsule("Turf repair in Harmony is quoted per visit based on what's actually wrong, not a flat per-square-foot rate. Homes in the neighborhoods built when Harmony opened in the early 2000s are old enough that some of the community's earliest turf installations, if any went in around then, are reaching the far end of a typical service life."),
    "sections": [
        ("Original-village lawns are old enough to show their age",
         f"<p>Harmony's founding neighborhoods opened for occupancy around 2003 {ext('https://en.wikipedia.org/wiki/Harmony,_Florida', 'more than two decades before this page was written')}, which puts any turf installed in that early wave near or past the upper end of a typical 10-to-20-year lifespan. A lawn that age commonly shows matting along the paths people actually walk, infill that's thinned from repeated rinsing, and seams that were never built to the state's current anchoring standard because that standard didn't exist yet when the turf went in.</p>"),
        ("Wind and standing water after a storm",
         f"<p>A lifted edge or a peeled seam after a tropical storm is the most common repair call on any Central Florida lawn, and Harmony's lakefront and pond-adjacent lots see more standing water pressure on an edge than a lot set back from any waterbody. Walking the perimeter of a lawn near Buck Lake, Cat Lake or a stormwater pond after heavy rain, checking specifically where the turf meets a hardscape edge, catches a small lift before it becomes a larger tear.</p>"),
        ("Bringing an older lawn's base up to the current standard",
         f"<p>A repair on a lawn old enough to predate {src('dep-rule', "Florida's May 2026 turf rule")} is a chance to check whether the original base ever met the washed-rock specification the state now requires, since older installs sometimes used unwashed fill that binds into a crust over time. A seam repair alone doesn't require redoing the whole base, but a section with recurring drainage complaints is worth checking against the current standard rather than patching the same spot twice.</p>"),
    ],
    "scenario": ("Say a seam has opened along 12 linear feet of an older lawn",
                 "<p>A 12-foot open seam along the edge of an original-village lawn, part of a roughly 950 sq ft yard installed when the neighborhood was newer, is a small fraction of the total lawn area but the kind of repair that gets worse fast if left through another rainy season, since water working under an open seam widens the gap with every storm. Repair pricing here reflects the linear footage of the fix and site access, not the size of the whole lawn, which is why two seam repairs on similarly sized yards can carry different quotes depending on how the section failed.</p>"),
    "faqs": [
        faq("How do I know if my Harmony lawn is original to when the neighborhood opened?",
            "If the home dates to Harmony's early phases and the turf has never been replaced, it's worth having a repair visit include a general age assessment rather than assuming a single seam fix solves an aging installation's broader wear."),
        faq("Does a Harmony repair need Residential Owners Association approval?",
            "A like-for-like repair that doesn't change the turf's footprint or appearance typically doesn't need a new design review submission, but confirm with the association if the repair also involves changing color, product or the edged area."),
    ],
    "sources": SRC,
}

LOCAL["cleaning"] = {
    "title": "Artificial Turf Cleaning in Harmony, FL",
    "meta": "Artificial turf cleaning in Harmony, FL handles tree canopy debris and lake-adjacent humidity as much as pet odor. Local facts and what's involved, Sept. 2026.",
    "h1": "Cleaning turf under Harmony's tree canopy and lake air",
    "lede": capsule("A Harmony cleaning visit carries no flat rate; a crew prices it once they see the lawn's footprint and how much has built up since a rinse or brush last touched it. Harmony's tree-lined streets and its two namesake lakes add debris and humidity to the usual pet-odor reasons a Central Florida lawn needs a power-brooming and sanitizing visit."),
    "sections": [
        ("Tree-lined streets mean more debris than an open subdivision",
         f"<p>Harmony's New Urbanism design leans on shade trees along its streets and sidewalks as part of the walkable layout {ext('https://movingtosaintcloudfl.com/saint-cloud-neighborhoods/harmony/', 'the community was built around from the start')}. That canopy drops more leaf litter, seed pods and pollen onto a nearby lawn than an open, tree-sparse yard would see, and debris left sitting on turf breaks down into the infill layer over time, changing drainage and eventually feeding odor the same way it would on natural grass.</p>"),
        ("Humidity near Buck Lake and Cat Lake",
         "<p>Yards within a block or two of Harmony's lakes or one of its stormwater ponds sit in slightly damper air than a lot set well back from open water, which can slow how quickly a lawn dries out between rinses. That's rarely a problem on its own, but paired with heavy pet use or leaf buildup it can extend how long odor lingers after a rinse, which is part of why a lakeside lawn sometimes needs sanitizing on a shorter interval than the same size lawn set back from the water.</p>"),
        ("Pet odor treatment on top of the usual maintenance",
         "<p>Zeolite and coated-sand infill both fight odor passively, but neither replaces an occasional deeper clean once ammonia has built up past what routine rinsing handles. A power-brooming and sanitizing visit lifts matted fiber and treats the infill layer directly, which is a different job than the daily hose rinse a homeowner does, and it's the visit worth scheduling before a problem area gets bad enough that neighbors notice.</p>"),
    ],
    "scenario": ("Say a 700 sq ft lawn near Buck Lake needs its seasonal clean",
                 "<p>A 700 sq ft lawn two blocks from Buck Lake, shaded by a mature oak along the property line, typically needs a power-brooming and infill sanitizing visit more often than the same lawn out in an open, sun-baked section of Harmony West, since the combination of leaf litter and lake-adjacent humidity slows natural drying between rinses. Cleaning here is quoted by the visit based on square footage and condition, factoring in how much debris has worked into the infill since the last service, rather than a flat rate that ignores those local differences.</p>"),
    "faqs": [
        faq("How often does turf near Harmony's lakes need professional cleaning?",
            "It varies by shade cover and pet use, but a lakeside or heavily shaded lawn often benefits from a deeper clean on a shorter interval than a sunnier, more open lot in the same neighborhood."),
        faq("Does leaf litter from Harmony's street trees damage turf if left too long?",
            "Left for weeks it can, since decomposing debris changes how the infill drains and can hold moisture against the backing longer than the turf is meant to sit wet."),
    ],
    "sources": SRC,
}

LOCAL["replacement"] = {
    "title": "Turf Removal & Replacement in Harmony, FL",
    "meta": "Turf replacement in Harmony, FL often means bringing an early-2000s install up to the state's 2026 material rule. Local facts and pricing context, September 2026.",
    "h1": "Replacing turf that predates the state's current rule",
    "lede": capsule("Turf replacement in Harmony prices close to a new installation at the " + price("residential") + " range, minus whatever base can be reused, as of September 2026. Because Harmony's original neighborhoods opened around 2003, a replacement job here often means correcting a base or infill built before the state's May 2026 material standard existed."),
    "sections": [
        ("An older lawn built to a different set of assumptions",
         f"<p>Turf installed when Harmony's founding neighborhoods were new, if any dates that far back, went in years before {src('dep-rule', "Florida's synthetic turf standard")} set requirements for washed base material and restricted infill to natural products. A replacement project on a lawn that old is a natural point to check whether the original infill was ever crumb rubber or another synthetic material now barred outside a playground's footprint, since a full tear-out is the easiest time to correct that rather than layering new turf over an outdated base.</p>"),
        ("Deciding what base survives the tear-out",
         "<p>Not every old base needs full replacement. If the original crushed rock was washed material that's held its shape and still drains, a replacement job can sometimes reuse that layer with a fresh compaction pass rather than hauling it out entirely. A base that's crusted over from unwashed fill or settled unevenly after two decades doesn't get that option, and the difference between the two usually only becomes clear once the old turf is pulled back.</p>"),
        ("Why replacement pricing tracks close to new installation",
         f"<p>A replacement job carries most of the same steps a first installation does, demolition, base work, seaming and edging, minus only the sod-removal step a first-time conversion needs. That's why {svc('replacement', 'turf replacement')} tends to price near the same {price('residential')} range as a new lawn rather than at a discount, with the final number depending mostly on how much of the old base survives inspection.</p>"),
    ],
    "scenario": ("Say you have 825 sq ft of turf original to the early 2000s",
                 f"<p>Replacing 825 sq ft of turf original to one of Harmony's earliest lawns, assuming the base needs a full rebuild rather than a reuse, prices between $6,600 and $14,850 at the {price('residential')} range, with most jobs this size landing near $8,250 to $13,200 using the typical $10–$16 band. That estimate assumes the crew finds unwashed fill or a settled base once the old turf comes up, which is common enough on an installation this old that it's worth budgeting for rather than assuming the existing rock will pass inspection.</p>"),
    "faqs": [
        faq("Does replacing turf in Harmony trigger a new Residential Owners Association review?",
            "A straightforward like-for-like replacement usually doesn't need a fresh submission, but a change in color, pile height or the edged footprint should go through the association's design review the same as a first-time installation would."),
        faq("How do I know if my old Harmony lawn's infill is compliant with the 2026 rule?",
            "The clearest way is a visual and material check once the turf is pulled back during a replacement quote; rubber infill has a distinct look and feel compared with sand or zeolite, and an installer can usually tell within minutes of exposing it."),
    ],
    "sources": SRC,
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
