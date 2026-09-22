# -*- coding: utf-8 -*-
"""Meadow Woods, FL (unincorporated Orange County). Hub + 12 city x service pages.
Research checked September 2026. Local sources are listed in SRC and cited inline with ext()/src()."""
from _data import CITIES
from _helpers import page, capsule, sec, table, faq, a, city, src, ext, price
from _cityservice import cityservice_pages

SLUG = "meadow-woods"
MILES = CITIES[SLUG]["miles"]

# ---------------------------------------------------------------- local source URLs (not in _data.SOURCES)
CENSUS_URL = "https://www.census.gov/quickfacts/fact/table/meadowwoodscdpflorida/PST045224"
WIKI_URL = "https://en.wikipedia.org/wiki/Meadow_Woods,_Florida"
CH24_URL = "https://library.municode.com/fl/orange_county/codes/code_of_ordinances?nodeId=PTIIORCOCO_CH24LABUOPSP"
OCU_URL = "https://www.orangecountyfl.net/watergarbagerecycling/wateringrestrictions.aspx"
OPA_URL = "https://ocpafl.org/"
ANNEX_URL = "https://www.orangecountyfl.net/PlanningDevelopment/Annexation.aspx"
FASTTRACK_URL = "https://fasttrack.ocfl.net/OnlineServices/"
SFWMD_URL = "https://www.sfwmd.gov/our-work/water-supply/upper-kissimmee"
SJRWMD_URL = "https://www.sjrwmd.com/about/maps/"
STR_URL = "https://www.bnbcalc.com/blog/short-term-rental-regulation/orange-county-florida-guide"
WLE_URL = "https://wyndhamlakesestates.org/"
WOODBRIDGE_URL = "https://www.homesbymarco.com/subdivisions/woodbridge-at-meadow-woods-in-orlando-fl"
FAIRWAY_URL = "https://www.homesbymarco.com/subdivisions/fairway-townhomes-at-meadow-woods-in-orlando-fl"
PARK_URL = "https://www.orangecountyfl.net/cultureparks/parks.aspx?m=dtlvw&d=75"
IMMOKALEE_URL = "https://soilseries.sc.egov.usda.gov/OSD_Docs/I/IMMOKALEE.html"
BASINGER_URL = "https://soilseries.sc.egov.usda.gov/OSD_Docs/B/BASINGER.html"

T_CENSUS = ("U.S. Census Bureau -- QuickFacts: Meadow Woods CDP, Florida", CENSUS_URL)
T_WIKI = ("Wikipedia -- Meadow Woods, Florida (population history, sourced to the U.S. Census Bureau)", WIKI_URL)
T_CH24 = ("Orange County Code, Chapter 24, Landscaping, Buffering and Open Space, Municode Library", CH24_URL)
T_OCU = ("Orange County Utilities -- watering restrictions", OCU_URL)
T_OPA = ("Orange County Property Appraiser -- parcel search", OPA_URL)
T_ANNEX = ("Orange County -- Annexation", ANNEX_URL)
T_FASTTRACK = ("Orange County Fast Track Online Services", FASTTRACK_URL)
T_SFWMD = ("South Florida Water Management District -- Upper Kissimmee Basin Water Supply Plan", SFWMD_URL)
T_SJRWMD = ("St. Johns River Water Management District -- Maps", SJRWMD_URL)
T_STR = ("BNBCalc -- Orange County, Florida short-term rental regulation guide", STR_URL)
T_WLE = ("Wyndham Lakes Estates HOA -- community information", WLE_URL)
T_WOODBRIDGE = ("Homes by Marco -- Woodbridge at Meadow Woods subdivision record", WOODBRIDGE_URL)
T_FAIRWAY = ("Homes by Marco -- Fairway Townhomes at Meadow Woods subdivision record", FAIRWAY_URL)
T_PARK = ("Orange County Parks and Recreation -- Meadow Woods Recreation Center/Meadow Woods Park", PARK_URL)
T_IMMOKALEE = ("USDA NRCS -- Official Series Description, Immokalee Series", IMMOKALEE_URL)
T_BASINGER = ("USDA NRCS -- Official Series Description, Basinger Series", BASINGER_URL)

SRC = ["dep-rule", "fs125572", "hb683", "fs7203045", "usda-wss", T_CENSUS, T_WIKI, T_CH24, T_OCU, T_OPA, T_ANNEX,
       T_FASTTRACK, T_SFWMD, T_SJRWMD, T_STR, T_WLE, T_WOODBRIDGE, T_FAIRWAY, T_PARK, T_IMMOKALEE, T_BASINGER]

