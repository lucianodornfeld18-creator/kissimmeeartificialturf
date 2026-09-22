# -*- coding: utf-8 -*-
"""Maitland, FL (tier 2). Researched September 2026: City of Maitland Community Development permitting
(itsmymaitland.com), the city's own Water Production/Distribution division, the Land Development Code
on Municode (recodified under Ordinance No. 1434, adopted October 14, 2024), the city's own lake and
history pages, U.S. Census QuickFacts, and USDA official series descriptions for the Candler and Apopka
ridge soils (same complex documented for neighboring Winter Park). Orange County permit, water and soil
facts are reused from c_permits.py and c_counties.py (facts and URLs, not sentences)."""
from _data import CITIES
from _helpers import page, capsule, sec, table, faq, a, svc, city, post, src, ext, price
from _cityservice import cityservice_pages

SLUG = "maitland"
MILES = CITIES[SLUG]["miles"]

MT_PERMIT = ("City of Maitland — Permit Applications, Community Development", "https://www.itsmymaitland.com/428/Permit-Applications")
MT_PORTAL = ("City of Maitland — online permitting (EnerGov)", "https://maitlandfl-energovpub.tylerhost.net/")
MT_WATER = ("City of Maitland — Water Production / Distribution", "https://www.itsmymaitland.com/225/Water-Production-Distribution")
MT_ABOUT = ("City of Maitland — About Maitland", "https://www.itsmymaitland.com/339/About-Maitland")
MT_LDC = ("Maitland Land Development Code, Municode Library (Ordinance No. 1434, adopted Oct. 14, 2024)", "https://library.municode.com/fl/maitland/codes/land_development_code")
MT_CENSUS = ("U.S. Census Bureau QuickFacts — Maitland city, Florida", "https://www.census.gov/quickfacts/maitlandcityflorida")
CANDLER_OSD = ("USDA NRCS — official series description, Candler series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/C/CANDLER.html")
APOPKA_OSD = ("USDA NRCS — official series description, Apopka series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/A/APOPKA.html")
ORANGE_PA = ("Orange County Property Appraiser — parcel search", "https://ocpafl.org/")
OC_PERMIT = ("Orange County Permitting Services & Building Safety, Fast Track Online Services", "https://fasttrack.ocfl.net/OnlineServices/")
OC_CH24 = ("Orange County Code, Chapter 24, Municode Library", "https://library.municode.com/fl/orange_county/codes/code_of_ordinances?nodeId=PTIIORCOCO_CH24LABUOPSP")
SJRWMD_RESTRICT = ("St. Johns River Water Management District — watering restrictions", "https://www.sjrwmd.com/wateringrestrictions/")

SRC = ["dep-rule", "fs125572", "hb683", "fs7203045", "usda-wss", "census-acs",
       MT_PERMIT, MT_PORTAL, MT_WATER, MT_ABOUT, MT_LDC, MT_CENSUS,
       CANDLER_OSD, APOPKA_OSD, ORANGE_PA, OC_PERMIT, OC_CH24, SJRWMD_RESTRICT]

