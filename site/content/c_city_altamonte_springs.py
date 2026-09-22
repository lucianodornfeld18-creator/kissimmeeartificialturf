# -*- coding: utf-8 -*-
"""Altamonte Springs, FL (tier 2, Seminole County). Researched September 2026.
No dedicated permit sub-page exists on this site for Altamonte Springs' own Land Development Code
(unlike Kissimmee, Orlando, etc.); we link the Seminole County permit page as the honest baseline
and name the city's own Building and Fire Safety Department for a code-specific answer."""
from _helpers import page, capsule, sec, table, faq, a, svc, city, cs, post, src, ext, price
from _cityservice import cityservice_pages

SLUG = "altamonte-springs"

ABFS = ("City of Altamonte Springs — Building and Fire Safety Department", "https://www.altamonte.org/406/Building-and-Fire-Safety")
PUREALTA = ("City of Altamonte Springs — About pureALTA", "https://www.altamonte.org/1011/About-pureALTA")
RECLAIMED = ("City of Altamonte Springs — Reclaimed Water", "https://www.altamonte.org/659/Reclaimed-Water")
CRANES = ("City of Altamonte Springs — Cranes Roost Park", "https://www.altamonte.org/367/Cranes-Roost-Park")
LAKE_ORIENTA = ("Seminole County Water Atlas (USF) — Lake Orienta", "https://seminole.wateratlas.usf.edu/waterbodies/lakes/7631/lake-orienta")
LAKE_BRANTLEY = ("Seminole County Water Atlas (USF) — Lake Brantley", "https://seminole.wateratlas.usf.edu/waterbodies/lakes/7519/lake-brantley")
APOPKA_OSD = ("USDA NRCS — official series description, Apopka series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/A/APOPKA.html")
TAVARES_OSD = ("USDA NRCS — official series description, Tavares series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/T/TAVARES.html")
CANDLER_OSD = ("USDA NRCS — official series description, Candler series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/C/CANDLER.html")
CENSUS_ALT = ("U.S. Census Bureau QuickFacts — Altamonte Springs city, Florida", "https://www.census.gov/quickfacts/altamontespringscityflorida")
CH718 = ("Florida Statutes Chapter 718 — Condominiums", "https://www.flsenate.gov/Laws/Statutes/2025/Chapter718/All")
SJRWMD_RESTRICT = ("St. Johns River Water Management District — watering restrictions", "https://www.sjrwmd.com/wateringrestrictions/")
PERMITS_SEM = "/laws/permits/seminole-county/"
HB683 = "/laws/florida-hb-683/"
HOA = "/laws/hoa-rules/"
COST = "/artificial-turf-cost/"

SRC = [ABFS, PUREALTA, RECLAIMED, CRANES, LAKE_ORIENTA, LAKE_BRANTLEY, APOPKA_OSD, TAVARES_OSD, CANDLER_OSD,
       CENSUS_ALT, CH718, SJRWMD_RESTRICT, "dep-rule", "fs125572", "fs7203045", "usda-wss"]

