# -*- coding: utf-8 -*-
"""Longwood, FL (tier 2). Local research checked September 2026; see SRC for every source used.
County-level permitting, water-management-district and soil facts are reused from
site/content/c_permits.py (Seminole County page) and site/content/c_counties.py (Seminole County hub) --
same underlying facts and URLs already verified there, new sentences written for this module."""
from _data import CITIES
from _helpers import page, capsule, sec, table, faq, a, svc, city, cs, post, src, ext, price
from _cityservice import cityservice_pages

SLUG = "longwood"
C = CITIES[SLUG]

LONGWOOD_BUILDING = ("City of Longwood -- Permitting and Inspections", "https://www.longwoodfl.org/169/Permitting-and-Inspections")
LONGWOOD_WATER = ("City of Longwood -- Water Restrictions & Conservation", "https://www.longwoodfl.org/291/Water-Restrictions-Conservation")
SEMINOLE_WATERING = ("Seminole County -- watering restrictions", "https://www.seminolecountyfl.gov/departments-services/environmental-services/water-conservation/watering-restrictions")
LONGWOOD_HISTORIC = ("City of Longwood -- Historic District", "https://www.longwoodfl.org/322/Historic-District")
BIG_TREE_PARK = ("Seminole County -- Big Tree Park", "https://www.seminolecountyfl.gov/locations/Big-Tree-Park.stml")
SWEETWATER_OAKS = ("Sweetwater Oaks -- neighborhood", "https://www.sweetwateroak.org/neighborhood/")
WEKIVA_FACT_SHEET = ("Seminole County -- Wekiva River Area Fact Sheet", "https://www.seminolecountyfl.gov/docs/default-source/pdf/wekivariverareafactsheetjuly2025ada.pdf")
SEM_PA = ("Seminole County Property Appraiser -- parcel search", "https://www.scpafl.org/")

SRC = [LONGWOOD_BUILDING, LONGWOOD_WATER, SEMINOLE_WATERING, LONGWOOD_HISTORIC, BIG_TREE_PARK, SWEETWATER_OAKS,
       WEKIVA_FACT_SHEET, SEM_PA, "dep-rule", "fs125572", "fs7203045", "usda-wss", "census-acs"]


def nb(slug, label=None):
    return (CITIES[slug]["route"], label or f"Turf in {CITIES[slug]['name']}")


