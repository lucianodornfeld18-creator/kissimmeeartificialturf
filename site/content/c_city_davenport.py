# -*- coding: utf-8 -*-
"""Davenport, FL city hub + city x service pages. Polk County (tier 1).
Research checked September 2026; sources below are primary where the city or county
publishes one, secondary (real-estate/HOA listing sites, news) where noted."""
from _helpers import page, capsule, sec, table, faq, a, svc, city, county, cs, post, src, ext, price
from _cityservice import cityservice_pages

SLUG = "davenport"

CITY_BP = ("City of Davenport, FL — Building & Planning Department", "https://www.mydavenport.org/buildingplanning")
CITY_PORTAL = ("City of Davenport, FL — permit portal (iWorQ Citizen Access)", "https://portal.iworq.net/DAVENPORT/permits/600")
CITY_UTIL = ("City of Davenport, FL — Utility Billing and watering schedule", "https://www.mydavenport.org/utilitybilling")
CITY_PARK = ("City of Davenport, FL — Jamestown Park", "https://www.mydavenport.org/jamestownpark")
HIST_DIST = ("Florida Backroads Travel — Davenport Historic District", "https://www.florida-backroads-travel.com/davenport-historic-district.html")
WIKI_DAV = ("Wikipedia — Davenport, Florida", "https://en.wikipedia.org/wiki/Davenport,_Florida")
POLK_PA = ("Polk County Property Appraiser — parcel search", "https://www.polkflpa.gov/")
POLK_BLD = ("Polk County Building Division — permitting", "https://www.polkfl.gov/services/building/permitting/")
POLK_WATER = ("Polk County — current watering restrictions", "https://www.polkfl.gov/services/utilities/water-restrictions/")
SWFWMD = ("Southwest Florida Water Management District — Florida's water management districts", "https://www.swfwmd.state.fl.us/about/floridas-water-management-districts")
POLK_TAX = ("Polk County Tax Collector — real estate property rentals (Class B tax receipt)", "https://www.polktaxes.com/services/ta-05-01-real-estate-property-rentals/")
CENSUS = ("U.S. Census Bureau QuickFacts — Davenport city, Florida", "https://www.census.gov/quickfacts/davenportcityflorida")
CANDLER = ("USDA NRCS — Candler series, official soil series description", "https://soilseries.sc.egov.usda.gov/OSD_Docs/C/Candler.html")
LAKE_DAV = ("Polk County Water Atlas — Lake Davenport", "https://polk.wateratlas.usf.edu/waterbodies/lakes/160005/lake-davenport-davenport")
RIDGE = ("Wikipedia — Lake Wales Ridge", "https://en.wikipedia.org/wiki/Lake_Wales_Ridge")
SOLTERRA_CDD = ("Solterra Resort Community Development District", "https://www.solterraresortcdd.org/")
SOLTERRA_PROFILE = ("Viva Orlando — Solterra Resort community profile", "https://vivaorlando.com/solterra-resort/")
PROVIDENCE = ("Providence Florida — golf community overview", "https://www.providenceflorida.com/")

SRC = [CITY_BP, CITY_PORTAL, CITY_UTIL, CITY_PARK, HIST_DIST, WIKI_DAV, POLK_PA, POLK_BLD, POLK_WATER, SWFWMD,
       POLK_TAX, CENSUS, CANDLER, LAKE_DAV, RIDGE, SOLTERRA_CDD, SOLTERRA_PROFILE, PROVIDENCE,
       "dep-rule", "fs125572", "fs7203045"]

