# -*- coding: utf-8 -*-
"""Permit hub + 8 jurisdiction pages. Informational, not legal advice.
Research checked September 2026; raw findings in research/permits-research.md."""
from _data import CITIES, COUNTIES
from _posts import PERMIT_PAGES
from _helpers import page, capsule, sec, table, faq, note, a, city, src, ext

CRUMBS_HUB = [("Laws & HOA", "/laws/")]
CRUMBS_J = [("Laws & HOA", "/laws/"), ("Permits", "/laws/permits/")]

OSCEOLA_PA = ("Osceola County Property Appraiser — parcel search", "https://www.property-appraiser.org/")
ORANGE_PA = ("Orange County Property Appraiser — parcel search", "https://ocpafl.org/")
POLK_PA = ("Polk County Property Appraiser — parcel search", "https://www.polkflpa.gov/")
LAKE_PA = ("Lake County Property Appraiser — parcel search", "https://www.lakecopropappr.com/")
SEM_PA = ("Seminole County Property Appraiser — parcel search", "https://www.scpafl.org/")

HB683_ROUTE = ("/laws/florida-hb-683/", "HB 683 and DEP Rule 62-308.100")
RESIDENTIAL_ROUTE = ("/artificial-grass-installation/", "Residential artificial grass installation")
HOA_ROUTE = ("/laws/hoa-rules/", "What a Florida HOA can and can't restrict")


def jroute(key):
    return f"/laws/permits/{key}/"


def jlink(key, text=None):
    return a(jroute(key), text or PERMIT_PAGES[key])


def crow(slug, label=None):
    c = CITIES[slug]
    return (c["route"], label or f"Turf installers in {c['name']}")


def corow(key, label=None):
    c = COUNTIES[key]
    return (c["route"], label or f"Service area: {c['name']}")


# ============================================================== hub
def hub():
    body = "".join([
        sec("Three offices, and only one of them writes the permit",
            f"<p>A synthetic turf project in Central Florida answers to three separate authorities, and only one of them stamps a permit. The State of Florida sets a floor: since May 19, 2026, Rule 62-308.100 keeps a city or county from banning or singling out compliant turf on a single-family lot of an acre or less ({src('dep-rule', 'the adopted rule')}; {src('fs125572', 'F.S. 125.572')}). Your city or county still runs its own permit counter, still reviews drainage and easements, and still decides what happens in a right-of-way or on a bigger lot. Your HOA, if you have one, is neither of those and answers to {a('/laws/hoa-rules/', 'a different statute entirely')}.</p>"
            + "<p>This page is about the middle layer: which office has your parcel, what its published code says about synthetic turf, and who to call before a crew shows up. The eight pages below cover Kissimmee, Osceola County, St. Cloud, Orange County, Orlando, Polk County, Lake County and Seminole County one at a time, because each office publishes something different, or in most cases here, publishes nothing on the subject at all.</p>"),
        sec("Do I need a permit for artificial turf in Kissimmee or Osceola County?",
            "<p>As of September 2026, neither the City of Kissimmee's nor Osceola County's Land Development Code mentions synthetic turf, and neither office has published a yes-or-no permit answer for a residential lawn swap. That silence isn't a green light: capping irrigation heads under the turf can need its own plumbing permit, and grading near a swale can draw a separate review. Call the Building Division before you schedule a crew.</p>"
            + f"<p>Capping the heads is required by the state standard itself, not a local choice, so budget time for that step regardless of what the city or county says. The City of Kissimmee's Building Division is reachable at 407-518-2120; the Osceola County Building Department is at 407-742-0200. Both take applications online, and both are covered in more depth on their own pages: {jlink('city-of-kissimmee')} and {jlink('osceola-county')}.</p>"),
        sec("Does artificial turf count as impervious surface?",
            "<p>It depends on the office's older code, and since May 19, 2026 that question has a new ceiling. A compliant system must sit on permeable backing over a pervious subgrade, and a local government's only drainage lever is a permeability cap of at most 10 inches an hour. A code that flatly labels synthetic turf impervious can no longer be applied that way to a compliant system.</p>"
            + f"<p>Orlando's landscape code is the one on this page that used to classify turf as impervious outright; the other seven never addressed the question in a published rule, so there's nothing old for the state standard to override there. {jlink('city-of-orlando', 'Orlando is the exception')}, and that page walks through what changed for its specific rule.</p>"),
        sec("Artificial turf rules by jurisdiction",
            "<p>Same state floor everywhere, different local starting point. This table is the short version; each linked page has the citations, the department contact and the parcel-lookup tool for that office.</p>"
            + table("Artificial turf rules by jurisdiction, Central Florida",
                    ["Jurisdiction", "What the local code says about synthetic turf", "Permit or review needed?", "Who to call", "Our page"],
                    [[jlink("city-of-kissimmee"), "No mention found in the Land Development Code", "Not published either way; confirm before starting", "Development Services, 407-518-2120", jlink("city-of-kissimmee", "Details")],
                     [jlink("osceola-county"), "No mention found in the Land Development Code", "Not published either way; confirm before starting", "Building Department, 407-742-0200", jlink("osceola-county", "Details")],
                     [jlink("city-of-st-cloud"), "No mention found in the Code of Ordinances", "Not published either way; confirm before starting", "Building Department, 407-957-7243", jlink("city-of-st-cloud", "Details")],
                     [jlink("orange-county"), "Landscape code defines \"turf\" as natural grass species only; no synthetic-turf section found", "Not published either way; confirm before starting", "Permitting Services, 407-836-5550", jlink("orange-county", "Details")],
                     [jlink("city-of-orlando"), "Landscape code has specific artificial-turf rules: classed impervious, barred within 50 ft of water and in the right-of-way", "Yes, an engineering permit under that code", "Permitting Services, 407-246-2121", jlink("city-of-orlando", "Details")],
                     [jlink("polk-county"), "No mention found in the Land Development Code", "Not published either way; confirm before starting", "Building Division, 863-534-6080", jlink("polk-county", "Details")],
                     [jlink("lake-county"), "No mention found in the Land Development Regulations", "Not published either way; confirm before starting", "Building Services, 352-343-9653", jlink("lake-county", "Details")],
                     [jlink("seminole-county"), "No mention found in the Land Development Code", "Not published either way; confirm before starting", "Building Division, 407-665-7050", jlink("seminole-county", "Details")]],
                    "Checked against each office's published code and website in September 2026; a jurisdiction's silence on synthetic turf is not the same as a written exemption from permitting.")),
        sec("How to find out which office actually has your parcel",
            f"<p>A Kissimmee mailing address doesn't guarantee City of Kissimmee jurisdiction. Plenty of homes with a Kissimmee or Orlando ZIP code sit in unincorporated county land, because the postal service draws its lines differently than a city charter does. The fix is a parcel search on the property appraiser's site for whichever county the lot is in: {ext(OSCEOLA_PA[1], "Osceola County's site")} for Kissimmee and St. Cloud addresses, {ext(ORANGE_PA[1], "Orange County's site")} for Orlando-area addresses, and the {ext(POLK_PA[1], "Polk")}, {ext(LAKE_PA[1], "Lake")} or {ext(SEM_PA[1], "Seminole")} county sites for the rest of the service area. Type in the address, and the parcel record lists the taxing jurisdiction, which tells you whether a city or the county handles your permit.</p>"),
        sec("What the state rule changed, and what your local office still controls",
            f"<p>{a('/laws/florida-hb-683/', 'HB 683 and Rule 62-308.100')} stop a city or county from banning compliant turf on a covered lot or writing a rule that conflicts with the state's material, drainage and setback standards. They don't stop a local office from requiring a permit or a plan review, setting a permeability number of its own as long as it's 10 in/hr or looser, keeping a waterbody buffer that's no tougher on turf than it is on grass, or regulating a right-of-way, an easement, a commercial site, an apartment complex or a lot bigger than an acre. Those categories sit outside the state rule entirely, and every jurisdiction on this page keeps full authority over them.</p>"
            + "<p>So a code office that says nothing about synthetic turf specifically hasn't lost any of its ordinary permitting power. What it's lost is the ability to point to an old ban, or to treat compliant turf worse than natural grass on the water-buffer and drainage questions the rule now covers.</p>"),
        sec("Your HOA runs on a different clock",
            f"<p>None of the eight offices below can tell your association what to approve. {a('/laws/hoa-rules/', 'F.S. 720.3045')} is the statute that limits an HOA, and it only protects turf that isn't visible from the street or a neighboring lot. A city or county permit and an ARC approval are two separate steps, and getting one doesn't excuse the other.</p>"),
    ])
    faqs = [
        faq("What if my city or county doesn't mention synthetic turf at all?", "Most of the eight offices here don't. That means no local ban to worry about and no local turf-specific standard either, so the state rule is the only written standard that applies; ordinary permitting rules for landscaping, irrigation and drainage still apply the way they would for any yard project."),
        faq("Does it cost anything to find out if I need a permit?", "No. Every office listed here answers permit questions by phone at no charge, and each online portal lets you browse permit types before applying. What a permit itself costs, if one applies, varies by office and by project value."),
        faq("Can a city or county still deny my turf project?", "Yes, for reasons outside the state rule: it's in a right-of-way or easement, it's on a lot over an acre or a commercial or multi-family property, or the application is missing a required drainage or zoning review. It can't deny a compliant residential project just because it's synthetic turf."),
        faq("Do I need a separate permit to cap the irrigation heads under the turf?", "Possibly. The state standard requires capping in-ground heads that would otherwise water synthetic turf, and depending on the office, that plumbing work can need its own permit even when the turf itself doesn't. Ask when you call."),
        faq("Where do I even start if I don't know which office has my lot?", "Run the address through the property appraiser's parcel search for your county, which the section above links for each county in our service area. The record shows the taxing jurisdiction, and from there the matching page on this site gives you the department and phone number."),
    ]
    return page("/laws/permits/", "permit",
                "Artificial Turf Permits in Central Florida (2026)",
                "Do you need a permit for synthetic turf in Kissimmee, Osceola, Orange, Polk, Lake or Seminole? Code findings and contacts for all eight, checked September 2026.",
                "Artificial turf permits, by city and county",
                capsule("As of September 2026, seven of the eight Central Florida offices we checked, including Kissimmee and Osceola County, publish nothing about synthetic turf and no stated permit rule for a residential lawn. Orlando is the exception, with a specific landscape-code section. Every office keeps its permit, drainage and right-of-way authority under the state's May 19, 2026 turf standard."),
                body, faqs=faqs, crumbs=CRUMBS_HUB, crumb="Permits",
                sources=["dep-rule", "fs125572", "hb683", "fs7203045"],
                related=[HB683_ROUTE, HOA_ROUTE, RESIDENTIAL_ROUTE, corow("osceola"), corow("orange")])


