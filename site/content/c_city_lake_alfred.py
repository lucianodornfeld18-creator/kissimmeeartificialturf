# -*- coding: utf-8 -*-
"""Lake Alfred, FL (tier 2). Researched September 2026: City of Lake Alfred Building Permits
(Community Development) and Public Works/Utilities pages, the city's own watering-schedule notice,
the Southwest Florida Water Management District's 2026 Modified Phase III order, Polk County Water
Atlas lake records, Wikipedia's Chain of Lakes (Winter Haven) entry, the city's own "Beginnings"
history page, UF/IFAS Citrus Research and Education Center history, Mackay Gardens and Lakeside
Preserve (city page + Trust for Public Land), and USDA NRCS official series descriptions / regional
guidance for the Apopka and Candler soils. No city-specific synthetic-turf ordinance was found, so
permit questions route to the Polk County page."""
from _helpers import page, capsule, sec, table, faq, a, svc, city, county, cs, post, src, ext, price
from _cityservice import cityservice_pages

SLUG = "lake-alfred"

SRC = [
    "dep-rule", "fs125572",
    ("City of Lake Alfred — Building Permits (Community Development)", "https://www.mylakealfred.com/166/Building-Permits"),
    ("City of Lake Alfred — Public Works / Utilities", "https://www.mylakealfred.com/199/Public-Works-Utilities"),
    ("City of Lake Alfred — new watering schedule notice", "https://mylakealfred.com/m/newsflash/home/detail/268"),
    ("Southwest Florida Water Management District — District extends Modified Phase III water shortage (2026)", "https://www.swfwmd.state.fl.us/the-newsroom/2026/district-extends-modified-phase-iii-water-shortage"),
    ("Polk County Property Appraiser — parcel search", "https://www.polkflpa.gov/"),
    ("Polk County — Building Division permitting", "https://www.polkfl.gov/services/building/permitting/"),
    ("USDA NRCS — official series description, Apopka series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/A/APOPKA.html"),
    ("USDA NRCS — official series description, Candler series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/C/CANDLER.html"),
    ("USDA NRCS eFOTG — sandy ridge soils guide referencing the Lake Alfred Experiment Station (FSG G154XB111FL)", "https://efotg.sc.egov.usda.gov/references/Public/FL/FSG_MLRA_154XB111FL.pdf"),
    ("City of Lake Alfred — Beginnings (city history)", "https://www.mylakealfred.com/211/Beginnings"),
    ("Census Reporter — Lake Alfred, FL", "http://censusreporter.org/profiles/16000US1237525-lake-alfred-fl/"),
    ("City of Lake Alfred — Mackay Gardens and Lakeside Preserve", "https://www.mylakealfred.com/191/Mackay-Gardens-Lakeside-Preserve"),
    ("Trust for Public Land — historic Mackay Gardens preserved", "https://www.tpl.org/media-room/historic-mackay-gardens-preserved-fl"),
    ("UF/IFAS Citrus Research and Education Center — about us", "https://crec.ifas.ufl.edu/about-us/"),
    ("Polk County Water Atlas (USF) — Lake Rochelle", "https://polk.wateratlas.usf.edu/waterbodies/lakes/160476/lake-rochelle"),
    ("Polk County Water Atlas (USF) — Lake Haines", "https://polk.wateratlas.usf.edu/waterbodies/lakes/160416/lake-haines"),
    ("Wikipedia — Chain of Lakes (Winter Haven)", "https://en.wikipedia.org/wiki/Chain_of_Lakes_(Winter_Haven)"),
]

PERMITS_PAGE = ("/laws/permits/polk-county/", "Polk County permit rules for turf")
HOA_PAGE = ("/laws/hoa-rules/", "what a Florida HOA can and can't restrict")
HB683_PAGE = ("/laws/florida-hb-683/", "HB 683 and DEP Rule 62-308.100")

