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
        table("How a Poinciana lot's paperwork changes by pin on the map",
              ["Where the lot sits", "Who signs off on ground cover", "What changes in the build"],
              [
                  ["APV village lot, Villages 1-9", "County building office plus the DCB's landscape review",
                   "Submit the turf plan as a sodding alternative before material gets ordered"],
                  ["Solivita villa", "Polk County plus the ARC's separate landscape submittal",
                   "Route the change through Solivita's own review, not APV's DCB"],
                  ["Broadmoor mobile home lot, Village 9", "Osceola County; public sewer, no septic tank",
                   "Keep the sewer connection clear and leave the canal bank open where fencing is barred"],
                  ["Canal- or pond-backed lot, either county", "State water-quality rule measured from the bank",
                   "Start turf ten feet off the water unless a seawall already stands there"],
                  ["Lot against the Lake Marion Creek buffer", "Managed conservation land along the rear line",
                   "Keep grading and turf inside the platted lot, clear of the buffer boundary"],
              ],
              "A lot's paperwork changes with its pin on the map; the price per square foot does not."),
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
            "Ten feet, measured from the canal or pond's actual edge rather than the house or the "
            "fence line, is the state's minimum; a property with a seawall or bulkhead already in "
            "place satisfies that distance without an added gap. The same measurement governs the "
            "Lake Marion Creek buffer between Village 7 and Solivita, where the creek itself sets "
            "the line rather than a platted lot boundary."),
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
        f"Installed cost for a synthetic Poinciana lawn sits at {price('residential')} a square "
        "foot as of September 2026, the same market range Central Florida sees regardless of "
        "address, since price doesn't move by ZIP. What does move here is the paperwork: most "
        "lots sit inside an Association of Poinciana Villages neighborhood built around a "
        "fully-sodded lawn standard, and which county's building office reviews the work depends "
        "on which village the address falls in."
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
        ("Statute protects the run from being banned, not from being reviewed",
         "<p>" + src("fs7203045", "F.S. 720.3045") + " keeps the Design Control Board from banning a "
         "dog run that a neighbor or the street can't see, but it doesn't excuse the run from the "
         "same landscaping submittal any other ground-cover change goes through. A run tucked "
         "behind a privacy fence on an interior village lot still needs the DCB paperwork "
         "describing the turf, the dog house and the six-foot enclosure height before work starts; "
         "the statute only stops the board from saying no on sightline grounds once that paperwork "
         "is filed. A corner lot fenced along two street-facing sides is the case worth flagging "
         "early, since neither side may clear the visibility bar the way a plain rear yard "
         "does.</p>"),
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
        faq("Does F.S. 720.3045 mean a Poinciana dog run skips DCB review entirely?",
            "No. The statute stops the board from banning a run it can't see from the street or an "
            "adjacent lot, but the run still needs the same landscaping submittal any other "
            "ground-cover change goes through. A corner lot fenced on two street-facing sides is "
            "worth checking before assuming either side counts as hidden."),
    ],
    "sources": SRC,
}