# ============================================================== hub
_hub_body = "".join([
    sec("An unincorporated community built one subdivision at a time",
        "<p>Meadow Woods has no city hall of its own. It's a census-designated place in unincorporated south "
        f"Orange County, sitting between {city('hunters-creek')} and {city('lake-nona')}, just north of the "
        f"Osceola County line, with {city('southchase')} to the west and Orlando International Airport to the "
        f"east ({ext(WIKI_URL, "Wikipedia's geography summary, sourced to the Census Bureau")}). Downtown "
        f"Kissimmee is about {MILES} miles south. A homeowner typing \"best artificial turf contractor near me "
        "in Meadow Woods\" into a search bar is usually trying to sort out two separate questions at once: which "
        "office signs off on the work, and which HOA board wants a copy of the plan first, since this community "
        "grew as many small subdivisions rather than one planned development.</p>"
        f"<p>The 2020 Census counted 43,790 residents here, a figure that more than quadrupled the 2010 count of "
        f"25,558, which itself had more than doubled the 2000 count of 11,286 ({ext(CENSUS_URL, 'Census Bureau QuickFacts')}; "
        f"{ext(WIKI_URL, 'population history by decade')}). That growth curve is a rough map of when the housing "
        "stock went in: older, smaller lots near the community's core date to the late 1980s, and the largest "
        "share of homes followed during the 1990s and 2000s.</p>"),
    sec("Two approvals, and neither one is automatic",
        f"<p>Because Meadow Woods sits outside every city limit, {a('/laws/permits/orange-county/', "Orange County's Permitting Services and Division of Building Safety")} "
        "reviews a synthetic turf project here, not a municipal building department. County Code Chapter 24 "
        f"defines \"turf, turf grass or sod\" only as living grass species and has no section written for a "
        f"manufactured surface ({ext(CH24_URL, 'Chapter 24, Landscaping, Buffering and Open Space')}), which "
        f"leaves {src('dep-rule', "the state's May 19, 2026 turf standard")} as the only rule written "
        "specifically for the material. The community's east edge, toward Lake Nona, sits close enough to "
        "Orlando's city limits that the boundary is worth checking before assuming which office applies: the "
        "county's own guidance is to read the street sign, since one marked \"Orange\" means unincorporated "
        f"land, and to confirm on the {ext(OPA_URL, "Property Appraiser's parcel search")} "
        f"({ext(ANNEX_URL, "Orange County's annexation page")}). A parcel that comes back inside Orlando "
        f"follows {a('/laws/permits/city-of-orlando/', "Orlando's own artificial-turf permit rule")} instead, "
        "which is a different process with its own engineering-permit step.</p>"
        "<p>None of that settles the second approval. Fairway Townhomes at Meadow Woods went up in 1988 and "
        "1989, Woodbridge at Meadow Woods followed in 1995 and 1996, and Wyndham Lakes Estates, on the "
        "community's east side, organized its own master association in 2005 covering ten subdivisions and "
        f"1,454 homes ({ext(WLE_URL, 'Wyndham Lakes Estates')}; {ext(WOODBRIDGE_URL, 'Woodbridge at Meadow Woods')}; "
        f"{ext(FAIRWAY_URL, 'Fairway Townhomes at Meadow Woods')}). Each of those runs its own architectural "
        "review, alongside smaller associations nearby such as Water's Edge, so a plan approved on one street "
        "says nothing about the next one over. We found no published guideline from any of these boards naming "
        f"synthetic turf specifically, which leaves {a('/laws/hoa-rules/', "the state law limiting what an HOA can restrict")} "
        "as the operative rule: a board can't block turf that isn't visible from the frontage or a neighboring "
        f"lot. {a('/laws/florida-hb-683/', "Florida's 2025 turf law")} caps what a city or county can require "
        f"and has nothing to do with what a board asks for on its own form; the {a('/tools/hoa-packet-checklist/', 'HOA and ARC packet checklist')} "
        "covers what most of these boards want to see before signing off, whichever subdivision is asking.</p>"),
    table("Meadow Woods yard types and what we do differently",
          ["Yard type", "What's typical", "What changes about the turf plan"],
          [["A 1988-89 Fairway Townhomes lot", "Small fenced rear yard sharing a wall with the next unit", "Tight access usually means wheelbarrows instead of a skid steer, and an older base gets checked before new rock goes on top"],
           ["A 1990s single-story pool-cage home", "Screened lanai plus a narrow strip outside the cage", "Turf inside the cage glues down over concrete with a drainage underlay; turf outside grades away from the pool's bond beam"],
           ["A Wyndham Lakes Estates lot built after 2005", "Larger rear yard, sometimes backing a retention pond", "The state's 10-ft waterbody setback and swale exclusion get measured before anything else goes on the plan"],
           ["A yard with mature oaks from the 1990s build-out", "Shade trees close to the house or the property line", "Turf stops short of the drip line unless a certified arborist signs off on the install"],
           ["An HOA entrance island or clubhouse courtyard", "Shared common ground rather than a private lot", "Quoted from the association's own drawings, with the paperwork going to a board instead of a homeowner"]],
          "Yard types are illustrative categories built from the community's documented housing and HOA history, not a survey of any specific address."),
    sec("Flatwoods soil, and two water districts meeting near Boggy Creek",
        "<p>Soils mapped across southern Orange County's flatwoods, the Immokalee and Basinger series among them, "
        "are sandy, nearly level and very poorly to poorly drained, built up in low flats and old drainageways "
        f"rather than a well-drained ridge ({src('usda-wss', "USDA's Web Soil Survey")}; {ext(IMMOKALEE_URL, 'Immokalee series description')}; "
        f"{ext(BASINGER_URL, 'Basinger series description')}). That's a big part of why the two to four inches "
        "of washed, open-graded crushed rock or crushed concrete the state's turf standard requires is doing "
        "real work here: on flat, slow-draining sand, the base is what moves a fast summer storm off the yard, "
        "not gravity.</p>"
        "<p>Meadow Woods also sits close to where two water management districts meet. The county's Upper "
        "Kissimmee Basin, which drains toward Boggy Creek along the community's north side and on to the "
        f"Kissimmee chain of lakes, falls under the South Florida Water Management District, while most of the "
        f"rest of Orange County answers to the St. Johns River Water Management District ({ext(SFWMD_URL, "SFWMD's Upper Kissimmee Basin plan")}; "
        f"{ext(SJRWMD_URL, "SJRWMD's district map")}). Retention ponds are common on the newer lots near that "
        "creek corridor, and the state rule keeps turf at least 10 feet from a pond, lake or canal edge unless "
        "a seawall already separates the two, with no exception for a drainage swale.</p>"),
    sec("Water rules for whatever isn't turf",
        "<p>Orange County Utilities runs water and sewer through most of unincorporated Meadow Woods, on a "
        "seasonal schedule: two watering days a week during daylight saving time, one day a week the rest of "
        f"the year, with no sprinklers running between 10 a.m. and 4 p.m. on any day ({ext(OCU_URL, "Orange County Utilities' watering restrictions page")}; "
        f"the Water Division takes calls at 407-254-9850). None of that schedule reaches a synthetic turf area "
        f"once the heads underneath are capped, something {src('dep-rule')} has required statewide since May "
        "19, 2026; it only governs whatever St. Augustine or Bahia stays around the new turf's edges.</p>"),
    sec("Vacation-rental turf is a smaller share of the work here",
        "<p>Unlike the vacation-home pockets closer to Disney, Meadow Woods isn't zoned for short-term rentals "
        "as a matter of course. Whole-home rentals under 30 nights generally aren't a permitted use in "
        "unincorporated Orange County's residential zoning without a discretionary Special Use Permit, under an "
        f"ordinance that predates the state's 2011 preemption on new local rental bans ({ext(STR_URL, "a 2026 guide to Orange County's short-term rental rules")}). "
        "The county's vacation-home-friendly zoning sits in a handful of zip codes near Disney; Meadow Woods' "
        "own 32824 isn't one of them. So turf built specifically for guest turnover, rather than for the family "
        "living there, comes up less often here than it does closer to the theme parks.</p>"),
    "<!--AUTO:city-services-->",
])

_hub_faqs = [
    faq("Is Meadow Woods part of the City of Orlando or unincorporated Orange County?",
        "Meadow Woods itself is unincorporated Orange County land with no city hall of its own. Its eastern edge toward Lake Nona sits close enough to Orlando's boundary that some nearby parcels are inside city limits; the street sign and the Property Appraiser's parcel record settle which office applies before you plan a permit."),
    faq("Does a Meadow Woods HOA have to approve artificial turf before installation?",
        "Only if that subdivision's covenants require review for exterior changes, which most here do. Florida law only forces a board to allow turf that isn't visible from the street or a neighboring lot; a front yard still goes through whatever architectural process that particular association runs."),
    faq("Is there a Meadow Woods or Orange County rule written specifically for synthetic turf?",
        "No local rule names it. Orange County Code Chapter 24 defines turf only as living grass species, so the only material-specific rule reaching a Meadow Woods yard is the state's Rule 62-308.100, in force since May 19, 2026."),
    faq("Can I install turf for a short-term rental in Meadow Woods?",
        "Only in a limited way. Unincorporated Orange County generally doesn't allow whole-home rentals under 30 nights in residential zoning without a discretionary Special Use Permit, so turf built purely for guest turnover is less common here than near Disney's vacation-home zoning."),
    faq("What water utility serves Meadow Woods, and does it affect a turf job?",
        "Orange County Utilities runs water and sewer through most of the community on a seasonal odd/even watering schedule. That schedule stops applying to a turf area once the irrigation heads underneath are capped, which the state's turf standard requires regardless."),
]

HUB = page("/areas/meadow-woods/", "city",
           "Artificial Turf in Meadow Woods, FL (Orange County)",
           "Artificial turf in Meadow Woods, FL: unincorporated county permits, subdivision HOA approval and flatwoods soil, checked September 2026.",
           "Artificial Turf for Meadow Woods, Florida Yards",
           capsule(
               f"Meadow Woods is unincorporated Orange County land, about {MILES} miles from downtown Kissimmee, "
               "built out mostly between the late 1980s and the mid-2000s across many separate subdivisions "
               "rather than one planned community. The 2020 Census counted 43,790 residents here. A synthetic "
               "turf job answers to Orange County's permit desk, not a city hall, and to whichever homeowners "
               "association runs that particular street."),
           _hub_body, faqs=_hub_faqs, sources=SRC, city=SLUG,
           crumbs=[("Service areas", "/areas/")], crumb="Meadow Woods",
           related=[("/areas/orange-county/", "Service area: Orange County"),
                    ("/laws/permits/orange-county/", "Artificial turf permits in Orange County"),
                    ("/laws/permits/city-of-orlando/", "Artificial turf permits in the City of Orlando"),
                    ("/areas/hunters-creek/", "Artificial turf in Hunters Creek"),
                    ("/areas/southchase/", "Artificial turf in Southchase"),
                    ("/areas/lake-nona/", "Artificial turf in Lake Nona"),
                    ("/areas/buenaventura-lakes/", "Artificial turf in Buenaventura Lakes"),
                    ("/artificial-turf-cost/", "Turf cost tables for Central Florida")])

