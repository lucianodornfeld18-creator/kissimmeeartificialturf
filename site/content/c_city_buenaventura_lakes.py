# -*- coding: utf-8 -*-
"""Buenaventura Lakes (BVL) hub + city x service pages."""
from _helpers import page, capsule, sec, table, faq, ul, price, svc, city, county, post, src, ext, a
from _cityservice import cityservice_pages

SLUG = "buenaventura-lakes"

# ---------------------------------------------------------------- local sources
BUILD_DEPT = ("Osceola County -- Building and Permits", "https://www.osceola.org/Doing-Business/Building-and-Permits")
PERMIT_PORTAL = ("Osceola County -- Online Permit Center", "https://permits.osceola.org/")
PROP_APPR = ("Osceola County Property Appraiser -- parcel and tax district search", "https://www.property-appraiser.org/")
TOHO_AREA = ("Toho Water Authority -- our service area", "https://www.tohowater.com/about-us/our-service-area")
SFWMD_KB = ("South Florida Water Management District -- Upper Kissimmee Basin water supply plan", "https://www.sfwmd.gov/our-work/water-supply/upper-kissimmee")
CENSUS_BVL = ("U.S. Census Bureau QuickFacts -- Buenaventura Lakes CDP, Florida", "https://www.census.gov/quickfacts/table/PST045223/1209415")
MSTU_BVL = ("Osceola County -- Buenaventura Lakes special assessment (MSTU)", "https://www.osceola.org/Government/County-Budget-and-Financial-Statements/Special-Assessments/Special-Assessment-Communities/Buenaventura-Lakes")
DRAIN_BVL = ("Osceola County -- BVL internal drainage improvements project", "https://one.osceola.org/bvldrainageimprovements")
PARK_BVL = ("Osceola County -- Buenaventura Community Park", "https://www.osceola.org/Community/Parks-and-Public-Lands/Find-a-Park-or-Facility/Buenaventura-Community-Park")
PARK_GUEVARA = ("Osceola County -- Robert Guevara Community and Park", "https://www.osceola.org/Community/Parks-and-Public-Lands/Find-a-Park-or-Facility/Robert-Guevara-Community-and-Park")
GOLF_BVL = ("GolfPass -- Osceola Golf Club / Buenaventura Lakes", "https://www.golfpass.com/travel-advisor/courses/2142-osceola-golf-club-buenaventura-lakes")
LANDSTAR = ("Landstar Development Group -- past projects", "https://landstardevelopment.com/past-projects/")
STRAFFORD = ("Florida Neighborhood Realty -- Strafford Park, Buenaventura Lakes", "https://www.floridaneighborhoodrealty.com/strafford-park-buenaventura-lakes-homes-sale/")
CORALWOOD = ("Florida Neighborhood Realty -- Coral Wood, Buenaventura Lakes", "https://www.floridaneighborhoodrealty.com/coral-wood-buenaventura-lakes-homes-sale/")
HOA_LAKEPOINTE = ("Florida HOA directory -- Lakepointe Townhomes at Buenaventura Lakes HOA", "https://www.florida-hoa.com/fhhoa_list.php?mastertable=fhtitle&masterkey1=N25251")
SOIL_IMMOKALEE = ("USDA NRCS -- official series description, Immokalee series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/I/IMMOKALEE.html")
SOIL_MYAKKA = ("USDA NRCS -- official series description, Myakka series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/M/MYAKKA.html")
SOIL_SMYRNA = ("USDA NRCS -- official series description, Smyrna series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/S/SMYRNA.html")
STR_OVERLAY = ("TrueNorth Property Management -- Osceola County short-term rental regulations", "https://truenorthmanaged.com/orlando/osceola-county/osceola-county-rental-regulations/")

SRC = [BUILD_DEPT, PERMIT_PORTAL, PROP_APPR, TOHO_AREA, SFWMD_KB, CENSUS_BVL, MSTU_BVL, DRAIN_BVL, PARK_BVL, PARK_GUEVARA,
       GOLF_BVL, LANDSTAR, STRAFFORD, CORALWOOD, HOA_LAKEPOINTE, SOIL_IMMOKALEE, SOIL_MYAKKA, SOIL_SMYRNA, STR_OVERLAY]

