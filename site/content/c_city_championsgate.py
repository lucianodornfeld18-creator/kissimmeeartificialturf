# -*- coding: utf-8 -*-
"""ChampionsGate: unincorporated golf-resort community straddling the Osceola-Polk line.
Research checked September 2026; sources below."""
from _helpers import page, capsule, sec, table, faq, a, svc, city, county, cs, post, src, ext, price
from _cityservice import cityservice_pages

SLUG = "championsgate"

SRC = [
    "dep-rule", "fs125572", "hb683", "fs7203045", "toho-days", "usda-wss",
    ("Osceola County Property Appraiser -- parcel search", "https://www.property-appraiser.org/"),
    ("Polk County Property Appraiser -- parcel search", "https://www.polkflpa.gov/"),
    ("ChampionsGate Community Development District -- governance", "https://championsgatecdd.com/"),
    ("ChampionsGate Master Association -- roads, gates and amenities", "https://www.retreatcg.com/masters"),
    ("Osceola County -- Short Term Rental Planned Development (STRPD) district", "https://www.osceola.org/My-Property/Zoning-and-Land-Use/Zoning-Designation/STRPD"),
    ("STR Law Map -- Orlando/Kissimmee short-term rental rules", "https://strlawmap.com/orlando-kissimmee-short-term-rental-rules/"),
    ("Toho Water Authority -- service area", "https://www.tohowater.com/about-us/our-service-area"),
    ("South Florida Water Management District -- Upper Kissimmee Basin water supply plan", "https://www.sfwmd.gov/our-work/water-supply/upper-kissimmee"),
    ("Polk County -- water restrictions", "https://www.polkfl.gov/services/utilities/water-restrictions/"),
    ("Omni Orlando Resort at ChampionsGate -- golf courses", "https://www.omnihotels.com/hotels/orlando-championsgate/golf"),
    ("USDA NRCS -- Official Series Description, Candler series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/C/Candler.html"),
    ("USDA NRCS -- Official Series Description, Immokalee series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/I/IMMOKALEE.html"),
    ("Move With Momentum -- ChampionsGate neighborhood guide", "https://movewithmomentum.com/neighborhoods/championsgate/"),
]