# ============================================================== City of Kissimmee
def kissimmee():
    body = "".join([
        sec("What the Kissimmee code says",
            "<p>As of September 2026, a search of the City of Kissimmee's Land Development Code, part of the city's Code of Ordinances, turns up no section that names synthetic turf, artificial turf or artificial grass. The landscaping and zoning chapters cover required planting, buffers and tree protection in terms of live vegetation, without a separate category for a manufactured surface.</p>"
            + "<p>That's a finding, not a guess: we searched the code and the city's own planning pages and found nothing to quote. If Kissimmee has an internal handout or interpretation that isn't posted publicly, the Building Division is the office that would have it.</p>"),
        sec("What the state rule changed here",
            f"<p>Kissimmee never had a synthetic-turf ban on the books to begin with, so {src('dep-rule', 'Rule 62-308.100')} didn't repeal anything visible in the city's code. What it did was set a statewide floor the city can't undercut for a single-family lot of an acre or less: turf has to be permeable, kept out of tree drip lines without an arborist's letter, capped instead of irrigated by an in-ground system, and at least 10 feet from a pond, lake or canal unless a seawall stands between. Kissimmee is still free to require its ordinary building or landscape permit and to review drainage the way it always has.</p>"),
        sec("What that means for a turf job here, as we read it",
            "<p>Since the code is silent, a straightforward backyard lawn conversion in Kissimmee proper isn't running into a written turf rule either way. What it can still run into is the city's general permitting process for exterior work, an irrigation permit for capping heads, or a drainage question if the lot backs up to a retention pond or a swale. An installer wrote this reading, not the Building Division, so it should guide a phone call, not replace one.</p>"
            + table("Kissimmee quick facts", ["Question", "Answer"],
                    [["Turf named in the code?", "No, as of September 2026."], ["Permit stated for residential turf?", "Not published either way."],
                     ["Department", "Development Services, Building Division"], ["Phone", "407-518-2120"],
                     ["Portal", "EnerGov Citizen Self-Service"], ["Property appraiser", "Osceola County"]])),
        sec("Who to call, and where to apply",
            f"<p>Kissimmee's Development Services Building Division sits at 101 Church Street; the fastest path is a call to 407-518-2120 or an email to the division's permitting inbox before you file anything. Online applications go through the city's Tyler EnerGov portal, reached from the {ext('https://www.kissimmee.gov/Business-Development/Permits-Inspections/File-for-a-Permit', 'File for a Permit page')} on kissimmee.gov.</p>"),
        sec("Checking your parcel",
            f"<p>Not every Kissimmee-addressed lot sits inside the city limits; plenty are in unincorporated Osceola County a block or two past the line. Search the address on the {ext(OSCEOLA_PA[1], OSCEOLA_PA[0])} to see the taxing jurisdiction on the parcel record. If it comes back unincorporated, {jlink('osceola-county', 'the Osceola County page')} has the office you actually need.</p>"),
        sec("Water utility and irrigation",
            f"<p>Toho Water Authority serves Kissimmee, with irrigation limited to two days a week by address, odd addresses on Wednesday and Saturday and even addresses on Thursday and Sunday, and no daytime watering ({src('toho-days', 'Toho’s schedule')}). None of that changes the turf job directly, since the state standard already bars using an in-ground system on synthetic turf; it matters for whatever grass stays around the edges.</p>"),
        note("This page is a contractor's plain-language reading of what's published, not a ruling from the city. Confirm anything your project depends on with Kissimmee's Building Division."),
    ])
    faqs = [
        faq("Does a Kissimmee ARC or HOA process replace the city permit?", "No. An architectural review from your homeowners association and a building or zoning permit from the city are separate approvals, and a synthetic-turf project inside city limits can need either, both or neither depending on the lot and the association."),
        faq("Is there a city fee just to ask a question about a permit?", "No. Calling or emailing the Building Division to ask whether a specific job needs a permit is free; fees apply only once you file an actual application."),
        faq("My lot backs onto Lake Tohopekaliga. Does the city add anything to the state's 10-foot rule?", "We found no Kissimmee-specific waterbody buffer for synthetic turf published as of September 2026, which leaves the state's 10-foot setback from the ordinary or mean high water line as the number to plan around unless the city tells you otherwise."),
        faq("Does the city require proof the turf meets the state's PFAS and heavy-metal standard?", "Nothing published says so. Ask for the manufacturer's statement anyway, since it's cheap insurance and the kind of document a reviewer could ask for later."),
    ]
    return page(jroute("city-of-kissimmee"), "permit",
                "Artificial Turf Permits in Kissimmee, FL (2026)",
                "Does the City of Kissimmee require a permit for synthetic turf? What the Land Development Code says, who to call, and how to check your parcel, as of September 2026.",
                "Artificial turf permits in the City of Kissimmee",
                capsule("As of September 2026, the City of Kissimmee's Land Development Code has no section naming synthetic or artificial turf, and the city hasn't published whether a residential lawn swap needs a permit. Development Services (407-518-2120) can confirm before you start. The state's May 19, 2026 turf standard still applies to any covered lot inside city limits."),
                body, faqs=faqs, crumbs=CRUMBS_J, crumb="City of Kissimmee",
                sources=["dep-rule", "fs125572", "toho-days", ("City of Kissimmee — File for a Permit", "https://www.kissimmee.gov/Business-Development/Permits-Inspections/File-for-a-Permit"), ("City of Kissimmee Land Development Code, Municode Library", "https://library.municode.com/fl/kissimmee/codes/code_of_ordinances"), OSCEOLA_PA],
                related=[crow("kissimmee"), corow("osceola"), HB683_ROUTE, RESIDENTIAL_ROUTE, HOA_ROUTE])


