# -*- coding: utf-8 -*-
"""Tier 2 city module: Pine Hills, FL. Unincorporated census-designated place in west Orange County;
Orange County's own Division of Building Safety reviews permits. Facts checked September 2026;
see docs/TIER2-BRIEF.md for the research assignment."""
from _helpers import page, capsule, sec, table, faq, a, svc, city, county, post, src, ext, price, note
from _cityservice import cityservice_pages

SLUG = "pine-hills"

ORANGE_PERMIT = ("Orange County Permitting Services & Building Safety", "https://fasttrack.ocfl.net/OnlineServices/")
ORANGE_CH24 = ("Orange County Code, Chapter 24, Municode Library", "https://library.municode.com/fl/orange_county/codes/code_of_ordinances?nodeId=ORCOCO_CH24LABUOPSP")
ORANGE_PA = ("Orange County Property Appraiser -- parcel search", "https://ocpafl.org/")
OC_UTIL = ("Orange County Utilities -- watering restrictions", "https://www.orangecountyfl.net/watergarbagerecycling/wateringrestrictions.aspx")
SJRWMD_ORANGE = ("St. Johns River Water Management District -- Orange County", "https://www.sjrwmd.com/district-counties/orange-county/")
PH_WIKI = ("Wikipedia -- Pine Hills, Florida", "https://en.wikipedia.org/wiki/Pine_Hills,_Florida")
PH_NID = ("Orange County -- Pine Hills Neighborhood Improvement District", "https://www.orangecountyfl.net/NeighborsHousing/PineHillsNeighborhoodImprovementDistrict.aspx")
PH_SEWER = ("OCFL Newsroom -- Pine Hills Septic 2 Sewer project completion, July 2026", "https://newsroom.ocfl.net/2026/07/mayors-office-district-6-commissioner-orange-county-utilities-commemorate-completion-of-the-pine-hills-septic-2-sewer-project/")
IMMOKALEE_OSD = ("USDA NRCS -- official series description, Immokalee series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/I/IMMOKALEE.html")
POMELLO_OSD = ("USDA NRCS -- official series description, Pomello series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/P/POMELLO.html")

SRC = [ORANGE_PERMIT, ORANGE_CH24, ORANGE_PA, OC_UTIL, SJRWMD_ORANGE, PH_WIKI, PH_NID, PH_SEWER, IMMOKALEE_OSD, POMELLO_OSD,
       "dep-rule", "fs125572", "fs7203045"]

PERMIT_ORANGE = ("/laws/permits/orange-county/", "Orange County permit rules for turf")
HOA_ROUTE = ("/laws/hoa-rules/", "What a Florida HOA can and can't restrict")
HB683_ROUTE = ("/laws/florida-hb-683/", "HB 683 and DEP Rule 62-308.100")


