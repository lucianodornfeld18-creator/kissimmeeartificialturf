# -*- coding: utf-8 -*-
"""St. Cloud, FL city hub + city x service pages."""
from _helpers import page, capsule, sec, table, faq, a, svc, city, post, src, ext, price
from _cityservice import cityservice_pages

SLUG = "st-cloud"

SRC = [
    ("City of St. Cloud - Building Department", "https://www.stcloudfl.gov/2105/Building-Department"),
    ("City of St. Cloud - Permit Information", "https://stcloudfl.gov/50/Permit-Information"),
    ("Osceola County - Building Office Plan Review", "https://www.osceola.org/Doing-Business/Building-and-Permits/Building-Office-Plan-Review"),
    ("Osceola County Property Appraiser - parcel search", "https://search.property-appraiser.org/"),
    ("City of St. Cloud - Watering Schedules", "https://stcloudfl.gov/1683/Watering-Schedules"),
    ("Toho Water Authority - utility consolidation with St. Cloud, October 2022", "https://www.tohowater.com/sites/default/files/2022-10/10.4.22%20St.%20Cloud.pdf"),
    ("Toho Water Authority - St. Cloud service area", "https://tohowater.com/st-cloud"),
    ("South Florida Water Management District - Upper Kissimmee Basin water supply plan", "https://www.sfwmd.gov/our-work/water-supply/upper-kissimmee"),
    ("St. Johns River Water Management District (Wikipedia)", "https://en.wikipedia.org/wiki/St._Johns_River_Water_Management_District"),
    ("USDA NRCS - Official Series Description, Myakka series", "https://soilseries.sc.egov.usda.gov/osd_docs/m/myakka.html"),
    ("USDA NRCS - Official Series Description, Immokalee series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/I/IMMOKALEE.html"),
    ("USDA NRCS - Official Series Description, Smyrna series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/S/SMYRNA.html"),
    ("East Lake Tohopekaliga (Wikipedia)", "https://en.wikipedia.org/wiki/East_Lake_Tohopekaliga"),
    ("Osceola County History - History of St. Cloud", "https://osceolahistory.org/history-of-st-cloud/"),
    ("Experience Kissimmee - The history behind downtown St. Cloud", "https://www.experiencekissimmee.com/article/history-behind-downtown-st-cloud-soldier-city"),
    ("Grand Army of the Republic Memorial Hall, St. Cloud (Wikipedia)", "https://en.wikipedia.org/wiki/Grand_Army_of_the_Republic_Memorial_Hall_(St._Cloud,_Florida)"),
    ("Florida Hikes - St. Cloud, Lakefront Park", "https://floridahikes.com/st-cloud/"),
    ("Sunbridge, Florida (Wikipedia)", "https://en.wikipedia.org/wiki/Sunbridge,_Florida"),
    ("Del Webb Sunbridge HOA - Architectural Criteria, July 2020", "https://www.delwebbsunbridgehoa.com/documents/20124/0/Del+Webb+Sunbridge+-+Architectural+Criteria.pdf/4fed5940-3233-08b5-2ae8-f171ae1639ee?t=1732044538865"),
    ("AARoads - Osceola County Road 534, Hickory Tree Road", "https://www.aaroads.com/guides/cr-534-fl"),
    ("Holopaw, Florida (Wikipedia)", "https://en.wikipedia.org/wiki/Holopaw,_Florida"),
    ("BNBCalc - St. Cloud, Florida short-term rental regulations", "https://www.bnbcalc.com/blog/short-term-rental-regulation/St-Cloud-Florida-Guide"),
    ("City of St. Cloud - Landlord Business Tax Receipt", "https://www.stcloudfl.gov/1210/Landlord-BTR"),
    ("Florida Demographics - St. Cloud", "https://www.florida-demographics.com/st-cloud-demographics"),
    ("St. Cloud, Florida (Wikipedia)", "https://en.wikipedia.org/wiki/St._Cloud,_Florida"),
]

