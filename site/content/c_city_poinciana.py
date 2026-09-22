# -*- coding: utf-8 -*-
"""Poinciana, FL city hub + city x service pages."""
from _data import CITIES
from _helpers import page, capsule, sec, table, faq, a, svc, city, post, src, ext, price
from _cityservice import cityservice_pages

SLUG = "poinciana"
MILES = CITIES[SLUG]["miles"]

SRC = [
    ("Association of Poinciana Villages - Design Control Board Criteria, effective March 18, 2021", "https://www.apvcommunity.com/_files/ugd/05e418_13ee909540a74f95876f2858717f9749.pdf?index=true"),
    ("Solivita Community Association - Architectural Review Requirements, adopted November 13, 2013", "https://aristainflorida.com/wp-content/uploads/2017/09/Solivita.5.Architectural-Review-Requirements-Final-11.22.13.pdf"),
    ("Osceola County - Building and Permits", "https://www.osceola.org/Doing-Business/Building-and-Permits"),
    ("Polk County - Building Division", "https://www.polkfl.gov/services/building/"),
    ("Osceola County Property Appraiser - parcel search", "https://search.property-appraiser.org/"),
    ("Polk County Property Appraiser - property search", "https://www.polkflpa.gov/CamaSearch.aspx"),
    ("Toho Water Authority - our service area", "https://www.tohowater.com/about-us/our-service-area"),
    ("Association of Poinciana Villages - utility companies", "https://www.apvcommunity.com/utility-companies"),
    ("South Florida Water Management District - Upper Kissimmee Basin water supply plan", "https://www.sfwmd.gov/our-work/water-supply/upper-kissimmee"),
    ("Polk Forever - Upper Kissimmee Basin", "https://polkforever.com/upper-kissimmee-basin/"),
    ("PRFSC - our local history", "https://prfsc.org/our-local-history/"),
    ("Poinciana, Florida (Wikipedia)", "https://en.wikipedia.org/wiki/Poinciana,_Florida"),
    ("Lake Marion Creek Wildlife Management Area (Wikipedia)", "https://en.wikipedia.org/wiki/Lake_Marion_Creek_Wildlife_Management_Area"),
    ("NEON - Disney Wilderness Preserve soil site summary", "https://data.neonscience.org/api/v0/documents/DSNY_Soil_SiteSummary"),
    ("USDA NRCS - Official Series Description, Immokalee series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/I/IMMOKALEE.html"),
    ("USDA NRCS - Official Series Description, Smyrna series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/S/SMYRNA.html"),
    ("USDA NRCS - Official Series Description, Myakka series", "https://soilseries.sc.egov.usda.gov/osd_docs/m/myakka.html"),
    ("USDA NRCS - Official Series Description, Basinger series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/B/BASINGER.html"),
]

