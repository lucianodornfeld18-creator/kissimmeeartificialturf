# -*- coding: utf-8 -*-
"""Blog cluster: safety, product, licensing and process (module c_posts_c in _posts.py).
Ten posts: licensing and vetting a contractor, PFAS/lead safety, environmental trade-offs,
turf near live oaks and palms, pile height and face weight by use, what specs hold up in
Florida, front-yard legality, shady side yards, the install sequence step by step, and a
35-plus term glossary."""
from _helpers import page, capsule, sec, table, faq, ul, steps, note, cta, a, svc, post, src, ext

CRUMBS = [("Blog", "/blog/")]
PUB = "2026-09-21"

# ---------------------------------------------------------------- sources not already in _data.SOURCES
DBPR_CH489 = ("Florida DBPR — Construction Industry Licensing Board, statutes and rules", "https://www2.myfloridalicense.com/construction-industry/statutes-and-rules/")
FLCARE_LICENSE = ("Florida Lawn Care Authority — landscaping contractor licensing and certification requirements", "https://floridalawncareauthority.com/florida-landscaping-contractor-licensing/")
SUNBIZ = ("Florida Division of Corporations — Sunbiz business entity search", "https://search.sunbiz.org/")
OSCEOLA_BTR = ("Osceola County Tax Collector — local business tax receipt", "https://osceolataxcollector.org/local-business-tax-receipt/")
ORANGE_BTR = ("Orange County, FL — Business Tax Receipt (BTR)", "https://www.ocfl.net/PermitsLicenses/Permits/BTR.aspx")
POLK_BTR = ("Polk County Tax Collector — local business taxes", "https://www.polktaxes.com/services/local-business-taxes/")
WC_SEARCH = ("Florida Division of Workers' Compensation — Exemption Search database", "https://dwcdataportal.fldfs.com/Exemption.aspx")
WC_EXEMPT_CONST = ("Florida DFS — Workers' Compensation exemptions, construction industry", "https://www.myfloridacfo.com/division/wc/employer/exemptions/construction")
CPSC_LEAD = ("U.S. CPSC — Lead in Artificial Turf, 2008 staff analysis", "https://www.cpsc.gov/content/Lead-in-Artificial-Turf")
EPA_FRAP = ("EPA & CDC/ATSDR — Federal Research Action Plan on recycled tire crumb rubber, final reports", "https://archive.cdc.gov/www_atsdr_cdc_gov/frap/federal_research_action_plan.html")
OSCEOLA_FERT = ("Osceola County — fertilizer management (NPDES)", "https://www.osceola.org/My-Property/Flooding-and-Stormwater/Stormwater-Management/Pollutant-Discharge-Elimination-System-NPDES/Fertilizer-Management")
ORANGE_FERT = ("Orange County, FL — new rules for fertilizer use, press release", "https://newsroom.ocfl.net/media-advisories/press-releases/2022/06/new-rules-for-fertilizer-use-now-in-effect-in-orange-county/")
ISA_ROOT = ("International Society of Arboriculture, Rocky Mountain Chapter — protecting trees from construction damage", "https://isarmc.org/protecting_trees_from_damage")
IFAS_TREEPROTECT = ("UF/IFAS EDIS UW323 — conservation subdivision construction phase, protecting trees", "https://edis.ifas.ufl.edu/publication/UW323")
GLOBALSYNTURF_PILE = ("Global Syn-Turf — synthetic turf buying guide: how to choose pile height", "https://www.globalsynturf.com/synthetic-turf-buying-guide-pile-height")
MSI_SURFACES = ("MSI Surfaces — artificial grass features: pile height, face weight and total weight", "https://www.msisurfaces.com/blogs/post/2023/07/12/how-to-choose-the-best-artificial-grass-for-your-project-understanding-pile-height,-face-weight,-and-total-weight.aspx")
STC_SPEC = ("Synthetic Turf Council — guidelines for synthetic turf performance and ASTM test methods", "https://www.mvcommission.org/sites/default/files/docs/stc_guidelines_for_synthetic.pdf")
IFAS_STAUG = ("UF/IFAS Agronomy — Homeowners Guide to St. Augustinegrass Management", "https://agronomy.ifas.ufl.edu/media/agronomyifasufledu/turfgrass-science/turf-science-pdfs/home-owners-guide/EH_HomeownersGuideToStAugustinegrassManagement_Factsheet_Final.pdf")


# ================================================================== 1. licensing
def p_license():
    body = "".join([
        sec("Does Florida license artificial turf installers?",
            f"<p>No specific state license covers laying artificial turf. The Florida Department of Business and Professional Regulation's Construction Industry Licensing Board, created under Chapter 489 of the Florida Statutes, certifies general, building and residential contractors along with specialty trades such as electrical, plumbing and irrigation, but turf installation itself isn't one of those licensed classes ({src('dbpr', "DBPR's license search")}; {ext(DBPR_CH489[1], "DBPR's Construction Industry statutes and rules page")}). A {svc('residential', 'residential turf job')} or a {svc('commercial', 'commercial installation')} can proceed without a state contractor's license for the turf and base work, the same way a mowing or mulching business does.</p>"
            f"<p>That surprises some homeowners, since Florida licenses dozens of trades tightly. {ext(FLCARE_LICENSE[1], 'One licensing guide for the green industry')} sums up the split plainly: routine landscape work, including grading a yard and installing turf, sits outside Chapter 489's contractor classes, while work that crosses into irrigation, electrical or structural territory pulls a different license into the job. It is illegal under Chapter 489 to perform or advertise a licensed trade, irrigation or electrical work among them, without holding the license that trade requires, or to claim a state license for turf installation that doesn't exist.</p>"),
        sec("What Chapter 489 actually licenses",
            table("Chapter 489 contractor classes and where turf work fits", ["License class", "What it covers", "Whether a turf job typically needs it"],
                  [["General contractor", "Structural work of any building type, unlimited scope statewide", "Only if the project adds new structural construction, such as a wall past a code height threshold"],
                   ["Building contractor", "Structures up to three stories, a narrower scope than general", "Rarely, unless paired with a larger hardscape or structural project"],
                   ["Irrigation / plumbing contractor", "Installing, altering or repairing irrigation and water piping", "Yes, for new irrigation lines or valves; not for capping an existing head"],
                   ["Electrical contractor", "Wiring tied into the home's electrical panel, including landscape lighting circuits", "Yes, for a hardwired lighting circuit; usually no for a plug-in transformer kit"],
                   ["Landscaping / turf installation", "Not a licensed class under Chapter 489", "No state license required for the turf and base work itself"]],
                  "Compiled from DBPR's Construction Industry Licensing Board classes; a specific city or county permit office may still ask questions about scope before issuing a permit.")),
        sec("When does a turf job actually need a licensed specialty contractor?",
            f"<p>A turf job crosses into licensed territory in three common situations: new irrigation work, permanent electrical work, and structural elements like a tall retaining wall. Capping an existing sprinkler head, which Florida's 2026 turf rule requires anyway since {src('dep-rule', 'in-ground irrigation can no longer water synthetic turf')}, is valve-box work most installers handle directly. Running a brand-new irrigation zone to the planting beds beside the turf is a different job and calls for a licensed irrigation or plumbing contractor.</p>"
            + table("Where a specialty license gets triggered on a turf project", ["Situation", "License likely needed", "Why"],
                    [["Capping irrigation heads under the turf footprint", "Usually none; standard valve-box work", "The state rule requires the cap, but disconnecting an existing head isn't new plumbing construction"],
                     ["Adding a new irrigation zone for beds beside the turf", "Irrigation or plumbing contractor", "New piping and valves fall under Chapter 489's irrigation and plumbing classes"],
                     ["Wiring low-voltage lighting into a turf or putting-green border", "Electrical contractor, if tied into the home's panel", "A plug-in transformer kit usually doesn't trigger this; a hardwired circuit does"],
                     ["Building a retaining wall to level a sloped yard for turf", "Building or general contractor, plus a permit", "Walls above a jurisdiction's height threshold typically need engineered plans"]],
                    f"Height thresholds and permit rules vary by jurisdiction; {a('/laws/permits/', 'check the permit page for your city or county')} before assuming a wall is exempt.")),
        sec("What a county business tax receipt actually is",
            "<p>Since Florida doesn't license the trade itself, the paperwork that does apply locally is a business tax receipt, what used to be called an occupational license, issued by the county or city where a business operates. It's a tax registration, not a skills test, but a business that can't produce one for the county it's working in is worth a second look.</p>"
            + table("Local business tax receipts where we work", ["County", "What it's called", "Where to check"],
                    [["Osceola County", "Local Business Tax Receipt", ext(OSCEOLA_BTR[1], "Osceola County Tax Collector")],
                     ["Orange County", "Business Tax Receipt (BTR)", ext(ORANGE_BTR[1], "Orange County BTR")],
                     ["Polk County", "County Local Business Tax Receipt, Class A or B", ext(POLK_BTR[1], "Polk County Tax Collector")]],
                    "A business working across county lines typically needs a receipt in each county it operates in, not only the one where it's based.")),
        sec("How to check a contractor before you sign anything",
            "<p>Four free lookups cover most of what matters: whether the business is actually registered, whether it holds any state license the job's scope requires, whether its certificate of insurance is current, and whether its workers' compensation status is legitimate. None of them cost anything, and together they take a few minutes.</p>"
            + ul([f"<strong>Sunbiz.</strong> {ext(SUNBIZ[1], "Florida's Division of Corporations business search")} confirms a company is registered and active, and shows who its officers are.",
                  f"<strong>DBPR license search.</strong> {src('dbpr', 'myfloridalicense.com')} confirms whether a business or individual holds any state-regulated license it claims, useful for the irrigation or electrical piece of a job rather than the turf itself.",
                  "<strong>Certificate of insurance.</strong> Ask the installer's insurance agent, not the installer, to send it directly. A copy that only the business hands over can be outdated.",
                  f"<strong>Workers' compensation exemption search.</strong> Florida's Division of Workers' Compensation runs a free {ext(WC_SEARCH[1], 'exemption search database')}; a company with employees and no valid coverage or exemption is a liability risk on your own property if someone gets hurt ({ext(WC_EXEMPT_CONST[1], 'DFS construction-industry exemption rules')})."])),
        sec("A worked example",
            f"<p>Say you're comparing two bids for a 900 sq ft backyard in Buenaventura Lakes that also includes a two-foot paver step and a low-voltage light strip along the turf border. Neither bid needs a general contractor's license for the turf and base work itself. If the light strip plugs into a transformer instead of tying into the house's panel, no electrical license applies either. If either quote proposes a brand-new irrigation zone for the beds around the turf, that specific piece should be performed or supervised by a licensed irrigation or plumbing contractor, even though the turf portion right next to it isn't a licensed trade at all. {post('how-to-compare-artificial-turf-quotes', 'Comparing two quotes line by line')} covers the rest of what a complete bid should state.</p>"),
        sec("What this means once you're comparing bids",
            f"<p>A missing license isn't automatically a red flag on a turf-only job, since none applies. What's worth asking about directly is scope: does this bid include anything, irrigation, electrical or structural, that does require one, and can the company show it. {post('best-artificial-turf-contractor-kissimmee', 'Choosing a contractor in Kissimmee')} and {post('diy-vs-professional-artificial-turf-installation', 'the DIY-versus-professional breakdown')} both go further into what separates a careful installer from a rushed one, licensing aside.</p>"),
    ])
    faqs = [
        faq("Can an unlicensed handyman legally lay turf in Florida?", "Yes, for the turf and base work itself, since it isn't a licensed trade. The handyman exemption under Chapter 489 has its own dollar limits for other repair work, but turf installation doesn't need that exemption because no license applies to it in the first place."),
        faq("Does pulling a building permit require a state contractor's license?", "It depends on the jurisdiction and the scope. Many Central Florida permit offices let a homeowner pull an owner-builder permit for work on their own property, and a permit for grading or drainage doesn't by itself require a Chapter 489 license if the turf work itself isn't a licensed class."),
        faq("Is registering a business with Sunbiz the same as being licensed?", "No. Sunbiz registration establishes that a company legally exists as a corporation or LLC; it says nothing about whether that company holds any state trade license. Check the two separately."),
        faq("Does a workers' compensation exemption mean a company has no employees?", "Not necessarily. An exemption lets certain corporate officers or members opt out of coverage for themselves, but the same company can still have employees who are required to be covered. The exemption search shows whose exemption is on file, not the company's full payroll."),
        faq("Do irrigation or electrical subcontractors need to be named on a turf quote?", "It's reasonable to ask. If a quote includes new irrigation or wired lighting, ask who's performing that specific piece and whether that person or company holds the license it requires, separate from the turf and base work around it."),
    ]
    return page("/blog/do-turf-installers-need-a-license-in-florida/", "post",
                "Do Turf Installers Need a License in Florida?",
                "Florida has no state license for turf or landscaping installers as of September 2026. What Chapter 489 covers, county tax receipts, and how to vet a contractor.",
                "Does a turf installer need a license in Florida, and how do you check one?",
                capsule("Florida's DBPR issues no statewide license for landscaping or turf installation as of September 2026. Chapter 489 covers general, building and specialty contractors such as irrigation, electrical and structural trades, not laying turf itself. What actually protects a Kissimmee homeowner is a county business tax receipt, a certificate of insurance, and a workers' compensation exemption status anyone can check online before signing."),
                body, faqs=faqs, crumbs=CRUMBS, crumb="Licensing and checking a contractor", published=PUB,
                sources=["dbpr", "dep-rule", DBPR_CH489, FLCARE_LICENSE, SUNBIZ, OSCEOLA_BTR, ORANGE_BTR, POLK_BTR, WC_SEARCH, WC_EXEMPT_CONST],
                related=[("/laws/permits/", "Permits by city and county"), ("/blog/how-to-compare-artificial-turf-quotes/", "How to compare two turf quotes"),
                         ("/blog/best-artificial-turf-contractor-kissimmee/", "Choosing a contractor in Kissimmee"), ("/artificial-grass-installation/", "Residential turf installation")])