# ============================================================== HUB
HUB = page(
    "/areas/davenport/", "city",
    "Artificial Turf Installation in Davenport, FL (Polk County)",
    "Turf installation in Davenport, FL: city hall vs. Polk County permits, ridge sand drainage, lakes and HOA rules, checked September 2026.",
    "Turf in Davenport: city limits, county subdivisions and ridge sand",
    capsule(
        "Davenport sits about " + str(15) + " miles from Kissimmee, split between a small city government and a much "
        "larger unincorporated stretch of Polk County along US-27 and I-4. That split decides who reviews a turf "
        "permit, and the ridge sand under much of the county drains faster than flatter Osceola lots. As of "
        "September 2026, Florida's turf rule and Polk's own code both still apply here."
    ),
    "".join([
        sec("A city hall and a much bigger county around it",
            "<p>Davenport's own city limits cover only a few square miles around a downtown that predates the "
            "interstate. Most addresses carrying a Davenport, FL 33837 ZIP code sit outside those limits, in "
            "unincorporated Polk County subdivisions strung along US-27 and I-4 toward the Four Corners area, "
            "where Polk meets Osceola, Lake and Orange counties (" + ext(LAKE_DAV[1], "Polk County Water Atlas") + "). "
            "Whether a lot answers to " + a(CITY_BP[1], "Davenport's own city hall") + " or to the county's much "
            "larger Building Division changes which office reviews the job, though not the state material and "
            "drainage standard both have to follow.</p>"
            "<p>We measure yards on both sides of that line, from older in-town lots near the historic district to "
            "the gated communities that make up most of the growth. A five-minute parcel search settles which "
            "office has a given address before anyone calls the wrong department.</p>"),
        sec("Which office reviews the permit: city hall or the county",
            "<p>Inside Davenport's city limits, the " + a(CITY_BP[1], "Building & Planning Department") + " takes "
            "permit questions at 863-419-3300 and runs applications through an " + a(CITY_PORTAL[1], "iWorQ citizen "
            "portal") + ". We don't have a page built specifically around Davenport's own municipal code the way we "
            "do for Polk's countywide rules, so a call to that department is the right first step for anything "
            "inside city limits, including whether capping an irrigation head needs its own plumbing sign-off.</p>"
            "<p>Step outside the city line and Polk County's Building Division takes over instead, and our " +
            a("/laws/permits/polk-county/", "Polk County permits page") + " covers what that office has and hasn't "
            "published about synthetic turf. Because a Davenport-addressed lot is more often unincorporated than "
            "not, checking the " + a(POLK_PA[1], "Polk County Property Appraiser's parcel search") + " before a "
            "quote saves a call to the wrong desk. The record shows the taxing jurisdiction, which tells you "
            "whether city hall or the county Building Division has your permit.</p>"),
        sec("Two water utilities, one state rule on irrigation",
            "<p>Inside the city, Davenport runs its own utility rather than buying into a regional system, and "
            "lawn irrigation is limited to one day a week year-round by the last digit of the address, watering "
            "only before 6 a.m. or after 6 p.m. (" + ext(CITY_UTIL[1], "Davenport Utility Billing") + "). Step into "
            "unincorporated Polk County and Polk County Utilities has been running an even tighter emergency "
            "schedule since a Southwest Florida Water Management District shortage order, one day a week in "
            "overnight hours only, with the day set by the address's last digit (" + ext(POLK_WATER[1],
            "Polk's current restrictions page") + "). Davenport falls in the part of Polk County that SWFWMD "
            "covers, unlike the St. Johns district that reaches Lake and Seminole counties farther north (" +
            ext(SWFWMD[1], "SWFWMD's district map") + ").</p>"
            "<p>None of those schedules reach a synthetic lawn once its heads are capped, since the state's 2026 "
            "rule already bars watering turf from an in-ground system regardless of what day the calendar allows. "
            "Whichever utility bills a Davenport address, that's one fewer household chore once the conversion is "
            "done.</p>"),
        sec("From a citrus depot to a resort-home boom",
            "<p>Davenport incorporated in 1915, after the South Florida Railroad rebuilt the settlement a mile "
            "south of its original site following an 1900 fire (" + ext(WIKI_DAV[1], "Davenport's history") + "). "
            "Downtown still shows that era: 32 acres and 28 buildings, most from the 1920s, make up the Davenport "
            "Historic District on the National Register of Historic Places, a citrus-and-naval-stores-era core "
            "that's easy to overlook next to the newer growth around it (" + ext(HIST_DIST[1],
            "the historic district's listing") + ").</p>"
            "<p>That newer growth is enormous by comparison. The incorporated city counted 2,888 residents in the "
            "2010 Census and 9,043 in 2020, a jump of roughly 234 percent in one decade (" + ext(CENSUS[1],
            "Census Bureau QuickFacts") + "), and almost none of that landed downtown. Most of it filled gated, "
            "amenity-heavy subdivisions such as " + ext(SOLTERRA_PROFILE[1], "Solterra Resort") + ", where every "
            "home comes with its own pool, and " + ext(PROVIDENCE[1], "Providence") + ", a roughly 2,200-acre golf "
            "community built around an 18-hole course. " + city("championsgate", "ChampionsGate") + " sits close "
            "enough to share that same growth wave, though it gets its own page rather than this one.</p>"),
        sec("Ridge sand, slopes and the lakes it drains toward",
            "<p>Davenport sits near the northern end of the Lake Wales Ridge, an ancient dune system that runs "
            "the length of peninsular Florida and pushes elevations well above the flatwoods on either side (" +
            ext(RIDGE[1], "the Lake Wales Ridge's geology") + "). The Candler series dominates the mapped soil "
            "here: excessively drained, very rapid to rapid permeability, on slopes that usually run 0 to 12 "
            "percent but can reach 40 percent on the more dissected ridge shoulders (" + ext(CANDLER[1],
            "USDA's official Candler series description") + "). That's faster-draining, and on some lots "
            "steeper, ground than the flat Myakka and Basinger sand most of our Osceola jobs sit on.</p>"
            "<p>Water still collects somewhere. Lake Davenport anchors the Four Corners side of town (" +
            ext(LAKE_DAV[1], "the county's water atlas entry") + "), and the resort subdivisions built since the "
            "2010s ring their common areas with stormwater retention ponds. Florida's turf rule keeps synthetic "
            "grass at least 10 feet from any of that water, natural or built, unless a seawall already separates "
            "the two, and out of a pond's littoral zone entirely.</p>"),
    ]) + table(
        "Davenport yard types and what we do differently",
        ["Yard type", "What's different here", "What that changes about the install"],
        [
            ["Historic downtown lot", "Older grid streets, city permitting, mature shade trees near some homes",
             "Confirm with " + a(CITY_BP[1], "Building & Planning") + " first; check drip lines before excavating a base"],
            ["Resort subdivision (Solterra/Providence-type)", "Newer builder sod on ridge sand, CDD common areas, HOA design review",
             "Grade for the faster-draining Candler sand; bring the HOA packet before base work starts"],
            ["Golf-frontage lot", "Visible from a shared fairway, not just the street", "Treat the fairway view like street frontage for the HOA's visibility test"],
            ["Vacation-rental home", "Guest turnover, Polk's rental licensing, heavier week-to-week wear", "Size the base and edge anchoring for traffic, not just square footage"],
            ["Lakefront or pond-adjacent lot", "Retention ponds and natural lakes on nearly every newer plat", "Hold the 10-ft waterbody setback and skip any swale or littoral zone entirely"],
        ],
        "Every row still follows the same state material and drainage standard; the column that changes is the paperwork and the base."
    ) + sec(
        "What \"the best artificial turf installer near me\" should mean in Davenport",
        "<p>Homeowners searching for the best artificial turf installer near me in Davenport are usually trying to "
        "sort out one of two things: whether a quote accounts for the city-versus-county permit question, and "
        "whether it prices the base for ridge sand rather than a generic Florida yard. An installer who asks "
        "which side of the city line a lot sits on, and who prices a resort-subdivision retention pond into the "
        "layout before mentioning square footage, is doing the homework this page is describing rather than "
        "skipping it.</p>"
    ) + sec(
        "Permits, HOAs and the paperwork that actually applies",
        "<p>Three separate approvals can touch a Davenport project, and getting one doesn't settle the others. "
        "The city or county permit covers drainage, easements and the state's own material rule; our " +
        a("/laws/permits/polk-county/", "Polk County permits page") + " has the department names and phone "
        "numbers for the unincorporated side. " + a("/laws/florida-hb-683/", "HB 683 and Rule 62-308.100") +
        " set the statewide floor everyone answers to on a single-family lot of an acre or less. And an HOA or "
        "CDD, common in Davenport's newer subdivisions, runs on " + a("/laws/hoa-rules/", "a separate statute "
        "entirely") + " that only protects turf not visible from the street, an adjacent lot or, on a "
        "golf-frontage property, the fairway itself. Our " + a("/tools/hoa-packet-checklist/",
        "HOA and ARC packet checklist") + " lists what to bring to that meeting before a design gets drawn.</p>"
    ) + "<!--AUTO:city-services-->",
    faqs=[
        faq("Does the City of Davenport or Polk County issue my turf permit?",
            "It depends on the parcel, not the mailing address. A Davenport, FL ZIP code covers both the "
            "incorporated city and a much larger unincorporated area, so run the address through the " +
            a(POLK_PA[1], "Property Appraiser's parcel search") + " to see the taxing jurisdiction before "
            "assuming either office handles it."),
        faq("Do Solterra Resort or Providence restrict artificial turf?",
            "We haven't found a published design-guideline document from either community's association that "
            "names synthetic turf specifically, so treat any backyard project in a gated Davenport subdivision "
            "as an ARC submission first. " + a("/laws/hoa-rules/", "F.S. 720.3045") + " still protects turf a "
            "neighbor or the street can't see, golf-frontage lots included."),
        faq("Which water utility serves my Davenport address, and does it matter for turf?",
            "City utilities bill inside Davenport's limits; Polk County Utilities bills most of the surrounding "
            "subdivisions, and both currently limit lawn irrigation to one day a week. Neither schedule reaches a "
            "synthetic lawn once the heads underneath are capped, which the state's 2026 rule requires either way."),
        faq("Is there a permit rule for turf on a sloped ridge lot?",
            "Nothing published treats slope as its own turf category in either the city's or Polk's code. A "
            "steeper Candler-sand lot changes how a crew grades and anchors the base, which is a construction "
            "question, not a separate permit."),
        faq("Does renting a Davenport home short-term change the turf rules?",
            "The state's material and setback standard doesn't distinguish an owner-occupied home from a rental. "
            "Polk County's own rental licensing, covered on our vacation-rental turf page, is a separate "
            "requirement that doesn't touch the turf itself."),
        faq("How far is Davenport from your Kissimmee base?",
            "About 15 miles, mostly along US-27 and I-4, which is within the roughly 40-mile area we work "
            "across Osceola, Orange, Polk, Lake and Seminole counties."),
    ],
    sources=SRC, city=SLUG, crumbs=[("Service areas", "/areas/")], crumb="Davenport",
    related=[
        ("/areas/polk-county/", "Turf installers in Polk County"),
        ("/laws/permits/polk-county/", "Polk County artificial turf permits"),
        ("/areas/haines-city/", "Artificial turf in Haines City"),
        ("/areas/poinciana/", "Artificial turf in Poinciana"),
        ("/artificial-turf-cost/", "Turf cost tables for Central Florida"),
        ("/tools/hoa-packet-checklist/", "HOA / ARC application checklist for artificial turf"),
    ],
)