# ------------------------------------------------------------------ HUB
HUB = page(
    "/areas/poinciana/", "city",
    "Artificial Turf in Poinciana, FL: Local Guide (2026)",
    "Poinciana, FL artificial turf guide: Osceola vs. Polk County permits, APV and Solivita design review, Toho Water rules and canal setbacks, updated September 2026.",
    "Artificial turf installation and care across Poinciana's two counties",
    capsule(
        f"Poinciana straddles Osceola and Polk counties, about {MILES} miles from downtown "
        f"{city('kissimmee')}, and a synthetic lawn here runs {price('residential')} a square "
        "foot installed as of September 2026. What changes on a quote is the address: which "
        "county reviews the permit, whether the lot sits inside an Association of Poinciana "
        "Villages neighborhood or Solivita's 55-plus gates, and how close the yard backs onto "
        "a drainage canal or retention pond."
    ),
    "".join([
        sec("What makes turf different in a town split between two counties?",
            "<p>Poinciana was laid out as nine numbered villages under one master association, and "
            "four of them, Village 1 (which takes in the Cypress Woods and Stepping Stone "
            "neighborhoods), Village 2, Village 5 and Village 9 (the Broadmoor mobile home park), "
            "sit in Osceola County, while Villages 3, 4, 6, 7 and 8 sit across the line in Polk "
            "County, per the " + ext("https://www.apvcommunity.com/_files/ugd/05e418_13ee909540a74f95876f2858717f9749.pdf?index=true", "Association of Poinciana Villages' own Design Control Board Criteria")
            + ". Solivita, the 55-plus gated section on the Polk side, was counted as Village 10 "
            "until its executive committee split it off from the master association in November "
            "2011, according to " + ext("https://prfsc.org/our-local-history/", "the local history maintained by the Poinciana Residents for Self-Sufficiency")
            + ". That split matters for a turf quote for one plain reason: a permit for a Village "
            "2 backyard goes to Osceola County's building office, and the same job a few streets "
            "over in Village 6 goes to Polk County's, on a different timeline with a different "
            "phone number. Confirm the parcel with a property appraiser before assuming either "
            "one applies, and see our " + a("/laws/permits/osceola-county/", "Osceola County permit page")
            + " and " + a("/laws/permits/polk-county/", "Polk County permit page") + " for what "
            "each office asks for.</p>"),
        table("Poinciana yard types and what we do differently",
              ["Yard type", "Where", "What's different", "What we do differently"],
              [
                  ["APV village lot", "Villages 1-9, Osceola or Polk side", "Builder sod on a small fenced lot, Design Control Board review",
                   "File the landscaping plan with the DCB before ordering material, since ground cover is part of the approval"],
                  ["Solivita villa", "Polk County, gated, golf course frontage common", "Architectural Review Committee approval, no tennis or play courts allowed on the lot",
                   "Route a lawn or green change through the ARC's landscape submittal rather than a general building permit"],
                  ["Broadmoor mobile home lot", "Village 9, Osceola County, off Poinciana Boulevard", "Public sewer required, no septic tank, no fencing where a drainage canal runs the lot line",
                   "Build around the sewer connection and leave the canal bank open where fencing isn't allowed"],
                  ["Canal- or pond-backed lot", "Either county, common across Poinciana's platted grid", "State setback measured from the water's edge, not the house",
                   "Hold turf back at least 10 feet from the bank unless a seawall already separates the yard from the water"],
                  ["Lot near the Lake Marion Creek buffer", "Near Village 7 and Solivita's northern edge", "Managed conservation land runs along the rear property line",
                   "Keep grading and turf inside the platted lot and clear of the management area's boundary"],
              ],
              "Prices don't change by yard type; access, base depth and paperwork do."),
        sec("Which office reviews the permit, and how do you check a parcel?",
            "<p>" + ext("https://www.osceola.org/Doing-Business/Building-and-Permits", "Osceola County's Building and Permits office")
            + " covers the Osceola-side villages at 407-742-0200, with an online permit portal for "
            "tracking an application once it's filed. " + ext("https://www.polkfl.gov/services/building/", "Polk County's Building Division")
            + " covers the Polk-side villages instead, at 863-534-6080 out of the County "
            "Administration Building in Bartow. Neither office is the village association: the "
            "DCB Criteria state plainly that "
            + ext("https://www.apvcommunity.com/_files/ugd/05e418_13ee909540a74f95876f2858717f9749.pdf?index=true", "\"approval of any project by the DCB does not waive the necessity of obtaining the required County building permits\"")
            + ", and getting a county permit doesn't waive the village review either. To find "
            "which county a specific address falls in, search the parcel on the "
            + ext("https://search.property-appraiser.org/", "Osceola County Property Appraiser's site")
            + " or the " + ext("https://www.polkflpa.gov/CamaSearch.aspx", "Polk County Property Appraiser's site")
            + ", both of which list the taxing jurisdiction on the same record as the lot lines.</p>"),
        sec("What does the Association of Poinciana Villages say about lawns and turf?",
            "<p>APV's Design Control Board Criteria cover Villages One through Nine, not Solivita, "
            "and its minimum landscaping standard states that "
            + ext("https://www.apvcommunity.com/_files/ugd/05e418_13ee909540a74f95876f2858717f9749.pdf?index=true", "\"lots must be fully sodded\"")
            + " unless the board approves an alternative such as \"Florida Friendly Landscape, "
            "formerly known as Xeriscape,\" reviewed case by case. Nothing in the document names "
            "artificial turf specifically, so a synthetic lawn goes in as one of those case-by-case "
            "landscaping alternatives, with its own DCB application, rather than as an exception "
            "carved out of a rule written with turf in mind. The same criteria require any exterior "
            "change, a fence, a paved surface, a dog run, to clear the DCB before work starts, and "
            "list sod and landscape among the items an inspector checks during construction. See "
            + a("/laws/hoa-rules/", "what a Florida association can and can't restrict")
            + " and use our " + a("/tools/hoa-packet-checklist/", "HOA and ARC packet checklist") + " when preparing that application.</p>"),
        sec("Does Solivita review a landscape change differently?",
            "<p>Solivita runs its own Architectural Review Committee separate from APV, and its "
            "Architectural Review Requirements call for ARC sign-off on \"any exterior addition, "
            "changes, modifications or alterations,\" landscaping included, before work begins. "
            "Fences along a golf course, lake or pond have to sit at least 5 feet off the property "
            "line with no wall permitted in that stretch at all, a detail that matters on the many "
            "Solivita lots that back onto a fairway or a pond. Tennis courts, play courts and game "
            "courts aren't allowed on an individual lot there, which rules out a home sports surface "
            "outright even where a lawn conversion or a putting green would be welcome. Like the "
            "wider villages' criteria, Solivita's document never mentions synthetic turf by name, so "
            "a landscape submittal, not a turf-specific waiver, is what starts the review. Our "
            + post("artificial-turf-for-55-plus-communities", "guide to turf in 55-plus communities") + " covers the broader pattern.</p>"),
        sec("Where does Poinciana's water come from, and what's the watering schedule?",
            "<p>Toho Water Authority provides both water and sewer service on both sides of the "
            "county line, per " + ext("https://www.tohowater.com/about-us/our-service-area", "Toho's own service-area page")
            + " and " + ext("https://www.apvcommunity.com/utility-companies", "APV's utility listing")
            + ", which also names Duke Energy as the electric provider for both counties. " + src("toho-days", "Toho's published watering schedule")
            + " applies the same two-day-a-week rule here as everywhere else the utility serves, "
            "with no daytime irrigation regardless of which day gets assigned to the address. "
            "Poinciana's stretch of the Kissimmee chain sits inside the Central Florida Water "
            "Initiative's " + ext("https://www.sfwmd.gov/our-work/water-supply/upper-kissimmee", "Upper Kissimmee Basin")
            + ", managed by the South Florida Water Management District on both the Osceola and "
            "Polk sides, rather than the "
            + ext("https://polkforever.com/upper-kissimmee-basin/", "Southwest Florida district that covers ground farther west in Polk County")
            + ".</p>"),
        sec("What's under a Poinciana lawn, and where do the state's water rules bite hardest?",
            "<p>Poinciana sits in the Southern Florida Flatwoods, and the closest mapped survey "
            "work, at the Disney Wilderness Preserve just north of the community, lists "
            + ext("https://soilseries.sc.egov.usda.gov/OSD_Docs/I/IMMOKALEE.html", "Immokalee")
            + ", " + ext("https://soilseries.sc.egov.usda.gov/OSD_Docs/S/SMYRNA.html", "Smyrna") + ", "
            + ext("https://soilseries.sc.egov.usda.gov/osd_docs/m/myakka.html", "Myakka") + " and the poorly "
            "drained " + ext("https://soilseries.sc.egov.usda.gov/OSD_Docs/B/BASINGER.html", "Basinger series")
            + " as the dominant soils, per "
            + ext("https://data.neonscience.org/api/v0/documents/DSNY_Soil_SiteSummary", "a NEON site summary for the preserve")
            + ". All four are fine sand with a water table that sits close to the surface for weeks "
            "at a stretch, the exact condition Poinciana's platted grid of drainage canals and "
            "retention ponds was built to manage. Two of the state's turf rules come up more often "
            "here than in a drier inland town as a result: the 10-foot setback from any natural or "
            "man-made waterbody, and the ban on routing turf through a swale. Lake Marion Creek "
            "itself meanders \"between Poinciana Village 7 and Solivita\" on its way to the "
            "Kissimmee chain, per the local history, and sets the same 10-foot rule along the "
            + ext("https://en.wikipedia.org/wiki/Lake_Marion_Creek_Wildlife_Management_Area", "Lake Marion Creek management area")
            + " that Polk County and the water district jointly manage on the Osceola-Polk line.</p>"),
        sec("Housing, growth and what that means for a turf quote",
            "<p>Poinciana was formally established in 1972 on roughly 50,000 acres of former "
            "farmland and swamp that a predecessor of Avatar Holdings began assembling in the "
            "1960s, with the first homes built in 1973 around the community's original golf and "
            "racquet club, per " + ext("https://en.wikipedia.org/wiki/Poinciana,_Florida", "Wikipedia")
            + " and " + ext("https://prfsc.org/our-local-history/", "PRFSC's local history") + ". Avatar, "
            "later renamed AV Homes, has developed the community since the mid-1980s, and growth "
            "since then has been steep: the population went from roughly 8,000 in 1994 to 53,193 "
            "in 2010 to 69,309 in 2020. Most of the housing stock is 1990s-through-2020s "
            "single-family construction on lots platted decades earlier, small, straightforward "
            "footprints rather than the oversized yards found in some older Osceola towns, which "
            "puts more weight on lot access and DCB paperwork than on working around established "
            "landscaping.</p>"),
        sec("What has to be approved before turf goes into a Poinciana yard?",
            "<p>Three approvals can stack on one project here: the county building department for "
            "the address, Osceola or Polk; the village-level design board, APV's DCB for Villages "
            "1-9 or Solivita's ARC for the 55-plus section; and, where a backyard fence keeps the "
            "work out of street view, the statewide protection under " + src("fs7203045", "F.S. 720.3045")
            + " that stops either board from restricting turf it can't see from the frontage or an "
            "adjacent parcel. Florida's " + a("/laws/florida-hb-683/", "HB 683 and the DEP synthetic turf rule it created")
            + " set a floor for local governments, not for private associations, so that law "
            "doesn't decide what APV or Solivita will approve. How do you find the best artificial "
            "turf contractor in Poinciana? Start by asking whether they already know which board "
            "reviews the address, the county's or the village's, before they mention a price. Our "
            + a("/laws/hoa-rules/", "HOA rules page") + " and " + a("/tools/hoa-packet-checklist/", "packet checklist")
            + " cover what to bring to that meeting.</p>"),
        "<!--AUTO:city-services-->",
    ]),
    faqs=[
        faq("Which county issues the permit for a Poinciana backyard, Osceola or Polk?",
            "It depends on which village the address sits in. Villages 1, 2, 5 and 9 (Broadmoor) "
            "are in Osceola County; Villages 3, 4, 6, 7, 8 and Solivita are in Polk County. Check "
            "the parcel on either county's property appraiser site to confirm before calling a "
            "building department."),
        faq("Does the Association of Poinciana Villages allow artificial turf?",
            "Its criteria require lots to be fully sodded unless the Design Control Board approves "
            "an alternative such as Florida Friendly Landscape on a case-by-case basis. Turf isn't "
            "named in the document, so it would be submitted as one of those alternatives, with a "
            "DCB application, rather than requested under a rule written for it."),
        faq("Is Solivita's landscaping review different from the rest of Poinciana?",
            "Yes. Solivita left the Association of Poinciana Villages in 2011 and runs its own "
            "Architectural Review Committee, which approves any exterior or landscape change "
            "separately from APV's Design Control Board. Neither document names synthetic turf "
            "specifically."),
        faq("How close can turf go to a canal or pond in Poinciana?",
            "At least 10 feet from the water's edge, unless a seawall or bulkhead already separates "
            "the yard from the water. The same setback applies to a retention pond or a stretch of "
            "the Lake Marion Creek conservation buffer near Village 7 and Solivita."),
        faq("Is Poinciana on septic tanks or public sewer?",
            "Toho Water Authority provides both water and sewer service on both the Osceola and "
            "Polk sides, according to the utility's own service-area page. Broadmoor's mobile home "
            "rules go further and bar septic tanks outright, requiring a sewer connection instead."),
    ],
    sources=SRC,
    city=SLUG,
    crumbs=[("Service areas", "/areas/")],
    crumb="Poinciana",
    related=[
        ("/areas/osceola-county/", "Artificial turf in Osceola County"),
        ("/areas/polk-county/", "Artificial turf in Polk County"),
        ("/laws/permits/osceola-county/", "Osceola County permit rules"),
        ("/laws/permits/polk-county/", "Polk County permit rules"),
        ("/areas/kissimmee/", "Artificial turf in Kissimmee"),
        ("/areas/davenport/", "Artificial turf in Davenport"),
        ("/artificial-turf-cost/", "Turf cost tables for Central Florida"),
    ],
)