# ---------------------------------------------------------------- HUB
_hub_body = "".join([
    sec("What's different about a turf job in Buenaventura Lakes",
        "<p>Buenaventura Lakes sits about 4 miles northeast of downtown Kissimmee, an unincorporated community residents just call BVL. "
        f"{ext('https://landstardevelopment.com/past-projects/', 'Landstar Development Group')} built roughly 7,250 of its units starting in the late 1970s, and the build-out "
        f"continued through the 1990s: {ext('https://www.floridaneighborhoodrealty.com/strafford-park-buenaventura-lakes-homes-sale/', 'Strafford Park went up between 1991 and 1996')} and "
        f"{ext('https://www.floridaneighborhoodrealty.com/coral-wood-buenaventura-lakes-homes-sale/', 'Coral Wood followed in 1997 and 1998')}, both by the same builder. "
        "That leaves a lot of yards carrying 30- to 45-year-old irrigation, thin St. Augustine that gave up in the shade years ago, and screened pool cages "
        "original to the house. Canals and small lakes cut through many of the original subdivisions, so a turf plan here has to account for a setback the "
        f"county lot next door in a newer build usually doesn't. As of September 2026 the population runs about 30,251 ({ext(CENSUS_BVL[1], '2020 Census')}), and roughly three in four "
        "residents identify as Hispanic or Latino, a share the Census Bureau has tracked climbing with each count since 1990. That's a demographic fact, not a service "
        "offer: we don't advertise Spanish-language service, and nothing on this page should read that way.</p>"),
    sec("Who reviews a turf permit here, and does a Kissimmee address mean the city has jurisdiction",
        f"<p>No. BVL has never incorporated, so {ext('https://www.osceola.org/Doing-Business/Building-and-Permits', 'the Osceola County Building Division')} reviews permits here, "
        f"not Kissimmee City Hall, even though most parcels carry a Kissimmee, FL 34743 or 34744 mailing address. The fastest way to check where a specific "
        f"lot actually falls is to look it up on {ext('https://www.property-appraiser.org/', 'the Osceola County Property Appraiser site')}: the parcel record shows the taxing "
        "jurisdiction, and a parcel taxed by the county rather than the city sits outside Kissimmee's limits. When in doubt, call the county building line direct "
        f"at 407-742-0200 or start an application through {ext('https://permits.osceola.org/', 'the Online Permit Center')}. Rule 62-308.100 itself creates no new state permit for "
        f"synthetic turf ({src('dep-rule', 'DEP Rule 62-308.100')}), but a county reviewer can still ask about drainage, easements or a septic field, so checking the "
        f"{county('osceola', 'county rules for the whole area')} first is worth the five minutes. "
        f"{a('/laws/permits/osceola-county/', 'The county permit page for artificial turf')} walks through what a reviewer actually asks for.</p>"),
    sec("Can a Buenaventura Lakes HOA block artificial turf",
        "<p>Sometimes, and sometimes there's no association to ask. BVL was never platted as one master-planned, deed-restricted community the way Celebration or "
        "Reunion were; it's dozens of separate subdivisions Landstar and a handful of other builders recorded between the late 1970s and the late 1990s, and only "
        f"some of them still run an active homeowners' association. A cluster like {ext('https://www.florida-hoa.com/fhhoa_list.php?mastertable=fhtitle&masterkey1=N25251', 'the Lakepointe Townhomes association')} "
        "reviews exterior changes for its own streets; plenty of the older single-family PODs have no board left collecting dues or reviewing anything. The county's "
        f"own role in BVL is drainage, not architecture: {ext('https://www.osceola.org/Government/County-Budget-and-Financial-Statements/Special-Assessments/Special-Assessment-Communities/Buenaventura-Lakes', 'its special assessment district')} "
        f"funds pond and canal upkeep, nothing about what a homeowner plants or installs. Where covenants do apply, {src('fs7203045', 'F.S. 720.3045')} keeps an association from "
        f"restricting turf a neighbor or the street can't see, so a fenced backyard is protected differently than a front lawn ({src('olg-720', 'more on that statute')}). None of that "
        f"touches the state minimum standard in {a('/laws/florida-hb-683/', 'HB 683 and the DEP turf rule')}, which binds local governments, not associations. Read {a('/laws/hoa-rules/', 'what a Florida HOA is allowed to restrict')} before assuming either way.</p>"),
    table("Buenaventura Lakes yard types and what we do differently",
          ["Yard type", "What's common here", "What changes in the build"],
          [["1980s-90s screened pool cage", "Original lanai, worn turf-grade St. Augustine right up to the screen track", "Drainage underlay under the cage, edges glued rather than nailed into concrete"],
           ["Backyard on a canal or small lake", "Patio or lawn runs close to the bank, sometimes a low seawall", "Turf stops 10 ft from the water's edge unless a seawall already separates the two"],
           ["Original 1970s-80s POD lot, no active HOA", "Irrigation system pushing 30-45 years old, bare or thin grass in shade", "Zone valve capped, base rebuilt in washed rock rather than reusing old fill"],
           ["Townhome or condo cluster with an active HOA", "Small fenced patch, shared common ground nearby", "Spec sheet submitted to the board first; job scoped to the platted lot line only"],
           ["Lot backing the closed Osceola Golf Club fairways", "Deeper lot, mature 1980s landscaping and oaks", "Drip-line check on mature trees before any excavation starts"],
           ["Zero-lot-line or narrow side yard", "3-4 ft strip between houses, hard to mow", "Turf ribbon or a paver-and-turf combo since foot access is already tight"]],
          "Yard types repeat across BVL's older PODs; the market price range is the same across all of them."),
    sec("Water rules that shape a BVL install",
        f"<p>{ext('https://www.tohowater.com/about-us/our-service-area', 'Toho Water Authority')} serves Buenaventura Lakes along with the rest of Kissimmee and unincorporated Osceola County, "
        f"and its two-day watering schedule ({src('toho-days', 'watering days and times')}) still governs any sprinkler zone that survives a turf conversion. Osceola sits inside "
        f"{ext('https://www.sfwmd.gov/our-work/water-supply/upper-kissimmee', 'the South Florida Water Management District')}'s Upper Kissimmee Basin, and the county has been weighing tighter "
        f"conservation rules of its own ({src('osceola-water-2026', 'a 2026 ordinance proposal')}). None of that changes what happens under the turf itself: {src('dep-rule', 'the state turf rule')} bars in-ground irrigation "
        "on synthetic grass statewide, so any head inside the footprint gets capped at the valve, and a hose handles rinsing from there.</p>"),
    sec("Soil, canals and the base under a BVL lawn",
        f"<p>The flatwoods soils mapped across this part of Osceola County are mostly {ext('https://soilseries.sc.egov.usda.gov/OSD_Docs/I/IMMOKALEE.html', 'Immokalee')} and "
        f"{ext('https://soilseries.sc.egov.usda.gov/OSD_Docs/M/MYAKKA.html', 'Myakka')} fine sands, with the {ext('https://soilseries.sc.egov.usda.gov/OSD_Docs/S/SMYRNA.html', 'Smyrna series')} "
        f"first defined in this county in 1976 ({src('usda-wss', 'USDA Web Soil Survey')}); all three sit on a shallow hardpan and hold a seasonally high water table. That's consistent with what the "
        f"county keeps fixing: {ext('https://one.osceola.org/bvldrainageimprovements', 'a $4.6 million drainage improvement project')} is underway specifically to ease flooding across BVL's "
        f"internal pond network, and {ext('https://www.osceola.org/Government/County-Budget-and-Financial-Statements/Special-Assessments/Special-Assessment-Communities/Buenaventura-Lakes', 'the special assessment district')} "
        "already runs erosion control and aeration on individual ponds by number. On a lot like that, the two- to four-inch washed crushed rock base does the work; skipping it or "
        "compacting the sand underneath too hard is what leaves a lawn holding water after a summer storm.</p>"),
    sec("The old golf course and where people actually gather outdoors",
        f"<p>Many BVL streets were platted around {ext('https://www.golfpass.com/travel-advisor/courses/2142-osceola-golf-club-buenaventura-lakes', 'the Osceola Golf Club')}, an 18-hole course built in 1983 "
        "that course-tracking sites now list as closed, which is why some of the deeper, more open lots in the community still back onto old fairway corridors rather than a fence line. "
        f"Public recreation today centers on {ext('https://www.osceola.org/Community/Parks-and-Public-Lands/Find-a-Park-or-Facility/Buenaventura-Community-Park', 'Buenaventura Community Park')}, with its little league "
        f"and T-ball fields and batting cages, and {ext('https://www.osceola.org/Community/Parks-and-Public-Lands/Find-a-Park-or-Facility/Robert-Guevara-Community-and-Park', 'the Robert Guevara Community and Park')} "
        "near the center of the neighborhood. A backyard putting surface or a play lawn here is filling in around those public options, not replacing a private club amenity the way it "
        "might in a golf-front community farther south.</p>"),
    sec("Comparing quotes for a BVL yard",
        "<p>Someone typing \"best artificial turf installer near me in Buenaventura Lakes\" is usually trying to sort out which bid actually planned for the canal setback, the old "
        f"irrigation zone and the base, not which one uses the greenest-looking sample. Two bids that both say \"premium turf, installed\" don't tell you that. The "
        f"{ext('/artificial-turf-cost/', 'full cost guide')} breaks the market range down by project type; here the same {price('residential')} per sq ft applies as anywhere else we work, "
        "because BVL's older lots change the labor and base, not the published range itself.</p>"),
    "<!--AUTO:city-services-->",
])

HUB = page("/areas/buenaventura-lakes/", "city",
           "Artificial Turf in Buenaventura Lakes, FL (BVL) 2026",
           "Artificial turf installation in Buenaventura Lakes (BVL), an unincorporated Osceola County community 4 miles from Kissimmee: permits, HOAs, canals and cost.",
           "Artificial turf in Buenaventura Lakes",
           capsule("Buenaventura Lakes is an unincorporated community in Osceola County about 4 miles northeast of downtown Kissimmee, built out mostly from the late "
                   "1970s through the late 1990s by Landstar Homes. Canals and lakes run through many of its original subdivisions, and a large share of homes "
                   f"still carry 1980s and 1990s screened pools and aging irrigation. Turf here runs {price('residential')} per square foot installed, as of September 2026."),
           _hub_body,
           faqs=[
               faq("Is Buenaventura Lakes part of the City of Kissimmee?",
                   "No. BVL is an unincorporated census-designated place in Osceola County, so the Osceola County Building Division reviews permits, not the city. "
                   "A Kissimmee, FL 34743 or 34744 mailing address is normal here and doesn't put a lot inside the actual city limits; the Osceola County Property "
                   "Appraiser's parcel search shows the real taxing jurisdiction."),
               faq("Does Toho Water Authority serve Buenaventura Lakes?",
                   "Yes. Toho Water Authority lists BVL inside its Osceola County service area, and the same two-day-a-week watering schedule that covers Kissimmee "
                   "applies here. It only affects sprinkler zones you keep; the state rule bars in-ground irrigation on synthetic turf regardless."),
               faq("Do all BVL neighborhoods have an HOA that reviews turf?",
                   "No. Some townhome and condo clusters have an active association; many of the original single-family sections from the 1970s through the 1990s "
                   "have no board currently reviewing exterior changes. Check your own plat or association records rather than assuming either way."),
               faq("How close to a canal can artificial turf go in Buenaventura Lakes?",
                   "State rule keeps installed turf at least 10 feet from a canal, pond or lake edge unless a seawall or bulkhead already separates the yard from "
                   "the water. A swale that carries stormwater across the lot can't be turfed at all, seawall or not."),
               faq("What does a typical Buenaventura Lakes yard cost to turf?",
                   "The same Central Florida market range applies here as everywhere we work: $8 to $18 per sq ft installed, typically $10 to $16, as of September "
                   "2026. Older irrigation removal or canal-adjacent grading can push a specific quote toward the top of that range."),
           ],
           sources=SRC, city=SLUG, crumbs=[("Service areas", "/areas/")], crumb="Buenaventura Lakes",
           related=[("/areas/osceola-county/", "Osceola County: turf rules countywide"), ("/laws/permits/osceola-county/", "Osceola County permit rules for artificial turf"),
                    ("/areas/kissimmee/", "Artificial turf in Kissimmee"), ("/areas/meadow-woods/", "Artificial turf in Meadow Woods"), ("/areas/st-cloud/", "Artificial turf in St. Cloud"),
                    ("/artificial-turf-cost/", "Turf cost tables for Central Florida"), ("/blog/why-new-construction-sod-dies-in-osceola-county/", "Why builder sod struggles in Osceola County")])