# ============================================================== LOCAL (12 services)
LOCAL = {}

LOCAL["residential"] = {
    "title": "Artificial Grass Installation in Davenport, FL Yards",
    "meta": "Artificial grass installation in Davenport, FL: ridge sand base work, city vs. Polk County permits, and the $8–$18/sq ft market range, September 2026.",
    "h1": "Artificial grass for Davenport's ridge-sand lots",
    "lede": capsule(
        "Residential artificial grass in Davenport runs " + price("residential") + " a square foot installed, "
        "typically " + price("residential", True) + ", the same Central Florida range that applies everywhere "
        "we work as of September 2026. What changes locally is the base: the Candler sand under much of the "
        "county drains faster, and sometimes drops off at a steeper grade, than the flat lots most guides assume."
    ),
    "sections": [
        ("Building a base on faster-draining ridge sand",
         "<p>The Candler series that dominates Davenport's mapped soil is excessively drained with very rapid to "
         "rapid permeability, which sounds like an advantage until a base crew realizes the native ground already "
         "moves water faster than the compacted rock going on top of it. We still build the same two to four "
         "inches of washed, open-graded crushed rock the state rule calls for, compacted in lifts, because the "
         "base's job is holding the turf flat and anchored, not adding drainage the sand doesn't need. On a "
         "steeper shoulder lot, closer to the upper end of Candler's zero-to-40-percent slope range, we spend "
         "more time on compaction passes than on drainage math.</p>"),
        ("Older grid lots versus newer subdivision pads",
         "<p>A yard near Davenport's historic downtown core sits on decades-settled ground, often with mature "
         "shade and a narrower side yard than a newer plat allows. A lot in one of the resort-style subdivisions "
         "built since the 2010s growth wave usually sits on a builder-graded pad with thinner topsoil over the "
         "same ridge sand, which drains fast but can also settle unevenly if the builder's fill wasn't compacted "
         "before the sod went down. Both situations call for the same washed-rock base; the difference is how "
         "much regrading a crew does before that base ever goes in.</p>"),
        ("Checking which office signs off before the crew arrives",
         "<p>A Davenport-addressed residential lot is more often in unincorporated Polk County than inside the "
         "city, and " + city("davenport", "our Davenport hub") + " walks through how to check a specific parcel. "
         "Inside city limits, " + a(CITY_BP[1], "Building & Planning") + " handles the review; outside them, " +
         a("/laws/permits/polk-county/", "Polk County's Building Division") + " does. Neither office has "
         "published a synthetic-turf-specific rule as of September 2026, which means ordinary permitting for "
         "exterior work and irrigation-head capping still applies either way.</p>"),
    ],
    "scenario": (
        "Say you have a shaded lot near downtown",
        "<p>Say you have a 1,400 sq ft front and side yard on an older Davenport lot near downtown, sod that's "
        "struggled in the shade of a mature oak for years. At the typical " + price("residential", True) +
        " range, that works out to roughly $14,000 to $22,400 installed, with the lower end more likely if "
        "access is easy and the base needs only light regrading. A crew still checks the oak's drip line before "
        "digging, since Florida's rule keeps turf out from under a canopy without a certified arborist's letter, "
        "and on a lot this close to downtown that's often the deciding factor in how the layout gets drawn.</p>"
    ),
    "faqs": [
        faq("Does Davenport's older housing stock change how turf gets installed?",
            "Mostly in prep work. Homes near the historic district tend to have established trees and older "
            "irrigation lines, so a crew spends more time locating and capping heads and checking drip lines "
            "than it would on a bare new-construction pad."),
        faq("Is the price different for a lot inside city limits versus the county?",
            "No. " + price("residential") + " a square foot applies the same on either side of the city line; "
            "access, base condition and drainage decide where a specific job lands in that range, not the "
            "jurisdiction. Our " + svc("residential") + " page covers the state material standard behind that "
            "range in full."),
    ],
    "sources": SRC,
}

