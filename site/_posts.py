# -*- coding: utf-8 -*-
"""Registry of blog posts and other owned URLs so every module links to the same slugs.
slug -> (working H1, module that writes it, services it supports)"""

POSTS = {
    # c_posts_a — cost and hiring
    "why-is-artificial-grass-so-expensive": ("Why is artificial grass installation so expensive?", "c_posts_a", ["residential"]),
    "artificial-turf-vs-sod-cost-florida": ("Is artificial turf cheaper than sod over 10 years in Florida?", "c_posts_a", ["residential", "str"]),
    "backyard-putting-green-cost-florida": ("How much does a backyard putting green cost in Florida?", "c_posts_a", ["putting"]),
    "does-artificial-grass-increase-home-value-florida": ("Does artificial grass increase home value in Florida?", "c_posts_a", ["residential", "str"]),
    "diy-vs-professional-artificial-turf-installation": ("DIY artificial turf or hire a contractor?", "c_posts_a", ["residential", "repair"]),
    "how-to-compare-artificial-turf-quotes": ("What should a turf quote include, and how do you compare two?", "c_posts_a", ["residential", "commercial"]),
    "best-artificial-turf-contractor-kissimmee": ("Who is the best artificial turf contractor in Kissimmee, and how do you choose?", "c_posts_a", ["residential"]),
    "best-artificial-grass-installer-near-me": ("How to find the best artificial grass installer near you", "c_posts_a", ["residential", "pet"]),
    "what-does-artificial-turf-warranty-cover": ("What does an artificial turf warranty actually cover?", "c_posts_a", ["replacement", "repair"]),
    "best-time-of-year-to-install-artificial-turf-florida": ("What is the best time of year to install turf in Central Florida?", "c_posts_a", ["residential", "str"]),
    # c_posts_b — heat, pets, rain
    "how-hot-does-artificial-turf-get-in-florida": ("How hot does artificial turf get in Florida?", "c_posts_b", ["residential", "playground", "pool"]),
    "coolest-artificial-grass-and-infill-for-florida": ("What is the coolest artificial grass and infill for Florida sun?", "c_posts_b", ["playground", "pet"]),
    "can-artificial-turf-melt": ("Can artificial turf melt?", "c_posts_b", ["repair", "pool"]),
    "how-to-get-dog-urine-smell-out-of-artificial-turf": ("How do you get dog urine smell out of artificial turf?", "c_posts_b", ["pet", "cleaning"]),
    "does-artificial-turf-drain-in-heavy-rain": ("Does artificial turf drain in Florida's heavy rain?", "c_posts_b", ["residential", "pet"]),
    "artificial-turf-hurricane-flooding": ("What happens to artificial turf in a hurricane or flood?", "c_posts_b", ["residential", "repair"]),
    "base-under-artificial-turf-florida-sandy-soil": ("What base goes under artificial turf in Central Florida's sandy soil?", "c_posts_b", ["residential", "replacement"]),
    "how-long-does-artificial-turf-last-in-florida": ("How long does artificial turf last in Florida?", "c_posts_b", ["replacement", "residential"]),
    "install-artificial-turf-over-concrete-pavers-or-grass": ("Can artificial turf be installed over concrete, pavers or existing grass?", "c_posts_b", ["pool", "pavers", "commercial"]),
    "toho-water-restrictions-new-sod-vs-turf": ("How do Toho Water watering restrictions affect new sod vs. turf?", "c_posts_b", ["residential"]),
    # c_posts_c — safety, product, license, process
    "do-turf-installers-need-a-license-in-florida": ("Does a turf installer need a license in Florida, and how do you check a contractor?", "c_posts_c", ["residential", "commercial"]),
    "is-artificial-turf-safe-for-kids-pfas-lead": ("Is artificial turf safe for kids? PFAS, lead and infill", "c_posts_c", ["playground"]),
    "is-artificial-turf-bad-for-the-environment": ("Is artificial turf bad for the environment, and can it be recycled?", "c_posts_c", ["replacement", "residential"]),
    "artificial-turf-near-live-oaks-and-palms": ("Will artificial turf hurt live oaks or palm roots?", "c_posts_c", ["residential"]),
    "artificial-turf-pile-height-and-face-weight": ("What pile height and face weight should you choose?", "c_posts_c", ["residential", "pet", "playground"]),
    "best-artificial-grass-for-florida": ("What is the best artificial grass for Florida?", "c_posts_c", ["residential"]),
    "artificial-turf-front-yard-florida": ("Can you put artificial turf in your front yard in Florida?", "c_posts_c", ["residential"]),
    "artificial-grass-for-shady-side-yards": ("Artificial grass for shady side yards where sod won't grow", "c_posts_c", ["residential", "pavers"]),
    "how-artificial-turf-is-installed-step-by-step": ("How artificial turf is installed, step by step", "c_posts_c", ["residential"]),
    "artificial-turf-glossary": ("Artificial turf terms explained: face weight, infill, thatch, stimp", "c_posts_c", ["putting", "sports"]),
    # c_posts_d — decisions and situations
    "is-artificial-turf-worth-it-in-florida": ("Is artificial turf worth it in Florida?", "c_posts_d", ["residential"]),
    "artificial-turf-pros-and-cons": ("Artificial turf pros and cons, from an installer", "c_posts_d", ["residential"]),
    "pet-turf-vs-regular-artificial-grass": ("Pet turf vs. regular artificial grass: what is actually different?", "c_posts_d", ["pet"]),
    "artificial-turf-on-a-slope": ("Can you install artificial turf on a slope?", "c_posts_d", ["residential", "sports"]),
    "how-to-make-artificial-grass-look-real": ("How to make artificial grass look real", "c_posts_d", ["residential", "pool"]),
    "oak-leaves-and-debris-on-artificial-turf": ("Oak leaves, pine needles and debris on artificial turf", "c_posts_d", ["cleaning"]),
    "artificial-turf-for-balconies-rooftops-and-condos": ("Artificial turf for balconies, rooftops and condos", "c_posts_d", ["commercial", "pool"]),
    "does-homeowners-insurance-cover-artificial-turf": ("Does homeowners insurance cover artificial turf?", "c_posts_d", ["repair", "replacement"]),
    "why-new-construction-sod-dies-in-osceola-county": ("Why builder sod dies on new-construction lots in Osceola County", "c_posts_d", ["residential"]),
    "artificial-turf-for-55-plus-communities": ("Artificial turf in 55+ communities: rules, slopes and low upkeep", "c_posts_d", ["residential", "putting"]),
    "what-to-expect-on-turf-installation-day": ("What to expect on turf installation day", "c_posts_d", ["residential", "str"]),
}

