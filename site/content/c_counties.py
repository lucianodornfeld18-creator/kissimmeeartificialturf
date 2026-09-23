# -*- coding: utf-8 -*-
"""Five county hub pages: /areas/<county>-county/ for Osceola, Orange, Polk, Lake and Seminole.
Permit-office facts, code findings and existing water-utility rules are reused from
research/permits-research.md and site/content/c_permits.py (same sources, fresh sentences).
Newly researched for this module: water management district boundaries for each county
(SFWMD/SJRWMD/SWFWMD, checked against sfwmd.gov and sjrwmd.com) and USDA official series
descriptions for the Candler and Astatula ridge sands, checked September 2026."""
from _data import CITIES
from _posts import PERMIT_PAGES
from _helpers import page, capsule, sec, table, faq, a, svc, city, post, src, ext, price

CRUMBS = [("Service areas", "/areas/")]

HB683 = "/laws/florida-hb-683/"
HOA = "/laws/hoa-rules/"
PERMITS_HUB = "/laws/permits/"
COST = "/artificial-turf-cost/"

SFWMD_WHO = ("South Florida Water Management District — service area by county", "https://www.sfwmd.gov/who-we-are")
SFWMD_KISS = ("South Florida Water Management District — Upper Kissimmee Basin water supply plan", "https://www.sfwmd.gov/our-work/water-supply/upper-kissimmee")
SJRWMD_ORANGE = ("St. Johns River Water Management District — Orange County", "https://www.sjrwmd.com/district-counties/orange-county/")
SJRWMD_RESTRICT = ("St. Johns River Water Management District — watering restrictions", "https://www.sjrwmd.com/wateringrestrictions/")
OC_UTIL = ("Orange County Utilities — watering restrictions", "https://www.orangecountyfl.net/watergarbagerecycling/wateringrestrictions.aspx")
POLK_UTIL = ("Polk County — current water restrictions", "https://www.polkfl.gov/services/utilities/water-restrictions/")
LAKE_PLAN = ("Lake County Water Supply Plan", "https://cdn.lakecountyfl.gov/media/2bwbhcsf/lc_water_supply_plan.pdf")
GREEN_SWAMP = ("Florida DEP — Green Swamp partnerships and regional incentives, Lake, Pasco and Polk counties", "https://floridadep.gov/sites/default/files/FLDEP_DSL_OES_FF_2026_GreenSwamp.pdf")
CANDLER_OSD = ("USDA NRCS — official series description, Candler series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/C/CANDLER.html")
ASTATULA_OSD = ("USDA NRCS — official series description, Astatula series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/A/ASTATULA.html")
TOHO_AREA = ("Toho Water Authority — our service area", "https://www.tohowater.com/about-us/our-service-area")


def plink(key, text=None):
    return a(f"/laws/permits/{key}/", text or PERMIT_PAGES[key])


def jrow(name, finding, office, key=None, town=None):
    last = plink(key, "Details") if key else (a(CITIES[town]["route"], "Town page") if town else "Not published")
    return [name, finding, office, last]


def drow(slug):
    c = CITIES[slug]
    kind = "Incorporated " + c["kind"] if c["kind"] in ("city", "town") else c["kind"].capitalize()
    return [city(slug), f"about {c['miles']} miles", kind]


DIST_HEAD = ["Town", "Straight-line distance from downtown Kissimmee", "Status"]


