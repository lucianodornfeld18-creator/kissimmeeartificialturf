# -*- coding: utf-8 -*-
"""Mascotte, FL (tier 3, Lake County). Hub + residential/pet/putting city x service pages.
Researched September 2026: City of Mascotte site (Building Department contracted to Willdan
Engineering, Water Division), a 2018 SJRWMD cost-share release, Lake.WaterAtlas.org for Sunset Lake
and Lake Linda, Census/Data USA population figures, and public listings for the Sunset Lakes Estates
and Woodbury subdivisions. USDA soil contrast drawn from the Candler/Astatula ridge series already
verified for Lake County (site/content/c_counties.py) against the Immokalee/Myakka flatwoods family
named on SJRWMD's own general soil map for the county."""
from _data import CITIES
from _helpers import page, capsule, sec, table, faq, a, svc, city, post, ext, price
from _cityservice import cityservice_pages

SLUG = "mascotte"

MASCOTTE_BUILDING = ("City of Mascotte — Building Department", "https://www.cityofmascotte.com/169/Building-Dept---Permits-Inspections")
MASCOTTE_PORTAL = ("City of Mascotte — online permit portal", "https://mascottefl.portal.iworq.net")
MASCOTTE_WATER = ("City of Mascotte — Water Division", "https://www.cityofmascotte.com/182/Water-Division")
SJRWMD_MASCOTTE = ("St. Johns River Water Management District — water main partnership with Mascotte, 2018", "https://www.sjrwmd.com/2018/09/district-partners-with-mascotte-for-water-main-replacement-project/")
SJRWMD_RESTRICT = ("St. Johns River Water Management District — watering restrictions", "https://www.sjrwmd.com/wateringrestrictions/")
IMMOKALEE_OSD = ("USDA NRCS — official series description, Immokalee series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/I/IMMOKALEE.html")
MYAKKA_OSD = ("USDA NRCS — official series description, Myakka series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/M/MYAKKA.html")
SJRWMD_SOILMAP = ("SJRWMD — general soil map metadata (Myakka-Immokalee-Waveland and related associations)", "https://secure.sjrwmd.com/docs/metadata/gensoils.htm")
MASCOTTE_POP = ("Data USA / U.S. Census Bureau — Mascotte, FL population", "https://datausa.io/profile/geo/mascotte-fl")
MASCOTTE_POP_RANK = ("BiggestUSCities.com — Mascotte, Florida population history, 1990-2022", "https://www.biggestuscities.com/city/mascotte-florida")
SUNSET_LAKE_SRC = ("Lake.WaterAtlas.org — Sunset Lake, Mascotte", "https://lake.wateratlas.usf.edu/waterbodies/lakes/8235/sunset-lake-in-mascotte")
LAKE_LINDA_SRC = ("Lake.WaterAtlas.org — Lake Linda, Mascotte", "https://lake.wateratlas.usf.edu/waterbodies/lakes/8228/lake-in-mascotte-linda")
SUNSET_LAKES_ESTATES_SRC = ("GrowthSpotter — Sunset Lakes Estates, Mascotte", "https://growthspotter.com/news/lake-county-developments/gs-news-residential-mascotte-lake-county-single-family-homes-20211110-l4lc33enufghvdtjuwo7ytpbfa-story.html")
WOODBURY_SRC = ("NewHomeSource — Woodbury, Mascotte, FL (Park Square Homes)", "https://www.newhomesource.com/communities/fl/orlando-area/mascotte")
PALATLAKAHA_SRC = ("USGS Water Data for the Nation — Palatlakaha River near Mascotte, FL", "https://waterdata.usgs.gov/monitoring-location/USGS-02237000/")

SRC = [MASCOTTE_BUILDING, MASCOTTE_PORTAL, MASCOTTE_WATER, SJRWMD_MASCOTTE, SJRWMD_RESTRICT, IMMOKALEE_OSD, MYAKKA_OSD,
       SJRWMD_SOILMAP, MASCOTTE_POP, MASCOTTE_POP_RANK, SUNSET_LAKE_SRC, LAKE_LINDA_SRC, SUNSET_LAKES_ESTATES_SRC, WOODBURY_SRC,
       PALATLAKAHA_SRC, "dep-rule", "fs125572", "fs7203045"]

MI = CITIES[SLUG]["miles"]