# ============================================================== hub
HUB_BODY = "".join([
    sec("Turf in a city that runs its own building department",
        "<p>Longwood incorporated in 1878, well before most of the subdivisions around it existed, and that history is the reason a turf job here answers to a city Building Division rather than to Seminole County's. The Community Development Department's Building Division works out of 174 West Church Avenue, takes permit questions at 407-260-3486, and files applications through the city's own SmartGov portal instead of the county's Accela-based system. We don't keep a page here that reads Longwood's municipal code section by section the way we do for the county offices in our service area, so the honest answer is to call before booking a crew, the same as you would anywhere else.</p>"
        + f"<p>A handful of Longwood-addressed streets, mostly toward Wekiva Springs Road, actually sit in unincorporated Seminole County rather than inside the city limits. For those addresses, {a('/laws/permits/seminole-county/', 'our Seminole County permit page')} and a different Building Division apply, not the office on Church Avenue. Either way, {src('dep-rule', 'the Florida turf standard')} treats both offices the same: a compliant lawn on a single-family lot of an acre or less can't be turned down outright, a local permeability demand can't run tighter than 10 inches an hour, and a waterbody buffer can't ask more of turf than it already asks of grass.</p>"),
    sec("Longwood yard types and what we do differently",
        "<p>Four lot types repeat often enough around Longwood that they change how a bid gets written before a crew ever measures anything.</p>"
        + table("Longwood yard types and what we do differently",
                ["Yard type", "Where it sits", "What changes for turf"],
                [["Historic district bungalow lots", "Near State Road 434 and County Road 427", "Irregular shapes and mature oaks often mean a design-review step on top of the city permit"],
                 ["Sweetwater Oaks and other Wekiva-area lots", "West of downtown, off Wekiva Springs Road", "Heavy oak canopy pulls the buildable area in from the drip line before square footage is final"],
                 ["Established ranch subdivisions", "East and south of the historic core", "Straightforward base work, but a full irrigation head count matters before anything gets capped"],
                 ["Lots backing the Little Wekiva or a neighborhood lake", "Scattered through the city and the pockets around it", "The state's 10-ft waterbody setback applies unless a seawall already separates yard from water"]],
                "Every lot still gets the same washed-rock base and the same published price range; what changes is access, canopy and the setback math.")),
    sec("Water, the district schedule and what capping changes",
        f"<p>Longwood runs its own water utility rather than buying service from a neighboring city, and the utility's own conservation page points residents to {ext(SEMINOLE_WATERING[1], 'the Seminole County watering-restrictions page')} for the current schedule: odd addresses water Wednesday and Saturday, even addresses Thursday and Sunday, nothing between 10 a.m. and 4 p.m., under the St. Johns River Water Management District's rules for the county. Questions about a specific address go to the city's Public Works line at 407-260-3470 rather than the district directly.</p>"
        + f"<p>None of that schedule reaches a synthetic lawn once its heads are capped, since {src('dep-rule', 'the state standard')} bars an in-ground system from watering turf regardless of which utility bills the property. A hose rinse takes over from there, on whatever day the yard actually needs it rather than the two the district allows for grass.</p>"),
    sec("Big Tree Park, the historic district and a canopy older than the town",
        f"<p>{ext(BIG_TREE_PARK[1], 'Big Tree Park')}, on General Hutchison Parkway, is where Seminole County has kept the legacy of \"The Senator\" since Senator M.O. Overstreet donated the cypress and the land around it in the 1920s, with President Calvin Coolidge dedicating the park in 1929. The Senator itself, once judged around 3,500 years old, burned in a 2012 fire; a roughly 2,000-year-old bald cypress nicknamed Lady Liberty still stands nearby, next to a young clone called The Phoenix. It's an unusual amount of continuity for a city its size, and it says something about how long this ground has held large trees before any subdivision arrived.</p>"
        + f"<p>Longwood's own {ext(LONGWOOD_HISTORIC[1], 'historic district')} covers roughly 190 acres and 37 contributing structures, listed on the National Register of Historic Places since October 1990 and anchored by buildings as old as the 1872 Inside-Outside House and the 1879 Christ Episcopal Church. Census figures put the city at a little over 16,000 residents ({src('census-acs', 'Census Bureau data')}), a number that's grown steadily around that historic core rather than replacing it with new subdivisions the way some neighboring towns have.</p>"),
    sec("Sweetwater Oaks, the Wekiva basin and the drip-line rule",
        f"<p>{ext(SWEETWATER_OAKS[1], 'Sweetwater Oaks')}, platted in 1971 and built out through the 1980s along Wekiva Springs Road, carries roughly 1,400 homes under a canopy of mature oak and pine between Wekiwa Springs State Park and Lake Lotus Park. It's the kind of lot where {src('dep-rule', 'the drip-line rule')} comes up on nearly every quote rather than the occasional one, since turf can't go inside a live oak's root spread on that property or an adjacent one without a certified arborist's letter.</p>"
        + f"<p>West and northwest of the city, unincorporated pockets fall inside Florida's Wekiva River Protection Area, where new development answers to its own tree-preservation and density rules on top of anything a building permit covers ({ext(WEKIVA_FACT_SHEET[1], 'the Seminole County Wekiva River Area fact sheet')}). That layer governs new construction, not a turf swap on an existing lawn, but it's worth knowing which side of the line a specific parcel falls on before assuming either way.</p>"),
    "<!--AUTO:city-services-->",
])