# ============================================================== local: residential
_residential = {
    "title": "Artificial Grass Installation in Meadow Woods, FL",
    "meta": f"Artificial grass installation in Meadow Woods, FL: unincorporated county permits, per-subdivision HOA approval, and the {price('residential')} sq ft market range, September 2026.",
    "h1": "Artificial Turf for Meadow Woods Front and Back Yards",
    "lede": capsule(
        f"Installed artificial grass in Meadow Woods runs about {price('residential')} per square foot, "
        f"typically {price('residential', True)}, as of September 2026. The install itself is straightforward; "
        "what takes planning is that Orange County's Building Safety office reviews the permit side while "
        "whichever subdivision's HOA runs the architectural side, and those are two separate approvals that "
        "don't come from the same desk."),
    "sections": [
        ("Why the permit and the HOA form come from different offices",
         "<p>A Meadow Woods homeowner planning a lawn conversion is really running two errands, not one. Orange "
         "County's Permitting Services and Division of Building Safety confirms whether the scope of work, "
         "capping a sprinkler zone, regrading a low spot, needs a permit of its own; the county's landscape "
         "code, Chapter 24, was written for living grass species and has no artificial-turf section to point to "
         "either way. Separately, whichever subdivision the lot sits in runs its own architectural review, "
         "since Meadow Woods went up as many individual communities rather than one master-planned "
         "neighborhood. Skipping either step doesn't save time. A crew that starts before the HOA packet clears "
         "risks pulling material back out, and a plumber capping heads without checking whether that trips a "
         "county permit can leave a homeowner explaining unpermitted work at resale.</p>"),
        ("What the flatwoods soil under a Meadow Woods lot means for the base",
         "<p>Flatwoods soil covers most of southern Orange County, and Meadow Woods sits on it: the Immokalee "
         "and Basinger series here run sandy, nearly level and very poorly to poorly drained, built up in low "
         "flats and old drainageways rather than a well-drained ridge. On a lot like that, the two to four "
         "inches of washed, open-graded crushed rock or crushed concrete the state's turf standard requires is "
         "doing real work, since native sand alone won't clear a fast summer storm off a flat yard on its own. "
         "Grading that base one to two percent away from the house, then compacting it firm without crushing "
         "the pore space that lets water pass, matters more on ground like this than it would on a sloped lot "
         "farther north in the county where gravity helps for free.</p>"),
        ("A yard built in phases, not all at once",
         "<p>Meadow Woods grew fast and in waves: the Census counted 4,876 residents here in 1990, 11,286 by "
         "2000 and 25,558 by 2010, and a lot's age tracks that curve almost as reliably as a plat map would. A "
         "yard behind a townhome from the Fairway Townhomes phase, built in 1988 and 1989, usually means a "
         "narrow footprint and an older irrigation line worth inspecting before anything gets capped. A yard in "
         "a section built during the 2000s expansion, closer to Wyndham Lakes Estates, tends to run larger and "
         "sometimes backs up to a retention pond, which brings the state's water-setback rule into the layout "
         "instead of just the base spec.</p>"),
    ],
    "scenario": ("Say you have a 950 sq ft backyard behind a two-story home",
                 "<p>Say you have a 950 sq ft backyard behind a two-story home in a section built after 2005, "
                 "the kind of lot common around Wyndham Lakes Estates. At the "
                 f"{price('residential', True)} typical range, that yard prices between roughly $9,500 and "
                 "$15,200 installed, covering sod removal, a washed-rock base graded away from the house, turf, "
                 "seams, edging and infill. If the lot backs up to one of the subdivision's retention ponds, "
                 "the crew also measures the state's 10-ft waterbody setback before laying anything out, and if "
                 "a live oak sits near the property line, that tree's drip line gets flagged before excavation "
                 "starts, not after. Neither step changes the per-square-foot number; both change where the "
                 "turf's edge actually falls.</p>"),
    "faqs": [
        faq("Does a 1990s Meadow Woods pool-cage lot need anything different?",
            "Usually just a smaller footprint outside the cage and an older irrigation line worth checking before heads get capped. The turf and base spec are otherwise the same as any residential lawn here."),
        faq("Do I need Orange County's approval and my HOA's approval separately?",
            "Generally yes. The county reviews whether the scope of work needs a permit; the subdivision's own board reviews how the finished yard looks. One approval doesn't stand in for the other."),
        faq("Is Meadow Woods soil different from Kissimmee's for a turf base?",
            "Not meaningfully. Both sit on sandy Central Florida flatwoods soil with a seasonally high water table, so the same washed, open-graded rock base and away-from-the-house grading apply on either side of the county line."),
    ],
    "sources": ["dep-rule", "attampa-cost", "lbs-fl-cost", "usda-wss", T_CH24, T_IMMOKALEE, T_BASINGER, T_WIKI, T_WLE],
}

# ============================================================== local: pet
_pet = {
    "title": "Pet Turf and Dog Runs, Meadow Woods FL",
    "meta": f"Pet turf and dog runs in Meadow Woods, FL: zero-lot-line fenced yards, poorly drained flatwoods soil, and the {price('pet')} sq ft market range, September 2026.",
    "h1": "Dog-Ready Turf for Meadow Woods Yards",
    "lede": capsule(
        f"Installed pet turf in Meadow Woods runs about {price('pet')} per square foot, typically "
        f"{price('pet', True)}, as of September 2026. Most of the community's fenced yards are small and share "
        "at least one wall with a neighbor, so a dog run here leans on a deeper base and a faster-draining "
        "backing more than a wide-open lawn ever needs to."),
    "sections": [
        ("Fenced, narrow yards are the norm, not the exception",
         "<p>Homeowners searching for the best pet turf installer near them in Meadow Woods are usually dealing "
         "with the same starting point: a fenced rear or side yard on a lot platted decades ago, sized for a "
         "single-story or attached home rather than a sprawling half-acre. Fairway Townhomes at Meadow Woods, "
         "built in 1988 and 1989, and the smaller lots around Water's Edge share property lines on at least one "
         "side, which limits where a dog can pace and concentrates wear along whichever fence line gets the "
         "most traffic. That layout is exactly why pet-grade backing and a deeper rock base matter more here "
         "than on a wide-open acreage lot: liquid has nowhere to spread out, so it has to move straight down "
         "instead.</p>"),
        ("What the area's poorly drained soil does to an undersized dog run",
         "<p>The Basinger and Immokalee soil series common across southern Orange County's flatwoods are "
         "classed very poorly to poorly drained, sitting in low flats rather than well-drained high ground. "
         "That's a routine condition for a lawn, but it's a bigger factor for a dog run, where rinse water and "
         "urine both need somewhere to go every single day, not just during a storm. A run built to the "
         "standard three to four inches of washed, open-graded rock, rather than the shallower depth a plain "
         "lawn can get away with, is what keeps a Meadow Woods dog yard from turning into a summer odor problem "
         "on ground that was never going to drain quickly on its own.</p>"),
        ("A community with its own dog park nearby",
         f"<p>Meadow Woods Park, the county's 19-acre recreation complex on Rhode Island Woods Circle, runs its "
         f"own fenced dog park alongside its playground and ball fields ({ext(PARK_URL, 'Orange County Parks and Recreation')}). "
         "A public dog park close by doesn't replace a private run, since a shared space means shared germs and "
         "no control over infill or drainage, but it does mean a fair number of households nearby are already "
         "used to giving a dog daily off-leash time, which is part of why a dedicated, easy-to-rinse run at "
         "home is worth the deeper base it takes to build one properly.</p>"),
    ],
    "scenario": ("Say you have a 320 sq ft fenced side yard for two dogs",
                 "<p>Say you have a 320 sq ft fenced side yard behind a townhome in an older Meadow Woods "
                 f"section, running two dogs. At the {price('pet', True)} typical pet-turf range, that run prices "
                 "between roughly $3,840 and $5,120 installed, which covers the deeper washed-rock base, a "
                 "fully permeable backing, and zeolite or coated-sand infill sized for daily rinsing rather than "
                 "occasional rainfall. Because the yard shares a wall with the neighboring unit, the crew also "
                 "plans the drain point to keep rinse water moving toward the yard's own low corner instead of "
                 "toward the shared fence line, which matters more on a narrow lot like this than it would on a "
                 "wide-open half-acre.</p>"),
    "faqs": [
        faq("Do older Meadow Woods yards need a bigger dog run base than newer ones?",
            "The base depth doesn't change with the lot's age, but an older section's existing drainage is worth checking first. A yard that already holds water after a storm needs that corrected before a run goes in, regardless of when the home was built."),
        faq("Is there a public dog park near Meadow Woods for the meantime?",
            "Yes. Meadow Woods Park, the county's recreation complex on Rhode Island Woods Circle, has a fenced dog park along with its playground and athletic fields."),
    ],
    "sources": ["dep-rule", "magnolia-pet-cost", "installartificial-pet", "usda-wss", T_BASINGER, T_IMMOKALEE, T_PARK, T_FAIRWAY],
}

