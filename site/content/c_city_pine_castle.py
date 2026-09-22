# -*- coding: utf-8 -*-
from _helpers import page, capsule, sec, table, faq, a, svc, city, post, src, ext, price
from _cityservice import cityservice_pages

SLUG = "pine-castle"

SRC = [
    "dep-rule", "fs125572", "usda-wss",
    ("Orange County Property Appraiser — parcel search", "https://ocpafl.org/"),
    ("Orange County Fast Track Online Services", "https://fasttrack.ocfl.net/OnlineServices/"),
    ("Orange County Code, Chapter 24, Municode Library", "https://library.municode.com/fl/orange_county/codes/code_of_ordinances?nodeId=PTIIORCOCO_CH24LABUOPSP"),
    ("Orange County Utilities — watering restrictions", "https://www.orangecountyfl.net/watergarbagerecycling/wateringrestrictions.aspx"),
    ("U.S. Census Bureau QuickFacts, Pine Castle CDP, Florida", "https://www.census.gov/quickfacts/fact/table/pinecastlecdpflorida/PST045224"),
    ("Orange County Water Atlas — Boggy Creek Watershed", "https://orange.wateratlas.usf.edu/watershed/?wshedid=2"),
    ("Orange County Water Atlas — Lake Jennie Jewel", "https://orange.wateratlas.usf.edu/waterbodies/lakes/140267/lake-jennie-jewel"),
    ("Orange County Water Atlas — Lake Gatlin", "https://orange.wateratlas.usf.edu/waterbodies/lakes/140208/lake-gatlin"),
    ("Orange County Water Atlas — Boggy Creek", "https://orange.wateratlas.usf.edu/waterbodies/rivers/130001/boggy-creek"),
    ("USDA NRCS official series description, Immokalee series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/I/IMMOKALEE.html"),
    ("USDA NRCS official series description, EauGallie series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/E/EAUGALLIE.html"),
    ("Pine Castle Historical Society — history", "http://www.pchsm.com/history/"),
    ("Pine Castle Pioneer Days Festival, Cypress Grove Park", "https://artsinorlando.com/event/pine-castle-pioneer-days-festival/"),
    ("Central Florida's Fascinating History: Pine Castle origins", "https://citruslandfl.blogspot.com/2017/03/pine-castle-origins.html"),
    ("Central Florida's Fascinating History: Orlando's Oak Ridge", "https://citruslandfl.blogspot.com/2017/10/orlandos-oak-ridge.html"),
]