# ============================================================== Osceola
def osceola():
    body = "".join([
        sec("Artificial turf across Osceola County",
            f"<p>Osceola County is where the trucks are parked, so most of a working week happens here. Residential {a('/artificial-grass-installation/', 'artificial grass installation')} runs {price('residential')} per square foot as of September 2026, the same range whether the address is downtown Kissimmee or a lakefront lot outside Harmony. Nearly the entire county sits inside our roughly 40-mile radius; only the cattle and citrus land south of Kenansville, near the Osceola-Okeechobee line, runs past it.</p>"
            + f"<p>Work here covers full lawns, {svc('pet', 'pet turf for the county’s dog runs')}, {svc('putting', 'backyard putting greens')} and turf for the {svc('str', 'short-term rental homes')} clustered west of the Turnpike. The county's own Land Development Code doesn't mention synthetic turf, so the floor everywhere in it is the state's, described in full at {a(HB683, 'HB 683 and Rule 62-308.100')}.</p>"),
        sec("Who reviews a turf job in Osceola County",
            "<p>Two cities and one county government split jurisdiction here. Kissimmee and St. Cloud each run their own Building Division; everything else, from Buenaventura Lakes to Poinciana to Harmony, answers to Osceola County's Building Department. None of the three has published a synthetic-turf-specific rule, which means an application gets measured against ordinary landscape, drainage and irrigation permitting rather than a dedicated turf code.</p>"
            + table("Who reviews a synthetic turf job in Osceola County",
                    ["Jurisdiction", "What we found on synthetic turf", "Office to call", "Permit page"],
                    [jrow("City of Kissimmee", "No turf-specific section in the Land Development Code", "Development Services, 407-518-2120", "city-of-kissimmee"),
                     jrow("City of St. Cloud", "No turf-specific section in the Code of Ordinances", "Building Department, 407-957-7243", "city-of-st-cloud"),
                     jrow("Osceola County (Poinciana, Celebration, BVL, Harmony, Four Corners and the rest of the unincorporated county)", "No turf-specific section in the Land Development Code", "Building Department, 407-742-0200", "osceola-county")],
                    "Checked against each office's published code September 2026; silence on synthetic turf isn't a written exemption from ordinary permitting.")
            + f"<p>A Poinciana parcel is the one worth double-checking: the community sits across the Osceola-Polk line, so the same street can answer to two different building departments depending on which side of it a lot falls. {a(PERMITS_HUB, 'Our permit hub')} walks through how to confirm a specific parcel before assuming which office applies.</p>"),
        sec("Water in Osceola County: Toho, a state rule and two chains of lakes",
            f"<p>Toho Water Authority supplies water, sewer and reclaimed water to Kissimmee, St. Cloud and Poinciana, plus the unincorporated pockets around them ({ext(TOHO_AREA[1], 'Toho’s service-area page')}). Irrigation is limited to two mornings or evenings a week by address, odd numbers on Wednesday and Saturday, even numbers on Thursday and Sunday, with no watering in daylight hours ({src('toho-days', 'Toho’s current schedule')}). Osceola County was also weighing a countywide water-conservation ordinance as of mid-2026, separate from Toho's rules ({src('osceola-water-2026', 'coverage of the proposal')}).</p>"
            + f"<p>Most of Osceola, including the Lake Tohopekaliga and East Lake Tohopekaliga chain that Kissimmee and St. Cloud sit on, drains south into the Kissimmee River and falls under the South Florida Water Management District's Kissimmee Basin planning area ({ext(SFWMD_KISS[1], 'SFWMD’s Upper Kissimmee Basin plan')}; {ext(SFWMD_WHO[1], 'SFWMD’s own county list')}). None of that schedule reaches a synthetic lawn once its irrigation heads are capped, since {src('dep-rule', 'the state standard')} bars watering synthetic turf from an in-ground system outright.</p>"),
        sec("What's under an Osceola County lawn",
            "<p>Most of the county sits on Immokalee, Myakka, Basinger and Smyrna fine sands, flatwoods soils with a water table that can rise within twenty to forty inches of the surface for weeks after a summer storm. That's the reason the standard build calls for washed, open-graded crushed rock instead of compacted native fill: a tight base traps the water this soil is already holding onto, and the yard stays soggy long after the rain stops.</p>"
            + f"<p>A crew treats a new-construction lot near Harmony or Four Corners differently from an older Kissimmee yard, because compacted fill left behind by a builder drains worse than undisturbed native sand. {post('why-new-construction-sod-dies-in-osceola-county', 'This post')} covers why that same compaction kills builder sod on new Osceola County lots, which is the same problem a turf base has to solve instead of repeat.</p>"),
        sec("Osceola County yards: pool cages, rental homes and lake lots",
            f"<p>Three yard types repeat across the county. Pool-screen enclosures in Buenaventura Lakes and older Kissimmee subdivisions leave narrow strips of grass that struggle in shade cast by the cage; turf inside the enclosure needs a drainage underlay over the deck. West of the Turnpike, ChampionsGate, Four Corners and Reunion carry the county's short-term-rental concentration, where {svc('str', 'guest-proof yards')} matter more than curb appeal, since the lawn gets walked by a new group of renters most weeks. Lakefront lots on Toho or East Lake Toho, and canal lots feeding either one, sit inside the state's 10-foot waterbody setback unless a seawall already separates the yard from the water.</p>"
            + "<p>Celebration is its own case: the community was planned with heavy street-tree canopy, so a yard there is more likely to sit inside a live oak's drip line than a newer subdivision, which triggers the certified-arborist exception before turf goes anywhere near the trunk.</p>"),
        sec("How far Osceola County towns sit from our Kissimmee base",
            "<p>Every distance below is a straight line from downtown Kissimmee, not a drive time, and the price for a job doesn't move with it.</p>"
            + table("Distance from Kissimmee: Osceola County towns", DIST_HEAD,
                    [drow(s) for s in ["kissimmee", "buenaventura-lakes", "st-cloud", "celebration", "poinciana", "reunion", "narcoossee", "championsgate", "four-corners", "harmony", "kenansville"]],
                    "Miles are a straight line from downtown Kissimmee, not a drive time, and the number in the table above doesn't change what a job costs.")),
        "<!--AUTO:county-cities-->",
    ])
    faqs = [
        faq("How do you find the best artificial turf contractor near you in Osceola County?",
            "Ask three things before signing anything: how deep the base runs and what it's made of, whether the quote lists face weight and infill by name, and whether the installer already knows Toho's watering schedule and the state's May 2026 turf standard without being prompted. A written quote with those specifics is worth more than a sales pitch."),
        faq("Is Kenansville, in far south Osceola County, still within your service area?",
            "It's close to the edge of it. Kenansville sits roughly 38 miles from downtown Kissimmee by straight line, near the outer limit of the roughly 40-mile radius we work within, so a job there is worth a call to confirm scheduling rather than an assumption either way."),
        faq("Does Osceola County's proposed water-conservation ordinance change anything for turf that's already installed?",
            "No. That proposal, still pending as of mid-2026, is aimed at irrigation and groundwater use generally. A synthetic turf area stops needing a sprinkler schedule the moment its heads are capped, which the state standard already requires, so a future county ordinance wouldn't add a new watering rule for turf specifically."),
        faq("Which water district actually regulates the lakes Kissimmee and St. Cloud sit on?",
            "The South Florida Water Management District, through its Kissimmee Basin planning area. The chain of lakes both cities border drains south toward the Kissimmee River, which puts most of the county in that district's territory rather than the one covering Orlando to the north."),
        faq("Is a Poinciana address in Osceola County or Polk County?",
            "It depends which side of the community line the lot sits on. Poinciana was built across the Osceola-Polk County line, so two houses on the same block can answer to different property appraisers and different building departments. A parcel search settles it before a permit question comes up."),
        faq("What should I expect digging in Buenaventura Lakes or Harmony?",
            "Fine, loose sand over a water table that sits closer to the surface than it looks in the dry season. Both areas map mostly to Myakka and Basinger series soils, which is why the base under a turf lawn there is washed crushed rock, never compacted native fill, so summer storms drain through it instead of pooling on top."),
    ]
    return page("/areas/osceola-county/", "county",
                "Artificial Turf in Osceola County, FL (2026 Guide)",
                "Synthetic turf installation, permits, water rules and soil facts for Osceola County, FL, from Kissimmee to Poinciana and Harmony. Checked September 2026.",
                "Artificial turf across Osceola County",
                capsule(f"Kissimmee Artificial Turf installs, repairs and cleans synthetic lawns, pet runs and putting greens across Osceola County, home base for the business, where residential installs run {price('residential')} per square foot as of September 2026. Nearly the whole county, from Kissimmee out to Harmony and Poinciana, sits inside our roughly 40-mile radius; only the ranch country past Kenansville runs beyond it."),
                body, faqs=faqs, crumbs=CRUMBS, crumb="Osceola County", county="osceola",
                sources=["dep-rule", "fs125572", "toho-days", "osceola-water-2026", "usda-wss", SFWMD_KISS, SFWMD_WHO, TOHO_AREA],
                related=[("/laws/permits/osceola-county/", "Osceola County permit rules for turf"), ("/areas/kissimmee/", "Artificial turf in Kissimmee"), ("/areas/st-cloud/", "Artificial turf in St. Cloud"), (COST, "Full turf cost guide"), ("/blog/why-new-construction-sod-dies-in-osceola-county/", "Why builder sod dies on new Osceola County lots")])