# ============================================================== hub
HUB = page(
    "/areas/championsgate/", "city",
    "Artificial Turf in ChampionsGate, FL: Osceola and Polk Lots",
    "ChampionsGate turf spans two counties, two golf courses and both gated and nightly-rental villages. Permits, HOA layers and setbacks, checked September 2026.",
    "Turf across ChampionsGate's two counties, two golf courses and gated villages",
    capsule(
        f"ChampionsGate is a golf-resort community straddling the Osceola-Polk county line off I-4, about 13 miles from downtown Kissimmee, mixing gated primary-residence villages with nightly-rental villas around two Greg Norman courses. Turf here runs {price('residential')} per sq ft installed as of September 2026. What actually differs by lot is which county's permit office has your parcel, which HOA layer signs off, and whether the yard backs a pond."
    ),
    "".join([
        sec("Which office reviews a ChampionsGate permit",
            f"<p>ChampionsGate started in 1998 as a Community Development District chartered by Osceola County, and that {ext('https://championsgatecdd.com/', 'district')} still runs the community's roads, drainage and common infrastructure from an Osceola base. The community has since grown west past the county line, and a share of the newer resort-home phases carry a Davenport mailing address on a Polk County parcel instead of an Osceola one, something a search engine won't sort out for you ({ext('https://movewithmomentum.com/neighborhoods/championsgate/', 'a straddling line this local guide describes plainly')}). "
            f"Run the address through the {ext('https://www.property-appraiser.org/', 'Osceola County Property Appraiser')} if the lot sits in the older core, or the {ext('https://www.polkflpa.gov/', 'Polk County Property Appraiser')} if it's one of the newer phases toward US 27, and let the parcel record settle it before anyone calls a permit office.</p>"
            f"<p>As of September 2026, neither county's Land Development Code names synthetic turf, and neither publishes a yes-or-no answer for a residential lawn swap. That silence isn't a waiver on capping irrigation heads or on a drainage review near a pond. {a('/laws/permits/osceola-county/', 'Our Osceola County permit page')} and {a('/laws/permits/polk-county/', 'our Polk County page')} carry the department names, phone numbers and portals for each side of ChampionsGate.</p>"),

        sec("Two golf courses, a master association, and villages that don't all play by the same rule",
            f"<p>The community wraps around the {ext('https://www.omnihotels.com/hotels/orlando-championsgate/golf', 'Omni Orlando Resort at ChampionsGate')} and its two Greg Norman designs, the National Course through former orange groves and wetlands and the International Course built as an inland-links layout, both of which put water in play on more than a few holes. Above the individual villages sits the ChampionsGate Master Association, which maintains the gatehouses, the shared roads, the landscaping around those roads and common areas, a tennis and pickleball clubhouse, and a dog park open to residents' guests "
            f"({ext('https://www.retreatcg.com/masters', 'per the association site')}). That master layer handles the golf-cart paths and entry islands; it doesn't replace the review your own lot goes through inside your specific village.</p>"
            "<p>The villages themselves split into two different lives. Country Club, Stoneybrook and Stoneybrook South are gated, owner-occupied sections without nightly rentals, while the resort district and the Vistas townhomes operate as licensed vacation rentals turning guests over by the week. The Retreat has its own tangled history, with parcels recorded on both sides of the county line under one homeowners association. Which kind of village a lot sits in changes who you're coordinating a turf install with far more than which service you're buying.</p>"),

        sec("ChampionsGate yard types and what we do differently",
            "<p>Four lot types cover most of the community, and each one changes the paperwork or the layout before it changes anything about the turf itself.</p>"
            + table("ChampionsGate yard types and what we do differently",
                    ["Yard type", "County and review layer", "What changes on our end"],
                    [["Gated owner-occupied village (Country Club, Stoneybrook, Stoneybrook South)", "Mostly Osceola; village ARC plus the master association", "A submittal packet with a sample and site plan; no turnover scheduling"],
                     ["Nightly-rental village or townhome row (resort district, the Vistas)", "Often Polk; short-term-rental zoning applies", "Install dates run around the booking calendar, coordinated through a property manager"],
                     ["The Retreat and other split-parcel sections", "Recorded in either county depending on the phase", "We confirm the parcel appraiser record before quoting, not the mailing address"],
                     ["Lot backing a golf-course lake, pond or conservation edge", "Either county", "Ten-foot waterbody setback, no routing through a swale, infill that stays on the property"],
                     ["Village common areas, gatehouses and clubhouses", "CDD or master association contract, not a homeowner's ARC form", "Quoted from a site walk and a landscape spec, not a per-yard price"]],
                    "Prices don't move with the county line; the paperwork and the schedule do.")),

        sec("Short-term rental zoning on both sides of the line",
            f"<p>On the Osceola side, whole-home nightly rentals run through the county's Short Term Rental Planned Development district, defined in Land Development Code Article 3.11.1 with the eligible areas shown on an overlay map referenced at Section 3.12.2 "
            f"({ext('https://www.osceola.org/My-Property/Zoning-and-Land-Use/Zoning-Designation/STRPD', 'osceola.org')}); operating one also takes a state DBPR vacation-rental license and a county business tax receipt. Polk County allows whole-home rentals in its own designated tourist and resort zones, and by most accounts the newest wave of ChampionsGate and Davenport-corridor resort-home construction has landed on the Polk side of that line "
            f"({ext('https://strlawmap.com/orlando-kissimmee-short-term-rental-rules/', 'a secondary compilation covering both counties')}, since we couldn't pull Polk's own zoning map in this pass).</p>"
            "<p>What that means for scheduling: a homeowner in Stoneybrook South picks the install date. A rental villa's date gets set by whoever manages the calendar, which is often a management company juggling forty other addresses. A resort-lot owner searching for the best artificial turf company near ChampionsGate that can hit a three-day gap between checkouts is really asking a scheduling question first and a turf question second, and we plan the crew day around the booking software's blackout dates rather than the other way around.</p>"),

        sec("Water: two utilities and two management districts under one community",
            f"<p>Toho Water Authority, which serves St. Cloud, Kissimmee, Poinciana and unincorporated pockets of Osceola, Polk and Orange counties, covers the Osceola side of ChampionsGate on its usual two-day watering schedule, odd addresses Wednesday and Saturday, even addresses Thursday and Sunday, no daytime hours "
            f"({src('toho-days', 'Toho posted schedule')}; {ext('https://www.tohowater.com/about-us/our-service-area', 'service-area map')}). The Osceola side also sits inside the South Florida Water Management District's Upper Kissimmee Basin planning area, the district that covers most of the county "
            f"({ext('https://www.sfwmd.gov/our-work/water-supply/upper-kissimmee', 'SFWMD basin plan')}). Cross into the Polk side and the rules change utilities and districts at once: whichever provider serves that parcel, Polk County itself has been running an emergency once-a-week watering order under the Southwest Florida Water Management District's Phase III shortage declaration since February 2026, with hours restricted to before dawn or after dusk "
            f"({ext('https://www.polkfl.gov/services/utilities/water-restrictions/', 'the county current restrictions page')}).</p>"
            f"<p>None of that reaches a synthetic lawn once its heads are capped. {a('/laws/florida-hb-683/', 'The state standard')} bars in-ground irrigation on synthetic turf outright, so a shortage order that tightens sod watering to one night a week has nothing left to restrict on the turfed part of the yard.</p>"),

        sec("What's under a ChampionsGate lot, and what's next to it",
            "<p>The soil changes across the community the way the jurisdiction does. Toward the Osceola core, lots tend to sit on flatwoods soils such as Immokalee, poorly drained with a seasonally high water table under natural conditions "
            f"({ext('https://soilseries.sc.egov.usda.gov/OSD_Docs/I/IMMOKALEE.html', 'the USDA series description')}), which is why a base has to be graded and compacted with real intention rather than just leveled. Push toward the Polk side and the ridge asserts itself: Candler sand, described by USDA as very deep and excessively drained with rapid to very rapid permeability, drains almost too well and holds a shape differently under a compacted base "
            f"({ext('https://soilseries.sc.egov.usda.gov/OSD_Docs/C/Candler.html', 'the Candler series description')}). A soil test on the county line isn't optional guesswork here; it decides whether the crew is fighting standing water or fighting a base that won't hold compaction.</p>"
            f"<p>Golf-course lakes, community retention ponds and the conservation edges along both Norman courses put the state's waterbody rule into play on a lot of ChampionsGate backyards. {a('/laws/florida-hb-683/', 'Rule 62-308.100')} keeps synthetic turf at least ten feet from a pond or lake's ordinary water line unless a seawall stands between, bars routing drainage through a swale, and requires that infill stay on the property rather than washing toward the water on a graded, sloped resort lot. A lot that looks like it backs open water at the closing table sometimes turns out to back a stormwater feature instead, and the setback math is the same either way.</p>"),

        sec("Getting a turf project approved in ChampionsGate",
            f"<p>Three approvals sit on top of each other here, and none of them substitutes for another. The county, Osceola or Polk depending on the parcel, still runs its own permitting and drainage review even though {a('/laws/florida-hb-683/', 'HB 683 and the DEP synthetic turf rule')} keep it from banning a compliant lawn on a covered lot. Your village's own architectural review board still wants a submittal, separate from anything the master association maintains along the shared roads. And "
            f"{a('/laws/hoa-rules/', 'Florida law limiting what an HOA can restrict')} only protects turf that isn't visible from the frontage or a neighboring parcel, so a front yard in a gated village gets a different answer than a fenced backyard does. {a('/tools/hoa-packet-checklist/', 'Our HOA and ARC packet checklist')} lists what most boards ask for before a shovel goes in.</p>"),
        "<!--AUTO:city-services-->",
    ]),
    faqs=[
        faq("Is my ChampionsGate address in Osceola or Polk County?",
            "Check the parcel, not the mailing address. Davenport, FL 33896 shows up on both sides of the line. Search the Osceola County Property Appraiser's site first if the lot is in the older core near the Omni resort, and the Polk County Property Appraiser if it's one of the newer phases toward US 27; the parcel record states the taxing jurisdiction directly."),
        faq("Does the master association review my turf, or does my village HOA?",
            "Your village's own board reviews an individual lot. The ChampionsGate Master Association maintains shared roads, gatehouses and common-area landscaping rather than approving lot-level projects, so a submittal still goes to whichever HOA governs your specific section."),
        faq("Can a nightly-rental villa in ChampionsGate get turf installed between bookings?",
            "Yes, and it's routine here given how much of the community rents nightly. We coordinate the install date with the property manager's calendar rather than picking a date first and working around guests second."),
        faq("Does the ten-foot pond setback apply to a lot backing the golf course?",
            "It applies to any natural or man-made waterbody unless a seawall separates the lot from it, and that includes a lake or pond bordering either Norman course as much as a neighborhood retention pond. A site check on the actual water line, not the view from the patio, settles the buildable area."),
        faq("Why would the same backyard need a different base on one side of ChampionsGate than the other?",
            "Soil changes with the county line here. The Osceola core sits on poorly drained flatwoods soil that needs a graded base to shed water; the Polk-side ridge runs on excessively drained sand that behaves differently under compaction. Both still take a washed crushed-rock base, just built to different local conditions."),
    ],
    sources=SRC, city=SLUG,
    crumbs=[("Service areas", "/areas/")], crumb="ChampionsGate",
    related=[
        ("/areas/osceola-county/", "Service area: Osceola County"),
        ("/areas/polk-county/", "Service area: Polk County"),
        ("/laws/permits/osceola-county/", "Osceola County turf permits"),
        ("/laws/permits/polk-county/", "Polk County turf permits"),
        ("/areas/reunion/", "Turf in Reunion"),
        ("/areas/four-corners/", "Turf in Four Corners"),
        ("/artificial-turf-cost/", "Turf cost tables for Central Florida"),
    ],
)

# ============================================================== per-service local content
LOCAL = {}

