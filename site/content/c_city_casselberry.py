# -*- coding: utf-8 -*-
"""Casselberry, FL (tier 2, Seminole County). Researched September 2026.
No dedicated permit sub-page exists on this site for Casselberry's own Land Development Code
(unlike Kissimmee, Orlando, etc.); we link the Seminole County permit page as the honest baseline
and name the city's own Building Division for a code-specific answer."""
from _helpers import page, capsule, sec, table, faq, a, svc, city, cs, post, src, ext, price
from _cityservice import cityservice_pages

SLUG = "casselberry"

CBLD = ("City of Casselberry — Building Division", "https://www.casselberry.org/668/Building-Division")
CUTIL = ("City of Casselberry — Utility Customer Service", "https://www.casselberry.org/74/Utility-Customer-Service")
CIRRIG = ("City of Casselberry — Irrigation Restrictions", "https://www.casselberry.org/836/Irrigation-Restrictions")
CHIST = ("City of Casselberry — History", "https://www.casselberry.org/33/History")
CSECRET = ("City of Casselberry — Secret Lake Park", "https://www.casselberry.org/303/Secret-Lake-Park")
HISTORIC_CAS = ("Historic Casselberry — History of Casselberry", "https://historiccasselberry.com/history-of-casselberry")
CENSUS_CAS = ("U.S. Census Bureau QuickFacts — Casselberry city, Florida", "https://www.census.gov/quickfacts/casselberrycityflorida")
SJRWMD_RESTRICT = ("St. Johns River Water Management District — watering restrictions", "https://www.sjrwmd.com/wateringrestrictions/")
PERMITS_SEM = "/laws/permits/seminole-county/"
HB683 = "/laws/florida-hb-683/"
HOA = "/laws/hoa-rules/"
COST = "/artificial-turf-cost/"

SRC = [CBLD, CUTIL, CIRRIG, CHIST, CSECRET, HISTORIC_CAS, CENSUS_CAS, SJRWMD_RESTRICT,
       "dep-rule", "fs125572", "fs7203045", "usda-wss"]