# ============================================================== Orange
def orange_co():
    body = "".join([
        sec("Orange County yards, from Hunters Creek to Apopka",
            f"<p>Orange County stretches from pool-cage subdivisions a few minutes past the Kissimmee line to lake towns thirty miles northwest, and the mix of yards changes more across that span than in any other county we work in. Turf installed here runs {price('residential')} per square foot as of September 2026, the published Central Florida range, whatever part of the county the address sits in. The urbanized two-thirds of Orange, from Hunters Creek and Lake Nona through Orlando to Apopka, sits inside our roughly 40-mile radius; the rural northeast corner past Christmas and Bithlo runs beyond it.</p>"
            + f"<p>Hunters Creek, Meadow Woods and Southchase are almost entirely 1990s pool-cage lots with a strip of grass on either side of a screen enclosure; a turf strip there needs a drainage underlay where it meets the deck. Windermere and Dr. Phillips run larger, older lake-front parcels where the state's 10-foot waterbody setback and drip-line rule both come up more often than in a landlocked subdivision. Orlando proper adds condos and rooftops to the mix, which is where {svc('commercial', 'commercial turf')} for a courtyard or a balcony comes in.</p>"),
        sec("What's in the ground on an Orange County lot",
            f"<p>East Orange County, including Hunters Creek, Meadow Woods, Southchase and Lake Nona, sits on the same flatwoods family as the rest of Central Florida: Immokalee, Myakka, Basinger and Smyrna fine sands, with a seasonal high water table that can sit within a few feet of the surface. West Orange, around Windermere, Winter Garden and Apopka, runs through more rolling, lake-pocked terrain, and a specific soil series there is worth checking on the {src('usda-wss', 'USDA Web Soil Survey')} address by address rather than assuming one blanket answer for the whole side of the county.</p>"
            + f"<p>Either way, the base doesn't change: 2 to 4 inches of washed, open-graded crushed rock or crushed concrete, leveled and firm, never limerock with fines. {post('base-under-artificial-turf-florida-sandy-soil', 'This article')} goes through why that specific mix matters more here than the turf brand does.</p>"),
        sec("Water rules for Orange County turf",
            f"<p>Orange County Utilities runs a seasonal schedule: two watering days a week during daylight saving months, one day the rest of the year, assigned by odd or even address, with no watering between 10 a.m. and 4 p.m. ({ext(OC_UTIL[1], 'the county’s current restrictions')}). Orlando's own utility, Orlando Utilities Commission, sets a separate schedule for the city and for a few unincorporated pockets it also bills, including parts of Dr. Phillips and Horizon West, so a specific address is worth checking against a water bill rather than assuming which schedule applies.</p>"
            + f"<p>Most of Orange County, including Orlando, Winter Garden, Ocoee, Winter Park and Apopka, falls in the St. Johns River Water Management District ({ext(SJRWMD_ORANGE[1], 'SJRWMD’s Orange County page')}). The southeastern edge of the county, toward Lake Nona and the Osceola line, sits in the South Florida Water Management District's Kissimmee Basin planning area instead ({ext(SFWMD_WHO[1], 'SFWMD’s county coverage list')}). Neither schedule reaches a synthetic lawn once the heads under it are capped, which {a(HB683, 'the state standard')} requires regardless of utility or district.</p>"),
        sec("Who signs off on a turf project in Orange County",
            "<p>Orlando is the one office on this list with a written artificial-turf section in its code; every other jurisdiction in the county has stayed quiet on the subject. That distinction matters more here than almost anywhere else in our service area, since Orlando's old landscape rules classed turf as impervious and required an engineering permit, something the May 2026 state standard now overrides in part for a covered single-family lot.</p>"
            + table("Who reviews a synthetic turf job in Orange County",
                    ["Jurisdiction", "What we found on synthetic turf", "Office to call", "Permit page"],
                    [jrow("City of Orlando", "Specific artificial-turf rules in the landscape code (engineering permit)", "Permitting Services, 407-246-2121", "city-of-orlando"),
                     jrow("Orange County (unincorporated, including Hunters Creek, Meadow Woods, Lake Nona, Dr. Phillips, Horizon West)", "“Turf” defined as natural grass species only; no synthetic-turf section", "Permitting Services, 407-836-5550", "orange-county"),
                     jrow("Belle Isle", "No in-house building department; plan review and inspections are contracted to a private engineering firm", "City hall; see the town page", town="belle-isle"),
                     jrow("Edgewood", "No building official; the city reviews zoning, then routes the permit to Orange County through Fast Track", "City hall, then Orange County", town="edgewood"),
                     jrow("Windermere", "Own Building Department; no synthetic-turf code found", "Town hall, 407-876-2563", town="windermere"),
                     jrow("Ocoee", "Own Building Division; no synthetic-turf code found", "407-905-3104, permits.ocoee.org", town="ocoee"),
                     jrow("Winter Garden", "Own Building Division; no synthetic-turf code found", "407-877-5136", town="winter-garden"),
                     jrow("Winter Park", "Own Building & Permitting Services; a secondhand code comparison suggests the city code addresses synthetic turf (pervious path, canopy limits) — confirm at the counter", "407-599-3237", town="winter-park"),
                     jrow("Maitland", "Own Community Development Department; land development code recodified in 2024, no synthetic-turf section found", "407-539-6150", town="maitland"),
                     jrow("Oakland", "Building and permit review contracted to a private engineering firm; no synthetic-turf code found", "Town hall; see the town page", town="oakland"),
                     jrow("Apopka", "Own Building Safety Division; no synthetic-turf code found", "407-703-1713", town="apopka")],
                    "Checked against each office's published code September 2026. The nine cities without their own line here haven't been researched individually; the state standard in the two right-hand columns above still sets the floor everywhere in the county.")),
        sec("Distance from our Kissimmee crew to Orange County towns", "<p>All figures below are straight-line distance from downtown Kissimmee.</p>"
            + table("Distance from Kissimmee: Orange County towns", DIST_HEAD,
                    [drow(s) for s in ["hunters-creek", "meadow-woods", "southchase", "lake-nona", "dr-phillips", "belle-isle", "oak-ridge", "pine-castle", "edgewood", "conway", "windermere", "horizon-west", "orlando", "azalea-park", "gotha", "pine-hills", "ocoee", "alafaya", "winter-garden", "winter-park", "avalon-park", "union-park", "maitland", "oakland", "apopka"]],
                    "Distances are measured as the crow flies from downtown Kissimmee, not by road, and Orange County has the longest list of any county on this page.")),
        "<!--AUTO:county-cities-->",
    ])
    faqs = [
        faq("What should you check before hiring the best artificial grass installer near you in Orange County?",
            "Ask whether the crew already knows Orlando's engineering-permit rule is different from the rest of the county, since that changes what paperwork a job needs before anything gets installed. Beyond that, the same checks apply everywhere: base depth, product name and face weight, and infill type in writing."),
        faq("Is Lake Nona covered by Orlando's turf ordinance or the county's?",
            "It depends on the exact address. Some Lake Nona parcels sit inside Orlando's city limits and others are unincorporated Orange County right next to them, so the two rules can apply on the same street. A parcel search on the county property appraiser's site settles which office actually has a given lot."),
        faq("Does a Hunters Creek HOA follow the same visibility rule as any other Florida association?",
            "Yes. Florida Statute 720.3045 doesn't carve out an exception for a specific community, so a fenced Hunters Creek backyard that can't be seen from the street or an adjacent lot gets the same protection as one anywhere else in the state. A front yard, or a yard visible from a neighbor's window, is a separate conversation."),
        faq("Which water district covers Winter Garden and Apopka?",
            "The St. Johns River Water Management District, along with most of the rest of Orange County outside its southeastern edge. Both cities also run their own water utilities, so the specific watering days come from the local bill rather than the district's regional schedule alone."),
        faq("Does Windermere's lake-heavy geography add to the state's 10-foot waterbody setback?",
            "Nothing published sets a Windermere-specific number beyond the state figure. The 10-foot setback from a pond, lake or canal applies the way it would on any other Florida lakefront lot, unless a seawall or bulkhead already stands between the yard and the water."),
    ]
    return page("/areas/orange-county/", "county",
                "Artificial Turf in Orange County, FL (2026 Guide)",
                "Synthetic turf installation, code findings, water rules and soil facts for Orange County, FL, from Hunters Creek to Orlando and Apopka. Checked September 2026.",
                "Artificial turf across Orange County",
                capsule(f"We install, repair and clean synthetic turf across Orange County, from Hunters Creek and Lake Nona through Orlando to Apopka, at the same {price('residential')} per square foot Central Florida range as of September 2026. The urbanized two-thirds of the county sits inside our roughly 40-mile radius from Kissimmee; the rural northeast corner runs past it. Orlando is the one city here with its own written turf rule."),
                body, faqs=faqs, crumbs=CRUMBS, crumb="Orange County", county="orange",
                sources=["dep-rule", "fs125572", "usda-wss", SJRWMD_ORANGE, SFWMD_WHO, SFWMD_KISS, OC_UTIL],
                related=[("/laws/permits/city-of-orlando/", "Orlando's artificial-turf permit rules"), ("/laws/permits/orange-county/", "Orange County permit rules for turf"), ("/areas/hunters-creek/", "Artificial turf in Hunters Creek"), (COST, "Full turf cost guide"), ("/blog/artificial-turf-for-balconies-rooftops-and-condos/", "Turf for balconies, rooftops and condos")])


