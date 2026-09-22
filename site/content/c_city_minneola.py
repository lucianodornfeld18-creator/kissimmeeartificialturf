# -*- coding: utf-8 -*-
"""Minneola, Lake County, tier 2. Building Department and irrigation facts checked directly
against minneola.us (Ordinance 2009-08 implements the St. Johns River Water Management
District's landscape rule); Hills of Minneola CDD facts checked against hillsofminneolacdd.net
and foundersridgecdd.com. See docs/TIER2-BRIEF.md. Note for the reviewer: this differs from the
"Green Swamp/SWFWMD" framing c_counties.py uses for Minneola — Minneola's own conservation
ordinance names SJRWMD specifically, so that is what this module states; see the final report."""
from _helpers import page, capsule, sec, table, faq, a, svc, city, county, cs, post, src, ext, price
from _cityservice import cityservice_pages

SLUG = "minneola"

BUILDING = ("City of Minneola — Building Department", "https://www.minneola.us/building-department")
IRRIGATION = ("City of Minneola — Irrigation Rules and Regulations", "https://www.minneola.us/utility-customer-service/pages/irrigation-rules-and-regulations")
LAKE_PA = ("Lake County Property Appraiser — parcel search", "https://www.lakecopropappr.com/")
LAKE_PERMIT = "/laws/permits/lake-county/"
ASTATULA_OSD = ("USDA NRCS — official series description, Astatula series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/A/ASTATULA.html")
CANDLER_OSD = ("USDA NRCS — official series description, Candler series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/C/CANDLER.html")
HILLS_CDD = ("Hills of Minneola Community Development District — About the District", "https://hillsofminneolacdd.net/about")
FOUNDERS_CDD = ("Founders Ridge Community Development District", "https://foundersridgecdd.com/")
GROWTHSPOTTER = ("GrowthSpotter, December 11, 2024 — Hills of Minneola industrial park", "https://www.growthspotter.com/2024/12/11/hills-of-minneola-developers-prep-for-construction-of-new-industrial-park/")
WIKI_MINNEOLA = ("Wikipedia — Minneola, Florida", "https://en.wikipedia.org/wiki/Minneola,_Florida")
TRAILHEAD = ("City of Minneola — Facilities & Parks", "https://www.minneola.us/recreation/pages/facilities-parks")
CENSUS = ("U.S. Census Bureau — QuickFacts, Minneola city, Florida", "https://www.census.gov/quickfacts/fact/table/minneolacityflorida")

SRC = [BUILDING, IRRIGATION, LAKE_PA, ASTATULA_OSD, CANDLER_OSD, HILLS_CDD, FOUNDERS_CDD, GROWTHSPOTTER,
       WIKI_MINNEOLA, TRAILHEAD, CENSUS, "dep-rule", "fs125572", "fs7203045"]

