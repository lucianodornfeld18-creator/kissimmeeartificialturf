# -*- coding: utf-8 -*-
"""Lake Mary, FL (tier 3, Seminole County). Permit-office, water, golf-community, soil and Census
facts researched September 2026; see report for sources. Reuses the Seminole County permit/water/soil
facts already established in c_permits.py and c_counties.py (facts and URLs only, fresh sentences)."""
from _data import CITIES
from _helpers import page, capsule, sec, table, faq, a, svc, city, price
from _cityservice import cityservice_pages

SLUG = "lake-mary"
LM = CITIES[SLUG]

SRC = [
    ("City of Lake Mary — Building Division", "https://www.lakemaryfl.com/157/Building"),
    ("City of Lake Mary — Irrigation Restrictions", "https://www.lakemaryfl.com/393/Irrigation-Restrictions"),
    ("Lake Mary, Florida — Wikipedia", "https://en.wikipedia.org/wiki/Lake_Mary,_Florida"),
    ("Timacuan Golf & Country Club", "https://timacuanclub.com/"),
    ("USDA NRCS — official series description, Candler series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/C/CANDLER.html"),
    ("USDA NRCS — official series description, Tavares series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/T/TAVARES.html"),
    ("USDA NRCS — official series description, Apopka series", "https://soilseries.sc.egov.usda.gov/OSD_Docs/A/APOPKA.html"),
    ("Seminole County Property Appraiser — parcel search", "https://www.scpafl.org/"),
    "dep-rule", "fs125572", "fs7203045", "usda-wss",
]