# ---------------------------------------------------------------- LOCAL entries
LOCAL = {}

LOCAL["residential"] = {
    "title": "Artificial Grass Installation in Buenaventura Lakes (BVL)",
    "meta": "Artificial grass installation in Buenaventura Lakes, FL: old irrigation, canal-front lots and 1970s-90s PODs, with September 2026 pricing.",
    "h1": "Turf for BVL's older lawns and canal-front yards",
    "lede": capsule(
        "Artificial grass installation in Buenaventura Lakes usually means replacing a lawn that has been fighting 30 to 45 years of irrigation wear and shade "
        "since Landstar built most of the neighborhood between the late 1970s and the late 1990s. Installed turf runs "
        f"{price('residential')} per sq ft, typically {price('residential', True)}, as of September 2026, whether the lot backs a canal, an old fairway or a plain fence line."),
    "sections": [
        ("Replacing irrigation and St. Augustine that gave up decades ago",
         "<p>A sprinkler system installed when a Strafford Park or Coral Wood house was new is now three to four decades old, and it usually shows before the lawn "
         "does: cracked risers, a zone that floods one corner and starves another, PVC that's brittle at every joint. Converting to turf means capping that zone "
         f"at the valve rather than trying to keep it alive, since {src('dep-rule', 'the state turf rule')} bars using in-ground irrigation on synthetic grass anyway. Underneath, decades "
         "of mowing and edging on native sand tend to leave the grade uneven, and the old sod mat is usually thicker than it looks from the surface. On a shaded "
         f"lot where St. Augustine thinned out years ago under a mature oak, the same excavation sets up the drip-line check a live oak here still requires. "
         f"{city('buenaventura-lakes', 'The BVL area page')} has more on how canals, soil and the neighborhood's age shape a build before it starts.</p>"),
        ("Backyards that end at a canal or small lake",
         "<p>A good share of BVL's original PODs were platted around a canal, retention pond or one of the community's small lakes, and the state's synthetic turf "
         "standard keeps installed grass at least 10 feet back from that edge unless a seawall or bulkhead already separates the yard from the water. Where a low "
         "seawall exists, turf can run to the cap; where the bank is just sloped earth, the buffer strip stays in sod, mulch or landscaping instead. The county "
         "tracks many of these ponds individually for erosion and aeration work, which is a reminder that the ground right at the bank moves and settles in ways "
         "the rest of the lot doesn't, so we keep the base transition at that 10-foot line clean rather than trying to feather turf into it.</p>"),
        ("Sequencing the permit check and the HOA check",
         "<p>Because BVL is unincorporated, the paperwork path here runs through Osceola County rather than city hall, and it's worth confirming which section of "
         "the neighborhood a lot sits in before ordering material. A parcel inside one of the townhome clusters with an active association usually means a spec "
         "sheet goes to the board first; a parcel in one of the older single-family PODs may have no board left to ask, in which case the county building line and "
         "the general Florida rule on what an association can restrict are the only checks that apply. Doing that sequencing before the crew shows up avoids a "
         f"job that has to pause mid-install for a signature nobody planned for. {a('/laws/permits/osceola-county/', 'The county turf permit page')} and "
         f"{a('/laws/hoa-rules/', 'our breakdown of what a Florida HOA can restrict')} cover both checks in more depth, and {svc('residential', 'the full installation guide')} "
         f"or {city('kissimmee', 'the Kissimmee area page')} are useful next stops for comparing options across the wider region.</p>"),
    ],
    "scenario": ("A typical BVL backyard, worked out in square feet",
                 "<p>Say you have a 950 sq ft backyard behind a 1993 Strafford Park single-story, screened lanai along the back third and a bare, root-bound strip "
                 "under a live oak along the side fence. At the published range that's $7,600 to $17,100 installed; at the more typical $10-$16 band most Central "
                 "Florida jobs land in, figure $9,500 to $15,200. The oak knocks the usable turf area down once the drip line is marked off, and if the yard also "
                 "backs a drainage canal, the last 10 feet of that boundary stays out of the turf footprint entirely unless a seawall is already there. None of "
                 "that changes the per-square-foot number; it changes how many square feet actually get turfed and how much of the quote goes into base work under "
                 "the oak instead of open lawn.</p>"),
    "faqs": [
        faq("Do I need a permit to install artificial turf on my BVL lawn?",
            "It depends on the scope, since the state rule creates no new turf-specific permit. Contact the Osceola County Building Division or check the Online "
            "Permit Center before work starts, especially if drainage, a septic field or irrigation capping is involved."),
        faq("My section of Buenaventura Lakes doesn't seem to have an active HOA anymore. Can I just install turf?",
            "Probably, but confirm it rather than assume it. Some BVL sections still have a board on paper even if it's quiet; pull your deed or ask a longtime "
            "neighbor before ordering material, since a dormant association can still have standing to object later."),
    ],
    "sources": [BUILD_DEPT, PERMIT_PORTAL, PROP_APPR, STRAFFORD, CORALWOOD, LANDSTAR, DRAIN_BVL],
}

LOCAL["pet"] = {
    "title": "Pet Turf for Dogs in Buenaventura Lakes, FL",
    "meta": "Pet turf and dog run installation in Buenaventura Lakes: zero-lot-line yards, canal setbacks and HOA-managed clusters. Market pricing, September 2026.",
    "h1": "Dog runs built for BVL's tighter, older lots",
    "lede": capsule(
        f"Pet turf in Buenaventura Lakes runs {price('pet')} per sq ft installed, typically {price('pet', True)}, as of September 2026. Most of the work here is "
        "sized to a narrow, fenced backyard on a 1980s or 1990s single-family lot rather than a wide-open estate yard, and a fair number of those lots also "
        "back a canal, which limits exactly where a run can go."),
    "sections": [
        ("Dog runs on BVL's narrower, zero-lot-line yards",
         "<p>Several of BVL's original PODs were platted with zero-lot-line or narrow side setbacks, which means a dog's whole outdoor world is often a rectangle "
         "20 to 30 feet deep rather than a sprawling backyard. That's not a problem for pet turf itself, but it does mean the drainage point and the infill choice "
         "matter more per square foot, since a smaller run absorbs the same daily rinsing and traffic as a larger one somewhere with more room to spread it out. "
         "Homeowners searching for the best pet turf installer near me in Buenaventura Lakes are usually trying to solve exactly this: how to keep a small, "
         "fenced strip from smelling by August rather than how to fill a big lawn.</p>"),
        ("Where a canal backyard limits run placement",
         "<p>On a lot that backs one of BVL's canals or retention ponds, a dog run has the same 10-foot waterbody buffer as any other turf, seawall or bulkhead "
         "aside, and it can't be routed through a drainage swale even if that flat strip looks like the obvious spot. That usually pushes a run closer to the "
         "house or along a side fence instead of the back property line, which changes the drain point planning more than it changes the build itself. On these "
         "lots we plan the run's low point toward an area the yard already sheds water to, rather than fighting the existing grade toward the canal. A fence "
         "line run also tends to sit farther from the bank than an owner first expects once the buffer and the dog's actual turning radius are both marked out "
         "on the ground.</p>"),
        ("Pet turf inside an HOA-managed cluster",
         "<p>In a townhome or condo section of BVL that still runs an active association, a small fenced pet area usually needs the same spec-sheet submittal as "
         "any other exterior change, and the board may care specifically about drainage onto a shared common area next door. That's a different conversation than "
         "the older single-family PODs have, where there's often no board to ask at all. Either way, the technical build, backing, base depth and infill, doesn't "
         f"change; what changes is whether paperwork happens before or instead of a phone call to the county. {svc('pet', 'The full pet turf guide')} covers backing "
         f"and infill choice in more depth, and {city('meadow-woods', 'the neighboring Meadow Woods page')} runs through a similar zero-lot-line pattern just across "
         "the county line.</p>"),
    ],
    "scenario": ("A dog run sized to a typical BVL side yard",
                 "<p>Say you have a 12 by 30 ft run along the fence line of a 1990s Coral Wood home, 360 sq ft total, for two dogs that already wear a visible path "
                 "along the fence. At the published pet turf range that's $3,600 to $6,480 installed; at the more typical $12-$16 band, figure $4,320 to $5,760. "
                 "That price covers the deeper washed-rock base a pet system needs, a fully permeable backing and zeolite or coated-sand infill, all sized up from "
                 "a plain lawn build because two dogs on 360 sq ft put more liquid through the base than the same footprint of family lawn ever would.</p>"),
    "faqs": [
        faq("Can I put a dog run right up to my BVL canal or pond?",
            "No, not without a seawall or bulkhead already there. The state buffer is 10 feet from the water's edge regardless of what the turf is for, and a "
            "drainage swale can't be turfed at all."),
        faq("Does my HOA need to approve a dog run in Buenaventura Lakes?",
            "Only if your section has an active association. Some BVL townhome clusters review exterior changes; many of the older single-family PODs currently "
            "have no board doing that. Check your own documents rather than assuming."),
        faq("What if my BVL dog run already smells no matter how often I rinse it?",
            f"That usually points to a base or infill problem rather than a rinsing schedule. {post('how-to-get-dog-urine-smell-out-of-artificial-turf', 'This guide')} "
            "walks through the causes step by step before assuming the whole run needs replacing."),
    ],
    "sources": [DRAIN_BVL, HOA_LAKEPOINTE, MSTU_BVL],
}