LOCAL["putting"] = {
    "title": "Putting Greens for Poinciana's Golf-Front Lots",
    "meta": "Backyard putting greens in Poinciana, FL run $14-$30 a sq ft installed as of September 2026, sized for Solivita's golf-front villas and standard APV lots alike.",
    "h1": "Backyard greens for Solivita's fairways and Poinciana's village lots",
    "lede": capsule(
        f"Installed cost for a Poinciana putting green sits at {price('putting')} a square foot "
        "as of September 2026, but the lot decides the design more than the price range does: a "
        "Solivita villa backing a fairway carries a fence setback and a review board built around "
        "golf-course sightlines, while a standard village lot on the Osceola or Polk side has "
        "plainer paperwork and a smaller footprint to work with."
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
        "expects. At " + price("playground", True) + " a square foot, the shock pad built to "
        "match that fall height prices out to roughly $2,640 to $4,180, filed with the DCB as a "
        "landscaping alternative alongside the play structure's own placement request. Since the "
        "lot sits on flatwoods soil with a shallow water table for parts of the year, the base "
        "underneath carries more of the drainage job than it would on higher ground.</p>"
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
        f"A Poinciana pool deck or screened lanai turf job prices at the residential rate, "
        f"{price('residential')} a square foot as of September 2026, since the material and "
        "install method don't change for a water feature. What changes by village is the pool "
        "rule that gets checked first: APV requires a solid privacy fence around an above-ground "
        "pool, while Solivita bars above-ground pools altogether and routes any in-ground pool "
        "through the ARC."
    ),
    "sections": [
        ("An above-ground pool's fence often does double duty",
         "<p>An above-ground pool on an APV lot needs a fully enclosed six-foot privacy fence "
         "before the DCB will approve it, tall enough that the pool can't be seen from a public "
         "side of the property. That same fence usually screens whatever turf goes in around the "
         "deck, so the visibility protection under " + src("fs7203045", "F.S. 720.3045")
         + " and the pool fence often line up on the same enclosure. Solivita skips that "
         "arrangement by prohibiting above-ground pools outright; an in-ground pool there still "
         "needs ARC sign-off before a shovel goes in the ground, turf included.</p>"),
        ("The narrow strip against the cage rarely holds sod",
         "<p>Most Poinciana pool cages sit on a concrete slab poured to the screen frame, and the "
         "strip of ground just outside that slab, where a gate opens onto the yard, takes more "
         "foot traffic and more chlorine splash-out than any other few feet of lawn on the "
         "property. Sod planted there rarely gets the recovery time between waterings that the "
         "rest of the yard does, since the gate path compacts the same track day after day. That "
         "narrow strip, not the open lawn beyond it, is usually the first section a homeowner "
         "asks about, and it's the section where a drainage underlay under the turf backing "
         "matters most, since the slab sheds water instead of letting it soak in the way native "
         "sand does. " + post("install-artificial-turf-over-concrete-pavers-or-grass", "Our guide to installing turf over an existing concrete deck")
         + " covers what changes when turf meets that kind of base.</p>"),
        ("A canal-adjacent lanai puts the setback line inside the yard, not at its edge",
         "<p>Poinciana's platted grid put a canal or a retention pond behind a meaningful share "
         "of its pool lots, and the state's water rule doesn't care how far the pool itself sits "
         "from the bank, only how far the turf does. Where the yard narrows between the screen "
         "frame and an open canal edge, the ten-foot line often falls inside the lanai rather "
         "than along the property's rear boundary, which can leave a strip of exposed ground "
         "between the turf and the water unless a seawall already stands there. Confirming that "
         "line before the layout is drawn avoids relaying a section of turf a second time.</p>"),
    ],
    "scenario": (
        "Say you have a 260 sq ft strip around a screened cage",
        "<p>Say you have a 260 sq ft strip of turf between a screened pool cage and the rear "
        "property line on a Village 4 lot, thin and patchy along the gate path where chlorine "
        "splash-out has browned the grass for years. Priced at " + price("residential", True)
        + " a square foot, that section runs roughly $2,600 to $4,160, seamed and glued to the "
        "slab edge with the drainage underlay a concrete base needs. Because this particular lot "
        "doesn't back onto a canal or pond, the waterbody setback never enters the layout, though "
        "the DCB still reviews the ground-cover change the same as it would for a lot that "
        "did.</p>"
    ),
    "faqs": [
        faq("Can I have an above-ground pool with turf around it in Poinciana?",
            "Only behind a fully enclosed six-foot privacy fence on the APV side, where the DCB "
            "approves it as part of that fence requirement; Solivita bans above-ground pools "
            "entirely and only permits an in-ground pool with ARC sign-off."),
        faq("Does pool-area turf cost more than a plain Poinciana lawn?",
            "It prices in the same range as any residential lawn; a small glue-down section "
            "against a slab just tends to land near the top of that range because of the extra "
            "edge and underlay work concrete requires."),
    ],
    "sources": SRC,
}

