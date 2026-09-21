# -*- coding: utf-8 -*-
"""Kissimmee: city hub + the twelve city x service pages. Kissimmee is the business's home base
(Osceola County seat), so distance is never stated as a drive time here."""
from _helpers import page, capsule, sec, table, faq, ul, steps, note, cta, a, svc, city, county, cs, post, src, ext, price
from _cityservice import cityservice_pages

SLUG = "kissimmee"

SRC = [
    "toho-days", "dep-rule", "hb683", "fs125572", "fs7203045", "olg-720", "stc-fl",
    "attampa-cost", "lbs-fl-cost", "magnolia-pet-cost", "installartificial-pet", "angi-putting", "homeguide-putting", "mightygrass-playground",
    ("City of Kissimmee, Development Services, Building Division, permitting process", "https://www.kissimmee.org/government/development-services-/building-division/permits/-fsiteid-1"),
    ("Osceola County Building Division, online permit records (Accela Citizen Access)", "https://permits.osceola.org/CitizenAccess/Cap/CapHome.aspx?module=Building"),
    ("Osceola County Property Appraiser, parcel search", "https://www.property-appraiser.org/"),
    ("Osceola County, zoning designation lookup", "https://www.osceola.org/My-Property/Zoning-and-Land-Use/Zoning-Designation"),
    ("Osceola County, Short Term Rental Planned Development (STRPD) district", "https://www.osceola.org/My-Property/Zoning-and-Land-Use/Zoning-Designation/STRPD"),
    ("South Florida Water Management District, Upper Kissimmee Basin water supply plan", "https://www.sfwmd.gov/our-work/water-supply/upper-kissimmee"),
    ("South Florida Water Management District, Hurricane Ian response", "https://www.sfwmd.gov/our-work/hurricane-ian"),
    ("USDA NRCS, Official Series Description, Myakka series", "https://soilseries.sc.egov.usda.gov/osd_docs/m/myakka.html"),
    ("USDA NRCS, Official Series Description, Immokalee series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/I/IMMOKALEE.html"),
    ("USDA NRCS, Official Series Description, Smyrna series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/S/SMYRNA.html"),
    ("Florida DEP, soil descriptions appendix (Basinger series)", "https://floridadep.gov/sites/default/files/Soil%20Descriptions%20Appendix_0.pdf"),
    ("Drought.gov, Kissimmee FL climate conditions, NOAA Climate Normals 1991-2020", "https://www.drought.gov/location/34746"),
    ("Osceola History, History of Kissimmee", "https://osceolahistory.org/history-of-kissimmee/"),
    ("Wikipedia, Lake Tohopekaliga", "https://en.wikipedia.org/wiki/Lake_Tohopekaliga"),
    ("Tohoqua, master-planned community, Kissimmee", "https://tohoqua.com/"),
    ("Bellalago HOA", "https://bellalagohoa.com/"),
    ("Remington Golf Club, Kissimmee, FL", "https://www.golfremington.com/"),
    ("Move With Momentum, Kissimmee FL 34741 housing data (Census ACS 5-year estimates)", "https://movewithmomentum.com/data/fl/34741-housing-scorecard"),
    ("Wikipedia, Osceola County Stadium", "https://en.wikipedia.org/wiki/Osceola_County_Stadium"),
    ("ClickOrlando, Osceola County flooding after Hurricane Ian, September 2022", "https://www.clickorlando.com/news/local/2022/09/30/osceola-county-leaders-respond-to-flooding-damage-caused-by-ian/"),
]