LOCAL["pet"] = {
    "title": "Pet Turf & Dog Runs in Davenport, FL Subdivisions",
    "meta": "Pet turf and dog run installation in Davenport, FL: fast-draining ridge sand, retention-pond setbacks, and the $10–$18/sq ft market range, September 2026.",
    "h1": "Dog turf for Davenport's newer, pond-lined subdivisions",
    "lede": capsule(
        "Pet turf in Davenport runs " + price("pet") + " a square foot installed, typically " + price("pet", True) +
        ", as of September 2026. Most of our pet-turf calls here come from the gated subdivisions built over the "
        "last decade, where a narrow side yard often backs straight onto a stormwater pond."
    ),
    "sections": [
        ("A dog run next to a retention pond",
         "<p>Nearly every subdivision built around Davenport and neighboring " + city("four-corners", "Four Corners")
         + " since the 2010s growth wave rings its common areas, and often individual lots, with a stormwater "
         "retention pond rather than a canal or natural lake. Florida's turf rule keeps synthetic grass at least "
         "10 feet from that water unless a seawall separates the two, and bars it from the pond's littoral zone "
         "outright, which on a narrow zero-lot-line yard can eat more of the usable run than a homeowner expects. "
         "We lay out the dog run's fenced footprint against that setback before pricing the job, not after.</p>"),
        ("Skipping the weed barrier where dogs actually go",
         "<p>A fabric layer between the compacted base and the turf backing is a fine option on a plain lawn, but "
         "we leave it out under a dedicated pet run, because urine sits on top of fabric instead of filtering "
         "down into the rock the way the base is built to handle it. That matters more in Davenport's newer "
         "subdivisions than it might elsewhere, since a builder-graded pad often has less native topsoil to "
         "buffer a run that sees the same two dogs every day for years.</p>"),
        ("Fast sand, faster odor control",
         "<p>The Candler sand under most of Davenport's newer ground already drains at a rapid clip on its own, "
         "which helps a pet run flush faster after a hose rinse than the same setup would on flatter, "
         "slower-draining soil. Zeolite or coated silica infill still does the odor-control work the sand alone "
         "can't, and either one meets the state's natural-material rule for what can go under a residential dog "
         "area.</p>"),
    ],
    "scenario": (
        "Say you have a fenced run next to a pond",
        "<p>Say you have a 450 sq ft side yard behind a Solterra-style rental-adjacent home, fenced for two dogs "
        "and backing onto a community pond about eight feet from the property line. At the typical " +
        price("pet", True) + " range, 450 sq ft runs about $5,400 to $7,200 installed, though the pond setback "
        "may trim the usable footprint before that math even starts. A crew measures the 10-foot line from the "
        "water first and prices the smaller, compliant shape rather than the full fenced area.</p>"
    ),
    "faqs": [
        faq("Can I install a dog run right up to my subdivision's retention pond?",
            "Not inside 10 feet of the water under the state's 2026 turf standard, unless a seawall or bulkhead "
            "already separates the yard from the pond, which most stormwater ponds don't have."),
        faq("Does pet turf need a different base on ridge sand than on flatter Osceola lots?",
            "The washed-rock depth and compaction are the same either way. What changes is how quickly the "
            "ground below drains on its own, which is an advantage for a run that gets rinsed daily. See our " +
            svc("pet") + " page for the infill options that fit a dog run specifically."),
    ],
    "sources": SRC,
}

LOCAL["putting"] = {
    "title": "Backyard Putting Greens in Davenport's Golf Communities",
    "meta": "Backyard putting green installation in Davenport, FL: golf-frontage HOA review, ridge-lot contouring, and the $14–$30/sq ft market range, September 2026.",
    "h1": "Putting greens on Davenport's golf-frontage lots",
    "lede": capsule(
        "Backyard putting greens in Davenport run " + price("putting") + " a square foot installed, typically " +
        price("putting", True) + ", as of September 2026. A fair share of our calls here come from Providence "
        "and other golf-course communities, where the green sits closer to a shared fairway than to the street."
    ),
    "sections": [
        ("A green that faces the fairway, not the sidewalk",
         "<p>Providence, a roughly 2,200-acre golf community built around an 18-hole course, is the kind of "
         "Davenport-area subdivision where a backyard putting green is often more visible from the course than "
         "from the street out front. " + a("/laws/hoa-rules/", "F.S. 720.3045") + " only protects turf that a "
         "neighboring parcel or the frontage can't see, and on a golf-frontage lot the fairway functions like "
         "that adjacent view, which is worth raising with the association before assuming a fenced backyard "
         "counts as hidden.</p>"),
        ("Contouring a green on sloped ridge ground",
         "<p>Davenport's share of the Lake Wales Ridge means some golf-community lots carry more natural slope "
         "than a flat " + city("kissimmee", "Kissimmee-area") + " yard would, which can work in a green's favor. "
         "A gentle existing grade gives a "
         "contoured green some of its break for free, rather than requiring the crew to build up a false ridge "
         "with extra base material. On the steeper end of Candler sand's slope range, we still terrace the "
         "surrounding fringe so the green itself plays true rather than tilting with the lot.</p>"),
        ("Cups, fringe and the base underneath both",
         "<p>A residential green needs a firmer, more consistent subgrade than the fringe around it, since a cup "
         "sleeve seated in loose or unevenly compacted rock works its way crooked within a season. We build the "
         "green's pad and the fringe as one continuous washed-rock base rather than two separate patches, which "
         "matters more on a ridge lot where the ground's natural drainage can otherwise pull moisture unevenly "
         "under a divided base.</p>"),
    ],
    "scenario": (
        "Say you have a green behind a fairway home",
        "<p>Say you have a 700 sq ft green and fringe behind a Providence fairway home, with two cups and a chipping "
        "apron worked into the layout. At the typical " + price("putting", True) + " range, that lands around "
        "$12,600 to $17,500 installed, before accounting for any extra contouring the existing slope adds or "
        "removes from the base work. Because the green faces the course, the HOA's architectural review usually "
        "asks for the same drawings a street-facing project would need.</p>"
    ),
    "faqs": [
        faq("Does a golf-frontage putting green need HOA approval even if neighbors can't see it?",
            "Likely yes. F.S. 720.3045 protects turf hidden from the street or an adjacent lot, and a green "
            "visible from a shared fairway generally doesn't fit that protection, so plan on an ARC submission."),
        faq("Does the ridge's slope make a green cheaper or more expensive to build?",
            "It can go either way. A gentle existing grade can reduce how much material a crew adds for contour, "
            "while a steeper shoulder lot adds compaction and edge work that pushes a job toward the top of the "
            "published range. Our " + svc("putting") + " page covers contouring and cup placement in general."),
    ],
    "sources": SRC,
}