# ============================================================== local: putting
_putting = {
    "title": "Backyard Putting Greens in Meadow Woods, FL",
    "meta": f"Backyard putting greens in Meadow Woods, FL: flat flatwoods lots, larger yards near Wyndham Lakes Estates, and the {price('putting')} sq ft range, September 2026.",
    "h1": "Putting Greens Built for Meadow Woods Lots",
    "lede": capsule(
        f"A backyard putting green in Meadow Woods runs about {price('putting')} per square foot, typically "
        f"{price('putting', True)}, as of September 2026. The community's flat, slow-draining flatwoods ground "
        "is actually an advantage for a green's contours, since a crew shapes them into the base rather than "
        "fighting a natural slope the way a hillside lot in Lake County would require."),
    "sections": [
        ("Flat ground means the contours come from the base, not the lot",
         "<p>The Immokalee and Basinger soils under most of Meadow Woods sit nearly level by nature, part of "
         "the broader flatwoods that cover southern Orange County. For a lawn that's a drainage question; for a "
         "putting green it's actually useful, because a nearly flat starting point means every roll, tier or "
         "false edge on the finished green comes from how the crushed-rock base gets shaped, not from working "
         "around whatever slope the lot already has. The tradeoff is that the same flatness that makes shaping "
         "easier also means the base has to handle drainage entirely on its own, since there's little natural "
         "grade to help water leave the property during a summer storm.</p>"),
        ("Larger lots near Wyndham Lakes Estates fit a bigger layout",
         f"<p>Wyndham Lakes Estates, the master association covering ten subdivisions and 1,454 homes on "
         f"Meadow Woods' east side, was built starting in 2005, later than most of the community, and its "
         "lots tend to run larger than the townhome-scale yards near the older core. A bigger rear yard there "
         "can fit a green with a real chipping fringe and two or three cups instead of a single small putting "
         "surface, though a layout that size still needs the same HOA architectural review any exterior change "
         "gets in that subdivision, since a green with contoured mounding is a more visible change than a flat "
         "lawn swap.</p>"),
        ("Keeping a green's edge away from a retention pond",
         "<p>A number of the newer lots in Meadow Woods back up to a subdivision retention pond, which is where "
         "a putting green's layout runs into the same state rule that governs a lawn: turf stays at least 10 "
         "feet from the pond's edge unless a seawall separates the two, and it can't be routed through a "
         "drainage swale even if that strip looks like the flattest, most convenient spot for an extra cup. "
         "Planning a green's footprint around that setback before shaping any contours avoids relocating "
         "finished grading later.</p>"),
    ],
    "scenario": ("Say you have a 420 sq ft green on a Wyndham Lakes Estates lot",
                 "<p>Say you have a 420 sq ft rear yard on a Wyndham Lakes Estates lot built after 2005, big "
                 f"enough for a green with a short fringe and two cups. At the {price('putting', True)} typical "
                 "range, that project prices between roughly $7,560 and $10,500 installed, covering contoured "
                 "base shaping, fringe turf, the putting surface itself and drainage underneath. If the lot "
                 "backs onto one of the subdivision's ponds, the green's layout gets pulled back from the "
                 "10-ft setback before any contouring starts, and the association's architectural packet gets "
                 "filed alongside the site plan rather than after it.</p>"),
    "faqs": [
        faq("Does Meadow Woods' flat terrain make a putting green cheaper to build?",
            "Not directly on price, since contouring still has to be built into the base either way. It does make the shaping more predictable, because the crew isn't correcting for an existing slope on top of building the green's own contours."),
        faq("Do I need HOA approval for a putting green in a Meadow Woods subdivision?",
            "Almost always, since a contoured green is a visible exterior change most architectural review boards want to see before work starts, separate from any county permit question."),
    ],
    "sources": ["dep-rule", "angi-putting", "homeguide-putting", "usda-wss", T_IMMOKALEE, T_WLE],
}

# ============================================================== local: playground
_playground = {
    "title": "Playground Turf Near Meadow Woods Park",
    "meta": f"Playground turf in Meadow Woods, FL: state infill rules, family lots near Meadow Woods Park, and the {price('playground')} sq ft market range, September 2026.",
    "h1": "Play-Area Turf for Meadow Woods Backyards",
    "lede": capsule(
        f"Playground turf in Meadow Woods runs about {price('playground')} per square foot, typically "
        f"{price('playground', True)}, as of September 2026, with the shock pad's thickness set by the "
        "equipment's fall height. Meadow Woods Park, the county's 19-acre complex on Rhode Island Woods Circle, "
        "gives the area's families a public reference point for what a play surface should feel like at home."),
    "sections": [
        ("A community with young families and a well-used county park",
         f"<p>Meadow Woods Park sits on Rhode Island Woods Circle and runs a play area, ball fields and youth "
         f"programs for the surrounding neighborhoods ({ext(PARK_URL, 'Orange County Parks and Recreation')}). "
         "A community built up mostly between the late 1980s and the mid-2000s, with the Census counting a "
         "population that grew from 11,286 in 2000 to 43,790 by 2020, tends to carry a steady share of young "
         "families through its housing turnover, which is part of why a backyard play surface, not just the "
         "public park, comes up often in Meadow Woods. A home version doesn't have to match a county complex's "
         "scale to be useful; it just has to fit the equipment that's actually going in the yard.</p>"),
        ("Sizing the shock pad to the equipment, not the yard",
         "<p>A playground turf system is really two layers doing different jobs: the turf and infill on top, "
         "and a shock-absorbing pad underneath sized to the fall height of whatever equipment sits on it. A "
         "small swing set needs less pad thickness than a full play structure with a platform several feet off "
         "the ground, so the equipment gets measured before the pad gets ordered, not after. On Meadow Woods' "
         "flat, poorly drained flatwoods soil, that pad sits on the same washed, open-graded rock base as any "
         "other turf project, since a play area still needs the water to leave once a storm passes.</p>"),
        ("What the state rule means for infill under swings and slides",
         "<p>Under Florida's turf standard, a single-family lawn's infill has to stay natural: sand, rock or "
         "shell, or a coated sand whose coating carries no toxicity. A separate carve-out sets rubber and other "
         "manufactured fill aside for exactly one spot, the ground directly beneath playground equipment. That "
         "distinction matters on a Meadow Woods lot where the play area sits right next to open lawn: a "
         "cushioned zone under a swing set can use a rubber or engineered-fiber product, while the turf running "
         "past that footprint back into the rest of the yard has to stay on the natural side of that line.</p>"),
    ],
    "scenario": ("Say you have a 260 sq ft play area behind a starter home",
                 "<p>Say you have a 260 sq ft corner of the backyard behind a single-story starter home from "
                 f"the community's 1990s build-out, set aside for a swing set and a small climbing structure. "
                 f"At the {price('playground', True)} typical range, that area prices between roughly $3,120 "
                 "and $4,940 installed, with the pad thickness set by the equipment's highest platform rather "
                 "than a flat assumption. The rest of the yard outside that footprint stays on standard turf "
                 "and silica infill, since the state's rubber-infill allowance only covers the ground directly "
                 "under the equipment.</p>"),
    "faqs": [
        faq("Can rubber infill go under a whole Meadow Woods backyard, not just the swing set?",
            "No. The state standard limits rubber or other synthetic infill to the footprint under playground equipment specifically; the rest of a residential lawn has to use silica sand, rock, shell or other natural material."),
        faq("Is there a public playground near Meadow Woods to compare surfaces?",
            "Yes. Meadow Woods Park on Rhode Island Woods Circle has a public play area alongside its dog park and ball fields, run by Orange County Parks and Recreation."),
    ],
    "sources": ["dep-rule", "mightygrass-playground", T_PARK, T_WIKI],
}