# ============================================================== hub
HUB = page(
    "/areas/pine-castle/", "city",
    "Artificial Turf in Pine Castle, FL: Permits, Soil, Setbacks",
    "Turf installers serving unincorporated Pine Castle, FL: who reviews the permit, the county watering days, the 10-ft lake setback, and 1920s-60s lots explained.",
    "How turf installers handle an unincorporated Pine Castle yard",
    capsule(
        "We install, repair and clean artificial grass for Pine Castle homes, about 13 miles from downtown Kissimmee, at the same "
        f"{price('residential')} a square foot Central Florida installers charge everywhere else, current as of September 2026. Pine Castle "
        "is unincorporated Orange County, home to 11,122 residents and two small lakes, Jennie Jewel and Gatlin, worth knowing about "
        "before turf goes in the ground."
    ),
    "".join([
        sec("Who reviews a Pine Castle turf permit?",
            "<p>Pine Castle has never incorporated as its own city, so a permit here goes through Orange County's Permitting Services "
            "and Division of Building Safety instead of a local building department. The office takes calls at 407-836-5550 and posts "
            f"application status through {ext('https://fasttrack.ocfl.net/OnlineServices/', 'Fast Track Online Services')}. That matters because Pine Castle's edges "
            "run close to both the City of Orlando and the City of Edgewood, and a mailing address alone does not say which office actually "
            f"holds the parcel. The fix is a search on the {ext('https://ocpafl.org/', 'Orange County Property Appraiser')} site, which lists "
            "the taxing jurisdiction for any address before a crew shows up. Orange County's landscape code, Chapter 24, defines "
            "\"turf, turf grass or sod\" only as living species such as Bahia and St. Augustine, and as of September 2026 we found no "
            "separate section covering synthetic turf there, so a Pine Castle install answers to the state's own turf standard rather than "
            f"a local ordinance written for it. More on the office and the process is on {a('/laws/permits/orange-county/', 'our Orange County permit page')}, "
            f"and {a('/laws/florida-hb-683/', 'what the state rule itself requires')} applies here regardless of which office is on the phone.</p>"),
        sec("What yard types make up Pine Castle, and how do we adjust?",
            "<p>Pine Castle grew in layers rather than all at once, and the layer a lot belongs to usually decides how a crew approaches it more "
            "than the square footage does.</p>"
            + table("Pine Castle yard types and what we do differently",
                    ["Lot type", "What's usually there", "What changes with the install"],
                    [["A 1920s-40s cottage near the old town center", "A mature live oak or two and a narrow side yard", "Base built up rather than dug down near the roots, turf kept outside the drip line"],
                     ["A 1950s-60s ranch home on a quarter acre", "A flat, open backyard behind a block or stucco house", "A simple rectangle layout keeps waste low and the per-foot price near the bottom of the range"],
                     ["A lot near Lake Jennie Jewel or Lake Gatlin", "Sod running toward the shoreline or a low bank", "Turf stops 10 ft short of the water unless a seawall already separates the two"],
                     ["A corner lot with two street frontages", "A drainage swale along the side street as well as the front", "Grade splits toward two legal exit points instead of piling water on one"]])
            + "<p>None of that changes the price per foot. It changes how many hours the base and grading take before turf ever gets rolled out.</p>"),
        sec("Which utility waters a Pine Castle lawn, and under what schedule?",
            "<p>Orange County Utilities meters most of Pine Castle and allows two watering days a week between the second Sunday in March and "
            "the first Sunday in November, dropping to one day a week the rest of the year, with no sprinkler running between 10 a.m. and "
            "4 p.m. regardless of the season. None of that reaches a synthetic lawn once its heads are capped, since the state's May 2026 "
            f"standard bars watering turf from an in-ground system outright ({src('dep-rule', 'Rule 62-308.100')}). On the drainage side, Pine "
            f"Castle sits inside the {ext('https://orange.wateratlas.usf.edu/watershed/?wshedid=2', 'Boggy Creek Watershed')}, an 84.9-square-mile "
            "basin that carries Lake Jennie Jewel and Lake Gatlin, both on the town's edge toward Edgewood, south to East Lake Tohopekaliga. "
            "That outlet into the lake chain puts this part of the county in Kissimmee Basin territory administered out of South Florida's water "
            "agency, a separate line of authority from the St. Johns district that oversees water closer to downtown Orlando.</p>"),
        sec("What's different about turf in one of Orange County's oldest communities?",
            "<p>Will Wallace Harney named his home \"the Pine Castle\" for its pine-board towers on Lake Conway, and the town that grew up "
            "around it in 1884 still shapes what a crew finds on a lot here. The Pine Castle Woman's Club, organized in 1940, has run the "
            "Pine Castle Pioneer Days festival at Cypress Grove Park every February since 1973, and the oaks that shade many of the town's "
            "original streets, including West Avenue and Maud Avenue from an 1884 addition to the town, are now old enough that their canopies "
            "reach well past the trunk. The state's turf rule keeps synthetic grass out from under that canopy unless a certified arborist signs "
            f"off that digging near the roots will not hurt the tree, which {a('/artificial-turf-cost/', 'changes the shape of a quote')} more "
            "than the size of the yard does. A newer infill lot two streets over, with no oak older than the house, skips that step entirely.</p>"),
        sec("Does an older Pine Castle lot need HOA sign-off?",
            "<p>Most of Pine Castle's original platted lots predate any homeowners association, so there is no architectural review board to "
            "clear before turf goes in beyond the county itself. A newer subdivision built on land that was later carved out of the old town "
            "might have one, and where an association does exist, Florida law keeps it from banning turf that a fence or a hedge already hides "
            f"from the street or a neighbor's yard ({src('fs125572', 'F.S. 125.572')}; {a('/laws/hoa-rules/', 'more on what a Florida HOA can restrict')}). "
            "Either way, the county's own permitting rules still apply, and they do not bend for a private covenant.</p>"),
    ]) + "<!--AUTO:city-services-->",
    faqs=[
        faq("Do I need a permit to put artificial turf in a Pine Castle yard?",
            "Pine Castle is unincorporated, so Orange County's Permitting Services and Division of Building Safety handles it, not a city hall. "
            "Call 407-836-5550 or check Fast Track Online Services before work starts; Chapter 24 covers living grass, not synthetic turf, so the "
            "state standard is what actually governs the install."),
        faq("My address says Orlando or Edgewood. Does that change who I call?",
            "It might. Pine Castle's boundary runs close to both cities, and a postal address is not proof of jurisdiction. Search the parcel on "
            "the Orange County Property Appraiser's site first; if it comes back inside a city, that city's building department handles the permit instead."),
        faq("How close can turf come to Lake Jennie Jewel or Lake Gatlin?",
            "The state holds new turf back 10 ft from the shoreline, measured from the ordinary high-water mark rather than a fence or property "
            "pin. A lot with an existing seawall or bulkhead is measured from that structure instead, which in practice often leaves more usable yard."),
        faq("How do you find the best artificial turf contractor near Pine Castle?",
            f"A contractor worth calling back volunteers three things unprompted: how thick the compacted base runs, which turf product they are "
            f"quoting by name, and how much infill goes down per square foot. {post('how-to-compare-artificial-turf-quotes', 'Comparing two written quotes')} "
            "line by line catches a bid that leaves all three vague."),
        faq("How far is Pine Castle from your Kissimmee base?",
            "About 13 miles by road, well inside the roughly 40-mile area we cover. Distance mainly affects scheduling, not price; the per-square-foot "
            "range is the same here as it is in Kissimmee itself."),
    ],
    sources=SRC, city=SLUG, crumbs=[("Service areas", "/areas/")], crumb="Pine Castle",
    related=[("/areas/orange-county/", "Orange County: permits, water and soil"),
             ("/laws/permits/orange-county/", "Orange County permit rules for turf"),
             ("/areas/edgewood/", "Artificial turf in Edgewood"),
             ("/areas/oak-ridge/", "Artificial turf in Oak Ridge"),
             ("/areas/orlando/", "Artificial turf in Orlando"),
             ("/artificial-turf-cost/", "Full turf cost guide for Central Florida")],
)

