# -*- coding: utf-8 -*-
"""FAQ hub: /faq/, /faq/cost/, /faq/pets-heat/, /faq/hoa-permits/, /faq/maintenance/.
Short-answer-plus-link for questions owned by another URL; full 50-90 word answers only for the
questions this hub owns outright (see docs/AGENT-BRIEF.md and docs/WRITING-GUIDE.md)."""
from _data import PRICE_DATE
from _helpers import page, capsule, sec, table, faq, ul, note, cta, a, svc, city, post, src, ext, price, price_note

TOHO_REBATE = ("Toho Water Authority — Smart Irrigation Rebate", "https://www.tohowater.com/irrigationrebate")
SFWMD_HOME = ("South Florida Water Management District — for homeowners", "https://www.sfwmd.gov/community-residents/homeowners")
SJRWMD_REBATE = ("St. Johns River Water Management District — Water Conservation Rebate Program, 2026 cycle", "https://www.sjrwmd.com/2026/08/districts-water-conservation-rebate-program-now-accepting-applications/")
SWFWMD_CONS = ("Southwest Florida Water Management District — water conservation programs", "https://www.swfwmd.state.fl.us/residents/water-conservation")
FAC_626 = ("Florida Administrative Code — Chapter 62-6, standards for onsite sewage treatment and disposal systems", "https://pasco.floridahealth.gov/wp-content/uploads/sites/53/2025/06/62-6.pdf")


