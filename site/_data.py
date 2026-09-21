# -*- coding: utf-8 -*-
"""Single source of truth for kissimmeeartificialturf.com. Nothing here is invented:
facts carry a source id (see SOURCES) and the date they were checked."""
import math

DOMAIN = "kissimmeeartificialturf.com"
BASE_URL = "https://" + DOMAIN
PUBLIC_NAME = "Kissimmee Artificial Turf"
PHONE_E164 = "+16892023710"
PHONE_DISPLAY = "(689) 202-3710"
EMAIL = "hello@" + DOMAIN
OWNER = "Luis Austin"
OWNER_ROLE = "Owner"
LAUNCH_DATE = "2026-09-21"
REVIEWED = "2026-09-21"          # date the facts on the site were last checked
REVIEWED_HUMAN = "September 2026"
OPERA_BRAND = "kissimmee-turf"
OPERA_ENDPOINT = "https://opera-portal.lucianodornfeld18.workers.dev/api/lead"
# Web3Forms access keys are public by design (they only identify the inbox).
# Interim: the owner's existing Kissimmee inbox key; replace with a key created for this domain (docs/OWNER-INPUTS.md).
WEB3FORMS_KEY = "b8ce0919-eef0-4c33-8ffc-421a98e9e410"
CENTER = (28.2920, -81.4076)     # downtown Kissimmee

BUSINESS = {
    "blurb": "Kissimmee Artificial Turf installs, repairs and cleans artificial grass for homes, vacation rentals and businesses in Kissimmee, Osceola County and the towns within about 40 miles.",
    "service_area_short": "Kissimmee, St. Cloud, Celebration, Poinciana, Hunters Creek, Lake Nona, Davenport, Orlando and Central Florida towns within about 40 miles",
}

# ---------------------------------------------------------------- services
# key -> name, route, short, primary keyword, price key, tier-2 / tier-3 availability
SERVICES = {
    "residential": {"name": "Artificial Grass Installation", "nav": "Residential lawns", "route": "/artificial-grass-installation/", "short": "Front and back yards, sod-to-turf conversions, side yards that won't grow grass.", "kw": "artificial grass installation", "price": "residential", "noun": "artificial grass"},
    "pet": {"name": "Pet Turf & Dog Runs", "nav": "Pet turf", "route": "/pet-turf/", "short": "Fast-draining turf, odor-control infill and dog runs built for daily rinsing.", "kw": "pet turf installation", "price": "pet", "noun": "pet turf"},
    "putting": {"name": "Backyard Putting Greens", "nav": "Putting greens", "route": "/putting-greens/", "short": "Contoured putting and chipping greens with fringe, cups and true roll.", "kw": "backyard putting green installation", "price": "putting", "noun": "a putting green"},
    "playground": {"name": "Playground Turf", "nav": "Playground turf", "route": "/playground-turf/", "short": "Cushioned play surfaces with a shock pad sized to the equipment's fall height.", "kw": "playground turf installation", "price": "playground", "noun": "playground turf"},
    "pool": {"name": "Pool & Lanai Turf", "nav": "Pool & lanai turf", "route": "/pool-turf/", "short": "Turf beside pools and inside screen enclosures, where sod never takes.", "kw": "artificial turf around pool", "price": "residential", "noun": "pool-area turf"},
    "str": {"name": "Vacation Rental Turf", "nav": "Vacation rentals", "route": "/vacation-rental-turf/", "short": "Guest-proof yards for short-term rentals, scheduled between bookings.", "kw": "artificial turf for vacation rental homes", "price": "residential", "noun": "rental-home turf"},
    "commercial": {"name": "Commercial Turf", "nav": "Commercial", "route": "/commercial-turf/", "short": "HOA common areas, apartment pet parks, patios, rooftops and storefronts.", "kw": "commercial artificial turf installation", "price": None, "noun": "commercial turf"},
    "sports": {"name": "Sports & Fitness Turf", "nav": "Sports & fitness", "route": "/sports-turf/", "short": "Bocce courts, batting cages, agility lanes and home-gym sled tracks.", "kw": "sports turf installation", "price": None, "noun": "sports turf"},
    "pavers": {"name": "Turf & Pavers", "nav": "Turf & pavers", "route": "/turf-and-pavers/", "short": "Turf ribbons between pavers, stepping-stone paths and driveway strips.", "kw": "turf between pavers", "price": None, "noun": "turf between pavers"},
    "repair": {"name": "Turf Repair", "nav": "Repair", "route": "/turf-repair/", "short": "Open seams, wrinkles, lifted edges, melted spots and drainage fixes.", "kw": "artificial turf repair", "price": None, "noun": "turf repair"},
    "cleaning": {"name": "Turf Cleaning & Maintenance", "nav": "Cleaning", "route": "/turf-cleaning/", "short": "Pet-odor treatment, power brooming, sanitizing and infill top-ups.", "kw": "artificial turf cleaning service", "price": None, "noun": "turf cleaning"},
    "replacement": {"name": "Turf Removal & Replacement", "nav": "Replacement", "route": "/turf-replacement/", "short": "Worn-out turf pulled, base corrected, new surface laid.", "kw": "artificial turf replacement", "price": None, "noun": "turf replacement"},
}
SERVICE_ORDER = ["residential", "pet", "putting", "playground", "pool", "str", "commercial", "sports", "pavers", "repair", "cleaning", "replacement"]
TIER_SERVICES = {
    1: SERVICE_ORDER,
    2: ["residential", "pet", "putting", "playground", "pool", "repair"],
    3: ["residential", "pet", "putting"],
}