LOCAL["putting"] = {
    "title": "Backyard Putting Greens in Buenaventura Lakes, FL",
    "meta": "Backyard putting green installation in Buenaventura Lakes: an honest look at lot sizes here versus golf-front communities, with September 2026 pricing.",
    "h1": "Putting greens sized to BVL's standard lots",
    "lede": capsule(
        f"Backyard putting greens in Buenaventura Lakes run {price('putting')} per sq ft installed, typically {price('putting', True)}, as of September 2026. It's "
        "a smaller market here than in a golf-front community: most BVL lots were platted for a family home and a screened pool, not a green, so the greens we "
        "build tend to be compact chip-and-putt setups rather than multi-hole layouts."),
    "sections": [
        ("Why this is a smaller market here than in a golf community",
         "<p>Communities built directly around an active course tend to generate steady putting-green work because the lots themselves were sold on that view and "
         "that lifestyle. BVL isn't that kind of place: the Osceola Golf Club that some of its streets were platted around is listed as closed by course-tracking "
         "sites, and the lots facing those old fairways are larger and more open than a typical BVL yard, but they were never marketed as golf-course real estate "
         "the way a community built in the last twenty years might be. We're honest that a putting green here is a smaller, occasional job, not a category we "
         "install every week, which is a different pitch than a hub page for a golf-front community would give.</p>"),
        ("Fitting a green onto a standard single-family lot",
         "<p>Most putting-green work in BVL fits into a backyard that also has to hold a pool cage, a shed and whatever's left of the original lawn, so contouring "
         "gets scaled down to what the space allows rather than built out with multiple pin positions. A compact green with two or three cups and a short fringe "
         "collar suits a yard like that better than a sprawling layout that would eat the whole usable footprint. Base work is the same washed crushed rock "
         "standard as any other turf project here, just crowned and compacted more precisely for a true roll, since a putting surface shows an uneven base far "
         "more obviously than a plain lawn ever would.</p>"),
        ("Putting turf near the old fairway lots",
         "<p>On the deeper lots that back the closed golf course, there's more room to work with, and a few of those yards could support a larger green than the "
         "average BVL lot. The mature landscaping planted when those lots were sold in the 1980s is the main constraint: a live oak or mature palm near the back "
         f"property line still triggers the drip-line rule before any excavation, arborist letter and all, no matter how much open grass the lot otherwise has. "
         f"{svc('putting', 'The putting green service page')} covers contouring and fringe options in more depth, and a nearby community with more purpose-built "
         f"golf lots, {city('hunters-creek', 'Hunters Creek')}, sees a different mix of requests for the same reason.</p>"),
    ],
    "scenario": ("Sizing a compact green for a standard BVL backyard",
                 "<p>Say you have a 300 sq ft corner of a backyard left over after the pool cage and a small lawn, enough for a two-cup green with a chipping "
                 "collar. At the published range that's $4,200 to $9,000 installed; at the typical $18-$25 band most putting-green jobs fall into, figure $5,400 "
                 "to $7,500. That's a modest job by putting-green standards, sized to what a standard-issue BVL lot has left over rather than to a purpose-bought "
                 "golf lot, and it's a realistic number for the kind of yard most of the community actually has. Adding a third cup or a small chipping bunker "
                 "would push that estimate toward the top of the range rather than change the footprint much.</p>"),
    "faqs": [
        faq("Is a backyard putting green a common request in Buenaventura Lakes?",
            f"Not especially. It's a real but small part of what we build here compared with a golf-front community, since most BVL lots were platted for a "
            f"family home rather than a golf view. {post('backyard-putting-green-cost-florida', 'This cost breakdown')} applies the same way it would anywhere "
            "else in Central Florida."),
        faq("Can a putting green go near the old Osceola Golf Club fairways?",
            "Often yes, since those lots tend to be deeper, but check for mature oaks or palms along the property line first. The drip-line rule applies there "
            "the same as anywhere else in the county."),
    ],
    "sources": [GOLF_BVL, LANDSTAR],
}

LOCAL["playground"] = {
    "title": "Playground Turf in Buenaventura Lakes, FL",
    "meta": "Playground turf for Buenaventura Lakes backyards and small play areas: shock pad sizing, fall height and September 2026 market pricing.",
    "h1": "Backyard play surfaces sized to BVL's family lots",
    "lede": capsule(
        f"Playground turf in Buenaventura Lakes runs {price('playground')} per sq ft installed, typically {price('playground', True)}, as of September 2026. Most "
        "jobs here are a backyard play corner sized for swings or a small climbing set rather than a full commercial structure, scaled to fit next to a pool "
        "cage or a dog run on the same standard-sized lot."),
    "sections": [
        ("Backyard play areas versus the community's public parks",
         f"<p>Buenaventura Lakes already has public play space at {ext('https://www.osceola.org/Community/Parks-and-Public-Lands/Find-a-Park-or-Facility/Buenaventura-Community-Park', 'Buenaventura Community Park')}, "
         "with its ball fields and batting cages, so backyard playground turf here tends to fill a different need: a safer surface right outside the back door "
         "for a toddler or a young grade-schooler, not a substitute for the county's fields. A shock pad sized to the fall height of whatever equipment sits on "
         "it matters more than the turf blade itself for that use, since the pad is what actually cushions a fall, not the grass on top of it. Sizing that pad "
         "correctly matters more on a small backyard corner than it would on a full-scale public field, since there's less margin for a fall to land past the "
         "cushioned area entirely.</p>"),
        ("Fitting a play surface onto a standard BVL lot",
         "<p>A typical single-family lot from the Strafford Park or Coral Wood era already has a screened pool, a shed and whatever's left of the lawn competing "
         "for backyard space, so a play area here is usually a defined corner rather than the whole yard. Keeping it out of a live oak's drip line and at least "
         "10 feet from a canal or pond edge, where either applies, generally still leaves enough room for a swing set or small climbing structure once the pad "
         "and turf are sized to the equipment rather than the whole lot. Measuring the fall zone around the equipment before finalizing the footprint avoids a "
         "corner that looks big enough on paper but comes up short once the pad's required clearance is marked out.</p>"),
        ("Building for a household with more than one child",
         "<p>Census figures for Buenaventura Lakes show larger average household sizes than many surrounding Central Florida suburbs, and in practice that often "
         "means a play surface here gets built for two or three kids using it at once rather than one. That mostly changes the shock-pad spec and the traffic "
         "pattern we plan for, denser infill and a slightly thicker pad under the busiest section, rather than the footprint itself. A yard serving multiple "
         "children also tends to need more than one activity zone worked into the same small corner, which is a layout question worth raising before ordering "
         f"equipment rather than after. {svc('playground', 'The playground turf guide')} goes through shock-pad ratings by fall height in more detail than fits here.</p>"),
    ],
    "scenario": ("A backyard play corner, sized and priced",
                 "<p>Say you have a 200 sq ft corner behind a Coral Wood home for a small swing set with a 4 ft fall height. At the published range that's "
                 "$2,000 to $5,000 installed; at the typical $12-$19 band most residential play areas fall into, figure $2,400 to $3,800. A shock pad rated for "
                 "that fall height is the main cost driver beyond the turf itself, and a corner that size usually clears both the oak drip line and any canal "
                 "buffer on a standard BVL lot without forcing a redesign. Stepping up to a taller swing set later would mean a thicker pad, not a bigger "
                 "turfed area, if the footprint stays the same.</p>"),
    "faqs": [
        faq("What fall height does playground turf need to handle in a BVL backyard?",
            "Whatever the tallest piece of equipment on it, measured from the highest platform or seat a child could fall from. The shock pad thickness is sized "
            "to that number, not to the turf itself."),
        faq("Can playground turf go near Buenaventura Community Park instead of in my own yard?",
            "The county park is public space we don't install on; it's mentioned here only as the community's existing play option. Backyard playground turf is "
            "a private-yard project on your own lot."),
    ],
    "sources": [PARK_BVL, PARK_GUEVARA, CENSUS_BVL],
}

