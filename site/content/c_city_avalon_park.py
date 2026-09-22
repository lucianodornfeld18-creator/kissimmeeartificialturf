# -*- coding: utf-8 -*-
"""Avalon Park, FL (tier 2): master-planned New Urbanism community in unincorporated east Orange County."""
from _helpers import page, capsule, sec, table, faq, ul, a, svc, city, post, src, ext, price
from _cityservice import cityservice_pages

SLUG = "avalon-park"

SRC = [
    ("Avalon Park Group — developer story", "https://avalonparkorlando.com/about/developer-story/"),
    ("Avalon Park, Florida — Wikipedia", "https://en.wikipedia.org/wiki/Avalon_Park,_Florida"),
    ("Era Grizzard — Avalon Park neighborhood profile", "https://blog.eragrizzard.com/hometalk/avalon-park-orlando-fl-neighborhood-profile"),
    ("HOA Bulletin Board — Avalon Park Property Owners Association", "https://www.hoabulletinboard.com/hoa/apalfl/about_hoa/"),
    ("Avalon Park Orlando — Property Owners Association", "https://avalonparkorlando.com/live/property-owners/"),
    ("Orange County — reclaimed water customer guide", "https://www.orangecountyfl.net/Portals/0/Library/Water-Garbage-Recycle/docs/Reclaimed_Water_Customer_Guide-CERT.pdf"),
    ("Orange County Code, Chapter 37, Municode Library — water, wastewater and reclaimed water service rules", "https://library.municode.com/fl/orange_county/codes/code_of_ordinances?nodeId=ORCOCO_CH37WAWA_ARTIORCOWAWAREWASERU_S37-1SHTI"),
    ("Florida Neighborhood Realty — Avalon Park Town Center", "https://www.floridaneighborhoodrealty.com/town-center-avalon-park-homes-sale/"),
    ("Orange County Code, Chapter 24, Municode Library", "https://library.municode.com/fl/orange_county/codes/code_of_ordinances?nodeId=PTIIORCOCO_CH24LABUOPSP"),
    ("Orange County Fast Track Online Services", "https://fasttrack.ocfl.net/OnlineServices/"),
    ("Orange County Property Appraiser — parcel search", "https://ocpafl.org/"),
    ("Orange County Utilities — watering restrictions", "https://www.orangecountyfl.net/watergarbagerecycling/wateringrestrictions.aspx"),
    ("St. Johns River Water Management District — Orange County", "https://www.sjrwmd.com/district-counties/orange-county/"),
    ("USDA NRCS — Official Series Description, Myakka series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/M/MYAKKA.html"),
    ("USDA NRCS — Official Series Description, Basinger series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/B/BASINGER.html"),
    "usda-wss", "dep-rule", "fs125572", "fs7203045",
]

