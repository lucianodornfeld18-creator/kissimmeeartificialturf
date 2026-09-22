# -*- coding: utf-8 -*-
"""Oviedo, FL (tier 2, Seminole County). Researched September 2026: City of Oviedo Building Services,
water and reclaimed-water pages; Oviedo's Land Development Code Section 15.7 (Econlockhatchee River
Protection Overlay) and reporting on its 2023 update; Black Hammock and Alafaya Woods; Census population;
USDA flatwoods soils already verified for Seminole County in c_counties.py / c_permits.py."""
from _helpers import page, capsule, sec, table, faq, a, svc, city, county, src, ext, price, post
from _cityservice import cityservice_pages

SLUG = "oviedo"

BUILDING = ("City of Oviedo — Building Services", "https://www.cityofoviedo.net/151/Building-Services")
PORTAL = ("City of Oviedo — Online Building Permit Applications", "https://www.cityofoviedo.net/1072/Online-Building-Permit-Applications")
WATERCONS = ("City of Oviedo — Water Conservation", "https://www.cityofoviedo.net/605/Water-Conservation")
RECLAIMED = ("City of Oviedo — Reclaimed Water", "https://www.cityofoviedo.net/1208/Reclaimed-Water")
ECON_LDC = ("Oviedo Community News — proposed Land Development Code updates to the Econlockhatchee River Protection Overlay", "https://oviedocommunitynews.org/2023/10/25/major-oviedo-land-development-code-updates-may-be-on-the-way/")
ECON_COUNTY = ("Seminole County — Econlockhatchee River Basin Protection Ordinance, Conservation Element", "https://www.seminolecountyfl.gov/docs/default-source/pdf/Conservation_Element_20240529_SH.pdf")
BLACK_HAMMOCK = ("Neighborhoods.com — Black Hammock, Oviedo, FL", "https://www.neighborhoods.com/black-hammock-oviedo-fl")
ALAFAYA_WOODS = ("Alafaya Woods Homeowners Association — About Us", "https://alafayawoodshoa.com/about/")
CHICKENS_1 = ("Roadside America — Oviedo, FL: Downtown's Wild Chickens", "https://www.roadsideamerica.com/tip/11246")
CHICKENS_2 = ("ClickOrlando, March 31, 2025 — the mysterious disappearance of Oviedo's chickens", "https://www.clickorlando.com/news/local/2025/03/31/the-mysterious-disappearance-of-oviedos-chickens-what-really-happened/")
UCF_ALAFAYA = ("Wikipedia — Alafaya, Florida (population growth 2010-2020)", "https://en.wikipedia.org/wiki/Alafaya,_Florida")
OVIEDO_HISTORY = ("ClickOrlando, March 26, 2025 — from citrus to celery: how Oviedo became a farming hub", "https://www.clickorlando.com/news/local/2025/03/26/from-citrus-to-celery-how-oviedo-became-a-farming-hub/")
CENSUS_OVIEDO = ("U.S. Census Bureau QuickFacts — Oviedo city, Florida", "https://www.census.gov/quickfacts/fact/table/oviedocityflorida/PST045224")
CENTER_LAKE = ("City of Oviedo — Center Lake Park / Oviedo on the Park", "https://www.cityofoviedo.net/511/Oviedo-on-the-Park")
SJRWMD = ("St. Johns River Water Management District — watering restrictions", "https://www.sjrwmd.com/wateringrestrictions/")

SRC = [BUILDING, PORTAL, WATERCONS, RECLAIMED, ECON_LDC, ECON_COUNTY, BLACK_HAMMOCK, ALAFAYA_WOODS,
       CHICKENS_1, CHICKENS_2, UCF_ALAFAYA, OVIEDO_HISTORY, CENSUS_OVIEDO, CENTER_LAKE, SJRWMD, "usda-wss", "dep-rule", "fs125572", "fs7203045"]

PERMITS_SEM = ("/laws/permits/seminole-county/", "Seminole County permit rules for turf")
HB683 = ("/laws/florida-hb-683/", "HB 683 and DEP Rule 62-308.100")
HOA = ("/laws/hoa-rules/", "What a Florida HOA can and can't restrict")

