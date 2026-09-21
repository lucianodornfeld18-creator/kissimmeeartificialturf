# -*- coding: utf-8 -*-
"""Service pages: residential lawns, pet turf, putting greens, playground turf."""
from _data import PRICE_DATE, PHONE_DISPLAY
from _helpers import page, capsule, sec, table, faq, ul, steps, note, cta, a, svc, city, cs, post, src, ext, price, price_note, tel

CPSC = ("CPSC — Public Playground Safety Handbook (Publication 325, 2025)", "https://www.cpsc.gov/s3fs-public/325_PublicPlaygroundSafetyHandbook2025_7-30-25_1.pdf")
ASTM_F1292 = ("ASTM F1292-22 — Standard Specification for Impact Attenuation of Surfacing Materials Within the Use Zone of Playground Equipment", "https://store.astm.org/f1292-22.html")
IPEMA = ("IPEMA — Certified Playground Surfacing certification program", "https://ipema.org/certified-product/certified-playground-surfacing/")
STIMP_SRC = ("InstallArtificial — what is stimp speed", "https://www.installartificial.com/how/what-is-stimp-speed")
NYLON_POLY_SRC = ("InstallArtificial — best turf for putting greens: poly vs. nylon vs. slit-film", "https://www.installartificial.com/how/best-artificial-putting-green-grass-poly-vs-nylon-and-slit")


