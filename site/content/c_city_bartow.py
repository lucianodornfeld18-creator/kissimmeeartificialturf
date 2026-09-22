# -*- coding: utf-8 -*-
"""Bartow, FL (tier 3, Polk County seat). Hub + residential/pet/putting city x service pages.
Researched September 2026: City of Bartow Building Department and water-restrictions pages, SWFWMD's
"where the river begins" page, the Polk County Water Atlas entry for Lake Hancock, Florida DEP's
phosphate-mining page, Wikipedia's NRHP entries for Bartow's historic districts and the Old Polk
County Courthouse, and Florida Demographics for population. County-level Polk permit/water/soil
facts are reused from site/content/c_permits.py and c_counties.py (same facts and URLs, fresh
sentences here)."""
from _data import CITIES
from _helpers import page, capsule, sec, table, faq, a, svc, city, post, src, ext, price
from _cityservice import cityservice_pages

SLUG = "bartow"

BUILD = ("City of Bartow - Building Department", "https://www.cityofbartow.net/159/Building-Department")
WATER = ("City of Bartow - Water Restrictions", "https://www.cityofbartow.net/463/Water-Restrictions")
RIVER = ("Southwest Florida Water Management District - where the Peace River begins", "https://www.swfwmd.state.fl.us/watersheds/peace-river/where-the-river-begins")
HANCOCK = ("Polk County Water Atlas - Lake Hancock", "https://polk.wateratlas.usf.edu/waterbodies/lakes/160718/lake-hancock")
PHOSPHATE = ("Florida DEP - phosphate mining and reclamation", "https://floridadep.gov/water/mining-mitigation/content/phosphate")
DOWNTOWN = ("Bartow Downtown Commercial District, National Register of Historic Places", "https://en.wikipedia.org/wiki/Bartow_Downtown_Commercial_District")
SOUTHDIST = ("South Bartow Residential District, National Register of Historic Places", "https://en.wikipedia.org/wiki/South_Bartow_Residential_District")
COURTHOUSE = ("Old Polk County Courthouse (1908-09), National Register of Historic Places", "https://en.wikipedia.org/wiki/Old_Polk_County_Courthouse_(Florida)")
POP = ("Florida Demographics - Bartow population", "https://www.florida-demographics.com/bartow-demographics")
PA = ("Polk County Property Appraiser - parcel search", "https://www.polkflpa.gov/")

SRC = [BUILD, WATER, RIVER, HANCOCK, PHOSPHATE, DOWNTOWN, SOUTHDIST, COURTHOUSE, POP, PA, "dep-rule", "fs125572", "fs7203045", "usda-wss"]