LOCAL["pool"] = {
    "title": "Pool & Lanai Turf in Buenaventura Lakes, FL",
    "meta": "Turf around pools and inside 1980s-90s screen enclosures in Buenaventura Lakes: drainage underlay, glue-down edges and September 2026 pricing.",
    "h1": "Turf inside BVL's original screen-cage pools",
    "lede": capsule(
        f"Pool and lanai turf in Buenaventura Lakes runs {price('residential')} per sq ft installed, typically {price('residential', True)}, as of September 2026, "
        "usually landing toward the upper half of that range. Most of the work is inside a screened cage original to a 1980s or 1990s home, where the concrete "
        "deck and the enclosure track shape the whole layout."),
    "sections": [
        ("Turf inside a 30- to 40-year-old screen enclosure",
         "<p>A pool cage built when Strafford Park or Coral Wood went up is now three to four decades old, and the concrete deck inside it rarely graded well "
         "even when new; sun and settling since then usually leave low spots that hold water after a rinse. Turf over that deck needs a drainage underlay between "
         "the concrete and the turf backing so water still has somewhere to go, plus edges glued rather than nailed, since driving a stake through a cage's "
         "existing slab isn't an option. Working inside the aluminum enclosure track also means every cut is measured to that fixed boundary rather than to an "
         "open yard where a little overage is easy to trim.</p>"),
        ("Where the deck meets the yard outside the cage",
         "<p>Plenty of BVL pool lots have a narrow strip of real lawn between the screen enclosure and the property line, and that strip often backs a canal or "
         "a neighbor's fence rather than opening onto open grass. The transition from glued turf-on-concrete inside the cage to turf-on-base outside it needs a "
         "clean edge at the enclosure's foundation, and if that outside strip also sits within 10 feet of a canal, the water buffer applies there even though the "
         "cage itself is unaffected. Planning both sections as one job rather than two separate ones is what keeps that transition line straight instead of "
         "wandering along the screen track, and it also means the base under both areas gets graded to the same finished height from the start.</p>"),
        ("Heat and glare around a screened pool",
         "<p>A screen enclosure cuts direct sun less than most homeowners expect, so pool-deck turf in BVL still reaches the 120 to 150 degree range common on "
         "exposed Florida turf, and a low-E window on the house side of some of these lanais can add reflected heat on top of that. A hose rinse before anyone "
         "walks the deck barefoot drops the surface temperature fast, and checking which windows face the cage before finalizing turf placement avoids the melted "
         f"spot that low-E glass can cause on a hot afternoon. {svc('pool', 'The pool and lanai turf page')} covers drainage underlay options in more depth, and "
         f"{city('st-cloud', 'St. Cloud')}, another lake-heavy Osceola County town, sees the same screen-cage pattern on its older lots.</p>"),
    ],
    "scenario": ("Turfing the deck strip inside a BVL pool cage",
                 "<p>Say you have a 500 sq ft ring of concrete deck inside a 1994 screen enclosure, plus a 150 sq ft strip of real lawn just outside the cage "
                 "wall. At the published residential range that's $5,200 to $11,700 installed for the combined 650 sq ft; since deck work runs the upper half of "
                 "that range for the glue-down and drainage underlay, expect the deck portion closer to $14-$18 a foot and the outside strip closer to the "
                 "standard $10-$16 band. The enclosure's footprint sets the deck cuts exactly; the outside strip has more flexibility, so any waste from an "
                 "awkward cut is easier to absorb there than inside the fixed aluminum track.</p>"),
    "faqs": [
        faq("Does pool-deck turf need a different base than a regular BVL lawn?",
            "Yes, over existing concrete it needs a drainage underlay instead of washed crushed rock, since there's no soil underneath to grade or compact."),
        faq("Will turf inside my screen enclosure still get hot?",
            "It can. A screen cuts glare more than heat, so the same hose-rinse routine that cools open-yard turf works just as well on a lanai."),
        faq("Can a window reflection actually melt turf on my BVL lanai?",
            f"Yes, if a low-E window or slider is aimed at it. {post('can-artificial-turf-melt', 'This explainer')} covers the temperature threshold and how to "
            "spot the damage pattern before it spreads."),
    ],
    "sources": [STRAFFORD, CORALWOOD, LANDSTAR],
}

LOCAL["str"] = {
    "title": "Vacation Rental Turf in Buenaventura Lakes, FL",
    "meta": "Artificial turf for rental-home yards in Buenaventura Lakes: an honest look at the market outside Osceola's short-term rental overlay, priced Sept. 2026.",
    "h1": "Rental-home turf outside BVL's overlay boundary",
    "lede": capsule(
        f"Vacation rental turf in Buenaventura Lakes runs {price('residential')} per sq ft installed, typically {price('residential', True)}, as of September "
        "2026. This is a small market here: BVL sits outside Osceola County's short-term rental overlay corridor, so most of the turf work tied to a rental "
        "property is for long-term tenant turnover rather than a licensed nightly guest home."),
    "sections": [
        ("Why BVL isn't a nightly-rental hotspot",
         f"<p>{ext(STR_OVERLAY[1], 'Osceola County limits licensed short-term rentals')} to specific overlay districts and resort-corridor communities along "
         "US-192, and standard residential zoning like most of BVL treats a nightly rental as a use it doesn't permit. That's a different situation from a "
         "community like Reunion or ChampionsGate, where nightly rentals are the zoned expectation and turf gets sized around guest turnover. In BVL, a "
         "homeowner turfing a rental-property yard is almost always managing a standard lease, not a nightly booking calendar, and the yard rarely needs to "
         "hold up to the same weekly guest turnover a resort-corridor property does. That difference shows up in the build itself, not just the paperwork, "
         "since there's less reason to over-spec the infill or backing for wear that isn't happening.</p>"),
        ("Turf for turnover between long-term tenants",
         "<p>Where turf does show up on a BVL rental, it's usually because an owner is tired of re-sodding a yard between tenants on a 30- to 45-year-old "
         "irrigation system that a new renter isn't going to maintain carefully. Turf removes that maintenance variable entirely between leases: no dead patches "
         "from a tenant who skipped watering, no re-sodding line item before the next listing goes up. The build itself is the same standard residential job as "
         "an owner-occupied lawn, since there's no guest-turnover wear pattern to design around, and the same market range applies whether the home is owner-"
         "occupied or leased out. Landlords managing several BVL units sometimes turf them one at a time as leases turn over, rather than all at once.</p>"),
        ("What changes if a BVL property is grandfathered or licensed",
         "<p>A small number of BVL parcels may carry an older license or fall under a different zoning history than the surrounding neighborhood, and that's a "
         "question for the county zoning office, not something we verify as part of a turf quote. If a property is actually operating as a licensed nightly "
         f"rental, the same guest-turnover reasoning that applies in the US-192 resort corridor, faster wear, more frequent rinsing, applies here too. "
         f"{svc('str', 'The vacation rental turf page')} goes through that guest-turnover build in full, and {city('lake-nona', 'Lake Nona')} is a useful "
         "comparison since it mixes long-term homes with a smaller pocket of licensed rentals the same way BVL's edges might. Confirming the zoning status "
         "first avoids designing around the wrong wear pattern entirely.</p>"),
    ],
    "scenario": ("Turf for a long-term rental's back lawn",
                 "<p>Say you have an 800 sq ft backyard on a rental home you lease on a standard 12-month term, tired of the sod dying every time a tenant "
                 "forgets to water through a dry spring. At the published range that's $6,400 to $14,400 installed; at the typical $10-$16 band, figure $8,000 "
                 "to $12,800. That one-time cost replaces a re-sodding bill an owner would otherwise face every lease turnover or two on an older irrigation "
                 "system, which is the actual math most BVL rental owners are running, not a nightly-guest calculation. Spread over several lease cycles, it "
                 "usually works out cheaper than repeatedly re-sodding the same 800 sq ft.</p>"),
    "faqs": [
        faq("Can I run a nightly vacation rental on artificial turf in Buenaventura Lakes?",
            "That depends on zoning, not turf. Most of BVL sits outside Osceola County's short-term rental overlay, so check with the county zoning office "
            "before assuming a property can operate as a licensed nightly rental at all."),
        faq("Is vacation rental turf a big part of what gets installed in BVL?",
            "No, it's a small slice compared with owner-occupied lawns, since the neighborhood isn't in the county's short-term rental corridor. Most rental-"
            "related turf work here is for standard long-term leases."),
        faq("What should a landlord expect on install day for a BVL rental property?",
            f"The same process as an owner-occupied job. {post('what-to-expect-on-turf-installation-day', 'This walkthrough')} covers the sequence from strip-out "
            "to final rinse, whether a tenant is currently living there or the unit is vacant between leases."),
    ],
    "sources": [STR_OVERLAY],
}

