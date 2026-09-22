# -*- coding: utf-8 -*-
"""Hunters Creek, FL: hub + city x service pages. Unincorporated south Orange County,
just north of the Osceola line. Research checked September 2026; see SRC below."""
from _helpers import page, capsule, sec, table, faq, a, post, price
from _cityservice import cityservice_pages

SLUG = "hunters-creek"

SRC = [
    ("Hunter's Creek Community Association — Architectural Guidelines and Community Standards, revised August 2024", "https://cwsamsinc.com/rp/HOA/ArchitecturalGuidelinesAugust62024.pdf"),
    ("Orange County Code, Chapter 24 — Landscaping, Buffering and Open Space, Municode Library", "https://library.municode.com/fl/orange_county/codes/code_of_ordinances?nodeId=PTIIORCOCO_CH24LABUOPSP"),
    ("Orange County Fast Track Online Services", "https://fasttrack.ocfl.net/OnlineServices/"),
    ("Orange County Zoning Division", "https://www.orangecountyfl.net/PermitsLicenses/ZoningDivision.aspx"),
    ("Orange County Utilities — watering restrictions", "https://www.orangecountyfl.net/watergarbagerecycling/wateringrestrictions.aspx"),
    ("Orange County Property Appraiser — parcel search", "https://ocpafl.org/"),
    ("South Florida Water Management District — Shingle Creek", "https://www.sfwmd.gov/recreation-site/shingle-creek"),
    ("South Florida Water Management District — Upper Kissimmee Basin water supply plan", "https://www.sfwmd.gov/our-work/water-supply/upper-kissimmee"),
    ("Wikipedia — Hunter's Creek, Florida", "https://en.wikipedia.org/wiki/Hunter%27s_Creek,_Florida"),
    ("U.S. Census Bureau QuickFacts — Hunters Creek CDP, Florida", "https://www.census.gov/quickfacts/hunterscreekcdpflorida"),
    ("USDA NRCS — Official Series Description, Immokalee series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/I/IMMOKALEE.html"),
    ("USDA NRCS — Official Series Description, Malabar series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/M/Malabar.html"),
    "usda-wss",
    ("Hunter's Creek Golf Club — course history, GolfPass", "https://www.golfpass.com/travel-advisor/courses/7-hunters-creek-golf-club"),
    ("Florida Neighborhood Realty — running and fitness in Hunter's Creek", "https://www.floridaneighborhoodrealty.com/blog/running-fitness-hunters-creek-trails-running-club-outdoor-workouts/"),
    ("Florida Neighborhood Realty — Hunter's Creek Town Center", "https://www.floridaneighborhoodrealty.com/blog/hunters-creek-town-center/"),
    "dep-rule", "fs125572", "fs7203045", "hb683",
]