# ============================================================== hub
HUB = page(
    "/areas/altamonte-springs/", "city",
    "Artificial Turf in Altamonte Springs, FL (2026)",
    "Synthetic grass installation, permits, the pureALTA reclaimed-water schedule and soil facts for Altamonte Springs, FL. Checked September 2026.",
    "Turf for Altamonte Springs' oaks, condos and lakefront yards",
    capsule(f"Kissimmee Artificial Turf installs, repairs and cleans synthetic lawns, pet turf and putting greens in Altamonte Springs, about 26 miles from our Kissimmee base, at {price('residential')} per square foot installed as of September 2026. The city runs its own reclaimed-water utility, and irrigation heads under a new lawn get capped rather than reconnected to that system, on a two-day-a-week schedule that no longer applies once they are."),
    "".join([
        sec("Turf work in Altamonte Springs",
            f"<p>Altamonte Springs is compact and built out, and its identity runs through {ext(CRANES[1], 'Cranes Roost Park')}, the 45-acre lake and plaza at the center of Uptown Altamonte. Around that core sit two very different housing generations: ranch and split-level subdivisions from the city's 1970s-through-1990s growth run, many under a mature oak canopy, and condo or townhome buildings built closer to the park itself. Both generations call us for the same handful of jobs: {svc('residential', 'a full lawn')}, {svc('pet', 'a run for the dog')}, {svc('putting', 'a putting green')}, {svc('pool', 'turf around a pool or lanai')}.</p>"
            + f"<p>What changes from yard to yard here isn't the price. It's whether a lot backs onto the Little Wekiva River or Lake Orienta and needs the state's waterbody setback staked before anything else, whether a live oak's canopy reaches further than it looks, and whether the property is a single-family lot at all or a condo unit answering to a different approval process entirely, a split that shows up less often in a ranch-lot town like {city('casselberry', 'Casselberry')} or {city('maitland', 'Maitland')} next door.</p>"),
        table("Altamonte Springs yard types and what we do differently",
              ["Yard type", "Where it turns up", "What changes about the job"],
              [["1970s–90s ranch and split-level subdivisions", "Spring Oaks and similar older neighborhoods", "Mature live oaks mean staking the drip line before ordering turf"],
               ["Condo and townhome buildings", "Uptown Altamonte and the streets around Cranes Roost", "Approval runs through the condo board under Florida's Condominium Act, not a single-family HOA process"],
               ["Lakefront and river-corridor lots", "Lake Orienta and the Little Wekiva River corridor", "State's 10-ft waterbody setback gets staked at layout, before turf is ordered"],
               ["Homes on the city's reclaimed system", "Neighborhoods served by Altamonte Springs' own reclaimed line", "Heads get capped at the valve box, and the twice-weekly reclaimed schedule stops applying to that area"]],
              "Checked against the city's own published pages and USDA soil data, September 2026."),
        sec("Permits and HOAs in Altamonte Springs",
            f"<p>Altamonte Springs runs its own Building and Fire Safety Department rather than routing permits through Seminole County, and we haven't searched the city's Land Development Code section by section the way we have for a handful of other Central Florida cities. The straightforward answer is to call the department at (407) 571-8446 and ask directly how it treats a synthetic-turf swap. {a(PERMITS_SEM, 'Our Seminole County permit page')} covers what we did check, the unincorporated county's own office, plus the state floor that reaches every address in the county regardless of what a specific city's code says: {src('dep-rule', 'Rule 62-308.100')} sets material, drainage and setback minimums no local government can undercut on a covered single-family lot.</p>"
            + f"<p>A homeowners association is a different matter than either government office. {a(HOA, 'F.S. 720.3045')} protects only the turf a street or a neighboring lot genuinely can't see, and a condo association works under an entirely different law, covered below.</p>"),
        sec("Water: Altamonte Springs' reclaimed system and the Little Wekiva watershed",
            f"<p>Altamonte Springs treats and delivers its own reclaimed water rather than buying it from a county authority, and the {ext(PUREALTA[1], 'pureALTA project')} built on that system, running already-reclaimed water through ozone and biological filtration in a demonstration partnership with the St. Johns River Water Management District that treated roughly 28,000 gallons a day during its test phase. Day to day, most residents interact with a simpler reclaimed connection instead: odd-numbered addresses get Wednesday and Saturday, even-numbered addresses get Thursday and Sunday, and apartments or condos get Tuesday and Friday, none of it before 4 p.m. or after 10 a.m. shuts it off for the day ({ext(RECLAIMED[1], 'the city’s reclaimed-water schedule')}). A property without that reclaimed connection instead follows {ext(SJRWMD_RESTRICT[1], 'the St. Johns River Water Management District’s')} tighter, one-day-a-week restriction. A synthetic lawn skips all of this the moment its irrigation heads get capped, a step the state's rule requires outright.</p>"),
        sec("What's under an Altamonte Springs lawn",
            f"<p>The city sits across two different sand profiles. Higher ground toward the ridge carries Apopka and Tavares series soils, well to moderately well drained and built from thick wind-blown and marine sand, with a clay-enriched layer that only shows up several feet down and Tavares' own seasonal water table sitting 42 to 72 inches deep ({ext(APOPKA_OSD[1], 'USDA’s Apopka series description')}; {ext(TAVARES_OSD[1], 'and its Tavares description')}). The same Apopka series turns up on ridge ground well to the west, toward {city('apopka', 'Apopka')} and the Orange County line, though the exact profile shifts some from one lot to the next. Candler sand, common on the same ridge system elsewhere in Central Florida, turns up on parts of this higher ground too ({ext(CANDLER_OSD[1], 'USDA’s Candler series description')}). Closer to the Little Wekiva River and Lake Orienta, the ground drops into wetter flatwoods sand that stays saturated much longer after a storm, part of the same soil belt covering most of the rest of Seminole County. Either soil gets the same washed, open-graded crushed rock base the state rule requires; the river side of town just gets more attention paid to depth.</p>"),
        "<!--AUTO:city-services-->",
    ]),
    faqs=[
        faq("How do you find the best turf installer near you in Altamonte Springs?",
            "Ask whether the crew already separates a single-family lot's rules from a condo's before quoting, since the two run through entirely different approval paths here. Beyond that, the usual checklist applies: base depth and material named in writing, infill type spelled out, and a plan for any live oak's drip line before a shovel goes in the ground."),
        faq("Does Altamonte Springs have its own written rule on synthetic turf?",
            "We haven't found a published one and haven't searched the city's code section by section the way we have for a handful of other Central Florida cities, so the honest answer is to call the Building and Fire Safety Department directly. Either way, the state's May 2026 standard sets a floor the city can't undercut on a covered single-family lot."),
        faq("Is a patio at a Cranes Roost-area condo covered by the same rule as a single-family yard?",
            "No. The state's synthetic-turf rule applies to single-family residential lots of an acre or less; a condo's common and limited common elements run through Florida's Condominium Act and the building's own declaration instead, so a patio or courtyard swap there goes through the condo board, not a homeowners association's visibility test."),
        faq("What if a yard backs onto the Little Wekiva River or Lake Orienta?",
            "Ten feet from the water is the number to plan around, measured to the ordinary or mean high line, and only a seawall or bulkhead standing between the lot and the water changes that. We haven't found a published Altamonte Springs buffer stricter than the state's figure."),
        faq("Does reclaimed water count as irrigation under the state's turf rule?",
            "Yes. An in-ground line still counts as an irrigation system whether the source is potable or reclaimed, so any head that used to water a section now covered in synthetic turf gets capped at the valve box either way."),
    ],
    sources=SRC, crumbs=[("Service areas", "/areas/")], crumb="Altamonte Springs", city=SLUG,
    related=[("/areas/seminole-county/", "Artificial turf in Seminole County"), (PERMITS_SEM, "Seminole County permit rules for turf"),
             ("/areas/casselberry/", "Turf in Casselberry"), ("/areas/maitland/", "Turf in Maitland"), (COST, "Full turf cost guide")])