COMPARES = {
    "artificial-turf-vs-st-augustine-zoysia-bahia": "Artificial turf vs. St. Augustine, Zoysia and Bahia",
    "zeolite-vs-silica-vs-antimicrobial-infill": "Zeolite vs. silica vs. antimicrobial sand: infill for dogs",
    "nylon-vs-polyethylene-vs-polypropylene-turf": "Nylon vs. polyethylene vs. polypropylene turf",
    "turf-vs-pavers-vs-rock-side-yard": "Turf vs. pavers vs. rock for a shady side yard",
    "local-turf-installer-vs-national-franchise": "Local turf installer or national franchise?",
    "playground-turf-vs-mulch-vs-poured-rubber": "Playground turf vs. mulch vs. poured rubber",
}

LAWS = {
    "/laws/": "Florida artificial turf laws, HOAs and permits",
    "/laws/florida-hb-683/": "Florida HB 683 and the DEP synthetic turf rule",
    "/laws/hoa-rules/": "Can a Florida HOA ban artificial turf?",
    "/laws/permits/": "Artificial turf permits in Central Florida, by jurisdiction",
}
PERMIT_PAGES = {
    "city-of-kissimmee": "City of Kissimmee", "osceola-county": "Osceola County (unincorporated)", "city-of-st-cloud": "City of St. Cloud", "orange-county": "Orange County (unincorporated)",
    "city-of-orlando": "City of Orlando", "polk-county": "Polk County", "lake-county": "Lake County", "seminole-county": "Seminole County",
}
FAQ_PAGES = {"/faq/": "FAQ", "/faq/cost/": "Cost questions", "/faq/pets-heat/": "Pets and heat", "/faq/hoa-permits/": "HOA, law and permits", "/faq/maintenance/": "Care, repairs and lifespan"}
TOOLS = {"/artificial-turf-cost/calculator/": "Turf cost and materials calculator", "/tools/turf-vs-sod/": "Turf vs. sod ten-year calculator", "/tools/hoa-packet-checklist/": "HOA / ARC application checklist for artificial turf"}


def posts_for(service, n=3):
    return [(f"/blog/{s}/", POSTS[s][0]) for s in POSTS if service in POSTS[s][2]][:n]