# ================================================================== index
def index_page():
    body = "".join([
        sec("What people ask before they call a Kissimmee turf installer",
            f"<p>Most first calls carry the same three worries: what this costs, whether it's actually allowed on the lot, and whether a Central Florida summer will ruin it. Below are the twenty questions we hear most, answered in a few sentences apiece, plus three from homeowners specifically trying to pick a contractor. Anything that needs real room, a cost table, the DEP standard that took effect {src('dep-rule', 'May 19, 2026')}, a repair diagnosis, gets a short answer here and a link to the fuller page.</p>"),
        sec("Jump to a topic",
            ul([f"{a('/faq/cost/', 'Cost questions')}: financing, rebates, deposits and what changes a quote.",
                f"{a('/faq/pets-heat/', 'Pets and heat questions')}: paws, digging, fleas and summer surface temperatures.",
                f"{a('/faq/hoa-permits/', 'HOA, law and permit questions')}: setbacks, drip lines and who signs off on what.",
                f"{a('/faq/maintenance/', 'Care, repair and lifespan questions')}: cleaning schedule, wrinkles and how long a lawn lasts."])),
    ])
    faqs = [
        faq("How much does artificial turf cost per square foot in Kissimmee?",
            f"Installed turf runs about {price('residential')} a square foot in Central Florida as of {PRICE_DATE}, with most yards landing between {price('residential', True)}. The number depends on access, base depth and shape, not your ZIP code. See the full {a('/artificial-turf-cost/', 'cost guide')} for tables by yard size and project type."),
        faq("Is artificial turf actually legal on a Florida property now?",
            f"Yes. Florida's DEP adopted Rule 62-308.100 on May 19, 2026, and a city or county can no longer ban compliant turf on a single-family lot of an acre or less. {a('/laws/florida-hb-683/', 'HB 683 and the DEP rule')} walks through what the standard requires."),
        faq("Can a homeowners association still say no to my turf?",
            f"For a front yard, usually yes, since HOA appearance rules still apply there. For a fenced backyard nobody can see from the street or next door, Florida law has protected artificial turf from HOA restriction since 2023. {a('/laws/hoa-rules/', 'See what F.S. 720.3045 covers')}."),
        faq("Do I need a city or county permit to install turf?",
            f"It depends on the jurisdiction and whether the job touches drainage, an easement or a right-of-way. What no city or county can do anymore is refuse turf outright on a covered lot. {a('/laws/permits/', 'Check the permit page for your jurisdiction')}."),
        faq("Will turf work under a covered lanai or in heavy shade where grass gives up?",
            "Better than grass does. Synthetic turf has no light requirement, so a lanai floor or a yard shaded by a two-story neighbor or a stand of oaks holds its color and shape the same as a sunny section would. The trade-off runs the other way: shade keeps a lawn damp longer after rain, so a permeable backing and a fast-draining base matter more there than they do on an open, sunny lot."),
        faq("Does Kissimmee's summer heat make turf unsafe for bare feet?",
            f"At 2 p.m. in July, yes, unless it's rinsed or shaded first; surface readings commonly hit 120 to 150°F ({src('magnolia-heat', 'measured Florida readings')}). Early morning and evening use is far more comfortable, and a quick hose-down brings the surface down fast. {a('/faq/pets-heat/', 'The pets and heat page')} has the full temperature table."),
        faq("Is artificial turf a good choice for a yard with dogs?",
            f"Yes, when it's built for them: a fully permeable backing, no weed fabric underneath, and an infill chosen to fight odor rather than a plain lawn-grade sand. {svc('pet', 'Pet turf')} covers the specific build and what it costs."),
        faq("What is infill, and does a synthetic lawn actually need it?",
            "Infill is the sand-like material brushed between the blades to hold the backing down, keep fibers standing, and, depending on the type, manage heat or odor. Almost every lawn needs some. On a Florida single-family lot the state rule limits it to clean silica sand, rock, shell or other natural material, plus non-toxic coated sand; rubber and other synthetic infill are allowed only under playground equipment."),
        faq("How long does a typical turf installation take?",
            "Most residential yards in the 800 to 1,200 sq ft range take two to four days from strip-out to the final rinse, longer for a putting green's shaped base or a playground's rated pad. Weather and access change that more than square footage does; a gate too narrow for equipment can add a full day on its own."),
        faq("How do I get the yard ready before installation day?",
            f"Move furniture, toys and potted plants off the work area, flag any shallow wiring or irrigation you know about, and plan for pets to be elsewhere on the loudest equipment days. {post('what-to-expect-on-turf-installation-day', 'The full installation-day walkthrough')} covers what the crew handles from there."),
        faq("What should I ask a contractor before signing a turf contract?",
            "Ask for base depth and material in writing, whether seams are taped and glued or only nailed, the product's name with pile height and face weight, and how they'd fix a low spot that ponds after rain. A contractor who answers in specifics, not \"premium turf, installed,\" is the one worth comparing against a second bid."),
        faq("Is there a waiting period before a new lawn can be used?",
            f"No. Unlike sod, synthetic turf has no root system to establish, so it's walkable the day the crew leaves. Infill settles a little more after the first few rinses, which is cosmetic, not a usability limit. {svc('residential', 'The residential installation page')} covers the full build."),
        faq("Does new artificial turf smell like plastic when it's first installed?",
            "A faint rubber-and-plastic smell is normal for the first few days as the backing warms in the sun, and it fades faster with a hose rinse or two. A strong chemical smell that lingers past a week or so is worth a call back to whoever installed it, not something to live with."),
        faq("How do I measure my yard before asking for a quote?",
            f"Break the space into rectangles and triangles, measure each, and add them up, subtracting anything you're keeping such as a planting bed. {a('/artificial-turf-cost/calculator/', 'The cost calculator')} does that arithmetic and adds base and infill quantities once you have rough numbers."),
        faq("Does turf fade or turn a strange color over time?",
            f"Some fading is normal. UV-stabilized polyethylene loses a little saturation over 10 to 20 years of Florida sun, more on an unshaded, south-facing lawn. {a('/faq/maintenance/', 'The care and lifespan page')} has the full picture, including what shortens that timeline."),
        faq("What happens to my irrigation system once turf goes down?",
            f"Sprinkler heads under the turf get capped at the valve box, since Florida's synthetic turf standard doesn't allow an in-ground system to water a synthetic lawn. Rinsing after that point is by hose. {a('/faq/hoa-permits/', 'More on what the state rule requires')}."),
        faq("Can turf go over an existing patio, pool deck or pavers?",
            f"Yes, glued down over a cleaned slab with a drainage underlay, or set into paver joints as a ribbon. {svc('pool', 'Turf around a pool or lanai')} and {a('/turf-and-pavers/', 'turf between pavers')} cover the different builds and what changes the price."),
        faq("Is artificial turf worth it compared to keeping natural grass?",
            f"Usually, over time, if you already pay for mowing and irrigation, though not in year one since turf costs more up front than sod. {post('is-artificial-turf-worth-it-in-florida', 'This breakdown')} and {post('artificial-turf-vs-sod-cost-florida', 'the ten-year cost comparison')} both work through the numbers."),
        faq("Can artificial turf be installed on a slope or uneven lot?",
            f"Yes, with extra base work to hold the grade and keep infill from washing downhill in a storm. {post('artificial-turf-on-a-slope', 'This article')} covers how a sloped build differs from a flat one."),
        faq("Does artificial turf hurt the environment or just create plastic waste later?",
            f"It's a fair question with a mixed answer: no watering or fertilizer runoff while it's down, but most turf is landfilled rather than recycled once it wears out. {post('is-artificial-turf-bad-for-the-environment', 'This page')} lays out both sides plainly."),
        faq("How do I find the best turf contractor near me?",
            f"Compare bids on the same five specifics: measured square footage, base depth and material, the turf product's name with face weight, infill type, and how seams and edges get secured. A local business tax receipt and proof of insurance sent from the agent matter more than a slick brochure. {post('best-artificial-turf-contractor-kissimmee', 'This checklist')} goes further."),
        faq("Who is the best artificial grass contractor for a small yard?",
            f"Size changes what to ask, not who to ask. A small job, a side yard or a dog run, still deserves a written base spec and a real minimum charge instead of a rushed guess. Look for an installer willing to quote a 200 sq ft yard with the same detail as a 2,000 sq ft one. {post('best-artificial-grass-installer-near-me', 'More on choosing for a small project')}."),
        faq("What makes the best pet turf installers near me different from a general lawn crew?",
            f"They spec a fully permeable backing, skip the weed barrier that traps urine, and choose zeolite or antimicrobial infill instead of standard silica sand. {svc('pet', 'The pet turf page')} lists the build differences worth asking a contractor about by name."),
    ]
    return page("/faq/", "faq",
                "Artificial Turf FAQ for Kissimmee, FL (2026)",
                "The questions Kissimmee homeowners ask most about turf cost, Florida law, pet and heat safety, and upkeep, answered as of September 2026.",
                "Artificial Turf Questions, Answered for Kissimmee",
                capsule("Kissimmee homeowners ask us the same handful of questions before a quote: what artificial turf costs, whether it's legal on a Florida lot, whether a dog or a bare foot can handle the heat, and how much upkeep it takes. This page answers the twenty questions we hear most, in plain terms, then points to a deeper page for anything that needs more room."),
                body, faqs=faqs, faq_title="Questions people ask most", crumb="FAQ",
                sources=["dep-rule", "magnolia-heat", "stn-life", "fs7203045"],
                related=[("/faq/cost/", "Cost questions, answered"), ("/faq/pets-heat/", "Pets and heat questions"),
                         ("/faq/hoa-permits/", "HOA, law and permit questions"), ("/faq/maintenance/", "Care, repair and lifespan questions")])