LOCAL["str"] = {
    "title": "Vacation Rental Turf in Poinciana: A Small Market",
    "meta": "Short-term rental turf in Poinciana, FL is a small market compared with Kissimmee's US-192 corridor. Association rules and county zoning both shape what's allowed.",
    "h1": "Rental-home turf where Poinciana isn't built for nightly guests",
    "lede": capsule(
        f"A rental property in Poinciana prices its turf at the same residential rate, "
        f"{price('residential')} a square foot as of September 2026, but comparatively few of "
        "these jobs come from nightly-rental listings the way they would closer to the theme "
        "parks. Poinciana was built and is still governed as a family and retiree community, and "
        "both county zoning and the village associations shape what a rental property can "
        "actually do."
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
        "A clubhouse lawn, a village entrance median and a commercial parcel in Poinciana each "
        "price from a site visit or a set of drawings rather than a single square-foot figure, "
        "since drainage and access needs differ by project more than they do between two "
        "backyards. Much of that commercial-scale work still answers to the same design-review "
        "structure that governs an individual lot, just at a larger footprint."
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
         "<p>Retail strips, medical offices and new institutional buildings have followed "
         "Poinciana's population growth since the 1990s out along the roads connecting the "
         "villages, most of it built on the same graded, flatwoods-adjacent ground the "
         "surrounding houses sit on. A commercial pad built on that ground has to solve the "
         "identical drainage problem a backyard does, keep water inside the property line and "
         "out of the nearest swale, just scaled up to a parking apron or a shared clubhouse lawn "
         "instead of a fenced yard.</p>"),
        ("City or county code still governs the building itself",
         "<p>Design-board approval never substitutes for the underlying zoning code: the building "
         "still has to satisfy Osceola County's or Polk County's rules for that parcel, and a "
         "commercial site plan usually takes longer to clear than the more routine review a "
         "single home's permit gets. Lining up both approvals, the association's and the "
         "county's, before scheduling a crew keeps a bigger build-out from stalling halfway "
         "through.</p>"),
    ],
    "scenario": (
        "Say you have a 1,000 sq ft village entrance median",
        "<p>Say you have a 1,000 sq ft entrance median at an APV village gate, sod that's patchy "
        "along the curb line where mower decks scalp it every cut and the irrigation heads miss "
        "the corners. Pricing that median starts with a site visit rather than a square-foot "
        "rate, since curb radius, how much of the old irrigation gets pulled, and daytime "
        "traffic past the gate all change the labor math in a way a private backyard never does. "
        "The DCB's own review still runs alongside whatever Osceola or Polk County requires for "
        "the parcel, not instead of it.</p>"
    ),
    "faqs": [
        faq("How is commercial turf priced in Poinciana?",
            "Each project gets its own site-visit quote rather than a square-foot rate, since "
            "access, existing irrigation, curb work and how much daytime traffic passes the site "
            "all vary more between commercial jobs than between two similarly sized backyards."),
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
        "Sports and fitness turf in Poinciana, a bocce lane, an agility strip or a home-gym sled "
        "track, gets quoted per job once the layout and length are known, not from a flat "
        "square-foot rate, since a narrow lane costs differently than an equivalent patch of "
        "lawn. Which village a lot sits in matters more here than almost anywhere else in the "
        "build, since Solivita rules out an on-lot court entirely."
    ),
    "sections": [
        ("Solivita's rule is worth stating plainly: courts aren't allowed",
         "<p>Solivita's Architectural Review Requirements state plainly that \"tennis courts, play "
         "courts and game courts are not permitted within Lots,\" which takes a fixed sports "
         "surface off the table for any individual villa there regardless of size or design. What "
         "a Solivita homeowner usually ends up asking for instead is something narrower, a sled "
         "or agility strip along a side yard rather than a marked court, and even that "
         "scaled-down request still needs the same ARC sign-off as any other exterior "
         "change.</p>"),
        ("A standard APV village lot has more room to work with, not more approval to skip",
         "<p>Outside Solivita, the DCB's Design Control Board Criteria don't ban a court the way "
         "Solivita's do, but they still box in where one can go: an ancillary structure has to "
         "sit at least 10 feet off the rear property line and seven and a half feet off the "
         "side, and a basketball hoop is capped at one per household in one of three approved "
         "locations. A bocce lane or a compact agility strip fits inside those same setbacks "
         "along a side or rear fence line on a standard village lot, more room than Solivita "
         "allows but still a bounded footprint rather than an open one.</p>"),
        ("Flatwoods drainage matters more on a longer, narrower surface",
         "<p>A sled lane or an agility strip runs long and narrow compared with a lawn section, "
         "which means a bigger share of its footprint sits right at whatever grade the crew "
         "builds into the base. On Poinciana's flatwoods soil, that grade has to carry water off "
         "a run twenty or thirty feet long just as reliably as it clears a compact square of "
         "lawn, or the low end of the lane holds water the rest of the yard sheds fine. "
         + post("artificial-turf-glossary", "Our glossary of turf terms")
         + " is worth checking when comparing pile height and backing options between a sports "
         "lane and a plain lawn.</p>"),
    ],
    "scenario": (
        "Say you have a 12 by 35 ft side yard",
        "<p>Say you have a Village 8 side yard, 12 feet wide and running 35 feet along the fence "
        "line, currently mowed grass that holds water for a day or two after any real summer "
        "storm. A sled and agility lane built into that strip clears the DCB's seven-and-a-half-"
        "foot side setback with room to spare, and gets priced from a site visit rather than a "
        "set range, since the base depth needed for repeated sled traffic drives labor more than "
        "the lane's square footage does. The same layout on a Solivita villa would never clear as "
        "a fixed lane, though a shorter fitness strip could still go in front of the ARC.</p>"
    ),
    "faqs": [
        faq("Can I put in a home sports court in Solivita?",
            "No. Solivita's Architectural Review Requirements rule out tennis, play and game "
            "courts on any individual lot regardless of size or design; a smaller fitness lane "
            "can still go before the ARC as a landscaping request."),
        faq("How is sports turf priced in Poinciana?",
            "Each lane or court gets its own site-visit quote instead of a square-foot rate, "
            "since length, layout and the base depth a specific surface needs vary more here "
            "than they do between two similarly sized lawns."),
    ],
    "sources": SRC,
}

