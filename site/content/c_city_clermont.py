# -*- coding: utf-8 -*-
"""Clermont, Lake County, tier 2. Building Services and water facts checked directly against
clermontfl.gov; Green Swamp/SJRWMD split checked against the FloridaDEP Green Swamp Florida
Forever description and Clermont's own Water Conservation page. See docs/TIER2-BRIEF.md."""
from _helpers import page, capsule, sec, table, faq, a, svc, city, county, cs, post, src, ext, price
from _cityservice import cityservice_pages

SLUG = "clermont"

BUILDING = ("City of Clermont — Building Services", "https://www.clermontfl.gov/departments/building-services/")
WATER = ("City of Clermont — Water Conservation", "https://www.clermontfl.gov/235/Water-Conservation")
LAKE_PA = ("Lake County Property Appraiser — parcel search", "https://www.lakecopropappr.com/")
LAKE_PERMIT = "/laws/permits/lake-county/"
GREEN_SWAMP = ("Florida DEP — Green Swamp Florida Forever project description", "https://floridadep.gov/sites/default/files/FLDEP_DSL_OES_FF_2026_GreenSwamp.pdf")
ASTATULA_OSD = ("USDA NRCS — official series description, Astatula series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/A/ASTATULA.html")
CANDLER_OSD = ("USDA NRCS — official series description, Candler series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/C/CANDLER.html")
SUGARLOAF = ("Wikipedia — Sugarloaf Mountain (Florida)", "https://en.wikipedia.org/wiki/Sugarloaf_Mountain_(Florida)")
CHAIN = ("Wikipedia — Clermont chain of lakes", "https://en.wikipedia.org/wiki/Clermont_chain_of_lakes")
NTC = ("National Training Center, Clermont — triathlon training", "https://usantc.com/training/triathlon/")
CHAMPIONS = ("WKMG ClickOrlando, May 16, 2025 — Clermont's \"Choice of Champions\" sports-tourism identity", "https://www.clickorlando.com/news/local/2025/05/16/choice-of-champions-clermont-offers-unique-landscape-commitment-to-sports-tourism/")
KINGS_RIDGE = ("55places — Kings Ridge, Clermont", "https://www.55places.com/florida/communities/kings-ridge")
LEGENDS = ("Zillow — Legends Golf & Country Club, Clermont", "https://www.zillow.com/clermont-fl/legends-golf-country-club_att/")
LOST_LAKE = ("Homes.com — Lost Lake neighborhood guide, Clermont", "https://www.homes.com/local-guide/clermont-fl/lost-lake-neighborhood/")
PARKS = ("City of Clermont — Parks", "https://www.clermontfl.gov/247/Parks")
SPLASH = ("City of Clermont — Champions Splash Park", "https://www.clermontfl.gov/facilities/facility/details/Champions-Splash-Park-31")
CENSUS = ("U.S. Census Bureau — QuickFacts, Clermont city, Florida", "https://www.census.gov/quickfacts/fact/table/clermontcityflorida")

SRC = [BUILDING, WATER, LAKE_PA, GREEN_SWAMP, ASTATULA_OSD, CANDLER_OSD, SUGARLOAF, CHAIN, NTC, CHAMPIONS,
       KINGS_RIDGE, LEGENDS, LOST_LAKE, PARKS, SPLASH, CENSUS, "dep-rule", "fs125572", "fs7203045"]