# ================================================================== cost
def cost_page():
    body = "".join([
        sec("Why the answer is a range, not a number",
            f"<p>Every cost question eventually runs into the same fact: artificial turf is priced by the yard, not by a catalog. Installed turf runs {price('residential')} a square foot in Central Florida as of {PRICE_DATE}, and the questions below cover what moves a project inside that range, plus the money questions that come up once the range itself makes sense: financing, deposits, rebates, resale value and what a red flag in a written quote looks like. The {a('/artificial-turf-cost/', 'full cost guide')} has the size-by-size tables; this page fills in what that guide doesn't.</p>"
            + table("Where a Kissimmee turf quote typically lands", ["Yard situation", "Typical price position", "Why"],
                    [["Flat, open lawn, easy truck access", "Lower half of the range", "Base goes in fast, with little cutting or hand-carrying"],
                     ["Pet yard or play area", "Middle to upper range", "A deeper base or a rated shock pad adds labor and material"],
                     ["Narrow gate, tight side yard", "Upper end, or a flat minimum", "Wheelbarrows and hand tools replace machine work"],
                     ["Putting green or heavy contouring", "Above the residential range entirely", "A hand-shaped base and a different turf product altogether"]],
                    price_note())
            + "<p>Three bids on the same backyard usually land in three different places for a reason that has nothing to do with one contractor padding the number. Ask each one to write down the same five specifics, measured area, base depth and material, product name with face weight, infill type, and how seams are joined, and the spread narrows fast once the comparison is apples to apples.</p>"),
    ])
    faqs = [
        faq("What's the going rate for turf installation, per square foot, in Kissimmee?",
            f"About {price('residential')} installed as of {PRICE_DATE}, with most yards landing between {price('residential', True)}. {a('/artificial-turf-cost/', 'The full cost guide')} breaks that down by project type and yard size, with a calculator for your own measurements."),
        faq("How much would a 1,000 or 1,500 sq ft yard cost to turf?",
            f"Roughly $10,000 to $16,000 for 1,000 sq ft and $16,500 to $22,500 for 1,500 sq ft at mid-grade turf, per the published Central Florida range. {a('/artificial-turf-cost/', 'The size-by-size tables')} carry three build levels for common yard sizes."),
        faq("Can I finance artificial turf?",
            "Financing terms vary by installer and by the lender they work with, so we can't quote a rate here, and we don't offer financing ourselves. Ask any contractor bidding your job whether financing is available, what the APR and term are, and whether the total cost changes if you pay cash. Compare that total, not the monthly payment, against the cash price before deciding."),
        faq("Are there rebates for replacing grass with turf in Osceola County?",
            f"As of {PRICE_DATE} we haven't found a rebate that pays a homeowner to replace grass with turf here. {ext(TOHO_REBATE[1], 'Toho Water Authority')} offers a $145 rebate toward a WaterSense smart irrigation controller, not turf, and the {ext(SFWMD_HOME[1], 'South Florida')}, {ext(SJRWMD_REBATE[1], 'St. Johns River')} and {ext(SWFWMD_CONS[1], 'Southwest Florida')} water management districts run rebate programs aimed at irrigation hardware, utilities and local governments, not a homeowner's turf conversion. We'll update this page if that changes."),
        faq("What are the red flags in a turf quote?",
            "Watch for a bid that says only \"premium turf, installed\" without naming pile height, face weight or infill type; a base described as \"compacted\" with no depth or material given; a demand for full payment before work starts; and a price that's only good \"today.\" A written scope with those five specifics is what separates a comparable bid from a guess."),
        faq("Is a deposit normal before a turf job starts?",
            "Yes, since turf and base rock are ordered ahead of the crew showing up. A deposit close to material cost, a progress payment once the base is compacted, and a balance due at the walkthrough is a reasonable structure. Be cautious of anyone asking for the full amount up front."),
        faq("If I sell my house, does a turf warranty transfer to the new owner?",
            f"Sometimes, and it depends entirely on the manufacturer's paperwork, not on the installer. Some warranties are tied to the original purchaser and end at sale; others transfer with a notification and a small fee. {post('what-does-artificial-turf-warranty-cover', 'This guide to what a turf warranty covers')} explains what to check before closing."),
        faq("What's the easiest way to get a rough number before calling anyone?",
            f"Measure the area in rectangles, pick a project type, and run it through {a('/artificial-turf-cost/calculator/', 'the turf cost calculator')}, which returns a planning range plus base rock and infill quantities. It's a starting point for a conversation, not a quote."),
        faq("Does a local installer cost more or less than a national franchise?",
            f"Not consistently either way; overhead and marketing spend vary more between companies than between local and national ones. {a('/compare/local-turf-installer-vs-national-franchise/', 'This comparison')} covers what actually differs: scheduling, who shows up, and how a warranty claim gets handled."),
        faq("Will my homeowners insurance help pay for a turf install?",
            f"Not for a first-time installation; that's a landscaping choice, not a covered loss. {post('does-homeowners-insurance-cover-artificial-turf', 'This page')} covers the narrower case of storm or fire damage to turf already installed, which a policy sometimes does cover."),
        faq("Does installing turf raise what my house is worth?",
            f"It can help a listing show better and remove a maintenance concern for a buyer, but there's no fixed figure to promise. {post('does-artificial-grass-increase-home-value-florida', 'This article')} looks at what appraisers and Realtors actually say about it in Florida."),
        faq("Does an HOA application add to the cost of a turf project?",
            f"Not usually in materials, but it adds time: a sample, a spec sheet and a site plan take a review cycle before work can start in most communities. {a('/laws/hoa-rules/', 'See how the approval process works')} and budget a few weeks, not a few days, for board sign-off."),
        faq("Can I save money by removing the old grass myself first?",
            "Sometimes, since demo and haul-off can run $1 to $2 a square foot. Talk to the installer before renting equipment, because the final grade still has to be right, and a poorly cut slope just gets corrected again at your cost."),
        faq("Is there a minimum job size or a smallest project you'll quote?",
            "Most installers, including small local crews, have a practical minimum because a truck and equipment show up whether the area is 150 sq ft or 1,500. Expect a small strip to price at the top of the per-foot range or as a flat minimum charge."),
        faq("Does turf pay off on a long-term rental property I don't live in?",
            "It can, since a tenant turnover often includes a neglected lawn that costs money to restore anyway. Run the same water-and-mowing math you'd use for your own house against what you currently spend keeping a rental's yard presentable between tenants."),
        faq("Does the type of infill change the price much?",
            f"A little. Standard silica sand is usually included in the base quote; zeolite or antimicrobial-coated sand for pets adds roughly $0.50 to $1.50 a square foot, and a cooling infill for a full-sun play area adds about $1 to $1.50. {a('/artificial-turf-cost/', 'The full cost guide')} breaks down where the rest of the money goes."),
    ]
    return page("/faq/cost/", "faq",
                "Artificial Turf Cost FAQ, Kissimmee, FL (2026)",
                "Financing, rebates, deposits and quote red flags for artificial turf in Kissimmee, answered plainly with 2026 price ranges and sources.",
                "Turf Cost Questions, Answered for Kissimmee Homeowners",
                capsule(f"Cost is the question we hear first, and the honest answer is a range, not a fixed number: about {price('residential')} a square foot installed in Central Florida as of {PRICE_DATE}. This page covers financing, rebates, deposits, warranties at resale and the other money questions that come up once a homeowner has that range in hand."),
                body, faqs=faqs, faq_title="Cost questions, answered", crumbs=[("FAQ", "/faq/")], crumb="Cost questions",
                sources=["attampa-cost", "lbs-fl-cost", TOHO_REBATE, SFWMD_HOME, SJRWMD_REBATE, SWFWMD_CONS],
                related=[("/artificial-turf-cost/", "Full cost guide with tables"), ("/artificial-turf-cost/calculator/", "Turf cost calculator"),
                         ("/tools/turf-vs-sod/", "Turf vs. sod ten-year calculator"), ("/faq/", "Back to all FAQ questions")])


