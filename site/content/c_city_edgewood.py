# -*- coding: utf-8 -*-
"""Edgewood, FL (tier 2): a very small incorporated city on Orange Avenue south of downtown
Orlando, with no building official of its own. Researched September 2026; see docs/TIER2-BRIEF.md."""
from _helpers import page, capsule, sec, table, faq, a, svc, city, county, src, ext, price
from _cityservice import cityservice_pages

SLUG = "edgewood"

SRC = [
    ("City of Edgewood — Building & Permitting", "https://edgewood-fl.gov/permitting"),
    ("City of Edgewood — Building & Construction Permit Applications", "https://edgewood-fl.gov/cityhall/page/building-construction-permit-applications"),
    ("Edgewood Code of Ordinances, Chapter 114 (Landscaping), Municode Library", "https://library.municode.com/fl/edgewood/codes/code_of_ordinances?nodeId=PTIICOOR_CH114LA"),
    ("Orange County Fast Track Online Services", "https://fasttrack.ocfl.net/OnlineServices/"),
    ("Orange County Property Appraiser — parcel search", "https://ocpafl.org/"),
    ("OUC — service rates and costs (Municipal Public Service Tax)", "https://www.ouc.com/account/service-rates-costs/"),
    ("OUC — water services", "https://www.ouc.com/about/water-services/"),
    ("Orange County Water Atlas — Lake Jessamine", "https://orange.wateratlas.usf.edu/waterbodies/lakes/140269/lake-jessamine"),
    ("Orange County Water Atlas — Boggy Creek Watershed", "https://orange.wateratlas.usf.edu/watershed/?wshedid=2"),
    ("South Florida Water Management District — Upper Kissimmee Basin water supply plan", "https://www.sfwmd.gov/our-work/water-supply/upper-kissimmee"),
    ("Wikipedia — Edgewood, Florida", "https://en.wikipedia.org/wiki/Edgewood,_Florida"),
    ("Homes.com local guide — Lake Jasmine neighborhood, Edgewood, FL", "https://www.homes.com/local-guide/edgewood-fl/lake-jasmine-neighborhood/"),
    ("USDA NRCS — official series description, Basinger series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/B/BASINGER.html"),
    ("USDA NRCS — official series description, Immokalee series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/I/IMMOKALEE.html"),
    "dep-rule", "fs125572", "hb683", "fs7203045",
]

EDG_PERMIT = ("City of Edgewood — Building & Permitting", "https://edgewood-fl.gov/permitting")
EDG_APPS = ("City of Edgewood — Building & Construction Permit Applications", "https://edgewood-fl.gov/cityhall/page/building-construction-permit-applications")
CH114 = ("Edgewood Code of Ordinances, Chapter 114 (Landscaping), Municode Library", "https://library.municode.com/fl/edgewood/codes/code_of_ordinances?nodeId=PTIICOOR_CH114LA")
FASTTRACK = ("Orange County Fast Track Online Services", "https://fasttrack.ocfl.net/OnlineServices/")
ORANGE_PA = ("Orange County Property Appraiser — parcel search", "https://ocpafl.org/")
OUC_TAX = ("OUC — service rates and costs (Municipal Public Service Tax)", "https://www.ouc.com/account/service-rates-costs/")
OUC_WATER = ("OUC — water services", "https://www.ouc.com/about/water-services/")
JESSAMINE = ("Orange County Water Atlas — Lake Jessamine", "https://orange.wateratlas.usf.edu/waterbodies/lakes/140269/lake-jessamine")
BOGGY_WSHED = ("Orange County Water Atlas — Boggy Creek Watershed", "https://orange.wateratlas.usf.edu/watershed/?wshedid=2")
SFWMD_KISS = ("South Florida Water Management District — Upper Kissimmee Basin water supply plan", "https://www.sfwmd.gov/our-work/water-supply/upper-kissimmee")
WIKI_EDGEWOOD = ("Wikipedia — Edgewood, Florida", "https://en.wikipedia.org/wiki/Edgewood,_Florida")
LAKE_GUIDE = ("Homes.com local guide — Lake Jasmine neighborhood, Edgewood, FL", "https://www.homes.com/local-guide/edgewood-fl/lake-jasmine-neighborhood/")
BASINGER = ("USDA NRCS — official series description, Basinger series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/B/BASINGER.html")
IMMOKALEE = ("USDA NRCS — official series description, Immokalee series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/I/IMMOKALEE.html")

PERMIT_ROUTE = ("/laws/permits/orange-county/", "Orange County turf permit rules")