LOCAL["commercial"] = {
    "title": "Commercial Turf for Buenaventura Lakes Properties",
    "meta": "Commercial artificial turf for Buenaventura Lakes: townhome common areas, HOA-managed clusters and the Osceola Parkway retail corridor. Quoted per job.",
    "h1": "Common-area turf along BVL's commercial edge",
    "lede": capsule(
        "Commercial turf jobs in Buenaventura Lakes are quoted per job rather than a flat per-square-foot rate, since scope ranges from a small HOA-managed "
        "common area to a storefront strip along the neighborhood's commercial edge. Most requests come from either a townhome association or a business "
        "fronting the Osceola Parkway corridor that runs along BVL's northern boundary."),
    "sections": [
        ("Common areas inside HOA-managed clusters",
         "<p>Sections of BVL with an active association, the townhome and condo clusters more than the older single-family PODs, sometimes maintain a shared "
         "entry median, mail-kiosk island or small common lawn that a board wants off an irrigation cycle entirely. That work runs through the association's "
         "approval process rather than an individual homeowner's, and the board typically wants a maintenance-cost comparison against the sod it's replacing "
         "before signing off, since the association is paying for years of upkeep at once rather than a single household budgeting for a private yard. That "
         "comparison is usually the deciding factor, more than the turf's appearance, since a board answers to owners who see the maintenance line item every "
         "year.</p>"),
        ("Storefronts along the Osceola Parkway corridor",
         "<p>East Osceola Parkway functions as BVL's commercial spine, and a storefront or small office along that frontage sometimes wants turf for a planter "
         "strip or an entry island where sod never establishes well under reflected heat off a parking lot. That's a different design problem than a residential "
         "yard: heavier foot traffic near a doorway, no irrigation zone to speak of in a lot of cases already, and a base built to handle a delivery cart more "
         "than bare feet. Visibility from the road also matters more here than on a backyard job, since a planter strip facing traffic gets judged on how flat "
         "and clean it looks from a moving car.</p>"),
        ("Scoping a commercial job before pricing it",
         "<p>Because a common-area island and a storefront planter strip are such different jobs, we measure and look at drainage and access before quoting "
         "either one rather than working from a published range the way a residential lawn can. An HOA board should expect the same site visit a homeowner gets, "
         f"plus a written scope covering who maintains the turf once it's down. {svc('commercial', 'The commercial turf page')} has more on scoping a shared-"
         f"area job, and {a('/laws/hoa-rules/', 'the rules governing what a Florida association can require')} apply to a board vote here the same as they "
         "would to an individual homeowner. Getting that scope in writing before a vote also gives owners something concrete to compare against a second bid.</p>"),
    ],
    "scenario": ("Pricing a small HOA entry island, roughly",
                 "<p>Say a townhome association wants a 400 sq ft entry median off irrigation, currently sod that needs mowing and replacing every few years. "
                 "Using the residential per-square-foot range as a rough planning number, not a quote, that lands somewhere between $3,200 and $7,200 depending "
                 "on how much of the existing irrigation has to be capped and whether the median's edging needs rebuilding to hold the turf in place. A board "
                 "comparing that one-time figure against years of mowing, edging and re-sodding a small median is usually the calculation driving the request, "
                 "and an actual number still needs a site visit rather than this kind of back-of-envelope math.</p>"),
    "faqs": [
        faq("Does an HOA need multiple bids for a common-area turf project in Buenaventura Lakes?",
            "Many association bylaws require it for a capital expense; check your governing documents. We're glad to provide one of several bids a board "
            "collects before a vote."),
        faq("Can commercial turf go on a planter strip along Osceola Parkway?",
            "Yes, with a base built for foot and cart traffic rather than a residential lawn spec. We measure the specific site before pricing it."),
    ],
    "sources": [HOA_LAKEPOINTE, MSTU_BVL],
}

LOCAL["sports"] = {
    "title": "Sports & Fitness Turf in Buenaventura Lakes, FL",
    "meta": "Backyard sports turf in Buenaventura Lakes: bocce lanes and home-gym strips sized to standard lots, priced per job as of September 2026.",
    "h1": "Home sports surfaces on BVL's standard lots",
    "lede": capsule(
        "Sports and fitness turf in Buenaventura Lakes is quoted per job rather than a flat rate, since a bocce lane, an agility strip and a sled track all "
        "need different lengths and bases. Most requests here fit into a standard single-family backyard rather than the acreage lots that support a full "
        "batting cage or multi-sport court elsewhere in the county."),
    "sections": [
        ("Backyard sports lanes versus the county's public fields",
         f"<p>Buenaventura Lakes residents already have access to real ball fields and batting cages at "
         f"{ext('https://www.osceola.org/Community/Parks-and-Public-Lands/Find-a-Park-or-Facility/Buenaventura-Community-Park', 'Buenaventura Community Park')}, so a backyard sports "
         "install here tends to be a training strip, a sled track, an agility lane, a home-gym pull-sled path, rather than a competitive-scale surface. That "
         "changes the design goal: a 40 to 60 ft straight run with a firm, consistent base matters more than the width or shape a full field would need. "
         "Most of these requests come from someone training for a specific sport rather than building a general-purpose backyard court, and the layout "
         "reflects that from the first measurement rather than being adjusted later once the base is already down.</p>"),
        ("Fitting a sports lane on a canal or narrow lot",
         "<p>A lane long enough for sled work often runs the full depth of a standard BVL backyard, which means it can bump into the same 10-foot canal or pond "
         "buffer a lawn conversion would face on a waterfront lot, or into a live oak's drip line on an older, more heavily landscaped property. Laying the lane "
         "out on a diagonal, or splitting it around an obstacle instead of running straight to the property line, usually solves both without shortening the "
         "usable length by much. Measuring the actual clear run before committing to a lane length avoids finding out mid-install that a buffer or a root zone "
         "eats more of the yard than expected.</p>"),
        ("A firmer base for repeated impact",
         "<p>A bocce lane or a sled track takes more repeated, concentrated load in one direction than a lawn ever does, so the washed crushed rock base under "
         "it gets compacted more aggressively and, on a bocce court specifically, screeded flatter than a general lawn base needs to be. That extra base "
         f"attention is where the per-job pricing difference from a plain residential install comes from, not the turf product itself. "
         f"{svc('sports', 'The sports and fitness turf page')} covers base specs for a batting cage or an agility lane too, for a BVL yard with room for "
         "either one. Skipping that extra compaction pass is the most common reason a backyard sports surface goes soft faster than the lawn next to it.</p>"),
    ],
    "scenario": ("A sled lane, roughly scoped",
                 "<p>Say you have a 50 by 4 ft strip along a side fence, 200 sq ft, for a home-gym sled track on a lot that also backs a drainage canal 30 "
                 "feet farther on. Using the residential range as a rough guide for the base and turf alone, before the extra compaction pass a lane like this "
                 "needs, that's $1,600 to $3,600 in material and standard labor terms; the firmer base work typically adds to the top of that range rather than "
                 "the bottom. The canal at the back of the lot doesn't affect a lane this short unless the layout is stretched toward the property line, which "
                 "usually isn't necessary for sled work anyway.</p>"),
    "faqs": [
        faq("How long does a home sled track need to be in a BVL backyard?",
            "Most run 40 to 60 ft, which fits most standard lots here once canal buffers or an oak's drip line are accounted for. We measure the actual yard "
            "before quoting a length."),
        faq("Is a backyard bocce court common in Buenaventura Lakes?",
            "It's a niche request compared with lawn conversions, but the base work is straightforward on a standard lot. We quote it per job after a site "
            "visit."),
    ],
    "sources": [PARK_BVL],
}