# ------------------------------------------------------------------ HUB
HUB = page(
    "/areas/st-cloud/", "city",
    "Artificial Turf in St. Cloud, FL: Local Guide (2026)",
    "St. Cloud, FL artificial turf guide: city vs. Osceola County permits, Toho Water rules, East Lake Toho setbacks, soil and HOAs, updated September 2026.",
    "Artificial turf installation and care in St. Cloud, Florida",
    capsule(
        "St. Cloud sits about " + str(8) + " miles east of downtown "
        + city("kissimmee") + ", and the right turf build here depends on the lot: a narrow platted "
        "block near the 1909 downtown grid, a canal lot on East Lake Tohopekaliga, a 1990s subdivision "
        "off Canoe Creek Road, or a half-acre well-and-septic parcel toward Holopaw. Installed turf runs "
        + price("residential") + " a square foot as of September 2026, and permitting splits between the "
        "city and unincorporated Osceola County depending on the address."
    ),
    "".join([
        sec("What makes a St. Cloud yard different from the rest of Osceola County?",
            "<p>" + ext("https://osceolahistory.org/history-of-st-cloud/", "St. Cloud was platted in 1909")
            + " as a retirement colony for Grand Army of the Republic Civil War veterans, and its downtown "
            "grid still carries that history: streets running toward the lake are numbered, while the "
            "cross streets carry the names of states, Union states first, Confederate states added as the "
            "grid grew. That old platted core, tight lots and mature trees, sits within a few miles of "
            "East Lake Tohopekaliga, a working lake of roughly 11,000 acres tied to the rest of the "
            + ext("https://en.wikipedia.org/wiki/East_Lake_Tohopekaliga", "Kissimmee chain by a canal") + ". "
            "Outward from both, growth looks nothing like 1909: a 27,000-acre master-planned community "
            "called " + ext("https://en.wikipedia.org/wiki/Sunbridge,_Florida", "Sunbridge") + " is filling "
            "in the county land south and east of the city, while acreage lots on well and septic still run "
            "toward Holopaw along US 192/441. A " + svc("residential") + " quote has to account for which "
            "of those four settings the yard sits in before it accounts for anything else.</p>"),
        table("St. Cloud yard types and what we do differently",
              ["Yard type", "Where", "What's different", "What we do differently"],
              [
                  ["Historic platted lot", "Downtown grid, numbered and state-named streets",
                   "Narrow lots, mature live oaks, homes dating to the 1920s boom", "Shallow, careful excavation and an arborist check before working inside a drip line"],
                  ["Lakefront or canal lot", "East Lake Tohopekaliga and its connecting canal",
                   "Higher water table, a seawall or open shoreline within feet of the lawn", "Hold turf back from the water by the state's 10-foot rule unless a seawall already separates the two"],
                  ["1980s-2000s subdivision", "Off Canoe Creek Road and Old Hickory Tree Road",
                   "Fenced backyards, established landscaping, some HOA review", "Confirm what's visible from the street before treating a backyard project as a front-yard one"],
                  ["New master-planned growth", "Sunbridge, Weslyn Park and nearby new construction",
                   "Fill-graded lots, builder sod, active architectural review", "Route any turf plan through the community's landscape approval before ordering material"],
                  ["Rural acreage", "East toward Holopaw, unincorporated county", "Well water, septic systems, no HOA", "Build a deeper base for bigger runs and keep the septic tank lid clear"],
              ],
              "Prices don't change by yard type; access, base depth and paperwork do."),
        sec("Does St. Cloud or Osceola County review a turf project?",
            "<p>Which office reviews the work depends on whether the address sits inside city limits. Inside "
            "St. Cloud, that's the " + ext("https://www.stcloudfl.gov/2105/Building-Department", "city's Building Department")
            + " at 1300 9th Street, phone 407-957-7300, with an online portal for tracking a permit once it's "
            "filed. Outside the city line, Osceola County's " + ext("https://www.osceola.org/Doing-Business/Building-and-Permits/Building-Office-Plan-Review", "Building Office")
            + " handles it instead, at 1 Courthouse Square in Kissimmee, phone 407-742-0200. Streets like Old "
            "Hickory Tree Road and Nova Road sit in unincorporated county territory even though the mailing "
            "address says St. Cloud, which trips up homeowners who assume the city handles everything with a "
            "34771 or 34772 ZIP. The fastest way to check which one applies to a specific parcel is "
            + ext("https://search.property-appraiser.org/", "the Osceola County Property Appraiser's parcel search")
            + ", which lists the jurisdiction on the same record as the lot size and legal description. Full "
            "detail on what each office asks for lives on our own " + a("/laws/permits/city-of-st-cloud/", "City of St. Cloud permit page")
            + " and " + a("/laws/permits/osceola-county/", "Osceola County permit page") + ".</p>"),
        sec("Where does St. Cloud's water come from, and what are the watering days?",
            "<p>St. Cloud ran its own utility until October 1, 2022, when it "
            + ext("https://www.tohowater.com/sites/default/files/2022-10/10.4.22%20St.%20Cloud.pdf", "consolidated into Toho Water Authority")
            + ", the same provider that serves Kissimmee, and most St. Cloud accounts saw rates go down rather "
            "than up as a result. Toho's " + ext("https://stcloudfl.gov/1683/Watering-Schedules", "published watering schedule")
            + " runs two assigned days a week by address, with no daytime irrigation, and Florida's synthetic "
            "turf rule adds a separate requirement on top of that: an in-ground irrigation system can never be "
            "used on synthetic turf at all, watering days or not. East Lake Tohopekaliga and the rest of the "
            "Kissimmee chain fall inside the "
            + ext("https://www.sfwmd.gov/our-work/water-supply/upper-kissimmee", "South Florida Water Management District's Upper Kissimmee Basin")
            + ", while the county's eastern edge toward Holopaw touches the "
            + ext("https://en.wikipedia.org/wiki/St._Johns_River_Water_Management_District", "St. Johns River Water Management District")
            + " instead, a detail that matters more for a well permit than for a turf installation.</p>"),
        sec("What's the soil under a St. Cloud lawn?",
            "<p>Most of the flatwoods around St. Cloud map to poorly drained, sandy series established for exactly "
            "this part of Florida: " + ext("https://soilseries.sc.egov.usda.gov/osd_docs/m/myakka.html", "Myakka")
            + ", " + ext("https://soilseries.sc.egov.usda.gov/OSD_Docs/I/IMMOKALEE.html", "Immokalee") + " and "
            + ext("https://soilseries.sc.egov.usda.gov/OSD_Docs/S/SMYRNA.html", "Smyrna") + ", the last of which "
            "was first described in this county. All three sit on fine sand with a spodic layer that perches "
            "water not far below grade, and that layer sits closer to the surface on lots nearer East Lake "
            "Tohopekaliga than it does on higher ground toward Sunbridge. A base built to the state's washed, "
            "open-graded standard clears that difference the same way everywhere, just with more depth where the "
            "flatwoods run wetter. There's more on how that base gets built in "
            + post("base-under-artificial-turf-florida-sandy-soil", "our guide to Central Florida's sandy base")
            + ".</p>"),
        sec("Where do the state's lake, canal and tree rules actually apply here?",
            "<p>Three of Florida's synthetic-turf requirements show up constantly on a St. Cloud site visit. "
            "Near East Lake Tohopekaliga or its connecting canal, turf has to stop at least 10 feet from the "
            "water unless a seawall or bulkhead already separates the yard from it, and a canal lot with a "
            "vertical seawall often clears that rule where an open bank wouldn't. Under the old-growth oaks "
            "at " + ext("https://floridahikes.com/st-cloud/", "Lakefront Park") + " and the downtown streets "
            "around them, turf can't go inside a live oak's drip line unless a certified arborist signs off "
            "that the install won't damage the roots. And on the well-and-septic lots east of town, turf has "
            "to leave the septic tank lid reachable for a pump-out truck, which changes where a run or a lawn "
            "edge can land on a Holopaw-area parcel. None of these are new Osceola County ordinances; they come "
            "straight from " + src("dep-rule", "the state's Rule 62-308.100") + ", adopted May 19, 2026.</p>"),
        sec("What can an HOA in St. Cloud actually restrict?",
            "<p>Florida law, " + src("fs7203045", "F.S. 720.3045") + ", already limits what any homeowners "
            "association statewide can restrict: an HOA can't ban something not visible from the parcel's "
            "frontage or an adjacent parcel, and the statute names artificial turf specifically. A fenced "
            "backyard off Canoe Creek Road is generally protected on that basis; a front lawn is not. Newer "
            "communities still run their own architectural review regardless of what's visible. At Del Webb "
            "Sunbridge, the 55-plus section of the Sunbridge development, "
            + ext("https://www.delwebbsunbridgehoa.com/documents/20124/0/Del+Webb+Sunbridge+-+Architectural+Criteria.pdf/4fed5940-3233-08b5-2ae8-f171ae1639ee?t=1732044538865", "any landscape change has to go through the HOA's contracted landscape vendor")
            + " and an architectural review application before work starts, whatever the change is. Full rules "
            "for the state law and how HOAs interact with it are in " + a("/laws/hoa-rules/", "what a Florida HOA can and can't restrict")
            + ".</p>"),
        sec("Looking for an installer in St. Cloud?",
            "<p>How do you pick the best artificial turf contractor in St. Cloud? Ask three things before "
            "anything else: which office, the city or the county, they expect to file the permit with for the "
            "address in question, how deep they're building the washed-rock base, and whether they've priced "
            "the lake or canal setback into the layout if the lot backs onto water. An installer who answers "
            "those three without hesitation has usually done the homework already.</p>"),
        "<!--AUTO:city-services-->",
    ]),
    faqs=[
        faq("Does the City of St. Cloud require a permit for artificial turf?",
            "It depends on scope and address. Turf itself isn't a state-licensed trade, but grading, drainage "
            "changes or work tied to a pool deck can trigger review. Call the city's Building Department at "
            "407-957-7300 for an in-city address, or Osceola County's Building Office at 407-742-0200 for an "
            "unincorporated one, before assuming either way."),
        faq("How do I know if my St. Cloud address is inside city limits?",
            "Look the parcel up on the Osceola County Property Appraiser's site. The record shows the taxing "
            "jurisdiction along with the legal description, which settles it faster than guessing from a ZIP "
            "code, since 34771 and 34772 both cover city and unincorporated county addresses."),
        faq("Can a St. Cloud HOA make me remove backyard turf?",
            "Not if it's not visible from the street or a neighboring parcel; F.S. 720.3045 protects that "
            "regardless of what a covenant says. A front yard, or a corner lot visible from two streets, "
            "doesn't get that protection, and a newer community's architectural review still applies to any "
            "landscape change either way."),
        faq("How close can turf go to East Lake Tohopekaliga?",
            "At least 10 feet from the water's edge, unless a seawall or bulkhead already separates the lawn "
            "from the lake or canal, in which case that barrier satisfies the setback. The same 10-foot rule "
            "covers a retention pond or a drainage canal anywhere else on the property."),
        faq("What soil should I expect on a St. Cloud lot?",
            "Mostly Myakka, Immokalee or Smyrna, all fine sand with a layer that holds water not far below the "
            "surface. Lots closer to East Lake Tohopekaliga tend to run wetter than higher ground toward "
            "Sunbridge, which is why we check the water table on site rather than assuming one base depth "
            "fits every address."),
    ],
    sources=SRC,
    city=SLUG,
    crumbs=[("Service areas", "/areas/")],
    crumb="St. Cloud",
    related=[
        ("/areas/osceola-county/", "Artificial turf in Osceola County"),
        ("/laws/permits/city-of-st-cloud/", "City of St. Cloud permit rules"),
        ("/laws/permits/osceola-county/", "Osceola County permit rules"),
        ("/areas/harmony/", "Artificial turf in Harmony"),
        ("/areas/narcoossee/", "Artificial turf in Narcoossee"),
        ("/artificial-turf-cost/", "Turf cost tables for Central Florida"),
    ],
)