# ============================================================== hub
HUB = page(
    "/areas/maitland/", "city",
    "Artificial Turf in Maitland, FL (2026 Guide)",
    "Synthetic turf installation, city permits, the seven-lake system and mid-century lots in Maitland, FL, a Central Florida town checked September 2026.",
    "Turf installation and local rules for Maitland, FL",
    capsule(f"About {MILES} miles from downtown Kissimmee, Maitland prices a lawn conversion at the same {price('residential')} a square foot as the rest of Central Florida, as of September 2026. The city runs its own water utility rather than buying through a district, and it rewrote its entire Land Development Code in October 2024 without adding a section for synthetic turf."),
    "".join([
        sec("A city that just rewrote its zoning book, minus a turf section",
            f"<p>Maitland's Community Development Department takes permit questions at {ext(MT_PERMIT[1], '(407) 539-6150')} from an office at 1776 Independence Lane, and applications run through the city's own {ext(MT_PORTAL[1], 'EnerGov online permitting system')}. The city recodified its entire {ext(MT_LDC[1], 'Land Development Code')} under Ordinance No. 1434, adopted October 14, 2024, a full rewrite rather than a patch. As of September 2026, that current code has no section naming synthetic or artificial turf, so a Maitland lawn conversion answers to the state's standard first and the city's ordinary building and drainage review second, not to a Maitland-specific turf rule the way a project in neighboring {city('winter-park', 'Winter Park')} might.</p>"
            + f"<p>Because Maitland runs its own permitting separate from unincorporated Orange County, our {a('/laws/permits/orange-county/', 'Orange County permit page')} describes the county's rules, not the city's; it's the closest reference on this site until a dedicated Maitland page exists. A parcel search on the {ext(ORANGE_PA[1], 'Orange County Property Appraiser')} confirms whether a specific address is inside Maitland's limits at all, since the city's boundary runs an irregular line against unincorporated pockets on its edges.</p>"),
        sec("Water from six wells, not a shared pipe",
            f"<p>Maitland treats and distributes its own water rather than buying it wholesale, drawing from three treatment plants and six groundwater wells across more than 70 miles of city-owned piping, according to the city's own {ext(MT_WATER[1], 'Water Production and Distribution page')}. That's different from a city that resells water from a regional utility, and it means Maitland's own office, not a district or a neighboring utility, is the first call for a watering-schedule question. The city sits within the St. Johns River Water Management District's territory along with most of Orange County, and the district's {ext(SJRWMD_RESTRICT[1], 'current restriction order')} sets the baseline days a Maitland account still has to follow for whatever lawn stays green, capped turf areas excepted under the state's May 2026 standard.</p>"),
        sec("Seven small lakes and a canal to the chain next door",
            f"<p>Maitland holds seven lakes inside its limits, Lake Maitland the largest at roughly 451 acres, followed by Lake Sybelia at about 76 acres, with Lake Lily, Lake Catherine, Lake Charity, Lake Faith and Lake Hope rounding out the list. A canal connects Lake Maitland north into the Winter Park Chain of Lakes, which is how the two cities share a single connected water system despite being separate jurisdictions. Turf on any of those shorelines has to keep 10 feet of clearance from open water under the state's turf standard, a line that moves right up to the property edge wherever a seawall or bulkhead already does the job a natural bank would otherwise need to do.</p>"),
        sec("Martin Marietta, Maitland Center, and the lots in between",
            f"<p>Maitland's population grew fastest after Martin Marietta relocated its aerospace operations from Baltimore to Orlando in the 1950s, moving employees in by the hundreds and filling in subdivisions across the city through the 1960s and 1970s; a further twelve residential subdivisions went in between 1972 and 1979 alone, per the city's own {ext(MT_ABOUT[1], 'history page')}. Late in the 1970s, 226 acres west of Interstate 4 became Maitland Center, now home to dozens of office buildings, while the residential streets around the seven lakes stayed largely as they were built, mid-century homes on lots wide enough to carry mature landscaping.</p>"
            + f"<p>The city's population held close to 19,543 at the 2020 census, per {ext(MT_CENSUS[1], 'Census Bureau figures')}, essentially flat since. Homes here skew toward the 1970s and 80s, with larger interiors and bigger lots than the newer, denser construction filling in parts of {city('altamonte-springs', 'Altamonte Springs')} or {city('winter-springs', 'Winter Springs')} to the north.</p>"),
        sec("The same ridge sand as Winter Park, without the same ordinance",
            f"<p>USDA maps Maitland to the same central Orange County ridge complex as Winter Park next door: {ext(CANDLER_OSD[1], 'Candler and Apopka series soils')}, excessively to well drained sand built from thick wind-blown and marine deposits, a different profile than the wetter flatwoods soil common around Kissimmee. Fast drainage through the native ground doesn't replace a compacted base; a washed crushed-rock layer is still what keeps a lawn's surface level under years of foot traffic, regardless of how quickly the sand underneath moves water on its own.</p>"),
        "<!--AUTO:city-services-->",
    ]),
    faqs=[
        faq("Does Maitland have a turf-specific rule like some nearby cities?",
            "Not as of September 2026, based on a search of the current Land Development Code, recodified under Ordinance No. 1434 in October 2024. That leaves the state's May 2026 standard as the only synthetic-turf-specific rule reaching a Maitland lot, alongside the city's ordinary building and drainage permitting."),
        faq("Is Maitland's water utility the same one that serves Winter Park or Orlando?",
            "No. Maitland treats and distributes its own water from city-owned wells and plants, separate from Winter Park's utility and from Orlando Utilities Commission, though both cities answer to the same St. Johns River Water Management District restrictions for whatever isn't capped synthetic turf."),
        faq("Which lake sets the waterbody setback if my lot backs onto a canal between two of Maitland's lakes?",
            "The state's 10-foot rule applies to the canal the same way it applies to the lake itself, since the standard covers any natural or man-made waterbody, not just the named lakes. A seawall or bulkhead along the canal bank is what triggers the exception."),
        faq("Do Maitland's older, mid-century lots need special handling for a turf conversion?",
            "Not because of their age specifically, though a lot from the 1970s often carries decades-old landscaping and irrigation zones that a newer install has to work around. Confirming what's actually buried in the yard before excavation starts matters more on an older lot than a newly platted one."),
        faq("What should the best synthetic grass company near you in Maitland already ask before quoting?",
            "Whether the yard backs onto one of the seven lakes or the canal to Winter Park, since that raises the setback question, and whether the address is actually inside city limits or a bordering unincorporated pocket, since that changes which office reviews the permit. A bid that skips both questions hasn't looked at the property closely."),
    ],
    sources=SRC, crumbs=[("Service areas", "/areas/")], crumb="Maitland", city=SLUG,
    related=[("/areas/orange-county/", "Artificial turf in Orange County"), ("/laws/permits/orange-county/", "Orange County permit rules (Maitland runs its own code)"),
             ("/areas/winter-park/", "Artificial turf in Winter Park"), ("/areas/altamonte-springs/", "Artificial turf in Altamonte Springs"), ("/artificial-turf-cost/", "Full turf cost guide")])

