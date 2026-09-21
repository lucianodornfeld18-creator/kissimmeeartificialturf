# -*- coding: utf-8 -*-
"""Home page."""
from _data import SERVICES, SERVICE_ORDER, PRICE_DATE, OWNER, PHONE_DISPLAY
from _helpers import page, capsule, sec, table, faq, ul, steps, cta, a, svc, city, county, post, src, price, price_note, tel
from templates import LAYERS_SVG

CARD = {
    "residential": "Front yards, backyards and sod-to-turf conversions. We strip the St. Augustine, build a washed crushed-rock base and lay synthetic grass that drains through a summer downpour.",
    "pet": "Artificial grass for dogs with a fully permeable backing, odor-control infill and no weed fabric to trap urine. Dog runs, side yards and potty areas that rinse clean.",
    "putting": "Backyard putting greens shaped with real breaks, a fringe collar and as many cups as the space allows. Chipping pads and tee lines if you want to practice the short game.",
    "playground": "Play-area turf over a shock pad matched to the fall height of the swing set or climber. Softer than mulch, cleaner than sand, and honest advice about shade.",
    "pool": "Turf beside pool decks and inside screen enclosures where sod never gets enough sun. Glue-down installs over concrete with a drainage layer underneath.",
    "str": "Yards for short-term rental homes from Four Corners to ChampionsGate. Green in every listing photo, no mowing crew to schedule between guests.",
    "commercial": "HOA common areas, apartment pet parks, daycare play yards, restaurant patios and rooftop decks, quoted from drawings or a site walk.",
    "sports": "Bocce courts, batting-cage lanes, agility strips and sled tracks for home gyms. Surfaces picked for the sport, not leftover lawn turf.",
    "pavers": "Turf ribbons between pavers, stepping-stone paths and driveway strips built on one continuous base so the joints stay level.",
    "repair": "Open seams, wrinkles, lifted edges, melted spots from window glare and low areas that hold water. We fix turf that other crews installed, too.",
    "cleaning": "Pet-odor treatment, power brooming, sanitizing and infill top-ups. A yearly refresh keeps blades standing and the lawn smelling like nothing.",
    "replacement": "Worn-out or faded turf pulled and hauled off, the base corrected where it settled, and a new surface laid on what can be reused.",
}