LOCAL["playground"] = {
    "title": "Playground Turf for Davenport, FL Family Yards",
    "meta": "Playground turf installation in Davenport, FL: shock-pad sizing for backyard play sets, fast population growth, and the $10–$25/sq ft market range, September 2026.",
    "h1": "Playground turf behind Davenport's newest family homes",
    "lede": capsule(
        "Playground turf in Davenport runs " + price("playground") + " a square foot installed, typically " +
        price("playground", True) + ", as of September 2026. The city's population grew roughly 234 percent "
        "between the 2010 and 2020 Census, and most of those new households are the young families driving this "
        "service."
    ),
    "sections": [
        ("A decade of new families, one backyard play set at a time",
         "<p>Davenport counted 2,888 residents in 2010 and 9,043 in 2020 (" + ext(CENSUS[1], "Census Bureau "
         "QuickFacts") + "), and most of that growth filled subdivisions built specifically for young households "
         "moving to Central Florida. A swing set or climbing structure going into a two- or three-year-old "
         "backyard is a common call here, usually on a builder-graded lot where the sod under it never had time "
         "to establish before kids started using the space.</p>"),
        ("Sizing the shock pad to the equipment, not the yard",
         "<p>The state's rule allows rubber or another synthetic infill only inside the footprint of playground "
         "equipment, never across the rest of a residential lawn, so we measure the critical fall height of "
         "whatever structure is going in and size a shock pad to that zone specifically. A taller climbing "
         "structure on a newer Davenport lot needs a thicker pad than a simple swing set does, and the two often "
         "share the same backyard.</p>"),
        ("What the city's own playgrounds tell us about surfacing choices",
         "<p>Davenport's own " + a(CITY_PARK[1], "Jamestown Park") + " upgraded its play equipment in 2026 with a "
         "rubberized safety surface, which is a poured system built for continuous public use rather than a "
         "residential budget. A backyard playground turf system does the equivalent job at home, cushioning the "
         "same fall zones with a turf-and-pad build sized for one family instead of a neighborhood.</p>"),
    ],
    "scenario": (
        "Say you have a play set behind a new build",
        "<p>Say you have a 500 sq ft backyard play area behind a home built in the last few years, with a swing set "
        "and a small climbing structure sharing the space. At the typical " + price("playground", True) +
        " range, that runs about $6,000 to $9,500 installed, with the higher end more likely if the climbing "
        "structure's fall height calls for a thicker pad than the swing set alone would need.</p>"
    ),
    "faqs": [
        faq("Can rubber infill go under a backyard swing set in Davenport?",
            "Yes, inside the footprint of the equipment itself. The state's 2026 rule limits rubber and other "
            "synthetic infill to that zone; the rest of the yard still uses silica, zeolite or coated sand."),
        faq("Does a newer Davenport subdivision's builder sod affect a playground turf job?",
            "Often. Thin, fast-installed builder sod rarely holds up under a swing set's traffic pattern, which "
            "is one reason playground turf calls here skew toward homes built in the last five to ten years."),
    ],
    "sources": SRC,
}

LOCAL["pool"] = {
    "title": "Pool & Lanai Turf in Davenport, FL Resort Homes",
    "meta": "Pool and lanai turf in Davenport, FL: screen-cage installs in resort-home subdivisions where every house has a pool, market range $8–$18/sq ft, September 2026.",
    "h1": "Turf around the pool cage in Davenport's resort homes",
    "lede": capsule(
        "Pool-area turf in Davenport uses the residential market range, " + price("residential") + " a square "
        "foot installed, typically " + price("residential", True) + ", as of September 2026. In resort "
        "subdivisions such as Solterra, where every home is built with its own pool, that turf usually goes "
        "inside a screened cage rather than an open yard."
    ),
    "sections": [
        ("Every home with a pool changes what \"pool turf\" means here",
         "<p>Solterra Resort's homes are built with a private pool as standard rather than an upgrade (" +
         ext(SOLTERRA_PROFILE[1], "Solterra Resort's community profile") + "), and Providence and several "
         "neighboring subdivisions follow a similar pattern. That makes pool-cage turf one of the more routine "
         "calls in Davenport's newer neighborhoods, rather than a one-off request tied to a single custom home, "
         "and it means most of these jobs happen inside a screen enclosure from the start.</p>"),
        ("Turf over concrete inside the cage",
         "<p>A lanai slab poured for a resort-home pool cage needs a drainage underlay and glued-down edges "
         "rather than the washed-rock base a lawn gets, since there's no soil underneath to grade or compact. "
         "On a Davenport builder home, that slab is usually flat and recently poured, which simplifies the layout "
         "compared with an older, settled patio elsewhere in the county.</p>"),
        ("Guest turnover raises the traffic question",
         "<p>Where a pool-cage home doubles as a short-term rental, which is common in Davenport's resort "
         "subdivisions, the turf around the pool sees a new set of feet every few days rather than one family's "
         "routine. We spec a denser, better-stabilized product for that traffic pattern, since a lighter economy "
         "turf mats faster under back-to-back guest turnovers than it would in an owner-occupied home.</p>"),
    ],
    "scenario": (
        "Say you have a screened lanai at a resort home",
        "<p>Say you have a 350 sq ft pool deck inside a screen cage at a Solterra-style rental home, with a poured "
        "concrete slab already in place around the pool shell. At the typical " + price("residential", True) +
        " range, 350 sq ft of turf-over-concrete runs about $3,500 to $5,600 installed, with the drainage "
        "underlay and edge-gluing adding labor a bare-soil yard wouldn't need at that same square footage.</p>"
    ),
    "faqs": [
        faq("Does turf over a Davenport lanai slab need a different base than a lawn?",
            "Yes. Concrete gets a drainage underlay and adhesive-secured edges instead of compacted crushed rock, "
            "since there's no soil layer to grade underneath the slab."),
        faq("Do rental-home pool cages need a heavier-duty turf product?",
            "We recommend it. A short-term rental's pool area sees more foot traffic per month than an "
            "owner-occupied home, so a denser, better-stabilized product holds its texture longer under that "
            "turnover."),
    ],
    "sources": SRC,
}

LOCAL["str"] = {
    "title": "Vacation Rental Turf in Davenport, FL",
    "meta": "Vacation rental turf in Davenport, FL: Polk County rental tax receipt, resort-zoned subdivisions, and guest-turnover scheduling, market range noted, September 2026.",
    "h1": "Guest-ready turf for Davenport's short-term rental homes",
    "lede": capsule(
        "Vacation rental turf in Davenport uses the residential market range, " + price("residential") +
        " a square foot installed, typically " + price("residential", True) + ", as of September 2026. Much of "
        "the county's short-term rental activity concentrates in resort-zoned subdivisions built for exactly "
        "that use, which is where most of these jobs come from."
    ),
    "sections": [
        ("What counts as a rental-ready lot here",
         "<p>Polk County requires anyone renting a property for six months or less to hold a Class B county "
         "local business tax receipt, on top of the corresponding state transient-lodging license (" +
         ext(POLK_TAX[1], "Polk County Tax Collector") + "). Resort-style subdivisions built around " +
         city("four-corners", "Four Corners") + ", including Solterra and neighborhoods near " +
         city("championsgate", "ChampionsGate") + ", are generally treated as suited to that use under their "
         "land-use coding, while a standard single-family residential parcel may not be, which is worth "
         "confirming with county planning before assuming a lot can be booked nightly.</p>"),
        ("Scheduling around guests instead of a single family",
         "<p>A turf conversion at an owner-occupied home can pause around a family's schedule; a rental has "
         "bookings on the calendar most weeks of the year, so we plan the crew's timeline around a guest-free "
         "gap rather than assuming open access. Capping irrigation heads and finishing edge anchoring before the "
         "next check-in matters more here than on a house nobody else is arriving at.</p>"),
        ("Building for guests who don't know the yard",
         "<p>A returning family that owns the home learns where a lawn slopes or where a pond setback trims the "
         "usable yard; a new set of guests every few days doesn't. We anchor perimeters and seams to the same "
         "storm-wind standard everywhere, but on a rental we lean toward the sturdier edge option and skip "
         "anything that depends on a homeowner remembering to warn a guest away from it.</p>"),
    ],
    "scenario": (
        "Say you have a rental yard booked most weekends",
        "<p>Say you have a 1,100 sq ft rental-home yard in a Four Corners-area subdivision, booked most weekends "
        "through a property manager, with a retention pond along the back fence line. At the typical " +
        price("residential", True) + " range, that runs about $11,000 to $17,600 installed, and the pond's "
        "10-foot setback is worked into the layout before the square footage is finalized rather than after.</p>"
    ),
    "faqs": [
        faq("Does Polk County treat every Davenport-area subdivision as rental-friendly?",
            "No. Resort-zoned communities built for that purpose are generally treated as suited to short-term "
            "rentals, while standard residential zoning may restrict it, so check the land-use code with county "
            "planning rather than assuming based on the neighborhood's reputation."),
        faq("Do you install turf around active bookings, or only between guests?",
            "We schedule around a confirmed gap in the booking calendar whenever a property manager can share "
            "one; the base compaction and seam work go faster without guests walking the yard mid-install."),
        faq("Does short-term rental turf cost more than a family home's turf?",
            "The published range is the same. What can push a specific quote toward the top of it is a denser "
            "product spec for heavier turnover traffic, not the fact that the home is rented. Our " +
            svc("str") + " page has more on how we spec turf for guest traffic."),
    ],
    "sources": SRC,
}