HUB = page(
    "/areas/clermont/", "city",
    "Artificial Turf Installation in Clermont, FL (2026)",
    "Artificial grass for Clermont's sloped ridge lots and lake shoreline, with the Lake County permit path, city water rules and soil facts, checked September 2026.",
    "Turf built for Clermont's hills, not a flat lot",
    capsule(f"We install, repair and clean artificial turf around Clermont, about 28 miles from Kissimmee. Installed turf here still runs {price('residential')} a square foot, the September 2026 figure for every town we cover. Clermont sits on the Lake Wales Ridge, and a sloped, fast-draining lot changes how a crew builds the base far more than it changes the price."),
    "".join([
        sec("A hill town in a state that mostly doesn't have them",
            f"<p>Clermont's skyline is rolling hills, and that alone sets it apart from most of the towns we serve. {ext(SUGARLOAF[1], 'Sugarloaf Mountain')} sits just outside city limits and tops out at 312 feet, the highest point on peninsular Florida, and the same ridge runs straight through town under the roads and yards a crew works on every week. A lawn built on a grade doesn't drain the way a flat Osceola County yard does, and it doesn't erode the way one does either, once the base and edges are built for the slope instead of against it.</p>"
            + f"<p>That terrain is also why Clermont brands itself the {ext(CHAMPIONS[1], 'Choice of Champions')}: the {ext(NTC[1], 'National Training Center')} on Don Wickham Drive has hosted USA Triathlon athletes since 2001, and the hills that make a backyard tricky are the same hills triathletes drive in for. A yard here often belongs to someone who already thinks about grade, traction and heat the way a cyclist does, a different starting conversation than a flat subdivision an hour east.</p>"),
        sec("Who reviews a turf permit here, and what our own site doesn't cover",
            f"<p>Clermont runs its own {ext(BUILDING[1], 'Building Services division')} out of 685 W. Montrose St., reachable at 352-241-7315, with online applications through the city's eTRAKiT portal. That office has the final word on how Clermont's own land development code treats a turf project; our own site goes only as far as {a(LAKE_PERMIT, 'the unincorporated Lake County rules')}, since we haven't put together a page decoding the city's municipal code the way we have for the county. What we can say is that {a('/laws/florida-hb-683/', 'the new state turf standard')} sets a floor Clermont can't undercut on a covered single-family lot regardless of what the city's own code does or doesn't say.</p>"
            + f"<p>A homeowners association is a separate step from the permit counter. {a('/laws/hoa-rules/', 'Florida law limits what an HOA can restrict')} to turf visible from the street or a neighboring lot, and an architectural review committee in a community like Kings Ridge or Legends works through its own submittal packet on its own schedule, independent of whatever the city decides about a permit.</p>"),
        table("Clermont yard types and what we do differently",
              ["Yard type", "Where it shows up in Clermont", "What changes for the turf job"],
              [["55-plus and golf-community lots", "Kings Ridge and Legends, gated, smaller footprints", "ARC packet first; base compacted in two lifts on a graded rear slope"],
               ["2000s Spanish-style subdivisions", "Lost Lake and similar built-out streets", "Wider lots, but runoff still needs a deliberate path away from the slab"],
               ["Older in-town lots near the lake", "Blocks close to Lake Minneola and downtown", "10-ft waterbody setback and a drip-line check under mature oaks"],
               ["New construction on the ridge", "Newer streets climbing toward the hilltops", "Builder sod strips fast on Candler and Astatula sand; base still goes in per the state rule"],
               ["Steep hillside lots", "Streets closest to Sugarloaf Mountain's flank", "Terracing or extra anchoring at the downhill edge instead of a flat base"]],
              "Prices don't change by neighborhood; the shape of the base and the edge work does."),
        sec("City water on a ridge that mostly drains toward St. Johns",
            f"<p>Clermont runs its own water utility rather than buying from a county system, and the city's own conservation page says outside watering follows {ext(WATER[1], 'the St. Johns River Water Management District rules')}: odd addresses water Wednesday and Saturday, even addresses Thursday and Sunday during daylight saving time, never between 10 a.m. and 4 p.m. None of that reaches a synthetic lawn once its heads are capped, which the state's turf rule requires either way.</p>"
            + f"<p>Lake County isn't uniformly St. Johns territory, though. {ext(GREEN_SWAMP[1], 'a Florida DEP Green Swamp project description')} draws that state land's boundary as starting from the southwest corner of the city of Clermont, which puts a sliver of the city's far southwest edge inside the Southwest Florida Water Management District's Green Swamp area while the rest of Clermont, including downtown and the lake, sits in St. Johns territory. It's worth knowing which side of that line a specific lot falls on before assuming a watering schedule.</p>"),
        sec("Kings Ridge, Legends, Lost Lake: three decades of hillside subdivisions",
            f"<p>Clermont's 2020 Census population was 43,021, more than four times the 9,475 counted in 2000 ({ext(CENSUS[1], 'Census QuickFacts')}), and most of that growth shows up as subdivisions climbing the ridge rather than spreading flat. {ext(KINGS_RIDGE[1], 'Kings Ridge')} is a gated 55-plus community of roughly 2,000 homes across two golf courses, with {ext(LEGENDS[1], 'Legends Golf & Country Club')} across the street running a similar layout for a younger buyer. {ext(LOST_LAKE[1], 'Lost Lake')}, developed through the 2000s, carries wider lots and Spanish-style homes a short drive from downtown.</p>"
            + "<p>None of the three has a published design document we could find that names synthetic turf specifically, so we're not going to invent an ARC rule for any of them. What we can say is that an application packet with a product sample, a site plan and the state's material specs in hand tends to move faster through a committee than one without.</p>"),
        sec("Choosing an installer when the yard isn't flat",
            "<p>A common question from a new Clermont homeowner is some version of \"who's the best artificial turf contractor near Clermont for a sloped lot?\" The honest answer has less to do with a company's name than with whether the crew asks about grade before it talks about turf brands. Anyone who quotes a hillside yard the same way they'd quote a flat one in St. Cloud hasn't accounted for the extra compaction passes or the anchoring a downhill edge needs.</p>"
            + "<p>Candler and Astatula sand, the two series that dominate this ridge, drain so fast that the usual Central Florida worry, a soggy base after a summer storm, mostly isn't the issue here. The opposite risk is erosion: loose material on a slope moves downhill under a hard rain instead of sitting still, so the base gets compacted, anchored and, on the steepest lots, terraced rather than laid on a single even grade.</p>"),
        "<!--AUTO:city-services-->",
    ]),
    faqs=[
        faq("Does Clermont have a synthetic-turf rule in its own code?", "Nothing published that we could find. Building Services, at 352-241-7315, is the office with a definitive answer for a specific address; our own coverage of Clermont's own code stops there, unlike the dedicated rules page we keep for the unincorporated county."),
        faq("Is my Clermont lot in the St. Johns district or the Green Swamp district?", "Most of the city runs on the St. Johns River Water Management District's schedule, per the city's own conservation page. Only a sliver at Clermont's far southwest edge, where Florida DEP's Green Swamp boundary begins, falls inside the Southwest Florida district instead."),
        faq("Does a steep lot cost more to turf than a flat one in Clermont?", "It can, mainly in labor. Terracing or anchoring a downhill edge takes a crew longer than compacting a flat rectangle, but the published per-square-foot range doesn't change by ZIP code; a slope shows up as more hours, not a different price list."),
        faq("Will fast-draining ridge sand let me skip the crushed-rock base?", "No. The state's turf rule still requires a washed, open-graded crushed rock or crushed concrete base regardless of how well the native sand drains; the base is what keeps the surface flat and anchored, not just what moves water."),
        faq("Are Kings Ridge and Legends the same community?", "No, they're separate developments across the street from each other. Kings Ridge is a gated 55-plus community with its own golf courses and clubhouse; Legends is a golf community without the same age restriction."),
    ],
    sources=SRC, city=SLUG, crumbs=[("Service areas", "/areas/")], crumb="Clermont",
    related=[("/areas/lake-county/", "Artificial turf across Lake County"), (LAKE_PERMIT, "Lake County permit rules (unincorporated)"),
             ("/areas/minneola/", "Artificial turf in Minneola"), ("/areas/montverde/", "Artificial turf in Montverde"),
             ("/artificial-turf-cost/", "Full turf cost guide")])

