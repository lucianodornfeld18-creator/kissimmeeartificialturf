# -*- coding: utf-8 -*-
"""City x service page assembler.

A city module (content/c_city_<slug>.py) supplies hand-written local material per service; the bank
(bank/b_<service>.py) supplies technical blocks in several variants. Variants are assigned with a
linear code over GF(5) so two cities never share more than one block on the same service."""
import importlib
import pathlib
import sys

from _data import CITIES, CITY_ORDER, SERVICES, SERVICE_ORDER, TIER_SERVICES, city_service_route, nearest
from _helpers import page, sec
from _posts import posts_for

ROOT = pathlib.Path(__file__).parent
sys.path.insert(0, str(ROOT / "bank"))
BLOCKS = ["base", "product", "process", "risks", "care"]
SKELETONS = [
    ["L0", "base", "L1", "product", "SC", "process", "risks", "L2", "care"],
    ["SC", "L0", "product", "L1", "base", "risks", "process", "care", "L2"],
    ["L0", "L1", "base", "process", "SC", "product", "L2", "risks", "care"],
    ["L0", "product", "SC", "L1", "risks", "base", "L2", "process", "care"],
]
_T1 = [s for s in CITY_ORDER if CITIES[s]["tier"] == 1]
_REST = [s for s in CITY_ORDER if CITIES[s]["tier"] > 1]


def has_module(slug):
    return (ROOT / "content" / f"c_city_{slug.replace('-', '_')}.py").exists()


def exists(city_slug, service):
    return has_module(city_slug) and service in TIER_SERVICES[CITIES[city_slug]["tier"]]


def _variant(city_slug, j, n):
    order = _T1 + _REST
    i = order.index(city_slug)
    if n in (5, 7):
        a, b = divmod(i % (n * n), n)
        return (a + b * j) % n
    return (i * (j + 2) + j) % n


def _bank(service):
    try:
        return importlib.import_module(f"b_{service}").BLOCKS
    except ModuleNotFoundError:
        return {}


def cityservice_pages(city_slug, local):
    """local: {service: {"title","meta","h1","lede","sections":[(h2,html)x3],"scenario":(h2,html),"faqs":[...],"sources":[...]}}"""
    c = CITIES[city_slug]
    out = []
    for service in TIER_SERVICES[c["tier"]]:
        if service not in local:
            continue
        L = local[service]
        bank = _bank(service)
        sk = SKELETONS[((_T1 + _REST).index(city_slug) + SERVICE_ORDER.index(service)) % 4]
        parts = []
        for token in sk:
            if token.startswith("L"):
                k = int(token[1])
                if k < len(L["sections"]):
                    parts.append(sec(*L["sections"][k]))
            elif token == "SC":
                parts.append(sec(*L["scenario"]))
            elif token in bank and bank[token]:
                vs = bank[token]
                h2, html = vs[_variant(city_slug, BLOCKS.index(token), len(vs))]
                poss = c["name"] + ("'" if c["name"].endswith("s") else "'s")
                rep = lambda t: t.replace("{city}'s", poss).replace("{city}", c["name"]).replace("{county}", c["county_name"])  # noqa: E731
                parts.append('<section class="bank"><h2>' + rep(h2) + "</h2>\n" + rep(html) + "\n</section>")
        near = [n for n in nearest(city_slug, 8) if exists(n, service)][:2]
        other = [s for s in TIER_SERVICES[c["tier"]] if s != service and s in local]
        idx = SERVICE_ORDER.index(service)
        other = other[idx % len(other):] + other[:idx % len(other)] if other else []
        related = [(SERVICES[service]["route"], f"{SERVICES[service]['name']}: the full guide"), (c["route"], f"Artificial turf in {c['name']}: local rules and yards")]
        related += [(city_service_route(n, service), f"{SERVICES[service]['name']} in {CITIES[n]['name']}") for n in near]
        related += [(city_service_route(city_slug, o), f"{SERVICES[o]['name']} in {c['name']}") for o in other[:2]]
        related += [("/artificial-turf-cost/", "Turf cost tables for Central Florida")] + posts_for(service, 2)
        out.append(page(city_service_route(city_slug, service), "cityservice", L["title"], L["meta"], L["h1"], L["lede"], "\n".join(parts),
                        faqs=L.get("faqs"), sources=L.get("sources"), related=related, related_title=f"More for {c['name']} yards",
                        crumbs=[(SERVICES[service]["name"], SERVICES[service]["route"])], crumb=c["name"], service=service, city=city_slug))
    return out