# ------------------------------------------------------------------ LOCAL
LOCAL = {}

LOCAL["residential"] = {
    "title": "Artificial Grass Installation in Poinciana, FL",
    "meta": "Artificial grass in Poinciana, FL runs $8-$18 a sq ft installed as of September 2026. APV's fully-sodded rule, county permits and starter-home lots, explained.",
    "h1": "Artificial grass for Poinciana's starter-home villages",
    "lede": capsule(
        f"A synthetic lawn in Poinciana, Florida costs {price('residential')} a square foot "
        "installed as of September 2026, the same range as anywhere else in Central Florida. "
        "What changes locally is the paperwork: most lots sit inside an Association of Poinciana "
        "Villages neighborhood built around a fully-sodded lawn standard, and which county's "
        "building office reviews the work depends on which village the address falls in."
    ),
    "sections": [
        ("Sod is the written baseline, so a lawn conversion needs its own approval",
         "<p>APV's Design Control Board Criteria set minimum landscaping at a fully sodded lot for "
         "Villages One through Nine, with a case-by-case exception for an alternative such as "
         "Florida Friendly Landscape. A synthetic lawn falls into that same exception lane rather "
         "than a rule built for it, so the plan submitted to the DCB should describe the turf, "
         "backing and infill the way a landscaping alternative would be described, not treated as "
         "an automatic swap for sod. Solivita, on the Polk side, runs a separate Architectural "
         "Review Committee that reviews any landscape change under its own paperwork instead. "
         "Either way, the review happens before material gets ordered, not after.</p>"),
        ("A starter-home lot in Poinciana isn't the same build as a rural acre",
         "<p>Most Poinciana houses sit on lots platted decades ago for a single-family footprint, "
         "small and rectangular, with a fenced backyard and a front lawn facing the street. That "
         "size works in favor of a turf conversion in one sense, less excavation and fewer "
         "obstacles than a half-acre parcel, and against it in another: a front yard here almost "
         "always faces the street, which means it doesn't get the visibility protection that a "
         "fenced backyard gets under state law. " + post("why-new-construction-sod-dies-in-osceola-county", "Our piece on why new-construction sod struggles in Osceola County")
         + " covers the mechanics behind why so many of these lawns get asked about in the first "
         "place.</p>"),
        ("Which office reviews the permit depends on the village, not the street name",
         "<p>Four villages, 1, 2, 5 and 9, sit in Osceola County and file with that county's "
         "building department; the rest sit in Polk County and file with its Building Division "
         "instead. A homeowner comparing notes with a neighbor two streets over in a different "
         "village can end up describing two different review timelines for what looks like the "
         "same job. Confirming the parcel's county on a property appraiser's site before scheduling "
         "an install saves a misdirected call, and " + city("poinciana") + " has the full breakdown "
         "of which villages sit where.</p>"),
    ],
    "scenario": (
        "Say you have a 650 sq ft front and side lawn",
        "<p>Say you have a 650 sq ft front and side lawn on an original Village 2 lot, St. "
        "Augustine that's thinned to bare patches along the driveway edge where foot traffic "
        "concentrates. At " + price("residential", True) + " a square foot, mid-grade turf for "
        "that area runs roughly $6,500 to $10,400, and because a front yard faces the street "
        "directly, the plan goes to the Design Control Board as a landscaping alternative before "
        "the county permit gets filed, not the other way around. A fenced backyard project on the "
        "same lot would still need DCB sign-off, but wouldn't carry the same street-visibility "
        "question a front lawn does.</p>"
    ),
    "faqs": [
        faq("Does turf cost more in an older Poinciana village than a newer one?",
            "The per-square-foot range doesn't change by village or by county. What varies is "
            "access and base condition: an original 1970s-80s lot may need more prep if the "
            "existing sod sits on compacted, unamended ground, while a newer section built on "
            "graded fill often installs faster."),
        faq("How do I find the best artificial grass installer near me in Poinciana?",
            "Ask whether they know the DCB or ARC submittal process for the specific village before "
            "they quote a price, and whether they've filed with Osceola County's or Polk County's "
            "building office. An installer who can answer both without hesitation has done the "
            "homework already."),
    ],
    "sources": SRC,
}