# ============================================================== residential
def residential():
    body = "".join([
        sec("What is artificial grass installation in Kissimmee, FL?",
            f"<p>Artificial grass installation in Kissimmee, FL means pulling out the living lawn and building a synthetic one in its place: sod and soil removed, a compacted base shaped to drain, then turf rolled, seamed and pinned down. Installed cost runs {price('residential')} a square foot as of {PRICE_DATE}, and a typical 800 to 1,200 sq ft yard takes a two- to four-person crew two to four days from strip-out to the first walk on the new grass.</p>"
            + f"<p>Around here that's a different job than the same artificial turf installation means in Arizona. Our base has to shed a Central Florida downpour, not just sit dry for ten months a year, and the fine sand under most Osceola County lots holds water close to the surface for weeks after a wet summer. Calls that start as a search for fake grass for backyard use often end up covering the front and side yards too once the quote's in hand. {post('base-under-artificial-turf-florida-sandy-soil', 'What goes under turf on this sand')} covers the build in more depth than this page does.</p>"),

        sec("Who this fits, and who should think twice",
            "<p>Artificial turf installation suits yards where sod already struggles: heavy shade from a two-story house or a stand of live oaks, a side yard too narrow for a mower, a rental property nobody's around to water, or a homeowner tired of a chinch-bug fight every June. Replace grass with turf and the watering schedule, the mowing bill and the brown August patches all go away at once.</p>"
            + "<p>It fits less well for a large, flat, full-sun lot where St. Augustine already thrives and the owner enjoys yard work; sod there is the cheaper year-one choice. It also isn't the answer for a yard that floods after every storm: standing water is a grading problem first, and turf over a wet spot just hides the puddle instead of fixing it.</p>"),

        sec("Pile height, face weight, backing and infill for a lawn",
            "<p>Three grades cover most Kissimmee yards. The differences aren't cosmetic: a taller, denser blade resists matting in a dog's favorite path or a kid's cutting corner to the trampoline, and a heavier backing holds infill and shape through a decade of afternoon storms.</p>"
            + table("Common turf builds for residential lawns", ["Grade", "Pile height", "Face weight", "Backing", "Best for"],
                    [["Economy", "1.25–1.5 in", "50–65 oz/sq yd", "Perforated polyurethane", "Rental homes, side yards, budget-first jobs"],
                     ["Standard lawn blend", "1.5–1.9 in", "65–90 oz/sq yd", "Perforated polyurethane, reinforced", "Front yards, backyards, most families"],
                     ["Premium / showcase", "1.75–2.25 in", "90–110 oz/sq yd", "Fully permeable, double-stitched", "Full-sun front lawns, heavy foot traffic"]],
                    "Face weight is the weight of fiber per square yard, not the whole roll; higher usually means denser blades and slower matting. Infill for a plain lawn is typically silica sand at roughly 1–2 lb per sq ft.")
            + f"<p>Blade color and shape matter as much as the numbers. {post('artificial-turf-pile-height-and-face-weight', 'Pile height and face weight, explained plainly')} and {post('best-artificial-grass-for-florida', 'what holds up in Florida sun')} go further than a spec table can, and the {a('/compare/nylon-vs-polyethylene-vs-polypropylene-turf/', 'fiber comparison')} covers why almost every residential lawn here is polyethylene, not nylon or polypropylene.</p>"),

        sec("How we build a lawn on Kissimmee sand",
            "<p>The turf on top is the easy part. What decides whether a front yard or backyard stays flat through a rainy season is the work nobody sees again once the grass is down.</p>"
            + steps([("Strip and haul.", "Existing sod, thatch and 3 to 4 inches of soil come out, because organic matter left under turf rots and settles unevenly within a year or two."),
                     ("Grade the subgrade.", "The bare soil is sloped 1 to 2 percent away from the house, matching wherever the lot already sheds water, usually a side swale or the rear property line."),
                     ("Compact the base in lifts.", "Washed, open-graded crushed rock or crushed concrete goes down 2 to 4 inches deep in two passes, each run over with a plate compactor before the next layer, packed firm without sealing off the native sand underneath so it still percolates."),
                     ("Cap the sprinklers.", "Any spray head that used to water the area gets capped at the valve box; the state's synthetic turf rule bars watering turf from an in-ground system, so a hose bib does the rinsing from here on."),
                     ("Roll, seam and trim.", "Rolls run in the same direction so the grain matches from one panel to the next, seams are cut between stitch rows and bonded with seam tape and adhesive rather than left to nails alone."),
                     ("Anchor the perimeter.", "Edges get galvanized nails every few inches or a bender-board and paver border where turf meets a bed, satisfying the state's requirement that edges and seams hold through wind and standing water."),
                     ("Infill and groom.", "Silica sand goes in at roughly 1 to 2 lb per sq ft, power-brushed against the grain so the backing stays weighted and the blades stand up instead of lying flat.")])
            + f"<p>{post('how-artificial-turf-is-installed-step-by-step', 'The full walkthrough')} has photos of each stage; {post('artificial-turf-on-a-slope', 'installing on a sloped lot')} covers what changes when the yard itself isn't flat.</p>"),

        sec("What artificial grass installation costs in Kissimmee",
            f"<p>Installed synthetic lawn runs {price('residential')} per square foot as of {PRICE_DATE}, with most Osceola and south Orange County yards landing between {price('residential', True)}. A 600 sq ft pool-home backyard usually prices near $6,600 to $9,600; a 1,200 sq ft corner lot in St. Cloud can run $12,000 to $19,200. Turf itself is under half of that; the rest is demolition, base material, compaction labor and edging.</p>"
            + table("What moves a residential quote up or down", ["Driver", "Effect on price", "Why"],
                    [["Gate width and access", "+$1–$3/sq ft below 36 in", "Wheelbarrows and hand tools replace a skid steer"],
                     ["Existing lawn condition", "+$0.50–$1.50/sq ft", "Thick St. Augustine thatch takes longer to strip than thin Bahia"],
                     ["Drainage correction", "+$500–$2,000 flat", "Low spots need extra base or a drain line before turf goes down"],
                     ["Shape and cuts", "+$0.50–$2/sq ft", "Curved beds, tree rings and stepping-stone cutouts waste more roll"],
                     ["HOA or ARC review", "No material cost, adds time", "A sample, spec sheet and site plan usually take one review cycle"]],
                    price_note())
            + f"<p>The {a('/artificial-turf-cost/', 'full turf cost guide')} breaks the number down further by yard size and compares it against sod over ten years; the {a('/artificial-turf-cost/calculator/', 'cost calculator')} does the arithmetic for your own measurements.</p>"
            + "<!--AUTO:service-cities-->"),

        sec("What Central Florida does to a new lawn",
            f"<p>Summer sun heats synthetic turf faster than it heats grass. Published measurements put a full-sun Florida lawn at 120 to 150 °F at the surface, occasionally past 160 °F, while natural grass stays close to air temperature ({src('magnolia-heat', 'Florida installer readings')}; {src('horsemans-heat', 'a second set of summer measurements')}). A 30-second hose rinse drops that 30 to 50 degrees within minutes, and a lighter-colored or cooling infill helps more than shade cloth does on a west-facing front yard.</p>"
            + "<p>Afternoon storms are the other constant: a typical June-through-September cell can drop an inch or two of rain in under an hour. Perforated turf backing passes water faster than 30 inches an hour on its own, so a yard that puddles after turf goes in almost always has a base or grading problem, not a drainage problem with the turf itself.</p>"
            + "<p>Two details catch installers who haven't worked here before. Low-emissivity glass on a south- or west-facing window can reflect enough sunlight to soften polyethylene blades, which start to give around 175 to 200 °F. And a live oak's roots run well past its canopy, so turf has to stop at the drip line unless a certified arborist signs off on going closer.</p>"),

        sec("HOA rules, state law and permits",
            f"<p>Two different rules apply, and they don't overlap the way people expect. {a('/laws/florida-hb-683/', 'HB 683')}, in effect since July 2025, keeps a city or county from banning synthetic turf on a single-family lot of an acre or less once it meets the state's adopted DEP standard, Rule 62-308.100, in force since May 19, 2026 ({src('dep-rule', 'the adopted rule text')}). That law says nothing about a homeowners association.</p>"
            + "<p>The rule itself: subgrade must be washed, open-graded crushed rock or crushed concrete that still lets water percolate below; lawn infill is limited to silica sand, rock, shell or other natural material, with coated silica sand allowed only if the coating is non-toxic; edges and seams are anchored against wind and flooding; and the septic tank lid stays reachable for pump-out. Turf stays 10 feet from a lake, pond or canal unless a seawall already separates the two, and never inside a swale, ditch or pond's littoral zone.</p>"
            + f"<p>For an HOA, the statute that matters is F.S. 720.3045: an association can't restrict what's installed somewhere it isn't visible from the street or a neighboring lot, and artificial turf is named specifically. A fenced backyard is protected; a front yard still goes through architectural review in most Osceola and Orange County communities. {a('/laws/hoa-rules/', 'What a Florida HOA can and can’t restrict')} and the {a('/laws/permits/', 'permit guide by jurisdiction')} cover the paperwork side, none of it legal advice.</p>"),

        sec("What a bad turf job looks like a year later",
            "<p>Both a careful install and a rushed one look identical on handoff day. The rushed one shows itself after the first real rainy season: seams that were nailed instead of taped start to gap at the corners, a base that was compacted in one thick pass settles into a shallow dip near a downspout, and a yard that was never graded away from the foundation sends water toward the slab instead of the swale.</p>"
            + f"<p>The other tell is a lawn that looks flat but smells or discolors within a season, usually because a crew skipped the compaction step to save a day or used unwashed fill instead of washed, open-graded crushed rock. {post('artificial-turf-pros-and-cons', 'An honest look at turf’s tradeoffs')} and {post('what-does-artificial-turf-warranty-cover', 'what a warranty actually covers')} both go into what separates a lawn that lasts from one that doesn't.</p>"),

        sec("Living with a synthetic lawn",
            f"<p>Rinse it occasionally with a hose, more often if a dog uses it, to settle infill and clear pollen. Blow or rake leaves off before they break down into the blades, especially during the live oak drop in late winter. Brush the highest-traffic path a few times a year against the grain so blades stand back up, or have it {svc('cleaning', 'power-broomed and topped off with infill')} once a year. After a tropical storm, walk the perimeter and call about anything that's lifted; a corner caught early is a small {svc('repair', 'repair')}, not a re-lay.</p>"
            + f"<p>A lawn built this way lasts 10 to 20 years depending on UV stabilization and traffic ({src('stn-life', 'manufacturer lifespan data')}). When it finally fades, the base underneath is usually still sound, which is what makes {svc('replacement', 'replacing just the turf')} cheaper than the original install.</p>"),

        sec("How do you pick the best artificial grass contractor near you?",
            "<p>You can't judge the work on the day it's finished; a good base and a shortcut base look the same until the first real storm. Synthetic turf installers vary widely in what they'll put in writing, so judge the bid, not the pitch. Ask for the base depth and material in writing, whether seams are taped and glued or just nailed, where the water is supposed to go once the yard is covered, and the product's pile height and face weight by name, not \"premium turf.\"</p>"
            + f"<p>A local business tax receipt and a certificate of insurance sent straight from the agent are worth more than a sales pitch. {post('best-artificial-turf-contractor-kissimmee', 'A longer checklist for choosing a Kissimmee contractor')} and {post('how-to-compare-artificial-turf-quotes', 'how to read two bids side by side')} go through this in detail, and {post('do-turf-installers-need-a-license-in-florida', 'whether Florida licenses turf installers at all')} explains why a business tax receipt, not a state license, is what to ask for.</p>"
            + cta("Get a measured quote")),
    ])
    faqs = [
        faq("Can artificial grass go in a front yard in Florida?", "Yes. Nothing in state law bans a front lawn of synthetic turf, and the DEP standard that took effect in May 2026 applies statewide to single-family lots of an acre or less. Front yards do usually need HOA architectural review, since F.S. 720.3045 only protects areas not visible from the street."),
        faq("Is a sod-to-turf conversion messier than a new install?", "About the same. Removing living St. Augustine takes slightly longer than removing a dead or thin lawn because the root mat holds together, but the base build underneath is identical either way."),
        faq("Can you install over an existing side yard that never grew grass?", "Usually, yes, and it's one of the more common calls we get. A side yard with heavy shade or AC condensate dripping on it often has compacted, unhealthy soil already, so it needs the same strip-and-rebuild as any other yard, not a shortcut."),
        faq("Do you install synthetic lawn in the backyard only, or the whole property?", "Either. Many owners start with a backyard and leave the front lawn natural for now, or the reverse. Pricing is by square footage, so partial-yard jobs are common and normal."),
        faq("How long before I can walk on a new lawn?", "Right away. Unlike sod, there's no establishment period. The infill settles a bit more over the first few rinses and rains, but the lawn is usable the day the crew leaves."),
        faq("Will turf color match across two yard sections?", "Only if it comes from one dye lot. Mixing rolls from different production runs is the most common cause of a visible seam line between sections."),
        faq("What if I only want part of the yard converted now and the rest later?", f"That's workable; we note the product and infill used so a second phase matches. Call or text {PHONE_DISPLAY} with rough measurements and we'll talk through sequencing."),
    ]
    return page(SERVICES_ROUTE["residential"], "service",
                "Artificial Grass Installation in Kissimmee, FL",
                f"Artificial grass installation in Kissimmee, FL costs {price('residential')} per sq ft installed as of {PRICE_DATE}. Base specs, cost drivers and Florida rules inside.",
                "Artificial Grass Installation Built for Kissimmee's Sandy Soil",
                capsule(f"Artificial grass installation in Kissimmee, FL runs about {price('residential')} per square foot installed as of {PRICE_DATE}, with most yards landing between {price('residential', True)}. A typical 800 to 1,200 sq ft lawn takes two to four days once the old sod is stripped, a compacted base is built, and turf is seamed, edged and infilled."),
                body, faqs=faqs, service="residential", crumbs=[("Services", "/services/")], crumb="Grass Installation",
                sources=["attampa-cost", "lbs-fl-cost", "magnolia-heat", "horsemans-heat", "sgw-faq", "stn-life", "hb683", "dep-rule", "marathon-pr", "fs7203045", "usda-wss"],
                related=[("/artificial-turf-cost/", "Full turf cost guide with tables"), ("/blog/artificial-turf-front-yard-florida/", "Can you put turf in a Florida front yard?"),
                         ("/blog/artificial-grass-for-shady-side-yards/", "Options for shady side yards"), ("/compare/artificial-turf-vs-st-augustine-zoysia-bahia/", "Turf vs. St. Augustine, Zoysia and Bahia"),
                         ("/blog/how-artificial-turf-is-installed-step-by-step/", "The full installation walkthrough")])