LOCAL["residential"] = {
    "title": "Artificial Grass Installation in ChampionsGate, FL",
    "meta": "Artificial grass in ChampionsGate runs $8-$18 per sq ft installed as of September 2026, with the base built differently on the Osceola side than on the Polk ridge.",
    "h1": "Lawn turf for ChampionsGate's gated and resort-built streets",
    "lede": capsule(
        f"A ChampionsGate lawn conversion runs {price('residential')} per sq ft installed as of September 2026, the same range whether the parcel sits in Osceola or Polk County. What changes is the base: flatwoods soil near the Omni resort core holds water differently than the excessively drained ridge sand toward the Polk line, and a gated village's ARC wants paperwork a resort-built rental street never asks for."
    ),
    "sections": [
        ("How we read the soil before we read the HOA rules",
         "<p>ChampionsGate's ground shifts under your feet across the community. Lots closer to the Omni resort core tend to sit on flatwoods soil such as Immokalee, poorly drained with a water table that rises after a summer storm, so the base needs a real 1-2% grade away from the house and a full washed crushed-rock lift to keep the surface from ponding. "
         f"Lots pushing toward the Polk-side ridge sit on soil closer to Candler sand, which USDA classes as excessively drained and very rapidly permeable, a different problem entirely: the base compacts less predictably because the sand underneath drains almost too fast. "
         "We check the soil map before we quote a base depth, because guessing wrong in either direction means a redo.</p>"),
        ("Gated village paperwork versus a resort-built rental street",
         f"<p>A lawn in {city('championsgate', 'ChampionsGate')}'s gated, owner-occupied sections such as Stoneybrook South goes through that village's own architectural review, typically a sample, a spec sheet and a site sketch, separate from anything the community's master association handles along the shared roads. "
         "A resort-built rental street inside the vacation zones often skips that step entirely, since many of those homes were built without a resident-facing ARC in the same sense, though the property's own management company usually wants a heads-up before a crew shows up mid-week. Either way, the county permit question sits underneath both, and it depends on which side of the line the parcel falls.</p>"),
        ("What a builder-sod front yard looks like after twenty-plus years",
         f"<p>The oldest sections of ChampionsGate date to the community's 1998 start as a Community Development District, which puts some original landscaping into its third decade. St. Augustine sod that age has usually been re-sodded more than once already, and the irrigation zones under it are original 1990s-era heads in a lot of cases. Swapping a tired front lawn for turf on one of these older lots means capping those original heads for good, a requirement under the state's turf standard regardless of the sod's age, and it's often the point where an aging irrigation system gets simplified rather than repaired again. "
         f"{post('why-new-construction-sod-dies-in-osceola-county', 'A separate piece on why builder sod struggles across the county')} goes deeper on that pattern, and the full {svc('residential', 'residential installation guide')} covers the rest of a standard build.</p>"),
    ],
    "scenario": (
        "Say you have a 900 sq ft front yard",
        f"<p>Say you have a 900 sq ft front yard in Stoneybrook South, a rectangle split by a walkway, with builder St. Augustine that's thinned out under a live oak's shade. At {price('residential')} per sq ft, a straightforward conversion lands between $7,200 and $16,200, though a front yard with a village ARC review and a tree canopy to work around usually settles in the upper half of that band rather than the bottom. Because the lot backs onto a shared road the master association landscapes rather than a private backyard, there's no waterbody setback to plan around here, just the drip line under the oak and the village's own submittal packet. Add the arborist letter to the ARC file if the oak's canopy reaches over the work area, since that clears both the HOA question and the state rule's drip-line requirement in one document.</p>"
    ),
    "faqs": [
        faq("Does it cost more to install turf on the Polk side of ChampionsGate than the Osceola side?",
            "No. The published market range is the same across the county line. What differs is base depth and grading time, which a bid should reflect based on the actual soil, not the address."),
        faq("Do I need my village's approval even if the master association already landscapes my street?",
            "Yes. The master association's landscaping authority covers shared roads and common areas, not an individual homeowner's lot, so your own village HOA still reviews a lawn conversion separately."),
    ],
    "sources": SRC,
}

LOCAL["pet"] = {
    "title": "Pet Turf and Dog Runs in ChampionsGate, FL",
    "meta": "Pet turf in ChampionsGate costs $10-$18 per sq ft installed as of September 2026, built for zero-lot-line yards and the community's shared dog park.",
    "h1": "Fast-draining turf for ChampionsGate's tight side yards and dog runs",
    "lede": capsule(
        f"Pet turf in ChampionsGate runs {price('pet')} per sq ft installed as of September 2026. Many gated-village lots here are narrow and zero-lot-line, so a dog's daily circuit is often a side strip rather than an open backyard, and the community's own shared dog park at the master association's clubhouse gives owners a second option worth planning around."
    ),
    "sections": [
        ("A shared dog park changes what a backyard has to do",
         f"<p>The ChampionsGate Master Association runs a dog park open to residents' guests at its tennis and pickleball clubhouse, which means a dog here often gets two different surfaces in its week: whatever's at home and a shared, sunbaked run maintained by the association. That takes some pressure off a small backyard to be the dog's only exercise space, but it doesn't take away the daily accidents a side yard absorbs between trips to the shared park. A narrow, fast-draining run at home still earns its keep even when the community has its own dog amenity.</p>"),
        ("Zero-lot-line yards in the gated villages",
         "<p>Country Club and Stoneybrook lots were built close together, and a dog run here is frequently a 3 to 6 ft strip along a privacy wall rather than an open lawn. That width rules out heavy equipment; base work in a strip that narrow is wheelbarrow-and-hand-tamper labor, and the drainage slope has to be built into a smaller cross-section than a typical backyard gets. Odor control matters more in a confined strip too, since there's less air movement to carry ammonia off than in an open yard.</p>"),
        ("Rental villas, guest dogs and infill that actually needs rinsing",
         f"<p>Vacation rentals that allow pets see a rotating cast of dogs rather than one household's routine, which means odor-control infill earns its cost faster on a rental lot than on an owner-occupied one. Zeolite traps ammonia and releases it on a rinse, so a property manager scheduling a mid-stay cleaning crew gets more consistent results than hoping a renter remembers to hose down the yard. On an owner-occupied lot in a gated village, the same infill just needs a homeowner's own rinse schedule instead of a manager's. "
         f"{post('how-to-get-dog-urine-smell-out-of-artificial-turf', 'Our guide to clearing dog-urine odor from turf')} walks through the rinse routine in more detail, and the full {svc('pet', 'pet turf guide')} covers infill choices beyond zeolite.</p>"),
    ],
    "scenario": (
        "Say you have a 4 by 60 ft side yard",
        f"<p>Say you have a 4 by 60 ft side yard along a privacy wall in one of Stoneybrook's zero-lot-line sections, 240 sq ft total, currently bare dirt where the dog has worn out whatever grass tried to grow. At {price('pet')} per sq ft, that runs $2,400 to $4,320, likely toward the top of the range given the narrow access and the extra drainage base a strip that tight needs. Zeolite infill adds a modest premium over standard silica but pays for itself in a run this size well before a typical lawn would notice the difference, since the whole strip is exposed to the same traffic every day rather than sharing space with a family's general yard use.</p>"
    ),
    "faqs": [
        faq("Does ChampionsGate's shared dog park mean I don't need pet turf at home?",
            "Not really. The association's dog park is a shared amenity at the clubhouse, useful for exercise, but it doesn't handle the daily relief trips a dog takes in its own yard between visits there."),
        faq("Can a rental villa in ChampionsGate advertise as pet-friendly with turf installed?",
            "That's a decision for the property manager and the village's pet policy, not something turf changes on its own. What turf does is make a pet-friendly listing easier to keep presentable between guest stays."),
        faq("Is a weed barrier worth it under pet turf here given the sandy soil?",
            "Generally no. A barrier traps urine against the fabric instead of letting it drain through, which works against the point of a fast-draining pet system regardless of which side of the county line the soil sits on."),
    ],
    "sources": SRC,
}