# ------------------------------------------------------------------ LOCAL
LOCAL = {}

LOCAL["residential"] = {
    "title": "Artificial Grass Installation in St. Cloud, FL",
    "meta": "Artificial grass in St. Cloud, FL runs $8-$18 a sq ft installed as of September 2026. Downtown lots, Sunbridge fill and city vs. county permits, explained.",
    "h1": "Artificial grass for St. Cloud lawns, from downtown lots to new construction",
    "lede": capsule(
        "A synthetic lawn in St. Cloud, Florida costs " + price("residential") + " a square foot installed "
        "as of September 2026, whether the address is a 1920s lot inside the historic grid or a new build "
        "in the Sunbridge growth area. What changes the number is the lot: a narrow downtown yard takes "
        "longer to access than an open new-construction rectangle, and which office reviews the permit "
        "depends on whether the address sits inside city limits."
    ),
    "sections": [
        ("A downtown lot and a Sunbridge lot don't file the same permit",
         "<p>St. Cloud's original townsite, platted in 1909 with numbered streets running one way and "
         "state-named cross streets the other, sits entirely inside city limits, so a lawn conversion there "
         "goes through the city's Building Department rather than the county. Newer growth south and east, "
         "including much of the Sunbridge development, mixes city and unincorporated Osceola County parcels "
         "depending on the phase, so the address decides which office reviews the work, not the subdivision "
         "name. Checking the parcel on the county's property appraiser site before calling anyone saves a "
         "misdirected phone call.</p>"),
        ("Why builder sod struggles on a fill lot faster than it used to",
         "<p>New construction around Sunbridge and Weslyn Park sits on graded fill rather than native ground, "
         "and builder-grade sod on that kind of lot often thins out within a year or two once irrigation "
         "settles into a normal schedule. " + post("why-new-construction-sod-dies-in-osceola-county", "Our piece on why new-construction sod struggles in Osceola County")
         + " goes into the mechanics; the short version is that a compacted fill pad drains and holds "
         "nutrients differently than the topsoil sod was grown on. A homeowner who's already replaced sod "
         "twice on a new St. Cloud lot is usually the one asking about turf next.</p>"),
        ("What the 2022 water consolidation changed for a lawn conversion",
         "<p>St. Cloud folded its utility into Toho Water Authority on October 1, 2022, and most St. Cloud "
         "accounts saw their rates drop rather than climb. That's a separate question from whether a new "
         "lawn can use in-ground irrigation at all: the state's turf rule bars it outright, so any sprinkler "
         "zone under a converted section gets capped at the valve box regardless of which utility bills for "
         "the water. Homeowners converting a full front and back yard sometimes ask whether that capped zone "
         "affects their Toho bill; it only lowers it, since that zone stops pulling water entirely.</p>"),
    ],
    "scenario": (
        "Say you have a 950 sq ft yard",
        "<p>Say you have a 950 sq ft front and side yard on a 1960s lot two blocks off the downtown grid, "
        "St. Augustine that's thinned out under a pair of mature oaks. At " + price("residential", True)
        + " a square foot, mid-grade turf for that area runs roughly $10,450 to $13,300, with the oaks "
        "themselves setting the real limit: excavation has to stay outside their drip line unless a "
        "certified arborist signs off first, which can shrink the usable footprint on a tight urban lot more "
        "than the square footage alone suggests. The permit for this address goes to the city, since it "
        "sits inside St. Cloud's limits, not the county.</p>"
    ),
    "faqs": [
        faq("Does turf cost more on a downtown St. Cloud lot than a new one?",
            "The per-square-foot range is the same either way. What changes is labor time: a narrow historic "
            "lot with mature trees and tight side access takes longer to excavate than an open new-construction "
            "rectangle, which is what pushes a small urban yard toward the top of the range."),
        faq("How do I find the best artificial grass installer near me in St. Cloud?",
            "Ask which office, city or county, they expect to file with for your specific address, and ask "
            "them to walk the yard before quoting rather than pricing from a satellite photo. An installer "
            "who can't answer the jurisdiction question hasn't done a St. Cloud job recently."),
    ],
    "sources": SRC,
}

LOCAL["pet"] = {
    "title": "Pet Turf & Dog Runs in St. Cloud, FL",
    "meta": "Pet turf in St. Cloud, FL runs $10-$18 a sq ft installed as of September 2026, built for half-acre well lots and fenced backyards off Canoe Creek Road.",
    "h1": "Dog runs and pet turf for St. Cloud yards, from acreage to a fenced backyard",
    "lede": capsule(
        "Pet turf installed in St. Cloud, Florida runs " + price("pet") + " a square foot as of September "
        "2026, and the build changes with the lot: a half-acre well-and-septic parcel east toward Holopaw "
        "can carry a much bigger run than a fenced backyard in a 1990s subdivision off Canoe Creek Road, "
        "where the yard itself sets the limit rather than anything a covenant says."
    ),
    "sections": [
        ("Bigger runs on well-and-septic acreage toward Holopaw",
         "<p>East of St. Cloud toward Holopaw, unincorporated Osceola County lots commonly run a half-acre "
         "or more on well water and a septic system rather than public sewer, which changes two things about "
         "a dog yard build. First, there's room for a run sized for multiple dogs without crowding the rest "
         "of the yard. Second, the state's turf rule requires keeping the septic tank lid reachable for a "
         "pump-out truck, so a run's layout has to work around that access point rather than covering it. "
         "Well water also means rinsing a run doesn't show up on a metered Toho bill the way it does closer "
         "to town.</p>"),
        ("Fenced backyards off Canoe Creek Road and Old Hickory Tree Road",
         "<p>Subdivisions built through the 1980s to the 2000s along Canoe Creek Road and Old Hickory Tree "
         "Road, a route " + ext("https://www.aaroads.com/guides/cr-534-fl", "documented as Osceola County Road 534")
         + ", typically put a privacy fence around the backyard, which under F.S. 720.3045 keeps a dog run "
         "there outside an HOA's reach regardless of what a covenant says about ground cover. A run visible "
         "from the street or a side yard facing a neighbor doesn't get that same protection, which matters on "
         "a corner lot in one of these older subdivisions more than on an interior lot.</p>"),
        ("Why the flatwoods soil here makes drainage non-negotiable",
         "<p>Much of St. Cloud sits on Myakka or Immokalee series soil, both fine sand with a layer that "
         "holds water not far below grade, and that layer runs shallower on lots closer to East Lake "
         "Tohopekaliga than on higher ground. A pet system's deeper base and fully permeable backing matter "
         "more here than on a plain lawn, since a dog run built on a lot with a high water table already "
         "working against it has less margin for a shallow or unwashed base before odor becomes a "
         "year-round problem instead of a rainy-season one.</p>"),
    ],
    "scenario": (
        "Say you have two dogs on a Holopaw-area half-acre",
        "<p>Say you have two large dogs on a half-acre lot toward Holopaw, on well water and septic, with a "
        "worn dirt path along the back fence where the grass gave up years ago. A 400 sq ft run at "
        + price("pet", True) + " a square foot runs roughly $4,800 to $6,400, built with the fuller "
        "three-to-four-inch base depth this soil calls for and routed so the septic tank's access lid stays "
        "clear. There's no HOA here to file paperwork with, which is one advantage a rural lot has over a "
        "fenced yard closer to town.</p>"
    ),
    "faqs": [
        faq("Do I need county approval for a dog run on unincorporated land near Holopaw?",
            "Fencing and structures can trigger a permit, so it's worth a call to Osceola County's Building "
            "Office at 407-742-0200 before digging, especially if the run includes a covered section. Turf "
            "itself isn't a licensed trade, but grading and drainage changes can still fall under review."),
        faq("Does a St. Cloud HOA count a dog run as artificial turf it can restrict?",
            "If it's inside a fenced backyard not visible from the street or an adjacent lot, F.S. 720.3045 "
            "protects it regardless of the label. A run built along a side yard facing a neighbor's driveway "
            "may not get that same protection, so check sightlines before assuming the statute covers it."),
    ],
    "sources": SRC,
}