HUB = page(
    "/areas/kissimmee/", "city",
    "Artificial Turf Installation in Kissimmee, FL",
    "Kissimmee artificial turf: city vs. county permits, Toho Water's two-day schedule, sandy soil and lakefront setbacks, as of September 2026.",
    "Installing turf on Kissimmee's sand, water table and paperwork",
    capsule(
        f"Kissimmee is home base, the town this crew starts every route from. A residential lawn here runs {price('residential')} per "
        f"square foot installed as of September 2026, but the build changes with the parcel: whether it sits inside city limits or "
        f"unincorporated Osceola County, how close it is to Lake Tohopekaliga, and which Toho Water watering day applies to the address."
    ),
    "".join([
        sec("What's different about a turf install in Kissimmee",
            f"""<p>Kissimmee is the county seat of Osceola County, and the address on a lot does more than set a mailing ZIP. A parcel
            inside the city limits gets its {a('/laws/permits/city-of-kissimmee/', 'permit reviewed by the city')}; a lot a few streets
            over, still carrying a Kissimmee mailing address, often sits in unincorporated Osceola County, where
            {a('/laws/permits/osceola-county/', "a separate county office")} does the same job. Toho Water Authority controls two
            irrigation mornings or evenings a week here, the native ground is fine sand with a water table that climbs close to the
            surface for weeks each summer, and the housing stock ranges from a downtown built on the shore of Lake Tohopekaliga in 1883
            to phases of {ext('https://tohoqua.com/', 'Tohoqua')} still being framed in 2026. Along US-192, whole subdivisions are zoned
            for nightly rentals under the county's short-term-rental overlay, which changes what a {svc('str', 'vacation rental turf')}
            crew plans for before ever pricing the job. None of that moves the {price('residential')} per square foot range for a
            {svc('residential', 'residential lawn')}; it moves the base, the paperwork, and where the state's ten-foot waterbody setback
            actually falls on the lot.</p>"""),
        sec("Does the City of Kissimmee or Osceola County review your permit?",
            f"""<p>It depends on the parcel, not the envelope. Most addresses inside the city limits go through the City of Kissimmee's
            Development Services Building Division, reached at 407-518-2379 or permitting@kissimmee.gov, which reviews site and
            landscape work including turf conversions ({ext('https://www.kissimmee.org/government/development-services-/building-division/permits/-fsiteid-1', 'permitting process')}).
            A good share of properties that say "Kissimmee, FL" on the mail are in unincorporated Osceola County instead, where the
            county's Building Division handles the same review at 407-742-0200, with records searchable online through
            {ext('https://permits.osceola.org/CitizenAccess/Cap/CapHome.aspx?module=Building', 'Accela Citizen Access')}. The fastest way
            to settle which office applies to one specific address is the {ext('https://www.property-appraiser.org/', "Osceola County Property Appraiser's")}
            parcel search, cross-checked against the county's own {ext('https://www.osceola.org/My-Property/Zoning-and-Land-Use/Zoning-Designation', 'zoning designation lookup')};
            both show whether a parcel falls inside the city boundary. Full detail on what each office wants on paper is at
            {a('/laws/permits/city-of-kissimmee/', 'permit rules for the City of Kissimmee')} and
            {a('/laws/permits/osceola-county/', 'permit rules for unincorporated Osceola County')}.</p>"""),
        sec("Kissimmee yard types and what we do differently",
            table(
                "Kissimmee yard types and what changes in the build",
                ["Yard type", "What's typical here", "What changes in the build"],
                [
                    ["Downtown lakefront lot near Lake Tohopekaliga", "Older bungalow or cottage lot, mature live oaks, inside city limits", "Ten-foot waterbody setback, a drip-line check before any digging, city permit review"],
                    ["1980s-2000s pool-cage subdivision", "Screened lanai, St. Augustine sod over a builder-grade base", "Drainage underlay and glue-down edges at the pool deck, HOA architectural review packet"],
                    ["US-192 short-term-rental home", "Resort-style villa inside the county's rental overlay, turned over between guests", "Guest-proof, low-upkeep turf and a cleaning schedule built around checkout instead of a mowing week"],
                    ["New master-planned community", "Zero-lot-line yard, 2019 or newer construction, deed-restricted", "Smaller footprint, tighter equipment access, an ARC drawing filed before work starts"],
                    ["Unincorporated acreage or a septic lot", "Larger parcel outside city limits, well and septic system", "County permit review, turf kept clear of the drainfield with the septic lid left reachable"],
                ],
                f"Every row above still prices inside the {price('residential')} per square foot range. Access, base depth and paperwork move the number, not the ZIP code."
            )),
        sec("What does Toho Water's schedule and Kissimmee's sandy soil mean for a lawn?",
            f"""<p>Toho Water Authority, which serves Kissimmee and most of Osceola County, limits irrigation to two mornings or evenings
            a week: odd-numbered addresses on Wednesday and Saturday, even-numbered addresses on Thursday and Sunday, with no daytime
            watering allowed ({src('toho-days', "Toho's watering-day rules")}). Kissimmee sits in the Kissimmee Basin that the South
            Florida Water Management District manages, part of the same chain of lakes that starts at Lake Tohopekaliga
            ({ext('https://www.sfwmd.gov/our-work/water-supply/upper-kissimmee', 'Upper Kissimmee Basin water supply plan')}). Underneath
            most yards sits fine sand from the Myakka, Immokalee, Smyrna and Basinger series, poorly to very poorly drained soils where
            the water table typically sits twenty to forty inches down for months and can climb within a couple of feet of the surface
            during the wettest weeks of summer. That pairing, tight watering days above ground and a shallow water table below it, is
            part of why {src('dep-rule', "the adopted state turf standard")} bans in-ground irrigation on synthetic turf and calls for a
            washed, open-graded rock base: a lawn here has to shed water on its own, since it isn't getting rinsed by a sprinkler on the
            other five days of the week.</p>"""),
        sec("Which Kissimmee neighborhoods need extra planning?",
            f"""<p>Downtown Kissimmee grew up on the north shore of Lake Tohopekaliga after the city incorporated in 1883, and
            {ext('https://osceolahistory.org/history-of-kissimmee/', 'the historic downtown core')} still carries mature live oaks and
            older lots close to the water, where the setback and drip-line rules both apply before excavation starts. Golf-adjacent
            lots around {ext('https://www.golfremington.com/', 'Remington Golf Club')}, open since 1996, and gated, ARC-reviewed
            communities such as {ext('https://bellalagohoa.com/', 'Bellalago')} on the lake and the newer
            {ext('https://tohoqua.com/', 'Tohoqua')} off Neptune Road add a design-review step most jobs skip entirely. Along US-192,
            {ext('https://www.osceola.org/My-Property/Zoning-and-Land-Use/Zoning-Designation/STRPD', "the county's short-term-rental overlay")}
            runs a district near the theme parks and another closer to the Turnpike, covering resort-style communities where a yard gets
            turned over between guests instead of mowed on a weekly rotation. Compare notes with a neighbor in {city('st-cloud')} or
            {city('buenaventura-lakes')} and the permit answer can differ block to block; {a('/laws/hoa-rules/', 'Florida law')} still
            lets an HOA require design review, it just can't ban turf that isn't visible from the frontage.</p>"""),
        sec("How do you pick the best turf installer near me in Kissimmee?",
            f"""<p>Two questions matter here more than a sales pitch does. First, who is actually filing the paperwork on this job,
            City Hall, the county's Building Division, or a community's architectural review committee, since a contractor who
            hasn't asked which one applies to the address hasn't done the homework yet. Second, how the quote treats a lot backing
            onto a lake, canal or drainage swale: an installer who mentions the ten-foot setback and the drip-line rule without being
            asked has clearly built {a('/laws/', 'the state standard')} into the estimate rather than finding out about it midway
            through the job.</p>"""),
        "<!--AUTO:city-services-->",
    ]),
    faqs=[
        faq("Is a Kissimmee mailing address the same as the city limits?",
            "Not always. Osceola County's largest city sits inside its own boundary, but plenty of addresses reading \"Kissimmee, FL\" sit in unincorporated Osceola County next door. The county Property Appraiser's parcel search and the county's zoning designation lookup both show which office actually reviews a permit for a given parcel."),
        faq("How many days a week can I run a sprinkler on new sod here?",
            "Toho Water Authority allows two irrigation days a week for residential accounts, tied to the address: odd numbers water Wednesday and Saturday, even numbers Thursday and Sunday, with no daytime watering. New sod struggles on that schedule in the dry season; established turf never touches the sprinkler at all, since the adopted state rule bars in-ground irrigation on synthetic turf outright."),
        faq("Can my Kissimmee HOA say no to a backyard nobody can see from the street?",
            "Under Florida Statute 720.3045, an association can't restrict artificial turf that isn't visible from the parcel's frontage or an adjacent lot, so a fenced backyard behind a home in a gated community is generally protected. A front yard is a different conversation, and the community's design review still applies to the paperwork."),
        faq("Does turf near Lake Tohopekaliga need special permission?",
            "In one specific way, yes. The adopted state turf rule keeps synthetic turf at least ten feet from a natural or man-made waterbody, which covers Lake Tohopekaliga, East Lake Tohopekaliga, Shingle Creek and the canals linking them, unless a seawall or bulkhead already separates the yard from the water."),
        faq("What soil should a crew expect to dig into here?",
            "Most Kissimmee lots sit on Myakka, Immokalee, Smyrna or Basinger fine sand, USDA series known for a water table that rises within twenty to forty inches of the surface for months at a stretch. That's why the base calls for washed, open-graded rock instead of compacted fill: a tight base traps water the soil is already holding."),
    ],
    sources=SRC, city=SLUG, crumbs=[("Service areas", "/areas/")], crumb="Kissimmee",
    related=[
        ("/areas/osceola-county/", "Osceola County: the county-wide permit and turf picture"),
        ("/laws/permits/city-of-kissimmee/", "City of Kissimmee permit rules for turf and landscape work"),
        ("/laws/permits/osceola-county/", "Osceola County permit rules for unincorporated parcels"),
        ("/areas/st-cloud/", "Artificial turf in St. Cloud, FL"),
        ("/areas/celebration/", "Artificial turf in Celebration, FL"),
        ("/artificial-turf-cost/", "Turf cost tables for Central Florida"),
    ],
)

LOCAL = {}