LOCAL["commercial"] = {
    "title": "Commercial Turf for Davenport, FL HOAs and CDDs",
    "meta": "Commercial artificial turf in Davenport, FL: clubhouse lawns, CDD entry features and HOA common areas in resort subdivisions, quoted per job, September 2026.",
    "h1": "Turf for Davenport's HOA and CDD common areas",
    "lede": capsule(
        "Commercial turf covers common-area lawns, clubhouse grounds and entry features rather than a single "
        "backyard, so we quote it per job after a site visit instead of a single square-foot range. In "
        "Davenport, most of that work comes from the community development districts that finance and maintain "
        "the county's larger resort subdivisions."
    ),
    "sections": [
        ("Who actually owns a Davenport subdivision's common ground",
         "<p>Solterra Resort operates under its own community development district (" + ext(SOLTERRA_CDD[1],
         "the Solterra Resort CDD") + "), a public body that finances and maintains shared infrastructure "
         "separately from the homeowners association's dues. A CDD's board, not an individual homeowner's ARC "
         "application, is usually the decision-maker for turf going into a clubhouse lawn or an entry median, "
         "which changes who signs off on the project compared with a backyard job.</p>"),
        ("Clubhouse lawns that see foot traffic every day",
         "<p>A resort community's clubhouse lawn or pool-deck perimeter gets walked by residents and guests far "
         "more often than any single backyard, so we spec a heavier-face-weight product and a fuller washed-rock "
         "base depth than a typical home lawn needs. That upfront spend is what keeps a shared lawn from matting "
         "within a season the way a lighter residential product would.</p>"),
        ("Entry features and medians on ridge sand",
         "<p>A gated Davenport subdivision's entrance often sits on the same fast-draining Candler sand as the "
         "homes behind it, graded into a berm or median that a mower crew used to maintain weekly. Converting "
         "that strip to turf removes a recurring maintenance line item for the CDD, though the base still needs "
         "the same compaction care a sloped residential shoulder lot would get.</p>"),
    ],
    "scenario": (
        "Say a CDD wants its entry median converted",
        "<p>Say a Davenport-area CDD wants to convert a 2,000 sq ft entry median and clubhouse walkway border from "
        "irrigated sod to turf ahead of a dry-season maintenance contract renewal. Commercial work like this is "
        "quoted per job rather than off a published range, since access, edge detailing around hardscape and the "
        "heavier product spec all vary by site, so a measured walk-through comes before any number goes on paper.</p>"
    ),
    "faqs": [
        faq("Does a CDD or an HOA approve commercial turf in a Davenport community?",
            "It depends on which entity owns the ground. A CDD typically controls roads, medians and shared "
            "infrastructure, while a homeowners association usually controls the clubhouse and its immediate "
            "landscaping, so check the deed or the district's boundary map before submitting a design."),
        faq("Why is commercial turf priced per job instead of a per-square-foot range?",
            "Commercial sites vary too much in access, existing hardscape and traffic level for one published "
            "range to mean much; a measured site visit is what a real quote is based on."),
    ],
    "sources": SRC,
}

LOCAL["sports"] = {
    "title": "Sports & Fitness Turf on Davenport's Sloped Lots",
    "meta": "Sports and fitness turf in Davenport, FL: grading bocce courts and batting cages on Lake Wales Ridge slopes, quoted per job, September 2026.",
    "h1": "Bocce courts and sled tracks on Davenport's ridge lots",
    "lede": capsule(
        "A backyard sport surface, a bocce court, a batting cage lane or a sled track, is sized and built to fit "
        "the equipment and the space, so we quote it per job rather than a single square-foot range. Davenport's "
        "share of the Lake Wales Ridge means more of that layout work here is about slope than it would be on a "
        "flat Osceola lot."
    ),
    "sections": [
        ("Grading a level lane on ridge ground",
         "<p>A batting cage or a sled track needs a genuinely flat, compacted lane, and Davenport's Candler-sand "
         "lots can carry noticeably more natural slope than the flatter ground most of our sports-turf jobs sit "
         "on elsewhere in the service area. " + a("/blog/artificial-turf-on-a-slope/", "Building on a slope") +
         " isn't a reason to skip a project here; it just means more of the budget goes into cutting and "
         "retaining a level bench before the turf itself ever gets ordered.</p>"),
        ("A bocce court that plays true across the lot",
         "<p>Bocce depends on a flat, consistent surface more than most backyard sports do, since a subtle grade "
         "change pulls a ball off line the way it wouldn't on a putting green built with intentional break. On a "
         "sloped Davenport shoulder lot, we cut into the high side and build up the low side with the same "
         "washed-rock base rather than laying turf over the existing grade unmodified.</p>"),
        ("Sizing a home-gym sled track to what the yard allows",
         "<p>A sled or agility lane needs a straight run of a specific length, and a narrower Davenport "
         "subdivision side yard sometimes can't fit the full distance a homeowner pictures. We measure the "
         "usable straight run first, including any retention-pond setback along a back property line, before "
         "designing around a length that fits the actual lot rather than an assumed one.</p>"),
    ],
    "scenario": (
        "Say you have a sloped side yard for a sled track",
        "<p>Say you have a side yard on a sloped Davenport lot that drops roughly two feet over its 40 ft length, "
        "and you want a home-gym sled track down the middle of it. Sports and fitness turf like this is quoted "
        "per job once we've cut and retained a level bench for the lane, since the grading work varies by how "
        "much slope a specific lot carries, so a site visit comes before a number.</p>"
    ),
    "faqs": [
        faq("Can a sloped Davenport lot support a bocce court or batting cage?",
            "Usually yes, once the lane is cut and retained to level. The slope changes how much base and "
            "retaining work a job needs, not whether the sport surface itself is possible."),
        faq("Does ridge sand drain well enough for a home-gym sled track?",
            "Better than most soils in the service area. Candler sand's rapid permeability means a graded, "
            "compacted lane sheds rain quickly once the turf and base are in."),
    ],
    "sources": SRC,
}