# ============================================================== local: pool
_pool = {
    "title": "Pool and Lanai Turf, Meadow Woods FL",
    "meta": f"Pool and lanai turf in Meadow Woods, FL: 1990s screen cages, capped irrigation, and the {price('residential')} sq ft market range, as of September 2026.",
    "h1": "Turf for Meadow Woods Pool Cages and Lanais",
    "lede": capsule(
        f"Turf around a Meadow Woods pool or inside a screened lanai runs within the {price('residential')} "
        f"per square foot market range, usually toward the upper half given the glue-down work a cage floor "
        "needs, as of September 2026. Screened pools are common on the community's 1990s and early-2000s "
        "single-story lots, where sod never held up well against the shade and edge of the enclosure anyway."),
    "sections": [
        ("Screened pool cages are a defining feature of the older sections",
         "<p>Woodbridge at Meadow Woods, built in 1995 and 1996, and the surrounding single-story sections from "
         "that same stretch of construction, put up a large share of Meadow Woods' screen-enclosed pools. A "
         "cage that age is old enough that its footing and deck have settled into their final shape, which "
         "matters for turf more than it does for sod: a concrete deck inside the cage takes a glue-down "
         "install with a drainage underlay, and the crew needs a deck that isn't actively shifting for that "
         "adhesive to hold through a Central Florida summer. The narrow strip of ground outside the cage, "
         "where sod usually struggled against the shade line the screen roof casts, is where a standard turf "
         "base goes down instead.</p>"),
        ("Why the irrigation step matters more around a pool cage",
         "<p>A sprinkler zone that used to reach the strip beside a pool cage has to be capped once turf goes "
         "down there, since Florida's turf standard bars watering synthetic turf from an in-ground system "
         "statewide. On a Meadow Woods lot served by Orange County Utilities, that capped zone also drops out "
         "of the utility's seasonal watering-day schedule entirely, which simplifies the yard's water plan "
         "rather than complicating it: fewer zones to track, and the pool deck's turf gets by on an occasional "
         "hose rinse instead.</p>"),
        ("Keeping turf away from a pool's equipment pad and bond beam",
         "<p>The grading question around a pool is different from a plain lawn. Turf outside a cage has to "
         "slope away from the pool's bond beam and stay clear of the equipment pad, both to keep water from "
         "pooling against the shell and to leave the pump and filter reachable for service. On Meadow Woods' "
         "flat, poorly drained flatwoods soil, that grading takes more deliberate planning than it would on a "
         "lot with natural fall away from the structure, since there's little slope already doing that work.</p>"),
    ],
    "scenario": ("Say you have a 480 sq ft pool deck and side strip",
                 "<p>Say you have a 480 sq ft combination of a screened pool deck and a narrow side strip "
                 f"outside the cage, on a single-story home from the 1990s build-out. Within the "
                 f"{price('residential')} market range, that project tends to land in the upper half, roughly "
                 "$13 to $17 a square foot, or about $6,240 to $8,160 installed, because the glue-down work "
                 "inside the cage and the drainage underlay both add labor a flat lawn doesn't need. The "
                 "sprinkler zone that used to reach that strip gets capped as part of the same job, not as a "
                 "separate call later.</p>"),
    "faqs": [
        faq("Does a 1990s Meadow Woods pool cage need special turf preparation?",
            "The deck itself needs checking for settling before turf glues down, but the turf system is otherwise a standard glue-down build over concrete with a drainage underlay, regardless of the cage's age."),
        faq("Does capping irrigation near the pool change my Orange County Utilities bill?",
            "It removes that zone from the watering schedule entirely, since the state rule bars in-ground irrigation on synthetic turf, but it doesn't change the rest of the property's water service."),
    ],
    "sources": ["dep-rule", "attampa-cost", "lbs-fl-cost", T_WOODBRIDGE, T_OCU],
}

# ============================================================== local: str
_str = {
    "title": "Vacation Rental Turf for Meadow Woods Homes",
    "meta": f"Vacation rental turf in Meadow Woods, FL: Orange County's Special Use Permit zoning, guest-proof yards, and the {price('residential')} sq ft range, September 2026.",
    "h1": "Turf for the Occasional Meadow Woods Rental Home",
    "lede": capsule(
        f"Turf for a Meadow Woods rental home falls within the {price('residential')} per square foot market "
        "range as of September 2026, the same as any residential yard. What's different here is the market "
        "itself: whole-home nightly rentals need a discretionary permit in this zoning, so this work comes up "
        "less often than in the vacation-home neighborhoods closer to Disney."),
    "sections": [
        ("Why a homeowner asking for the best rental-turf company near Meadow Woods gets a different answer here",
         "<p>Unincorporated Orange County generally doesn't treat a whole-home stay under 30 nights as a "
         "permitted use in residential zoning; it takes a discretionary Special Use Permit, granted case by "
         "case through a public hearing, under an ordinance that predates the state's 2011 cutoff on new local "
         "rental bans. Meadow Woods' own zip code, 32824, isn't one of the vacation-home-friendly zip codes "
         "Orange County carved out closer to Disney. That means a homeowner here searching for the best "
         "rental-turf company near Meadow Woods is more often turfing a full-time residence that occasionally "
         "hosts guests, rather than a dedicated short-term rental property.</p>"),
        ("What guest turnover still demands from a residential yard",
         "<p>Even without a dedicated STR license, a Meadow Woods home listed occasionally on a booking site "
         "still needs a yard that survives a string of strangers using it between cleanings. That favors the "
         "same build choices a family with kids or dogs would want anyway: a denser, shorter-pile turf that "
         "resists matting from repeated foot traffic, seams anchored more tightly than a lawn nobody walks on "
         "daily, and infill that doesn't need constant attention between visits. None of that changes because "
         "the home is occasionally a rental instead of always one; it just means the yard has less margin for "
         "a base that was cut corners on.</p>"),
        ("Capped irrigation matters more when nobody local is watching the yard",
         "<p>A property that sits empty between bookings, or between an owner's own visits, is exactly the "
         "kind of yard where a forgotten irrigation zone becomes a problem: a head left running under turf "
         "wastes water against a surface that can't use it and can undermine the base over time. Capping those "
         "heads as part of the turf install, which the state standard requires everywhere in Florida, removes "
         "that risk entirely rather than leaving it for whoever manages the property remotely to catch.</p>"),
    ],
    "scenario": ("Say you have a 700 sq ft fenced backyard at an occasional rental",
                 "<p>Say you have a 700 sq ft fenced backyard at a Meadow Woods home that hosts guests through "
                 f"a booking site a few weekends a month. At the {price('residential', True)} typical range, "
                 "that yard prices between roughly $7,000 and $11,200 installed, the same math as any "
                 "residential lawn of that size. Because the home isn't watched daily between stays, the crew "
                 "caps every sprinkler head under the new turf as part of the same visit rather than leaving "
                 "one zone for later, and the seams get the tighter edge-anchoring spec used for a yard with "
                 "regular, unfamiliar foot traffic.</p>"),
    "faqs": [
        faq("Can I get a Special Use Permit for nightly rentals just to justify vacation-rental turf in Meadow Woods?",
            "That's a zoning decision made through Orange County's own public-hearing process, not something this page can predict for a specific address. Check with the county's Zoning Division before assuming a permit will be granted."),
        faq("Does turf for an occasional-guest home cost more than a regular lawn in Meadow Woods?",
            "The per-square-foot range is the same. What can push a specific quote up is a denser turf spec and tighter seam anchoring chosen for repeated stranger foot traffic, not the fact that guests occasionally stay there."),
    ],
    "sources": ["dep-rule", "attampa-cost", "lbs-fl-cost", T_STR],
}