# ---------------------------------------------------------------- residential
LOCAL["residential"] = {
    "title": "Artificial Grass Installation in Kissimmee, FL – Sand & Setbacks",
    "meta": "Artificial grass installation in Kissimmee: which office signs the permit, Myakka and Immokalee sand, the ten-foot lake setback, and the September 2026 price range.",
    "h1": "A residential lawn built for Kissimmee's water table and paperwork",
    "lede": capsule(
        f"A residential lawn in Kissimmee installs for {price('residential')} per square foot as of September 2026, typically "
        f"{price('residential', True)}. The number doesn't change with the address; what changes is whether City Hall or Osceola "
        f"County signs the permit, and how deep the base has to run over the fine sand most Kissimmee lots sit on."
    ),
    "sections": [
        ("Which Kissimmee office signs off on a lawn conversion?",
         f"""<p>A straightforward sod-to-turf swap still counts as site and landscape work, and the office that reviews it depends on
         the parcel. Inside city limits, the City of Kissimmee's Development Services Building Division handles it at 407-518-2379;
         outside the boundary, in unincorporated Osceola County, the county's Building Division takes over at 407-742-0200. The
         quickest way to know which applies before calling either number is the Osceola County Property Appraiser's parcel search,
         which lists the taxing jurisdiction for the address. See {a('/laws/permits/city-of-kissimmee/', 'what the city asks for')} and
         {a('/laws/permits/osceola-county/', 'what the county asks for')}; the paperwork differs slightly, the {price('residential')}
         per square foot range doesn't.</p>"""),
        ("What's under a typical Kissimmee lawn before a crew touches it?",
         f"""<p>Most yards here sit on Myakka, Immokalee, Smyrna or Basinger fine sand, poorly drained series where the water table
         commonly sits twenty to forty inches down and rises further during the summer wet season. A downtown lot near Lake
         Tohopekaliga on older fill behaves differently than a slab poured for {ext('https://tohoqua.com/', 'Tohoqua')} in the last few
         years, but both need the same washed, open-graded crushed rock or crushed concrete base, two to four inches, graded one to two
         percent away from the house. Skimping on depth here shows up the first time a summer storm drops an inch of rain in twenty
         minutes, not on installation day.</p>"""),
        ("Where the lake setback and drip-line rule actually apply",
         f"""<p>Kissimmee's shoreline lots and canal-front yards near the {ext('https://en.wikipedia.org/wiki/Lake_Tohopekaliga', 'Kissimmee chain of lakes')}
         fall under the adopted state rule's ten-foot waterbody setback unless a seawall or bulkhead already separates the yard from
         the water. The same rule keeps turf out from under a live oak's drip line without a certified arborist's letter, which matters
         most on the older, tree-shaded lots near downtown rather than a bare new-construction pad in {city('poinciana')} or a
         {city('hunters-creek')} cul-de-sac. Neither rule shows up on a plain interior lot with no canopy and no water view. More on
         what the drip-line rule actually means for a mature oak is in {post('artificial-turf-near-live-oaks-and-palms', "this look at turf and live oak roots")}.</p>"""),
    ],
    "scenario": (
        "Say you have a 900 sq ft backyard behind a 1990s pool-cage home off Michigan Avenue",
        f"""<p>Say you have a 900 sq ft backyard behind a 1990s pool-cage home a few blocks off Michigan Avenue, St. Augustine sod
        thinning out under the oak in one corner and holding water everywhere else after a summer storm. At {price('residential')} per
        square foot, a straightforward rectangle prices between $7,200 and $16,200; at the {price('residential', True)} range most jobs
        actually land in, expect $9,000 to $14,400. The oak corner adds a drip-line check before the crew starts digging, and the
        low spot needs a slightly deeper base rather than more grading, since the sand underneath is already close to its seasonal high
        water table by August. Neither line item shows up on a bid that only quotes square footage.</p>"""
    ),
    "faqs": [
        faq("Do I need a permit just to swap sod for turf in Kissimmee?",
            "Usually yes, since it's still site and landscape work reviewed the same way regrading or a new patio would be, though requirements vary by jurisdiction and job size. Confirm with the City of Kissimmee at 407-518-2379 or Osceola County at 407-742-0200 depending on which one covers the parcel."),
        faq("Does a corner lot near downtown cost more than one in a newer subdivision?",
            "Not because of the neighborhood. An older downtown lot with mature trees and a drip-line check can add planning time, and a newer zero-lot-line yard can mean tighter equipment access; either factor moves a bid more than the ZIP code or the decade a house was built."),
    ],
    "sources": SRC,
}

# ---------------------------------------------------------------- pet
LOCAL["pet"] = {
    "title": "Pet Turf & Dog Runs in Kissimmee, FL – Gated Yards, Fast Base",
    "meta": "Pet turf and dog runs in Kissimmee: zero-lot-line HOA yards, Toho's two-day watering limit, and the September 2026 price range for odor-control turf.",
    "h1": "Dog-run turf sized for Kissimmee's narrow, gated backyards",
    "lede": capsule(
        f"Pet turf in Kissimmee runs {price('pet')} per square foot installed as of September 2026, typically {price('pet', True)}, "
        f"more than a plain lawn because the base runs deeper and the backing has to pass liquid, not just rainwater, on the narrow "
        f"fenced yards common in the city's newer gated communities."
    ),
    "sections": [
        ("Why narrow, gated-community yards drive most Kissimmee pet turf calls",
         f"""<p>Newer, deed-restricted communities such as {ext('https://tohoqua.com/', 'Tohoqua')} and
         {ext('https://bellalagohoa.com/', 'Bellalago')} build on zero-lot-line footprints, which leaves a dog with a narrow fenced
         strip rather than an open yard to patrol. That layout wears a path along the same fence line day after day, and it's exactly
         where a plain residential turf blend mats down fastest. A shorter, denser pet-grade product handles that repeated foot traffic
         better than the taller blend most homeowners picture when they think of {svc('residential', 'a family lawn')}. For the odor
         side of that build, see {post('how-to-get-dog-urine-smell-out-of-artificial-turf', 'how to keep a dog run from smelling by August')}.</p>"""),
        ("What Toho's watering limit has to do with a dog yard",
         f"""<p>Toho Water Authority's two-day-a-week schedule makes it hard to keep sod alive under a yard a dog uses daily, since
         urine spots need more than a twice-weekly soak to recover and the grass never gets the chance. Turf sidesteps that fight
         entirely, and the adopted state standard bars in-ground irrigation on synthetic turf anyway, so the sprinkler heads under a
         converted dog run get capped rather than left to run on Toho's schedule. A hose handles both rinsing and any extra water the
         area needs.</p>"""),
        ("Why the water table changes how a Kissimmee dog run gets built",
         f"""<p>Fine, poorly drained sand and a water table that can sit within a couple of feet of the surface in summer mean a dog
         run needs more base depth than the rest of the yard, not less. Raising the finished grade slightly and using the fuller depth
         the state's washed-rock standard allows keeps a run above that saturation line during Central Florida's wettest months, which
         matters more on a low interior lot in a subdivision than on a raised pad closer to {city('celebration')} or the
         {city('poinciana')} ridge.</p>"""),
    ],
    "scenario": (
        "Say you have a 300 sq ft dog run along the back fence of a zero-lot-line yard",
        f"""<p>Say you have a 300 sq ft dog run along the back fence of a zero-lot-line yard in a newer Kissimmee subdivision, one
        determined lab wearing a visible path from the patio slider to the gate. At {price('pet')} per square foot, that run prices
        between $3,000 and $5,400; at the {price('pet', True)} range most pet jobs land in, expect $3,600 to $4,800. The narrow
        footprint means a crew works mostly by hand rather than with a skid steer, and the deeper base and fully permeable backing a
        dog yard needs add real cost against a same-size patch of plain lawn turf, not padding on the invoice.</p>"""
    ),
    "faqs": [
        faq("Can I install pet turf myself in a Kissimmee HOA community?",
            "Check the architectural review process first. Communities such as Tohoqua and Bellalago route exterior changes, including turf, through a design committee, and Florida Statute 720.3045 only protects turf that isn't visible from the frontage or an adjacent lot, not a fenced yard someone else can see over."),
        faq("Searching for the best pet turf installer near me in Kissimmee for a multi-dog yard?", "Ask specifically how the quote handles base depth and backing permeability, since those two line items, not the visible turf blade, are what separate a pet system from a lawn conversion priced at the same square footage."),
    ],
    "sources": SRC,
}