# ============================================================== HUB
HUB = page(
    "/areas/edgewood/", "city",
    "Artificial Turf in Edgewood, FL: A Small City's Own Rules",
    "Synthetic turf installation for Edgewood, a small city on Orange Avenue with its own zoning but no building official of its own. Checked September 2026.",
    "Turf work in one of Orange County's smallest cities",
    capsule(f"With roughly 2,700 residents, Edgewood is small enough to review its own turf zoning but too small to keep a building official on staff, so Orange County still issues the permit. A synthetic lawn, pet run or putting green installed here in September 2026 costs {price('residential')} a square foot, the same as anywhere else we reach, on mid-century lots around Lake Jessamine and Lake Mary Jess about 14 miles from Kissimmee."),
    "".join([
        sec("A city small enough to review zoning but not issue its own permit",
            f"<p>Edgewood is its own incorporated city, with its own Code of Ordinances, but it has no building official on staff. The city instead reviews a project for zoning compliance first, then routes the application to Orange County's Building Department through the county's {ext(FASTTRACK[1], 'Fast Track')} system for the actual permit, inspections included ({ext(EDG_PERMIT[1], 'the Edgewood permitting page')}). A roofing, plumbing or electrical sub-permit can skip the city step and go straight to the county.</p>"
            + f"<p>That two-step arrangement means {a('/laws/permits/orange-county/', 'our Orange County permit page')} still applies to the actual issuance and inspection of an Edgewood turf project, even though the city's own Chapter 114 landscaping rules, not the county's Chapter 24, govern how the property has to look. City Hall answers zoning questions at (407) 851-2920.</p>"),
        table("Edgewood yard types and what we do differently",
              ["Where in Edgewood", "Typical home", "How that changes the job"],
              [["Lake Jessamine or Lake Mary Jess frontage", "Private docks, older seawalls, some deepwater lots", "State's 10-ft waterbody setback, waived where a seawall already stands"],
               ["Mid-century home off Orange Avenue", "1950s–60s ranch and mid-century modern styles, oak-shaded lots", "Drip-line rule; zoning sign-off from the city before the county's permit"],
               ["1990s-annexed edge parcel", "Newer subdivision product added when the city doubled in size", "Same city process, but a shorter permitting history to check against"],
               ["Commercial strip on Orange Avenue itself", "Small offices and shops rather than residential lots", "Falls outside the state's single-family, one-acre-or-less scope entirely"]],
              "Categories reflect what turns up on an average Edgewood site visit; the permitting column follows the city's published process, current as of September 2026, though every parcel is worth its own confirmation."),
        sec("Water and the district that actually covers Edgewood's lakes",
            f"<p>Edgewood is one of a handful of Orange County cities, alongside Orlando, St. Cloud and Winter Park, that levies its own tax on Orlando Utilities Commission (OUC) water sales inside its limits, which is the clearest public sign that OUC, not Orange County Utilities, bills most Edgewood addresses ({ext(OUC_TAX[1], 'the OUC rate page')}; {ext(OUC_WATER[1], 'OUC water services')}).</p>"
            + f"<p>Edgewood's own lake breaks from the county's usual pattern: the water atlas maps Lake Jessamine into the Boggy Creek Watershed, a basin whose water works south toward the Kissimmee chain instead of north like most of the region ({ext(JESSAMINE[1], 'the Lake Jessamine entry')}; {ext(BOGGY_WSHED[1], 'Boggy Creek Watershed, general information')}). South Florida's water managers, not St. Johns, hold authority over that particular basin ({ext(SFWMD_KISS[1], 'SFWMD’s Upper Kissimmee Basin plan')}), even though St. Johns still oversees the rest of the city and most of the county surrounding it.</p>"),
        sec("A railroad town's mid-century lots and the water they surround",
            f"<p>Edgewood grew up beside a rail line built in the 1880s, incorporated as a town in 1924 and became a city in 1973, and today counts roughly 2,700 residents at the 2020 Census, one of the smallest municipal populations in the county ({ext(WIKI_EDGEWOOD[1], 'Edgewood, Florida')}). Homes around Lake Jessamine and Lake Mary Jess run mid-century modern and ranch styles from the 1950s and 60s alongside newer infill, several with private docks on either lake ({ext(LAKE_GUIDE[1], 'a Lake Jasmine neighborhood guide')}).</p>"
            + f"<p>Lake Jessamine covers 294 surface acres at a 16-foot average depth ({ext(JESSAMINE[1], 'the Lake Jessamine entry')}), and a lot on its shore or on the smaller Lake Mary Jess beside it sits inside the state's 10-foot waterbody setback unless a seawall already separates yard from water. Away from the two lakes, the low ground common in Orange County's lake basins maps to Basinger and Immokalee series soils, poorly drained flatwoods sand that holds a seasonal high water table closer to the surface than the excessively drained ridge sand found a few miles east ({ext(BASINGER[1], 'Basinger series description')}; {ext(IMMOKALEE[1], 'Immokalee series description')}).</p>"),
        sec("City code, county permit, state floor",
            f"<p>Edgewood's Chapter 114 landscaping rules don't mention synthetic or artificial turf as of September 2026; they call for planted turf grass or groundcover in landscaped areas and separately cap grass height at 12 inches as a nuisance rule, both written around living plant material ({ext(CH114[1], 'Chapter 114, Municode')}). {a('/laws/florida-hb-683/', 'HB 683 and Rule 62-308.100')} still set the floor underneath whatever the city or county eventually writes: permeable turf over a washed base, capped irrigation, natural infill. An Edgewood HOA is a separate matter again, covered by {a('/laws/hoa-rules/', 'F.S. 720.3045')} rather than city code.</p>"
            + "<p>Anyone comparing turf installers near you in Edgewood should ask one specific question this small a city makes relevant: does the crew already know a project needs the city's zoning sign-off before Orange County issues anything, or will the first application bounce back for missing that step.</p>"),
        "<!--AUTO:city-services-->",
    ]),
    faqs=[
        faq("Does Edgewood have its own building official?",
            "No. The city reviews a project for zoning compliance and issues a stamped local approval, then Orange County's Building Department handles the actual permit and inspections through its Fast Track system. Roofing, plumbing and electrical sub-permits can go straight to the county without the city step."),
        faq("Which water utility bills most Edgewood addresses, OUC or Orange County Utilities?",
            "Edgewood is one of the Orange County cities that taxes OUC's water sales within its limits, which points to OUC as the utility serving most of the city, though a specific address is worth confirming against a recent bill."),
        faq("Is Lake Jessamine really in a different water management district than most of Orange County?",
            "Yes, according to the county's own water atlas. Lake Jessamine falls inside the Boggy Creek Watershed, a basin that answers to South Florida's water managers because its water eventually reaches the Kissimmee chain, even though most of Orange County, Edgewood included on its other sides, is St. Johns territory."),
        faq("How small is Edgewood, and does that change how a turf permit gets handled?",
            "The city counted roughly 2,700 residents at the 2020 Census, small enough that it never built its own building department and instead contracts that function to Orange County, while still keeping its own zoning and landscaping code."),
        faq("How far is Edgewood from your Kissimmee crew?",
            "Roughly 14 miles as the crow flies, well inside the 40-mile radius we work across from Kissimmee. That distance doesn't move the published price range; access, base condition and lot shape do."),
    ],
    sources=SRC, city=SLUG, crumbs=[("Service areas", "/areas/")], crumb="Edgewood",
    related=[("/areas/orange-county/", "Artificial turf in Orange County"), PERMIT_ROUTE, ("/areas/pine-castle/", "Turf in Pine Castle"), ("/areas/belle-isle/", "Turf in Belle Isle"), ("/artificial-turf-cost/", "Full turf cost guide")],
)