# ============================================================== hub
HUB = page(
    "/areas/hunters-creek/", "city",
    "Artificial Turf in Hunters Creek, FL (Orange County)",
    "Hunters Creek sits in unincorporated Orange County, not Osceola. What the community association allows for turf, plus permits and ponds, September 2026.",
    "Turf installation for Hunters Creek's pool-cage homes and ponds",
    capsule(
        f"Hunters Creek is an unincorporated Orange County community roughly 5 miles from downtown Kissimmee, so a "
        "turf project answers to Orange County's Building Safety Division and to the Hunter's Creek Community "
        "Association's own architectural review, not to the Osceola offices that cover Kissimmee. Installed turf "
        f"runs {price('residential')} per square foot as of September 2026, and the association weighs a synthetic "
        "lawn case by case, in enclosed rear yards only."
    ),
    "".join([
        sec("Which office actually reviews a Hunters Creek turf project",
            "<p>A Hunters Creek address can read as Orlando or Kissimmee on a piece of mail, but the parcel itself "
            "sits in unincorporated Orange County, so a turf project answers to the county's Division of Building "
            "Safety and Permitting Services at 407-836-5550, filed through the Fast Track Online Services portal, "
            "not a city hall. Orange County's Chapter 24 landscaping ordinance treats &quot;turf&quot; as living "
            "grass species only, St. Augustine and Bahia among them, so synthetic turf sits outside that definition "
            "entirely rather than being named as allowed or banned in the county's own text. "
            "The county's Zoning Division, a separate office reached at 407-836-3111, is who answers a rental-use or "
            "district question instead. Because the community borders both Orlando and the Osceola County line, "
            "confirming a specific lot's jurisdiction starts with a search on the Orange County Property Appraiser's "
            f"site, and the fuller picture of what the county code does and doesn't say is on {a('/laws/permits/orange-county/', 'our Orange County permits page')}.</p>"),
        sec("What the Hunter's Creek Community Association's guideline says about turf",
            "<p>The HCCA's Architectural Guidelines and Community Standards, last revised in August 2024, route "
            "every exterior change, landscaping included, through an Architectural Review Committee. Ordinary sod "
            "from the association's own approved list, Bahia, Bermuda, St. Augustine, Zoysia and two certified "
            "Paspalum varieties, needs no ARC sign-off as long as it stays under six inches tall; a synthetic lawn "
            "does. Its Artificial Turf section treats that as a case-by-case application for an enclosed back yard "
            "only, asks for a substrate three to four inches deep and compacted before the surface goes down, "
            "steers drainage toward a dedicated easement instead of a neighbor's lot, and rules out turf or "
            "turf-like carpet on a patio or an entry altogether. None of that is a state or county requirement; "
            "it's this one association's own published standard, approved a year and a half before Florida's own "
            "turf rule took effect, and it sits on top of whatever the county's permit counter separately expects.</p>"),
        sec("Ponds, golf-course fairways and the state's water buffer",
            "<p>Dozens of Hunters Creek lots back onto a retention pond, Lake Calabay, Mallard Lake or a fairway at "
            "the community's own golf club, and the association's fence rules already treat that edge with care: a "
            "lot against a pond, lake, golf-course fairway or park area gets a low picket fence set within 20 feet "
            "of the rear line, with hedges inside that zone capped at 18 inches. That 20-foot line runs well past "
            "the 10-foot waterbody setback Florida's synthetic-turf standard has required since May 19, 2026, so on "
            "most water- or fairway-backing lots the association's own fence buffer, not the state figure, ends up "
            "being the tighter constraint on where turf can start. A separate rule covers a rear line that meets "
            "conservation land or the Osceola County line itself: only a black vinyl-coated chain-link fence is "
            "allowed there, subject to the ARC's own sight-line review.</p>"),
        sec("Pool-cage homes from the late 1980s through the 2000s",
            "<p>Hunters Creek grew outward from 1986 across roughly 38 named single-family villages, Foxhaven, "
            "Glenhurst, Ocita, Quail Lake, Tanglewood and Calabay Cove among them, and the 2020 Census counted "
            "24,433 residents across the community's 7.07 square miles. Almost every lot from that era carries a "
            "screened pool cage: the HCCA's guideline caps a pool, spa or screen enclosure at a five-foot side and "
            "rear setback, 15 feet on a side-street yard, and rules out an above-ground pool outright, so the lawn "
            "that's left is usually a narrow band between the enclosure and the property line rather than an open "
            "rectangle. Web Soil Survey data places much of this stretch of south Orange County in Immokalee and "
            "Basinger series soils, nearly level and poorly drained sands that sit only inches above a seasonally "
            "high water table, part of why the neighborhood carries so many depressional ponds to begin with.</p>"),
        table("Hunters Creek yard types and what we do differently",
              ["Yard type", "What's typical here", "What changes the turf plan"],
              [["A 1990s pool-cage lot on an interior street", "5-ft side/rear pool setback, screen enclosure, no above-ground pool", "Turf runs beside the shell, not the deck; the guideline bars turf on a patio or entry"],
               ["A lot backing a pond, lake or fairway", "HCCA fence sits within 20 ft of the rear line", "The association's own buffer, not the state's 10-ft rule, usually sets where turf can start"],
               ["A zero-lot-line or narrow side yard (Foxhaven, Glenhurst, Ocita)", "3-6 ft between homes, a dog's daily fence-line path", "Pet-grade backing and a shorter pile so one worn strip drains and doesn't mat"],
               ["A lot against conservation land or the county line", "Black vinyl-coated chain-link fence required at the rear line", "Turf stops at the fence; an oak inside the yard still keeps its own drip-line rule"],
               ["A front yard or street-facing side yard", "ARC's turf clause reviews enclosed rear yards only", "Front lawns stay natural sod from the approved list; turf plans go to the back"]],
              "Based on the HCCA's Architectural Guidelines (revised August 2024) and Florida Rule 62-308.100, effective May 19, 2026. A specific lot can vary."),
        sec("Water, irrigation and the district behind the tap",
            "<p>Irrigation here runs on Orange County Utilities rather than a city system; the HCCA's own guideline "
            "even ties easement watering directly to &quot;Orange County's water system.&quot; The utility cuts "
            "outdoor watering to two mornings a week in daylight saving months, one the rest of the year, and shuts "
            "sprinklers off through the middle of the day, roughly 10 to 4. None of that reaches a turf area once "
            "the heads underneath are capped, which Florida's 2026 standard requires no matter what the local "
            "schedule says. Hunters Creek also falls inside the South Florida Water Management District's Upper "
            "Kissimmee Basin rather than the St. Johns district that covers most of Orlando to the north; the "
            "1,585-acre Shingle Creek Management Area, the northernmost headwaters of the Everglades, runs through "
            "the community's own conservation corridor.</p>"),
        sec("Two approvals, not one, before a crew shows up",
            f"<p>An Orange County permit question and an HCCA architectural approval are separate steps, and "
            "clearing one doesn't substitute for the other; a homeowner who only calls the county and skips the ARC "
            f"application can still get a violation notice for the same yard. Start with what {a('/laws/hoa-rules/', 'Florida law actually lets an HOA restrict')} "
            f"and how {a('/laws/florida-hb-683/', 'the state turf standard limits a local rule')}, since the two work "
            "together differently here than on an Osceola lot with no master association. Then build the ARC "
            f"packet itself: a site plan, a substrate and drainage note, and the product spec the association's "
            f"application asks for; {a('/tools/hoa-packet-checklist/', 'our HOA packet checklist')} walks through "
            "what most Central Florida associations want to see before they sign off.</p>"),
        sec("Is Hunters Creek a vacation-rental market?",
            "<p>Homeowners typing something like &quot;best artificial turf installer near Hunters Creek&quot; into "
            "a search bar are almost always asking about their own back yard, not a rental listing, and that tracks "
            "with how the community is zoned. Orange County's Zoning Division limits a single-family transient "
            "rental, anything under 30 days, to the R-3 district, and prohibits it in every other residential "
            "district unless a Planned Development expressly allows it; a longer, month-plus furnished lease is a "
            "different question the Zoning Division answers parcel by parcel. That's a real contrast with the "
            "short-term-rental corridors closer to the theme parks in Osceola County, and it's why a turf "
            "conversation in Hunters Creek is almost always about a family's own yard rather than a guest-turnover "
            "schedule.</p>"),
        "<!--AUTO:city-services-->",
    ]),
    faqs=[
        faq("Does Hunters Creek's HOA allow artificial turf?",
            "Case by case, and only in an enclosed back yard. The Hunter's Creek Community Association's "
            "Architectural Guidelines, revised August 2024, require an ARC application, a compacted substrate and "
            "drainage toward a dedicated easement, and they rule out turf on a patio or entry; approved natural sod "
            "doesn't need that same sign-off."),
        faq("Do I need a county permit on top of the HCCA's approval?",
            "Possibly, mainly for capping the irrigation heads under the new turf, since that's plumbing work. "
            "Orange County's landscaping code doesn't name synthetic turf either way, so call the Division of "
            "Building Safety at 407-836-5550 before scheduling a crew, separately from whatever the ARC needs."),
        faq("Can I install turf in my Hunters Creek front yard?",
            "The association's guideline only reviews turf for an enclosed rear yard, so a front-yard synthetic "
            "lawn isn't something the ARC process covers at all; a front lawn is expected to stay natural sod from "
            "the approved list. Florida's HOA turf statute only protects turf that isn't visible from the "
            "frontage, which a front yard by definition is."),
        faq("How close to a Hunters Creek pond can turf go?",
            "The state standard sets a 10-foot setback from a pond, lake or canal unless a seawall separates the "
            "two, but the HCCA's own fence rule for a water- or fairway-backing lot already sits at 20 feet, so "
            "that association line usually ends up governing the layout instead."),
        faq("Can I put my Hunters Creek home on a nightly rental site after adding turf?",
            "Turf doesn't change the zoning answer. Orange County limits under-30-day rentals to the R-3 district "
            "and to Planned Developments that expressly allow it, so most Hunters Creek parcels can't run nightly "
            "bookings regardless of what's in the yard; the Zoning Division confirms a specific address."),
    ],
    sources=SRC, city=SLUG,
    crumbs=[("Service areas", "/areas/")], crumb="Hunters Creek",
    related=[
        ("/laws/permits/orange-county/", "Artificial turf permits in Orange County"),
        ("/laws/hoa-rules/", "What a Florida HOA can and can't restrict"),
        ("/laws/florida-hb-683/", "HB 683 and DEP Rule 62-308.100"),
        ("/tools/hoa-packet-checklist/", "HOA / ARC packet checklist"),
        ("/areas/dr-phillips/", "Turf in Dr. Phillips"),
        ("/areas/meadow-woods/", "Turf in Meadow Woods"),
        ("/artificial-grass-installation/", "Residential turf installation, the full guide"),
        ("/artificial-turf-cost/", "Turf cost tables for Central Florida"),
        ("/areas/kissimmee/", "Artificial turf in Kissimmee"),
        ("/areas/buenaventura-lakes/", "Turf in Buenaventura Lakes, across the county line"),
        ("/areas/southchase/", "Turf in Southchase"),
    ],
)