HUB = page(
    "/areas/lake-mary/", "city",
    "Synthetic Grass for Lake Mary, FL Yards (2026)",
    "Artificial turf for Lake Mary, FL homes along the I-4 corridor and golf-course lots near Heathrow and Timacuan, at Central Florida prices, September 2026.",
    "Turf for Lake Mary yards, from the I-4 corridor to golf-course lots",
    capsule(f"Between corporate-corridor subdivisions off Interstate 4 and golf-course lots near Heathrow and Timacuan, Lake Mary covers two very different kinds of yard, and we work both, synthetic lawns, pet turf and putting greens alike. Residential turf runs {price('residential')} per square foot as of September 2026. Lake Mary sits about {LM['miles']} miles from our Kissimmee base, close to the edge of where we schedule regular work."),
    "".join([
        sec("A corporate-corridor city at the edge of our range",
            f"<p>Lake Mary covers just over 9 square miles along the western side of Interstate 4, and the corridor itself carries more office parks than any other stretch we work near, home to regional or national offices for companies that include the American Automobile Association, Deloitte and Verizon. The city sits about {LM['miles']} miles from our Kissimmee crew's base, near the edge of the roughly 40-mile radius we schedule around, so a Lake Mary date usually shares a route with another Seminole County stop rather than standing alone on the calendar. None of that changes the {price('residential')} per square foot range a job here costs as of September 2026; it only affects which day of the week we can offer, since the drive itself takes a real bite out of a morning.</p>"),
        sec("Golf-course lots at Heathrow and Timacuan",
            f"<p>Timacuan, a roughly 400-acre golf community built around a course designed by Ron Garl and Bobby Weed, sits inside Lake Mary, and its executive lots run wider than almost anything else in the city. Heathrow, the larger master-planned community just north and west of the city line, carries its own golf courses and a homeowners association that reviews exterior changes, though we have not found a published Heathrow or Timacuan document naming synthetic turf specifically, so treat any claim about a written turf rule at either one as unverified until an association confirms it. What we can say is that both run an architectural review for anything visible from the street or a fairway, a separate step from either the city or the county permit process and worth clearing before ordering material.</p>"),
        sec("Water, irrigation days and the utility that bills for it",
            "<p>Lake Mary runs its own water utility, and its irrigation ordinance caps every zone at three-quarters of an inch and one hour per watering day. Wednesdays and Saturdays cover odd-numbered addresses, Thursdays and Sundays the even ones, cut back to a single day apiece once standard time returns each fall. Drip, micro-spray and bubbler systems, along with a hand-held hose fitted with an automatic shutoff, are exempt from that calendar entirely, which is close to how a capped turf area behaves once the state standard takes its in-ground heads out of service for good. The St. Johns River Water Management District sets the regional policy underneath the city's own ordinance.</p>"),
        sec("What a Lake Mary permit covers, and what we have not researched",
            f"<p>Lake Mary's Building Division, at 911 Wallace Court, handles permits for the city directly instead of routing them through Seminole County, and applications run through the city's own online plan-review portal. We have not gone through Lake Mary's ordinance page by page the way {a('/laws/permits/seminole-county/', 'our Seminole County permit page')} covers unincorporated land nearby, so we are not going to guess at what the city's code says about synthetic turf specifically. A call to the Building Division before scheduling a crew settles that, and a parcel search on the county property appraiser's site is worth running first, since a Lake Mary mailing address does not always sit inside the city limits, Heathrow being the clearest example nearby. An association's own architectural review is a separate matter again: {a('/laws/hoa-rules/', 'the HOA visibility law')} sets what it can restrict, not either government's permit counter, and Heathrow and Timacuan both run one.</p>"),
        sec("Choosing who builds it",
            "<p>A search for the best artificial turf installer near you in Lake Mary turns up plenty of options, and the way to narrow it is with specifics rather than star ratings: base depth and material by name, whether the crew already knows Timacuan and Heathrow run their own architectural review, and what happens to the irrigation zone once the turf goes in.</p>"
            + table("Lake Mary neighborhoods and how the build changes",
                    ["Neighborhood type", "What we find there", "How that changes the job"],
                    [["Timacuan or Heathrow golf-course lot", "A wide executive lot with a review for anything visible from a fairway or street", "Clearing the review before ordering material; contouring room for a larger putting green"],
                     [f"Lakefront on {city('lake-mary', 'Lake Mary')} lake or Crystal Lake", "A shoreline inside the state's 10-foot setback unless a seawall exists", "Staking the buildable line before pricing the job"],
                     ["I-4 corridor subdivision, 1980s-2000s", "A builder-graded sandy ridge lot with pines and oaks", "Standard washed crushed-rock base; watching for drip lines under mature pines"],
                     ["Older lot near original downtown Lake Mary", "A smaller, established yard predating the city's fastest growth", "Tighter access, with more cutting and edging per square foot"]],
                    f"The base recipe does not change from row to row, compacted washed crushed rock under every neighborhood type listed; what shifts is the review paperwork, the grading and how close a yard sits to a fairway or a shoreline. The {price('residential')} per square foot range, checked September 2026, applies the same way to all four.")),
        "<!--AUTO:city-services-->",
    ]),
    faqs=[
        faq("Is Heathrow actually part of the City of Lake Mary?",
            "Only partly. Some of Heathrow sits inside Lake Mary and some sits in unincorporated Seminole County right next to it, so the two halves can answer to different building departments even though the community reads as one place. A parcel search settles which office has a specific address."),
        faq("Do Timacuan or Heathrow have a written rule about artificial turf?",
            "We have not found one published by either association as of September 2026. Both run an architectural review for anything visible from the street or the course, which is a real step to clear, but we are not going to attribute a specific turf rule to either community without a document to point to."),
        faq("Is Lake Mary too small to be worth its own service page?",
            "No, though it is compact: just over 9 square miles, built out mostly since the 1970s. The I-4 corridor and its golf communities produce enough turf calls to make Lake Mary a regular stop, not an occasional one."),
        faq("How does Lake Mary's three-quarter-inch watering limit affect a new turf lawn?",
            "It does not, once the heads under the turf are capped, which the state standard requires regardless of the city's own irrigation math. The limit still governs whatever lawn or bed stays on a sprinkler around the turf."),
    ],
    sources=SRC, city=SLUG, crumbs=[("Service areas", "/areas/")], crumb="Lake Mary",
    related=[("/areas/seminole-county/", "Artificial turf in Seminole County"), ("/laws/permits/seminole-county/", "Seminole County permit rules for turf"),
             ("/areas/sanford/", "Artificial turf in Sanford"), ("/areas/altamonte-springs/", "Artificial turf in Altamonte Springs"),
             ("/artificial-turf-cost/", "Full turf cost guide")],
)