LOCAL["putting"] = {
    "title": "Backyard Putting Greens in St. Cloud, FL",
    "meta": "Backyard putting greens in St. Cloud, FL run $14-$30 a sq ft installed as of September 2026, sized for Sunbridge lots, acreage and older downtown yards.",
    "h1": "Putting greens built for St. Cloud lots, from Sunbridge to acreage toward Holopaw",
    "lede": capsule(
        "A backyard putting green in St. Cloud, Florida runs " + price("putting") + " a square foot "
        "installed as of September 2026. Lot size drives the design more here than anywhere else in the "
        "build: a gated 55-plus section of Sunbridge has its own architectural review for any yard change, "
        "while a rural acre toward Holopaw has room for a green two or three times the size with no "
        "committee to answer to."
    ),
    "sections": [
        ("Del Webb Sunbridge and the review that comes before the green",
         "<p>Del Webb Sunbridge, the 55-plus gated section of the wider Sunbridge development, "
         + ext("https://www.delwebbsunbridgehoa.com/documents/20124/0/Del+Webb+Sunbridge+-+Architectural+Criteria.pdf/4fed5940-3233-08b5-2ae8-f171ae1639ee?t=1732044538865", "requires any landscape modification to go through the HOA's contracted landscape vendor")
         + " and an architectural review submittal before work starts. That process asks for color samples "
         "and a site plan the same way it would for any hardscape change, which means a putting green project "
         "here needs that paperwork lined up before a crew ever shows up to shape the base.</p>"),
        ("Bigger greens fit on Holopaw-area acreage",
         "<p>Unincorporated lots east toward Holopaw run larger, often a half-acre to several acres on well "
         "and septic, with no homeowners association to submit plans to at all. A green designed for that "
         "kind of lot can carry more tiers and a longer chipping approach than a suburban backyard allows, "
         "since the limiting factor becomes budget and the septic system's drain field location rather than "
         "lot width or an HOA's size cap.</p>"),
        ("Sizing a green for a lot inside St. Cloud's 1909 grid",
         "<p>Downtown St. Cloud's original platted lots, laid out when the city was founded as a Grand Army "
         "of the Republic veterans' colony, tend to run narrower and shallower than a modern suburban lot, "
         "and mature live oaks common to that part of town add another constraint the state's drip-line rule "
         "enforces directly. A green on one of these lots usually means a smaller single-tier design tucked "
         "to one side of the yard rather than the multi-tier layout an open acreage lot can support.</p>"),
    ],
    "scenario": (
        "Say you have a 400 sq ft Sunbridge backyard",
        "<p>Say you have a 400 sq ft backyard in a Del Webb Sunbridge villa with a screened lanai on one "
        "side, wanting a small green with a single cup rather than a full multi-tier design. At "
        + price("putting", True) + " a square foot, that runs roughly $7,200 to $10,000, plus the time it "
        "takes to clear the HOA's landscape vendor and architectural review before the base gets shaped. A "
        "similarly sized green on an unincorporated acreage lot toward Holopaw skips that review step "
        "entirely, though it still needs the same base and drainage work underneath.</p>"
    ),
    "faqs": [
        faq("Do I need HOA approval for a putting green at Del Webb Sunbridge?",
            "Yes. The community's architectural criteria route any landscape change through its contracted "
            "landscape vendor, with a full submittal before work begins. Budget time for that review before "
            "scheduling installation."),
        faq("What do the best putting green builders near you check on a Sunbridge lot before quoting?",
            "Whether the community's landscape vendor and architectural review apply to the phase the lot "
            "sits in, and how much of the backyard a screened lanai or property line leaves usable for the "
            "green's shape."),
        faq("Can a putting green go on a well-and-septic lot near Holopaw?",
            "Yes, and the larger lot size out there often allows a bigger design than a suburban yard would. "
            "The base still has to leave the septic tank's access point clear, which the design accounts for "
            "before excavation starts."),
    ],
    "sources": SRC,
}

LOCAL["playground"] = {
    "title": "Playground Turf for St. Cloud, FL Backyards",
    "meta": "Playground turf in St. Cloud, FL runs $10-$25 a sq ft installed as of September 2026, sized for new Sunbridge families and established Canoe Creek yards.",
    "h1": "Backyard play turf across St. Cloud's growing family neighborhoods",
    "lede": capsule(
        "Playground turf installed in St. Cloud, Florida runs " + price("playground") + " a square foot as "
        "of September 2026. St. Cloud's population has roughly doubled since 2010, and much of that growth "
        "is young families moving into new construction south and east of downtown, which is where most "
        "backyard play-turf requests in this town come from."
    ),
    "sections": [
        ("A city that's grown around families, not retirees, since 2010",
         "<p>St. Cloud's population grew from roughly 38,000 in 2010 to more than 70,000 today, and most of "
         "that new housing sits in family-oriented neighborhoods rather than age-restricted ones. Weslyn "
         "Park, the family section of the Sunbridge development, is one of the newest examples, with a "
         "waterfront gathering place planned as part of its build-out. A backyard play surface in one of "
         "these newer neighborhoods usually goes in on a flat, freshly graded fill lot with no mature trees "
         "yet to work around.</p>"),
        ("Play areas under oaks in the older Canoe Creek subdivisions",
         "<p>Subdivisions built from the 1980s through the 2000s off Canoe Creek Road carry established "
         "landscaping that new construction doesn't have yet, including live oaks that have had two or three "
         "decades to grow. A swing set or play structure going into one of these older yards has to respect "
         "the same drip-line rule as any other turf project, which sometimes means shifting a play area a "
         "few feet from where a family originally pictured it.</p>"),
        ("Keeping a play area clear of the lake setback on older lakefront lots",
         "<p>A handful of older homes back directly onto East Lake Tohopekaliga or its connecting canal, and "
         "a play area on one of those lots has to stay outside the state's 10-foot waterbody setback the same "
         "as any other turf, unless a seawall already separates the yard from the water. That rule applies "
         "regardless of how far back from the house the play equipment sits, since the setback measures from "
         "the water's edge, not from the residence.</p>"),
    ],
    "scenario": (
        "Say you have a 200 sq ft play area in Weslyn Park",
        "<p>Say you have a 200 sq ft corner of a new Weslyn Park backyard set aside for a swing set on a "
        "6-foot fall height. At " + price("playground", True) + " a square foot, a shock-pad system sized to "
        "that equipment runs roughly $2,400 to $3,800, and since the lot is new construction on graded fill "
        "with no mature trees, there's no drip-line check needed the way there would be on an older Canoe "
        "Creek Road lot. The main variable left is whether the HOA's landscape review applies to this phase "
        "of the community.</p>"
    ),
    "faqs": [
        faq("Is play turf common in new St. Cloud neighborhoods like Weslyn Park?",
            "It's a natural fit for new construction, since fill lots often struggle to hold sod under heavy "
            "kid traffic in the first couple of years, and a shock-pad turf system solves the fall-height "
            "requirement without reseeding a worn patch every season."),
        faq("Does a play area near mature oaks need extra planning in St. Cloud?",
            "Yes, if the oaks are close enough that excavation would enter the drip line. A certified "
            "arborist's sign-off is required before digging there under the state's rule, so it's worth "
            "checking tree canopy before finalizing a layout in an older subdivision."),
    ],
    "sources": SRC,
}