# ============================================================== hub
HUB = page(
    "/areas/avalon-park/", "city",
    "Artificial Turf in Avalon Park, FL: Alley Lots & Porches",
    "Artificial turf for Avalon Park's alley-loaded lots and village ponds in unincorporated Orange County, FL, checked September 2026.",
    "Turf built for a front porch everyone on the block can see",
    capsule(f"Avalon Park is a planned village community in unincorporated Orange County, about 22 miles from our Kissimmee shop, built from 1998 onward around a walkable town center. Turf here prices the same as anywhere in the region, {price('residential')} a square foot this September. What changes is the lot: alley-loaded garages put the whole front yard on display, and a village pond often sits closer than a fence line would elsewhere."),
    "".join([
        sec("A town center built before most of the houses around it",
            f"<p>Avalon Park Group, founded by Beat Kahli in 1995, began building the 1,860-acre master plan in 1998, a good decade after most of the subdivisions elsewhere in east Orange County had already filled in. The Clock Tower went up in 2000 as the first anchor, Downtown I opened in 2002, and Downtown II followed in 2005 along Avalon Lake ({ext('https://avalonparkorlando.com/about/developer-story/', "the developer's own history")}). Rather than one big subdivision, the plan reads as a series of villages wrapped around that town center, with an estimated {ext('https://en.wikipedia.org/wiki/Avalon_Park,_Florida', '14,000-plus residents')} across roughly 3,400 single-family homes and just over 1,400 multi-family units once the plan built out.</p>"
            + f"<p>The signature move, uncommon anywhere else in our service area, is pushing garages onto rear alleys so the street sees a porch instead of a driveway. That single decision is why so much of what we quote in Avalon Park starts with a front-yard conversation rather than a backyard one; there's often no side yard to speak of, and the front lawn is the whole show.</p>"),
        table("Reading an Avalon Park lot before we quote it",
              ["Lot type", "Why it isn't an ordinary yard", "What we build instead"],
              [["Alley-loaded rowhouse or bungalow near the Town Center", "The front lawn is the only lawn, and it's what the whole street sees from a porch a few feet away", "A tidy, simple layout built to look right from the sidewalk on day one"],
               ["Village lot backing a pond or preserve buffer", "The state's 10 ft waterbody line and its swale exclusion cut into the yard before a fence line would", "Setback staked first, turf sized to whatever's left"],
               ["Later-phase village lot on a reclaimed-water line", "An existing reclaimed irrigation zone has to be capped at the valve, not just switched off", "We confirm the meter and cap the zone rather than assume it's already been done"],
               ["Narrow strip between a garage and the alley pavement", "Sits in view of alley traffic and neighbors' garages rather than tucked behind a house", "A width-matched run instead of leftover, unused ground"]],
              "Village layouts and dates per the sources below; every lot still gets walked before we quote it."),
        sec("Water, wetlands and the preserve wrapped around the villages",
            f"<p>About 240 acres of Avalon Park's original plan stayed wetland, another 400 acres became upland preserve, and roughly 250 acres went into the man-made lakes and ponds that sit at the center of most of its villages ({ext('https://blog.eragrizzard.com/hometalk/avalon-park-orlando-fl-neighborhood-profile', 'community acreage figures')}). That much water on a plan this size is exactly why the state's turf standard's pond setback and swale exclusion come up on more Avalon Park lots than on a typical subdivision built without a central lake in every village. Orange County places the community in the {ext('https://www.sjrwmd.com/district-counties/orange-county/', 'St. Johns River Water Management District')}, and its irrigation restriction runs on the county's usual seasonal calendar, tighter during daylight saving months than the rest of the year.</p>"
            + f"<p>Where a lot sits on a reclaimed-water line, county rule already prefers that supply over drinking water for irrigation once it's available ({ext('https://library.municode.com/fl/orange_county/codes/code_of_ordinances?nodeId=ORCOCO_CH37WAWA_ARTIORCOWAWAREWASERU_S37-1SHTI', 'Chapter 37')}; {ext('https://www.orangecountyfl.net/Portals/0/Library/Water-Garbage-Recycle/docs/Reclaimed_Water_Customer_Guide-CERT.pdf', "the county's reclaimed water guide")}), and Avalon Park's own town center has been marketed on exactly that feature ({ext('https://www.floridaneighborhoodrealty.com/town-center-avalon-park-homes-sale/', 'reclaimed irrigation as a listed amenity')}). None of that changes what happens once turf goes down: the state standard doesn't let a reclaimed line water synthetic grass any more than a potable one can, so that zone gets capped the same way. Underneath it all sits the fine, poorly drained flatwoods sand common to east Orange County, Myakka and Basinger among the named series, which is why the base recipe leans on washed rock rather than anything with fines in it.</p>"),
        sec("Permitting, and the POA layer that sits on top of it",
            f"<p>Avalon Park has never incorporated, so a turf job answers to the same office as the rest of unincorporated {a('/laws/permits/orange-county/', 'Orange County')} — Permitting Services and the Division of Building Safety at 407-836-5550, applications tracked through Fast Track Online Services, under a county landscape code that defines turf as living grass and has nothing written yet for a synthetic one. A quick pull on {ext('https://ocpafl.org/', "the property appraiser's site")} confirms that for any specific address before assuming it.</p>"
            + f"<p>What Orange County doesn't touch, the Avalon Park Property Owners Association does. Its governing declaration is recorded in the county's own public records ({ext('https://www.hoabulletinboard.com/hoa/apalfl/about_hoa/', 'Official Records Book 5593, Page 2234')}), and Leland Management runs its day-to-day architectural review from an office right on Tanja King Boulevard. We looked for a published clause naming sod, ground cover or synthetic turf specifically and didn't find one we could point to, so we're describing the review step here, not quoting a rule: expect a sample and a site plan to go in front of that committee before installation, the same as any other exterior change. {a('/laws/hoa-rules/', "What Florida law actually limits an HOA to")} still sets the outer boundary on what that committee can ask for.</p>"),
        sec("Why 'not visible from the street' means less here than elsewhere",
            f"<p>Florida law keeps an HOA from restricting anything a parcel's frontage doesn't show, and in most subdivisions that protects a fenced backyard from ever needing approval at all. Alley-loaded design flips that math: with the garage and driveway moved to the rear, a much larger share of an Avalon Park lot's usable ground sits in the front, in plain view from the sidewalk and the porch across the street, and the alley-side strip behind the house isn't fully hidden either. Practically, that means more of a typical Avalon Park yard falls inside the committee's reach than would in a community where the backyard is the private half of the lot.</p>"
            + "<p>Ask a neighbor a few doors down in Avalon Park how they'd judge the best artificial grass company near their own block, and the answer tends to start with the front lawn everyone walks past, not the price sheet.</p>"),
        "<!--AUTO:city-services-->",
    ]),
    faqs=[
        faq("Is Avalon Park its own municipality?", "No. It's an unincorporated community in Orange County, so permitting runs through the county's Permitting Services and Division of Building Safety rather than a city hall of its own."),
        faq("Does the Avalon Park POA have to approve turf before it goes in?", "Its architectural review committee reviews exterior changes generally, and we couldn't find a published rule naming turf specifically one way or the other. Submitting a sample and site plan ahead of ordering material is the safer route given that gap."),
        faq("Why does turf placement matter more in Avalon Park than in a typical subdivision?", "Because alley-loaded garages put most of the visible, judged part of the lot in front rather than behind the house. A front-yard installation here is effectively always visible from the street, which a backyard install elsewhere often isn't."),
        faq("Can I still water new turf if my lot has reclaimed irrigation?", "No. The state standard treats a reclaimed line the same as a potable one: neither can be used to irrigate synthetic turf, so that zone gets capped at installation regardless of which water supply used to feed it."),
        faq("How far are Avalon Park's ponds from where turf can go?", "The state sets a 10 ft line from the water's edge, plus the swale beside it, unless a seawall already separates the yard from the pond. Village lots built around a central lake often lose more of that back strip than a lot without one."),
    ],
    sources=SRC, city=SLUG, crumbs=[("Service areas", "/areas/")], crumb="Avalon Park",
    related=[("/areas/orange-county/", "Orange County: turf rules and yards"), ("/laws/permits/orange-county/", "Orange County turf permit rules"), ("/areas/alafaya/", "Turf in Alafaya"), ("/areas/lake-nona/", "Turf in Lake Nona"), ("/artificial-turf-cost/", "Turf cost tables for Central Florida")],
)

# ============================================================== local (city x service)
LOCAL = {
    "residential": {
        "title": "Artificial Grass Installation in Avalon Park, FL",
        "meta": "Artificial grass installation in Avalon Park, FL for alley-loaded front lawns and village pond lots, priced as of September 2026.",
        "h1": "Front-lawn turf for Avalon Park's alley-loaded houses",
        "lede": capsule(f"Installed residential turf costs the same in Avalon Park as it does anywhere in our service area: {price('residential')} a square foot, with most jobs settling near {price('residential', True)}. A lot of new owners here search for the best artificial turf installer near me only after they realize the front lawn, not the back, is the one everybody sees."),
        "sections": [
            ("A front lawn that has to look finished from the sidewalk",
             f"<p>Because Avalon Park's garages sit on the alley, the street-facing lawn is usually the only lawn a passerby ever sees, and it reads differently than a backyard would. Curves, cutouts and anything that looks unfinished stand out more here than on a lot where the front is just the approach to a driveway. We tend to steer toward a cleaner, simpler shape for a street-facing install for exactly that reason, since a plain, well-edged rectangle photographs better from a sidewalk than a busy one does, and it's also the layout {a('/laws/hoa-rules/', "an architectural committee")} has the least to ask about.</p>"
             f"<p>The porch itself changes the sightline too: most Avalon Park houses put the porch a few feet from the property line, which means whoever's sitting on it has a close, ongoing view of the lawn's edge quality in a way a homeowner further back from the street wouldn't notice as often.</p>"),
            ("What a village pond lot loses to the setback, and what it doesn't",
             f"<p>A meaningful share of Avalon Park's villages are built around a central lake, so a back lot line meeting water is common rather than an exception. We stake the state's 10 ft waterbody line and the swale beside it before laying out anything, since {a('/laws/florida-hb-683/', "that setback")} doesn't bend for a nicer view of the water. What's left over is usually still a workable lawn, just narrower along that one edge than the property line alone would suggest, and worth measuring in person rather than off a plat map.</p>"
             f"<p>On the villages built later in the plan, that same lot may also carry a reclaimed-water line, which gets capped at the valve exactly like a potable zone would, since {svc('residential', 'a synthetic lawn')} can't be watered through either supply once it's installed.</p>"),
            ("Getting a sample past the POA's architectural committee",
             f"<p>Every exterior change in Avalon Park, turf included, runs through the property owners association's architectural review before work starts, on top of whatever unincorporated {a('/laws/permits/orange-county/', "Orange County's")} own permitting requires. We haven't found a published clause that names synthetic turf specifically, which cuts both ways: nothing pre-approves it, but nothing bans it outright either. Bringing a physical turf sample, a simple site plan and a fiber and infill spec to that meeting tends to move faster than a verbal description alone, especially on a lot where the whole front yard is what the committee is being asked to picture.</p>"),
        ],
        "scenario": ("Running the numbers on a 480 sq ft Town Center front lawn",
                     f"<p>Take a 480 sq ft front lawn on an alley-loaded lot near Avalon Park's Town Center, a simple rectangle with no side yard to speak of since the garage sits off the alley behind the house. At {price('residential')} a square foot, that job prices between {f'${480*8:,.0f}'} and {f'${480*18:,.0f}'}, and a straightforward shape like this one usually lands near {f'${480*11:,.0f}'} to {f'${480*13:,.0f}'} rather than the top of the range. Because the whole lawn faces the street, we'd also budget a few extra days into the schedule for the POA's architectural review before ordering material, not after.</p>"),
        "faqs": [
            faq("Does a front-yard-only lawn cost more per square foot than a backyard?", "Not because it's in front; a smaller area of any shape prices toward the upper part of the range since a crew and equipment mobilize the same way for 400 sq ft as for 1,200. Simple front-yard rectangles common in Avalon Park often help offset that with less cutting and fewer curves."),
            faq("What happens if my lot doesn't have a real backyard at all?", "That's normal for an alley-loaded design. We plan the whole job around the front lawn and whatever narrow strip exists along the alley, rather than assuming a standard rear yard the way we would elsewhere."),
        ],
        "sources": SRC,
    },
    "pet": {
        "title": "Pet Turf for Avalon Park, FL Alley Lots",
        "meta": "Pet turf for Avalon Park's narrow alley-side yards in unincorporated Orange County, FL: layout, drainage and pricing, September 2026.",
        "h1": "Dog turf for the alley strip behind an Avalon Park house",
        "lede": capsule(f"Pet turf holds the same range across our whole service area, {price('pet')} a square foot, most jobs settling near {price('pet', True)}. In Avalon Park that turf usually goes into a narrow strip along the alley rather than an open backyard, since that's often the only fenced ground a dog actually gets."),
        "sections": [
            ("A dog run that's visible to more than just the household",
             f"<p>Because the alley runs behind a row of garages, a dog area built along it sits in view of neighbors backing out of their own garages and anyone walking the alley, not tucked away the way a fenced suburban backyard usually is. That visibility doesn't change the build, but it does change what looks acceptable: a clean, well-edged run reads better in that setting than a patchy one would, and it's worth asking whether {a('/laws/hoa-rules/', "the property owners association")} treats an alley-facing run any differently from a front lawn before assuming it doesn't need the same sample-and-plan submittal.</p>"),
            ("Sizing a run for the width Avalon Park actually gives you",
             "<p>An alley-loaded lot's usable side ground is often just the gap between the garage wall and the property line, sometimes only a handful of feet across, which is a real constraint on how a pet area gets laid out. Rather than force a bigger run than the space allows, we build to that actual width and lean on a denser infill and tighter perimeter fastening to make the narrow footprint hold up to daily use, since there's no room to spread wear across a wider area the way a big backyard dog run can.</p>"),
            ("Keeping infill and drainage working in a tight, shaded gap",
             f"<p>A narrow side strip between two structures often gets less direct sun and airflow than an open yard, which slows how fast a hose rinse dries and can make odor control matter more, not less, in that setting. Zeolite or a coated sand infill earns its keep here, and skipping the weed barrier under the turf still applies the same as anywhere else, since a barrier would hold moisture against the backing in a spot that already drains slower than open ground. {post('how-to-get-dog-urine-smell-out-of-artificial-turf', "This guide")} covers the rinse routine that keeps a tight run from smelling worse than a wide one.</p>"),
        ],
        "scenario": ("Running the numbers on a 130 sq ft alley-side dog strip",
                     f"<p>Take a 130 sq ft strip between a garage wall and the alley on a typical Avalon Park lot, about 6 ft wide and narrow the whole way down. At {price('pet')} a square foot for pet turf, that run prices between {f'${130*10:,.0f}'} and {f'${130*18:,.0f}'}, with a zeolite build usually landing near {f'${130*14:,.0f}'}. Given the shade from the garage wall on one side, we'd plan a coated sand or zeolite infill rather than the cheapest option, since a slower-drying strip benefits more from odor-control infill than an open, sunny yard would.</p>"),
        "faqs": [
            faq("Is a narrow alley strip enough space for a dog run?", "Yes, a run as narrow as five or six feet still works well for most dogs, though we build with denser infill and tighter edge fastening than we would on a wider run to help it hold up without room to spread the wear."),
            faq("Does an alley-facing dog run need the POA's approval too?", "Treat it the same as any other exterior change until told otherwise. We haven't found a published exception for alley-side areas in the association's rules, so a sample and plan submitted ahead of time is the safer assumption."),
        ],
        "sources": SRC,
    },
    "putting": {
        "title": "Backyard Putting Greens in Avalon Park, FL",
        "meta": "Backyard putting greens on Avalon Park's larger village lots in Orange County, FL: sizing and pricing, checked September 2026.",
        "h1": "Putting greens on Avalon Park's outer village lots",
        "lede": capsule(f"A putting green here prices the way it does everywhere we work, {price('putting')} a square foot with most builds around {price('putting', True)}. Searching for the best putting green installer near me in Avalon Park usually turns up the same answer: it depends on whether your particular lot has the depth for one."),
        "sections": [
            ("Why lot depth, not lot type, decides whether a green fits",
             f"<p>Avalon Park's alley-loaded design keeps most lots narrow but doesn't necessarily make them shallow, so the deciding factor for a green is usually how far the house sits from the rear property line rather than the neighborhood's layout in general. A lot backing open ground or a wider common area tends to have more room than one backing directly onto another alley or a tight village common. Since {svc('putting', 'a green')} needs both length for the putting surface and separate room for a fringe and chipping pad, we measure that depth before quoting rather than assuming a standard Avalon Park lot has it.</p>"),
            ("Building the contour without disturbing what the POA already approved",
             f"<p>A green's base gets shaped rather than simply graded flat, which on an already-landscaped Avalon Park lot means working carefully around whatever beds, edging or hardscape the architectural committee signed off on previously. We treat the existing approved landscape as a boundary to build within, not something to redo, so a green installation here typically leaves the rest of the yard's already-approved layout untouched while the contoured base goes in underneath the new turf.</p>"),
            ("What a pond-adjacent lot gives up for a green's layout",
             f"<p>On a village lot where the rear property line meets a pond, the state's waterbody setback comes off the buildable footprint before a green's shape gets drawn, the same as it would for a plain lawn. That usually means designing a shorter green with a tighter chipping area rather than the longer layout a deeper, non-waterfront lot could support. {post('artificial-turf-glossary', 'Stimp and nap direction')} matter enough on a green that we'd rather size it correctly within that smaller footprint than stretch it toward the setback line.</p>"),
        ],
        "scenario": ("A quick estimate for a 300 sq ft green on a deeper village lot",
                     f"<p>Consider a 300 sq ft green on one of Avalon Park's deeper village lots, away from the narrower Town Center rowhouses, with room for a two-cup layout and a small chipping pad. At {price('putting')} a square foot, that project runs between {f'${300*14:,.0f}'} and {f'${300*30:,.0f}'}, with the contouring work typically pushing it toward {price('putting', True)} rather than the entry end of the range. Most of that cost is in shaping the compacted base correctly, since a green with a flat, uncontoured base is a redo waiting to happen, not a shortcut.</p>"),
        "faqs": [
            faq("Do Avalon Park's alley-loaded lots ever have room for a putting green?", "Some do. Lot width is limited by the alley design, but depth varies more, and a lot backing open common ground rather than another alley often has enough room for a compact green with a fringe and chipping pad."),
            faq("Will installing a green disturb landscaping the POA already approved?", "We build the green's footprint to work around existing approved beds and edging rather than removing them, so the rest of an already-approved yard typically stays as it was."),
        ],
        "sources": SRC,
    },
    "playground": {
        "title": "Playground Turf for Avalon Park, FL Backyards",
        "meta": "Playground turf for Avalon Park backyards near Live Oak Park, Orange County, FL: shock pad sizing and cost, September 2026.",
        "h1": "Play-area turf behind an Avalon Park village home",
        "lede": capsule(f"Playground turf prices between {price('playground')} a square foot, narrowing to {price('playground', True)} once the shock pad is specified, no different in Avalon Park than anywhere else we install it. Between Live Oak Park and the smaller village greens, a lot of Avalon Park's play happens outside the home already, which shapes what a family actually needs in their own yard."),
        "sections": [
            ("Filling the gap between community parks and a home play set",
             f"<p>With a park inside most of Avalon Park's villages and a larger one, Live Oak Park, in Village 1, families here often use a home play area as the everyday, low-key option rather than the only place kids play ({ext('https://blog.eragrizzard.com/hometalk/avalon-park-orlando-fl-neighborhood-profile', 'Live Oak Park and village amenities')}). That changes the brief a little: instead of building out a full play yard, most of what we install is a shock pad sized to a single swing set, a trampoline, or a small climbing structure tucked into whatever yard space an alley-loaded lot actually has.</p>"),
            ("Sizing the shock pad correctly on a smaller footprint",
             f"<p>A narrower Avalon Park yard means less room to spread a play structure out, which makes getting the shock pad's thickness right more important, not less, since there's no extra buffer space to compensate for a pad that's thinner than the equipment's fall height calls for. We measure the specific equipment on site and size the pad to that number rather than installing a flat, one-size-fits-all thickness across every job.</p>"),
            ("Full sun on an alley-facing yard and what that means for heat",
             f"<p>A play area tucked against a garage wall on the alley side can trade tree shade for full afternoon sun, since Avalon Park's newer villages don't always have the mature canopy an older, larger lot elsewhere would. Surface temperatures on unshaded turf commonly reach 120 to 150°F in Florida summer sun, so we'll usually flag a lighter or cooling infill option on a yard like that rather than defaulting to standard silica. {post('is-artificial-turf-safe-for-kids-pfas-lead', 'This explainer')} covers infill safety questions that come up alongside the heat question.</p>"),
        ],
        "scenario": ("Estimating a 150 sq ft play pad by a garage wall",
                     f"<p>Consider a 150 sq ft play pad tucked against a garage wall for a swing set with a 6 ft fall height, on a lot with little tree cover. At {price('playground')} a square foot with the shock pad matched to that fall height, the job runs between {f'${150*10:,.0f}'} and {f'${150*25:,.0f}'}, typically closer to {f'${150*14:,.0f}'} for a pad rated correctly rather than a thinner default. Given the full sun on that wall, we'd also talk through a cooling infill option before finalizing the order.</p>"),
        "faqs": [
            faq("Do Avalon Park families need a full home play yard given the community's parks?", "Not usually a full one. Many jobs here are a shock pad sized to one piece of equipment rather than a large dedicated play area, since community parks cover the rest."),
            faq("Does an alley-facing play area need different infill than a shaded yard?", "It's worth considering a lighter or cooling infill if the spot gets full afternoon sun with no canopy, since surface temperatures run higher there than under mature trees."),
        ],
        "sources": SRC,
    },
    "pool": {
        "title": "Pool & Lanai Turf in Avalon Park, FL",
        "meta": "Turf for screened pool lanais on Avalon Park's village lots in Orange County, FL: install method and cost, September 2026.",
        "h1": "Lanai turf on Avalon Park's screened pool decks",
        "lede": capsule(f"Pool and lanai turf falls under the residential range here, {price('residential')} a square foot, since the state doesn't set a separate price category for a screen enclosure. On Avalon Park's smaller village lots, that lanai strip is often the only patch of ground with room for anything green at all."),
        "sections": [
            ("A small lot's pool cage carries more weight than a big one's",
             f"<p>On a larger, older lot elsewhere, a pool cage is one feature among several green spaces. On a tighter Avalon Park village lot, especially one with an alley-loaded garage eating into the rear footprint, the screened lanai can be most of the outdoor living space a household actually has. That raises the bar on how finished the turf strip around the pool deck needs to look, since it's doing double duty as both a pool surround and, in effect, the backyard.</p>"),
            ("Building over the deck rather than digging into a lot that has little ground to spare",
             f"<p>A small lot doesn't leave room to excavate a traditional base alongside the pool even if that were the plan, so the crew works with what's actually there: the concrete deck itself becomes the working surface, topped with a drainage underlay instead of compacted rock, with the perimeter bonded by adhesive at the screen frame rather than relying on nails driven into soil that isn't there to begin with. That approach fits the space Avalon Park's village lots actually offer, instead of requiring more of it.</p>"),
            ("Keeping a small lanai's turf from taking on more heat than it should",
             f"<p>A screen enclosure traps heat differently than open yard does, and on a lot with limited shade, reflected sun off a nearby window or a light-colored wall can add to what the turf already absorbs on its own. {post('can-artificial-turf-melt', 'Checking nearby glass for a low-E coating')} is worth doing before installation on any lanai, but especially on a compact village lot where the pool cage sits closer to the house wall than a larger property's would.</p>"),
        ],
        "scenario": ("Pricing a 190 sq ft strip around a village-lot pool",
                     f"<p>On a compact Avalon Park village lot, the lanai's whole contribution to the yard might be a 190 sq ft ring of bare ground squeezed between the pool deck and the screen frame. Because pool-area turf rides the residential price band rather than its own category, that ring costs between {f'${190*8:,.0f}'} and {f'${190*18:,.0f}'} at {price('residential')} a square foot, with the deck-mounted method and smaller footprint usually pushing the number toward the top half rather than the middle. For a household on a lot this size, that ring can end up doing more work as green space than the price tag alone would suggest.</p>"),
        "faqs": [
            faq("Can turf go directly over my Avalon Park lanai's existing concrete?", "Yes. It installs over sound concrete with a drainage underlay underneath and glued edges at the screen frame, without needing to remove the slab first."),
            faq("Is a lanai strip worth turfing if it's the only green space on a small lot?", "Often, yes, since it turns unused bare concrete-adjacent ground into usable space without needing more square footage than the lot already has."),
        ],
        "sources": SRC,
    },
    "repair": {
        "title": "Artificial Turf Repair in Avalon Park, FL",
        "meta": "Turf repair for Avalon Park's front lawns and alley strips in Orange County, FL, quoted after photos or a visit, September 2026.",
        "h1": "Repairing turf on Avalon Park's front-facing lawns",
        "lede": capsule("A repair in Avalon Park gets priced after we've seen photos or walked the yard, since the fix depends on what actually failed, not the lawn's total square footage. Because so much of what we install here faces the street, a repair also tends to get noticed faster than it might in a yard tucked behind a fence."),
        "sections": [
            ("Why a front-lawn seam gets reported sooner here",
             f"<p>A lifted seam or a thin, matted path in a backyard can go unnoticed for a season if nobody's back there to see it. On an Avalon Park front lawn a few feet from a public sidewalk and a porch, the same issue tends to get caught and called in faster, simply because more people, including the homeowner walking to the mailbox, pass it every day. That's a benefit more than a problem: small issues get fixed while they're still small repairs rather than turning into a bigger rebuild.</p>"),
            ("What changes when the repair also needs the POA's sign-off",
             f"<p>A repair that puts back exactly what was there before, same material, same footprint, generally doesn't call for a fresh look from {a('/laws/hoa-rules/', "the property owners association")}, and that holds even on a front lawn the whole street can see, since nothing about its appearance is actually changing. Where that logic breaks down is a repair that alters something on purpose, trading a nailed edge for a paver border, say, since that's a different look than what the committee approved the first time around. On a lot where the front yard carries all the visual weight, flagging a change like that ahead of time is worth the extra step.</p>"),
            ("Alley-strip repairs versus front-lawn repairs",
             f"<p>A narrow alley-side dog run or side strip takes a different kind of damage than a front lawn: infill migrating toward one low corner, or an edge lifting where it meets the garage's concrete apron, rather than the general wear a highly visible front lawn shows. {svc('cleaning', 'A power-broom and infill top-up')} handles the cosmetic wear on either one; a proper seam or edge repair is for anything that's actually lifted or opened, and the two aren't interchangeable fixes for the same problem.</p>"),
        ],
        "scenario": ("Looking at a lifted edge on a Town Center front lawn",
                     f"<p>Consider a 420 sq ft alley-loaded front lawn, installed a few years back in the {price('residential')} range, with about 3 ft of edge lifting where it meets the front walkway after a season of heavy foot traffic. That's an edge-bond repair, not a full re-lay, since the rest of the lawn is still flat and holding. We'd want to see photos of the lifted section and how it's anchored before quoting, since a walkway edge that keeps lifting sometimes needs a different fastening method at that one spot rather than just fresh adhesive over the same approach.</p>"),
        "faqs": [
            faq("Does a visible front-lawn repair need to go back through the POA?", "Only if it changes something visible, like the edge material or the overall shape. A like-for-like seam or edge repair that restores what was already there typically doesn't need a fresh submittal."),
            faq("Why do front-lawn issues in Avalon Park seem to get caught earlier?", "Simply because more people, including the homeowner, pass a front lawn daily compared with a backyard. That tends to mean smaller repairs rather than a problem that goes unnoticed for a season."),
        ],
        "sources": SRC,
    },
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