# ============================================================== hub
HUB = page(
    "/areas/pine-hills/", "city",
    "Artificial Turf in Pine Hills, FL (Orange County)",
    "Synthetic grass installation in unincorporated Pine Hills, Orange County: permits, water rules, older ranch lots and mature oaks, checked September 2026.",
    "Synthetic grass for Pine Hills lots, from ranch homes to Barnett Park",
    capsule(f"We install and repair artificial grass across unincorporated Pine Hills, where a residential lawn runs {price('residential')} per square foot as of September 2026. Pine Hills has no city hall of its own; Orange County's Division of Building Safety reviews the permit and Orange County Utilities delivers the water. About 19 miles from downtown Kissimmee, it's one of the closer stops on our northwest Orange County list."),
    "".join([
        sec("Pine Hills is unincorporated, and that changes who answers the phone",
            f"<p>Pine Hills has never incorporated as its own city, so there's no Pine Hills building department, mayor's office or municipal code to check. Every permit question runs through Orange County's Permitting Services and Division of Building Safety instead, reached at 407-836-5550 with applications filed through the county's {ext(ORANGE_PERMIT[1], 'Fast Track Online Services')} portal. Orange County Code Chapter 24 defines &quot;turf, turf grass or sod&quot; as a natural grass species such as Bahia, Bermuda or St. Augustine, and as of September 2026 we found no section anywhere in the county code that addresses a synthetic product by name ({ext(ORANGE_CH24[1], 'Orange County Code, Chapter 24')}).</p>"
            + f"<p>That gap is a finding, not a green light: {a(PERMIT_ORANGE[0], 'our Orange County permit page')} covers what the silence does and doesn't mean, and the {ext(ORANGE_PA[1], ORANGE_PA[0])} confirms a specific Pine Hills parcel sits where county code, rather than a neighboring city's code, actually applies.</p>"),
        sec("A neighborhood built in three waves: 1953, the 1960s and a decade of ranch homes",
            f"<p>Pine Hills traces back to 1953, when the Robinswood and Pine Ridge Estates subdivisions went in along the newly finished Pine Hills Road, and it filled in through the 1960s and 1970s as a bedroom community for workers at the Martin Marietta aerospace plant nearby ({ext(PH_WIKI[1], 'Pine Hills history summarized by Wikipedia')}). Census figures put more homes here built in the 1970s than in any other decade, which means a typical lot runs larger than a newer subdivision's and often carries oak trees planted when the block was new, now fifty or more years into their canopy.</p>"
            + f"<p>That combination, an older lot with mature shade trees, shows up across the six service pages linked from here: it's what pushes {svc('residential', 'a lawn conversion')}'s drip-line planning and a dog run's layout in different directions than a newer, treeless subdivision would.</p>"),
        sec("Pine Hills lot types and how a turf job differs",
            "<p>The table below is the short version; each city-times-service page linked from here goes further on a single service.</p>"
            + table("Pine Hills lot types and how a turf job differs",
                    ["Common lot", "What's usually on it", "The turf angle"],
                    [["1950s-70s ranch home", "A larger lot than a newer subdivision, often with a mature oak", "Drip-line rule limits how close turf and base excavation can get to the trunk"],
                     ["Pine Hills Road corridor (Alhambra Drive to Golf Club Parkway)", "Recently converted from septic to county sewer as of June 2026", "No pump-out lid to route around on a converted parcel; still required nearby"],
                     ["Lot near Lawne Lake or Barnett Park", "Backs onto or sits close to public water", "The state's 10-foot waterbody setback applies unless a seawall separates yard and water"],
                     ["Rental or investor-owned lot", "Older irrigation heads and sod original to the property", "Heads get capped under the new turf regardless of who owns the lot"],
                     ["Newer infill construction", "Built on a subdivided piece of an older, larger parcel", "Smaller footprint, but the same washed-rock base as its older neighbors"]],
                    "Checked against Orange County's published record and the sources listed below, September 2026.")),
        sec("Water and irrigation: Orange County Utilities, not a city system",
            f"<p>Orange County Utilities delivers the water here, not a city system, something the county's own project along Pine Hills Road confirms directly: crews spent from 2024 to June 2026 swapping septic tanks for sewer lines between Alhambra Drive and Golf Club Parkway, converting 30 of 95 total parcels before the county marked the corridor finished ({ext(PH_SEWER[1], 'the county’s Pine Hills sewer-conversion announcement')}). Watering under that utility follows a calendar that shifts with the calendar itself: address parity decides the day, the count doubles from one morning a week to two once daylight saving time begins, and neither window opens at midday ({ext(OC_UTIL[1], "Orange County's current watering restrictions")}).</p>"
            + f"<p>The water management district drawing the boundary here is St. Johns River, covering most of Orange County apart from a southeastern sliver near the Osceola line ({ext(SJRWMD_ORANGE[1], 'SJRWMD’s coverage of Orange County')}). A capped synthetic lawn steps outside that calendar entirely once its irrigation heads are disconnected, a requirement {src('dep-rule', "the state's turf standard")} sets no matter which utility or district applies.</p>"),
        sec("No single HOA here, but a public district with its own mission",
            f"<p>Pine Hills isn't one master-planned community with a single association, so there's no countywide ARC process the way a place like Celebration has. Individual subdivisions inside Pine Hills can carry their own deed restrictions, and where one exists, it answers to the same statute every Florida HOA does: {a(HOA_ROUTE[0], "an association can't ban turf that isn't visible from the street or an adjacent lot")}, full stop.</p>"
            + f"<p>What Pine Hills does have is a public body called the Neighborhood Improvement District, created in 2011 to strengthen local business and reinvest in infrastructure across the community, run by the county rather than by residents' dues ({ext(PH_NID[1], 'the Pine Hills Neighborhood Improvement District')}). It doesn't review individual homeowners' yards, so it has no bearing on a specific turf project, but it's worth knowing the difference between that district and an actual HOA before assuming either one applies. {a(HB683_ROUTE[0], "Florida's May 2026 turf standard")} is the one rule that reaches every Pine Hills yard regardless of which of these bodies, if any, also has a say.</p>"),
        "<!--AUTO:city-services-->",
    ]),
    faqs=[
        faq("What's the best way to compare artificial turf installers serving Pine Hills?",
            "Ask for base depth and material in writing, whether the crew has priced a job on Pine Hills' older, larger ranch lots before, and how they'd handle a mature oak's drip line if one sits near the planned area. A quote that answers all three without prompting says more than one that just lists a price per square foot."),
        faq("Does Orange County Utilities really serve Pine Hills, or is it a city system?",
            "Orange County Utilities. The county's own 2024-2026 project converting septic tanks to sewer along Pine Hills Road, completed in June 2026, confirms the county utility as the service provider here, not a separate municipal system, since Pine Hills has never incorporated its own city government."),
        faq("Is the Pine Hills Neighborhood Improvement District the same as an HOA?",
            "No. It's a public special district created by the county in 2011 to invest in local business and infrastructure, not a homeowners association, and it doesn't review or approve what an individual resident puts in a backyard. A subdivision-level deed restriction, where one exists, is the closer equivalent to an HOA."),
        faq("Do Pine Hills' older oak trees complicate a turf installation?",
            "Sometimes. A tree planted when a 1960s or 1970s subdivision was built has had five decades to extend its root system well past the edge of its canopy, and the state's drip-line rule follows the roots, not just the branches, unless a certified arborist certifies the work won't cause harm."),
        faq("Does a lot near Lawne Lake get a different setback than one away from the water?",
            "No. The state's 10-foot setback from a natural or man-made waterbody's ordinary or mean high water line applies to a Lawne Lake-adjacent lot the same way it would anywhere else in Pine Hills, unless a seawall or bulkhead already separates the yard from the water."),
    ],
    sources=SRC, city=SLUG, crumbs=[("Service areas", "/areas/")], crumb="Pine Hills",
    related=[("/areas/orange-county/", "Artificial turf in Orange County"), PERMIT_ORANGE, ("/areas/orlando/", "Turf in Orlando"), ("/areas/ocoee/", "Turf in Ocoee"), ("/artificial-turf-cost/", "Full turf cost guide")],
)


# ============================================================== local service content
LOCAL = {
    "residential": {
        "title": "Artificial Grass Installation for Pine Hills Ranch Homes",
        "meta": "Synthetic lawn installation for Pine Hills, Florida's 1950s-70s ranch-home lots, from " + price("residential") + " per sq ft, September 2026.",
        "h1": "Turf for Pine Hills' original ranch-home lots",
        "lede": capsule(f"A residential lawn conversion in Pine Hills runs {price('residential')} per square foot as of September 2026. Most homes here were built in the 1970s on lots wider than a newer subdivision carries, which usually means more square footage to plan a base for and, on many blocks, a mature oak to work around."),
        "sections": [
            ("What a decade of ranch-home construction left behind",
             f"<p>Pine Hills filled in fastest during the 1970s, and census figures show more homes from that single decade than any other in the community ({ext(PH_WIKI[1], 'Pine Hills housing history')}). A lot from that era tends to run wider and deeper than a lot in a subdivision built in the last fifteen years, which means more open square footage for a full lawn conversion, but also original grading that's had fifty years of settling, additions and driveway work to shift it away from whatever slope the builder first cut.</p>"
             + "<p>Checking the current grade before ordering material matters more on a lot this age than on new construction, since assumptions about where water used to run no longer hold after decades of small changes.</p>"),
            ("Excavating near roots that have had fifty years to spread",
             f"<p>A live oak or laurel oak planted when a Pine Hills block was new has had five decades to send roots well past its canopy's edge, further than a newer tree in a fifteen-year-old subdivision ever could. The state's drip-line rule follows those roots rather than just the visible branches, so a lawn conversion plan on an older Pine Hills lot starts by walking the actual canopy's reach, not by measuring from the trunk outward on a tape.</p>"
             + f"<p>{post('artificial-turf-near-live-oaks-and-palms', 'This article')} covers what base excavation actually does to a root system nearby, and why a certified arborist's letter is the only way around the setback rather than a shortcut past it.</p>"),
            ("Where Orange County's Division of Building Safety fits in",
             f"<p>Pine Hills answers to Orange County's own permitting office rather than a city hall, and the county's landscape code defines turf only in terms of living grass species, with nothing written for a synthetic product either way. A straightforward residential conversion here isn't running into a named turf rule, but general permitting for exterior alteration and drainage still applies; {a('/laws/permits/orange-county/', "our Orange County permit page")} walks through what that means in practice for a specific address.</p>"),
        ],
        "scenario": ("Say you have a 950 sq ft backyard behind a 1968 ranch home",
                     f"<p>Say you have a 950 sq ft backyard behind a 1968 ranch home a few blocks from Lawne Lake, wider than a newer subdivision lot but with a laurel oak anchoring one corner. At the published {price('residential')} range, that lawn prices between $7,600 and $17,100, with most conversions like it landing in the {price('residential', True)} typical band, or $9,500 to $15,200. The oak's canopy reaches roughly a third of the way across the yard, so the crew stakes the drip line first and plans the layout around it rather than measuring the full 950 sq ft as buildable from the start.</p>"
                     + "<p>Because the block still runs on the county's original irrigation zones from decades ago, capping the heads under the new lawn is part of the same visit, not a separate call later."),
        "faqs": [
            faq("Are Pine Hills lots really bigger than a newer Orange County subdivision?",
                "Often, yes. Homes built here during the 1960s and 1970s tend to sit on wider lots than a subdivision platted in the last two decades, since lot-size standards and buyer expectations have both shifted since Pine Hills was built out."),
            faq("Does an older Pine Hills lawn need different base prep than a newer one nearby?",
                "The base recipe is the same, washed crushed rock compacted in two lifts, but an older lot's original grading has usually shifted after decades of small changes, so checking today's actual slope matters more than trusting an assumption about how the lot was originally built."),
        ],
        "sources": SRC,
    },
    "pet": {
        "title": "Pet Turf and Dog Runs in Pine Hills, FL",
        "meta": "Dog-run turf for Pine Hills' older, larger lots, priced " + price("pet") + " per sq ft as of September 2026, with septic and irrigation notes.",
        "h1": "A dog run built for a Pine Hills backyard",
        "lede": capsule(f"A Pine Hills dog run built in pet turf falls inside the published {price('pet')}-a-square-foot span, current as of September 2026, with {price('pet', True)} covering most jobs. The community's older, wider 1960s and 1970s lots give a run more room than a newer subdivision yard typically spares, and a share of those same lots still route around a septic system's access point."),
        "sections": [
            ("Room a newer subdivision lot doesn't have",
             "<p>A dog run competes for space on a small, newer lot in a way it usually doesn't on an older Pine Hills parcel, where a wider side yard or a deeper backyard leaves room for a run alongside a family lawn instead of replacing it. That extra width also means a run can be laid out as a long rectangle along a fence line rather than squeezed into an odd-shaped leftover corner, which is easier to keep dogs contained in and easier to drain evenly.</p>"),
            ("Where a septic tank still sits under the yard",
             f"<p>Most of Pine Hills still runs on individual septic systems outside the stretch of Pine Hills Road between Alhambra Drive and Golf Club Parkway that the county converted to sewer by June 2026 ({ext(PH_SEWER[1], 'the county’s septic-to-sewer project')}). On a lot that hasn't converted, the tank's pump-out lid has to stay reachable once a dog run or any other turf area is finished, which means mapping the system's layout before staking a run's corners, not after the base is already down.</p>"),
            ("Capping a sprinkler zone that's older than the dog",
             "<p>A Pine Hills lot from the 1960s or 1970s often still runs on its original irrigation zones, sometimes patched or partially replaced over the decades but rarely redesigned from scratch. Before a dog run's turf goes in, whatever zone used to water that section gets capped at the valve, the same requirement that applies anywhere in Florida under the state's rule, and it's a good moment to check whether nearby zones still work at all before the rest of the yard gets attention later.</p>"),
        ],
        "scenario": ("Say you have a 260 sq ft run behind a 1962 ranch home",
                     f"<p>Say you have a 260 sq ft dog run planned for the back fence line of a 1962 ranch home on a lot that hasn't yet converted from septic to county sewer. At {price('pet')} per square foot, that run prices between $2,600 and $4,680, with most jobs like it landing in the {price('pet', True)} typical band, or $3,120 to $4,160, once zeolite infill is added for odor control.</p>"
                     + "<p>Because the property is still on septic, the crew locates the tank and drain field before finalizing the run's footprint, keeping the pump-out lid clear and shifting the layout a few feet if the original plan would have covered it."),
        "faqs": [
            faq("Does a Pine Hills lot that already converted to sewer still need pump-out access planned?",
                "No, not for that specific system. Once a parcel has switched from septic to county sewer, there's no tank left to keep reachable, though a neighboring lot that hasn't converted still needs that access point mapped before any turf goes in."),
            faq("Is a weed barrier a good idea under a Pine Hills dog run?",
                "Skip it specifically under the run. A layer of fabric between the base and the turf backing holds waste right at the surface rather than letting it pass down into the rock, fighting the fast drainage a dog run needs most. Elsewhere on the same lawn, the same fabric is fine, and optional."),
        ],
        "sources": SRC,
    },
    "putting": {
        "title": "Backyard Putting Greens in Pine Hills, FL",
        "meta": "Backyard putting greens sized for Pine Hills' older, wider lots in Orange County, priced " + price("putting") + " per sq ft as of September 2026.",
        "h1": "A stand-alone green for a Pine Hills yard",
        "lede": capsule(f"Most backyard greens built in Pine Hills land in the {price('putting', True)} typical band, part of a wider {price('putting')}-a-square-foot span published as of September 2026. There's no golf-course subdivision behind any of them here, so a green gets built purely for the game itself, usually on a lot wider than a newer Orange County community offers."),
        "sections": [
            ("A green built for the game, not a fairway view",
             "<p>Some Orange County suburbs grew up around a golf course, where a backyard green is almost an extension of the community's own layout. Pine Hills didn't develop that way, so a homeowner here who wants a private green is building it purely to practice, with no shared course setting the tone. That actually simplifies the ARC question in most cases, since there's no golf-community design committee weighing in on top of whatever a specific subdivision's own deed restrictions say.</p>"),
            ("Using an original 1970s lot's extra width",
             "<p>A putting green with an attached chipping area needs more square footage than most people expect once fringe and approach cuts are factored in, and that's easier to fit on an older Pine Hills lot than on a compact newer parcel. A wider side yard or a deeper backyard here can host a modest green and a small chipping pad without crowding out the rest of the lawn the way it would on a tighter, newer subdivision lot.</p>"),
            ("Building a green above a seasonal high water table",
             f"<p>Pine Hills sits in the same Central Florida flatwoods soil family as much of the rest of the county, Immokalee and related series that hold water within a few feet of the surface for weeks after a heavy rainy season ({ext(IMMOKALEE_OSD[1], 'the Immokalee series description')}). A putting green's contoured subgrade has less room for error than a flat lawn's, so on this kind of ground the base gets built toward the fuller end of the state's two-to-four-inch range rather than the minimum, keeping the green's surface further above whatever water the soil is holding onto below it.</p>"),
        ],
        "scenario": ("Say you have a 400 sq ft green on a wide 1970s lot",
                     f"<p>Say you have a 400 sq ft putting green with a small attached chipping area planned for the side yard of a 1970s Pine Hills ranch home, wide enough to keep the green well clear of the property line. At the published {price('putting')} range, that project prices between $5,600 and $12,000, with most jobs like it landing in the {price('putting', True)} typical band, or $7,200 to $10,000, depending on how much contouring and how many cups the design calls for.</p>"
                     + "<p>Because the lot sits on flatwoods soil that holds water close to the surface after a wet summer, the crew builds the compacted base at the deeper end of the state's range before shaping any contours into it."),
        "faqs": [
            faq("Does a Pine Hills subdivision's deed restriction review a putting green differently than a lawn?",
                "Not usually as its own category. Where a deed restriction exists, it applies the visibility standard Florida law sets for any synthetic turf feature, a green included, rather than singling out putting greens for separate treatment."),
            faq("Why would a Pine Hills green need a deeper base than one on drier ground?",
                "Flatwoods soil here holds a seasonal high water table closer to the surface than a well-drained ridge lot would, and a green's shaped subgrade has less tolerance for settling than a flat lawn does, so building toward the deeper end of the state's base-depth range keeps more separation between the surface and that water."),
        ],
        "sources": SRC,
    },
    "playground": {
        "title": "Playground Turf for Pine Hills Families",
        "meta": "Cushioned play-area turf for Pine Hills backyards, priced " + price("playground") + " per sq ft as of September 2026, near Barnett Park.",
        "h1": "A play surface for a Pine Hills backyard",
        "lede": capsule(f"Priced inside the {price('playground')} range published for September 2026, backyard play turf in Pine Hills still needs a shock pad matched to whatever equipment sits on top of it. Roughly a quarter of the community's residents are under 18, and Barnett Park's own play areas sit right alongside Lawne Lake in the middle of the neighborhood."),
        "sections": [
            ("A community with children in a large share of its households",
             f"<p>Roughly 26 percent of Pine Hills residents are under 18, a larger share of children than many neighboring Orange County communities carry ({ext(PH_WIKI[1], 'Pine Hills demographics')}). That shows up in demand for a backyard play area that doesn't need mowing or reseeding after a season of swing-set traffic wearing a bare patch into whatever grass used to be there.</p>"),
            ("Building near canopy that predates most of the swing sets going in today",
             "<p>A Pine Hills lot from the 1960s or 1970s often carries an oak planted when the block was new, now with a canopy and root system that reach well past where a homeowner might assume the drip line sits. Siting a play structure on one of these lots means walking the actual canopy first, since the state's rule bars excavating for turf inside that boundary on either the property itself or an adjacent one, unless a certified arborist signs off.</p>"),
            ("Two infill specs on one Pine Hills lawn",
             "<p>A single Pine Hills backyard project can end up running two different infill specs at once: rubber or another synthetic material directly under a swing set or climbing structure, and silica sand, rock, shell or a coated sand across every other section of turf the yard includes. The dividing line follows the equipment's own footprint rather than a rule-of-thumb distance, so a taller structure with a wider fall zone pushes that rubber boundary out further than a low platform toy would.</p>"),
        ],
        "scenario": ("Say you have a 240 sq ft play area near an established oak",
                     f"<p>Say you have a 240 sq ft play area planned for a swing set on a Pine Hills lot where an established oak's canopy reaches close to the intended footprint. At the published {price('playground')} range, that job prices between $2,400 and $6,000, with most projects like it landing in the {price('playground', True)} typical band, or $2,880 to $4,560, depending on the shock pad thickness the equipment's fall height calls for.</p>"
                     + "<p>Once the crew stakes the oak's actual drip line rather than guessing from the trunk, the buildable area sometimes shrinks by 30 to 50 sq ft from the original sketch, which changes the layout more than it changes the total price."),
        "faqs": [
            faq("Does Barnett Park's proximity change what a home playground can include?",
                "No. The park's own equipment and grounds are public property with their own maintenance, unrelated to a private backyard nearby. A home play area follows the state's May 2026 turf standard and Orange County's ordinary permitting regardless of how close it sits to the park."),
            faq("Can the same backyard use rubber infill under the swing set and silica everywhere else?",
                "Yes, and that's actually what the state's rule requires rather than just allows. Rubber and other synthetic infill are limited to the equipment's own footprint; the rest of the yard's turf has to use silica sand, rock, shell or a coated sand instead."),
        ],
        "sources": SRC,
    },
    "pool": {
        "title": "Turf Around Pools in Pine Hills, FL",
        "meta": "Turf beside older, often unscreened pools in Pine Hills, Florida, priced like a residential lawn at " + price("residential") + " per sq ft, September 2026.",
        "h1": "Turf beside a Pine Hills pool",
        "lede": capsule("A number of Pine Hills' original 1960s and 1970s pools were built with no screen cage at all, which changes how much direct sun the surrounding turf takes on compared with a newer, covered deck. Open or caged, the turf around it still prices at the residential span, " + price("residential") + " a square foot, current as of September 2026."),
        "sections": [
            ("Older pools without the screen cage a newer subdivision assumes",
             "<p>A pool installed in Pine Hills during the 1960s or 1970s often went in without a screen enclosure at all, since cage construction became standard practice on new Central Florida pools later than that. Turf around an open, unscreened pool deck takes full sun rather than the filtered light a cage provides, which means checking for nearby low-emissivity replacement windows matters here, since reflected heat off that kind of glass can soften turf from several feet away.</p>"),
            ("A pool lot backing onto Lawne Lake or a connecting canal",
             "<p>A smaller number of Pine Hills pool homes sit close enough to Lawne Lake or a connecting waterway to bring the state's 10-foot setback into the layout alongside the pool deck itself. That buffer runs from the water's ordinary high-water line, and only a seawall or bulkhead already in place closes the gap it otherwise requires, which on a narrow lot can leave the water-side turf shorter than the deck next to it.</p>"),
            ("What a capped irrigation zone means next to an older pool deck",
             f"<p>Orange County Utilities' seasonal watering schedule, two days a week in daylight saving months and one day the rest of the year, stops applying to a turfed pool-area section once its heads are capped, the same requirement that reaches any synthetic turf under {src('dep-rule', "the state's rule")}. What stays on the county's schedule is whatever natural grass remains around the edges of the pool deck once the turf section is finished.</p>"),
        ],
        "scenario": ("Say you have 380 sq ft of turf around an unscreened pool",
                     f"<p>Say you have 380 sq ft of ground around an older, unscreened Pine Hills pool, split between a strip along one side and a run behind the shallow end, both in full sun most of the day. At the residential range of {price('residential')} per square foot, that job prices between $3,040 and $6,840, with most jobs like it landing in the {price('residential', True)} typical band, or $3,800 to $6,080.</p>"
                     + "<p>Because the deck sits in direct sun without a cage overhead, the crew checks nearby windows for low-emissivity glass before finalizing turf placement, since a reflected hot spot from the wrong angle can do more damage to an open, sun-exposed lawn than to one shaded by a screen enclosure."),
        "faqs": [
            faq("Do most Pine Hills pools have a screen cage?",
                "Not universally. A meaningful share of the community's pools date to the 1960s and 1970s, before cage enclosures became the Central Florida default, so an open, unscreened pool deck is more common here than in a newer subdivision built in the last two decades."),
            faq("Does an unscreened pool change the turf product recommended around it?",
                "Not the product itself, but the sun exposure it takes on. Full, uninterrupted sun pushes surface temperature toward the higher end of what turf reaches in Florida, which is a reason to plan for regular hose rinsing rather than a reason to choose a different turf."),
        ],
        "sources": SRC,
    },
    "repair": {
        "title": "Artificial Turf Repair in Pine Hills, FL",
        "meta": "Seam, edge and base repairs for artificial turf in Pine Hills, Florida, quoted after photos or a site visit, checked September 2026.",
        "h1": "Repairing turf on an older Pine Hills lot",
        "lede": capsule("What actually failed underneath decides the cost of a Pine Hills turf repair, which is why a firm number comes from photos or a site visit rather than a posted flat rate. A lawn on one of the community's original 1960s or 1970s lots usually carries different history working against it than a newer installation would."),
        "sections": [
            ("What five decades of settling does to a lot's grade",
             "<p>A Pine Hills lot from the 1960s or 1970s has usually seen an addition, a repaved driveway, or simple decades of erosion reshape its original grade in small ways nobody tracked at the time. A turf lawn installed without rechecking that current slope can develop a low spot years later that has nothing to do with the installation itself and everything to do with ground that shifted after the base went in.</p>"),
            ("Repairing near a septic system that hasn't converted",
             f"<p>Outside the stretch of Pine Hills Road the county converted to sewer by June 2026, most Pine Hills properties still run on individual septic systems ({ext(PH_SEWER[1], 'the county’s septic-to-sewer project')}). A repair visit on one of these lots is a chance to confirm the tank's pump-out lid is still where records show it and still clear of turf and infill, since older installations sometimes predate the state's access requirement and buried the lid without meaning to.</p>"),
            ("What the Neighborhood Improvement District's work means for a yard repair",
             f"<p>Orange County's Pine Hills Neighborhood Improvement District has spent recent years on public infrastructure and business-district investment, not on individual residential yards ({ext(PH_NID[1], 'the Pine Hills Neighborhood Improvement District')}), so its projects don't change what a specific repair costs or requires. What they do change is the surrounding streetscape a repaired lawn sits inside, which is one more reason a lifted edge or a bare patch on an otherwise-solid lawn is worth fixing rather than living with.</p>"),
        ],
        "scenario": ("Say you have a 70 sq ft dip near a driveway that was repaved",
                     "<p>Say you have a 70 sq ft section of turf near a Pine Hills driveway that was repaved a few years after the lawn went in, and the grade shifted enough at that edge to leave a shallow dip that collects water after storms. Fixing this usually means pulling the affected turf, checking whether the base underneath still has the depth and compaction it needs, correcting the grade at the transition, and reinstalling that section.</p>"
                     + "<p>Only opening up that section shows whether it's a grading problem at the driveway edge or a compaction issue below, and the quote follows from what the crew actually finds there, not from a description over the phone."),
        "faqs": [
            faq("Does a repair on an older Pine Hills lawn cost more than on a newer one?",
                "Not automatically. What matters is what actually failed, a grading shift, a compaction issue, or a worn seam, not the age of the surrounding house. An older lot's history of small changes, additions, repaving, does make a grade check worth doing before assuming the original layout still holds."),
            faq("Should a repair also address an unmarked septic lid it uncovers?",
                "Yes, worth flagging at minimum. If a repair opens up ground near a septic system and the pump-out lid isn't where records suggest, correcting that access is a reasonable add to the same visit, since the state's rule requires it stay reachable going forward."),
        ],
        "sources": SRC,
    },
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
