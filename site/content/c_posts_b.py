# -*- coding: utf-8 -*-
"""Blog cluster: heat, pets, rain and base. Registered to c_posts_b in _posts.py.
Ten posts: how hot turf gets, coolest turf/infill, melting, dog urine odor, drainage in heavy rain,
hurricane/flood, base for sandy soil, lifespan, turf over concrete/pavers/grass, Toho watering vs. turf."""
from _helpers import page, capsule, sec, table, faq, ul, steps, note, cta, a, svc, post, src, ext

# ---------------------------------------------------------------- sources not already in _data.SOURCES
BYU = ("Brigham Young University News, the science behind the grass at LaVell Edwards Stadium",
       "https://news.byu.edu/news/science-behind-grass-lavell-edwards-stadium")
PSU = ("Act Global, summarizing Penn State Center for Sports Surface Research turf-temperature findings",
       "https://www.actglobal.com/turf-temperature-irrigation-penn-state/")
SOFFALL = ("Sof'Fall, how different playground surfaces respond to heat",
           "https://sof-fall.com/how-do-different-playground-surfaces-respond-to-heat/")
POLY = ("Wikipedia, polyethylene melting and softening temperature ranges",
        "https://en.wikipedia.org/wiki/Polyethylene")
NOAA14 = ("NOAA/NWS Precipitation Frequency Data Server, Atlas 14 point estimates near Kissimmee, FL",
          "https://hdsc.nws.noaa.gov/pfds/pfds_map_cont.html?bkmrk=fl")
OSD_MYAKKA = ("USDA NRCS Official Series Description, Myakka series (Florida's state soil)",
              "https://soilseries.sc.egov.usda.gov/OSD_Docs/M/MYAKKA.html")
OSD_SMYRNA = ("USDA NRCS Official Series Description, Smyrna series",
              "https://soilseries.sc.egov.usda.gov/OSD_Docs/S/SMYRNA.html")
OSD_IMMOKALEE = ("USDA NRCS Official Series Description, Immokalee series",
                  "https://soilseries.sc.egov.usda.gov/OSD_Docs/I/IMMOKALEE.html")
OSD_CANDLER = ("USDA NRCS Official Series Description, Candler series",
               "https://soilseries.sc.egov.usda.gov/OSD_Docs/C/CANDLER.html")
SFWMD = ("South Florida Water Management District, Year-Round Landscape Irrigation Rule (Ch. 40E-24, F.A.C.)",
         "https://www.sfwmd.gov/community-residents/landscape-irrigation")
IFAS_BAHIA = ("UF/IFAS Gardening Solutions, Bahiagrass",
              "https://gardeningsolutions.ifas.ufl.edu/plants/lawns/bahiagrass")


def xt(tup, text=None):
    return ext(tup[1], text or tup[0])


CRUMBS = [("Blog", "/blog/")]
PUB = "2026-09-21"


# ================================================================== 1
def p_heat():
    body = "".join([
        sec("How hot does turf get, hour by hour?",
            f"<p>Bare {svc('residential', 'artificial turf')} tracks close to the air early in the morning, climbs fast once direct sun hits it after about 10 a.m., and peaks between 1 and 4 p.m. On a still, cloudless Kissimmee afternoon in July or August, installers routinely read 120°F to 150°F at the surface, and a university field study has recorded synthetic turf above 195°F under similar heat ({xt(BYU, 'BYU field measurements')}). Cloud cover, wind and a lower sun angle in October or February knock 20 to 40 degrees off those numbers.</p>"
            "<p>The reading falls off quickly once the sun drops behind a roofline or a stand of oaks, usually within twenty or thirty minutes, because the turf layer itself is thin and has little mass to hold heat the way a slab of concrete does. A digital infrared thermometer, the same kind used to check a barbecue grate, is the easiest way to see the swing for yourself on any given afternoon.</p>"),
        sec("Surface temperatures by material, published measurements",
            table("Surface temperatures in full Florida summer sun (published studies, not our own readings)",
                  ["Material", "Typical reading", "Extreme reading", "Source"],
                  [["Artificial turf, full sun", "120–150°F", "Above 195°F on a hot, still afternoon", xt(BYU, "BYU field study")],
                   ["Artificial turf, full shade", "Close to the day's air temperature", "Rarely feels hot to bare skin", xt(PSU, "Penn State turf-temperature review")],
                   ["Concrete or pavers", "Above 120°F once air passes 90°F", "Not separately measured for pavers in published data", xt(SOFFALL, "Sof'Fall playground surface study")],
                   ["Sand", "Around 100°F when air is 75°F", "Burn risk once air passes 90°F", xt(SOFFALL, "Sof'Fall playground surface study")],
                   ["Natural grass", "Close to air temperature", "Rarely above 120°F even on the hottest days", xt(BYU, "BYU field study")]],
                  "These are published measurements from turf research and a playground-surfacing study, not readings we took on a specific yard. Instrument type, cloud cover and time of day change the number by 10 to 20 degrees between studies, so treat every row as a range.")),
        sec("Does a hose rinse actually cool it down?",
            f"<p>Yes, and quickly: spraying turf with a garden hose drops the surface temperature within a minute or two and keeps it comfortable for roughly an hour or two before the sun brings it back up ({src('magnolia-heat', 'a Florida installer field test')}). Florida's turf rule, in force since May 19, 2026, rules out an automatic fix: in-ground irrigation systems can't be used to water synthetic turf, so a scheduled sprinkler cycle isn't an option and the rinse has to be a hose someone turns on ({src('dep-rule', 'Rule 62-308.100, F.A.C.')}).</p>"
            f"<p>{post('coolest-artificial-grass-and-infill-for-florida', 'What actually lowers the temperature, beyond a rinse')} goes through color, blade shape and infill choices in more detail.</p>"),
        sec("What does this mean for kids and dogs on a hot afternoon?",
            f"<p>Treat {svc('playground', 'playground turf')} and pool-deck turf the way you'd treat a sandy beach path at midday: fine before 10 a.m. and after 5 p.m., worth a rinse and a look before letting bare feet or paw pads on it between noon and 4 p.m. Published playground-surfacing research notes that surfaces above roughly the concrete and sand readings in the table carry a real burn risk to skin in under a minute ({xt(SOFFALL, 'the Sof Fall playground heat findings')}). Shade sails, a rinse before playtime and scheduling active use for morning or evening cover most of the risk without changing the yard's design.</p>"),
        sec("Why do some yards run hotter than others?",
            ul(["<strong>Sun exposure.</strong> A west-facing lawn with no canopy runs hotter in the 2 to 5 p.m. window than an east-facing yard shaded by afternoon.",
                f"<strong>Nearby reflective surfaces.</strong> A low-E window or a mirrored fence panel can add a hot spot well above the ranges in the table; {post('can-artificial-turf-melt', 'reflected sunlight is what actually melts turf')}.",
                f"<strong>Color and infill.</strong> Blade color, pile height and infill type all shift the reading somewhat; {post('coolest-artificial-grass-and-infill-for-florida', 'the cooling options that hold up in Florida')} covers what's proven and what's marketing.",
                f"<strong>What's under it.</strong> Turf laid directly over {svc('pool', 'a pool deck or concrete patio')} reads closer to the concrete numbers above than turf laid over soil, because the slab holds heat longer after sunset."])
            + "<p>Say you have a full-sun pool-deck turf install in Hunters Creek, laid in a tan-green blend. On a 92°F August afternoon the surface could sit near 140–150°F by 2 p.m. and settle into the 90s within an hour of sunset. A hose rinse before the kids go out mid-afternoon brings it down enough to cross barefoot, though it climbs back within an hour or two in direct sun.</p>"
            + cta("Ask about shade and color options before you install", "We'll walk the lot at the time of day the yard sees the most sun.")),
        sec("Does the season change any of this in Osceola County?",
            "<p>Some. Dry season, roughly October through May, brings lower humidity and a lower sun angle, so a January afternoon rarely pushes turf past the 90s even in full exposure. Rainy season, June through September, adds near-daily afternoon storms that cool the surface for free most days, but the mornings and early afternoons before those storms roll in are the hottest stretch of the year, since high humidity traps heat close to the ground. A yard that never sees shade runs warm most of the year here, not just in mid-summer.</p>"
            "<p>Wind matters more than most homeowners expect. A breezy afternoon can hold turf ten or fifteen degrees below a still one at the same air temperature and sun angle, which is part of why two yards a few blocks apart can feel noticeably different underfoot at the same hour.</p>"),
    ])
    faqs = [
        faq("Can bare feet or paws get burned on hot turf?", "It's possible in the early-afternoon window on a full-sun installation. Published playground research treats surfaces in the same range as hot pavement or sand as a burn risk to bare skin within about a minute once air temperature passes 90°F. A rinse and a quick hand-test before letting kids or dogs on it removes most of the risk."),
        faq("Does turf cool off at night the same way pavement does?", "Faster, in most cases. Turf is a thin surface with little mass, so it sheds heat within twenty to thirty minutes of losing direct sun. A concrete slab or asphalt driveway several inches thick stays noticeably warm well after sunset because it holds more heat."),
        faq("Is a putting green just as hot as a lawn?", "Close to it. Putting-green turf has a shorter pile and a denser face, and the ranges in the table apply about the same. Fringe turf around the cups behaves like standard residential turf."),
        faq("Does rain cool artificial turf down?", f"Yes, the same way a hose rinse does, and for about as long. Central Florida's summer storms do this for free most afternoons; {post('does-artificial-turf-drain-in-heavy-rain', 'how fast that water actually leaves the yard')} depends on the base underneath, not the turf itself."),
        faq("Is turf hotter in Kissimmee than in a cooler climate?", "The sun angle and humidity here push readings toward the upper end of the published ranges for more months of the year than in a northern state, but the underlying material behaves the same everywhere. A dark-colored yard in Michigan can still hit similar peaks on its hottest July days; Florida just has more of those days and a longer season of them."),
    ]
    return page("/blog/how-hot-does-artificial-turf-get-in-florida/", "post",
                "How Hot Does Artificial Turf Get in Kissimmee, FL?",
                "Published studies show artificial turf hits 120-150°F in Florida sun, over 195°F in one field test, as of September 2026, plus the hose-rinse fix that works.",
                "How hot does artificial turf get in Florida?",
                capsule("In Kissimmee's full summer sun, artificial turf commonly reads 120°F to 150°F at the surface and can top 160°F on a still, cloudless July afternoon, as of September 2026. A university field study has measured synthetic turf above 195°F, while nearby natural grass stayed close to air temperature. A hose rinse brings the surface down within minutes, though the relief lasts only an hour or two."),
                body, faqs=faqs, crumbs=CRUMBS, crumb="Turf heat in Florida", published=PUB,
                sources=["magnolia-heat", "horsemans-heat", "sgw-faq", "dep-rule", BYU, PSU, SOFFALL],
                related=[("/blog/coolest-artificial-grass-and-infill-for-florida/", "What actually lowers turf's surface temperature"),
                         ("/blog/can-artificial-turf-melt/", "Can artificial turf melt?"),
                         ("/playground-turf/", "Playground turf with a sized shock pad"),
                         ("/pool-turf/", "Pool and lanai turf")])