# ============================================================== pet
def pet():
    body = "".join([
        sec("What is pet turf installation in Kissimmee, FL?",
            f"<p>Pet turf installation in Kissimmee, FL builds a synthetic lawn specifically for dogs: a fully permeable backing instead of a semi-perforated one, no weed barrier underneath to trap urine, and infill chosen to control odor rather than just cushion a footstep. It costs {price('pet')} a square foot as of {PRICE_DATE}, more than a plain residential lawn, because the base and the infill both do more work.</p>"
            + f"<p>Dog runs, fenced side yards, a dedicated dog potty area and full backyards are all common projects. A narrow K9 turf run down the side of the house is often the first phase, with the rest of the yard following once the owner sees how it holds up. {svc('residential', 'Regular lawn turf')} and pet-friendly artificial grass share a base; what changes is the backing, the weed barrier and the infill.</p>"),

        sec("Is artificial grass good for dogs?",
            "<p>Yes, when it's built for them. A permeable backing that drains fast, no weed fabric underneath to hold urine, and an odor-control infill make artificial grass for dogs a durable, easy-to-rinse surface that holds up better than St. Augustine under daily traffic and digging. Built like a plain residential lawn instead, it will smell by the second summer and the backing can trap standing urine against the base.</p>"
            + "<p>The difference isn't the turf blade at all; polyethylene fiber is the same material either way. It's the three layers underneath: whether water and liquid pass straight through the backing, whether a weed barrier is sitting there holding it back, and whether the infill is inert sand or something formulated to bind ammonia. Dogs also do better on a shorter, denser pile that resists matting along a fence-line patrol path, and a flush-out zone near a hose bib gives a place to rinse daily without soaking the whole run.</p>"
            + f"<p>{post('pet-turf-vs-regular-artificial-grass', 'Pet turf vs. regular artificial grass, in detail')} walks through the backing and infill differences product by product.</p>"),

        sec("Turf and infill built for a dog yard",
            table("Pet turf components and what they change", ["Component", "Common options", "What it does for a dog yard"],
                  [["Pile height", "0.75–1.25 in for runs; 1.25–1.5 in for shared yards", "Shorter fiber resists matting along a fence-patrol path"],
                   ["Backing", "Fully permeable, no latex coating", "Liquid drains straight through instead of pooling on a semi-solid backing"],
                   ["Infill", "Zeolite, antimicrobial-coated sand, or none", "Zeolite binds ammonia; coated sand resists bacteria; some fully-drained systems skip infill entirely"],
                   ["Weed barrier", "Omitted under pet areas", "A fabric layer under turf holds urine against the base instead of letting it pass through"],
                   ["Flush zone", "A hose bib and slight slope to a drain point", "Gives daily rinsing somewhere to go besides sitting in the yard"]],
                  "K9 turf for boarding or daycare runs usually goes to the shorter pile height and heavier infill weight; a family backyard with one dog can use a taller, softer blend.")),

        sec("How we build a base a dog can't wreck",
            "<p>The build starts the same as any lawn and diverges at the weed barrier and the drainage layer.</p>"
            + steps([("Strip the sod.", "Grass, thatch and 3 to 4 inches of soil come out, same as any conversion."),
                     ("Grade toward a flush point.", "The subgrade slopes 1 to 2 percent toward a drain or the yard's low corner, not just away from the house, so rinse water and rain both have somewhere to go."),
                     ("Build a deeper, coarser base.", "3 to 4 inches of washed, open-graded crushed rock or crushed concrete, compacted in two lifts, gives urine and rinse water a fast path down instead of pooling at the surface, without packing the native sand below so tight that it quits draining."),
                     ("Skip the weed barrier.", "Fabric that would normally go between base and turf is left out under pet areas because it holds liquid against the base instead of letting it pass."),
                     ("Cap irrigation, add a hose bib.", "Sprinkler heads in the area are capped, and if there's no spigot nearby we recommend adding one, since rinsing here is more frequent than on a plain lawn."),
                     ("Seam, edge and infill.", "Seams are taped and glued, edges nailed or bordered, and zeolite or antimicrobial-coated sand goes in at a slightly heavier rate than a standard lawn to keep up with daily use.")])
            + f"<p>{post('how-to-get-dog-urine-smell-out-of-artificial-turf', 'What to do if odor is already a problem')} covers rescuing a yard that wasn't built this way from the start.</p>"),

        sec("How much does pet turf cost?",
            f"<p>Pet turf installation runs {price('pet')} per square foot as of {PRICE_DATE}, with most Osceola and Orange County dog yards landing between {price('pet', True)}. A 300 sq ft dog run typically prices between $3,600 and $4,800; a full 1,000 sq ft backyard for two dogs runs roughly $12,000 to $16,000. The premium over a plain lawn is usually $1.50 to $3 a foot, covering the deeper base, the omitted weed barrier's extra grading time and the infill upgrade.</p>"
            + table("What adds to a pet turf quote", ["Driver", "Typical add", "Why"],
                    [["Zeolite or antimicrobial infill", "+$0.50–$1.50/sq ft", "Coated or mineral infill costs more than plain silica sand"],
                     ["Deeper drainage base", "+$0.50–$1/sq ft", "3–4 in of washed crushed rock instead of 2–3 in, to move liquid faster"],
                     ["Multiple dogs or a boarding run", "+$0.25–$0.75/sq ft", "Heavier traffic calls for a denser, shorter pile and a flush zone"],
                     ["Adding a hose bib", "+$150–$400 flat", "Not every dog-yard project has one nearby already"]],
                    price_note())
            + "<!--AUTO:service-cities-->"),

        sec("Heat, storms and where the state draws lines for a dog yard",
            f"<p>Full Florida sun pushes synthetic turf to 120 to 150 °F at the surface and occasionally past 160 °F ({src('magnolia-heat', 'Florida installer measurements')}). A dog yard needs at least one shaded corner or a rinse routine timed before the hottest part of the afternoon; a light-colored or cooling infill takes the edge off but doesn't replace shade entirely. Afternoon storms are routine from June through September, and a properly built dog run drains faster than the rain falls, since perforated turf passes over 30 inches of water an hour on its own ({src('sgw-faq', 'drainage rate data')}).</p>"
            + "<p>The same statewide rules apply to a dog run as anywhere else on the lot: turf stays outside a live oak's drip line, on either side of the property line, unless a certified arborist signs off, sprinkler heads under the area are capped rather than left running, and a run near a pond or canal has to sit at least 10 feet back from the water unless a seawall already separates the two. A run can't be routed through a drainage swale or a ditch either, even if that's the flattest, driest-looking strip of yard.</p>"
            + "<p>One more Kissimmee-specific check: a screened pool cage or a low-emissivity window facing a dog run can reflect enough sun to soften the blades along that edge, since polyethylene starts to give around 175 to 200 °F. It's worth a look at any west- or south-facing glass near the run before committing to a layout.</p>"),

        sec("HOA rules and Florida law for a dog run",
            f"<p>A fenced backyard dog run is usually the easiest artificial turf project to get past a homeowners association, because F.S. 720.3045 protects anything not visible from the street or a neighboring parcel, and the statute names artificial turf directly. A side-yard run visible from the sidewalk is a different story and typically needs the same {a('/laws/hoa-rules/', 'architectural review')} as a front lawn.</p>"
            + f"<p>Statewide, {a('/laws/florida-hb-683/', 'HB 683')} and the DEP rule it created, adopted as Rule 62-308.100 and in force since May 19, 2026 ({src('dep-rule', 'the adopted rule text')}), keep a city or county from banning turf on a single-family lot of an acre or less once it meets the state standard. That standard is why a dog run's infill has to stay in the natural-material column, silica, zeolite or coated sand, rather than crumb rubber or any other synthetic infill, which the rule reserves for the ground under playground equipment. Check the {a('/laws/permits/', 'permit page for your jurisdiction')} for anything a specific city adds on top.</p>"),

        sec("What a bad pet turf job smells like by August",
            "<p>The tell isn't visible, it's olfactory. A yard built with a weed barrier under the turf, standard lawn infill instead of zeolite, or a base that's too shallow to drain fast will hold ammonia against the backing no matter how often it's rinsed. The smell typically shows up within one summer, not right away, which is why it's easy for a rushed installer to hand the job off looking fine.</p>"
            + f"<p>The fix usually isn't a full tear-out. Pulling the turf, adding drainage or removing a weed barrier, and switching infill can solve it without redoing the whole base. {svc('cleaning', 'A pet-odor treatment and infill refresh')} handles milder cases; a {svc('repair', 'partial rebuild')} is worth it when the base itself never drained.</p>"),

        sec("Keeping a dog yard from smelling by the second summer",
            "<p>Rinse two to three times a week in warm months, more if there are multiple dogs, and pick up solid waste daily rather than letting it break down into the infill. An enzyme-based deodorizer applied monthly through summer helps more than an occasional deep clean. Brush against the grain every few weeks to keep the pile from matting along a fence-patrol route, and check the flush zone after heavy rain to confirm it's still draining as designed.</p>"),

        sec("What should the best pet turf installer near me get right?",
            "<p>Ask what backing the product uses and whether a weed barrier goes under the pet area; the right answers are fully permeable and no. Ask what infill is proposed and why, not just its brand name, since zeolite and antimicrobial-coated sand solve slightly different problems. Ask where the base drains to and whether a hose bib is within reach of a hose, not a fifty-foot walk.</p>"
            + f"<p>Anyone answering \"our standard turf\" to all three questions is describing a residential lawn, not a pet system. {post('pet-turf-vs-regular-artificial-grass', 'This comparison')} lists the specific products and specs worth asking for by name.</p>"
            + cta("Get a measured quote", "Tell us about the dogs, the fence line and any spot that already smells.")),
    ])
    faqs = [
        faq("Can artificial turf burn my dog's paws?", "It can if a dog walks across an unshaded run in peak afternoon sun, since the surface can reach 120 to 150 °F or more. A shaded area, a quick hose rinse before playtime and scheduling outdoor time before mid-afternoon in summer avoid the problem; check the surface with your own hand first on a hot day."),
        faq("Can dogs dig through or chew artificial turf?", "A determined digger can pull at a poorly secured edge or an unglued seam, which is why pet-area perimeters get nailed every few inches and seams are taped and glued rather than just butted together. Chewing on the blades themselves is rare once a dog is past the puppy stage, and most damage seen on repair calls is at an edge, not mid-yard."),
        faq("Do fleas and ticks live in artificial grass?", "Less readily than in natural grass, since there's no organic thatch layer or soil for eggs and larvae to develop in, but turf isn't a flea-proof surface on its own. Regular rinsing, sweeping out organic debris and standard pet flea prevention still matter as much as they would on a natural lawn."),
        faq("How often do I need to replace infill in a dog run?", "Expect to top it off, not fully replace it, every one to two years depending on how many dogs use the area. Rinsing and UV exposure gradually reduce the volume, and a thin infill layer is the most common reason an older pet yard starts to smell again."),
        faq("Does pet turf need a fence to work?", "No, though most projects have one already for the dog's safety rather than the turf's. Unfenced yards get the same build; the only difference is that boundary and containment become the owner's concern, not the turf's."),
        faq("Can I install pet turf around an existing pool cage?", f"Yes, and it's a common combination in Osceola County pool homes. The base and drainage plan are the same; access through a screen door usually just means smaller equipment and a slightly longer timeline. Call or text {PHONE_DISPLAY} to talk through a specific layout."),
        faq("Is zeolite infill safe if a dog eats a mouthful of it?", "Zeolite is a natural mineral used specifically because it's inert and low-risk in small amounts, but no infill is meant to be eaten regularly. A dog that repeatedly mouths infill is worth mentioning to a vet regardless of which product is used."),
    ]
    return page(SERVICES_ROUTE["pet"], "service",
                "Pet Turf Installation in Kissimmee, FL",
                f"Pet turf installation in Kissimmee, FL costs {price('pet')} per sq ft as of {PRICE_DATE}. What makes turf good for dogs, infill choices, cost drivers and care.",
                "Pet Turf Installation for Florida Dog Yards",
                capsule(f"Pet turf installation in Kissimmee, FL typically costs {price('pet')} per square foot installed as of {PRICE_DATE}, with most dog yards landing between {price('pet', True)}. A permeable backing, no weed barrier, and zeolite or antimicrobial infill are what keep a 300 to 1,000 sq ft dog area from smelling by the second summer."),
                body, faqs=faqs, service="pet", crumbs=[("Services", "/services/")], crumb="Pet Turf",
                sources=["magnolia-pet-cost", "installartificial-pet", "sgw-faq", "magnolia-heat", "stn-life", "watersavers-pfas", "mtsinai-turf", "hb683", "dep-rule", "marathon-pr", "fs7203045"],
                related=[("/blog/pet-turf-vs-regular-artificial-grass/", "Pet turf vs. regular artificial grass"), ("/blog/how-to-get-dog-urine-smell-out-of-artificial-turf/", "Getting urine odor out of turf"),
                         ("/compare/zeolite-vs-silica-vs-antimicrobial-infill/", "Zeolite vs. silica vs. antimicrobial infill"), ("/artificial-turf-cost/", "Full turf cost guide"),
                         ("/blog/coolest-artificial-grass-and-infill-for-florida/", "The coolest infill for Florida sun")])