LOCAL["pool"] = {
    "title": "Pool & Lanai Turf in St. Cloud, FL Backyards",
    "meta": "Pool and lanai turf in St. Cloud, FL prices like a residential lawn, $8-$18 a sq ft as of September 2026, for screened cages built since the early 2000s.",
    "h1": "Turf around St. Cloud pool cages and screened lanais",
    "lede": capsule(
        "Turf around a St. Cloud pool or inside a screened lanai prices the same as a residential lawn, "
        + price("residential") + " a square foot as of September 2026. St. Cloud's housing stock is "
        "young by Florida standards, with a median construction year in the 2000s, which means most pool "
        "cages in this town were built in an era when screen enclosures over a slab were already the norm."
    ),
    "sections": [
        ("Why sod fails first at the pool deck's edge",
         "<p>St. Cloud's housing is comparatively new, with a median year built in the 2000s, and a large "
         "share of that housing includes a screened pool cage poured on compacted fill right up to the deck "
         "edge. Sod struggles in that narrow strip worse than anywhere else on the lot: the fill drains "
         "differently than native soil, foot traffic concentrates right at the gate, and pool chemical "
         "splash browns a strip of grass that never gets a chance to recover between waterings. That "
         "combination is why the ring around a screened pool is one of the first places a St. Cloud "
         "homeowner asks about turf.</p>"),
        ("Lakefront lanais and the 10-foot setback",
         "<p>A smaller number of St. Cloud pool homes sit directly on East Lake Tohopekaliga or its "
         "connecting canal, with a screened lanai opening almost to the water. On a lot like that, turf "
         "around the pool cage still has to respect the state's 10-foot waterbody setback measured from the "
         "shoreline, not from the pool itself, unless a seawall or bulkhead already separates the yard from "
         "the lake. A lanai built close to an unprotected bank has less usable turf area than the deck's "
         "footprint alone would suggest.</p>"),
        ("Irrigation zones that used to wrap the pool cage",
         "<p>Older sprinkler layouts commonly ran a zone around the perimeter of a pool cage to keep sod "
         "alive right up to the screen, and that zone gets capped at the valve box the same as any other "
         "irrigation line once turf goes in, since the state's rule bars watering synthetic turf through an "
         "in-ground system entirely. Homeowners on Toho Water Authority's system, which absorbed St. Cloud's "
         "utility in October 2022, sometimes notice that capped zone show up as a small drop on the next "
         "bill rather than any change at all.</p>"),
    ],
    "scenario": (
        "Say you have a 350 sq ft pool deck ring",
        "<p>Say you have a 350 sq ft ring of turf between a screened pool cage and the property's rear fence "
        "on a 2006 St. Cloud pool home, with the original sod worn to dirt along the gate path. At "
        + price("residential", True) + " a square foot, that section runs roughly $3,850 to $5,600, glued "
        "and seamed to the concrete deck's edge with a drainage underlay so water clears the screen track "
        "instead of pooling against it. If the lot backs onto a canal, the layout also needs to confirm the "
        "10-foot setback before the crew finalizes where the turf can start.</p>"
    ),
    "faqs": [
        faq("Does turf around a St. Cloud pool cost more than a plain lawn?",
            "It prices in the same range as a residential lawn, though small, glue-down sections against a "
            "concrete deck often land toward the upper half of that range because of the extra edge work and "
            "drainage underlay a slab requires."),
        faq("Can I put turf right up to my lanai screen on a lake lot?",
            "Only if the screen and pool sit outside the state's 10-foot waterbody setback, or if a seawall "
            "already separates the yard from the water. A site visit confirms the distance before any layout "
            "gets finalized."),
        faq("What happens to my pool cage's old sprinkler zone?",
            "It gets capped at the valve box during installation, since in-ground irrigation can't be used on "
            "synthetic turf under state rule. The rest of the system serving other parts of the yard keeps "
            "running normally."),
    ],
    "sources": SRC,
}

LOCAL["str"] = {
    "title": "Vacation Rental Turf in St. Cloud, FL: A Smaller Market",
    "meta": "Vacation rental turf in St. Cloud, FL is a smaller market than the US-192 corridor. How the city's rental rules shape it, what it costs and what to check first.",
    "h1": "Turf for St. Cloud rental homes, where short-term rental zoning is tighter",
    "lede": capsule(
        "Turf for a St. Cloud rental property prices like a residential lawn, " + price("residential")
        + " a square foot as of September 2026, but the market for it is smaller here than along "
        "Kissimmee's US-192 corridor. Published guides to St. Cloud's rental rules describe nightly rentals as "
        "limited to hotel and motel districts, so most turf work for rental homes here serves longer-term "
        "tenancies rather than nightly vacation-home subdivisions. Confirm zoning with the city first."
    ),
    "sections": [
        ("Why St. Cloud isn't a nightly-rental subdivision town",
         "<p>Kissimmee's US-192 corridor and communities like Storey Lake or ChampionsGate were built around "
         "whole-home nightly rentals, with zoning to match. St. Cloud took a different path: "
         + ext("https://www.bnbcalc.com/blog/short-term-rental-regulation/St-Cloud-Florida-Guide", "a published guide to the city's rental rules says short-term rentals are limited to hotel and motel districts")
         + ", so a residential neighborhood inside city limits generally can't operate as a nightly rental; "
         "the city's Planning and Zoning office is the place to confirm a specific address. That's worth saying "
         "plainly rather than pretending otherwise: nightly-rental turf is a smaller market here than it is closer to the theme parks, and a homeowner asking about vacation-rental "
         "turf in St. Cloud is more often furnishing a longer-term or licensed property than a weekend "
         "rental.</p>"),
        ("Where legal short-term rentals do exist here",
         "<p>Any property renting for less than 30 days more than three times a year needs a state vacation "
         "rental license regardless of city or county, and a landlord renting inside city limits also needs "
         "the city's Landlord Business Tax Receipt. Where a licensed rental does operate, often a lakefront "
         "guest property near East Lake Tohopekaliga catering to anglers and boaters, durable turf still pays "
         "off the same way it would anywhere: no mowing schedule to coordinate around guest turnover, and no "
         "dead patch from a week the yard sat empty between bookings.</p>"),
        ("Unincorporated county rules run differently from the city's",
         "<p>Outside St. Cloud's city limits, in the unincorporated stretches along Old Hickory Tree Road or "
         "Nova Road, Osceola County's short-term rental rules are a separate set of regulations from the "
         "city's hotel-and-motel restriction. A rental property just outside the city line isn't automatically "
         "covered by the same limits that apply inside it, which is exactly the kind of detail worth checking "
         "with the county before assuming either set of rules applies.</p>"),
    ],
    "scenario": (
        "Say you have a licensed lakefront guest cottage",
        "<p>Say you have a licensed, permitted guest cottage on an East Lake Tohopekaliga lot, rented "
        "seasonally to anglers rather than as a weekend party house, with a 500 sq ft yard that shows wear "
        "between cleanings. At " + price("residential", True) + " a square foot, turf for that yard runs "
        "roughly $5,500 to $8,000, and because the lot backs onto the lake, the layout has to confirm the "
        "10-foot setback before finalizing how close turf can run to the shoreline.</p>"
    ),
    "faqs": [
        faq("Can I run a short-term rental in a St. Cloud neighborhood?",
            "Generally no, based on published guides to the city's rental rules, which describe nightly rentals as limited to hotel and motel districts; confirm your address with Planning and Zoning. Most "
            "residential zones inside St. Cloud don't allow nightly rentals regardless of what the property "
            "looks like."),
        faq("Searching for the best vacation-rental turf company near me in St. Cloud?",
            "Ask whether they've worked on a licensed rental before, since turnover cleaning and guest wear "
            "matter more there than on an owner-occupied lawn, and confirm they'll check any lakefront setback "
            "before quoting."),
        faq("Does Osceola County allow what St. Cloud doesn't?",
            "Unincorporated county rules are separate from the city's hotel-and-motel restriction, so a "
            "property just outside city limits should be checked against county rules specifically rather "
            "than assumed to follow the city's."),
    ],
    "sources": SRC,
}