# ============================================================== HUB
HUB = page(
    "/areas/oviedo/", "city",
    "Artificial Turf Installation in Oviedo, FL",
    "Synthetic turf installers covering Oviedo, FL: Building Services, the Econlockhatchee buffer, reclaimed-water rules and soil facts, checked September 2026.",
    "Artificial turf and synthetic grass in Oviedo, Florida",
    capsule(f"A synthetic lawn in Oviedo prices between {price('residential')} per square foot installed, holding to the same Central Florida range as of September 2026 on a fenced quarter-acre or a well-and-septic acreage lot alike. Oviedo answers permit questions through its own Building Services counter rather than Seminole County's, and its Econlockhatchee River corridor brings a wetland buffer most towns on this site never plan around."),
    "".join([
        sec("What's different about a turf job in Oviedo",
            f"<p>Oviedo sits about 29 miles from downtown Kissimmee and grew from a citrus settlement into the self-described Celery Capital of the World after an 1894-95 freeze pushed farmers toward the muck around Black Hammock ({ext(OVIEDO_HISTORY[1], 'ClickOrlando, 2025')}); more recently it has grown again on the strength of its shared border with the University of Central Florida. Housing spans 1980s and 1990s subdivisions with mature oak canopy, newer family neighborhoods on the eastern edge, and rural acreage on Lake Jesup's southeast shore.</p>"
            + f"<p>Two things separate Oviedo from most towns on this site: the city runs its own {ext(BUILDING[1], 'Building Services counter')} rather than sending permit questions to the county, and its code sets aside a protection zone along the Econlockhatchee River corridor most Central Florida cities never think about. Neither one changes the price.</p>"),
        table("Oviedo yard types and what we do differently",
              ["Neighborhood type", "Typical lot", "What changes for the turf plan"],
              [["1980s-90s HOA subdivisions (Alafaya Woods, Tuska Ridge)", "Quarter-acre, fenced, mature oaks", "Architectural review submittal; drip-line rule on most jobs"],
               ["Black Hammock rural acreage", "One acre or more, well and septic", "No HOA review; septic pump-out lid stays clear of the base"],
               ["Newer eastern subdivisions (Live Oak Reserve and similar)", "Wider lots, younger canopy", "Fewer tree conflicts; room for a full lawn or a green"],
               ["Lots inside the Econlockhatchee corridor", "Larger, often adjoining conservation land", "State's 10-ft waterbody setback applies at the water's edge"]],
              "Lot type changes the plan, not the price; a quote runs the same Central Florida range regardless of the row above."),
        sec("Does Oviedo require a permit for synthetic turf?",
            f"<p>Oviedo's Land Development Code doesn't name synthetic or artificial turf anywhere we could find, and the city has never posted a stated yes-or-no on a residential lawn swap, as of September 2026. That silence isn't a green light: an irrigation head under the new turf still has to be capped, a step {a(HB683[0], HB683[1])} requires outright. {ext(BUILDING[1], 'Oviedo Building Services')} takes questions at 407-971-5755 from 320 Alexandria Boulevard, with applications through the city's online Click2Gov portal rather than a paper counter.</p>"
            + f"<p>Because Oviedo is its own permitting authority, {county('seminole', 'Seminole County')}'s building department only covers the unincorporated pockets outside the city line, and we don't have a page written for Oviedo's own code the way we do for {a(PERMITS_SEM[0], 'the county')}. An unincorporated address reads that county page instead. {a(HOA[0], HOA[1])} is a separate question; an HOA approval never substitutes for a city permit.</p>"),
        sec("Water, reclaimed irrigation and the Econlockhatchee corridor",
            f"<p>Oviedo runs its own water utility rather than buying through Toho or the county, and offers reclaimed water to a large share of the city: potable customers water one day a week in cooler months and two in summer; reclaimed customers can run three days a week year-round, though the city recommends holding it to two, with no watering 10 a.m.-4 p.m. either way ({ext(WATERCONS[1], 'Oviedo Water Conservation')}; {ext(RECLAIMED[1], 'Oviedo Reclaimed Water')}). Like the rest of {county('seminole')}, Oviedo falls under the St. Johns River Water Management District, tightened through a 2026 shortage order ({ext(SJRWMD[1], 'SJRWMD watering restrictions')}). A converted lawn stops answering to any of it the moment its old heads are capped, a step {src('dep-rule', 'the state standard')} requires outright.</p>"
            + f"<p>The city's east side carries a second, less common rule: Oviedo's zoning code sets aside an Econlockhatchee River Protection Overlay along the river corridor, and Seminole County keeps a parallel ordinance for the same stretch. Local reporting on a 2023 proposal described a 25-foot minimum, 50-foot average wetland buffer and a cap of one dwelling per 10 acres inside the zone ({ext(ECON_LDC[1], 'Oviedo Community News')}); we couldn't confirm whether it was formally adopted, so treat the figures as reported, not current code. Either way, that's a density rule for the corridor, not a turf-specific setback, so it isn't what {src('fs125572', 'the state law')} caps at whatever natural grass gets; a lot fronting the river still answers to the state's own 10-foot line.</p>"),
        sec("Black Hammock, Alafaya Woods and how Oviedo grew",
            f"<p>Black Hammock, the rural pocket on Lake Jesup's southeast shore, is the clearest contrast to the rest of the city: roughly 1,641 residents on parcels that mostly run well and septic, with houses built mostly between 1972 and 2005 ({ext(BLACK_HAMMOCK[1], 'Black Hammock, Oviedo, FL')}), where a turf job plans around septic access rather than an HOA submittal. Alafaya Woods is the opposite case: a covenant-controlled subdivision from the late 1980s and early 1990s with sidewalk-lined streets and mature oak trees, run by its own elected board ({ext(ALAFAYA_WOODS[1], 'Alafaya Woods HOA')}); Tuska Ridge and Live Oak Reserve sit nearby with a similar pattern, built a little later.</p>"
            + f"<p>Downtown carries its own local color: wild chickens roamed the historic core for more than 40 years, tracing back to a single bird near a Geneva Drive surveying office in the mid-1990s, though the flock has thinned since nuisance complaints ({ext(CHICKENS_1[1], 'Roadside America')}; {ext(CHICKENS_2[1], 'ClickOrlando, 2025')}). The bigger growth story is UCF, whose shared border and research park have pulled new subdivisions onto Oviedo's eastern edge, pushing the population to an estimated 40,599 as of 2024 ({ext(CENSUS_OVIEDO[1], 'Census QuickFacts')}).</p>"),
        sec("What's under an Oviedo lawn",
            f"<p>Oviedo sits in the same flatwoods belt as the rest of {county('seminole', 'Seminole County')}, where the Myakka, Basinger, Immokalee and Smyrna series keep the ground damp to within a couple of feet of grade for weeks after a hard summer rain ({src('usda-wss', 'USDA Web Soil Survey')}). That's why the standard build leans on washed, open-graded crushed rock rather than anything with fines, and why a lot backing the Black Hammock wetlands or the Econlockhatchee corridor gets graded with extra care for where the water goes.</p>"),
        "<!--AUTO:city-services-->",
    ]),
    faqs=[
        faq("What should an Oviedo homeowner ask before picking the best turf company for the job?",
            "Start with whether the crew knows Oviedo answers its own permit questions instead of routing them through the county. From there: base depth and material in writing, infill type and rate spelled out, and a straight answer about the Econlockhatchee buffer if the lot sits anywhere near that corridor."),
        faq("Does Oviedo's Econlockhatchee buffer mean turf can't go near the river at all?",
            "Not necessarily. The buffer we found reported limits how densely a parcel inside the zone can be developed, a broader rule than a turf-specific setback. A lot that actually fronts the river still clears the state's 10-foot waterbody setback separately, and a site visit is the only way to place that line precisely."),
        faq("Is Black Hammock too rural for a scheduled turf install?",
            "No, though the job looks different there. Without an HOA to submit plans to, the main step is locating the septic tank's pump-out lid before the crew starts, since state rule keeps that access clear, and confirming whether the address sits inside Oviedo's city limits or the unincorporated county next door."),
        faq("Do Alafaya Woods, Tuska Ridge or Live Oak Reserve have a published rule on artificial turf?",
            "We didn't find one specific to synthetic turf in what Alafaya Woods publishes, and didn't locate published design documents for Tuska Ridge or Live Oak Reserve at all. Treat any of the three as a standard architectural-review submittal, and bring a product spec sheet and a site plan to that conversation."),
    ],
    sources=SRC, city=SLUG, crumbs=[("Service areas", "/areas/")], crumb="Oviedo",
    related=[("/areas/seminole-county/", "Turf across Seminole County"), PERMITS_SEM,
             ("/areas/winter-springs/", "Turf in Winter Springs"), ("/areas/casselberry/", "Turf in Casselberry"),
             ("/artificial-turf-cost/", "Turf cost tables for Central Florida")])