# ============================================================== putting
def putting():
    body = "".join([
        sec("What is backyard putting green installation in Kissimmee, FL?",
            f"<p>Backyard putting green installation in Kissimmee, FL means shaping a small piece of the yard into a contoured, true-rolling surface: a crowned or breaking sub-base under a short synthetic putting surface, edged with a taller fringe turf and set with one or more cups. It runs {price('putting')} a square foot as of {PRICE_DATE}, more than a lawn, because the base is sculpted by hand and the surface product is chosen for ball roll rather than looks.</p>"
            + f"<p>Most residential greens in Osceola and Orange County run 300 to 800 sq ft, tucked into a back corner or wrapped around an existing pool deck. A simple flat pad with one cup is a weekend-scale project; a multi-tier green with breaks and a chipping green area takes longer to shape and costs more per foot. Whether a homeowner calls it an artificial putting green, a synthetic putting green or just a home putting green, all three describe the same build. {svc('residential', 'A surrounding lawn')} usually gets built at the same time so the two surfaces meet cleanly.</p>"),

        sec("Is a backyard green right for your yard?",
            "<p>A putting green fits a yard with at least a few hundred square feet of reasonably level, sun-reachable space and an owner who'll actually use it; the ones that get the most use tend to sit somewhere visible from a lanai or kitchen window rather than tucked out of sight. It works in shade better than a natural green would, since the surface doesn't need sunlight to survive, though full shade all day can leave the turf feeling permanently damp underfoot after rain.</p>"
            + "<p>It fits less well on a lot with no flat run at all, since even a small green needs a stable, gently sloped pad to hold its shape, and on a lot where the only open space sits inside a live oak's root zone, where excavation for the shaped base has to stay shallow. A chipping pad instead of a full green is often the better answer on a tight or heavily treed lot.</p>"),

        sec("Putting green turf: nylon vs. polypropylene, and what stimp speed?",
            f"<p>Nylon is the more durable, longer-lasting fiber for a putting surface, typically holding up 10 to 15 years under regular play, while polypropylene is softer, cheaper and more prone to matting over 3 to 5 years of heavy use ({ext(NYLON_POLY_SRC[1], 'a side-by-side comparison of both fibers')}). Ball roll speed, measured on a stimpmeter, comes mostly from the surface's texture and grooming rather than which plastic it's made from: backyard greens typically stimp 10 to 12, with 7.5 considered slow and 14 considered fast for a home installation, against roughly 12 for tour-level professional greens ({ext(STIMP_SRC[1], 'stimp speed reference ranges')}).</p>"
            + table("Putting green surface options", ["Fiber", "Feel and durability", "Typical stimp", "Best for"],
                    [["Nylon", "Firm, consistent roll; most abrasion-resistant", "10–13", "Daily players, full-sun greens, longer-term investment"],
                     ["Textured polyethylene", "Softer chip feel around the fringe", "N/A (fringe, not putting surface)", "The taller collar around the green, not the putting surface itself"],
                     ["Polypropylene", "Realistic look, lower cost, mats sooner under heavy traffic", "8–11", "Occasional players, budget-conscious builds"]],
                    "Grooming, nap direction and how tightly the surface is stitched affect roll as much as fiber type. Ask an installer for a stimp reading on their own sample, not just a spec sheet number.")
            + f"<p>Whichever fiber a quote specifies, ask to see the golf green turf sample rolled out in the sun, not just under a showroom light; grain direction shows up differently outdoors. {a('/compare/nylon-vs-polyethylene-vs-polypropylene-turf/', 'The full fiber comparison')} and {post('artificial-turf-glossary', 'the turf glossary')} define stimp, nap and the other terms that show up on a putting green quote.</p>"),

        sec("Shaping and building a green on Kissimmee sand",
            "<p>A putting green base is a smaller, more precise version of a lawn base, built to hold contours instead of a flat plane.</p>"
            + steps([("Design the breaks.", "Slopes and tiers are laid out first, since the base has to hold whatever shape the green is meant to play, not just drain."),
                     ("Excavate to depth.", "4 to 6 inches typically comes out, deeper than a lawn, to leave room for a thicker shaped base without raising the green above grade."),
                     ("Build and shape the base in lifts.", "Washed, open-graded crushed rock or crushed concrete goes down 3 to 4 inches deep in two compacted lifts, hand-shaped into the designed breaks rather than screeded flat, with an overall 1 to 2 percent slope still carried toward the yard's drainage path and the native sand below left able to drain."),
                     ("Cap irrigation at the edge.", "Any sprinkler zone crossing the green's footprint is capped or rerouted around it, since the state's turf rule bars watering synthetic surfaces with an in-ground system."),
                     ("Lay the putting surface and fringe separately.", "The short nylon or polypropylene putting surface and the taller fringe turf are cut and seamed as separate pieces so the transition reads as a mowing line, not a patch."),
                     ("Set cups and edging.", "Cups are cored through the base at the design locations, and the perimeter is secured with bender board or paver edging so mower-line crispness holds over time."),
                     ("Infill and roll-test.", "A thin, even layer of silica sand, the same natural-material infill the state allows on any home lawn, goes in and the surface gets rolled and checked for speed before the crew leaves, adjusting brush direction if the roll pulls to one side.")])),

        sec("What does a backyard putting green cost in Kissimmee?",
            f"<p>Backyard putting green installation runs {price('putting')} per square foot as of {PRICE_DATE}, with most projects landing between {price('putting', True)}. A 400 sq ft green with a fringe collar and two or three cups typically prices between $7,200 and $10,000; adding a chipping pad or extra tiers pushes toward the top of the range.</p>"
            + table("What changes a putting green quote", ["Driver", "Typical add", "Why"],
                    [["Contouring and breaks", "+$2–$5/sq ft", "Hand-shaping a sculpted base takes longer than screeding flat"],
                     ["Number of cups", "+$150–$300 each", "Each cup is cored, set and edged individually"],
                     ["Chipping pad", "+$1,500–$4,000 flat", "A separate turf zone, often with a different pile height for lie realism"],
                     ["Fringe turf area", "+$3–$6/sq ft of fringe", "A taller collar product priced and installed separately from the putting surface"],
                     ["Nylon vs. polypropylene surface", "+$2–$4/sq ft for nylon", "Nylon costs more per yard and lasts longer under daily play"]],
                    price_note())
            + "<!--AUTO:service-cities-->"),

        sec("Heat, storms and tree roots around a green",
            f"<p>A putting surface gets as hot as any other turf in full sun, 120 to 150 °F and occasionally more ({src('magnolia-heat', 'Florida heat measurements')}), which matters most for bare feet and for how a ball rolls; extreme surface heat can make a nylon green feel slightly faster as the fiber stiffens, though grooming has a bigger effect than temperature does. A shaded green plays a touch slower and stays far more comfortable to use at 4 p.m. in July.</p>"
            + "<p>Afternoon storms need to be planned into the base, not just the turf: a contoured green with poor drainage holds water in its low tiers after a downpour instead of shedding it, so the washed crushed-rock base under a green is built to drain fast even while carrying a shape. The same statewide limits apply here as anywhere else on the lot: turf stays 10 feet back from a pond or canal unless a seawall already separates the two, out of a live oak's drip line without an arborist's sign-off, and outside any swale that carries stormwater off the property.</p>"
            + "<p>Pool cages built around a green are common in Kissimmee and worth a second look for low-emissivity glass: a west-facing screen door or window can throw enough reflected sun to soften a putting surface's edge, since polyethylene fringe starts to give around 175 to 200 °F even though the nylon putting surface itself tolerates heat better.</p>"),

        sec("HOA review and Florida law for a putting green",
            f"<p>A putting green is still artificial turf under Florida law, so the same two rules apply as to a lawn: {a('/laws/florida-hb-683/', 'HB 683')} and its DEP rule stop a city or county from prohibiting turf that meets the state's permeability and setback standard on a single-family lot up to an acre, and F.S. 720.3045 protects a green that isn't visible from the street or a neighboring lot from HOA restriction. Because greens are often built in a backyard already screened by a fence or pool cage, they tend to clear architectural review more easily than a front-yard lawn, though {a('/laws/hoa-rules/', 'confirming what your specific community asks for')} and checking the {a('/laws/permits/', 'local permit page')} before digging still saves a redo.</p>"),

        sec("What a poorly built green looks like in a year",
            "<p>The most common failure isn't the turf, it's the shape underneath losing its breaks. A base that wasn't compacted evenly in the low tiers settles unevenly, and a green that used to roll true develops a dead spot or an unintended break within a season. Seams between the putting surface and the fringe that were cut on the wrong line show up as a visible ridge where a ball catches instead of rolling through.</p>"
            + "<p>Ponding in a low tier after a storm is the other common complaint, usually traced back to a base that was shaped for looks rather than drainage. Most of these are fixable without a full rebuild if caught early; a green that's settled badly over years is closer to a full-base replacement.</p>"),

        sec("Keeping the roll true",
            "<p>Brush the putting surface lightly against the grain every few weeks to keep the nap consistent, since roll speed drifts more from grooming than from age. Clear leaves and pine needles promptly, especially from low spots where debris collects and breaks down into the infill. A light infill top-up every year or two keeps the surface playing the way it did when it was new, and an occasional check of the cups after a storm catches any that have worked loose.</p>"),

        sec("How do you find the best putting green installer near you?",
            "<p>Ask to see the base plan before the fiber samples: how deep the excavation goes, how the breaks are shaped, and how drainage is handled in the low tiers. Ask what the quoted stimp speed is based on and whether it's been tested on that installer's own work, not copied from a manufacturer's brochure. A green is one of the few turf projects where craftsmanship, not just material choice, decides whether it plays well.</p>"
            + f"<p>{post('backyard-putting-green-cost-florida', 'A closer look at what drives putting green pricing in Florida')} and the {a('/compare/local-turf-installer-vs-national-franchise/', 'local vs. franchise comparison')} are worth reading before signing a contract for this particular project, since shaping work varies more between installers than lawn installation does.</p>"
            + cta("Get a measured quote", "We'll walk the space, talk through breaks and cup count, and put the build in writing.")),
    ])
    faqs = [
        faq("How many cups can fit on a small backyard green?", "Most 300 to 500 sq ft greens hold one to three cups comfortably without the breaks feeling cramped. Packing in more than that on a small pad usually shortens the useful putting line between them more than it adds practice value."),
        faq("Does a putting green need full sun?", "No. Since the surface is synthetic, it doesn't need sunlight to stay healthy the way natural grass does, so a shaded backyard corner that would never grow a real green works fine for a turf one."),
        faq("Can I add a chipping pad later instead of all at once?", "Yes, as long as the area for it is planned into the original grading so a second phase ties into the same base height and drainage path. Adding it as a total afterthought sometimes means rebuilding an edge."),
        faq("How long does a backyard putting green take to install?", "A straightforward 300 to 500 sq ft green with modest breaks usually takes three to five days from strip-out to a rolled, playable surface; heavier contouring or a chipping pad adds a day or two."),
        faq("Do I need a specific type of cup or flagstick?", "Standard 4.25-inch golf cups fit any regulation-sized hole, and most residential greens use them. Flagsticks are a personal preference and not a structural part of the install."),
        faq("Will tree roots damage a putting green over time?", "Roots that grow under a shallow base can eventually push it out of shape, which is one reason greens are kept outside a live oak's drip line. Away from major roots, a well-compacted base is stable long-term."),
        faq("Can an existing green be resurfaced without redoing the base?", "Often, yes, if the base itself never settled or shifted. A worn or faded putting surface can usually be pulled and replaced on the same shaped base, which is considerably cheaper than a full rebuild."),
    ]
    return page(SERVICES_ROUTE["putting"], "service",
                "Backyard Putting Green Installation in Kissimmee, FL",
                f"Backyard putting green installation in Kissimmee, FL runs {price('putting')} per sq ft as of {PRICE_DATE}. Nylon vs. polypropylene, stimp speed, base build and cost drivers.",
                "Backyard Putting Green Installation for Central Florida Yards",
                capsule(f"Backyard putting green installation in Kissimmee, FL runs {price('putting')} per square foot as of {PRICE_DATE}, with most greens landing between {price('putting', True)} once contouring, fringe turf and cups are included. A 400 to 600 sq ft green on a shaped, compacted base usually takes three to five days from strip-out to the first putt."),
                body, faqs=faqs, service="putting", crumbs=[("Services", "/services/")], crumb="Putting Greens",
                sources=["angi-putting", "homeguide-putting", "stn-life", "magnolia-heat", "hb683", "dep-rule", "marathon-pr", "fs7203045", STIMP_SRC, NYLON_POLY_SRC],
                related=[("/blog/backyard-putting-green-cost-florida/", "What drives putting green pricing in Florida"), ("/blog/artificial-turf-glossary/", "Turf terms: face weight, infill, stimp"),
                         ("/compare/nylon-vs-polyethylene-vs-polypropylene-turf/", "Nylon vs. polyethylene vs. polypropylene"), ("/artificial-turf-cost/", "Full turf cost guide"),
                         ("/blog/artificial-turf-for-55-plus-communities/", "Turf and putting greens in 55+ communities")])