LOCAL["pavers"] = {
    "title": "Turf & Pavers for Buenaventura Lakes Driveways",
    "meta": "Turf ribbons between pavers and stepping-stone paths for Buenaventura Lakes yards, sized to the narrow side yards common in 1980s-90s PODs. Quoted per job.",
    "h1": "Turf ribbons for BVL's narrow side yards",
    "lede": capsule(
        "Turf-and-paver work in Buenaventura Lakes is quoted per job, and it's a natural fit for the narrow side yards common across the neighborhood's original "
        "1980s and 1990s PODs, where a strip too tight for a mower still needs to look finished between two houses."),
    "sections": [
        ("Zero-lot-line side yards that never grow grass well",
         "<p>A side yard three to four feet wide between two BVL homes gets almost no direct sun for most of the day, and mower access is often nonexistent "
         "without walking through a neighbor's gate. Turf ribbons set between paver stepping stones solve both problems at once: no mowing required, and the "
         "paver line gives a clean walking surface where grass alone would just wear into a dirt path within a season regardless of how much sun it got. It's "
         "one of the more straightforward jobs we do in BVL precisely because there's so little else the space could realistically be used for, and there's no "
         "irrigation zone worth saving in a strip that narrow.</p>"),
        ("Driveway edging and stepping-stone paths",
         "<p>Original concrete driveways from the Strafford Park and Coral Wood era are often narrower than a modern two-car driveway calls for, and a turf "
         "strip along one edge, paver-lined or not, adds functional width without pouring more concrete. The same combination works for a stepping-stone path "
         "from a driveway to a side gate, a common request on lots where the direct route was never paved in the original build. Either job usually takes a "
         "day or two, since there's no sod or old turf to strip out first the way a full lawn conversion needs, which keeps the cost toward the lower end of "
         "a typical residential quote per square foot involved.</p>"),
        ("Base work for a turf-and-paver combination",
         "<p>Where turf meets a paver edge, the base under both needs to be compacted to the same finished height so the two surfaces read as one flat plane "
         "rather than a lip that catches a mower wheel or a stroller. That's more precise grading than a plain lawn conversion needs, since the tolerance is "
         f"measured against a fixed paver line instead of just sloping generally away from the house. Resetting a few pavers is often part of getting that "
         f"height right rather than an extra step added on afterward. {svc('pavers', 'The turf-and-pavers page')} has more on combination layouts, and "
         f"{post('artificial-grass-for-shady-side-yards', 'this article')} goes deeper into shade-only side yards specifically, a common condition on these "
         "narrow lots.</p>"),
    ],
    "scenario": ("A side-yard turf-and-paver strip, worked out",
                 "<p>Say you have a 4 by 40 ft side yard, 160 sq ft, between two Coral Wood-era houses, with a run of stepping-stone pavers already down the "
                 "middle. Treating the turf portion at the standard residential range, the turf alone runs $1,280 to $2,880 before adding the paver-line "
                 "grading work, which is priced per job rather than by the foot since it depends on how many pavers are being reset versus left in place. A "
                 "strip this size and shape is a common layout across BVL's original PODs, where the lot width between houses rarely leaves more room than "
                 "this to work with.</p>"),
    "faqs": [
        faq("Can turf and pavers go in a side yard that gets almost no sun?",
            "Yes. Since the turf isn't living grass, shade that would kill sod isn't a factor; the main design question is drainage and how the paver line "
            "meets the base."),
        faq("Is a turf-and-paver driveway edge common in Buenaventura Lakes?",
            "It's a frequent request given how many original driveways here are narrower than current builds. We quote it per job based on the specific "
            "layout."),
    ],
    "sources": [STRAFFORD, CORALWOOD],
}

LOCAL["repair"] = {
    "title": "Artificial Turf Repair in Buenaventura Lakes, FL",
    "meta": "Turf repair in Buenaventura Lakes: seams, root heave from mature oaks and low-E glass damage on closely spaced 1980s-90s lots. Quoted per visit.",
    "h1": "Fixing turf on BVL's older, closely spaced lots",
    "lede": capsule(
        "Artificial turf repair in Buenaventura Lakes is quoted per visit rather than by the square foot, since a lifted seam, a root-heaved section and a "
        "melted patch each take a different amount of work to fix. Repair calls here often trace back to the neighborhood's age: turf installed years ago on "
        "an unwashed base, or a mature tree that's grown since the original install."),
    "sections": [
        ("Root heave from oaks planted decades ago",
         "<p>Landscaping planted when Strafford Park and Coral Wood were new is now mature enough that a live oak's surface roots can lift a turf section from "
         "underneath years after installation, even when the original build respected the drip line. That shows up as a rise or wrinkle that wasn't there when "
         "the turf went in, and the fix usually means pulling that section, trimming or working around the root without an arborist's sign-off if it's a "
         "structural cut, and rebuilding the base flat before relaying the same or matching turf. A repair like this tends to recur every few years on a lot "
         "with a large, actively growing oak nearby, since the root keeps expanding after the first fix.</p>"),
        ("Seams and edges on turf installed on the wrong base",
         "<p>Some of the older turf around BVL went down years before the current state standard required a washed, open-graded rock base, and unwashed fill "
         "with fines in it can bind into a crust that shifts unevenly under a seam over time. A lifted seam or a gapping edge on turf like that often isn't a "
         "simple re-glue; the base underneath usually needs correcting or the same movement just reopens the repair within a season. Telling the two apart "
         "before quoting saves a homeowner from paying twice for the same seam within a year, since a re-glue on a moving base rarely holds through a full "
         "rainy season once the ground underneath starts shifting again.</p>"),
        ("Low-E glass damage on closely spaced lots",
         "<p>Several of BVL's original PODs put homes close enough together that a low-E window or slider on one house can reflect concentrated sun onto a "
         "neighboring yard's turf, softening the blades in an odd, sharply defined patch that doesn't match wear from foot traffic. Identifying the reflecting "
         f"window before repairing the spot matters, since patching the turf without addressing the reflection angle just leads to the same damage returning. "
         f"{svc('repair', 'The turf repair page')} covers seam, edge and heat-damage fixes in more depth, and {post('artificial-turf-near-live-oaks-and-palms', 'this piece')} "
         "goes further into root damage from live oaks specifically. A yard with both problems, close-set homes and a mature oak, sometimes needs both fixes "
         "addressed on the same visit.</p>"),
    ],
    "scenario": ("A lifted seam repair, roughly scoped",
                 "<p>Say you have a 12 ft seam that's gapped open along one edge of a 600 sq ft backyard turfed about eight years ago on an original, unwashed "
                 "base. A straightforward re-glue on ground that's still draining and holding its grade is usually a single, minimum-charge service call; if "
                 "the gap traces back to base movement, the fix extends to pulling that section, rebuilding a few feet of base in washed rock, and relaying "
                 "the turf over it, which prices closer to a small partial-replacement job than a seam visit. Checking which cause applies before quoting is "
                 "what separates the two, and it's why repair here is priced after a look at the yard rather than off a flat rate.</p>"),
    "faqs": [
        faq("Why did my BVL turf wrinkle years after it was installed?",
            "Root growth from a nearby oak or unwashed fill settling under the base are the two most common causes here, given how mature the landscaping and "
            "how old some of the original builds are."),
        faq("Can a melted turf patch from a neighbor's window be repaired?",
            "Yes, but the reflection angle needs identifying first, or the same spot melts again. We check for low-E glass before quoting a repair on an odd, "
            "sharply outlined burn mark."),
    ],
    "sources": [STRAFFORD, CORALWOOD],
}

