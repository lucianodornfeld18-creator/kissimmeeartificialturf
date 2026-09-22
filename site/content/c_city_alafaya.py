# -*- coding: utf-8 -*-
"""Alafaya, FL (tier 2): unincorporated Orange County community around Alafaya Trail and UCF."""
from _helpers import page, capsule, sec, table, faq, ul, a, svc, city, post, src, ext, price
from _cityservice import cityservice_pages

SLUG = "alafaya"

SRC = [
    ("U.S. Census Bureau — QuickFacts, Alafaya CDP, Florida", "https://www.census.gov/quickfacts/fact/table/alafayacdpflorida/PST045224"),
    ("Waterford Lakes, Florida — Wikipedia", "https://en.wikipedia.org/wiki/Waterford_Lakes,_Florida"),
    ("Waterford Lakes Town Center — Wikipedia", "https://en.wikipedia.org/wiki/Waterford_Lakes_Town_Center"),
    ("Homes.com — Eastwood neighborhood guide, Alafaya, FL", "https://www.homes.com/alafaya-fl/eastwood-neighborhood/houses-for-sale/"),
    ("Waterford Lakes Community Association — homeowner information", "https://www.hoabulletinboard.com/hoa/wlalfl/about_hoa/"),
    ("Econlockhatchee River — Wikipedia", "https://en.wikipedia.org/wiki/Econlockhatchee_River"),
    ("St. Johns River Water Management District — Econlockhatchee Sandhills Conservation Area", "https://www.sjrwmd.com/lands/recreation/econlockhatchee/"),
    ("St. Johns River Water Management District — Orange County", "https://www.sjrwmd.com/district-counties/orange-county/"),
    ("Orange County Parks — Little Econ Greenway", "https://www.orangecountyfl.net/cultureparks/parks.aspx?m=dtlvw&d=25"),
    ("Orange County Parks — Blanchard Park", "https://www.ocfl.net/cultureparks/parks.aspx?m=dtlvw&d=8"),
    ("Florida Forest Service — Little Big Econ State Forest", "https://www.fdacs.gov/Forest-Wildfire/Our-Forests/State-Forests/Little-Big-Econ-State-Forest"),
    ("USDA NRCS — Official Series Description, Immokalee series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/I/IMMOKALEE.html"),
    ("USDA NRCS — Official Series Description, Myakka series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/M/MYAKKA.html"),
    ("USDA NRCS — Official Series Description, EauGallie series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/E/EAUGALLIE.html"),
    ("BNBCalc — Orange County, Florida short-term rental regulation guide", "https://www.bnbcalc.com/blog/short-term-rental-regulation/orange-county-florida-guide"),
    ("The Short Term Shop — Orlando short-term rental regulations, 2026", "https://theshorttermshop.com/orlando-short-term-rental-regulations/"),
    ("Orange County Code, Chapter 24, Municode Library", "https://library.municode.com/fl/orange_county/codes/code_of_ordinances?nodeId=PTIIORCOCO_CH24LABUOPSP"),
    ("Orange County Fast Track Online Services", "https://fasttrack.ocfl.net/OnlineServices/"),
    ("Orange County Property Appraiser — parcel search", "https://ocpafl.org/"),
    ("Orange County Utilities — watering restrictions", "https://www.orangecountyfl.net/watergarbagerecycling/wateringrestrictions.aspx"),
    "usda-wss", "dep-rule", "fs125572", "fs7203045",
]