LOCAL["pet"] = {
    "title": "Pet Turf and Dog Runs on Poinciana's Small Lots",
    "meta": "Pet turf in Poinciana, FL runs $10-$18 a sq ft installed as of September 2026, sized to fit APV's 200 sq ft dog-run rule on a fenced starter-home lot.",
    "h1": "Dog runs built for Poinciana's fenced backyards",
    "lede": capsule(
        f"Pet turf installed in Poinciana, Florida runs {price('pet')} a square foot as of "
        "September 2026, and most of the demand comes from small, fenced backyards rather than "
        "acreage, since Poinciana's villages were platted for single-family lots, not rural "
        "parcels. The Association of Poinciana Villages caps a dog run's size directly, which "
        "shapes the layout before the turf spec does."
    ),
    "sections": [
        ("APV's own dog-run rule sets the footprint before anything else",
         "<p>The Design Control Board Criteria allow a dog run without a kennel structure, but the "
         "run itself is capped at 200 square feet, can't stand taller than six feet, has to sit at "
         "the rear of the property, and must come with a dog house for weather protection; the "
         "criteria also cap a household at one run and two pets. That 200 square foot ceiling is "
         "smaller than a lot of dog-run layouts we'd otherwise recommend for two large dogs, which "
         "means the drainage and infill choice inside that footprint matter more here than they "
         "would on an open acreage lot with room to spread the run out.</p>"),
        ("A fenced backyard clears the visibility question a front yard can't",
         "<p>Under " + src("fs7203045", "F.S. 720.3045") + ", an association can't restrict "
         "something not visible from the parcel's frontage or an adjacent parcel, and a privacy-fenced "
         "backyard on a standard Poinciana lot generally clears that bar. A side yard facing a "
         "neighbor's driveway, or a corner lot with two street-facing sides, doesn't get the same "
         "protection automatically, which is worth checking before assuming a run built there is "
         "shielded from review the same way a plain rear-yard run would be.</p>"),
        ("Flatwoods soil raises the stakes on drainage more than on a plain lawn",
         "<p>Poinciana's ground maps to the same fine-sand flatwoods series common across this part "
         "of Osceola and Polk, Immokalee, Smyrna and Myakka among them, with a water table that "
         "sits close to the surface for weeks during the rainy season. A dog run's deeper base and "
         "fully permeable backing carry more of the drainage load on that kind of soil than they "
         "would on higher ground, since a shallow or unwashed base with a high water table pushing "
         "up from below has almost no margin left before odor turns into a year-round problem. "
         + post("how-to-get-dog-urine-smell-out-of-artificial-turf", "Our guide to clearing dog-urine odor from turf")
         + " covers what that build looks like day to day.</p>"),
    ],
    "scenario": (
        "Say you have two dogs on a Village 5 lot",
        "<p>Say you have two mid-size dogs on a fenced Village 5 backyard, with a worn dirt track "
        "along the fence line where the grass gave up years ago. Built to APV's 200 square foot "
        "maximum, a run at " + price("pet", True) + " a square foot runs roughly $2,400 to $3,200, "
        "with the layout including the required dog house and staying inside the six-foot height "
        "cap on the enclosure itself. Because the run sits behind a privacy fence not visible from "
        "the street, it clears the state's visibility protection even before the DCB signs off on "
        "the landscaping plan.</p>"
    ),
    "faqs": [
        faq("Can a Poinciana dog run be bigger than 200 square feet?",
            "Not under APV's Design Control Board Criteria, which cap a run at 200 square feet "
            "per household along with a six-foot height limit and a one-run maximum. Solivita's "
            "rules are separate and don't set the same numeric cap, but any addition there still "
            "needs ARC approval first."),
        faq("Does a Poinciana HOA count pet turf as artificial turf it can restrict?",
            "If it sits inside a fenced backyard not visible from the street or an adjacent lot, "
            "F.S. 720.3045 protects it regardless of the label. A run along a side yard facing a "
            "neighbor's driveway may not get that same protection, so check sightlines first."),
    ],
    "sources": SRC,
}

LOCAL["putting"] = {
    "title": "Putting Greens for Poinciana's Golf-Front Lots",
    "meta": "Backyard putting greens in Poinciana, FL run $14-$30 a sq ft installed as of September 2026, sized for Solivita's golf-front villas and standard APV lots alike.",
    "h1": "Backyard greens for Solivita's fairways and Poinciana's village lots",
    "lede": capsule(
        f"A backyard putting green in Poinciana, Florida runs {price('putting')} a square foot "
        "installed as of September 2026. Lot type drives the design more than almost anything "
        "else here: a Solivita villa backing onto a fairway has a fence setback and a review "
        "board built around golf-course sightlines, while a standard village lot on the Osceola "
        "or Polk side has more straightforward paperwork but less room to work with."
    ),
    "sections": [
        ("Solivita's fence rule shapes a green built along a fairway",
         "<p>Solivita's Architectural Review Requirements set a fence setback of at least 5 feet "
         "from the property line along a golf course, lake or pond, and bar a wall entirely in "
         "that same stretch. A putting green built close to that edge has to work within an open "
         "sightline toward the course rather than behind a screened boundary, which changes how "
         "much of the yard reads as green space from the fairway side versus how much is usable "
         "for cups and contouring. The ARC's landscape approval covers that layout the same way it "
         "covers any other exterior change, and " + post("artificial-turf-for-55-plus-communities", "our piece on turf in 55-plus communities")
         + " goes into how that review typically runs.</p>"),
        ("A standard APV village lot trades golf views for a simpler process",
         "<p>Outside Solivita, a putting green on a Village 2 or Village 6 lot answers to APV's "
         "Design Control Board instead, under the same fully-sodded landscaping standard that "
         "governs any other ground cover change, with a case-by-case alternative for something "
         "like a synthetic green. There's no golf-course fence rule to work around on these lots, "
         "but the tradeoff is a smaller, more rectangular yard than a fairway-front Solivita villa "
         "typically has, which usually means a single-tier design rather than a multi-level layout.</p>"),
        ("Low-upkeep appeal matters more here than the putting itself",
         "<p>A meaningful share of putting-green interest in Poinciana traces back to homeowners "
         "who want a low-maintenance lawn feature more than a serious short-game practice tool, "
         "particularly in Solivita's active-adult section where mowing a full backyard isn't part "
         "of the appeal. A smaller green with a fringe collar can serve as that low-upkeep lawn "
         "substitute just as well as a larger multi-cup layout, and it's worth discussing which "
         "goal matters more before the design gets fixed.</p>"),
    ],
    "scenario": (
        "Say you have a 350 sq ft Solivita backyard",
        "<p>Say you have a 350 sq ft Solivita villa backyard with a screened lanai on one side and "
        "a fairway view along the rear property line, wanting a single-cup green rather than a "
        "full practice layout. At " + price("putting", True) + " a square foot, that runs roughly "
        "$6,300 to $8,750, with the fence and landscape plan submitted to the ARC ahead of time "
        "since the yard backs directly onto the course. A similar footprint on a standard village "
        "lot near " + city("championsgate", "ChampionsGate") + " or elsewhere on the Osceola side "
        "clears a different review board but runs the same price range.</p>"
    ),
    "faqs": [
        faq("Does a Solivita putting green need ARC approval before installation?",
            "Yes. Any exterior or landscape change in Solivita goes through the Architectural "
            "Review Committee, and a green backing onto a golf course also has to respect the "
            "5-foot fence setback from that boundary."),
        faq("Can a putting green go in a standard Poinciana village lot?",
            "Yes, under APV's Design Control Board Criteria as a case-by-case landscaping "
            "alternative to the fully-sodded standard. The lot's smaller, more rectangular shape "
            "usually points toward a single-tier design rather than a multi-level one."),
        faq("Are Poinciana putting greens usually built for practice or for looks?",
            "Both, but a fair share of interest here is about a low-upkeep lawn feature rather "
            "than serious short-game practice, especially in Solivita's active-adult section where "
            "mowing a full lawn isn't the draw."),
    ],
    "sources": SRC,
}