# ============================================================== local (city x service)
LOCAL = {
    "residential": {
        "title": "Artificial Grass Installation in Maitland, FL",
        "meta": "Artificial grass installation in Maitland, FL runs $8–$18 per sq ft. What a rewritten 2024 city code and mid-century lots near seven lakes mean for a lawn.",
        "h1": "Converting a Maitland lawn to synthetic turf",
        "lede": capsule(f"A residential lawn conversion in Maitland runs {price('residential')} per square foot installed as of September 2026, most jobs between {price('residential', True)}. The city's own Land Development Code, rewritten in October 2024, still doesn't name synthetic turf, which leaves the state's May 2026 standard as the operative rule for most of what a crew runs into here."),
        "sections": [
            ("A rewritten code that skipped turf entirely",
             f"<p>Maitland's Community Development Department reviews exterior work under a Land Development Code recodified from the ground up in October 2024, and a search of that current code turns up no section addressing synthetic or artificial turf specifically. That's a different situation from a city that once had an old turf rule and is now squaring it against the state standard; Maitland's rulebook simply never wrote one, so a residential conversion here answers to {a('/laws/florida-hb-683/', 'Rule 62-308.100')} directly, plus whatever ordinary drainage or grading review the city applies to any exterior alteration.</p>"),
            ("Mid-century lots built for bigger yards",
             f"<p>Homes going up through the 1970s and into the 1980s here tended toward larger lots than the infill built more recently in parts of {city('winter-springs', 'Winter Springs')} or {city('casselberry', 'Casselberry')}, which usually means more open lawn to work with and fewer of the narrow side-yard constraints that shape a job in an older, denser town. What that older construction can carry instead is decades of landscaping changes and buried irrigation zones from past owners, which a crew has to map before excavation starts rather than assume from the current layout.</p>"),
            ("The same ridge soil, a different water source",
             f"<p>{ext(CANDLER_OSD[1], 'Candler and Apopka series sand')} sits under most of Maitland the same way it does under Winter Park, draining fast on its own but still needing a washed crushed-rock base to hold the surface level. Because Maitland runs its own water utility instead of buying through OUC or a county system, capping the in-ground heads under a new lawn is a step the city's own Water Production and Distribution division can confirm directly, rather than routing the question through a regional provider.</p>"),
        ],
        "scenario": ("A 1970s ranch home near Lake Sybelia",
                     f"<p>Say you have a 540 sq ft backyard behind a 1976 ranch home two streets from Lake Sybelia, flat and open with an old irrigation zone running through the middle of it that the current owner inherited from the house's original build. At {price('residential', True)} per square foot, that lawn prices around $5,400 to $8,640 installed, with capping the buried zone's heads a small add rather than a separate project.</p>"
                     + f"<p>A similar-sized yard near {city('altamonte-springs', 'Altamonte Springs')} or {city('longwood', 'Longwood')} prices the same way; what changes the bid here is whatever the old irrigation layout adds to the prep work, not the town's name.</p>"),
        "faqs": [
            faq("Since Maitland's code doesn't mention turf, is a permit still required?",
                "Ordinary building and land-alteration permitting still applies to exterior work even without a turf-specific rule, and capping irrigation heads can need its own plumbing permit. Confirm the current requirement for a specific scope with Community Development at (407) 539-6150."),
            faq("Do older Maitland lots near Martin Marietta-era subdivisions have unusual soil to plan around?",
                "Not unusually so. The same Candler and Apopka ridge sand common across this part of Orange County sits under most of the city's mid-century subdivisions, and the base build doesn't change based on when a lot was platted."),
        ],
        "sources": SRC,
    },
    "pet": {
        "title": "Pet Turf & Dog Runs in Maitland, FL",
        "meta": "Pet turf and dog run installation in Maitland, FL runs $10–$18 per sq ft. Fenced backyards near the city's seven lakes and canals.",
        "h1": "Pet turf for fenced Maitland backyards",
        "lede": capsule(f"Pet turf in Maitland runs {price('pet')} per square foot as of September 2026, typically {price('pet', True)}. Most dog runs here go into a fenced backyard on one of the city's mid-century subdivisions, several of them a short walk from one of Maitland's seven lakes."),
        "sections": [
            ("Fenced yards from an era before dog parks were common",
             f"<p>Subdivisions built through the 1960s and 70s here were laid out with full backyard fencing as standard, unlike some newer developments where a shared amenity space substitutes for a private yard. That gives a dog run more room to work with than a zero-lot-line yard elsewhere in our service area, though older wood or chain-link fencing sometimes needs a look before a crew commits to where the run's flush-out zone drains.</p>"),
            ("Canal-adjacent runs and the setback that comes with them",
             f"<p>A dog run planned near one of the canals connecting Maitland's lakes, or the canal running north toward Winter Park, answers to the same 10-foot minimum from open water that a full lawn does, with the usual carve-out once a seawall or bulkhead is already doing the work of a bank. Staking that buildable line before ordering material matters just as much on a modest pet run as it does on a full yard.</p>"),
            ("Maitland's own water utility and a capped irrigation zone",
             f"<p>Because {svc('pet', 'a pet turf area')} never needs the in-ground system once its heads are capped, and Maitland's water utility bills and schedules independently of any neighboring city, a homeowner here deals with one office, not a district and a city both, when confirming that a capped zone is properly documented on the account.</p>"),
        ],
        "scenario": ("A dog run behind a fenced 1960s home",
                     f"<p>Say you have a 220 sq ft dog run planned for a fenced backyard in one of Maitland's older subdivisions, roughly 200 feet from a canal but with no direct waterfront frontage, so the setback rule doesn't apply. At {price('pet', True)} a square foot, that run costs about $2,640 to $3,520 installed, with a coated-sand infill adding a modest amount for odor control.</p>"
                     + f"<p>A run the same size directly on a lake or canal lot, inside the 10-foot line, would need the layout staked back from the water first, which a run set back from the shoreline like this one skips entirely.</p>"),
        "faqs": [
            faq("Does a Maitland dog run near a canal need the same 10-foot setback as a full lawn?",
                "Yes. The state's waterbody setback applies to any size of synthetic turf area, pet runs included, measured the same way from the ordinary or mean high water line."),
            faq("Who do I call to confirm Maitland's irrigation zones are properly capped after a pet turf install?",
                "The city's own Water Production and Distribution division, since Maitland doesn't buy water through OUC or a county utility and handles its own account records directly."),
        ],
        "sources": SRC,
    },
    "putting": {
        "title": "Backyard Putting Greens in Maitland, FL",
        "meta": "Backyard putting green installation in Maitland, FL runs $14–$30 per sq ft. Larger mid-century lots near Lake Sybelia fit a contoured green well.",
        "h1": "Putting greens on Maitland's larger lots",
        "lede": capsule(f"A backyard putting green in Maitland costs {price('putting')} per square foot as of September 2026, most landing between {price('putting', True)}. The larger lots built through the 1970s and 80s here, especially around Lake Sybelia and the interior lakes away from Interstate 4, tend to have the open, level backyard a contoured green actually needs."),
        "sections": [
            ("Why the city's older subdivisions suit a green",
             f"<p>A lot from Maitland's main growth period, the 1970s and 80s, typically runs wider and deeper than a lot platted in the decades since, leaving more usable backyard once the house and pool, if there is one, are accounted for. Searching for the best backyard putting green installer near you in Maitland usually turns up a similar answer regardless of which company you call: the lot itself, not the town's name, determines whether a contoured green fits.</p>"),
            ("Lakefront contouring and the setback that comes with it",
             f"<p>A green planned for a lot backing onto Lake Sybelia, Lake Maitland or one of the smaller interior lakes has to stake the state's 10-foot waterbody line before any contouring work starts, the same rule that applies to a plain lawn on the same lot. Losing a strip of buildable yard to that setback can shrink a planned green's footprint more than a homeowner expects going in, which is worth confirming with a site visit before ordering material.</p>"),
            ("Grading around decades of established landscaping",
             f"<p>A backyard that's carried the same mature landscaping since the 1970s or 80s sometimes has tree roots or old irrigation lines running exactly where a green's contours need to go, which a newer subdivision's yard usually doesn't have to work around. Locating what's buried before excavation starts avoids having to redesign the green's shape mid-project.</p>"),
        ],
        "scenario": ("A green on an oversized Lake Sybelia-area lot",
                     f"<p>Say you have a 500 sq ft green and fringe planned for a backyard two blocks from Lake Sybelia, with three cups and a three-foot fall built into the contour, clear of any waterfront setback. At {price('putting', True)} a square foot, that installs for roughly $9,000 to $12,500, with the contouring work pushing toward the top of that range given the grading involved.</p>"
                     + f"<p>A flatter green of the same footprint, without the contour work, would price closer to the bottom of the range, whether it's built in Maitland or in {city('winter-park', 'Winter Park')} next door.</p>"),
        "faqs": [
            faq("Do Maitland's older subdivisions typically have enough backyard depth for a putting green?",
                "Many do, since lots platted through the 1970s and 80s here run larger than more recent infill construction elsewhere in the county. A site visit confirms whether a specific yard has the flat run a contoured green needs."),
            faq("Does the lake setback shrink a planned putting green's footprint on a Maitland waterfront lot?",
                "It can. The 10-foot line comes off the buildable area before contouring starts, so a green planned close to a lake or canal sometimes ends up smaller than the lot's total open space would suggest."),
        ],
        "sources": SRC,
    },
    "playground": {
        "title": "Playground Turf for Maitland Families",
        "meta": "Playground turf installation in Maitland, FL runs $10–$25 per sq ft. Shock pad sizing for backyard play areas near Lake Lily and Fort Maitland Park.",
        "h1": "Playground turf for Maitland backyards",
        "lede": capsule(f"Families in Maitland are about as likely to add a backyard play set to an established 1970s or 80s lot as to build one into new construction, which changes what a crew finds already in the ground. A small residential play area typically prices around {price('playground', True)} a square foot as of September 2026, inside the {price('playground')} range that holds across Central Florida."),
        "sections": [
            ("Retrofitting play equipment onto an established yard",
             f"<p>A swing set or climbing structure added to a mature Maitland backyard, rather than planned in with new construction, often lands somewhere a mid-century tree canopy already casts partial shade, which helps with surface heat but can also mean root systems close to where the shock pad needs to sit. {post('coolest-artificial-grass-and-infill-for-florida', 'This article')} covers what infill choices do for a play surface that's only partly shaded.</p>"),
            ("Fall-height pad sizing follows the equipment, not the lake",
             f"<p>Whatever play equipment goes in, the cushioning pad underneath has to match that equipment's manufacturer-rated fall height, a requirement that doesn't shift based on whether the home sits near Lake Lily, Lake Maitland or away from the water entirely. What can shift is the layout's shape, since an irregular older lot sometimes fits a play area better in an L-shape around existing landscaping than in a simple rectangle.</p>"),
            ("A family-friendly city with parks of its own",
             f"<p>Lake Lily Park, a ten-acre city park with a walking trail and a Sunday farmers market through much of the year, and Fort Maitland Park on Lake Maitland give Maitland families public play space to compare a backyard install against. A private play area still has to meet the same fall-height and infill standards a public one would, even without the foot traffic a park sees.</p>"),
        ],
        "scenario": ("A play set added to an established backyard",
                     f"<p>A 1978 home replacing a decades-old mulch bed with a 220 sq ft turfed play corner, sized for a swing set rated to a four-foot fall height, is a fairly typical Maitland job. Installed cost lands around $2,640 to $4,180 at {price('playground', True)} a square foot, with clearing the old mulch and checking the grade underneath it adding modest prep time a bare-soil lot wouldn't need.</p>"
                     + f"<p>{svc('playground', 'Playground turf')} in {city('casselberry', 'Casselberry')} or {city('longwood', 'Longwood')} prices the same way; what moves the number here is what's being replaced, not the address.</p>"),
        "faqs": [
            faq("Does an older Maitland backyard need extra prep before playground turf goes in?",
                "Sometimes. A yard that's carried a mulch bed, a sandbox or an older play structure for years often needs that material cleared and the grade checked before the new base goes down, which a bare-soil newer lot doesn't require."),
            faq("Is playground turf near Lake Lily or Lake Maitland subject to a different heat standard?",
                "No. Surface heat and cooling infill work the same way regardless of which lake a home sits near; shade from nearby trees, not proximity to water, is what actually changes how hot a play area gets."),
        ],
        "sources": SRC,
    },
    "pool": {
        "title": "Pool and Lanai Turf in Maitland, FL",
        "meta": "Pool and lanai turf in Maitland, FL prices in the same range as a residential lawn, $8–$18 per sq ft. Screened enclosures old and new near Maitland Center.",
        "h1": "Turf around a Maitland pool enclosure",
        "lede": capsule(f"Turf around a pool or inside a screened lanai in Maitland prices in the same range as a residential lawn, {price('residential')} per square foot as of September 2026, typically {price('residential', True)}. The city's mix of decades-old pool homes and newer construction near Maitland Center means two fairly different retrofit situations, depending on which side of town a job is on."),
        "sections": [
            ("Older pool cages built before turf was an option",
             f"<p>A pool enclosure added to a 1970s or 80s Maitland home decades ago was built around whatever sod was standard at the time, and the strip of ground between the deck and the screen frame on a retrofit like that is often narrower and more settled than a newer subdivision's factory-planned pool yard. Turf there needs a drainage underlay at the concrete transition, since that's where water collects first if the grading isn't right.</p>"),
            ("Newer construction near Maitland Center",
             f"<p>The residential streets that filled in around Maitland Center after its 1982 development tend to carry more standardized pool-deck layouts than the older subdivisions closer to the lakes, which usually means a more predictable retrofit with fewer surprises once the screen enclosure's footprint is measured.</p>"),
            ("Candler sand under the deck, concrete at the edge",
             f"<p>The same fast-draining ridge sand common across Maitland doesn't change how turf bonds to a pool deck's concrete edge, since that transition relies on adhesive and a drainage underlay rather than the native soil. {post('install-artificial-turf-over-concrete-pavers-or-grass', 'This article')} covers what changes when turf meets a hard surface instead of open ground.</p>"),
        ],
        "scenario": ("A lanai retrofit on an older pool cage",
                     f"<p>A 1979 pool home where the sod inside the screen cage has struggled for years in partial shade is a common enough repeat job here, and a strip like that often works out to around 260 sq ft once the deck's curves are subtracted out. That's roughly $2,600 to $4,160 at {price('residential', True)} a square foot, with the concrete-edge drainage underlay adding a modest amount on top.</p>"
                     + f"<p>The same retrofit near Maitland Center's newer construction would price the same way; the enclosure's age changes the prep work more than the total cost.</p>"),
        "faqs": [
            faq("Do older Maitland pool cages need more prep work than newer ones for a turf retrofit?",
                "Often, yes, since decades-old sod struggling in a shaded enclosure usually means more soil correction before the base goes in than a newer, better-drained pool deck needs."),
            faq("Does turf around a Maitland pool need a different infill near the water?",
                "No infill change is required specifically for pool proximity; the standard silica or coated-sand options used on any residential lawn work the same way beside a pool deck."),
        ],
        "sources": SRC,
    },
    "repair": {
        "title": "Artificial Turf Repair in Maitland, FL",
        "meta": "Artificial turf repair in Maitland, FL is quoted after a site visit, not a per-square-foot rate. Older installs near the city's canals show wear first.",
        "h1": "Fixing turf problems on established Maitland lots",
        "lede": capsule("A lifted edge and a full re-lay call for very different amounts of work, so a Maitland repair job gets priced from a site visit rather than a flat rate. Maitland's own Land Development Code doesn't attach a maintenance-agreement requirement to turf the way some nearby cities do, so a repair here answers mainly to the state's standard and the homeowner's own priorities."),
        "sections": [
            ("What shows up first on an installation from before the state rule",
             f"<p>A lawn installed in Maitland before Rule 62-308.100 took effect in May 2026 may have been built with fewer of the current anchoring and base requirements, and the first sign of that gap usually turns up as a corner that's lifted after a season of storms, not as a full failure. {post('artificial-turf-hurricane-flooding', 'This article')} covers what a properly anchored edge is supposed to withstand and what a rushed one doesn't.</p>"),
            ("Canal-adjacent lots and infill migration",
             f"<p>A lawn graded toward one low corner on a lot near one of Maitland's canals can shed a visible amount of infill into the water during a hard storm if the edge isn't properly anchored there. The fix for that isn't switching infill types; it's correcting the grade and the edge treatment at the specific spot where water actually exits the property.</p>"),
            ("Matching an old lawn's infill and grain on a repair",
             f"<p>A repair patch on a lawn that's been down for several years has to account for however much the surrounding turf has faded or matted since installation, since a fresh patch next to older material can look mismatched even when the repair itself is done correctly. {post('what-does-artificial-turf-warranty-cover', 'This article')} covers what a manufacturer's warranty does and doesn't cover once a lawn is years past its install date.</p>"),
        ],
        "scenario": ("A settled corner near a canal-adjacent lot",
                     "<p>Say you have a lawn installed about six years ago on a lot near one of Maitland's canals, with a corner that's started to hold water after storms and a visible dusting of infill along the low edge. A site visit determines whether that's a simple edge re-anchor or a sign the base settled unevenly at that corner, which would call for pulling back more turf than the visible problem suggests.</p>"
                     + "<p>A settled base at that corner costs more to correct properly than a straightforward edge re-bond would, even though the two problems can look nearly identical from a few feet away.</p>"),
        "faqs": [
            faq("Does Maitland require any ongoing maintenance agreement for installed turf, the way some cities do?",
                "Not based on the current Land Development Code, recodified in October 2024, which doesn't address synthetic turf at all. A repair decision here comes down to the homeowner's own priorities rather than a recorded city agreement."),
            faq("Why does turf near a Maitland canal seem to lose infill faster than turf elsewhere on the same lawn?",
                "A grade that slopes toward the canal edge, combined with a loosely anchored border there, lets infill travel during a hard rain. Correcting the grade and the edge anchor at that specific spot usually solves it without a full infill replacement."),
        ],
        "sources": SRC,
    },
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