LOCAL["putting"] = {
    "title": "Backyard Putting Greens in ChampionsGate, FL",
    "meta": "Putting greens in ChampionsGate cost $14-$30 per sq ft installed as of September 2026, an amenity homeowners add beside two Greg Norman-designed courses.",
    "h1": "A home green to go with ChampionsGate's two championship courses",
    "lede": capsule(
        f"A backyard putting green in ChampionsGate runs {price('putting')} per sq ft installed as of September 2026. Living beside the Omni resort's National and International courses, some homeowners want a home green to work on a stroke between rounds rather than to replace the course itself, and a golf-community lot often backs a lake that sets the buildable area before the design ever starts."
    ),
    "sections": [
        ("A practice green next to two championship courses, not instead of one",
         f"<p>The two Greg Norman designs at {ext('https://www.omnihotels.com/hotels/orlando-championsgate/golf', 'Omni Orlando Resort at ChampionsGate')}, the National Course through former citrus groves and wetlands and the harder International Course built as an inland-links layout, give ChampionsGate residents a reason to want a green at home for something a round on either course doesn't offer: unlimited reps on one specific putt with no group waiting behind. A three- or four-cup home green sized for that kind of practice looks nothing like a course green and doesn't need to; it needs consistent roll on the breaks a homeowner actually plays. "
         f"{post('backyard-putting-green-cost-florida', 'A broader look at putting green pricing across Florida')} and the full {svc('putting', 'putting green guide')} cover design options beyond what's local to this community.</p>"),
        ("Golf-course pond lots decide the buildable footprint first",
         "<p>A lot backing a lake along either course, or a retention pond tucked between fairways, has to keep the green at least ten feet from the water's ordinary line unless a seawall separates the two, and that setback often lands right where a homeowner first imagined the green sitting for the best view of the course beyond it. We confirm the actual water line against the property survey before any shaping design gets drawn, because a green pushed a few feet closer to the view than the setback allows is a green that gets rejected before it gets built.</p>"),
        ("Someone asking who builds the best putting green near ChampionsGate usually means this",
         "<p>Most calls about a green here aren't about finding a lower price; they're about finding an installer who's shaped a contoured base before; a green built by someone chasing a flat lawn's compaction method instead of a shaped, tiered one tends to hold water in its lowest tier after the first real storm. Ask to see how a prospective installer handles a green's deeper excavation and hand-shaped lifts, since that's the part of the job a lawn quote and a green quote genuinely diverge on, well before the surface product gets chosen.</p>"),
    ],
    "scenario": (
        "Say you have a 350 sq ft green",
        f"<p>Say you have a 350 sq ft green planned for a Stoneybrook South backyard that backs a lake along the National Course, with two tiers and three cups. At {price('putting')} per sq ft, that prices between $4,900 and $10,500 depending on fringe turf, cup count and how much shaping the tiers need. Because the lot backs open water, the buildable footprint stops ten feet from the shoreline, which on a typical resort-style lot here still leaves enough room for a green this size closer to the house. The village ARC packet for a green usually wants the same site plan a lawn conversion needs, plus a rough sketch of the contours, since the association is approving a shape as much as a material.</p>"
    ),
    "faqs": [
        faq("Do I need a bigger setback for a green near the golf course than for one anywhere else?",
            "The ten-foot waterbody rule applies to any pond or lake edge the same way, golf-course-adjacent or not, unless a seawall separates the lot from the water. What changes near a course is how often that water shows up on the property line."),
        faq("Can a putting green go in a ChampionsGate rental villa's backyard?",
            "It can, and a well-built one can be a selling point in a listing description, though the tight lots in some rental sections leave less room for real contouring than a larger gated-village yard does."),
        faq("Does the state's turf rule change what infill goes in a green here?",
            "Yes, the same as any other lawn: infill on a single-family lot has to be silica sand, rock, shell or another natural material, or coated sand with a non-toxic coating, which covers what most greens already use for roll consistency."),
    ],
    "sources": SRC,
}

LOCAL["playground"] = {
    "title": "Playground Turf for ChampionsGate Homes, FL",
    "meta": "Playground turf in ChampionsGate runs $10-$25 per sq ft installed as of September 2026, a small but real market on the community's owner-occupied lots.",
    "h1": "Cushioned play turf for ChampionsGate's family lots",
    "lede": capsule(
        f"Playground turf in ChampionsGate runs {price('playground')} per sq ft installed as of September 2026. This is a smaller market here than pool turf or vacation-rental lawns, since the demand clusters on the community's owner-occupied family lots rather than on the resort-built rental streets, where a swing set rarely fits the listing."
    ),
    "sections": [
        ("Where the demand actually sits in this community",
         "<p>A shock-padded play surface makes sense where a family lives in the house year-round and a swing set earns its keep every week, which in ChampionsGate mostly means the gated, owner-occupied villages such as Stoneybrook South and Country Club rather than the nightly-rental streets. A rental villa's backyard is more often built around a pool cage than a jungle gym, since that's what books better on a listing, so we're honest that playground turf is a smaller slice of the work here than it is in a family-heavy suburb further from the resort core.</p>"),
        ("Sizing the shock pad to what's actually going in the yard",
         "<p>A home swing set or a small climbing structure needs a shock pad sized to its fall height, thinner under a low slide than under a tall climbing tower, and that pad sits under the turf rather than replacing the base beneath it. On a ChampionsGate lot with a live oak somewhere near the play area, which is common in the community's older sections, we also confirm the drip line before excavating, since a shallow shock-pad dig can still disturb roots close to the surface even without going as deep as a lawn's full base.</p>"),
        ("Infill choice is simpler here than the marketing suggests",
         f"<p>As of the state's May 2026 standard, infill under home playground equipment can be a synthetic material within the equipment's footprint, but everywhere else on the same single-family lot it has to stay natural, silica, rock, shell or a similarly compliant material. A backyard with a play area and an open lawn around it in the same ChampionsGate yard ends up with two infill zones rather than one uniform product, which is worth knowing before a quote comes in assuming a single infill for the whole job. "
         f"{post('is-artificial-turf-safe-for-kids-pfas-lead', 'Our piece on PFAS, lead and infill safety for kids')} goes through that question in full, and the {svc('playground', 'playground turf guide')} covers shock-pad sizing by fall height. A family weighing the same question in {city('celebration', 'nearby Celebration')} faces the same infill split.</p>"),
    ],
    "scenario": (
        "Say you have a 220 sq ft play area",
        f"<p>Say you have a 220 sq ft play area in a Country Club backyard, sized around a swing set with a 6 ft fall height, next to an open lawn already turfed in a separate project. At {price('playground')} per sq ft, the play area alone runs $2,200 to $5,500 depending on shock-pad thickness, generally toward the upper half given the pad sizing a swing set that tall calls for. Because the equipment footprint is small relative to the whole yard, most of the ChampionsGate installs we're asked about at this size are add-ons to an already-turfed lawn rather than the first project on the lot.</p>"
    ),
    "faqs": [
        faq("Is playground turf common in ChampionsGate's rental villas?",
            "Not especially. Most rental-village backyards here are built around the pool cage rather than play equipment, so this service sees more calls from the community's owner-occupied family sections."),
        faq("Does a live oak near the play area need an arborist letter?",
            "If the equipment or the shock pad falls inside the tree's drip line, yes, the same certified-arborist exception the state's turf rule requires for any synthetic surface applies to a shock pad too."),
    ],
    "sources": SRC,
}