# ============================================================== LOCAL
LOCAL = {
    "residential": {
        "title": "Artificial Grass Installation in Oviedo, FL – Yards & HOAs",
        "meta": "Synthetic lawn installation in Oviedo, FL: Building Services permits, Alafaya Woods-style HOA review and flatwoods soil, checked September 2026.",
        "h1": "Synthetic lawns for Oviedo yards, from downtown to the county line",
        "lede": capsule(f"A residential synthetic lawn in Oviedo runs {price('residential')} per square foot installed, typically {price('residential', True)}, as of September 2026. Oviedo reviews its own permits rather than routing them to Seminole County, and a fenced backyard in a covenant-controlled subdivision like Alafaya Woods still goes through an architectural review before the crew shows up."),
        "sections": [
            ("Who reviews the permit for a lawn conversion in Oviedo",
             f"<p>Oviedo runs its own Building Services division rather than sending residential permit questions to Seminole County, so a call to {ext(BUILDING[1], '407-971-5755')} is the first step for anything the state rule doesn't already settle. We didn't find a Land Development Code section that names synthetic turf specifically, which means the office weighs a lawn swap against its ordinary rules for exterior work and drainage rather than a dedicated turf ordinance. Applications go through the city's online Click2Gov portal, not a paper counter, so an installer who already has the property's parcel details on hand moves faster through that step.</p>"
             + f"<p>Because Oviedo has no page of its own on this site yet, an address that turns out to sit in unincorporated Seminole County instead uses {a(PERMITS_SEM[0], PERMITS_SEM[1])} rather than anything written for the city. Sorting that out before scheduling saves a callback later.</p>"),
            ("What an Alafaya Woods or Tuska Ridge review actually asks for",
             f"<p>A covenant-controlled subdivision from the late 1980s or early 1990s, the era that produced Alafaya Woods and its sidewalk-lined streets, runs its own architectural review separate from the city permit, and we didn't find a published clause naming turf, sod or ground cover on the association's own site. That means an application goes in as a general exterior-change request: a product sample, a spec sheet and a simple site plan showing where the lawn goes, the same packet {a(HOA[0], 'Florida law')} lets an association review as long as the yard is visible from the street or a neighbor's lot.</p>"
             + "<p>The mature oak canopy that gives these streets their shade is the other thing a plan has to answer to, since the state's drip-line rule keeps turf out from under a live oak's canopy on either side of a property line unless a certified arborist signs off first.</p>"),
            ("Building above Oviedo's flatwoods water table",
             f"<p>Most of Oviedo shares the flatwoods sand common across {county('seminole', 'Seminole County')}, including the Myakka and Basinger series, ground where a heavy wet season leaves the water table sitting close enough to grade to matter for months at a stretch ({src('usda-wss', 'USDA')}). A base built at the shallow end of the state's allowed range barely clears that saturation zone on a lot that already drains slowly, which is why a crew leans toward the fuller two-to-four-inch depth of washed crushed rock on any Oviedo yard where standing water already shows up after a storm, rather than assuming every lot behaves the same.</p>"),
        ],
        "scenario": ("What an 850 sq ft Alafaya Woods backyard runs",
                     f"<p>Say a 1988-built home in Alafaya Woods has an 850 sq ft fenced backyard behind a low privacy fence, with a live oak in one corner and a run of St. Augustine that never fully recovered from a dry spring. At the published {price('residential', True)} typical range, a straightforward rectangle of that size prices between $8,500 and $13,600 once the association has signed off on the sample and the site plan. The oak takes some of that budget: keeping excavation shallow inside its drip line, instead of digging the full base depth, adds a step the association review won't ask about but the state rule requires regardless.</p>"
                     + "<p>Because the association's own documents don't name turf directly, the packet that goes in reads like any other exterior-change request rather than a pre-approved category, which is normal for a subdivision this age and not a sign the request will run into trouble.</p>"),
        "faqs": [
            faq("Does Oviedo's Building Services office check for HOA approval before issuing a permit?",
                "No. The city's review and an association's architectural approval are separate steps, and a Building Services permit doesn't confirm or replace an HOA sign-off in a community like Alafaya Woods or Tuska Ridge."),
            faq("Is there a faster path for a lot outside any HOA, like in Black Hammock?",
                "The city or county permit step is the same either way; what changes without an HOA is skipping the architectural-review packet entirely, since there's no association to submit it to."),
        ],
        "sources": SRC,
    },
    "pet": {
        "title": "Pet Turf Installation in Oviedo, FL – Dog Runs",
        "meta": "Pet-friendly synthetic turf in Oviedo, FL: Black Hammock acreage, HOA fence rules and drainage for the county's flatwoods soil, checked September 2026.",
        "h1": "Dog-run turf for Oviedo's acreage lots and fenced subdivisions",
        "lede": capsule(f"Pet turf in Oviedo runs {price('pet')} per square foot installed, typically {price('pet', True)}, as of September 2026. A well-and-septic property out in Black Hammock and a fenced quarter-acre in Alafaya Woods need the same infill and drainage decisions, just without the same paperwork in front of them."),
        "sections": [
            ("Dog runs on Black Hammock's well-and-septic lots",
             f"<p>Black Hammock's roughly 1,641 residents mostly run their own wells and septic systems rather than city water and sewer, on parcels built out mostly between 1972 and 2005 ({ext(BLACK_HAMMOCK[1], 'Black Hammock, Oviedo, FL')}). A dog run out there plans around the septic tank first: the state's turf rule requires the pump-out lid stay reachable once the lawn is finished, so a crew maps that spot before laying any base, then builds the run's boundary and infill zone around it rather than over it. No HOA reviews any of it, which is the trade-off for a system that also needs its own maintenance schedule the city's utility customers don't think about.</p>"),
            ("What Alafaya Woods' fence line means for a visible dog run",
             f"<p>Florida law lets an association restrict artificial turf only where it's visible from the street or an adjacent lot, so a dog run tucked behind Alafaya Woods' typical privacy fencing sits outside what the HOA can weigh in on at all, even without a documented turf clause to point to. A run that wraps around a side yard toward the street is the exception, since that stretch is visible the way a front lawn is, and it's the part of the layout worth confirming with the association before ordering material.</p>"),
            ("Odor control in ground that already holds water",
             f"<p>Oviedo's flatwoods sand holds moisture near the surface for weeks after a heavy summer, which changes how zeolite and other odor-control infills behave compared with a fast-draining ridge lot elsewhere in Central Florida. A dog run here still gets a deeper, more open base than a plain lawn calls for, since urine has to clear the infill and the rock beneath it quickly rather than sitting against ground that's already close to saturated. Skipping the weed barrier under a pet area, standard practice regardless of soil type, matters even more on ground this wet, since fabric there would trap liquid right at the surface instead of letting it pass through.</p>"),
        ],
        "scenario": ("Sizing a run for a Black Hammock acre lot",
                     f"<p>Say a Black Hammock property on well and septic has two dogs and wants a 400 sq ft run along the side of the house, away from the septic field and clear of a large oak's canopy. At the typical {price('pet', True)} range, that prices between $4,800 and $6,400, including a zeolite infill zone sized for two dogs rather than the lighter rate a single-dog yard would need. Because the lot has no HOA, the only approval step before the crew starts is confirming the septic tank's exact pump-out location with the property's own records or a service call, not an architectural-review packet.</p>"
                     + "<p>A similarly sized run in Alafaya Woods would add one more step: a quick submittal showing the run sits behind the property's fence line, which the association can review as an ordinary exterior request even without a rule written for turf by name.</p>"),
        "faqs": [
            faq("Do Black Hammock properties need county or city approval for a dog run?",
                "That depends on which side of the line a specific parcel sits on. Some Black Hammock addresses are inside Oviedo, others are unincorporated Seminole County, so a parcel search settles which office to call before scheduling."),
            faq("Does a dog run near a Black Hammock wetland trigger the state's water setback?",
                "It can, if the run sits within 10 feet of a pond, canal or the lake shoreline itself. A site visit is the only reliable way to confirm the distance on a specific rural lot."),
        ],
        "sources": SRC,
    },
    "putting": {
        "title": "Backyard Putting Greens in Oviedo, FL",
        "meta": "Backyard putting greens in Oviedo, FL: room on newer eastern lots, the Econlockhatchee buffer and flatwoods drainage, checked September 2026.",
        "h1": "Putting greens for Oviedo's wider eastern lots",
        "lede": capsule(f"A backyard putting green in Oviedo runs {price('putting')} per square foot installed, typically {price('putting', True)}, as of September 2026. The city's newer subdivisions on the UCF-facing eastern edge tend to have the flattest, widest lots on this list, which is exactly the shape a green's contouring needs before cups or fringe turf come into it."),
        "sections": [
            ("Why flat ground still needs a shaped base",
             "<p>A putting green doesn't need slope, but it does need a base built to move water somewhere specific, since a flat Oviedo lot with no natural fall can hold a puddle just as easily as a sloped one sheds it. The crew grades the compacted rock to a slight, deliberate pitch toward one edge of the green rather than leaving it dead level, then builds the contours homeowners actually want, a rolling two-foot break toward the cup, for example, on top of that drainage plan rather than instead of it. Skipping that step is the difference between a green that plays true after a storm and one that holds a film of water on the low side for a day.</p>"),
            ("Room to build on Oviedo's newer eastern lots",
             f"<p>Subdivisions built on Oviedo's UCF-facing eastern side over the past two decades tend to run wider and shallower than the oak-shaded quarter-acre lots closer to downtown, since {ext(UCF_ALAFAYA[1], 'growth tied to the university and the Central Florida Research Park')} filled in that land more recently and with less mature landscaping to work around. That extra width is what makes room for a full green with fringe and a chipping pad, rather than a compact putting surface squeezed against a fence line, and it usually means fewer live-oak drip lines to route the layout around.</p>"),
            ("Building a green near the Econlockhatchee corridor",
             f"<p>A larger parcel inside or near Oviedo's Econlockhatchee River Protection Overlay has room for a green that a standard subdivision lot doesn't, but the corridor's own development and density rules still apply to the property as a whole, separate from where the green itself can sit relative to the water. The state's 10-foot setback from a pond, canal or the river's edge is the number that actually limits how close a green can go to water on one of these lots, and confirming exactly where that line falls, ahead of ordering material, is worth a site visit rather than an estimate off a plat map.</p>"),
        ],
        "scenario": ("A 500 sq ft green on a Live Oak Reserve-style lot",
                     f"<p>Say a newer home on Oviedo's east side has a wide, flat 500 sq ft side yard, more room than an older subdivision closer to downtown typically offers, and wants a green with a contoured two-tier surface and a small chipping pad. At the typical {price('putting', True)} range, that prices between $9,000 and $12,500, with the upper end reflecting the extra grading work a two-tier design takes over a flat single-level green. Because the lot sits well outside any wetland or waterbody buffer, the layout isn't constrained the way a lakefront property near Black Hammock or the river corridor would be.</p>"
                     + "<p>A comparable green on an older, narrower Alafaya Woods lot would likely shrink to a single-level surface without the chipping pad, simply because there's less flat ground to work with once the fence lines and an oak's drip line are accounted for.</p>"),
        "faqs": [
            faq("Searching for the best putting-green installer near me in Oviedo? Here's what to ask first.",
                "Ask how the contractor plans drainage on a flat lot before discussing cup placement or fringe turf, since a green that looks right on install day but holds water after the first storm was graded wrong from the start. A crew that raises grading before design usually understands Oviedo's flatwoods ground already."),
            faq("Can a putting green go inside Oviedo's Econlockhatchee protection zone?",
                "Often yes, away from the water itself. The corridor's density and buffer rules govern how the property overall gets developed, not specifically where a green can sit, so the state's 10-foot waterbody setback is the number that actually constrains layout near the river or a connected pond."),
            faq("Do newer Oviedo subdivisions need less base depth because the lots are flatter?",
                "No. Base depth answers to the soil's drainage, not the lot's slope, and Oviedo's flatwoods sand holds water near the surface regardless of which part of the city a lot sits in."),
        ],
        "sources": SRC,
    },
    "playground": {
        "title": "Playground Turf Installation in Oviedo, FL",
        "meta": "Playground turf for Oviedo, FL backyards: swing-set infill rules, family subdivisions and drainage for flatwoods soil, checked September 2026.",
        "h1": "Play-area turf for Oviedo's family neighborhoods",
        "lede": capsule(f"Cushioned playground turf in Oviedo runs {price('playground')} per square foot installed, typically {price('playground', True)}, as of September 2026. Between the city's downtown parks and the newer family subdivisions filling in near UCF, a swing set or a playset in the backyard is a common enough request that the infill rule underneath it is worth knowing before ordering anything."),
        "sections": [
            ("Rubber infill stays under the equipment, nowhere else",
             "<p>Florida's turf standard limits rubber and other synthetic infill to the footprint of playground equipment itself, so a family adding a swing set or a small climbing structure to an Oviedo backyard gets one infill type directly under the frame and a different one, silica, zeolite or coated sand, across the rest of the play lawn. The dividing line usually follows the equipment's required fall zone rather than a fence or a flower bed, and a contractor should be able to point to exactly where that line falls on a specific layout before installation starts, not after.</p>"),
            ("Families near the city's parks still turf their own yards",
             f"<p>Oviedo's downtown investment in {ext(CENTER_LAKE[1], 'Center Lake Park')}, with its splash pad and playground, hasn't reduced demand for a home play area, since a public park a short drive away doesn't cover the daily use a backyard gets between visits. Families in the newer subdivisions on the city's eastern side, filled in as UCF-area growth pulled new construction toward Oviedo, tend to ask for a play area sized to a specific swing set or trampoline rather than a full lawn conversion, which keeps both the layout and the infill question smaller in scope.</p>"),
            ("Shock pad depth on ground that already holds water",
             "<p>A shock pad sized to the equipment's fall height sits on top of the same washed, open-graded rock base every Oviedo yard needs for drainage, but the pad itself adds a second layer of specification a plain lawn doesn't carry. On flatwoods soil that already holds a high water table for weeks after a summer storm, getting the base grade right underneath that pad matters more than it would on faster-draining ground, since a play area that puddles is both a maintenance headache and a slip risk in a way an ordinary lawn corner isn't.</p>"),
        ],
        "scenario": ("A 300 sq ft play area behind a Live Oak Reserve home",
                     f"<p>Say a family on Oviedo's east side has a swing set and a small trampoline taking up roughly 300 sq ft of a fenced backyard, on a lot without the mature oak canopy an older subdivision closer to downtown would have. At the typical {price('playground', True)} range, that prices between $3,600 and $5,700, with roughly a third of that area needing the shock pad and rubber infill under the swing set's fall zone and the rest getting standard silica or coated sand. Because the lot sits outside any HOA-mandated architectural review, the main planning step is confirming the equipment's exact footprint before the crew orders material.</p>"
                     + "<p>A similar play area behind an older Alafaya Woods home would likely need the layout shifted a few feet to clear a live oak's drip line, which changes where the pad sits without changing the total square footage much.</p>"),
        "faqs": [
            faq("Does a homeowner in an Oviedo HOA need approval before adding play-area turf?",
                "If the association is one like Alafaya Woods, a backyard play area visible only from inside the fence typically falls outside what an HOA can restrict under Florida law, though a play structure tall enough to be seen over the fence line is a separate conversation worth having with the board first."),
            faq("Can crumb rubber cover a whole Oviedo backyard play lawn?",
                "No. The state's material rule allows rubber and other synthetic infill only under the playground equipment's actual footprint, not across the rest of a play lawn, which uses silica, zeolite or coated sand instead."),
        ],
        "sources": SRC,
    },
    "pool": {
        "title": "Pool & Lanai Turf in Oviedo, FL",
        "meta": "Turf beside pools and inside screen enclosures in Oviedo, FL, built for the county's high water table, checked September 2026.",
        "h1": "Screened pool and lanai turf, built for Oviedo's yards",
        "lede": capsule(f"Pool and lanai turf in Oviedo prices toward the top of the {price('residential')} residential range as of September 2026, since a screen enclosure's small footprint and tight access cost more per foot than an open backyard. The 1980s and 1990s subdivisions that built most of Oviedo's screened pool cages sit on the same high water table as the rest of the city, which shapes the deck-edge drainage plan more than it changes the turf itself."),
        "sections": [
            ("Pool-cage subdivisions from Oviedo's HOA-era growth",
             "<p>The screen-enclosure pool lot common in Alafaya Woods, Tuska Ridge and similar subdivisions from the late 1980s and 1990s leaves a narrow strip of grass on one or two sides of the deck, usually shaded enough by the cage and neighboring fences that St. Augustine has already struggled there for years. Turf laid inside that enclosure runs against the deck's slab edge rather than a fence line, so the crew tapers the compacted rock to meet the slab's exact height along its whole length, not just wherever it's easiest to check.</p>"),
            ("Drainage underlay where the deck meets the base",
             "<p>A screen enclosure's slab drains toward a specific low point, usually a deck drain or the enclosure's outer edge, and turf tying into that slab needs its own drainage underlay so water shed off the concrete doesn't just pool against the new turf's edge instead. That underlay matters more on an Oviedo lot than it would somewhere with faster-draining sand, since the native soil beneath an older pool deck is already close to saturated for weeks at a time during a wet summer, leaving less capacity to absorb whatever the slab sheds.</p>"),
            ("Small strips, tighter access, higher per-foot cost",
             "<p>Most pool-lanai turf jobs in Oviedo's older subdivisions run under 600 sq ft total, split into two or three narrow strips rather than one open rectangle, and a crew working through a screen enclosure's door rather than a gate loses time a wide-open backyard job wouldn't. That combination of small area and awkward access is why pool and lanai turf prices toward the upper half of the residential range rather than the middle, the same pattern that shows up on tight side yards anywhere else in Central Florida.</p>"),
        ],
        "scenario": ("A 550 sq ft screen-enclosure strip near a 1991 pool home",
                     f"<p>Say a 1991-built home in one of Oviedo's established subdivisions has a pool inside a screen enclosure, with two narrow strips of struggling grass totaling 550 sq ft along the deck's edges. At the typical {price('residential', True)} range, that prices between $5,500 and $8,800, landing toward the upper end because the access runs through the enclosure's screen door rather than a side gate wide enough for equipment. The drainage underlay where the turf meets the pool deck's slab adds a line item a plain backyard lawn wouldn't carry, since that edge sheds water the rest of the yard's grading doesn't have to handle.</p>"
                     + "<p>Because the strips sit fully inside the fenced, screened enclosure, an HOA architectural review, if the subdivision has one, typically treats the request as invisible from the street rather than a submittal that needs a sample and a site plan.</p>"),
        "faqs": [
            faq("Does turf inside an Oviedo screen enclosure need the same base depth as an open lawn?",
                "Yes, the same washed, open-graded crushed rock at the same two-to-four-inch depth applies. What changes is the edge treatment where the base meets the pool deck, not the depth of the base itself."),
            faq("Can turf go all the way to the pool's coping?",
                "Typically it stops a short distance back with a hard edge or drain strip rather than butting directly against the coping, since that gap is what keeps splash-out water from pooling under the turf instead of draining away."),
        ],
        "sources": SRC,
    },
    "repair": {
        "title": "Artificial Turf Repair in Oviedo, FL",
        "meta": "Turf repair in Oviedo, FL for oak-root heave, storm-lifted edges and drainage fixes, quoted after a site visit, checked September 2026.",
        "h1": "Repairing synthetic turf on Oviedo's older, oak-shaded lots",
        "lede": capsule("A turf repair in Oviedo gets priced from photos or a short visit, not a flat rate by the square foot, because a lifted seam, a root-heaved base and a washed-out edge each call for a different fix. The city's oldest lawns, many installed under decades-old live oaks, tend to show a specific kind of damage a newer subdivision rarely does."),
        "sections": [
            ("Oak root heave under a decade-old Alafaya Woods lawn",
             "<p>A live oak planted when Alafaya Woods or Tuska Ridge went in during the late 1980s has had thirty-plus years to send roots well past its canopy, and a root running under turf installed more recently can lift a base section from underneath without ever breaking the surface cleanly. The fix usually means pulling back the affected turf, regrading around the root rather than cutting it, since a certified arborist's involvement is the only path around the state's drip-line protection, and reinstalling with slightly more base depth to buffer future movement. That kind of repair is exactly why the price depends on what a visit finds, not a flat rate by the foot.</p>"),
            ("Base failure from Oviedo's high water table",
             "<p>A lawn built with a shallow or under-compacted base on Oviedo's flatwoods sand can hold visible dips after two or three rainy seasons, especially where the original installer didn't plan for ground that stays wet for weeks after a summer storm. Repairing that kind of settling means pulling the turf back, adding properly washed crushed rock to correct the low spot, and recompacting in lifts instead of resurfacing over ground that already gave way underneath. Catching it after one season is a smaller job than waiting for a second summer to make the dip worse.</p>"),
            ("Edges lifted near the Econlockhatchee corridor and Black Hammock",
             "<p>A lawn on a lot near the Econlockhatchee corridor or the Black Hammock shoreline sees more standing water and higher wind exposure than an interior subdivision lot, and an edge anchored lightly at installation is the first thing to show it after a tropical storm passes through. Repairing that edge means re-anchoring with the fastener spacing the state's wind standard actually calls for, not just re-gluing the same seam that failed, and checking whether infill washed toward the property's low point during the same storm, since both problems often show up together on the same visit.</p>"),
        ],
        "scenario": ("A lifted seam along a 30-year-old oak root in Alafaya Woods",
                     "<p>Say a home in Alafaya Woods has a 12-foot seam that's lifted along one edge of the backyard, tracing the path of a live oak root that's grown considerably since the lawn went in years ago. A repair visit checks whether the root is still actively growing under that spot or has settled, since an actively growing root changes the fix from a simple reglue to a full regrade with an arborist's input on how close excavation can safely go. Either way, the quote follows what the visit finds rather than the length of the seam alone, because a 12-foot lift caused by a root costs more to fix correctly than the same length lifted by a simple installation shortcut.</p>"
                     + "<p>A homeowner who notices the lift early, before the root pushes the seam much further, usually has the cheaper of the two repair paths still available.</p>"),
        "faqs": [
            faq("Why can't Oviedo turf repair be quoted over the phone?",
                "Because a lifted seam, a settled base and a washed-out edge each need a different fix, and the cause matters as much as the size of the damaged area. A photo or a short visit tells a repair crew which problem they're actually looking at before they quote it."),
            faq("Does storm damage near Black Hammock or the river corridor usually mean starting over?",
                "Rarely. Most storm damage in those areas shows up as a lifted edge or migrated infill rather than a failed base, and both are addressable repairs rather than a full tear-out, though a visit is still the only way to confirm that for a specific yard."),
            faq("Is oak root damage covered differently than a normal seam repair?",
                "Not by us directly, since we don't sell or reference any warranty here, but a homeowner should ask their original installer whether root-related lifting falls inside a workmanship warranty before paying for a repair out of pocket."),
        ],
        "sources": SRC,
    },
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