# ---------------------------------------------------------------- putting
LOCAL["putting"] = {
    "title": "Backyard Putting Greens in Kissimmee, FL – Golf-Lot Builds",
    "meta": "Backyard putting greens in Kissimmee: golf-adjacent lots near Remington, sandy soil for contouring, and the September 2026 installed price range.",
    "h1": "Putting greens contoured for Kissimmee's golf-adjacent lots",
    "lede": capsule(
        f"A backyard putting green in Kissimmee installs for {price('putting')} per square foot as of September 2026, typically "
        f"{price('putting', True)}, with the higher end covering the contouring and fringe work that a golf-adjacent lot near "
        f"Remington Golf Club or a course-view community usually calls for."
    ),
    "sections": [
        ("Golf-adjacent lots and what they ask of a green",
         f"""<p>{ext('https://www.golfremington.com/', 'Remington Golf Club')}, an 18-hole course open in Kissimmee since 1996, anchors
         one of the city's older golf-lot neighborhoods, and course-facing yards elsewhere in town carry the same expectation: a green
         that reads true from multiple cup positions, not a flat patch of turf with a hole cut in it. Contouring, fringe turf and cup
         placement all add labor beyond what a plain {svc('residential', 'lawn conversion')} needs, which is most of the gap between
         the low and high end of the putting-green price range. A fuller cost breakdown is in
         {post('backyard-putting-green-cost-florida', 'how backyard putting green costs break down in Florida')}.</p>"""),
        ("Building a stable base on Kissimmee's fine sand",
         f"""<p>The Myakka and Immokalee fine sand common under Kissimmee yards holds contour reasonably well once compacted, but a
         green asks more of that base than a lawn does, since a soft spot shows up as a dead spot in the roll rather than just a low
         area that puddles. A deeper, more thoroughly compacted washed-rock base under the contoured sections keeps the surface
         predictable through a Central Florida rainy season, when a lawn's base only has to shed water, not hold a shape.</p>"""),
        ("Space, HOA review and where a green actually fits",
         f"""<p>A course-adjacent lot often has the open backyard a green needs, but it also usually sits inside a homeowners
         association with a design-review step before work starts, on top of whichever office, city or county, reviews the permit
         itself. A tighter interior lot in {city('buenaventura-lakes')} or a Kissimmee subdivision without a golf view can still fit a
         smaller two- or three-cup layout; it just changes the shape of the green rather than ruling it out.</p>"""),
    ],
    "scenario": (
        "Say you have a 500 sq ft green with two cups behind a course-facing lot",
        f"""<p>Say you have a 500 sq ft green with two cups and a chipping fringe behind a course-facing lot near Remington. At
        {price('putting')} per square foot, that scope prices between $7,000 and $15,000; at the {price('putting', True)} range most
        contoured builds land in, expect $9,000 to $12,500. Two breaks worked into the surface and a fringe cut around both cups sit
        toward the top of that range, while a flat single-cup practice green of the same size would land closer to the bottom, since
        contouring is the labor line that moves a putting-green quote more than material choice does.</p>"""
    ),
    "faqs": [
        faq("Do golf-adjacent Kissimmee communities require HOA approval for a green?",
            "Most do, since a putting green is a visible exterior change even when it sits behind the house. Expect to submit a sketch showing the green's footprint and cup locations alongside whatever permit paperwork the city or county requires for the parcel."),
        faq("What is the best putting green option for a small Kissimmee backyard?",
            "A single-cup, two-break layout in the 300 to 400 sq ft range usually fits a standard interior lot without crowding the rest of the yard, and it still needs the same contoured base as a larger course-facing green."),
    ],
    "sources": SRC,
}

# ---------------------------------------------------------------- playground
LOCAL["playground"] = {
    "title": "Playground Turf in Kissimmee, FL – Shaded, Cushioned Yards",
    "meta": "Playground turf for Kissimmee backyards: shock-pad sizing for pool-cage-era lots, shade near Lake Toho's open sun, and the September 2026 price range.",
    "h1": "Cushioned play turf for Kissimmee's sunniest backyards",
    "lede": capsule(
        f"Playground turf in Kissimmee installs for {price('playground')} per square foot as of September 2026, typically "
        f"{price('playground', True)}, with the shock pad sized to the play equipment's fall height rather than the size of the yard "
        f"around it."
    ),
    "sections": [
        ("Where families are already asking for it",
         f"""<p>Kissimmee's park system, anchored by {ext('https://osceolahistory.org/history-of-kissimmee/', 'the historic downtown lakefront')}
         and its own playground on Lake Tohopekaliga, sets a visible bar for what a swing set and slide area should feel like, and a lot
         of the calls for backyard play turf come from parents who want that same cushioned, mud-free surface at home instead of a trip
         across town. A 1980s or 1990s pool-cage subdivision lot usually has the flat, open footprint a small play area needs without
         much regrading.</p>"""),
        ("Sizing the shock pad for real Central Florida sun",
         f"""<p>A play structure's fall height sets the shock pad thickness, not the homeowner's preference, and Kissimmee's mostly
         treeless newer-subdivision yards see more direct summer sun than a shaded downtown lot near mature oaks. Full sun pushes turf
         surface temperature into the 120 to 150°F range and occasionally past 160°F, so a play area with no shade structure at all
         benefits from a lighter-colored or cooling infill on top of whatever pad thickness the equipment calls for. A rundown of
         which products handle that best is in {post('coolest-artificial-grass-and-infill-for-florida', 'the coolest turf and infill options for Florida sun')}.</p>"""),
        ("Fitting a play area around a pool cage or a small lot",
         f"""<p>Plenty of Kissimmee backyards built between the 1980s and 2000s already give up most of the footprint to a screened
         pool enclosure, which leaves a play area to fit into whatever's left, often a side strip or a corner rather than a wide-open
         lawn. That tighter shape doesn't change the shock-pad math, but it does mean more cutting and edging labor than a play area
         dropped into an open lot in a newer part of town.</p>"""),
    ],
    "scenario": (
        "Say you have a 250 sq ft play corner beside a screened pool cage",
        f"""<p>Say you have a 250 sq ft play corner beside a screened pool cage, a swing set with a five-foot fall height and full
        afternoon sun for most of the day. At {price('playground')} per square foot, that area prices between $2,500 and $6,250; at the
        {price('playground', True)} range most residential play areas land in, expect $3,000 to $4,750. The fall height sets a shock
        pad thick enough to matter, and the sun exposure makes a lighter-colored infill worth the small add against standard silica,
        since the surface underneath a swing set gets touched by small hands and knees more than any other patch of turf on the lot.</p>"""
    ),
    "faqs": [
        faq("How thick does the shock pad need to be for a home swing set in Kissimmee?",
            "It's set by the equipment's fall height under ASTM guidance, not by preference, so the manufacturer's spec sheet for the specific swing set or slide is the starting point before ordering pad material."),
        faq("Does a shaded Kissimmee lot near mature oaks need less cooling infill?",
            "Often yes, since shade from live oaks keeps surface temperatures well below a treeless yard's peak, though the drip-line rule still applies if the play area sits close enough to the trunk to reach the canopy's edge."),
    ],
    "sources": SRC,
}