LOCAL["pool"] = {
    "title": "Pool and Lanai Turf in ChampionsGate, FL",
    "meta": "Pool-area turf in ChampionsGate runs $8-$18 per sq ft installed as of September 2026, built for the screened pool cages on the community's resort-style homes.",
    "h1": "Turf inside ChampionsGate's screened pool cages and lanais",
    "lede": capsule(
        f"Pool and lanai turf in ChampionsGate prices in the {price('residential')} per sq ft range as of September 2026. Screened pool cages are close to standard on the resort-style homes built across both the Osceola and Polk sides of the community, and the strip of ground inside that screen is often the one part of the yard sod never held onto in the first place."
    ),
    "sections": [
        ("Screened cages are the norm on ChampionsGate's resort-built homes",
         f"<p>A private pool inside a screen enclosure is close to the default layout on the vacation-home construction that fills ChampionsGate's resort district and townhome rows, and the same style shows up plenty in the gated owner-occupied villages too. The ground inside that screen gets shade from the cage frame for part of the day and heavy foot traffic in wet swimsuits the rest of it, a combination sod handles poorly and turf handles by design, since it doesn't need sun to survive and doesn't hold water the way soil does underfoot. "
         f"{post('can-artificial-turf-melt', 'Our note on turf and melting risk near reflective glass')} is worth a read before placing turf close to a low-E slider, and the {svc('pool', 'pool and lanai turf guide')} covers deck-mounted installs beyond ChampionsGate.</p>"),
        ("Turf over the pool deck itself, not just around it",
         "<p>Where the deck is concrete rather than pavers, which is common inside these cages, turf goes down with a drainage underlay and glue-down edges rather than the nailed perimeter a lawn gets, since there's no soil underneath to anchor into. That underlay is what keeps water from sheeting across the deck after a rinse or a rain instead of passing through, and it's a different install method entirely from a backyard conversion even though the finished look reads the same to a guest walking out to the pool.</p>"),
        ("What a nightly-rental pool cage needs that an owner-occupied one doesn't",
         "<p>A rental villa's pool area sees a new set of feet, sunscreen and pool chemicals every week or two, and a property manager scheduling turnover cleaning benefits from a surface that rinses clean fast between groups rather than one that needs raking or edging. An owner-occupied pool cage in a gated village gets the same turf but a slower wear cycle, since it's one household's routine rather than a rotating guest list putting the surface through its paces.</p>"),
    ],
    "scenario": (
        "Say you have a 400 sq ft pool deck",
        f"<p>Say you have a 400 sq ft strip of concrete pool deck inside a screen cage on a rental villa in ChampionsGate's resort district, currently bare and hot underfoot by afternoon. At the {price('residential')} per sq ft range, glue-down turf over that deck runs $3,200 to $7,200, with the underlay and edge work usually pushing a small enclosed area like this toward the top of the band rather than the bottom. Scheduling the two-day job between guest stays is the main coordination point, since the deck has to be fully cured before the next check-in, and a property manager with a booking calendar handles that timing better than picking a date and hoping it holds.</p>"
    ),
    "faqs": [
        faq("Does turf over a pool deck need the same base as a lawn?",
            "No. A concrete deck inside a screen cage gets a drainage underlay and glued, taped seams instead of the washed crushed-rock base and nailed edges a soil lawn needs, since there's no ground to build up underneath it."),
        faq("Do property managers usually schedule pool-area turf between guest bookings?",
            "Yes, that's the common pattern in ChampionsGate's rental villages, and it's worth telling us the booking calendar up front so the job doesn't overlap a check-in."),
    ],
    "sources": SRC,
}

LOCAL["str"] = {
    "title": "Vacation Rental Turf in ChampionsGate, FL",
    "meta": "Vacation-rental turf in ChampionsGate prices near $8-$18 per sq ft installed as of September 2026, scheduled around bookings on Osceola and Polk rental lots.",
    "h1": "Guest-proof yards for ChampionsGate's nightly-rental villas",
    "lede": capsule(
        f"Vacation-rental turf in ChampionsGate prices in the {price('residential')} per sq ft range as of September 2026. Between Osceola's Short Term Rental Planned Development zoning and Polk's own resort-zone rentals, a large share of this community operates as nightly housing, and the install date usually answers to a booking calendar rather than a homeowner's own schedule."
    ),
    "sections": [
        ("Two counties, two ways of licensing the same kind of home",
         f"<p>On the Osceola side, nightly rentals operate through the county's Short Term Rental Planned Development district, defined under Land Development Code Article 3.11.1 with eligible parcels mapped at Section 3.12.2, on top of a state DBPR vacation-rental license "
         f"({ext('https://www.osceola.org/My-Property/Zoning-and-Land-Use/Zoning-Designation/STRPD', 'per osceola.org')}). Polk County permits the same kind of whole-home rental in its own designated tourist and resort zones, and a large share of ChampionsGate's newer resort-built construction sits on that side of the county line, sharing a Davenport address with {city('davenport', 'Davenport proper')} a few miles further down US 27. Two different zoning frameworks end up producing the same result on the ground: a street of homes that turn over guests weekly rather than housing one family long-term. The full {svc('str', 'vacation rental turf guide')} covers scheduling patterns that apply community-wide.</p>"),
        ("A yard built to survive turnover, not just look good in photos",
         "<p>A rental yard here takes different wear than a family's own lawn. Suitcases roll across it, kids from a dozen different households run the same path to a pool gate every week, and a landscaping crew or property manager, not the resident, notices when it starts to look tired. Turf's advantage in this setting isn't really the heat or the water bill; it's that a guest-facing yard photographs the same in month eighteen as it did on move-in day, which matters more to a booking listing than it does to a homeowner who's there every day and notices gradual wear less.</p>"),
        ("Coordinating install day with a property manager's calendar",
         f"<p>A vacation-rental install runs on the same clock a cleaning turnover does: a crew needs the property empty for the work, which usually means fitting between a checkout and the next check-in rather than picking a date off a calendar in isolation. We ask for the booking software's blackout window before scheduling, and a job that would take two days on an empty lawn sometimes gets split or timed around a longer vacancy gap instead. Property managers who handle several ChampionsGate addresses tend to have this coordination down to a routine already. "
         f"{post('what-to-expect-on-turf-installation-day', 'What to expect on install day')} walks through the crew's actual sequence, useful to forward to an owner asking about timing.</p>"),
    ],
    "scenario": (
        "Say you own a rental villa with a 700 sq ft yard",
        f"<p>Say you own a rental villa in the resort district with a 700 sq ft backyard behind the pool cage, currently sod that's browned out from being mowed on whatever schedule a landscaping contractor keeps rather than a homeowner's own attention. At {price('residential')} per sq ft, that conversion runs $5,600 to $12,600, and because the yard sits outside the pool cage rather than inside it, it uses a standard soil base rather than the deck-mounted method a screened area needs. Booking a five-day vacancy gap, which most calendars have at least once between peak seasons, gives the crew room for the base, the seams and a full cure before the next guest walks the yard.</p>"
    ),
    "faqs": [
        faq("Do I need to confirm my ChampionsGate parcel is in a rental zone before installing turf?",
            "That's a licensing question for the county, not a turf one, but it's worth confirming since Osceola's overlay and Polk's resort zones are drawn differently and a mailing address alone won't tell you which applies."),
        faq("How far in advance should a property manager book a turf install?",
            "As soon as a vacancy gap of three or more days is visible on the calendar. Base work and cure time need that window, and last-minute scheduling around a single-night gap usually isn't enough."),
        faq("Does rental turf need different infill than an owner-occupied lawn?",
            "Not by rule. The same state material standard applies to both; a rental yard more often benefits from odor-control infill simply because more dogs and more feet pass through it in a given month."),
    ],
    "sources": SRC,
}