LOCAL["playground"] = {
    "title": "Playground Turf for Poinciana Family Backyards",
    "meta": "Playground turf in Poinciana, FL runs $10-$25 a sq ft installed as of September 2026, sized for APV's family villages where the community keeps growing fast.",
    "h1": "Backyard play surfaces across Poinciana's growing family villages",
    "lede": capsule(
        f"Playground turf installed in Poinciana, Florida runs {price('playground')} a square "
        "foot as of September 2026. Almost all of the demand for it sits in the Association of "
        "Poinciana Villages' family neighborhoods rather than Solivita, since the 55-plus "
        "community restricts play structures on individual lots and courts entirely."
    ),
    "sections": [
        ("A community built for families, growing faster than most of Central Florida",
         "<p>Poinciana's population climbed from roughly 8,000 residents in 1994 to more than "
         "69,000 by 2020, growth concentrated almost entirely in the family-oriented villages "
         "rather than the age-restricted section. That pace of new households is exactly where "
         "backyard play-turf requests come from: a fenced yard with a swing set or a small play "
         "structure that needs a surface tougher than sod under daily kid traffic. "
         + post("is-artificial-turf-safe-for-kids-pfas-lead", "Our guide to what makes play turf safe for kids")
         + " covers the material side of that question.</p>"),
        ("APV's own rule keeps play equipment small and out of sight",
         "<p>The Design Control Board Criteria classify swing sets, slides and jungle gyms as "
         "portable structures that should be \"prefabricated and erected to the rear of the house "
         "as inconspicuously as possible,\" and specifically prohibit combining a storage shed with "
         "play equipment. That rule shapes the footprint a play-turf area needs to work around more "
         "than the turf spec itself does: a shock pad sized to a compact rear-yard structure, not a "
         "sprawling play set visible from the street.</p>"),
        ("Solivita is a small market for this service, and that's worth saying plainly",
         "<p>Solivita's Architectural Review Requirements restrict games, play structures and "
         "recreational equipment on individual lots, and the community is age-restricted to begin "
         "with, so backyard playground turf isn't a realistic request there the way it is in the "
         "family villages. Anyone asking about play surfaces for a Solivita property is more often "
         "planning for visiting grandchildren on a short-term basis than a permanent installation, "
         "and the ARC's review process still applies to whatever gets proposed.</p>"),
    ],
    "scenario": (
        "Say you have a 220 sq ft corner of a Village 4 backyard",
        "<p>Say you have a 220 sq ft corner of a fenced Village 4 backyard set aside for a swing "
        "set on a 5-foot fall height, tucked toward the rear of the house the way APV's rule "
        "expects. At " + price("playground", True) + " a square foot, a shock-pad system sized to "
        "that equipment runs roughly $2,640 to $4,180, filed with the DCB as a landscaping "
        "alternative alongside the play structure's own placement request. Since the lot sits on "
        "flatwoods soil with a shallow water table for parts of the year, the base underneath "
        "carries more of the drainage job than it would on higher ground.</p>"
    ),
    "faqs": [
        faq("Does APV restrict where a play structure can go in the yard?",
            "Yes. Its criteria call for swing sets, slides and similar equipment to be placed at "
            "the rear of the house as inconspicuously as possible, and specifically prohibit "
            "combining a storage shed with play equipment."),
        faq("Is playground turf common in Solivita?",
            "It's a small market there. Solivita's rules restrict play structures on individual "
            "lots, and the community is age-restricted, so most requests for this service come "
            "from Poinciana's family villages instead."),
    ],
    "sources": SRC,
}

LOCAL["pool"] = {
    "title": "Pool-Area Turf for Poinciana, FL Screened Cages",
    "meta": "Pool and lanai turf in Poinciana, FL prices like a residential lawn, $8-$18 a sq ft as of September 2026, for cages built under two different design boards.",
    "h1": "Turf around Poinciana pool cages, from APV villages to Solivita",
    "lede": capsule(
        f"Turf around a Poinciana pool or inside a screened lanai prices the same as a "
        f"residential lawn, {price('residential')} a square foot as of September 2026. What "
        "differs by village is the pool rule itself: APV allows an above-ground pool behind a "
        "solid privacy fence, while Solivita bans above-ground pools outright and requires ARC "
        "approval for any in-ground one."
    ),
    "sections": [
        ("Two different pool rules, one turf answer",
         "<p>APV's Design Control Board Criteria permit an in-ground pool without special review "
         "and allow an above-ground pool only inside a fully enclosed six-foot solid privacy "
         "fence tall enough to block the view from any public side. Solivita's Architectural "
         "Review Requirements go further, permitting in-ground pools with ARC sign-off but "
         "prohibiting above-ground pools entirely. Whichever rule applies, the turf around the "
         "cage's edge is the same product and the same install method, since a screened enclosure "
         "changes the drainage detail far more than which association wrote the pool rule.</p>"),
        ("Sod struggles hardest right at the deck edge",
         "<p>A pool cage poured on compacted fill up to the deck edge creates the same narrow, "
         "high-traffic strip in Poinciana that it does anywhere else in Central Florida: the fill "
         "drains differently than native ground, foot traffic concentrates at the gate, and "
         "chemical splash browns a band of grass that never fully recovers between waterings. That "
         "combination is why the ring around a screened pool is often the first place a homeowner "
         "here asks about turf, ahead of the rest of the lawn. "
         + post("install-artificial-turf-over-concrete-pavers-or-grass", "Our guide to installing turf over an existing concrete deck")
         + " covers the base detail that changes when turf meets a slab.</p>"),
        ("A canal- or pond-adjacent lanai still has to clear the state setback",
         "<p>A smaller number of Poinciana pool homes sit close to a drainage canal or a retention "
         "pond on the lot's edge, and turf around that pool cage still has to respect the state's "
         "10-foot waterbody setback measured from the water, not from the pool itself, unless a "
         "seawall or bulkhead already separates the two. That distance can trim the usable turf "
         "area on a lanai built close to an open bank more than the deck's footprint alone would "
         "suggest.</p>"),
    ],
    "scenario": (
        "Say you have a 300 sq ft pool deck ring",
        "<p>Say you have a 300 sq ft ring of turf between a screened pool cage and the rear fence "
        "on a Village 6 lot, where the original sod is worn to dirt along the gate path. At "
        + price("residential", True) + " a square foot, that section runs roughly $3,000 to "
        "$4,800, glued and seamed to the concrete deck's edge with a drainage underlay so water "
        "clears the screen track. Since the lot doesn't back onto a canal or pond, the layout "
        "doesn't need to account for the state's waterbody setback, though the DCB application "
        "still covers the landscaping change itself.</p>"
    ),
    "faqs": [
        faq("Can I have an above-ground pool with turf around it in Poinciana?",
            "It depends on the village. APV allows an above-ground pool behind a fully enclosed "
            "six-foot privacy fence; Solivita bans above-ground pools entirely and only permits "
            "in-ground pools with ARC approval."),
        faq("Does pool-area turf cost more than a plain Poinciana lawn?",
            "It prices in the same range, though small glue-down sections against a concrete deck "
            "often land toward the higher end because of the extra edge work and drainage underlay "
            "a slab requires."),
    ],
    "sources": SRC,
}