# ================================================================== 2
def p_coolest():
    body = "".join([
        sec("Does turf color make a real difference?",
            f"<p>Some, but less than the marketing suggests. Lighter, multi-tone blends run a little cooler than a single dark green because they reflect more sunlight, and every {svc('residential', 'turf manufacturer')} we've seen literature from claims a color-based cooling edge for its lighter lines. We haven't found an independent, side-by-side Florida test that isolates color alone from blade shape and infill, so treat a manufacturer's specific-degree color claim as a sales number until you see it measured outside a lab.</p>"),
        sec("What about blade shape and thatch?",
            "<p>Diamond and W-shaped blade profiles are sold on the idea that more surface area sheds heat faster between blades, and a thatch layer (the curled fibers mixed in at the base) is sold as extra airflow. Both are plausible engineering, and both are also the manufacturer's own claim rather than a published, independent field comparison. The honest version: these features change the feel underfoot and how natural the lawn looks more reliably than they change the thermometer reading.</p>"
            "<p>Pile height plays a smaller, more consistent role. A taller pile holds a thin layer of slightly cooler air near the base of the blades, which is one reason a 1.75-inch residential product can feel a shade less scorching underfoot than a 1-inch sports-style turf in the same spot at the same hour.</p>"),
        sec("Do cooling infills work, and which ones are legal on a home lawn?",
            f"<p>The infills marketed as cooling work by evaporation: a coating on the sand holds a little water and releases it as the surface heats, the same principle as a swamp cooler. That only helps while the coating is damp, so it fades within an hour or two of the last rinse. Under Florida's turf rule, effective May 19, 2026, a single-family lawn can only use natural infill or coated silica sand with a non-toxic coating, which rules out gel beads or any rubber-based cooling product on the lawn itself ({src('dep-rule', 'Rule 62-308.100, F.A.C.')}); those stay legal only inside the footprint of playground equipment.</p>"
            + table("Cooling methods for artificial turf in Florida",
                    ["Method", "How it lowers surface temperature", "Allowed on a home lawn under the state rule", "What to expect"],
                    [["Lighter/multi-tone blade color", "Reflects more sunlight than solid dark green", "Yes, it's the turf itself", "A modest, unmeasured difference in most reports"],
                     ["Coated evaporative silica sand", "Holds moisture, cools by evaporation while damp", "Yes, it's coated silica sand", "Works for roughly an hour or two after a rinse, then fades"],
                     ["Rubber or gel cooling infill", "Similar evaporative or reflective claim", "No, only inside playground-equipment footprints", "Not an option for a lawn, dog run or putting green"],
                     ["Shade sail or tree canopy", "Blocks direct sun outright", "Yes, and required near tree drip lines anyway", "The single biggest, least disputed reduction available"],
                     ["Hose rinse", "Evaporative cooling across the whole surface", "Yes, required since in-ground irrigation can't water turf", "Immediate drop, fading over one to two hours"]],
                    "Cooling-infill and blade claims above reflect manufacturer literature; independent, Florida-specific side-by-side testing is limited, so we've flagged that in the description rather than attaching a number to it.")),
        sec("How much does a hose rinse help, and how long does it last?",
            f"<p>A hose rinse is still the most reliable tool in the list, dropping the surface within a minute or two and holding the relief for roughly an hour or two before full sun brings it back {src('magnolia-heat', 'per a Florida installer field test')}. {post('how-hot-does-artificial-turf-get-in-florida', 'How hot the surface gets in the first place')} sets the baseline the rinse is working against. Because in-ground sprinklers can't legally water synthetic turf under the May 2026 rule, this has to be a hose someone turns on, not a timer.</p>"
            "<p>Say you have a west-facing play area in Celebration that reads close to 150°F at 3 p.m. Swapping standard silica for a coated evaporative sand might shave several degrees while it's damp, a shade sail over the hottest third of the yard removes far more, and a hose rinse right before the kids go out does the rest for the next hour or so. Stacking the three does more than any one alone.</p>"),
        sec("Do putting greens and pet turf need the same cooling approach?",
            f"<p>Mostly yes. A {svc('putting', 'putting green')}'s shorter pile and denser face read close to standard turf in the sun, so shade over the practice tee and a rinse before a hot-afternoon round help the same way. {svc('pet', 'Pet turf')} usually already carries zeolite or coated sand for odor control; that same coated-sand family happens to be the only infill format the state rule allows for cooling on a lawn, so there's no real trade-off between odor control and heat control in the infill choice.</p>"),
        sec("Does planting shade trees near turf create a conflict with the state rule?",
            f"<p>It can, and it's worth planning around rather than working out after the fact. Florida's turf rule keeps synthetic turf outside the drip line of any tree, on your lot or a neighbor's, unless a certified arborist certifies the installation won't harm the tree ({src('dep-rule', 'Rule 62-308.100, F.A.C.')}). That means the shadiest, coolest spot near a mature live oak is often also the spot where turf legally can't go without that letter. A young shade tree planted well outside the intended turf area avoids the conflict entirely and starts paying off in shade within five to ten years, while a fast-growing canopy tree such as an East Palatka holly does it sooner on a smaller footprint.</p>"
            f"<p>{post('how-hot-does-artificial-turf-get-in-florida', 'The shaded-versus-full-sun comparison')} in our temperature article shows why that planning is worth the wait.</p>"),
    ])
    faqs = [
        faq("Is darker green turf always hotter than lighter turf?", "In most manufacturer testing, yes, though the gap is smaller than the color difference suggests. Blade material, pile height and how much shade the yard gets change the reading more than color alone."),
        faq("Can I install a misting system over turf to cool it?", "Not one tied to an in-ground irrigation line; the state's May 2026 turf rule bars using in-ground irrigation to water synthetic turf. A portable hose-end mister you run yourself isn't part of that irrigation system and works the same as a rinse."),
        faq("Does cooling infill color fade in Florida sun?", "All infill and turf fiber fades some over years of UV exposure, cooling-coated sand included. It's a gradual color shift, not a sudden loss of the coating's evaporative function."),
        faq("Does artificial turf need less cooling help in shade all day?", f"Turf under a full tree canopy rarely needs any of this; it tracks close to air temperature most of the day. {post('how-hot-does-artificial-turf-get-in-florida', 'The shaded reading in our turf-temperature table')} shows how much of a difference full shade makes on its own."),
        faq("Do reflective or metallic infill products exist for Florida lawns?", "We haven't found one that meets the state's infill rule for a home lawn, which limits infill to natural material or coated silica sand. A reflective or metallic-coated product would need to clear that same standard before it belongs on a residential yard here. A lighter-colored border or edge material offers a similar, smaller benefit by reflecting a bit more sunlight than a dark bender-board edge, though it's a minor factor next to shade and a rinse schedule."),
    ]
    return page("/blog/coolest-artificial-grass-and-infill-for-florida/", "post",
                "Coolest Artificial Grass & Infill for Florida Sun",
                "Color, blade shape, coated sand and a hose rinse all affect turf heat; what's proven versus marketed, and what Florida's 2026 turf rule allows on a home lawn.",
                "What is the coolest artificial grass and infill for Florida sun?",
                capsule("Nothing keeps synthetic grass at air temperature in full Florida sun, but a hose rinse, shade and coated evaporative sand make the most difference, cutting surface readings for an hour or two at a time. Under the state turf rule in force since May 19, 2026, the only infill allowed to help with cooling on a Kissimmee-area home lawn is coated silica sand, not a rubber or gel product."),
                body, faqs=faqs, crumbs=CRUMBS, crumb="Coolest turf & infill", published=PUB,
                sources=["magnolia-heat", "horsemans-heat", "dep-rule", "hb683"],
                related=[("/blog/how-hot-does-artificial-turf-get-in-florida/", "How hot does artificial turf get in Florida?"),
                         ("/compare/zeolite-vs-silica-vs-antimicrobial-infill/", "Zeolite vs. silica vs. antimicrobial infill"),
                         ("/laws/florida-hb-683/", "What Florida's turf rule requires for infill"),
                         ("/pet-turf/", "Pet turf & dog runs")])