LOCAL["commercial"] = {
    "title": "Commercial Turf for ChampionsGate Common Areas, FL",
    "meta": "Commercial turf for ChampionsGate's clubhouses and common areas is quoted per job, built around the master association's own landscape contract, not a homeowner ARC.",
    "h1": "Turf for ChampionsGate's clubhouses, gatehouses and shared grounds",
    "lede": capsule(
        "Commercial turf for ChampionsGate's shared spaces, gatehouse entries, clubhouse grounds and village amenity centers, is quoted per job rather than off a per-square-foot table, since a landscape contract with the master association or a village's own board looks nothing like a homeowner's ARC submittal."
    ),
    "sections": [
        ("Whose contract this actually runs through",
         f"<p>The ChampionsGate Master Association, chartered alongside the community's Community Development District, maintains the gatehouses, shared road landscaping and a tennis and pickleball clubhouse "
         f"({ext('https://www.retreatcg.com/masters', 'per the association site')}), and any turf work at those locations runs through that entity's own vendor process rather than through {a('/tools/hoa-packet-checklist/', 'the ARC packet')} a homeowner files. A village-level clubhouse or pool deck, where one exists separately from the master association's amenities, follows its own board's procurement instead. Knowing which body owns the ground is the first question on a commercial bid here, before square footage even comes up. The full {svc('commercial', 'commercial turf guide')} covers amenity-center work beyond this community.</p>"),
        ("Gatehouse entries and paver medians see heavier equipment traffic",
         "<p>A gatehouse island or an entry median gets mowed, blown and driven past by delivery trucks and moving vans far more than a residential lot ever does, so turf at these locations needs a firmer, more heavily compacted base and an edge detail that survives a truck tire clipping the corner. These are also usually the most visible turf in the community, greeting every resident and guest at the gate, which raises the bar on a clean, consistent seam line more than a backyard install typically does.</p>"),
        ("A CDD's stormwater responsibility runs alongside a landscape contract",
         f"<p>Osceola County's ordinance chartering the district assigns the CDD's own engineer and manager responsibility for stormwater management and its associated landscaping, which means a commercial turf project on district-maintained ground has to work inside whatever drainage system the CDD already runs, not create a new one. That's a coordination step a homeowner's backyard project never has to clear, since a private lot's drainage doesn't answer to a special district's engineer the way common-area ground does. "
         f"{post('artificial-turf-for-balconies-rooftops-and-condos', 'Our piece on turf for condos and shared buildings')} covers a similar multi-party approval process outside this community.</p>"),
    ],
    "scenario": (
        "Say a village clubhouse pool deck",
        "<p>Say a village clubhouse pool deck and its surrounding turf strip, roughly 1,800 sq ft total, needs replacing after years of resident and rental-guest foot traffic wore the sod down to dirt in the high-use paths. A commercial job this size gets quoted from a site walk and a landscape spec rather than a flat per-foot number, since the board typically wants a firmer base spec and a longer warranty conversation than a single homeowner's yard does. Scheduling around the pool's own operating hours, rather than a single household's calendar, is usually the bigger constraint than the turf work itself.</p>"
    ),
    "faqs": [
        faq("Does a village board or the master association pay for common-area turf?",
            "It depends on which entity maintains the specific ground. Shared roads and gatehouses generally fall under the master association; an individual village's own clubhouse or pool deck usually falls under that village's own board."),
        faq("Can commercial turf work interfere with the CDD's stormwater system?",
            "It shouldn't, but any work on district-maintained ground has to route around the existing drainage the CDD's engineer already manages rather than altering it, which is part of why these jobs start with a site walk."),
    ],
    "sources": SRC,
}

LOCAL["sports"] = {
    "title": "Sports and Fitness Turf in ChampionsGate, FL",
    "meta": "Sports turf in ChampionsGate is quoted per job, a small market here focused on home-gym sled tracks and agility lanes on owner-occupied lots.",
    "h1": "Sled tracks and home fitness turf on ChampionsGate lots",
    "lede": capsule(
        "Sports and fitness turf in ChampionsGate, a sled track in a garage or an agility lane in a side yard, is quoted per job rather than a published range. It's a small market here next to the community's two full golf courses and its putting-green demand, but it comes up on owner-occupied lots with room to spare."
    ),
    "sections": [
        ("A small slice of the work, next to two full golf courses",
         f"<p>With {ext('https://www.omnihotels.com/hotels/orlando-championsgate/golf', 'two Greg Norman-designed courses')} already inside the community, ChampionsGate residents looking for a home sports surface are far more likely to call about a putting green than a batting cage or a full agility course, and we're straightforward that dedicated sports turf is a narrower slice of demand here than in a suburb without a resort golf amenity built in. What does come up regularly is something smaller: a sled track along a garage wall or a short agility lane for a dog, both of which fit lots that don't have room for anything bigger. The {svc('sports', 'sports and fitness turf guide')} covers bocce courts and batting cages for lots with more room to spare.</p>"),
        ("Where the ridge-side soil actually helps",
         f"<p>A sled track or a short sprint lane needs a firm, stable base more than it needs drainage capacity, and lots on the Polk side of ChampionsGate sitting on excessively drained Candler sand "
         f"({ext('https://soilseries.sc.egov.usda.gov/OSD_Docs/C/Candler.html', 'per USDA series description')}) tend to compact into a firmer working surface than the flatwoods soil closer to the Osceola core, once it's brought to the right moisture content during the build. That's one of the few places in this community where the ridge-side ground works in the homeowner's favor rather than against it.</p>"),
        ("A garage sled track still answers to the same state material rule",
         f"<p>Turf inside a garage for a sled or a short conditioning lane sits on a slab rather than soil, so it skips the drainage-base conversation entirely, but the infill and backing rules under the state's synthetic turf standard still apply if any part of the lane extends outside onto the lot. A build that stays entirely inside a garage slab is simpler on paper than one that steps out into the yard, which is worth deciding early since it changes both the base method and which rules govern the infill. "
         f"{post('artificial-turf-on-a-slope', 'Our notes on turf on a graded or sloped surface')} apply to a sled lane that steps down off a garage slab toward a side yard.</p>"),
    ],
    "scenario": (
        "Say you have a 12 by 20 ft garage bay",
        "<p>Say you have a 12 by 20 ft garage bay, 240 sq ft, that you want turfed for sled pushes and light conditioning work rather than parking a second car. Because it sits entirely on a slab, the job skips soil excavation and base rock altogether, going straight to a glued or friction-fit surface sized for repeated sled traffic, which is a different scope than a yard conversion of the same square footage would be. A firm, low-pile product built for load rather than looks holds up to a loaded sled far better than a residential-lawn-weight turf would, and it's worth specifying that distinction before a quote comes back priced like a backyard.</p>"
    ),
    "faqs": [
        faq("Is a backyard sports court common in ChampionsGate?",
            "Not especially, given how much of the community already has golf and community amenities built in. Garage sled tracks and small agility lanes come up more often than a dedicated court."),
        faq("Does a garage sled track need a permit in ChampionsGate?",
            "A build that stays entirely inside an existing garage slab typically doesn't trigger the same review a yard project does, but confirm with your village HOA if the garage door or exterior look changes at all."),
    ],
    "sources": SRC,
}