LOCAL["pavers"] = {
    "title": "Turf and Pavers for Poinciana Driveways and Walks",
    "meta": "Turf between pavers in Poinciana, FL is quoted per job, working within APV's driveway width limits and walkway rules that apply across the villages.",
    "h1": "Turf ribbons and paver paths built to Poinciana's driveway rules",
    "lede": capsule(
        "A driveway ribbon, a stepping-stone path and a patio border in Poinciana each use "
        "different quantities of paver and turf for the same footprint, which is why this work "
        "gets priced per job rather than at a flat rate per square foot. Here the layout starts "
        "with APV's own driveway width limit, a hard number that shapes the design before anyone "
        "draws it."
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
        "driveway on a Village 3 lot, going in alongside the pavers themselves and staying well "
        "under the 24-foot combined width cap. Pricing comes from the driveway's own drawings "
        "instead of a flat rate per square foot, since the paver base and the turf strip beside "
        "it compact differently but still have to land at one shared grade, and the DCB reviews "
        "both materials together as a single landscaping submittal rather than two separate "
        "ones.</p>"
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
        "What a repair costs in Poinciana depends on what the crew finds once the turf is pulled "
        "back, so each visit is quoted on its own rather than by the square foot. Two questions "
        "shape most calls here: how old the install is in one of the original 1970s-80s "
        "villages, and whether the property is about to change hands, since a resale on these "
        "streets often surfaces turf nobody's inspected in years."
    ),
    "sections": [
        ("A resale on an older street is when repair questions surface",
         "<p>Poinciana's first villages date to the community's 1972 founding, and turf converted "
         "there over the past 10 to 15 years changes hands with the house more often than it gets "
         "inspected on its own terms. A resale on one of these older streets is usually the first "
         "time anyone asks whether a manufacturer's warranty transfers to a new owner, and the "
         "honest answer is that it depends on paperwork the seller may or may not still have: "
         "most warranties want the original invoice, and some want proof the base was built to "
         "spec. A repair call ahead of a closing is worth treating as a chance to document what's "
         "actually under the turf, since that record is what any later warranty question comes "
         "back to. " + post("does-homeowners-insurance-cover-artificial-turf", "Our guide to insurance and turf damage")
         + " covers the separate question of what a storm claim does and doesn't pay for.</p>"),
        ("A Solivita repair still clears the same review as new work",
         "<p>Fixing a lifted seam or a settled corner on a Solivita villa sounds like plain "
         "maintenance, but the ARC doesn't automatically treat a like-for-like repair differently "
         "from a new landscaping change; the Architectural Review Requirements cover \"any "
         "exterior addition, changes, modifications or alterations,\" and a repair that touches "
         "the visible surface of the lawn falls inside that wording. In practice a straightforward "
         "reseat of an existing edge rarely needs the full submittal a new installation would, but "
         "a repair that expands the footprint or swaps in a different product is the kind of "
         "change worth confirming with the ARC before the crew starts rather than after.</p>"),
        ("Canal-adjacent turf takes the most weather, and the setback is worth rechecking",
         "<p>A lawn backing onto one of Poinciana's drainage canals or retention ponds takes more "
         "water at its perimeter than an interior lot does, since storm runoff working against an "
         "unprotected edge can loosen a seam or a nailed border faster than it would away from "
         "open water. Central Florida's storm season adds to that wear: a named storm can lift or "
         "shift an older install anchored to a lighter standard than today's rule requires, and a "
         "repair visit after one typically starts by checking whether the base underneath washed "
         "out before simply renailing a corner back down. A lifted edge near a canal is also "
         "worth checking against the state's 10-foot waterbody setback, since an install that "
         "predates the current rule sometimes sits closer to the bank than the state would allow "
         "for a brand-new layout. " + post("artificial-turf-hurricane-flooding", "Our piece on turf after a hurricane or flood")
         + " covers what that inspection looks for.</p>"),
    ],
    "scenario": (
        "Say you have a repair call ahead of closing on a Village 1 resale",
        "<p>Say you have a repair call ahead of closing on a Village 1 resale, a decade-old dog "
        "run along the fence line with one corner lifting and a seller who can't find the "
        "original invoice. The visit starts with the same diagnosis any repair gets, checking "
        "whether the rock underneath washed out before renailing the corner, but it also means "
        "documenting what the crew finds, base depth, drainage condition, infill type, since that "
        "record is what the buyer's own warranty question will lean on later. Reseating the edge "
        "without that documentation fixes the corner but leaves the ownership question exactly "
        "where it was.</p>"
    ),
    "faqs": [
        faq("Does a manufacturer's turf warranty transfer to a new owner in Poinciana?",
            "It depends on the manufacturer and the paperwork the seller kept. Most warranties "
            "ask for the original invoice, and some ask for proof the base met spec at "
            "installation, so confirming that documentation before closing is worth doing on any "
            "of the community's older resale streets."),
        faq("Does a like-for-like repair in Solivita need ARC approval?",
            "Often not a full submittal for a straightforward reseat of an existing edge, but the "
            "Architectural Review Requirements cover any exterior alteration, so a repair that "
            "changes the footprint or swaps in a different product is worth confirming with the "
            "ARC first rather than after."),
    ],
    "sources": SRC,
}