# ============================================================== Polk
def polk():
    body = "".join([
        sec("Turf work on the Polk County side of our service area",
            f"<p>Polk County is the widest single county we cover, and the part of it we reach starts at Davenport and runs out to Lakeland, Bartow and Frostproof, all still inside the roughly 40-mile radius from Kissimmee. Installed turf here runs the same {price('residential')} per square foot Central Florida range as everywhere else in our area, checked as of September 2026; the citrus country south of Frostproof and Fort Meade sits past that radius and outside what we normally quote.</p>"
            + f"<p>The county's housing splits between full-time homes in the older lake towns and the vacation-home corridor along US 27 near Davenport and Championsgate, where {svc('str', 'rental-home turf')} takes more daily foot traffic than a family lawn ever does. A putting green or a pet run behind one of the ridge's citrus-grove-turned-subdivision lots is a natural fit for {svc('putting', 'backyard putting greens')} or {svc('pet', 'pet turf')} alike.</p>"),
        sec("How far Polk County towns sit from Kissimmee",
            "<p>Distance is straight-line from downtown Kissimmee, and it doesn't change what a job costs.</p>"
            + table("Distance from Kissimmee: Polk County towns", DIST_HEAD,
                    [drow(s) for s in ["davenport", "haines-city", "dundee", "lake-alfred", "polk-city", "winter-haven", "auburndale", "lake-wales", "lakeland", "bartow", "frostproof"]],
                    "Figures are a straight line from downtown Kissimmee, and Lakeland, Bartow and Frostproof sit right at the edge of what we'll drive out for.")),
        sec("Who handles turf permits in Polk County",
            "<p>Polk County's own Land Development Code has no synthetic-turf section, and none of the eleven incorporated cities inside it has been checked individually for one beyond the county seat's own general rules. That leaves the state's May 2026 standard as the only written turf-specific rule reaching a Polk County lot, city or unincorporated, until a specific office says otherwise.</p>"
            + table("Who reviews a synthetic turf job in Polk County",
                    ["Jurisdiction", "What we found on synthetic turf", "Office to call", "Permit page"],
                    [jrow("Polk County (unincorporated)", "No turf-specific section in the Land Development Code", "Building Division, 863-534-6080", "polk-county"),
                     jrow("Davenport", "Own Building & Planning Department inside the city limits; the surrounding unincorporated area is Polk County", "863-419-3300", town="davenport"),
                     jrow("Haines City", "Own Development Services Building Division; no synthetic-turf code found", "863-421-3600", town="haines-city"),
                     jrow("Dundee", "Own Development Services (Building) Department; applications by emailed form", "863-438-8330", town="dundee"),
                     jrow("Lake Alfred", "Own Building Inspection Division; no synthetic-turf code found", "863-291-5748", town="lake-alfred"),
                     jrow("Polk City", "No building department of its own; Polk County's Building Division reviews permits inside the city limits", "Polk County, 863-534-6080", town="polk-city"),
                     jrow("Winter Haven", "Own Building & Permitting Division; no synthetic-turf code found", "863-291-5695", town="winter-haven"),
                     jrow("Auburndale", "Own Construction Services division; no synthetic-turf code found", "863-965-5530", town="auburndale"),
                     jrow("Lake Wales", "Own Building Division; no synthetic-turf code found", "863-676-5115", town="lake-wales"),
                     jrow("Lakeland", "Own Building Inspection Division; no synthetic-turf ordinance found", "863-834-6012", town="lakeland"),
                     jrow("Bartow", "Own Building Department; no synthetic-turf ordinance found", "863-534-0157", town="bartow"),
                     jrow("Frostproof", "Own Building Department; applications by email, no full portal", "863-635-7854", town="frostproof")],
                    "Checked against the county's published code September 2026. Cities with a “Town page” link were checked individually when their pages were written; cities marked “not individually researched” haven't been; call ahead rather than assume any of them matches the county's silence.")),
        sec("The Lake Wales Ridge under a Polk County yard",
            f"<p>Once the ground rises toward Lake Wales, Winter Haven and the ridge running through the county's middle, the soil changes from flatwoods sand to Candler series: excessively drained, very rapid to rapid permeability, built from thick wind-blown and marine sand deposits with slopes running from flat up to 12 percent in most spots ({ext(CANDLER_OSD[1], 'USDA’s official series description')}). That kind of ground barely holds water at all, which sounds like an advantage until a crew is trying to compact a stable base on sand that shifts before the plate compactor finishes a pass.</p>"
            + f"<p>Ridge lots also bring real slope into the picture in a way flatter Osceola or Orange yards rarely do, since a subdivision built into old citrus grove terrain can carry several feet of grade change across one backyard. That changes anchoring and drainage planning more than it changes the turf itself.</p>"),
        sec("Water and irrigation rules in Polk County",
            f"<p>A Phase III shortage declaration from the Southwest Florida Water Management District has held Polk County Utilities customers to a single overnight watering slot since February 2026, with the qualifying night keyed to whether the house number is odd or even. Because an emergency order like that can loosen or tighten with little notice, {ext(POLK_UTIL[1], "the current status page")} is worth checking directly instead of relying on a number printed here. Several of the larger cities, including Lakeland and Winter Haven, bill and schedule their own water rather than buying through the county, so the specific days for a given address depend on which utility sends the bill.</p>"
            + f"<p>The western and central county, Lakeland, Bartow, Winter Haven and Auburndale included, sits under the Southwest Florida Water Management District. The northeast corner, toward Haines City, Davenport and the Four Corners line, falls inside the South Florida Water Management District's Kissimmee Basin planning area instead, the same district that covers most of Osceola County next door ({ext(SFWMD_KISS[1], 'SFWMD’s Upper Kissimmee Basin plan')}; {ext(SFWMD_WHO[1], 'SFWMD’s county list')}). Whichever district applies, a capped synthetic lawn stops needing either schedule the day the state rule's irrigation ban takes effect on that yard.</p>"),
        "<!--AUTO:county-cities-->",
    ])
    faqs = [
        faq("Searching for the best artificial turf company near me in Polk County? Start with these checks.",
            "Confirm the crew measures square footage on site rather than off a listing photo, asks about which side of the county's water-district line a lot sits on before quoting irrigation work, and puts base depth and infill type in writing. A company that skips straight to a number without those questions is worth a second call before hiring."),
        faq("Is Four Corners, near Disney, inside Polk County or Osceola County?",
            "Both, depending on the exact parcel. Four Corners sits across the Osceola-Polk-Lake line, so a subdivision entrance can be in one county while a house two streets over is in another. A property appraiser search for the specific address is the only reliable way to know which building department applies."),
        faq("Does the Lake Wales Ridge's fast-draining sand mean a yard never needs a compacted base?",
            "No. Fast drainage keeps water from pooling, but it doesn't hold a flat, stable surface on its own, which is what the compacted base is actually for. A ridge lot still gets 2 to 4 inches of washed crushed rock, just with extra attention to keeping loose native sand from working up through it on a slope."),
        faq("Are Haines City and Davenport in the same water management district as Lakeland?",
            "No. Lakeland answers to the Southwest Florida Water Management District, while Haines City and Davenport, in the county's northeast corner, fall under the South Florida Water Management District's Kissimmee Basin area instead. The two districts set separate watering schedules for the properties each one covers."),
        faq("Does a vacation home near US 27 need different turf than a full-time house in Polk County?",
            "Not a different product, but a different plan for it. A rental home in the Davenport-Championsgate corridor sees more strangers walking the yard between bookings than a family home does, which is an argument for a denser, higher-face-weight product over the cheapest option in the range, even though the same crew and base method apply either way."),
        faq("Is Lakeland or Bartow too far from Kissimmee for a quote to make sense?",
            "Not usually. Both sit close to the outer edge of our roughly 40-mile radius, at 37 and 38 miles respectively, so a job there is still within reach; it just gets scheduled alongside other Polk County stops on the same day rather than as a standalone trip."),
    ]
    return page("/areas/polk-county/", "county",
                "Artificial Turf in Polk County, FL (2026 Guide)",
                "Synthetic turf installation, permits, the Lake Wales Ridge soil and water rules for Polk County, FL, from Davenport to Lakeland. Checked September 2026.",
                "Artificial turf across Polk County",
                capsule(f"We install, repair and clean synthetic turf across the Polk County towns within reach of Kissimmee, from Davenport out to Lakeland, Bartow and Frostproof, at the same {price('residential')} per square foot range as the rest of Central Florida, checked as of September 2026. That stretch sits inside our roughly 40-mile radius; the citrus country south of Frostproof runs past it. The Lake Wales Ridge's sandy soil changes how a base gets built here."),
                body, faqs=faqs, crumbs=CRUMBS, crumb="Polk County", county="polk",
                sources=["dep-rule", "fs125572", CANDLER_OSD, POLK_UTIL, SFWMD_KISS, SFWMD_WHO],
                related=[("/laws/permits/polk-county/", "Polk County permit rules for turf"), ("/areas/davenport/", "Artificial turf in Davenport"), ("/areas/haines-city/", "Artificial turf in Haines City"), (COST, "Full turf cost guide"), ("/blog/artificial-turf-on-a-slope/", "Installing artificial turf on a slope")])