LOCAL["pavers"] = {
    "title": "Turf and Pavers in ChampionsGate, FL",
    "meta": "Turf-between-pavers work in ChampionsGate is quoted per job, common along the resort-style paver driveways and walkways built across the community.",
    "h1": "Turf ribbons for ChampionsGate's paver driveways and walkways",
    "lede": capsule(
        "Turf set between pavers in ChampionsGate, a green ribbon down a driveway or a stepping-stone path to a side gate, is quoted per job rather than a flat rate. Paver driveways and walkways are close to standard on the community's resort-built homes, which makes this a more common ask here than in an area built mostly on plain concrete."
    ),
    "sections": [
        ("Why paver hardscape shows up so often on these lots",
         f"<p>Resort-style construction across both the Osceola and Polk sides of ChampionsGate tends to favor paver driveways, walkways and pool decks over plain concrete, a builder choice that shows up on gated owner-occupied lots and rental villas alike. That much paver surface creates plenty of joints and borders where a strip of turf can replace grass that struggles to grow in a narrow gap anyway, whether that's a center ribbon down a two-track driveway or a border along a front walkway leading to a gatehouse-adjacent entry. "
         f"{post('install-artificial-turf-over-concrete-pavers-or-grass', 'Our guide to installing over concrete, pavers or grass')} covers the method differences, and the {svc('pavers', 'turf and pavers guide')} has more paver-pattern examples.</p>"),
        ("A narrow strip needs different edge work than an open lawn",
         "<p>Turf set into a paver joint or border gets pinned and glued against the hard edge rather than nailed into soil, since there's often no dirt to anchor into on either side. On a driveway ribbon specifically, the strip also needs to handle occasional car tire weight if anyone parks across it, which calls for a firmer, shorter product than a lawn-weight turf and a base that won't rut under that occasional load.</p>"),
        ("Where the master association's shared-road paving meets a private driveway",
         f"<p>Some ChampionsGate entry roads and paver medians fall under the master association's maintenance rather than an individual lot's, so a turf-and-paver project that touches the transition between a private driveway and a shared road frontage can involve a quick check with the association before work starts, separate from whatever a homeowner's own village ARC wants for the driveway itself.</p>"),
    ],
    "scenario": (
        "Say you have a paver driveway with a 3 ft center strip",
        "<p>Say you have a paver driveway with a 3 ft wide, 40 ft long center strip currently patched with whatever grass survives between the wheel tracks, 120 sq ft total. A turf ribbon there is a smaller, more detail-heavy job than its square footage suggests, since pinning and gluing along two paver edges takes more careful trim work per foot than an open lawn does. Most quotes for a strip this size and shape land toward the higher end of a comparable open-lawn price per square foot, purely because of the edge labor rather than the material itself.</p>"
    ),
    "faqs": [
        faq("Can turf between pavers handle a car parking on it occasionally?",
            "A firmer, shorter-pile product built for light load can, but it should be specified up front rather than assumed, since a standard lawn-weight turf isn't built for regular tire traffic."),
        faq("Do paver strips near a shared entry road need the master association's sign-off?",
            "Only where the work touches ground the association maintains rather than the private lot itself, which is worth a quick check before starting a project near a shared entry or median."),
    ],
    "sources": SRC,
}

LOCAL["repair"] = {
    "title": "Turf Repair in ChampionsGate, FL",
    "meta": "Turf repair in ChampionsGate is priced per visit, covering everything from guest-turnover wear on rental lots to seams lifted after a storm off the golf courses.",
    "h1": "Fixing seams, lifts and worn spots on ChampionsGate turf",
    "lede": capsule(
        "Turf repair in ChampionsGate is priced by the visit rather than the square foot, and what brings a crew out here splits along the same line as everything else in this community: rental lots wear from guest turnover, while owner-occupied lots more often call about a seam or an edge after a storm."
    ),
    "sections": [
        ("Guest-turnover wear shows up in predictable spots",
         "<p>A rental villa's turf takes its heaviest traffic along the same paths every week, the route from the sliding door to the pool gate, the corner where suitcases get set down, and repair calls on these lots tend to cluster right there rather than spreading evenly across the yard. A property manager who catches a lifted edge or a worn seam between one checkout and the next check-in can usually get it fixed in a single visit, which beats letting several guest cycles wear a small problem into a bigger one.</p>"),
        ("Irrigation heads that were capped, not removed, sometimes resurface",
         f"<p>The state's turf standard requires capping in-ground heads under synthetic turf rather than pulling the pipe entirely, and on some ChampionsGate lots, especially ones with original 1990s-era irrigation, a cap installed without enough care can work loose or a line can settle, pushing a small bump up through the turf where a head sits. That's a repair call distinct from a torn seam or a wind-lifted edge, and it's worth mentioning irrigation history when booking a repair visit so the crew brings the right fix. "
         f"{post('does-homeowners-insurance-cover-artificial-turf', 'Our look at what homeowners insurance covers on turf damage')} is worth reading before a storm-related repair, and the full {svc('repair', 'turf repair guide')} lists what a service call typically costs.</p>"),
        ("Storm exposure differs by how open the lot sits",
         "<p>A lot with an open sightline toward a fairway or a retention pond, common across ChampionsGate's golf-adjacent sections, catches more direct wind during a summer storm than one tucked behind other homes, and edge lift after a bad blow shows up more on those exposed lots. Checking edge anchoring after any significant storm, rather than waiting for a visible lift to spread, catches the problem while it's still a quick pin-and-reglue job instead of a full edge redo.</p>"),
    ],
    "scenario": (
        "Say you have a 30 ft seam that's opened",
        "<p>Say you have a 30 ft seam along the pool-cage edge of a rental villa's backyard that's opened after eighteen months of guest turnover and hose rinses, along with one corner where the perimeter nails have pulled loose. A repair visit for a seam and an edge section this size is typically a single crew, a few hours, priced as a service call rather than a per-foot job, and scheduling it in the same vacancy gap as a routine deep clean between guests avoids a second empty-property visit. Left unaddressed through another few guest cycles, a seam like this tends to widen rather than stay put, so it's worth booking before the next long-stay guest rather than after a complaint.</p>"
    ),
    "faqs": [
        faq("Does turf repair in ChampionsGate cost more on a rental lot than an owner-occupied one?",
            "The repair itself is priced the same either way; what differs is how often a rental lot needs a visit, since guest turnover wears specific paths faster than one household's routine does."),
        faq("Can a repair crew work around a property's booking calendar?",
            "Yes, and for a rental lot it's worth sharing the calendar up front so the visit lands in a vacancy gap rather than overlapping a guest stay."),
    ],
    "sources": SRC,
}