# ---------------------------------------------------------------- pool
LOCAL["pool"] = {
    "title": "Pool & Lanai Turf in Kissimmee, FL – Pool-Cage Homes",
    "meta": "Pool and lanai turf for Kissimmee's screened pool-cage homes: glue-down edges, drainage underlay over concrete, and the September 2026 price range.",
    "h1": "Turf for the deck sod never grew around in Kissimmee's pool cages",
    "lede": capsule(
        f"Turf around a pool or inside a screen enclosure in Kissimmee prices at the residential rate, {price('residential')} per "
        f"square foot installed as of September 2026, typically {price('residential', True)}, since it's the small, tight-access "
        f"areas rather than the material that push a lanai job toward the top of that range."
    ),
    "sections": [
        ("Why so much of Kissimmee's pool turf work is inside a screen cage",
         f"""<p>Kissimmee's housing stock is thick with 1980s-through-2000s subdivisions built with a screened pool enclosure as
         standard, and grass never really takes hold on the narrow strip of ground between the pool deck and the screen frame. Low
         light along the cage wall, mower access that's nearly impossible in a space that width, and constant splash-out from swimmers
         all work against sod in a way they don't against turf, which is why lanai conversions make up a steady share of Kissimmee
         calls independent of a homeowner's HOA situation.</p>"""),
        ("Building over concrete instead of soil",
         f"""<p>Most Kissimmee lanai turf goes down over an existing concrete pool deck rather than native fine sand, which flips the
         usual build: instead of washed rock for drainage, the job needs a purpose-built drainage underlay between the slab and the
         turf backing so pool splash-out and rain both have somewhere to go besides pooling on hard concrete. Edges get glued rather
         than nailed, since there's no soil to anchor a perimeter stake into, and any expansion joint in the slab still needs to be
         accounted for so the turf doesn't tent or wrinkle as the concrete moves with temperature. Reflected heat off a screen frame
         or a nearby window is its own risk, covered in {post('can-artificial-turf-melt', 'when artificial turf can actually melt')}.</p>"""),
        ("Where the HOA and state rules land on a lanai",
         f"""<p>A screened enclosure is often the one part of a Kissimmee yard that genuinely isn't visible from the street or an
         adjacent lot, which is the exact test Florida Statute 720.3045 uses for what an association can and can't restrict, so a lanai
         conversion in a design-reviewed community such as {ext('https://bellalagohoa.com/', 'Bellalago')} sometimes clears review more
         easily than a front-yard change would. The adopted state turf rule's irrigation ban still applies inside the cage, so any
         sprinkler head that used to reach the pool bed gets capped rather than left running under the new surface.</p>"""),
    ],
    "scenario": (
        "Say you have a 400 sq ft ring of turf inside a screened pool cage",
        f"""<p>Say you have a 400 sq ft ring of turf between the pool deck's edge and the screen frame of a 1990s Kissimmee pool home,
        concrete underneath the whole footprint and a narrow gate that rules out anything wider than a wheelbarrow. Priced at the
        residential rate of {price('residential')} per square foot, that scope runs $3,200 to $7,200; most jobs like it land in the
        {price('residential', True)} range, or $4,000 to $6,400. The narrow gate access and the glue-down edging against concrete, not
        the turf itself, are what push a job like this toward the upper half of that range rather than the lower half a same-size
        open-yard lawn would land in.</p>"""
    ),
    "faqs": [
        faq("Can turf go directly over an existing pool deck in Kissimmee?",
            "Yes, over concrete, but it needs a drainage underlay between the slab and the turf backing plus glued rather than nailed edges, since there's no soil underneath to anchor a perimeter stake."),
        faq("Does a screened lanai still need to follow the state's setback rule if it's near a pond?",
            "Yes. A pool cage that sits within ten feet of a natural or man-made waterbody still falls under the adopted state rule's setback unless a seawall or bulkhead already separates the enclosure from the water."),
        faq("Who reviews the permit for a lanai turf job, the city or the county?",
            "Whichever office reviews the rest of the parcel's permits. Confirm the jurisdiction with the Osceola County Property Appraiser's parcel search before assuming a Kissimmee mailing address means a city permit."),
    ],
    "sources": SRC,
}

# ---------------------------------------------------------------- str
LOCAL["str"] = {
    "title": "Vacation Rental Turf in Kissimmee, FL – US-192 Corridor",
    "meta": "Vacation rental turf for Kissimmee's US-192 short-term-rental overlay: guest-proof builds, turnover scheduling, and the September 2026 price range.",
    "h1": "Guest-proof turf for Kissimmee's short-term-rental corridor",
    "lede": capsule(
        f"Vacation-rental turf in Kissimmee prices at the residential rate, {price('residential')} per square foot installed as of "
        f"September 2026, typically {price('residential', True)}, sized for the resort-style yards along US-192 that get walked by a "
        f"new group of guests most weeks of the year."
    ),
    "sections": [
        ("Why the US-192 corridor is its own category",
         f"""<p>Osceola County's short-term-rental overlay runs two zones, one near the theme parks and one closer to the Turnpike, and
         inside them entire subdivisions such as Storey Lake are built and licensed specifically for nightly rentals rather than
         long-term residents. A yard in that overlay gets walked by a new set of guests most weeks of the year instead of the same
         family every day, which changes what "durable" means: turf here has to survive suitcase wheels and pool-deck traffic on a
         weekly cycle, not settle in slowly under one household's routine.</p>"""),
        ("What the county actually requires before a yard is a rental",
         f"""<p>Short-term rentals in Osceola County are only permitted inside a designated overlay zone or a short-term-rental planned
         development, and an owner still needs a state Vacation Rental license from Florida's Division of Hotels and Restaurants plus a
         county local business tax receipt before listing the property. None of that paperwork covers the yard itself, but confirming
         the zoning first, through the county's own zoning designation lookup, matters more here than on a standard
         {svc('residential', 'owner-occupied lawn')}, since turf added to a property outside the overlay doesn't change what the
         property is allowed to be used for.</p>"""),
        ("Building for turnover instead of a weekly mow",
         f"""<p>A rental yard gets serviced on the same schedule as the housekeeping turnover, not a mowing calendar, so the build
         favors a denser, more traffic-resistant blend over the taller pile a homeowner might pick for looks. Keeping the design simple,
         a plain rectangle rather than tight curves around landscaping, also matters more here than on an owner-occupied lot, since a
         property manager coordinating a same-day clean-and-inspect has less flexibility to work around an odd-shaped yard than a
         homeowner does. What a first installation day actually involves is covered generally in
         {post('what-to-expect-on-turf-installation-day', 'what to expect on turf installation day')}.</p>"""),
    ],
    "scenario": (
        "Say you have a 700 sq ft rental backyard with a pool deck off US-192",
        f"""<p>Say you have a 700 sq ft rental backyard with a pool deck off US-192, booked most weekends of the year and cleaned
        between every stay. At the residential rate of {price('residential')} per square foot, that yard prices between $5,600 and
        $12,600; most rental-home jobs land in the {price('residential', True)} range, or $7,000 to $11,200. A simple rectangular layout
        keeps the turnover crew's job easy and the install cost down, while a yard with a fire pit, curved beds and a side path adds
        cutting time that shows up on both the install invoice and every future turf-repair visit.</p>"""
    ),
    "faqs": [
        faq("Does a vacation rental need a different turf product than a family lawn?",
            "Not a different material category, but a denser, shorter pile handles repeated guest traffic and suitcase wheels better than a taller residential blend, similar to the reasoning behind a dedicated dog-run product."),
        faq("What separates the best turf company near me from an average bid on a Kissimmee rental?", "Whether the quote accounts for turnover-day servicing access. A property manager coordinating same-day cleaning crews needs a yard that a repair or rinse visit won't disrupt for long, which a bid built for an owner-occupied home rarely addresses."),
        faq("Is my Kissimmee property zoned for short-term rental in the first place?", "Only if it falls inside the county's short-term-rental overlay or a short-term-rental planned development; the county's own zoning designation lookup confirms this before any turf or licensing decision is worth making."),
    ],
    "sources": SRC,
}

