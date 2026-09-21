# -*- coding: utf-8 -*-
"""Authoring helpers. Content modules import from here and return page dicts via page()."""
import html as _html
import re

from _data import (BASE_URL, PUBLIC_NAME, PHONE_E164, PHONE_DISPLAY, EMAIL, OWNER, OWNER_ROLE, REVIEWED, SERVICES, SERVICE_ORDER,
                   CITIES, CITY_ORDER, COUNTIES, SOURCES, PRICES, PRICE_DATE, PRICE_LABEL, WEB3FORMS_KEY, price_range, city_service_route, nearest, TIER_SERVICES)


def esc(s):
    return _html.escape(str(s), quote=True)


# ---------------------------------------------------------------- links
def a(route, text, title=None):
    """Internal link. Routes are checked by qa/qa_all.py after the build."""
    t = f' title="{esc(title)}"' if title else ""
    return f'<a href="{route}"{t}>{text}</a>'


def svc(key, text=None):
    return a(SERVICES[key]["route"], text or SERVICES[key]["name"].lower())


def city(slug, text=None):
    return a(CITIES[slug]["route"], text or CITIES[slug]["name"])


def county(key, text=None):
    return a(COUNTIES[key]["route"], text or COUNTIES[key]["name"])


def cs(city_slug, service, text=None):
    return a(city_service_route(city_slug, service), text or f"{SERVICES[service]['name'].lower()} in {CITIES[city_slug]['name']}")


def post(slug, text):
    return a(f"/blog/{slug}/", text)


def ext(url, text):
    return f'<a href="{esc(url)}" rel="noopener">{text}</a>'


def src(sid, text=None):
    label, url = SOURCES[sid]
    return ext(url, text or label)


def tel(text=None):
    return f'<a class="tel" href="tel:{PHONE_E164}">{text or PHONE_DISPLAY}</a>'


# ---------------------------------------------------------------- blocks
def capsule(html):
    """40-70 word direct answer that must stand alone if quoted."""
    return f'<p class="capsule">{html}</p>'


def sec(h2, html, sid=None):
    i = f' id="{sid}"' if sid else ""
    return f'<section{i}><h2>{h2}</h2>\n{html}\n</section>'


def table(caption, headers, rows, note=None):
    th = "".join(f'<th scope="col">{h}</th>' for h in headers)
    trs = []
    for r in rows:
        tds = "".join((f'<th scope="row">{c}</th>' if i == 0 else f"<td>{c}</td>") for i, c in enumerate(r))
        trs.append(f"<tr>{tds}</tr>")
    n = f'<p class="tnote">{note}</p>' if note else ""
    return f'<div class="tw" role="region" aria-label="{esc(re.sub("<[^>]+>", "", caption))}" tabindex="0"><table><caption>{caption}</caption><thead><tr>{th}</tr></thead><tbody>{"".join(trs)}</tbody></table></div>{n}'


def steps(items):
    return "<ol class=\"steps\">" + "".join(f"<li><strong>{t}</strong> {d}</li>" for t, d in items) + "</ol>"


def ul(items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def faq(q, a_html):
    return (q, a_html)


def note(html):
    return f'<p class="note">{html}</p>'


def price_note():
    return f"{PRICE_LABEL}, {PRICE_DATE}, compiled from published installer pricing and national cost guides. A written quote follows a site measure."


def price(key, typical=False):
    return price_range(key, typical)


def cta(text="Get a measured quote", sub=None):
    s = f"<p>{sub}</p>" if sub else ""
    return f'<aside class="cta"><div>{s}<p class="cta-row"><a class="btn" href="/contact/">{text}</a> <span>or call {tel()}</span></p></div></aside>'


# ---------------------------------------------------------------- page constructor
def page(route, kind, title, meta, h1, lede, body, faqs=None, sources=None, related=None, crumbs=None, **kw):
    """kind: home | service | cityservice | city | county | price | law | permit | post | faq | compare | tool | page
    lede: capsule html shown under the H1. faqs: list of faq(). sources: list of SOURCES ids. related: list of (route, label).
    crumbs: list of (label, route) after Home. Extra keys: noindex, service, city, form (bool), author (bool), schema (list of dicts), published."""
    p = {"route": route, "kind": kind, "title": title, "meta": meta, "h1": h1, "lede": lede, "body": body,
         "faqs": faqs or [], "sources": sources or [], "related": related or [], "crumbs": crumbs or []}
    p.update(kw)
    return p