# ============================================================== Osceola County
def osceola():
    body = "".join([
        sec("What the Osceola County code says",
            "<p>As of September 2026, Osceola County's Land Development Code, searched through the county's Municode library, has no section on synthetic or artificial turf. The landscaping standards in the code are written around plant material, buffers and tree protection, and don't carve out a separate rule for a manufactured surface one way or the other.</p>"
            + "<p>Osceola County's own planning pages don't publish a turf-specific FAQ or handout either, at least not one we could find. That leaves the county's general zoning and building rules as the only written framework for a project until the county says otherwise.</p>"),
        sec("What the state rule changed here",
            f"<p>{src('fs125572', 'F.S. 125.572')} and {src('dep-rule', 'Rule 62-308.100')} bind Osceola County the same way they bind every county in Florida: on a single-family lot of an acre or less, the county can't ban compliant turf or hold it to a stricter waterbody buffer than natural grass gets, and its only drainage lever is a permeability number no tighter than 10 inches an hour. The county is separately weighing a broader water-conservation ordinance in 2026, which is about irrigation generally and hasn't been finalized as of this writing.</p>"),
        sec("What that means for a turf job in unincorporated Osceola County, as we see it",
            "<p>A backyard or front-yard conversion on an unincorporated lot isn't colliding with a published county turf rule, because there isn't one yet. It can still run into the county's ordinary permitting for exterior alterations, a plumbing permit for capping irrigation heads, or a stormwater review on a lot near a retention pond or canal. This paragraph is our contractor's read of a public code, not the county's own guidance, so treat it as a starting point for a phone call.</p>"
            + table("Osceola County quick facts", ["Question", "Answer"],
                    [["Turf named in the code?", "No, as of September 2026."], ["Permit stated for residential turf?", "Not published either way."],
                     ["Department", "Osceola County Building Department"], ["Phone", "407-742-0200"],
                     ["Portal", "Osceola County Permit Center (Accela)"], ["Property appraiser", "Osceola County"]])),
        sec("Who to call, and where to apply",
            f"<p>The Osceola County Building Department takes questions at 407-742-0200 or by email at permitting@osceola.org, and applications, inspection scheduling and fee payment run through the county's {ext('https://permits.osceola.org/', 'Online Permit Center')}, built on Accela Citizen Access.</p>"),
        sec("Checking your parcel",
            f"<p>Osceola County covers a wide unincorporated area outside Kissimmee, St. Cloud and Celebration, from Poinciana down to Harmony, and the fastest way to confirm a specific address is unincorporated is a lookup on the {ext(OSCEOLA_PA[1], OSCEOLA_PA[0])}. The record will show whether the parcel falls under the county or one of its cities; {jlink('city-of-kissimmee', 'the Kissimmee page')} and {jlink('city-of-st-cloud', 'the St. Cloud page')} cover those two.</p>"),
        sec("Water utility and irrigation",
            f"<p>Toho Water Authority serves most of unincorporated Osceola County on the same two-day-a-week schedule it uses in Kissimmee: odd addresses Wednesday and Saturday, even addresses Thursday and Sunday, no watering during daylight hours ({src('toho-days', 'Toho watering days')}). A synthetic turf area skips that schedule entirely once the in-ground heads are capped, per {src('dep-rule', 'the state standard')}; a proposed county water-conservation ordinance covering the rest of the yard was still pending as of mid-2026 ({src('osceola-water-2026', 'coverage of the proposal')}).</p>"),
        note("An installer put this page together from public sources, not the county's legal staff, so confirm anything that matters before a crew is on site."),
    ])
    faqs = [
        faq("Is my rural Osceola County property covered by the state turf standard?", "Only if it's a single-family residential lot of one acre or less. Larger parcels, and property zoned for agriculture or multiple units, fall outside Rule 62-308.100 and answer only to the county's own code."),
        faq("Does the county require a survey before approving a turf permit, if one is required?", "Nothing published addresses turf specifically. General land-alteration and drainage permits in the county often ask for a site plan or survey, so bring one to the conversation regardless."),
        faq("What if my community has a golf course pond or a canal behind the lot?", "The state's 10-foot waterbody setback applies unless a local buffer requirement already exists, and we found no county-specific synthetic-turf buffer published as of September 2026; ask the Building Department whether one applies to your specific parcel."),
        faq("Does unincorporated Osceola County allow turf in the front yard?", "The state rule doesn't distinguish front and back yards on a covered lot, and we found no county rule that does either. An HOA in a planned community, which the county's zoning doesn't control, is a separate question covered on our HOA page."),
    ]
    return page(jroute("osceola-county"), "permit",
                "Artificial Turf Permits in Osceola County, FL (2026)",
                "Does unincorporated Osceola County require a permit for synthetic turf? What the Land Development Code says, plus department contacts, checked September 2026.",
                "Artificial turf permits in Osceola County",
                capsule("As of September 2026, Osceola County's Land Development Code doesn't mention synthetic or artificial turf, and the county hasn't stated whether a residential lawn conversion needs a permit. The Building Department (407-742-0200) can confirm for a specific address. The state's May 19, 2026 turf standard applies on any covered lot in unincorporated Osceola County."),
                body, faqs=faqs, crumbs=CRUMBS_J, crumb="Osceola County",
                sources=["dep-rule", "fs125572", "toho-days", "osceola-water-2026", ("Osceola County Land Development Code, Municode Library", "https://library.municode.com/fl/osceola_county/codes/land_development_code"), ("Osceola County Online Permit Center", "https://permits.osceola.org/"), OSCEOLA_PA],
                related=[corow("osceola"), crow("kissimmee"), crow("st-cloud"), HB683_ROUTE, RESIDENTIAL_ROUTE])