# ================================================================== 3
def p_melt():
    body = "".join([
        sec("What actually makes turf melt?",
            f"<p>Ordinary Florida sun almost never does it on its own, and a melted spot is a different problem from the general wear a {svc('repair', 'turf repair')} visit usually addresses. {post('how-hot-does-artificial-turf-get-in-florida', 'Full-sun surface readings')} of 120°F to 150°F, even the rare 195°F-plus extreme, sit below where polyethylene blades soften and well below where they melt outright. What crosses that line is concentrated, reflected light: a low-emissivity (low-E) window, a mirrored or reflective vinyl fence panel, a glass storm door, or even a curved patio umbrella can focus sunlight onto one small patch of turf like a magnifying glass, holding that spot far hotter than the open yard around it for as long as the sun angle lines up.</p>"),
        sec("How hot does turf actually have to get to melt?",
            f"<p>Polyethylene, the resin most turf blades are made from, softens somewhere in the roughly 195°F to 275°F range depending on density and grade, and fully melts above that ({xt(POLY, 'general polyethylene melting-point data')}). A focused reflection can hold a small area well past that point for hours at a time, which is why melt damage almost always shows up as a tight, localized patch rather than a general fading across the whole lawn. Direct contact heat sources cross that line even faster: a grill, a fire pit, a dropped cigarette or a sparkler all run hot enough to deform or burn turf on contact in seconds.</p>"
            + table("What actually melts artificial turf",
                    ["Heat source", "How it reaches melting range", "Typical damage pattern"],
                    [["Ordinary full-sun exposure", "Rarely reaches polyethylene's softening range on its own", "None, under normal conditions"],
                     ["Low-E window or reflective glass", "Focuses reflected sunlight onto one spot for hours", "A small, sharply-defined melted or discolored patch"],
                     ["Reflective vinyl fence or mirrored surface", "Similar concentrated-reflection effect at certain sun angles", "A patch that tracks the sun's path across the day"],
                     ["Grill, fire pit or chiminea", "Direct radiant heat and stray embers", "Scorching or a hardened, glassy spot near the source"],
                     ["Dropped cigarette or sparkler", "Direct contact at flame temperature", "A small burn hole, not a wider melted zone"]],
                    "Melting-point range is general polyethylene polymer data, not a figure specific to any turf brand; individual products vary by resin grade and additive package.")),
        sec("How do you spot a melt risk before it happens?",
            "<p>Stand in the planned turf area in the early afternoon on a sunny day, ideally between roughly 1 and 4 p.m., and look back toward the house and any neighboring windows or fences. A bright, hot glare reflecting into your eyes from a second-story window or a west-facing sliding door is the same light that will land on the turf. Reflective fence panels, chrome grill lids left open, and curved mirrored gazing balls or fence toppers are worth the same check. This is a walk-the-lot method, not a lab test, but it catches the great majority of real cases before installation.</p>"),
        sec("How do you fix a melted spot once it's happened?",
            f"<p>Melted polyethylene doesn't reflow back to normal once it cools, so the fix is almost always a patch: cutting out the damaged section and splicing in a matching piece along the grain and seam lines, the same {svc('repair', 'seam and edge repair')} technique used for a burn hole or a tear. Small, isolated spots patch invisibly enough that most people never notice unless they're looking for the seam.</p>"
            "<p>Preventing a repeat matters more than the patch itself. Exterior window screens or a low-E-compatible solar film cut the reflection at the source; a retractable awning or shade sail over the affected strip works if the window can't be treated; and simply relocating a grill or fire pit a few feet away from the turf line removes a direct heat source entirely. Say you have a two-story home in Storey Lake where an upstairs low-E window throws a hot afternoon glare onto an eight-inch strip of backyard turf each summer. Applying an exterior solar film to that one window, rather than replacing the glass, is usually the cheaper fix and it stops the reflection at the source instead of managing the damage every season.</p>"),
        sec("Does a fire pit ring or patio umbrella need its own buffer?",
            f"<p>Yes. A fire pit or chiminea needs a non-combustible pad, paver ring or gravel buffer between the flame and any turf, sized to the manufacturer's clearance instructions, because embers and radiant heat both reach melting range quickly at close range. {svc('pool', 'Pool and lanai turf')} near a heated spa or a reflective screen enclosure frame benefits from the same kind of buffer check, since screen aluminum can throw a milder version of the same reflected-glare effect at the wrong angle.</p>"),
        sec("What if the reflection is coming from a neighbor's house, not yours?",
            "<p>It happens, especially between two-story homes on tighter lots in newer subdivisions, and it's a harder problem because you can't put film on someone else's window. A tall shade sail, a section of taller fencing, or a fast-growing screening shrub planted between the two properties intercepts the reflection on your side of the line without needing the neighbor's cooperation. Where the reflection also lands on the neighbor's own siding or deck, it's often worth a friendly conversation first, since the fix may be simpler and cheaper for them to address at the source. HOA architectural guidelines sometimes limit fence height or screening plant choices in exactly this kind of dispute, so it's worth checking the community's design standards before committing to a specific fix.</p>"),
    ])
    faqs = [
        faq("Does artificial turf melt just from an ordinary hot Florida summer?", "Not typically. Published surface readings for turf in full sun, even the rare extremes recorded in university field studies, generally sit below where polyethylene softens. Melting almost always traces back to a concentrated heat source like a reflected window or a grill, not ambient sun."),
        faq("Will a metal fire pit ring protect the turf around it?", "It helps but doesn't fully solve it; radiant heat still reaches outward from the sides and top of most rings. A paver or gravel buffer between the ring and the turf line, sized to the manufacturer's clearance distance, is the more reliable protection."),
        faq("Can melted turf be repaired so it doesn't show?", "Usually, for a small, isolated spot. A clean patch spliced in along the seam lines and grain direction blends in closely enough that it's hard to spot without knowing where to look. A widespread, repeated melt pattern from an unaddressed reflection is harder to hide and worth fixing at the source instead."),
        faq("Do all artificial turf products use the same plastic?", "No. Blades are usually polyethylene or a polyethylene blend, sometimes with polypropylene in the backing or thatch layer, and exact resin grades vary by manufacturer. That's part of why melting-point ranges are given as a range rather than one fixed number."),
        faq("Does tinted or hurricane-rated glass cause the same reflection problem?", "It can, since the reflective coatings used for both energy efficiency and impact-glass tinting are what concentrate the light in the first place. A clear, uncoated single-pane window is far less likely to cause a hot spot than a coated low-E or reflective hurricane unit. A pool cage or screen enclosure's aluminum framing can do a milder version of the same thing, though it's a smaller, less continuous reflective surface than a full pane of glass and rarely causes the same degree of damage."),
    ]
    return page("/blog/can-artificial-turf-melt/", "post",
                "Can Artificial Turf Melt? Causes & Fixes in Florida",
                "Yes, turf can melt, almost always from a reflected low-E window or a grill rather than ordinary sun. What melts it, how to check for it, and how it's repaired.",
                "Can artificial turf melt?",
                capsule("Yes: polyethylene turf blades soften starting around 195°F and melt into hard, glassy patches above that, hot enough that reflected sunlight from a low-E window, a grill or a reflective fence can do it on a single bright Kissimmee afternoon, as of September 2026, even though ordinary summer sun exposure alone rarely reaches that point."),
                body, faqs=faqs, crumbs=CRUMBS, crumb="Can turf melt?", published=PUB,
                sources=["magnolia-heat", "horsemans-heat", POLY],
                related=[("/turf-repair/", "Turf repair for seams, tears and melted spots"),
                         ("/blog/how-hot-does-artificial-turf-get-in-florida/", "How hot does artificial turf get in Florida?"),
                         ("/blog/does-homeowners-insurance-cover-artificial-turf/", "Does homeowners insurance cover artificial turf?"),
                         ("/pool-turf/", "Pool & lanai turf")])