# ================================================================== pets & heat
def pets_heat_page():
    body = "".join([
        sec("How hot turf actually gets, and what brings it down",
            f"<p>Heat and pets are the two worries that come up in almost every Kissimmee consultation, so this page leads with a straight answer on both before getting into the specific questions. Full summer sun commonly pushes synthetic turf to 120 to 150°F and sometimes past 160°F ({src('horsemans-heat', 'measured Florida readings')}), while a permeable, well-built pet system drains fast enough that standing water, and the mosquitoes and odor that come with it, isn't the problem people expect it to be ({src('sgw-faq', 'manufacturer drainage data')}).</p>"
            + table("Turf surface temperature by condition", ["Condition", "Typical surface temperature", "What helps"],
                    [["Full sun, mid-afternoon in July", "120–150°F, occasionally over 160°F", "A hose rinse, shade, or a lighter infill color"],
                     ["Full sun, morning or evening", "Noticeably cooler, closer to skin-safe", "The best window for bare feet or a dog's paws"],
                     ["Partial shade at midday", "Meaningfully lower than full sun", "A live oak canopy or shade sail matters more than infill color alone"],
                     ["Right after a hose rinse", "Drops 30–50°F within minutes", "Faster relief than waiting on shade alone"],
                     ["Rinsed, shaded turf after dark", "Close to air temperature", "No different from natural grass once the sun's down"]],
                    f"Readings from {src('magnolia-heat', 'Florida installer measurements')}; drainage rate from {src('sgw-faq', 'manufacturer specifications')}.")),
    ])
    faqs = [
        faq("Will artificial turf be too hot to walk on in July?",
            f"In full sun during peak afternoon, yes, commonly 120 to 150°F and sometimes past 160°F. Thirty seconds under a garden hose cools the surface down 30 to 50 degrees, and mornings and evenings are far more forgiving than 2 p.m. {post('how-hot-does-artificial-turf-get-in-florida', 'This page')} has the full measurements and which infill helps most."),
        faq("Does artificial turf attract mosquitoes, bugs or snakes?",
            "Less than a damp natural lawn does. Mosquitoes need standing water to breed, and a properly built turf base drains faster than a Florida storm falls, so it doesn't hold the puddles they need. Snakes and other wildlife go toward cover and prey, not toward a mowed-looking synthetic surface, though a cluttered yard edge will draw them regardless of what's underfoot."),
        faq("Are dogs actually safer on turf than on a natural lawn?",
            f"In several ways: no fire ants, no chinch-bug spray to keep dogs off of, and a permeable pet-turf backing that doesn't hold urine against the base the way soil sometimes can. {svc('pet', 'The pet turf page')} covers the build differences and what changes with multiple dogs."),
        faq("Could hot turf burn a dog's paw pads?",
            f"It can on an unshaded run in peak afternoon sun, the same way hot asphalt or a metal ramp can. Test it with your own hand first, rinse before playtime, and schedule outdoor time before mid-afternoon in summer. {svc('pet', 'Pet turf')} covers shade and infill choices that help."),
        faq("Can a determined dog dig up or chew through artificial turf?",
            f"Rarely mid-lawn once a dog is past the puppy stage; most damage we see on repair calls is at an unglued edge a digger can get a claw under. {svc('pet', 'The pet turf page')} explains how pet-area perimeters are fastened differently from a standard lawn's."),
        faq("Do fleas and ticks live in artificial grass the way they do in real grass?",
            f"Less readily, since there's no organic thatch or soil layer for eggs to develop in, but it isn't flea-proof on its own. {svc('pet', 'The pet turf page')} covers rinsing and prevention alongside a normal flea routine."),
        faq("Why does pet turf cost more than a regular lawn?",
            f"The permeable backing, the omitted weed barrier and the odor-control infill all add labor and material a plain lawn doesn't need. {svc('pet', 'Pet turf')} runs {price('pet')} a square foot as of {PRICE_DATE}, against {price('residential')} for a standard lawn."),
        faq("Does artificial turf grow mold, mildew or algae in Florida's humidity?",
            "It can, under the same conditions any damp, shaded surface would: heavy tree cover, poor drainage, or organic debris left to rot in the pile. A base that drains properly and a rinse that clears leaves and pollen before a wet week prevent nearly all of it. A lawn that stays dark and matted in deep shade is worth a look at drainage before assuming the turf itself is at fault."),
        faq("Can switching to turf reduce lawn-related allergies?",
            "It can help with grass-pollen sensitivity specifically, since a synthetic lawn doesn't flower or shed pollen the way St. Augustine or Bahia does. It won't touch tree or ragweed pollen drifting in from elsewhere, and dust or mildew from neglected infill can bother some people just as natural thatch would."),
        faq("Does Central Florida ever get cold enough to hurt turf?",
            "Rarely, and when it does, turf handles it better than grass does. An occasional freeze that browns St. Augustine for weeks doesn't touch synthetic fiber; the blades stay green and pliable through anything Kissimmee's mild winters produce. The bigger seasonal stress here is heat, not cold, which is why the rest of this page focuses there."),
        faq("Does artificial turf create noticeable glare in direct sun?",
            f"Not usually; matte, multi-tone blades scatter light rather than reflecting it the way a pool or a metal roof does. What can cause a hot spot is the reverse problem, sunlight reflecting off a nearby window onto the turf, which is a window issue, not a turf one. {post('can-artificial-turf-melt', 'This page')} explains that specific failure."),
        faq("Can spilled pool chemicals stain or damage nearby turf?",
            f"Everyday splash and chlorine or saltwater exposure don't harm the fiber, but a concentrated spill of shock or algaecide can discolor or stiffen it where it lands. {svc('pool', 'The pool turf page')} covers storage and rinsing near a pool deck."),
        faq("Do lovebugs, pollen and other Florida residue damage the turf itself?",
            f"Not the fiber, but the residue can dull its color if it bakes in the sun instead of getting rinsed off. Lovebug season runs roughly April into May and again in late summer, and a same-week hose-down keeps the acidic residue from sitting on the blades. {a('/faq/maintenance/', 'The care and cleaning page')} has the full seasonal schedule."),
        faq("Does a screened pool enclosure change how hot turf inside it gets?",
            f"A little cooler than open sun, since the screen cuts direct UV somewhat, but a cage still gets plenty hot by afternoon. {svc('pool', 'Turf inside a screen enclosure')} covers the glue-down build and drainage a lanai floor needs."),
        faq("Is a lighter turf color actually cooler underfoot?",
            "Yes, modestly. Lighter and multi-tone blades reflect a bit more sun than a single dark green, and a cooling or light-colored infill adds a further few degrees of relief while it stays damp. Shade and a rinse still do more for comfort than color choice alone."),
        faq("How much does having a dog change the infill choice compared to a kid-only yard?",
            f"More than most other factors. A play-only yard can use plain silica sand; a dog yard usually needs zeolite or an antimicrobial coated sand to keep ammonia from building up between rinses. {a('/compare/zeolite-vs-silica-vs-antimicrobial-infill/', 'This infill comparison')} lines up all three side by side."),
    ]
    return page("/faq/pets-heat/", "faq",
                "Pets & Heat FAQ: Artificial Turf in Kissimmee",
                "Dog paws, Florida heat, bugs and humidity: what artificial turf actually does in Kissimmee's climate, answered with a surface-temperature table.",
                "Pets and Heat Questions About Artificial Turf",
                capsule("Heat and pets are the two worries that come up in almost every Kissimmee consultation: will a dog's paws be fine, will a barefoot kid get burned, and does Florida humidity breed mold or bugs underneath. This page answers those directly, with a table of typical surface temperatures, then points to the fuller pet-turf and heat pages for the rest."),
                body, faqs=faqs, faq_title="Pets and heat questions, answered", crumbs=[("FAQ", "/faq/")], crumb="Pets and heat",
                sources=["magnolia-heat", "horsemans-heat", "sgw-faq"],
                related=[("/pet-turf/", "Pet turf, built for dogs"), ("/pool-turf/", "Turf around pools and lanais"),
                         ("/compare/zeolite-vs-silica-vs-antimicrobial-infill/", "Infill compared for odor and heat"), ("/faq/", "Back to all FAQ questions")])