# ============================================================== LOCAL
LOCAL = {
    "residential": {
        "title": "Artificial Grass Installation in Edgewood, FL",
        "meta": "Synthetic lawn installs for Edgewood, FL, a small city that reviews zoning itself before Orange County issues the permit. Prices checked September 2026.",
        "h1": "A synthetic lawn under Edgewood's two-step permit process",
        "lede": capsule(f"Edgewood keeps its own zoning code but relies on Orange County to actually issue a building permit, so a lawn conversion here clears two offices instead of one. Installed turf runs {price('residential')} per square foot as of September 2026, on mid-century lots that mostly date to the 1950s and 60s."),
        "sections": [
            ("Two offices, one project: how a lawn conversion actually gets approved",
             f"<p>An Edgewood residential turf project starts with the city, which checks the application against local zoning before stamping it for the next step, then moves to Orange County's Building Department through the county's Fast Track system for the permit itself and any inspections ({ext(EDG_PERMIT[1], 'the Edgewood permitting page')}; {ext(FASTTRACK[1], 'Fast Track Online Services')}). Skipping the city's zoning sign-off is the single most common reason an Edgewood application bounces back before Orange County ever sees it.</p>"),
            ("What Edgewood's own landscaping chapter says, and doesn't",
             f"<p>Chapter 114 of Edgewood's Code of Ordinances calls for landscaped areas to carry a full sun or shade tolerant turf grass or groundcover, and separately treats grass over 12 inches tall as a code violation, both written for living plant material rather than a manufactured surface ({ext(CH114[1], 'Chapter 114, Municode')}). As of September 2026 we found nothing in that chapter naming synthetic or artificial turf, which leaves the state's May 2026 standard as the specific rule a compliant residential lawn actually has to meet.</p>"),
            ("Mid-century lots built around a railroad town's two lakes",
             f"<p>Edgewood's housing grew up beside a rail corridor from the 1880s and the city itself was incorporated in 1924, and homes near its two signature lakes today run a mix of mid-century modern and ranch styles from the 1950s and 60s ({ext(WIKI_EDGEWOOD[1], 'Edgewood, Florida')}; {ext(LAKE_GUIDE[1], 'a Lake Jasmine neighborhood profile')}). Lots that age typically carry oak canopy mature enough to reach into a planned lawn's footprint, which is where the state's drip-line rule and its certified-arborist exception come into play before excavation starts.</p>"
             + f"<p>{a('/blog/how-artificial-turf-is-installed-step-by-step/', 'Our step-by-step installation guide')} covers the excavation-through-infill sequence in full, and the {svc('residential', 'general residential installation guide')} goes through base and product choices in more depth than a city page needs. See the {city('edgewood', 'Edgewood turf guide')} above for the full permitting picture, or {city('pine-castle', 'Pine Castle')}, {city('conway', 'Conway')} and {city('belle-isle', 'Belle Isle')} for how three nearby communities handle the same oak-lot pattern.</p>"),
        ],
        "scenario": ("Say you have a 950 sq ft yard behind a mid-century ranch",
                     f"<p>A 950 square foot yard behind an Edgewood ranch home from the 1950s, with an oak holding down one corner near the property line, prices between $9,500 and $15,200 at the published {price('residential', True)} typical range. Before ordering material, the application still needs Edgewood's zoning sign-off, a step that adds a short review rather than a fee most homeowners notice, followed by Orange County's Fast Track permit for the work itself. If the oak's canopy reaches into the planned turf area, the certified-arborist letter gets sorted during that same window, so the buildable footprint is settled before the county issues anything. The $9,500–$15,200 range doesn't move based on which office is reviewing what; it moves with the yard's access, shape and base condition.</p>"),
        "faqs": [
            faq("Does Edgewood charge its own permit fee on top of Orange County's?",
                "The city's zoning review is part of its own process before an application moves to the county, and Orange County's Fast Track system issues the permit itself and sets any associated fee. Confirming both offices' current fee schedule before signing a contract avoids a surprise line item."),
            faq("Do Edgewood's mid-century lots need a different base than a newer subdivision's?",
                "The washed crushed rock base itself doesn't change, but a lot that's carried the same landscaping for sixty-plus years often has more established root systems near the work area, which can slow excavation without changing the finished base depth the state rule requires."),
        ],
        "sources": SRC,
    },
    "pet": {
        "title": "Pet Turf & Dog Runs in Edgewood, FL",
        "meta": "Dog-run turf for Edgewood, FL homes near Lake Jessamine and Lake Mary Jess, with the state's setback rule explained. Checked September 2026.",
        "h1": "Dog runs near Edgewood's two lakes and its inland streets",
        "lede": capsule(f"A dog run on Lake Jessamine or Lake Mary Jess answers to the state's 10-foot waterbody setback; one on an inland Edgewood street usually doesn't. A pet-turf install in the city costs {price('pet')} a square foot as of September 2026, built to drain fast and skip the weed barrier a plain lawn often keeps."),
        "sections": [
            ("A shoreline dog run against a 294-acre lake",
             f"<p>Lake Jessamine covers 294 surface acres at a 16-foot average depth ({ext(JESSAMINE[1], 'the Lake Jessamine entry')}), and a dog run built along its shore, or along the smaller Lake Mary Jess next door, sits inside the state's 10-foot setback zone unless an existing seawall already separates the run from the water. Several Edgewood lake lots carry private docks rather than a hard seawall, and a dock alone doesn't satisfy the exception, so confirming what's actually at the water's edge matters before a run gets designed.</p>"),
            ("Which utility bill actually reaches a dog run's irrigation cap",
             f"<p>Edgewood is one of the few Orange County cities that taxes water sales made within its limits by the Orlando Utilities Commission, a detail that points to OUC as the main utility serving the city rather than Orange County Utilities ({ext(OUC_TAX[1], 'the OUC rate schedule')}). Whichever utility appears on a specific bill, any spray head that used to reach a dog run's fenced area gets capped at installation, since the state's rule already bars watering synthetic turf from an in-ground system.</p>"),
            ("Sizing odor control for a small city's fenced yards",
             f"<p>Edgewood's mid-century lots tend toward modest fenced side or back yards rather than large open runs, which suits zeolite or coated-sand infill well: a smaller footprint means less water and less time spent rinsing on a warm afternoon, and both options fit the state's natural-material rule the way rubber crumb infill does not. A run tucked against the low ground near either lake also benefits from that faster-rinsing routine, since Basinger and Immokalee soils in the area hold water closer to the surface than higher ground a few miles east.</p>"
             + f"<p>{city('belle-isle', 'Belle Isle')} and {city('conway', 'Conway')} sit on that same broader lake system from other sides, so a similar setback calculation applies there too; the {city('edgewood', 'Edgewood turf guide')} above has Edgewood's own permitting wrinkle layered on top of it. For backing and drainage specs, {svc('pet', 'the dog-run turf page')} has the technical rundown, and {a('/blog/how-to-get-dog-urine-smell-out-of-artificial-turf/', 'our piece on dog odor')} covers the rinsing habit that keeps zeolite working.</p>"),
        ],
        "scenario": ("Say you have a 200 sq ft run beside Lake Mary Jess",
                     f"<p>A 200 square foot dog run tucked beside a fenced yard on Lake Mary Jess prices between $2,400 and $3,200 at the published {price('pet', True)} typical range. If that fence sits within ten feet of the water's edge without a seawall to claim the exception, the buildable run shrinks to whatever remains outside that strip, and the number gets recalculated off the smaller shape rather than the fence's full run. Move the same 200 square feet to an inland Edgewood street with no lake nearby, and the price lands identically, since proximity to water changes the buildable area, never the published range.</p>"),
        "faqs": [
            faq("Does a private dock on Lake Jessamine count as a seawall for the setback exception?",
                "No. The exception applies to a seawall or bulkhead that physically separates the yard from the water, not a dock, which leaves gaps for water to reach the shoreline directly. A run near a dock-only lot still measures its ten feet from the actual water line."),
            faq("Is OUC or Orange County Utilities the right one to call about capping heads in Edgewood?",
                "OUC serves most Edgewood addresses, based on the city's own tax on OUC's water sales within its limits, though checking a recent bill confirms it for a specific property before scheduling the capping work."),
        ],
        "sources": SRC,
    },
    "putting": {
        "title": "Backyard Putting Greens in Edgewood, FL",
        "meta": "Putting green installs for Edgewood, FL's small mid-century lots near Lake Jessamine, with oak drip lines explained. Prices checked September 2026.",
        "h1": "Fitting a putting green onto one of Edgewood's small lots",
        "lede": capsule(f"Edgewood counted roughly 2,700 residents at the 2020 Census, one of Orange County's smallest cities, and its mid-century lots are sized accordingly. A putting green installed here costs {price('putting')} a square foot as of September 2026, with the routing shaped to fit the yard rather than the reverse."),
        "sections": [
            ("Best turf installer near you in Edgewood starts with lot size",
             f"<p>Searching for the best putting green installer near you in Edgewood should start with a simple question: has the crew actually measured the yard, or is it quoting from a generic backyard size. The city's roughly 2,700 residents live on lots that run smaller than Conway's ranch-era acreage a few miles east, so a green here more often needs tiered contouring to make the most of a modest footprint rather than open space to fill ({ext(WIKI_EDGEWOOD[1], 'Edgewood, Florida')}).</p>"),
            ("Oak canopy on a lot that's carried the same trees for decades",
             f"<p>Mid-century Edgewood lots near Orange Avenue and around the city's two lakes often carry oak canopy that predates the current owner by a generation, and Florida's turf standard treats that canopy as off-limits unless a certified arborist signs off first ({ext(LAKE_GUIDE[1], 'a neighborhood profile of the area')}). On a smaller lot, losing a corner to that drip line reshapes a green's whole routing rather than just trimming an edge, since there's proportionally less yard left to redesign around.</p>"),
            ("A green near Lake Jessamine still answers to the same setback",
             f"<p>A putting green on a lot backing onto Lake Jessamine or Lake Mary Jess owes the water the same ten feet any other turf does, and only a standing seawall between green and lake removes that requirement ({ext(JESSAMINE[1], 'the Lake Jessamine entry, 294 surface acres')}). On a compact Edgewood lot, staking that line before finalizing cups and breaks often decides how many holes actually fit rather than just where the last foot of fringe lands.</p>"
             + f"<p>{city('pine-castle', 'Pine Castle')} and {city('oak-ridge', 'Oak Ridge')} carry the same mix of small, older lots a short drive away, and the {city('edgewood', 'Edgewood turf guide')} above ties the lot-size and lake-district facts together. Anyone weighing cup placement or a specific break percentage can check {svc('putting', 'the putting green service page')} for fringe and hardware specs, or {a('/blog/artificial-turf-glossary/', 'the terms glossary')} for what stimp speed actually measures.</p>"),
        ],
        "scenario": ("Say you have a 280 sq ft green shaped around an oak",
                     f"<p>A 280 square foot green fit into an Edgewood backyard, routed around an oak's canopy on one side and a fence line on the other, prices between $5,000 and $7,000 at the published {price('putting', True)} typical range. Because the lot itself runs smaller than a Conway ranch parcel, that 280 square feet often represents most of the usable backyard rather than a section carved out of a much larger space, which is part of why the routing gets designed before any digging starts. If the oak's canopy actually overlaps the planned green, the arborist letter comes first, and the final shape follows whatever that review allows.</p>"),
        "faqs": [
            faq("Does Edgewood's small lot size limit how big a putting green can be?",
                "It shapes the design more than it limits the size outright. A compact lot usually means a green routed around fences, oaks and the house itself rather than one long open run, which favors tiered contouring over a single flat surface."),
            faq("Do I need a certified arborist's letter for a green near an old Edgewood oak?",
                "Only if the canopy actually overlaps the planned turf area. The state's rule allows synthetic turf inside a tree's drip line solely with a certified arborist's written certification that the installation won't cause harm."),
        ],
        "sources": SRC,
    },
    "playground": {
        "title": "Playground Turf for Edgewood, FL Backyards",
        "meta": "Play-area turf for Edgewood, FL families, sized to the city's smaller mid-century lots with shock pad notes. Prices checked September 2026.",
        "h1": "Cushioned play surfaces on Edgewood's mid-century lots",
        "lede": capsule(f"Edgewood's own landscaping code caps grass height at 12 inches as a nuisance rule, a line a play surface never approaches since it never grows at all. A cushioned play area installed here costs {price('playground')} a square foot as of September 2026, with the shock pad matched to the specific equipment's fall height rather than a flat guess."),
        "sections": [
            ("A code written for mowing, and a surface that skips it entirely",
             f"<p>Edgewood's Chapter 114 treats grass taller than 12 inches as a code violation, a rule aimed at mowing compliance on living lawns rather than at play surfaces specifically ({ext(CH114[1], 'Chapter 114, Municode')}). A synthetic play area never grows past that line in the first place, which sidesteps the nuisance question entirely, though the state's own turf standard, not the city's mowing rule, is still what governs the pad, backing and infill underneath the equipment.</p>"),
            ("Fitting a play corner into a smaller Edgewood backyard",
             f"<p>With roughly 2,700 residents on lots that run smaller than the ranch-era acreage found a few miles east, an Edgewood play area typically claims one defined corner of the yard rather than spreading across it, leaving room for a family's regular lawn on the same property ({ext(WIKI_EDGEWOOD[1], 'Edgewood, Florida')}). Containment edging around that corner matters for one specific reason: it's what keeps rubber infill from migrating past the footprint Florida's rule actually permits it in, which is strictly the ground directly under the equipment.</p>"),
            ("Low ground near the lakes and what it means for the base",
             f"<p>The flatwoods sand common around Edgewood's two lakes, mapped to Basinger and Immokalee series soils, holds a seasonal high water table closer to the surface than the drier ridge ground found toward Conway to the east ({ext(BASINGER[1], 'Basinger series description')}; {ext(IMMOKALEE[1], 'Immokalee series description')}). A play area's shock pad needs to drain at least as fast as that base moves water, which is part of why the crushed-rock layer underneath gets built toward the fuller end of the state's allowed depth on a lot near either lake.</p>"
             + f"<p>{a('/blog/is-artificial-turf-safe-for-kids-pfas-lead/', 'Our article on turf safety for kids')} covers the PFAS and infill questions parents ask most, and the {svc('playground', 'playground turf guide')} goes through ASTM fall-height ratings in full. The {city('edgewood', 'Edgewood turf guide')} above has the lot-size context; {city('pine-castle', 'Pine Castle')} and {city('oak-ridge', 'Oak Ridge')} handle similar small-lot play areas nearby.</p>"),
        ],
        "scenario": ("Say you have a 300 sq ft play corner near Orange Avenue",
                     f"<p>A 300 square foot play corner behind an Edgewood home a few streets off Orange Avenue, sized for a swing set and a slide, prices between $3,600 and $5,700 at the published {price('playground', True)} typical range, with the shock pad's thickness set by the equipment's tallest fall height rather than a flat guess. Because the lot itself runs on the smaller side, that 300 square feet often sits close to a fence line on at least one edge, which affects how the containment border gets anchored more than it affects the price. The rest of the yard's lawn, if any remains once the play corner and any dog run are laid out, prices separately at the residential range.</p>"),
        "faqs": [
            faq("Does Edgewood's 12-inch grass rule apply to playground turf?",
                "No. That nuisance rule targets mowing on living lawns, and a synthetic play surface never grows tall enough to trigger it. The surface still has to meet the state's own material and shock-pad standards regardless."),
            faq("Why does a play area near Edgewood's lakes need a deeper base than one further inland?",
                "The Basinger and Immokalee soils common around Lake Jessamine and Lake Mary Jess hold water closer to the surface than drier ground a few miles away, so building the crushed-rock base toward the fuller end of the state's allowed depth keeps the shock pad draining at the rate it needs to."),
        ],
        "sources": SRC,
    },
    "pool": {
        "title": "Pool & Lanai Turf in Edgewood, FL Screen Enclosures",
        "meta": "Turf around Edgewood, FL pool cages, including how the city's zoning review and Orange County's permit both apply. Checked September 2026.",
        "h1": "Turf beside an Edgewood pool cage, city and county both",
        "lede": capsule(f"A pool-area turf project in Edgewood clears the city's zoning desk before Orange County issues anything, since Edgewood has no building official of its own. Turf around a screened pool costs the same {price('residential')} a square foot here as of September 2026, glued at the hardscape edges and set on a drainage underlay beneath the enclosure."),
        "sections": [
            ("Searching for the best pool turf installer near you in Edgewood?",
             f"<p>Searching for the best pool and lanai turf installer near you in Edgewood should turn up a crew that already knows the city's two-step process: zoning approval from Edgewood, then the permit itself from Orange County's Building Department through Fast Track ({ext(EDG_PERMIT[1], 'the Edgewood permitting page')}; {ext(FASTTRACK[1], 'Fast Track Online Services')}). A contractor who has to look that up mid-quote hasn't worked in the city before.</p>"),
            ("Pool cages added when Edgewood doubled in size",
             f"<p>Edgewood annexed several contiguous Orange County neighborhoods in the 1990s, roughly doubling its footprint, and much of that newer stock came with a screened pool cage as a standard feature ({ext(WIKI_EDGEWOOD[1], 'Edgewood, Florida')}). A lanai turf strip inside one of those enclosures needs a drainage underlay where it meets the existing deck, since the concrete slab doesn't pass water the way soil does, regardless of whether the home sits in the original 1920s town footprint or the 1990s-annexed edge.</p>"),
            ("Capped irrigation regardless of which utility bills the address",
             f"<p>Edgewood's own tax on Orlando Utilities Commission water sales within city limits points to OUC as the utility serving most pool-cage addresses here ({ext(OUC_TAX[1], 'the OUC rate schedule')}), though a specific bill is worth checking. Either way, any spray head that used to reach a pool deck's border gets capped as part of the install, because Florida's May 2026 standard simply doesn't allow an in-ground system to keep watering synthetic turf, whichever utility happens to be billing the account.</p>"
             + f"<p>{city('belle-isle', 'Belle Isle')} and {city('conway', 'Conway')} see similar pool-cage jobs on their own older enclosures, and the {city('edgewood', 'Edgewood turf guide')} above walks through the permitting sequence specific to this city. On the product side, {svc('pool', 'the pool and lanai service page')} lays out backing choices for a glued edge, and {a('/blog/can-artificial-turf-melt/', 'our article on whether turf can melt')} is worth a look given how much reflective glass a screen cage puts near the ground.</p>"),
        ],
        "scenario": ("Say you have a 220 sq ft border inside a 1990s pool cage",
                     f"<p>A 220 square foot pool-deck border in one of Edgewood's 1990s-annexed neighborhoods prices between $2,200 and $3,520 at the published {price('residential', True)} typical range. The application still needs Edgewood's zoning sign-off before Orange County's Fast Track system issues the actual permit, a sequence that adds a short review step rather than a separate fee most homeowners notice. Whether the home sits in that newer annexed section or closer to Edgewood's original footprint on Orange Avenue, the same drainage underlay goes in beneath the turf at the deck line.</p>"),
        "faqs": [
            faq("Does a newer, 1990s-annexed Edgewood home skip the city's zoning review?",
                "No. Every address inside Edgewood's current limits goes through the same city zoning check before Orange County issues a permit, regardless of whether the neighborhood was part of the original 1924 town or added during the 1990s annexation."),
            faq("Does an Edgewood pool cage need a different drainage underlay than one in Conway or Belle Isle?",
                "The underlay itself is the same product and method. What can differ is the deck's age and condition, since older concrete has had more time to develop control-joint gaps or minor settling worth checking before turf goes down tight to the slab."),
        ],
        "sources": SRC,
    },
    "repair": {
        "title": "Turf Repair in Edgewood, FL Small-Lot Yards",
        "meta": "Turf repair for Edgewood, FL yards near Lake Jessamine and Orange Avenue, priced after a site visit rather than a flat rate. Checked September 2026.",
        "h1": "Fixing turf on Edgewood's small lots and lake edges",
        "lede": capsule("There's no published per-square-foot rate for a repair, since the number depends entirely on what a crew finds once it looks. Edgewood's calls tend to cluster around three things: a seam near Jessamine or Mary Jess that never respected the setback, an older patch that doesn't match what's already down, or a base that skipped washed rock before the 2026 standard existed."),
        "sections": [
            ("A lifted edge near Lake Jessamine usually points at the setback",
             f"<p>Turf that lifts along a fence or border near Lake Jessamine or Lake Mary Jess often traces back to how close the original install sat to the water rather than a bonding defect: a section inside the state's 10-foot setback, or inside a swale carrying runoff toward either lake, takes more direct water pressure during a storm than a properly set-back edge does ({ext(JESSAMINE[1], 'the Lake Jessamine entry')}). A repair there usually starts with re-staking the actual setback line before any patching begins.</p>"),
            ("What low ground near the lakes does to an old, unwashed base",
             f"<p>Edgewood's lake-basin soils, mapped to Basinger and Immokalee series with a seasonal high water table close to the surface, hide an old unwashed base differently than drier ground would ({ext(BASINGER[1], 'Basinger series description')}). Fines that bound into a crust under an older Edgewood lawn tend to show up as standing water that lingers well after a storm passes, since the naturally poorly drained soil beneath the crust has nowhere else for that water to go.</p>"),
            ("Patching a small lot without the repair reading as an obvious rectangle",
             f"<p>On a compact Edgewood lot, a repaired section is more visible relative to the whole yard than the same patch would be on a wider Conway or Belle Isle lawn, simply because there's less surrounding turf to blend it into. Cutting the patch along an existing seam or panel line, and matching pile height and infill rate to what's already down, matters more here for the same reason: there's less room for a mismatch to hide.</p>"
             + f"<p>{city('pine-castle', 'Pine Castle')} and {city('belle-isle', 'Belle Isle')} field similar small-lot repair calls of their own, and the {city('edgewood', 'Edgewood turf guide')} above has the lake-setback numbers specific to this city. {svc('repair', 'The repair service page')} covers how pile height and infill rate get matched during a patch, and {a('/blog/does-homeowners-insurance-cover-artificial-turf/', 'our piece on homeowners insurance')} is worth a read before assuming a repair comes out of pocket.</p>"),
        ],
        "scenario": ("Say a section near your dock in Edgewood starts to lift",
                     "<p>A dock-side lift on Lake Jessamine rarely gets a number over the phone, because the first question is whether that dock was ever meant to count as the seawall exception, and most private docks weren't built to. A crew walks the original setback line before touching anything, checks the base for the crust an unwashed subgrade leaves behind on Edgewood's slow-draining lake-basin soil, and only then prices the reseam, since patching a bad base without fixing it just delays the next failure by a season. A photo is enough to schedule the visit; it's never enough to schedule the repair itself.</p>"),
        "faqs": [
            faq("Why would turf near Lake Jessamine fail faster than turf on an inland Edgewood street?",
                "Usually because of proximity to water rather than product quality: turf installed inside the state's 10-foot setback or inside a drainage path absorbs more direct water pressure during storms than turf set back the required distance, which shows up over time as lifted edges and shifted infill."),
            faq("Can a small Edgewood lot make a turf repair more noticeable than it would be elsewhere?",
                "Often, yes, simply because there's less surrounding lawn to blend a patch into on a compact lot. Matching the patch to an existing seam line and the original product's pile height and infill rate matters more here than on a much larger yard."),
        ],
        "sources": SRC,
    },
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