# ============================================================== local: commercial
_commercial = {
    "title": "Commercial Turf for Meadow Woods HOAs & Retail",
    "meta": "Commercial turf in Meadow Woods, FL: HOA entrance islands, retail strips along Landstar Boulevard, and how pricing and permits differ from a residential lawn.",
    "h1": "Commercial Turf for Meadow Woods Common Areas",
    "lede": capsule(
        "Commercial turf in Meadow Woods is quoted per job from drawings or a site walk rather than a flat "
        "per-square-foot range, since an HOA entrance island, a retail strip along Landstar Boulevard and an "
        "apartment courtyard all carry different access, grading and irrigation-capping needs."),
    "sections": [
        ("HOA common ground is a different client than a homeowner",
         "<p>With ten subdivisions and 1,454 homes under one board, Wyndham Lakes Estates is the kind of "
         "association in Meadow Woods that maintains its own entrance monuments, mailbox kiosks and common "
         "landscape strips separate from any individual homeowner's yard. Turf on that kind of shared ground "
         "gets quoted from the association's own drawings and goes through its board, not a homeowner's "
         "architectural packet, and the base spec has to hold up to mowing crews and foot traffic from every "
         "resident rather than one household. Smaller associations nearby, without a maintenance crew of that "
         "size, sometimes turn to turf specifically to cut the mowing and irrigation load on a shared entrance "
         "strip.</p>"),
        ("Bigger parcels sit outside the state's one-acre residential rule",
         "<p>Florida's 2025 turf law, and the DEP rule that followed it, only sets a floor for single-family "
         "residential lots of one acre or less. An HOA common area, a retail pad along Landstar Boulevard or an "
         "apartment courtyard in Meadow Woods generally falls outside that scope, which means Orange County "
         "keeps full authority over material, drainage and setback questions on that kind of site rather than "
         "answering to the state standard the way a private backyard does. That doesn't mean no rule applies; "
         "it means the applicable rule is whatever the county's commercial landscape and stormwater review "
         "requires for that specific parcel.</p>"),
        ("Access and irrigation on a shared or leased property",
         "<p>A retail strip or clubhouse courtyard often has irrigation and drainage tied into a larger site "
         "system shared with other tenants, so capping a zone isn't as simple as disconnecting one homeowner's "
         "sprinkler head. That makes an early conversation with the property manager or HOA's irrigation "
         "contractor part of the job before any turf goes down, since a zone that also feeds landscaping "
         "outside the turf footprint can't just be shut off without a plan for what stays green around it.</p>"),
    ],
    "scenario": ("Say you have a 300 sq ft HOA entrance island",
                 "<p>Say a Meadow Woods subdivision's board wants to replace a 300 sq ft entrance island that's "
                 "struggled to hold sod under a shade tree for years. There's no flat per-square-foot number "
                 "for that kind of job the way there is for a backyard, since access for equipment, the "
                 "irrigation zone's connection to the rest of the entrance landscaping, and whether the tree's "
                 "drip line limits excavation all factor into the quote. A site walk with the board's landscape "
                 "committee, followed by a written scope with the same five specification lines any turf quote "
                 "should carry, base depth, product, infill, edging and irrigation capping, is what turns that "
                 "into a real number.</p>"),
    "faqs": [
        faq("Does an HOA entrance island in Meadow Woods need a county permit for turf?",
            "Possibly, depending on the scope: grading, drainage or irrigation changes on common ground can trigger a permit even where the turf material itself doesn't. Orange County's Permitting Services can confirm for the specific parcel."),
        faq("Is commercial turf priced the same per square foot as a residential lawn in Meadow Woods?",
            "No. Commercial and common-area jobs are quoted from drawings or a site walk because access, existing irrigation and site-specific grading vary too much for one flat range."),
    ],
    "sources": ["dep-rule", "fs125572", T_WLE],
}

# ============================================================== local: sports
_sports = {
    "title": "Sports and Fitness Turf, Meadow Woods FL",
    "meta": "Sports and fitness turf in Meadow Woods, FL: flat flatwoods lots for a home gym strip or bocce court, quoted per job as of September 2026.",
    "h1": "Home Sports Turf for Meadow Woods Yards",
    "lede": capsule(
        "Sports and fitness turf in Meadow Woods, a sled track along a side yard, a bocce court or an agility "
        "lane, is quoted per job rather than a flat per-square-foot range, since layout and base depth vary "
        "with what the surface has to support."),
    "sections": [
        ("Flat flatwoods ground is easier to lay out a court on",
         "<p>The same nearly level flatwoods terrain that defines most of Meadow Woods' residential lots, built "
         "on the sandy, poorly drained Immokalee and Basinger soil series, makes laying out a straight sled "
         "track or a squared bocce court simpler than it would be on a sloped lot elsewhere in the county. "
         "There's little existing grade to correct for before the base goes in, which keeps the layout work "
         "closer to what it would take on a flat lawn than what a hillside installation in Lake County "
         "requires. The tradeoff, as with any flatwoods lot, is that drainage has to be built into the base "
         "deliberately rather than relying on the ground's own slope.</p>"),
        ("Sizing a lot's leftover space for a home sports surface",
         "<p>Meadow Woods' housing stock runs from small, older townhome lots to the larger yards common around "
         "Wyndham Lakes Estates' post-2005 sections, and that range decides what actually fits. A narrow side "
         "yard next to a Fairway Townhomes-era unit might only hold a compact sled track or an agility lane "
         "along the fence line; a bigger rear yard near the community's newer east side has more room for a "
         "full bocce court or a multi-use turf pad. Either way, the base underneath is denser and more heavily "
         "compacted than a lawn's, since repeated sled pulls or ball impact wear a surface differently than "
         "foot traffic does.</p>"),
        ("Checking HOA rules before a court goes in",
         "<p>A bocce court or a fenced batting cage is a more visible change to a yard than a lawn swap, which "
         "means it's more likely to need sign-off from whichever subdivision's architectural review board "
         "covers that lot. Getting that approval before ordering material avoids the same problem a putting "
         "green or a large play structure runs into: a board that asks for changes after installation costs "
         "more to fix than one consulted at the drawing stage.</p>"),
    ],
    "scenario": ("Say you have a 200 sq ft side-yard sled track",
                 "<p>Say you have a 200 sq ft strip along a side yard fence, wide enough for a sled track and a "
                 "short sprint lane. There's no flat per-square-foot rate for that kind of surface the way "
                 "there is for a lawn, since the base has to handle repeated sled drag and sprint impact rather "
                 "than foot traffic alone, which usually means a denser compacted base and a tighter-woven turf "
                 "than a standard residential product. A site visit settles the base depth and product spec "
                 "before a number goes on paper, and, if the yard sits inside an HOA's review area, the "
                 "association's sign-off gets requested at the same time.</p>"),
    "faqs": [
        faq("Can a sled track or bocce court go on the same base as a lawn in Meadow Woods?",
            "The layers are similar, washed crushed rock over graded native soil, but a sports surface usually needs a more heavily compacted base and a denser turf product to handle repeated impact, so it isn't a direct swap with lawn-grade material."),
        faq("Does Meadow Woods' flat terrain make a backyard sports court cheaper?",
            "It simplifies the layout, since there's little existing slope to correct, but the base still has to be built for the specific activity, so pricing depends on the site and the surface's intended use, not the terrain alone."),
    ],
    "sources": ["dep-rule", "usda-wss", T_IMMOKALEE, T_BASINGER, T_WLE],
}