LOCAL["str"] = {
    "title": "Vacation Rental Turf in Poinciana: A Small Market",
    "meta": "Short-term rental turf in Poinciana, FL is a small market compared with Kissimmee's US-192 corridor. Association rules and county zoning both shape what's allowed.",
    "h1": "Rental-home turf where Poinciana isn't built for nightly guests",
    "lede": capsule(
        f"Turf for a Poinciana rental property prices like a residential lawn, "
        f"{price('residential')} a square foot as of September 2026, but the market for it is "
        "small compared with the nightly-rental subdivisions closer to the theme parks. "
        "Poinciana was built and is still governed as a family and retiree community, and both "
        "county zoning and the village associations shape what a rental property can actually do."
    ),
    "sections": [
        ("Poinciana isn't a nightly-rental subdivision the way Storey Lake or ChampionsGate is",
         "<p>Communities built around whole-home nightly rentals sit closer to US-192 and I-4, "
         "with zoning designed for that use from the start. Poinciana's villages were platted for "
         "single-family occupancy under deed restrictions written decades before short-term "
         "rental platforms existed, and whether a specific address can operate as a nightly rental "
         "depends on the zoning for that side of the county line as much as on the village's own "
         "rules. Confirming zoning with " + a("/laws/permits/osceola-county/", "Osceola County") + " or "
         + a("/laws/permits/polk-county/", "Polk County") + " before assuming either way is the "
         "first step, not the last one.</p>"),
        ("A village or ARC review still applies on top of county zoning",
         "<p>Even where county zoning permits a rental, APV's Design Control Board or Solivita's "
         "Architectural Review Committee still reviews any exterior change to the property "
         "independently, the same as it would for an owner-occupied home. A landlord converting a "
         "lawn to turf ahead of listing a property has to clear that review the same way any other "
         "homeowner does; a rental use doesn't shortcut the landscaping approval.</p>"),
        ("Where turf pays off is turnover, not nightly volume",
         "<p>Where a Poinciana property is licensed for shorter stays, whether that's a longer-term "
         "furnished rental or an occasional guest booking, durable turf still solves the same "
         "problem it solves anywhere: no mowing schedule to coordinate around tenant turnover, and "
         "no dead patch from weeks the yard sat vacant between occupants. "
         + post("what-to-expect-on-turf-installation-day", "Our walkthrough of installation day") + " is worth "
         "reading before scheduling around a rental calendar.</p>"),
    ],
    "scenario": (
        "Say you have a furnished rental on a Village 7 lot",
        "<p>Say you have a furnished, longer-term rental on a Village 7 lot near " + city("davenport", "Davenport")
        + ", with a 450 sq ft yard showing wear from repeated move-ins. At " + price("residential", True)
        + " a square foot, turf for that yard runs roughly $4,500 to $7,200, and because the "
        "property still sits inside a village governed by APV's Design Control Board, the "
        "landscaping plan needs sign-off there regardless of how the property is rented out.</p>"
    ),
    "faqs": [
        faq("Can I run a nightly vacation rental in Poinciana?",
            "It depends on county zoning for the specific address and, separately, on the village "
            "association's own rules. Check with Osceola County's or Polk County's planning office "
            "before assuming a property can operate that way."),
        faq("Does a rental property skip the DCB or ARC review for turf?",
            "No. The village design board reviews an exterior or landscaping change the same way "
            "it would for an owner-occupied home, whether or not the property is currently rented "
            "out."),
    ],
    "sources": SRC,
}

LOCAL["commercial"] = {
    "title": "Commercial Turf for Poinciana Village Amenities",
    "meta": "Commercial turf in Poinciana, FL is quoted per job from a site visit, covering APV and Solivita amenity centers, clubhouses and community entrances.",
    "h1": "Turf for Poinciana's clubhouses, entrances and amenity campuses",
    "lede": capsule(
        "Commercial turf in Poinciana, Florida is quoted per job from a site visit or drawings "
        "rather than one square-foot range, since a clubhouse lawn, a community entrance median "
        "and a commercial parcel each carry different drainage and access needs. Much of the "
        "commercial-scale work here sits inside the same design-review structure that governs a "
        "single home, just at a larger footprint."
    ),
    "sections": [
        ("Amenity centers answer to the same design boards as individual lots",
         "<p>APV's criteria devote a separate section to commercial and institutional buildings, "
         "stating that such projects \"will blend with their scale and material selection into the "
         "portion of the Poinciana Villages that they serve\" and that each one gets reviewed by "
         "the DCB on its own basis, in accordance with county code. Solivita's clubhouse and "
         "amenity campus fall under the same Architectural Review Committee that reviews an "
         "individual villa's landscaping, just with the added engineering detail a larger project "
         "requires. A turf project for either kind of common area should expect that same layer "
         "of review before a county permit even enters the picture.</p>"),
        ("Growth is pulling more commercial construction toward the corridor",
         "<p>Poinciana's population growth since the 1990s has brought retail, medical offices and "
         "new institutional buildings along the roads connecting the villages, and much of that "
         "construction sits on the same graded, flatwoods-adjacent ground as the residential lots "
         "around it. The same drainage planning that matters for a single backyard, keeping runoff "
         "on the property and clear of any swale, applies at a larger scale to a commercial pad or "
         "a shared clubhouse lawn.</p>"),
        ("City or county code still governs the building itself",
         "<p>Whichever design board signs off on the appearance, the underlying commercial "
         "structure still has to meet Osceola County's or Polk County's building and zoning code "
         "for that parcel, and a commercial site plan typically runs a longer review timeline than "
         "the more routine path available for a residential permit. Confirming both the "
         "association's process and the county's timeline early keeps a landscape contractor's "
         "schedule from slipping against a larger build-out.</p>"),
    ],
    "scenario": (
        "Say you have a 1,000 sq ft village entrance median",
        "<p>Say you have a 1,000 sq ft entrance median at an APV village gate, currently St. "
        "Augustine that browns out every dry season despite a working irrigation system. That "
        "project gets quoted from a site visit rather than a flat per-square-foot number, since "
        "the median's curbing, existing irrigation removal and traffic exposure all factor into "
        "labor differently than a private backyard would. The village association's own approval "
        "process runs alongside, not in place of, whatever county code applies to that median.</p>"
    ),
    "faqs": [
        faq("How is commercial turf priced in Poinciana?",
            "By the job, from a site visit or drawings, since access, existing irrigation, curbing "
            "and traffic exposure vary more between commercial sites than between residential "
            "backyards of similar size."),
        faq("Does an amenity center need its own approval on top of a county permit?",
            "Yes. APV's Design Control Board or Solivita's Architectural Review Committee reviews "
            "the appearance and landscaping separately from whatever building department has "
            "jurisdiction over the parcel."),
    ],
    "sources": SRC,
}