# ============================================================== City of St. Cloud
def st_cloud():
    body = "".join([
        sec("What the St. Cloud code says",
            "<p>As of September 2026, a search of St. Cloud's Code of Ordinances and Land Development Code, hosted on Municode, doesn't turn up a section on synthetic or artificial turf. Landscape requirements in the code are written for live plant material, buffer strips and tree preservation, without a category built for a manufactured surface.</p>"
            + "<p>The city's Planning and Building pages don't carry a turf handout or FAQ either, based on what's published. Until St. Cloud adds language of its own, the state standard is the only written rule specific to synthetic turf that reaches a St. Cloud lot.</p>"),
        sec("What the state rule changed here",
            f"<p>{src('dep-rule', 'Rule 62-308.100')} took effect May 19, 2026 and, under {src('fs125572', 'F.S. 125.572')}, stops St. Cloud from adopting or keeping a rule that conflicts with the state's material, drainage and setback standards on a single-family lot of an acre or less. Because the city's code never singled out turf, there was nothing local to strike down. What changed is the ceiling on anything St. Cloud might write in the future, and the floor a homeowner can now point to if a future proposal goes further than the state allows.</p>"),
        sec("What that means for a turf job here, in our experience",
            "<p>A yard conversion inside St. Cloud city limits isn't up against a specific municipal turf rule, because the search came back empty. It can still meet the city's usual permitting for exterior work, a separate permit for capping an irrigation head, or a drainage question on a lot near one of St. Cloud's many lakes. We're describing what a crew runs into on the ground, not repeating anything the city's Building Department has told us directly.</p>"
            + table("St. Cloud quick facts", ["Question", "Answer"],
                    [["Turf named in the code?", "No, as of September 2026."], ["Permit stated for residential turf?", "Not published either way."],
                     ["Department", "St. Cloud Building Department"], ["Phone", "407-957-7243"],
                     ["Portal", "WebPermits"], ["Property appraiser", "Osceola County"]])),
        sec("Who to call, and where to apply",
            f"<p>St. Cloud's Building Department answers permit questions at 407-957-7243, and the city's {ext('https://stcloudfl.gov/50/Permit-Information', 'Permit Information page')} links to the WebPermits portal for filing, checking status and scheduling inspections.</p>"),
        sec("Checking your parcel",
            f"<p>St. Cloud sits entirely inside Osceola County, so every parcel search runs through the {ext(OSCEOLA_PA[1], OSCEOLA_PA[0])}. A search will confirm whether a given address is inside the city limits or in the unincorporated county just outside them; if it's the latter, {jlink('osceola-county', 'the county page')} has the office to call instead.</p>"),
        sec("Water utility and irrigation",
            f"<p>Toho Water Authority took over St. Cloud's water and wastewater utility on October 1, 2022, so the city now runs on Toho's rules rather than a separate municipal schedule, and the city's own {ext('https://stcloudfl.gov/1683/Watering-Schedules', 'watering-schedule page')} points there for the current days and times; questions go to 407-957-7344. Whatever the schedule says, it stops applying to a turf area entirely once the heads underneath are capped, which {src('dep-rule', 'the state standard')} now requires.</p>"),
        note("This isn't legal or code advice from the city; it's a local installer's summary, so verify anything that changes a bid with St. Cloud's Building Department directly."),
    ])
    faqs = [
        faq("Did St. Cloud have its own artificial turf ban before the state rule?", "We found no evidence of one in the current code, and the city's own published materials don't mention a former ban being repealed. If St. Cloud had an unwritten practice, only the Building Department would know."),
        faq("Does St. Cloud's lake-heavy geography change the waterbody setback?", "Not that we found published. The state's 10-foot setback from a pond, lake or canal applies unless the city has adopted its own buffer, and we saw no St. Cloud-specific buffer for synthetic turf as of September 2026."),
        faq("Is a permit required to remove old sod before installing turf?", "St. Cloud's code doesn't call this out for turf specifically. Because sod removal alone rarely needs a permit in most Florida cities, but grading and drainage changes often do, the safest move is asking the Building Department about your specific scope."),
        faq("Does St. Cloud allow turf on a lot backing up to East Lake Tohopekaliga?", "Nothing published treats that differently from any other waterfront lot. The state's 10-foot setback and drip-line rule both apply, and a local buffer, if St. Cloud ever adopts one, could add to that but not go below what natural turf gets."),
    ]
    return page(jroute("city-of-st-cloud"), "permit",
                "Artificial Turf Permits in St. Cloud, FL (2026)",
                "Does the City of St. Cloud require a permit for synthetic turf? What the code says, who to call, and how St. Cloud's water utility changed in 2022.",
                "Artificial turf permits in the City of St. Cloud",
                capsule("As of September 2026, St. Cloud's Code of Ordinances doesn't mention synthetic or artificial turf, and the city hasn't published whether a residential lawn conversion needs a permit. The Building Department (407-957-7243) can confirm for a specific job. The state's May 19, 2026 turf standard applies on any covered lot inside St. Cloud."),
                body, faqs=faqs, crumbs=CRUMBS_J, crumb="City of St. Cloud",
                sources=["dep-rule", "fs125572", ("City of St. Cloud — Permit Information", "https://stcloudfl.gov/50/Permit-Information"), ("Toho Water Authority — St. Cloud", "https://tohowater.com/st-cloud"), ("St. Cloud Code of Ordinances, Municode Library", "https://library.municode.com/fl/st._cloud/codes/code_of_ordinances"), OSCEOLA_PA],
                related=[crow("st-cloud"), corow("osceola"), HB683_ROUTE, RESIDENTIAL_ROUTE, HOA_ROUTE])