# ============================================================== playground
def playground():
    body = "".join([
        sec("What is playground turf installation?",
            f"<p>Playground turf installation, sometimes just called artificial grass for playgrounds, is a synthetic play surface built over a cushioned shock pad sized to the equipment's fall height, rather than a lawn-grade turf laid straight over dirt. It runs {price('playground')} per square foot as of {PRICE_DATE}: small residential play areas typically land at $10 to $16, and daycare turf with a full-thickness pad runs $15 to $25. In Kissimmee and Osceola County most projects take two to four days, and the bulk of that time goes into the base and pad, not the turf on top.</p>"
            + f"<p>Backyard swing sets, HOA tot lots and daycare play yards are the three most common jobs, and each has a different fall-height requirement to design around. {svc('residential', 'A surrounding lawn')} is often installed at the same time so the play area reads as one yard, not a patch.</p>"),

        sec("Where playground turf makes sense",
            "<p>Play area turf fits any spot under swings, slides or a climbing structure where mulch has to be raked back into place weekly, or where sand tracks into the house and holds standing water after a storm. It also suits an HOA common-area tot lot or a home daycare, where a documented, fall-rated turf system matters more than it does for a single backyard swing set.</p>"
            + "<p>It fits less well for a budget-constrained backyard with only a small, low swing set, where engineered wood fiber mulch meets the same safety standard for a fraction of the cost, or for an area with no drainage plan at all, since a shock pad holds water if the base underneath can't move it along. A quick conversation about the actual fall height of the equipment usually settles which surface makes sense.</p>"),

        sec("What fall-height rating does playground turf need (ASTM F1292, IPEMA)?",
            f"<p>Playground turf needs a shock pad rated for a critical fall height equal to or greater than the highest point a child could fall from on the equipment it surrounds, tested to ASTM F1292 and documented by the manufacturer. A typical backyard swing set with a 5- to 6-foot platform needs roughly a 1-inch pad rated for that height; taller commercial or daycare structures at 8 to 10 feet need a thicker pad rated accordingly, and the rating has to match the tallest piece of equipment in the use zone, not the average one.</p>"
            + f"<p>The testing method comes from {ext(ASTM_F1292[1], 'ASTM F1292')}, the standard specification for impact attenuation of surfacing materials within a playground's use zone, measured using the Head Injury Criterion. The {ext(CPSC[1], 'the CPSC’s Public Playground Safety Handbook')} explains critical height as the fall distance below which a life-threatening head injury isn't expected, and recommends that a surface's rated critical height meet or exceed the equipment's actual fall height, not just come close. {ext(IPEMA[1], 'IPEMA')} runs third-party testing and certification against that ASTM standard; a certified logo means an independent lab validated the manufacturer's claimed rating, not just that the company is an IPEMA member.</p>"
            + table("Matching shock pad thickness to fall height (general ranges; confirm the exact rating with the manufacturer's ASTM F1292 test data)", ["Equipment fall height", "Typical shock pad", "Common use"],
                    [["Up to 5 ft", "¾–1 in bonded pad", "Backyard swing sets, small slides"],
                     ["5–8 ft", "1–1.5 in bonded pad", "Larger residential structures, small HOA play sets"],
                     ["8–10 ft+", "1.5–2.5 in or engineered pad system", "Daycare and commercial-grade equipment"]],
                    "These are planning ranges, not a substitute for the specific pad manufacturer's tested critical-height rating against the exact equipment installed.")
            + f"<p>{post('is-artificial-turf-safe-for-kids-pfas-lead', 'Safety questions beyond fall height, including infill and PFAS')} covers the rest of what parents ask before installing.</p>"
            + f"<p>One infill rule is specific to this service: Florida's synthetic turf standard limits infill on a home lawn, pet area or putting green to silica sand, rock, shell or other natural material, but it carves out an exception for the ground directly under playground equipment, where rubber or another synthetic infill is allowed ({src('dep-rule', 'the adopted rule text')}). That's why a play surface can specify a crumb-rubber or engineered infill inside the equipment's fall zone even though the same infill would be off the table for the lawn next to it.</p>"),

        sec("Building a play surface over Kissimmee sand",
            "<p>A playground base carries more weight in its design than a lawn base does, because the pad and turf both depend on what's underneath staying stable and draining well.</p>"
            + steps([("Excavate for the full system.", "Depth accounts for the base, the shock pad and the turf together, typically 4 to 6 inches more than a lawn conversion of the same footprint."),
                     ("Set a containment edge.", "A curb, header board or buried edging defines the play area before base material goes in, keeping infill and pad material from migrating into surrounding beds."),
                     ("Grade and compact the base.", "3 to 4 inches of washed, open-graded crushed rock or crushed concrete is compacted in lifts and sloped 1 to 2 percent to a drainage point, firm enough to hold the pad steady without sealing off the native soil's ability to drain."),
                     ("Install the shock pad.", "A bonded rubber or foam pad matched to the equipment's fall height is set and, on most systems, glued to the base to keep it from shifting under repeated impact."),
                     ("Cap irrigation nearby.", "Any sprinkler head that would spray into the play area is capped, both for the state turf rule and because standing water on a shock pad shortens its life."),
                     ("Lay turf and seam for a tight fit.", "Turf is seamed with tape and adhesive directly over the pad, trimmed tight to the containment edge so there's no gap where a foot or infill could catch."),
                     ("Infill and inspect.", "Infill goes in at the manufacturer's specified rate and the finished surface is walked and checked for flat, even coverage before handoff.")])),

        sec("How much does playground turf cost?",
            f"<p>Playground turf installation runs {price('playground')} per square foot as of {PRICE_DATE}. A small residential play area typically lands at $10 to $16 per square foot, while a daycare- or HOA-grade system with a full shock pad rated for taller equipment runs $15 to $25. A 500 sq ft backyard play area often prices between $6,000 and $9,500 depending on pad thickness and containment edging.</p>"
            + table("What drives a playground turf quote", ["Driver", "Typical add", "Why"],
                    [["Shock pad thickness", "+$2–$8/sq ft", "A pad rated for a 9-foot fall height costs more than one rated for 5 feet"],
                     ["Containment edging", "+$3–$8/linear ft", "A curb or buried header keeps loose infill from migrating off the surface"],
                     ["IPEMA-certified system", "+$1–$3/sq ft", "Independently tested products carry documentation a daycare or HOA may require"],
                     ["Site drainage correction", "+$500–$2,500 flat", "A pad on a poorly draining base holds water and fails early"],
                     ["Area and shape", "Varies", "Curved play zones around fixed equipment waste more material than a simple rectangle"]],
                    price_note())
            + "<!--AUTO:service-cities-->"),

        sec("Heat, storms and shade over a play area",
            f"<p>Being direct about heat matters more here than on any other turf project, because children play barefoot and touch the surface directly. Full Florida sun pushes turf to 120 to 150 °F and sometimes past 160 °F ({src('magnolia-heat', 'Florida installer measurements')}), hot enough to be uncomfortable or worse on bare skin within seconds. A shade sail, mature tree canopy or a scheduled play window before mid-morning matters as much as the turf product itself, and a lighter-colored or cooling infill helps but doesn't substitute for shade on a west-facing play yard.</p>"
            + "<p>Afternoon storms need a base and pad that drain fast, since a soggy shock pad softens and its cushioning performance can suffer, which is part of why the base grading gets extra attention on a playground job. The same statewide rules apply as elsewhere on a lot: turf and pad stay outside a live oak's drip line without an arborist's sign-off, at least 10 feet from a pond or canal unless a seawall already separates the two, and out of any swale carrying stormwater off the property.</p>"
            + "<p>A patio door or low-emissivity window facing a play area is worth checking too, the same as anywhere else on the lot: reflected sun off that kind of glass can get hot enough to soften polyethylene turf, which starts to give around 175 to 200 °F, well below what a magnified reflection can reach on a clear afternoon.</p>"),

        sec("Permits, HOAs and the state turf rule for playgrounds",
            f"<p>A backyard play area follows the same rules as any residential turf project: {a('/laws/florida-hb-683/', 'HB 683')}'s DEP standard keeps a city or county from banning turf that meets state permeability and setback requirements on a single-family lot up to an acre, and {a('/laws/hoa-rules/', 'F.S. 720.3045')} protects a fenced backyard play area from HOA restriction the way it protects any other yard feature not visible from the street. An HOA common-area tot lot or a licensed daycare play yard is a different animal, since it's typically on association or commercial property rather than a private lot and may involve its own permitting and inspection process; check the {a('/laws/permits/', 'permit page for the relevant jurisdiction')} and the community's own rules before ordering equipment. None of this is legal advice, and daycare licensing requirements are worth confirming directly with the state agency that oversees child care facilities.</p>"),

        sec("What a bad playground turf install misses",
            "<p>The most serious failure is a shock pad that doesn't match the equipment: a pad rated for a 5-foot fall height installed under an 8-foot platform looks identical to a correctly rated one until it's tested or until a fall proves the gap. The next most common problem is a seam that wasn't trimmed tight to the containment edge, leaving a gap that can catch a shoe or let infill wash out during a storm.</p>"
            + "<p>A base that wasn't graded to drain leaves the pad sitting in water after every afternoon storm, which softens the pad faster than normal use would and shortens its rated life well before the turf itself wears out. Any of these is worth a second opinion before assuming a play surface is safe just because it looks finished.</p>"),

        sec("Keeping a play surface safe over time",
            f"<p>Clear leaves, acorns and other debris regularly so they don't work down into the infill or create an uneven spot underfoot. Check seams and the containment edge after storms for anything that's lifted or opened, since a small gap is a quick {svc('repair', 'fix')} and a bigger one is a trip hazard. Shock pads compress gradually under years of use, so a play surface installed five or more years ago is worth having checked against its original fall-height rating, not assumed to still perform the same as new.</p>"),

        sec("What separates the best playground turf contractor from a lawn installer?",
            "<p>Ask for the shock pad's actual ASTM F1292 test documentation matched to the specific equipment's fall height, not a general product brochure. Ask whether the containment edge and drainage were designed before the pad went in or added afterward, since a play surface built around drainage from day one behaves differently than one where drainage was an afterthought. A contractor who can't produce fall-height documentation for the pad they're proposing isn't equipped for this particular job, even if their lawn work is excellent.</p>"
            + f"<p>{a('/compare/playground-turf-vs-mulch-vs-poured-rubber/', 'Comparing turf against mulch and poured rubber')} is worth reading before deciding a synthetic surface is the right call for a specific play area.</p>"
            + cta("Get a measured quote")),
    ])
    faqs = [
        faq("Is playground turf infill safe for kids?", f"Play-area infill is chosen for the application and typically avoids crumb rubber in favor of sand-based or engineered options. Ask any installer for the specific infill's safety documentation, and see {post('is-artificial-turf-safe-for-kids-pfas-lead', 'this page on PFAS, lead and infill')} for the broader safety picture."),
        faq("Can I install playground turf myself over an existing sandbox?", "The turf and pad can go over an existing sand base only if that base is regraded and compacted correctly first; sand alone doesn't compact the way crushed aggregate does, and a shock pad over uncompacted sand will settle unevenly within a season."),
        faq("Does playground turf need to be replaced as kids get older and the equipment changes?", "Not necessarily. If new equipment has a similar or lower fall height, the existing pad and turf can often stay. Taller new equipment usually means upgrading the pad to match the higher fall-height rating, even if the turf itself is fine."),
        faq("How is playground turf different from pet turf or lawn turf?", "The turf blade itself can be similar, but the layer underneath is different: playground systems need a tested, fall-height-rated shock pad, while lawn and pet turf rely on a compacted aggregate base without that cushioning requirement."),
        faq("What's the difference between IPEMA membership and IPEMA certification?", "Membership just means a company belongs to the trade association. Certification means an independent lab tested a specific product against the ASTM standard and validated the manufacturer's claimed rating, which is the distinction worth asking about."),
        faq("Do daycares have different requirements than a backyard?", "Often, yes, since licensed child care facilities may fall under additional state health and safety inspection beyond what a private backyard does. Confirm current requirements with the state licensing agency before finalizing a daycare play yard design."),
        faq("Can playground turf be installed on a slope?", "A play area needs a level or very gently sloped surface for both safety and pad performance, so a sloped section of yard usually gets leveled with additional base material rather than turfed as-is."),
    ]
    return page(SERVICES_ROUTE["playground"], "service",
                "Playground Turf Installation in Kissimmee, FL",
                f"Playground turf installation runs {price('playground')} per sq ft as of {PRICE_DATE}. Shock pad and ASTM F1292 fall-height ratings, cost drivers, and honest heat guidance.",
                "Playground Turf Installation for Kissimmee Yards and Daycares",
                capsule(f"Playground turf installation in Kissimmee and Osceola County costs {price('playground')} per square foot as of {PRICE_DATE}: small residential play areas typically run $10 to $16, and a daycare or HOA system with a full shock pad runs $15 to $25. Most jobs take two to four days, and most of that time goes into the base and shock pad, not laying the grass."),
                body, faqs=faqs, service="playground", crumbs=[("Services", "/services/")], crumb="Playground Turf",
                sources=["mightygrass-playground", "magnolia-heat", "watersavers-pfas", "mtsinai-turf", "hb683", "dep-rule", "marathon-pr", "fs7203045", CPSC, ASTM_F1292, IPEMA],
                related=[("/blog/is-artificial-turf-safe-for-kids-pfas-lead/", "Is artificial turf safe for kids?"), ("/blog/how-hot-does-artificial-turf-get-in-florida/", "How hot turf gets in Florida"),
                         ("/blog/coolest-artificial-grass-and-infill-for-florida/", "The coolest turf and infill for Florida sun"), ("/compare/playground-turf-vs-mulch-vs-poured-rubber/", "Playground turf vs. mulch vs. poured rubber"),
                         ("/artificial-turf-cost/", "Full turf cost guide")])


SERVICES_ROUTE = {"residential": "/artificial-grass-installation/", "pet": "/pet-turf/", "putting": "/putting-greens/", "playground": "/playground-turf/"}


def get_pages():
    return [residential(), pet(), putting(), playground()]