# ============================================================== hub
HUB = page(
    "/areas/lake-alfred/", "city",
    "Artificial Turf Installation in Lake Alfred, FL",
    "Artificial turf installers serving Lake Alfred, FL, about 24 miles from Kissimmee: building permits, SWFWMD's watering order and the lake-chain setback.",
    "Turf built for Lake Alfred's citrus ridge and lake chain",
    capsule(f"We install, repair and clean artificial turf across Lake Alfred, a small US-17/92 city about 24 miles from Kissimmee built on citrus ground and threaded with canal-linked lakes. A square foot of installed synthetic grass here costs {price('residential')}, matching what the rest of Polk County pays heading into fall. A ridge lot on old grove soil and a canal-front lot on the Winter Haven chain call for two different build plans."),
    "".join([
        sec("A city split between citrus ridge and lake chain",
            f"<p>Away from the water, Lake Alfred sits on a {ext('https://efotg.sc.egov.usda.gov/references/Public/FL/FSG_MLRA_154XB111FL.pdf', 'Candler-Apopka soil complex')} that a federal soil guide names specifically at the old Lake Alfred Experiment Station: Candler is excessively drained pure sand, while {ext('https://soilseries.sc.egov.usda.gov/OSD_Docs/A/APOPKA.html', 'Apopka')} is a loamier, well-drained cousin, moderately slowly permeable rather than fast-draining, on the same upland ridges and knolls. Toward the shoreline of Lake Rochelle, Lake Haines and Lake Alfred itself, the ground turns low and slow to drain the way lake-margin soil does across this part of Polk County. A base built for a former grove lot on the ridge rarely matches what a canal-front lot two streets away actually needs.</p>"),
        table("Lake Alfred yard types and what we do differently",
              ["Property type", "Local factor", "Build adjustment"],
              [["Canal or lakefront lot on the Winter Haven chain", "Ten feet of state-required clearance from the water, unless a seawall already exists", "Mark that clearance line before turf gets measured"],
               ["Ridge lot on former grove land", "Candler-Apopka complex, well to excessively drained", "Standard base depth; watch for old grove-row grading"],
               ["Small lot near the historic packing district", "Older, narrow parcel, slower-draining ground", "Careful hand-grading; little room to redirect a storm"],
               ["Newer subdivision toward Haines City on US 17-92", "Builder sod on a shallow irrigation zone", "Cap the existing heads rather than adding plumbing"],
               ["Lot near Mackay Gardens on Lake Rochelle", "Conservation land next door, shoreline habitat", "Keep grading and runoff on the residential side of the line"]],
              "Prices don't change by location in Lake Alfred; the base and grading plan do."),
        sec("Who reviews a turf permit in Lake Alfred",
            f"<p>Lake Alfred's own {ext('https://www.mylakealfred.com/166/Building-Permits', 'Community Development Department')} runs building permits through its Building Inspection Division, reachable at (863) 291-5748 out of 155 N. Lake Shore Way, with applications filed online through the state's Accela system rather than mailed in. As in any Florida city, an owner can also hire a licensed private provider for plan review or inspection instead of using the city's own reviewers, though nothing about that option is specific to Lake Alfred. We haven't found anything in the city's code naming synthetic turf directly, so it's the state standard, explained on the {a(*PERMITS_PAGE)}, that actually governs a lawn conversion here. Before assuming Lake Alfred is even the right office, run the address through the {ext('https://www.polkflpa.gov/', 'Polk County Property Appraiser')}, since a few edge-of-town parcels answer to the county instead. A homeowners association is a separate layer entirely: {a(*HB683_PAGE)} only reaches city and county rules, leaving a subdivision's own architectural review committee free to keep reviewing turf requests under its covenants, within the limits {a(*HOA_PAGE)} lays out.</p>"),
        sec("Water rules for a Lake Alfred address",
            f"<p>The city's own {ext('https://www.mylakealfred.com/199/Public-Works-Utilities', 'Public Works Department')} bills and manages Lake Alfred's water directly rather than buying it through the county, and since February 8, 2026 the city has posted the same {ext('https://www.swfwmd.state.fl.us/the-newsroom/2026/district-extends-modified-phase-iii-water-shortage', 'Southwest Florida Water Management District Modified Phase III')} restriction as the rest of the region: once a week, on a day set by the address, inside an 8 p.m.-to-4 a.m. window, running through October 1, 2026. Turf doesn't answer to that calendar at all once its heads are capped, since the state's own rule already keeps synthetic sections off in-ground irrigation regardless of the season or any shortage order.</p>"),
        sec("Lakes, a preserve and a citrus research legacy",
            f"<p>Lake Rochelle, at 516 acres, connects by canal north to the 672-acre Lake Haines and south to Lake Conine, and both Rochelle and Haines belong to the {ext('https://en.wikipedia.org/wiki/Chain_of_Lakes_(Winter_Haven)', 'Winter Haven Northern Chain of Lakes')}, ten canal-linked lakes spanning Winter Haven, Lake Alfred and Lake Hamilton; the paved Chain of Lakes Trail follows part of that same water out to {city('winter-haven')}. On Rochelle's shore, the 112-acre {ext('https://www.mylakealfred.com/191/Mackay-Gardens-Lakeside-Preserve', 'Mackay Gardens and Lakeside Preserve')} protects nearly a mile of lakefront around a 1915 Craftsman estate. Lake Alfred also hosts the University of Florida's Citrus Research and Education Center, founded in 1917 on land Polk County growers helped buy, a reminder that the ground under a lot here was citrus country before it was a subdivision.</p>"),
        "<!--AUTO:city-services-->",
    ]),
    faqs=[
        faq("Does Lake Alfred have its own artificial turf ordinance?",
            f"No section of the city's code addresses synthetic turf specifically as of this fall. The Community Development Department (863-291-5748) handles building permits generally, and the state's May 2026 standard governs a covered residential lawn here rather than a city-specific rule; the {a(*PERMITS_PAGE)} explains what that standard covers."),
        faq("What is Lake Alfred's current watering schedule, and does it affect turf?",
            "One day a week, assigned by address, from February 2026 through October 1, 2026, under the regional water shortage order. Turf that's had its irrigation heads capped drops off that schedule entirely, since the state's rule already bars watering synthetic sections through an in-ground system."),
        faq("Does a canal-front lot on the Winter Haven chain need extra clearance for turf?",
            "Yes. Absent a seawall or bulkhead already standing between the lot and the water, turf has to stay ten feet off the lake or canal edge, the same way on Lake Haines, Lake Rochelle or Lake Alfred itself, and on the canals connecting them."),
        faq("Is the ground near the old citrus research station different from the rest of Lake Alfred?",
            "It can be. The ridge ground a federal soil guide associates with the old Lake Alfred Experiment Station is a Candler-Apopka complex, generally well to excessively drained, while lots closer to Rochelle, Haines or Lake Alfred's own shoreline sit on slower, lower ground typical of a Polk County lake margin."),
        faq("What should the best turf installer near you in Lake Alfred check before quoting a canal-front lot?",
            "Whether the yard actually touches the Winter Haven chain or just sits nearby, since the ten-foot setback and its seawall exception only matter on a true waterfront parcel. A contractor who skips that question before pricing the job is worth a second call."),
    ],
    sources=SRC, city=SLUG,
    crumbs=[("Service areas", "/areas/")], crumb="Lake Alfred",
    related=[("/areas/polk-county/", "Turf across Polk County"), ("/laws/permits/polk-county/", "Polk County permit rules for turf"),
             ("/areas/auburndale/", "Turf in Auburndale"), ("/areas/winter-haven/", "Turf in Winter Haven"),
             ("/artificial-turf-cost/", "Turf cost tables for Central Florida")],
)