# ============================================================== Orange County
def orange_county():
    body = "".join([
        sec("What the Orange County code says",
            "<p>Orange County Code Chapter 24, Landscaping, Buffering and Open Space, defines \"turf, turf grass or sod\" as a mat of species such as Bahia, Bermuda, Centipede, Paspalum, St. Augustine and Zoysia, all of them living grass, and uses that definition to limit where lawn grass can go: not on landscape strips at least seven feet wide, and not inside interior vehicle-use areas. As of September 2026, we found no section in that chapter, or elsewhere in the county code, that uses the words synthetic turf or artificial turf.</p>"
            + "<p>Because that natural-grass definition is the only one on the books, a synthetic product doesn't technically meet or fail it either way. That's a gap in the published code, not a stated allowance, and it's worth confirming directly with the county before assuming either reading.</p>"),
        sec("What the state rule changed here",
            f"<p>Orange County's landscape code was written around living grass, so {src('dep-rule', 'Rule 62-308.100')} didn't have an existing synthetic-turf rule to override on May 19, 2026. What it did was set the outer limit on anything the county could write from here: no ban on compliant turf on a covered lot, no waterbody buffer stricter than what natural turf gets, and no permeability standard tighter than 10 inches an hour. Orange County keeps its usual authority over permitting, drainage review, rights-of-way, easements, larger lots and commercial or multi-family sites.</p>"),
        sec("What that means for a turf job in unincorporated Orange County, by our read",
            "<p>A residential conversion outside city limits isn't tripping a named synthetic-turf rule, since the code's turf definition only covers grass species. What it can still trip is the county's general landscape permitting, a plumbing permit for capped irrigation heads, or a drainage review near one of Orange County's many chain-of-lakes lots. This is a contractor's interpretation of a public ordinance, not a determination from county staff, so a call is worth more than this paragraph.</p>"
            + table("Orange County quick facts", ["Question", "Answer"],
                    [["Turf named in the code?", "No; \"turf\" is defined as natural grass species only"], ["Permit stated for residential turf?", "Not published either way"],
                     ["Department", "Orange County Permitting Services & Building Safety"], ["Phone", "407-836-5550"],
                     ["Portal", "Fast Track Online Services"], ["Property appraiser", "Orange County"]])),
        sec("Who to call, and where to apply",
            f"<p>Orange County's Permitting Services and Division of Building Safety, at 201 S. Rosalind Avenue in downtown Orlando, takes calls at 407-836-5550 and email at PermittingServices@ocfl.net. Applications and status checks run through {ext('https://fasttrack.ocfl.net/OnlineServices/', 'Fast Track Online Services')}.</p>"),
        sec("Checking your parcel",
            f"<p>Unincorporated Orange County wraps around Orlando and includes communities such as {city('hunters-creek', 'Hunters Creek')}, {city('meadow-woods', 'Meadow Woods')} and {city('lake-nona', 'Lake Nona')}, several of which sit close enough to city boundaries that an address alone won't settle it. Search the {ext(ORANGE_PA[1], ORANGE_PA[0])} to see the taxing jurisdiction on file; if the parcel comes back inside Orlando, {jlink('city-of-orlando', 'that page')} has the department you need instead.</p>"),
        sec("Water utility and irrigation",
            f"<p>Orange County Utilities runs a seasonal odd/even schedule: two days a week during daylight saving time and one day a week the rest of the year, with no watering between 10 a.m. and 4 p.m.; the Water Division takes questions at 407-254-9850. A handful of unincorporated pockets, including parts of Dr. Phillips and Horizon West, are billed by the Orlando Utilities Commission instead, which sets its own schedule, so check the bill before assuming which one applies. Either way, the state standard bars an in-ground system from watering a synthetic turf area once it's capped.</p>"),
        note("Read this as one contractor's summary of a public ordinance, not a legal opinion; Orange County's own staff should confirm anything a permit application depends on."),
    ])
    faqs = [
        faq("Does Orange County's seven-foot landscape-strip rule apply to synthetic turf?", "That rule is written for natural turf grass species and doesn't mention a synthetic product, so it's unclear whether it applies by analogy. Ask the Zoning division directly if your project involves a narrow landscape strip."),
        faq("Is unincorporated Orange County's rule the same as Orlando's?", "No, and that's the point of having two separate pages. Orlando's landscape code has specific artificial-turf language; the county's Chapter 24 does not, which changes both the written rule and the permit type involved."),
        faq("Do I need an engineering permit for a backyard turf lawn in the unincorporated county?", "Nothing published requires one for turf specifically outside city limits, unlike Orlando's code. General building or land-alteration permits can still apply depending on the scope of work."),
        faq("What if my property is served by OUC instead of Orange County Utilities?", "Then OUC's irrigation schedule, not the county's, controls until the turf area's heads are capped. Check ouc.com or a recent bill for the current days."),
    ]
    return page(jroute("orange-county"), "permit",
                "Artificial Turf Permits in Orange County, FL (2026)",
                "Does unincorporated Orange County require a permit for synthetic turf? What Chapter 24 says about \"turf,\" department contacts, checked September 2026.",
                "Artificial turf permits in Orange County",
                capsule("As of September 2026, Orange County Code Chapter 24 defines \"turf, turf grass or sod\" only as natural grass species and has no section on synthetic or artificial turf. Permitting Services (407-836-5550) can confirm whether a specific job needs review. The state's May 19, 2026 turf standard still applies on any covered lot in unincorporated Orange County."),
                body, faqs=faqs, crumbs=CRUMBS_J, crumb="Orange County",
                sources=["dep-rule", "fs125572", ("Orange County Code, Chapter 24, Municode Library", "https://library.municode.com/fl/orange_county/codes/code_of_ordinances?nodeId=PTIIORCOCO_CH24LABUOPSP"), ("Orange County Fast Track Online Services", "https://fasttrack.ocfl.net/OnlineServices/"), ("Orange County Utilities — watering restrictions", "https://www.orangecountyfl.net/watergarbagerecycling/wateringrestrictions.aspx"), ORANGE_PA],
                related=[corow("orange"), crow("hunters-creek"), crow("orlando", "Turf installers in Orlando"), HB683_ROUTE, RESIDENTIAL_ROUTE])