# ---------------------------------------------------------------- prices (market ranges, not quotes)
# (low, high, typical_low, typical_high, unit, source ids)
PRICES = {
    "residential": (8, 18, 10, 16, "sq ft installed", ["attampa-cost", "lbs-fl-cost"]),
    "pet": (10, 18, 12, 16, "sq ft installed", ["magnolia-pet-cost", "installartificial-pet"]),
    "putting": (14, 30, 18, 25, "sq ft installed", ["angi-putting", "homeguide-putting"]),
    "playground": (10, 25, 12, 19, "sq ft installed", ["mightygrass-playground"]),
}
PRICE_DATE = "September 2026"
PRICE_LABEL = "Central Florida market range"


def price_range(key, typical=False):
    lo, hi, tlo, thi, unit, _ = PRICES[key]
    return f"${tlo}–${thi}" if typical else f"${lo}–${hi}"


# ---------------------------------------------------------------- sources
SOURCES = {
    "hb683": ("Florida Senate — CS/CS/CS/HB 683 (2025), Construction Regulations", "https://www.flsenate.gov/Session/Bill/2025/683"),
    "fs125572": ("Florida Statutes §125.572 (2025) — synthetic turf on single-family lots", "https://www.flsenate.gov/Laws/Statutes/2025/0125.572"),
    "dep-rule": ("Florida Administrative Code — Rule 62-308.100, Synthetic Turf (effective May 19, 2026)", "https://flrules.org/gateway/RuleNo.asp?id=62-308.100"),
    "dep-rulemaking": ("Florida DEP — Division of Water Restoration Assistance rules and rulemaking", "https://floridadep.gov/wra/wra/content/division-rules-and-rulemaking"),
    "marathon-pr": ("City of Marathon press release, May 25, 2026 — summary of the new state synthetic turf standards", "https://www.ci.marathon.fl.us/sites/default/files/fileattachments/community/page/32998/synthitic_turf.pdf"),
    "fs7203045": ("Florida Statutes §720.3045 — items not visible from the frontage or an adjacent parcel", "https://www.flsenate.gov/Laws/Statutes/2025/720.3045"),
    "fs7203075": ("Florida Statutes §720.3075 — prohibited clauses in association documents", "https://www.flsenate.gov/Laws/Statutes/2025/720.3075"),
    "olg-720": ("The Orlando Law Group — how §720.3045 applies to backyard artificial turf", "https://www.theorlandolawgroup.com/blog/all/astroturf-your-backyard/"),
    "stc-fl": ("Synthetic Turf Council — FAQ: Florida law and synthetic turf", "https://www.syntheticturfcouncil.org/page/florida-law"),
    "ifas-turf": ("UF/IFAS Gardening Solutions — synthetic turfgrass fact sheet", "https://gardeningsolutions.ifas.ufl.edu/pdf/infographics/synthetic-turfgrass.pdf"),
    "toho-days": ("Toho Water Authority — watering days and times", "https://www.tohowater.com/residents-business/watering-days-and-times"),
    "osceola-water-2026": ("WKMG ClickOrlando, July 6, 2026 — Osceola County water conservation ordinance proposal", "https://www.clickorlando.com/news/local/2026/07/06/osceola-county-proposes-water-conservation-ordinance-to-protect-groundwater-supply/"),
    "dbpr": ("Florida DBPR — verify a license", "https://www.myfloridalicense.com/wl11.asp"),
    "attampa-cost": ("Artificial Turf Tampa — installation cost in Florida, 2026 guide", "https://artificialturftampa.com/artificial-turf-installation-cost-florida-2026-guide/"),
    "lbs-fl-cost": ("Lawn by Season — artificial turf cost in Florida, 2026", "https://lawnbyseason.com/artificial-turf-cost/florida"),
    "magnolia-pet-cost": ("Magnolia Turf — how much does pet turf cost", "https://magnoliaturf.com/how-much-does-pet-turf-cost/"),
    "installartificial-pet": ("InstallArtificial — cost of pet-friendly turf, 2026", "https://www.installartificial.com/how/cost-of-pet-friendly-turf"),
    "angi-putting": ("Angi — backyard putting green cost, 2026", "https://www.angi.com/articles/backyard-putting-green-cost.htm"),
    "homeguide-putting": ("HomeGuide — backyard putting green cost, 2026", "https://homeguide.com/costs/backyard-putting-green-cost"),
    "mightygrass-playground": ("Mighty Grass — playground turf cost per square foot, 2026", "https://www.mightygrass.com/playground-turf-cost-per-square-foot-guide/"),
    "angi-turf": ("Angi — artificial grass installation cost, 2026", "https://www.angi.com/articles/how-much-does-artificial-turf-cost.htm"),
    "lawnstarter-cost": ("LawnStarter — artificial grass cost, 2026", "https://www.lawnstarter.com/blog/cost/artificial-grass-price/"),
    "bearcat-10yr": ("Bearcat Turf — natural grass vs. artificial turf, 10-year cost", "https://bearcatturf.com/blog/natural-grass-vs-artificial-turf-10-year-cost/"),
    "attampa-sod": ("Artificial Turf Tampa — turf vs. sod long-term cost", "https://artificialturftampa.com/artificial-turf-vs-sod-long-term-cost-comparison/"),
    "magnolia-heat": ("Magnolia Turf — does artificial grass get too hot? A Florida installer's answer", "https://magnoliaturf.com/artificial-grass-hot/"),
    "horsemans-heat": ("Horsemans Landscape — how hot artificial turf gets in Florida's summer sun", "https://www.horsemanslandscape.com/how-hot-does-artificial-turf-get-in-floridas-summer-sun/"),
    "sgw-faq": ("Synthetic Grass Warehouse — FAQs (drainage rate, heat, pets)", "https://syntheticgrasswarehouse.com/resources/terminology/faqs/"),
    "magnolia-drain": ("Magnolia Turf — artificial grass drainage, a Texas and Florida buyer's guide", "https://magnoliaturf.com/artificial-grass-drainage/"),
    "mtsinai-turf": ("Mount Sinai Institute for Exposomic Research — artificial turf health risks", "https://mountsinaiexposomics.org/artificial-turf/"),
    "watersavers-pfas": ("Watersavers Turf — PFAS-free artificial turf and the 2026 California rule", "https://www.watersaversturf.com/about/artificial-grass-testing/pfas-free-artificial-turf/"),
    "stn-life": ("Synthetic Turf Northwest — how long artificial turf lasts", "https://www.syntheticturfnorthwest.com/how-long-does-turf-last/"),
    "noaa-normals": ("NOAA NCEI — U.S. Climate Normals 1991–2020", "https://www.ncei.noaa.gov/products/land-based-station/us-climate-normals"),
    "usda-wss": ("USDA NRCS — Web Soil Survey", "https://websoilsurvey.nrcs.usda.gov/app/"),
    "census-acs": ("U.S. Census Bureau — American Community Survey (year structure built)", "https://data.census.gov/"),
}