# ================================================================== hoa & permits
def hoa_permits_page():
    body = "".join([
        sec("Three authorities, three different jobs",
            "<p>The state, your city or county, and your HOA each control a different slice of a turf project, and none of the three defers to another the way people assume. The table below sorts common situations by who actually has the final word, with a link to the page that goes deeper on each one.</p>"
            + table("Who signs off on what, situation by situation", ["Situation", "Who decides", "Where to read more"],
                    [["Backyard turf nobody can see from the street", "State law protects it from your HOA; the DEP standard keeps your city or county from a blanket ban", a("/laws/hoa-rules/", "HOA rules")],
                     ["Front-yard turf", "Your city or county can't refuse it if it meets the state standard; your HOA's design review still can shape it", a("/laws/permits/", "Permits by jurisdiction")],
                     ["Turf within 10 ft of a pond, lake or canal", "The state rule sets that setback, not your HOA or your city", a("/laws/florida-hb-683/", "The DEP rule, explained")],
                     ["Turf inside a tree's drip line", "The state rule requires a certified arborist's sign-off, regardless of your HOA's own guidelines", a("/laws/florida-hb-683/", "Rule requirements")],
                     ["Commercial property or a lot over an acre", "State preemption doesn't apply; local code and your association's documents govern fully", a("/commercial-turf/", "Commercial turf")]])),
    ])
    faqs = [
        faq("Will installing turf send extra runoff onto my neighbor's yard?",
            "It isn't supposed to, and the state won't let it. Florida's synthetic turf standard bars any increase in runoff volume, direction or rate onto an adjacent property, along with pooling on your own. Permeable turf and backing over a properly graded, washed-rock base is what keeps a compliant install on the right side of that rule; a clogged or capped-off drainage path is what usually causes a complaint."),
        faq("Is crumb rubber infill allowed under Florida's new turf rule?",
            "Only under playground equipment. Rule 62-308.100 limits infill on the rest of a single-family lot, lawns, dog runs, putting greens, to clean silica sand, rock, shell or other natural material, plus coated silica sand if the coating is non-toxic. Rubber and other synthetic infill are reserved for the ground directly under swings and slides, where a different safety standard applies."),
        faq("What has to happen to my sprinkler system once turf goes in?",
            "Any head that used to water the area gets capped at the valve box, since Florida's synthetic turf standard doesn't allow an in-ground irrigation system to water a synthetic lawn at all. A local government can also require the pipe itself capped, not just the head. From that point, rinsing is by hose, which also cools the surface on a hot afternoon."),
        faq("Can artificial turf cover a septic tank or its drainfield?",
            f"Florida's onsite sewage rules ({ext(FAC_626[1], 'Chapter 62-6, F.A.C.')}) treat covering a drainfield's required area with impervious material as grounds for the health department to step in, and the state's synthetic turf standard separately requires the septic tank lid to stay reachable for pump-out. A permeable product laid over the tank lid, left uncovered by anything solid, is a different question from turf across the whole drainfield; ask your installer and the county health department before running turf over either."),
        faq("How close to my pond or lake can turf actually go?",
            "At least 10 feet back from the ordinary or mean high water line of a lake, pond or canal, unless a seawall or bulkhead already separates the yard from the water. Turf also can't go inside a stormwater pond's littoral zone or within a drainage swale or ditch, even where those spots look like the driest, flattest part of the lot."),
        faq("Can turf go under my oak tree, or does the canopy rule it out?",
            "Not without a certified arborist's sign-off. Florida's synthetic turf standard keeps turf outside a tree's drip line, on your lot or a neighbor's, unless an arborist certifies the installation won't harm the tree. Around Kissimmee's older live oaks that often means mulch or groundcover under the canopy and turf starting only where the branches stop."),
        faq("My backyard is fenced. Does my HOA still have any say?",
            f"Less than you'd think. Since 2023, Florida law has kept an association from restricting artificial turf that isn't visible from the street or a neighboring parcel, which covers most fenced backyards. {a('/laws/hoa-rules/', 'This page')} covers what still counts as visible and what doesn't."),
        faq("What exactly did the 2025 turf law change?",
            f"It created a state floor: DEP's Rule 62-308.100, in force since May 19, 2026, that a city or county can't undercut with a local turf ban on a single-family lot of an acre or less. {a('/laws/florida-hb-683/', 'HB 683 and the DEP rule, in full')} covers every requirement."),
        faq("Does artificial turf count as impervious surface for drainage or permit purposes?",
            f"It depends on the jurisdiction and the permeability of the specific product installed, so there's no single answer across Osceola, Orange, Polk, Lake and Seminole counties. {a('/laws/permits/', 'The permit guide for your city or county')} lists what each office says, and DEP's own standard requires the turf itself to stay permeable regardless."),
        faq("My turf went in before the 2026 rule. Do I have to redo it?",
            f"Nothing we've read describes a retrofit requirement for turf that's already down. If you extend the lawn or replace it, build the new section to the current standard. {svc('replacement', 'Turf replacement')} is usually the moment an older install gets brought up to code."),
        faq("Which office do I even call, the city or the county?",
            f"It depends on your parcel, not your mailing address; a Kissimmee address can sit inside the city, in unincorporated Osceola County, or across a line into Orange or Polk. {a('/laws/permits/', 'The permit guide')} lists what each office requires and how to find out which one has your lot."),
        faq("I live in a CDD, not an HOA. Does any of this still apply?",
            "The state turf standard applies to the property regardless of what governs it. A community development district is a unit of local government, not a private association, so the HOA-visibility statute doesn't cover it directly; check whether a separate HOA inside the CDD handles design review instead."),
        faq("Will a hurricane or heavy flooding tear turf loose?",
            f"A properly built lawn is anchored at every edge and seam specifically to withstand wind and flooding under the state standard, so isolated lifting after a named storm is a repair, not a rebuild. {post('artificial-turf-hurricane-flooding', 'This page')} covers what actually happens and when to call someone."),
        faq("Does a turf project need to go through my mortgage company or lender?",
            "Not typically for a straightforward backyard lawn; that's a landscaping change, not a structural one requiring lender approval. A larger project that changes drainage significantly, or that's financed against the home, is worth a quick call to whoever holds the note, but most turf jobs don't touch that at all."),
        faq("Can a renter install turf without the landlord's written approval?",
            "No. The HOA-visibility statute protects an owner's or tenant's installation from the association, but a tenant still needs the property owner's permission for the alteration itself. Get that in writing before ordering material, along with who's responsible for it at move-out."),
        faq("What does it mean that the state rule creates no new DEP permit?",
            "It means Rule 62-308.100 sets a material and installation standard, not a new state-level application to file. Whatever permit process your city or county already runs, for drainage, grading or a building permit, still applies where it applied before; the rule just limits what that local process can prohibit."),
    ]
    return page("/faq/hoa-permits/", "faq",
                "HOA & Permit FAQ: Artificial Turf in Florida",
                "Setbacks from water, tree drip lines, septic tanks and who regulates what: Florida turf law and permit questions, answered for Kissimmee.",
                "HOA, Law and Permit Questions About Artificial Turf",
                capsule("Three different authorities can have an opinion about a Florida yard, the state, your city or county, and your HOA, and they don't overlap the way most people assume. This page answers the specific situations that come up most: setbacks from water, tree drip lines, septic tanks, sprinklers, and who actually gets the final word on each one."),
                body, faqs=faqs, faq_title="HOA, law and permit questions, answered", crumbs=[("FAQ", "/faq/")], crumb="HOA, law and permits",
                sources=["dep-rule", "fs7203045", "hb683", "marathon-pr", FAC_626],
                related=[("/laws/", "Florida turf laws, HOA rules and permits"), ("/laws/florida-hb-683/", "HB 683 and the DEP rule, in full"),
                         ("/laws/permits/", "Permits by city and county"), ("/faq/", "Back to all FAQ questions")])