# ============================================================== City of Orlando
def orlando():
    body = "".join([
        sec("What the Orlando code says",
            "<p>Orlando is the one jurisdiction on this page with a code section built specifically for artificial turf. Search results point to an amendment covering Chapter 60 (Subdivision and Landscaping), Part 2 (Landscaping and Tree Protection), and Chapter 66 (Definitions) of the city's Land Development Code, titled to provide standards for installing and maintaining artificial turf. A direct fetch of Orlando's Municode pages failed twice during this research pass, so the specifics below come from a Florida city's public comparison of local artificial-turf ordinances, not from Orlando's code text itself, and should be confirmed with the city before you plan around them.</p>"
            + "<p>That comparison describes Orlando's rule this way: synthetic turf counts as impervious, because the landscape code only treats living material as pervious; the material has to look natural in color, with any other color needing sign-off from an Appearance Review Officer; it stays outside any tree's drip line; seams are nailed and glued, edges anchored against wind, and a solid barrier such as a mow strip separates turf from living beds; it can't go within 50 feet of any water body, inside a drainage feature, inside a Historic Preservation District, or inside a public or private right-of-way; and plain plastic or nylon carpeting doesn't qualify as artificial turf. It's allowed on residential lots, private parks, schools, commercial sites and limited park play areas, and it requires an Engineering Permit with a signed survey, dimensioned placement, impervious-surface-ratio math and an erosion-control statement.</p>"),
        sec("What the state rule changed here",
            f"<p>This is the page where {src('dep-rule', 'Rule 62-308.100')} does the most work. On a single-family lot of an acre or less, the state standard requires turf on permeable backing over a pervious subgrade and caps any local permeability rule at 10 inches an hour, which means Orlando's blanket \"impervious\" classification, as described in that comparison, can't be applied to a compliant system on a covered lot anymore. The state's waterbody rule sets a 10-foot setback unless a local buffer already exists and caps that local buffer at whatever natural turf gets, which is hard to square with an artificial-turf-only 50-foot setback if Orlando's buffer for grass is shorter. And the state's drip-line rule carries a certified-arborist exception that the summarized city rule doesn't appear to include.</p>"
            + "<p>What the state rule leaves standing: keeping turf out of the right-of-way, out of drainage features and out of Historic Preservation Districts, because none of those fall inside the rule's scope. Whether Orlando has actually updated its ordinance language since May 2026 to match, we could not confirm, which is exactly why this section is our reading of a conflict, not a report that the city has changed anything.</p>"),
        sec("What that means for a turf job in Orlando, as we read it",
            "<p>Plan on an Engineering Permit application either way, since that part of Orlando's process isn't something the state rule touches. Where the state and city rules appear to disagree, on the impervious classification and the 50-foot waterbody setback, bring both sets of numbers to the pre-application conversation and ask which one the reviewer is applying to a covered single-family lot in September 2026. This section is a contractor's analysis of a conflict between two sources, not a promise about how a specific reviewer will rule.</p>"
            + table("Orlando quick facts", ["Question", "Answer"],
                    [["Turf named in the code?", "Yes, in Chapter 60, Part 2 and Chapter 66 (per a secondary source)"], ["Permit stated for residential turf?", "Yes, an Engineering Permit, per that source"],
                     ["Old local classification", "Impervious, unless the code has since changed"], ["Department", "Orlando Permitting Services Division"],
                     ["Phone", "407-246-2121"], ["Property appraiser", "Orange County"]])),
        sec("Who to call, and where to apply",
            f"<p>Orlando's Permitting Services Division, at 400 S. Orange Avenue, answers general questions at 407-246-2121. Applications and plan tracking run through the {ext('https://digitalpermits.orlando.gov/', 'Orlando Permitting Portal')}, and permit lookup and inspection scheduling run through a separate {ext('https://permitlookup.cityoforlando.net/WebPermits/', 'WebPermits lookup tool')}.</p>"),
        sec("Checking your parcel",
            f"<p>Orlando's city limits aren't a simple ring, and several neighborhoods that feel like Orlando, including parts near {city('lake-nona', 'Lake Nona')}, sit in unincorporated Orange County instead. Confirm which one applies to a specific address on the {ext(ORANGE_PA[1], ORANGE_PA[0])}; if the parcel is unincorporated, {jlink('orange-county', 'the county page')} has the office that actually handles it.</p>"),
        sec("Water utility and irrigation",
            f"<p>Orlando Utilities Commission (OUC) supplies water to most of the city, on a schedule it sets independently of Orange County Utilities. We couldn't confirm OUC's current specific irrigation days within this research pass, so check a recent bill or {ext('https://www.ouc.com/about/water-services/', 'OUC’s water services page')} for the number in force. Whatever it is, it stops mattering for a turf area once the in-ground heads are capped, which {src('dep-rule', 'the state standard')} requires.</p>"),
        note("The artificial-turf specifics here come from a secondary comparison of city ordinances, not a live read of Orlando's own code, so verify current requirements with Permitting Services before finalizing a design."),
    ])
    faqs = [
        faq("Does Orlando really require an engineering permit for a backyard lawn?", "A comparison of Florida artificial-turf ordinances describes Orlando's process that way, including a signed survey and impervious-surface-ratio calculations. We couldn't independently confirm the current version of that requirement in this research pass, so ask Permitting Services to walk through what a residential lawn conversion needs today."),
        faq("Can Orlando still ban turf within 50 feet of a lake?", "The state standard only guarantees a 10-foot setback and caps any stricter local buffer at whatever natural grass gets, so a flat 50-foot synthetic-only setback is questionable on a covered lot as of May 2026; how Orlando applies it in practice is a question for the city, not something we can settle here."),
        faq("Does the Historic Preservation District rule still apply?", "Likely yes. The state rule doesn't cover historic-district design review, so a described ban on artificial turf inside those districts falls outside what Rule 62-308.100 preempts."),
        faq("What about a rooftop or commercial installation in Orlando?", "The rule described in the comparison document allows turf on commercial sites and limited park play areas, and neither the state rule nor its preemption reaches commercial or multi-family property at all, so Orlando's own standards control those projects without a state floor underneath them."),
    ]
    return page(jroute("city-of-orlando"), "permit",
                "Artificial Turf Permits in Orlando, FL (2026)",
                "Orlando has a specific artificial-turf code section requiring an engineering permit. What it says, what the 2026 state rule overrides, and who to call.",
                "Artificial turf permits in the City of Orlando",
                capsule("Orlando's Land Development Code, unlike the other seven offices on this page, has specific artificial-turf standards in Chapter 60 and Chapter 66, including an Engineering Permit and, as described in a secondary source checked September 2026, an impervious-surface classification and a 50-foot waterbody setback. Florida's May 19, 2026 turf standard now overrides parts of that on covered single-family lots."),
                body, faqs=faqs, crumbs=CRUMBS_J, crumb="City of Orlando",
                sources=["dep-rule", "fs125572", ("City of Orlando Land Development Code, Chapter 60, Municode Library", "https://library.municode.com/fl/orlando/codes/code_of_ordinances?nodeId=TITIICICO_CH60SULA"), ("City of Belle Isle, FL — comparison of local Florida artificial turf ordinances", "https://www.belleislefl.gov/sites/default/files/fileattachments/community/page/9922/artificial_turf_comparisons_of_local_florida_ordinances_-_sheet1.pdf"), ("Orlando Permitting Services Division", "https://www.orlando.gov/Our-Government/Departments-Offices/Economic-Development/Permitting-Services"), ORANGE_PA],
                related=[crow("orlando"), corow("orange"), HB683_ROUTE, RESIDENTIAL_ROUTE, HOA_ROUTE])