# ============================================================== hub
HUB = page(
    "/areas/mascotte/", "city",
    "Artificial Turf Installation in Mascotte, FL (2026)",
    "Synthetic turf for Mascotte's flatwoods lots, new starter-home subdivisions and lakefront yards. Permits, water rules and pricing, checked September 2026.",
    "Synthetic turf for a small, fast-growing Lake County city",
    capsule(f"Mascotte has grown faster than 96 percent of similarly sized U.S. cities since 2000, and most of that growth shows up as new subdivisions on flat, low-lying ground rather than the ridge terrain just up the road toward Groveland. Installed synthetic turf here prices at {price('residential')} a square foot, matching the Central Florida figure for September 2026."),
    "".join([
        sec("A small city building fast on flat ground",
            "<p>Mascotte's population went from 5,101 at the 2010 census to 6,609 in 2020, and estimates put it near 8,536 by 2024, a pace few Lake County towns can match. Unlike Groveland a few miles east, Mascotte sits mostly on level ground rather than the sand ridge, closer to the flatwoods soil that dominates Osceola County than to the excessively drained hills near Clermont.</p>"
            + "<p>That growth is landing as named subdivisions rather than infill on existing streets. Stanley Martin Homes won city approval for a 134-lot community at Mascotte Empire Road and Pearl Street, and Park Square Homes has built out a 78-lot community of three- and four-bedroom houses between roughly 1,300 and 1,900 sq ft. Both sit alongside older SR 50 corridor lots and rural acreage still running on wells and septic systems, so a crew can work three very different lot types in the same afternoon.</p>"),
        table("Types of lots in Mascotte and what we build differently",
              ["Type of lot", "What changes for the build"],
              [["New subdivisions (Sunset Lakes Estates, Woodbury)", "Base still meets the state's washed-rock spec regardless of how recently a builder graded the lot"],
               ["Rural acreage on well and septic", "Septic tank pump-out access gets mapped and kept clear before any base goes in"],
               ["In-town lots near Sunset Lake or Lake Linda", "10-ft waterbody setback from the shoreline, plus the littoral-zone exclusion near the park's edge"],
               ["Older homes along the SR 50 corridor", "Base is built to drain where the native flatwoods sand does not, rather than to hold shape on ridge sand"]],
              "Checked against the city's own site and USDA/SJRWMD soil references, September 2026."),
        sec("Permits: a contracted building official, not an in-house office",
            f"<p>Mascotte doesn't run permitting in-house the way Groveland does a few miles east. The city contracts its building official work to Willdan Engineering, and applications route through the same general line, 352-557-8888, or the city's {ext('https://mascottefl.portal.iworq.net', 'online iworq portal')}. As of September 2026 we found nothing published naming synthetic turf specifically in Mascotte's code, so a phone call before scheduling a crew settles what a search of the code can't.</p>"
            + f"<p>Since Mascotte is its own permitting jurisdiction rather than unincorporated territory, {a('/laws/permits/lake-county/', 'the Lake County turf permit page we maintain')} is background reading, not the office that actually reviews a Mascotte address. {a('/laws/florida-hb-683/', 'the statewide May 2026 turf rule')} still sets the floor here regardless of which office holds the file: capped irrigation heads, a washed-rock subgrade, and turf kept out of any swale or wetland buffer.</p>"),
        sec("Water: the same district as Groveland, a different set of lakes",
            f"<p>Mascotte's own {ext('https://www.cityofmascotte.com/182/Water-Division', 'Water Division page')} lists the St. Johns River Water Management District among its resources, and the city has taken district money for infrastructure before: a {ext('https://www.sjrwmd.com/2018/09/district-partners-with-mascotte-for-water-main-replacement-project/', '2018 cost-share grant')} put $500,000 toward replacing roughly 2.5 miles of aging water main. That puts Mascotte's utility on the same side of the line as Groveland's, even though several of the town's small lakes drain toward the Withlacoochee River system that the Southwest Florida district manages instead.</p>"
            + f"<p>Under the St. Johns district's current shortage order, odd addresses may water Saturday only and even addresses Sunday only, with irrigation barred outright between 8 a.m. and 6 p.m. None of that matters once a synthetic lawn's heads are capped, which {a('/laws/florida-hb-683/', 'the state turf rule')} already requires everywhere in Florida.</p>"),
        sec("About as far from Kissimmee as we go",
            f"<p>Mascotte sits roughly {MI} miles from downtown Kissimmee by straight line, at the outer edge of the roughly 40-mile radius we cover. A job here typically rides along with other {a('/areas/lake-county/', 'Lake County')} stops rather than getting its own trip, often the same day as a visit to {city('groveland')} or {city('clermont')} a few miles closer in.</p>"),
        "<!--AUTO:city-services-->",
    ]),
    faqs=[
        faq("What should you ask before hiring the best artificial turf company near me in Mascotte?",
            "Ask whether the crew has worked flatwoods soil rather than the ridge sand a few miles away, since Mascotte's ground holds water closer to the surface than Groveland's does and calls for a different base plan. Beyond that, the same checklist applies anywhere: measured square footage, named base depth, and infill type spelled out in writing."),
        faq("Who handles building permits in Mascotte if the city has no in-house building official?",
            "Willdan Engineering, under contract to the city. Applications and questions still go through the city's general line or its online iworq portal; the review just happens through a contracted firm rather than city staff sitting in the building itself."),
        faq("Does Mascotte answer to the same water management district as Groveland?",
            "Its Water Division page points to the same St. Johns River Water Management District that Groveland answers to, and the city has accepted St. Johns grant money for water-main work before. Several of Mascotte's own small lakes drain toward the Withlacoochee system instead, which the Southwest Florida district manages, so the two roles don't fully overlap."),
        faq("Is the soil under a Mascotte yard the same as Groveland's ridge sand?",
            "No. Mascotte sits mainly on level, low-lying ground closer to the Immokalee and Myakka flatwoods family that Lake County's own general soil map places away from the ridge, soil that holds water nearer the surface than the excessively drained Candler and Astatula sands a few miles toward Groveland and Clermont."),
        faq("How close to Sunset Lake can a yard be turfed?",
            "The state's rule holds synthetic turf back at least 10 feet from the shoreline unless a seawall or bulkhead already separates the yard from the water, and it excludes any littoral shelf outright. That applies to a Sunset Lake lot the same way it would on any other Florida lake."),
    ],
    sources=SRC, city=SLUG,
    crumbs=[("Service areas", "/areas/")], crumb="Mascotte",
    related=[("/areas/lake-county/", "Artificial turf across Lake County"),
             ("/laws/permits/lake-county/", "Lake County turf permit rules"),
             ("/areas/groveland/", "Artificial turf in Groveland"),
             ("/areas/polk-city/", "Artificial turf in Polk City"),
             ("/artificial-turf-cost/", "Full turf cost guide")])