LOCAL["commercial"] = {
    "title": "Commercial Turf in St. Cloud, FL: HOAs & Storefronts",
    "meta": "Commercial turf in St. Cloud, FL is quoted per job from drawings, covering Sunbridge HOA common areas, storefronts and growth-corridor properties.",
    "h1": "Commercial and HOA-common-area turf as St. Cloud's growth corridor fills in",
    "lede": capsule(
        "Commercial turf in St. Cloud, Florida is quoted per job from a site visit or drawings rather than "
        "one square-foot range, since an HOA clubhouse lawn, an apartment pet park and a storefront strip "
        "each carry different base and drainage needs. St. Cloud's population has nearly doubled since 2010, "
        "and that growth is what's filling in new commercial and common-area work east and south of "
        "downtown."
    ),
    "sections": [
        ("Growth along the corridor is bringing the commercial work",
         "<p>St. Cloud grew from roughly 38,000 residents in 2010 to more than 70,000 today, and that growth "
         "has pulled retail, medical offices and apartment complexes out along the corridors connecting "
         "downtown to Narcoossee Road and the Sunbridge development. New commercial construction in this "
         "stretch tends to sit on the same graded fill as the residential lots around it, which means the "
         "same drainage planning that matters for a Sunbridge backyard applies at a larger scale to a "
         "commercial pad or a shared community lawn.</p>"),
        ("HOA common areas in Sunbridge run through a landscape vendor",
         "<p>Del Webb Sunbridge, the community's 55-plus section, requires any landscape change to run "
         "through the HOA's contracted landscape vendor with a full architectural submittal, and that same "
         "review process applies to shared amenity areas, not just individual lots. An HOA board considering "
         "turf for a clubhouse pool deck or a community entrance should expect that approval step before a "
         "contractor can start, the same as any homeowner inside the community would.</p>"),
        ("City or county review depends on the parcel, not the tenant",
         "<p>A storefront or office park's turf project goes through whichever building department has "
         "jurisdiction over that parcel, the city's Building Department for an in-city address or Osceola "
         "County's Building Office for an unincorporated one, and a commercial site plan typically involves a "
         "longer review than the expedited path available for smaller residential permits. Confirming "
         "jurisdiction and expected review time early keeps a landscape contractor's schedule from slipping "
         "against a broader commercial build-out timeline.</p>"),
    ],
    "scenario": (
        "Say you have a 1,200 sq ft HOA entrance lawn",
        "<p>Say you have a 1,200 sq ft entrance median at a Canoe Creek Road-era HOA, currently St. "
        "Augustine that browns out every dry season despite a working irrigation system. That project gets "
        "quoted from a site visit rather than a flat per-square-foot number, since the median's curbing, "
        "irrigation removal and traffic exposure all factor into labor differently than a private backyard "
        "would. The HOA's board would also need to confirm its own landscape approval process before signing "
        "off, separate from whatever the city or county requires.</p>"
    ),
    "faqs": [
        faq("How is commercial turf priced in St. Cloud?",
            "By the job, from a site visit or drawings, since access, existing irrigation, curbing and "
            "traffic exposure all vary more between commercial sites than they do between residential "
            "backyards. There's no single per-square-foot number that fits every property type."),
        faq("Does an HOA need its own approval on top of city or county permits?",
            "Often yes, especially in a newer community like Sunbridge with an active architectural review "
            "process. That approval is separate from whatever building department has jurisdiction over the "
            "parcel, and both usually need to be cleared before work starts."),
        faq("Can turf go around a commercial retention pond in St. Cloud?",
            "Not inside the pond's littoral zone or the 10-foot waterbody setback, the same rule that applies "
            "to a residential yard. A commercial site plan needs to route landscaping around that buffer the "
            "same way a house on a canal lot does."),
    ],
    "sources": SRC,
}

LOCAL["sports"] = {
    "title": "Sports & Fitness Turf in St. Cloud, FL Yards",
    "meta": "Sports and fitness turf in St. Cloud, FL is quoted per job, fitting batting cages and agility lanes on Holopaw-area acreage and Sunbridge lots alike.",
    "h1": "Home sports turf on St. Cloud's bigger lots and newer subdivisions",
    "lede": capsule(
        "Sports and fitness turf in St. Cloud, Florida, a bocce court, a batting cage or a sled track, is "
        "quoted per job from a site visit rather than a flat square-foot range, since layout and length "
        "matter more than area alone. Lot size varies more here than in most towns on our list, from "
        "quarter-acre subdivision lots to multi-acre parcels toward Holopaw, and that range is what shapes "
        "what fits."
    ),
    "sections": [
        ("Acreage toward Holopaw fits a longer lane",
         "<p>Rural lots east of St. Cloud toward Holopaw, on well water and septic with no HOA to answer to, "
         "commonly run a half-acre to several acres, which is enough room for a batting cage or a full "
         "agility lane without crowding a house or a septic drain field. Those inland lots also sit well "
         "clear of the state's 10-foot waterbody setback, since there's no canal or pond nearby to measure "
         "against, which simplifies the layout compared with a lot backing onto East Lake Tohopekaliga.</p>"),
        ("Low-impact courts fit a 55-plus community's smaller footprint",
         "<p>Active-adult communities like Del Webb Sunbridge favor smaller, low-impact features, a bocce "
         "court more often than a batting cage, sized to fit a villa-scale backyard. Any addition there still "
         "has to clear the HOA's landscape vendor and architectural review before work starts, the same "
         "process that applies to a putting green or a simple lawn conversion in that community.</p>"),
        ("Waterfront lots need the setback built into the layout",
         "<p>A handful of St. Cloud properties back onto East Lake Tohopekaliga or its canal, and a sports "
         "surface there, an agility lane or a small practice court, has to keep its full footprint at least "
         "10 feet from the water's edge unless a seawall already separates the yard from it. That setback can "
         "shorten a planned lane's length more than a homeowner expects once it's measured from the actual "
         "shoreline rather than from the house.</p>"),
    ],
    "scenario": (
        "Say you have a 20 by 60 ft strip on 1.5 acres",
        "<p>Say you have a 20 by 60 ft strip along the side yard of a 1.5-acre lot off Hickory Tree Road, "
        "flat and clear, wanting a synthetic sled and agility lane rather than mowed grass that stays soggy "
        "after a summer storm. That project gets quoted from a site visit rather than a set range, since the "
        "lane's length and the base depth needed for repeated sled traffic both factor into labor more than "
        "square footage alone. Being well clear of any pond or canal simplifies the layout here, since the "
        "10-foot setback doesn't come into play at all.</p>"
    ),
    "faqs": [
        faq("What sports surfaces fit on a St. Cloud acreage lot?",
            "A batting cage, a full agility lane or a small practice court all fit more comfortably on a "
            "half-acre-plus lot toward Holopaw than on a standard quarter-acre subdivision lot, simply "
            "because there's more open ground to work with."),
        faq("Does a sports surface at Del Webb Sunbridge need HOA approval?",
            "Yes, the same architectural review and landscape vendor process applies to a bocce court or any "
            "other addition as it does to a lawn conversion or a putting green in that community."),
        faq("How is sports turf priced in St. Cloud?",
            "By the job, from a site visit, since layout, length and base depth vary more across sports "
            "surfaces than they do across residential lawns of similar size."),
    ],
    "sources": SRC,
}