# ============================================================== local
LOCAL = {
    "residential": {
        "title": "Artificial Grass Installation in Lake Alfred, FL",
        "meta": "Lake Alfred artificial grass installers building on former citrus ridge ground and small historic lots near downtown, priced like the rest of Polk County.",
        "h1": "Artificial grass for Lake Alfred's grove lots and old town core",
        "lede": capsule(f"Installed artificial grass in Lake Alfred runs {price('residential')} a square foot, the same Polk County range that's held all year. A former-grove lot on the ridge drains fast through its Candler-Apopka sand, while a small lot near the old citrus packing district downtown sits on slower ground and gives a crew far less yard to work with."),
        "sections": [
            ("Building on former grove ground",
             f"<p>Plenty of Lake Alfred's residential lots were citrus grove before they were subdivided, and the {ext('https://soilseries.sc.egov.usda.gov/OSD_Docs/A/APOPKA.html', 'Apopka soil')} common on that ridge ground is well drained and loamier than the pure sand found elsewhere in the county, moderately slowly permeable rather than fast-draining. That's a small but real difference for base planning: a lift of washed crushed rock still goes down at the same two-to-four-inch depth, but the native ground underneath holds a touch more moisture after a storm than excessively drained Candler sand does a few miles away, so grading the fall away from the house gets checked carefully rather than assumed from the lot's overall slope. None of that changes how deep the base goes, only how closely the crew watches compaction on the way down.</p>"),
            ("Small lots near the old packing district",
             f"<p>Close to downtown and the historic citrus packing buildings along the rail corridor, Lake Alfred's oldest residential lots run narrow, often with a home sitting close to both the front and side property lines, not unlike the tight gaps covered in our post on {post('artificial-grass-for-shady-side-yards', 'converting a shady side yard')}. A full lawn conversion on one of these parcels is usually a modest square footage, and the bigger design question is fitting an edge treatment, nailed border or paver strip, into a yard with little room between the house and the fence line. Newer subdivisions built out toward {city('haines-city', 'Haines City')} along US 17-92 don't share that constraint, giving a crew a more open, straightforward lawn to grade.</p>"),
            ("What Lake Alfred's Community Development Department expects",
             f"<p>Lake Alfred's Building Inspection Division processes permits through the state's Accela system, and nothing in the city's published code calls out synthetic turf on its own, so a lawn conversion generally moves through whatever review a project's actual scope requires, often centered on capping irrigation heads that a converted section no longer uses. That capping step matters locally too, since the city's Public Works Department currently limits every address to one watering day a week, a schedule a capped turf section simply exits once the state's rule takes over. A homeowner keeping part of the yard in sod near {svc('residential', 'a residential turf conversion')} should mention that split scope when calling the department.</p>"),
        ],
        "scenario": ("A small lot near downtown converts its front yard",
                     f"<p>A 1950s home two blocks from the old packing district has a 540 sq ft front yard, patchy St. Augustine that struggles in the narrow strip between the porch and the sidewalk. At {price('residential')} installed, that yard runs roughly $4,320 to $9,720, with most small in-town lots like this one landing in the {price('residential', typical=True)} typical band, about $5,400 to $8,640. Given how little side-yard room this lot has, the crew nails the border tight along both property lines and grades the short fall toward the sidewalk's existing storm inlet rather than trying to redirect water toward a back corner that doesn't exist on a lot this narrow.</p>"),
        "faqs": [
            faq("Is grove-land soil harder to build a lawn base on in Lake Alfred?",
                "Not harder, just slightly different. Apopka soil on the old ridge ground holds a little more moisture after rain than pure Candler sand does, so the crew pays closer attention to grading the fall away from the house rather than assuming the lot drains itself the way faster ridge sand elsewhere in the county would."),
            faq("Who handles a residential turf permit question in Lake Alfred?",
                f"The Community Development Department's Building Inspection Division, at (863) 291-5748, since nothing in the city's code addresses synthetic turf on its own. Whichever office ends up reviewing the paperwork, the {a(*PERMITS_PAGE)} is what actually spells out the standard the job has to meet."),
        ],
        "sources": SRC,
    },
    "pet": {
        "title": "Pet Turf & Dog Runs in Lake Alfred, FL",
        "meta": "Pet turf for Lake Alfred yards on the Winter Haven chain of lakes and near Mackay Gardens, with the state's waterbody setback and local rinse rules explained.",
        "h1": "Dog turf and runs for Lake Alfred's canal and lake lots",
        "lede": capsule(f"Pet turf in Lake Alfred installs at {price('pet')} a square foot, holding at the same range as the rest of Central Florida. A dog run on a canal or lake lot along the Winter Haven chain has to respect the state's 10-foot waterbody setback, while a run inland near Mackay Gardens is mostly about drainage toward the preserve's protected shoreline instead."),
        "sections": [
            ("Dog runs on the canal and chain-of-lakes lots",
             f"<p>A backyard on Lake Haines, Lake Rochelle or one of the canals connecting them to the wider {ext('https://en.wikipedia.org/wiki/Chain_of_Lakes_(Winter_Haven)', 'Winter Haven chain')} has to keep any new turf, including a dog run, a state-required ten feet off the water's edge, unless a seawall or bulkhead is already doing that job. Grading direction matters as much as the buffer line itself: a run that slopes toward the canal instead of toward the street risks carrying infill into the water during a hard rain, which the state's material rule doesn't allow regardless of how far back the run actually sits. Checking which way the yard actually falls, rather than assuming it slopes toward the street the way most lots do, is worth doing before the run gets staked.</p>"),
            ("Yards near Mackay Gardens and Lakeside Preserve",
             f"<p>Homes near the {ext('https://www.mylakealfred.com/191/Mackay-Gardens-Lakeside-Preserve', '112-acre Mackay Gardens and Lakeside Preserve')} sit close to a stretch of protected shoreline and habitat for wading and migratory birds, which is worth factoring into a dog run's layout even without a specific rule attached to the neighborhood. Keeping a run's drainage and infill on the residential side of any shared boundary, rather than assuming the preserve absorbs runoff, avoids sending sand or debris toward ground the city has spent effort protecting. The preserve's 1.1-mile trail and its stretch of shoreline draw a steady run of walkers, a fair share of them with a dog on leash, so a run built near that boundary is also one other dogs and owners pass on a regular basis, which is one more reason to keep the fence line snug and the grading tidy rather than an afterthought.</p>"),
            ("Rinsing instead of watering under the city's own schedule",
             f"<p>Lake Alfred's Public Works Department currently holds every address to one irrigation day a week, but a dog run gets rinsed by hose on whatever day it actually needs it, since the state's rule already keeps a capped synthetic section off the sprinkler system entirely, the same point our post on {post('how-to-get-dog-urine-smell-out-of-artificial-turf', 'clearing dog odor from artificial turf')} covers in more depth. That's a real advantage for a household managing dog odor and heat in the same yard where the remaining sod is stuck on a single watering day, since the run itself never has to wait for its turn on the calendar the way the rest of the yard still does.</p>"),
        ],
        "scenario": ("A canal-lot household adds a dog run",
                     f"<p>A home backing onto a canal near Lake Haines has a fenced 300 sq ft side yard where two dogs have worn a bare track along the fence closest to the water. At {price('pet')} installed, that run costs roughly $3,000 to $5,400, with most jobs this size landing in the {price('pet', typical=True)} typical range, about $3,600 to $4,800. Since the fence sits well inside the ten-foot setback from the canal, the crew grades the run's low point back toward the house side of the yard instead of toward the water, keeping infill away from the canal bank entirely, a small layout choice that costs nothing extra at this size.</p>"),
        "faqs": [
            faq("Can I put a dog run right up to a canal bank in Lake Alfred?",
                "Only if a seawall or bulkhead is already doing that separating; otherwise the run stays ten feet off the canal bank, exactly like a full lawn would. Fencing the run right up to the bank doesn't change that distance, since the setback is measured from the water, not from where a homeowner would prefer the fence to sit."),
            faq("Does living near Mackay Gardens change how a pet run gets built?",
                "There's no special rule tied to the preserve itself, but grading a nearby run's drainage away from the shoreline and its habitat is good practice regardless, especially since the property protects nearly a mile of lake frontage next door."),
        ],
        "sources": SRC,
    },
    "putting": {
        "title": "Backyard Putting Greens in Lake Alfred, FL",
        "meta": "Backyard putting greens for Lake Alfred's larger former-grove lots, with notes on Candler-Apopka subgrade behavior and the Chain of Lakes Trail as local context.",
        "h1": "Putting greens on Lake Alfred's old citrus-ground lots",
        "lede": capsule(f"A backyard putting green in Lake Alfred installs at {price('putting')} a square foot, unchanged from the rest of the region this fall. Larger lots left over from the city's citrus-grove past give a green more room to work with than a canal lot does, and the loamier Apopka ground under some of that ridge land behaves a little differently under a green's subgrade than pure sand."),
        "sections": [
            ("Grove-scale lots leave room for a full layout",
             f"<p>Because a fair share of Lake Alfred's residential land was platted out of old citrus groves rather than built up in tight modern subdivisions, some lots here run larger than what a putting green project typically has to work with in denser towns like {city('davenport', 'Davenport')} or {city('polk-city', 'Polk City')}. That extra room supports a full green with a chipping approach and more than one cup location, rather than a compact practice pad squeezed into a standard backyard, and it's worth surveying the whole lot before assuming a green has to be small just because the house itself is modest. Our {post('artificial-turf-glossary', 'glossary of turf and putting-green terms')} is worth a skim before that first conversation about fringe, stimp and pile height.</p>"),
            ("How Apopka's loamier sand behaves under a green",
             f"<p>Where the ridge ground follows the {ext('https://soilseries.sc.egov.usda.gov/OSD_Docs/A/APOPKA.html', 'Apopka series')} rather than pure Candler sand, the subgrade under a putting green holds slightly more moisture after rain, being moderately slowly permeable instead of excessively drained. That doesn't change the base depth a green needs, but it does mean the crew checks compaction and drainage a bit more carefully than on faster-draining ground nearby, since a green's subtle contours show a soft spot in a way a flat residential lawn wouldn't. A green built for true roll also has less tolerance for that kind of hidden settling than an ordinary lawn does, so the extra compaction pass here is about keeping a putt honest years later, not just about the ground holding shape.</p>"),
            ("A recreation corridor running past Lake Alfred",
             f"<p>The paved Chain of Lakes Trail passes near Lake Alfred on its way between the city and {city('winter-haven', 'Winter Haven')}, part of a broader stretch of Polk County where walking, biking and lakeside recreation are already part of daily life. A backyard green fits that same pattern at home, and homeowners asking about one here are often the same households already using the trail or the lakes on weekends, looking for a low-upkeep way to practice without a drive to a course. A short chipping approach tacked onto the green scratches the same itch on a morning when the trail itself is busier than usual, and it costs nothing extra to build the two side by side.</p>"),
        ],
        "scenario": ("A former-grove lot adds a green with a chipping approach",
                     f"<p>A house on a half-acre former-grove lot has room for a 520 sq ft green with a short chipping approach, currently just mowed grass with a few dips left over from old citrus rows. At {price('putting')} installed, that project runs roughly $7,280 to $15,600, with most greens this size landing in the {price('putting', typical=True)} typical band, about $9,360 to $13,000. The crew shapes the subgrade to smooth out the old row dips into a couple of intentional breaks rather than grading everything flat, and checks compaction a little more closely given the loamier Apopka ground underneath, since a soft spot would show up in the roll long before it showed up anywhere else in the yard.</p>"),
        "faqs": [
            faq("Do larger Lake Alfred lots cost more per square foot for a putting green?",
                "No, the price per square foot holds the same regardless of lot size; a bigger property just means more usable space to design around, not a different rate. What changes is the design conversation, since a half-acre former-grove lot can support a full green with a chipping approach where a standard subdivision yard usually can't."),
            faq("Does Apopka soil need extra drainage work under a putting green?",
                "Not extra work, just closer attention during compaction, since it holds a bit more moisture than pure Candler sand without being poorly drained. The base itself is built the same way either soil sits underneath."),
        ],
        "sources": SRC,
    },
    "playground": {
        "title": "Playground Turf in Lake Alfred, FL",
        "meta": "Playground turf for Lake Alfred's newer subdivisions and shaded older lots near Mackay Gardens, covering heat, shade and the drip-line rule, current this fall.",
        "h1": "Playground turf for Lake Alfred's older and newer yards",
        "lede": capsule(f"Playground turf in Lake Alfred is priced at {price('playground')} a square foot installed, the same range Central Florida installers are quoting everywhere this fall. A new subdivision toward Haines City usually means full sun and no mature shade yet, while an older lot nearer downtown or Mackay Gardens often has legacy trees that bring the state's drip-line rule into play instead."),
        "sections": [
            ("Full-sun yards in the newer subdivisions",
             f"<p>Subdivisions built out toward {city('haines-city', 'Haines City')} along US 17-92 tend to be younger, with landscaping and shade trees still a decade or more from full size, which leaves a swing set or trampoline sitting in open sun most of the afternoon. Surface temperature on unshaded synthetic turf commonly reaches 120 to 150°F in full Florida summer sun, so a play area on one of these lots gets a lighter-colored fiber or a cooling infill built into the spec rather than relying on shade that isn't there yet, plus a hose rinse worked into the household's afternoon routine. Planting a fast-growing shade tree at the same time as the turf install is worth considering too, even though it won't help for a season or two.</p>"),
            ("Older lots with legacy shade near downtown",
             f"<p>Closer to Lake Alfred's historic core and toward Mackay Gardens, older lots often carry mature oaks or long-established citrus trees that throw real shade over a backyard, which helps with heat but brings the state's drip-line rule into the planning instead, and means more fall cleanup than a bare new-build yard, exactly what our post on {post('oak-leaves-and-debris-on-artificial-turf', 'oak leaves and debris on artificial turf')} walks through. Synthetic turf can't go inside a tree's drip line, on that property or a neighbor's, unless a certified arborist certifies the install won't cause harm, so a play area planned near one of these older trees needs that step scheduled before any digging starts, not treated as an afterthought.</p>"),
            ("A preserve next door as a family-recreation reference",
             f"<p>Families near {ext('https://www.mylakealfred.com/191/Mackay-Gardens-Lakeside-Preserve', 'Mackay Gardens and Lakeside Preserve')}, with its own pavilion and playground on 112 acres of lakefront, often want a similar cushioned surface at home under a smaller backyard play structure. A shock pad sized to the actual fall height of a home swing set or slide matters more for that comparison than infill color, since a public park's surface gets engineered to a specific safety standard that a backyard build should match rather than guess at. Asking a contractor for that fall-height number in writing, the way a county park spec sheet would list it, is a fair thing for a Lake Alfred parent to expect before equipment goes in the ground.</p>"),
        ],
        "scenario": ("A Haines City-corridor subdivision adds a play area",
                     f"<p>A family in a subdivision along US 17-92 wants a 300 sq ft play area under a new swing set, currently open sod in a yard with only a single young shade tree. At {price('playground')} installed, that area costs roughly $3,000 to $7,500, with most small residential play areas landing in the {price('playground', typical=True)} typical band, about $3,600 to $5,700. Given the lack of established shade, the crew specifies a lighter-colored fiber and confirms the pad thickness against the swing set's documented fall height before ordering material. The family plants a shade tree near the play area the same week, mostly for the yard a few summers from now rather than this one.</p>"),
        "faqs": [
            faq("Does a Lake Alfred play area near an old citrus tree need special approval?",
                "Only if the turf or equipment falls inside that tree's drip line; the state's rule requires a certified arborist to certify no harm before installing there, whether the tree is a live oak or a legacy citrus tree from the property's grove days."),
            faq("Why does a newer Lake Alfred subdivision need a different infill than an older shaded lot?",
                "Mainly heat. A full-sun yard in a newer subdivision benefits from a lighter-colored or cooling infill to manage surface temperature, while a shaded older lot near downtown has less of that problem and more of a drip-line question to answer instead."),
        ],
        "sources": SRC,
    },
    "pool": {
        "title": "Pool & Lanai Turf in Lake Alfred, FL",
        "meta": "Pool and lanai turf for Lake Alfred's canal-front cages and small historic lots, covering deck edges and the waterbody setback, priced this September.",
        "h1": "Pool and lanai turf for Lake Alfred's lake and in-town lots",
        "lede": capsule(f"Turf around a Lake Alfred pool prices from the same {price('residential')} range as a residential lawn, steady across Polk County this fall. A screen-cage lot on the Winter Haven chain has to keep any turf outside the cage clear of the state's lake setback, while an older in-town lot usually means a pool built close to the house with very little deck margin to work with."),
        "sections": [
            ("Pool cages on canal and lake lots",
             f"<p>A pool cage backing onto Lake Haines, Lake Rochelle or a connecting canal sits inside a yard where turf beyond the enclosure, not the pool or the cage itself, has to respect the state's ten-foot waterbody setback unless a seawall already separates the property from the water. That layout comes up often enough on Lake Alfred's chain-of-lakes lots that staking the setback line is one of the first steps before pricing turf for the strip between the cage and the shoreline. Skipping that step and pricing off the fence line alone tends to produce a quote for more square footage than the yard can actually carry, which is a frustrating number to walk back once a homeowner has already mentally spent it.</p>"),
            ("Small in-town lots with little deck margin",
             f"<p>On Lake Alfred's older, smaller lots near downtown, a pool often sits close enough to the house that the turf around it amounts to a narrow strip rather than an open lawn, with the screen-track edge doing most of the visual work, the same edge-bonding question our post on {post('install-artificial-turf-over-concrete-pavers-or-grass', 'installing turf over concrete, pavers or existing grass')} covers in general. That edge bonds to the track with adhesive rather than nails, since there's no soil there to anchor into, and getting that narrow strip's grading right, sloped toward a drain rather than back toward the house, matters more on a tight lot than on a wide-open one, since there's no second chance to widen the strip once the deck and the fence line are both already fixed in place.</p>"),
            ("Apopka and Candler ground under a pool deck",
             "<p>Whether a pool sits on the ridge's Apopka-leaning soil or on flatter ground closer to a lake, the base under surrounding turf still runs the same washed-rock depth, graded away from the pool's overflow and the screen track alike. The loamier ridge soil holds a touch more moisture after rain than pure sand does, which is one more reason to check that grading carefully rather than assume the deck area drains itself the way it might on excessively drained ground elsewhere in the county. Neither soil changes what the deck edge itself needs, since that bond depends on the concrete underneath, not on whatever the native ground happens to be doing a few inches down.</p>"),
        ],
        "scenario": ("A canal-lot pool cage gets finished with turf",
                     f"<p>A home on a canal near the Winter Haven chain has a 440 sq ft pool cage with bare dirt around the deck, never landscaped since the screen enclosure went up. At the {price('residential')} residential range, that area runs roughly $3,520 to $7,920 installed; a straightforward deck like this one more often prices out near the {price('residential', typical=True)} typical band, closer to $4,400 or $7,040 than either extreme. Since the cage sits close to the canal bank, the crew confirms the ten-foot setback for any turf running past the enclosure toward the water before finalizing the layout, rather than pricing the full lot and adjusting afterward.</p>"),
        "faqs": [
            faq("Does the pool cage itself count toward Lake Alfred's lake setback?",
                "No, the setback applies to turf, not to the pool or the screen enclosure. It only becomes relevant if the same yard also has turf running from the cage toward the shoreline, which is common enough on a canal lot that it's worth asking about before the cage itself gets designed."),
            faq("What should the best pool turf contractor near me in Lake Alfred confirm on a canal lot?",
                "Whether any turf planned outside the screen cage falls within ten feet of the water, and whether a seawall already exists there, before pricing the job. Skipping that check is how a quote ends up needing revision after the setback gets discovered mid-project."),
        ],
        "sources": SRC,
    },
    "repair": {
        "title": "Turf Repair in Lake Alfred, FL",
        "meta": "Artificial turf repair in Lake Alfred for canal-lot infill loss, grove-lot edge lifting and old in-town driveway seams, quoted after photos or a site visit.",
        "h1": "Repairing artificial turf on Lake Alfred's lake and grove lots",
        "lede": capsule("Turf repair in Lake Alfred is quoted after photos or a site visit rather than a flat rate, since a shifted seam and a full re-anchor cost very differently to fix. Canal-front lots tend to show infill loss toward the water first, while older grove-turned-subdivision lots more often show edge lifting where the original perimeter was under-anchored."),
        "sections": [
            ("Infill drifting toward a canal or lake",
             f"<p>On a lot backing onto a canal or one of the lakes in the {ext('https://en.wikipedia.org/wiki/Chain_of_Lakes_(Winter_Haven)', 'Winter Haven chain')}, a common repair call is infill that's visibly thinned along the edge closest to the water, usually the result of a grade that slopes toward the shoreline instead of away from it. The state's material rule requires infill stay on the property, so the fix is rarely just adding more sand; regrading that edge so water moves toward a swale or the street instead of the canal bank is what actually stops the loss from repeating. Topping off infill without touching the grade usually buys only a season or two before the same thin spot reappears.</p>"),
            ("Edge lifting on former grove-land lots",
             "<p>Lots platted out of old citrus groves sometimes carry a slight grade left over from the original planting rows, and a perimeter edge that wasn't anchored with that grade in mind can lift at the low point after a season or two of heavy rain. That's usually a localized re-anchoring fix rather than a sign the whole lawn needs redoing, though it's worth checking the rest of the perimeter along the same low-lying stretch while a crew is already on site. A quick walk of the fence line after the next hard storm usually shows whether that low point is an isolated spot or part of a longer run that got missed the first time.</p>"),
            ("Driveway seams on Lake Alfred's older lots",
             f"<p>Near the historic downtown and the old packing district, older lots often have turf meeting a driveway or walkway with very little transition space, and that adhesive-bonded seam is one of the more frequent repair points on these smaller properties. A lifted strip right at that edge is typically a bonding issue specific to that one seam rather than evidence of a problem with the rest of the lawn, the kind of distinction our post on {post('what-does-artificial-turf-warranty-cover', 'what a turf warranty actually covers')} gets into before anyone assumes a manufacturer defect. Re-bonding that one seam, rather than pulling and relaying the whole driveway edge, is usually enough to settle it for good.</p>"),
        ],
        "scenario": ("Say you have infill thinning near a canal bank",
                     "<p>Say a canal-lot yard has about 50 sq ft of visibly thin infill along the fence closest to the water, with sand clearly having washed toward the bank after several heavy storms this year. That kind of repair is priced after a site visit, since the work is mostly regrading that stretch and topping off infill rather than replacing turf outright. Photos showing the thin section next to the canal, along with roughly how long it's been happening, help a crew scope the visit before showing up, and a quick look at where the fence sits relative to the water tells them most of what they need before they even arrive.</p>"),
        "faqs": [
            faq("Why does infill keep disappearing near my Lake Alfred canal lot?",
                "Almost always a grade issue: if that section of yard slopes toward the water, infill washes that direction during heavy rain regardless of infill type. Regrading the low point away from the canal, not switching infill, is what actually fixes it."),
            faq("Is a lifted edge on a former grove lot a sign the whole lawn is failing?",
                "Usually not. It's more often a localized anchoring problem where the old grove-row grade left a low spot the original perimeter wasn't secured for, and re-anchoring that one stretch typically resolves it. Checking the rest of the perimeter at the same visit is still worth doing, since the same grade issue sometimes shows up at more than one low point."),
        ],
        "sources": SRC,
    },
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