HUB_FAQS = [
    faq("Does the City of Longwood have its own rule for synthetic turf?",
        "Not one we could find published. The city's Land Development Code doesn't name synthetic or artificial turf, so a project here meets ordinary exterior-permit rules plus the state's May 19, 2026 turf standard, not a Longwood-specific ordinance. Call the Building Division at 407-260-3486 to confirm for a specific address."),
    faq("How do you find the best artificial turf installer near you in Longwood?",
        "Ask three things before signing: whether the base is washed crushed rock or crushed concrete rather than fill with fines in it, whether the quote names infill type and rate, and whether the crew already plans around any oak drip line on the lot without being asked first."),
    faq("Are Sweetwater Oaks and other Wekiva-area neighborhoods inside Longwood's city limits?",
        "Not always. Several streets that carry a Longwood mailing address, especially near Wekiva Springs Road, sit in unincorporated Seminole County instead, which changes which Building Division and which permit page actually applies to that parcel."),
    faq("Does turf near the Little Wekiva or a neighborhood pond need a bigger setback?",
        "Florida's rule keeps turf at least 10 feet back from a pond, lake or canal's normal water line, and the only thing that shortens that distance is an existing seawall or bulkhead standing between the lawn and the water. Longwood hasn't published a stricter number of its own for that setback."),
    faq("What does the historic district's design review mean for a turf application?",
        "It's a separate step from the city's building permit, not a replacement for it. A home inside the roughly 190-acre district can face its own expectations for anything visible from the street, so a design-review question is worth raising alongside the permit call, not instead of it."),
]

HUB = page("/areas/longwood/", "city",
           "Artificial Turf Installation in Longwood, FL (2026)",
           "Synthetic turf installed and repaired in Longwood, FL, from the historic district to Sweetwater Oaks, at $8-$18 a square foot. Checked September 2026.",
           "Artificial turf across Longwood",
           capsule(f"Kissimmee Artificial Turf installs and repairs synthetic lawns in Longwood, an incorporated Seminole County city built around a 190-acre historic district, at {price('residential')} a square foot as of September 2026. Mature oak canopy from Sweetwater Oaks to the old downtown core means a quote here often starts with a drip-line check before a tape measure comes out."),
           HUB_BODY, faqs=HUB_FAQS, sources=SRC, city=SLUG,
           crumbs=[("Service areas", "/areas/")], crumb="Longwood",
           related=[("/areas/seminole-county/", "Artificial turf in Seminole County"),
                    ("/laws/permits/seminole-county/", "Seminole County permit rules for turf"),
                    nb("altamonte-springs", "Turf in Altamonte Springs"),
                    nb("casselberry", "Turf in Casselberry"),
                    ("/artificial-turf-cost/", "Full turf cost guide")])