# ============================================================== city x service
LOCAL = {
    "residential": {
        "title": "Artificial Grass Installation in Hunters Creek, FL",
        "meta": "Installing artificial grass in Hunters Creek clears Orange County's desk and the HCCA's back-yard-only turf review, not an Osceola office. Rates for 2026.",
        "h1": "Turf installation for Hunters Creek's pool-cage lots",
        "lede": capsule(
            f"Installed artificial grass in Hunters Creek runs {price('residential')} per square foot as of "
            "September 2026, the same range as anywhere else in Central Florida, but getting a lawn finished here "
            "runs through two approvals: an Orange County permit question and the Hunter's Creek Community "
            "Association's own case-by-case review for an enclosed back yard. Homeowners searching for the best "
            "artificial turf installer near Hunters Creek are usually comparing how each contractor handles that "
            "second approval."
        ),
        "sections": [
            ("Orange County's permit question, and the HCCA's separate one",
             "<p>Orange County's landscaping code, Chapter 24, defines &quot;turf, turf grass or sod&quot; as a "
             "living grass species, Bahia, Bermuda, St. Augustine and several others, so a synthetic lawn doesn't "
             "trip a written rule at the county's permit counter one way or the other; the more common trigger is "
             "the plumbing question once the sprinkler heads under the new lawn get capped. The Hunter's Creek "
             "Community Association runs on its own separate timeline: its Architectural Guidelines route a "
             "residential turf request through an application covering substrate depth, drainage direction and the "
             "finished product, and that packet has to clear the ARC before or alongside whatever the county's "
             "Building Safety Division wants to see. Treating the two as one conversation is the most common "
             f"mistake on a first-time Hunters Creek quote. More on the county side is in {a('/laws/permits/orange-county/', 'our Orange County permits guide')}.</p>"),
            ("What the association's base and drainage language means for the build",
             "<p>The HCCA's turf clause asks for a substrate three to four inches deep, compacted before the "
             "surface goes on, with drainage steered toward a dedicated easement rather than a neighbor's fence "
             "line, wording that lines up closely with Florida's own 2026 standard requiring a washed, open-graded "
             "base under any covered lot. On a typical lot here that means stripping the old sod and a few inches "
             "of soil, laying and compacting crushed rock to that same depth, and grading the finished surface "
             "toward whichever swale or drain the original builder used for stormwater, not toward a pond fence 20 "
             "feet away. The guideline also calls for a licensed contractor and edging driven into the prepared "
             "base, both worth confirming in writing before an ARC packet goes in.</p>"),
            ("Why the native soil here needs real depth, not a thin base",
             "<p>Web Soil Survey mapping puts much of this stretch of south Orange County in Immokalee and Basinger "
             "series soils, nearly level and poorly to very poorly drained, sitting close to a seasonally high "
             "water table for weeks at a stretch in summer. That's a large part of why so many retention ponds sit "
             "among Hunters Creek's villages, and it's also why skimping on the crushed-rock base is the fastest "
             "way to end up with a lawn that holds water after an afternoon storm instead of clearing it in "
             "minutes. Building the full depth, compacted in two lifts the way a wet Florida base actually needs, "
             f"costs more in labor than a thin shortcut, but it holds up through a rainy June. More on that "
             f"sequence is in {post('base-under-artificial-turf-florida-sandy-soil', 'what goes under turf in sandy Central Florida soil')}.</p>"),
        ],
        "scenario": ("Say you have a 620 sq ft lawn behind a Glenhurst pool cage",
                     f"<p>Say you have a 1990s pool-cage home in Glenhurst with roughly 620 sq ft of actual lawn "
                     "left once the screen enclosure and a paver walkway are subtracted, backing onto a retention "
                     f"pond at the HCCA's 20-foot fence line. At the published {price('residential')} per sq ft "
                     "range, that yard prices between $4,960 and $11,160 installed, typically landing near "
                     f"{price('residential', True)}: about $6,200 to $9,920 for the full 620 sq ft. The ARC "
                     "application for that lot needs to show the turf staying inside the fence line rather than "
                     "crowding the pond buffer, which is a drawing detail more than a pricing one.</p>"),
        "faqs": [
            faq("Does a Hunters Creek residential lawn need a different base than a lawn elsewhere in Central Florida?",
                "The build itself is the same washed crushed-rock base Florida's standard requires everywhere; "
                "what's different here is that the HCCA's own guideline states the same three- to four-inch depth "
                "in its own words, so the county's rule and the association's line point at the same number."),
            faq("Is there a faster way through the ARC for a simple backyard lawn?",
                "Not officially, but a complete packet moves faster than an incomplete one. Bringing a site plan, "
                "the product spec and a drainage note to the first submission avoids the review-and-resubmit cycle "
                "that slows down most first-time applications here."),
        ],
        "sources": SRC,
    },
    "pet": {
        "title": "Hunters Creek Pet Turf for Narrow Side Yards",
        "meta": "Pet turf in Hunters Creek's zero-lot-line villages, Foxhaven, Glenhurst and Ocita, needs pet-grade backing for a worn fence-line path. Rates for September 2026.",
        "h1": "Dog-run turf built for Hunters Creek's zero-lot-line yards",
        "lede": capsule(
            f"Pet turf in Hunters Creek runs {price('pet')} per square foot as of September 2026, priced above a "
            "plain lawn because the backing, base depth and infill are all upgraded for daily rinsing. Several "
            "villages here, Foxhaven, Glenhurst and Ocita among them, were built with narrow zero-lot-line side "
            "yards, exactly where a dog's fence-line path wears grass bare fastest. Owners asking who installs the "
            "best pet turf near Hunters Creek are usually the ones staring at that worn path."
        ),
        "sections": [
            ("Zero-lot-line yards and the fence-line path a dog wears in",
             "<p>Foxhaven, Glenhurst and Ocita were all built with three to six feet between homes on one side, a "
             "layout from the community's original late-1980s and 1990s plat maps that leaves little room for a dog "
             "to range beyond a single narrow strip. That strip becomes the daily patrol route, and on real sod it "
             "shows up as a bare, compacted lane within a season no matter how it's watered. A pet-grade build with "
             "a fully permeable backing and a shorter, denser pile handles that one worn path the way a wider "
             "yard's turf handles traffic spread across a whole lawn, which is the main reason a dog-run quote in "
             "one of these villages reads differently from a quote for an open Calabay Cove back yard of the same "
             "size.</p>"),
            ("The HCCA's back-yard-only rule already matches where dog turf goes",
             "<p>The Hunter's Creek Community Association limits its turf review to an enclosed rear yard, which "
             "happens to line up with where a dog run almost always sits anyway, since a fenced back yard is both "
             "the practical spot for a run and the only spot the association will weigh for synthetic turf on a "
             "case-by-case basis. The same packet a residential lawn needs, substrate depth, drainage direction, "
             "product spec, applies to a pet system too, with one addition worth flagging on the drawing: a pet "
             "build usually skips the weed-barrier layer under the turf entirely, since fabric there traps liquid "
             "instead of letting the washed-rock base carry it straight down to the sand underneath.</p>"),
            ("Central sewer, not septic, removes one variable from the layout",
             "<p>The association's governing documents prohibit septic tanks and other non-central systems on a "
             "Hunters Creek lot, so every home here runs on Orange County's central sewer, unlike a rural Osceola "
             "or Polk property where a dog run's drainage plan has to steer clear of a septic drainfield. That's "
             "one variable this community's pet-turf layout doesn't have to solve for. What it still has to account "
             "for is the high water table in the area's flatwoods sand, which pushes toward the fuller base depth "
             "on a run getting a rinse every day rather than just rainfall.</p>"),
        ],
        "scenario": ("Say you have a 320 sq ft run along a Foxhaven fence line",
                     f"<p>Say you have an eight-foot-wide, 40-foot-long run along the side fence of a Foxhaven "
                     "zero-lot-line home, about 320 sq ft in all, where the family dog has already worn the sod "
                     f"down to dirt. At the published {price('pet')} per sq ft range, that run prices between "
                     f"$3,200 and $5,760 installed, typically {price('pet', True)}: roughly $3,840 to $5,120 for "
                     "the full 320 sq ft. Because the run sits entirely inside the back yard, it fits the HCCA's "
                     "rear-yard rule without raising the front-yard exception a corner lot sometimes does.</p>"),
        "faqs": [
            faq("Does pet turf need a different ARC application than a regular lawn in Hunters Creek?",
                "Not a different form, the same one, but the drawing should call out the run's drainage point and "
                "note that the weed barrier is being skipped, since a reviewer used to a standard lawn packet may "
                "otherwise ask about that omission."),
            faq("Will a dog run trigger the community's pond setback if it sits near the fence?",
                "Only if the run itself crosses into the 20-foot zone the HCCA keeps clear along a pond, lake or "
                "fairway line; a run built entirely inside that buffer's inner edge doesn't raise the question."),
        ],
        "sources": SRC,
    },
    "putting": {
        "title": "Backyard Putting Greens Near the Hunters Creek Golf Club",
        "meta": "A putting green on a Hunter's Creek Golf Club fairway lot needs the HCCA's 20-ft fence buffer and rear-yard-only ARC review. Rates for September 2026.",
        "h1": "Putting greens for lots backing the Hunter's Creek fairways",
        "lede": capsule(
            f"A backyard putting green in Hunters Creek runs {price('putting')} per square foot as of September "
            "2026, reflecting the contouring, fringe turf and cups a green needs beyond a flat lawn. Hunter's Creek "
            "Golf Club, built in 1986 and once ranked among Golf Digest's top public courses, backs directly onto a "
            "number of the community's own lots, and homeowners asking about the best putting-green builder near "
            "Hunters Creek are usually the ones with a fairway view already."
        ),
        "sections": [
            ("A fairway view changes the ARC drawing, not just the yard",
             "<p>A lot backing one of Hunter's Creek Golf Club's fairways carries the same buffer the HCCA applies "
             "to any pond- or lake-facing yard: a low picket fence set within 20 feet of the rear line, with hedges "
             "capped at 18 inches inside that zone. A green on that kind of lot has to fit inside the buffer rather "
             "than running its contour up to the fence, which usually means a smaller footprint than the flat "
             "rectangle a green would ideally want. The association still treats a putting surface as artificial "
             "turf for review purposes, so the same case-by-case, rear-yard-only application applies whether the "
             "finished product is a lawn or a contoured green with a collar and cups.</p>"),
            ("Why a green needs more grading attention on this soil",
             "<p>The flatwoods sands common across south Orange County drain slowly and sit close to a seasonally "
             "high water table, which matters more on a putting green than on a flat lawn because a green's whole "
             "purpose depends on a subgrade that holds its shape through a rainy Central Florida summer without a "
             "low spot forming under the nylon surface. Getting the base right here takes more attention to layered "
             "compaction and to the crown and contour built into the crushed rock itself, not just a deeper base "
             "the way a dog run gets. A green built on an undercompacted base in this soil is the build most likely "
             "to develop a dip inside its first year.</p>"),
            ("Golf Club history, and why a home green still isn't the same game",
             "<p>Hunter's Creek Golf Club opened in 1986 and was named one of Golf Digest's Top 75 Public Courses "
             "in 1990, anchoring the community's identity since its earliest villages went in. A backyard green "
             "built off that reputation is still a different product: home greens use a synthetic surface built for "
             "a consistent roll at a modest size, not the maintained natural turf a public course runs, and a good "
             "installer sets stimp speed and slope through the base contour rather than through mowing height. The "
             "association's application doesn't distinguish a green from any other artificial turf request, so the "
             "same substrate and drainage requirements apply regardless of how elaborate the contouring gets.</p>"),
        ],
        "scenario": ("Say you have a 450 sq ft green on a fairway-backing lot",
                     f"<p>Say you have a 450 sq ft putting and chipping green planned for a lot backing Hunter's "
                     "Creek Golf Club's back nine, with the green's edge held 21 feet off the rear line to clear "
                     f"the HCCA's 20-foot buffer with a foot to spare. At the published {price('putting')} per sq "
                     f"ft range, that green prices between $6,300 and $13,500 installed, typically "
                     f"{price('putting', True)}: about $8,100 to $11,250 for the full 450 sq ft, with contouring "
                     "and a fringe collar pushing toward the top of that range rather than the bottom.</p>"),
        "faqs": [
            faq("Does living on a golf-course lot in Hunters Creek make ARC approval easier for a green?",
                "No. The Architectural Review Committee treats a putting green the same as any other back-yard "
                "turf request, so the substrate depth, drainage direction and 20-foot fence buffer all still "
                "apply regardless of the fairway view."),
            faq("Can a green extend past the HCCA's fence line toward the fairway?",
                "No, the green has to stay on the homeowner's side of the association's fence buffer, which sits "
                "within 20 feet of the rear property line on a fairway lot; the course itself is never part of the "
                "layout."),
        ],
        "sources": SRC,
    },
    "playground": {
        "title": "Playground Turf for Hunters Creek's Family Backyards",
        "meta": "Playground turf under a Hunters Creek swing set needs a shock pad sized to fall height, and only clears ARC review in an enclosed rear yard. 2026 rates.",
        "h1": "Backyard play turf for Hunters Creek's second-generation families",
        "lede": capsule(
            f"Playground turf in Hunters Creek runs {price('playground')} per square foot as of September 2026, "
            "priced by pad thickness and the fall height of whatever equipment sits on top. Many of the "
            "community's original 1990s buyers have been replaced by a second generation of young families filling "
            "the same swing sets and jungle gyms, and a cushioned surface under that equipment is one of the few "
            "turf jobs the association reviews under the same enclosed-back-yard rule as a full lawn."
        ),
        "sections": [
            ("A community built for kids, now filling with a second generation",
             "<p>Hunters Creek's villages went in mostly between the late 1980s and the early 2000s, and three "
             "decades later many of the original swing sets and play structures have been replaced once already, "
             "sometimes twice, as homes changed hands to families with young children again. The community's "
             "recreation amenities, ball fields, a playground and courts near the clubhouse, reflect that same "
             "family orientation, but a backyard play area is still where most of the daily use actually happens. "
             "Turf under a home play structure holds up to that kind of repeated, concentrated traffic in a way "
             "grass under a swing set rarely does past the first year.</p>"),
            ("Why a front-yard play set still needs natural grass here",
             "<p>The HCCA's turf review only covers an enclosed rear yard, which matters for any family whose play "
             "structure sits in view of the street rather than behind a fence. A front-yard play area has to stay "
             "on natural sod from the association's approved list, kept under six inches, since the guideline "
             "doesn't extend its case-by-case turf review to a front lot at all. That's not a state or county rule, "
             "just this one association's own line between what gets reviewed and what doesn't, worth checking "
             "before pricing a play area that isn't actually in the back yard.</p>"),
            ("Sizing the pad to the equipment, not just the yard",
             "<p>A shock pad under playground turf gets sized to the fall height of the specific equipment sitting "
             "on it, not a flat number that works for every swing set, and on a modest pool-cage-era lot the play "
             "area itself is often the main constraint on layout rather than square footage. Florida's turf "
             "standard allows rubber infill only within the footprint of the play equipment; the ground outside "
             f"that footprint, if it's turfed at all, goes back to the same silica or coated-sand infill a lawn "
             f"would use. {post('is-artificial-turf-safe-for-kids-pfas-lead', 'What the material standard covers for kids')} goes through the rest of that rule.</p>"),
        ],
        "scenario": ("Say you have a 300 sq ft play area behind a swing set",
                     f"<p>Say you have a 300 sq ft play area planned behind a swing set and a small climbing "
                     "structure in a fenced Villanova back yard, sized for a seven-foot fall height on the tallest "
                     f"platform. At the published {price('playground')} per sq ft range, that area prices between "
                     f"$3,000 and $7,500 installed, typically {price('playground', True)}: about $3,600 to $5,700 "
                     "for the full 300 sq ft, with pad thickness under the platform driving most of the difference "
                     "between the low and high end.</p>"),
        "faqs": [
            faq("Can playground turf go around a swing set that's already installed?",
                "Yes, most jobs build the pad and turf around existing equipment rather than requiring it to come "
                "down first, though the footings sometimes need temporary support during excavation."),
            faq("Does a play area need the same ARC drainage note as a lawn?",
                "Yes, since the association reviews it as artificial turf either way; the note should also flag "
                "where infill differs, rubber under the fall zone, standard infill everywhere else on the turfed "
                "area."),
        ],
        "sources": SRC,
    },
    "pool": {
        "title": "Pool-Cage Turf for Hunters Creek Screen Enclosures",
        "meta": "Turf beside a Hunters Creek pool goes on the ground strip, not the deck: the HCCA bars turf on a patio or entry. Setbacks and rates for September 2026.",
        "h1": "Turf beside the pool inside a Hunters Creek screen cage",
        "lede": capsule(
            f"Turf around a pool or inside a screen enclosure in Hunters Creek prices in the same {price('residential')} "
            "per square foot range as a lawn, as of September 2026, since it's the same washed-rock base and "
            "backing doing the work. Almost every home from the community's original build-out carries a screened "
            "pool cage under the HCCA's five-foot side and rear setback, which usually leaves only a narrow strip "
            "of ground for grass or turf between the shell and the enclosure wall."
        ),
        "sections": [
            ("Why the guideline bans turf on the pool deck itself",
             "<p>The HCCA's Artificial Turf clause is specific on one point that matters most for a pool project: "
             "turf or turf-like carpet isn't permitted on a patio or an entry, and a pool deck counts as exactly "
             "that kind of hard surface. What a pool-area turf job actually covers is the narrow planted strip "
             "between the deck's edge and the screen enclosure's aluminum frame, or a side yard visible through the "
             "cage's mesh panels, not the concrete or pavers underfoot. Getting that distinction right on the ARC "
             "application, turf on the ground strip rather than the deck, is usually the difference between a quick "
             "approval and a request for revisions.</p>"),
            ("A five-foot setback squeezes the layout before turf even starts",
             "<p>The association's guideline holds a pool, spa or screen enclosure to a five-foot side and rear "
             "yard setback and 15 feet on a side-street yard, and rules out an above-ground pool outright, "
             "standards that shaped almost every back yard built here from the late 1980s on. That geometry usually "
             "leaves a planting strip only a few feet wide running around two or three sides of the cage, a "
             "different design problem than a wide-open lawn: narrow curves and corners mean more cuts and seams "
             "per square foot than a rectangle of the same size, one reason pool-area turf often prices toward the "
             "upper half of the range.</p>"),
            ("Drainage under an old slab, not just around it",
             "<p>Many pool cages here sit on a concrete deck poured in the 1990s or early 2000s, and turf going in "
             "beside that slab, rather than the strip of dirt a plain lawn conversion works with, needs a drainage "
             "underlay and glue-down edges where it meets the concrete so water doesn't collect at the seam. The "
             "same slow-draining flatwoods sand common elsewhere in the community makes that detail matter even "
             "more right against a slab, since water that can't move sideways through the base has nowhere to go "
             f"but up against the concrete edge. {post('install-artificial-turf-over-concrete-pavers-or-grass', 'Installing turf over concrete or pavers')} covers that underlay in more detail.</p>"),
        ],
        "scenario": ("Say you have a 280 sq ft strip inside a screen cage",
                     "<p>Say you have a 1990s pool home in Eagles Landing with a screen cage roughly 30 feet by 20 "
                     "feet, and once the concrete deck and a small paver landing are subtracted, about 280 sq ft of "
                     f"ground remains along two sides for turf. At the published {price('residential')} per sq ft "
                     f"range, that strip prices between $2,240 and $5,040 installed, typically "
                     f"{price('residential', True)}: about $2,800 to $4,480 for the full 280 sq ft, with the narrow "
                     "curves around the cage's support posts pushing toward the higher end.</p>"),
        "faqs": [
            faq("Can turf go directly on my Hunters Creek pool deck?",
                "No, the association's guideline specifically bars turf or turf-like carpet on a patio or entry, "
                "and a pool deck falls into that category; turf goes on the ground strip around the deck instead."),
            faq("Does an above-ground pool change the turf plan?",
                "The HCCA's guideline doesn't permit an above-ground pool at all, so every project here works "
                "around an in-ground pool with a screen enclosure, and the turf plan follows that enclosure's "
                "footprint accordingly."),
        ],
        "sources": SRC,
    },
    "str": {
        "title": "Vacation Rental Turf in Hunters Creek: What's Realistic",
        "meta": "Orange County zoning keeps most of Hunters Creek out of the nightly-rental business, so turf here usually serves a furnished long-term lease. 2026 rates.",
        "h1": "What vacation rental turf looks like in Hunters Creek",
        "lede": capsule(
            f"Turf for a rental home in Hunters Creek prices in the same {price('residential')} per square foot "
            "range as any other lawn, as of September 2026, but the market itself is small: Orange County zoning "
            "keeps a nightly rental out of most of the community's residential districts. Owners searching for the "
            "best turf option near Hunters Creek for a rental are usually managing a longer-term furnished lease, "
            "not weekly guest turnover, which changes what the turf actually needs to withstand."
        ),
        "sections": [
            ("Why Hunters Creek isn't a short-term-rental cluster",
             "<p>Orange County's Zoning Division limits a single-family transient rental, defined as anything under "
             "30 days, to the R-3 district, and prohibits short-term rental in every other residential zoning "
             "district unless a Planned Development expressly allows it. Most of Hunters Creek's villages are "
             "owner-occupied family homes rather than the purpose-built vacation product found closer to the parks "
             "in Osceola County, and that zoning backdrop is a real part of why: an owner here can't simply decide "
             "to run nightly bookings the way an owner in a Four Corners or ChampionsGate community sometimes can. "
             "Anyone weighing a change in use should confirm the specific parcel's zoning with the county before "
             "planning turf around a rental strategy at all.</p>"),
            ("Where turf still fits: a furnished, longer-term rental",
             "<p>A 30-day-plus furnished rental, corporate housing near the airport corridor or a longer "
             "medical-stay lease, is a realistic use inside this zoning, and turf makes sense there for a different "
             "reason than on a nightly vacation rental: durability between tenants rather than between weekend "
             "guests. A yard that has to look presentable for a new tenant every few months, without the owner "
             "scheduling a landscaper in between, benefits from turf's consistency much the way a busy family yard "
             "does, even with a lighter traffic pattern than a true short-term rental would see.</p>"),
            ("The ARC application doesn't care who's living there",
             "<p>Whether a home is owner-occupied or leased long-term, the Hunter's Creek Community Association's "
             "turf review runs the same process: a case-by-case application for an enclosed back yard, the same "
             "substrate and drainage requirements, the same licensed-contractor line. Landlords sometimes assume a "
             "rental property gets a lighter review, but nothing in the published guideline distinguishes an "
             "owner-occupant's application from an owner-of-record renting the home out, so the packet should be "
             "prepared exactly as it would be for a primary residence.</p>"),
        ],
        "scenario": ("Say you have a 540 sq ft yard between long-term tenants",
                     "<p>Say you own a rental home in Quail Lake with a 540 sq ft back yard that turns over to a "
                     "new furnished-lease tenant every four to six months, and re-sodding between each turnover has "
                     f"become a recurring cost. At the published {price('residential')} per sq ft range, converting "
                     f"that yard prices between $4,320 and $9,720 installed, typically {price('residential', True)}: "
                     "about $5,400 to $8,640 for the full 540 sq ft, a one-time cost weighed against what repeated "
                     "re-sodding runs across several tenant cycles.</p>"),
        "faqs": [
            faq("Can I legally rent my Hunters Creek home nightly on a site like Airbnb?",
                "In most of the community's residential zoning, no. Orange County limits under-30-day rentals to "
                "the R-3 district and to Planned Developments that expressly allow it, so check with the Zoning "
                "Division before planning around nightly income."),
            faq("Does a furnished long-term rental need a different turf spec than an owner-occupied home?",
                "Not structurally. The same base, backing and infill choices apply; the main difference is planning "
                "for a tenant-turnover schedule rather than one family's daily routine."),
        ],
        "sources": SRC,
    },
    "commercial": {
        "title": "Commercial Turf Near the Hunters Creek Town Center",
        "meta": "Retail plazas along Town Center Boulevard sit outside the HCCA's residential review and answer to Orange County's commercial permitting. Quoted per job, 2026.",
        "h1": "Turf for retail and common areas around Town Center Boulevard",
        "lede": capsule(
            "Commercial turf around Hunters Creek, planted islands, common-area strips and outparcel plantings near "
            "the Publix-anchored Town Center on Town Center Boulevard, is quoted per job rather than off a flat "
            "per-square-foot rate, since drainage design, ADA-compliant edging and irrigation tie-ins vary by site. "
            "That corridor sits under Orange County's standard commercial zoning and permitting, separate entirely "
            "from the HCCA's residential architectural review, which only covers single-family lots inside the "
            "association."
        ),
        "sections": [
            ("A commercial parcel answers to the county, not the HCCA",
             "<p>The Hunter's Creek Community Association's Architectural Guidelines govern single-family lots and "
             "the association's own common property, not the retail parcels along Town Center Boulevard where "
             "Hunter's Creek Promenade, a Publix-anchored center of roughly 258,000 square feet, and several "
             "smaller plazas sit. Those properties answer to Orange County's ordinary commercial zoning and "
             "permitting process instead, run through the same Division of Building Safety that handles "
             "residential work, but on a different review track entirely. A commercial turf project near that "
             "corridor, a planted median, a courtyard or a pet-relief area outside a multifamily building, follows "
             "county commercial code rather than a homeowner's ARC packet.</p>"),
            ("Why a flat per-foot rate doesn't work for a commercial site",
             "<p>A homeowner's lawn is close to a known quantity: a rectangle or two, a driveway, a fence line. A "
             "commercial site near this retail core usually isn't, since a planted island has curbs and irrigation "
             "stubs to work around, an ADA-compliant walking surface carries edge and slope requirements a "
             "residential yard never sees, and a shopping center's common-area maintenance agreement decides who "
             "signs off on the work before it starts. Those variables are why commercial turf gets quoted from a "
             "site visit and a set of drawings rather than a rate card, even though the base and backing underneath "
             "it aren't fundamentally different from a residential build.</p>"),
            ("Orange County's older code treats turf as a grass species, not a material",
             "<p>Orange County's Chapter 24 landscaping code defines &quot;turf, turf grass or sod&quot; only as a "
             "living grass species, which leaves synthetic turf without a named place in the commercial landscaping "
             "standards that set requirements such as the seven-foot minimum planting strip along a vehicle-use "
             "area. That gap plays out differently on a commercial site than a residential one, since a commercial "
             "landscape plan already has to satisfy code sections a homeowner's yard never triggers, so the right "
             "first call for a commercial project is the county's Permitting Services, not an assumption drawn from "
             "how a residential lawn gets treated.</p>"),
        ],
        "scenario": ("Say a plaza wants a 900 sq ft planted entry median",
                     "<p>Say a small plaza along Town Center Boulevard wants to replace a struggling St. Augustine "
                     "median, roughly 900 sq ft, with turf to cut irrigation and mowing costs between tenants. "
                     f"Material and base alone for a job that size would land somewhere in the {price('residential')} "
                     "per sq ft residential range, but a commercial bid adds an engineered drainage plan, curb-tie "
                     "edging and a site-specific irrigation cutover that a homeowner's quote never carries, which is "
                     "why the number comes back after a site visit rather than off that residential rate.</p>"),
        "faqs": [
            faq("Does a Hunters Creek business need HOA approval for turf?",
                "No, if the property is a commercial parcel outside the HCCA's residential boundaries; it answers "
                "to Orange County's commercial permitting instead. A property inside a mixed-use association with "
                "its own commercial review would follow that association's process."),
            faq("Why does commercial turf cost more per square foot than a home lawn?",
                "It doesn't always, but engineered drainage, ADA edge details and coordination with a property's "
                "irrigation and maintenance systems add scope a residential quote doesn't carry, which is why "
                "commercial work is priced from a site visit rather than a flat rate."),
        ],
        "sources": SRC,
    },
    "sports": {
        "title": "Home Sports and Fitness Turf in Hunters Creek",
        "meta": "A bocce court, batting lane or sled track in Hunters Creek shares a base with a putting green but skips the contouring. Quoted per job for September 2026.",
        "h1": "Building a home sports surface on a Hunters Creek lot",
        "lede": capsule(
            "A home sports surface in Hunters Creek, a bocce court, a batting-cage lane or a sled track for home "
            "fitness, is quoted per job rather than a flat per-square-foot rate, since base prep and edge restraint "
            "vary with what the surface has to withstand. With Hunter's Creek Golf Club anchoring the community and "
            "a paved trail network already threading its villages, plenty of households here are active outdoors "
            "and want a piece of that closer to the back door."
        ),
        "sections": [
            ("Golf-adjacent households and the home-practice instinct",
             "<p>Living beside or near Hunter's Creek Golf Club, built in 1986 and once ranked among Golf Digest's "
             "top public courses, puts golf in front of a lot of households here daily, and it's a short step from "
             "that to wanting a chipping pad, a putting strip or an agility lane for practice at home rather than "
             "always at the course. A sports surface like that shares a base with a putting green in one way, a "
             "compacted subgrade that holds its shape, but usually skips the contouring and drainage-to-collar "
             "detail a true green needs, which keeps the build simpler even on the same sandy flatwoods soil.</p>"),
            ("What a bocce court or batting lane needs that a lawn doesn't",
             "<p>A bocce court needs a crowned, compacted base and a rigid edge restraint, timber or paver, to keep "
             "the playing surface true over years of use, requirements a residential lawn's simple rock-and-turf "
             "build doesn't carry. A batting cage or home-gym sled track has its own demand: a denser, shorter-pile "
             "turf built to resist compaction ruts from repeated foot traffic in one narrow lane rather than the "
             "varied traffic a family lawn sees. Both surfaces still fall under the HCCA's artificial-turf review as "
             "an enclosed-back-yard, case-by-case application, so the added base engineering doesn't change which "
             "approval a homeowner has to clear first.</p>"),
            ("The community's trail culture, and where a home surface fits alongside it",
             "<p>Hunters Creek's own paved trail network connects its villages for walking, running and cycling, "
             "and plenty of households already treat that infrastructure as their main fitness outlet rather than a "
             "gym membership. A home sports surface tends to complement that pattern rather than replace it, "
             "filling a specific gap, agility work, batting practice, a short sled push, that the trail system "
             "itself doesn't cover. Sizing that kind of surface usually comes down to whatever back-yard footprint "
             f"is left once the pool cage and existing landscaping are accounted for. {post('artificial-turf-on-a-slope', 'Turf on an uneven or sloped yard')} covers a related layout question.</p>"),
        ],
        "scenario": ("Say you want a 200 sq ft agility lane and sled track",
                     "<p>Say you want a 10-by-20-foot, 200 sq ft turf lane along a side yard for agility drills and "
                     "a sled push, in a back yard that already has a pool cage taking up most of the rest of the "
                     f"lot. Material and base for a lane that size would land in roughly the same {price('residential')} "
                     "per sq ft territory as a lawn that size, but the denser turf spec and a timber edge restraint "
                     "on both long sides push the finished bid above that residential number, which is why a job "
                     "like this is quoted from a site visit rather than a flat rate.</p>"),
        "faqs": [
            faq("Does a home sports surface need a different base than a lawn in Hunters Creek?",
                "Usually yes, more compaction and a rigid edge restraint for something like a bocce court, since "
                "the surface needs to hold a true, flat plane under repeated concentrated use rather than just "
                "drain well."),
            faq("Will the HCCA review a batting cage or sled track the same way as a lawn?",
                "Yes, as an enclosed-back-yard artificial turf application with the same substrate, drainage and "
                "licensed-contractor requirements, regardless of what the finished surface gets used for."),
        ],
        "sources": SRC,
    },
    "pavers": {
        "title": "Turf and Paver Walkways in Hunters Creek Yards",
        "meta": "Turf ribbons between pavers in Hunters Creek fall under the HCCA's landscape-plan review, the same as any stepping-stone path. Quoted per job, September 2026.",
        "h1": "Turf ribbons between pavers on a Hunters Creek walkway",
        "lede": capsule(
            "Turf set between pavers, a stepping-stone path or a driveway accent strip, is quoted per job in "
            "Hunters Creek rather than a flat per-square-foot rate, since the paver layout and cut count drive most "
            "of the cost. The HCCA's own guidelines define a stepping stone as a landscape feature in its own right "
            "and require ARC approval for poured concrete curbing, which makes a paver-and-turf path here a "
            "two-part decision: the hardscape layout first, the turf ribbons second."
        ),
        "sections": [
            ("The association's own glossary already has a word for this",
             "<p>The HCCA's Architectural Guidelines define a stepping stone as a stone integrated into a landscape "
             "plan as a feature in its own right, a small detail that matters because it means the association "
             "already treats a stepping-stone path as landscaping subject to plan review rather than as an "
             "incidental addition. A turf-and-paver design, stones or pavers set with ribbons of grass or synthetic "
             "turf running between them, falls under that same landscape-plan review, and poured concrete curbing "
             "anywhere in the layout needs its own separate ARC sign-off with color samples and a border photo "
             "submitted alongside the plan.</p>"),
            ("Why the cut count, not the square footage, sets the price",
             "<p>A straight paver walkway with turf ribbons on either side is a simple layout to price, but a "
             "curved stepping-stone path through a planting bed multiplies the cuts a crew has to make, since turf "
             "comes in wide rolls that run one direction and every stone edge needs its own trimmed piece. On a "
             "typical lot here, where many villages were built with paver driveway extensions and accent walkways "
             "as standard builder features, retrofitting turf between existing pavers usually costs more per square "
             "foot than the same turf laid as one open panel, purely from the added labor of all those edges.</p>"),
            ("What the base looks like when pavers are already in place",
             "<p>Turf going in between pavers that are already set doesn't get the same clean excavate-and-compact "
             "sequence a fresh lawn conversion does, since the crew works around fixed hardscape rather than an "
             "open bed. A thinner, well-compacted base gets built in each gap, sized to sit flush with the paver "
             "surface once turf and infill are in, and drainage has to move water down through that narrow strip "
             "rather than across a broad graded yard, which matters on the area's slow-draining sand even at this "
             "smaller scale.</p>"),
        ],
        "scenario": ("Say you have a 200 sq ft ribbon along a paver walkway",
                     "<p>Say you have a 40-foot paver walkway from the driveway to the front entry with an "
                     "18-inch turf ribbon planned on each side, roughly 200 sq ft of turf in narrow strips once "
                     f"both sides are added up. Priced at labor rates closer to the {price('residential')} range "
                     "for the turf portion alone, plus the added time for two long, narrow cuts instead of one open "
                     "panel, a ribbon job like this typically lands above what 200 sq ft of open lawn would cost, "
                     "which is why it's quoted from the actual layout rather than a flat number.</p>"),
        "faqs": [
            faq("Do I need ARC approval just for turf ribbons between existing pavers?",
                "Likely yes, since the association's guideline treats a landscape change tied to a hardscape "
                "feature as part of the same plan review a stepping-stone path or paver walkway already falls "
                "under."),
            faq("Is turf between pavers cheaper than turfing the whole yard?",
                "Not per square foot. Narrow strips with more cuts and edges typically cost more per foot than one "
                "open panel of the same total area, even though the total project is smaller."),
        ],
        "sources": SRC,
    },
    "repair": {
        "title": "Artificial Turf Repair for Hunters Creek Lawns",
        "meta": "Repair calls in Hunters Creek skew toward drainage and fence-line edges given the area's ponds, swales and slow-draining soil. Priced by the visit, September 2026.",
        "h1": "Fixing turf damage on an established Hunters Creek lawn",
        "lede": capsule(
            "Turf repair in Hunters Creek, an open seam, a lifted edge, a low spot that holds water, is priced by "
            "the visit with a minimum service charge rather than by the square foot, since most of the invoice is "
            "diagnosis and re-securing existing material rather than new turf. With some of the community's turf "
            "conversions now well over a decade old, repair calls here skew toward edge and drainage fixes more "
            "than plain surface wear."
        ),
        "sections": [
            ("Why an older Hunters Creek lawn calls for a different fix than a new one",
             "<p>Homes from the community's original build-out are old enough now that an early turf conversion, if "
             "the lot ever had one, is approaching or past the upper end of a typical lifespan, and even a "
             "well-built lawn from a decade ago has weathered years of Central Florida storms working at every seam "
             "and staple. A repair visit on a lawn that age usually starts by checking whether the base underneath "
             "has settled or shifted before touching the surface at all, since re-securing a seam over a base "
             "that's already moved just means doing the same repair again within a season.</p>"),
            ("Ponds and swales make drainage repairs a recurring call here",
             "<p>A yard graded toward one of the HCCA's fence-line pond buffers or a shared drainage swale can "
             "develop a low spot over time as the base settles unevenly, especially on this area's slow-draining "
             "flatwoods sand. That kind of repair isn't a seam fix; it's regrading a section of base and relaying "
             "the turf over it, and it shows up more often on lots backing water or a fairway than on an interior "
             "lot with a straightforward yard shape. Catching a low spot before it holds standing water for more "
             "than a few hours after a storm keeps the fix smaller.</p>"),
            ("Corner and edge damage where a fence line meets the turf",
             "<p>The HCCA requires specific fencing at a rear line, a low picket style against a pond or fairway, "
             "black vinyl-coated chain-link against conservation land or the county line, and turf meeting either "
             "fence type at ground level is a common spot for a lifted edge after a storm shoves loose debris "
             "against the base of the fence. Re-anchoring that edge with fresh nails or a bender-board strip, "
             "rather than just gluing the flap back down, is usually what keeps the same corner from lifting again "
             "the next time wind or heavy rain hits that line.</p>"),
        ],
        "scenario": ("Say you have a 60 sq ft section with a lifted edge",
                     "<p>Say a section of turf along your back fence, roughly 60 sq ft, has lifted at the seam "
                     "after a summer storm pushed water and debris against the base of the fence. A repair on a "
                     f"section that size is priced by the visit rather than the {price('residential')} per sq ft "
                     "range a full install would use, since most of the cost is labor to pull back the flap, check "
                     "the base and re-anchor the edge, not new material, so the bill usually lands well under what "
                     "60 sq ft of new turf would cost outright.</p>"),
        "faqs": [
            faq("Is there a minimum charge for a small turf repair in Hunters Creek?",
                "Most repair visits carry a minimum service charge, since a crew and tools show up whether the fix "
                "is one seam or several; ask for that minimum up front when you call."),
            faq("Do I need HCCA approval for a repair, or just for a new install?",
                "A like-for-like repair that doesn't change the footprint or product typically doesn't need a fresh "
                "ARC application, but check with the association if the fix involves regrading or a different "
                "product than what was originally approved."),
        ],
        "sources": SRC,
    },
    "cleaning": {
        "title": "Turf Cleaning and Odor Control in Hunters Creek",
        "meta": "Turf in Hunters Creek never breaks the HCCA's six-inch grass rule, but it still needs brushing, rinsing and infill top-ups to look kept up. Priced by visit, 2026.",
        "h1": "Keeping Hunters Creek turf clean between community inspections",
        "lede": capsule(
            "Turf cleaning in Hunters Creek, power brooming, pet-odor treatment and an infill top-up, is priced by "
            "the visit and by how long it's been since the last one, not by the square foot. The Hunter's Creek "
            "Community Association's Community Standards Department enforces a tidy, well-kept look across the "
            "neighborhood, and a turf lawn that's brushed and rinsed on a routine schedule clears that bar "
            "year-round without the mowing a natural lawn needs to stay under the six-inch height rule."
        ),
        "sections": [
            ("The association's own standard for a tidy lawn, met a different way",
             "<p>The HCCA's Community Standards Department exists to keep the neighborhood looking maintained, and "
             "its published rules cap natural lawn grass at six inches, a limit that assumes mowing on a schedule. "
             "Turf never grows past that limit in the first place, but it still needs its own upkeep to keep "
             "looking the way it did on installation day: brushing the pile back upright against matted paths, "
             "rinsing off pollen and debris, and topping up infill that settles or washes out over time. Skipping "
             "that upkeep doesn't break a height rule the way overgrown grass would, but a flattened, thin lawn "
             "draws the same kind of attention from a passing neighbor.</p>"),
            ("Pet-odor treatment where a dog run shares the same fence line",
             "<p>Plenty of back yards here combine a family lawn with a dog run along the same fence, often the "
             "identical narrow strip a zero-lot-line village like Foxhaven or Ocita was built with, and pet turf in "
             "that shared space needs a tighter rinse-and-clean schedule than the rest of the lawn sees. Zeolite or "
             "coated-sand infill used for odor control depletes faster with heavier daily traffic, so a cleaning "
             "visit on a combined lawn-and-run yard typically treats the two zones differently: standard power "
             f"brooming across the open lawn, a closer look at infill depth along the fence line. {post('how-to-get-dog-urine-smell-out-of-artificial-turf', 'Getting odor out of pet turf')} has the full routine.</p>"),
            ("Leaf litter along the golf corridor and conservation edges",
             "<p>Lots backing Hunter's Creek Golf Club's fairways or the conservation land near the county line "
             "collect more windblown leaf litter and clippings than an interior lot does, material that can work "
             "down into turf infill over time much the way pet waste does if it's left too long. A cleaning visit "
             "on one of these edge lots usually spends more time on debris removal before the power-brooming step "
             "than a typical interior-lot visit would, since the base only drains as well as the infill layer "
             "sitting on top of it lets it.</p>"),
        ],
        "scenario": ("Say your 900 sq ft lawn has two dogs using it daily",
                     "<p>Say you have a 900 sq ft rear lawn in Mallard Cove shared by two dogs, where the smell has "
                     "started coming back faster than it used to between routine rinses. A cleaning visit for a "
                     f"yard that size is priced by the visit rather than the {price('residential')} per sq ft range "
                     "an install would use, and typically runs a fraction of that install cost, since the work is "
                     "deep power brooming, a sanitizing treatment and an infill top-up rather than buying and "
                     "laying new material.</p>"),
        "faqs": [
            faq("How often should Hunters Creek turf be professionally cleaned?",
                "It depends on pets and shade, but a yard with a dog benefits from more frequent attention than one "
                "without, since odor concentrates faster in warm months than a homeowner's own hose rinsing alone "
                "usually clears."),
            faq("Does the HCCA ever inspect for turf maintenance specifically?",
                "The Community Standards Department enforces a general well-kept appearance rather than a "
                "turf-specific checklist, so a matted, thin or odorous lawn is more likely to draw a general "
                "complaint than a turf-specific citation."),
        ],
        "sources": SRC,
    },
    "replacement": {
        "title": "Replacing Aging Turf in Hunters Creek, FL",
        "meta": "The community's oldest turf conversions are reaching the end of a 10-20 year lifespan, and reused base can keep a Hunters Creek replacement below full price. 2026.",
        "h1": "When it's time to replace turf in Hunters Creek",
        "lede": capsule(
            "Turf replacement in Hunters Creek, tearing out a worn lawn and rebuilding the base where needed, is "
            "priced closer to a fresh install than to a repair visit, since most of the material is new either way. "
            "With the community's housing stock now 20 to 35 years old, the earliest turf conversions here are "
            "reaching or passing the far end of a typical lifespan, showing up as more replacement calls than "
            "new-lawn calls in some of the older villages."
        ),
        "sections": [
            ("Why a 15-year-old lawn here is due, not just worn",
             "<p>Turf generally lasts ten to twenty years depending on UV stabilization, traffic and infill, and an "
             "early adopter who converted a lawn here not long after the community's mid-2000s build-out finished "
             "is now well into that window, sometimes past it. A lawn approaching that age often shows fading and "
             "thinning blade fiber before the base underneath actually fails, which points toward a straightforward "
             "tear-out and reinstall over the existing crushed-rock base, if it still drains the way it should, "
             "rather than a full rebuild from bare soil.</p>"),
            ("Reusing the base when it still works, rebuilding it when it doesn't",
             "<p>An older lawn's base gets tested before a single new roll of turf goes down: a section that still "
             "drains within a couple of minutes under a hose test can usually be reused, holding the job's cost "
             "under a first-time install's full range, while a section that's compacted, contaminated with fines, "
             "or settled unevenly needs to come out and get rebuilt to the washed, open-graded standard Florida's "
             "current turf rule requires on any covered lot. On this area's sandy flatwoods soil, a base that was "
             "under-built the first time around is more likely to have failed by year ten than one built to full "
             "depth from the start.</p>"),
            ("Sod struggling under the same watering limits often ends the same way",
             "<p>Not every replacement call here starts with old turf; plenty start with St. Augustine sod that's "
             "thinned out under the county's seasonal watering schedule and the area's slow-draining soil, to the "
             "point a homeowner decides to convert rather than keep re-sodding. That's a different project than "
             "swapping out aging turf, closer to a first-time residential install, but it lands in the same "
             "category because the decision is the same: weighing another round of sod and irrigation against a "
             "one-time build that doesn't depend on the county's watering days at all.</p>"),
        ],
        "scenario": ("Say you have a 750 sq ft lawn installed in the mid-2010s",
                     "<p>Say you have a 750 sq ft backyard lawn in Settlers Landing installed around 2014, now "
                     "fading and thinning after more than a decade of Central Florida sun, with a base that still "
                     f"passes a quick drainage check. Reusing that base keeps the job below a first-time install's "
                     f"full {price('residential')} per sq ft range, since only the turf, seams and infill are new, "
                     "though the exact number depends on how much of the old material a crew ends up pulling out "
                     "once the surface comes off.</p>"),
        "faqs": [
            faq("How do I know if my Hunters Creek turf needs replacing rather than repairing?",
                "Widespread fading, matting that brushing won't fix, or a base that no longer drains within a "
                "couple of minutes under a hose all point toward replacement rather than a spot repair."),
            faq("Does a replacement job need a new HCCA application?",
                "If the footprint and product stay the same as what was originally approved, usually not; a "
                "different footprint, product or drainage plan does need a fresh application."),
        ],
        "sources": SRC,
    },
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