# ================================================================== 4
def p_urine():
    body = "".join([
        sec("Why does dog urine smell get trapped in artificial turf?",
            f"<p>Urine breaks down into ammonia and feeds bacteria as it dries, and both processes happen inside the infill and along the backing where a quick surface rinse doesn't always reach ({src('sgw-faq', 'Synthetic Grass Warehouse pet-turf FAQ')}). A weed barrier laid under {svc('pet', 'pet turf')} makes it worse: it's meant to block weeds from below, but it also blocks urine from soaking on down into the base, so it pools and sits right where the odor forms fastest. We skip weed barrier under pet turf for exactly that reason, even though it means a few more weeds to pull by hand along the fence line each year.</p>"),
        sec("What is the hose-and-enzyme routine that actually works?",
            steps([("Rinse daily in a high-use dog run, or every two to three days in a general backyard.", "A hose on a wide fan spray, not a narrow jet, flushes fresh urine through the infill before it dries and crystallizes."),
                   ("Apply an enzyme-based pet-odor cleaner every one to two weeks.", "Enzymes break down the uric-acid crystals a plain water rinse leaves behind; a vinegar-and-water rinse can help with fresh spots but doesn't reach the same crystals."),
                   ("Broom or rake the infill upright monthly.", "Matted infill traps moisture at the base of the blades; standing the fibers back up lets the surface dry faster between rinses."),
                   ("Check drainage after every rinse.", f"Water should disappear within a few minutes. {post('does-artificial-turf-drain-in-heavy-rain', 'Slow drainage under pet turf')} usually points to a clogged or undersized base, not the turf itself.")])),
        sec("Which infill helps most for dogs?",
            f"<p>Zeolite and antimicrobial coated sand are both built to handle ammonia better than plain silica; {a('/compare/zeolite-vs-silica-vs-antimicrobial-infill/', 'the full comparison')} goes through the trade-offs in depth. Under Florida's turf rule in force since May 19, 2026, both qualify as allowed infill for a single-family lawn because they're natural material or a coated sand, unlike a crumb-rubber pet infill, which the rule restricts to playground equipment only.</p>"
            + table("Infill for dog urine and odor control",
                    ["Infill", "How it handles ammonia", "Upkeep it needs", "Allowed on a home lawn"],
                    [["Rounded silica sand", "No odor treatment; ammonia just sits until rinsed", "Frequent rinsing to keep up", "Yes"],
                     ["Zeolite", "A natural mineral that adsorbs ammonia and releases it on rinsing", "Needs regular rinsing to keep working; loses capacity over time", "Yes, it's a natural material"],
                     ["Antimicrobial coated sand", "Coating resists bacteria growth that produces odor", "Similar rinsing schedule to zeolite", "Yes, it's a coated sand"],
                     ["Crumb rubber or gel pet infill", "Varies by product; not the state's focus", "N/A on a home lawn", "No, restricted to playground equipment"]],
                    "Coating performance claims are manufacturer literature; independent, long-term odor comparisons across brands are limited.")),
        sec("Does the size or breed of dog change any of this?",
            "<p>Not the routine itself, but it changes how often you'll run it. A single small dog on a large lawn spreads urine over enough area that a twice-weekly rinse often keeps up fine. Two or more large dogs concentrated on a smaller run, especially one with a favorite corner, load that spot faster than infill and drainage can keep pace with on a casual schedule, which is why dedicated dog runs get the daily-rinse recommendation rather than the general-yard one. Female dogs, which tend to squat and saturate one spot rather than marking in passing the way males often do, also tend to concentrate urine more heavily in fewer places. A household with three or more dogs sharing one run benefits from treating that area more like a commercial dog park than a residential lawn, with the rinse-and-enzyme schedule to match.</p>"),
        sec("Does the season change how bad the smell gets?",
            "<p>Yes. Heat and humidity speed up the bacterial activity that produces the sharp ammonia smell, so a Kissimmee summer makes a skipped rinse noticeable within a day where the same lapse in a cooler, drier month might take three or four days to turn strong. Rainy-season storms give the yard a free rinse most afternoons, which helps, but they also raise humidity between storms in a way that can make a neglected dog run smell worse, not better, if the routine slips during the wettest months. Dry season cuts the opposite way: fewer free storm rinses mean the hose-and-enzyme routine is doing all the work on its own, so it's worth keeping to the schedule even when the yard doesn't smell bad yet.</p>"),
        sec("When does the base itself need to be redone?",
            f"<p>If the yard smells strongly right after a thorough rinse and enzyme treatment, or the smell rises from cracks and low spots rather than the turf surface itself, urine has likely worked past the infill and into the base, or a weed barrier underneath is holding it there. {svc('cleaning', 'A deep power-brooming and sanitizing service')} can reset infill that's simply overdue for attention, but a base that's been saturated for years usually needs to come up: pull the turf, remove any weed barrier, flush or replace the saturated base material, and rebuild.</p>"
            "<p>Say you have two Labradors on a 400 sq ft dog run installed four years ago with a weed barrier under the turf. Rinsing daily and treating with enzyme cleaner every week cuts the smell noticeably but it comes back within a day or two, and it's strongest near the drain corner. That pattern points to urine trapped under the weed barrier rather than a cleaning problem, and the fix is pulling that corner up, removing the barrier, and letting the base drain the way it was designed to before the barrier went in.</p>"),
    ])
    faqs = [
        faq("Can I use bleach instead of an enzyme cleaner on pet turf?", "We don't recommend it. Bleach can discolor turf fibers and doesn't break down the uric-acid crystals that cause lingering odor the way an enzyme cleaner does. A pet-safe enzyme product built for artificial turf is the more reliable choice."),
        faq("How often should dog-run infill be topped up?", "Roughly once a year for daily use, sooner if brushing reveals thin or compacted spots. Infill migrates out through normal traffic and rinsing over time, and a thin layer holds less odor-control capacity."),
        faq("Does a bigger dog run smell worse than a small one?", "Not necessarily; it's more about dogs per square foot and how often it's rinsed than total size. A small, heavily used run with infrequent rinsing usually smells worse than a larger yard rinsed on a regular schedule."),
        faq("Is baking soda enough for an occasional accident on turf?", "For a single fresh spot, a baking soda application followed by a water rinse can help absorb odor while it's still wet. It isn't a substitute for the enzyme routine on a yard dogs use daily."),
        faq("Do puppies cause more odor problems than adult dogs?", "Often yes, mainly from frequency rather than anything different in the urine itself. A puppy on a house-training schedule can produce far more small accidents across the yard in a day than an adult dog on a routine, which spreads the ammonia load around and makes it easier to miss a spot during rinsing. Natural grass and soil, by comparison, absorb urine and let soil microbes break it down over a larger area, which is part of why a consistent rinse routine matters more on turf than it typically does on a real lawn."),
    ]
    return page("/blog/how-to-get-dog-urine-smell-out-of-artificial-turf/", "post",
                "Get Dog Urine Smell Out of Artificial Turf",
                "A hose-and-enzyme routine plus zeolite or coated-sand infill clear most dog urine odor from artificial turf; when it doesn't, the base underneath usually needs work.",
                "How do you get dog urine smell out of artificial turf?",
                capsule("Regular hose rinsing, an enzyme cleaner every one to two weeks and an ammonia-handling infill such as zeolite clear most dog-urine odor from artificial turf. Under Florida's turf rule, in force since May 19, 2026, that infill has to be natural material or coated sand, and in Kissimmee yards the smell that survives all of that almost always means the base underneath is holding urine, not the turf."),
                body, faqs=faqs, crumbs=CRUMBS, crumb="Dog urine odor", published=PUB,
                sources=["sgw-faq", "dep-rule"],
                related=[("/pet-turf/", "Pet turf & dog runs"),
                         ("/turf-cleaning/", "Turf cleaning & maintenance"),
                         ("/compare/zeolite-vs-silica-vs-antimicrobial-infill/", "Zeolite vs. silica vs. antimicrobial infill"),
                         ("/blog/does-artificial-turf-drain-in-heavy-rain/", "Does artificial turf drain in Florida's heavy rain?")])


# ================================================================== 5
def p_drain():
    body = "".join([
        sec("How much rain can turf's backing actually handle?",
            f"<p>Perforated turf backing drains at more than 30 inches of rain an hour ({src('sgw-faq', 'a published drainage-rate spec')}), a figure no Central Florida storm comes close to touching. That number describes the backing material in isolation, tested with water poured straight through it; it says nothing about how fast water actually leaves a real {svc('residential', 'installed lawn')}, which depends on what's underneath the turf, not the turf itself.</p>"
            "<p>It's worth separating the two claims because most drainage complaints we hear start from the assumption that the turf failed. In nearly every case we've walked, the perforations were doing their job fine and the water was backing up somewhere below them.</p>"),
        sec("How does that compare to a real Kissimmee storm?",
            table("Published 1-hour rainfall depths near Kissimmee, FL vs. turf backing's drainage rate",
                  ["Storm frequency", "1-hour rainfall depth", "Turf backing's rated capacity"],
                  [["Common summer storm (roughly 1-in-2-year)", "About 2.2 in/hr", "Over 30 in/hr"],
                   ["1-in-10-year storm", "About 2.9 in/hr", "Over 30 in/hr"],
                   ["1-in-25-year storm", "About 3.3 in/hr", "Over 30 in/hr"],
                   ["1-in-100-year storm", "About 3.9 in/hr", "Over 30 in/hr"]],
                  f"Rainfall depths from {xt(NOAA14, 'NOAA/NWS Atlas 14 point precipitation frequency data')} for a location near Kissimmee, checked September 2026. Even the rarest storm on this table uses less than an eighth of the backing's rated capacity.")
            + "<p>In practice that means the turf itself is never the bottleneck, even in a rare, intense downpour. Whatever is slowing the water down is beneath it.</p>"),
        sec("Why does a base decide drainage, not the turf?",
            f"<p>Water that passes through the backing has to keep moving through the base and into the native soil, and that's where the real limits show up. Florida's turf rule requires the subgrade to be washed, open-graded crushed rock or crushed concrete rather than a dusty material full of fines, because unwashed fines bind together into a crust that blocks percolation the same way a driveway's compacted road base does ({src('dep-rule', 'Rule 62-308.100, F.A.C.')}). {post('base-under-artificial-turf-florida-sandy-soil', 'What that base looks like in practice')} covers depth, compaction and the local soil series in more detail. Grading matters just as much: the base and the soil below it need a slope of roughly 1 to 2 percent away from the house, or water finds the lowest point and sits there no matter how fast the backing itself drains.</p>"),
        sec("What does Rule 62-308.100 require for stormwater?",
            ul(["<strong>No pooling and no added runoff.</strong> Installation can't increase the volume, direction or rate of runoff onto a neighboring property.",
                "<strong>A permeability standard.</strong> A local government may set a quantifiable cap of up to 10 inches per hour for all layers combined, well above anything a Florida storm produces.",
                "<strong>Swales, ditches and stormwater ponds are off-limits.</strong> Turf can't be installed inside them or alter a lot's permitted stormwater system.",
                f"<strong>The base has to stay washed and open.</strong> {src('dep-rule', 'The same subgrade requirement')} that keeps the base permeable is what keeps a yard from ponding in the first place."])),
        sec("What about the high water table under Kissimmee-area yards?",
            f"<p>Much of the native soil around Kissimmee sits over a seasonally high water table that can rise to within a couple of feet of the surface during the wettest months, which slows how fast the ground itself can absorb water even when the base above it is built correctly. {post('base-under-artificial-turf-florida-sandy-soil', 'The soil-series article')} goes through which specific series sit under different parts of the service area and what that means for a build. Say you have a quarter-acre lot in St. Cloud that holds standing water in one back corner for two days after a June storm. If the turf itself drains fine everywhere else, the fix is almost always regrading that low corner or adding a drain line to move water off the lot faster, not replacing the turf.</p>"),
        sec("Does the size of the storm matter, or just how long it lasts?",
            "<p>Duration matters more than most people expect. A short, intense burst that drops half an inch in ten minutes rarely overwhelms a correctly built base, because the ground has a moment to catch up between the heaviest bands. A slow-moving system that parks over the same neighborhood for six or eight hours, common with a tropical system rather than an ordinary afternoon storm, saturates the soil beneath the base fully, and once the native soil itself is saturated no amount of base permeability speeds up how fast the ground can accept more water. That's a soil-capacity limit, not a turf or base failure, and it affects a natural lawn on the same lot just as much. The practical takeaway is that a yard can drain perfectly all summer and still hold water for a day after an unusually slow-moving system, without anything having gone wrong with the build.</p>"),
        sec("What's the difference between a wet yard and a flooded one?",
            f"<p>A wet yard clears within twenty to forty minutes and never has water sitting more than an inch or two deep. A flooded yard holds water for hours, often because a swale, retention pond or drainage easement nearby is itself full and has nowhere to send the runoff it was designed to carry. Turf installed near a swale or pond has to stay outside of it under the state rule, and for good reason: those features are doing the neighborhood's stormwater work, and a yard that floods because the swale behind it is full needs the drainage system addressed, not the lawn.</p>"
            f"<p>{a('/laws/florida-hb-683/', 'The full rule breakdown')} covers where turf can and can't go near a stormwater feature in more detail, including the exact wording on swales and littoral zones.</p>"),
    ])
    faqs = [
        faq("Does artificial turf need a French drain?", "Not on a lot that's graded correctly. A French drain or a shallow drain line becomes worth adding when a low spot can't be regraded away, such as a corner boxed in by a fence and a neighbor's higher lot line."),
        faq("Can heavy rain wash turf infill away?", "A hard, fast storm can shift a small amount of infill toward the lowest point of a slope, especially on a newly installed lawn before the infill has fully settled in over the first few weeks. It's a minor top-up issue, not a sign the turf or base has failed."),
        faq("Does artificial turf increase runoff onto a neighbor's yard?", "It shouldn't, and the state standard specifically prohibits it. Correctly graded, permeable turf drains through the base into the soil roughly the way the sod it replaced did, rather than sheeting off toward a fence line."),
        faq("How fast should a yard drain after a typical storm?", "Standing water should be gone within twenty to thirty minutes on a well-built lawn, faster on sandy Candler-series soil and a little slower on the flatter, poorly drained series common closer to Kissimmee's lakes."),
        faq("Does the color or brand of turf affect drainage?", "No. Drainage is a function of backing perforation, base material and grading, not blade color or the manufacturer's branding. Two different turf products over the same well-built base drain at essentially the same rate, all else being equal. Gutters and downspouts near the turf area matter more: one emptying directly onto turf can concentrate far more water on one spot than the base was graded to handle, and redirecting it to a splash block or drain line away from the edge usually solves that."),
    ]
    return page("/blog/does-artificial-turf-drain-in-heavy-rain/", "post",
                "Artificial Turf Drainage in Kissimmee's Heavy Rain",
                "Turf backing drains over 30 in/hr, far above any Florida storm on record near Kissimmee. What decides real drainage, and what the 2026 state rule requires.",
                "Does artificial turf drain in Florida's heavy rain?",
                capsule("Perforated turf backing drains faster than 30 inches of rain an hour, far above anything Florida produces; NOAA's rainfall data for the Kissimmee area puts even a 100-year, one-hour storm at under 4 inches. As of September 2026, a yard that floods after a storm has a base or grading problem, not a turf problem."),
                body, faqs=faqs, crumbs=CRUMBS, crumb="Drainage in heavy rain", published=PUB,
                sources=["sgw-faq", "dep-rule", "magnolia-drain", NOAA14],
                related=[("/blog/base-under-artificial-turf-florida-sandy-soil/", "What base goes under turf in Central Florida sandy soil"),
                         ("/blog/artificial-turf-hurricane-flooding/", "What happens to artificial turf in a hurricane or flood?"),
                         ("/laws/florida-hb-683/", "Florida's turf rule, stormwater section"),
                         ("/pet-turf/", "Pet turf & dog runs")])