# ============================================================== Polk County
def polk():
    body = "".join([
        sec("What the Polk County code says",
            "<p>As of September 2026, Polk County's Land Development Code, available through Municode, has no section addressing synthetic or artificial turf. The code's landscaping and buffer standards, like most of the counties on this page, are written for planted material and don't define a manufactured alternative.</p>"
            + "<p>Polk County's Building Division site doesn't carry a turf-specific page or handout either, from what's published. Until the county writes something, the state rule is the only synthetic-turf-specific standard reaching a Polk County lot.</p>"),
        sec("What the state rule changed here",
            f"<p>Polk County didn't have a turf ordinance for {src('dep-rule', 'Rule 62-308.100')} to conflict with, so the practical change is about the ceiling going forward: no ban on compliant turf on a covered single-family lot of an acre or less, no permeability rule tighter than 10 inches an hour, and no waterbody buffer stricter than natural grass gets. Polk County keeps its regular say over permits, land alteration, drainage and anything outside the rule's one-acre, single-family scope.</p>"),
        sec("What that means for a turf job in Polk County, in our view",
            "<p>A lawn conversion in unincorporated Polk County, from Davenport down through the ridge towns, isn't running into a written synthetic-turf rule, since none exists yet. It can still meet the county's usual building or land-alteration permitting, a plumbing permit if irrigation heads are capped, or a review near a lake, which Polk County has plenty of. This paragraph reflects what a turf crew runs into, not a determination the county has issued.</p>"
            + table("Polk County quick facts", ["Question", "Answer"],
                    [["Turf named in the code?", "No, as of September 2026."], ["Permit stated for residential turf?", "Not published either way."],
                     ["Department", "Polk County Building Division"], ["Phone", "863-534-6080"],
                     ["Portal", "Polk County Citizen Access (Accela)"], ["Property appraiser", "Polk County"]])),
        sec("Who to call, and where to apply",
            f"<p>Polk County's Building Division, at 330 W. Church Street in Bartow, takes permit questions at 863-534-6080. Applications go through {ext('https://www.polkfl.gov/services/building/permitting/', 'the county’s Citizen Access portal')}, built on Accela.</p>"),
        sec("Checking your parcel",
            f"<p>Polk County's northern edge, around Davenport, Haines City and Auburndale, is the part of the county inside our service area, and a handful of those addresses are inside a city limit rather than unincorporated county land. Confirm the taxing jurisdiction on the {ext(POLK_PA[1], POLK_PA[0])} before assuming which building department to call.</p>"),
        sec("Water utility and irrigation",
            f"<p>Polk County Utilities has been on an emergency once-a-week watering schedule since February 2026, under a Southwest Florida Water Management District Phase III shortage order, with hours limited to 12:01-4 a.m. or 8-11:59 p.m. and the day assigned by the last digit of the address. Emergency orders change without much notice, so check {ext('https://www.polkfl.gov/services/utilities/water-restrictions/', 'the county’s current watering-restrictions page')} rather than treating this as permanent. A capped synthetic turf area sidesteps the schedule entirely under {src('dep-rule', 'the state standard')}.</p>"),
        note("A local installer put this together from Polk County's public code and website, not from the Building Division's legal staff, so a call is worth more than this paragraph for anything load-bearing."),
    ])
    faqs = [
        faq("Does the SWFWMD water shortage order affect a synthetic turf lawn?", "No, once the irrigation heads under it are capped, because the state standard already bars watering synthetic turf from an in-ground system regardless of any shortage order. The order affects whatever grass or beds remain."),
        faq("Is a permit needed just to cap irrigation heads under future turf in Polk County?", "Nothing published carves out an exception for a small capping job, so it's worth asking the Building Division whether your specific scope needs a plumbing permit before work starts."),
        faq("Do Polk County cities like Lakeland or Winter Haven have their own turf rules?", "Those are separate municipalities with their own codes, outside the unincorporated county page here. Check with each city's own building department directly; we haven't researched every Polk County city individually."),
        faq("What if my Polk County lot is bigger than one acre?", "Then the state's synthetic-turf standard doesn't apply to it at all, and Polk County's own land development code, unchanged by the 2026 rule, governs the property on its own."),
        faq("Does Polk County require proof the turf meets the state's material standard?", "Nothing published says the county checks for a PFAS or heavy-metal statement at permit time, but keeping the manufacturer's paperwork with the job file is cheap insurance if a reviewer or an inspector ever asks."),
    ]
    return page(jroute("polk-county"), "permit",
                "Artificial Turf Permits in Polk County, FL (2026)",
                "Does unincorporated Polk County require a permit for synthetic turf? Code findings, the 2026 water-shortage order, and department contacts.",
                "Artificial turf permits in Polk County",
                capsule("As of September 2026, Polk County's Land Development Code doesn't mention synthetic or artificial turf, and the county hasn't published a permit answer for a residential lawn conversion. The Building Division (863-534-6080) can confirm for a specific address. Florida's May 19, 2026 turf standard applies on any covered lot in unincorporated Polk County."),
                body, faqs=faqs, crumbs=CRUMBS_J, crumb="Polk County",
                sources=["dep-rule", "fs125572", ("Polk County Land Development Code, Municode Library", "https://library.municode.com/fl/polk_county/codes/land_development_code"), ("Polk County Building permitting", "https://www.polkfl.gov/services/building/permitting/"), ("Polk County water restrictions", "https://www.polkfl.gov/services/utilities/water-restrictions/"), POLK_PA],
                related=[corow("polk"), crow("davenport"), crow("haines-city"), HB683_ROUTE, RESIDENTIAL_ROUTE])


# ============================================================== Lake County
def lake():
    body = "".join([
        sec("What the Lake County code says",
            "<p>As of September 2026, we found no mention of synthetic or artificial turf in Lake County's Land Development Regulations. The county's landscaping standards address planted buffers, tree preservation and open space in terms of living vegetation, and don't reference a manufactured surface.</p>"
            + "<p>Lake County's Building Services pages don't publish a turf handout either, based on a search of the site. Absent that, the state standard is the only turf-specific rule that currently reaches a Lake County property.</p>"),
        sec("What the state rule changed here",
            f"<p>Lake County's regulations predate {src('dep-rule', 'the state’s turf rule')} and never needed turf-specific language for the May 19, 2026 preemption to bind the county. From that date, Lake County can't ban compliant synthetic turf on a covered single-family lot of an acre or less, can't hold it to a waterbody buffer stricter than natural grass gets, and can't set a permeability standard under 10 inches an hour. The county otherwise keeps its usual permitting, drainage and zoning authority.</p>"),
        sec("What that means for a turf job in Lake County, as we understand it",
            "<p>A lawn conversion around Clermont, Minneola or the unincorporated county in between isn't up against a written synthetic-turf ordinance, because the search turned up nothing to cite. County permitting for exterior work, a plumbing permit for capped heads, or a review on one of Lake County's many hilltop or lakefront lots can still apply on their own terms. This is a contractor's take on a quiet code, not a statement from the county.</p>"
            + table("Lake County quick facts", ["Question", "Answer"],
                    [["Turf named in the regulations?", "No, as of September 2026."], ["Permit stated for residential turf?", "Not published either way."],
                     ["Department", "Lake County Building Services"], ["Phone", "352-343-9653"],
                     ["Portal", "Accela-based citizen access"], ["Property appraiser", "Lake County"]])),
        sec("Who to call, and where to apply",
            f"<p>Lake County Building Services, at 315 W. Main Street in Tavares, answers permit questions at 352-343-9653, with inspection scheduling handled at 352-343-9734. Details on filing are on the county's {ext('https://www.lakecountyfl.gov/building-services/permitting-information', 'permitting information page')}.</p>"),
        sec("Checking your parcel",
            f"<p>Lake County's south end, near Clermont and Minneola, has grown fast enough that city and county lines get crossed often on the same street. Search an address on the {ext(LAKE_PA[1], LAKE_PA[0])} to see which one has the parcel before calling a building department.</p>"),
        sec("Water utility and irrigation",
            f"<p>Most of Lake County falls under the St. Johns River Water Management District, which runs two watering days a week during daylight saving months and one day a week in winter by address parity, and which declared a Phase III emergency shortage in 2026 that tightened those numbers further ({ext('https://www.sjrwmd.com/wateringrestrictions/', 'SJRWMD’s current restrictions page')}). Some cities, including Clermont and Minneola, run their own water utility with a schedule that can differ from the district's default, so check the local bill. A capped synthetic turf area is exempt from either schedule once the heads underneath it are disconnected.</p>"),
        note("This page reflects what we could find published as of September 2026 and isn't a determination from Lake County; verify anything a permit depends on with Building Services."),
    ])
    faqs = [
        faq("Does Lake County treat hillside lots near Clermont differently for turf?", "Nothing published sets a slope-specific turf rule. A steep lot can still trigger the county's general grading or erosion-control review regardless of what surface goes down."),
        faq("Is Lake County split between two water management districts?", "Yes, roughly: most of the county answers to the St. Johns River Water Management District, while a western sliver falls under a different district. Which one applies to a specific address is worth confirming with the county or the district directly."),
        faq("Do I need county approval if my lot is in a Lake County city instead?", "No, cities like Clermont, Minneola and Mount Dora run their own permitting separate from the county. This page only covers unincorporated Lake County; check the specific city's building department for a job inside its limits."),
        faq("What if my property backs onto a spring-fed lake?", "The state's 10-foot waterbody setback and its ban on turf inside a pond's littoral zone apply the same way they would on any other lake, and Lake County's own code doesn't appear to add a stricter number as of September 2026."),
    ]
    return page(jroute("lake-county"), "permit",
                "Artificial Turf Permits in Lake County, FL (2026)",
                "Does unincorporated Lake County require a permit for synthetic turf? Code findings, water district rules, and Building Services contacts.",
                "Artificial turf permits in Lake County",
                capsule("As of September 2026, Lake County's Land Development Regulations don't mention synthetic or artificial turf, and the county hasn't published a permit answer for a residential lawn conversion. Building Services (352-343-9653) can confirm for a specific address. Florida's May 19, 2026 turf standard applies on any covered lot in unincorporated Lake County."),
                body, faqs=faqs, crumbs=CRUMBS_J, crumb="Lake County",
                sources=["dep-rule", "fs125572", ("Lake County Building Services — permitting information", "https://www.lakecountyfl.gov/building-services/permitting-information"), ("St. Johns River Water Management District — watering restrictions", "https://www.sjrwmd.com/wateringrestrictions/"), LAKE_PA],
                related=[corow("lake"), crow("clermont"), crow("minneola"), HB683_ROUTE, RESIDENTIAL_ROUTE])