def get_pages():
    cards = '<ul class="grid">' + "".join(
        f'<li class="card"><h3><a href="{SERVICES[k]["route"]}">{SERVICES[k]["name"]}</a></h3><p>{CARD[k]}</p></li>' for k in SERVICE_ORDER) + "</ul>"

    body = "".join([
        sec("Artificial grass services we install, repair and maintain",
            f"<p>Kissimmee Artificial Turf is a local synthetic turf company. {OWNER} started it in 2024 to do one thing well: put down artificial grass that still looks flat and drains fast after a Central Florida summer. That takes a different build than the one written for Arizona or California, because our ground is fine sand over a high water table and our rain arrives two inches at a time. Here is everything we do, with a full page behind each service.</p>"
            + cards
            + f"<p>Not sure which one fits? Most calls start as a plain lawn replacement and turn into something more specific once we see the yard: a {svc('pet', 'dog run down the side of the house')}, a {svc('putting', 'putting green in the back corner')}, or {svc('pool', 'a turf border around the pool deck')}. The {a('/services/', 'services overview')} compares them side by side.</p>"),

        sec("What does artificial turf cost in Kissimmee?",
            f"<p>As of {PRICE_DATE}, installed artificial turf in Kissimmee and Osceola County runs about <strong>{price('residential')} per square foot</strong>, and most residential yards finish between {price('residential', True)}. That covers sod removal, the compacted base, turf, seams, edging, infill and cleanup. A 600 sq ft pool-home backyard typically lands between $6,600 and $9,600; 1,000 sq ft between $10,000 and $16,000.</p>"
            + table("Installed turf prices by project type, Central Florida", ["Project", "Market range per sq ft", "Typical 2026 job"],
                    [[svc("residential", "Residential lawn"), price("residential"), "800 sq ft backyard: $8,800–$12,000"],
                     [svc("pet", "Pet turf / dog run"), price("pet"), "300 sq ft run with odor-control infill: $3,600–$4,800"],
                     [svc("putting", "Putting green"), price("putting"), "400 sq ft green with fringe and three cups: $7,200–$10,000"],
                     [svc("playground", "Playground turf"), price("playground"), "500 sq ft play area over a shock pad: $6,000–$9,500"]],
                    price_note())
            + f"<p>The {a('/artificial-turf-cost/', 'turf cost guide')} breaks those numbers down by yard size, shows where the money goes, and compares ten years of turf against ten years of St. Augustine. If you'd rather punch in your own dimensions, use the {a('/artificial-turf-cost/calculator/', 'cost and materials calculator')}.</p>"),

        sec("How we build turf for sand, storms and a high water table",
            "<p>Turf fails from underneath. The blades on top are UV-stabilized polyethylene that will outlast the mortgage on some houses; what gives out is a thin, loosely raked base that settles the first time the water table comes up in August. So most of our day on site is spent on the part you'll never see.</p>"
            + LAYERS_SVG
            + steps([("Strip and haul.", "Sod, thatch and 3 to 4 inches of soil come out. St. Augustine roots hold a lot of organic matter, and organic matter under turf rots and sinks."),
                     ("Set the grade.", "We slope the subgrade 1 to 2 percent away from the house and toward wherever the lot already drains, usually the side-yard swale or the rear easement. Turf stops at the edge of a swale; the state rule keeps it out of swales, ditches and pond banks."),
                     ("Build the base.", "Two to four inches of washed crushed rock or crushed concrete, leveled and run over with a plate compactor until a boot heel doesn't mark it. Washed matters: the state standard requires it, because rock dust binds into a crust that stops water. We leave the native sand underneath loose enough to percolate."),
                     ("Cap the irrigation.", "Spray heads under the turf get capped at the line. Florida's 2026 synthetic turf rule doesn't allow an in-ground system to water turf, so rinsing is done with a hose and we make sure a spigot is within reach."),
                     ("Lay and seam.", "Rolls run the same direction so the grain matches, seams are cut between stitch rows and joined with seam tape and adhesive, never just nailed."),
                     ("Secure the edges.", "Perimeter nails every few inches, or a bender-board or paver border where the turf meets a planting bed."),
                     ("Infill and brush.", "One to two pounds of infill per square foot, power-broomed in so the blades stand up and the backing stays weighted down.")])
            + f"<p>The long version, including why decomposed granite advice from out West doesn't transfer here, is in {post('base-under-artificial-turf-florida-sandy-soil', 'what goes under turf on Central Florida sand')} and the {post('how-artificial-turf-is-installed-step-by-step', 'step-by-step installation walkthrough')}.</p>"),

        sec("The honest part: heat, dogs and rain",
            f"<p><strong>Heat.</strong> Synthetic turf in full July sun gets hot: published measurements put the surface at 120 to 150 °F, sometimes higher, while natural grass stays near air temperature ({src('magnolia-heat', 'Florida installer measurements')}). Shade, a light-colored cooling infill and a 30-second rinse bring it down 30 to 50 degrees. We'll tell you when a yard is a bad candidate, such as an unshaded play area that faces west. {post('how-hot-does-artificial-turf-get-in-florida', 'How hot turf gets in Florida')} has the numbers.</p>"
            f"<p><strong>Dogs.</strong> Turf is a good surface for dogs when it's built for them: fully permeable backing, no weed barrier, zeolite or coated-sand infill and a hose within reach. Built like a regular lawn, it will smell by the second summer. The {svc('pet', 'pet turf page')} explains the difference and {post('how-to-get-dog-urine-smell-out-of-artificial-turf', 'this guide covers odor')} if you already have a problem.</p>"
            f"<p><strong>Rain.</strong> Perforated turf passes more than 30 inches of water an hour, far more than any storm delivers. The base and the grade decide whether your yard drains, which is why we look at where water goes before we quote. See {post('does-artificial-turf-drain-in-heavy-rain', 'turf drainage in heavy rain')} and {post('artificial-turf-hurricane-flooding', 'what a hurricane does to turf')}.</p>"),

        sec("How do you pick the best artificial turf contractor in Kissimmee?",
            "<p>You can't tell a good turf job from a bad one on the day it's finished. Both look perfect. The difference shows up after the first rainy season, so choose on what's written down rather than on who claims to be number one. Five things separate careful installers from fast ones:</p>"
            + ul(["<strong>A base spec in writing.</strong> Depth, material and how it's compacted. \"Standard prep\" isn't a spec.",
                  "<strong>Seams joined with tape and adhesive.</strong> Nailed seams open when the ground moves.",
                  "<strong>A drainage plan.</strong> Where does the water go now, and where will it go after? Anyone who doesn't ask hasn't looked.",
                  "<strong>The product named on the quote.</strong> Pile height, face weight, backing type and infill by the pound, so two bids can be compared.",
                  "<strong>Proof you can check.</strong> A local business tax receipt, a certificate of insurance sent from the agent, and a Sunbiz record that matches the name on the contract."])
            + f"<p>We'd rather you compare us on those five points than take our word for anything. {post('best-artificial-turf-contractor-kissimmee', 'How to choose a turf contractor in Kissimmee')} goes through each one, and {post('how-to-compare-artificial-turf-quotes', 'this guide shows how to read two quotes side by side')}.</p>"),

        sec("Florida turf law and HOA rules in two minutes",
            f"<p>Two state laws matter. {a('/laws/florida-hb-683/', 'HB 683')} created F.S. 125.572, and the rule that carries it out, DEP Rule 62-308.100, took effect on May 19, 2026. On a single-family lot of one acre or less, a city or county can no longer prohibit synthetic turf that meets the state standard. The standard has teeth: turf, backing and infill free of heavy metals and intentionally added PFAS, natural infill only on lawns, a washed permeable base, nothing in a swale or within 10 feet of a lake, pond or canal unless there's a seawall, nothing inside a tree's drip line without a certified arborist's letter, and no in-ground sprinklers watering it ({src('dep-rule', 'Rule 62-308.100')}). HB 683 says nothing about homeowners associations.</p>"
            f"<p>For HOAs, the statute to know is F.S. 720.3045: an association can't restrict what you install where it isn't visible from the street or from a neighboring lot, and the text names artificial turf. A fenced backyard is covered. A front yard isn't, so that still goes through architectural review. {a('/laws/hoa-rules/', 'What a Florida HOA can and can’t restrict')} lays it out, and the {a('/laws/permits/', 'permit guide')} lists what Kissimmee, St. Cloud, Osceola, Orange, Polk, Lake and Seminole ask for. None of this is legal advice; it's what we've read and what we see on applications.</p>"
            + f"<p>We put together the ARC package when a community wants one: a sample, the manufacturer's spec sheet, a site plan and a drainage note. The {a('/tools/hoa-packet-checklist/', 'HOA application checklist')} shows what reviewers usually ask for.</p>"),

        sec("Where we work: Kissimmee and about 40 miles around it",
            f"<p>We're based in Kissimmee and spend most weeks in {county('osceola')}: {city('kissimmee')}, {city('st-cloud')}, {city('celebration')}, {city('poinciana')}, {city('buenaventura-lakes', 'BVL')}, {city('harmony')}, and the resort belt along US-192 and I-4 at {city('four-corners')}, {city('championsgate')} and {city('reunion')}. North of the county line it's {city('hunters-creek')}, {city('meadow-woods')}, {city('southchase')}, {city('lake-nona')} and {city('dr-phillips')} in {county('orange')}; southwest it's {city('davenport')} and the ridge towns of {county('polk')}.</p>"
            f"<p>Each town page covers what's different there: which office reviews a permit, which water utility sets the irrigation days, what the big HOAs ask for, and what kind of sand you're building on. Yards in Harmony and east St. Cloud sit on wetter flatwoods soils than the sandy ridge under Davenport and Clermont, and the base changes to match.</p>"
            + "<!--AUTO:all-areas-->"
            + f"<p>Outside those towns but inside the circle? Call. If we can reach you in about an hour from Kissimmee, we'll come measure. {a('/areas/', 'See the full service-area map and list')}.</p>"),

        sec("Yards we see every week around Kissimmee",
            "<p>Florida lots repeat themselves, and each type has its own trap. Knowing which one you have tells us most of what the quote will say.</p>"
            + ul([f"<strong>The pool home with a strip of grass behind the cage.</strong> Four hundred to 700 square feet, shaded half the day by the screen enclosure, soaked by deck runoff. Sod thins out within two summers. This is the most natural fit for synthetic grass, and the job is mostly about catching the water that comes off the deck. See {svc('pool', 'turf around pools and lanais')}.",
                  f"<strong>The new-construction lot.</strong> Builder sod laid over compacted fill with two inches of sand on top. It looks fine at closing and struggles after the establishment watering ends. {post('why-new-construction-sod-dies-in-osceola-county', 'Why builder sod dies here')} explains what to try before spending money on turf.",
                  f"<strong>The narrow side yard.</strong> Five to seven feet between houses, no sun, AC condensate dripping, a drainage swale down the middle. The swale has to stay a swale, so turf goes beside it, never in it. {post('artificial-grass-for-shady-side-yards', 'Options for shady side yards')} compares turf, pavers and rock.",
                  "<strong>The lakefront or pond-front lot.</strong> Common in Kissimmee, St. Cloud, Lake Nona and Harmony. Since May 2026 the state standard keeps synthetic turf at least 10 feet back from the water line and off pond banks, so we design a planted or natural buffer along the edge and turf the usable yard above it.",
                  f"<strong>The yard under live oaks.</strong> Grass won't grow in that shade, which is why people call us, but the same rule keeps turf outside a tree's drip line unless a certified arborist signs off. We'll tell you where the line falls and what can go under the canopy instead. {post('artificial-turf-near-live-oaks-and-palms', 'Turf near live oaks and palms')} has the detail.",
                  f"<strong>The dog yard.</strong> Two big dogs can wreck St. Augustine in a season. A {svc('pet', 'pet turf system')} holds up, provided it's built to be rinsed and the infill is chosen for odor."])),

        sec("Choosing the turf itself",
            f"<p>Most of the samples we carry into a yard look alike from six feet away. The differences that matter are on the spec sheet. For a family lawn we usually steer people toward a 1.5 to 1.9 inch pile with a tan thatch layer and a face weight in the 60 to 90 ounce range: tall enough to look like a lawn, short enough that the blades don't mat flat in the traffic paths. Dogs do better on a shorter, denser product with a fully permeable backing. Putting greens use a very short nylon or textured polyethylene surface chosen for ball speed, with a taller fringe around it. Play areas get a soft, mid-height turf over a shock pad.</p>"
            f"<p>Blade color matters more than people expect. A blend of two or three greens with tan thatch reads as grass; a single bright green reads as carpet. Florida sun is hard on cheap yarn, so ask for the UV warranty in writing and for a statement that the product has no intentionally added PFAS or heavy metals, which the state standard now requires anyway. {post('artificial-turf-pile-height-and-face-weight', 'Pile height and face weight explained')}, {post('best-artificial-grass-for-florida', 'what to look for in turf for Florida')} and the {a('/compare/nylon-vs-polyethylene-vs-polypropylene-turf/', 'fiber comparison')} go deeper, and {a('/compare/zeolite-vs-silica-vs-antimicrobial-infill/', 'the infill comparison')} covers what goes between the blades.</p>"),

        sec("Living with it: care, repairs and lifespan",
            f"<p>Synthetic grass isn't maintenance-free; it's low maintenance. Blow leaves off before they break down into the infill, especially during the live oak drop in late winter. Rinse pet areas a few times a week with a hose. Brush the traffic lanes against the grain a few times a year, or have us {svc('cleaning', 'power-broom and refresh the infill')} once a year. After a tropical storm, walk the edges and seams, and call if anything has lifted; the state rule requires edges and seams to be anchored for wind and flooding, and a lifted corner is a small {svc('repair', 'repair')} if it's caught early.</p>"
            f"<p>A well-built lawn lasts 10 to 20 years in Florida UV, depending on traffic and product. When it's finally worn, the base is usually reusable, which makes {svc('replacement', 'replacing the turf')} cheaper than the first install. {post('how-long-does-artificial-turf-last-in-florida', 'How long turf lasts here')} breaks that down by use.</p>"),

        sec("Vacation homes, property managers and commercial sites",
            f"<p>A large share of the homes around Kissimmee earn their keep as short-term rentals, and a rental yard has a different job than a family lawn: look good in photos, survive guests, and need nobody on site between check-out and check-in. {svc('str', 'Turf for vacation rental homes')} covers scheduling around bookings, working through a property manager and what resort-community review boards ask for. For shared spaces such as clubhouse lawns, apartment dog parks and daycare play yards, see {svc('commercial', 'commercial turf installation')}.</p>"),

        sec("Turf or sod? A quick way to decide",
            f"<p>Sod is cheap to put down, about $1 to $2 a square foot, and expensive to keep. Turf is the reverse. On 1,000 sq ft, published ten-year totals run $18,000 to $37,000 for a maintained St. Augustine lawn and $11,500 to $23,000 for turf, with the lines crossing between year five and year eight ({src('bearcat-10yr', 'ten-year cost model')}). If you mow it yourself and water from a well, grass wins on cost for a long time. If you pay a lawn service, fight chinch bugs every summer and water on Toho's two-day schedule, turf usually wins.</p>"
            + f"<p>Run your own numbers in the {a('/tools/turf-vs-sod/', 'turf vs. sod calculator')}, read {post('is-artificial-turf-worth-it-in-florida', 'whether turf is worth it in Florida')}, or compare it with {a('/compare/artificial-turf-vs-st-augustine-zoysia-bahia/', 'St. Augustine, Zoysia and Bahia')} head to head.</p>"),

        sec("Water rules, dry springs and the best months to install",
            f"<p>Most of Kissimmee and Osceola County gets its water from Toho Water Authority, which limits lawn irrigation to two days a week by address: Wednesday and Saturday for odd numbers, Thursday and Sunday for even ({src('toho-days', 'Toho watering schedule')}). That's enough for an established Bahia lawn and often not enough for St. Augustine in an April dry spell, when Central Florida can go three or four weeks without meaningful rain. The county spent 2026 debating tighter conservation rules, so the trend isn't toward more watering days. Synthetic turf takes irrigation out of the equation; the state standard actually bars running an in-ground system on it.</p>"
            f"<p>As for timing, we install all year. October through May is the easy season: dry subgrade, no afternoon lightning, adhesive that cures on schedule. June through September works too, with earlier starts and tarps over the base when storms build. {post('best-time-of-year-to-install-artificial-turf-florida', 'The month-by-month breakdown')} and {post('toho-water-restrictions-new-sod-vs-turf', 'how watering restrictions treat new sod')} have the detail.</p>"),

        sec("What working with us looks like",
            steps([("You send the basics.", f"Use the form below or call or text {tel()}. Photos help: the yard, the gate, and any spot that holds water."),
                   ("We measure and look at drainage.", "A site visit takes about half an hour. We measure, check access and slope, find the irrigation zones and ask about dogs, kids and shade."),
                   ("You get a written quote.", "Square footage, base depth and material, the turf product with pile height and face weight, infill type and weight, how seams and edges are secured, and the price."),
                   ("Paperwork, if any.", "We prepare the HOA or ARC submittal and check with the permit office where one applies."),
                   ("Install.", "Most residential yards take two to four days depending on size and access. We call 811 before digging, protect the pool screen and pavers, and leave the site swept."),
                   ("Walkthrough and care sheet.", "We go over rinsing, brushing and what to do after a storm, and you know who to call if a seam or edge ever needs attention.")])
            + f"<p>There's more detail in {post('what-to-expect-on-turf-installation-day', 'what to expect on installation day')}.</p>"),

        sec("About Kissimmee Artificial Turf",
            f"<p>{OWNER} owns and runs the company, established in 2024 and based in Kissimmee. We're a small local installer, which means the person who measures your yard is the person accountable for how it looks in three years. We don't run a showroom; we bring samples to you and work across the five counties around Kissimmee. {a('/about/', 'More about how we work')}.</p>"
            + cta("Get a measured quote", "Tell us about the yard and we’ll set a time to come measure it.")),
    ])

    faqs = [
        faq("Which towns does Kissimmee Artificial Turf cover?", "Kissimmee and everything within roughly 40 miles: St. Cloud, Celebration, Poinciana, BVL, Harmony, Four Corners, ChampionsGate, Reunion and Davenport, north through Hunters Creek, Lake Nona, Dr. Phillips and Orlando, and out to Clermont, Winter Haven and Sanford. The service-area page lists every town by county."),
        faq("How do I know I'm hiring the best grass contractor near me and not just the cheapest?", "Ask each bidder for the same five things in writing: base depth and material, seam method, drainage plan, the turf's spec sheet and proof of insurance. The cheapest quote almost always saves money on the base. Compare the written scope first and the price second."),
        faq("Do you work with HOAs and property managers?", "Yes. We prepare architectural review submittals with a sample, spec sheet and site plan, and we coordinate access, gate codes and scheduling with property managers for rental homes so the owner doesn't have to be on site."),
        faq("Can you turf only part of a yard?", "Often that's the smart move. Side yards that won't grow grass, the strip behind a pool cage, a dog run or a play corner are common partial projects. Small areas cost more per square foot because the crew and equipment are the same either way."),
        faq("Do you remove the old grass and haul it away?", "Yes. Removal, hauling and disposal are part of a standard quote. We take out the sod and three to four inches of soil so the new base sits on firm ground instead of rotting thatch."),
        faq("Is artificial grass the same thing as AstroTurf?", "AstroTurf is a brand from the 1960s that became a nickname. Today's landscape turf is a different product: softer polyethylene blades in several greens with a tan thatch layer, a perforated or fully permeable backing and sand-based infill."),
        faq("Can I text photos of my yard for a rough number?", f"Yes. Text photos and rough dimensions to {PHONE_DISPLAY} and we'll reply with a ballpark from the published ranges. A firm quote still needs a site visit, because access and drainage change the price more than the turf does."),
        faq("Will you repair turf that another company installed?", "Yes. Seams that opened, edges that lifted, wrinkles, low spots and melted patches from window reflection can usually be repaired without replacing the lawn. We'll tell you if the base is the real problem."),
        faq("Do you install during the rainy season?", "We install year-round. From June through September we start early, plan base work around the afternoon storms and won't glue seams over a damp base. Dry-season dates, roughly October to May, book up faster."),
        faq("What do you need from me for a quote?", "An address, the areas you want covered, whether dogs use the yard, whether there's an HOA, and any drainage trouble you've noticed. Gate width matters too: a 36-inch gate means wheelbarrows, a double gate means machines."),
    ]
    return [page("/", "home", "Artificial Turf Installation in Kissimmee, FL | Kissimmee Turf",
                 "Artificial turf installation in Kissimmee, FL: lawns, pet turf, putting greens and playgrounds. $8–$18 per sq ft installed in 2026. Call (689) 202-3710.",
                 "Artificial turf installation in Kissimmee, Florida",
                 capsule(f"Kissimmee Artificial Turf installs, repairs and cleans artificial grass in Kissimmee, Osceola County and towns within about 40 miles. Installed turf runs {price('residential')} per square foot as of {PRICE_DATE}, built on a washed crushed-rock base that drains through Florida's summer storms. Locally owned by {OWNER} since 2024."),
                 body, faqs=faqs, eyebrow="Locally owned · Kissimmee, FL · Est. 2024", wide=False, faq_title="Questions we hear every week",
                 sources=["attampa-cost", "lbs-fl-cost", "magnolia-heat", "sgw-faq", "bearcat-10yr", "hb683", "dep-rule", "marathon-pr", "fs7203045", "toho-days", "osceola-water-2026"],
                 related=[("/artificial-turf-cost/", "Turf cost guide: tables by yard size and project"), ("/laws/", "Florida turf law, HOAs and permits"), ("/faq/", "Every question, answered briefly"), ("/blog/", "All articles")])]