# ================================================================== 6
def p_hurricane():
    body = "".join([
        sec("Can wind pull artificial turf up during a storm?",
            f"<p>A properly anchored {svc('residential', 'lawn installation')} shouldn't lift in anything short of the most extreme wind, because Florida's turf rule, in force since May 19, 2026, requires turf to be anchored at all edges and seams enough to withstand wind or flooding ({src('dep-rule', 'Rule 62-308.100, F.A.C.')}). What actually fails in a storm is almost always a shortcut from years earlier: a perimeter held down with too few nails, a bender-board edge that rotted and let the border pull loose, or a seam where the adhesive skinned over before it fully bonded. A gap that starts an inch wide at one corner gives wind something to grab, and it grows from there.</p>"),
        sec("What does floodwater do to a turf lawn?",
            f"<p>Standing water on its own doesn't damage turf the way it damages drywall or wood; the blades and backing are built to sit wet. The real issues are what the water carries: silt and debris that smother the fibers, infill that shifts or washes out at the low end of a slope, and contamination if the water has been in contact with a road, a septic drainfield or a stormwater system. We treat any floodwater that fits that description as contaminated until it's rinsed clean: rubber gloves, a thorough hose-down before working the yard, and a wash-up afterward. Surge flooding from brackish or saltwater leaves turf and infill looking dull and salt-crusted until it's rinsed through.</p>"),
        sec("What should you check after a storm?",
            steps([("Walk the perimeter first.", "Look for lifted edges, pulled staples or a bender board that's separated from the turf, starting at corners and gate openings where wind load concentrates."),
                   ("Clear debris before it sits.", "Branches, roofing grit and mulch that blow in can stain or abrade turf if left in place for days under a hot sun."),
                   ("Rinse anything the floodwater touched.", "Treat it as contaminated water, especially near a septic system or a low spot that collects road runoff."),
                   ("Check that the base still drains.", f"Silt from floodwater can clog the base's surface even when the {svc('residential', 'turf itself')} looks fine; {post('does-artificial-turf-drain-in-heavy-rain', 'slow drainage after a storm')} usually traces back to that, not storm damage."),
                   ("Look for infill loss on slopes.", "A hard-driving storm can wash infill toward the low end of a graded yard; a light top-up evens it back out.")])),
        sec("Does the state anchoring standard actually help in a real storm?",
            f"<p>It sets a floor that most careful installers were already building to, and it gives homeowners a standard to check a contractor against. {src('dep-rule', 'The rule text itself')} ties the requirement directly to withstanding wind or flooding, which in practice means a nailed or glued perimeter, taped and glued seams rather than loose-laid edges, and material anchored at every seam, not just the visible border. It doesn't promise a yard will come through a major hurricane untouched, and it says nothing about debris impact or floodwater contamination, both of which are cleanup issues rather than anchoring issues.</p>"
            "<p>Say you have a fenced yard in Poinciana where turf rode out a tropical storm's several inches of afternoon rain without trouble, but a corner near the side gate has a torn flap where staples pulled loose from repeated gate traffic rubbing the edge over time, not from the storm's wind alone. That's a straightforward patch, not a sign the whole install failed; the surrounding turf, anchored properly, held through the same storm without moving.</p>"),
        sec("Should turf be removed before a major hurricane?",
            f"<p>No, and there's no practical way to remove and reinstall an anchored system on short notice before a storm anyway. The more useful pre-storm step is securing or storing anything loose nearby that could become wind-driven debris: patio furniture, potted plants, decorative borders, since those cause more turf damage on impact than the wind acting on the turf itself. After the storm passes, {svc('repair', 'a repair visit')} can address anything that did lift or tear.</p>"),
        sec("Does turf near a pool or screen enclosure need any extra attention before a storm?",
            f"<p>A screen enclosure's own aluminum frame and mesh panels are far more likely to fail in high wind than the {svc('pool', 'pool-deck turf')} beneath them, and torn screen material becomes its own debris hazard when it does. Securing loose pool furniture, umbrellas and floats before a storm keeps them from scraping or gouging turf as they're thrown around inside the enclosure. After the storm, check the drain at the low point of the deck; a screen enclosure sheds a lot of water fast, and a clogged drain there backs water up onto the turf longer than open-yard turf typically sees. Pool water itself, if it overtops the deck during a direct hit, carries pool chemicals along with any storm debris, so it's worth including in the same contaminated-water rinse routine as floodwater from elsewhere on the lot.</p>"),
        sec("How does hurricane season line up with turf installation timing?",
            f"<p>Central Florida's hurricane season runs from June through November, overlapping most of the rainy season. Installs still happen during those months, and a base built to the state's drainage and anchoring standard performs the same in October as it does in February. {post('does-artificial-turf-drain-in-heavy-rain', 'The bigger seasonal factor')} is simply more frequent afternoon storms to work around on the install schedule itself, not any difference in how the finished lawn holds up once it's anchored and cured. A lawn installed in September, right in the thick of the season, still has to meet the same anchoring standard as one installed the following January, so timing an install around a named storm on the calendar isn't necessary the way it might be for exterior painting or roofing work.</p>"),
    ])
    faqs = [
        faq("Can saltwater flooding kill artificial turf permanently?", "Not the turf material itself, which tolerates saltwater better than a living lawn would. A thorough freshwater rinse afterward clears salt residue from the blades and infill; skipping that rinse leaves a dull, gritty surface longer than necessary."),
        faq("Does wind-blown debris like roof shingles puncture turf?", "It can gouge or tear the surface on impact, especially sharp metal edging or broken tile. A torn spot patches the same way a melted or worn spot does, by splicing in a matching piece."),
        faq("How soon after a storm can turf be walked on safely?", "Once standing water has cleared and any visible debris is removed, walking on it is fine. If the water was contaminated, rinsing the area first before regular use is the more cautious approach."),
        faq("Does a screened lanai protect turf from hurricane debris?", "Partly. Screen mesh stops leaves and light debris but tears easily in high wind, so a lanai isn't a reliable barrier against heavier wind-driven objects during a direct hit."),
        faq("Does infill need to be replaced after a hurricane?", "Only where it's visibly thin or washed toward a low point, which a normal top-up handles well. A full re-infill is rarely necessary unless the base itself was disturbed, undermined or excavated during storm damage. Heavy cleanup equipment is a bigger risk to the surface than the storm itself; a skid steer or debris trailer can rut or compact turf the way it would a soft lawn, and plywood sheets laid down as temporary tracks protect the surface if equipment has to cross it."),
    ]
    return page("/blog/artificial-turf-hurricane-flooding/", "post",
                "Artificial Turf in a Hurricane or Flood: What Happens",
                "Anchored turf edges are built to withstand wind or flooding under Florida's 2026 turf rule. What actually happens in a storm, and what to check afterward.",
                "What happens to artificial turf in a hurricane or flood?",
                capsule("Properly anchored turf usually survives Central Florida's hurricane season with its edges intact, but wind can lift a loose perimeter, and floodwater can carry debris and contamination onto the surface. Florida's turf rule, in force since May 19, 2026, requires edges and seams anchored against exactly that, as of September 2026, though it doesn't prevent debris damage or guarantee a yard through a direct hit."),
                body, faqs=faqs, crumbs=CRUMBS, crumb="Hurricane & flood", published=PUB,
                sources=["dep-rule", "hb683"],
                related=[("/turf-repair/", "Turf repair for edges, seams and tears"),
                         ("/blog/does-artificial-turf-drain-in-heavy-rain/", "Does artificial turf drain in Florida's heavy rain?"),
                         ("/blog/does-homeowners-insurance-cover-artificial-turf/", "Does homeowners insurance cover artificial turf?"),
                         ("/laws/florida-hb-683/", "What the state turf rule requires for anchoring")])