LOCAL["pavers"] = {
    "title": "Turf & Pavers: Davenport, FL Walkways and Strips",
    "meta": "Turf between pavers in Davenport, FL: historic downtown walkways and new-build driveway strips on ridge sand, quoted per job, September 2026.",
    "h1": "Turf ribbons between pavers, downtown to the new subdivisions",
    "lede": capsule(
        "Turf laid between pavers, along a driveway strip or a stepping-stone path, is priced per job rather "
        "than a single square-foot range, since the paver layout and base condition vary from one Davenport lot "
        "to the next. We see this request on both ends of town, from the historic core to the newest builder "
        "streets."
    ),
    "sections": [
        ("Uneven old sidewalks near the historic district",
         "<p>The Davenport Historic District's preserved downtown still shows some original, uneven sidewalks "
         "from its 1920s buildout (" + ext(HIST_DIST[1], "the district's own description") + "), and a nearby "
         "home's paver walkway sometimes inherited that same settled, irregular base. Turf ribbons between those "
         "pavers need a base leveled independently of whatever the surrounding hardscape is doing, rather than "
         "simply matching an old grade that's already shifted over a century.</p>"),
        ("New-build driveway strips on fast-draining sand",
         "<p>A newer Davenport subdivision home often has a paver driveway with a narrow turf accent strip down "
         "the middle or along an edge, a common builder-era detail. Because the Candler sand underneath drains "
         "quickly on its own, a shallow washed-rock base under that strip rarely holds standing water the way "
         "the same detail might on heavier soil elsewhere in the county.</p>"),
        ("Where the ribbon meets the paver edge",
         "<p>The seam between turf and paver is the part that fails first if it's built wrong, since a loose "
         "edge lets infill wash out from underneath during a heavy Central Florida downpour. We set a hard edge "
         "restraint against the paver course itself rather than relying on the turf's perimeter nails alone to "
         "hold that line.</p>"),
    ],
    "scenario": (
        "Say you have a paver driveway near downtown",
        "<p>Say you have a 90-linear-foot paver driveway near downtown Davenport with a 12-inch turf strip planned "
        "down the center, replacing grass that never filled in under the paver joints. Turf-and-paver work like "
        "this is quoted per job once we've measured the strip's total area and checked the paver edge condition, "
        "since the edge-restraint detail is what drives labor more than the square footage itself.</p>"
    ),
    "faqs": [
        faq("Does turf between pavers need the same base depth as a full lawn?",
            "A shallower base often works for a narrow strip, but it still has to be washed, open-graded material "
            "rather than fines-heavy fill, for the same reasons a full lawn's base does."),
        faq("Will turf accent strips wash out during Davenport's rainy season?",
            "Not if the paver edge is restrained properly. Most washouts trace back to a loose edge letting "
            "infill escape, not to the ridge sand's naturally fast drainage."),
    ],
    "sources": SRC,
}

LOCAL["repair"] = {
    "title": "Artificial Turf Repair in Davenport, FL",
    "meta": "Artificial turf repair in Davenport, FL: wind-lifted edges on exposed ridge lots and rental-home wear, quoted per job after a site visit, September 2026.",
    "h1": "Fixing lifted seams and worn turf around Davenport",
    "lede": capsule(
        "Turf repair, open seams, lifted edges, melted spots or a drainage complaint, is priced per job once "
        "we've seen the damage, since the fix depends on what actually failed. Davenport's newer subdivisions "
        "and its handful of exposed ridge-top lots each produce a slightly different repair call."
    ),
    "sections": [
        ("Wind working an edge loose on an open ridge lot",
         "<p>A lot near the higher, more open ground on Davenport's stretch of the Lake Wales Ridge can catch "
         "more sustained wind than a sheltered in-town yard, especially where a newer subdivision hasn't grown "
         "in mature landscaping yet. An edge anchored with too few fasteners, or a border that relied on "
         "adhesive alone instead of a paver or bender-board restraint, is the kind of repair we see more often on "
         "those exposed lots after a windy stretch.</p>"),
        ("Heavier wear on rental-home turf",
         "<p>A short-term rental's turf, common across Davenport's resort subdivisions, takes more cumulative "
         "foot traffic per year than an owner-occupied lawn does, simply from the volume of different guests "
         "walking the same paths to a pool gate or a fire pit. Matted high-traffic lanes and infill that's "
         "thinned out faster than expected are repair patterns that show up sooner on a rental's timeline than "
         "on a family home's.</p>"),
        ("A base that was never built for ridge sand's drainage",
         "<p>Occasionally a repair call traces back to a base built with unwashed or fines-heavy fill instead of "
         "the washed crushed rock the state rule requires, which clogs over a season or two regardless of how "
         "well the native ridge sand underneath drains. That kind of repair usually means pulling the affected "
         "section and rebuilding the base correctly, not just re-seaming the turf on top of it.</p>"),
    ],
    "scenario": (
        "Say you have a lifted edge at a rental pool cage",
        "<p>Say you have a 200 sq ft section of turf along a Davenport rental home's pool-cage edge that's lifted "
        "and curled after a windy few months, with infill visibly thin along the same stretch. Repairs like this "
        "are quoted per job after a site visit, since re-anchoring a lifted edge costs far less than pulling and "
        "rebuilding a section where the base itself failed, and the two aren't obvious apart until someone lifts "
        "the turf and looks.</p>"
    ),
    "faqs": [
        faq("Why do edges lift more often on Davenport's ridge-top lots?",
            "More consistent wind exposure on open, higher ground, combined with young subdivision landscaping "
            "that hasn't grown in to break the wind yet, is the pattern we see most on those repair calls."),
        faq("Does a rental home's turf need repairs more often than a family home's?",
            "Generally yes, proportional to how much guest traffic it sees. High-traffic lanes to a pool gate or "
            "grill area wear faster than the rest of the yard on any property, but a rental accumulates that "
            "traffic faster."),
        faq("Do you handle repair calls outside Davenport itself?",
            "Yes, including neighboring " + city("haines-city", "Haines City") + " and " +
            city("poinciana", "Poinciana") + ", where the same wind and traffic patterns show up on similarly "
            "exposed lots."),
    ],
    "sources": SRC,
}