LOCAL = {
    "residential": {
        "title": "Artificial Grass Installation in Clermont, FL – Ridge Lots",
        "meta": "Artificial grass built for Clermont's sloped ridge lots, from Kings Ridge to new construction near Sugarloaf Mountain, priced and permitted as of September 2026.",
        "h1": "Turf built for Clermont's sloped, sandy ridge lots",
        "lede": capsule(f"Installed artificial grass in Clermont runs {price('residential')} per square foot as of September 2026, the same range as the rest of Central Florida. What changes here is the ground: Clermont sits on the Lake Wales Ridge, and a sloped, excessively drained lot changes how the base gets built more than it changes what the job costs."),
        "sections": [
            ("Building a base on a slope instead of a flat lot",
             f"<p>Most of the yards we {svc('residential', 'install artificial grass')} on run flat, or close to it. Clermont is the exception: a rear yard that drops several feet from the patio to the back fence is normal here, not a special case, and the base has to be shaped and compacted with that grade in mind. On a moderate slope, grading the subbase to carry water sideways toward a low corner works; on a steeper lot, we terrace the base into shallow steps or add extra anchoring at the downhill edge so the finished turf doesn't creep under its own weight.</p>"
             + f"<p>The native ground underneath is Candler and Astatula sand, {ext(ASTATULA_OSD[1], 'excessively drained and rapidly permeable to more than seven feet down')}, first described right here in Lake County. That solves the drainage question before it's asked, but it also means loose material on a graded slope can wash before it settles, so compaction happens in passes rather than all at once; {post('artificial-turf-on-a-slope', 'the general technique for building on a grade')} carries over here with the ridge sand as an added variable.</p>"),
            ("Kings Ridge, Legends and the subdivisions that filled Clermont's hills",
             f"<p>A lot in {ext(KINGS_RIDGE[1], 'Kings Ridge')} or {ext(LEGENDS[1], 'Legends')} tends to be smaller and gated, with an ARC packet due before a shovel moves; a lot in {ext(LOST_LAKE[1], 'Lost Lake')} or a newer street toward the hilltops runs wider and newer, sometimes still carrying thin builder sod that never established on the ridge sand. Either way, {a('/laws/hoa-rules/', 'the state statute on HOA restrictions')} only protects turf that a street or a neighbor can't see, so a front lawn in a community with mandatory architectural review still goes through that committee regardless of what the city permit process requires.</p>"
             + f"<p>Clermont's {ext(BUILDING[1], 'Building Services division')} (352-241-7315) confirms whatever the city's own permit process requires for a specific address, and that call is worth making before an ARC packet and a crew's schedule get locked in around each other.</p>"),
            ("Ten feet from Clermont's lakes, and clear of the oaks",
             f"<p>Clermont sits inside the {ext(CHAIN[1], 'Clermont chain of lakes')}, with Minneola, Minnehaha and Louisa forming the core of it, and the state measures any lot backing onto one of them by the same yardstick: turf stops 10 feet short of the water, a distance that only disappears once a hard shoreline barrier, a seawall or bulkhead, is already doing that job. A live oak canopy over an older in-town lot near downtown adds a second boundary: turf stays outside the drip line unless a certified arborist signs off, and on a lot this size that line often runs closer to the house than a homeowner expects.</p>"
             + "<p>Neither rule changes because the lot slopes. A hillside yard backing onto a lake still gets measured from the water's edge up the grade, not along it, so the setback can eat more usable yard on a slope than it would on a flat lot of the same size.</p>"),
        ],
        "scenario": ("Say you have a sloped quarter-acre behind a Kings Ridge villa",
                     f"<p>A typical Kings Ridge lot behind a villa runs about 850 sq ft of usable rear yard once the lanai and a narrow side strip are subtracted, on a grade that drops roughly 18 inches from the patio to the back property line. At {price('residential')} a square foot, the job lands between $6,800 and $15,300 depending on the turf and infill chosen, and the slope itself doesn't move that range; it moves how many hours the base takes. Expect the crew to compact in two passes instead of one and add a row of extra anchoring stakes along the downhill edge, both line items already inside a normal quote rather than an upcharge on top of it.</p>"
                     + "<p>An ARC submittal for a community like this typically wants a product sample, a site plan and a note on drainage before it approves anything, so building that packet while the base work is scheduled keeps the two from stacking delays on each other.</p>"),
        "faqs": [
            faq("Does a sloped Clermont yard need a retaining wall before turf goes in?", "Usually not for a moderate grade; terracing the base or adding anchoring handles most residential slopes. A genuinely steep drop, closer to a hillside than a sloped lawn, is a conversation for a site visit rather than a phone estimate."),
            faq("Will Candler sand let a Clermont yard skip the crushed-rock base?", "No. The state's synthetic turf rule requires a washed, open-graded crushed rock or crushed concrete base regardless of how well the native sand drains underneath it; the base controls the surface shape and anchoring, not just water movement."),
            faq("Do nearby ridge towns share the same sloped-lot approach?", f"Yes. {city('montverde', 'Montverde')} and the hillier stretches of {city('winter-garden', 'Winter Garden')} sit on the same general ridge system, so the terracing and anchoring approach carries over there with only the soil series changing slightly by address."),
        ],
        "sources": SRC,
    },
    "pet": {
        "title": "Pet Turf & Dog Runs in Clermont, FL",
        "meta": "Dog-run turf for Clermont's hillside yards and narrow gated-community lots, built for a triathlon town full of active households, checked September 2026.",
        "h1": "Dog turf for a hill town full of runners and cyclists",
        "lede": capsule(f"Pet turf in Clermont runs {price('pet')} per square foot as of September 2026. A lot of the households we hear from here train for something, running, riding or swimming toward the next event at the National Training Center, and their dogs keep the same pace, which wears a bare, sloped track across a natural lawn faster than a sedentary yard ever would."),
        "sections": [
            ("A dog run on a slope wears differently than a flat one",
             "<p>On a flat lot, a dog wears a path back and forth along a fence line. On a Clermont hillside, that same dog tends to run the fence at an angle, cutting diagonally across the grade, and that diagonal wear is what strips grass and starts erosion on a natural lawn faster than straight-line traffic does. Turf solves the wear question outright, but the base underneath still needs the same grading and compaction a sloped residential lawn gets, just sized to a smaller footprint.</p>"
             + f"<p>Zeolite or an antimicrobial coated sand handles the odor side the way it would anywhere else in Central Florida; the ridge's fast-draining sand doesn't change that infill choice, only how quickly a rinse disappears into the ground underneath. {post('how-to-get-dog-urine-smell-out-of-artificial-turf', 'The routine for keeping urine odor out of turf')} still applies whether the base drains slowly or almost instantly.</p>"),
            ("Narrow side yards in Clermont's gated communities",
             f"<p>A dog run in {ext(KINGS_RIDGE[1], 'Kings Ridge')} or a similar gated section usually means a side strip a few feet wide rather than an open backyard, since the lot itself is smaller and the rear often backs a golf fairway. A weed barrier gets skipped under that strip, the way it does under any pet area, because trapped urine at the surface causes more odor than it prevents. An ARC packet for a side-yard dog run tends to move faster when it names the product and shows where the run sits relative to the property line.</p>"
             + f"<p>Further out toward newer construction near {city('minneola', 'Minneola')} or the ridge's outer streets, lots run wider and a dog run can sit further from a fence line altogether, which changes the shape of the job more than the infill.</p>"),
            ("Keeping a dog run outside the 10-foot lake buffer",
             f"<p>A number of Clermont lots back onto the {ext(CHAIN[1], 'chain of lakes')} or a canal feeding it, and a dog run built right up to the water's edge runs into the same 10-foot setback a plain residential lawn does, seawall exception included. Placing the run a bit further up the yard, rather than fighting that setback, is usually the simpler fix, and it keeps a dog that likes to explore the bank away from water access at the same time.</p>"
             + "<p>Drip lines matter here too: a mature oak shading a dog run is worth keeping outside its canopy edge unless an arborist has signed off, since excavation for the run's base is exactly the kind of digging that can damage surface roots.</p>"),
        ],
        "scenario": ("Say you have a 250 sq ft dog run along a sloped side yard",
                     f"<p>A 250 sq ft strip running the length of a side fence on a graded Clermont lot, at {price('pet')} a square foot, lands between $2,500 and $4,500 depending on the infill. Add zeolite for odor control and the number sits toward the upper half of that range rather than outside it. On a graded strip like this, the base gets a touch more depth on the downhill end so the finished surface reads level even though the ground underneath isn't.</p>"
                     + "<p>A flush-out zone near the gate, where a dog tends to relieve itself first on the way out, is worth planning into the layout before the base goes in rather than adding after the fact; it's a placement decision, not an extra cost.</p>"),
        "faqs": [
            faq("Does Clermont's hilly terrain change what infill works best for dogs?", "Not directly. Zeolite and antimicrobial coated sand work the same way on a slope as on a flat lot; what changes is how the base is graded underneath the run, not the infill choice on top of it."),
            faq("Can a dog run sit right up to a Clermont lake or canal?", "Only where a hard shoreline barrier is already standing in for that buffer. Without a seawall or bulkhead in place, the state's 10-foot rule reaches a pet area the same way it reaches the rest of the lawn."),
            faq("Do dog runs in Montverde face the same ridge conditions?", f"Largely, yes. {city('montverde', 'Montverde')} sits on the same general ridge and shares the fast-draining sand, so the odor-focused infill choice matters more there than any drainage concern too."),
        ],
        "sources": SRC,
    },
    "putting": {
        "title": "Backyard Putting Greens in Clermont, FL",
        "meta": "Contoured putting greens for a golf-community town, from Kings Ridge and Legends to hillside lots, with the Central Florida market range checked September 2026.",
        "h1": "Putting greens for a town built around two golf communities",
        "lede": capsule(f"Backyard putting greens in Clermont run {price('putting')} per square foot as of September 2026. Between Kings Ridge and Legends Golf & Country Club sitting across the street from each other, a lot of Clermont homeowners already play regularly, which makes a contoured green a natural extension of a game they're already in rather than a new hobby."),
        "sections": [
            ("Contouring a green on a lot that already slopes",
             "<p>Everywhere else we work, contouring a putting surface means building undulation into an otherwise flat base on purpose. In Clermont, the lot itself often supplies part of that contour before the design even starts, which can work in a green's favor or against it depending on which direction the grade runs. A green laid across the slope, rather than straight down it, usually plays truer and drains more predictably than one that fights the existing grade.</p>"
             + "<p>The fringe and cup placement still follow the same build regardless of the starting grade: a firm, level pad under each cup, and fringe turf transitioning cleanly to whatever surrounds it, whether that's a natural lawn or a bed.</p>"),
            ("A green for a golf-community backyard versus a hilltop lot",
             f"<p>In {ext(KINGS_RIDGE[1], 'Kings Ridge')} or {ext(LEGENDS[1], 'Legends')}, a small green tends to fit into an already-landscaped rear yard behind a lanai, sized to match a footprint that's been fixed since the home was built. Further up toward the ridge's newer streets, a hilltop lot can carry a larger green with more break built in, since the yard itself hasn't been shaped around existing hardscape the way an older gated-community lot has.</p>"
             + f"<p>Either way, an ARC submittal in a community with design review wants the same basics: dimensions, a sample of the turf, and where the green sits relative to the lot line, the same packet {a('/laws/hoa-rules/', 'the state HOA statute')} assumes exists before covering what an association can and can't restrict.</p>"),
            ("What the ridge's sand means for a green's subbase",
             f"<p>{ext(CANDLER_OSD[1], 'Candler sand')}, common across the ridge, drains so fast on its own that the usual concern with a putting green base elsewhere, water sitting under the surface and softening the roll, mostly doesn't apply here. The base still needs the same washed, open-graded crushed rock the state's rule requires, compacted firm enough that a rolled putt doesn't develop a soft spot near the cup after a season of play.</p>"
             + f"<p>What the sand does add is the same erosion consideration as a residential lawn: a green built into a slope needs its edges anchored well enough that heavy rain doesn't undercut the fringe at the low end over time. {post('backyard-putting-green-cost-florida', 'What a Florida putting green costs')} breaks the price range down further by feature.</p>"),
        ],
        "scenario": ("Say you have a 400 sq ft green built into a gentle backyard slope",
                     f"<p>A 400 sq ft green with a two-cup layout, built into a lot that falls about a foot across its width, runs {price('putting')} a square foot, or $5,600 to $12,000 depending on how much contouring and fringe the design carries. Using the existing grade for part of the break, rather than flattening it first, typically keeps the shaping cost from climbing toward the top of that range the way building break from scratch on a flat lot can.</p>"
                     + "<p>Fringe turf usually adds a modest amount beyond the green's own square footage once it wraps the perimeter, which is worth accounting for when comparing a quote against the raw putting-surface number alone.</p>"),
        "faqs": [
            faq("Can a Clermont lot's natural slope replace built-in contouring?", "Partly. A gentle existing grade can supply some of a green's break, which can lower the shaping cost, but cup placement and a level pad under each cup still need to be built regardless of the starting slope."),
            faq("Do Kings Ridge or Legends require a specific putting-green design?", "Neither has a published design document we could find naming synthetic greens specifically. An ARC submittal with dimensions, a product sample and a site plan is the standard packet either community's review committee is likely to expect."),
            faq("Is Clermont the only nearby town with golf-community putting greens?", f"No. {city('four-corners', 'Four Corners')} and the resort corridor toward {city('minneola', 'Minneola')} both carry golf-adjacent subdivisions where a home green is a common request, though Clermont's Kings Ridge and Legends pairing is the densest concentration in our south Lake County coverage."),
        ],
        "sources": SRC,
    },
    "playground": {
        "title": "Playground Turf Installation in Clermont, FL",
        "meta": "Cushioned playground turf for Clermont's family subdivisions and sloped backyards, sized to fall height, with the market range checked September 2026.",
        "h1": "Play surfaces built for Clermont's graded family lots",
        "lede": capsule(f"Playground turf in Clermont runs {price('playground')} per square foot as of September 2026. Between the play area at {ext(SPLASH[1], 'Champions Splash Park')} on Lake Minneola and the backyard swing sets going up in newer subdivisions climbing the ridge, a shock pad sized to the equipment's fall height matters here on a graded lot more than it would on a flat one."),
        "sections": [
            ("Leveling a play area before the shock pad goes down",
             "<p>A swing set or a climbing structure needs a level landing zone regardless of what the rest of the yard does, and on a sloped Clermont lot that means building a level pad into a grade rather than laying turf straight across it. The shock pad's thickness gets sized to the tallest piece of equipment's fall height either way, but on a slope the excavation has to cut deeper on the uphill side to reach that same level plane.</p>"
             + "<p>Once that pad is level and compacted, the turf and infill layer on top work the same as they would on flat ground, which is the point of building it that way in the first place.</p>"),
            ("What families moving into Clermont's newer streets ask for",
             f"<p>{ext(CENSUS[1], 'Census figures for Clermont')} show the population more than quadrupled between 2000 and 2020, and a lot of that growth is young families in new construction climbing the ridge's outer streets, the same builder-sod lots covered on our {svc('residential', 'residential turf page')}. A play area is often one of the first additions after move-in, since builder sod rarely survives the traffic a swing set brings before it's had a season to establish.</p>"
             + f"<p>{ext(PARKS[1], 'The city park system')} runs more than twenty parks citywide, which sets a visible bar for a backyard play area, though nothing about the city's public playgrounds dictates what a private yard has to look like.</p>"),
            ("Shade, heat and a west-facing slope",
             f"<p>A play area on the western side of a hillside lot catches more direct afternoon sun than one tucked against an east-facing slope, and turf surface temperature climbs the same way here as it would on a flat lot in full sun, commonly well past 120°F in summer. A hose rinse before a hot-afternoon play session drops that fast, and a cooling infill helps more on an exposed western slope than it does in a shaded yard; {post('coolest-artificial-grass-and-infill-for-florida', 'the cooling products worth comparing')} go into more depth on that trade-off.</p>"
             + f"<p>Low-E glass from a newer home's windows is worth checking on these lots too, since a hillside build often faces a different direction than its neighbors and a reflection that never reached a flat-lot play area might reach one shaped by the grade.</p>"),
        ],
        "scenario": ("Say you have a 300 sq ft play area cut into a sloped backyard",
                     f"<p>A 300 sq ft play area for a swing set and a small climbing structure, cut level into a lot that drops about a foot across that footprint, runs {price('playground')} a square foot, landing between $3,000 and $7,500 depending on shock-pad thickness. The extra excavation on the uphill side to reach a level plane adds labor rather than material, so it shows up as more time on site rather than a separate line on the invoice.</p>"
                     + "<p>Fall height for the tallest piece of equipment sets the pad thickness the same way it would on a flat lot; a taller climbing structure simply means a deeper cut into the slope to make room for it.</p>"),
        "faqs": [
            faq("Does a sloped Clermont lot need a deeper shock pad than a flat one?", "The pad thickness itself is set by the equipment's fall height, not the slope. What the slope adds is deeper excavation on the uphill side to reach a level plane before that pad goes in."),
            faq("Is there a public playground in Clermont worth looking at for design ideas?", "The play area at Champions Splash Park on Lake Minneola is a common reference point locally, though a backyard design isn't held to any public-park standard."),
            faq("Do families in nearby Groveland or Four Corners ask for the same shock-pad build?", f"Yes. {city('groveland', 'Groveland')} and {city('four-corners', 'Four Corners')} both send us similar requests, and the fall-height-driven pad thickness works the same way regardless of which of the three towns the yard sits in."),
        ],
        "sources": SRC,
    },
    "pool": {
        "title": "Pool & Lanai Turf in Clermont, FL",
        "meta": "Turf around Clermont's screened pool cages and lanais on sloped lots, where deck drainage matters more than it does on a flat subdivision, checked September 2026.",
        "h1": "Pool-deck turf for Clermont's screened, sloped lanais",
        "lede": capsule(f"Turf around a Clermont pool cage or lanai prices in the same {price('residential')} per square foot range as a residential lawn, since it uses the same materials in a smaller footprint. A screen enclosure built on a graded lot needs its deck drainage checked before turf goes in, since a lanai on a slope doesn't shed water the same way one on a flat pad does."),
        "sections": [
            ("A screened lanai on a grade needs its own drainage check",
             "<p>A pool cage built during Clermont's subdivision boom sits on a concrete deck poured to whatever grade the lot had at the time, and that deck doesn't always slope evenly away from the house the way a textbook lanai would. Turf laid over that deck needs a drainage underlay regardless, but on a hillside lot it's worth confirming which direction the existing deck actually sheds water before assuming the underlay alone will handle a heavy summer storm.</p>"
             + "<p>Glue-down edges around the cage's perimeter secure the turf against the deck itself rather than relying on stakes, since a concrete pad doesn't accept a nailed edge the way open ground does.</p>"),
            ("Narrow strips inside a gated-community screen enclosure",
             f"<p>A pool cage in {ext(KINGS_RIDGE[1], 'Kings Ridge')} or a similarly built-out community usually leaves a strip only a few feet wide between the pool deck and the screen wall, too narrow and too shaded for grass to hold up, which is exactly the kind of space turf handles well. That narrow footprint also means less material and less labor than an open backyard lawn, even though the per-square-foot price is the same.</p>"
             + f"<p>An ARC submittal for a pool-area change is a smaller ask than a full yard conversion in most of these communities, since the work stays inside an existing screen enclosure rather than changing what's visible from the street.</p>"),
            ("Heat inside a screened enclosure on a sunny slope",
             "<p>A screen mesh cuts direct sun somewhat but doesn't eliminate the heat a turf surface picks up on a west-facing lanai, and a hillside lot's orientation can put more or less afternoon sun on a pool deck than a flat lot's would, depending which way the grade faces. A hose rinse before an afternoon swim brings the surface down quickly regardless, and a lighter-colored or cooling infill is worth the small add-on for a lanai that gets full sun most of the day.</p>"
             + f"<p>Screen enclosures also concentrate whatever heat the deck itself holds, since airflow is more limited than in an open yard, which is one more reason a rinse habit matters more inside a cage than outside one. A reflected low-E window is a separate, rarer risk worth ruling out too; {post('can-artificial-turf-melt', 'what actually melts turf')} covers both causes side by side.</p>"),
        ],
        "scenario": ("Say you have a 200 sq ft strip inside a Clermont pool cage",
                     f"<p>A 200 sq ft strip between the pool deck and the screen wall, glued down over a drainage underlay, runs toward the upper half of the {price('residential')} range given the small footprint and tight access through a screen door, landing between $3,200 and $3,600. Access is the main cost driver here: a crew working through a standard screen door frame carries material in by hand rather than wheeling it in, which adds labor time a wide-open backyard wouldn't.</p>"
                     + "<p>Confirming which way the existing pool deck sheds water, before the underlay goes down, is a five-minute check that avoids redoing the strip later if water turns out to pool at one end of the enclosure.</p>"),
        "faqs": [
            faq("Does a sloped Clermont lot change how pool-deck turf drains?", "It can. The deck's own slope, poured when the pool cage was built, doesn't always match the rest of the yard's grade, so checking which way it currently sheds water before installing the drainage underlay is worth doing on a hillside lot."),
            faq("Is pool-area turf cheaper than a full yard conversion in Clermont?", "The total cost is lower simply because the footprint is smaller, though the per-square-foot price sits at the upper half of the residential range given tight access through a screen enclosure."),
            faq("Do pool cages toward Montverde have the same drainage question?", f"Yes, wherever a lanai sits on graded ground rather than a flat pad, which covers a fair share of {city('montverde', 'Montverde')} too. Checking the deck's actual slope before adding a turf underlay matters on any hillside pool enclosure in south Lake County."),
        ],
        "sources": SRC,
    },
    "repair": {
        "title": "Turf Repair in Clermont, FL",
        "meta": "Turf repair for Clermont's sloped lots, where a lifted downhill edge or a washed-out seam shows up faster than on a flat Central Florida yard.",
        "h1": "Fixing turf that a Clermont slope has worked loose",
        "lede": capsule("Turf repair in Clermont is quoted after we see photos or visit the site, since a lifted seam, a settled low spot or a washed edge each need a different fix. A hillside lot shows this kind of damage in a specific place almost every time: the downhill edge, where water and gravity both push the same direction."),
        "sections": [
            ("Why the downhill edge fails first on a sloped lot",
             "<p>An edge that was stapled instead of properly bonded, or a seam that wasn't tucked tight before compaction, tends to hold up for a while on a flat lot and fail fast on a graded one, because gravity is doing extra work on top of ordinary wind and foot traffic. Water running downhill during a summer storm finds that weak point and works it wider each time it rains, which is why a repair call in Clermont skews toward the low side of a sloped yard more often than the high side.</p>"
             + "<p>A proper fix re-anchors that edge into ground that's been checked for compaction underneath, not just restapled at the surface, since restapling a spot that's already settling just buys a few more months before the same repair call comes back.</p>"),
            ("What a rushed base on the ridge looks like a year later",
             f"<p>Candler and Astatula sand drains fast enough that a poorly compacted base here doesn't show up as standing water the way it might on flatwoods soil closer to Kissimmee; instead it shows up as a soft, settling low spot where loose material has shifted under the turf over a season of rain and foot traffic. That kind of settling is harder to spot on a walkthrough than a puddle is, which is part of why {ext(ASTATULA_OSD[1], 'this ridge sand')} can hide a build problem longer before it becomes obvious.</p>"
             + f"<p>{svc('repair', 'A repair visit')} usually starts by pulling back the turf at the affected spot to see what the base actually looks like underneath, rather than guessing from the surface symptom alone.</p>"),
            ("Low-E glass and storm anchoring on a hillside build",
             f"<p>Newer construction climbing Clermont's ridge often faces a different direction than the older, flatter subdivisions closer to downtown, which means a west- or south-facing window that reflects concentrated sun onto turf can show up somewhere a homeowner wouldn't expect on a flat-lot layout. A scorched patch that doesn't trace back to any obvious cause is worth checking against a nearby low-E window before assuming it's a material defect.</p>"
             + f"<p>After a tropical storm, walking the full perimeter of a sloped lawn is worth the extra few minutes it takes compared to a flat one, since a downhill edge that's started to lift is easier to re-anchor early than after another storm works the gap wider. {post('artificial-turf-hurricane-flooding', 'What a hurricane or heavy flooding can do to turf')} covers the storm side of this in more detail.</p>"),
        ],
        "scenario": ("Say you have a 12-ft washed-out edge at the bottom of a sloped lawn",
                     "<p>A section of edge that's lifted along the lowest run of a sloped backyard, roughly 12 running feet, usually means the anchoring underneath has washed loose rather than the turf itself failing. A repair visit checks the base at that spot, re-anchors the edge into compacted ground, and reseams any turf that pulled away from the join. Because pricing depends on what the crew finds underneath once the edge is pulled back, we quote this kind of fix after photos or a site visit rather than over the phone.</p>"
                     + f"<p>Catching a lifted edge early, before a second storm works the gap wider, is usually the difference between a small repair and a section that needs {svc('replacement', 'a larger tear-out and rebuild')}.</p>"),
        "faqs": [
            faq("Why do repairs in Clermont happen more at the bottom of a sloped yard?", "Water and gravity both push toward the downhill edge during a storm, so a weak seam or a loosely anchored edge tends to fail there first. The same defect on a flat lot might take longer to show up."),
            faq("Can a settling low spot on ridge sand be fixed without pulling up the whole lawn?", "Usually yes. Pulling back the turf at just the affected spot lets a crew check and recompact the base underneath, then reseam and infill that section without redoing the entire yard."),
            faq("Do you handle repair calls out toward Groveland and Four Corners too?", f"Yes, {city('groveland', 'Groveland')} and {city('four-corners', 'Four Corners')} both fall inside the radius we cover, and the same downhill-edge and settling checks apply on the ridge terrain either town shares with Clermont."),
        ],
        "sources": SRC,
    },
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