# ---------------------------------------------------------------- counties and cities
COUNTIES = {
    "osceola": {"name": "Osceola County", "route": "/areas/osceola-county/"},
    "orange": {"name": "Orange County", "route": "/areas/orange-county/"},
    "polk": {"name": "Polk County", "route": "/areas/polk-county/"},
    "lake": {"name": "Lake County", "route": "/areas/lake-county/"},
    "seminole": {"name": "Seminole County", "route": "/areas/seminole-county/"},
}
COUNTY_ORDER = ["osceola", "orange", "polk", "lake", "seminole"]

# slug: (name, county, tier, lat, lon, kind)  kind: city | town | cdp | community | neighborhood
_C = {
    "kissimmee": ("Kissimmee", "osceola", 1, 28.2920, -81.4076, "city"),
    "st-cloud": ("St. Cloud", "osceola", 1, 28.2489, -81.2812, "city"),
    "celebration": ("Celebration", "osceola", 1, 28.3253, -81.5331, "community"),
    "poinciana": ("Poinciana", "osceola", 1, 28.1403, -81.4584, "community"),
    "buenaventura-lakes": ("Buenaventura Lakes", "osceola", 1, 28.3358, -81.3531, "community"),
    "hunters-creek": ("Hunters Creek", "orange", 1, 28.3606, -81.4223, "community"),
    "meadow-woods": ("Meadow Woods", "orange", 1, 28.3856, -81.3665, "community"),
    "southchase": ("Southchase", "orange", 1, 28.3931, -81.3834, "community"),
    "lake-nona": ("Lake Nona", "orange", 1, 28.3772, -81.2473, "neighborhood"),
    "four-corners": ("Four Corners", "osceola", 1, 28.3328, -81.6473, "community"),
    "championsgate": ("ChampionsGate", "osceola", 1, 28.2611, -81.6201, "community"),
    "reunion": ("Reunion", "osceola", 1, 28.2767, -81.5895, "community"),
    "davenport": ("Davenport", "polk", 1, 28.1614, -81.6017, "city"),
    "harmony": ("Harmony", "osceola", 1, 28.1897, -81.1476, "community"),
    "dr-phillips": ("Dr. Phillips", "orange", 1, 28.4494, -81.4923, "community"),
    # tier 2
    "narcoossee": ("Narcoossee", "osceola", 2, 28.3300, -81.2400, "community"),
    "orlando": ("Orlando", "orange", 2, 28.5384, -81.3789, "city"),
    "windermere": ("Windermere", "orange", 2, 28.4956, -81.5348, "town"),
    "horizon-west": ("Horizon West", "orange", 2, 28.4336, -81.6226, "community"),
    "winter-garden": ("Winter Garden", "orange", 2, 28.5653, -81.5862, "city"),
    "ocoee": ("Ocoee", "orange", 2, 28.5692, -81.5440, "city"),
    "winter-park": ("Winter Park", "orange", 2, 28.6000, -81.3392, "city"),
    "belle-isle": ("Belle Isle", "orange", 2, 28.4583, -81.3592, "city"),
    "conway": ("Conway", "orange", 2, 28.5028, -81.3306, "community"),
    "edgewood": ("Edgewood", "orange", 2, 28.4861, -81.3723, "city"),
    "pine-castle": ("Pine Castle", "orange", 2, 28.4717, -81.3678, "community"),
    "oak-ridge": ("Oak Ridge", "orange", 2, 28.4711, -81.4245, "community"),
    "alafaya": ("Alafaya", "orange", 2, 28.5280, -81.1868, "community"),
    "avalon-park": ("Avalon Park", "orange", 2, 28.5130, -81.1530, "community"),
    "union-park": ("Union Park", "orange", 2, 28.5670, -81.2390, "community"),
    "azalea-park": ("Azalea Park", "orange", 2, 28.5411, -81.3006, "community"),
    "maitland": ("Maitland", "orange", 2, 28.6278, -81.3631, "city"),
    "altamonte-springs": ("Altamonte Springs", "seminole", 2, 28.6611, -81.3656, "city"),
    "casselberry": ("Casselberry", "seminole", 2, 28.6778, -81.3278, "city"),
    "gotha": ("Gotha", "orange", 2, 28.5278, -81.5231, "community"),
    "oakland": ("Oakland", "orange", 2, 28.5550, -81.6331, "town"),
    "pine-hills": ("Pine Hills", "orange", 2, 28.5578, -81.4534, "community"),
    "apopka": ("Apopka", "orange", 2, 28.6934, -81.5322, "city"),
    "clermont": ("Clermont", "lake", 2, 28.5494, -81.7729, "city"),
    "minneola": ("Minneola", "lake", 2, 28.5744, -81.7462, "city"),
    "montverde": ("Montverde", "lake", 2, 28.6003, -81.6739, "town"),
    "oviedo": ("Oviedo", "seminole", 2, 28.6700, -81.2081, "city"),
    "winter-springs": ("Winter Springs", "seminole", 2, 28.6989, -81.3081, "city"),
    "longwood": ("Longwood", "seminole", 2, 28.7031, -81.3384, "city"),
    "haines-city": ("Haines City", "polk", 2, 28.1142, -81.6179, "city"),
    "winter-haven": ("Winter Haven", "polk", 2, 28.0222, -81.7329, "city"),
    "auburndale": ("Auburndale", "polk", 2, 28.0653, -81.7887, "city"),
    "lake-alfred": ("Lake Alfred", "polk", 2, 28.0920, -81.7234, "city"),
    "dundee": ("Dundee", "polk", 2, 28.0225, -81.6192, "town"),
    "polk-city": ("Polk City", "polk", 2, 28.1825, -81.8240, "city"),
    # tier 3
    "lakeland": ("Lakeland", "polk", 3, 28.0395, -81.9498, "city"),
    "sanford": ("Sanford", "seminole", 3, 28.8003, -81.2731, "city"),
    "lake-mary": ("Lake Mary", "seminole", 3, 28.7589, -81.3178, "city"),
    "mount-dora": ("Mount Dora", "lake", 3, 28.8025, -81.6445, "city"),
    "bartow": ("Bartow", "polk", 3, 27.8964, -81.8431, "city"),
    "lake-wales": ("Lake Wales", "polk", 3, 27.9014, -81.5859, "city"),
    "groveland": ("Groveland", "lake", 3, 28.5580, -81.8512, "city"),
    "mascotte": ("Mascotte", "lake", 3, 28.5783, -81.8868, "city"),
    "frostproof": ("Frostproof", "polk", 3, 27.7459, -81.5306, "city"),
    "kenansville": ("Kenansville", "osceola", 3, 27.8767, -80.9889, "community"),
}


def _miles(lat, lon):
    la1, lo1, la2, lo2 = map(math.radians, (CENTER[0], CENTER[1], lat, lon))
    a = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return 3958.8 * 2 * math.asin(math.sqrt(a))


CITIES = {}
for _slug, (_n, _co, _t, _la, _lo, _k) in _C.items():
    _d = _miles(_la, _lo)
    CITIES[_slug] = {"slug": _slug, "name": _n, "county": _co, "county_name": COUNTIES[_co]["name"], "tier": _t, "kind": _k,
                     "miles": int(round(_d)), "route": f"/areas/{_slug}/"}
CITY_ORDER = sorted(CITIES, key=lambda s: (CITIES[s]["tier"], _miles(_C[s][3], _C[s][4])))


def nearest(slug, n=3, tier_max=3):
    la, lo = _C[slug][3], _C[slug][4]

    def dist(o):
        a, b = _C[o][3], _C[o][4]
        return math.hypot((a - la) * 69.0, (b - lo) * 60.8)
    return sorted([s for s in CITIES if s != slug and CITIES[s]["tier"] <= tier_max], key=dist)[:n]


def city_service_route(city, service):
    return f"{SERVICES[service]['route']}{city}/"