HUB = page(
    "/areas/minneola/", "city",
    "Artificial Turf Installation in Minneola, FL (2026)",
    "Artificial grass for Minneola's fast-growing subdivisions near the Turnpike interchange, with Lake County permit and water facts checked September 2026.",
    "Turf for a Turnpike-interchange town that's still filling in",
    capsule(f"We install, repair and clean artificial turf around Minneola, about 28 miles from Kissimmee. The going Central Florida figure, {price('residential')} a square foot as of September 2026, holds here too. Minneola is the fastest-growing town we cover: new subdivisions, new CDDs and new streets keep landing on the same ridge sand, and a job here is as often about a two-year-old lawn as a decades-old one."),
    "".join([
        sec("A city built around an interchange it didn't used to have",
            f"<p>Minneola's population went from 5,435 at the 2000 Census to 13,843 in 2020, and it's kept climbing since ({ext(CENSUS[1], 'Census QuickFacts')}). Most of that growth traces back to Florida's Turnpike's Hancock Road interchange, which opened land east of the highway to development that used to be out of easy commuting reach of Orlando. {ext(GROWTHSPOTTER[1], 'The Hills of Minneola')}, a roughly 1,900-acre project straddling the Turnpike there, is the biggest single piece of that growth, with nearly 4,000 homes planned across single-family neighborhoods, apartments and a Del Webb active-adult section.</p>"
            + "<p>What that means for a turf job: a much larger share of our Minneola calls involve a lawn that's two or three years old and never took, rather than an established yard that's finally worn out. Builder sod on freshly graded ridge sand dries out fast, and by the time a homeowner calls us the grass has usually already thinned past saving.</p>"),
        sec("Two CDDs, a building department run by contract, and no city permit page on our site",
            f"<p>Minneola has two active community development districts, the older {ext(FOUNDERS_CDD[1], 'Founders Ridge CDD')} and the newer {ext(HILLS_CDD[1], 'Hills of Minneola CDD')}, which covers about 885 acres east of the Turnpike and south of Sugarloaf Mountain Road. Neither district reviews building permits; that's the city's own {ext(BUILDING[1], 'Building Department')}, staffed through a contract with a third-party provider, reachable at (352) 394-3598 ext. 180 from a City Hall address at 800 N. US Highway 27. Unlike neighboring Clermont, Minneola's forms are downloadable PDFs submitted at the counter or by email rather than filed through a self-service online portal, at least as of what's published.</p>"
            + f"<p>A specific question about how Minneola treats synthetic turf belongs with that office, not with us; the dedicated rules page on our own site covers {a(LAKE_PERMIT, 'the unincorporated county')} rather than any single city's code. {a('/laws/florida-hb-683/', 'the new state turf standard')} still sets a floor the city can't write around on a covered single-family lot.</p>"),
        table("Minneola yard types and what we do differently",
              ["Lot type", "Part of town", "How we build it differently"],
              [["New construction east of the Turnpike", "Hills of Minneola and Founders Ridge streets", "Strip thin builder sod fast and cap fresh irrigation heads before the base goes in"],
               ["Older in-town lots near the lake", "Blocks close to downtown and Lake Minneola", "10-ft waterbody setback, and check for a seawall before assuming the buffer"],
               ["Del Webb active-adult section", "Smaller lots inside the Hills of Minneola plan", "Tighter turf areas, less excavation, a quicker single-day install"],
               ["Ridge-sand lots west of downtown", "Older streets toward Clermont's boundary", "Fast-draining Candler sand, but the crushed-rock base still goes in either way"],
               ["Lots near active construction", "Streets still being built out near Hancock Road", "Check existing grade before building the base rather than assuming even compaction"]],
              "Prices don't change by subdivision; what changes is how fresh the ground under the turf still is."),
        sec("A downtown on the lake, still SJRWMD despite the county's Green Swamp corner",
            f"<p>Minneola runs its own water utility, and {ext(IRRIGATION[1], 'the city irrigation ordinance')}, in force since 2009, implements the St. Johns River Water Management District's landscape rule directly rather than a schedule the city wrote on its own. The two-day cycle runs by address parity during daylight saving months, odd-numbered homes on Wednesdays and Saturdays and even-numbered ones on Thursdays and Sundays, with a blanket ban on any watering between 10 a.m. and 4 p.m. Lake County as a whole isn't entirely St. Johns territory, since a slice near Clermont and Groveland sits inside the Southwest Florida district's Green Swamp area, but Minneola's own ordinance points to St. Johns specifically, which is worth knowing if a homeowner has read otherwise about this stretch of the county.</p>"
            + "<p>None of that schedule reaches a synthetic lawn once the heads underneath it are capped, which the state's turf rule requires on its own regardless of which water district a given address answers to.</p>"),
        sec("Lake Minneola's shoreline and the ridge sand under everything else",
            f"<p>Downtown Minneola sits directly on Lake Minneola's north shore, once known as Cow House Lake before an early surveyor renamed it, and the state's buffer for that shoreline is the same ten feet it is everywhere else, waived only on a lot where a seawall or bulkhead is doing the work instead. Away from the water, the ridge underneath the city is {ext(CANDLER_OSD[1], 'Candler sand')}, excessively drained and rapid to very rapidly permeable, with {ext(ASTATULA_OSD[1], 'Astatula sand')} showing up on the steeper stretches nearby.</p>"
            + "<p>That fast-draining ground is a fair-weather advantage for new construction: it rarely holds standing water the way flatter Osceola County soil does, but it also means a shallow, rushed base won't announce itself with a puddle the way it would elsewhere. The base still gets built to the state's washed, open-graded spec regardless of how well the sand underneath drains on its own.</p>"),
        sec("Picking an installer while the town is still being built",
            "<p>A homeowner moving into a brand-new Minneola subdivision often asks some version of \"who's the best artificial turf company near Minneola for a yard that's only a year or two old?\" The honest answer is: whoever asks what the builder actually put down before quoting a fix, since a thin layer of sod over unamended fill needs full removal, not a patch job laid on top of a lawn that never established in the first place.</p>"
            + f"<p>Trailhead Park, one of the city's newer facilities, gives a sense of how fast Minneola is filling out its own public amenities alongside the private subdivisions; {ext(TRAILHEAD[1], 'the city parks listing')} lists walking trails, a skate park and a playground that didn't exist a decade ago, on land that was likely still citrus grove or open ridge before then.</p>"),
        "<!--AUTO:city-services-->",
    ]),
    faqs=[
        faq("Does Minneola have its own synthetic-turf rule?", "Not that's published anywhere we could find. The Building Department, at (352) 394-3598 ext. 180, is the office with a real answer for a specific address; our own site's dedicated coverage stops at the unincorporated county's rules."),
        faq("Is Minneola in the St. Johns or the Southwest Florida water district?", "Minneola's own irrigation ordinance implements the St. Johns River Water Management District's landscape rule directly, on the same schedule as Clermont's. A different, small slice of Lake County closer to Clermont and Groveland sits inside the Southwest Florida district's Green Swamp area instead."),
        faq("Why do so many Minneola turf calls involve a lawn under three years old?", "New construction east of the Turnpike, in Hills of Minneola and Founders Ridge, has been adding streets faster than most towns we cover, and builder-grade sod on freshly graded ridge sand often doesn't survive its first Florida summer without heavy irrigation."),
        faq("Do the Hills of Minneola or Founders Ridge CDDs review landscaping?", "A community development district under Florida law handles infrastructure like roads, stormwater and amenities, not architectural review; a homeowners association inside either development, if one exists for a given section, is the body that reviews a yard change."),
        faq("Can I apply for a Minneola building permit online?", "As of what the city has published, applications are downloadable PDF forms submitted at the counter or by email rather than through a self-service web portal, unlike neighboring Clermont's online system."),
    ],
    sources=SRC, city=SLUG, crumbs=[("Service areas", "/areas/")], crumb="Minneola",
    related=[("/areas/lake-county/", "Artificial turf across Lake County"), (LAKE_PERMIT, "Lake County permit rules (unincorporated)"),
             ("/areas/clermont/", "Artificial turf in Clermont"), ("/areas/montverde/", "Artificial turf in Montverde"),
             ("/artificial-turf-cost/", "Full turf cost guide")])