# ============================================================== hub
HUB = page(
    "/areas/alafaya/", "city",
    "Artificial Turf in Alafaya, FL (Near UCF)",
    "Artificial turf installation near UCF and Waterford Lakes in Alafaya, FL: pond setbacks, HOA review, soil and permits, checked September 2026.",
    "Synthetic grass for Alafaya's pond-lot and rental-duplex yards",
    capsule(f"Alafaya runs along Alafaya Trail against the University of Central Florida, in unincorporated Orange County about 21 miles from our Kissimmee shop. Installed turf here prices like everywhere else in the region, {price('residential')} a square foot this September, on lots that mostly date to the 1990s build-out around Waterford Lakes. A backyard pond usually means a setback question before it means a turf question."),
    "".join([
        sec("A campus community built around its ponds",
            f"<p>Alafaya is a census-designated place, not its own city, and most of what people mean by the name is the stretch of unincorporated Orange County that grew up around Alafaya Trail once the University of Central Florida expanded through the 1980s and 1990s. The U.S. Census Bureau counted {ext('https://www.census.gov/quickfacts/fact/table/alafayacdpflorida/PST045224', '92,452 residents')} here at the 2020 census, spread across a mix of 1990s subdivisions, apartment complexes and duplexes built for students and staff rather than a single town center.</p>"
            + f"<p>The area's namesake development is Waterford Lakes, platted under the name Huckleberry before it was renamed in 1991 and built out through the rest of the decade into one of east Orange County's largest master-planned communities, with {ext('https://en.wikipedia.org/wiki/Waterford_Lakes,_Florida', 'its own parks, lakes and community association')}. Eastwood, just south, filled in between 1990 and 2002 with the ranch and two-story houses typical of that build-out, including a gated section called {ext('https://www.homes.com/alafaya-fl/eastwood-neighborhood/houses-for-sale/', 'The Preserve at Eastwood')}. Both plans came with the retention ponds Florida started requiring for new stormwater systems around that time, which is why so many Alafaya backyards end at water instead of a fence line.</p>"),
        table("How four Alafaya lot types change a turf job",
              ["Common Alafaya lot", "The local wrinkle", "How we adjust"],
              [["1990s Waterford Lakes or Eastwood lot on a pond", "The lot line often sits inside 10 ft of the bank, and the swale beside it is off-limits under the state rule", "We stake the setback and swale first, then turf only the buildable rest"],
               ["UCF-area rental duplex or townhome", "A landlord owns it, tenants and pets turn over every year or two, and the state rule bars watering it through the old sprinkler zone", "A tougher-face-weight product in a plain rectangle a property manager can inspect at a glance"],
               ["Zero-lot-line townhome side strip", "Three or four feet of shaded, root-crossed ground where sod has never filled in", "Narrow-format turf trimmed tight to the fence and the slab"],
               ["Screened lanai on a 1990s pool home", "Concrete deck, no soil underneath, edges that have to glue rather than pin", "A drainage underlay so the deck still sheds toward its original drain"]],
              "Housing ages and pond placement per the sources above; every yard still gets measured before anything is ordered."),
        sec("Water, soil and the Econ River at the edge of town",
            f"<p>Orange County Utilities bills most of Alafaya and runs the county's seasonal watering schedule: two days a week during daylight saving time, one day the rest of the year, by odd or even address, with nothing between 10 a.m. and 4 p.m. ({ext('https://www.orangecountyfl.net/watergarbagerecycling/wateringrestrictions.aspx', 'current restrictions')}). A synthetic lawn doesn't draw from either schedule once installed, since {a('/laws/florida-hb-683/', "the state's turf rule")} requires the old sprinkler zone under it to be capped at the valve rather than left running. The county sits in the {ext('https://www.sjrwmd.com/district-counties/orange-county/', 'St. Johns River Water Management District')}, and Alafaya's own namesake waterway, the Econlockhatchee, is the district's water to manage: a blackwater tributary of the St. Johns designated an Outstanding Florida Water, with a roughly 173,000-acre watershed running through the county's east side ({ext('https://en.wikipedia.org/wiki/Econlockhatchee_River', 'watershed detail')}).</p>"
            + f"<p>The county's own {ext('https://www.orangecountyfl.net/cultureparks/parks.aspx?m=dtlvw&d=25', 'Little Econ Greenway')} follows the river for several miles from Alafaya Trail through {ext('https://www.ocfl.net/cultureparks/parks.aspx?m=dtlvw&d=8', 'Blanchard Park')} toward Forsyth Road, and the state's Little Big Econ forest protects more of the floodplain a few miles north. Underneath the subdivisions, expect the same poorly drained flatwoods sand as the rest of east Orange County: Myakka, Immokalee and EauGallie series soils with a water table that can sit within a couple of feet of grade after a wet summer ({ext('https://soilseries.sc.egov.usda.gov/OSD_Docs/I/IMMOKALEE.html', 'Immokalee')}, {ext('https://soilseries.sc.egov.usda.gov/OSD_Docs/M/MYAKKA.html', 'Myakka')}, {ext('https://soilseries.sc.egov.usda.gov/OSD_Docs/E/EAUGALLIE.html', 'EauGallie')}), which is exactly the ground a washed crushed-rock base is built to handle. A parcel-level pull from the {src('usda-wss', 'Web Soil Survey')} is worth doing before excavation starts, since flatwoods soils vary lot to lot.</p>"),
        sec("Permits, the county code, and what Waterford Lakes actually reviews",
            f"<p>Alafaya has no city hall of its own, so a turf job here answers to {a('/laws/permits/orange-county/', 'unincorporated Orange County')}: Permitting Services and the Division of Building Safety, reachable at 407-836-5550, with applications tracked through Fast Track Online Services. Orange County Code Chapter 24 defines &ldquo;turf, turf grass or sod&rdquo; as living grass species and, as of this writing, has no section written for a synthetic product, so a residential conversion here isn't tripping a named turf ordinance the way it might in a city with its own rule. A parcel search on {ext('https://ocpafl.org/', 'the county appraiser’s site')} confirms the taxing jurisdiction before anyone assumes it.</p>"
            + f"<p>Waterford Lakes runs its own layer on top of that: its community association reviews exterior and landscaping changes through an architectural committee and a change-request form before work starts ({ext('https://www.hoabulletinboard.com/hoa/wlalfl/about_hoa/', "the association's own listing")}). We could not find a published clause naming synthetic turf specifically, so treat a submittal there as a case the committee decides on its own terms rather than a pre-approved item. Either way, {a('/laws/hoa-rules/', "Florida law limits what an HOA can restrict")} to what's actually visible from the street or a neighboring lot, which matters on a corner lot more than an interior one.</p>"),
        sec("Duplexes, student housing and the short-term-rental question",
            f"<p>A lot of Alafaya's housing near campus is landlord-owned duplexes and townhomes leased by the semester or the year, not by the night. That's consistent with how unincorporated Orange County zones the area: nightly and weekly rentals aren't a permitted use in standard residential districts, and the county's vacation-rental activity concentrates instead in a separate zoning district near the theme parks, not around UCF ({ext('https://www.bnbcalc.com/blog/short-term-rental-regulation/orange-county-florida-guide', 'zoning summary')}; {ext('https://theshorttermshop.com/orlando-short-term-rental-regulations/', 'a 2026 rules roundup')}). For a landlord here, the pitch for turf is closer to a maintenance decision than a guest-experience one: no mower to schedule between leases, no dead patch to explain at move-out.</p>"
            + '<p>Ask around a UCF-area leasing office for the best artificial turf installer near Alafaya and the answers usually circle back to the same two questions: how fast can it be inspected between tenants, and does it survive a security deposit walkthrough.</p>'),
        "<!--AUTO:city-services-->",
    ]),
    faqs=[
        faq("Is Alafaya a city with its own building department?", "No. Alafaya is a census-designated place, so permitting runs through unincorporated Orange County's Permitting Services and Division of Building Safety rather than a city hall. There's no separate Alafaya code to check, only the county's."),
        faq("How close does turf have to stay from a Waterford Lakes pond?", "Ten feet is the line, measured from the bank, unless the pond already has a seawall standing between the water and the yard. The swale beside the pond is also off the table for turf. Most lots keep plenty of usable yard outside that line; a site visit confirms where it falls."),
        faq("Can a rental duplex near UCF get artificial turf without irrigation?", "Yes, and it has to run that way. The state standard bars using an in-ground system to water synthetic turf, so any zone under the new lawn gets capped at installation and a hose handles rinsing after that."),
        faq("Does the Waterford Lakes HOA require pre-approval for a lawn change?", "Its architectural committee reviews exterior and landscaping changes through a change-request form, and we haven't seen a published rule naming synthetic turf one way or the other. Submitting a sample and a site plan before ordering material is the safer route."),
        faq("What soil should I expect digging a base in Alafaya?", "Mostly Myakka, Immokalee and EauGallie fine sands, the same poorly drained flatwoods family as the rest of east Orange County, with a water table that can sit close to the surface after summer rain. A Web Soil Survey pull for the specific parcel confirms it before excavation."),
    ],
    sources=SRC, city=SLUG, crumbs=[("Service areas", "/areas/")], crumb="Alafaya",
    related=[("/areas/orange-county/", "Orange County: turf rules and yards"), ("/laws/permits/orange-county/", "Orange County turf permit rules"), ("/areas/avalon-park/", "Turf in Avalon Park"), ("/areas/union-park/", "Turf in Union Park"), ("/artificial-turf-cost/", "Turf cost tables for Central Florida")],
)

# ============================================================== local (city x service)
LOCAL = {
    "residential": {
        "title": "Artificial Grass Installation in Alafaya, FL – Pond Lots",
        "meta": "Artificial grass installation in Alafaya, FL for pond-backed Waterford Lakes and Eastwood lots: setbacks, soil and cost, checked September 2026.",
        "h1": "Converting a pond-lot lawn near Waterford Lakes to turf",
        "lede": capsule(f"Most Alafaya residential quotes land between {price('residential', True)} a square foot, inside the wider {price('residential')} range that's held steady across Central Florida since before this September. What's different here is how often the yard ends at a retention pond from the area's 1990s build-out, which decides where turf can actually go before price ever comes up."),
        "sections": [
            ("How the pond behind a Waterford Lakes lot changes the layout",
             f"<p>Waterford Lakes and the subdivisions around it were platted once Florida required new developments to hold their own stormwater on site, so a big share of the area's backyards border a pond rather than another fence line. Before we quote a lawn like that, we stake the state's 10 ft waterbody setback from the bank and mark the swale that usually runs along it, since {a('/laws/florida-hb-683/', 'the rule')} keeps turf out of both unless a seawall already separates the yard from the water. Most lots still have a comfortable amount of buildable yard once that strip is set aside; a few narrower ones lose more of the usable rectangle than the owner expected until we walk it together.</p>"
             "<p>The upside of a pond lot is drainage direction: water already has somewhere to go, so grading the base toward the bank instead of fighting a flat interior lot is usually the simpler build. What still needs checking is whether the pond has a littoral shelf planted with wetland vegetation, since that strip counts the same as the pond itself for setback purposes even when it looks like ordinary bank.</p>"),
            ("What a landlord-owned rental yard needs that an owner-occupied one doesn't",
             f"<p>A meaningful share of Alafaya's housing stock near campus is owned by someone who doesn't live there, leased to tenants who change every year or two. That changes what we recommend more than it changes the install itself: a heavier face-weight product holds up to a security deposit's worth of scrutiny and the occasional moving truck better than a budget-grade blade, and a plain rectangle without a lot of curves or planting cutouts is faster for a property manager to walk and approve at turnover. {svc('pet', 'Pet turf')} comes up often in the same conversation, since a rotating cast of tenants usually means a rotating cast of dogs using the same patch of yard.</p>"
             f"<p>Because the state standard caps irrigation on any turf area, a landlord converting a rental yard also stops paying to water it between tenants, not just to mow it. {post('does-artificial-grass-increase-home-value-florida', 'Whether that shows up in resale value')} is a separate question from whether it lowers a rental's carrying cost, and for a landlord the second number usually matters more.</p>"),
            ("Permits, the HOA layer, and who actually signs off",
             f"<p>A residential conversion in Alafaya answers to unincorporated {a('/laws/permits/orange-county/', "Orange County's permitting office")} rather than a city hall, since the area has none of its own. County code doesn't have a section written for synthetic turf specifically, so the review that applies is the general one: drainage, any plumbing work capping irrigation, and, on a pond lot, whether the county's own stormwater permit for that subdivision restricts work near the bank. Inside {city('alafaya', 'Waterford Lakes')}, the community association layers its own architectural review on top of the county's, through a change-request form rather than a walk-in permit desk.</p>"
             f"<p>Nothing published tells us the association names turf one way or the other, so we treat a submittal there as a case decided on its merits rather than a pre-cleared item, and we build the sample board and site plan around whatever the committee asks to see. {a('/laws/hoa-rules/', 'What state law actually limits an HOA to')} still applies underneath that review either way.</p>"),
        ],
        "scenario": ("A worked example: a 760 sq ft Eastwood backyard on a pond",
                     f"<p>Say an Eastwood house built in the mid-1990s has a 760 sq ft backyard that ends at a retention pond about 14 ft from the patio. Staking the 10 ft setback and a 3 ft swale along the bank removes roughly 90 sq ft from the plan, leaving about 670 sq ft to turf. At {price('residential')} a square foot, that yard prices between {f'${670*8:,.0f}'} and {f'${670*18:,.0f}'}, with a straightforward rectangle like this one usually landing in the {price('residential', True)} band rather than the top of the range. The old irrigation zone for that section gets capped at the valve, not removed, and the swale strip stays whatever ground cover it already has rather than turf.</p>"),
        "faqs": [
            faq("Do I lose the whole yard if it backs a Waterford Lakes pond?", "No. The setback only removes a strip near the water, usually 10 to 15 ft counting the swale, not the whole lot. Most Eastwood and Waterford Lakes backyards keep most of their square footage once that line is staked."),
            faq("Does a rental property need a different turf product than an owner-occupied home?", "Not a different product line, just a different spec. We usually push toward a heavier face weight and standard silica infill for a rental, since it holds up to tenant turnover without adding an odor-control cost the landlord doesn't need yet."),
        ],
        "sources": SRC,
    },
    "pet": {
        "title": "Pet Turf Installation in Alafaya, FL – Rentals & Yards",
        "meta": "Pet turf for Alafaya rentals and Waterford Lakes yards: drainage, odor control and cost as of September 2026, with sources.",
        "h1": "Dog turf for Alafaya's duplexes, townhomes and pond lots",
        "lede": capsule(f"Pet turf pricing doesn't move for the address: {price('pet')} a square foot, usually {price('pet', True)}, the same this month as it's been all year. A lot of the calls we get in Alafaya are from a landlord or a property manager rather than a single owner, since so much of the housing near UCF turns over tenants, and pets, every lease cycle."),
        "sections": [
            ("Why a rotating cast of tenants changes the pet-turf spec",
             f"<p>A duplex or townhome near campus rarely has the same dog using its yard for more than a year or two, which is a different problem than a family's forever-home dog run. We lean toward zeolite or a coated sand infill for that reason: both keep working on whatever the next tenant's dog leaves behind without a deep clean between leases, and neither needs the yard rebuilt to switch tenants. A weed barrier gets skipped under the turf either way, because a membrane there catches liquid at the surface rather than letting it pass through into the rock, and that holds whether the current dog has lived there five years or five months.</p>"
             f"<p>{svc('residential', 'A plain residential lawn')} can take the same infill if an owner wants odor control without a dedicated dog run, so the choice isn't really about the yard's shape, it's about how often the ground gets asked to reset for a new animal.</p>"),
            ("Small yards, alley gates and the flush-out routine",
             "<p>Alafaya's townhome and zero-lot-line lots tend to hand a dog a narrow strip rather than an open backyard, often the same three or four feet where sod has never taken hold in the shade of a fence line. That narrow footprint actually helps a pet build: a smaller area is faster and cheaper to flush out with a hose, and a tight strip is easier to grade toward a single low corner than a wide-open lawn is. Where the gate is narrow, which is common on these lots, we plan the base delivery and compaction equipment around wheelbarrow access rather than assuming a skid steer fits.</p>"),
            ("What backing onto a pond changes for a dog run",
             f"<p>On the Waterford Lakes and Eastwood lots that back up to a retention pond, a dog run sitting near that edge still has to clear the state's 10 ft waterbody setback and stay off the swale, the same as any other turf. That's rarely a problem for a run sized for a dog rather than a full lawn, since most pet areas are smaller to begin with, but we still stake the line before laying out fencing so the run isn't built half inside the setback. {a('/laws/florida-hb-683/', "The rule")} treats a dog run and a front lawn the same way here; there's no separate exception for pet areas.</p>"),
        ],
        "scenario": ("A worked example: a 220 sq ft dog run behind a UCF-area rental",
                     f"<p>Say a landlord owns a 220 sq ft fenced strip behind a rental townhome near UCF, currently bare dirt where grass never survived two dogs and no irrigation schedule. At {price('pet')} a square foot for pet turf, that run prices between {f'${220*10:,.0f}'} and {f'${220*18:,.0f}'}, with a mid-grade zeolite build typically landing near {f'${220*14:,.0f}'}. Skipping the weed barrier and grading the narrow strip toward the alley gate keeps the flush-out simple for whichever tenant's dog uses it next, and the whole run installs in well under a day given the size.</p>"),
        "faqs": [
            faq("What's the best pet turf setup for a rental property near UCF?", "A heavier-backing product with zeolite or coated-sand infill and no weed barrier underneath, since that combination resets easily between tenants without a rebuild. A simple rectangle also makes the run faster for a property manager to inspect at turnover."),
            faq("Can two dogs share a small Alafaya townhome yard on turf?", "Yes, though a smaller area needs more frequent hose rinsing than a bigger one carrying the same two dogs, since there's less ground to spread the use across. Zeolite or coated sand infill helps stretch the time between deep flush-outs."),
            faq("Does a dog run near a retention pond need extra permission?", "It needs to clear the same 10 ft setback and stay off the swale as any other turf near the water, but that's a site-layout question, not a separate permit category for pets."),
        ],
        "sources": SRC,
    },
    "putting": {
        "title": "Backyard Putting Greens in Alafaya, FL",
        "meta": "Backyard putting greens in Alafaya, FL on Waterford Lakes and Eastwood lots: sizing, contour and pricing, checked September 2026.",
        "h1": "Putting greens on Alafaya's larger 1990s lots",
        "lede": capsule(f"A green's price starts at the low end of {price('putting')} a square foot and climbs toward the top with contouring and cups, landing most Alafaya builds around {price('putting', True)} this year. Room for one is the real filter here, and that usually means an older, larger Waterford Lakes or Eastwood parcel rather than the newer townhome product closer to campus."),
        "sections": [
            ("Which Alafaya lots actually have room for a green",
             f"<p>Alafaya doesn't have a golf-course community anchoring it the way some Central Florida towns do, so the demand here is almost entirely backyard practice space rather than a lot chosen for its fairway view. The candidates are usually the wider, deeper parcels from the original Waterford Lakes and Eastwood plats, where the house sits well forward of a rear property line that often meets a pond. That distance between patio and water is exactly where a two- or three-cup green with a chipping apron fits, once the 10 ft setback from the bank is marked off.</p>"
             f"<p>A zero-lot-line townhome closer to UCF almost never has the run of grass a green needs, so for those addresses we're usually pointing people toward {svc('residential', 'a small putting-adjacent patch of regular turf')} instead of a dedicated green.</p>"),
            ("Building a green over Alafaya's sandy base",
             "<p>The subgrade work is where a putting green earns its price over a flat lawn: contouring the compacted base to hold a break, rather than just grading it flat, has to happen in the crushed-rock layer itself, because turf laid over an uneven base just telegraphs every dip and high spot into the roll. On the area's sandy flatwoods soil, that means building the contour in compacted lifts the same way a flat lawn's base goes down, just shaped rather than sloped in one direction, with the fringe turf and cups set once the contoured base has been checked with a level in more than one direction.</p>"),
            ("Fitting a green around a pond-lot setback",
             f"<p>On a lot where the buildable yard already loses ground to the state's waterbody setback, the green's footprint has to be planned around whatever's left rather than assumed first. That usually means a shorter green with a tighter chipping apron instead of the longer layout a full-acre lot could carry, and it's worth deciding the green's shape before ordering turf rather than after, since {a('/laws/florida-hb-683/', "the setback")} doesn't flex for a green any more than it does for a lawn. {post('artificial-turf-glossary', 'Stimp, nap and pile direction')} matter more on a green than on any other service we install, since they're what makes the roll true.</p>"),
        ],
        "scenario": ("A worked example: a 340 sq ft green on an Eastwood lot",
                     f"<p>Say an Eastwood backyard has 340 sq ft available for a green once the pond setback is staked off, enough for a contoured two-cup layout with a fringe collar and a small chipping pad. At {price('putting')} a square foot, that project prices between {f'${340*14:,.0f}'} and {f'${340*30:,.0f}'}, with the contouring and fringe work usually landing it in the {price('putting', True)} band rather than the entry end. Most of that cost sits in shaping the base correctly, not in the putting-surface turf itself, since a flat green with a wrong break is a redo, not a repair.</p>"),
        "faqs": [
            faq("Is there room for a putting green on a typical Alafaya townhome lot?", "Rarely. Townhome and zero-lot-line yards near campus are usually too narrow for a green with a real chipping apron. The larger original Waterford Lakes and Eastwood lots are the better candidates."),
            faq("Does the pond setback shrink a green's usable size?", "It can, since the 10 ft waterbody line and any swale beside it come off the buildable footprint the same as they would for a lawn. Sizing the green after staking the setback avoids redesigning it midway through."),
        ],
        "sources": SRC,
    },
    "playground": {
        "title": "Playground Turf Installation in Alafaya, FL",
        "meta": "Playground turf for Alafaya backyards near Blanchard Park and UCF: shock pad sizing and pricing, checked September 2026.",
        "h1": "Backyard play turf for families near Blanchard Park",
        "lede": capsule(f"Budget {price('playground')} a square foot for playground turf, narrowing to {price('playground', True)} once the shock-pad thickness is picked; that hasn't shifted by ZIP code this year. Families here often already have a county playground nearby along the Little Econ Greenway, so a home install is usually about covering a swing set or a trampoline circle rather than building a full play yard from scratch."),
        "sections": [
            ("Sizing a shock pad for a backyard swing set, not a public park",
             f"<p>Blanchard Park and the Little Econ Greenway give Alafaya families public play space along the river, but a swing set or a trampoline at home still lands on whatever is under it in the owner's own yard, which on a lot from the 1990s build-out usually means bare dirt or thin, worn grass by the second summer. We size the shock pad to the equipment's actual fall height rather than a flat default thickness, since a taller swing set frame needs more cushioning underneath its arc than a low playhouse does, and that's a measurement we take on site rather than guess from a catalog listing.</p>"),
            ("Full sun near a pond and what that means for surface heat",
             f"<p>A lot of Alafaya's backyard play areas sit open to full sun on a lot that backs a retention pond with no mature tree canopy left standing after construction. Full Florida sun can push synthetic turf past 150°F at the surface, hot enough to matter for bare feet, so we talk through infill choice on these jobs more than on a shaded lot: a lighter-colored or cooling infill helps, and a hose rinse before an afternoon at the swing set drops the surface temperature fast. {post('coolest-artificial-grass-and-infill-for-florida', 'This comparison of infill options')} goes through what each one actually does.</p>"),
            ("Keeping play turf inside the pond setback",
             f"<p>A swing set placed too close to a Waterford Lakes or Eastwood pond can put its turf pad partly inside the state's 10 ft waterbody setback without anyone noticing until a permit question comes up. We stake that line before laying out play equipment on a pond lot, not after, since moving a swing set's footprint is a lot easier before the base goes in than after. {a('/laws/hoa-rules/', "A visible play structure")} is also more likely to draw an HOA look than turf alone, so worth mentioning if a submittal is needed.</p>"),
        ],
        "scenario": ("A worked example: a 180 sq ft play area under a swing set",
                     f"<p>Say a family's Eastwood backyard has a metal swing set with an 8 ft fall height needing a 180 sq ft turf pad around its perimeter. At {price('playground')} a square foot with a shock pad sized to that fall height, the job prices between {f'${180*10:,.0f}'} and {f'${180*25:,.0f}'}, typically closer to {f'${180*15:,.0f}'} for a pad rated to that height rather than a thinner residential-grade cushion. Because the yard gets full afternoon sun with no tree cover, we'd also talk through a lighter infill option before ordering material.</p>"),
        "faqs": [
            faq("What is the best playground turf option near me for a home swing set?", "The one sized to your equipment's actual fall height rather than a generic pad, since an 8 ft swing set frame needs more cushioning than a 4 ft playhouse. We measure that on site rather than assume a standard depth."),
            faq("Does full sun near a pond make backyard play turf too hot?", "It runs hotter than a shaded yard would, since there's no canopy to block afternoon sun. A lighter or cooling infill and a quick hose rinse before playtime keep the surface manageable."),
        ],
        "sources": SRC,
    },
    "pool": {
        "title": "Pool & Lanai Turf in Alafaya, FL – Screen Cages",
        "meta": "Turf for screened pool lanais on Alafaya's 1990s homes near UCF: drainage over concrete and pricing, checked September 2026.",
        "h1": "Turf inside Alafaya's screened pool cages",
        "lede": capsule(f"Pool-area turf isn't its own price tier; it rides the residential range, {price('residential')} a square foot, since the state doesn't carve out a separate category for a lanai. A large share of Alafaya's 1990s and early-2000s homes were built with a screened pool cage, and the concrete deck around that pool is exactly where sod has never had a chance."),
        "sections": [
            ("Why so many Alafaya pool decks never grew grass",
             "<p>Homes built through Waterford Lakes and Eastwood's main construction years commonly came with a screened lanai wrapped around the pool, and whatever strip of ground sits between the pool deck and the screen frame usually gets too much foot traffic and too little direct rain, since the screen roof sheds water away from that narrow band. What's there after twenty-plus years is often bare soil, weeds, or a thin remnant of sod that never filled in, not a lawn that's declining, more a lawn that was never really established.</p>"),
            ("Building turf on a concrete deck instead of soil",
             f"<p>Inside the cage, turf usually goes down over the existing concrete deck rather than excavated soil, which changes the base from crushed rock to a drainage underlay designed for hard surfaces, and changes the edges from nailed to glued, since there's no ground to anchor into at the screen frame's base. That underlay is what keeps the deck draining toward its original drain instead of pooling under the turf during a summer storm, which matters more inside a screen enclosure than outside one, since there's no way for rain to just run off the edge of a lanai the way it can off an open lawn.</p>"),
            ("Chemicals, screen frames and what shortens a pool-area lawn's life",
             f"<p>A pool deck's turf takes a different kind of abuse than a front yard's: chlorine splash, acid wash runoff during a resurface, and bare feet dripping pool water rather than rain. None of that is covered by {a('/laws/florida-hb-683/', "the state's turf standard")}, which is written around lawns and waterbodies, not pool chemistry, so keeping concentrated chemicals off the turf's edge and rinsing splash away before it dries into the fibers is on the homeowner more than the installer. {post('can-artificial-turf-melt', 'Reflected heat off glass')} is also worth checking on a screen enclosure with a west-facing house wall nearby, since a lanai traps heat differently than open yard does.</p>"),
        ],
        "scenario": ("A worked example: a 260 sq ft lanai strip around a pool",
                     f"<p>Say a 1990s Eastwood pool home has a 260 sq ft strip of bare, unusable ground between the pool deck and the screen frame. Priced in the residential range at {price('residential')} a square foot, glue-down turf over a drainage underlay for that strip runs between {f'${260*8:,.0f}'} and {f'${260*18:,.0f}'}, usually toward the upper half of that band because of the smaller area and the underlay and edge-gluing work a concrete deck needs. The result replaces a patch that's been bare dirt for years with a surface that actually drains toward the deck's existing drain.</p>"),
        "faqs": [
            faq("Can turf go over an existing Alafaya pool deck without removing the concrete?", "Yes. Turf installs directly over sound concrete with a drainage underlay underneath it and glued edges at the screen frame, since there's no soil there to nail into. The concrete itself doesn't need to come out first."),
            faq("Why did grass never grow on my screened lanai in the first place?", "A screen roof blocks enough direct rain and light that ordinary sod struggles to establish there even before foot traffic and pool splash are factored in. That's a lanai problem more than a species problem, and it's why the strip usually needs turf rather than a different grass."),
        ],
        "sources": SRC,
    },
    "repair": {
        "title": "Artificial Turf Repair in Alafaya, FL",
        "meta": "Turf repair in Alafaya, FL for storm-lifted seams, pond-lot drainage and rental turnovers, quoted after a look, September 2026.",
        "h1": "Fixing lifted seams and worn turf around Alafaya",
        "lede": capsule("Turf repair in Alafaya is quoted after we see photos or visit, since the cost depends on what's actually wrong rather than the size of the whole lawn. What we see most here traces back to a pond-adjacent drainage issue or the wear a rental yard takes between tenants, not a defect in the turf itself."),
        "sections": [
            ("What a pond-adjacent lawn does to a seam over time",
             f"<p>A yard graded toward a retention pond moves more water across its lowest seams during a heavy summer storm than an interior lot does, and if that seam wasn't bonded tightly enough at installation, years of that runoff finds the weak point eventually. What usually shows up first is a few inches of lifted edge right at the low corner nearest the water, not a seam failing all at once. Catching that early, before a whole panel pulls loose, is the difference between a small re-glue and pulling back several feet of turf to redo the bond properly.</p>"),
            ("Turnover damage on a landlord-owned Alafaya yard",
             f"<p>A rental duplex or townhome near UCF sees a different repair pattern than an owner-occupied home: a moving truck's tires cutting a rut near the driveway edge, a security deposit walkthrough that flags a corner a previous tenant's dog dug at, or infill that's gone thin in one high-traffic path to the door. None of that is usually a base problem, which is good news, since {svc('cleaning', 'a power-broom and infill top-up')} handles the cosmetic wear and a small patch handles a dug-at corner, without pulling the whole yard's turf. {post('does-homeowners-insurance-cover-artificial-turf', "Whether a specific incident is a claim")} is worth a quick look before paying for it directly.</p>"),
            ("When an HOA visibility rule matters for a repair",
             f"<p>A community with active architectural review, {city('avalon-park', 'Avalon Park')} to the south being one example, treats a repair differently than an open subdivision would, but here in Waterford Lakes, most repairs restore what was already approved and don't need a fresh submittal, since the material and footprint aren't changing. The exception is a repair that swaps the edge material, say from nailed turf to a paver border, which does change something visible from the street or a neighboring yard. Mentioning that kind of change up front avoids a conversation with the association after the work is already done.</p>"),
        ],
        "scenario": ("A worked example: a lifted corner on a pond-lot lawn",
                     f"<p>Say an 820 sq ft Waterford Lakes backyard installed a few years ago in the {price('residential')} range now has one corner near the pond where the turf has lifted about 4 ft along the low edge after a rainy summer. That's a seam and edge repair, not a rebuild, since the rest of the lawn is still bonded and draining the way it should. We'd want photos of the lifted section and the drainage direction around it before naming a number, since a corner that's lifting because of standing water needs a small grading fix along with the re-glue, not just fresh adhesive over the same problem.</p>"),
        "faqs": [
            faq("Why does turf near a pond lift more often than turf elsewhere in the yard?", "That edge carries more runoff during a storm than an interior seam does, so any weak spot in the original bond tends to show up there first. It's usually a localized fix, not a sign the whole lawn needs to come up."),
            faq("Will you repair turf a rental property's previous installer put in?", "Yes. The original crew doesn't need to still be in business for us to open a seam, patch a dug-at corner, or re-glue a lifted edge. We just need to see the base once we're into it to confirm nothing under the turf caused the problem."),
        ],
        "sources": SRC,
    },
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