# ================================================================== 7
def p_base():
    body = "".join([
        sec("Why can't you just use the same limerock people use for driveways?",
            f"<p>Ordinary driveway base, sometimes sold as limerock road base, and crushed-concrete screenings both carry a lot of fine dust mixed in with the larger stone. Compacted under a driveway that's a feature, not a flaw, because it sets up hard and stays put under a car. Under {svc('residential', 'artificial turf')}, that same dust binds together when it gets wet and forms a crust that water can't pass through, which is exactly what Florida's turf rule is written to prevent: subgrade material has to be washed before installation to keep fines from binding ({src('dep-rule', 'Rule 62-308.100, F.A.C.')}).</p>"),
        sec("What base material is actually allowed?",
            table("Base material under artificial turf: what's compliant and what isn't",
                  ["Material", "Permeable once compacted?", "Compliant with Rule 62-308.100?", "Why"],
                  [["Washed, open-graded crushed rock", "Yes", "Yes", "Fines are washed out before it ever reaches the yard"],
                   ["Washed crushed concrete", "Yes", "Yes", "Same principle as washed crushed rock; the rule names both"],
                   ["Limerock road base (with fines)", "No, once compacted", "No", "Unwashed fines bind into a crust that blocks percolation"],
                   ["Crushed-concrete screenings/fines", "No", "No", "Same binding problem as unwashed limerock"],
                   ["Decomposed granite", "No", "No", "Not a crushed rock or crushed concrete material, and binds similarly"],
                   ["Bare native sand, no base", "Loose but unstable", "Not a real subgrade", "Ruts and settles unevenly under foot traffic without a compacted layer above it"]],
                  "Compliance column reflects our reading of Rule 62-308.100's subgrade and permeability requirements, effective May 19, 2026.")),
        sec("What's actually native under a Kissimmee-area yard?",
            f"<p>Much of Osceola County sits on flatwoods soils in the Myakka, Smyrna and Immokalee series, all very deep, sandy soils with a seasonally high water table and a hardened spodic layer at some depth that slows how fast water moves through ({xt(OSD_MYAKKA, 'Myakka series description')}; {xt(OSD_SMYRNA, 'Smyrna series description')}; {xt(OSD_IMMOKALEE, 'Immokalee series description')}). Head toward the Polk and Lake county ridge and the soil changes to Candler series, deep, excessively drained sand with almost no water-holding capacity at all ({xt(OSD_CANDLER, 'Candler series description')}). A base built the same way performs differently over these two soil types: on Myakka or Immokalee, the base does more of the drainage work because the native soil beneath is slow to accept water; on Candler, the native sand alone drains fast and the base mainly provides a stable, level surface to seam turf onto.</p>"
            + note(f"Soil series vary by parcel, not just by city. {src('usda-wss', 'USDA Web Soil Survey')} gives a specific reading for any address; we check it before quoting a job.")),
        sec("How deep should the base be, and how hard do you compact it?",
            f"<p>A standard residential build uses 2 to 4 inches of washed, open-graded base, spread and compacted in the top layer only. The rule is specific about the layer underneath: soil beneath the installed subgrade can't be compacted to the point that it hurts percolation ({src('dep-rule', 'Rule 62-308.100(4)(c), F.A.C.')}), so the goal is a firm, stable base on top without pounding the native sand below it into something water can no longer pass through. A geotextile fabric between the base and the native soil, a different material from the weed barrier sometimes used under the turf itself, keeps the two layers from mixing over time as water moves through both.</p>"),
        sec("What does the geotextile fabric actually do, if it's not a weed barrier?",
            "<p>A geotextile fabric laid between the compacted base and the native soil below it is a separation layer, not a weed control layer. Its job is keeping the two materials from working into each other over years of foot traffic and rain cycles, sand from below migrating up into the rock or rock working down into the sand, either of which reduces how well the assembly drains over time. It's a different product placed at a different point in the build than the optional weed barrier some installers put directly under the turf face, and the two get confused often enough that it's worth naming both separately on a quote. Asking a bidder which layer their fabric sits at, and why, is a quick way to tell whether a quote was written by someone who builds to the state's percolation standard or one that's just filling in a line item.</p>"),
        sec("Does a weed barrier belong under the base or the turf?",
            f"<p>Neither one, if the yard has dogs. A weed barrier laid under pet turf traps urine against the base instead of letting it pass through, which is one of the more common causes of lingering odor, a failure mode {post('how-to-get-dog-urine-smell-out-of-artificial-turf', 'covered in detail here')}. On a standard residential lawn without heavy pet use, a weed barrier under the turf (above the base, not mixed into it) is optional and mainly a defense against runners from bordering St. Augustine or Bahia creeping in at the edges.</p>"
            "<p>Say you have a 900 sq ft backyard in Buenaventura Lakes built on Immokalee fine sand, with a water table that sits about two feet down by September. The build removes the sod and 3 to 4 inches of soil, grades the exposed native sand 1 to 2 percent away from the house, lays 3 inches of washed crushed rock compacted firm, and seams turf on top with the perimeter nailed and glued. Because Immokalee holds water longer than the sandy ridge soils to the west, the grading step matters more here than the base depth does.</p>"),
    ])
    faqs = [
        faq("Can you skip the base and lay turf on bare sand?", "No. Bare sand shifts and ruts under foot traffic and doesn't hold a level surface for seaming. A compacted base layer is what keeps the finished lawn flat and stops low spots from forming within the first year. A putting green follows the same washed-rock principle, usually with a slightly thicker, more precisely graded base to hold its contours and true roll."),
        faq("How do you find out which soil series is under your lot?", f"{src('usda-wss', 'USDA Web Soil Survey')} shows the mapped series for any address for free. We also check it as part of a site visit before quoting a job."),
        faq("Does a French drain ever replace proper grading?", "No, it supplements it. A French drain moves water that's already collected at a low point; it doesn't fix a base or subgrade that was never sloped correctly in the first place."),
        faq("Is crushed shell ever used as a base material in Florida?", "It's less common than crushed rock or crushed concrete for turf bases here, though the state rule's own material list for infill, not subgrade, does name shell as an allowed natural material. For the base itself, washed crushed rock and crushed concrete remain the two the rule specifically names."),
        faq("Does a sloped lot need a different base approach than a flat one?", "The base material and washing requirement stay the same; what changes is how the grading and, on a steeper slope, any retaining or terracing work is planned before the base ever goes down, since correcting a slope after the base is compacted is far more disruptive than planning it up front. A base that's settled unevenly or washed out at an edge years later can often be lifted, corrected and relaid with the same turf, rather than requiring a full replacement."),
    ]
    return page("/blog/base-under-artificial-turf-florida-sandy-soil/", "post",
                "Base Under Artificial Turf in Central Florida Sand",
                "Washed crushed rock or crushed concrete, 2-4 in, is the compliant turf base under Florida's 2026 rule. What's out, and how Osceola soil series change the build.",
                "What base goes under artificial turf in Central Florida's sandy soil?",
                capsule("In Kissimmee and the rest of Osceola County, the base under artificial turf is 2 to 4 inches of washed, open-graded crushed rock or crushed concrete, compacted firm over graded native sand. Florida's turf rule, in force since May 19, 2026, requires that subgrade material washed before installation, which is why limerock road base, crushed-concrete fines and decomposed granite are out; they bind into a crust once compacted."),
                body, faqs=faqs, crumbs=CRUMBS, crumb="Base for sandy soil", published=PUB,
                sources=["dep-rule", "hb683", "usda-wss", OSD_MYAKKA, OSD_SMYRNA, OSD_IMMOKALEE, OSD_CANDLER],
                related=[("/blog/does-artificial-turf-drain-in-heavy-rain/", "Does artificial turf drain in Florida's heavy rain?"),
                         ("/blog/how-to-get-dog-urine-smell-out-of-artificial-turf/", "Getting dog urine smell out of artificial turf"),
                         ("/turf-replacement/", "Turf removal & replacement"),
                         ("/laws/florida-hb-683/", "Florida's turf rule, subgrade requirements")])