# ---------------------------------------------------------------- commercial
LOCAL["commercial"] = {
    "title": "Commercial Turf in Kissimmee, FL – HOA & Resort Common Areas",
    "meta": "Commercial turf in Kissimmee: HOA common areas, resort clubhouse lawns near US-192, apartment pet parks, and city vs. county permit review.",
    "h1": "Common-area turf for Kissimmee's HOAs, resorts and apartments",
    "lede": capsule(
        "Commercial turf in Kissimmee is quoted per job from a site walk or a set of drawings, not a flat per-square-foot number, "
        "since a clubhouse lawn, an apartment pet park and an HOA entrance island each carry different access, drainage and permit "
        "requirements even inside the same zip code."
    ),
    "sections": [
        ("Where Kissimmee commercial turf calls actually come from",
         f"""<p>A lot of demand comes from the same resort-style communities that drive {svc('str', 'vacation-rental turf')} along
         US-192, where a clubhouse lawn, pool deck and entrance median all see far more foot traffic than any single homeowner's yard
         and need a surface that holds up to it without a maintenance crew mowing weekly. Gated, ARC-governed communities such as
         {ext('https://bellalagohoa.com/', 'Bellalago')} also maintain common-area turf separately from what any individual homeowner
         installs behind their own fence, which is a different scope and a different point of contact than a residential quote.</p>"""),
        ("Apartment pet parks and a different kind of wear",
         f"""<p>Apartment communities along the 192 corridor and near the city's newer growth areas increasingly carve out a dedicated
         pet relief area rather than letting residents use a shared lawn, and that area sees the same daily-use, odor-control demands
         as a single-family {svc('pet', 'dog run')}, just at a much larger scale and with dozens of dogs instead of one. Sizing the
         base and backing for that volume of use matters more than it would on a single home's dog yard, since there's no slow season
         to let the ground recover.</p>"""),
        ("Permitting a commercial job in Kissimmee versus a residential one",
         f"""<p>Commercial site work inside the city limits goes through the same Development Services Building Division that reviews
         residential permits, while a commercial property in unincorporated Osceola County goes through the county's Building Division
         instead, the same jurisdiction split that applies to a homeowner's backyard. A commercial job usually also means a formal site
         plan rather than a simple sketch, particularly for anything touching stormwater, parking or a shared common area governed by
         an association. The same five spec lines a homeowner should ask for still apply here, laid out in
         {post('how-to-compare-artificial-turf-quotes', 'how to compare two turf quotes line by line')}, just against a bigger site plan.</p>"""),
    ],
    "scenario": (
        "Say you have a 2,000 sq ft apartment pet park near an entrance off US-192",
        f"""<p>Say you have a 2,000 sq ft apartment pet park planned near a property entrance off US-192, expected to see daily use from
        residents across several buildings rather than one household's dog. A job at that scale is priced from a site walk rather than
        a flat per-square-foot figure, since the base depth, backing permeability and infill volume all scale up from a residential dog
        run rather than simply multiplying a homeowner's price per square foot by the larger area. Drainage capacity and where runoff
        goes once it leaves the pet park both need to be worked out before a number goes on paper, since a property this size can't
        rely on a hose rinse the way a single backyard can.</p>"""
    ),
    "faqs": [
        faq("How is Kissimmee commercial turf priced if there's no per-square-foot rate?",
            "From a site walk or a set of drawings, since access, drainage capacity, expected foot traffic and whether the area serves one building or several all change the base and backing spec more than they would on a single-family yard."),
        faq("Does an HOA common area in Kissimmee need the same permit as a resident's backyard?",
            "The same office reviews it, city or county depending on the parcel, but a common-area job usually needs a fuller site plan than a homeowner's sketch, especially where stormwater or shared parking is involved."),
    ],
    "sources": SRC,
}

# ---------------------------------------------------------------- sports
LOCAL["sports"] = {
    "title": "Sports & Fitness Turf in Kissimmee, FL – Home Training Areas",
    "meta": "Sports and fitness turf in Kissimmee: home batting cages, bocce courts and sled tracks, sized for pool-cage lots and priced per job.",
    "h1": "Home sports turf for a town built around organized sport",
    "lede": capsule(
        "Sports and fitness turf in Kissimmee, a bocce court, a batting cage lane or a home-gym sled track, is quoted per job from "
        "the equipment and layout involved rather than a flat per-square-foot rate, since a sled lane and a bocce court need "
        "completely different base and pile specs."
    ),
    "sections": [
        ("A town with a sports history to build on",
         f"""<p>Kissimmee spent three decades as the Houston Astros' spring-training home at
         {ext('https://en.wikipedia.org/wiki/Osceola_County_Stadium', 'Osceola County Stadium')}, from 1985 until the team moved to
         Palm Beach County in 2017, and the stadium site is still an active sports venue today as part of Osceola Heritage Park. That
         history shows up now mostly as backyard demand, batting cages and agility lanes for kids in local leagues, home sled tracks
         for adults training on their own, rather than any connection to the old ballpark itself.</p>"""),
        ("Fitting a training surface into a Kissimmee pool-cage lot",
         f"""<p>Plenty of the yards asking for a sled track or an agility lane are the same 1980s-through-2000s pool-cage lots that
         drive {svc('pool', 'lanai turf')} demand, which means the usable straight-line run is often a side yard or the strip beside
         the screen enclosure rather than an open backyard. A short, dense, high-face-weight product handles repeated sled drags and
         cleat traffic better than a taller residential blend, and that density matters more on a narrow side-yard lane than it would
         on a wide-open rural lot. Terms like face weight and pile height are defined in
         {post('artificial-turf-glossary', 'the artificial turf glossary')}.</p>"""),
        ("Why the base runs deeper for sports use than for a lawn",
         f"""<p>A sled lane or a batting-cage pad sees concentrated, repeated impact in the same few square feet rather than the
         general foot traffic a lawn gets, and Kissimmee's fine, poorly drained sand needs a firmer, more thoroughly compacted base
         under that kind of load to avoid rutting over time. That's closer to how a putting green's base gets built than a plain
         residential lawn, even though the finished surface and pile height are completely different.</p>"""),
    ],
    "scenario": (
        "Say you have a 12x40 ft sled and agility lane beside a screened pool cage",
        f"""<p>Say you have a 12x40 ft sled and agility lane running beside the screen enclosure of a Kissimmee pool home, 480 sq ft
        total on ground that used to be plain St. Augustine nobody could mow close enough to the fence line anyway. A lane like this is
        priced from the layout and expected training load rather than a flat per-square-foot figure, since a dense, high-face-weight
        product and a firmer compacted base both cost more per square foot than a comparable stretch of family lawn would, even before
        counting the extra grading needed to keep a narrow side yard level end to end.</p>"""
    ),
    "faqs": [
        faq("What sports turf projects come up most often in Kissimmee?",
            "Home batting cages and agility lanes for kids in local leagues, plus sled and fitness lanes for adults training at home, most often fitted into a side yard or the strip beside a screened pool cage rather than a full backyard."),
        faq("Does a home sports surface need a different base than a lawn conversion?",
            "Yes. Repeated impact in the same footprint, from a sled drag or cleats, needs a firmer, more thoroughly compacted base than a lawn's, closer to what a contoured putting green requires than what a plain residential yard needs."),
    ],
    "sources": SRC,
}