# ============================================================== local (6 services)
LOCAL = {
    "residential": {
        "title": "Artificial Grass Installation in Altamonte Springs, FL",
        "meta": "Synthetic lawns for Altamonte Springs yards, from Spring Oaks' oak canopy to Uptown Altamonte condos, with the state's 10-ft lake setback explained.",
        "h1": "A synthetic lawn built for Altamonte Springs' oaks, lakes and condos",
        "lede": capsule(f"A residential conversion in Altamonte Springs runs {price('residential')} per square foot installed as of September 2026, whether the lot sits under Spring Oaks' mature oak canopy or a block from Cranes Roost Park. Older ranch lots and newer condo buildings both change the base and approval steps we plan around, not the published price range."),
        "sections": [
            ("What a live oak canopy changes about a residential lawn here",
             f"<p>Altamonte Springs grew up through the 1970s, 1980s and into the 1990s, and a lot of that growth left mature live oaks standing over what's now an established residential lawn. A certified arborist has to sign off before synthetic grass goes in anywhere under one of those canopies, whether the tree sits on the lot itself or next door, unless the crew is willing to work entirely outside the drip line instead. On an older Altamonte Springs lot that canopy often reaches further than the trunk suggests, past a fence line and into a neighbor's yard, which is worth walking before measuring a single square foot for turf.</p>"
             + f"<p>Getting that letter first, rather than digging and hoping a root isn't in the way, is the only path around the setback instead of a shortcut past it. A yard with two or three mature oaks can lose more usable lawn to drip lines than a homeowner expects going into the first measurement; {post('artificial-turf-near-live-oaks-and-palms', 'our piece on turf near live oaks and palms')} goes into what a root system actually tolerates.</p>"),
            ("Ridge sand or river-bottom sand: what's actually under the lawn",
             f"<p>{a('/artificial-grass-installation/', 'A residential lawn conversion')} in Altamonte Springs sits on one of two different sand profiles depending on which side of town the address falls on. Toward the ridge, {ext(APOPKA_OSD[1], 'Apopka')} and {ext(TAVARES_OSD[1], 'Tavares')} series soils drain well to moderately well, built from thick wind-blown sand with a clay layer buried several feet down. Toward the Little Wekiva River and Lake Orienta, the ground drops into wetter flatwoods sand, the kind that stays close to saturated for a good while once the summer rains start.</p>"
             "<p>Both get the same washed, open-graded crushed rock base the state standard requires, but a river-side lot earns extra attention to depth and grade, since that ground is already holding more water before the first shovel of rock goes in.</p>"),
            ("From a 1978 ranch lot to a 2015 condo renovation",
             f"<p>A {city('altamonte-springs', 'residential')} conversion here can mean two very different starting points. An older ranch or split-level home, often with a fenced backyard and a pool cage, is a single-family lot the way the state's turf rule and {a(HOA, 'Florida’s HOA-visibility statute')} both expect. A condo or townhome near Uptown Altamonte is a different animal: any turf on a shared patio or courtyard runs through the building's own declaration and board, a Chapter 718 process rather than a single-family approval, which {cs('altamonte-springs', 'pool', 'our pool turf page for this city')} covers in more depth for a screened lanai specifically.</p>"
             + f"<p>Knowing which category a given address falls into, before pricing anything, changes who signs off on the job as much as it changes the yard itself, the same split a crew works around in condo-heavy {city('winter-park', 'Winter Park')} a few miles east.</p>"),
        ],
        "scenario": ("Say your Altamonte Springs backyard is 900 square feet",
                     "<p>Say you have a 900 sq ft backyard behind a 1982 ranch home near Spring Oaks, with a mature live oak in one corner whose canopy covers roughly 150 sq ft of that space. Staying outside the drip line without an arborist letter leaves about 750 sq ft to convert. "
                     f"At {price('residential')} per square foot, that's roughly ${750*8:,}–${750*18:,} installed, or {price('residential', typical=True)} a square foot for a typical build, putting the job closer to ${750*10:,}–${750*16:,}. "
                     "Getting an arborist to sign off on the full canopy footprint instead would open up the remaining 150 sq ft, but on a lot this size, most homeowners find the math doesn't change enough to bother once the fee for that letter is factored in. The base underneath still runs washed, open-graded crushed rock either way, graded to fall away from the house toward the yard's low corner.</p>"),
        "faqs": [
            faq("Does a live oak on a neighbor's lot still count against my Altamonte Springs yard?",
                "Yes. The drip-line rule applies to a tree's canopy regardless of which property the trunk sits on, so a neighbor's oak reaching over a shared fence line still sets the boundary for where turf can go without an arborist's letter."),
            faq("Is Spring Oaks' soil really different from a newer Altamonte Springs subdivision?",
                "Often, yes. Spring Oaks and other ridge-adjacent neighborhoods tend to sit on better-drained Apopka or Tavares sand, while a lot closer to the Little Wekiva River or Lake Orienta is more likely on wetter flatwoods soil, which changes how much attention the base gets during grading."),
        ],
        "sources": SRC,
    },
    "pet": {
        "title": "Pet Turf and Dog Runs in Altamonte Springs, FL",
        "meta": "Fast-draining pet turf for Altamonte Springs' fenced ranch yards, built for the flatwoods water table near the Little Wekiva River. Checked 2026.",
        "h1": "Dog-run turf for Altamonte Springs' fenced backyards",
        "lede": capsule(f"Pet turf in Altamonte Springs runs {price('pet')} per square foot as of September 2026, sized to the fenced backyards that came with the city's 1970s-through-1990s ranch subdivisions. A dog run near the Little Wekiva River or Lake Orienta needs the same 10-ft waterbody setback any other synthetic surface does."),
        "sections": [
            ("Why Altamonte Springs' older fence lines suit a dog run",
             "<p>Ranch and split-level homes from the city's biggest growth years, the 1970s through the 1990s, mostly came with a fenced backyard, which is exactly the layout a dog run wants: a contained space a homeowner can rinse without worrying about a loose dog wandering off. A run built inside that existing fence line skips the cost of adding new fencing, and it's usually sized by where the fence already sits rather than by a fixed dimension.</p>"
             + f"<p>What changes from one Altamonte Springs yard to the next is less the fence itself than what's underneath it, which is where the city's two sand profiles start to matter for a pet run specifically; keeping the finished surface smelling fresh afterward is a separate question, one {post('how-to-get-dog-urine-smell-out-of-artificial-turf', 'this post')} covers on its own.</p>"),
            ("A high water table changes how a dog run drains",
             f"<p>Sand closer to the Little Wekiva River or Lake Orienta holds more moisture near the surface for longer after a storm than the ridge sand does, and a dog run, concentrating urine and rinse water onto one small patch of ground, feels that difference more than an open lawn would. A crew works toward four inches of compacted washed rock here rather than two, and drops the weed fabric a residential lawn might otherwise get, since fabric under a run would hold liquid right at the surface instead of letting it soak into the rock below.</p>"
             "<p>A lot on the ridge's better-drained Apopka or Tavares sand has more room for error, but the build method itself doesn't change.</p>"),
            ("Keeping a dog run clear of the lake setback",
             f"<p>A dog run gets no exception from the state's water rule just because it's smaller than a full lawn: the same 10-foot line applies whether the yard backs onto Lake Orienta or a stretch of the Little Wekiva River, and only an existing seawall shortens that number. {svc('pet', 'Staking the line before the fence posts go in')} keeps a layout from being ordered for square footage the setback won't actually allow, and grading the run gently near that edge sends rinse water away from the bank instead of toward it.</p>"
             "<p>None of this changes what a run costs; it changes where its fence line ends up on a waterfront lot.</p>"),
        ],
        "scenario": ("A 10x16 dog run behind a fenced Altamonte Springs yard",
                     "<p>Say you have a 10x16 ft dog run, 160 sq ft, tucked along the fence line of a 1985 ranch home a few blocks from the Little Wekiva River. "
                     f"At {price('pet')} per square foot, that run lands around ${160*10:,}–${160*18:,} installed, or roughly ${160*12:,}–${160*16:,} for a typical odor-control build with silica or zeolite infill. "
                     "Because the lot sits on the wetter side of town, the base goes in at the fuller four inches rather than two, which doesn't change the square-foot price but does add a little to the total rock delivered for a run this size. Skipping the weed barrier under the run, standard for a pet area, keeps urine from pooling on a fabric layer instead of draining through it.</p>"),
        "faqs": [
            faq("Can I put a dog run right next to Lake Orienta?",
                "The same 10 feet applies to a run as it would to a full lawn, measured from the water's ordinary or mean high line, unless an existing seawall shortens it. Staking that distance before the fence goes up avoids planning a footprint that has to shrink later."),
            faq("Does the flatwoods water table near the river make pet turf smell worse?",
                "Not on its own. What matters more is base depth and infill choice: a fuller rock base and a silica or zeolite infill, rinsed regularly, manage odor the same way regardless of which side of town the water table sits closer to the surface."),
        ],
        "sources": SRC,
    },
    "putting": {
        "title": "Backyard Putting Greens in Altamonte Springs, FL",
        "meta": "Putting greens for Altamonte Springs' larger lakefront lots, staked to the state's 10-ft setback before the first contour is cut. Checked Sept. 2026.",
        "h1": "Putting greens sized to Altamonte Springs' larger lots",
        "lede": capsule(f"A backyard putting green in Altamonte Springs runs {price('putting')} per square foot as of September 2026. The lots with room for one tend to be the older, larger parcels near the Little Wekiva River and Lake Orienta, where the state's 10-ft waterbody setback gets staked before a single contour is cut."),
        "sections": [
            ("Staking the setback before shaping a green near the water",
             f"<p>A putting green's contours, tiers and cupped sections take up more continuous ground than a flat lawn does, which makes a waterfront Altamonte Springs lot both the most tempting and the most restricted place to put one. Ten feet of clearance from the water is the number Florida's rule holds a green to, the same as any other turf, and only an existing seawall changes it; that line gets staked during layout, before ordering material, so the green is designed around the buildable footprint rather than the full lot down to the shoreline.</p>"
             "<p>A lot backing onto Lake Orienta usually has more room than that setback first suggests once the actual buildable strip is measured out.</p>"),
            ("Why ridge sand makes contour work easier",
             f"<p>Toward the ridge, where {ext(APOPKA_OSD[1], 'Apopka')} and {ext(TAVARES_OSD[1], 'Tavares')} series sand drains well and holds a shaped grade without much fuss, cutting the rolls and breaks a green needs is more straightforward than it is on the wetter flatwoods sand closer to the river. That doesn't mean a river-corridor lot can't have a green, only that the base gets built with more margin for settling, and drainage away from any low tier matters more on that side of town.</p>"
             + f"<p>Either soil still needs a firm, compacted subbase before the green's contours go in; the sand type changes how much attention that step gets, not whether it happens. {post('artificial-turf-glossary', 'A quick glossary of terms like stimp and face weight')} is worth a look before comparing two green quotes side by side.</p>"),
            ("Why a Cranes Roost-area condo patio usually can't fit one",
             f"<p>A putting green needs enough uninterrupted square footage for a cup, a fringe and at least one break, which is a tall order on a condo's limited common-element patio near {ext(CRANES[1], 'Cranes Roost Park')}. Beyond the space problem, that patio would run through the building's own Chapter 718 approval process rather than a single-family HOA's visibility test, adding a step a ranch-lot green never has to clear. For most Altamonte Springs condo owners, {svc('putting', 'a compact chipping mat or a small fringe section')} fits the space better than a full green ever would.</p>"),
        ],
        "scenario": ("A 300 sq ft green on a Little Wekiva-adjacent lot",
                     "<p>Say you have a 300 sq ft putting surface with a 100 sq ft fringe planned for a backyard that runs down toward a Little Wekiva tributary. Staking the 10-foot setback first shows the buildable strip actually starts a bit further from the water than the property line suggests, but there's still room for the full 400 sq ft combined footprint. "
                     f"At {price('putting')} per square foot for the green itself, that's ${300*14:,}–${300*30:,}, with the fringe typically priced closer to residential turf rather than putting-green spec. "
                     "Shaping two mild breaks into a green this size works fine on the property's flatwoods sand, as long as the base compacts firm enough first to hold those contours through a full rainy season without settling unevenly.</p>"),
        "faqs": [
            faq("Is Lake Brantley inside Altamonte Springs city limits?",
                f"No. Lake Brantley sits just north of the city, mostly in {city('longwood', 'Longwood')} and unincorporated Seminole County, though a handful of Altamonte Springs lots sit close enough to it that the same 10-foot state setback still applies if a yard actually touches the water."),
            faq("Can a putting green go on a condo's patio near Cranes Roost?",
                "Rarely, and not without clearing it through the building's own board first, since a condo's common and limited common areas run through Chapter 718 rather than a single-family process. Space is usually the bigger obstacle before the approval question even comes up."),
        ],
        "sources": SRC,
    },
    "playground": {
        "title": "Playground Turf in Altamonte Springs, FL",
        "meta": "Cushioned playground turf for Altamonte Springs' family subdivisions, with the oak drip-line rule and capped irrigation explained. Checked 2026.",
        "h1": "Play-area turf for Altamonte Springs' family neighborhoods",
        "lede": capsule(f"Playground turf in Altamonte Springs runs {price('playground')} per square foot as of September 2026. The city's population, about 46,000 at the 2020 Census, grew mostly through family subdivisions built in the 1970s, 1980s and 1990s, many of which still shade a swing set under the same oaks planted when the houses went up."),
        "sections": [
            ("A city that grew up around families, and still is one",
             f"<p>Altamonte Springs counted 46,231 residents at the 2020 Census ({ext(CENSUS_ALT[1], 'the Bureau’s own count')}), most of them in neighborhoods built during the city's 1970s-to-1990s growth run. A lot of those original family lots have cycled to a new generation of kids, which is why a play area request here is as likely to come from a 1980s ranch home as a newer build. {a('/playground-turf/', 'Playground turf')} on an older lot usually means working around whatever landscaping the original owners planted decades ago.</p>"
             + f"<p>That includes the oaks, which is where the state's tree rule comes into the picture for a play area specifically. Material safety is a separate, common question for a play surface, one {post('is-artificial-turf-safe-for-kids-pfas-lead', 'this post')} answers directly.</p>"),
            ("Oak shade over a swing set, and what the drip-line rule actually covers",
             "<p>A live oak's shade is often exactly what a homeowner wants over a play structure in Central Florida's summer sun, but the state's rule keeps synthetic turf out of that same tree's drip line unless a certified arborist signs off. The rule applies to the turf installation itself, not to the swing set or slide sitting on the ground, so a play structure can stay under an oak's canopy; it's the excavation and turf laid around its base that needs the arborist's letter first if it reaches inside the drip line.</p>"
             "<p>Working out where that line actually falls, rather than assuming a play area automatically clears it, is worth doing before a shock pad and turf get ordered for the space.</p>"),
            ("Capping the heads under a play area first",
             f"<p>A play area built over what used to be lawn on Altamonte Springs' reclaimed-water system needs its irrigation heads capped at the valve box before turf and pad go down, the same as anywhere else the state's rule reaches, since {ext(RECLAIMED[1], 'the city’s twice-weekly reclaimed schedule')} no longer applies to that footprint once it's converted. That's a small step, but it's one worth confirming happened correctly under a play area specifically, since a missed head buried under a shock pad is harder to locate later than one left exposed in open lawn.</p>"),
        ],
        "scenario": ("A 10x16 play area in an established Altamonte Springs yard",
                     "<p>Say you have a 10x16 ft play area, 160 sq ft, planned for a swing set in the backyard of a 1979 home near one of the city's older subdivisions, with a shock pad sized to the equipment's fall height. "
                     f"At {price('playground')} per square foot, that's roughly ${160*10:,}–${160*25:,} installed, or {price('playground', typical=True)} a square foot for a typical build with pad included, landing closer to ${160*12:,}–${160*19:,}. "
                     "If part of that footprint reaches under a mature oak's canopy, the number holds, but the timeline doesn't, since an arborist's letter needs to come back before the crew can excavate that section. Capping the two irrigation heads that used to water this part of the yard happens before the pad goes in, not after.</p>"),
        "faqs": [
            faq("How many families with kids actually live in Altamonte Springs?",
                "The city's 2020 Census count was 46,231 residents, spread mostly across subdivisions built during its 1970s-through-1990s growth run, which is why a lot of play-area requests come from older lots being updated for a second or third generation of kids rather than brand-new construction."),
            faq("Does a swing set under an oak canopy violate the state's turf rule?",
                "No. The rule restricts installing synthetic turf inside a tree's drip line without an arborist's letter; it doesn't restrict where play equipment itself can sit. Only the turfed footprint around the structure needs to clear that rule if it reaches under the canopy."),
        ],
        "sources": SRC,
    },
    "pool": {
        "title": "Pool and Lanai Turf in Altamonte Springs, FL",
        "meta": "Turf for Altamonte Springs pool decks and lanais, from ranch-home screen cages to condo common elements under Chapter 718. Checked Sept. 2026.",
        "h1": "Pool-deck turf for two kinds of Altamonte Springs property",
        "lede": capsule(f"Turf around a pool or inside a lanai in Altamonte Springs runs {price('residential')} per square foot as of September 2026. What changes the job more than the price is whether the pool sits on a single-family ranch lot or a condo's common element near Uptown Altamonte, since the two answer to different approval rules entirely."),
        "sections": [
            ("A condo pool deck runs through a different rulebook",
             f"<p>Several Uptown Altamonte and Cranes Roost-area buildings hold their pools as a common or limited common element rather than something an individual unit owner controls outright, and turf on that deck goes through the association's board under {ext(CH718[1], 'Florida’s Condominium Act')} rather than the single-family process the state's turf rule and {a(HOA, 'HOA-visibility statute')} both describe. Neither of those two laws was written with a condo's shared pool deck in mind, since both apply specifically to single-family residential property.</p>"
             "<p>Practically, that means a condo board's own rules, not a state floor, decide what a pool-deck turf project needs to clear before work starts. This is informational, not legal advice, and a specific building's declaration is the document that actually controls.</p>"),
            ("Older ranch pool cages need a different fix entirely",
             f"<p>A 1970s or 1980s ranch home's screen-enclosed lanai is a single-family lot problem, not a condo one, and the turf question there is about drainage rather than approval process: turf laid over the enclosure's concrete deck needs a drainage underlay and glue-down edges rather than nails, since there's no soil underneath to anchor into. {a('/pool-turf/', 'Pool and lanai turf')} inside an older screen cage also tends to run through narrower side strips than a newer enclosure, which changes how a crew seams the turf more than it changes the base.</p>"
             + f"<p>Both jobs use the same product family; the deck itself dictates the install method. {post('install-artificial-turf-over-concrete-pavers-or-grass', 'This post')} covers the underlay question for concrete, pavers and existing grass side by side.</p>"),
            ("Reclaimed heads near a pool deck still get capped",
             f"<p>A pool-cage yard on Altamonte Springs' reclaimed system often had a head or two watering the narrow strip just inside the screen, and that head gets capped at the valve box the same as any other once the strip is converted to turf, since {ext(RECLAIMED[1], 'the city’s reclaimed schedule')} stops applying to synthetic turf under the state's rule regardless of where the head sat. A crew checking a pool-deck job for old irrigation lines before laying turf avoids leaving one live under the new surface by accident.</p>"),
        ],
        "scenario": ("A 6x40 ft strip inside a screened lanai",
                     "<p>Say you have a 6x40 ft strip of turf planned for the two sides of a screened pool cage on a 1983 ranch home, 240 sq ft total, replacing grass that never filled in fully under the enclosure's shade. "
                     f"At {price('residential')} per square foot, that's roughly ${240*8:,}–${240*18:,} installed, or {price('residential', typical=True)} a square foot for a typical build, closer to ${240*10:,}–${240*16:,}. "
                     "Because the strip sits over a concrete deck rather than soil, the quote adds a drainage underlay and adhesive-set edges rather than a standard rock base, and any irrigation head that used to reach that strip gets capped at the valve box as part of the same visit.</p>"),
        "faqs": [
            faq("Does a condo pool deck near Cranes Roost need HOA-visibility approval under F.S. 720.3045?",
                "No. That statute covers a single-family homeowners association's declaration; a condo's common and limited common elements run through Florida's Condominium Act and the building's own declaration instead, which is a separate approval path with its own board."),
            faq("Can turf go over an existing concrete pool deck inside a screen cage?",
                "Yes, with a drainage underlay beneath it and the edges set with adhesive rather than nails, since there's no soil at that point to anchor into. The rest of the yard, if any, can still use a standard compacted rock base."),
        ],
        "sources": SRC,
    },
    "repair": {
        "title": "Turf Repair in Altamonte Springs, FL",
        "meta": "Turf repair for Altamonte Springs lawns: root-heaved seams under old oaks, capped-head checks and drainage fixes. Quoted after a site visit.",
        "h1": "Fixing turf that's aged under Altamonte Springs' oaks and lakes",
        "lede": capsule("Turf repair in Altamonte Springs is quoted after photos or a short site visit, since a lifted seam, a root heave and a drainage dip all cost differently to fix even though they can look similar from the porch. Two local causes come up more than most: a live oak root working under an older lawn, and a capped irrigation head that was never fully removed."),
        "sections": [
            ("When a live oak root is the actual cause",
             f"<p>Altamonte Springs' oldest neighborhoods carry decades of oak growth over lawns that were installed well after the trees themselves, and a root working its way under an established turf lawn tends to heave a narrow ridge tracking back toward the trunk, different from the broad, shallow dip a simply settled base produces. A repair here sometimes needs an arborist's read on the root itself, not just a base rebuild, before deciding whether to reroute the turf's edge around it or accept that spot will need attention again as the root keeps growing.</p>"
             + f"<p>Telling the two problems apart before quoting anything is most of what determines whether a repair is quick or involved, and whether {post('does-homeowners-insurance-cover-artificial-turf', 'a homeowner’s policy')} is even worth checking depends partly on which one it turns out to be.</p>"),
            ("No dedicated Altamonte Springs permit page, so a call settles it",
             f"<p>Most turf repairs don't touch anything a city permit reaches, but a repair that involves regrading near the Little Wekiva River, a canal, or a lake's edge is worth a call to Altamonte Springs' Building and Fire Safety Department at (407) 571-8446 first, since we haven't researched this city's own code closely enough to promise an answer either way. {a(PERMITS_SEM, 'Our Seminole County permit page')} covers the unincorporated county's rules and the state floor that applies regardless of which office actually has a given repair site.</p>"),
            ("A capped head that never got fully removed",
             f"<p>An older Altamonte Springs lawn, especially one converted before the current subgrade standard, sometimes had an irrigation head capped at the surface without pulling the pipe and fitting below it, and that buried hardware can corrode into a small void that shows up years later as a dip in the turf above it. On a reclaimed-water property, that dip often lines up with where the twice-weekly schedule used to reach before the area was converted. Digging down to the old fitting and filling the void properly is what actually stops the dip from reappearing.</p>"),
        ],
        "scenario": ("A lifted seam near an oak root in a 1980s yard",
                     "<p>Say a four-foot seam has opened along a driveway edge on a 1985 ranch home near one of Altamonte Springs' older subdivisions, where a live oak's roots have been pushing up from below for a couple of years. That's roughly 15 to 20 sq ft of turf and base needing attention, not a whole-yard replacement. A repair like this gets a firm number after photos or a short visit, since the fix could mean reseating and regluing that one edge, or pulling back a larger section to deal with the root underneath, and those two jobs price very differently. What holds regardless: matching grain direction and infill on the patch matters as much as the seam work, and if the root is still active, this spot may need another look in a few years no matter how well today's fix goes.</p>"),
        "faqs": [
            faq("What's the best way to find a turf repair company near me in Altamonte Springs?",
                "Ask how they tell a root heave from a settled base before quoting, since the two look similar but need different fixes. A repair crew that wants to see the spot in person, or at least a clear photo, before naming a number is being straight with you rather than guessing."),
            faq("Does Altamonte Springs require a permit to fix a lifted turf edge?",
                "Usually not for a small patch, but we haven't checked this city's code closely enough to promise that for every scope, especially anything involving regrading near water. A quick call to the Building and Fire Safety Department settles it faster than guessing."),
        ],
        "sources": SRC,
    },
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