# ============================================================== Lake
def lake():
    body = "".join([
        sec("Artificial turf in Lake County",
            f"<p>The part of Lake County we reach is its southern edge: Montverde, Clermont and Minneola closest in, Groveland and Mascotte a bit further, Mount Dora at the outer limit. Installed turf runs {price('residential')} per square foot as of September 2026, the same Central Florida range as the rest of our area. That southern strip sits inside our roughly 40-mile radius; Leesburg and the county's northern lakes, past Mount Dora, run beyond it.</p>"
            + f"<p>South Lake's terrain is hillier than anywhere else we work, which changes how a {a('/artificial-grass-installation/', 'residential lawn conversion')} gets planned more than it changes the finished lawn. A shaped subbase handles moderate grade on its own; a steeper slope needs terracing or extra anchoring at the bottom edge before turf goes down.</p>"),
        sec("Two water districts, one Lake County yard",
            f"<p>Lake County is genuinely split, and it's worth knowing which side a lot falls on before assuming a watering schedule. Roughly the southern and western edge of the county, around Groveland, Mascotte and the southwest corner of Clermont, sits inside the Southwest Florida Water Management District's Green Swamp area, a small but distinct slice of the county's total footprint ({ext(LAKE_PLAN[1], 'Lake County’s own water supply plan')}; {ext(GREEN_SWAMP[1], 'Florida DEP’s Green Swamp overview')}). The rest of the county, including Mount Dora and most of Clermont, answers to the St. Johns River Water Management District instead, which runs a seasonal odd/even schedule and was under a tightened Phase III shortage order in 2026 ({ext(SJRWMD_RESTRICT[1], 'SJRWMD’s current restrictions')}). That Green Swamp line is about land conservation and drainage, not watering days: the city utilities in Clermont, Minneola, Groveland and Mascotte all publish irrigation schedules under the St. Johns district's rule, so inside those cities go by the city's own page rather than the district map.</p>"
            + f"<p>Clermont and Minneola both run their own water utilities rather than buying through the district, so a specific address's watering days come off the local bill. None of it matters once a synthetic lawn's irrigation heads are capped, which {a(HB683, 'the state’s May 2026 turf rule')} requires regardless of which district or utility serves the property.</p>"),
        sec("Lake County housing, from Clermont's hills to Mount Dora's oaks",
            f"<p>Clermont and Minneola have grown fast over the last decade, filling hillsides with newer subdivisions where a sloped backyard is closer to the rule than the exception. South of both, a run of 55-plus communities has spread through Minneola and Groveland, where low-maintenance yards and {svc('putting', 'a small putting green')} come up more often than a full-size lawn. Mount Dora sits at the other end of the spectrum: an older, historic lake town with mature oak canopy over narrow lots, where the state's drip-line rule and its certified-arborist exception matter on almost every job.</p>"
            + f"<p>{post('artificial-turf-for-55-plus-communities', 'This article')} covers what changes, and what doesn't, when a community's HOA also happens to be an age-restricted one.</p>"),
        sec("Sand on the ridge: Lake County's soil",
            f"<p>South Lake County sits on the same ridge system as Polk's Lake Wales Ridge, and its defining soil, Astatula, was actually first described and named right here in Lake County, in 1970. It's excessively drained with very rapid permeability, built from more than seven feet of sandy marine and windblown deposits, on slopes that can run from flat up to 30 percent in the hillier stretches ({ext(ASTATULA_OSD[1], 'USDA’s official series description')}). Candler sand, the same series common on Polk's ridge, also turns up on parts of the same landscape.</p>"
            + f"<p>That kind of ground drains almost as fast as the turf sitting on top of it, which is unusual for Central Florida and worth mentioning on a bid: the base's job here is less about fighting a high water table, the way it is in Osceola or Seminole, and more about holding a stable, level surface on sand that wants to shift on its own.</p>"),
        sec("Who reviews a Lake County turf permit",
            "<p>Lake County's own Land Development Regulations don't mention synthetic turf, and the six incorporated towns closest to our service area haven't each been checked individually for a rule of their own.</p>"
            + table("Who reviews a synthetic turf job in Lake County",
                    ["Jurisdiction", "What we found on synthetic turf", "Office to call", "Permit page"],
                    [jrow("Lake County (unincorporated)", "No mention in the Land Development Regulations", "Building Services, 352-343-9653", "lake-county"),
                     jrow("Clermont", "Own Building Services division; no synthetic-turf code found", "352-241-7315", town="clermont"),
                     jrow("Minneola", "Own Building Department (staffed through a contracted provider); no synthetic-turf code found", "352-394-3598", town="minneola"),
                     jrow("Montverde", "Town hall takes permit applications and contracts inspections to a private firm; Bella Collina is unincorporated Lake County", "Town hall; see the town page", town="montverde"),
                     jrow("Groveland", "Own Building & Permitting division; no synthetic-turf code found; irrigation days set under SJRWMD", "352-429-2141", town="groveland"),
                     jrow("Mascotte", "Building-official work contracted to a private engineering firm; no synthetic-turf code found", "352-557-8888", town="mascotte"),
                     jrow("Mount Dora", "Runs its own permitting; not individually researched", "City hall; call before starting")],
                    "Checked against the county's published regulations September 2026. Each city runs permitting separately from the county; confirm directly rather than assuming the county's silence carries over.")),
        sec("Distance from Kissimmee to Lake County towns", "<p>Figures are straight-line distance from downtown Kissimmee.</p>"
            + table("Distance from Kissimmee: Lake County towns", DIST_HEAD,
                    [drow(s) for s in ["montverde", "clermont", "minneola", "groveland", "mascotte", "mount-dora"]],
                    "These are straight-line miles, not road miles, and Mount Dora sits closest to where our roughly 40-mile radius runs out.")),
        "<!--AUTO:county-cities-->",
    ])
    faqs = [
        faq("How do you pick the best turf installer near you in Lake County?",
            "Ask how they'd handle a sloped backyard specifically, since a flat-lot answer doesn't cover terracing or edge anchoring on a grade. Beyond that, the standard checklist applies everywhere: measured square footage, named base material and depth, and infill type spelled out on the quote rather than left as “premium turf, installed.”"),
        faq("Why do Minneola and Groveland answer to a different water district than Mount Dora?",
            "Geography, mostly. The southwestern edge of Lake County drains toward the Green Swamp and falls under the Southwest Florida Water Management District, while Mount Dora and most of the rest of the county drain toward the St. Johns River system instead. The boundary runs through the middle of the county rather than along a city line."),
        faq("Are Clermont's rolling hills actually harder to turf than a flat yard elsewhere?",
            "The material and the crew are the same. What changes is the base plan: a hillside lot often needs the bottom edge of a slope anchored more tightly than the top, since gravity and rainfall runoff both concentrate there, and a steep enough grade can call for a terraced section instead of one continuous run."),
        faq("Is south Lake County's sand the same as what's under a Kissimmee lawn?",
            "No. Kissimmee and most of Osceola County sit on flatwoods soils like Myakka and Immokalee, which hold water near the surface. South Lake's Astatula and Candler sands drain almost immediately and barely hold water at all, which is close to the opposite problem for a base to solve."),
        faq("How far is Mount Dora from your Kissimmee base, and is it still worth a quote?",
            "About 38 miles by straight line, near the outer edge of the roughly 40-mile radius we work within. A job there is still workable; it typically gets scheduled with other Lake County stops on the same trip rather than as its own visit."),
        faq("Do Lake County's 55-plus communities near Clermont and Minneola follow a different turf rule?",
            "No. The state's turf standard and Florida's HOA-visibility statute both apply the same way regardless of a community's age restriction. What changes in a 55-plus neighborhood is usually the yard itself: smaller, easier to maintain, and more likely to include a small putting green than a play area."),
    ]
    return page("/areas/lake-county/", "county",
                "Artificial Turf in Lake County, FL (2026 Guide)",
                "Synthetic turf installation, the Astatula ridge soil, split water districts and permits for south Lake County, FL. Checked September 2026.",
                "Artificial turf across Lake County",
                capsule(f"We install, repair and clean synthetic turf across south Lake County, from Montverde and Clermont out to Groveland, Mascotte and Mount Dora, at the same {price('residential')} per square foot range as the rest of Central Florida, checked as of September 2026. That stretch sits inside our roughly 40-mile radius; the county's northern lakes run past it. Lake County is split between two water management districts."),
                body, faqs=faqs, crumbs=CRUMBS, crumb="Lake County", county="lake",
                sources=["dep-rule", "fs125572", "fs7203045", ASTATULA_OSD, LAKE_PLAN, GREEN_SWAMP, SJRWMD_RESTRICT],
                related=[("/laws/permits/lake-county/", "Lake County permit rules for turf"), ("/areas/clermont/", "Artificial turf in Clermont"), ("/areas/minneola/", "Artificial turf in Minneola"), (COST, "Full turf cost guide"), ("/blog/artificial-turf-for-55-plus-communities/", "Turf in 55-plus communities")])