# ---------------------------------------------------------------- pavers
LOCAL["pavers"] = {
    "title": "Turf & Pavers in Kissimmee, FL – Driveways & Walking Paths",
    "meta": "Turf between pavers in Kissimmee: driveway strips on newer subdivision lots, walking-path ribbons, and how the septic and setback rules apply.",
    "h1": "Turf ribbons for Kissimmee's paver driveways and paths",
    "lede": capsule(
        "Turf set between pavers in Kissimmee, a driveway strip, a stepping-stone path or a border around a patio, is quoted per "
        "job since the paver layout and cut count decide the cost far more than the total square footage does."
    ),
    "sections": [
        ("Where paver-and-turf combinations show up around town",
         f"""<p>Newer master-planned communities such as {ext('https://tohoqua.com/', 'Tohoqua')} lean on paver driveway aprons and
         walking-trail edging as part of the standard build, which leaves a narrow turf ribbon running between the pavers and the lot
         line that's too tight for a mower to cut cleanly. Older downtown lots near {ext('https://osceolahistory.org/history-of-kissimmee/', 'historic Kissimmee')}
         see the same problem from a different angle, a brick or paver walkway laid decades ago with grass strips beside it that never
         filled in evenly under mature shade trees.</p>"""),
        ("Why the cut count matters more than the square footage",
         f"""<p>A driveway strip or a stepping-stone path is mostly edges, every paver joint and every curve is another cut in the
         turf, so a small paver-and-turf job can take longer per square foot than an open {svc('residential', 'backyard lawn')} many
         times its size. Grain direction matters here too, since turf comes in rolls that all lean one way, and a ribbon that snakes
         around a curved paver path needs the pieces planned out before cutting starts so the direction reads consistently end to
         end.</p>"""),
        ("Septic fields and side-yard access on a paver strip",
         f"""<p>On a lot outside city limits with its own septic system, a paver-and-turf path or driveway border has to stay clear of
         the drainfield and leave the septic lid reachable for pump-out, the same requirement the adopted state turf rule applies to a
         full lawn conversion. A narrow side-yard gate common on older Kissimmee lots also means paver material and turf rolls often
         get moved in by hand rather than machine, which is worth asking about before assuming a small job means a quick one. The same
         logic applies to turf laid over an existing paver patio, covered in
         {post('install-artificial-turf-over-concrete-pavers-or-grass', 'installing turf over concrete, pavers or existing grass')}.</p>"""),
    ],
    "scenario": (
        "Say you have a 60 ft paver driveway apron with turf ribbons on both sides",
        f"""<p>Say you have a 60 ft paver driveway apron on a Kissimmee subdivision lot, turf ribbons about a foot wide running along
        both edges where a mower can't get a clean cut against the pavers. The job is priced from the linear footage and the number of
        paver-edge cuts rather than a simple square-foot rate, since two long, narrow strips with dozens of joints to trim around take
        more labor time than the small total area suggests. A straight paver line with square joints prices faster than a curved
        walkway with irregular stones, even at the same total square footage.</p>"""
    ),
    "faqs": [
        faq("Is turf between pavers cheaper than turfing a whole yard in Kissimmee?",
            "Not per square foot. A narrow ribbon with many paver-joint cuts often costs more per square foot than an open lawn of the same total area, since cutting and edging labor, not material, drives the price on a job shaped like this."),
        faq("Does a septic system change where turf can go between pavers?",
            "Yes, on lots outside city limits with their own septic system. The path or border has to avoid the drainfield and leave the tank's access lid reachable, the same rule that applies to a full-yard turf conversion."),
    ],
    "sources": SRC,
}

# ---------------------------------------------------------------- repair
LOCAL["repair"] = {
    "title": "Turf Repair in Kissimmee, FL – Storm and Age Damage",
    "meta": "Artificial turf repair in Kissimmee: storm-lifted edges after events like Hurricane Ian, aging infill from before the 2026 state rule, quoted per visit.",
    "h1": "Fixing what storms and time do to Kissimmee turf",
    "lede": capsule(
        "Turf repair in Kissimmee, an open seam, a lifted edge, a melted spot or a drainage complaint, is quoted per visit rather "
        "than by the square foot, since most repair calls involve a small area and a diagnosis first."
    ),
    "sections": [
        ("What storm exposure does to turf edges here",
         f"""<p>Hurricane Ian dropped roughly a foot of rain on the Kissimmee area over about a day and a half in September 2022,
         flooding an estimated 1,700 structures citywide and pushing {ext('https://en.wikipedia.org/wiki/Lake_Tohopekaliga', 'Lake Tohopekaliga')}
         and nearby canals well above normal ({ext('https://www.sfwmd.gov/our-work/hurricane-ian', "the South Florida Water Management District's Hurricane Ian response")}).
         A yard that saw water rise that high often comes out the other side with a lifted perimeter edge or a seam that's started to
         gap, even when the turf itself never went underwater, since standing water around a poorly anchored edge softens the adhesive
         over time. More on what a major storm does to a yard is in
         {post('artificial-turf-hurricane-flooding', 'what happens to artificial turf in a hurricane or flood')}.</p>"""),
        ("Repairing turf installed before the state's 2026 material rule",
         f"""<p>Turf put down in Kissimmee before {src('dep-rule', "the adopted state synthetic turf standard")} took effect in May
         2026 sometimes used infill or backing that wouldn't meet today's requirements, most commonly a rubber crumb infill on a home
         lawn rather than the natural-material infill the rule now calls for. A repair visit on an older lawn is a natural point to
         swap that infill for silica sand or zeolite, even though the rule itself only reaches new installations and doesn't require
         retrofitting an existing yard.</p>"""),
        ("Why an older downtown lot repairs differently than a newer one",
         f"""<p>A lawn installed years ago near Kissimmee's older, tree-shaded neighborhoods has usually had more root movement and
         leaf litter working into the base than a lawn in a subdivision built in the last five years, and root intrusion under an aging
         base is a more common repair call downtown than a simple seam failure is. Diagnosing which one it is, drainage, roots or just a
         worn seam, decides whether a repair visit fixes it in an hour or turns into a partial {svc('replacement', 'section replacement')}.</p>"""),
    ],
    "scenario": (
        "Say you have a 15 ft stretch of lifted edge after a summer storm",
        f"""<p>Say you have a 15 ft stretch of lifted turf edge along a fence line after a summer storm, the perimeter nails pulled
        loose and water pooling under the gap instead of draining through. A repair visit like this is priced by the job rather than by
        the square foot, since the fix is mostly labor, re-securing the edge and checking whether the base underneath washed out or
        just shifted, not new material. Catching it within a season or two of the storm keeps the repair small; left alone through a
        second rainy season, the same gap tends to spread and pull more of the seam with it.</p>"""
    ),
    "faqs": [
        faq("Does homeowners insurance cover storm-damaged turf in Kissimmee?",
            "It depends on the policy and the cause, so check with the carrier directly rather than assuming either way; a lifted edge from wind is a different claim than turf sitting under floodwater for days."),
        faq("Is it worth swapping old rubber infill for silica during a repair visit?",
            "Often yes for a pet or play lawn, since the adopted state rule now limits new residential infill to natural materials, and a repair visit that already has the turf pulled back is the easiest time to make that swap."),
    ],
    "sources": SRC,
}