# ================================================================== 8
def p_lifespan():
    body = "".join([
        sec("What wears out first: the blades, the backing or the infill?",
            f"<p>Usually the blades, and it shows up as fading and a flattened, less springy feel in the highest-traffic paths years before the {svc('residential', 'turf')} needs full replacement. UV exposure breaks down the polymer's color and flexibility gradually; foot and paw traffic crushes the pile in the same few paths a family or a dog actually walks. The backing and stitching that hold everything together generally outlast the blades, though a backing that was never properly seamed can open at a seam well before the fibers themselves look tired. Infill compacts and migrates over the years and is the easiest piece to renew along the way, which is part of why it's not usually what ends a turf's life ({src('stn-life', 'published turf-lifespan guidance')}).</p>"),
        sec("How long does turf actually last by type of use?",
            table("Expected artificial turf lifespan by use, Central Florida",
                  ["Use", "Typical lifespan", "What shortens it most"],
                  [["Shaded residential lawn, light foot traffic", "Toward the high end of 10–20 years", "Little UV exposure and light wear; infill upkeep still needed"],
                   ["Full-sun residential lawn", "Middle of the 10–20 year range", "Constant UV exposure fades and stiffens blades over time"],
                   ["Pet turf, one or two dogs", "Toward the lower-middle of the range", "Traffic concentrated in a few paths, plus regular rinsing and brushing wear"],
                   ["High-traffic dog run, full sun", "Toward the low end of the range", "Combined UV exposure and concentrated wear in a small footprint"],
                   ["Putting green", "Comparable to a full-sun lawn", "Ball and foot traffic concentrated on the same cup and approach lines"]],
                  f"Ranges anchor to the published {src('stn-life', '10-to-20-year lifespan figure')} for UV-stabilized residential turf; placement within that range reflects how sun exposure and traffic typically shorten or extend it, not a separate published statistic for each use.")),
        sec("Does Florida's sun shorten turf life compared to other states?",
            f"<p>Florida's high UV index and long, intense summer push turf toward the lower half of its published lifespan range faster than a similar lawn would wear in a shorter, milder-summer climate, which is part of why UV stabilization in the resin matters more here than it does in a place with fewer full-sun months. The surface-temperature side of that same sun exposure, {post('how-hot-does-artificial-turf-get-in-florida', 'covered separately here')}, is a different issue from UV degradation, though both trace back to the same cause: how much direct summer sun a given yard sees.</p>"),
        sec("Does the specific price tier of turf change these numbers much?",
            "<p>Resin quality and UV stabilizer content vary between a budget product and a premium line, and that difference shows up more in a hot, sunny climate like Florida's than it would somewhere with a shorter, milder summer. On lifespan specifically, a heavier face weight and a better UV package tend to land toward the upper half of the published range, while an entry-level product installed in full sun tends toward the lower half, all else being equal. It's one of the few places where paying more up front reliably buys years of extra service, rather than just a nicer-looking lawn on day one.</p>"),
        sec("What maintenance actually extends the life of turf here?",
            ul([f"<strong>Brush against traffic lanes.</strong> Standing the blades back up where feet or paws travel most keeps that path from matting down permanently.",
                f"<strong>Rinse pet areas regularly.</strong> {post('how-to-get-dog-urine-smell-out-of-artificial-turf', 'A consistent rinse routine')} does double duty: it controls odor and keeps ammonia from degrading fibers over years of exposure.",
                "<strong>Top up infill before it gets thin.</strong> Thin infill lets blades fold over instead of springing back, which accelerates wear in that spot.",
                f"<strong>Keep the base draining.</strong> {post('does-artificial-turf-drain-in-heavy-rain', 'A base that drains properly')} prevents the kind of standing moisture that can degrade backing and adhesive over time.",
                f"<strong>Watch for melt and reflection sources.</strong> {post('can-artificial-turf-melt', 'A reflected hot spot')} damages a small area outright rather than aging the whole lawn gradually."])
            + "<p>Say you installed 1,500 sq ft of turf in a full-sun ChampionsGate backyard in 2020 with two large dogs using it daily. By year eight or nine, expect visible wear concentrated along the gate-to-patio path and any spot dogs favor, noticeably more than the shaded side yard sees, even though both were installed the same day from the same roll. That uneven wear pattern, not a single lawn-wide failure, is usually what triggers a replacement conversation.</p>"),
        sec("Does the manufacturer's warranty tell you how long turf will last?",
            "<p>Not directly, and it's worth understanding the difference before treating a warranty term as a lifespan promise. A manufacturer's warranty typically covers defects such as premature UV fading or seam failure under normal use for a set number of years; it doesn't guarantee the turf will look new for that entire period, and it doesn't cover wear from traffic, pets or a poorly built base underneath it. A lawn can easily outlive its warranty period in good shape, or show heavy wear well before the warranty expires if it's a high-traffic dog run, without either outcome being a warranty claim.</p>"),
        sec("What's the first sign turf is nearing the end of its life?",
            f"<p>Matting that doesn't spring back after brushing, noticeable color fade compared to a shaded reference spot such as under a step or a planter, and seams that have started to separate at the edges despite being properly bonded originally are the three most common signs. None of them mean the whole lawn needs to go at once; {svc('replacement', 'a full tear-out and replacement')} usually reuses the existing base if it's still sound, which keeps the cost and disruption below what the original installation required. A yard showing only one of these three signs, in one section, is usually a candidate for a localized patch rather than a full replacement.</p>"),
    ])
    faqs = [
        faq("Can you extend turf life by adding more infill later?", "Somewhat. Topping up thin infill helps blades stand upright and resist matting, which slows visible wear, but it doesn't reverse UV fading that's already happened to the fibers themselves."),
        faq("Does turf left in full shade actually last longer?", "Generally yes, since UV exposure is one of the main things that ages the blades. Shaded turf still needs the same infill and drainage upkeep as sunny turf, just with less color fade over the years."),
        faq("Does washing turf with soap shorten its life?", "An occasional mild soap-and-water cleaning for a heavily soiled spot is fine. Frequent harsh chemical cleaning, as opposed to a hose rinse and an enzyme product built for turf, can dull fibers faster than normal wear would on its own."),
        faq("Does a lawn with kids wear out faster than one without?", "It depends more on the specific activity than on kids as a category. Running and walking traffic wears turf gradually like any foot traffic; a fixed trampoline, a swing set's landing zone or a repeated slide-and-scoot spot concentrates wear the same way a dog's favorite path does, in the same handful of square feet, year after year."),
        faq("Is there a way to test how much life is left in existing turf?", "There's no formal test most homeowners have access to, but a simple check helps: brush a worn section and see whether the blades spring back upright or lie flat again within a few minutes. Fibers that no longer recover after brushing have lost most of their remaining resilience, whatever the calendar says about the original install date. Fresh infill can refresh the feel and drainage of an aging lawn in the meantime, but it won't reverse UV fading already visible in the fibers themselves."),
    ]
    return page("/blog/how-long-does-artificial-turf-last-in-florida/", "post",
                "Artificial Turf Lifespan in Kissimmee, FL (2026)",
                "Artificial turf typically lasts 10-20 years in Florida sun, less under heavy pet traffic. A lifespan table by use, what wears out first, and what extends it.",
                "How long does artificial turf last in Florida?",
                capsule("Quality artificial turf typically lasts 10 to 20 years in Kissimmee's sun and rain, with UV-stabilized residential turf commonly landing in the middle of that range under normal family use, according to published installer lifespan data checked in September 2026. Heavy dog traffic, full-sun exposure and skipped maintenance push a lawn toward the lower end, while shade and regular brushing push it toward the higher end."),
                body, faqs=faqs, crumbs=CRUMBS, crumb="How long turf lasts", published=PUB,
                sources=["stn-life", "magnolia-heat"],
                related=[("/turf-replacement/", "Turf removal & replacement"),
                         ("/blog/base-under-artificial-turf-florida-sandy-soil/", "What base goes under Florida turf"),
                         ("/artificial-turf-cost/", "What artificial turf costs in Kissimmee"),
                         ("/blog/how-hot-does-artificial-turf-get-in-florida/", "How hot does artificial turf get in Florida?")])


# ================================================================== 9
def p_over():
    body = "".join([
        sec("Can turf go straight over concrete, pavers or grass?",
            table("Installing artificial turf over an existing surface",
                  ["Existing surface", "Can turf go over it?", "What it needs"],
                  [["Concrete patio or pool deck", "Yes", "Drainage underlay plus glued and taped edges; can't nail into concrete"],
                   ["Pavers", "Yes", "Same drainage underlay approach; edges secured at the paver joints"],
                   ["Living sod or lawn grass", "No", "Sod and root mat stripped to bare graded soil first"],
                   ["Bare compacted dirt, no base", "No", "A proper washed-rock base has to go in before turf, same as any new lawn"],
                   ["Old, worn-out artificial turf", "No", "Old system torn out first; the base underneath is inspected and often reused"],
                   ["Existing putting-green base still draining well", "Yes", "New turf can often be seamed onto a sound existing base"]],
                  "Underlay and edging methods are ours; every yard still gets a site visit before we commit to reusing an existing surface or base.")
            + f"<p>Yes over {svc('pool', 'a concrete pool deck')} or {svc('pavers', 'a paver patio')} with the right underlay, and yes over an existing lawn once it's stripped down to bare, graded soil. What doesn't work, ever, is gluing or stapling turf directly on top of living grass, which traps moisture underneath and rots the backing within a season.</p>"),
        sec("Why can't turf just go over living grass?",
            "<p>Grass under turf keeps growing for a while in the dark before it finally dies, and as it decomposes it releases moisture and gases that have nowhere to go once turf seals the surface above it. The result is an uneven, spongy feel within months, an odor as the organic matter breaks down, and settling as the old root mat collapses unevenly beneath the new surface. None of that shows up on day one, which is exactly why it's a common shortcut on lower-end jobs. It always shows up eventually.</p>"),
        sec("What does turf over concrete or pavers need that a lawn install doesn't?",
            f"<p>A hard surface can't be graded the way soil can, so a foam or perforated drainage underlay does the job the base and native soil normally handle, moving water sideways to an existing drain or the slab's edge. Nails aren't an option on concrete, so the perimeter gets glued or mechanically fastened into the slab instead, and seams are taped and glued rather than pinned. Any existing slope or drain on the {svc('pool', 'pool deck')} or patio has to be checked and, ideally, kept working exactly as it did before turf went down, since there's no regrading a slab after the fact the way there is with soil.</p>"),
        sec("What about turf over an old paver patio with weeds in the joints?",
            f"<p>Weeds in paver joints need to be killed and cleared before the underlay goes down, since the same moisture and root pressure that pushed weeds up through the joints originally will do the same thing under turf if it's not addressed first. Uneven or heaved pavers get reset before turf covers them, because turf follows the shape of whatever is under it and won't hide a lumpy or sunken paver field the way people sometimes hope. A patio that's heaved badly enough in multiple spots is sometimes cheaper to address by resetting the whole field at once rather than chasing individual high and low pavers one at a time.</p>"
            "<p>Say you have a screened lanai in a Storey Lake vacation rental with existing pavers that pond near the drain after a hard rain. Installing turf directly over that low spot without addressing it first just moves the ponding under the turf instead of on top of it. Correcting the underlay thickness at that one low area, sloping it toward the existing drain, fixes the pattern before turf ever goes down rather than after.</p>"),
        sec("What about turf over a wooden deck or a rooftop?",
            f"<p>The same underlay logic applies to a wood deck, with an added check: the deck's structural boards and flashing need to handle the added weight and moisture cycling of turf, infill and an underlay layer over years of use, which is worth a look from whoever built or last inspected the deck rather than assumed. {svc('commercial', 'Rooftop and balcony installations')} add drainage-plane and structural-load questions specific to the building, which is why those go through a site visit before we quote a per-square-foot number the way a ground-level yard can. A building's roofing membrane and its warranty terms also come into play on a rooftop job in a way they never do on a ground-level lawn, so involving the property's roofing contractor early avoids conflicts later.</p>"),
        sec("Does turf over a hard surface behave differently day to day?",
            f"<p>It runs a little warmer than turf over soil, because the slab beneath holds heat longer after sunset the way {post('how-hot-does-artificial-turf-get-in-florida', 'concrete does in our surface-temperature comparison')}. It also drains differently: water moves sideways across the underlay to a drain point rather than straight down into soil, so the underlay's slope matters as much as the base's slope does on a soil install. Everything else, infill, brushing, UV fade, wears the same regardless of what's underneath.</p>"),
    ])
    faqs = [
        faq("Does turf over concrete get hotter than turf over soil?", f"Yes, somewhat, because the slab holds heat longer after sunset. {post('how-hot-does-artificial-turf-get-in-florida', 'Published surface-temperature data')} shows concrete running hot in its own right, and turf directly above it inherits some of that lingering warmth."),
        faq("Can turf be installed over turf that's already there?", "No. Old turf and any degraded infill underneath it need to come out first so the base can be inspected, since it's impossible to tell from the surface whether the existing base still drains and compacts correctly. Turf over pavers still needs infill the same way a lawn does, doing its normal job of holding blades upright and adding weight; the underlay and edging change, not the infill approach."),
        faq("What happens to turf laid over grass that wasn't fully removed?", "Patchy sod or lingering root mat left behind decomposes under the turf the same way a full lawn would, just in smaller, uneven pockets. It shows up as soft or sunken spots scattered across the yard rather than one uniform low area."),
        faq("Can an existing drain in a concrete patio be reused under turf?", "Usually, yes. The underlay is built to direct water toward it the same way the bare concrete did before, as long as the drain itself is clear and still functions. A drain that was already slow or partially clogged should be serviced before turf covers it and makes the problem harder to see. A drainage underlay in otherwise good condition can often stay in place under a new layer of turf during a later replacement, too, once it's inspected and its slope toward the drain is confirmed."),
        faq("Is turf over pavers noisier or harder underfoot than turf over soil?", "It can feel slightly firmer underfoot than turf over soil, since a compacted washed-rock base still has some give that a paver or concrete slab doesn't. A thicker drainage underlay narrows that gap and is worth asking about for an area where people will sit or lie on the surface often. On a rooftop or balcony, the infill rules stay the same, but weight becomes a bigger factor, so a lighter infill loading is sometimes specified once the structure's load limit is confirmed."),
    ]
    return page("/blog/install-artificial-turf-over-concrete-pavers-or-grass/", "post",
                "Artificial Turf Over Concrete, Pavers or Grass",
                "Turf can go over concrete or pavers with a drainage underlay, and over an old lawn once it's stripped to bare soil, but never glued directly onto living grass.",
                "Can artificial turf be installed over concrete, pavers or existing grass?",
                capsule("Yes over concrete and pavers with a drainage underlay and glued-down edges, yes over existing lawn grass once the sod and root mat are stripped to bare graded soil, and no, never glued or stapled directly on top of living grass, which traps moisture and rots the backing within a season, as of September 2026 for Kissimmee-area installs."),
                body, faqs=faqs, crumbs=CRUMBS, crumb="Turf over pavers or grass", published=PUB,
                sources=["sgw-faq", "magnolia-drain"],
                related=[("/pool-turf/", "Pool & lanai turf"),
                         ("/turf-and-pavers/", "Turf & pavers"),
                         ("/blog/artificial-turf-for-balconies-rooftops-and-condos/", "Artificial turf for balconies, rooftops and condos"),
                         ("/commercial-turf/", "Commercial turf")])