LOCAL["cleaning"] = {
    "title": "Turf Cleaning and Care Across Poinciana Villages",
    "meta": "Turf cleaning in Poinciana, FL is quoted by yard size and visit history, timed around the rainy season and the water table on canal- and pond-adjacent lots.",
    "h1": "Keeping Poinciana turf clean, from village lawns to canal-side yards",
    "lede": capsule(
        "How big the yard is and how long it's been since the last visit set the price for turf "
        "cleaning in Poinciana, not a flat rate per square foot. Two things drive the schedule "
        "here more than tree canopy does: the rainy-season water table under Poinciana's "
        "flatwoods soil, and how close the lot sits to one of the community's drainage canals or "
        "retention ponds."
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
        "shaded by young landscaping too new to drop much leaf litter yet. Pricing that visit "
        "starts with how damp the pond-adjacent ground has kept the infill and how many months "
        "have passed since anyone last cleared it, since a lawn left alone over a full rainy "
        "season needs meaningfully more work than one kept on a tighter summer rotation.</p>"
    ),
    "faqs": [
        faq("Does turf near a Poinciana pond need cleaning more often than an interior lot?",
            "Often, since ground next to a retention pond or canal holds moisture nearer the "
            "surface than higher lots do elsewhere in the same village, and that extra dampness "
            "is usually what pushes a lawn onto a tighter schedule through the wettest months."),
        faq("Do Poinciana's older villages need more frequent cleaning than newer ones?",
            "Usually, since the mature landscaping in the original 1970s-80s villages drops more "
            "leaf litter and organic debris than the younger plantings in sections built since "
            "the 2000s."),
    ],
    "sources": SRC,
}

