# -*- coding: utf-8 -*-
"""Law hub: /laws/, /laws/florida-hb-683/, /laws/hoa-rules/. Informational, not legal advice."""
from _posts import PERMIT_PAGES
from _helpers import page, capsule, sec, table, faq, ul, steps, note, cta, a, svc, city, county, post, src, ext

DISC = [note("We install turf; we aren't attorneys. This page summarizes public statutes and rules as we read them in September 2026 and links to the text. For a dispute with an association or a code office, talk to a Florida attorney."),
        note("Nothing here is legal advice. It's our reading of F.S. 125.572 and the public summaries of Rule 62-308.100, checked in September 2026; the rule text controls, and a code office or attorney should confirm anything your project depends on."),
        note("An installer wrote this, not a lawyer. Statutes are quoted as they stood in September 2026 and every claim links to its source; if your board or management company disagrees, a Florida community-association attorney is the right next call.")]


def get_pages():
    crumbs = [("Laws & HOA", "/laws/")]

    # ------------------------------------------------------------------ hub
    hub_body = "".join([
        sec("Who gets a say over artificial turf on a Florida lot?",
            "<p>Three different authorities can weigh in, and they don't overlap the way most people assume. The state sets the floor for single-family lots. Your city or county handles permits, drainage and anything the state rule doesn't reach. Your homeowners association, if you have one, runs on its own contract with you and isn't bound by the state turf law at all.</p>"
            + table("Who regulates what", ["Authority", "What it controls", "What changed recently", "Read more"],
                    [["State of Florida (F.S. 125.572 and DEP Rule 62-308.100)", "Minimum installation standards on single-family lots of one acre or less; stops local bans", "Rule effective May 19, 2026", a("/laws/florida-hb-683/", "HB 683 and the DEP rule")],
                     ["City or county", "Permits, lot drainage, easements, rights-of-way, commercial and multi-family sites, lots over one acre", "Can no longer prohibit compliant turf on covered lots, or regulate it inconsistently with the state standard", a("/laws/permits/", "Permits by jurisdiction")],
                     ["HOA or condo association", "Appearance rules in the declaration, architectural review", "Since July 2023 can't restrict turf that isn't visible from the frontage or a neighboring parcel (F.S. 720.3045)", a("/laws/hoa-rules/", "HOA rules and turf")]])),
        sec("The short version for a homeowner",
            ul(["<strong>Backyard, fenced, not visible from the street or next door:</strong> state law protects it from HOA restriction, and your city or county can't ban turf that meets the DEP standard.",
                "<strong>Front yard:</strong> the city or county can't prohibit compliant turf on a covered lot, but your HOA still can. Expect an architectural review application.",
                "<strong>Beside a lake, pond or canal:</strong> the state standard keeps turf at least 10 feet back from the water line and out of pond banks and littoral zones.",
                "<strong>Under a live oak:</strong> turf stays outside the drip line unless a certified arborist certifies it won't harm the tree.",
                "<strong>In the side-yard swale:</strong> no. Swales, ditches and stormwater ponds are excluded.",
                "<strong>Sprinklers:</strong> an in-ground irrigation system can't be used to water synthetic turf. Heads under the turf are capped.",
                "<strong>Commercial property, apartments, lots over an acre:</strong> the state preemption doesn't apply. Local code governs."])
            + f"<p>Those points come from the {src('marathon-pr', 'summary a Florida city published when the rule took effect')} and from the statute itself. The pages in this section go through each one with the citations, and the {a('/faq/hoa-permits/', 'HOA and permit FAQ')} keeps the short answers in one place.</p>"),
        sec("Permit pages for the places we work",
            "<p>Whether you need a permit for a residential turf job depends on which office has your parcel. A Kissimmee mailing address can be inside the City of Kissimmee, in unincorporated Osceola County, or across the line in Orange or Polk. Each page below says what that jurisdiction publishes, who to call and how to check which one you're in.</p>"
            + ul([a(f"/laws/permits/{k}/", v) for k, v in PERMIT_PAGES.items()])),
        sec("Why this matters more in Central Florida than most places",
            f"<p>Around Kissimmee the three layers collide constantly. Most subdivisions built since the 1990s have an association, many have a retention pond behind the back fence, and lot lines put a drainage swale between nearly every pair of houses. Add the short-term-rental communities along US-192 and I-4, where an out-of-state owner, a property manager and a resort review board all have opinions, and a simple backyard job can involve more paperwork than digging. Knowing which rule comes from which authority is what keeps a project from stalling. It's also why a turf layout in {city('harmony')} or {city('lake-nona')}, with water on one side, looks different from one on an interior lot in {city('buenaventura-lakes', 'BVL')}.</p>"),
        sec("How we handle the paperwork",
            f"<p>On a quote we note which jurisdiction the parcel sits in, whether there's a waterbody, swale or protected tree that limits where turf can go, and whether an association review is needed. If an ARC application is required, we assemble it: a physical sample, the manufacturer's spec sheet showing permeability and the PFAS and heavy-metal statement, a site plan with the turf area drawn, and a drainage note. The {a('/tools/hoa-packet-checklist/', 'HOA application checklist')} lists what reviewers usually want. Starting from {svc('residential', 'a residential lawn quote')} is the easiest way to get all of that on paper.</p>"
            + DISC[0]),
    ])
    hub = page("/laws/", "law", "Florida Artificial Turf Laws, HOA Rules & Permits (2026)",
               "Florida's synthetic turf rule took effect May 19, 2026. What the state, your city or county and your HOA can each control, with sources for Central Florida.",
               "Artificial turf laws, HOA rules and permits in Florida",
               capsule("As of September 2026, Florida law stops cities and counties from banning synthetic turf on single-family lots of one acre or less when it meets DEP Rule 62-308.100, in force since May 19, 2026. Homeowners associations are separate: they can't restrict turf hidden from the street and neighbors, but they still control front yards."),
               hub_body, crumb="Laws & HOA", sources=["hb683", "fs125572", "dep-rule", "marathon-pr", "fs7203045", "stc-fl"],
               faqs=[faq("Is this legal advice?", "No. It's an installer's plain-language summary of public law with links to the text. Statutes get amended and associations differ, so confirm anything that matters with the agency involved or a Florida attorney."),
                     faq("Which law came first, the HOA statute or the turf statute?", "The HOA provision, F.S. 720.3045, took effect July 1, 2023. HB 683, which created F.S. 125.572 for local governments, took effect July 1, 2025, and the DEP rule that activates its preemption took effect May 19, 2026."),
                     faq("Does any of this apply to condos?", "Not directly. F.S. 720.3045 covers homeowners associations under Chapter 720, and F.S. 125.572 covers single-family residential lots. Condominium balconies and common elements are governed by Chapter 718 and the condo documents.")],
               related=[("/laws/florida-hb-683/", "HB 683 and DEP Rule 62-308.100, requirement by requirement"), ("/laws/hoa-rules/", "What a Florida HOA can and can't restrict"), ("/laws/permits/", "Permits by city and county"), ("/blog/artificial-turf-front-yard-florida/", "Turf in a Florida front yard")])

    # ------------------------------------------------------------------ HB 683
    hb_body = "".join([
        sec("Is artificial turf legal in Florida? What did HB 683 change?",
            f"<p>Yes. Synthetic turf was never illegal statewide, but some Florida cities banned it, limited it to backyards or counted it as pavement. {src('hb683', 'HB 683')}, signed in 2025, created {src('fs125572', 'section 125.572 of the Florida Statutes')}. It told the Department of Environmental Protection to write minimum installation standards for single-family residential lots of one acre or less, and it barred local governments from prohibiting turf that meets those standards or regulating it in a way that conflicts with them.</p>"
            "<p>The catch was timing. The preemption only switched on once DEP adopted its rule. For most of a year, local ordinances stayed in force while the department held a workshop in August 2025 and published a proposed rule in January 2026.</p>"),
        sec("When did the DEP synthetic turf rule take effect?",
            f"<p>{src('dep-rule', 'Rule 62-308.100, Florida Administrative Code')}, titled Synthetic Turf, took effect on <strong>May 19, 2026</strong>. Its chapter is named \"Minimum Standards for the Installation of Synthetic Turf on Specified Properties,\" and it lists F.S. 125.572 as both its authority and the law it implements. From that date, a Florida city or county can't enforce a ban on compliant synthetic turf on a covered lot.</p>"
            + table("Timeline of Florida's synthetic turf law", ["Date", "What happened"],
                    [["July 1, 2023", "F.S. 720.3045 takes effect: HOAs can't restrict items not visible from the frontage or an adjacent parcel, naming artificial turf"],
                     ["July 1, 2025", "HB 683 takes effect, creating F.S. 125.572 and directing DEP to set standards"],
                     ["August 5, 2025", "DEP rule development workshop in Tallahassee"],
                     ["January 20, 2026", "DEP publishes its Notice of Proposed Rule for Chapter 62-308"],
                     ["May 19, 2026", "Rule 62-308.100 becomes effective; local prohibitions on compliant turf end for covered lots"]])),
        sec("What does Rule 62-308.100 require?",
            f"<p>{src('dep-rule', 'The rule')} is short, about a page, and organized under nine headings: scope, material type, color, permeability, stormwater management, potable water conservation, water quality, proximity to trees, and other factors affecting neighboring properties. It creates no new state permit. Here is each requirement in plain terms, next to what it means on a job.</p>"
            + table("Florida's minimum standards for synthetic turf on single-family lots (Rule 62-308.100, F.A.C.)",
                    ["What the rule says", "What it means for the job"],
                    [["Turf, backing and infill must contain no heavy metals and no intentionally added PFAS, and must be disposable at a Florida-permitted landfill", "Get the manufacturer's written statement and keep it with the quote"],
                     ["Infill may only be clean silica sand, rock, shell or other natural material; coated silica sand is allowed if the coating is non-toxic. Rubber or other synthetic infill only within the footprint of playground equipment", "No crumb rubber or plastic pellets on a lawn, dog run or putting green. Silica, zeolite and coated sands are fine"],
                     ["Infill must not wash off the property", "Edges detailed so a storm doesn't carry sand into the street or the neighbor's yard"],
                     ["Subgrade of natural material such as crushed rock or crushed concrete, washed before installation so fines don't bind; soil beneath not compacted to the point it hurts percolation", "A washed, free-draining base instead of dusty road base that sets into a crust"],
                     ["Green synthetic turf shall be allowed", "A local code can't require an odd color or reject green"],
                     ["Permeable turf on permeable backing over a pervious subgrade graded for positive drainage; a local government may set a standard of at most 10 inches per hour for all layers", "Perforated or fully permeable backing, and a base that drains as fast as the turf"],
                     ["No pooling, and no increase in runoff volume, direction or rate onto adjacent properties; not within a swale, ditch, stormwater pond or a pond's littoral zone", "Turf stops at the top of the side-yard swale and stays off retention-pond banks"],
                     ["In-ground irrigation can't be used to irrigate synthetic turf; a local government may require heads removed and pipes capped", "Sprinkler heads under the turf are capped; rinsing is by hose"],
                     ["Where no local buffer exists, at least 10 feet from a natural or man-made waterbody, measured from the ordinary or mean high water line, unless a physical barrier such as a seawall or bulkhead stands between", "Lake, canal and pond lots get a planted buffer strip; a seawalled canal lot doesn't need one"],
                     ["Not inside tree drip lines, on the property or on adjacent properties, unless a certified arborist certifies it won't harm the tree", "Under a live oak, plan on mulch or groundcover inside the canopy, or get the arborist's letter first. The neighbor's oak counts too"],
                     ["Installed to the manufacturer's specifications and anchored at all edges and seams to withstand wind or flooding", "Glued and taped seams, a nailed or restrained perimeter, nothing loose-laid"],
                     ["Must leave access to the septic tank for routine pump-out; must sit landward of any dune system", "On septic lots in rural St. Cloud or Polk County, the tank lid stays reachable under a removable panel or outside the turf"]],
                    "Paraphrased from Rule 62-308.100, F.A.C., effective May 19, 2026. The rule text controls.")
            + f"<p>Most of that is how a careful installer already builds in Central Florida. Three items change real projects here. The 10-foot setback matters on the many lake and pond lots in Kissimmee, St. Cloud, Lake Nona and Harmony. The drip-line rule changes the conversation in older neighborhoods where the reason grass won't grow is a 60-foot live oak; {post('artificial-turf-near-live-oaks-and-palms', 'turf near live oaks and palms')} goes into that. And the infill rule ends the use of crumb rubber on home lawns, which we never liked in Florida heat anyway.</p>"),
        sec("What the law doesn't do",
            ul(["<strong>It doesn't override your HOA.</strong> Section 125.572 restricts local governments. Association covenants are a private contract governed by Chapter 720. " + a("/laws/hoa-rules/", "See the HOA page") + ".",
                "<strong>It doesn't cover every property.</strong> Single-family residential lots of one acre or less only. Commercial sites, apartments, condos and larger lots still answer to local code.",
                "<strong>It doesn't erase permits.</strong> A city or county can still require a permit and review drainage, easements and rights-of-way, as long as it doesn't prohibit compliant turf or contradict the state standard. " + a("/laws/permits/", "Check your jurisdiction") + ".",
                "<strong>It doesn't make turf \"Florida-Friendly Landscaping.\"</strong> That's a separate program under F.S. 373.185, and " + src("ifas-turf", "UF/IFAS doesn't class synthetic turf as Florida-Friendly") + "."])),
        sec("A worked example",
            "<p>Say you own a 0.22-acre lot in unincorporated Osceola County with a retention pond behind the fence and a swale along the left side. You want the 900 sq ft backyard done. Under the state standard the turf has to stop 10 feet short of the pond's water line and at the top of the swale, which might leave 640 sq ft of turf and a planted buffer along the back. The sprinkler zone in that area gets capped. The county can't refuse the turf itself, though it can still ask for a permit or a drainage review if its code calls for one. If you're in an HOA, the backyard is protected from restriction so long as it isn't visible from the frontage or a neighbor's parcel.</p>"
            + DISC[1] + cta("Ask us to check your lot", "We’ll mark the setbacks, swales and drip lines before quoting.")),
    ])
    hb = page("/laws/florida-hb-683/", "law", "Florida HB 683 & DEP Rule 62-308.100: Synthetic Turf Law",
              "Florida's synthetic turf rule, 62-308.100, took effect May 19, 2026. What HB 683 changed, each installation standard, and what cities can still regulate.",
              "Florida HB 683 and the DEP synthetic turf rule, explained",
              capsule("Florida HB 683 created F.S. 125.572, and DEP Rule 62-308.100 put it into force on May 19, 2026. On single-family lots of one acre or less, cities and counties can no longer ban synthetic turf that is permeable, free of added PFAS and heavy metals, 10 feet from waterbodies, out of swales and tree drip lines, and not irrigated by an in-ground system. Infill must be natural or coated sand."),
              hb_body, crumbs=crumbs, crumb="HB 683 & DEP rule", sources=["hb683", "fs125572", "dep-rule", "dep-rulemaking", "marathon-pr", "ifas-turf", "stc-fl"],
              faqs=[faq("Does HB 683 apply to lots bigger than one acre?", "No. Section 125.572 covers single-family residential properties of one acre or less. On a larger lot, your county or city's landscape and zoning code still decides what's allowed."),
                    faq("Can my city still require a permit for turf?", "It can require a permit and review drainage, easements and rights-of-way. What it can't do on a covered lot is prohibit turf that meets the DEP standard or impose rules that conflict with it."),
                    faq("Can I keep one sprinkler zone to cool the turf?", "Not an in-ground one. The standard says in-ground irrigation systems can't be used to irrigate synthetic turf areas. A hose rinse does the same job and drops the surface temperature 30 to 50 degrees in a minute or two."),
                    faq("My turf was installed before May 2026. Do I have to change it?", "The summaries we've read describe installation standards and don't mention retrofits. If you replace the turf or extend it, build the new work to the standard. For anything beside a pond or inside a drip line, ask your local code office."),
                    faq("Who enforces the DEP turf standard?", "The rule sets the standard; day-to-day enforcement runs through local code and permitting offices, which may now regulate only in ways consistent with it. DEP's Division of Water Restoration Assistance handled the rulemaking.")],
              related=[("/laws/hoa-rules/", "HOA rules: what F.S. 720.3045 covers"), ("/laws/permits/", "Permits by city and county"), ("/blog/is-artificial-turf-safe-for-kids-pfas-lead/", "PFAS, lead and turf safety"), ("/blog/artificial-turf-front-yard-florida/", "Turf in a front yard")])

    # ------------------------------------------------------------------ HOA
    hoa_body = "".join([
        sec("Can my HOA ban artificial turf in Florida?",
            f"<p>Partly. Since July 1, 2023, {src('fs7203045', 'section 720.3045')} says an association may not restrict parcel owners or tenants from installing, displaying or storing items that are \"not visible from the parcel's frontage or an adjacent parcel, including, but not limited to, artificial turf.\" If your backyard is fenced so that neither the street nor the neighbors can see the turf, the association can't prohibit it. If the turf would be visible, including nearly every front yard, the declaration and the architectural review process still apply.</p>"
            f"<p>The 2025 turf law doesn't change that. HB 683 limits cities and counties, and an HOA is neither ({src('stc-fl', 'Synthetic Turf Council FAQ on Florida law')}).</p>"),
        sec("What \"not visible\" means in practice",
            "<p>The statute doesn't define visibility with a measurement, so it comes down to sight lines. A six-foot privacy fence on a flat interior lot usually settles it. It gets harder on a corner lot, on a lot that backs onto a golf course or pond with an open rail fence, and next to a two-story house whose upstairs windows look down into your yard. Associations have argued that a second-floor view counts as visible from an adjacent parcel. We haven't seen a Florida appellate decision that settles the point.</p>"
            + table("How F.S. 720.3045 tends to play out by yard type", ["Situation", "Protected from HOA restriction?", "What we suggest"],
                    [["Backyard behind a solid 6-ft fence, single-story neighbors", "Usually yes", "Send the ARC a courtesy notice with the spec sheet anyway"],
                     ["Backyard with open picket or aluminum rail fence", "Often disputed", "Apply through the ARC; add hedge screening to the plan"],
                     ["Backyard on a pond or golf course", "Often disputed, and the 10-ft state setback from water applies", "Apply; show the buffer strip on the site plan"],
                     ["Side yard visible from the street", "No", "Full ARC application"],
                     ["Front yard", "No", "Full ARC application; expect conditions on color, pile height and borders"]],
                    "Our reading of how the statute is applied, not a legal opinion.")),
        sec("Does the law apply to declarations written before 2023?",
            f"<p>That's the open question. A statute that changes existing contract rights can be challenged as an unconstitutional impairment, and Florida courts look at whether a declaration adopts future amendments to the law, wording lawyers call Kaufman language. {src('olg-720', 'The Orlando Law Group’s analysis')} concludes that owners can likely rely on the statute for now because new laws are presumed valid until a court says otherwise, while noting an association could bring a challenge. If your board cites its older documents, that's the moment to get an attorney's opinion rather than an installer's.</p>"),
        sec("Isn't turf \"Florida-Friendly Landscaping\" that an HOA can't prohibit?",
            f"<p>No, and that argument tends to backfire. {src('fs7203075', 'Section 720.3075(4)')} stops associations from prohibiting Florida-Friendly Landscaping as defined in F.S. 373.185, which is about plants, water conservation and soil. {src('ifas-turf', 'UF/IFAS, which runs the program, doesn’t treat synthetic turf as Florida-Friendly')}. Use section 720.3045 for a hidden backyard and the ARC process for anything else.</p>"),
        sec("How to get an ARC approval for visible turf",
            steps([("Read the declaration and the design guidelines first.", "Look for words such as \"sod,\" \"living ground cover\" or a minimum percentage of landscaped area. If turf is named and banned, ask what it would take to amend the guidelines; many boards have loosened them since 2023."),
                   ("Submit a complete packet.", "Application form, a physical sample at least a foot square, the manufacturer's spec sheet, a site plan with dimensions, border details, and a drainage note saying grades and swales stay unchanged."),
                   ("Answer the three objections before they're raised.", "It looks fake: choose a multi-tone blade with thatch, 1.5 to 1.9 inches. It floods the neighbor: show the permeable backing and the base. It's plastic: include the no-added-PFAS and heavy-metals statement the state standard now requires."),
                   ("Keep it in writing.", "Florida's HOA statute sets procedures for architectural review; get the decision, and any conditions, on paper.")])
            + f"<p>We prepare this packet as part of a {svc('residential', 'residential turf quote')}. The {a('/tools/hoa-packet-checklist/', 'HOA application checklist')} lists every item, and {post('artificial-turf-front-yard-florida', 'the front-yard article')} covers the design choices that get approvals. Resort communities in the short-term-rental belt have their own habits; see {svc('str', 'turf for vacation rental homes')}.</p>"
            + DISC[2]),
    ])
    hoa = page("/laws/hoa-rules/", "law", "Can a Florida HOA Ban Artificial Turf? F.S. 720.3045 Explained",
               "Florida HOAs can't restrict artificial turf that isn't visible from the street or a neighboring lot (F.S. 720.3045, 2023). Front yards still need ARC approval.",
               "Can a Florida HOA ban artificial turf?",
               capsule("Under F.S. 720.3045, in effect since July 1, 2023, a Florida homeowners association can't restrict artificial turf that isn't visible from the parcel's frontage or an adjacent parcel, which protects most fenced backyards. Visible areas, including front yards, still fall under the HOA's declaration and architectural review. HB 683 doesn't change that."),
               hoa_body, crumbs=crumbs, crumb="HOA rules", sources=["fs7203045", "fs7203075", "olg-720", "stc-fl", "ifas-turf", "hb683", "marathon-pr"],
               faqs=[faq("My HOA fined me for backyard turf nobody can see. What now?", "Point the board to F.S. 720.3045 in writing and ask which sight line they believe makes it visible. If they hold their position, Florida's HOA statute provides for pre-suit mediation, and an attorney's letter often resolves it sooner."),
                     faq("Does the HOA statute cover renters?", "Yes. Section 720.3045 refers to parcel owners or their tenants. A tenant still needs the owner's permission to alter the yard."),
                     faq("Can an HOA require a specific turf product or color?", "For visible areas, an association with architectural control in its declaration can set reasonable standards such as blade color, pile height and border materials. Ask for the standard in writing before you order material."),
                     faq("Do I have to apply to the ARC for a hidden backyard?", "The statute says the association may not restrict it, but many declarations still require an application for any exterior change. Filing a short notice with the spec sheet costs nothing and avoids an argument later."),
                     faq("We're in a CDD, not an HOA. Does any of this apply?", "A community development district is a unit of local government, not an association, so it isn't covered by Chapter 720. Many CDD communities also have an HOA that handles architectural review. Check which entity issued your design guidelines.")],
               related=[("/laws/florida-hb-683/", "HB 683 and the DEP turf rule"), ("/tools/hoa-packet-checklist/", "HOA / ARC application checklist"), ("/blog/artificial-turf-for-55-plus-communities/", "Turf in 55+ communities"), ("/faq/hoa-permits/", "More HOA and permit questions")])
    return [hub, hb, hoa]