# ============================================================== hub
HUB = page(
    "/areas/casselberry/", "city",
    "Artificial Turf in Casselberry, FL (2026 Guide)",
    "Synthetic turf installation, permits, irrigation rules and lake setbacks for Casselberry, FL, a city built around more than 30 lakes. Checked Sept. 2026.",
    "Turf built for a city with more lake frontage than street frontage",
    capsule(f"Casselberry packs more than 30 lakes and ponds into just 4.6 square miles, roughly 27 miles from our Kissimmee base, so the state's 10-ft waterbody setback comes up more often here than almost anywhere else we work. We install, repair and clean synthetic lawns, pet turf and putting greens across the city at {price('residential')} per square foot as of September 2026."),
    "".join([
        sec("Turf work in Casselberry",
            f"<p>Casselberry is small in land area and dense in water: {ext(CSECRET[1], 'Secret Lake Park')} alone holds three connected lakes inside a 40-acre park, and the city counts more than 30 lakes and ponds overall. Most of the housing stock dates to the 1950s through the 1980s, ranch-style homes built up around {ext(CHIST[1], 'the Triplet Chain of Lakes')} that founder Hibbard Casselberry developed after the old US 17-92 highway opened the area to growth. Newer townhome and condo buildings have filled in gaps along that same US 17-92 corridor since.</p>"
            + f"<p>{svc('residential', 'A full lawn')}, {svc('pet', 'a fenced-yard dog run')}, {svc('putting', 'a backyard green')}, {svc('pool', 'turf around a pool cage')}: whichever one brings someone to us, the same question comes up almost every time, which is how close the lot actually sits to a lake and whether the state's setback needs staking before anything else gets measured, a question that comes up on a smaller share of jobs in neighboring {city('winter-springs', 'Winter Springs')} or {city('altamonte-springs', 'Altamonte Springs')}, where lakes cluster more than they blanket the whole map.</p>"),
        table("Casselberry yard types and what we do differently",
              ["Housing or lot type", "Where you'll find it", "What we build differently"],
              [["1950s–80s ranch homes", "Streets around Triplet Lake Drive and the older core", "Decades of oak growth mean checking the drip line before ordering turf"],
               ["Lakefront lots", "Lake Howell, the Triplet Lakes chain, Lake Kathryn, Secret Lake", "State's 10-ft setback staked at layout, seawall exception checked first"],
               ["Newer townhome infill", "Along the US 17-92 corridor", "Smaller footprints, often a courtyard or a strip rather than a full lawn"],
               ["Low-lying flatwoods lots away from any lake", "Interior streets between the city's lake clusters", "Base leans toward the fuller end of the state's rock-depth range for drainage"]],
              "Sourced from the city's own pages, USDA soil data and the Census Bureau, current as of September 2026."),
        sec("Permits and HOAs in Casselberry",
            f"<p>We haven't gone through Casselberry's own Land Development Code line by line the way we have for Kissimmee or Orlando's own permit pages, so the honest move here is a phone call: Community Development's Building Division answers permit questions at (407) 262-7700, option 5, out of its Triplet Lake Drive office. {a(PERMITS_SEM, 'The Seminole County permit page')} is the closest baseline we've actually researched, covering the unincorporated county's own process alongside the statewide floor beneath it, since {src('dep-rule', 'the state’s May 2026 rule')} keeps a city or county from banning or singling out a compliant lawn on a covered single-family lot, whatever a specific municipal code happens to say.</p>"
            + f"<p>A homeowners association answers to a different statute than either government office; {a(HOA, 'F.S. 720.3045')} protects only the turf a street or an adjacent lot genuinely can't see.</p>"),
        sec("Water: Casselberry's own utility and the St. Johns district",
            f"<p>Casselberry bills and delivers its own water rather than buying through a county authority. Its watering days track the {ext(SJRWMD_RESTRICT[1], 'St. Johns River Water Management District’s')} schedule: Wednesday and Saturday for odd-numbered addresses, Thursday and Sunday for even-numbered ones, Tuesday and Friday for non-residential accounts, and nothing at all between 10 in the morning and 4 in the afternoon ({ext(CIRRIG[1], 'the city’s current irrigation restrictions')}). Billing questions go to Utility Customer Service at (407) 262-7760 ({ext(CUTIL[1], 'the city’s utility contact page')}). A capped synthetic lawn steps outside that entire schedule, a requirement the state's rule puts on every covered yard regardless of who sends the water bill.</p>"),
        sec("What's under a Casselberry lawn",
            f"<p>Casselberry sits low relative to the ridge towns further west, in the same flatwoods sand family that covers most of Seminole County: Myakka, Immokalee, Basinger and Smyrna series, ground that holds onto summer rain far longer than a well-drained ridge lot would ({src('usda-wss', 'USDA Web Soil Survey')}). A city with this many lakes and ponds packed into 4.6 square miles is exactly the kind of low, flat terrain that soil profile describes, and it's the reason the base under a Casselberry lawn leans toward the fuller end of the state's two-to-four-inch washed-rock range rather than the shallow end. Unwashed fill with clay fines binds into a crust on this kind of ground faster than it would on a better-drained ridge lot, which is why the standard here never varies by neighborhood.</p>"),
        "<!--AUTO:city-services-->",
    ]),
    faqs=[
        faq("How do you pick the best artificial grass company near you in Casselberry?",
            "Start with how the crew handles a lake-adjacent lot, since a large share of Casselberry addresses sit within reach of the state's 10-foot setback. Past that, look for the basics any honest quote should show: a named base depth and material, infill spelled out by type, and drainage called out specifically for a lot this close to open water."),
        faq("Does Casselberry have its own written rule on synthetic turf?",
            "We can't point to one, though that's different from confirming there isn't one; we simply haven't gone through the city's Land Development Code page by page the way we did for a handful of other cities. Call the Building Division if a decision hinges on the answer. Either way, nothing Casselberry's code says can undercut the floor Florida set in May 2026."),
        faq("Does every lake in Casselberry trigger the same 10-foot setback?",
            "Yes. Florida's rule doesn't carve out an exception for a named lake like Lake Howell versus a smaller connected pond; a physical barrier, a seawall or bulkhead standing between the lot and the water, is the only thing that changes the distance requirement."),
        faq("Is Casselberry's water utility the same as Seminole County's?",
            "No. Casselberry bills and delivers its own water rather than buying through the county, though its watering-day schedule matches the St. Johns River Water Management District's regional restrictions that apply across most of the county."),
        faq("Are Casselberry's newer townhomes covered by the same turf rule as an older ranch lot?",
            "If a townhome is a single-family lot of an acre or less, yes, the same state standard and HOA-visibility statute apply. A unit inside a true condominium building instead runs through the building's own declaration and board."),
    ],
    sources=SRC, crumbs=[("Service areas", "/areas/")], crumb="Casselberry", city=SLUG,
    related=[("/areas/seminole-county/", "Artificial turf in Seminole County"), (PERMITS_SEM, "Seminole County permit rules for turf"),
             ("/areas/altamonte-springs/", "Turf in Altamonte Springs"), ("/areas/winter-springs/", "Turf in Winter Springs"), (COST, "Full turf cost guide")])