# ============================================================== local
LOCAL = {
    "residential": {
        "title": "Artificial Grass Installation in Mascotte, FL",
        "meta": "Artificial grass for Mascotte's new subdivisions, rural acreage and flatwoods lots. Base method, permits and pricing, checked September 2026.",
        "h1": "Lawn conversions for Mascotte's flat, fast-growing lots",
        "lede": capsule(f"Much of the current demand for artificial grass in Mascotte traces back to the city's new subdivisions, built on level flatwoods ground that behaves nothing like the sand ridge a few miles toward Groveland and Clermont. Installed pricing here matches the rest of Central Florida at {price('residential')} a square foot, September 2026's figure."),
        "sections": [
            ("Flatwoods ground instead of ridge sand",
             f"<p>Lake County's own general soil map groups the low ground around Mascotte with the Myakka and Immokalee flatwoods family rather than the excessively drained Candler and Astatula sands that dominate the ridge toward {city('groveland')} and {city('clermont')}. Both series carry a shallow, seasonally high water table, closer to a couple of feet down than the 80-plus inches the ridge soils allow, since flatwoods ground was never as well drained to begin with.</p>"
             "<p>A base built on ground like that is doing familiar work for anyone who has installed turf around Kissimmee: the washed, open-graded rock the state's rule requires has to lift the lawn clear of water sitting closer to the surface, not just hold a stable shape the way it would on drier, sandier ground. Grading the subgrade to shed water toward a natural low point matters more here than it would a few miles west.</p>")],
        "scenario": ("A worked example: a new Woodbury backyard",
                     f"<p>Say you have a 1,000 sq ft backyard at a newly built Woodbury or Sunset Lakes Estates home, graded flat by the builder and currently bare dirt waiting on a lawn. At Mascotte's {price('residential')} range, that yard prices between $8,000 and $18,000 depending on base depth and how much correction the builder's grading needs; most jobs this size land closer to $10,000–$16,000 at the typical grade.</p>"
                     "<p>New-construction fill compacted by heavy equipment during the build often drains worse than the undisturbed flatwoods sand around it, so a crew checks how the lot sheds water before setting base depth rather than assuming a brand-new lot is the easiest kind to build on. Sod removal usually isn't a factor on a lot this new; capping any stub-out for a future irrigation zone is.</p>"),
        "faqs": [
            faq("Does a brand-new Mascotte subdivision lot need a different base than an older one?",
                "Often a deeper one, not a different method. Construction traffic can compact fill on a new lot tighter than the undisturbed sand around it, which drains worse than it looks, so a crew checks the lot's actual drainage rather than assuming new construction is the simple case."),
            faq("Is rural acreage outside Mascotte's subdivisions harder to turf?",
                "Not harder, just different. A well-and-septic lot needs the tank's pump-out access mapped before base work starts, and a larger property often means more square footage and more grading rather than a more complicated build."),
        ],
        "sources": SRC,
    },
    "pet": {
        "title": "Pet Turf & Dog Runs in Mascotte, FL",
        "meta": "Dog runs and pet turf for Mascotte's rural septic lots, starter-home yards and Sunset Lake frontage. Setbacks and pricing, checked September 2026.",
        "h1": "Dog runs built for Mascotte's septic lots and small yards",
        "lede": capsule(f"A dog run in Mascotte is as likely to sit on a well-and-septic acreage lot as it is in a starter-home side yard barely wide enough for a wheelbarrow, and each layout answers to a different rule first. Pet turf here installs at {price('pet')} a square foot, September 2026's Central Florida figure."),
        "sections": [
            ("Dog runs sharing ground with a septic system",
             "<p>Rural lots around Mascotte still run heavily on private wells and septic systems, and a dog run staked out near the drain field has to leave the tank's pump-out lid reachable once the work is finished, the same requirement the state's turf rule sets for a full lawn. Mapping that lid before any rock goes down avoids a base built up over ground a pump-out truck needs to reach years later.</p>"
             f"<p>{post('how-to-get-dog-urine-smell-out-of-artificial-turf', 'This post')} covers why a pet run skips the weed barrier other turf projects sometimes use, letting rinse water and urine pass straight into the rock below instead of pooling on a fabric layer near a septic system's drain field.</p>"),
            ("Narrow side yards in Woodbury-sized starter homes",
             f"<p>A starter home in the 1,300 to 1,900 sq ft range common in Mascotte's newer subdivisions often leaves only a narrow strip between the house and the fence line, barely enough for a wheelbarrow, let alone a skid steer. A dog run in that space usually goes in by hand cart, which adds labor time on a small job that a wider ridge lot toward {city('groveland')} or {city('polk-city')} wouldn't need.</p>"
             "<p>That narrow footprint also limits how a run can be graded: with one fall line instead of several options, the crew routes drainage toward whichever end of the yard already sits lowest rather than reshaping the whole strip.</p>"),
            ("Runs near Sunset Lake's shoreline",
             f"<p>A lot backing onto {ext('https://lake.wateratlas.usf.edu/waterbodies/lakes/8235/sunset-lake-in-mascotte', 'Sunset Lake')} has to keep any turfed dog run at least 10 feet from the shoreline, the same setback a full lawn would need, unless a seawall or bulkhead already stands between the yard and the water. The park's public shoreline nearby is a reminder of how visible a lakefront yard is here, which is also where Florida's HOA-visibility rule matters least since there's often no fence to hide behind.</p>"
             "<p>Where a fence does exist between a dog run and the water, keeping the run itself outside the setback line still comes first in the layout, before deciding how much of the run infill needs for odor control.</p>")],
        "scenario": ("A worked example: a rural well-and-septic run",
                     f"<p>Say you have a 250 sq ft dog run planned for a rural Mascotte acreage lot, positioned well clear of the drain field but still within reach of an outdoor spigot for rinsing. At {price('pet')} per square foot, that run prices between roughly $2,500 and $4,500, with most landing near $3,000 to $4,000 once a coated antimicrobial infill is added for odor control.</p>"
                     "<p>Because the property sits on flatwoods soil rather than ridge sand, the base gets built toward the fuller end of the state's two-to-four-inch range so the run stays above a water table that can rise closer to the surface after a wet-season storm. The weed barrier gets skipped the way it would on any pet project, letting the rock underneath carry rinse water away instead of trapping it.</p>"),
        "faqs": [
            faq("Can a dog run sit next to a septic drain field in Mascotte?",
                "It can sit nearby, but not over the tank's pump-out access, which has to stay reachable once the run is finished. Mapping the septic system's layout before any base work starts is a standard step on rural Mascotte lots."),
            faq("Does a narrow Woodbury-style side yard cost more to turf as a dog run?",
                "Sometimes, since equipment often has to come through by hand cart rather than a skid steer, which adds labor time on a small area. The turf, base and infill specs stay the same as a wider yard; only the access changes."),
        ],
        "sources": SRC,
    },
    "putting": {
        "title": "Backyard Putting Greens in Mascotte, FL",
        "meta": "Backyard putting greens built on Mascotte's flat lots and rural acreage. Contouring, drainage and pricing for Lake County, checked September 2026.",
        "h1": "Putting greens shaped from Mascotte's flat ground",
        "lede": capsule(f"Unlike the naturally rolling ridge lots toward Groveland, most Mascotte yards start dead level, which puts more of a green's contour on the crew's shaping plan than on ground that already leans one way. A backyard green here prices at {price('putting')} a square foot, September 2026's Central Florida figure."),
        "sections": [
            ("Building contour where the ground starts flat",
             f"<p>A putting green needs rolls, tiers and a slightly raised collar around each cup to read as real turf rather than a tabletop, and on Mascotte's flatwoods lots almost all of that shape has to be built rather than borrowed from the site. That's the reverse of a ridge lot near {city('groveland')} or {city('minneola')}, where some grade change already exists before a shovel goes in.</p>"
             "<p>Shaping a green from flat, moisture-holding ground also means the subbase has to manage drainage while it's being contoured, not just after: a cup set at the bottom of a roll on flatwoods soil can hold water if the crew doesn't grade a path for it to escape underneath the surface.</p>"),
            ("Room to build bigger on rural acreage",
             f"<p>A well-and-septic lot outside Mascotte's subdivisions often carries more open ground than a platted starter-home yard, which gives a green more room for a longer roll or a second cup without crowding a fence line. {svc('putting', 'A larger green')} on acreage like this still needs the septic tank's pump-out access mapped and kept clear of the build, the same as any other project on a lot with a private system.</p>"
             "<p>More space doesn't mean less shaping work; a bigger green on flat ground still needs the same engineered subbase as a small one, just across more square footage.</p>"),
            ("Compact greens for Woodbury-sized backyards",
             "<p>A starter-home backyard in the 1,300 to 1,900 sq ft house range common in Mascotte's newer subdivisions leaves a modest footprint once a patio and any shed are subtracted, which usually means a single-cup green with a short fringe rather than a multi-hole layout. Fitting real practice into that space matters more than length, so the fringe and approach cut often take up as much of the design as the putting surface itself.</p>"
             f"<p>{post('artificial-turf-glossary', 'This glossary')} explains stimp, fringe and the other terms that come up once a small green's actual layout gets discussed with a homeowner.</p>")],
        "scenario": ("A worked example: a green on a starter-home lot",
                     f"<p>Say you have a 350 sq ft area at the back of a Woodbury-style starter home, flat and freshly sodded by the builder before anyone asked about a green. At Mascotte's {price('putting')} range, a single-cup green with fringe prices between about $4,900 and $10,500, with most builds landing near $6,300 to $8,750 once cup hardware and a compact chipping pad are added.</p>"
                     "<p>Because the lot starts level, the subbase takes more shaping time per square foot than it would on a naturally rolling ridge lot, building rolls and a raised collar from scratch rather than following ground that already leans somewhere. Grading still has to send water off the green rather than trap it in a low cup, which on flatwoods soil is worth checking twice before the turf goes down.</p>"),
        "faqs": [
            faq("Is it harder to build a putting green on flat Mascotte ground than a Groveland ridge lot?",
                "Not harder, just different work. A flat lot needs the crew to build contour into the subbase from scratch, while a ridge lot starts with some grade already there; both still need an engineered, compacted subbase rather than turf laid straight over native soil."),
            faq("Can a putting green go on a rural acreage lot with a septic system in Mascotte?",
                "Yes, as long as the septic tank's pump-out access stays clear of the build and is mapped before shaping starts. Acreage lots often have more room for a longer green than a platted subdivision yard would allow."),
            faq("How big a putting green fits in a Woodbury-style backyard?",
                "Most fit a single cup with a short fringe and approach cut rather than a multi-hole layout, since the yard itself usually runs a few hundred square feet once a patio is subtracted. A compact design still gives a real short-game practice area within that space."),
        ],
        "sources": SRC,
    },
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