LOCAL["pavers"] = {
    "title": "Turf & Pavers in St. Cloud, FL Driveways and Paths",
    "meta": "Turf between pavers in St. Cloud, FL is quoted per job, from new Sunbridge driveways to stepping-stone paths on 1980s Canoe Creek Road lots.",
    "h1": "Turf ribbons and paver paths across St. Cloud's older and newer lots",
    "lede": capsule(
        "Turf set between pavers in St. Cloud, Florida is quoted per job rather than a flat square-foot "
        "range, since a driveway ribbon, a stepping-stone path and a patio border all use different "
        "quantities of paver and turf for the same footprint. New-construction driveways in Sunbridge and "
        "older paths in the Canoe Creek Road subdivisions call for different layouts even when the idea "
        "behind them is the same."
    ),
    "sections": [
        ("New-construction driveways with a turf ribbon",
         "<p>New homes in Sunbridge and Weslyn Park often go in with a paver driveway on freshly graded "
         "fill, and a turf ribbon down the center or along the edge softens the visual mass of a wide "
         "driveway on a lot where the rest of the landscaping hasn't filled in yet. Building that ribbon on "
         "fill soil means checking that the base under the turf strip drains as well as the compacted "
         "aggregate under the pavers does, since the two materials need opposite compaction for their own "
         "purposes even while sharing one finished grade.</p>"),
        ("Stepping-stone paths on older Canoe Creek Road lots",
         "<p>Established subdivisions off Canoe Creek Road, built mostly through the 1980s to 2000s, tend to "
         "have side-yard paths that were never formally hardscaped, worn dirt tracks between a gate and a "
         "shed or a garden. A stepping-stone path with turf between the pavers replaces that worn track "
         "without paving the whole strip, and on an older lot with established roots nearby, the shallower "
         "footprint of stepping stones disturbs less ground than a continuous paver walkway would.</p>"),
        ("Long driveways on Holopaw-area acreage",
         "<p>Rural lots east toward Holopaw often have driveways several hundred feet long connecting a house "
         "to the road, and a full paver treatment over that distance gets expensive fast. A paver apron near "
         "the garage with a turf-and-gravel or turf-ribbon treatment for the rest of the run is a common "
         "compromise on these lots, and on a septic system, the base and turf strip get routed clear of the "
         "drain field the same way any other turf project on that kind of lot would.</p>"),
    ],
    "scenario": (
        "Say you have a 45 ft driveway ribbon",
        "<p>Say you have a 45 ft by 3 ft turf ribbon down the center of a new paver driveway on a Weslyn "
        "Park lot, installed at the same time as the pavers themselves. That project gets quoted from the "
        "driveway's drawings rather than a flat per-square-foot rate, since the paver base and the turf base "
        "have to meet at one consistent grade even though they're built from different material, and "
        "coordinating that with the paver crew's schedule is part of the job as much as the turf itself "
        "is.</p>"
    ),
    "faqs": [
        faq("Can turf and pavers be installed in the same visit in St. Cloud?",
            "Yes, and coordinating both trades together usually produces a cleaner shared grade than adding "
            "turf to an already-finished paver driveway later, since the two bases can be built to meet at "
            "one level from the start."),
        faq("Does a long rural driveway need a different approach than a subdivision one?",
            "Often yes. A several-hundred-foot driveway toward Holopaw is usually treated with a paver apron "
            "near the house and a simpler turf-and-gravel run for the rest, rather than pavers the full "
            "length, purely for cost."),
    ],
    "sources": SRC,
}

LOCAL["repair"] = {
    "title": "Turf Repair in St. Cloud, FL: Lakefront & Older Yards",
    "meta": "Turf repair in St. Cloud, FL is quoted per visit, covering lakefront edges near East Lake Tohopekaliga and turf installed in older Canoe Creek subdivisions.",
    "h1": "Fixing turf on St. Cloud's older lakefront and subdivision lots",
    "lede": capsule(
        "Turf repair in St. Cloud, Florida is quoted per visit rather than a flat square-foot rate, since a "
        "lifted seam, a settled corner and a washed-out edge each take different work to fix. Two settings "
        "account for most of the repair calls we'd expect in this town: older lots backing onto East Lake "
        "Tohopekaliga, and turf installed years ago in the established subdivisions off Canoe Creek Road."
    ),
    "sections": [
        ("Lakefront edges take more weather than an inland yard",
         "<p>Turf along East Lake Tohopekaliga or its connecting canal takes more wind and water exposure at "
         "its perimeter than a lawn set back from any water feature, since storm surge on an open lake edge "
         "can work at a seam or a nailed border more aggressively over the years. A lifted edge on a "
         "lakefront lot is worth checking against the state's 10-foot setback too, since older installs that "
         "predate the current rule sometimes sit closer to the water than a new project would be allowed to "
         "start today.</p>"),
        ("Turf installed years ago in the Canoe Creek Road subdivisions",
         "<p>Subdivisions built off Canoe Creek Road and Old Hickory Tree Road through the 1980s and 2000s "
         "now carry some of the oldest turf installs in this part of the county, old enough in a few cases to "
         "be approaching the upper end of a typical service life. A repair call on one of these older "
         "installs often traces back to a base that was never built to today's washed-rock standard, since "
         "that requirement postdates a lot of the turf already in the ground here.</p>"),
        ("Septic access on rural repairs east of town",
         "<p>On well-and-septic lots toward Holopaw, a repair visit sometimes coincides with a septic "
         "pump-out, and turf that was laid without leaving the tank's access lid reachable has to be lifted "
         "and reset properly rather than just patched back down over the same spot. Building that access into "
         "the repair the correct way avoids repeating the same lift-and-patch cycle at the next pump-out.</p>"),
    ],
    "scenario": (
        "Say you have a 10-year-old dog run off Hickory Tree Road",
        "<p>Say you have a dog run installed about ten years ago on a lot off Hickory Tree Road, with one "
        "corner lifting after last season's storms and a soft, spongy feel along that same edge underfoot. A "
        "repair visit checks whether the base underneath washed out from years of runoff before simply "
        "renailing the corner, since reseating the edge without addressing an eroded base fixes the problem "
        "for a matter of weeks rather than years. That diagnosis, more than the repair itself, is what the "
        "visit is quoted around.</p>"
    ),
    "faqs": [
        faq("Why does turf near East Lake Tohopekaliga need more repair than inland lawns?",
            "Wind and water exposure at an open shoreline edge works at seams and borders harder over time "
            "than a lawn set back from any water feature, which is why perimeter checks matter more on a "
            "lakefront lot."),
        faq("Is older turf in the Canoe Creek Road subdivisions worth repairing or replacing?",
            "It depends on the base underneath. A repair fixes a surface issue like a lifted seam; if the "
            "base itself was never built to the current washed-rock standard, replacement is usually the more "
            "lasting fix."),
    ],
    "sources": SRC,
}