# ============================================================== Seminole
def seminole():
    body = "".join([
        sec("Artificial turf in Seminole County",
            f"<p>Seminole is Florida's second-smallest county by land area, and nearly all of it is already inside a city limit, which makes it the most fully built-out county we serve. Installed turf runs {price('residential')} per square foot as of September 2026, matching the rest of Central Florida. Every town we list below, Sanford included at 36 miles, sits inside our roughly 40-mile radius from Kissimmee.</p>"
            + f"<p>The county's housing leans toward older, established neighborhoods more than new construction: Altamonte Springs, Casselberry and Longwood were largely built out by the 1980s, so mature landscaping and {a(HOA, 'an HOA’s architectural review')} come up more often than in a still-growing subdivision. Oviedo and Winter Springs, on the county's east side, carry more recent family subdivisions, the kind where {svc('pool', 'turf around a pool cage')} and {svc('pet', 'pet turf for a fenced yard')} tend to fit best.</p>"),
        sec("Who reviews a turf job in a Seminole County city",
            "<p>Unincorporated Seminole County is the exception here rather than the rule, since most addresses fall inside one of the county's seven cities. None of them, or the county itself, has published a synthetic-turf-specific rule as of September 2026.</p>"
            + table("Who reviews a synthetic turf job in Seminole County",
                    ["Jurisdiction", "What we found on synthetic turf", "Office to call", "Permit page"],
                    [jrow("Seminole County (the limited unincorporated area)", "No turf-specific section in the Land Development Code", "Building Division, 407-665-7050", "seminole-county"),
                     jrow("Altamonte Springs", "Own Building and Fire Safety Department; no synthetic-turf code found", "407-571-8446", town="altamonte-springs"),
                     jrow("Casselberry", "Own Building Division; no synthetic-turf code found", "407-262-7700", town="casselberry"),
                     jrow("Oviedo", "Own Building Division; no synthetic-turf code found", "City hall; see the town page", town="oviedo"),
                     jrow("Winter Springs", "Own Building Division; no synthetic-turf code found", "City hall; see the town page", town="winter-springs"),
                     jrow("Longwood", "Own Building Division; no synthetic-turf code found", "407-260-3486", town="longwood"),
                     jrow("Lake Mary", "Own Building Division; no synthetic-turf code found", "407-585-1361", town="lake-mary"),
                     jrow("Sanford", "Own Building Division; no synthetic-turf code found", "407-688-5150", town="sanford")],
                    "Checked against the county's published code September 2026. If an address isn't inside one of the seven cities above, it's worth confirming with the county rather than assuming which office applies.")
            + f"<p>Because so little of the county sits outside a city, {a(PERMITS_HUB, 'our permit hub')} and the county's own page are more useful here as a baseline for the state rule than as a guide to a specific office; the city that actually has a given parcel is the one to call first.</p>"),
        sec("What Seminole County yards look like",
            f"<p>Sanford's historic riverfront neighborhoods carry some of the oldest oak canopy in our whole service area, old enough that a drip-line question comes up on a large share of jobs there, not just the occasional one. Altamonte Springs and Casselberry, built out a generation earlier than Oviedo or Winter Springs, run more established, fenced backyards where {svc('pet', 'pet turf')} for a dog run is a common ask. Lake Mary's newer neighborhoods, closer to the county's office parks, lean toward tidy, low-maintenance front yards more than large backyard lawns.</p>"
            + f"<p>{post('oak-leaves-and-debris-on-artificial-turf', 'This post')} covers what an oak canopy like Sanford's actually does to a turf lawn over a season, beyond just the drip-line permitting question.</p>"),
        sec("Distance from Kissimmee to Seminole County towns", "<p>Every figure below is a straight line from downtown Kissimmee, not a drive time.</p>"
            + table("Distance from Kissimmee: Seminole County towns", DIST_HEAD,
                    [drow(s) for s in ["altamonte-springs", "casselberry", "oviedo", "winter-springs", "longwood", "lake-mary", "sanford"]],
                    "All seven Seminole County towns we list sit closer to Kissimmee than several Polk and Lake County stops do.")),
        sec("Water rules in Seminole County",
            f"<p>Most of Seminole County falls under the St. Johns River Water Management District, which runs a seasonal schedule, two days a week during daylight saving months and one day the rest of the year, tightened under a Phase III shortage declaration in 2026 ({ext(SJRWMD_RESTRICT[1], 'SJRWMD’s current restrictions')}). Almost none of the county's cities buy water from the same source, though: Sanford, Altamonte Springs, Casselberry, Oviedo, Winter Springs and Longwood each bill and schedule their own utility, so the district's regional number is a starting point, not the final answer for a specific address.</p>"
            + f"<p>Whichever city's schedule applies, it stops being relevant to a synthetic lawn the day its irrigation heads are capped, since {a(HB683, 'the state’s turf rule')} bars using an in-ground system on synthetic turf regardless of local watering days.</p>"),
        sec("Soil under a Seminole County lawn",
            f"<p>Seminole sits in the same flatwoods belt as Osceola County and east Orange: Myakka, Immokalee, Basinger and Smyrna fine sands, with a water table that can rise within a few feet of the surface during the summer rainy season ({src('usda-wss', 'USDA Web Soil Survey')}). That's a wetter, slower-draining profile than the ridge sand under a Lake or Polk County yard, which is exactly why the base recipe leans so heavily on washed, open-graded rock instead of anything with fines that could bind into a crust.</p>"),
        "<!--AUTO:county-cities-->",
    ])
    faqs = [
        faq("What makes a search for the best synthetic grass contractor near me in Seminole County worth narrowing down?",
            "Whether the contractor already treats an old oak-canopied Sanford lot differently from a newer Oviedo subdivision. Both need the same base and materials, but a mature canopy adds a drip-line question a newer yard usually doesn't have, and an installer who raises it unprompted has clearly thought about the specific lot."),
        faq("Since most of Seminole County is inside a city, does the county's own permit page even apply to me?",
            "Only if the specific address is in the small unincorporated area outside all seven cities. Most Seminole addresses answer to a city building department instead, so checking which city actually has a parcel matters more here than in a county with a large unincorporated share."),
        faq("Do Sanford's older, oak-lined neighborhoods complicate a turf install?",
            "Sometimes, yes. A canopy that's been growing for decades often reaches further than a homeowner expects, which can put more of a small lot inside a drip line than it first appears. Marking where branch tips actually end, not just eyeballing the trunk, is the first step before planning where turf can go."),
        faq("Is Lake Mary's soil the same flatwoods sand as the rest of Seminole County?",
            "Largely yes, though a newer subdivision there is more likely to sit on fill brought in during construction than on undisturbed native sand. Either way, the base still calls for washed, open-graded crushed rock rather than compacted fill, since fill with fines in it drains worse than the sand it replaced."),
        faq("Are Winter Springs and Oviedo far enough from Kissimmee to change the price?",
            "No. Both are about 29 miles away by straight line, and the published Central Florida price range doesn't move with distance. What can move a quote is access, an HOA submittal, or how much of the yard sits inside a tree's drip line, not the town's name."),
        faq("Does every Seminole County city buy water from the same utility?",
            "No. Sanford, Altamonte Springs, Casselberry, Oviedo, Winter Springs and Longwood each run or contract their own water service and set their own watering days, so two neighboring cities can be on different schedules even though both sit in the same water management district."),
    ]
    return page("/areas/seminole-county/", "county",
                "Artificial Turf in Seminole County, FL (2026 Guide)",
                "Synthetic turf installation, permits, oak-canopy drip lines and water rules for Seminole County, FL, from Sanford to Oviedo. Checked September 2026.",
                "Artificial turf across Seminole County",
                capsule(f"We install, repair and clean synthetic turf across Seminole County, Florida's second-smallest county by land area, at the same {price('residential')} per square foot Central Florida range as of September 2026. Every Seminole town in our service list, Sanford included, sits inside our roughly 40-mile radius from Kissimmee. Nearly the whole county is already inside a city limit."),
                body, faqs=faqs, crumbs=CRUMBS, crumb="Seminole County", county="seminole",
                sources=["dep-rule", "fs125572", "usda-wss", SJRWMD_RESTRICT],
                related=[("/laws/permits/seminole-county/", "Seminole County permit rules for turf"), ("/areas/sanford/", "Artificial turf in Sanford"), ("/areas/oviedo/", "Artificial turf in Oviedo"), (COST, "Full turf cost guide"), ("/blog/oak-leaves-and-debris-on-artificial-turf/", "Oak leaves and debris on artificial turf")])


def get_pages():
    return [osceola(), orange_co(), polk(), lake(), seminole()]