# ============================================================== LOCAL
LOCAL = {
    "residential": {
        "title": "Artificial Grass Installation in Longwood, FL",
        "meta": "Synthetic lawn installation in Longwood, FL: the city's own Building Division, historic-district lots and oak canopy, priced $8-$18 a sq ft, checked September 2026.",
        "h1": "Installing artificial grass in Longwood",
        "lede": capsule(f"Artificial grass installed in Longwood runs {price('residential')} a square foot, typically {price('residential', True)}, as of September 2026. Many of the city's older lots sit inside or near the 190-acre historic district, where a builder-grade sod strip usually gives way to a base built from washed crushed rock rather than whatever fill happens to already be there."),
        "sections": [
            ("Longwood's own permit office, not the county's",
             f"<p>Because Longwood has run its own government since 1878, a lawn conversion inside city limits answers to the Community Development Department's Building Division, reachable at 407-260-3486 from an office at 174 West Church Avenue, with applications filed through the city's SmartGov portal rather than a county system. We don't maintain a page that walks through Longwood's own code section by section the way we do for the six county offices nearby, so the honest step is a phone call before scheduling anything, the same as it would be anywhere else.</p>"
             + f"<p>A number of Longwood-addressed streets, particularly toward Wekiva Springs Road, actually sit in unincorporated Seminole County instead, where {a('/laws/permits/seminole-county/', 'a different permit page and Building Division')} apply. A quick parcel search on the {ext(SEM_PA[1], SEM_PA[0])} settles which office actually has a given address before a call gets made to the wrong one.</p>"),
            ("What the historic district changes about a quote",
             f"<p>Longwood's historic district covers roughly 190 acres and has stood on the National Register of Historic Places since October 1990, anchored by buildings as old as the 1872 Inside-Outside House and the 1885 Bradlee-McIntyre House. None of that changes {src('dep-rule', 'the state turf material rule')} directly, since the rule governs composition and drainage, not architectural review. What it adds in practice is a second conversation beyond the city building permit: a home inside the district's boundary, roughly around State Road 434 and County Road 427, can carry its own expectations for anything visible from the street, layered on top of whatever {a('/laws/hoa-rules/', 'the HOA visibility statute')} might add a few blocks over.</p>"),
            ("Sizing a lot that's rarely a clean rectangle",
             f"<p>Longwood's older streets were platted well before modern subdivision standards, so irregular lot shapes and decades-old landscaping are common in a way a newer {city('winter-springs', 'Winter Springs')} or {city('apopka', 'Apopka')} subdivision doesn't have to work around. A quote here usually starts with a walk of the property rather than a satellite measurement, since a mature oak, an old well cap or a curved driveway can shrink the buildable area well below what the lot lines alone suggest. That same walk is when a crew flags anything inside a tree's drip line, since {post('artificial-turf-near-live-oaks-and-palms', 'turf that close to a live oak')} needs a certified arborist's letter before it goes in. The base and product side of the job otherwise matches {svc('residential', 'our residential installation write-up')} step for step; only the lot itself changes in Longwood.</p>"),
        ],
        "scenario": ("Say you have a quarter-acre lot near the old town core",
                     f"<p>Say you have a 1,400 sq ft front and side yard around a bungalow a few streets from the historic district, most of it thin St. Augustine struggling under two mature live oaks. At {price('residential')} a square foot, a full conversion runs $11,200 to $25,200, and at the more typical {price('residential', True)}, most quotes land between $14,000 and $22,400. Keeping turf outside both drip lines usually trims the buildable area by a few hundred square feet, which moves the total more than it moves the per-foot number. The irrigation heads that used to reach that lawn get capped rather than removed, since an in-ground system can't legally water the new surface either way, and a hose takes over the rinsing a hot afternoon calls for.</p>"),
        "faqs": [
            faq("Does Longwood require a permit for a residential turf conversion?",
                "The city hasn't published a specific answer for synthetic turf, so the Building Division treats it as ordinary exterior work until told otherwise. Call 407-260-3486 before scheduling a crew, especially on a lot that backs onto a swale or a shared drainage easement."),
            faq("Is my Longwood-addressed home actually inside the city limits?",
                "Not necessarily. Several streets with a Longwood mailing address, particularly near Wekiva Springs Road, sit in unincorporated Seminole County, which changes which Building Division and which permit page apply to that specific parcel."),
            faq("Do older Longwood lots need a survey before a quote?",
                "Not for the turf itself, but a property line that's shifted from decades of fence and landscaping changes is common enough on the city's oldest streets that having one on hand speeds up an accurate measurement."),
        ],
        "sources": SRC,
    },
    "pet": {
        "title": "Longwood Pet Turf and Dog Run Installation",
        "meta": "Pet turf and dog runs in Longwood, FL, built for Sweetwater Oaks and Wekiva-area oak canopy, priced $10-$18 a sq ft. Checked September 2026.",
        "h1": "Pet turf and dog runs built for Longwood yards",
        "lede": capsule(f"Pet turf in Longwood runs {price('pet')} a square foot, typically {price('pet', True)}, as of September 2026. Sweetwater Oaks and the other Wekiva-area subdivisions carry enough mature oak canopy that a dog run's layout often answers to a drip line before it answers to the fence line."),
        "sections": [
            ("Sweetwater Oaks and a canopy that runs the layout",
             f"<p>{ext(SWEETWATER_OAKS[1], 'Sweetwater Oaks')}, platted in 1971 and built out through the 1980s along Wekiva Springs Road, sits under mature oak and pine on roughly 1,400 lots between Wekiwa Springs State Park and Lake Lotus Park. A dog run planned for one of those backyards usually gets drawn around the canopy first and the fence second, since {src('dep-rule', 'the drip-line rule')} keeps turf out from under a live oak's root spread on that lot or the one next door without a certified arborist's letter.</p>"),
            ("Why pet turf skips the weed barrier here",
             f"<p>A plain residential lawn often gets a fabric layer between the compacted rock and the turf backing; a dog run skips it, since fabric traps urine at the surface instead of letting it filter down through the base the way the infill is designed to handle. On an oak-shaded Longwood lot where the ground underneath already drains slower than an open, sunny yard, that distinction matters more than it would on a bare, full-sun run with nothing overhead competing for drainage. The infill and backing choices follow the same rules {svc('pet', 'we cover for pet turf generally')}; a shaded Longwood run just applies them under more canopy than most.</p>"),
            ("Fencing, gates and a run that doesn't double as a mud strip",
             f"<p>Longwood's established neighborhoods, many built out by the 1980s, tend toward older wood or chain-link fencing rather than the vinyl common in newer {city('winter-springs', 'Winter Springs')} subdivisions, and a gate that's shifted over the decades can leave an odd-shaped strip along the fence line that turns to mud faster than the rest of the yard. That strip is usually the first place a dog wears a path anyway, which makes it a reasonable place to start a pet-turf conversion even on a lot too shaded for a full lawn swap.</p>"),
        ],
        "scenario": ("Say you have a fenced run along a shaded property line",
                     f"<p>Say you have a 300 sq ft run along the side fence of a Sweetwater-area lot, shaded most of the day by a live oak two lots over. At {price('pet')} a square foot, that run costs $3,000 to $5,400, and at the more typical {price('pet', True)}, most quotes fall between $3,600 and $4,800. Because the run sits close enough to the neighbor's oak to raise a drip-line question, the crew checks that boundary before finalizing the layout rather than after, which can pull the usable footprint in by a foot or two along that edge. Coated silica sand or zeolite goes in as infill either way, never rubber, since {a('/laws/florida-hb-683/', 'the state rule')} reserves synthetic infill for playground equipment.</p>"),
        "faqs": [
            faq("Does a dog run in Longwood need its own permit, separate from a full lawn?",
                "Nothing published treats pet turf differently from any other synthetic-turf project for permit purposes, so the same call to the Building Division at 407-260-3486 applies regardless of how much of the yard is being converted."),
            faq("Can pet turf go under a Sweetwater Oaks oak without an arborist letter?",
                "Not if it sits inside that tree's drip line. The state's rule applies the same way to a small dog run as it does to a full lawn, so a certified arborist's sign-off is the only way around the setback rather than a shortcut past it."),
        ],
        "sources": SRC,
    },
    "putting": {
        "title": "Backyard Putting Greens, Longwood FL",
        "meta": "Backyard putting greens in Longwood, FL, on established Seminole County lots, priced $14-$30 a sq ft. No irrigation needed year-round. Checked September 2026.",
        "h1": "Backyard putting greens for Longwood lots",
        "lede": capsule(f"A backyard putting green in Longwood runs {price('putting')} a square foot, typically {price('putting', True)}, as of September 2026. A contoured green never needs irrigation in the first place, which means it sits entirely outside the watering-day schedule that governs the rest of a Longwood yard, inside city limits or in one of the unincorporated pockets around it."),
        "sections": [
            ("A green that never touches the watering schedule",
             f"<p>Longwood's own water utility follows {ext(SEMINOLE_WATERING[1], 'the Seminole County odd-and-even schedule')}: odd addresses Wednesday and Saturday, even addresses Thursday and Sunday, nothing between 10 a.m. and 4 p.m. A putting green was never part of that math to begin with, since synthetic turf on a contoured green needs a hose rinse for dust and pollen, not a sprinkler zone, so the household's watering days keep applying to whatever lawn surrounds it rather than to the green itself.</p>"),
            ("Grading a contour into a lot platted decades ago",
             "<p>A number of Longwood's established subdivisions were graded for drainage long before anyone planned a putting green on the lot, which means the yard's existing high and low points often become the starting contour rather than something built from scratch. A green tucked into a natural swale in the corner of an older yard can borrow that existing fall for a subtle break, while a flatter section closer to the house usually needs its own shaped subbase to get any roll at all.</p>"),
            ("Fringe, cups and a lawn built around a much older canopy",
             f"<p>On a lot with a mature oak within reach of where a green would sit, {src('dep-rule', 'the drip-line rule')} shapes the layout before the contour does, since the fringe and the green itself both count as turf under that setback. A crew planning a green near {city('casselberry')}-style established canopy, or anywhere else in Longwood with decades-old trees, checks the drip line first and designs the hole placement and fringe width around whatever space is left. Contour shaping and cup placement work the same everywhere; {svc('putting', 'the general putting-green guide')} has the fringe and turf-pile specifics this page doesn't repeat.</p>"),
        ],
        "scenario": ("Say you have a corner of the backyard for a green",
                     f"<p>Say you have a 480 sq ft green with fringe planned for the back corner of an established Longwood lot, far enough from the house to avoid the low-E glass on a rear sliding door. At {price('putting')} a square foot, that runs $6,720 to $14,400, and at the more typical {price('putting', True)}, most quotes land between $8,640 and $12,000. A single cup and a gentle two-tier break keep the shaping simple, and because the green sits well clear of any drip line on this lot, the full 480 sq ft stays buildable rather than shrinking once a tree canopy gets factored in.</p>"),
        "faqs": [
            faq("Does a putting green in Longwood need irrigation heads capped like a lawn does?",
                "Only if heads already exist under where the green will sit. A green typically replaces grass that was already being watered, so any head in that footprint gets capped the same way it would for a full lawn conversion, per the state's turf standard."),
            faq("Can a putting green go inside Longwood's historic district?",
                "Nothing published treats a putting green differently from any other synthetic-turf project inside the district's roughly 190 acres, so the same design-review question that applies to a full lawn applies here if the green would be visible from the street."),
            faq("Do Longwood's older lots have enough flat space for a green?",
                "Often yes, since many were platted with a rear lawn deep enough for one, but a lot heavy with mature oak canopy may only offer a smaller, shadier footprint than a newer subdivision would."),
        ],
        "sources": SRC,
    },
    "playground": {
        "title": "Playground Turf Near Longwood's Big Tree Park",
        "meta": "Cushioned playground turf for Longwood, FL backyards, priced $10-$25 a sq ft, sized to fall height near Big Tree Park's own play area. Checked Sept. 2026.",
        "h1": "Playground turf for Longwood families",
        "lede": capsule(f"Playground turf in Longwood runs {price('playground')} a square foot, typically {price('playground', True)}, as of September 2026. Seminole County's own Big Tree Park, a short drive from downtown, already pairs a shaded play structure with a bonded surface, which sets a reasonable bar for what a backyard version should feel like underfoot."),
        "sections": [
            ("What a county park next door gets right",
             f"<p>{ext(BIG_TREE_PARK[1], 'Big Tree Park')}, home to the cypress once known as The Senator and now to a younger tree called The Phoenix, pairs its play structure with ground-level components and a bonded rubber surface rather than bare mulch. A backyard play area can't use rubber infill across an open lawn, since {src('dep-rule', 'the state rule')} limits synthetic infill to the footprint directly under playground equipment, but the same idea, a surface engineered for a fall height rather than left to whatever ground was already there, carries over directly.</p>"),
            ("Sizing the pad to the swing set, not the yard",
             f"<p>A shock pad under playground turf gets specified to the equipment's fall height, which means a taller swing set or climbing structure needs a thicker pad than a simple slide does, on the same square footage. Getting that number from the equipment's own manufacturer specification sheet before ordering material avoids the two most common mistakes: a pad too thin for the height it's under, or a pad sized for the tallest piece applied everywhere when only one corner of the layout actually needs it. Fall-height math and infill limits are covered in full in {svc('playground', 'our playground turf guide')}; the Longwood-specific part is mostly the shade overhead.</p>"),
            ("Building around a canopy families already use for shade",
             f"<p>Longwood's tree canopy, the same feature that shapes {city('altamonte-springs', 'nearby')} subdivisions' oak-heavy lots, does double duty for a backyard play area: existing shade keeps a play surface cooler than it would run in full sun, which matters given that unshaded turf commonly reaches 120 to 150°F in direct summer light. Where a play structure sits close enough to a tree to raise a drip-line question, the same certified-arborist rule that applies to a lawn conversion applies here too.</p>"),
        ],
        "scenario": ("Say you have a swing set going in near the patio",
                     f"<p>Say you have a 260 sq ft play area planned around a swing set with an 8-foot fall height, in a partly shaded corner of the backyard. At {price('playground')} a square foot, that runs $2,600 to $6,500, and at the more typical {price('playground', True)}, most quotes land between $3,120 and $4,940, with the shock pad sized to that 8-foot height rather than a standard default. Partial shade from an existing tree keeps the surface noticeably cooler on a summer afternoon than the same layout would run in open sun, though a hose rinse still helps before barefoot play on the hottest days.</p>"),
        "faqs": [
            faq("Can rubber infill go under a Longwood backyard play structure?",
                "Yes, but only inside the footprint of the equipment itself. The state's rule reserves rubber and other synthetic infill for that specific area; the rest of the yard still uses silica sand, coated sand or zeolite."),
            faq("Does playground turf near Big Tree Park's example need a specific pad thickness?",
                "There's no county standard for a backyard project; the pad thickness follows the equipment manufacturer's stated fall height, which varies by structure rather than by location in Longwood."),
        ],
        "sources": SRC,
    },
    "pool": {
        "title": "Pool and Lanai Turf in Longwood, FL",
        "meta": "Turf around Longwood pool cages and lanais, priced with the $8-$18 residential range, built for flatwoods sand and screened decks. Checked September 2026.",
        "h1": "Turf around Longwood pool cages and lanais",
        "lede": capsule(f"Turf around a pool cage or lanai in Longwood runs the same {price('residential')} residential range as of September 2026. Fine, seasonally wet flatwoods sand sits under most of the city, which is exactly why the base under a pool-deck strip matters more here than the product brochure ever does."),
        "sections": [
            ("Flatwoods sand under a screened deck",
             f"<p>Seminole County's own soil data classes most of Longwood on the same Myakka, Immokalee, Basinger and Smyrna fine sands that cover the rest of the county's flatwoods ({src('usda-wss', 'USDA Web Soil Survey')}), ground with a water table that can sit within a few feet of the surface after a summer storm. That's the same kind of low, damp ground that let a 3,500-year-old cypress take root at nearby Big Tree Park, and it's why a turf strip against a pool cage needs a drainage underlay where it meets the deck rather than a thin bed of sand pressed against the concrete. {svc('pool', 'Our pool-area turf page')} goes through the backing and drainage-underlay choices in more depth than this page needs to repeat.</p>"),
            ("Where the ten-foot setback meets a screen enclosure",
             f"<p>A handful of Longwood lots back onto the Little Wekiva River or a neighborhood lake close enough that a pool cage's turf border brushes up against {src('dep-rule', 'the state-mandated 10-foot waterbody setback')}, which applies unless a seawall or bulkhead already separates the yard from the water. On a pool-cage lot, that setback usually eats into the outer strip of lawn beyond the screen rather than anything inside the enclosure itself, so it rarely changes what goes down against the pool deck.</p>"),
            ("Low-E glass on a lanai's own sliding doors",
             f"<p>A screened lanai often faces west or south to catch afternoon light, which is exactly the orientation where low-emissivity glass can reflect enough concentrated sun to soften turf several feet away, since {post('can-artificial-turf-melt', 'polyethylene blades start to give')} around 175 to 200°F under that kind of focused heat. Checking a lanai's own sliding-door glass before installation, not just the house's front windows, catches a problem a homeowner in {city('oviedo', 'Oviedo')} or Longwood alike might not think to look for on their own.</p>"),
        ],
        "scenario": ("Say you have a narrow strip inside the screen",
                     f"<p>Say you have a 220 sq ft strip of turf planned along both sides of a screened pool deck, replacing sod that never filled in under the enclosure's shade. At {price('residential')} a square foot, that runs $1,760 to $3,960, and at the more typical {price('residential', True)}, most quotes land between $2,200 and $3,520. Because the strip sits on concrete rather than soil at its inner edge, it takes a drainage underlay and an adhesive-set border there instead of the nailed perimeter used on open ground, which is a labor difference more than a material one.</p>"),
        "faqs": [
            faq("Does pool-area turf in Longwood cost more than a regular lawn?",
                "It's priced from the same residential range, since the turf and base materials don't change; what can add labor time is a drainage underlay at the concrete transition and working inside a screen enclosure's tighter access."),
            faq("Can turf go all the way to the edge of a Longwood lake lot's pool cage?",
                "Only if a seawall or bulkhead separates the yard from the water. Without one, the state's 10-foot setback from the ordinary water line still applies, even where a screen enclosure sits close to that line."),
        ],
        "sources": SRC,
    },
    "repair": {
        "title": "Artificial Turf Repair Serving Longwood, FL",
        "meta": "Artificial turf repair in Longwood, FL: seams, edges and drainage fixes on established lots, quoted after a site visit. Checked September 2026.",
        "h1": "Fixing artificial turf in Longwood",
        "lede": capsule("Turf repair in Longwood is quoted after photos or a site visit, not a flat rate, because a lifted seam on a 1980s ranch-subdivision lawn and a storm-loosened edge on a historic-district lot call for two different fixes. As of September 2026, the most common calls involve a driveway-edge seam, a low spot that holds water, and infill gone thin after years of Central Florida sun."),
        "sections": [
            ("Repairing turf on some of the county's older installs",
             f"<p>Longwood's housing stock, much of it built out by the 1980s well before {a('/laws/florida-hb-683/', 'the current state turf standard')} existed, means a fair share of the turf a repair call turns up here predates the rule's material and anchoring requirements entirely. A repair on one of those older lawns sometimes means matching infill and backing to a product that's no longer sold, which is a different problem than a straightforward seam re-bond on a newer install. {svc('repair', 'Our general turf-repair page')} lists the most common failure types; Longwood's older stock just makes a few of them more likely.</p>"),
            ("Septic lids and drip lines on a repair visit",
             f"<p>A repair crew working an older Longwood lot checks for two things a newer install would already have documented: where a septic tank's pump-out lid sits, since {src('dep-rule', 'the state rule')} requires that access stay reachable, and whether any nearby oak has grown enough since installation to put more of the yard inside its drip line than it once did. Both checks take a few minutes and matter more on a lawn that's been in the ground for a decade than on one installed last year.</p>"),
            ("Storm damage after a summer system passes through",
             f"<p>Central Florida's June-through-September storm season is when most repair calls come in, since wind and standing water are exactly what a turf edge's anchoring is built to withstand, and a section that was under-anchored or bonded over a damp base tends to show it after the season's first hard system rather than on a calm day. {post('does-homeowners-insurance-cover-artificial-turf', 'whether a homeowners policy covers that kind of damage')} is a separate question worth asking before assuming a repair is an out-of-pocket cost either way.</p>"),
        ],
        "scenario": ("Say a corner lifted after last month's storm",
                     "<p>Say you have a 15-foot run of turf where it meets a paver patio on an established Longwood lot, and the edge lifted a few inches after a hard afternoon storm pushed water underneath it. A repair visit checks whether the original bond failed at the concrete transition or whether the base underneath settled unevenly, since those two causes call for different fixes: a re-bonded edge in the first case, or pulling back a short section to correct the grade in the second. Either way, the quote follows what the visit finds rather than a number given over the phone, since the same symptom can point to two different jobs underneath it.</p>"),
        "faqs": [
            faq("Why can't Longwood turf repair be quoted over the phone?",
                "Because the same visible problem, a lifted edge or a soggy spot, can come from a bad bond, a settled base, or a drainage issue underneath, and those three fixes take different time and material. A photo or a site visit tells a technician which one applies before a number gets given."),
            faq("Does an older Longwood lawn need different infill for a repair than a new one?",
                "Often yes. A lawn installed years ago may use an infill type or backing weight that's since been discontinued, so a repair sometimes means finding the closest current match rather than the exact original product."),
        ],
        "sources": SRC,
    },
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