LOCAL["cleaning"] = {
    "title": "Turf Cleaning & Maintenance in Davenport, FL",
    "meta": "Artificial turf cleaning in Davenport, FL: sandy debris, oak and pine litter on ridge lots, and rental turnover cleaning, quoted per job, September 2026.",
    "h1": "Keeping Davenport's ridge-lot turf clean between seasons",
    "lede": capsule(
        "Turf cleaning, pet-odor treatment, power brooming, infill top-ups, is priced per job based on the "
        "square footage and how neglected the surface has gotten, not a flat per-square-foot rate. In Davenport, "
        "the two most common triggers are ridge-lot yard debris and short-term rental turnover."
    ),
    "sections": [
        ("Oak and pine debris off ridge ground",
         "<p>The native plant community on Davenport's stretch of the Lake Wales Ridge leans toward scrub and "
         "sand-live oaks alongside pine, and even a landscaped subdivision lot planted near remnant ridge "
         "vegetation sheds a heavier load of leaves and needles than a typical suburban yard. Left sitting, that "
         "debris breaks down into the infill layer and changes how the turf drains, which is the main reason a "
         "seasonal power-brooming visit pays for itself here.</p>"),
        ("Sand tracked in from a fast-draining base",
         "<p>Because so much of Davenport sits on excessively drained Candler sand, a bare or thinly planted "
         "border next to a turf lawn tracks more loose sand onto the surface than heavier native soils would "
         "elsewhere in the county. A quick broom or blower pass along those borders keeps that sand from working "
         "down into the infill and adding weight the backing wasn't sized to carry.</p>"),
        ("Turnover cleaning between rental guests",
         "<p>A short-term rental's turf needs a faster cleaning cadence than a family home's, since sunscreen, "
         "food debris and pool splash-out around a pool cage build up across back-to-back bookings rather than "
         "one household's routine. Property managers in Davenport's resort subdivisions often fold a turf rinse "
         "and spot-clean into the same schedule as the interior turnover clean.</p>"),
    ],
    "scenario": (
        "Say you have oak litter matted into an older lawn",
        "<p>Say you have a 600 sq ft backyard lawn under a stand of sand-live oaks in an older Davenport "
        "neighborhood, matted with several seasons of unswept leaf litter and thin on infill in the shaded "
        "corners. Cleaning jobs like this are quoted per job once we've seen how much debris has worked down "
        "into the backing, since a light seasonal broom and a full power-clean with an infill top-up take very "
        "different amounts of labor for the same square footage.</p>"
    ),
    "faqs": [
        faq("How often should ridge-lot turf be cleaned in Davenport?",
            "It depends on nearby tree cover more than location alone; a lot near mature oaks or pines needs a "
            "seasonal clean, especially after a late-winter leaf drop, while an open lot with little canopy can "
            "often go longer between visits."),
        faq("Do rental-home turf areas need cleaning after every guest?",
            "Not usually every stay, but a property manager on a weekly or biweekly cleaning cadence for the "
            "interior often adds a turf rinse and spot-check to that same visit rather than waiting for a "
            "seasonal service."),
        faq("Is the cleaning routine different from what you'd recommend in Kissimmee?",
            "Not in method, only in frequency. The same rinse-and-broom routine we recommend for " +
            city("kissimmee", "Kissimmee") + " lawns applies here; Davenport's oak and pine litter is what "
            "usually pushes the schedule tighter."),
    ],
    "sources": SRC,
}

LOCAL["replacement"] = {
    "title": "Turf Removal & Replacement in Davenport, FL",
    "meta": "Turf and worn-sod replacement in Davenport, FL: new-construction sod failing on ridge sand, and aging turf rebuilds, quoted per job, September 2026.",
    "h1": "Replacing failed sod and worn turf around Davenport",
    "lede": capsule(
        "Removal and replacement, pulling worn turf or dead sod and rebuilding the base underneath, is priced "
        "per job depending on how much of the old base gets reused versus rebuilt. In Davenport's newest "
        "subdivisions, most of these calls start with builder sod that never had a chance on ridge sand."
    ),
    "sections": [
        ("New-construction sod that never took",
         "<p>A builder's crew typically lays sod over a thin layer of topsoil spread across whatever fill graded "
         "the lot, and on Davenport's fast-draining Candler ground, that shallow layer can dry out faster than "
         "sod's roots can establish, especially before an irrigation system is fully dialed in. " +
         post("why-new-construction-sod-dies-in-osceola-county", "Builder sod failing on a new lot") + " is a "
         "pattern that shows up on ridge sand for a similar reason, even outside the county the post is titled "
         "for: fast drainage plus thin topsoil equals a lawn that struggles from day one.</p>"),
        ("Pulling old turf without disturbing a good base",
         "<p>When an aging turf installation has reached the end of its 10- to 20-year lifespan but the "
         "washed-rock base underneath is still sound, we pull and replace only the turf layer, saving the labor "
         "and cost of rebuilding compaction that's already holding. That's more often the case on a Davenport lot "
         "where the original base was built to the state's washed-material standard than on an older install "
         "predating that rule.</p>"),
        ("Rebuilding a base that was cut corners the first time",
         "<p>Where the old base itself has crusted over from unwashed fill or settled unevenly, replacement means "
         "starting over: strip the turf, remove the failed base material, regrade, and compact a proper washed-rock "
         "layer before anything new goes down. On a sloped ridge-adjacent lot, that regrading step often takes "
         "longer than the original install did, since correcting a bad grade is harder than building one right "
         "the first time.</p>"),
    ],
    "scenario": (
        "Say you have builder sod that died in year two",
        "<p>Say you have a 1,600 sq ft front and side yard on a three-year-old Davenport home where the builder sod "
        "died back within its first two summers and was never successfully replanted. Replacing that dead sod "
        "with turf is quoted per job once we've confirmed whether the existing grade needs correction, since a "
        "yard that's been bare and eroding for months often needs more regrading than a healthy lawn being "
        "converted fresh.</p>"
    ),
    "faqs": [
        faq("Why does new-construction sod fail so often in Davenport?",
            "Thin builder topsoil over fast-draining ridge sand dries out faster than young sod roots can keep "
            "up with, particularly before irrigation is fully established, which is the pattern behind most of "
            "these replacement calls."),
        faq("Can old turf be replaced without rebuilding the whole base?",
            "Often yes, if the original base was built to the state's washed-rock standard and simply settled or "
            "aged normally. A base that crusted over from unwashed fill usually needs a full rebuild instead."),
    ],
    "sources": SRC,
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