# ============================================================== local (6 services)
LOCAL = {
    "residential": {
        "title": "Artificial Grass Installation in Casselberry, FL",
        "meta": "Synthetic lawns for Casselberry's ranch homes and lake lots, with the state's 10-ft setback and flatwoods base explained. Checked Sept. 2026.",
        "h1": "A synthetic lawn built for Casselberry's ranch lots and lake edges",
        "lede": capsule(f"A residential conversion in Casselberry runs {price('residential')} per square foot installed as of September 2026, on a ranch lot near Triplet Lake Drive or a newer townhome off US 17-92. What changes the job is the lake count around a given address, not the price."),
        "sections": [
            ("Ranch homes built up around the Triplet Chain of Lakes",
             f"<p>Casselberry's oldest subdivisions sit around Triplet Lake Drive, developed after founder Hibbard Casselberry bought land surrounding the {ext(CHIST[1], 'Triplet Chain of Lakes')} and marketed it to retirees along the newly opened US 17-92. Ranch-style homes built between 1960 and 1985 still dominate that core, and decades of tree growth since then means a residential lawn conversion on one of these lots usually starts with locating every oak's drip line before a single measurement gets taken for turf.</p>"
             + f"<p>A yard shaped this long ago rarely has the flat, uninterrupted footprint a newer subdivision offers, which is part of why an accurate walk of the property matters more here than a satellite-photo estimate. {post('does-artificial-grass-increase-home-value-florida', 'Whether any of this actually helps resale value')} is a separate question worth a look before treating it as a given.</p>"),
            ("Why the base leans heavier on Casselberry's flatwoods sand",
             f"<p>Most of Casselberry sits on the same low, flatwoods soil family that covers much of Seminole County, Myakka, Immokalee, Basinger and Smyrna series, where the water table can rise within a few feet of the surface after a summer storm. A city built around more than 30 lakes and ponds is a visible clue to how flat and wet that underlying ground actually is. {a('/artificial-grass-installation/', 'A residential lawn')} here gets built toward the fuller end of the state's washed-rock depth range rather than the shallow end, since a thin base barely clears ground that's already close to saturated.</p>"
             "<p>That's a build decision, not a price change; the same published range applies whether the lot sits near a lake or three streets back from one.</p>"),
            ("A ranch lot and a US 17-92 townhome need different plans",
             f"<p>An older ranch home near {city('casselberry', 'Casselberry')}'s lake core usually has a full backyard and an established fence line to work with. A newer townhome along the US 17-92 corridor is a different project: smaller footprint, often a courtyard or a narrow side strip rather than a full lawn, and depending on the building, an association process that looks more like {a(HOA, 'Florida’s HOA-visibility statute')} for a true single-family townhome, or a condo board's own rules for a unit inside a shared building.</p>"
             "<p>Knowing which category applies before pricing a job changes the approval conversation more than it changes the installation itself.</p>"),
        ],
        "scenario": ("Say your Casselberry backyard is 800 square feet",
                     "<p>Say you have an 800 sq ft backyard behind a 1968 ranch home a few streets from Lake Concord, with two mature oaks along the back fence whose combined canopy covers about 120 sq ft. Staying outside both drip lines without an arborist letter leaves roughly 680 sq ft to convert. "
                     f"At {price('residential')} per square foot, that's about ${680*8:,}–${680*18:,} installed, or {price('residential', typical=True)} a square foot for a typical build, closer to ${680*10:,}–${680*16:,}. "
                     "Because this lot sits on flatwoods sand well away from the lake itself, the base still runs toward four inches of washed rock rather than two, even though no waterbody setback applies here. Grading falls toward the yard's existing low corner, the same direction water already moved before any rock went down.</p>"),
        "faqs": [
            faq("Do all of Casselberry's ranch homes have the same soil under them?",
                "Mostly, yes. The flatwoods sand series common across Seminole County, Myakka, Immokalee, Basinger and Smyrna, covers most of Casselberry regardless of which decade a given subdivision was built, since the terrain itself hasn't changed even as the houses on it have aged."),
            faq("Does a townhome near US 17-92 need HOA approval the same way a ranch home does?",
                f"Only if it's a true single-family townhome governed by a homeowners association; a unit inside a condominium building instead answers to that building's own declaration and board, the same distinction that applies to newer condo stock in {city('oviedo', 'Oviedo')} or {city('winter-park', 'Winter Park')}."),
        ],
        "sources": SRC,
    },
    "pet": {
        "title": "Pet Turf and Dog Runs in Casselberry, FL",
        "meta": "Fast-draining pet turf for Casselberry's fenced ranch yards, sized for the city's flatwoods water table and lake-adjacent setbacks. Checked 2026.",
        "h1": "Dog runs built for Casselberry's older fenced yards",
        "lede": capsule(f"Pet turf in Casselberry runs {price('pet')} per square foot as of September 2026, fitted to the fenced backyards that came standard with the city's 1950s-through-1980s ranch subdivisions. A run near any of Casselberry's 30-plus lakes still needs the same 10-ft setback as a full lawn."),
        "sections": [
            ("Established fences make an easy start for a dog run",
             "<p>A Casselberry ranch home built during the city's main growth decades almost always came with a fenced backyard, since that was the standard lot style of the era, and a dog run built inside that existing fence line saves the cost of adding new fencing altogether. What varies from yard to yard is less the fence than the ground underneath it, since decades of settling and, in some cases, past flooding from a nearby lake can leave the soil in an older yard less even than a newer lot's would be.</p>"
             + f"<p>A quick walk of the fenced area before quoting catches most of that variation before it becomes a surprise mid-install. Pet turf itself differs from a standard lawn product in a few specific ways, which {post('pet-turf-vs-regular-artificial-grass', 'this post')} lays out.</p>"),
            ("Flatwoods drainage matters more for a concentrated dog run",
             f"<p>A dog run puts far more urine and rinse water onto a small patch of ground than a full lawn ever spreads across its own footprint, and on Casselberry's low, lake-dotted flatwoods sand, with its seasonally high water table, that concentration matters more than it would on drier ground. A crew building a run here compacts the fuller four inches of washed, open-graded rock instead of stopping at two, and leaves out the weed fabric a residential lawn might otherwise get, since a fabric layer under a pet area would hold liquid at the surface rather than letting it work down into the rock.</p>"
             "<p>None of that changes the published price per square foot; it changes how much rock a crew delivers for a run this size.</p>"),
            ("Keeping a run back from Lake Howell or the Triplet Lakes",
             f"<p>Casselberry dog owners sometimes want a run built right along the bank for the view, but a pet area gets no exception from the state's water rule that a full lawn wouldn't also need: 10 feet is 10 feet, and only an existing seawall or bulkhead shortens it. {svc('pet', 'Fencing a run to that line')} first, instead of measuring from the property boundary, means the layout never has to shrink after the fact, and a gentle grade near the bank keeps waste and rinse water moving away from the shoreline rather than toward it during a storm.</p>"),
        ],
        "scenario": ("A 12x18 dog run behind a fenced Casselberry yard",
                     "<p>Say you have a 12x18 ft dog run, 216 sq ft, along the back fence of a 1972 ranch home two streets from Secret Lake Park. "
                     f"At {price('pet')} per square foot, that run runs roughly ${216*10:,}–${216*18:,} installed, or about ${216*12:,}–${216*16:,} for a typical build with silica or zeolite infill for odor control. "
                     "Because the lot sits on Casselberry's typical flatwoods sand, the base goes in at four inches rather than two, which adds a bit to the rock delivered but doesn't change the square-foot price. Skipping the weed barrier under this run, standard for a pet area, keeps waste and rinse water draining through the base instead of pooling on a fabric layer.</p>"),
        "faqs": [
            faq("Can a dog run sit right up against Lake Howell?",
                "No closer than 10 feet to the water, the same distance a full lawn would need, unless the yard already has a seawall between it and the lake. Marking that boundary before the run's fence goes up beats moving a finished run back later."),
            faq("Does Casselberry's high water table make pet turf smell worse than elsewhere?",
                "Not by itself. Base depth and infill choice matter more: a fuller rock base and a regularly rinsed silica or zeolite infill manage odor about the same regardless of how close the water table sits to the surface."),
        ],
        "sources": SRC,
    },
    "putting": {
        "title": "Backyard Putting Greens in Casselberry, FL",
        "meta": "Putting greens for Casselberry's older, larger lake-lot yards, staked to the state's 10-ft setback before shaping begins. Checked Sept. 2026.",
        "h1": "Putting greens for Casselberry's roomier lake-adjacent lots",
        "lede": capsule(f"A backyard putting green in Casselberry runs {price('putting')} per square foot as of September 2026. The best-suited lots tend to be older, larger parcels near Lake Howell or the Triplet Lakes chain, where the state's 10-ft waterbody setback gets staked before any contour is shaped."),
        "sections": [
            ("Staking the setback on a Triplet Lakes-adjacent lot",
             f"<p>A putting green's tiers and cupped sections need more continuous, undisturbed ground than a flat lawn does, which makes a lot backing onto {ext(CSECRET[1], 'the Triplet Lakes chain')} or Lake Howell both an appealing and a restricted place to build one. The state's setback keeps turf at least 10 feet from the water's ordinary or mean high line unless a seawall or bulkhead already stands between the yard and the lake, and that line gets staked at layout, before ordering any material, so the green's footprint is designed around what's actually buildable.</p>"
             + f"<p>A lot along Casselberry's lake chain often has more usable depth than the setback first suggests once that strip is actually measured out, the same measuring-first approach that matters on a lake lot in {city('maitland', 'Maitland')} or anywhere else water borders a yard.</p>"),
            ("Building a green's base on flatwoods sand",
             f"<p>Casselberry's flatwoods sand holds more water near the surface than a ridge lot's soil would, which means a putting green's subbase here needs firmer compaction and a bit more drainage attention than the same green would on better-drained ground. That doesn't rule out a green on this soil; it changes how carefully a crew grades each tier so water sheds off a low break rather than pooling at the bottom of a slope after a summer storm.</p>"
             + f"<p>The contour work itself, cupping and shaping the surface, doesn't change between soil types; what changes is how much margin the base needs before those shapes go in. {post('artificial-turf-glossary', 'A short glossary of putting-green terms')} helps when comparing two quotes that describe the same build differently.</p>"),
            ("Why an older ranch lot has more room than a newer townhome",
             f"<p>A 1960s or 1970s ranch lot near Casselberry's lake core typically has a deeper backyard than a newer townhome built along the US 17-92 corridor, simply because lot sizes shrank as the city filled in over the decades. A full green with a fringe fits comfortably on the older lot style; a townhome yard usually has room only for {svc('putting', 'a compact chipping mat or a small practice section')} instead, which is a realistic substitute rather than a compromise for a tighter footprint.</p>"),
        ],
        "scenario": ("A 280 sq ft green near Lake Howell",
                     "<p>Say you have a 280 sq ft putting surface with an 80 sq ft fringe planned for a backyard two lots back from Lake Howell. Staking the 10-foot setback shows the buildable area starts a little further from the water than the fence line suggests, but the full 360 sq ft footprint still fits comfortably inside it. "
                     f"At {price('putting')} per square foot for the green itself, that's ${280*14:,}–${280*30:,}, with the fringe priced closer to standard residential turf. "
                     "Because the lot sits on typical Casselberry flatwoods sand, the crew compacts the subbase a little more deliberately than it would on drier ground, so a shaped break at the low end of the green sheds water instead of holding it after the next storm.</p>"),
        "faqs": [
            faq("Do all of Casselberry's lakes require the same setback for a putting green?",
                "Yes. A green gets no different treatment than any other turf on the property; whether the water is a named lake like Lake Kathryn or a smaller connected pond, the same 10-foot line applies unless a seawall or bulkhead already stands between the lot and the water."),
            faq("Is a full putting green realistic on a Casselberry townhome lot?",
                "Usually not a full-size one. Townhome yards along the US 17-92 corridor tend to be narrower than the city's older ranch lots, so a compact chipping section or a small fringe area is the more realistic fit for that footprint."),
        ],
        "sources": SRC,
    },
    "playground": {
        "title": "Playground Turf in Casselberry, FL",
        "meta": "Cushioned playground turf for Casselberry's family neighborhoods near Secret Lake Park, sized to the equipment's fall height. Checked Sept. 2026.",
        "h1": "Play-area turf for Casselberry's park-adjacent neighborhoods",
        "lede": capsule(f"Casselberry's older lakeside ranch neighborhoods and its newer townhome infill along US 17-92 both send us playground turf requests, at {price('playground')} per square foot as of September 2026. The city's population climbed to 30,135 in the Census Bureau's latest estimate, and young families show up in both housing types."),
        "sections": [
            ("A growing city built around its parks",
             f"<p>Casselberry's population reached 30,135 in the Census Bureau's 2019–2023 American Community Survey estimate, up from 28,794 at the 2020 Census ({ext(CENSUS_CAS[1], 'the Bureau’s own figures')}). A lot of that growth has landed in the newer townhome infill along US 17-92, where a private backyard is often smaller than what an older ranch lot near {ext(CSECRET[1], 'Secret Lake Park')} offers, which is part of why a compact play area request looks different from one neighborhood to the next.</p>"
             + f"<p>{a('/playground-turf/', 'Playground turf')} sized to a specific footprint, rather than assumed from a standard yard, fits both neighborhood types without over- or under-building the base.</p>"),
            ("Why a Casselberry play pad's base gets extra drainage attention",
             f"<p>A shock pad has one job under a swing set or climbing structure: cushion a fall the way the equipment's rated fall height calls for, and that only works if water moves through the pad and the base beneath it instead of pooling at the surface. Casselberry's flatwoods sand holds water closer to the surface, longer, than a ridge lot's soil would, which is the wrong condition for a surface a child might land on right after a storm. A crew here builds the rock base under a play area to the fuller end of the state's depth range for exactly that reason, with less margin for shortcuts than an open lawn might get away with.</p>"
             + f"<p>A play area that stays soggy after rain isn't just unpleasant to use; it's a safety surface behaving differently than its rating assumes, which is reason enough to get the base right from the first pass. Heat is the other factor worth planning for on an open play surface, covered in {post('how-hot-does-artificial-turf-get-in-florida', 'this post')}.</p>"),
            ("A smaller play footprint for newer townhome yards",
             f"<p>A townhome along the US 17-92 corridor typically has less open yard than an older Casselberry ranch lot, which usually means a play area here is sized closer to a single swing set or a small climbing structure than a full playset. That smaller footprint doesn't change the per-square-foot price or how the pad gets matched to the equipment's fall rating; it just means the crew is building for a tighter space than a ranch-lot job would need.</p>"),
        ],
        "scenario": ("A 9x12 play area on a Casselberry townhome lot",
                     "<p>Say you have a 9x12 ft play area, 108 sq ft, planned for a small climbing structure in the fenced yard of a newer townhome off US 17-92. "
                     f"A build like this typically totals somewhere between ${108*10:,} and ${108*19:,}, working out to {price('playground', typical=True)} per square foot for a pad-included job inside the published {price('playground')} range. "
                     "The pad itself gets matched to whatever fall height the structure's manufacturer specifies, not a generic thickness, and this particular lot has no lake setback or oak canopy to plan around, which keeps the job about as simple as a Casselberry play area gets. A footprint this size is typical for the townhome corridor, where the yard itself sets the practical ceiling more than any rule does.</p>"),
        "faqs": [
            faq("How much has Casselberry grown recently?",
                "The Census Bureau's 2019–2023 estimate put the population at 30,135, up from 28,794 at the 2020 Census, growth that's landed mostly in newer townhome development along the US 17-92 corridor rather than in the city's older lake-adjacent neighborhoods."),
            faq("Does Casselberry's high water table change how a play area's pad performs?",
                "Not if the base underneath is built for it. A shock pad rated for a given fall height cushions the same regardless of soil type; what changes on this ground is how much care the rock base gets during grading, since it starts out holding more water than a ridge lot's soil would."),
        ],
        "sources": SRC,
    },
    "pool": {
        "title": "Pool and Lanai Turf in Casselberry, FL",
        "meta": "Turf for Casselberry pool cages and lanais, built for the screen enclosures common on the city's 1960s–80s ranch lots. Checked Sept. 2026.",
        "h1": "Pool-deck turf for Casselberry's ranch-era screen cages",
        "lede": capsule(f"Turf around a pool or inside a lanai in Casselberry runs {price('residential')} per square foot as of September 2026. Most requests come from the screen-enclosed pool cages that came standard with the city's 1960s-through-1980s ranch homes, where sod along the deck rarely holds up under the enclosure's shade."),
        "sections": [
            ("Why ranch-era pool cages struggle to grow grass",
             "<p>A screen-enclosed lanai built during Casselberry's main growth decades usually leaves a narrow strip of ground between the pool deck and the enclosure's frame, shaded for most of the day and walked constantly, which is a combination sod rarely survives for long. Turf laid over that strip needs a drainage underlay where it meets the existing concrete deck and adhesive-set edges instead of nails, since there's no soil at that specific point to anchor into.</p>"
             "<p>The rest of the enclosure, if any open ground remains outside the deck itself, can still use a standard compacted rock base the way an open yard would.</p>"),
            ("A narrower cage means more careful seam work, not a different product",
             f"<p>An older Casselberry ranch home's pool cage often runs narrower than a newer enclosure would, since screen rooms from that era were built to a smaller standard footprint. {a('/pool-turf/', 'Pool and lanai turf')} in a tight strip like that takes more careful seaming to avoid a visible cut line in a small space where every inch is visible from the pool itself, but it doesn't call for a different product than a wider enclosure would use.</p>"
             + f"<p>Measuring the exact strip width before ordering material matters more here than on an open lawn, where a small miscalculation is easier to absorb. A pool deck also concentrates reflected sun in a way an open lawn doesn't, a heat question {post('can-artificial-turf-melt', 'covered here')}.</p>"),
            ("A pool deck near the water still respects the lake setback",
             f"<p>A handful of Casselberry pool cages sit close enough to Lake Howell or one of the Triplet Lakes that the state's 10-foot waterbody setback comes into play even for a small deck strip, unless a seawall already separates the property from the water. Staking that line before finalizing a pool-deck layout on a lakefront lot avoids planning turf for a strip that has to be trimmed back once the setback is confirmed.</p>"),
        ],
        "scenario": ("A 4x30 ft strip inside a ranch home's pool cage",
                     "<p>Say you have a 4x30 ft strip of turf planned for one side of a screened pool cage on a 1975 ranch home, 120 sq ft total, where grass never filled in under the enclosure's shade. "
                     f"At {price('residential')} per square foot, that's roughly ${120*8:,}–${120*18:,} installed, or {price('residential', typical=True)} a square foot for a typical build, closer to ${120*10:,}–${120*16:,}. "
                     "Because the strip runs along an existing concrete deck, the quote includes a drainage underlay and adhesive-set edges rather than a standard rock base. This particular lot sits several streets back from the nearest lake, so the state's waterbody setback doesn't factor into the layout at all.</p>"),
        "faqs": [
            faq("Can turf go inside a narrow ranch-era pool cage in Casselberry?",
                "Yes. A narrower enclosure just means more careful seam placement to avoid a visible cut line in a small space; the turf product and the drainage underlay under it are the same as they'd be in a wider cage."),
            faq("Does a pool deck near Lake Howell need the same setback as an open lawn?",
                "Yes, if the deck sits within 10 feet of the water's ordinary or mean high line and no seawall separates the two. That distance is worth confirming before finalizing a layout on any lakefront pool cage."),
        ],
        "sources": SRC,
    },
    "repair": {
        "title": "Turf Repair in Casselberry, FL",
        "meta": "Turf repair for Casselberry lawns: lake-edge erosion checks, flatwoods settling and irrigation-head fixes. Quoted after photos or a site visit.",
        "h1": "Fixing turf that's aged on Casselberry's lake-heavy ground",
        "lede": capsule("Turf repair in Casselberry gets a number after photos or a short visit, not a phone quote, since an eroded lake-edge strip and a slowly settling low spot can look alike from a few feet away but need different fixes. Two causes come up here more than most: wave-driven erosion along a setback strip with no seawall, and a base that never fully compacted on the city's low, wet ground."),
        "sections": [
            ("A dip that keeps returning near the water",
             f"<p>Ground inside the setback strip along a Casselberry pond or lake edge can erode a little faster than the rest of a yard, especially where there's no seawall absorbing wave action from wind or passing boats. A repair that reopens in roughly the same spot along that edge, rather than somewhere new each time, usually points to the location itself rather than a one-time installation problem, since that strip takes on water-driven movement the rest of the lawn's base never has to handle.</p>"
             + f"<p>Recognizing that pattern before quoting a fix changes whether the repair addresses the actual cause or just the visible symptom, and it's worth ruling out storm damage specifically, which {post('artificial-turf-hurricane-flooding', 'this post')} covers on its own.</p>"),
            ("A low spot that traces back to the water table, not a root",
             "<p>A dip that keeps reappearing in the same spot on a Casselberry lawn doesn't always point to erosion or a tree; on this city's low, flatwoods ground, a section of base that never fully compacted during the original install can settle gradually over a few rainy seasons instead of failing all at once. That kind of settling shows up as a shallow, broad depression rather than a narrow ridge, and it tends to hold a puddle a little longer after a storm than the rest of the yard does before the underlying problem becomes obvious.</p>"
             "<p>Confirming that a low spot is a compaction issue, and not something else working against the base, is what decides whether the fix is a straightforward rebuild of that one section or a longer look at what's happening underneath it.</p>"),
            ("A quick call beats guessing on anything near the water",
             f"<p>Most repairs never touch anything a city office cares about, but reworking grade within reach of a lake edge or a drainage swale is the exception worth checking on first. Casselberry's Building Division fields that kind of question at (407) 262-7700, option 5, and since we haven't gone through this city's own code with the same depth we gave a handful of others, that call is worth more than anything we'd guess here. {a(PERMITS_SEM, 'The Seminole County page')} is what we actually researched, along with the state floor sitting underneath it regardless of which office ends up handling a specific address.</p>"),
        ],
        "scenario": ("A settling low spot on an older Casselberry lawn",
                     "<p>Say a shallow, roughly three-foot-wide depression has developed near the middle of a lawn on a 1974 ranch home several streets back from any lake, holding a puddle for most of a day after a hard rain where the rest of the yard clears within hours. The affected area runs somewhere around 12 to 15 sq ft, small enough that a full-yard base rebuild isn't on the table. A number here waits on a short visit, since the fix depends on how deep the compaction problem actually goes: sometimes it's pulling back that one section and repacking it correctly, other times water has been finding its way into a wider area than the surface dip alone suggests. Either way, the patched section gets matched to the surrounding turf's grain and infill so it doesn't stand out once it's finished.</p>"),
        "faqs": [
            faq("How urgent is a low spot that holds water after rain?",
                "If it holds a puddle noticeably longer than the rest of the yard after a normal rain, it's worth scheduling before the next heavy storm enlarges the affected area. A shallow depression that stays dry between storms usually isn't urgent."),
            faq("Does Casselberry require a permit to regrade a small section of an existing lawn?",
                "Usually not for a patch this size, but we haven't gone through the city's code closely enough to promise that for every scope, especially near a lake edge. The Building Division can confirm faster than a guess would."),
        ],
        "sources": SRC,
    },
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