# ================================================================== maintenance
def maintenance_page():
    body = "".join([
        sec("A quick care calendar",
            "<p>Artificial turf takes a fraction of the upkeep a lawn does, but a fraction isn't zero. The schedule below covers what a Kissimmee lawn actually needs across a year; the questions after it cover the specific problems and edge cases that don't fit neatly into a calendar.</p>"
            + table("A quick care calendar", ["Season or trigger", "What to do"],
                    [["Every week or two", "Hose rinse; more often on a dog yard"],
                     ["Monthly", "Power broom against the grain wherever traffic has matted the pile"],
                     ["Late winter into spring", "Rake off live oak leaf drop before storms work it into the infill"],
                     ["Spring and late summer", "A same-week rinse after each lovebug swarm keeps residue from staining the blades"],
                     ["Twice a year", "A deeper sanitizing clean and infill top-up, spring and fall"],
                     ["After any named storm", "Walk every edge and seam for anything wind or rain lifted"]])
            + "<p>None of this calendar involves a sprinkler zone. Florida's synthetic turf standard doesn't allow an in-ground irrigation system to water a synthetic lawn at all, so every rinse on that schedule, weekly, monthly or after a storm, is by hose or a portable sprinkler moved by hand.</p>"),
    ])
    faqs = [
        faq("Does artificial grass fade or change color as it ages?",
            f"Some fading is normal. UV-stabilized polyethylene loses a bit of saturation over 10 to 20 years in full Florida sun ({src('stn-life', 'manufacturer lifespan data')}), faster on an unshaded, south-facing lawn than on a partly shaded one. It's a slow, even change, not the patchy discoloration a poorly built or damaged lawn shows, and it doesn't affect drainage or feel underfoot."),
        faq("Do weeds ever grow through artificial turf?",
            "Occasionally, at a seam, an unsealed edge, or wherever windblown seed lands in the infill itself rather than actually pushing up through the backing. A weed barrier under the base cuts that down further, though it gets skipped under pet areas because it traps urine instead. An occasional weed at the perimeter is a five-minute pull, not a sign the lawn failed."),
        faq("Can I use a pressure washer to clean artificial turf?",
            "We don't recommend it. A pressure washer can blow infill out of the pile, fray blade tips, and on an older lawn loosen a seam that a garden hose would leave alone. A steady hose rinse plus a stiff push broom against the grain does the job a pressure washer is tempted to rush."),
        faq("Can I put a grill, fire pit, trampoline or pool furniture on my turf?",
            "A grill or fire pit needs to stay off turf entirely; a stray coal or radiant heat melts polyethylene fiber the same way a cigarette does. A trampoline or heavy furniture won't burn it, but legs left in one spot for months can flatten the pile and press infill down; moving furniture occasionally and using a pad under trampoline legs both help."),
        faq("How do I fix a wrinkle or wave that's shown up in the lawn?",
            f"Lift the panel, pull it drum-tight, and re-secure the edge; weighting or ironing a bump only hides it until the next hot week. {svc('repair', 'The turf repair page')} covers this and the other common failures, cause by cause."),
        faq("An edge of my turf lifted after a storm. Is that urgent?",
            f"Worth handling within a week or two, since wind and standing water both work under a lifted corner and can widen the problem. {svc('repair', 'A repair visit')} for this is usually quick if the base underneath is still sound."),
        faq("How often should pet turf actually be rinsed and deep cleaned?",
            f"A hose rinse most days at the spot a dog favors, at least weekly across the whole run, and a professional deep clean with an enzyme treatment every three to four months. {svc('cleaning', 'The turf cleaning page')} has the full calendar and what changes with more than one dog."),
        faq("Can a cigarette or a firework leave a permanent burn mark on turf?",
            f"Yes, a dropped ember or a spent firework can scorch a small area the same way a reflected window flare can, since polyethylene fiber softens around 175 to 200°F. {svc('repair', 'A burn patch is usually a small, matched repair')}, not a reason to redo the whole lawn."),
        faq("Can I drive a car or a golf cart across turf without wrecking it?",
            "An occasional pass won't hurt a properly built lawn, but repeated wheel traffic in the same track compresses the base and flattens the pile faster than foot traffic does. If a vehicle needs to cross regularly, a paver strip or turf-and-paver ribbon in that exact path holds up better than turf alone."),
        faq("Is it safe to use a leaf blower on artificial turf?",
            "Yes, and it's one of the easier ways to clear debris without pressing leaves and lovebug residue down into the infill the way a rake sometimes does. Use it on a normal setting; there's nothing turf-specific to worry about."),
        faq("Does a turf lawn still need any kind of lawn service?",
            f"Not mowing or fertilizing, but occasional brushing, rinsing and an infill top-up are real maintenance, even if it's a fraction of what a natural lawn takes. Some owners handle it themselves with a hose and a stiff broom; others book {svc('cleaning', 'a yearly cleaning visit')} and skip the upkeep entirely."),
        faq("What do terms like face weight and pile height on a spec sheet mean?",
            f"Face weight is how much fiber sits on each square yard of backing, roughly how dense the lawn is; pile height is how tall the blades stand. {post('artificial-turf-glossary', 'The turf glossary')} defines those and the rest of the vocabulary a quote uses."),
        faq("How many years should a well-built lawn actually last?",
            f"Ten to twenty years is the typical range, depending on UV stabilization, foot traffic and infill choice, with unshaded Central Florida lawns usually landing toward the lower end of that. {post('how-long-does-artificial-turf-last-in-florida', 'This page')} breaks lifespan down by use and product grade."),
        faq("What's the right way to deal with oak leaves and pine needles on turf?",
            f"Rake or blow them off promptly rather than letting an afternoon storm work them into the pile, since wet leaves left sitting can stain the fiber. {post('oak-leaves-and-debris-on-artificial-turf', 'This page')} covers debris season month by month."),
        faq("Will the seams between rolls of turf be visible once it's installed?",
            "Not on a well-run job. Rolls are laid so the grain runs the same direction and seams are cut between stitch rows, then taped and glued so the join disappears into the pile. A visible ridge or color break at a seam usually means the grain direction didn't match or the wrong dye lot was used."),
        faq("Does artificial turf cause static shock the way carpet sometimes does?",
            "Rarely outdoors. Static builds up in dry, insulated conditions, and a turf lawn sits on damp ground, gets rained on, and stays grounded the whole time, unlike carpet over a dry subfloor indoors. It isn't a complaint we hear about installed lawns here."),
    ]
    return page("/faq/maintenance/", "faq",
                "Turf Care & Repair FAQ, Kissimmee, FL (2026)",
                "How often to rinse, when a wrinkle needs fixing, and how long turf lasts in Florida: care, repair and lifespan questions, answered plainly.",
                "Care, Repair and Lifespan Questions About Artificial Turf",
                capsule("Artificial turf takes far less work than a lawn, but not none: a rinse schedule, an occasional brush, and knowing when a wrinkle or a lifted edge needs a repair rather than a shrug. This page answers the specific care, damage and lifespan questions that come up most, with a quick calendar and links to the deeper repair and cleaning pages."),
                body, faqs=faqs, faq_title="Care, repair and lifespan questions, answered", crumbs=[("FAQ", "/faq/")], crumb="Care, repairs and lifespan",
                sources=["stn-life", "dep-rule"],
                related=[("/turf-repair/", "Artificial turf repair"), ("/turf-cleaning/", "Turf cleaning and maintenance"),
                         ("/turf-replacement/", "When to replace instead of repair"), ("/faq/", "Back to all FAQ questions")])


def get_pages():
    return [index_page(), cost_page(), pets_heat_page(), hoa_permits_page(), maintenance_page()]