LOCAL["cleaning"] = {
    "title": "Artificial Turf Cleaning in Buenaventura Lakes, FL",
    "meta": "Turf cleaning and pet-odor treatment in Buenaventura Lakes: canal debris, oak leaf litter and multi-pet households. Quoted per visit, Sept. 2026.",
    "h1": "Turf cleaning for BVL's canals, oaks and pets",
    "lede": capsule(
        "Turf cleaning and maintenance in Buenaventura Lakes is quoted per visit based on yard size and how long it's been since the last service. The two "
        "recurring drivers here are organic debris blown in off the community's canals and lakes, and pet-odor buildup on the smaller, fenced yards common "
        "across the neighborhood."),
    "sections": [
        ("Debris from BVL's canals and mature tree canopy",
         "<p>A yard near one of BVL's canals or retention ponds collects windblown leaf litter and algae residue that a yard farther from water doesn't see as "
         "often, and mature oak canopy across many of the older PODs adds acorns and leaf drop through the fall and winter into that same mix. Left to work "
         "into the infill, that organic material slows the base's drainage the same way solid pet waste does, so a power-brooming and infill-refresh visit "
         "matters more here than on a newer, more open lot. A yard tucked under heavy canopy usually needs that visit on a shorter interval than an open, "
         "sunnier lot a few streets over.</p>"),
        ("Multi-pet households on smaller fenced yards",
         f"<p>Given BVL's larger average household sizes and the number of zero-lot-line yards in the community, pet-odor calls here often involve more than "
         "one dog on a yard smaller than the typical suburban lot, which concentrates odor faster than the same infill handles on a bigger property. A tighter "
         "rinsing and infill-check schedule than a single-dog household needs is usually the difference between staying ahead of it and calling for an "
         "odor-treatment visit every few months. Waiting until the smell is noticeable from the house usually means the infill has already fallen behind by "
         "more than a routine rinse can fix, at which point a single visit has more ground to make up.</p>"),
        ("Cleaning turf inside an older screen enclosure",
         "<p>Turf on a pool deck inside a 30- to 40-year-old screen cage traps different debris than open-yard turf, mostly fine dust and pollen that settles "
         "under a roofed structure rather than blowing through, plus whatever tracks in from the pool itself. That calls for a different cleaning approach than "
         f"power brooming an open lawn, closer to detailing a hard surface with a turf-safe rinse than raking infill back into shape. "
         f"{svc('cleaning', 'The turf cleaning and maintenance page')} covers pet-odor treatment in more depth, and "
         f"{post('oak-leaves-and-debris-on-artificial-turf', 'this article')} walks through clearing leaf and pine litter step by step. A deck cage rarely "
         "needs the same infill top-up an open-yard visit does, since less blows in and less washes out.</p>"),
    ],
    "scenario": ("A two-dog household near a canal, cleaning-wise",
                 "<p>Say you have a 700 sq ft fenced backyard on a canal lot with two dogs and a stand of oaks dropping leaves most of the fall. That's a "
                 "yard doing double duty: pet odor building up on a smaller footprint than a two-dog household would have farther from the water, plus "
                 "windblown debris settling into the infill from the canal side and the tree canopy on the other. A visit that combines power brooming, an "
                 "infill top-up and an odor treatment in one stop is usually more efficient here than scheduling the two separately, since both jobs start "
                 "with the same rake-through of the surface before anything gets treated.</p>"),
    "faqs": [
        faq("Why does turf near my BVL canal need more cleaning than a regular yard?",
            "Windblown organic debris, leaves, algae residue, acorns from mature oaks, works into the infill faster near water and under tree canopy, which "
            "slows drainage if it's not cleared regularly."),
        faq("How often should pet turf be cleaned in a multi-dog BVL household?",
            "More often than a single-pet yard, since odor concentrates faster on a smaller footprint with more daily use. We size a schedule to the specific "
            "yard and pet count rather than a fixed interval."),
    ],
    "sources": [CENSUS_BVL, DRAIN_BVL],
}

LOCAL["replacement"] = {
    "title": "Turf Removal & Replacement in Buenaventura Lakes",
    "meta": "Replacing worn-out artificial turf or dead lawns in Buenaventura Lakes on original 1970s-90s lots, with base correction. Quoted per job, Sept. 2026.",
    "h1": "Replacing worn turf on BVL's original lots",
    "lede": capsule(
        "Turf removal and replacement in Buenaventura Lakes is quoted per job, close to a new install minus whatever base can be reused. Replacement calls here "
        "tend to involve either turf that's aged out after ten to twenty years or a natural lawn that's been declining since the neighborhood's original "
        "1970s-90s build-out."),
    "sections": [
        ("Turf that's reached the end of a ten- to twenty-year lifespan",
         "<p>Some of the earliest turf installed in BVL predates the current state standard for base and infill, and turf that age is often faded, matted flat "
         "along traffic paths, or backed with material that's stopped draining the way it did when it was new. Replacement on a lot like that usually means "
         "pulling the old surface, checking whether the existing base still meets today's washed, open-graded standard, and rebuilding it if it doesn't rather "
         "than laying new turf over old fill that was never washed to begin with. A visible fade in the color is usually the least of the problems by the time "
         "a lawn reaches this point, since the backing and infill underneath have typically worn out well before the color does.</p>"),
        ("Correcting a base built before the current standard",
         f"<p>{src('dep-rule', 'the state synthetic turf rule')} now requires subgrade material washed before installation so fines do not bind into a crust, a step some older BVL installs "
         "skipped entirely. A base like that often shows up as a lawn that stayed soggy for days after a storm even though the turf on top drained fine, which "
         "points to the rock underneath rather than the surface as the actual problem. Replacement is the point where that gets corrected, since redoing the "
         "base is far more disruptive once new turf is already down, and skipping the correction just carries the same drainage complaint into the new "
         "surface for another decade rather than actually fixing it.</p>"),
        ("Replacing a declining natural lawn instead of turf",
         "<p>Plenty of BVL replacement calls start with St. Augustine or Bahia that's been thinning for years under mature oak shade or fighting an aging "
         "irrigation zone that no longer covers the yard evenly. Converting that lawn rather than replacing dead grass with more sod addresses the underlying "
         "cause, shade and irrigation, rather than the symptom, and it's the same base-and-turf build as any other residential install once the old grass and "
         f"root mat are stripped out. {svc('replacement', 'The turf removal and replacement page')} covers that base-correction process step by step, and "
         f"{post('how-long-does-artificial-turf-last-in-florida', 'this article')} sets realistic expectations for how long the new surface should hold up "
         "once the underlying cause is actually addressed.</p>"),
    ],
    "scenario": ("Replacing a 15-year-old turf lawn on an original BVL lot",
                 "<p>Say you have an 850 sq ft backyard turfed roughly 15 years ago on a base that was never washed, now faded and holding water for days after "
                 "rain. At the published residential range that's $6,800 to $15,300 for a full replacement including base correction; at the typical $10-$16 "
                 "band, figure $8,500 to $13,600. Reusing any part of the old base isn't an option here since the fines that caused the drainage problem are "
                 "exactly what has to come out, so this prices closer to a full new install than a simple resurfacing job would. The new turf on top of a "
                 "corrected base should hold up for the full ten- to twenty-year range rather than repeating the same failure early.</p>"),
    "faqs": [
        faq("How do I know if my BVL turf needs replacing versus just cleaning?",
            "Matted, faded turf that stays wet for days after rain usually points to a base or backing problem cleaning won't fix. A site visit can tell the "
            "difference before you pay for one or the other."),
        faq("Can the old base be reused when replacing turf in Buenaventura Lakes?",
            "Sometimes, if it was washed rock to begin with and still drains well. Older installs on unwashed fill usually need the base rebuilt, not just the "
            "surface replaced."),
    ],
    "sources": [DRAIN_BVL],
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