LOCAL["cleaning"] = {
    "title": "Turf Cleaning & Maintenance in St. Cloud, FL",
    "meta": "Turf cleaning in St. Cloud, FL is quoted by yard size and visit, timed around live oak leaf drop downtown and higher water tables near East Lake Toho.",
    "h1": "Keeping St. Cloud turf clean, from downtown oaks to lakefront flatwoods",
    "lede": capsule(
        "Turf cleaning in St. Cloud, Florida is quoted by yard size and how long it's been since the last "
        "visit, not a flat square-foot rate. Two local factors set the schedule more than anything else: leaf "
        "drop from the mature oaks around the historic downtown, and how close a lawn sits to East Lake "
        "Tohopekaliga's higher water table."
    ),
    "sections": [
        ("Live oak leaf drop around the historic downtown",
         "<p>The stand of old-growth live oaks at " + ext("https://floridahikes.com/st-cloud/", "Lakefront Park")
         + " and the mature canopy along St. Cloud's numbered and state-named downtown streets shed heavily "
         "in late winter, and a lawn under that canopy can collect enough leaf litter in a couple of weeks to "
         "start affecting drainage if it's left alone. Clearing debris before it works down into the infill "
         "matters more on these older, tree-covered lots than on a newer, open lot with little canopy yet.</p>"),
        ("Lots closer to the lake hold more moisture between visits",
         "<p>St. Cloud's flatwoods soil, mostly Myakka and Immokalee series, holds water closer to the "
         "surface on lots nearer East Lake Tohopekaliga than it does on higher ground toward Sunbridge, and a "
         "lawn on that lower ground can need a tighter cleaning schedule during the wettest months for that "
         "reason alone, independent of how well the turf itself was built.</p>"),
        ("Rural well water changes the rinsing math",
         "<p>Homeowners on well water east toward Holopaw don't see a rinse show up on a metered Toho Water "
         "Authority bill the way an in-city address does, since well water isn't billed by the gallon the "
         "same way. That doesn't change how often a lawn actually needs rinsing, but it does mean the "
         "decision to rinse more often during a hot stretch isn't weighed against a utility bill the way it "
         "would be on a Toho account.</p>"),
    ],
    "scenario": (
        "Say you have a 600 sq ft lawn near Lakefront Park",
        "<p>Say you have a 600 sq ft pet-turf lawn two blocks from Lakefront Park, shaded by a mature live "
        "oak that drops heavily every February. A cleaning visit there is quoted around that seasonal debris "
        "load and the yard's history since the last visit, not a flat per-square-foot number, since a lawn "
        "that's gone six months without clearing needs meaningfully more work than one cleaned every few "
        "weeks through the drop season.</p>"
    ),
    "faqs": [
        faq("How often should turf near downtown St. Cloud's oaks be cleaned?",
            "More often through the late-winter leaf drop than the rest of the year, since debris from mature "
            "live oaks can build up in the infill within a couple of weeks if it's left alone during that "
            "stretch."),
        faq("Does turf near East Lake Tohopekaliga need cleaning more often than inland lawns?",
            "It can, since lots closer to the lake sit on soil that holds water nearer the surface. That "
            "higher moisture level can call for a tighter schedule during the wettest months than a "
            "similar-sized lawn on higher, drier ground."),
    ],
    "sources": SRC,
}

LOCAL["replacement"] = {
    "title": "Turf Removal & Replacement in St. Cloud, FL",
    "meta": "Turf replacement in St. Cloud, FL is quoted per job, for lawns installed in the 2000s-2010s boom and older lakefront lots nearing the end of their run.",
    "h1": "Replacing worn turf across St. Cloud's older subdivisions and lakefront lots",
    "lede": capsule(
        "Turf replacement in St. Cloud, Florida is quoted per job after a base inspection, not a flat "
        "square-foot rate. St. Cloud's housing stock has a median construction year in the 2000s, which "
        "means a meaningful share of the turf installed here over the past 10 to 15 years is now reaching "
        "the point where replacement, not just repair, becomes the honest recommendation."
    ),
    "sections": [
        ("Housing from the 2000s boom is reaching turf's replacement window",
         "<p>With St. Cloud's median home built in the 2000s and turf generally lasting 10 to 20 years "
         "depending on stabilization and traffic, lawns converted to turf in the early-to-mid 2010s, often "
         "the first wave of St. Cloud homeowners to try it, are now old enough that a base inspection makes "
         "more sense than another round of spot repairs. Replacement at that point usually means rebuilding "
         "the base to the current washed-rock standard rather than reusing whatever sat underneath the "
         "original install.</p>"),
        ("Re-checking the lake setback on an older lakefront replacement",
         "<p>An older turf install on a lot backing onto East Lake Tohopekaliga or its canal sometimes "
         "predates the state's current 10-foot waterbody setback, adopted as part of Rule 62-308.100 in May "
         "2026, and a full replacement is the natural point to confirm the new layout meets that distance "
         "rather than simply relaying turf in the same footprint as before.</p>"),
        ("Correcting septic access during a rural replacement",
         "<p>On well-and-septic lots east toward Holopaw, an older install sometimes covered the septic "
         "tank's access point entirely, since that requirement wasn't part of the build standard when the "
         "original turf went in. Replacement is the practical time to correct that, resetting the layout so "
         "the lid stays reachable for future pump-outs instead of needing to be dug up again later.</p>"),
    ],
    "scenario": (
        "Say you have a 2012-installed dog run off Canoe Creek Road",
        "<p>Say you have a dog run installed in 2012 off Canoe Creek Road, now matted flat along the fence "
        "line with a base that's started holding water after storms in a way it never used to. At roughly 14 "
        "years old, that run sits near the upper end of a typical service life, and a replacement quote would "
        "include probing the base in more than one spot before deciding whether the rock underneath can stay "
        "or needs to come out with the old turf.</p>"
    ),
    "faqs": [
        faq("How do I know if St. Cloud turf needs replacing instead of repairing?",
            "A base inspection at more than one spot on the lawn is the reliable way to tell. Turf that's "
            "matted but sitting on a base that still drains fine can often be repaired; a base that's crusted "
            "or holding water usually means replacement."),
        faq("Searching for the best turf replacement company near me in St. Cloud?",
            "Start with whether they probe the old base before quoting a tear-out, rather than pricing from "
            "a look at the surface alone. That single step is what separates an honest replacement quote from "
            "a guess."),
        faq("Does replacing lakefront turf change how close it can sit to the water?",
            "It can. If the original install predates the state's current 10-foot setback, a replacement "
            "project resets the layout to meet that distance unless a seawall already separates the yard from "
            "the water."),
    ],
    "sources": SRC,
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