LOCAL["sports"] = {
    "title": "Home Sports Turf in Poinciana, Where Space Allows",
    "meta": "Home sports turf in Poinciana, FL is quoted per job. Solivita bars courts on individual lots outright, while APV village lots leave more room to work with.",
    "h1": "Sports and fitness turf on Poinciana's village-sized lots",
    "lede": capsule(
        "Sports and fitness turf in Poinciana, Florida, a bocce strip, an agility lane or a "
        "home-gym sled track, is quoted per job from a site visit rather than a flat "
        "square-foot range, since layout and length matter more than area alone. Where it fits "
        "depends heavily on which village the lot sits in, since one of Poinciana's largest "
        "communities rules out on-lot courts entirely."
    ),
    "sections": [
        ("Solivita's rule is worth stating plainly: courts aren't allowed",
         "<p>Solivita's Architectural Review Requirements state that \"tennis courts, play courts "
         "and game courts are not permitted within Lots,\" which rules out a home sports surface "
         "on an individual villa regardless of size or design. A homeowner there asking about a "
         "sports surface is more often looking at a small fitness strip, like a sled track along a "
         "side yard, than a court-style layout, and even that still needs ARC approval as any "
         "other landscaping change would.</p>"),
        ("A standard APV village lot has more room to work with, not more approval to skip",
         "<p>Outside Solivita, a village lot on the Osceola or Polk side doesn't carry the same "
         "court ban, and a bocce strip or a compact agility lane can fit along a side yard or "
         "backyard fence line. The DCB's setback rules still apply, ancillary structures 10 feet "
         "from the rear property line and seven and a half feet from the side, and basketball "
         "hoops specifically are limited to one per household in one of three approved locations. "
         "A sports surface layout has to work inside those same lines.</p>"),
        ("Flatwoods drainage matters more on a longer, narrower surface",
         "<p>A sled track or agility lane runs longer and narrower than a typical lawn section, "
         "which means more of its footprint sits at whatever grade the base was built to, and on "
         "Poinciana's flatwoods soil, that grade has to move water off a longer run just as "
         "reliably as it does off a compact square. " + post("artificial-turf-glossary", "Our glossary of turf terms")
         + " is a useful reference when comparing pile height and backing options across a sports "
         "surface versus a plain lawn.</p>"),
    ],
    "scenario": (
        "Say you have a 15 by 40 ft side yard",
        "<p>Say you have a 15 by 40 ft side yard along the fence line of a standard Village 8 "
        "lot, flat and clear, wanting a sled and agility lane rather than mowed grass that stays "
        "soggy after a summer storm. That project gets quoted from a site visit rather than a set "
        "range, since the lane's length and the base depth needed for repeated sled traffic both "
        "factor into labor more than square footage alone. The same request on a Solivita villa "
        "wouldn't move forward as a fixed court, though a smaller fitness strip could still be "
        "proposed through the ARC.</p>"
    ),
    "faqs": [
        faq("Can I put in a home sports court in Solivita?",
            "No. Solivita's Architectural Review Requirements specifically state that tennis, "
            "play and game courts aren't permitted on individual lots, regardless of size or "
            "design."),
        faq("How is sports turf priced in Poinciana?",
            "By the job, from a site visit, since layout, length and base depth vary more across "
            "sports surfaces than they do across residential lawns of similar size."),
    ],
    "sources": SRC,
}

LOCAL["pavers"] = {
    "title": "Turf and Pavers for Poinciana Driveways and Walks",
    "meta": "Turf between pavers in Poinciana, FL is quoted per job, working within APV's driveway width limits and walkway rules that apply across the villages.",
    "h1": "Turf ribbons and paver paths built to Poinciana's driveway rules",
    "lede": capsule(
        "Turf set between pavers in Poinciana, Florida is quoted per job rather than a flat "
        "square-foot range, since a driveway ribbon, a stepping-stone path and a patio border "
        "each use different quantities of paver and turf for the same footprint. APV's own "
        "driveway rules set a hard width limit that shapes the layout before the design gets "
        "drawn."
    ),
    "sections": [
        ("APV's width limits set the driveway layout first",
         "<p>The Design Control Board Criteria require driveways of concrete, asphalt or brick "
         "pavers, cap a combined driveway width at 24 feet (27 feet for a three-car garage), and "
         "limit any walkway next to the house to 2 feet wide. A turf ribbon down the center of a "
         "driveway, or a turf border along a walkway, has to fit inside those same numbers rather "
         "than being designed independently of them, which is a constraint most other Central "
         "Florida associations don't spell out this specifically.</p>"),
        ("New driveways and older paths call for different sequencing",
         "<p>A new-construction driveway going in with pavers from day one can have its turf "
         "ribbon built at the same time, sharing one finished grade even though the two materials "
         "compact differently underneath. An older village lot with a worn dirt path between a "
         "gate and a shed, more common in the original 1970s-80s sections, usually calls for "
         "retrofitting a stepping-stone path with turf between the pavers instead, disturbing less "
         "established ground than a full paver walkway would. "
         + post("artificial-grass-for-shady-side-yards", "Our guide to turf for shady side yards")
         + " covers a similar retrofit scenario.</p>"),
        ("Any driveway or walkway change still needs DCB sign-off",
         "<p>Because driveways and walks are enumerated in the same landscaping section that "
         "covers minimum sodding, a paver-and-turf project has to be submitted for approval the "
         "same as any other exterior change, with the plan showing materials, dimensions and how "
         "the finished width compares to the 24-foot cap. Skipping that step risks a rework rather "
         "than saving time.</p>"),
    ],
    "scenario": (
        "Say you have a 40 ft driveway ribbon",
        "<p>Say you have a 40 ft by 3 ft turf ribbon planned down the center of a new paver "
        "driveway on a Village 3 lot, installed alongside the pavers themselves and staying well "
        "under the 24-foot combined width cap. That project gets quoted from the driveway's "
        "drawings rather than a flat per-square-foot rate, since the paver base and the turf base "
        "have to meet at one consistent grade despite compacting differently, and the DCB "
        "application covers both materials as one submittal rather than two separate approvals.</p>"
    ),
    "faqs": [
        faq("Does APV limit how wide a Poinciana driveway can be?",
            "Yes. Its criteria cap a combined driveway width at 24 feet, or 27 feet for a "
            "three-car garage, and a turf-and-paver design has to fit inside that number."),
        faq("Can turf and pavers go in on an older Poinciana lot with a worn path?",
            "Yes, and it's often a cleaner retrofit than adding turf to an already-finished paver "
            "walkway later, since the stepping-stone approach disturbs less established ground on "
            "an older village lot."),
    ],
    "sources": SRC,
}

LOCAL["repair"] = {
    "title": "Turf Repair for Poinciana's Older APV Yards",
    "meta": "Turf repair in Poinciana, FL is quoted per visit, covering the original 1970s-80s villages where installs are aging and canal-adjacent yards that take more wear.",
    "h1": "Fixing turf across Poinciana's original and newer villages",
    "lede": capsule(
        "Turf repair in Poinciana, Florida is quoted per visit rather than a flat square-foot "
        "rate, since a lifted seam, a settled corner and a washed-out edge each take different "
        "work to fix. Two settings account for most repair calls we'd expect here: turf installed "
        "years ago in the original 1970s-80s villages, and yards backing onto a canal or "
        "retention pond."
    ),
    "sections": [
        ("The oldest villages carry the oldest installs",
         "<p>Poinciana's first villages date to the community's 1972 founding, and turf converted "
         "in those neighborhoods over the past 10 to 15 years is old enough in places that a base "
         "inspection makes more sense than another round of spot repairs. A repair call on one of "
         "these older installs often traces back to a base that predates today's washed-rock "
         "standard, since that requirement is more recent than a meaningful share of the turf "
         "already in the ground here. " + post("does-homeowners-insurance-cover-artificial-turf", "Our guide to insurance and turf damage")
         + " is worth a read before assuming a repair is covered.</p>"),
        ("Canal and pond edges take more weather than an interior lot",
         "<p>Turf along one of Poinciana's drainage canals or retention ponds takes more water "
         "exposure at its perimeter than a lawn set well back from any water feature, since storm "
         "runoff working at an unprotected edge can loosen a seam or a nailed border faster than it "
         "would on an interior lot. A lifted edge near water is worth checking against the state's "
         "10-foot setback too, since an older install that predates the current rule sometimes sits "
         "closer to the bank than a new project would be allowed to start today.</p>"),
        ("A hurricane season repair often means a full base check, not a patch",
         "<p>Central Florida's storm season can lift or shift turf that was anchored to an older "
         "standard, and a Poinciana repair visit after a named storm typically starts by checking "
         "whether the base underneath washed out before simply renailing a corner back down. "
         + post("artificial-turf-hurricane-flooding", "Our piece on turf after a hurricane or flood")
         + " covers what that inspection looks for.</p>"),
    ],
    "scenario": (
        "Say you have a decade-old dog run in Village 1",
        "<p>Say you have a dog run installed about ten years ago in Village 1, now matted flat "
        "along the fence line with a base that's started holding water after storms in a way it "
        "never used to. A repair visit checks whether the rock underneath washed out from years of "
        "runoff before simply renailing the corner, since reseating the edge without addressing an "
        "eroded base fixes the problem for weeks rather than years. That diagnosis, more than the "
        "repair itself, is what the visit is quoted around.</p>"
    ),
    "faqs": [
        faq("Is older turf in Poinciana's original villages worth repairing or replacing?",
            "It depends on the base underneath. A repair fixes a surface issue like a lifted "
            "seam; if the base was never built to the current washed-rock standard, replacement is "
            "usually the more lasting fix."),
        faq("Does turf near a Poinciana canal need more repair than an interior lot?",
            "It can. Water exposure at an unprotected edge works at seams and borders harder over "
            "time than a lawn set back from any water feature, which is why perimeter checks "
            "matter more there."),
    ],
    "sources": SRC,
}