LOCAL = {
    "residential": {
        "title": "Artificial Grass Installation in Minneola, FL",
        "meta": "Artificial grass for Minneola's newest subdivisions near the Turnpike interchange, where builder sod often fails fast, priced as of September 2026.",
        "h1": "Turf for lawns that never quite got established",
        "lede": capsule(f"Installed artificial grass in Minneola runs {price('residential')} per square foot as of September 2026, the same range as everywhere else in Central Florida. A large share of the lawns we see here are only a year or two old, thin builder sod laid over freshly graded lots near the Turnpike interchange that never had a real chance to root before the first dry stretch hit it."),
        "sections": [
            ("Why so much of Minneola's turf work starts with a young lawn",
             f"<p>{svc('residential', 'A residential conversion')} elsewhere in Central Florida usually replaces grass that held on for a decade or more. A Minneola homeowner reaching out about turf is more often standing on a subdivision that broke ground within the last few years, where builder-grade sod went down over rough-graded fill and never built the root mass it needed before the first summer dry spell. Pulling that thin sod is faster than an older, thatched lawn, but the soil underneath often needs more attention, since construction traffic can leave it unevenly compacted in ways an older, settled yard doesn't have.</p>"
             + "<p>The state's washed, open-graded crushed rock base goes in the same way regardless of how new the lot is; what changes is how carefully the crew checks the existing grade first; skipping that check on a still-settling new-construction lot is how a flat-looking yard turns into an uneven one within a year.</p>"),
            ("Hills of Minneola, Founders Ridge and what a CDD does and doesn't cover",
             f"<p>A lot inside {ext(FOUNDERS_CDD[1], 'Founders Ridge')} or {ext(HILLS_CDD[1], 'Hills of Minneola')} sits inside a community development district, which under Florida law funds and maintains shared infrastructure, roads, stormwater ponds, entry features, not private landscaping. Turf review, where a section has an active homeowners association, runs through that association separately, and {a('/laws/hoa-rules/', 'the state turf-visibility statute')} still limits any such review to what a street or a neighbor can actually see.</p>"
             + f"<p>Minneola's {ext(BUILDING[1], 'Building Department')} handles the city permit side at (352) 394-3598 ext. 180, out of City Hall at 800 N. US Highway 27.</p>"),
            ("Candler sand under a growing town",
             f"<p>{ext(CANDLER_OSD[1], 'Candler sand')}, the series under most of Minneola's ridge, drains so fast that standing water after a storm is rarely the problem a new lawn runs into here. Erosion during construction is more common: a newly graded lot can shed loose sand off a bare slope before turf or even sod gets a chance to hold it down, and a base built on top of that eroded grade needs to be re-leveled rather than laid straight over the low spots.</p>"
             + f"<p>None of that changes the published price range. It changes how much time a crew spends checking and correcting grade before the base itself goes in, which on a newer lot can be more of the job than the installation that follows it; {post('base-under-artificial-turf-florida-sandy-soil', 'the base recipe for Central Florida sand')} is the same one applied a little more carefully here.</p>"),
        ],
        "scenario": ("Say your two-year-old sod already died on a 1,000 sq ft new-construction lot",
                     f"<p>A 1,000 sq ft backyard behind a home finished within the last two years, where the original builder sod has thinned to bare dirt in most spots, runs {price('residential')} a square foot, or $8,000 to $18,000 depending on the turf chosen. Because the lot is still relatively new, the crew spends extra time checking the existing grade for uneven settling from construction before building the base, rather than assuming a flat, stable start the way an older lawn usually allows.</p>"
                     + "<p>Capping whatever irrigation heads the builder installed happens early in that process, since a newer system is sometimes still under a builder or manufacturer warranty worth checking before anything gets cut or capped.</p>"),
        "faqs": [
            faq("Why did my brand-new Minneola sod die so fast?", "Builder-grade sod laid over freshly graded ridge sand often doesn't build enough root mass before the first hot, dry stretch, especially on a lot where in-ground irrigation hasn't been dialed in yet. It's a common enough pattern in newer Minneola subdivisions that we plan for it rather than treat it as unusual."),
            faq("Does a Minneola CDD need to approve a turf conversion?", "No. A community development district funds shared infrastructure, not private landscaping decisions. A homeowners association within that district's boundary, if one exists for a given section, is the body that reviews a yard change, not the CDD itself."),
            faq("Is new-construction sod failure common in nearby Lake County towns too?", f"Yes, wherever building has moved fastest. {city('clermont', 'Clermont')} sees some of it on its newer ridge streets, and {city('groveland', 'Groveland')} has similar new subdivisions, though Minneola's pace of construction is the fastest of the three right now."),
        ],
        "sources": SRC,
    },
    "pet": {
        "title": "Pet Turf & Dog Runs in Minneola, FL",
        "meta": "Dog-run turf for Minneola's new-construction yards and lakeside lots, sized for zero-lot-line subdivisions near the Turnpike, checked September 2026.",
        "h1": "Dog turf for a town of small, brand-new backyards",
        "lede": capsule(f"Pet turf in Minneola runs {price('pet')} per square foot as of September 2026. New subdivisions here tend to carry smaller, zero-lot-line yards than an older Lake County lot, and a dog on fresh sod over unsettled fill wears a bare patch faster than one on an established lawn ever would."),
        "sections": [
            ("A small new-construction yard wears out fast under a dog",
             "<p>A newer Minneola lot often leaves less open yard than an older subdivision does, once the pool cage or covered lanai and the required setbacks are subtracted, and a dog confined to that smaller footprint concentrates its wear into a tighter space. Combine that with sod that never fully rooted in the first place, and a bare, muddy strip along the fence line can show up within months of move-in rather than years.</p>"
             + "<p>Turf sized to that same footprint solves the wear question directly, and because the lot's base is often still freshly graded, tying the pet area's base into the same grading pass as the rest of the yard, rather than treating it as a separate patch, keeps the whole project on one schedule.</p>"),
            ("Odor control on sand that drains almost immediately",
             f"<p>{ext(CANDLER_OSD[1], 'The ridge sand')} under most of Minneola drains fast enough that a rinse disappears into the ground within seconds rather than sitting on the surface, which sounds like an advantage for pet odor and mostly is. The trade-off is that infill needs to actually trap ammonia rather than rely on drainage speed alone to carry it away, so zeolite or an antimicrobial coated sand earns its keep here the same way it would on slower-draining soil, just for a different reason.</p>"
             + f"<p>A weed barrier still gets skipped under a dog run regardless of how fast the sand drains, since trapped moisture at the surface is what causes odor, not moisture that's already passed through. {post('pet-turf-vs-regular-artificial-grass', 'what actually separates a pet product from a standard lawn turf')} is worth reading before assuming any turf works fine for a dog.</p>"),
            ("Keeping a dog run back from Lake Minneola's shoreline",
             f"<p>A lot near downtown Minneola or along the lake's edge carries the same 10-foot waterbody setback as anywhere else in Florida, seawall exception included, and a dog run built right up to the water invites exactly the kind of repeated bank erosion the setback exists to prevent. Placing the run further up the yard, away from the shoreline, keeps a dog that likes to explore water access at a safer distance from the lake at the same time it satisfies the setback.</p>"
             + f"<p>{city('clermont', 'Clermont')} and {city('montverde', 'Montverde')} both carry similar lakefront setback questions on their own turf, if a homeowner is comparing options across more than one South Lake town.</p>"),
        ],
        "scenario": ("Say you have a 180 sq ft strip along a zero-lot-line side yard",
                     f"<p>A 180 sq ft dog run along a narrow side yard in a newer Minneola subdivision, at {price('pet')} a square foot, runs $1,800 to $3,240, with zeolite infill pushing that toward the higher end. Because the lot is recently graded, the base for that strip usually ties directly into whatever leveling the rest of the new construction already needed, which can shave a little labor off what the same size run would take on an older, unevenly settled yard.</p>"
                     + "<p>A flush-out zone near the gate is worth planning into a tight zero-lot-line layout from the start, since there's less spare room to relocate one later than on a wider, older lot.</p>"),
        "faqs": [
            faq("Are Minneola's new-construction yards big enough for a real dog run?", "Most are, even with a smaller footprint than an older subdivision's lot. Sizing the run to fit the available side or rear yard, rather than assuming a standard size, is the more useful starting question."),
            faq("Does fast-draining ridge sand mean pet turf needs less infill in Minneola?", "No. Infill quantity is set by weight needed to hold the backing down and support the fiber, not by how fast the ground underneath drains; a fast-draining base changes how quickly a rinse disappears, not how much infill the job calls for."),
            faq("Do smaller, newer lots show up in Mascotte too?", f"To a lesser degree. {city('mascotte', 'Mascotte')} hasn't grown as fast as the Turnpike-interchange side of Minneola, so a tight zero-lot-line dog run comes up less often there than it does here."),
        ],
        "sources": SRC,
    },
    "putting": {
        "title": "Backyard Putting Greens in Minneola, FL",
        "meta": "Compact backyard putting greens for Minneola's tighter new-construction lots and Del Webb section, with the market range checked September 2026.",
        "h1": "Putting greens sized for a smaller, newer Minneola lot",
        "lede": capsule(f"Backyard putting greens in Minneola run {price('putting')} per square foot as of September 2026. Lots here tend to run tighter than an established Lake County subdivision, so a green usually gets designed to fit a smaller footprint from the start rather than carved out of an already generous yard."),
        "sections": [
            ("Designing small when the lot itself is small",
             "<p>A putting green on a newer Minneola lot competes for space with a pool cage, a covered lanai and whatever setback the builder left, which usually leaves less open ground than an older, more established Lake County yard would. That constraint pushes the design toward a compact two- or three-cup layout with modest break, built to use every available foot rather than a sprawling green with room to spare.</p>"
             + "<p>A smaller footprint isn't a lesser build, though: the same firm, level pad goes under each cup and the same fringe transition finishes the edge, regardless of whether the green covers 200 square feet or 600.</p>"),
            ("A green that fits the Del Webb section's low-maintenance pitch",
             f"<p>The active-adult section inside {ext(HILLS_CDD[1], 'Hills of Minneola')} markets itself on low-maintenance living, and a small putting green fits that pitch better than a full lawn conversion does for a homeowner who wants a yard that doesn't demand much upkeep. A tighter lot there usually means less excavation and a shorter install than a green built into a full backyard elsewhere in town.</p>"
             + f"<p>{a('/laws/hoa-rules/', 'the same state HOA statute')} still only protects what a fence or a hedge actually screens from view, so a green visible from a common walking path in an age-restricted section can draw more design-review attention than one tucked entirely behind a privacy fence.</p>"),
            ("Building on ground that's still freshly graded",
             f"<p>A lot inside a still-growing section of town, closer to active construction near the Hancock Road interchange, sometimes carries fill that hasn't fully settled yet, which matters more for a putting green than a plain lawn since an uneven base shows up immediately in how a ball rolls. Checking compaction before shaping the green's contours avoids building break into the design that later turns out to be an unintentional dip from settling fill rather than an intended slope.</p>"
             + f"<p>{ext(CANDLER_OSD[1], 'Candler sand')} itself drains fast enough that water pooling under the green isn't the typical failure mode here; an unlevel base from unsettled fill is the more common one on a newer lot. {post('artificial-turf-glossary', 'A quick glossary of stimp, face weight and the rest of the terms')} helps when comparing two green quotes side by side.</p>"),
        ],
        "scenario": ("Say you have a 250 sq ft green fit into a Hills of Minneola backyard",
                     f"<p>A 250 sq ft green with a two-cup layout, sized to fit what's left of a newer Minneola backyard after the lanai and setbacks, runs {price('putting')} a square foot, landing between $3,500 and $7,500. Because the lot's grading is recent, the crew checks compaction across the footprint before shaping any break into the surface, adding a step an older, already-settled yard usually doesn't need.</p>"
                     + "<p>Fringe turf around the green's edge adds modestly to that total once it wraps the perimeter, worth factoring in when comparing the quote against the green's raw square footage alone.</p>"),
        "faqs": [
            faq("Is a putting green realistic on a small new-construction Minneola lot?", "Usually, at a compact size. A two- or three-cup design with modest contouring fits most newer lots once the pool cage and setbacks are accounted for, even where a full backyard lawn wouldn't leave much room to spare."),
            faq("Does the Del Webb section of Hills of Minneola allow putting greens?", "We haven't found a published design document naming synthetic greens specifically for that section. A design-review submittal with dimensions and a product sample is the standard packet a homeowners association there would likely expect."),
            faq("Would a compact green fit better in an older Clermont community instead?", f"Not necessarily better, just differently. {city('clermont', 'Clermont')} tends to have more room in an established golf-community backyard, while a Minneola green is more often shaped around a newer lot's tighter setbacks."),
        ],
        "sources": SRC,
    },
    "playground": {
        "title": "Playground Turf Installation in Minneola, FL",
        "meta": "Cushioned playground turf for Minneola's family-heavy new subdivisions, sized to fall height, with the Central Florida market range checked September 2026.",
        "h1": "Play surfaces for a town filling up with young families",
        "lede": capsule(f"Playground turf in Minneola runs {price('playground')} per square foot as of September 2026. Between Trailhead Park's own playground and skate park and the young families filling new subdivisions east of the Turnpike, a shock pad sized to the equipment's fall height comes up more often here than in an older, more settled Lake County town."),
        "sections": [
            ("A play area added while the rest of the yard is still new",
             "<p>A swing set or climbing structure in a newer Minneola backyard often goes in within the first year or two after move-in, while builder sod is still struggling or has already failed, which means the play area's base sometimes becomes the first real landscaping decision a family makes on the lot. Sizing the shock pad to the tallest piece of equipment's fall height works the same way it would anywhere else; what's different is that the surrounding yard's own base and grade may not be established yet either.</p>"
             + "<p>Building the play area's base correctly from the start, rather than as an afterthought once the rest of the yard gets addressed, avoids having to redo it later when a full lawn conversion catches up to the same footprint.</p>"),
            ("Trailhead Park as a sign of how fast the town is growing up",
             f"<p>{ext(TRAILHEAD[1], 'Trailhead Park, one of the newest city facilities,')} added a playground, a skate park, a BMX course and an outdoor fitness area on land that was likely open ridge not long ago, which tracks with a population that grew from 5,435 in 2000 to 13,843 by the 2020 Census. A public park that new is a reasonable signal that a lot of {svc('playground', 'backyard playground turf')} requests we get here come from families who moved in within the last few years rather than households replacing an aging play area.</p>"
             + "<p>None of that changes the build itself, but it does mean a shock-pad conversation in Minneola is more often a first installation than a replacement of something that's already there.</p>"),
            ("Heat and shade on a lot with young trees",
             "<p>A brand-new subdivision often hasn't grown its shade canopy yet, since builder-planted trees take years to reach a size that actually shelters a play area, and a play surface in full, unshaded sun reaches the same 120 to 150°F range any exposed Florida turf does. A hose rinse before an afternoon play session brings that down quickly, and until the yard's own trees mature, a shade sail or an awning over the play area is worth considering the way it might not be on an older, tree-shaded lot elsewhere in the county.</p>"
             + f"<p>A cooling or lighter-colored infill helps more on a lot without established shade than it does once nearby trees have grown in, which is worth weighing against the modest added cost on a newer build. {post('is-artificial-turf-safe-for-kids-pfas-lead', 'What actually goes into a play-area turf and infill spec')} is worth a read before choosing a product for a young family's yard.</p>"),
        ],
        "scenario": ("Say you have a 280 sq ft play area on a lot with no shade yet",
                     f"<p>A 280 sq ft play area for a swing set, sized for a newer Minneola backyard with young, not-yet-shading trees, runs {price('playground')} a square foot, landing between $2,800 and $7,000 depending on shock-pad thickness. Because the surrounding lot may still be settling, the crew checks the base's compaction across the whole footprint before locking in a final grade, the same step a putting green or a residential lawn nearby would need on the same newly graded ground.</p>"
                     + "<p>A cooling infill is worth the modest add here given the lack of mature shade, a cost that fades in relative importance once nearby trees grow enough to shelter the area on their own.</p>"),
        "faqs": [
            faq("Does a brand-new Minneola lot need anything extra under a play area?", "Mainly a compaction check. Freshly graded fill on a newer lot can settle unevenly, so confirming the base is stable before building the shock pad avoids a dip showing up under the equipment later."),
            faq("Is there a public playground in Minneola worth comparing a backyard design to?", "Trailhead Park's playground, skate park and BMX course are the city's newest recreation additions, though a backyard design isn't held to any public-park standard."),
            faq("Do families in Clermont or Montverde deal with the same unshaded new-build issue?", f"{city('clermont', 'Clermont')} sees it on its own newer ridge streets; {city('montverde', 'Montverde')}, being smaller and slower-growing, has it less often since fewer of its lots are freshly cleared."),
        ],
        "sources": SRC,
    },
    "pool": {
        "title": "Pool & Lanai Turf in Minneola, FL",
        "meta": "Turf around Minneola's new-construction pool cages and lanais, where fresh concrete and rapid-growth crews raise different quality questions, checked September 2026.",
        "h1": "Pool-deck turf for Minneola's newest screen enclosures",
        "lede": capsule(f"A pool enclosure prices at the {price('residential')} rate too, the same base and material scaled to a smaller footprint. What's different in Minneola is the age of the concrete underneath: most of the screened cages we see here went up within the last few years, and a deck that new hasn't been tested by a real summer storm season the way an older lanai has."),
        "sections": [
            ("Checking a new deck's slope before turf goes over it",
             "<p>An older pool deck has usually proven, one way or another, whether it sheds water correctly; a deck poured within the last year or two hasn't been tested by many storms yet. Fast-growth construction means a lot of concrete gets poured on tight schedules, and a deck that looks flat can still carry a subtle grading error that only shows up once turf and a drainage underlay are already down and water starts pooling in a corner.</p>"
             + "<p>Checking a new deck's actual slope before installing anything over it catches that kind of problem while it's still cheap to flag, rather than after the turf has to come back up to fix it.</p>"),
            ("A tight screen enclosure on a zero-lot-line lot",
             f"<p>Lot sizes in a newer Minneola subdivision tend to run tighter than an established Lake County community, and that shrinks the screened area around the pool right along with everything else on the property. Whatever sliver of concrete sits between the water and the mesh wall was never going to hold real grass anyway, shaded and walked on far too much for that, so the total job here is small in scope even though the price per foot matches a full backyard lawn.</p>"
             + f"<p>{a('/laws/hoa-rules/', 'HOA turf-visibility protections')} apply the same way here as anywhere else: work inside an existing screen enclosure rarely changes what's visible from the street, which usually simplifies any design-review step.</p>"),
            ("Heat inside a cage with limited established shade",
             "<p>A screen mesh cuts some direct sun but not all of it, and a lanai on a newer lot without mature landscaping nearby holds heat inside the enclosure the way any full-sun surface does. A hose rinse before pool time brings the surface down quickly, and until surrounding trees or structures cast more shade, that rinse habit matters more here than it will once the lot's landscaping catches up to the home itself.</p>"
             + f"<p>Glue-down edges around the enclosure's perimeter secure the turf to the concrete regardless of how new or old the deck is, since a poured pad never accepts a staked edge the way open ground does. {post('install-artificial-turf-over-concrete-pavers-or-grass', 'The general rules for gluing turf to concrete')} apply the same way to a brand-new pour as to an old one.</p>"),
        ],
        "scenario": ("Say a newly poured lanai deck needs its slope checked first",
                     f"<p>Before quoting a 220 sq ft enclosure on a home finished within the last two years, we check which direction the existing concrete actually sheds water, since passing a first inspection isn't the same as surviving a real summer storm. Once that's confirmed, the job itself prices like any other pool-area strip, glued down over a drainage underlay: near the top of the {price('residential')} range because of the tight screen-door access, landing around $3,500 to $4,000 for this footprint.</p>"
                     + "<p>Because the surrounding yard on a newer lot is often still under construction itself, scheduling the pool-area turf separately from a future full lawn conversion is common here, rather than doing both in one visit.</p>"),
        "faqs": [
            faq("Should a brand-new Minneola pool deck be checked before turf goes on it?", "Yes. A recently poured deck hasn't been tested by many storms yet, and confirming it actually sheds water the way it was designed to is worth doing before installing turf and a drainage underlay over it."),
            faq("Is pool-area turf a separate project from the rest of a new Minneola yard?", "Often, yes, since the surrounding lawn on a newer lot may still be under construction or not yet landscaped. Scheduling the pool enclosure on its own timeline is common rather than waiting for the whole yard to be ready."),
            faq("Is the same fresh-concrete check worth doing in Clermont or Groveland?", f"Only where the pool cage itself is new. Older established communities in {city('clermont', 'Clermont')} and {city('groveland', 'Groveland')} more often have decks that have already been through several storm seasons, which settles the drainage question on its own."),
        ],
        "sources": SRC,
    },
    "repair": {
        "title": "Turf Repair in Minneola, FL",
        "meta": "Turf repair for Minneola's newer installs, where builder-grade shortcuts and unsettled fill show up faster than they would on an established Lake County lawn.",
        "h1": "Fixing turf installed during Minneola's fastest growth years",
        "lede": capsule("Turf repair in Minneola is quoted after we see photos or visit the site, since a lifted edge, a settling low spot and a capped-irrigation mistake each need a different fix. A fair share of our repair calls here trace back to a rushed install on a still-settling new-construction lot rather than years of ordinary wear."),
        "sections": [
            ("When a fast-growth install cuts a corner",
             "<p>A town adding as many streets as Minneola has in the last few years attracts crews working on tight schedules, and a rushed job on freshly graded, not-yet-settled ground is where corners get cut most often: a single compaction pass instead of two, unwashed fill instead of the state's required washed crushed rock, or a seam bonded without giving the adhesive time to cure properly. None of those mistakes are visible on installation day; they show up months later as a soft spot, a lifted seam or a section that's pulled away from its anchoring.</p>"
             + f"<p>{svc('repair', 'A repair visit')} starts by pulling back the turf at the affected spot to see what's actually underneath, since a settling low spot on a newer lot can look identical on the surface to one caused by a completely different problem.</p>"),
            ("Irrigation heads that were never actually capped",
             f"<p>The state's turf rule requires capping any in-ground head that used to water an area before synthetic turf goes over it, and on a newer construction lot with a recently installed irrigation system, that step sometimes gets missed or done incompletely during a rushed original install. A soggy patch under turf that should drain fine is worth checking against the irrigation zone map before assuming it's a base or drainage problem, since a head that's still cycling on a timer underneath the turf is a common and easy-to-miss cause.</p>"
             + f"<p>{ext(IRRIGATION[1], 'The city irrigation ordinance')} bars watering that area from an in-ground system either way, so a head found still running under turf needs capping regardless of what triggered the original oversight.</p>"),
            ("Unsettled fill and what it does to a repair a year later",
             f"<p>{ext(CANDLER_OSD[1], 'Ridge sand')} drains fast enough that a repair issue in Minneola rarely shows up as standing water; it shows up as an uneven surface where fill under a newer lot kept settling after the turf was already down. That settling isn't a defect in the turf itself, but a base built too shallow or compacted too quickly on ground that hadn't finished moving yet will telegraph that settling to the surface faster than it would on an older, stable lot.</p>"
             + f"<p>Re-leveling that section means correcting the base underneath, not just adding more infill on top to mask a dip that will likely reappear. Whether a homeowner's policy or a builder's warranty covers any of that work is its own question; {post('does-homeowners-insurance-cover-artificial-turf', 'what a standard policy actually covers')} walks through the usual answer.</p>"),
        ],
        "scenario": ("Say a soggy 6 x 6 ft patch shows up on turf installed last year",
                     f"<p>A damp, slightly sunken 6 x 6 ft patch on an otherwise dry lawn, on turf installed within the past year on a newer Minneola lot, is worth checking against the property's irrigation zone map before anything else, since a head that was supposed to be capped but wasn't is a common enough cause on a recent new-construction install. A repair visit checks that possibility first, then looks at the base underneath if the irrigation system turns out to be fully capped after all.</p>"
                     + f"<p>Because the cause could be irrigation, base settling or a combination of both, we quote this kind of fix after {svc('repair', 'a site visit')} rather than over the phone.</p>"),
        "faqs": [
            faq("Why would a one-year-old Minneola lawn already need a repair?", "New construction here moves fast, and an installer working a tight schedule on freshly graded, still-settling ground is more likely to cut a corner on compaction or capping irrigation heads. Those shortcuts often don't show up until months after installation."),
            faq("Could an uncapped irrigation head be causing a soggy spot under my turf?", "It's common enough on a newer Minneola lot to check first. Comparing the wet spot's location against the property's irrigation zone map, before assuming a base or drainage problem, is a quick way to rule it in or out."),
            faq("Do repair calls in Clermont or Winter Garden trace back to the same cause?", f"Less often. {city('clermont', 'Clermont')} and {city('winter-garden', 'Winter Garden')} both have a larger share of established lawns, so a repair call there is more often ordinary wear than a shortcut from a still-settling new build."),
        ],
        "sources": SRC,
    },
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