# ============================================================== local: pavers
_pavers = {
    "title": "Turf and Pavers for Meadow Woods Driveways",
    "meta": "Turf between pavers in Meadow Woods, FL: narrow older lots, sandy flatwoods soil, and joint-erosion fixes, quoted per job as of September 2026.",
    "h1": "Turf Between Pavers in Meadow Woods",
    "lede": capsule(
        "Turf ribbons between pavers on a Meadow Woods driveway or walkway are quoted per job rather than a "
        "flat range, since the amount of turf involved is usually small and the base work matters more than "
        "square footage."),
    "sections": [
        ("Narrow older lots make paver-and-turf strips a common fix",
         "<p>A Fairway Townhomes-era lot from 1988 or 1989, or a similar narrow footprint elsewhere in Meadow "
         "Woods' older core, often has a driveway that runs close to the property line with little room for a "
         "planting bed beside it. A turf ribbon between paver courses, or a turf strip down the center of a "
         "two-track driveway, softens that hardscape without giving up any of the usable pavement width, which "
         "matters more on a lot where the side yard is already too tight for much else.</p>"),
        ("Why sandy, poorly drained soil erodes paver joints without the right base",
         "<p>The Immokalee and Basinger soils under most of Meadow Woods are sandy and, per the USDA's own "
         "series descriptions, very poorly to poorly drained. Loose sand alone under a paver joint washes out "
         "under repeated rain and foot traffic, which is why a turf ribbon needs the same washed, open-graded "
         "rock base as any other turf application underneath it, not just a bed of joint sand. Skipping that "
         "base is the most common reason a turf-and-paver strip settles unevenly within a year or two on ground "
         "this poorly drained.</p>"),
        ("Where a paver strip runs into the state's tree and setback rules",
         "<p>A stepping-stone path or driveway strip that passes near a mature oak from the community's 1990s "
         "build-out still has to respect that tree's drip line under the state's turf standard, the same as a "
         "full lawn would. And a driveway strip that runs close to a subdivision's retention pond, more common "
         "on the newer, larger lots near Wyndham Lakes Estates, still needs the 10-ft waterbody setback "
         "factored into the layout before any pavers or turf go down.</p>"),
    ],
    "scenario": ("Say you have a 150 linear ft driveway strip",
                 "<p>Say you have a 150 linear ft two-track driveway on an older Meadow Woods lot, with a turf "
                 "strip planned down the center between the paver runners. There's no flat per-square-foot rate "
                 "for that kind of job, since the actual turf area is small but the base work underneath, "
                 "washed rock, compaction and a clean transition against each paver edge, drives most of the "
                 "cost. A site visit confirms whether the existing base under the driveway is salvageable or "
                 "needs rebuilding before a number goes on the quote.</p>"),
    "faqs": [
        faq("Does a small turf ribbon between pavers need the same base as a full lawn in Meadow Woods?",
            "Yes. Even a narrow strip needs washed, open-graded rock underneath it, since loose sand alone erodes under paver joints on the area's poorly drained soil."),
        faq("Can turf go between pavers near a Meadow Woods retention pond?",
            "Only if it clears the state's 10-ft waterbody setback from the pond's edge, the same rule that applies to a full lawn, so that distance gets checked before any layout is finalized."),
    ],
    "sources": ["dep-rule", "usda-wss", T_IMMOKALEE, T_BASINGER, T_FAIRWAY],
}

# ============================================================== local: repair
_repair = {
    "title": "Artificial Turf Repair, Meadow Woods FL",
    "meta": "Artificial turf repair in Meadow Woods, FL: aging 1990s-2000s systems, storm damage near Boggy Creek, and oak-root heave, quoted per visit, September 2026.",
    "h1": "Fixing Artificial Turf in Meadow Woods",
    "lede": capsule(
        "Turf repair in Meadow Woods, open seams, lifted edges, a melted patch or a drainage fix, usually "
        "carries a minimum service charge rather than a per-square-foot rate, since most repair visits cover a "
        "small area with a specific cause."),
    "sections": [
        ("A lot of the community's turf is old enough to need it",
         "<p>Meadow Woods' population climbed from 11,286 in 2000 to 25,558 by 2010, and a good share of the "
         "turf installed during and just after that stretch of growth is now approaching, or past, the lower "
         "end of a synthetic system's 10-to-20-year working life. That's long enough for UV exposure to soften "
         "adhesive at a seam, for infill to have washed thin in high-traffic spots, and for an irrigation "
         "system installed alongside a 1990s or early-2000s home to be closer to 30 years old than 10, which is "
         "worth checking whenever a repair crew is already on site.</p>"),
        ("Root heave from mature oaks in the older sections",
         "<p>Live oaks planted or left standing during Meadow Woods' original build-out have had two to three "
         "decades to put down roots that can lift a turf edge or crack a seam from underneath, even where the "
         "install itself stayed well outside the tree's original drip line. A section of turf that's started "
         "to tent or wrinkle near a mature tree is often a root problem rather than a backing failure, and the "
         "state's drip-line rule, plus a certified arborist's read on the root's actual path, both factor into "
         "how that repair gets done without hurting the tree further.</p>"),
        ("Storm and flood checks near the Boggy Creek corridor",
         "<p>Lots along Meadow Woods' northern edge, closer to the Boggy Creek drainage that feeds toward the "
         "Kissimmee chain of lakes, see more standing water after a heavy storm than lots farther from that "
         "corridor. Turf itself drains fast once it's clean, but a base that's been submerged repeatedly can "
         "compact unevenly over time, which shows up as a soft or spongy spot rather than an obvious tear. "
         "Checking the base, not just the visible turf, is part of a proper repair call on a lot in that "
         "part of the community.</p>"),
    ],
    "scenario": ("Say you have a 30 sq ft lifted seam near a patio",
                 "<p>Say you have a 30 sq ft section of turf near a patio edge where the seam has lifted and "
                 "started to curl, on a lawn installed sometime during the community's 2000s growth. That's a "
                 "repair-visit job rather than a per-square-foot quote: expect a minimum service charge that "
                 "covers the crew's time to re-glue or re-tape the seam and re-secure the edge, plus a quick "
                 "check of the base underneath for the kind of settling a 15-to-20-year-old install can "
                 "develop. If the irrigation line under that section is original to the home, it's worth asking "
                 "whether it's been capped correctly the whole time.</p>"),
    "faqs": [
        faq("How do I know if my Meadow Woods turf issue is a repair or a full replacement?",
            "A localized seam, edge or small melted spot is usually a repair. Widespread thinning infill, a base that's settled across most of the yard, or turf original to a 1990s install are signs a replacement is the more practical fix."),
        faq("Does root growth from an old oak count as storm damage for a repair?",
            "No, it's a separate cause with its own fix. A root-related lift needs the root's path checked, sometimes with an arborist, before deciding whether the turf can be reset or needs to move outside the drip line."),
    ],
    "sources": ["dep-rule", "stn-life", T_WIKI],
}