# ============================================================== hub
HUB = page(
    "/areas/bartow/", "city",
    "Artificial Turf Installation in Bartow, FL (2026)",
    "Artificial turf installers serving Bartow, FL, the Polk County seat: its own permit office, Lake Hancock's setback, and reclaimed mine-land soil, 2026.",
    "Artificial turf and synthetic grass in Bartow, Florida",
    capsule(f"Kissimmee Artificial Turf installs, repairs and cleans synthetic lawns in Bartow, the Polk County seat, at the same {price('residential')} per square foot Central Florida range as of September 2026. Bartow runs its own Building Department and its own water utility, separate from the county offices that share its name, and the Peace River's headwaters sit just northeast of downtown."),
    "".join([
        sec("The county seat, and what that means for a turf crew",
            f"<p>Bartow is the Polk County seat, home to the county courthouse and, confusingly for a homeowner searching for the right office, its own city government layered on top of the county one. A turf job at a Bartow address goes through the city's own departments, not the Polk County Building Division whose number tends to surface first in a general search. {ext(POP[1], 'Just over 20,000 people')} live inside the city limits, a mix of century-old homes near the courthouse square and newer rooftops on annexed land toward the edges of town. At {CITIES['bartow']['miles']} miles from downtown Kissimmee, Bartow sits at the far edge of where we work, and a job here typically shares a route with a stop in {city('lakeland')} or {city('winter-haven')} rather than standing alone on the schedule.</p>"),
        sec("Permits: Bartow's own Building Department",
            f"<p>The City of Bartow's Building Department, at 450 N. Wilson Avenue, takes permit and inspection calls at {ext(BUILD[1], '(863) 534-0157')}, a line answered in person or by voicemail around the clock, with applications filed through the city's own online portal rather than the county's Accela system. We haven't found a Bartow ordinance written specifically for synthetic turf, so {a('/laws/florida-hb-683/', "the state's May 2026 turf standard")} is the clearest written rule reaching a Bartow lot; call the Building Department with the address before assuming anything else applies. A property just outside the city limit, toward the old mining land, may sit in unincorporated Polk County instead, where {a('/laws/permits/polk-county/', "Polk County's own permit page")} and a {ext(PA[1], 'parcel search')} settle which office is in charge. Where a homeowners' association sits on top of either jurisdiction, {a('/laws/hoa-rules/', 'state law still limits what it can restrict')} once turf sits behind a fence line.</p>"),
        sec("Bartow yard types and how the build changes",
            "<p>Two very different pieces of ground make up most of Bartow: the old town near the courthouse square, and land that spent decades as a phosphate mine before it was reclaimed for houses. Neither rules out turf; each changes a detail of the build.</p>"
            + table("Bartow property types and how we adjust", ["Property", "Local factor", "How we adjust"],
                    [["Courthouse-square historic home", "Century-old oaks, a design-review district", "Base plan respects the drip line; no digging under a canopy without an arborist letter"],
                     ["Lot on reclaimed phosphate land", "Fill placed during mine reclamation", "Compaction gets checked on site rather than assumed to match native county sand"],
                     ["Property near Lake Hancock or the Peace River", "Headwaters of the Peace River", "10-ft waterbody setback measured from the ordinary water line"],
                     ["Newer rooftop toward the annexed edge of town", "HOA or deed-restricted subdivision", "Architectural packet with a turf sample and site plan before work starts"]],
                    "Bartow's Building Department reviews the permit; an HOA, where one exists, reviews the paperwork separately.")),
        sec("Water, Lake Hancock and the setback that follows the river",
            f"<p>Bartow bills its own water rather than buying through the county, and like the rest of the region it currently sits under the Southwest Florida Water Management District's Modified Phase III order: one watering day a week by address, the last digit setting Monday through Friday, in a window before 4 a.m. or after 8 p.m. for a lot under an acre. {ext(WATER[1], "The city's water-restrictions page")} carries the current schedule, since an order like this one can change with little notice. {ext(HANCOCK[1], 'Lake Hancock')}, a 4,584-acre lake sitting mostly inside Bartow, marks the start of the Peace River at the point where {ext(RIVER[1], 'Saddle Creek and the Peace Creek Drainage Canal meet')} northeast of downtown. Any synthetic lawn near that shoreline, or along the river itself, keeps the same 10-foot setback as a yard on a small backyard pond, unless a seawall already stands between the turf and the water.</p>"),
        sec("Reclaimed ground and the oaks around the square",
            f"<p>South and east of downtown, some of Bartow's newer growth sits on ground that spent decades as an open phosphate pit before {ext(PHOSPHATE[1], 'state rules required it reclaimed')}, a standard in place for every mine permitted after 1975. Reclaimed land here has gone on to become pasture, fishing lakes and, on annexed parcels at the edge of the city, home sites, but the soil under a reclaimed lot is rebuilt rather than a natural Polk County sand series, and how consistently it compacts can vary block to block in a way the standard soil maps don't fully capture. Inside {ext(DOWNTOWN[1], 'the historic district ringing the courthouse square')}, the concern runs the other way: mature live oaks shading Broadway and Summerlin since the early 1900s put {a('/laws/florida-hb-683/', "the state's drip-line rule")} into play on almost any lot old enough to sit in the district at all.</p>"),
        "<!--AUTO:city-services-->",
    ]),
    faqs=[
        faq("Does the City of Bartow require a permit for synthetic turf?",
            "The city's own Building Department reviews permits for any address inside the Bartow city limit, and we haven't found a code section written specifically for artificial turf, so the state's 2026 standard is the clearest rule on the books. Call (863) 534-0157 to confirm what a specific address needs."),
        faq("What's Bartow's current watering schedule?",
            "One day a week, assigned by the last digit of the address, under the Southwest Florida Water Management District's Modified Phase III order in place since spring 2026. The city's own water-restrictions page carries the current hours, since the order can change before it's due to expire. A capped synthetic lawn doesn't need to follow the schedule at all."),
        faq("How close to Lake Hancock or the Peace River can turf go?",
            "At least 10 feet from the ordinary water line, the same statewide setback that applies to any pond, lake or canal, unless a seawall already separates the yard from the water. The rule also keeps turf out of any drainage swale or ditch on the way to the river."),
        faq("Is ground on Bartow's old phosphate-mining land safe to build a lawn on?",
            "Yes. Turf doesn't change what's in the ground either way. The practical issue is that reclaimed mine land is rebuilt soil rather than a natural sand series, so a site visit checks compaction instead of assuming it behaves like the rest of the county."),
        faq("What's the best way to find an artificial turf company near me in Bartow?",
            "Ask for the same three things anywhere in the county: a measured site visit rather than a phone quote, the base depth and material in writing, and a straight answer on whether the parcel is inside the city limit or unincorporated county land, since that decides which office reviews the permit."),
    ],
    sources=SRC, city=SLUG, crumbs=[("Service areas", "/areas/")], crumb="Bartow",
    related=[("/areas/polk-county/", "Turf rules for all of Polk County"), ("/laws/permits/polk-county/", "Polk County's permit page"),
             ("/areas/lake-wales/", "Artificial turf in Lake Wales"), ("/areas/haines-city/", "Artificial turf in Haines City"),
             ("/artificial-turf-cost/", "Full turf cost guide"), ("/blog/base-under-artificial-turf-florida-sandy-soil/", "What base goes under turf in Central Florida soil")],
)

# ============================================================== residential
_RES_S1 = ("Old town versus reclaimed ground",
           f"<p>Bartow's residential lots split roughly into two stories. Close to the courthouse square, {ext(SOUTHDIST[1], 'the South Bartow and Northeast Bartow residential districts')} carry homes that go back to the early 1900s, Victorian-era porches giving way to 1920s and 1930s bungalows under oaks that have had a century to spread their canopy. Head south and east instead and some of the newest rooftops sit on land that was an open phosphate pit within living memory, annexed and built out only after reclamation rules caught up with it. A lawn conversion on the first kind of lot is mostly about respecting what's already grown in; on the second, {post('base-under-artificial-turf-florida-sandy-soil', 'the base question')} comes first, before assuming the native county sand the rest of Polk gets.</p>")

_RES_S2 = ("What USDA's soil map does, and doesn't, say about reclaimed land",
           f"<p>{a('/areas/polk-county/', "Polk County's")} standard soil story runs to Candler and other sand series across most of the county, but reclaimed phosphate ground doesn't fit neatly into that map, since the original profile was stripped away in 30- to 40-foot lifts and rebuilt afterward rather than laid down naturally. We won't claim a specific series for a lot we haven't stood on; the honest answer is that fill on former mine land can compact more inconsistently than native sand, block to block, depending on how that particular parcel was reclaimed. That's a reason to have the crew check the ground with a site visit before quoting a number, not a reason to avoid turf on that side of town.</p>")

_RES_S3 = ("Permits for a straightforward Bartow lawn",
           f"<p>A plain backyard conversion inside the city limit goes through Bartow's own Building Department at {ext(BUILD[1], '(863) 534-0157')}, a line staffed or voicemail-monitored around the clock, with the application filed online rather than mailed in. We haven't found a section of Bartow's code written for synthetic turf specifically, so {a('/laws/florida-hb-683/', 'the state standard adopted in 2026')} is what actually governs the build itself. A subdivision built under a homeowners' association layers its own review on top, and {a('/laws/hoa-rules/', "state law keeps that review from reaching a backyard no one can see from the street")}. Either way, the crew still caps any irrigation head that used to reach the converted area, since {src('dep-rule', "the state rule")} bars watering synthetic turf through an in-ground system.</p>")

_RES_SC = ("Say you have an 880 sq ft yard off the square",
           f"<p>Say you have an 880 sq ft backyard behind a 1925 bungalow two blocks off the courthouse square, shaded by a live oak that sits just inside the property line. At the {price('residential', True)} typical range that runs about ${880 * 10:,}–${880 * 16:,} installed, or ${880 * 8:,}–${880 * 18:,} across the full published range, with the oak's drip line trimming a corner off the usable area rather than the whole yard. Grading has to work around exposed roots near the trunk instead of cutting straight through them, which asks for a crew that reads the roots before it digs, not just a tape measure.</p>")

LOCAL_RESIDENTIAL = {
    "title": "Artificial Grass Installation in Bartow: Square to Reclaimed Land",
    "meta": "Artificial grass installation in Bartow, FL spans courthouse-square historic lots and reclaimed phosphate-land subdivisions, $8–$18 a sq ft, September 2026.",
    "h1": "Installing artificial grass from Bartow's square to its reclaimed land",
    "lede": capsule(f"A lawn conversion in Bartow costs the same {price('residential')} per square foot as anywhere else in Central Florida, typical jobs at {price('residential', True)}, as of September 2026. What differs by block is the ground: a courthouse-square lot from the 1900s sits on settled native sand under mature oaks, while a newer home toward the annexed south side may sit on ground rebuilt after decades as a phosphate mine."),
    "sections": [_RES_S1, _RES_S2, _RES_S3],
    "scenario": _RES_SC,
    "faqs": [
        faq("Does a Bartow lawn conversion need a permit?",
            "Call the city's Building Department at (863) 534-0157 to confirm for a specific address, since we haven't found a Bartow code section written for synthetic turf on its own. The state's 2026 turf standard is the clearest rule that applies either way."),
        faq("Is reclaimed phosphate-mine land safe to build a lawn on?",
            "Yes, though the fill can compact less predictably than native Polk County sand, since the ground was stripped and rebuilt during mine reclamation rather than laid down naturally. A site visit before quoting catches that; a phone estimate based on the address alone can't."),
    ],
    "sources": SRC,
}

# ============================================================== pet
_PET_S1 = ("Dog runs near the river versus dog runs on new ground",
           f"<p>Bartow sits at the headwaters of the Peace River, where Saddle Creek drains out of {ext(HANCOCK[1], 'Lake Hancock')} and meets the Peace Creek Drainage Canal just northeast of downtown, and a handful of in-town lots back directly onto that water or onto the lake itself. A dog run planned for one of those lots keeps the same 10-foot setback from the ordinary water line as any Florida waterbody, seawall exception included. Move to one of the newer subdivisions built on annexed, formerly mined land toward the edge of the city, and the setback question mostly disappears, replaced by a different one: whether the reclaimed fill under that particular lot drains and compacts the way the rest of the county's native sand does.</p>")

_PET_S2 = ("A dog run's base on ground that used to be a mine",
           f"<p>Fully permeable backing and a firm base matter on any dog run, but they matter more on Bartow's reclaimed-land subdivisions, where fill placed during {ext(PHOSPHATE[1], 'phosphate-mine reclamation')} doesn't always compact as evenly as the native sand the rest of Polk County sits on. That gets checked with a site visit rather than assumed, since two lots a block apart can have been reclaimed at different times with different material. None of that changes the infill choice; silica, zeolite or a coated sand still cover a dog run's odor-control needs the same way they would on a courthouse-square lot with a century of settled ground underneath it instead. {post('pet-turf-vs-regular-artificial-grass', 'What actually differs on a pet system')} comes down to backing and infill, not location.</p>")

_PET_S3 = ("Keeping a run's fence line clear of the historic district's review",
           f"<p>A dog run tucked behind a fence on a South Bartow or Northeast Bartow residential-district lot mostly avoids the design review that covers street-facing changes to those historic properties, since {a('/laws/hoa-rules/', "Florida law already protects anything not visible from the frontage or an adjacent parcel")}. What that review does still reach is a fence itself, if the run needs a new one built to keep a dog in, so that piece is worth checking with the Building Department separately from the turf. A run on annexed land at the city's edge answers to whatever HOA exists there instead, which typically wants a sample and a site plan regardless of visibility. {post('how-to-get-dog-urine-smell-out-of-artificial-turf', 'Odor control')} is the same conversation either way.</p>")

_PET_SC = ("Say you have a 300 sq ft run off State Road 60",
           f"<p>Say you have a 300 sq ft run along a chain-link fence on a newer lot off State Road 60, on ground that was part of a phosphate operation two decades ago. At the {price('pet', True)} typical range that's about ${300 * 12:,}–${300 * 16:,} installed, or ${300 * 10:,}–${300 * 18:,} across the full range, with the crew's first stop being a few test holes to see how the reclaimed fill actually compacts before finalizing the base depth. A run this size on settled ground would skip that step entirely; here it's the difference between a bid that holds and one that needs revising after the first heavy rain.</p>")

LOCAL_PET = {
    "title": "Pet Turf & Dog Runs in Bartow, FL",
    "meta": "Pet turf and dog runs in Bartow, FL: the setback near Lake Hancock and the Peace River, and reclaimed-land soil checks, September 2026.",
    "h1": "Pet turf and dog runs near Bartow's river and reclaimed land",
    "lede": capsule(f"Pet turf in Bartow runs {price('pet')} per square foot, typical jobs at {price('pet', True)}, the same Central Florida range as of September 2026 as anywhere else we work. The detail worth asking about here is location: a run near Lake Hancock or the Peace River answers to the state's 10-foot waterbody setback, while one on reclaimed ground toward the edge of town answers to a soil question instead."),
    "sections": [_PET_S1, _PET_S2, _PET_S3],
    "scenario": _PET_SC,
    "faqs": [
        faq("How do I find the best artificial turf company near me in Bartow?",
            "Start with a crew that measures the actual run and asks whether the lot sits on original ground or reclaimed mine land, since that changes what the base needs. A bid that's identical regardless of location, without ever asking where the property sits, is worth a second opinion before signing."),
        faq("Can a dog run sit next to Lake Hancock or the Peace River?",
            "Yes, as long as it stays at least 10 feet back from the ordinary water line, or right up to a seawall if one already exists. The same setback applies whether the water is a small retention pond or a lake as large as Hancock."),
    ],
    "sources": SRC,
}

# ============================================================== putting
_PUT_S1 = ("Where a green fits near the county seat",
           f"<p>Bartow doesn't have a golf-community corridor the way {city('davenport')} or {city('championsgate')} does along US 27; a putting green here is almost always a single large lot's own project instead. The properties with room for a full multi-tier layout tend to sit on the edges of the historic core or out toward {ext(HANCOCK[1], 'Lake Hancock')} and the Circle B Bar Reserve, where older parcels run deeper than a typical in-town lot. Inside the South Bartow or Northeast Bartow residential districts, a narrower yard usually limits the build to a single-tier green and a short fringe rather than the multiple breaks a bigger property allows, which isn't a downgrade so much as a different design brief for the same square footage.</p>")

_PUT_S2 = ("Excavating deeper on ground the Peace River sometimes reaches",
           f"<p>A putting green needs deeper excavation than a flat lawn to shape its tiers, and on a lot close to the Peace River or Lake Hancock's floodplain, that deeper cut has to answer to the state turf rule's stormwater language too: no pooling, and no added runoff toward a neighboring property. Polk County has flagged potential Peace River flooding in past wet seasons, and a low-lying lot near that floodplain needs its drainage worked out before any rock goes in, not adjusted afterward. Land that sits higher, away from the river, doesn't carry that complication, and the base work looks like what a green needs anywhere else in the county, just with the extra excavation a tiered layout always takes.</p>")

_PUT_S3 = ("Distance and how a Bartow green gets scheduled",
           f"<p>At {CITIES['bartow']['miles']} miles from downtown Kissimmee, Bartow is the farthest of our regular Polk County stops, and a putting green's longer layout day makes that distance more relevant than it would be for a quick repair call. We usually schedule a Bartow green alongside another job in {city('lakeland')} or {city('auburndale')} the same week rather than as a single standalone trip. {post('backyard-putting-green-cost-florida', 'The price range')} doesn't change because of the drive; what changes is how far out the install date tends to land on the calendar.</p>")

_PUT_SC = ("Say you have a 480 sq ft green near Circle B",
           f"<p>Say you have a 480 sq ft green and fringe planned for a deep backyard near the Circle B Bar Reserve, with three gentle tiers and a chipping pad off to one side. At the {price('putting', True)} typical range that prices around ${480 * 18:,}–${480 * 25:,}, or ${480 * 14:,}–${480 * 30:,} across the full published range, with the lower tier's drainage checked carefully given how close the property sits to the Peace River basin. A yard with that much room usually keeps the green as its own contained piece, fringe seamed in separately from any lawn turf nearby.</p>")

LOCAL_PUTTING = {
    "title": "Backyard Putting Greens in Bartow, FL",
    "meta": "Backyard putting greens in Bartow, FL fit larger lots near Lake Hancock and the historic core, priced $14–$30 a sq ft, September 2026.",
    "h1": "Backyard putting greens near Bartow's lake and historic core",
    "lede": capsule(f"A backyard putting green in Bartow costs {price('putting')} per square foot, typical jobs at {price('putting', True)}, the same range published for the rest of Central Florida as of September 2026. The lots with the most room for one tend to sit on larger, older parcels near Lake Hancock and the Circle B Bar Reserve, rather than inside the tighter courthouse-square historic district."),
    "sections": [_PUT_S1, _PUT_S2, _PUT_S3],
    "scenario": _PUT_SC,
    "faqs": [
        faq("Is there enough land in Bartow for a full-sized putting green?",
            "On the right lot, yes. Properties near Lake Hancock and the Circle B Bar Reserve, and some of the larger parcels at the edge of the historic core, run deep enough for a multi-tier layout; a narrower in-town lot usually fits a single-tier green instead."),
        faq("Does floodplain land near the Peace River need a different green?",
            "Not a different product, but more attention to drainage before excavation starts, since the state's turf rule bars any added runoff toward a neighboring lot. A low-lying property gets its stormwater plan settled first; the green itself is built the same way anywhere else in the county."),
    ],
    "sources": SRC,
}

LOCAL = {"residential": LOCAL_RESIDENTIAL, "pet": LOCAL_PET, "putting": LOCAL_PUTTING}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