# ================================================================= 10
def p_toho():
    body = "".join([
        sec("What is Toho's current watering schedule, and did it just change?",
            f"<p>Anyone weighing a new {svc('residential', 'sod lawn')} against artificial turf in Toho Water Authority's service area needs the current schedule first. As of September 2026, Toho limits landscape irrigation to two days a week by address: odd-numbered addresses water Wednesday and Saturday, even-numbered addresses water Thursday and Sunday, and non-residential accounts water Monday and Friday, with no watering between 10 a.m. and 4 p.m. ({src('toho-days', 'the current posted schedule')}). That schedule follows the South Florida Water Management District's year-round two-day-a-week irrigation rule under Chapter 40E-24, F.A.C. ({xt(SFWMD, 'SFWMD landscape irrigation rule')}). Osceola County floated a separate water-conservation ordinance in 2026 that could tighten local rules further ({src('osceola-water-2026', '2026 news coverage of the proposal')}); nothing in what we've found supersedes Toho's posted schedule as of this writing.</p>"),
        sec("What is the new-sod establishment exception, exactly?",
            f"<p>Toho allows extra watering for newly installed sod for 30 days from the install date, with frequency tapering down across that window rather than staying constant: heavier watering in the first third of the period, reduced through the middle third, and down to something close to the normal two-day schedule by the end of it ({src('toho-days', 'Toho new-sod exception details')}). If a watering citation shows up during that window, the utility asks for a receipt, invoice or similar proof of the installation date to confirm the exception applies.</p>"
            + table("Watering allowance: new sod vs. an established lawn vs. artificial turf",
                    ["Situation", "Normal schedule applies?", "Special allowance", "Source"],
                    [["Newly installed sod, first 30 days", "No, a temporary exception applies", "Increased frequency, tapering down over 30 days, with proof of install date on request", src("toho-days", "Toho Water Authority")],
                     ["Established sod or lawn grass", "Yes, two days a week, no 10 a.m.-4 p.m. watering", "None beyond the standard schedule", src("toho-days", "Toho Water Authority")],
                     ["Artificial turf", "Not applicable", "None; in-ground irrigation can't be used on synthetic turf at all", src("dep-rule", "Rule 62-308.100, F.A.C.")]],
                    "Toho's schedule and exception details checked September 2026; confirm current terms directly with the utility before relying on them for a citation dispute.")),
        sec("Why is a dry spring hard on new St. Augustine sod under this schedule?",
            f"<p>St. Augustine sod needs consistent moisture in its first few weeks to root into the soil beneath it, and Central Florida's dry season, roughly October through May, is exactly when that moisture doesn't fall from the sky reliably. Sod installed early in the establishment window gets the benefit of Toho's extra watering allowance, but once that 30-day period ends, a new lawn dropped into a dry April or May has to survive on the standard two-day schedule well before its root system is deep enough to handle it, which is when thin, stressed, or dead patches most often show up.</p>"
            f"<p>Say you plant new St. Augustine sod on a builder-graded lot in Poinciana in April. The 30-day exception covers the riskiest early rooting period, but if a dry spell stretches past that window before the roots are established, the lawn is now competing with the same two-day watering limit as every established yard around it, at the exact point it can least afford the gap. {post('why-new-construction-sod-dies-in-osceola-county', 'New-construction sod failure')} traces back to this timing mismatch as often as it does to poor soil prep.</p>"),
        sec("Can established Bahia really survive on rainfall alone?",
            f"<p>Bahia has an extensive root system that gives it better drought tolerance than most other Florida lawn grasses ({xt(IFAS_BAHIA, 'UF/IFAS Gardening Solutions on Bahiagrass')}), and in our experience, established Bahia lawns around Osceola County get by on rainfall alone for long stretches outside the driest weeks of spring, going pale and semi-dormant rather than dying, then greening back once summer rain returns. That's a different plant than the St. Augustine most homeowners default to, and it's worth an honest look for anyone tired of managing a watering schedule around a lawn that could tolerate a lot more neglect. Bahia's coarser texture and open growth habit aren't for everyone, which is exactly the kind of trade-off worth weighing against a two-day watering schedule before defaulting to St. Augustine out of habit.</p>"),
        sec("Does the 30-day exception actually cover a full establishment period?",
            "<p>Not entirely, and that gap is worth planning around rather than discovering partway through a dry spring. Sod generally needs closer to six to eight weeks of consistent moisture to root deeply enough to handle a normal two-day watering schedule without stress, longer in cooler, slower-growing months. A 30-day allowance covers the most critical early rooting window but can end while a lawn is still only partly established, especially one installed in a stretch with little natural rainfall to help fill the gap. Timing an installation to land near the start of the rainy season, rather than deep in the dry season, reduces how much of that gap the irrigation schedule has to cover alone. A homeowner who can't control timing that closely, because of a builder's schedule or a real-estate closing date, is exactly who ends up calling about a struggling new lawn in May.</p>"),
        sec("Where does artificial turf fit into this debate?",
            f"<p>It skips the argument entirely, for a different reason than most people expect. It isn't that turf is exempt from watering restrictions; it's that Florida's turf rule, in force since May 19, 2026, bars using an in-ground irrigation system to water synthetic turf at all ({src('dep-rule', 'Rule 62-308.100, F.A.C.')}). There's no watering-day schedule to track, no 30-day establishment window, and no dry-spring stress period, because the only water turf ever gets is an occasional hose rinse for {post('how-hot-does-artificial-turf-get-in-florida', 'cooling, not survival')}. {svc('residential', 'A turf lawn')} simply removes the entire category of problem this article describes for sod.</p>"),
    ])
    faqs = [
        faq("Does the 30-day new-sod exception apply if turf is installed instead?", "No, because turf doesn't need it. The exception exists to help sod's roots establish; turf has no roots and no establishment period, so the watering-schedule question doesn't apply to it either way."),
        faq("What happens if Toho's restrictions change again later in 2026?", "We'll update this page if the posted schedule changes. Osceola County's broader water-conservation proposal was still under review as of our last check, so confirm the current schedule directly with Toho before planning a sod installation around it."),
        faq("Can drip irrigation be used on planting beds next to turf?", "Drip irrigation for shrubs, flowers or a vegetable bed next to a turf area is a separate system from what waters the turf itself, and it isn't affected by the turf-specific irrigation rule as long as it doesn't water the synthetic surface."),
        faq("Does St. Cloud follow the same watering schedule as Kissimmee?", "St. Cloud is also served by Toho Water Authority, so the same odd/even schedule and new-sod exception generally apply. Confirm with Toho directly if an address sits near a service-area boundary."),
        faq("Does a rain sensor override the watering-day schedule?", "A rain sensor or soil-moisture shutoff prevents an irrigation cycle from running when it isn't needed, which most Florida jurisdictions already require on automatic systems, but it doesn't grant extra watering days beyond what the schedule allows on days it does run. A private irrigation well is typically regulated by the water management district rather than Toho's utility billing, but the same Chapter 40E-24 watering-day rule generally applies regardless of the water source."),
    ]
    return page("/blog/toho-water-restrictions-new-sod-vs-turf/", "post",
                "Toho Water Restrictions: New Sod vs. Artificial Turf",
                "Toho Water limits irrigation to two days a week with a 30-day new-sod exception, as of September 2026. Artificial turf skips the schedule entirely under state law.",
                "How do Toho Water watering restrictions affect new sod vs. turf?",
                capsule("As of September 2026, Toho Water Authority limits landscape irrigation to two days a week by address, with no watering 10 a.m. to 4 p.m., though new sod gets a 30-day establishment exception with tapering frequency. Artificial turf skips the debate entirely because Florida's turf rule bars watering it with an in-ground irrigation system at all."),
                body, faqs=faqs, crumbs=CRUMBS, crumb="Toho watering vs. turf", published=PUB,
                sources=["toho-days", "osceola-water-2026", "dep-rule", SFWMD, IFAS_BAHIA],
                related=[("/blog/artificial-turf-vs-sod-cost-florida/", "Is artificial turf cheaper than sod over 10 years?"),
                         ("/blog/why-new-construction-sod-dies-in-osceola-county/", "Why builder sod dies on new-construction lots"),
                         ("/tools/turf-vs-sod/", "Turf vs. sod ten-year calculator"),
                         ("/laws/florida-hb-683/", "Florida's turf rule, water-conservation section")])


def get_pages():
    return [p_heat(), p_coolest(), p_melt(), p_urine(), p_drain(), p_hurricane(), p_base(), p_lifespan(), p_over(), p_toho()]