# ============================================================== local
LOCAL = {
    "residential": {
        "title": "Artificial Grass Installation in Pine Castle: Old Oak Lots",
        "meta": "Artificial grass installation in Pine Castle, FL: drip-line rules for mature oaks, capping older irrigation, and 2026 pricing per square foot.",
        "h1": "Turf for Pine Castle's oak-shaded, in-town lots",
        "lede": capsule(
            f"A straightforward Pine Castle lawn conversion runs {price('residential')} installed, with most jobs settling at {price('residential', True)}; "
            "that range has held steady since we checked it in September 2026. What moves the number here is less the size of the yard than how "
            "many mature live oaks stand over it and how the base has to step around their roots."
        ),
        "sections": [
            ("Why the drip line decides more than the fence line",
             "<p>A live oak planted when Pine Castle was still a crossroads town has a canopy that now reaches well past its trunk, and Florida's "
             "turf rule keeps synthetic grass out from under that whole canopy, on this lot or the neighbor's, unless a certified arborist certifies "
             "that the work will not harm the tree. On a typical in-town lot that can put a third of the yard off-limits without a letter in hand. "
             "Where turf is allowed near a root zone, the base gets built up in shallow lifts rather than excavated down to the usual 2 to 4 inches, "
             "trading some depth for roots left undisturbed. Homeowners on West Avenue and Maud Avenue, part of an 1884 addition to the original town, "
             "often ask about this first, since the oaks along those blocks predate most of the houses.</p>"),
            ("Capping a sprinkler system nobody has a map for",
             "<p>A lot of Pine Castle's 1950s and 60s ranch homes still run the irrigation system installed with the house, long before anyone kept "
             "a zone map or a permit file. Before base material goes down, the crew traces every head that reaches the turf area and caps it at the "
             "valve, since the state standard bars watering synthetic grass from an in-ground system regardless of how old that system is. A hose "
             "handles the occasional rinse afterward. Where a head cannot be traced with confidence, capping it at the box rather than guessing "
             "underground avoids cutting into a base that was already compacted and finished.</p>"),
            ("What a narrow historic-grid lot means for equipment",
             f"<p>Streets platted in the 1880s were not laid out with a skid steer in mind, and a lot on one of {city('pine-castle', 'Pine Castle')}'s "
             "original narrow blocks often means wheelbarrows instead of machinery for part of the job. That adds labor hours on a small footprint, "
             "which is why a 400 sq ft in-town yard can price nearer the top of the range than a 1,200 sq ft ranch lot with a gate wide enough for a "
             "compact loader. Removing the old St. Augustine and its root mat is the same either way; getting the base material to the back of the "
             f"lot is where the two jobs diverge. {svc('residential', 'The full installation guide')} covers what goes into that base regardless of "
             "how it gets hauled in.</p>"),
        ],
        "scenario": ("Turf math for a 680 sq ft cottage yard",
                     "<p>Say you have a 680 sq ft backyard behind a 1948 cottage a few blocks from the old town center, with a single large oak "
                     "shading roughly a third of it. At the published range, that's $5,440 to $12,240 before any add-ons; most jobs this size land "
                     "closer to $6,800 to $10,880 once labor for the drip-line work is priced in. The oak itself does not raise the turf cost, since "
                     "material and per-foot labor stay the same in shade as in sun. What it adds is the arborist letter, if the root zone reaches "
                     f"into the turf area, and a few extra hours building the base up instead of down near the trunk. {post('artificial-turf-near-live-oaks-and-palms', 'Whether a given oak forces that step')} "
                     "depends on where the canopy actually falls, not on the tree's age alone.</p>"),
        "faqs": [
            faq("Do I need an arborist before installing turf under my oak?",
                "Only if the turf area falls inside the tree's drip line. Outside the canopy, no letter is required. We can usually tell from a walk "
                "of the yard whether the layout needs one before we quote it."),
            faq("Is there an HOA review for an old Pine Castle lot?",
                "Most of the original platted lots have none. A newer pocket subdivision carved out of the old town might, in which case Florida "
                "law still protects turf that a fence hides from the street or a neighbor's parcel."),
            faq("Does an older irrigation system on my lot cause problems?",
                "Not for the turf itself. It means the crew spends more time tracing heads before capping them, since a lot from the 1950s or 60s "
                "rarely has a zone diagram on file anywhere."),
        ],
        "sources": SRC,
    },
    "pet": {
        "title": "Pet Turf & Dog Runs for Pine Castle's Narrow Lots",
        "meta": "Pet turf and dog runs in Pine Castle, FL: fast-draining systems for narrow historic-grid yards, flatwoods soil, and 2026 market pricing.",
        "h1": "Dog-run turf built for Pine Castle's tighter yards",
        "lede": capsule(
            f"Dog owners on Pine Castle's older, narrower lots pay {price('pet')} a square foot for a turf run built to drain fast and "
            f"shed odor, a figure that has stood since our September 2026 check and typically lands at {price('pet', True)}. The flatwoods "
            "sand under most of the town holds water near the surface, which is exactly what a pet system's base has to work around."
        ),
        "sections": [
            ("Flatwoods sand and why a dog run needs deeper drainage",
             "<p>Soil maps for this part of Orange County show Immokalee and EauGallie fine sands, both poorly drained flatwoods soils where the "
             "water table can sit within 6 to 18 inches of the surface for one to four months most years. A plain lawn tolerates that; a dog run "
             "carrying daily urine and a hose rinse does not, so pet turf here leans on the fuller 4-inch end of the washed crushed rock base rather "
             "than the minimum, giving liquid somewhere to go before it reaches saturated native sand. Skipping the weed barrier under a pet area, "
             "standard practice regardless of soil, matters even more on this ground, since trapped liquid on top of already-slow-draining sand is "
             "the fastest way to a smell that will not rinse out.</p>"),
            ("A zero-lot-line side yard on the historic grid",
             "<p>Several of Pine Castle's original blocks, platted narrow in the 1880s and filled in through the 1950s, leave side yards barely "
             "wide enough for a dog to turn around in, let alone a full lawn. A dedicated run along that strip, fenced separately from the rest of "
             "the yard, uses the space better than trying to pet-proof an entire small lot, and it isolates the odor-control infill to the area that "
             "actually needs it. Chain-link along a property line here is common enough that tying the turf's edge into the existing fence, rather "
             "than adding a separate border, is often the simpler fix.</p>"),
            ("Why the town's oak canopy affects a run's layout, not its cost",
             f"<p>A dog run tucked under oak shade behaves differently than one in full sun: it never gets as hot underfoot, but leaf litter and "
             "acorns build up faster and need clearing before they work into the infill. Where the shade falls inside a tree's drip line, the same "
             "arborist rule that applies to a residential lawn applies to a run, so the layout sometimes shifts a few feet rather than the tree "
             f"coming down or the project stalling. {svc('pet', 'The full pet turf drainage and infill breakdown')} covers the zeolite-versus-silica "
             "choice in more depth than a single yard's shade pattern changes.</p>"),
        ],
        "scenario": ("A 240 sq ft run behind a duplex-style lot",
                     "<p>Say you have a 240 sq ft side yard behind a 1955 concrete-block duplex conversion near the old town center, fenced on "
                     "three sides already. At the published pet-turf range that's $2,400 to $4,320, with most jobs this size landing at $2,880 to "
                     "$3,840 once zeolite infill is added for odor control. Because the space is narrow, more of that total goes to labor and hand "
                     "compaction than it would on an open backyard the same size; the base still runs the fuller 4 inches given the flatwoods soil "
                     "underneath. A flush-out hose bib at one end, if there is not one already, is worth adding while the ground is open.</p>"),
        "faqs": [
            faq("Does Pine Castle's sandy soil make pet turf smell worse?",
                "Not if the base is built for it. Immokalee and EauGallie soils hold water close to the surface, so pet systems here use a deeper, "
                "fully washed rock base and skip the weed barrier so nothing traps liquid at ground level."),
            faq("What do the best pet turf systems near Pine Castle actually need on this soil?",
                "Fast drainage first: a 3 to 4 inch washed crushed rock base, no fabric underneath, and zeolite or coated sand infill rather than plain "
                "silica. Everything else, fencing and layout, follows the shape of the lot."),
        ],
        "sources": SRC,
    },
    "putting": {
        "title": "Backyard Putting Greens in Pine Castle Under Oak Canopy",
        "meta": "Backyard putting greens in Pine Castle, FL: contouring flat ranch lots, staying outside oak drip lines, and 2026 installed pricing.",
        "h1": "Putting greens built around Pine Castle's oaks",
        "lede": capsule(
            f"A backyard putting green in Pine Castle prices between {price('putting')} a square foot, September 2026 figures that swing more "
            f"on contouring and fringe than on the green's overall size, with most builds landing at {price('putting', True)}. The town's flat "
            "post-war ranch lots are naturally suited to a green; its mature oaks are the thing that decides where one can go."
        ),
        "sections": [
            ("Why a flat 1950s ranch lot is a good starting point",
             "<p>Many of Pine Castle's ranch homes sit on lots graded flat and open decades ago, with none of the slope or retaining-wall work that "
             "complicates a green elsewhere in Central Florida. That head start shows up in labor, not material: shaping breaks and a false edge into "
             "an already-level pad takes less excavation than building contour from a sloped starting point. The trade-off is that a flat lot often "
             "carries one dominant oak near the property line rather than several smaller trees spread out, which concentrates the drip-line problem "
             "in one spot instead of scattering it across the yard.</p>"),
            ("Keeping the green and fringe outside the canopy",
             "<p>The same rule that keeps a residential lawn out from under an oak's canopy applies to a putting green and its fringe turf, since "
             "both are synthetic grass under the state's standard. Root zones under a mature oak on a Pine Castle lot can run wider than the canopy "
             "itself, so a green designed to end right at the drip line sometimes needs to pull back further once the roots are actually located. "
             "A certified arborist's sign-off opens up ground that would otherwise be off-limits, which on a small lot can be the difference between "
             "a 200 sq ft green and one half that size.</p>"),
            ("Fringe turf on flatwoods sand versus ridge sand",
             "<p>Pine Castle's flatwoods soil, mapped mostly to Immokalee and EauGallie series, holds more moisture near the surface than the drier "
             "ridge sand found toward Lake County. That does not change how a putting surface plays, since the base and backing handle drainage "
             "either way, but it does mean the fringe turf's base gets built to the same washed, open-graded standard as the green itself rather than "
             "a lighter spec, so the two surfaces settle at the same rate over the years instead of one dipping before the other.</p>"),
        ],
        "scenario": ("A 320 sq ft green with fringe on a ranch lot",
                     "<p>Say you have a flat 320 sq ft area at the back of a 1958 ranch home, room enough for a green with two cups and a modest "
                     "fringe once a single oak's drip line is mapped out. At the published range that prices between $4,480 and $9,600, with most "
                     "builds this size landing near $5,760 to $8,000 depending on how much contouring the design calls for. Because the lot is "
                     "already flat, less of that total goes toward grading than on a sloped yard the same size; more of it goes to the cups, the "
                     "fringe transition and keeping the whole layout clear of the root zone next door.</p>"),
        "faqs": [
            faq("Can a putting green go under my oak tree in Pine Castle?",
                "Not inside the drip line, unless a certified arborist certifies the install will not damage the roots. Most greens here get "
                "designed around the canopy rather than under it."),
            faq("Does Pine Castle's soil affect how a putting green plays?",
                "No. The green's roll and speed come from the turf, pad and backing, not the native sand underneath, as long as the base beneath "
                "it is built to the same washed-rock standard as anywhere else."),
            faq("How big a green fits on a typical Pine Castle ranch lot?",
                "It depends more on where the oaks fall than on the lot's total size. A quarter-acre yard with a canopy along one side can still "
                "fit a 200 to 350 sq ft green once the drip line is mapped out."),
        ],
        "sources": SRC,
    },
    "playground": {
        "title": "Playground Turf Near Pine Castle's Cypress Grove Park",
        "meta": "Playground turf in Pine Castle, FL: shock-pad sizing for home play areas, oak-canopy shade, and 2026 installed pricing per square foot.",
        "h1": "Play-area turf for Pine Castle's ranch-home yards",
        "lede": capsule(
            f"September 2026 pricing puts playground-grade turf in Pine Castle at {price('playground')} a square foot, with the shock pad "
            f"underneath moving that number more than the surface fabric does, and most home play areas landing at {price('playground', True)}. "
            "Families near Cypress Grove Park, where the town's Pioneer Days festival has run every February since 1973, are typical buyers here."
        ),
        "sections": [
            ("Sizing the pad to the equipment, not the yard",
             "<p>A shock pad has one job: keeping a fall from a swing set or a climbing structure survivable, and the pad thickness that does that "
             "is set by the equipment's fall height, not by how much yard space is available around it. A small residential set with a 4-foot fall "
             "height needs far less pad than a taller structure, and pricing a play area without knowing the fall height first is guessing. Families "
             "renovating a ranch home near Cypress Grove Park for a young child tend to already have the play structure picked out before calling, "
             "which makes this measurement the first thing worth confirming.</p>"),
            ("Shade from an oak canopy changes upkeep, not safety",
             "<p>A play area set under one of Pine Castle's older oaks runs cooler underfoot through a Florida summer than one in open sun, which "
             "matters for bare feet and knees more than for the shock pad's performance. The trade-off is leaf and acorn litter, heaviest through late "
             "winter, working down into the infill faster than it would in an open yard. Clearing debris before it decomposes into the surface keeps "
             "drainage and cushioning working the way they were built to; letting it sit is the more common reason an otherwise well-built play area "
             "starts to hold water after a storm.</p>"),
            ("What the state rule allows under the equipment itself",
             "<p>Florida's May 2026 turf standard reserves rubber and other synthetic infill for the ground directly under playground equipment, "
             "the one place on a residential property where that material is allowed at all; the rest of a home lawn, pool deck or fringe area has to "
             "use silica sand, rock, shell or a coated natural material instead. That line matters on a combination yard where turf runs from an open "
             f"play area into a plain lawn, since the two sections legally take different infill even though they look the same from the porch. "
             f"{svc('playground', 'The playground turf guide')} goes through pad thickness ranges by fall height in more detail.</p>"),
        ],
        "scenario": ("A 200 sq ft play area behind a ranch home",
                     "<p>Say you have a 200 sq ft corner of the backyard set aside for a swing set with a 5-foot fall height, a few blocks from "
                     "Cypress Grove Park. At the published range that prices between $2,000 and $5,000, with most jobs this size landing near $2,400 "
                     "to $3,800 once a shock pad sized to that fall height is added. A chunk of that total is the pad itself rather than the turf "
                     "on top, which is why two 200 sq ft quotes with different equipment underneath can land at noticeably different numbers even "
                     "though the visible surface looks identical.</p>"),
        "faqs": [
            faq("What information do you need before quoting playground turf?",
                "The equipment's fall height above all, since that sets the shock pad thickness. Overall area and whether any of it falls under an "
                "oak canopy come next."),
            faq("Can rubber infill go under a swing set in Pine Castle?",
                "Yes, that is the one place the state standard allows it. The rest of the yard, including any turf just outside the equipment's "
                "footprint, has to use a natural-material infill instead."),
        ],
        "sources": SRC,
    },
    "pool": {
        "title": "Pool & Lanai Turf for Pine Castle Screen Enclosures",
        "meta": "Pool and lanai turf in Pine Castle, FL: glue-down edges over concrete, drainage under a screen cage, and 2026 installed pricing.",
        "h1": "Turf for inside a Pine Castle pool cage",
        "lede": capsule(
            f"Inside a screened Pine Castle lanai, turf prices the same as an open lawn, {price('residential')} a square foot as of September "
            "2026, though a small pool-deck strip often lands near the top of that range. Many of the town's pool cages date to the 1970s and "
            "80s infill years, when a screen enclosure was the standard way to add a pool to an older lot."
        ),
        "sections": [
            ("Why concrete inside a cage needs a different edge",
             "<p>A lanai floor is almost always concrete, so turf laid across it cannot anchor into soil the way a lawn's perimeter does; the "
             "edge instead bonds to the slab with adhesive, and a drainage underlay goes beneath the turf itself to move water toward whatever deck "
             "drain the pool already has. That underlay does more work here than open lawn ever needs, since a lanai floor has nowhere else for "
             "rainwater blown in through the screen to go. Skipping it is the single most common reason a pool-deck turf job ends up holding water "
             "after a storm even though the yard beyond the cage drains fine.</p>"),
            ("Shade from the house and the cage itself",
             "<p>A screen enclosure cuts direct sun by roughly a third depending on the mesh, and a Pine Castle lanai on the shaded side of the "
             "house gets even less, which is exactly the condition that kills St. Augustine sod around a pool deck in the first place. Turf does "
             "not care about the light level, so the shade that used to be the whole problem stops mattering once synthetic grass replaces the sod "
             "strip along the cage's edge. The one place shade still matters is heat: a fully shaded pool-deck strip stays noticeably cooler "
             "underfoot through summer than an open lawn a few feet away in full sun.</p>"),
            ("Checking the windows before choosing turf color",
             "<p>Some of Pine Castle's older pool additions sit close enough to a neighboring house that low-emissivity glass on a west- or "
             "south-facing window can reflect enough concentrated sun to soften a nearby patch of turf, since polyethylene blades give way "
             "starting around 175 to 200°F under that kind of focused heat. It is a quick check to make before ordering material: stand where the "
             "turf will go in the late afternoon and look for a bright reflected glare off any nearby glass. A lighter-colored product or a small "
             "shift in layout usually solves it without any change to the underlying build.</p>"),
        ],
        "scenario": ("A 450 sq ft lanai strip around a screened pool",
                     "<p>Say you have a 450 sq ft ring of turf planned around a screened pool added to a 1978 ranch home, replacing sod that has "
                     "thinned out along the shaded side. At the residential range that prices between $3,600 and $8,100, with most lanai jobs this "
                     "size landing near $4,500 to $7,200 once the drainage underlay and glue-down edging are figured in. Because the space is "
                     "narrow and runs against a concrete deck the whole way around, expect the labor share of that total to run higher than it "
                     "would on an open backyard rectangle of the same size.</p>"),
        "faqs": [
            faq("Does turf inside a screen cage need a different base than an open lawn?",
                "Where it sits on soil, no. Where it sits on the concrete deck itself, yes: it needs a drainage underlay and glued edges instead "
                "of a compacted rock base and nailed perimeter."),
            faq("Will low-E windows near my Pine Castle pool melt the turf?",
                "Only if the reflection is concentrated and direct, which is worth checking before installation. A lighter turf color or a small "
                "layout adjustment usually resolves it without any change to the base."),
        ],
        "sources": SRC,
    },
    "repair": {
        "title": "Artificial Turf Repair in Pine Castle, FL",
        "meta": "Artificial turf repair in Pine Castle, FL: diagnosing lifted seams, storm damage near the lake setback, and how a repair visit works.",
        "h1": "Fixing turf that was built for somewhere else",
        "lede": capsule(
            "A lifted seam or a scorched patch on a Pine Castle lawn gets diagnosed in person, since repair is quoted after photos or a site "
            "visit rather than off a per-square-foot chart. As of September 2026, most callouts here start with checking who actually installed "
            "the lawn and whether that crew understood they were working in unincorporated Orange County."
        ),
        "sections": [
            ("When the installer did not know the jurisdiction",
             "<p>Because Pine Castle sits close enough to Orlando and Edgewood that an address alone does not settle which office has authority, "
             "a crew unfamiliar with the area sometimes builds to a generic Central Florida spec without checking the county's own landscape code "
             "or confirming the lot was not inside a swale or too close to a lake. That does not usually show up as a code violation years later; "
             "it shows up as a base that was never quite right for this specific lot, a corner that never anchored properly, or infill that "
             f"migrates toward a low point faster than it should. {a('/laws/permits/orange-county/', 'Confirming the permitting picture')} before a "
             "repair starts is often the fastest way to figure out what was skipped the first time.</p>"),
            ("Storm damage near Lake Jennie Jewel or Lake Gatlin",
             "<p>A yard within the state's 10-ft waterbody setback of either lake carries slightly more risk in a hard summer storm, since wind and "
             "standing water both concentrate at the point closest to open water. An edge that was stapled instead of properly bonded tends to lift "
             "there first, and infill can wash toward the setback line if the original grade sent water in that direction instead of toward a proper "
             f"drain point. {post('artificial-turf-hurricane-flooding', 'What a hurricane or heavy flooding actually does to a lawn')} covers the "
             "broader pattern; a lakeside Pine Castle lot just sees it sooner than a lot in the middle of a block.</p>"),
            ("Reading a base that was built wrong from the start",
             "<p>A rushed base does not announce itself on installation day, since the surface looks the same whether the crew compacted it "
             "properly or not. The tell comes later: a section that settles just enough to hold water overnight, or unwashed fill that clogs with "
             "fine particles until the base stops draining at all. On an older Pine Castle lot where the original install predates the state's "
             "current material standard, a repair sometimes means pulling back further than the damaged spot itself to reach base that was actually "
             "built correctly.</p>"),
        ],
        "scenario": ("Diagnosing a 35 sq ft lifted section",
                     "<p>Say you have a 35 sq ft patch near a side gate where the seam has pulled up and infill has washed thin, on a lawn "
                     "installed by a crew that is no longer around to ask. As of September 2026 we would not quote that over the phone; a repair "
                     "call starts with photos or a short visit to see whether the seam itself failed or the base underneath it settled, since "
                     "those two problems get fixed differently and only one of them means pulling turf back further than the visible damage. A gate "
                     "that gets heavy foot or cart traffic is a common place for this kind of lift to start.</p>"),
        "faqs": [
            faq("Why can't you give a repair price without seeing the yard?",
                "Because the same symptom, a lifted edge or a bare patch, can come from a failed seam, a settled base or migrated infill, and each "
                "one takes a different fix. Photos or a visit tell us which one we are actually dealing with."),
            faq("What should the best turf repair company near Pine Castle check before quoting a fix?",
                "Whether the problem is the surface or what's underneath it. A company that quotes a lifted edge without asking about the base, "
                "the grade, or how close the spot is to a lake setback is guessing at the real cause."),
            faq("Is storm damage near the two lakes covered by a warranty?",
                "That depends on the original installer's workmanship warranty, which is separate from the turf manufacturer's material warranty. "
                "Ask which one, if either, was in writing before assuming a repair is covered."),
        ],
        "sources": SRC,
    },
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