# ============================================================== Seminole County
def seminole():
    body = "".join([
        sec("What the Seminole County code says",
            "<p>As of September 2026, Seminole County's Land Development Code, indexed on Municode, has no section on synthetic or artificial turf. Its landscaping provisions cover buffers, tree protection and required plant material without a corresponding rule for a manufactured surface.</p>"
            + "<p>Seminole County's Development Services site doesn't post a turf-specific handout either, from what we could find. That leaves the state standard as the only turf-specific rule currently reaching a Seminole County lot.</p>"),
        sec("What the state rule changed here",
            f"<p>Seminole County answers to the same May 19, 2026 deadline as the rest of the state under {src('dep-rule', 'Rule 62-308.100')}, whether or not its code has ever used the words synthetic turf. On a single-family lot of an acre or less, the county can't ban a compliant installation, can't apply a waterbody buffer tougher than natural grass gets, and can't set a permeability figure under 10 inches an hour. It keeps ordinary control over permits, drainage review, easements and anything the one-acre single-family scope doesn't reach.</p>"),
        sec("What that means for a turf job in Seminole County, from where we sit",
            "<p>A backyard or front-yard project in unincorporated Seminole County, near Geneva or the rural stretches outside the cities, isn't running into a named synthetic-turf ordinance, because there isn't one. County permitting for exterior alterations, a plumbing permit for capped irrigation heads, or a stormwater review near one of Seminole's many spring-fed lakes can still come into play. We build lawns here; we don't write county code, so this is a working read of a quiet ordinance, not a promise about how a reviewer treats a specific lot.</p>"
            + table("Seminole County quick facts", ["Question", "Answer"],
                    [["Turf named in the code?", "No, as of September 2026."], ["Permit stated for residential turf?", "Not published either way."],
                     ["Department", "Seminole County Building Division"], ["Phone", "407-665-7050"],
                     ["Portal", "Building Permits Online / Click2Gov"], ["Property appraiser", "Seminole County"]])),
        sec("Who to call, and where to apply",
            f"<p>Seminole County's Building Division, at 1101 E. First Street in Sanford, takes calls at 407-665-7050 and email at bpcustomerservice@seminolecountyfl.gov. Filing and inspection scheduling run through the county's {ext('https://www.seminolecountyfl.gov/departments-services/development-services/building/building-permitting', 'online building permitting system')}.</p>"),
        sec("Checking your parcel",
            f"<p>Seminole County is small enough that most of its area sits inside one city or another, from Sanford down to Altamonte Springs, so unincorporated pockets are the exception rather than the rule. Confirm a specific address on the {ext(SEM_PA[1], SEM_PA[0])} before assuming the county, rather than a city, has jurisdiction.</p>"),
        sec("Water utility and irrigation",
            f"<p>Most of Seminole County falls under the St. Johns River Water Management District's seasonal schedule, two days a week in daylight saving months and one day a week in winter, currently tightened under a 2026 Phase III shortage declaration ({ext('https://www.sjrwmd.com/wateringrestrictions/', 'SJRWMD’s restrictions page')}). Most Seminole cities, including Sanford, Altamonte Springs, Casselberry, Oviedo, Winter Springs and Longwood, bill their own water and can set their own schedule on top of that, so a resident's actual watering days come from the local utility bill, not the district alone. None of that reaches a synthetic turf area once its irrigation heads are capped under {src('dep-rule', 'the state standard')}.</p>"),
        note("We're turf installers describing a public code, not Seminole County staff, so confirm anything a permit application depends on with the Building Division."),
    ])
    faqs = [
        faq("Is unincorporated Seminole County land hard to find?", "It's limited; most of the county sits inside a city. If your address is in Sanford, Altamonte Springs, Casselberry, Oviedo, Winter Springs or Longwood, that city's own building department, not the county, handles the permit."),
        faq("Does Seminole County's spring-fed geography add to the waterbody setback?", "Nothing published sets a Seminole-specific number beyond the state's 10-foot rule and its littoral-zone exclusion for ponds, so plan around the state figures unless the county tells you otherwise."),
        faq("Do I need a tree permit before removing sod near an oak in Seminole County?", "Seminole County has its own tree-protection rules separate from the turf question, and a live oak near the work area can trigger a tree permit regardless of what surface replaces the grass. Ask Building Services or the county's tree-protection staff before removing anything near the trunk."),
        faq("What if my HOA in a Seminole County community pre-dates 2023?", "Age doesn't exempt it automatically. F.S. 720.3045 applies to the association's current declaration, and our HOA page covers how that plays out for an older set of covenants."),
    ]
    return page(jroute("seminole-county"), "permit",
                "Artificial Turf Permits in Seminole County, FL (2026)",
                "Does unincorporated Seminole County require a permit for synthetic turf? Code findings, water district rules, and Building Division contacts.",
                "Artificial turf permits in Seminole County",
                capsule("As of September 2026, Seminole County's Land Development Code doesn't mention synthetic or artificial turf, and the county hasn't published a permit answer for a residential lawn conversion. The Building Division (407-665-7050) can confirm for a specific address. Florida's May 19, 2026 turf standard applies on any covered lot in unincorporated Seminole County."),
                body, faqs=faqs, crumbs=CRUMBS_J, crumb="Seminole County",
                sources=["dep-rule", "fs125572", "fs7203045", ("Seminole County building permitting", "https://www.seminolecountyfl.gov/departments-services/development-services/building/building-permitting"), ("St. Johns River Water Management District — watering restrictions", "https://www.sjrwmd.com/wateringrestrictions/"), SEM_PA],
                related=[corow("seminole"), crow("altamonte-springs"), crow("oviedo"), HB683_ROUTE, RESIDENTIAL_ROUTE])


def get_pages():
    return [hub(), kissimmee(), osceola(), st_cloud(), orange_county(), orlando(), polk(), lake(), seminole()]