LOCAL["cleaning"] = {
    "title": "Turf Cleaning and Maintenance in ChampionsGate, FL",
    "meta": "Turf cleaning in ChampionsGate is quoted by yard size, timed around guest turnovers on rental lots and a regular schedule on owner-occupied ones.",
    "h1": "Keeping ChampionsGate turf fresh between guests and seasons",
    "lede": capsule(
        "Turf cleaning and maintenance in ChampionsGate is quoted by yard size and how long it's been, not a flat rate. On the community's rental villas, cleaning runs on a turnover schedule set by a property manager; on the gated, owner-occupied lots, it runs on whatever seasonal rhythm the homeowner prefers."
    ),
    "sections": [
        ("A turnover schedule that a lawn crew never sees",
         f"<p>A rental villa's turf gets cleaned on the same clock as the sheets and towels, timed to a checkout-to-check-in gap rather than a monthly calendar, and a property manager who bundles a power-brooming and odor pass into that turnover routine catches problems before a new guest ever notices them. That rhythm is different enough from a typical residential cleaning schedule that we ask about the property's booking pattern before quoting a recurring service, since a weekly-turnover villa and a long-term rental need different visit frequencies even on the same square footage. The full {svc('cleaning', 'turf cleaning guide')} covers visit frequency for a standard owner-occupied lot in {city('kissimmee', 'Kissimmee')} or elsewhere in the service area.</p>"),
        ("Pet-odor treatment on a rotating cast of guest dogs",
         "<p>A pet-friendly rental sees more dogs pass through in a season than most owner-occupied households see in years, which means odor buildup in the infill can move faster than the same product would on a private lawn. A deodorizing treatment timed to a deep-clean turnover, rather than waiting for a guest complaint, keeps a pet-friendly listing from developing a reputation problem the property manager only hears about after the fact.</p>"),
        ("What debris looks like near the golf courses and the water",
         f"<p>Lots backing a fairway or a pond along either of {ext('https://www.omnihotels.com/hotels/orlando-championsgate/golf', 'the community’s two courses')} collect a different mix of debris than an interior lot does, occasional grass clippings carried by a mower's discharge, leaf litter from the mature landscaping around a pond edge, and the odd stray ball. None of that requires anything beyond a routine power-brooming and rinse, but it's worth clearing before it works down into the infill and becomes a longer job than a quick pass would have been. "
         f"{post('oak-leaves-and-debris-on-artificial-turf', 'Our notes on oak leaves and yard debris on turf')} cover the same pattern under mature canopy elsewhere in the service area.</p>"),
    ],
    "scenario": (
        "Say you manage a rental villa with 600 sq ft of pet-friendly turf",
        "<p>Say you manage a rental villa with 600 sq ft of pet-friendly turf that turns guests over roughly every five to seven days, with dogs staying about a third of the time. A monthly deep clean plus a lighter rinse-and-brush pass at each pet-guest turnover keeps odor from building between visits, priced by the visit rather than a flat annual number given how much the workload depends on that turnover frequency. Coordinating the deep-clean visits with the property's own cleaning-crew schedule, rather than running two separate vendor visits, is usually the simpler path for a manager juggling more than one address.</p>"
    ),
    "faqs": [
        faq("How often should pet-friendly rental turf get a deep clean in ChampionsGate?",
            "It depends on how many pet stays the property books, but a monthly deep clean with a lighter rinse at each pet-guest turnover is a reasonable starting schedule for a busy vacation rental."),
        faq("Does debris from a nearby golf course require special cleaning?",
            "No. Grass clippings, leaf litter and the occasional stray ball near a fairway-backing lot clear with a routine power-brooming pass, not a specialized treatment."),
    ],
    "sources": SRC,
}

LOCAL["replacement"] = {
    "title": "Turf Removal and Replacement in ChampionsGate, FL",
    "meta": "Turf replacement in ChampionsGate is quoted per job, increasingly relevant as the community's original 1998-era landscaping and first-generation turf age out.",
    "h1": "Replacing worn turf on ChampionsGate's oldest sections",
    "lede": capsule(
        "Turf removal and replacement in ChampionsGate is priced per job rather than off a table, based on how much of the old base can be reused. The community's roots go back to 1998, which puts its earliest sections and any first-generation synthetic turf installed there well into the age range where a base correction, not just a new surface, becomes the real scope of work."
    ),
    "sections": [
        ("A community old enough for its first turf generation to be aging out",
         f"<p>ChampionsGate's Community Development District dates to 1998 "
         f"({ext('https://championsgatecdd.com/', 'per the district’s own site')}), which means any synthetic turf installed in the community's earliest phase is now well past the 10 to 20 year lifespan a well-built system typically reaches, depending on UV stabilization and traffic. A replacement job on one of these older lots often starts with a base inspection rather than an assumption that the original crushed rock is still doing its job, since two decades of settling changes what's underneath more than the worn-out surface on top suggests.</p>"),
        ("Flatwoods soil settles differently than ridge sand over twenty years",
         f"<p>On the Osceola side of ChampionsGate, where flatwoods soils such as Immokalee sit under a seasonally high water table, a base that was fine at installation can settle unevenly after years of wet-season saturation, which shows up as a soft or uneven spot once the old turf comes up. On the Polk-side ridge, where {ext('https://soilseries.sc.egov.usda.gov/OSD_Docs/C/Candler.html', 'Candler sand')} drains excessively rather than holding water, the more common issue at replacement is a base that's washed thin in spots rather than one that's settled soft. Both call for regrading before new turf goes down, just for opposite reasons.</p>"),
        ("What changed in the rules since the original install",
         f"<p>A lot turfed years before May 2026 was built under whatever standard existed at the time, which in most of Osceola and Polk County meant no published local turf rule at all. A replacement project today has to meet the current state standard regardless of what the original installation used, which most often means confirming the infill is a compliant natural material and that any irrigation heads under the old turf were actually capped rather than just buried, since older installs sometimes skipped that step. "
         f"{post('how-long-does-artificial-turf-last-in-florida', 'Our piece on turf lifespan in Florida')} sets expectations for a new system, and {city('championsgate', 'our ChampionsGate area page')} has the rest of the community's local rules in one place, alongside {city('reunion', 'neighboring Reunion')}.</p>"),
    ],
    "scenario": (
        "Say you have 1,100 sq ft of turf installed in ChampionsGate's early years",
        f"<p>Say you have 1,100 sq ft of turf installed in one of ChampionsGate's earliest sections not long after the community's 1998 start, now faded, thin in the high-traffic paths, and showing a soft spot near where an old sprinkler head sits underneath. At {price('residential')} per sq ft, replacement runs $8,800 to $19,800, with the final number depending heavily on whether the base needs a full regrade or just a fresh compacted lift on top of what's still sound. Confirming that old irrigation head is properly capped, not just covered, is a small addition to the job that closes out a two-decade-old shortcut before new turf goes back down on top of it.</p>"
    ),
    "faqs": [
        faq("Does turf from ChampionsGate's original 1998-era construction need full base replacement?",
            "Not always, but it's worth checking rather than assuming. Two decades of settling affects flatwoods and ridge-sand lots differently, and a base inspection before quoting tells us whether a full regrade is needed or just a refresh."),
        faq("Do I need to redo the HOA approval for a replacement, or just the original permit?",
            "Most village boards want a fresh submittal for a replacement project even if the original installation was approved years ago, since the board reviewing it today may not be the same one that approved it originally."),
    ],
    "sources": SRC,
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