# ---------------------------------------------------------------- cleaning
LOCAL["cleaning"] = {
    "title": "Turf Cleaning & Maintenance in Kissimmee, FL – Humidity & Pets",
    "meta": "Artificial turf cleaning in Kissimmee: pet-odor treatment for gated-community dog yards, humidity near Lake Toho, quoted by yard size and condition.",
    "h1": "Keeping Kissimmee turf clean through heat, humidity and pets",
    "lede": capsule(
        "Turf cleaning in Kissimmee, pet-odor treatment, power brooming, sanitizing and infill top-ups, is quoted by yard size and "
        "how long it's been since the last service, not a flat rate, since a neglected dog yard takes longer than routine "
        "upkeep."
    ),
    "sections": [
        ("Why humidity near the lakes changes a cleaning schedule",
         f"""<p>Yards close to Lake Tohopekaliga, Shingle Creek or one of Kissimmee's canals sit in some of the most humid pockets of
         an already humid city, and that damp air slows how fast a turf surface dries out after a rinse or a storm. A shaded lawn near
         the water that stays damp longer is more prone to the mildew smell homeowners sometimes mistake for pet odor, and the fix,
         more frequent power brooming and better airflow at ground level, differs from what an odor problem on a sun-baked interior lot
         actually needs.</p>"""),
        ("Pet-odor service in Kissimmee's gated communities",
         f"""<p>The narrow, fenced dog yards common in newer gated communities such as {ext('https://tohoqua.com/', 'Tohoqua')}
         concentrate pet traffic onto a small footprint, which means zeolite or coated-sand infill in those yards depletes faster than
         the same infill on an open family lawn and needs checking more often. A {svc('pet', 'dedicated dog run')} on that kind of lot
         usually needs an odor-treatment visit on a tighter schedule than the plain lawn beside it, even when both were installed the
         same week with the same product.</p>"""),
        ("What builds up in an older Kissimmee lawn's infill",
         f"""<p>A lawn installed years ago near the city's older tree canopy collects oak leaf litter and pollen into the infill layer
         at a rate a newer subdivision's turf, with less mature shade overhead, doesn't see nearly as much. That buildup slows drainage
         gradually rather than all at once, so a lawn that seemed fine at the last visit can show up noticeably slower to clear a rinse
         a year later, which is usually a sign it's due for a deeper clean rather than a repair. Debris under mature canopy is covered
         directly in {post('oak-leaves-and-debris-on-artificial-turf', 'clearing oak leaves and pine needles off artificial turf')}.</p>"""),
    ],
    "scenario": (
        "Say you have an 800 sq ft shaded lawn near a canal that's gone two years without service",
        f"""<p>Say you have an 800 sq ft shaded lawn near a Kissimmee canal that hasn't had a cleaning visit in about two years, oak
        leaf litter worked into the infill and a faint mildew smell along the fence line that isn't from a pet. A yard in that condition
        takes longer to service than a routine seasonal visit, since power brooming has to lift compacted debris out of the pile before
        infill top-up and any odor treatment can actually reach the base underneath. Getting on a regular schedule after that first
        deeper clean, rather than waiting another two years, keeps future visits closer to routine maintenance than a full reset.</p>"""
    ),
    "faqs": [
        faq("How often should turf near Lake Tohopekaliga be cleaned compared to an inland lot?",
            "More often in most cases, since higher humidity near the water slows drying time after rain and makes mildew-related odor more likely than on a sun-exposed inland yard, independent of whether pets are involved."),
        faq("Can a mildew smell near a Kissimmee canal be mistaken for pet odor?",
            "Yes, and the fix differs. Mildew responds to better airflow and more frequent power brooming, while pet odor responds to infill choice and rinse frequency, so an accurate diagnosis before treatment saves a wasted service visit."),
    ],
    "sources": SRC,
}

# ---------------------------------------------------------------- replacement
LOCAL["replacement"] = {
    "title": "Turf Removal & Replacement in Kissimmee, FL – Aging Lawns",
    "meta": "Turf removal and replacement in Kissimmee: correcting an old base under Myakka sand, updating infill to the 2026 state standard, quoted per job.",
    "h1": "Replacing worn-out turf on Kissimmee's older installs",
    "lede": capsule(
        "Turf removal and replacement in Kissimmee is quoted per job once the base underneath is inspected, since how much of the "
        "old base can be reused, and how much has to come out with the worn turf, decides most of the cost."
    ),
    "sections": [
        ("Why so many replacement calls trace back to the base, not the turf",
         f"""<p>A lawn installed a decade or more ago on Kissimmee's Myakka or Immokalee fine sand often shows its age at the base
         level before the visible turf looks worn out, low spots where fines migrated into the rock over the years and slowed
         drainage, or a perimeter that settled unevenly as the sand beneath it shifted with the seasonal water table. Pulling the old
         turf back is also the only real way to see whether that base is worth keeping or needs to be rebuilt from bare soil up. General
         lifespan expectations are in {post('how-long-does-artificial-turf-last-in-florida', 'how long artificial turf lasts in Florida')}.</p>"""),
        ("Bringing an older lawn up to today's material standard",
         f"""<p>A yard turfed years before {src('dep-rule', "the state's synthetic turf rule")} took effect in May 2026 may have been
         built with unwashed fill or a rubber-based infill that wouldn't meet today's residential standard, and a full replacement is
         the natural point to correct both, washed open-graded rock this time, natural-material infill instead of crumb rubber. None of
         that is required on an existing lawn that isn't being touched, but it's worth doing once the turf is already coming up.</p>"""),
        ("What changes on a replacement near water or mature trees",
         f"""<p>A replacement on a shoreline lot near Lake Tohopekaliga or a canal gets rechecked against the ten-foot setback the same
         way a brand-new install would, since older turf installed before the rule existed may sit closer to the water than a new job
         would be allowed to. The same goes for a live oak that's grown significantly since the original install; a drip line that
         wasn't a factor a decade ago can be one now, which sometimes reshapes the replacement footprint rather than just swapping
         material like-for-like.</p>"""),
    ],
    "scenario": (
        "Say you have a 1,100 sq ft lawn installed twelve years ago with a settled low corner",
        f"""<p>Say you have a 1,100 sq ft lawn installed roughly twelve years ago on the edge of a Kissimmee subdivision, one low
        corner that's held water after every storm for the last few summers and a seam nearby that's started to separate. Replacement
        pricing here depends on how much of that base is salvageable once the old turf comes up: if the rock underneath the good two-
        thirds of the yard is still sound, only the low corner needs full excavation and a rebuilt base, while a section that's clearly
        healthy gets new turf laid straight over the reused rock. That inspection, not a flat area calculation, is what a replacement
        quote is actually built from.</p>"""
    ),
    "faqs": [
        faq("Is replacing old turf cheaper than the original installation was?",
            "It can be, if most of the existing base is sound and only needs cleaning and releveling rather than full excavation, but a base with drainage problems or settling usually costs close to a new install once it's rebuilt properly."),
        faq("Does old turf near Lake Tohopekaliga need to move further from the water when it's replaced?",
            "Sometimes. If the original install predates the current ten-foot setback and sits closer to the water than that, a replacement is a natural point to pull the new footprint back to meet today's rule."),
    ],
    "sources": SRC,
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