# ================================================================== 2. PFAS, lead, safety
def p_safety():
    body = "".join([
        sec("Is artificial turf safe for kids?",
            f"<p>As of September 2026, Florida's synthetic turf standard bars heavy metals and any intentionally added PFAS from turf, backing and infill on single-family lots, and limits rubber infill to the footprint of playground equipment ({src('dep-rule', 'Rule 62-308.100, F.A.C.')}). That answers the material question a 2026 build has to meet. It doesn't settle every safety question a parent asks, and the honest picture includes some history and some real disagreement. {svc('playground', 'Playground turf')} is where most of these questions come up, since that's the surface a child spends the most time on.</p>"),
        sec("Where did the lead-in-turf concern come from?",
            f"<p>From older nylon turf fibers, mostly fields built before 2010, whose lead-based pigments could degrade into dust as UV light and heat broke the fiber down over years of sun exposure. {ext(CPSC_LEAD[1], "The U.S. Consumer Product Safety Commission's 2008 staff analysis")} sampled a small set of fields and concluded that young children weren't at risk from the lead levels found, a finding that outside researchers criticized as based on too few fields tested too early in the debate. Today's polyethylene lawn turf, the material used on nearly every residential Florida install, isn't the nylon product that raised the original concern, and Florida's 2026 rule now bars added heavy metals outright regardless of fiber type.</p>"),
        sec("What about crumb rubber infill?",
            f"<p>Crumb rubber, ground-up recycled tires used as infill on some sports fields, drew years of parent concern before a joint federal study answered it directly. The EPA and CDC's Agency for Toxic Substances and Disease Registry ran the multi-agency Federal Research Action Plan, and its final reports found that players weren't at an elevated exposure risk from the chemicals, metals or air emissions crumb rubber can release on a field ({ext(EPA_FRAP[1], 'Federal Research Action Plan on recycled tire crumb rubber')}). The question has also gotten narrower in Florida: the state's 2026 rule already keeps rubber and other synthetic infill off a home lawn, dog run or putting green, reserving it for the ground directly under swings and slides.</p>"),
        sec("What changed with PFAS in 2026?",
            f"<p>Two states moved on PFAS the same year. Florida's rule requires turf, backing and infill sold for a covered lot to contain no intentionally added PFAS, and {src('watersavers-pfas', "California's own PFAS ban took effect January 1, 2026")}, pushing national manufacturers toward PFAS-free product lines across the board rather than a Florida-only formulation. Ask a supplier for the written no-added-PFAS statement the state standard now requires; a manufacturer selling into Florida in 2026 should have one ready.</p>"),
        sec("The critical view and the industry view",
            f"<p>Mount Sinai's environmental health researchers remain skeptical of synthetic turf for children's play generally, pointing to the mix of chemicals in plastic and rubber products as a category, not just PFAS or lead specifically, and to how little long-term exposure data exists for young children on turf across a full childhood ({src('mtsinai-turf', "Mount Sinai's synthetic turf research summary")}). Turf manufacturers and the Synthetic Turf Council point to the federal crumb-rubber findings and the new state material bans as evidence the product has gotten measurably cleaner. Both things can be true at once: the specific hazards regulators have tested for keep coming back lower than feared, and a category-wide, decades-long safety record still doesn't exist the way it does for a material like sand or grass.</p>"),
        sec("How does this compare to a natural lawn's own chemical exposure?",
            "<p>A natural lawn isn't automatically the safer surface by default, since a St. Augustine lawn under real pest pressure often gets a pesticide application for chinch bugs and a seasonal fertilizer round, both of which a child or a pet can contact directly on the grass blades within hours of treatment. Turf never receives either, since there's nothing living to fertilize or protect. That doesn't cancel out the PFAS and infill questions this page covers; it just means the honest comparison is turf's material questions against a treated lawn's chemical exposure, not turf against some chemical-free ideal that most Central Florida lawns don't actually maintain.</p>"),
        sec("What to ask for before a playground or lawn install",
            table("A short checklist for a family evaluating turf", ["Ask for", "Why it matters"],
                  [["Written no-added-PFAS and no-heavy-metals statement", "Now required under Florida's 2026 rule for turf, backing and infill on a covered lot"],
                   ["Infill named by type", "Confirms it's silica sand, rock, shell or non-toxic coated sand, not rubber, outside a playground footprint"],
                   ["Product age and fiber type, if reusing existing turf", "Older nylon turf predates current lead restrictions and current testing standards"],
                   ["A rinse and shade plan for full-sun areas", "Surface heat, not chemistry, is the safety issue that shows up on nearly every hot afternoon"]])),
        sec("A worked example",
            f"<p>Say you're installing playground turf under a swing set and slide in a Celebration backyard, with a plain lawn area beside it for everything else. Under the state's silhouette for infill, the swing set's fall-zone footprint can use a shock pad or, where allowed, a rubber infill component sized to the equipment's fall height, while the surrounding lawn area next to it has to stay on silica, zeolite or non-toxic coated sand. Two infill types, one yard, both compliant, because the rule draws the line at the equipment footprint rather than at the property line.</p>"),
        sec("Heat is the risk that shows up the most",
            f"<p>Whatever a family decides about PFAS and infill history, the safety issue that actually comes up on a Tuesday afternoon is surface temperature: full Florida sun commonly pushes turf to 120 to 150 degrees and sometimes past 160. {post('how-hot-does-artificial-turf-get-in-florida', 'How hot turf gets, hour by hour')} and {a('/faq/pets-heat/', 'the pets and heat FAQ')} both cover the rinse-and-shade routine that manages it in practice.</p>"),
    ])
    faqs = [
        faq("Does Florida's turf rule apply to a school playground the same way it applies to a home?", "No. Rule 62-308.100 covers single-family residential lots of one acre or less. A school or public playground answers to a different set of state and local safety standards for surfacing, not this residential rule."),
        faq("Can a child get sick from chewing on artificial grass blades?", "A single mouthful of modern polyethylene fiber isn't considered acutely toxic, but it isn't food either, and a young child who regularly puts turf in their mouth is worth watching the same way you'd watch any non-food item a toddler explores."),
        faq("Does a hot lawn release more chemical odor than a cool one?", "A faint plastic smell can be more noticeable when the backing warms in full sun, similar to a new shower curtain or car interior off-gassing, and it fades with age and rinsing. It isn't the same finding as the PFAS or lead questions this page covers, which are about material content, not smell."),
        faq("Is older turf installed before 2026 automatically unsafe?", "Not automatically. The 2026 material rule sets a standard for new installations; nothing in the published rule summaries describes a retrofit requirement for turf already down. A family with real concerns about an older nylon lawn can ask a supplier for current testing on that specific product's age and type."),
        faq("Do artificial turf manufacturers publish independent lab test results?", "Some do, typically a certificate of analysis or a lead and heavy-metals test from a third-party lab tied to a specific product batch. Ask for the actual document rather than a general marketing claim of being PFAS-free or lead-free."),
    ]
    return page("/blog/is-artificial-turf-safe-for-kids-pfas-lead/", "post",
                "Is Artificial Turf Safe for Kids? PFAS and Lead",
                "Florida's 2026 turf rule bars PFAS and heavy metals in turf and infill. What CPSC's 2008 lead finding and the EPA/CDC crumb-rubber study actually found.",
                "Is artificial turf safe for kids? PFAS, lead and infill, explained",
                capsule("As of September 2026, Florida's synthetic turf rule bars heavy metals and intentionally added PFAS from turf, backing and infill on single-family lots, and limits rubber infill to the footprint of playground equipment. Old nylon turf's lead history and crumb rubber's chemical exposure have both been studied by federal agencies since, with lower risk found than early fears suggested. The everyday risk that remains is surface heat, not chemistry."),
                body, faqs=faqs, crumbs=CRUMBS, crumb="PFAS, lead and turf safety", published=PUB,
                sources=["dep-rule", "watersavers-pfas", "mtsinai-turf", CPSC_LEAD, EPA_FRAP],
                related=[("/playground-turf/", "Playground turf with a sized shock pad"), ("/laws/florida-hb-683/", "What Florida's 2026 turf rule requires"),
                         ("/blog/is-artificial-turf-bad-for-the-environment/", "Is artificial turf bad for the environment?"), ("/faq/pets-heat/", "Pets and heat questions, answered")])


# ================================================================== 3. environment
def p_environment():
    body = "".join([
        sec("Is artificial turf bad for the environment?",
            f"<p>It's a genuine trade-off, not a clean yes or no. Turf removes a Central Florida lawn's roughly 20,000 to 30,000 gallons a year of irrigation demand and, since it's never fertilized or sprayed, ends the fertilizer and pesticide runoff a natural lawn can send toward a storm drain. Against that: turf runs hotter than grass in full sun, and once it wears out, {a('/turf-replacement/', 'a worn lawn')} almost always goes to a landfill rather than a recycling stream, as of September 2026. Neither side of that ledger cancels the other out.</p>"),
        sec("Does turf actually save meaningful water?",
            f"<p>Yes, for the area it covers. A natural Central Florida lawn that size uses an estimated 20,000 to 30,000 gallons of irrigation water a year, water a turfed area no longer draws once heads under it are capped, since Florida's 2026 rule doesn't allow in-ground irrigation on synthetic turf at all ({src('dep-rule', 'Rule 62-308.100, F.A.C.')}). {post('artificial-turf-vs-sod-cost-florida', 'The ten-year cost comparison between turf and sod')} covers the dollar side of that same water savings.</p>"),
        sec("What about the heat island effect?",
            f"<p>This is turf's clearest environmental downside. Full Florida sun commonly pushes synthetic turf to 120 to 150 degrees at the surface, well above the natural grass nearby, which stays close to air temperature ({src('magnolia-heat', 'measured Florida readings')}; {src('horsemans-heat', 'Florida installer heat data')}). A single backyard's heat gain doesn't move a neighborhood's temperature, but a large expanse of unshaded turf, a sports field or a big commercial lot, contributes to the same local heat-island effect that a parking lot or a dark roof does. Shade and lighter color blends reduce it; they don't erase it.</p>"),
        sec("Does turf cut chemical runoff into Florida's waterways?",
            f"<p>Meaningfully, yes, for the area converted. Both {ext(OSCEOLA_FERT[1], "Osceola County's fertilizer management rules")} and {ext(ORANGE_FERT[1], "Orange County's fertilizer ordinance")} bar nitrogen and phosphorus fertilizer on lawns from June 1 through September 30, the same rainy season that carries the most runoff into local lakes and canals, precisely because a fertilized lawn's nutrients wash off fastest during a summer storm. A lawn that's never fertilized at all sidesteps that seasonal restriction entirely, and Florida's turf rule adds its own water-quality layer: turf can't sit within a swale, ditch or stormwater pond, and generally has to stay at least 10 feet from a lake, pond or canal, which limits how close a converted area can push toward the water it's trying not to affect.</p>"),
        sec("What happens to turf at the end of its life?",
            f"<p>Mostly, it goes into a landfill. Florida's 2026 rule actually requires this indirectly: turf, backing and infill sold for a covered lot must be disposable at a Florida-permitted landfill, which is a safety and material standard, not a recycling mandate. Some manufacturers run take-back or recycling programs for their own product lines, but no broad, guaranteed recycling infrastructure exists in Central Florida as of September 2026, so a homeowner shouldn't count on one being available when a 10-to-20-year lawn eventually wears out. {post('how-long-does-artificial-turf-last-in-florida', "How long a Florida lawn actually lasts")} covers what shortens or extends that timeline.</p>"),
        sec("What does UF/IFAS say?",
            f"<p>UF/IFAS doesn't classify synthetic turf as Florida-Friendly Landscaping under state law, the program built around plants, soil and water conservation ({src('ifas-turf', "UF/IFAS's synthetic turfgrass fact sheet")}). That's a classification statement, not a condemnation. It means turf's water and chemical-runoff benefits are real but sit outside a separate state framework built for living plant material, which is worth knowing if an HOA's design guidelines specifically require Florida-Friendly plantings rather than just a maintained yard.</p>"),
        sec("Does converting a lawn to turf ease pressure on the local aquifer?",
            f"<p>At the scale of one household, barely; at the scale of a subdivision, it adds up. Osceola County has floated a water conservation ordinance aimed at protecting the groundwater supply as growth and irrigation demand both climb ({src('osceola-water-2026', 'a 2026 report on the proposed county ordinance')}). A single converted lawn's 20,000 to 30,000 gallons a year is a rounding error against the aquifer as a whole, but it's also the same category of demand utilities and counties are trying to reduce through watering-day restrictions, which is why turf gets mentioned in that conversation even though no rebate currently rewards it here.</p>"),
        sec("Turf versus natural grass, side by side",
            table("Environmental trade-offs, artificial turf vs. natural grass", ["Factor", "Artificial turf", "Natural grass"],
                  [["Irrigation water", "None once installed; in-ground irrigation can't legally water it", "20,000-30,000 gal/year on a typical 1,000 sq ft Central Florida lawn"],
                   ["Fertilizer and pesticide runoff", "None; nothing is applied to synthetic turf", "Ongoing, seasonally restricted in Osceola and Orange counties"],
                   ["Surface heat in full sun", "120-150°F common, sometimes over 160°F", "Stays close to air temperature"],
                   ["End of life", "Almost always landfilled; must be landfill-disposable under the 2026 rule", "Biodegrades; no landfill disposal issue"],
                   ["Ongoing carbon footprint", "None from mowing; a one-time manufacturing and shipping footprint", "Gas or electric mower emissions over decades of upkeep"]],
                  "A qualitative comparison, not a life-cycle assessment; neither column is a net environmental score.")),
        sec("A worked example",
            "<p>Say you have a 1,000 sq ft front lawn that currently gets watered on Toho's two allowed days a week and fertilized twice during the growing season. Converting it to turf removes an estimated 20,000 to 30,000 gallons of annual irrigation and both fertilizer applications, including the summer one that currently falls inside the June-through-September blackout window most counties here enforce. In exchange, that same 1,000 sq ft runs meaningfully hotter on a still, sunny July afternoon than the grass it replaced, and in fifteen or twenty years it becomes a landfill load the grass never would have.</p>"),
        sec("The honest bottom line",
            f"<p>Turf trades one set of environmental costs for a different set, not a smaller total. A household that already struggles to keep a lawn watered and fed within Florida's rules, or that's converting a section that barely grows anyway, gets a real reduction in water use and runoff. A household mainly chasing a lower-maintenance yard should weigh the heat and eventual landfill fact honestly rather than treat turf as a free environmental upgrade. {svc('residential', 'A site visit')} that looks at how much of a specific lot is realistically watered and fertilized today is a better starting point than a blanket answer either way.</p>"),
    ])
    faqs = [
        faq("Does artificial turf reduce a household's carbon footprint?", "It removes the fuel or electricity a mower uses over the turf's lifespan, but manufacturing and shipping the turf itself carries its own one-time footprint. No published study we've found puts a net carbon number on that trade for a Florida installation specifically."),
        faq("Can old artificial turf be repurposed instead of thrown away?", "Occasionally, for non-turf uses like weed-suppressing groundcover under mulch or temporary erosion control, but this is a homeowner workaround, not an established recycling channel, and it doesn't apply to the backing or infill."),
        faq("Do stormwater ponds near Kissimmee treat turf runoff differently than lawn runoff?", "A properly built turf system isn't supposed to increase runoff volume or rate at all under the state's 2026 rule, so it shouldn't be sending anything new to a retention pond. A pond's design doesn't distinguish between the two surfaces beyond that requirement."),
        faq("Does removing a lawn for turf affect local wildlife?", "It removes a food source for lawn-dwelling insects and the birds or lizards that eat them, though a mowed, chemically treated lawn wasn't providing much habitat value to begin with. Keeping some plant beds alongside a turfed area preserves more of that value than turf alone would."),
    ]
    return page("/blog/is-artificial-turf-bad-for-the-environment/", "post",
                "Is Artificial Turf Bad for the Environment?",
                "Turf cuts irrigation and fertilizer runoff but adds heat and, as of September 2026, ends up in a Florida landfill. Here's the honest trade-off, sourced.",
                "Is artificial turf bad for the environment, and can it be recycled?",
                capsule("As of September 2026, artificial turf cuts a Central Florida lawn's estimated 20,000 to 30,000 gallons of yearly irrigation and ends fertilizer and pesticide runoff entirely. It also runs 120 to 150 degrees hotter than grass in full sun and, when it wears out after 10 to 20 years, almost always goes to a landfill rather than a recycling stream. Both facts are true at once."),
                body, faqs=faqs, crumbs=CRUMBS, crumb="Turf and the environment", published=PUB,
                sources=["dep-rule", "ifas-turf", "magnolia-heat", "horsemans-heat", "toho-days", "osceola-water-2026", OSCEOLA_FERT, ORANGE_FERT],
                related=[("/turf-replacement/", "Turf removal and replacement"), ("/blog/artificial-turf-vs-sod-cost-florida/", "Turf vs. sod, 10-year cost"),
                         ("/blog/how-long-does-artificial-turf-last-in-florida/", "How long turf lasts in Florida"), ("/laws/florida-hb-683/", "Florida's 2026 turf rule, in full")])


# ================================================================== 4. live oaks and palms
def p_oaks():
    body = "".join([
        sec("Will artificial turf hurt live oaks or palm roots?",
            f"<p>Not if it stays where Florida's 2026 rule says it has to. {src('dep-rule', 'Rule 62-308.100')} keeps synthetic turf outside a tree's drip line, the ring on the ground under a canopy's outermost branches, on your own lot and on a neighbor's, unless a certified arborist certifies the specific installation won't harm the tree. A mature live oak's drip line can run 20 to 40 feet across in an older Kissimmee neighborhood, which changes the usable footprint of {svc('residential', 'a backyard turf project')} more than almost any other single site condition.</p>"),
        sec("Why does the rule protect the neighbor's tree too?",
            "<p>Because roots don't stop at a property line. A live oak's critical root zone extends outward with the canopy regardless of whose yard the trunk sits in, so turf, base excavation and compaction equipment on your side of the fence can still compress or sever roots feeding a tree rooted next door. The state standard closes that gap by naming both your property and adjacent parcels, not just the lot the turf is going on.</p>"),
        sec("What is a drip line, and how far out does a live oak's root zone actually reach?",
            f"<p>The drip line is the ground directly beneath a tree's outermost branch tips, and it's the standard rule of thumb for estimating a tree's critical root zone. Arborist guidance goes a step further for larger, older specimens: a tree protection zone for a tall, mature tree should extend to roughly one and a half times the drip line's radius, since a live oak's structural and feeder roots commonly reach past where the canopy visibly ends ({ext(ISA_ROOT[1], 'ISA Rocky Mountain Chapter tree protection guidance')}; {ext(IFAS_TREEPROTECT[1], 'UF/IFAS construction-phase tree protection publication')}). Grading, trenching or heavy equipment inside that zone is what actually damages roots, more than the finished turf sitting on top of them afterward.</p>"),
        sec("Are palms treated the same way as live oaks?",
            "<p>The rule doesn't distinguish by species, so a mature Sabal or Canary Island date palm's drip line is off-limits the same as an oak's, unless an arborist signs off. In practice palms tend to cause fewer conflicts, since a palm's root system is fibrous, shallow and doesn't spread with the trunk's height the way an oak's structural roots do, so a palm's drip line and its practical root zone sit closer together. The species that actually gets an exception under the rule is a noxious weed tree, invasive species such as Brazilian pepper or melaleuca that Florida doesn't discourage removing, which the standard exempts from the drip-line protection entirely.</p>"),
        sec("What hiring a certified arborist actually involves",
            f"<p>A certified arborist for this purpose means someone credentialed through the International Society of Arboriculture, not a general lawn or tree-trimming crew. A site visit typically involves the arborist inspecting the specific tree's root flare, checking for signs of existing stress, and reviewing where excavation would occur relative to the trunk before writing a letter certifying the project won't cause harm. That letter is worth keeping with the permit file and any HOA application, since a code office or a future buyer's inspector may ask for it years later if a question comes up about work done near a protected tree.</p>"),
        sec("What to put under the canopy instead of turf",
            table("Ground cover options inside a protected drip line", ["Option", "Why it works under a canopy", "What to watch"],
                  [["Mulch, 2-3 in deep", "Retains moisture, adds no weight or compaction, easy to refresh after leaf drop", "Keep it a few inches back from the trunk itself"],
                   ["Shade-tolerant groundcover", "Low root disturbance to plant; some soil enrichment as it decomposes", "Choose species suited to deep, dry shade under a dense canopy"],
                   ["Decomposed leaf litter, raked to an even layer", "Zero cost, mimics what the tree already drops", "Looks less finished than a landscaped bed"],
                   ["Turf, with an arborist letter in hand", "Extends the yard's usable, low-maintenance area up to the trunk", "Requires certified arborist sign-off and usually hand digging, not machine excavation, near the trunk"]])),
        sec("Leaf drop and keeping turf clean near a canopy",
            f"<p>Even turf placed outside the drip line still catches what falls from above it. Live oaks drop leaves nearly year-round rather than all at once, and {post('oak-leaves-and-debris-on-artificial-turf', 'a steady debris routine')} keeps that litter from staining the pile or working into the infill during a rainy-season downpour. {a('/faq/maintenance/', 'The care and lifespan FAQ')} has the seasonal rinse-and-rake calendar that routine runs on.</p>"),
        sec("A worked example",
            "<p>Say you have a 60-foot live oak on the property line between your lot and your neighbor's, with a canopy that reaches about 35 feet into your backyard. On an 800 sq ft turf project, the drip line alone could take up 300 to 400 sq ft of that space off the table without an arborist's letter, leaving roughly 400 to 500 sq ft available for turf outright, with mulch or groundcover filling the protected zone. Getting a certified arborist to inspect the tree and certify a specific, limited turf area, hand-dug rather than machine-graded near the trunk, is often the difference between losing that space entirely and reclaiming most of it.</p>"),
        sec("Getting the arborist step right before, not after, installation",
            f"<p>Once the sitework has already disturbed roots inside a drip line, an arborist's letter can no longer prevent damage that's already done. Bringing in a certified arborist during planning, before any excavation, is what the exception actually depends on. {a('/laws/florida-hb-683/', "The full DEP rule breakdown")} covers this alongside the other site conditions, ponds, swales and septic tanks among them, that shape where turf can go on a given lot.</p>"),
    ])
    faqs = [
        faq("Does trimming a tree's canopy back change where the drip line falls?", "Yes, since the drip line follows the branches, not a fixed measurement from the trunk. A canopy that's been reduced through pruning has a smaller drip line than an unpruned tree of the same age, though roots that grew under the wider canopy may still extend past the newly trimmed edge."),
        faq("Can a dead or dying oak's drip line be turfed without an arborist letter?", "The rule's language centers on protecting a living tree from harm, so a tree already dead or being removed likely falls outside that concern, though a local arborist or code office can confirm the specific tree's status before work starts."),
        faq("Do smaller ornamental trees carry the same drip-line protection as a live oak?", "The rule's drip-line language applies to trees generally, not just live oaks specifically, so a mature crape myrtle or magnolia's canopy edge gets the same protection. A small, young tree's modest drip line simply takes up much less of the yard."),
        faq("Does root pruning let turf go closer to a protected tree?", "Sometimes, when done correctly by an arborist using clean cuts outside the tree protection zone rather than machine excavation, but it's a decision for the certified arborist evaluating that specific tree, not something to attempt as a workaround on your own."),
        faq("Does a fence or property survey settle where a shared drip line actually falls?", "A survey shows the property line, not the canopy's edge, so the two often need to be checked separately. Standing under the canopy and marking where the branch tips actually end is a more direct way to find the drip line than working from a survey alone."),
    ]
    return page("/blog/artificial-turf-near-live-oaks-and-palms/", "post",
                "Artificial Turf Near Live Oaks and Palms",
                "Florida's 2026 turf rule keeps synthetic turf outside a tree's drip line on your lot and your neighbor's, unless a certified arborist signs off.",
                "Will artificial turf hurt live oaks or palm roots?",
                capsule("As of September 2026, Florida's synthetic turf rule keeps turf outside a tree's drip line, on your property or an adjacent one, unless a certified arborist certifies the installation won't cause harm. A mature Kissimmee live oak's drip line can span 20 to 40 feet, and arborist guidance extends the true root protection zone even further. Noxious-weed trees are the one exception the rule carves out."),
                body, faqs=faqs, crumbs=CRUMBS, crumb="Turf near live oaks and palms", published=PUB,
                sources=["dep-rule", "hb683", ISA_ROOT, IFAS_TREEPROTECT],
                related=[("/laws/florida-hb-683/", "HB 683 and the DEP rule, requirement by requirement"), ("/blog/base-under-artificial-turf-florida-sandy-soil/", "Base for Central Florida's sandy soil"),
                         ("/blog/oak-leaves-and-debris-on-artificial-turf/", "Oak leaves and debris on turf"), ("/artificial-grass-installation/", "Residential turf installation")])


# ================================================================== 5. pile height and face weight
def p_spec():
    body = "".join([
        sec("What pile height and face weight should you choose?",
            f"<p>It depends entirely on what the surface has to do. A standard {svc('residential', 'residential lawn')} in Central Florida typically runs 1.5 to 2 inches of pile at 50 to 70 ounces per square yard, a dog run drops the pile shorter for easier cleanup, a putting surface shrinks to 0.4 to 0.5 inches for a true roll, and a commercial walkway favors a short, dense pile that resists matting under constant foot traffic. Picking one spec for an entire property is how a yard ends up with turf that looks wrong for at least one of its uses.</p>"),
        sec("Pile height, face weight, backing and infill, by use",
            table("Typical spec ranges by use, Central Florida residential and light commercial", ["Use", "Pile height", "Face weight (oz/sq yd)", "Backing", "Typical infill"],
                  [["Standard lawn", "1.5-2 in", "50-70", "Fully permeable, perforated", "Silica sand"],
                   ["Pet turf / dog run", "0.75-1.25 in", "60-80", "Fully permeable, no weed barrier beneath", "Zeolite or antimicrobial coated sand"],
                   ["Play area", "1-1.5 in, plus a shock pad sized to fall height", "60-90", "Permeable, over a rated foam or rubber pad", "Silica sand on the turf; rubber only inside equipment footprint"],
                   ["Putting surface", "0.4-0.5 in", "30-40, dense", "Permeable, precision-tufted", "Fine silica sand, lightly applied"],
                   ["Pool deck / lanai", "1-1.5 in", "50-70", "Permeable, glued to hard surfaces where needed", "Silica sand, moderate rate"],
                   ["Commercial walkway / common area", "0.75-1.25 in", "70-90+, heavy duty", "Reinforced permeable backing for repeated traffic", "Silica sand, heavier application"]],
                  f"Ranges compiled from published turf buying guides ({ext(GLOBALSYNTURF_PILE[1], 'Global Syn-Turf')}; {ext(MSI_SURFACES[1], 'MSI Surfaces')}) and Florida's 2026 infill standard; a specific manufacturer's spec sheet controls for any named product.")),
        sec("What do gauge, denier and tuft bind add on top of those two numbers?",
            f"<p>Pile height and face weight get most of the attention on a quote, but three other spec-sheet terms decide how a lawn wears over years, not just how it looks on day one. Gauge, the spacing between tufted rows, runs 3/8 to 5/8 inch and sets how dense the turf feels underfoot. Denier measures each yarn fiber's thickness, and a higher-denier fiber resists matting and holds its blade shape longer under Florida's combination of UV and foot traffic. Tuft bind, tested to ASTM D1335, is the pull force needed to yank a single blade out of the backing; the industry commonly targets above roughly 6.8 pounds, and a low number here shows up years later as thinning, bald patches rather than a defect visible at installation ({ext(STC_SPEC[1], 'Synthetic Turf Council performance guidelines')}).</p>"),
        sec("Why heavier isn't automatically better",
            "<p>A heavier face weight costs more and generally wears longer, but stacking maximum numbers on every spec doesn't produce the best lawn for every use. An extra-tall, extra-dense pile on a putting surface would ruin the roll a green needs. A heavy, plush lawn-grade product laid in a dog run traps moisture and odor longer than a shorter, faster-draining pet-specific build. Matching the spec to the use matters more than chasing the highest number on the sheet.</p>"),
        sec("What backing type has to do with any of this",
            "<p>Pile height and face weight sit on top of a backing that's doing its own separate job: holding the tufted rows in place while letting water pass straight through. A fully perforated backing with evenly spaced drainage holes across the whole sheet, not just at the seams, is what lets a heavier face weight drain as fast as a lighter one. A backing that's only lightly perforated can bottleneck water even under an otherwise well-specified lawn, which is one reason two products with identical pile height and face weight numbers can still perform differently after a heavy Central Florida storm.</p>"),
        sec("How Florida's 2026 rule shapes the infill half of this decision",
            f"<p>Whatever pile height and face weight a homeowner lands on, the infill choice now has a hard boundary. {src('dep-rule', "Rule 62-308.100")} limits infill on the rest of a single-family lot, lawn, dog run or putting green, to clean silica sand, rock, shell or other natural material, plus non-toxic coated sand; rubber and other synthetic infill stay legal only inside a playground's equipment footprint. That rule doesn't touch pile height or face weight directly, but it does mean a spec sheet promising a heavier, cushier lawn feel through rubber-blend infill isn't an option on a Florida lawn anymore.</p>"),
        sec("A worked example",
            "<p>Say you have a 700 sq ft yard in Winter Garden split roughly in half between a dog run along the fence line and a play strip for the kids near the patio. The dog run calls for a shorter pile, around 1 inch, with a permeable backing and no weed barrier underneath, plus zeolite infill for odor control. The play strip wants a taller, softer pile closer to 1.5 inches with a shock pad sized to the swing set's fall height and plain silica infill, since rubber infill is only legal directly under the equipment itself. Two zones, two specs, one property, and neither spec is wrong for the other's job, just mismatched to it.</p>"),
        sec("Reading a spec sheet like the numbers matter, because they do",
            f"<p>A quote that lists a product name with its pile height and face weight is describing an actual, checkable thing; one that says only \"premium turf\" is not. {post('artificial-turf-glossary', 'The full turf glossary')} defines the rest of the vocabulary a spec sheet uses, and {post('why-is-artificial-grass-so-expensive', 'the cost breakdown article')} covers how these same numbers show up as line items on an invoice.</p>"),
    ])
    faqs = [
        faq("Does a taller pile always look more like real grass?", "Not past a certain point. A pile over roughly 2 inches on a home lawn can lean over under its own weight and mat down faster than a moderate 1.5 to 1.75 inch pile with a multi-tone blade blend, which often reads as more natural once it's down."),
        faq("Can one turf product work for both a lawn and a putting green on the same property?", "Not well. A green's short, dense pile is built for ball roll, not for the softer, taller feel a lawn area wants underfoot, so most properties with both use two different products rather than one compromise spec."),
        faq("Does face weight include the backing's weight too?", "No. Face weight measures only the yarn fiber per square yard, not the backing material beneath it. Total weight, a separate spec some sheets list, adds the backing back in."),
        faq("Is a higher gauge number denser or less dense turf?", "Less dense. Gauge measures the spacing between tufted rows, so a tighter gauge, a smaller number like 3/8 inch, packs rows closer together and produces denser turf than a wider 5/8 inch gauge."),
        faq("Does the same face weight look identical across two different colors?", "Not necessarily to the eye. Dye lot and blade shape can make two rolls at the same stated face weight look slightly different in density, which is one reason installers try to source an entire job's turf from a single production run rather than mixing rolls."),
        faq("Should a putting green's fringe use the same face weight as the surrounding lawn?", "Not usually. Fringe turf typically sits between the green's dense, short spec and the lawn's taller, lighter one, giving the transition a visual and textural step rather than a hard jump from one extreme to the other."),
    ]
    return page("/blog/artificial-turf-pile-height-and-face-weight/", "post",
                "Artificial Turf Pile Height and Face Weight",
                "Pile height and face weight change by use: lawn, pets, play, putting, pool and commercial turf each spec differently. A by-use table, September 2026.",
                "What pile height and face weight should you choose?",
                capsule("Pile height and face weight change by use as of September 2026: a Central Florida lawn typically runs 1.5 to 2 inches at 50 to 70 oz/sq yd, a home putting surface drops to 0.4 to 0.5 inches for a true roll, and a dog run shortens the pile for easier cleanup. Gauge, denier and tuft bind decide how well any of those specs hold up over years of Florida sun and traffic."),
                body, faqs=faqs, crumbs=CRUMBS, crumb="Pile height and face weight", published=PUB,
                sources=["dep-rule", GLOBALSYNTURF_PILE, MSI_SURFACES, STC_SPEC],
                related=[("/blog/artificial-turf-glossary/", "Turf terms explained"), ("/pet-turf/", "Pet turf and dog runs"),
                         ("/putting-greens/", "Backyard putting green installation"), ("/playground-turf/", "Playground turf")])


# ================================================================== 6. best grass for Florida
def p_bestgrass():
    body = "".join([
        sec("What artificial grass holds up in Florida?",
            f"<p>No single brand is objectively the best choice for every Florida yard; what holds up here is a specific combination of specs, not a logo. A UV-stabilized polyethylene blade over a fully permeable backing, matched to a face weight in the 50 to 70 oz/sq yd range for {svc('residential', 'a residential lawn')}, with a written manufacturer statement of no added PFAS or heavy metals, covers what Florida's climate and its 2026 material rule both actually demand. {a('/compare/nylon-vs-polyethylene-vs-polypropylene-turf/', 'The full fiber comparison')} goes deeper on the material choice itself; this page covers the criteria around it.</p>"),
        sec("UV stabilization: the difference between fading in 5 years and 15",
            f"<p>Every square foot of Florida turf sits in more annual sun exposure than turf in most of the country, so UV-stabilized fiber isn't optional the way it might be in a shadier climate. UV stabilizers built into the yarn slow the color loss and brittleness that unprotected fiber develops under constant sun, and the gap between a stabilized and an unstabilized product shows up as roughly 10 to 20 years of useful life versus a fraction of that ({src('stn-life', 'manufacturer lifespan data')}). Ask specifically whether the fiber is UV-stabilized, not just whether the turf carries a warranty, since warranty terms and UV treatment are two different things.</p>"),
        sec("Polyethylene, nylon or polypropylene, briefly",
            f"<p>Polyethylene dominates Central Florida residential lawns because of its soft hand feel and price, and it's the material behind most of the pile-height and face-weight ranges elsewhere on this site. Nylon holds its shape better under extreme heat and heavier loads, useful on a putting green's fringe or a high-traffic commercial strip, but it costs more and feels stiffer underfoot. Polypropylene is the budget option, and it's also the one that softens fastest once Florida summer heat gets involved, which is why we don't recommend it for a full-sun lawn here. {a('/compare/nylon-vs-polyethylene-vs-polypropylene-turf/', 'This comparison')} lays out the trade-offs product by product.</p>"),
        sec("Why a permeable backing isn't negotiable in Central Florida",
            f"<p>Perforated-backing turf drains at more than 30 inches an hour ({src('sgw-faq', "a manufacturer's published drainage rate")}), which matters because Central Florida summer storms routinely drop 1 to 3 inches of rain in an hour. Florida's 2026 rule requires permeable turf over a permeable backing on a pervious, positively graded base as the baseline standard, not an upgrade, so a solid-backed product sold as a budget option isn't actually a legal option on a covered residential lot.</p>"),
        sec("Color blend and heat",
            f"<p>A lighter, multi-tone blend reflects a bit more sun than a single dark green and looks less artificial in bright Florida light, though the difference in surface temperature it produces is modest next to what shade and a hose rinse do. {post('coolest-artificial-grass-and-infill-for-florida', 'What actually lowers turf temperature')} separates the proven cooling methods from the marketing claims.</p>"),
        sec("What a real Florida spec sheet usually looks like",
            "<p>A supplier's actual documentation for a Florida-ready residential product typically runs a page or two: a product name, fiber type and denier, pile height and gauge, face weight in ounces per square yard, backing construction and its drainage rate, and, since May 2026, a dated statement addressing PFAS and heavy metals. A one-line description on a sales flyer isn't a substitute for that document, even when the flyer uses the same buzzwords a real spec sheet would.</p>"),
        sec("The PFAS and heavy-metal statement to ask for",
            f"<p>Since May 19, 2026, turf, backing and infill sold for a Florida single-family lot legally can't carry intentionally added PFAS or heavy metals ({src('dep-rule', 'Rule 62-308.100, F.A.C.')}), and California's own PFAS rule took effect the same year, pushing most national product lines toward PFAS-free formulations regardless of which state they ship to. Ask for the written statement in hand, not a verbal assurance; {post('is-artificial-turf-safe-for-kids-pfas-lead', 'the full safety article')} covers what that statement should say and why it matters more for a family with young kids.</p>"),
        sec("A criteria checklist, not a shopping list",
            table("What to check on any turf spec sheet before choosing for a Florida yard", ["Criterion", "What to look for", "Why it matters here"],
                  [["UV stabilization", "Explicitly stated on the spec sheet, not just a general warranty", "Central Florida sun exposure is higher than most of the country's"],
                   ["Backing permeability", "Fully perforated, drainage rate stated", "Required under the 2026 state rule; also the difference between a dry lawn and standing water after a storm"],
                   ["Face weight for the use", "Matched to lawn, pet, play or putting range, not maximized blindly", "A mismatched spec wears wrong or performs wrong for its actual job"],
                   ["PFAS / heavy-metal statement", "Written, product-specific, dated", "Required for Florida sales on a covered lot as of May 2026"],
                   ["Color blend", "Multi-tone rather than a single flat green", "Reads more natural and reflects slightly more heat"]])),
        sec("A worked example",
            "<p>Say you're comparing two spec sheets for a sunny 900 sq ft lawn in Davenport. Sheet A lists a 60 oz/sq yd polyethylene product, 1.75 inch pile, perforated backing and a dated PFAS-free statement. Sheet B lists \"premium synthetic grass, heavy-duty,\" no fiber type, no backing description and no material statement at all. Sheet A gives you every criterion above in writing; Sheet B gives you an adjective. That gap, not brand recognition, is what separates a Florida-ready spec from a guess.</p>"),
    ])
    faqs = [
        faq("Does a more expensive turf product always mean a better one for Florida?", "Not automatically. Price often tracks face weight and fiber quality reasonably well, but the criteria on this page, UV stabilization, permeability and a material statement, matter more than the price tag alone, and a mid-priced product that states all four clearly can outperform a pricier one that states none of them."),
        faq("Is a thicker backing better than a thinner one?", "Not by itself. What matters is whether the backing is fully permeable and rated for the drainage the site needs, not its thickness. A thick but poorly perforated backing can drain worse than a thinner, properly perforated one."),
        faq("Do manufacturer warranties differ meaningfully between turf grades?", "Yes, and warranty length alone isn't a reliable stand-in for quality, since terms and exclusions vary by manufacturer. What does an artificial turf warranty actually cover has more on reading the fine print rather than the number of years advertised."),
        faq("Does a turf's origin country affect whether it meets Florida's 2026 rule?", "The rule sets a material and performance standard regardless of where a product is manufactured, so an imported or domestically made turf both need the same no-added-PFAS and no-heavy-metals statement to be sold for a covered Florida lot."),
        faq("Should a shaded yard use a different spec than a full-sun one?", "The material criteria on this page don't change with shade, but a shaded lawn benefits less from a lighter color's heat reflection and more from drainage, since shade keeps a base damp longer after rain than full sun does."),
        faq("Does a sample swatch tell you everything a full spec sheet would?", "No. A swatch shows color, texture and blade shape well, but it can't show face weight, backing permeability or a dated material statement, so ask for the full spec sheet alongside any physical sample before comparing two products."),
        faq("Is a heavier product automatically the more Florida-ready choice?", "Not by itself. Weight helps durability, but a heavy product with poor backing permeability or no material statement fails the criteria on this page just as easily as a lighter one would; check every criterion rather than defaulting to the heaviest option on the shelf."),
    ]
    return page("/blog/best-artificial-grass-for-florida/", "post",
                "What Artificial Grass Holds Up in Florida?",
                "No brand is 'the best' for Florida. UV stabilization, permeable backing, face weight and a PFAS statement are the specs that actually matter, 2026.",
                "What Artificial Grass Holds Up in Florida? Specs That Matter",
                capsule("As of September 2026, no single brand is objectively best for a Florida lawn; what holds up here is UV-stabilized polyethylene fiber, a fully permeable backing that drains over 30 inches an hour, a face weight matched to the lawn's use, and a written manufacturer statement of no added PFAS or heavy metals, the standard Florida's DEP rule has required since May 19, 2026."),
                body, faqs=faqs, crumbs=CRUMBS, crumb="What holds up in Florida", published=PUB,
                sources=["stn-life", "sgw-faq", "dep-rule", "watersavers-pfas"],
                related=[("/artificial-grass-installation/", "Residential turf installation"), ("/compare/nylon-vs-polyethylene-vs-polypropylene-turf/", "Nylon vs. polyethylene vs. polypropylene"),
                         ("/blog/coolest-artificial-grass-and-infill-for-florida/", "What actually lowers turf temperature"), ("/blog/is-artificial-turf-safe-for-kids-pfas-lead/", "PFAS, lead and turf safety")])


# ================================================================== 7. front yard
def p_frontyard():
    body = "".join([
        sec("Can you put artificial turf in your front yard in Florida?",
            f"<p>Yes, as far as your city or county is concerned. Since Florida's DEP Rule 62-308.100 took effect May 19, 2026, a local government can no longer prohibit compliant synthetic turf anywhere on a covered single-family lot, front yard included, and the rule specifically says green turf has to be allowed ({src('dep-rule', 'Rule 62-308.100, F.A.C.')}). {svc('residential', 'A residential turf installation')} in a front yard has to meet the same material and drainage standard as a backyard job; what it doesn't automatically clear is your homeowners association, which is a separate authority the state rule was never written to reach.</p>"),
        sec("Why F.S. 720.3045 doesn't help here",
            f"<p>Homeowners sometimes point to the 2023 HOA statute expecting it to cover a front yard too, and it doesn't. {src('fs7203045', 'Section 720.3045')} protects items, artificial turf specifically named among them, that aren't visible from the parcel's frontage or an adjacent parcel. A front yard is, by definition, visible from the frontage, so it sits outside what that statute protects. {a('/laws/hoa-rules/', "The HOA rules page")} covers exactly where that visibility line falls for backyards and side yards, which is the situation the statute was actually written for.</p>"),
        sec("What could a city do to a front yard before May 2026?",
            f"<p>Before the rule took effect, a Central Florida city or county could ban synthetic turf outright, limit it to backyards only, or count it as impervious pavement for drainage purposes, all of which some local ordinances actually did. {src('hb683', 'HB 683')} created the statewide standard in 2025, but the preemption only switched on once DEP adopted its rule, so a front yard turf project attempted in early 2026, before May 19, could still have run into a local ban that no longer applies today. That gap is worth knowing if you're working from an old blog post or a neighbor's account of what happened a year or two ago.</p>"),
        sec("What still gets decided at the ARC",
            table("What a Florida HOA can typically still control in a front yard", ["Design element", "What an ARC often requires"],
                  [["Blade color and blend", "A natural-looking green tone; some boards restrict unusually light or dark blends"],
                   ["Pile height", "A range that visually matches the neighborhood's typical lawn height"],
                   ["Borders and edging", "A defined, often paver or bender-board edge rather than a raw cut line"],
                   ["Percentage of yard covered", "Some declarations cap how much of a visible yard can be non-living material"],
                   ["Product sample and spec sheet", "A physical sample and the manufacturer's documentation submitted with the application"]],
                  "General patterns from how ARC review tends to work, not a specific association's rules; your declaration and design guidelines control.")),
        sec("How to approach an ARC for front-yard turf",
            steps([("Read the declaration's landscaping language before applying.", "Look for words like \"sod,\" \"living ground cover\" or a minimum landscaped percentage. Some boards have already updated their guidelines since the 2025-2026 state changes; others haven't and will need to see the state rule cited."),
                   ("Bring the compliance paperwork, not just a request.", "A physical turf sample, the manufacturer's spec sheet showing permeability, and the no-added-PFAS and heavy-metals statement the state rule now requires all support the application before a single objection comes up."),
                   ("Address the visual objection directly.", "A board worried turf will look artificial responds better to a multi-tone, textured product photo or sample than to an assurance alone."),
                   ("Get the decision and any conditions in writing.", "Florida's HOA statute sets procedures for architectural review regardless of what's being reviewed; a written approval with stated conditions protects you if a future board member questions it.")])
            + f"<p>{a('/tools/hoa-packet-checklist/', 'The HOA and ARC application checklist')} lists everything reviewers typically want assembled before a front-yard submission goes in.</p>"),
        sec("A worked example",
            "<p>Say you have a corner lot in a Poinciana subdivision with frontage on two streets and a homeowners association whose guidelines require \"a maintained, living lawn\" without mentioning turf by name. The city or county can't refuse a compliant turf installation on either street-facing side of that lot. The HOA can still require an ARC application, and because a corner lot has two visible frontages instead of one, expect the board to review both sides as front yard, not treat the shorter side as a hidden backyard the way it might on an interior lot.</p>"),
        sec("What about the strip between the sidewalk and the street?",
            f"<p>That strip usually sits inside a public right-of-way or a utility easement, and Florida's turf rule doesn't change either one. {src('dep-rule', 'Rule 62-308.100')} explicitly doesn't alter easements or rights-of-way, so a city that requires a permit, a specific setback, or simply prohibits any permanent installation in that strip keeps that authority regardless of what's allowed on the rest of the front yard. Check with your city or county before extending turf past your own property line into that gap, even if the rest of the front yard is straightforward.</p>"),
        sec("What happens if the HOA says no anyway",
            f"<p>An association that flatly refuses to consider a compliant application, rather than reviewing it under its normal design standards, is on shakier ground than one that approves it with conditions on color or borders. This isn't legal advice, and a board that won't budge is a conversation for a Florida community-association attorney, not an installer. {a('/laws/hoa-rules/', "The HOA rules page")} covers what the 2023 visibility statute does and doesn't reach, and where the open legal questions still sit.</p>"),
    ])
    faqs = [
        faq("Does a wider street setback count as making a front yard less visible?", "Not under the state rule, which addresses local government bans, not HOA visibility standards at all. Under the separate HOA visibility statute, a deep setback might factor into whether an association argues a specific area reads as visible from the frontage, but it isn't a fixed distance rule."),
        faq("Can a city require a minimum percentage of the front yard to stay living plant material regardless of the state turf rule?", "The published rule summaries describe a local government being unable to prohibit compliant turf outright or regulate it inconsistently with the state standard, which is a different question from a design ordinance requiring some live landscaping elsewhere on the lot, such as foundation plantings. Check your specific city or county's landscape code for anything beyond the turf itself."),
        faq("Does a model home or builder-installed front lawn have to meet the same 2026 standard?", "The rule applies to installation on covered single-family lots generally, not by who performs the work, so a builder installing turf in a new front yard would be expected to meet the same material and drainage standard as any other installer."),
        faq("If my HOA already allowed turf before 2026, does anything change now?", "Not for an HOA-approved installation specifically; the 2026 rule addresses what local governments can prohibit, not what an association that already permits turf requires. If your board's design standards predate current material rules, a new install still has to meet the state's PFAS, infill and drainage requirements regardless of what the HOA's older paperwork says."),
        faq("Does a front yard turf project need a separate drainage review from the city?", "Some jurisdictions review drainage as part of any permit application regardless of the surface material; check your specific city or county's permit page, since the state rule stops an outright ban but doesn't erase a legitimate drainage review process."),
    ]
    return page("/blog/artificial-turf-front-yard-florida/", "post",
                "Artificial Turf in a Florida Front Yard",
                "Since May 19, 2026, Florida cities can't ban compliant turf in a front yard. Here's why your HOA still can, and how to approach an ARC application.",
                "Can you put artificial turf in your front yard in Florida?",
                capsule("Since Florida's DEP Rule 62-308.100 took effect May 19, 2026, a city or county can no longer prohibit compliant synthetic turf anywhere on a covered single-family lot, front yard included, and green turf specifically must be allowed. What the state rule doesn't touch is your homeowners association, which still runs its own design review for anything visible from the street. This isn't legal advice."),
                body, faqs=faqs, crumbs=CRUMBS, crumb="Turf in a front yard", published=PUB,
                sources=["dep-rule", "hb683", "fs7203045", "marathon-pr", "olg-720"],
                related=[("/laws/florida-hb-683/", "HB 683 and the DEP rule, requirement by requirement"), ("/laws/hoa-rules/", "Can a Florida HOA ban artificial turf?"),
                         ("/laws/permits/", "Permits by city and county"), ("/tools/hoa-packet-checklist/", "HOA / ARC application checklist")])


# ================================================================== 8. shady side yards
def p_sideyard():
    body = "".join([
        sec("Artificial grass for shady side yards where sod won't grow",
            f"<p>St. Augustine needs several hours of direct sun a day to hold density, and the narrow side yard between two Central Florida homes, often 5 to 10 feet wide and shaded most of the day by both roof lines, rarely gets it ({ext(IFAS_STAUG[1], "UF/IFAS's homeowners guide to St. Augustinegrass")}). {svc('residential', 'Artificial turf')} has no light requirement at all, which is why a side yard is one of the most common places we get called for exactly this reason. It comes with two site conditions most other parts of a lot don't have: a drainage swale, and an AC condensate line.</p>"),
        sec("Why does grass die in the side yard specifically?",
            "<p>Shade is only part of it. A narrow side yard traps humidity between two exterior walls with less airflow than an open backyard, which favors fungal disease over healthy turfgrass growth even before chinch bugs or foot traffic get involved. Add a shared drainage path running down the middle, and the side yard ends up damp, dim and disease-prone all at once, exactly the combination St. Augustine handles worst.</p>"),
        sec("Where's the swale, and why can't turf touch it?",
            f"<p>Most Central Florida subdivisions route stormwater through a shallow swale along at least one side yard, and Florida's 2026 turf rule puts that area off-limits: synthetic turf can't be installed within a swale, ditch or stormwater pond, since covering it would block the drainage path it's designed to carry ({src('dep-rule', 'Rule 62-308.100, F.A.C.')}). In practice that means turf runs up to the top edge of the swale on either side and stops, leaving the swale itself open or lightly planted rather than turfed over.</p>"),
        sec("AC condensate: the side yard's other water source",
            "<p>A side yard is also where most homes route their air conditioner's condensate line, which can drip steadily onto the same few square feet for years during Florida's long cooling season. Left unmanaged, that steady drip keeps one section of turf backing damp longer than the rest of the yard, inviting the mold and mildew a well-drained lawn otherwise avoids. Running the condensate line to a splash block a few feet past the turf's edge, or tying it into a French drain alongside the swale, keeps that moisture from concentrating on one section of the pile.</p>"),
        sec("Does a narrow width change how turf gets seamed?",
            "<p>Often, yes. A side yard rarely matches turf's standard 15-foot roll width, so a strip that's only 6 to 10 feet wide usually means cutting one long panel down rather than running a full, uncut roll the way a wide backyard would. Fewer total seams is generally the goal in a tight space, since every seam is a place moisture and debris can work in over time, so a good layout plan for a narrow run favors one long cut with the grain running the length of the yard over several shorter cross-pieces.</p>"),
        sec("What a narrow gate does to equipment access",
            f"<p>Many side yards are also the only path equipment has to reach a backyard beyond, and a gate narrower than about 3 feet rules out a plate compactor or a small skid steer entirely. {post('how-artificial-turf-is-installed-step-by-step', 'The installation sequence, step by step')} covers how much longer hand tools add to base compaction specifically; a side yard that's tight enough to work by hand for its own turf can also be the bottleneck that slows down a larger backyard project behind it.</p>"),
        sec("Comparing turf against the other side-yard options",
            table("Side yard surface options compared", ["Option", "Handles shade", "Handles the swale", "Upkeep"],
                  [["Artificial turf", "Fully; no light requirement at all", "Stops at the swale's edge; can't be laid inside it", "A rinse and occasional brush, no mowing"],
                   ["Pavers", "Fully; unaffected by shade", "Can be set beside a swale with proper joint spacing for drainage", "Occasional joint-sand top-up and washing"],
                   ["Rock or gravel", "Fully; unaffected by shade", "Works within some swale designs if permeable and properly graded", "Weed control and occasional raking; can shift over time"],
                   ["St. Augustine sod", "Struggles; thins and dies in deep shade", "Grows through a swale, since it's a living surface", "Mowing, fertilizing on a restricted schedule, frequent replacement in shade"]],
                  f"{a('/compare/turf-vs-pavers-vs-rock-side-yard/', 'The full side-yard comparison')} goes deeper on cost and drainage for each option.")),
        sec("A worked example",
            "<p>Say you have an 8-foot-wide side yard running 40 feet between a Hunters Creek home and its neighbor, with a shallow swale down the middle and a condensate line dripping near the AC pad closer to the back of the house. Turf can go on both sides of the swale, roughly 3 feet of usable width on each side after accounting for the drainage path itself, with the swale left as a narrow planted or gravel strip in between. Rerouting the condensate line to drain a few feet past the turf's edge, rather than directly onto it, keeps that one section from staying wet longer than the rest of the run.</p>"),
        sec("What this changes about the base underneath",
            f"<p>A side yard's tighter footprint and shared drainage path make the base work more finicky, not less important, than a wide-open backyard. {post('base-under-artificial-turf-florida-sandy-soil', "The base guide for Central Florida's sandy soil")} covers the washed crushed rock standard that applies here just as much as anywhere else, with less room to correct a grading mistake once turf is down in a narrow strip.</p>"),
    ])
    faqs = [
        faq("Can turf be laid over the swale itself if it's fully permeable?", "No. Florida's 2026 rule excludes swales, ditches and stormwater ponds from synthetic turf regardless of the product's permeability rating, since the concern is preserving the drainage path itself, not just water passing through the surface on top of it."),
        faq("Does a side yard need a different infill than a sunny backyard?", "Not because of shade specifically, though a consistently damp, shaded section benefits from the same fast-draining, natural-material infill the state rule already requires everywhere else on the lot: silica sand, zeolite or non-toxic coated sand."),
        faq("Will moss or algae grow on turf in a permanently shaded side yard?", "It can, under the same conditions that would grow it on any damp, shaded surface, usually where drainage is poor or organic debris sits and rots. A properly graded, permeable base and an occasional rinse prevent nearly all of it."),
        faq("Is a side yard a good candidate for turf between pavers instead of full turf coverage?", f"Often, yes, especially in a very narrow strip where a full turf panel would be hard to seam cleanly. {a('/turf-and-pavers/', 'Turf between pavers')} covers that hybrid approach and what changes about the layout."),
        faq("Does a fence post or footer in the middle of the run complicate turf layout?", "A little. Turf gets cut around a post rather than seamed at it, which adds a small custom cut but doesn't otherwise change the base or drainage plan for the rest of the strip."),
        faq("Does a side yard need its own drainage plan separate from the rest of the property?", "Generally yes, since a side yard's grade and swale often route water independently of the front and back yards. A grading plan that only considers the main lawn can miss a side yard's specific low point."),
        faq("Can a side yard's turf tie visually into a backyard's turf on the other side of a gate?", "Usually, if the same product, color and grain direction carry through both areas; a gate or fence line is a natural break point, so a slight product change there is far less noticeable than one in the middle of an open lawn."),
    ]
    return page("/blog/artificial-grass-for-shady-side-yards/", "post",
                "Artificial Grass for Shady Side Yards",
                "St. Augustine fails in narrow, shaded Florida side yards. What turf can and can't do there under the state's 2026 rule, plus alternatives compared.",
                "Artificial grass for shady side yards where sod won't grow",
                capsule("St. Augustine needs several hours of direct sun to hold density, which a narrow, 5-to-10-foot Central Florida side yard rarely gets. Artificial turf has no light requirement, but as of September 2026 the state's turf rule keeps it out of the drainage swale that runs down most side yards, so turf goes beside the swale, not over it, with the AC condensate line routed away from the pile."),
                body, faqs=faqs, crumbs=CRUMBS, crumb="Turf for shady side yards", published=PUB,
                sources=["dep-rule", "ifas-turf", IFAS_STAUG],
                related=[("/compare/turf-vs-pavers-vs-rock-side-yard/", "Turf vs. pavers vs. rock for a side yard"), ("/turf-and-pavers/", "Turf between pavers"),
                         ("/blog/base-under-artificial-turf-florida-sandy-soil/", "Base for Central Florida's sandy soil"), ("/laws/florida-hb-683/", "Florida's 2026 turf rule, in full")])


# ================================================================== 9. install steps
def p_steps():
    body = "".join([
        sec("How artificial turf is installed, step by step",
            f"<p>A typical 600 to 1,000 sq ft Central Florida backyard moves through ten stages over two to four working days, from the first shovel to the final rinse. {svc('residential', 'A residential installation')} follows this same sequence whether it's a straightforward rectangle or a yard with curves and a pool cage; what changes is how long each stage takes and how much cutting the layout requires.</p>"),
        sec("The full sequence",
            steps([("Layout and utility check.", "Mark the turf area, flag any shallow irrigation lines, low-voltage wiring or cable, and confirm gate widths for equipment access. Roughly half a day on a standard yard."),
                   ("Sod and soil removal, haul-off.", "Strip the existing sod and the top 3 to 4 inches of soil so the finished grade lands at the right height once base and turf go back on top. About one day for 600 to 1,000 sq ft, longer with a rented sod cutter than with tracked equipment."),
                   ("Grading.", "Shape the exposed soil to a 1-2% slope away from the house, checked with a laser level or string line rather than by eye. Often combined with removal on the same day for a straightforward, flat lot."),
                   ("Irrigation capping.", "Cap any sprinkler heads that fell inside the turf footprint at the valve box, since Florida's 2026 rule doesn't allow in-ground irrigation to water synthetic turf. Usually an hour or two, done alongside grading."),
                   ("Base placement.", "Spread 2 to 4 inches of washed, open-graded crushed rock or crushed concrete, material rinsed ahead of time so fines don't bind into a crust once wet. Roughly half a day for a standard yard."),
                   ("Compaction.", "Run a plate compactor over the base in two lifts rather than one thick pass, checking firmness as you go. Often combined with base placement, adding a half day on a larger or more complex layout."),
                   ("Turf layout and cutting.", "Unroll the turf, match grain direction across seams, and cut panels to the yard's actual shape, working around beds, drains and hardscape edges. About half a day for a standard rectangular yard, more with curves."),
                   ("Seaming and perimeter anchoring.", "Join panels with seam tape and adhesive, then anchor every edge and seam with nails or a bender-board edge to meet the state rule's wind and flood anchoring standard. Half a day to a full day depending on how many seams the layout needs."),
                   ("Infill application.", "Broom in infill at roughly 1 to 2 lb per square foot, then power-broom against the grain to stand the blades up and settle the material evenly. About half a day."),
                   ("Final rinse and walkthrough.", "Rinse the finished lawn, check every edge and seam by hand, and walk the yard together before calling the job done. A couple of hours.")])),
        sec("How long each stage actually takes, on a 600-1,000 sq ft yard",
            table("Typical stage duration on a standard Central Florida backyard", ["Stage", "Typical time", "What extends it"],
                  [["Layout, removal, grading", "1-1.5 days", "Narrow gate access, tree roots, or a yard with more than one grade change"],
                   ["Base placement and compaction", "0.5-1 day", "A larger delivery of base rock that has to be wheelbarrowed rather than dumped directly"],
                   ["Turf layout, seaming, anchoring", "1-1.5 days", "Curved beds, multiple turf zones, or a high seam count from a narrow, irregular shape"],
                   ["Infill and final rinse", "0.5 day", "A large area needing multiple infill passes, or wind that scatters loose material before it's brushed in"]],
                  "Ranges assume normal weather and reasonable equipment access; a gate too narrow for a compactor can add most of a day on its own.")),
        sec("What Florida specifics show up at each stage",
            f"<p>Three details separate a Central Florida build from a generic install guide. The base has to be washed, not just crushed, so fines don't bind into the crust Florida's 2026 rule was written to prevent. Irrigation heads under the footprint get capped rather than removed entirely in most cases, since capping is faster and meets the same no-in-ground-irrigation standard. And every edge and seam gets anchored specifically to withstand wind and flooding, language the state standard uses directly, which is a firmer requirement than \"taped down\" implies.</p>"),
        sec("Where permits and inspections fit into the schedule",
            f"<p>If a specific jurisdiction requires a permit for the job, that step happens before layout begins, not somewhere in the middle of the sequence, since most offices want the application in hand before equipment shows up on site. {a('/laws/permits/', 'The permit page for your city or county')} covers whether a standard residential turf job needs one at all; a straightforward backyard often doesn't, while a project that touches drainage, an easement or a protected tree's drip line is more likely to. Building that lead time into the schedule up front avoids a stalled project once base material has already been delivered.</p>"),
        sec("A worked example",
            f"<p>Say you have an 800 sq ft backyard behind a Hunters Creek pool cage with a double gate wide enough for a compact skid steer. Layout, removal and grading fill day one. Base placement and compaction take most of day two, timed around an afternoon thunderstorm that pushes the final compaction pass to the next morning. Turf layout, seaming and anchoring take most of day three, and infill plus the final rinse wrap up by early afternoon. Three days total, close to the shorter end of the typical range because access wasn't a problem and the layout was a simple rectangle.</p>"),
        sec("What to expect once the crew arrives",
            f"<p>{post('what-to-expect-on-turf-installation-day', 'A full walkthrough of installation day')} covers what to move out of the way beforehand and what the noisiest stages sound like from inside the house. For a side-by-side look at doing some of this yourself, {post('diy-vs-professional-artificial-turf-installation', 'the DIY-versus-professional comparison')} breaks down which of these ten stages are the ones most likely to go wrong without experience.</p>"),
    ])
    faqs = [
        faq("Does a Central Florida rainy-season afternoon storm delay every stage equally?", "No. Base placement and compaction are the most weather-sensitive, since a soaked, uncompacted base needs to dry before the final compaction pass. Turf laying and seaming can often continue under a covered or partly finished area even after a storm passes through."),
        faq("Can seaming happen the same day as base compaction?", "On a small, simple yard, sometimes, if compaction finishes early and the base has had time to firm up. On most 600 to 1,000 sq ft jobs, splitting them across two days gives the compacted base a chance to settle before turf goes down on top of it."),
        faq("Does the crew inspect the base before laying turf, or just move straight to it?", "A careful crew checks grade and firmness by walking the compacted base and looking for any soft spots or low points before turf goes down, since a mistake here is far more work to fix once the turf is in place."),
        faq("How much of the timeline is cutting turf to fit curves versus laying it flat?", "On a yard with curved beds or an irregular shape, cutting and seaming can take noticeably longer than the table above shows for a simple rectangle, sometimes adding most of an extra half day for the added seam count alone."),
        faq("Does a putting green or playground pad add extra days to this same sequence?", "Yes, mainly at the base stage. A putting green's shaped, contoured subbase and a playground's rated shock pad both take longer to build correctly than the flat, compacted base a standard lawn uses, even though the surrounding steps stay the same."),
    ]
    return page("/blog/how-artificial-turf-is-installed-step-by-step/", "post",
                "How Artificial Turf Installation Works",
                "A 600-1,000 sq ft Central Florida yard takes two to four days across ten stages, from layout to final rinse. Each stage timed, September 2026.",
                "How artificial turf is installed, step by step",
                capsule("As of September 2026, a typical 600 to 1,000 sq ft Central Florida backyard takes two to four working days across ten stages: layout, removal, grading, irrigation capping, base placement, compaction, turf laying, seaming, infill and a final rinse. Washed base rock, capped irrigation heads and anchored seams and edges are the three Florida-specific details that separate this sequence from a generic install guide."),
                body, faqs=faqs, crumbs=CRUMBS, crumb="Installation, step by step", published=PUB,
                sources=["dep-rule", "hb683"],
                related=[("/artificial-grass-installation/", "Residential turf installation"), ("/blog/base-under-artificial-turf-florida-sandy-soil/", "Base for Central Florida's sandy soil"),
                         ("/blog/what-to-expect-on-turf-installation-day/", "What to expect on installation day"), ("/blog/diy-vs-professional-artificial-turf-installation/", "DIY or hire a contractor?")])


# ================================================================== 10. glossary
def p_glossary():
    body = "".join([
        sec("Artificial turf terms explained",
            f"<p>This glossary defines the terms that show up on a Florida turf quote or spec sheet, grouped by product, base, installation, putting greens, pets and law, from face weight and denier to drip line and PFAS. {svc('putting', 'A putting green quote')} and {svc('sports', 'a sports-turf bid')} tend to use the widest mix of these terms in one document, which is where a glossary like this earns its keep.</p>"
            + table("Test standards behind common spec numbers", ["Spec", "What it measures", "Test standard"],
                    [["Face weight", "Weight of yarn fiber per square yard, not the backing", "ASTM D5848"],
                     ["Pile height", "Blade length from the backing to the tip", "ASTM D5793"],
                     ["Denier", "Thickness of an individual yarn fiber", "ASTM D1907"],
                     ["Tuft bind", "Pull force before a tufted blade releases from the backing", "ASTM D1335"]],
                    f"{ext(STC_SPEC[1], 'Synthetic Turf Council performance guidelines')} lists the full set of test methods manufacturers use.")),
        sec("Product terms",
            ul(["<strong>Face weight.</strong> How much yarn sits on a square yard of backing, in ounces; heavier generally means denser and longer-wearing turf.",
                f"<strong>Pile height.</strong> How tall the blades stand, from about 0.4 in on a putting surface to 2 in on a full, plush lawn. {post('artificial-turf-pile-height-and-face-weight', 'The full by-use table')} breaks this down by application.",
                "<strong>Gauge.</strong> The spacing between tufted rows, commonly 3/8 to 5/8 in; a tighter gauge packs more yarn into the same area.",
                "<strong>Denier.</strong> The thickness of a single yarn fiber; a higher denier resists matting and holds its shape longer under sun and traffic.",
                "<strong>Tuft bind.</strong> The force needed to pull one tufted blade out of the backing; low tuft bind shows up years later as bald, thinning patches.",
                "<strong>Thatch.</strong> Curled fiber tufted in at the base of the blades to add body and a more natural look, similar to dead grass mixed into a real lawn.",
                "<strong>Backing.</strong> The material the yarn is tufted into; a primary backing holds the tufts, and a secondary coating locks them in place.",
                "<strong>UV stabilization.</strong> Additives built into the yarn that slow color loss and brittleness from sun exposure, the difference between a lawn that fades in years and one that fades in a decade or more."])),
        sec("Base and drainage terms",
            ul(["<strong>Subgrade.</strong> The native soil beneath the base rock; Florida's 2026 rule requires it not be compacted so hard that it hurts percolation.",
                "<strong>Base rock.</strong> Washed, open-graded crushed rock or crushed concrete laid under the turf; \"washed\" means fines have been rinsed out so the material doesn't bind into a crust.",
                "<strong>Compaction, in lifts.</strong> Compacting base material in more than one thin layer rather than one thick pass, which produces a firmer, more even base.",
                "<strong>Percolation.</strong> How well water moves down through soil; a subgrade compacted too hard percolates poorly and can pool water under the base.",
                "<strong>Permeable backing.</strong> A backing perforated to let water pass through rather than pool on top; required under the state's 2026 material standard.",
                "<strong>Positive grade.</strong> A slope, typically 1-2%, that carries water away from the house instead of toward it.",
                "<strong>Weed barrier.</strong> A fabric layer sometimes placed under the base to slow weed growth; usually skipped under pet turf because it can trap urine against the base."])),
        sec("Installation terms",
            ul(["<strong>Seam.</strong> The joint between two turf panels, joined with tape and adhesive and matched for grain direction so the join disappears into the pile.",
                "<strong>Grain direction.</strong> Which way the blades lean on a roll of turf; mismatched grain across a seam shows up as a visible line or color shift.",
                "<strong>Perimeter anchor.</strong> Nails, staples or a bender-board edge securing the turf's outer edge; Florida's rule requires anchoring at all edges and seams to withstand wind or flooding.",
                "<strong>Infill.</strong> Granular material brushed between the blades to hold the backing down and keep fibers standing; limited to natural or coated sand on a Florida lawn.",
                "<strong>Silica sand.</strong> The standard, natural infill material for a lawn; rounded silica grains help fibers stand without excess heat retention.",
                "<strong>Zeolite.</strong> A natural mineral infill that helps neutralize pet-urine odor between rinses, common in pet-turf builds.",
                "<strong>Coated sand.</strong> Silica sand with a functional coating, such as an antimicrobial or cooling treatment; the coating has to be non-toxic to comply with the state rule."])),
        sec("Putting green terms",
            ul([f"<strong>Stimp speed.</strong> A measurement of how far a ball rolls on a green; most home greens land in the 8-10 range, slower than a tournament green. {post('backyard-putting-green-cost-florida', 'The putting green cost guide')} has more on what shapes a home build.",
                "<strong>Cup and flag.</strong> The actual hole and marker set into a green, priced separately from the turf and base beneath it.",
                "<strong>Fringe / collar.</strong> The longer-pile turf bordering a putting surface, transitioning it visually into the surrounding lawn.",
                "<strong>Contouring.</strong> A shaped subbase built to add slope and break to a green's roll, priced separately from a flat installation.",
                "<strong>Chipping pad.</strong> A separate turf zone with a taller pile than the putting surface, built for a wedge to interact with the way it would on real fairway grass."])),
        sec("Pet terms",
            ul([f"<strong>Odor-control infill.</strong> Zeolite or an antimicrobial coated sand chosen specifically to manage ammonia buildup between rinses. {svc('pet', 'The pet turf page')} covers the full build.",
                "<strong>Flush-and-drain.</strong> Rinsing a pet area thoroughly enough that liquid moves through the backing and base rather than sitting on the surface.",
                "<strong>No weed barrier.</strong> A deliberate choice on pet-turf builds, since a fabric layer under the base can trap urine against it instead of letting it drain through."])),
        sec("Law and paperwork terms",
            ul([f"<strong>Drip line.</strong> The ring on the ground beneath a tree's outermost branches, used to estimate its protected root zone. {post('artificial-turf-near-live-oaks-and-palms', 'This page')} covers how it applies to turf.",
                "<strong>Setback.</strong> A required distance from a feature, such as the 10-foot setback Florida's rule sets from a lake, pond or canal.",
                "<strong>PFAS.</strong> A class of manufactured chemicals; Florida's 2026 rule bars any intentionally added PFAS in turf, backing or infill.",
                "<strong>Certified arborist.</strong> A tree-care professional credentialed to certify that a specific project, such as turf near a drip line, won't harm a protected tree.",
                f"<strong>ARC.</strong> An architectural review committee, the HOA body that approves visible exterior changes; {a('/laws/hoa-rules/', 'the HOA rules page')} covers what it can and can't require.",
                "<strong>Rule 62-308.100.</strong> Florida's DEP synthetic turf standard, effective May 19, 2026, setting minimum material and installation requirements for single-family lots of one acre or less.",
                "<strong>Local business tax receipt.</strong> A county or city tax registration for operating a business locally; not a skills license, but worth checking before hiring."])),
        sec("A worked example",
            "<p>Say you have a quote that lists \"80 oz, 1.75 in, C-shape blade, coated silica infill\" for a 900 sq ft backyard. That's a face weight of 80 ounces per square yard, a 1.75-inch pile height, a curved blade profile sold for a fuller look, and infill that's silica sand carrying a functional coating, most likely for odor control or a mild cooling effect. Reading a spec sheet this way turns four glossary terms into an actual picture of what's going down in the yard, rather than four numbers to take on faith.</p>"),
    ])
    faqs = [
        faq("What's the difference between face weight and total weight on a spec sheet?", "Face weight counts only the yarn fiber per square yard; total weight adds the backing material back in. A spec sheet that lists only one of the two isn't necessarily hiding anything, but ask which figure you're looking at before comparing two products."),
        faq("Why do two turf products with the same pile height feel different underfoot?", "Face weight, denier and blade shape all affect how dense and springy a lawn feels, so two products can share a pile height while differing noticeably in hand feel and how quickly the blades spring back after foot traffic."),
        faq("Is stimp speed the same measurement pro golfers use?", "Yes, the same stimpmeter method, though a home green's turf and infill are tuned more for durability outdoors than for matching a tournament green's faster, more delicate surface."),
        faq("Does a manufacturer ever list denier without listing face weight?", "Some do, since the two measure different things: denier is about individual fiber thickness, and face weight is about total yarn density. A complete spec sheet lists both, along with pile height and backing type."),
    ]
    return page("/blog/artificial-turf-glossary/", "post",
                "Artificial Turf Glossary: Key Terms Explained",
                "Face weight, thatch, stimp, drip line and PFAS: turf terms defined in plain language, grouped by product, base, install, law and pets.",
                "Artificial turf terms explained: face weight, infill, thatch, stimp",
                capsule("This glossary defines the terms that show up on a Florida turf quote or spec sheet as of September 2026, from face weight and denier to drip line and PFAS, grouped by product, base, installation, putting greens, pets and law, with each term linked to the page that covers it in full."),
                body, faqs=faqs, crumbs=CRUMBS, crumb="Turf glossary", published=PUB,
                sources=["dep-rule", "fs7203045", STC_SPEC],
                related=[("/putting-greens/", "Backyard putting green installation"), ("/pet-turf/", "Pet turf and dog runs"),
                         ("/laws/florida-hb-683/", "HB 683 and the DEP rule, requirement by requirement"), ("/blog/artificial-turf-pile-height-and-face-weight/", "Pile height and face weight by use")])


def get_pages():
    return [p_license(), p_safety(), p_environment(), p_oaks(), p_spec(), p_bestgrass(), p_frontyard(), p_sideyard(), p_steps(), p_glossary()]