LOCAL["replacement"] = {
    "title": "Turf Removal and Replacement in Poinciana, FL",
    "meta": "Turf replacement in Poinciana, FL is quoted per job after a base inspection, for lawns converted in the community's earliest 1970s-80s villages.",
    "h1": "Replacing worn turf in Poinciana's earliest villages",
    "lede": capsule(
        "A full tear-out and relay in Poinciana gets priced per job once the crew has opened up "
        "the old lawn, not from a flat rate per square foot. The community's original villages "
        "date to 1972, and turf put in there anywhere from the early 2010s back is now old "
        "enough in places that replacement, rather than another round of spot repair, is the "
        "straight answer."
    ),
    "sections": [
        ("Two growth waves left two different replacement timelines",
         "<p>Turf generally lasts 10 to 20 years depending on UV stabilization, traffic and "
         "infill, and Poinciana's oldest conversions cluster around two distinct building waves: "
         "the first villages built soon after the 1972 founding, and the larger wave that "
         "followed once Avatar Holdings, later AV Homes, took over development in the mid-1980s. "
         "A lawn converted early in either wave is closer to the upper end of that service-life "
         "range than one converted in a 2000s-era section of the same village, which matters more "
         "to a replacement timeline than the house's own age does. "
         + post("how-long-does-artificial-turf-last-in-florida", "Our guide to turf lifespan in Florida")
         + " covers what shortens that window on a given lot.</p>"),
        ("The state's material rule is newer than a lot of the turf already down",
         "<p>Rule 62-308.100 didn't take effect until May 2026, which means turf installed in "
         "Poinciana any time before that could have gone in over unwashed base material or with "
         "an infill the rule wouldn't allow on a new job today. A full replacement is the point "
         "where that gets corrected as a matter of course, since the old base and infill come out "
         "with the worn turf anyway; there's no separate obligation to retrofit a yard that isn't "
         "being touched, but rebuilding to the current standard while the ground is already open "
         "costs little extra against putting the same specification back.</p>"),
        ("Replacement is also when the village board looks again",
         "<p>APV's and Solivita's landscaping criteria treat a full tear-out and relay as an "
         "exterior change no different from a first-time install, so a replacement project goes "
         "back through the DCB or the ARC even on a lawn that's carried turf for a decade or more "
         "already. That second look is also the practical moment to confirm a canal- or "
         "pond-adjacent layout against the state's 10-foot waterbody setback, since an install "
         "that predates the current rule can sit closer to the water than a new submittal would "
         "be approved for today. " + post("what-does-artificial-turf-warranty-cover", "Our piece on what a turf warranty actually covers")
         + " is worth reading before assuming a manufacturer's coverage still applies to a lawn "
         "this old.</p>"),
    ],
    "scenario": (
        "Say you have a 2011-installed lawn in Village 2",
        "<p>Say you have a lawn converted to turf in 2011 in Village 2, worn thin along the path "
        "from the driveway to the back gate and slower to drain than it used to be after a "
        "storm. At roughly 15 years in the ground, that lawn is deep into its expected service "
        "window, and a replacement quote works out from what the crew finds once the old turf "
        "comes up, whether the rock underneath still drains well enough to reuse or has to come "
        "out along with everything on top of it.</p>"
    ),
    "faqs": [
        faq("How do I know if Poinciana turf needs replacing instead of repairing?",
            "The condition of the rock underneath, not just how the surface looks, is what "
            "decides it. If that base still drains well once probed, a repair on the surface is "
            "often enough; if it's crusted over or holding water, replacement is the more honest "
            "fix, and the only way to tell for certain is to open up a section and look."),
        faq("Does a replacement project need DCB or ARC approval again?",
            "Yes. Either board treats a full tear-out and relay as an exterior change no "
            "different from new construction, so the same landscaping submittal applies "
            "regardless of how long turf was already on the lot."),
    ],
    "sources": SRC,
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
