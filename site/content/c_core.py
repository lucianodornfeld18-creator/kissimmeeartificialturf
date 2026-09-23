# -*- coding: utf-8 -*-
"""Index pages, tools, about/contact and legal pages."""
from _data import SERVICES, SERVICE_ORDER, PUBLIC_NAME, OWNER, PHONE_DISPLAY, PHONE_E164, EMAIL, BASE_URL, COUNTIES, COUNTY_ORDER, PRICE_DATE
from _posts import COMPARES, TOOLS
from _helpers import page, capsule, sec, table, faq, ul, steps, note, cta, a, svc, city, county, post, src, price, price_note, tel


def get_pages():
    P = []

    # ---------------------------------------------------------------- /services/
    rows = [[svc(k, SERVICES[k]["name"]), SERVICES[k]["short"], (price(SERVICES[k]["price"]) + " / sq ft") if SERVICES[k]["price"] else "Quoted per job"] for k in SERVICE_ORDER]
    body = sec("Twelve services, one trade",
               "<p>Everything we do is synthetic turf: putting it in, fixing it, cleaning it and replacing it when it's worn out. We don't mow, pour concrete or build pools. Staying narrow is how a small crew stays good at the details that decide whether a lawn lasts, which are base work, seams and drainage.</p>"
               + table("Artificial turf services and 2026 market price ranges", ["Service", "What it covers", "Installed range"], rows, price_note())) \
        + sec("Which one do you need?",
              ul([f"Grass that won't grow, or a lawn you're tired of paying for: {svc('residential', 'residential artificial grass installation')}.",
                  f"Dogs: {svc('pet', 'a pet turf system')}, which is built differently from a regular lawn.",
                  f"Golf: {svc('putting', 'a backyard putting green')}.", f"Kids and swing sets: {svc('playground', 'playground turf over a shock pad')}.",
                  f"A strip by the pool cage or inside the lanai: {svc('pool', 'pool and lanai turf')}.",
                  f"A short-term rental: {svc('str', 'vacation rental turf')}.", f"A clubhouse, apartment dog park, daycare or patio: {svc('commercial', 'commercial turf')}.",
                  f"Bocce, batting or a sled lane: {svc('sports', 'sports and fitness turf')}.", f"Green joints between pavers or a driveway ribbon: {svc('pavers', 'turf and pavers')}.",
                  f"Something wrong with turf you already own: {svc('repair', 'repair')}, {svc('cleaning', 'cleaning')} or {svc('replacement', 'replacement')}."])
              + f"<p>Prices for all of them are collected in the {a('/artificial-turf-cost/', 'turf cost guide')}, and the {a('/faq/', 'FAQ')} answers the questions that come up on nearly every site visit, with separate pages for {a('/faq/pets-heat/', 'dogs and summer heat')} and {a('/faq/maintenance/', 'upkeep and repairs')}.</p>"
              + cta("Not sure? Send photos", "Text a few pictures and rough dimensions and we’ll point you to the right service."))
    P.append(page("/services/", "index", "Artificial Turf Services in Kissimmee, FL: Install to Repair",
                  "All twelve artificial turf services from Kissimmee Artificial Turf: lawns, pet turf, putting greens, playgrounds, pool areas, repairs, cleaning and replacement.",
                  "Artificial turf services", capsule("Kissimmee Artificial Turf offers twelve synthetic turf services across Central Florida: residential lawns, pet turf, putting greens, playground, pool and lanai, vacation rental, commercial and sports surfaces, turf between pavers, plus repair, cleaning and replacement. Installed lawns run " + price("residential") + f" per square foot as of {PRICE_DATE}."),
                  body, crumb="Services", form=True))

    # ---------------------------------------------------------------- /areas/
    body = sec("Towns we cover, by county",
               f"<p>We're based in Kissimmee and work within about 40 miles, which takes in all of {county('osceola')}, most of {county('orange')}, the northern half of {county('polk')}, south {county('lake')} and {county('seminole')}. Each town page covers what's different there: the permit office, the water utility and its irrigation days, the associations you're likely to deal with and the soil under the yard.</p><!--AUTO:all-areas-->") \
        + sec("How distance affects a job",
              "<p>It doesn't change the price per square foot. It can change scheduling: towns inside about 15 miles of Kissimmee are easy to fit between larger jobs, while Lakeland, Sanford or Mount Dora usually get a dedicated day. Repairs and cleanings far from Kissimmee are grouped by area so the trip makes sense for everyone.</p>"
              + table("Service area at a glance", ["Distance from downtown Kissimmee", "Examples", "What we offer there"],
                      [["0–15 miles", "Kissimmee, St. Cloud, Celebration, Poinciana, Hunters Creek, Lake Nona, Davenport", "All twelve services"],
                       ["15–30 miles", "Orlando, Windermere, Winter Garden, Winter Park, Clermont, Haines City, Winter Haven", "All installs, repairs by area"],
                       ["30–40 miles", "Lakeland, Sanford, Lake Mary, Mount Dora, Bartow, Lake Wales", "Installs and larger repairs"]])
              + f"<p>The law is the same everywhere in the area since the state turf standard took effect in May 2026, but permits aren't. {a('/laws/permits/', 'See the permit guide by city and county')}.</p>")
    P.append(page("/areas/", "index", "Service Areas | Artificial Turf Within 40 Miles of Kissimmee",
                  "Kissimmee Artificial Turf serves Osceola, Orange, Polk, Lake and Seminole counties: every town within about 40 miles of Kissimmee, with a local page for each.",
                  "Where we install artificial turf", capsule("Kissimmee Artificial Turf works within about 40 miles of downtown Kissimmee: all of Osceola County, Orlando and south Orange County, the Polk County ridge from Davenport to Winter Haven and Lakeland, south Lake County around Clermont, and Seminole County up to Sanford. Price per square foot is the same in every town."),
                  body, crumb="Service areas", form=True))

    # ---------------------------------------------------------------- /blog/
    P.append(page("/blog/", "index", "Artificial Turf Blog | Straight Answers for Florida Yards",
                  "Plain answers about artificial grass in Central Florida: cost, heat, dogs, drainage, HOA rules, the 2026 state turf standard, product choices and care.",
                  "Artificial turf articles for Florida homeowners", capsule("Every article here answers one question people ask before buying artificial grass in Central Florida, with numbers, dates and sources: what it costs, how hot it gets, how it drains, what the HOA and the state allow, which product fits, and how to look after it."),
                  '<section class="auto"><h2>All articles</h2><!--AUTO:blog-index--></section>' + sec("Looking for a quick answer?", f"<p>The {a('/faq/', 'FAQ')} has short versions of most of these, the {a('/compare/', 'comparisons')} put options side by side, and the {a('/artificial-turf-cost/', 'cost guide')} has the price tables.</p>"),
                  crumb="Blog", wide=True))

    # ---------------------------------------------------------------- /tools/
    P.append(page("/tools/", "index", "Artificial Turf Calculators & Checklists | Kissimmee, FL",
                  "Free tools for planning an artificial turf project in Central Florida: a cost and materials calculator, a turf vs. sod ten-year calculator and an HOA checklist.",
                  "Turf planning tools", capsule("Three free planning tools for Central Florida yards: a calculator that turns your dimensions into a 2026 installed price range with base and infill quantities, a ten-year turf vs. sod comparison that uses your own mowing and water bills, and a checklist for an HOA or ARC application."),
                  sec("Pick a tool", '<ul class="grid">' + "".join(f'<li class="card"><h3><a href="{r}">{t}</a></h3></li>' for r, t in TOOLS.items()) + "</ul>"
                      + f"<p>They run in your browser and don't collect anything. When you want real numbers for your yard, {a('/contact/', 'ask for a measured quote')}.</p>"), crumb="Tools"))

    tvs = sec("Compare ten years of turf and grass with your own numbers",
              """<form id="tvs" class="lead" data-opera="skip"><div><label for="t-area">Lawn area (sq ft)</label><input id="t-area" name="area" type="number" min="0" inputmode="decimal" value="1000"></div><div><label for="t-turf">Turf installed price ($ per sq ft)</label><input id="t-turf" name="turf" type="number" min="0" step="0.5" inputmode="decimal" value="12"></div><div><label for="t-mow">Mowing and lawn service ($ per month)</label><input id="t-mow" name="mow" type="number" min="0" inputmode="decimal" value="140"></div><div><label for="t-water">Irrigation water ($ per month)</label><input id="t-water" name="water" type="number" min="0" inputmode="decimal" value="45"></div><div class="full"><label for="t-other">Fertilizer, weed and pest control ($ per year)</label><input id="t-other" name="other" type="number" min="0" inputmode="decimal" value="450"></div><div class="full"><p id="tvs-out" role="status" aria-live="polite">Enter the lawn area.</p></div></form>"""
              + "<p>The math is deliberately simple. Turf: area times your installed price, plus yearly upkeep of 30 cents a square foot with a $150 floor for brushing, infill and deodorizer. Grass: sod at $1.50 a square foot, your monthly mowing and water bills, your yearly treatment cost, and one re-sod in year six, which is about how long St. Augustine lasts in a yard with chinch bugs or shade. No inflation, no financing, no resale value.</p>") \
        + sec("How to read the result",
              f"<p>If you mow your own lawn and water from a well, enter zeros and grass will win for decades; that's the honest answer. If you pay a service and irrigate from Toho or OUC water, the lines usually cross between year five and year eight, which matches {src('bearcat-10yr', 'published ten-year models')}. The {a('/artificial-turf-cost/', 'cost guide')} has the table version, and {post('artificial-turf-vs-sod-cost-florida', 'this article walks through it year by year')}.</p>")
    P.append(page("/tools/turf-vs-sod/", "tool", "Turf vs. Sod Cost Calculator: 10 Years in Florida",
                  "Enter your lawn size, mowing bill and water bill to compare ten years of artificial turf against St. Augustine sod in Central Florida. Simple, transparent math.",
                  "Turf vs. sod: ten-year cost calculator", capsule("Enter your lawn's size and what you pay now for mowing, water and treatments. The calculator totals ten years of natural grass, including one re-sod, against ten years of artificial turf at the installed price you choose, and tells you the year turf catches up. With typical Central Florida bills that's between year five and eight."),
                  tvs, crumbs=[("Tools", "/tools/")], crumb="Turf vs. sod", sources=["bearcat-10yr", "attampa-sod", "toho-days"]))

    chk = sec("What goes in an HOA or ARC application for artificial turf",
              "<p>Review boards in Central Florida ask for roughly the same things. A complete packet gets a decision in one meeting; an incomplete one gets tabled for a month.</p>"
              + table("Application packet checklist", ["Item", "What the reviewers want to see", "Who provides it"],
                      [["Application form", "The association's own form, signed by the owner of record", "Owner"],
                       ["Site plan", "Survey or plot plan with the turf area outlined and dimensioned, plus fences, pool, easements, swales and any pond or lake edge", "Installer, from your survey"],
                       ["Product sample", "A piece at least 12 × 12 inches showing blade colors and thatch", "Installer"],
                       ["Manufacturer spec sheet", "Pile height, face weight, backing type, drainage rate, UV warranty", "Installer"],
                       ["Material safety statement", "No intentionally added PFAS or heavy metals, as the state standard requires since May 2026", "Manufacturer, via installer"],
                       ["Base and drainage note", "Base depth and material, confirmation that lot grading, swales and drainage patterns stay unchanged", "Installer"],
                       ["Edge and border detail", "How turf meets beds, pavers, sidewalks and the neighbor's lot", "Installer"],
                       ["Setback notes", "10 ft from any waterbody; outside tree drip lines or an arborist's letter; nothing in swales", "Installer"],
                       ["Contractor documents", "Business tax receipt and certificate of insurance naming the association if it asks", "Installer"],
                       ["Photos", "Current condition of the area from the street and from inside the yard", "Owner"]])) \
        + sec("Before you apply",
              steps([("Read the design guidelines.", "Search the PDF for \"turf,\" \"synthetic,\" \"sod\" and \"ground cover.\" Note any minimum planted area."),
                     ("Decide whether the area is visible.", f"If it can't be seen from the frontage or an adjacent parcel, F.S. 720.3045 limits what the association can restrict. {a('/laws/hoa-rules/', 'See how that works')}."),
                     ("Ask for the meeting calendar.", "Most boards meet monthly and need the packet a week or two ahead."),
                     ("Get the decision in writing.", "Including any conditions on color, height or borders, before material is ordered.")])
              + f"<p>We put this packet together as part of a quote. See {a('/laws/', 'the law overview')} for who regulates what, and {post('artificial-turf-front-yard-florida', 'the front-yard article')} for design choices that tend to get approved.</p>"
              + cta("Want us to prepare the packet?", "It’s part of a measured quote."))
    P.append(page("/tools/hoa-packet-checklist/", "tool", "HOA / ARC Application Checklist for Artificial Turf (Florida)",
                  "The ten items Florida HOA and ARC boards ask for before approving artificial turf, who provides each, and what changed with the 2026 state standard.",
                  "HOA and ARC application checklist for turf", capsule("A complete Florida HOA or ARC application for artificial turf has ten parts: the form, a dimensioned site plan, a 12-inch product sample, the spec sheet, a no-added-PFAS statement, a base and drainage note, border details, setback notes, contractor documents and photos. Complete packets are usually decided in one monthly meeting."),
                  chk, crumbs=[("Tools", "/tools/")], crumb="HOA checklist", sources=["fs7203045", "marathon-pr", "dep-rule"]))

    # ---------------------------------------------------------------- /about/
    body = sec("A small, local turf company",
               f"<p id=\"luis-austin\"><strong>{OWNER}</strong> owns and runs {PUBLIC_NAME}, established in 2024 and based in Kissimmee, Florida. We install, repair and clean synthetic turf, and that's the whole list. There's no showroom and no call center. When you call or text {tel()}, you reach the company, and the person who measures your yard stays responsible for the job.</p>"
               "<p>We're a service-area business: we come to you, anywhere within about 40 miles of Kissimmee. Samples, spec sheets and a measuring wheel fit in the truck.</p>") \
        + sec("How we work",
              ul(["<strong>We quote in writing, with specs.</strong> Square footage, base depth and material, the turf's pile height and face weight, infill type and weight, seam and edge method.",
                  "<strong>We build for Florida.</strong> Washed crushed rock over graded sand, natural infill, seams glued and taped, edges anchored, which is what the state's 2026 turf standard requires.",
                  "<strong>We say no when turf is the wrong answer.</strong> An unshaded west-facing play area, a swale, the ground under a live oak's canopy, the 10 feet beside a pond: we'll tell you what works there instead.",
                  "<strong>We don't publish what we can't back up.</strong> Prices on this site are market ranges with sources and dates. Laws are linked to their text. When we don't know, we say so."])
              + f"<p>The facts on this site were last reviewed in {PRICE_DATE} by {OWNER}. If you spot something out of date, email {a('mailto:' + EMAIL, EMAIL)}.</p>") \
        + sec("Where to go from here",
              f"<p>See {a('/services/', 'what we do')}, {a('/artificial-turf-cost/', 'what it costs')}, {a('/areas/', 'where we work')} and {a('/laws/', 'what Florida law says')}. Or {a('/contact/', 'ask for a quote')}.</p>")
    P.append(page("/about/", "page", "About Kissimmee Artificial Turf | Locally Owned by Luis Austin",
                  "Kissimmee Artificial Turf is a locally owned synthetic turf installer in Kissimmee, FL, established in 2024 by owner Luis Austin. How we work.",
                  "About Kissimmee Artificial Turf", capsule(f"{PUBLIC_NAME} is a locally owned synthetic turf company in Kissimmee, Florida, established in 2024 and run by owner {OWNER}. We install, repair and clean artificial grass within about 40 miles of Kissimmee, quote in writing with full specifications, and build to Florida's 2026 state turf standard."),
                  body, crumb="About", author=True,
                  schema=[{"@type": "Person", "@id": BASE_URL + "/about/#luis-austin", "name": OWNER, "jobTitle": "Owner", "worksFor": {"@id": BASE_URL + "/#business"}, "url": BASE_URL + "/about/"}]))

    # ---------------------------------------------------------------- /contact/
    body = sec("Call, text or write",
               f"<p><strong>Phone and text:</strong> {tel()}<br><strong>Email:</strong> {a('mailto:' + EMAIL, EMAIL)}<br><strong>Based in:</strong> Kissimmee, Florida. We come to you; there's no storefront to visit.</p>"
               "<p>Photos speed everything up. Text the yard, the gate you'd bring materials through, and any spot that holds water after rain. Calls may be recorded so we don't lose the details.</p>") \
        + sec("What happens next",
              steps([("We reply.", "Usually the same day, with any questions about the yard."), ("We measure.", "About half an hour on site: dimensions, access, slope, irrigation, trees, water's edge, HOA."),
                     ("You get a written quote.", "With the specs spelled out so you can compare it with anyone else's.")])
              + f"<p>Want a rough number first? Try the {a('/artificial-turf-cost/calculator/', 'cost calculator')} or read the {a('/artificial-turf-cost/', 'cost guide')}. Wondering about rules? Start at {a('/laws/', 'Florida turf laws and HOAs')}. Common questions are in the {a('/faq/', 'FAQ')}, and our {a('/areas/', 'service area')} lists every town we cover.</p>")
    P.append(page("/contact/", "page", "Contact Kissimmee Artificial Turf | (689) 202-3710",
                  "Call or text (689) 202-3710 or send the form for a measured artificial turf quote in Kissimmee and Central Florida. Photos of the yard help us answer faster.",
                  "Get a turf quote", capsule(f"Call or text {PHONE_DISPLAY}, email {EMAIL}, or send the form. We reply, usually the same day, set a time to measure, and send a written quote with base, turf, infill, seam and edge specifications."),
                  body, crumb="Contact", form=True, form_title="Request a measured quote"))

    # ---------------------------------------------------------------- legal
    body = sec("What we collect and why",
               f"<p>When you send a form on this site we receive what you typed: name, phone, email, city, the service you're interested in, approximate area, whether dogs use the yard, whether an HOA is involved, and your message. We also record the page you sent it from and, if present, the advertising parameters in the link that brought you here. We use this to reply to you and to prepare a quote. We don't sell it.</p>"
               "<p>Form submissions are delivered to our inbox by Web3Forms, a form-delivery service, and copied to our customer management system. Both act on our instructions. Email to our domain is forwarded through Cloudflare Email Routing.</p>") \
        + sec("Phone calls and texts", f"<p>Our number, {PHONE_DISPLAY}, is provided by Twilio. Calls may be recorded and voicemails transcribed so we can keep track of project details; the greeting says so before you're connected. If you text us, we keep the conversation. We contact you by phone, text or email only about your request, and only if you ticked the consent box or contacted us first. Reply STOP to any text to end messages.</p>") \
        + sec("Analytics and cookies", "<p>We use Cloudflare Web Analytics, which doesn't use cookies or fingerprinting and doesn't track you across sites. The site sets no advertising cookies. Your browser's session storage holds the address of the first page you visited so that, if you send a form, we know which page was useful; it's cleared when you close the tab.</p>") \
        + sec("Sharing, retention and your choices", f"<p>We share project details with crew members and subcontractors who need them to do the work, and with service providers named above. We keep quotes and job records for as long as needed for warranty and tax purposes. To see, correct or delete what we hold about you, email {a('mailto:' + EMAIL, EMAIL)}.</p><p>Effective September 21, 2026.</p>")
    P.append(page("/privacy/", "page", "Privacy Policy | Kissimmee Artificial Turf", "How Kissimmee Artificial Turf handles form submissions, calls, texts and analytics. No advertising cookies, no selling of personal information.",
                  "Privacy policy", capsule("We collect what you send us through the form, by phone, text or email, use it to reply and quote, and don't sell it. The site uses cookie-free analytics."), body, crumb="Privacy"))

    body = sec("Using this site", "<p>The information here is general guidance about synthetic turf in Central Florida. Prices are market ranges with a date, not offers. Articles about laws, permits and associations summarize public sources and aren't legal advice. Calculators do simple arithmetic on the numbers you enter. A quote becomes binding only when it's written, signed and accepted.</p>") \
        + sec("Content and links", f"<p>Text, tables and graphics are ours unless credited. You're welcome to quote short passages with a link back. We link to government, university and industry sources; we don't control those sites. If something here is wrong or out of date, tell us at {a('mailto:' + EMAIL, EMAIL)}.</p>") \
        + sec("Messages", "<p>By sending a form with the consent box ticked, you agree that we may call, text or email you about that request. Consent isn't a condition of purchase. Message and data rates may apply. Reply STOP to opt out of texts.</p><p>These terms are governed by the laws of the State of Florida. Effective September 21, 2026.</p>")
    P.append(page("/terms/", "page", "Terms of Use | Kissimmee Artificial Turf", "Terms for using kissimmeeartificialturf.com: prices are dated market ranges, legal articles are informational, and quotes are binding only in writing.",
                  "Terms of use", capsule("Prices on this site are dated market ranges, legal articles are informational, calculators are arithmetic, and only a written, accepted quote is binding."), body, crumb="Terms"))

    body = sec("Our aim", "<p>We want everyone to be able to use this site, including people who navigate by keyboard, use a screen reader, zoom the page or prefer reduced motion. We build to the Web Content Accessibility Guidelines 2.2, level AA: real headings and landmarks, labelled form fields, visible focus, sufficient color contrast, touch targets of at least 24 pixels, tables with captions and header cells, and no content that depends on hover or animation.</p>") \
        + sec("If something doesn't work", f"<p>Tell us what page and what happened: call or text {tel()} or email {a('mailto:' + EMAIL, EMAIL)}. We'll fix it, and in the meantime we'll give you the information or take your request another way.</p>")
    P.append(page("/accessibility/", "page", "Accessibility | Kissimmee Artificial Turf", "Kissimmee Artificial Turf builds its website to WCAG 2.2 AA. How to report a problem and get help by phone, text or email.",
                  "Accessibility", capsule("This site is built to WCAG 2.2 level AA. If any part of it doesn't work for you, call, text or email and we'll help directly and fix the page."), body, crumb="Accessibility"))

    P.append(page("/thank-you/", "plain", "Thanks | Kissimmee Artificial Turf", "Your request was sent.", "Thanks. We have your request.",
                  capsule(f"We'll reply soon, usually the same day. If it's urgent, call or text {PHONE_DISPLAY}."),
                  f"<p>While you wait: the {a('/artificial-turf-cost/', 'cost guide')} explains what moves a quote up or down, and the {a('/faq/', 'FAQ')} covers what people ask on site visits.</p>", noindex=True))
    P.append(page("/404/", "plain", "Page Not Found | Kissimmee Artificial Turf", "That page doesn't exist.", "We can't find that page",
                  capsule("The link may be old or mistyped."),
                  f"<p>Try the {a('/', 'home page')}, {a('/services/', 'services')}, {a('/artificial-turf-cost/', 'turf cost guide')}, {a('/areas/', 'service areas')}, {a('/blog/', 'blog')} or {a('/faq/', 'FAQ')}. Or call {tel()}.</p>", noindex=True))
    return P