# ============================================================== local: cleaning
_cleaning = {
    "title": "Turf Cleaning and Odor Control, Meadow Woods",
    "meta": "Turf cleaning in Meadow Woods, FL: pet odor in fenced yards, oak-leaf debris near Boggy Creek, and humidity control, quoted by size, September 2026.",
    "h1": "Turf Cleaning for Meadow Woods Yards",
    "lede": capsule(
        "Keeping turf clean in Meadow Woods, treating pet odor, power brooming, sanitizing and topping off "
        "infill, gets priced from a look at the actual yard rather than a flat per-square-foot number, since "
        "how long the surface has gone untreated changes the work more than its footprint does. Fenced, "
        "tree-covered lots common in the community's older sections tend to need attention on a tighter "
        "schedule than a wide-open newer yard."),
    "sections": [
        ("Dense, fenced yards concentrate pet odor faster",
         "<p>Meadow Woods' housing stock, built mostly on lots sized for townhomes and attached single-family "
         "homes from the 1980s through the 2000s, tends to put a fenced yard closer to a neighbor's than a "
         "half-acre property would. A dog yard on a lot like that has less open ground for odor to disperse "
         "into, so a rinse-and-brush routine that would keep a wide-open Wyndham Lakes Estates-era lawn fresh "
         "sometimes isn't enough on a narrower older lot, where a deeper sanitizing treatment on a tighter "
         "schedule keeps ammonia from building up between visits.</p>"),
        ("Oak leaves and debris in the community's older, tree-covered sections",
         "<p>Sections of Meadow Woods built during the original 1980s and 1990s wave of construction have had "
         "decades for live oaks to mature into real canopy, and that canopy drops leaves and small debris onto "
         "turf year-round, not just in one season. Left alone, that organic material works down into the "
         "infill layer and blocks the drainage the base is built to provide, the same mechanism that clogs a "
         "dog run's infill but from leaf litter instead of waste. A power-broom pass that lifts the turf's pile "
         "and pulls debris back to the surface, done on a routine that matches how much canopy actually hangs "
         "over a given yard, keeps that base doing its job.</p>"),
        ("Humidity near the Boggy Creek corridor and algae or mold risk",
         "<p>Lots closer to Meadow Woods' northern edge, near the Boggy Creek drainage, sit in a slightly "
         "damper microclimate than the drier stretches of the community farther from that corridor, since "
         "standing water and retention ponds nearby keep humidity higher at ground level. That extra moisture "
         "gives algae and mold more of a foothold on turf that isn't rinsed and brushed regularly, particularly "
         "in shaded pockets under a screen enclosure or dense tree cover, which is where a periodic sanitizing "
         "treatment earns its cost over a plain hose rinse.</p>"),
    ],
    "scenario": ("Say you have a 900 sq ft yard needing pet-odor treatment",
                 "<p>Say you have a 900 sq ft fenced backyard on an older Meadow Woods lot that's carried two "
                 "dogs for several years without a deep clean. That's quoted by the yard's size and how long "
                 "it's been since the last service rather than a flat per-square-foot number, since a yard "
                 "that's gone a year or more between treatments needs a more thorough sanitizing pass, and "
                 "possibly an infill top-up, compared with one that's been rinsed and brushed on a regular "
                 "schedule. A quick check of the base's drainage is part of that same visit, since a base "
                 "that's stopped clearing rinse water quickly is often the real source of a smell that keeps "
                 "coming back.</p>"),
    "faqs": [
        faq("How often does turf need cleaning in a fenced Meadow Woods yard with dogs?",
            "It depends on the yard's size relative to how many dogs use it and how narrow the fenced space is; a tighter, older lot with heavy use needs more frequent attention than a wide-open yard with the same number of dogs."),
        faq("Does living near Boggy Creek mean more turf maintenance?",
            "Slightly, mainly because of higher humidity and shaded, damp pockets that favor algae or mold, so a yard in that part of the community can benefit from a periodic sanitizing pass rather than a hose rinse alone."),
    ],
    "sources": ["dep-rule", "sgw-faq", T_WIKI, T_WLE],
}

# ============================================================== local: replacement
_replacement = {
    "title": "Turf Replacement for Meadow Woods Yards",
    "meta": "Turf replacement in Meadow Woods, FL: turf from the 2000s growth boom aging out, capping older irrigation lines, quoted per job, September 2026.",
    "h1": "Replacing Worn Turf in Meadow Woods",
    "lede": capsule(
        "Turf replacement in Meadow Woods, tearing out a worn system, correcting the base and laying new "
        "material, prices close to a new residential install minus whatever base can be reused, rather than a "
        "flat per-square-foot rate."),
    "sections": [
        ("Turf from the community's growth years is reaching the end of its life",
         "<p>Meadow Woods added more than 14,000 residents between 2000 and 2010, and any turf installed during "
         "that stretch of construction and the years right after is now old enough to sit inside, or past, the "
         "lower end of a synthetic system's typical 10-to-20-year lifespan. UV exposure, foot traffic and "
         "whatever infill was used all decide where a given yard actually falls in that range, but a system "
         "installed before Florida's current material standard took effect in 2026 is also worth checking "
         "against today's rules on infill and backing before assuming a like-for-like swap is the right call.</p>"),
        ("Thirty-year-old irrigation lines under a yard about to be redone",
         "<p>A home built during Meadow Woods' 1990s wave of construction is now old enough that its original "
         "irrigation system is approaching three decades in the ground, and a full turf replacement is the "
         "natural point to deal with it properly rather than working around it again. Any head still live under "
         "the footprint gets capped as part of the state's turf standard regardless of the line's age, but a "
         "replacement job is also the easier moment to have a plumber confirm the rest of that aging system "
         "isn't leaking into the base before new rock goes down on top of it.</p>"),
        ("How much of the old base actually gets reused",
         "<p>Replacing turf on Meadow Woods' flat, poorly drained flatwoods soil usually means opening up the "
         "base to check it, not just pulling the surface material and relaying new turf on what's there. A base "
         "that's held its grade and still drains well can often be topped up and re-compacted; one that's "
         "settled unevenly, which is more common on this area's poorly drained soil after 15 to 20 years, needs "
         "a fuller rebuild. That distinction is most of what separates a lower-cost replacement from one that "
         "prices close to a brand-new install.</p>"),
    ],
    "scenario": ("Say you have a 1,100 sq ft lawn installed during the 2000s",
                 "<p>Say you have a 1,100 sq ft backyard lawn installed sometime during Meadow Woods' 2000s "
                 "growth years, now showing thin infill, a couple of open seams and a base that's started to "
                 "hold water after storms. There's no flat per-square-foot number for that kind of job the way "
                 "there is for a first-time install, since the price depends heavily on how much of the "
                 "existing base can be reused versus rebuilt. A base that's still draining and holding grade "
                 "keeps the job closer to a straightforward resurface; a base that's settled unevenly pushes "
                 "the price close to what a brand-new install on that same footprint would cost.</p>"),
    "faqs": [
        faq("Is turf installed in Meadow Woods during the 2000s boom safe to just resurface?",
            "Sometimes. If the base has held its grade and still drains well, a resurface can work. If it's settled unevenly, which is common after 15 to 20 years on this area's poorly drained soil, a fuller rebuild is the more reliable fix."),
        faq("Does replacing turf trigger the state's newer infill rules on an older Meadow Woods lawn?",
            "A replacement is a new install for practical purposes, so it should meet the current state standard on infill and backing even if the original system predated the 2026 rule."),
    ],
    "sources": ["dep-rule", "stn-life", T_WIKI],
}

LOCAL = {
    "residential": _residential,
    "pet": _pet,
    "putting": _putting,
    "playground": _playground,
    "pool": _pool,
    "str": _str,
    "commercial": _commercial,
    "sports": _sports,
    "pavers": _pavers,
    "repair": _repair,
    "cleaning": _cleaning,
    "replacement": _replacement,
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