LOCAL["cleaning"] = {
    "title": "Turf Cleaning and Care Across Poinciana Villages",
    "meta": "Turf cleaning in Poinciana, FL is quoted by yard size and visit history, timed around the rainy season and the water table on canal- and pond-adjacent lots.",
    "h1": "Keeping Poinciana turf clean, from village lawns to canal-side yards",
    "lede": capsule(
        "Turf cleaning in Poinciana, Florida is quoted by yard size and how long it's been "
        "since the last visit, not a flat square-foot rate. The rainy-season water table on "
        "Poinciana's flatwoods soil, and how close a lot sits to one of its many drainage canals "
        "or retention ponds, matter more to the cleaning schedule here than tree canopy does."
    ),
    "sections": [
        ("A platted grid of canals and ponds sets the cleaning rhythm",
         "<p>Poinciana's original layout included the drainage canals and retention ponds that a "
         "community this size needs to move rainy-season storms off the streets, and a lawn on a "
         "lot bordering one of them holds more surface moisture between visits than a lot on "
         "higher, drier ground in the same village. " + src("dep-rule", "Florida's turf rule")
         + " requires permeable backing and an open-graded base precisely so that moisture keeps "
         "moving through rather than sitting at the surface, but a cleaning schedule still needs "
         "to account for how much water the surrounding ground is holding.</p>"),
        ("Flatwoods soil holds water longer than higher ground",
         "<p>Immokalee, Smyrna and Myakka series soils common across Poinciana carry a water table "
         "close to the surface for weeks during the wettest months, and a lawn on that kind of "
         "ground can need a tighter cleaning schedule during summer than the same size lawn on "
         "better-drained ground elsewhere in Osceola or Polk County, independent of how well the "
         "turf itself was originally built.</p>"),
        ("A village's age changes what debris shows up",
         "<p>Poinciana's original 1970s-80s villages carry more established landscaping and shade "
         "trees than the newer sections built since the 2000s, which means more leaf litter and "
         "organic debris to clear from an older yard's turf than from a newer one on freshly graded "
         "ground. " + post("does-artificial-turf-drain-in-heavy-rain", "Our piece on drainage in heavy Florida rain")
         + " explains why clearing that debris before it works into the infill matters as much as "
         "the base underneath does.</p>"),
    ],
    "scenario": (
        "Say you have a 500 sq ft lawn near a retention pond",
        "<p>Say you have a 500 sq ft pet-turf lawn on a lot backing onto a village retention pond, "
        "shaded by young landscaping that hasn't matured into heavy leaf drop yet. A cleaning "
        "visit there is quoted around the pond-adjacent moisture and the time since the last "
        "visit, not a flat per-square-foot number, since a lawn that's gone months without "
        "clearing needs meaningfully more work than one cleaned on a tighter summer schedule.</p>"
    ),
    "faqs": [
        faq("Does turf near a Poinciana pond need cleaning more often than an interior lot?",
            "It can. Lots closer to a retention pond or canal sit on ground that holds moisture "
            "closer to the surface, which can call for a tighter cleaning schedule during the "
            "wettest months than a similar-sized lawn on higher ground."),
        faq("Do Poinciana's older villages need more frequent cleaning than newer ones?",
            "Often yes, since established landscaping in the original 1970s-80s villages sheds "
            "more leaf litter and organic debris than the younger plantings common in newer "
            "sections."),
    ],
    "sources": SRC,
}

LOCAL["replacement"] = {
    "title": "Turf Removal and Replacement in Poinciana, FL",
    "meta": "Turf replacement in Poinciana, FL is quoted per job after a base inspection, for lawns converted in the community's earliest 1970s-80s villages.",
    "h1": "Replacing worn turf in Poinciana's earliest villages",
    "lede": capsule(
        "Turf replacement in Poinciana, Florida is quoted per job after a base inspection, not a "
        "flat square-foot rate. Poinciana's original villages date to 1972, and turf converted "
        "there over the past 10 to 20 years is now old enough in places that replacement, not "
        "another repair, becomes the honest recommendation."
    ),
    "sections": [
        ("Some of the community's oldest turf is reaching the end of its window",
         "<p>Turf generally lasts 10 to 20 years depending on UV stabilization, traffic and "
         "infill, and lawns converted in Poinciana's first villages soon after the community's "
         "1972 founding, or during the growth wave that followed Avatar's takeover in the "
         "mid-1980s, are now old enough that a base inspection makes more sense than another round "
         "of spot repairs. " + post("how-long-does-artificial-turf-last-in-florida", "Our guide to turf lifespan in Florida")
         + " covers what shortens that window on a given lot.</p>"),
        ("A full replacement is the point to correct an older base",
         "<p>Replacement at that stage usually means rebuilding to the current washed, open-graded "
         "standard rather than reusing whatever sat underneath the original install, since that "
         "requirement postdates a meaningful share of the turf already in Poinciana's ground. It's "
         "also the practical point to re-check a canal- or pond-adjacent layout against the "
         "state's 10-foot waterbody setback, in case the original install predates the current "
         "rule.</p>"),
        ("The village's design board reviews a replacement the same as new work",
         "<p>Because a full tear-out and relay counts as an exterior change under APV's or "
         "Solivita's landscaping criteria, a replacement project goes through the same DCB or ARC "
         "submittal a brand-new installation would, even though the yard has carried turf for a "
         "decade or more already. " + post("what-does-artificial-turf-warranty-cover", "Our piece on what a turf warranty actually covers")
         + " is worth reading before deciding whether a manufacturer's coverage applies to the old "
         "install.</p>"),
    ],
    "scenario": (
        "Say you have a 2011-installed lawn in Village 2",
        "<p>Say you have a lawn converted to turf in 2011 in Village 2, now matted flat across "
        "the high-traffic path from the driveway to the back gate, with a base that's started "
        "holding water after storms. At roughly 15 years old, that lawn sits near the upper end "
        "of a typical service life, and a replacement quote would include probing the base in more "
        "than one spot before deciding whether the rock underneath can stay or needs to come out "
        "with the old turf.</p>"
    ),
    "faqs": [
        faq("How do I know if Poinciana turf needs replacing instead of repairing?",
            "A base inspection at more than one spot on the lawn is the reliable way to tell. Turf "
            "that's matted but sitting on a base that still drains fine can often be repaired; a "
            "base that's crusted or holding water usually means replacement."),
        faq("Does a replacement project need DCB or ARC approval again?",
            "Yes. A full tear-out and relay counts as an exterior change under either board's "
            "criteria, so it goes through the same landscaping submittal a new installation would, "
            "regardless of how long turf was already on the lot."),
    ],
    "sources": SRC,
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