LOCAL = {
    "residential": {
        "title": "Artificial Grass Installation Near the Lake Mary I-4 Corridor",
        "meta": "Synthetic lawns for Lake Mary homes near the I-4 corridor and golf communities, at Central Florida prices, checked September 2026.",
        "h1": "Installing artificial grass on an I-4 corridor lot in Lake Mary",
        "lede": capsule(f"A synthetic lawn in Lake Mary runs {price('residential')} per square foot installed as of September 2026, the same range whether the lot backs up to a fairway at Timacuan or sits on a quiet street built in the 1980s. What moves the number here is the sandy ridge soil under most of the city and how much of the existing yard is builder fill rather than native ground."),
        "sections": [
            ("Building on Lake Mary's ridge sand",
             "<p>Most of Lake Mary sits on excessively to moderately well drained ridge sands, mapped to series such as Candler, Tavares and Apopka, rather than the flatwoods soils found closer to the St. Johns River to the north. Ridge sand like this holds almost no water on its own, a trait that reads as a benefit right up until a plate compactor tries to lock down a stable layer on ground that keeps shifting underfoot with every pass. The payoff comes after a storm: a lawn built on this soil almost never traps the standing water a flatwoods lot elsewhere in the county would, so the work here is less about fighting a high water table and more about pinning down a level surface on ground that would rather move.</p>"),
            ("1980s-2000s subdivisions under pine and oak canopy",
             "<p>The bulk of Lake Mary's housing went up between the 1980s and the early 2000s, on ridge lots planted with a mix of pines and oaks rather than the citrus-grove terrain found further south in the county. A pine's roots sit shallower and spread less aggressively than a live oak's, so a typical Lake Mary yard is less likely to trigger the state's drip-line exception than an old in-town lot elsewhere in Seminole County, though a mature oak on an older street here still counts the same way it would anywhere else. Pine needles are the more constant issue: a thick bed of them left to break down against a new turf edge changes drainage there gradually, the same way leaf litter does under any oak.</p>"),
            ("Permits, the county line and what we have not verified",
             f"<p>Lake Mary runs its own Building Division rather than routing permits through Seminole County, and we have not gone through the city's ordinance the way {a('/laws/permits/seminole-county/', 'our county permit page')} covers unincorporated land nearby. A call to the Building Division, or a look at the city's own online plan-review portal, is the honest next step rather than a guess. Checking the county property appraiser's parcel record first is worth doing on any lot near the city's edge, since parts of neighboring Heathrow sit outside Lake Mary's own limits even though the mailing address looks the same.</p>"),
        ],
        "scenario": ("Say you have a 1990s Lake Mary lot near the corridor",
                     f"<p>Say you have a 1994 home two streets off the I-4 corridor with a 1,100 sq ft lawn, sandy ridge soil throughout, and a single live oak near the driveway that does not reach far enough to trigger the drip-line rule. At {price('residential')} per square foot, that lawn runs roughly ${1100 * 10:,}–${1100 * 16:,} for a straightforward install with no tree exception to work around. A similar lot at Timacuan with a wider 1,800 sq ft yard and an architectural review to clear first prices around ${1800 * 10:,}–${1800 * 16:,} for the turf itself, plus whatever time the review adds before a crew can start.</p>"),
        "faqs": [
            faq("Does Lake Mary's sandy soil mean less base material, not more?",
                "No, the depth stays the same, two to four inches of washed crushed rock either way. What changes is compaction technique: loose ridge sand needs closer attention during compaction than a wetter flatwoods lot, since it shifts more easily under a plate compactor."),
            faq("Is a Timacuan or Heathrow architectural review the same as a city permit?",
                "No, they are two separate approvals. An association review covers what is visible from a fairway or the street under its own design guidelines, while a Building Division permit, if one applies, covers the construction itself. Clearing one does not excuse the other."),
            faq("Are there Lake Mary neighborhoods old enough to have mature oaks like Sanford's historic district?",
                f"A few streets near the original downtown predate most of the city's 1980s and 1990s growth and carry older oak canopy, but nothing in Lake Mary matches the scale of {city('sanford', 'the historic district in Sanford')}. Most drip-line questions here involve a single mature tree rather than a whole street of them."),
        ],
        "sources": SRC,
    },
    "pet": {
        "title": "Pet Turf for Lake Mary, FL Backyards",
        "meta": "Fast-draining pet turf for Lake Mary dog runs, from golf-course backyards to older fenced lots, at Central Florida prices, checked September 2026.",
        "h1": "Pet turf for a fenced Lake Mary backyard",
        "lede": capsule(f"Lake Mary's irrigation ordinance caps every zone at three-quarters of an inch a day, a limit that stops mattering the moment a dog run's heads are capped for good. That run then costs {price('pet')} per square foot installed as of September 2026, with the faster-draining base and odor-control infill a plain lawn does not carry."),
        "sections": [
            ("A fenced yard at Timacuan or Heathrow",
             f"<p>A dog run behind a Timacuan or Heathrow home usually means clearing an architectural review first, since both communities review exterior changes visible from a fairway or the street, even though neither has a published rule naming synthetic turf specifically as far as we have found. A run tucked behind a privacy fence, out of sight from those sightlines, is the simpler version of that conversation, and {a('/laws/hoa-rules/', 'the HOA visibility law')} is why a fenced backyard gets treated differently from a front-yard installation in the first place. Either way, the wider lots common to both communities usually leave enough room for a run sized well past what a smaller in-town yard could manage.</p>"),
            ("Rinsing instead of watering on Lake Mary's schedule",
             "<p>Lake Mary's ordinance exempts a hand-held hose with an automatic shutoff nozzle from the watering calendar entirely, which happens to describe exactly how a capped pet turf area gets cleaned: a quick rinse whenever the yard needs it, any day, any hour, since the schedule limiting sprinklers was never built to cover a hose in someone's hand. The three-quarter-inch, one-hour cap that governs the rest of a Lake Mary lawn has nothing to do with a pet run once its heads are out of service, which is one less thing to plan around on a day when a dog has tracked in more than usual.</p>"),
            ("Older, established Lake Mary lots away from the golf communities",
             f"<p>Not every Lake Mary address sits inside a golf community. Streets built in the 1980s away from Timacuan and Heathrow carry the same fenced, established backyards found in older subdivisions anywhere else in the county, without an architectural review to clear first. A dog run on one of these older lots is closer in scope to a job in {city('altamonte-springs', 'Altamonte Springs')} or {city('longwood', 'Longwood')} than to one at Timacuan, and it usually costs less to schedule since there is no association paperwork sitting between the quote and the install date.</p>"),
        ],
        "scenario": ("Say a Heathrow-area dog run needs turf before winter",
                     f"<p>Say you have a 300 sq ft run behind a Heathrow-area home, already cleared through the architectural review, with two sprinkler heads to cap along the back fence line. At {price('pet')} per square foot, that run prices around ${300 * 12:,}–${300 * 16:,}, infill included. A second, smaller 150 sq ft run added along a side yard for a second dog brings the combined job to roughly ${450 * 12:,}–${450 * 16:,} total, and since the review paperwork is already on file, adding that second run later is mostly a scheduling question rather than another approval to chase down.</p>"),
        "faqs": [
            faq("Does a Timacuan or Heathrow dog run need approval before it goes in?",
                "Likely yes, if any part of it would be visible from the street or a fairway. A run entirely behind a privacy fence is the more straightforward case, and either way, checking with the association before ordering material avoids redoing an application after the fact."),
            faq("Is pet turf cheaper on an older Lake Mary lot without an association?",
                "Usually a little, mainly because there is no review process adding time to the schedule, not because the turf or base costs less. The material and labor price the same across Lake Mary regardless of which neighborhood it goes into."),
        ],
        "sources": SRC,
    },
    "putting": {
        "title": "Backyard Putting Greens for Lake Mary, FL Golf Lots",
        "meta": "Contoured putting greens for Lake Mary yards near Timacuan and Heathrow, plus lakefront lots, at Central Florida prices, checked September 2026.",
        "h1": "A putting green for a Lake Mary golf-community lot",
        "lede": capsule(f"A backyard putting green in Lake Mary runs {price('putting')} per square foot as of September 2026, and the city's golf communities, Timacuan and Heathrow among them, produce more of these calls than anywhere else in our Seminole County work. Lot width, not the state's waterbody rules, is usually the first design question."),
        "sections": [
            ("Designing around Timacuan's wide golf-course lots",
             "<p>An executive lot backing onto Timacuan's course, or one inside Heathrow, tends to run wide enough for a full green with a chipping pad and more than one cup, a layout a narrower older lot elsewhere in the county could not fit. Both communities review anything visible from a fairway before it goes in, and a putting green, sitting in plain sight of the golf course by definition, is the kind of project where clearing that review first matters more than it would for a fenced dog run tucked out of sight. Neither association has a published rule naming synthetic turf specifically as far as we have found, so the review is a design conversation, not a known checklist.</p>"),
            ("Lake Mary lake and Crystal Lake: the 10-foot line",
             "<p>Lake Mary takes its name from the small lake near the center of town, and Crystal Lake nearby is where the original Bent's Station settlement stood, on its north shore, before the area took the Lake Mary name in the 1880s. A handful of homes on either shoreline today sit close enough to the water that the state's 10-foot waterbody setback becomes the first line on a putting-green design, not an afterthought added once the layout is already drawn, unless a seawall or bulkhead already separates the yard from the lake. Staking that boundary before ordering fringe turf or contouring material keeps a green's design honest about how much usable space actually fits, since pulling back a finished contour afterward costs more than planning around the line from the start.</p>"),
            ("What changes on a wider lot versus a narrower one",
             "<p>Lot width, more than which body of water is nearby, is what actually sets a Lake Mary putting green's scope. A Timacuan or Heathrow lot wide enough for a fairway view usually has room for a green well past the minimum size that makes contouring worthwhile, while an older, narrower Lake Mary lot away from either community often fits a smaller, single-cup green better than an ambitious multi-tier design. Either way the base does not change: the same washed, open-graded crushed rock, built slightly deeper than a plain lawn's base to hold a level, consistent roll through a Central Florida rainy season.</p>"),
        ],
        "scenario": ("Say a Timacuan-area lot has room for a full green",
                     f"<p>Say you have a Timacuan-area lot with a 600 sq ft area set aside along the back fence, wide enough for a two-cup green with a chipping pad and fringe turf around the edges. At {price('putting')} per square foot, that project runs roughly ${600 * 18:,}–${600 * 25:,}, contouring included. A smaller, single-cup version on a narrower 350 sq ft lot near older Lake Mary streets runs about ${350 * 18:,}–${350 * 25:,}, with less fringe turf and a simpler subgrade shape, proof that lot width changes this number more than proximity to either golf course does.</p>"),
        "faqs": [
            faq("Does a putting green need association approval at Timacuan even if it is not visible from the course?",
                "Possibly still yes, depending on the association's review threshold for backyard changes generally, not just what is visible from the fairway. Confirming the exact scope with the association before ordering material avoids a design that has to be redone."),
            faq("Is Lake Mary's Crystal Lake the same body of water tracked separately by the Census Bureau?",
                "No, and that mix-up is worth avoiding. The Crystal Lake tied to Lake Mary's own history is the small lake on the north side of the original settlement, not the separate, similarly named place the Census Bureau tracks elsewhere in Florida."),
            faq("Why does lot width matter more than golf-course proximity for a Lake Mary green?",
                "Because contouring, multiple cups and a chipping pad all need physical space to read correctly, and a wide executive lot has that room regardless of whether it faces a fairway. A narrower lot can still get a green, just a simpler one."),
        ],
        "sources": SRC,
    },
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
