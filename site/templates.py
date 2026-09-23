# -*- coding: utf-8 -*-
"""HTML shell, inline CSS, JSON-LD and the lead form for kissimmeeartificialturf.com."""
import datetime
import hashlib
import json
import pathlib
import re

from _data import (BASE_URL, DOMAIN, PUBLIC_NAME, PHONE_E164, PHONE_DISPLAY, EMAIL, OWNER, OWNER_ROLE, REVIEWED, LAUNCH_DATE, SERVICES, SERVICE_ORDER,
                   CITIES, CITY_ORDER, COUNTIES, COUNTY_ORDER, SOURCES, WEB3FORMS_KEY, BUSINESS)
from _helpers import esc
from _photos import info as _pinfo, url as _purl, ORDER as PHOTO_ORDER

ROOT = pathlib.Path(__file__).parent
_js = (ROOT / "static" / "site.js").read_bytes()
SITE_JS = "/static/site." + hashlib.sha256(_js).hexdigest()[:10] + ".js"
try:
    WIKI = json.loads((ROOT / "_wiki.json").read_text(encoding="utf-8"))
except Exception:
    WIKI = {}

CSS = """
@font-face{font-family:"DM Serif Display";src:url(/static/fonts/dm-serif-display-latin.woff2) format("woff2");font-weight:400;font-style:normal;font-display:optional}
:root{--bg:#FBF7EE;--card:#FFFDF8;--ink:#14261F;--text:#22352E;--mute:#4C5F57;--line:#DDD3BF;--pine:#1C6A29;--pine-d:#0B4A18;--sun:#B8431A;--sun-d:#953512;--sand:#F1E7D2;--r:10px;--w:1120px;
--disp:"DM Serif Display",Georgia,"Times New Roman",serif;--body:system-ui,-apple-system,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%;scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--text);font-family:var(--body);font-size:1.0625rem;line-height:1.65}
img,svg{max-width:100%;height:auto}a{color:var(--pine);text-underline-offset:3px}a:hover{color:var(--sun-d)}
:focus-visible{outline:3px solid var(--sun);outline-offset:2px;border-radius:4px}
h1,h2,h3{font-family:var(--disp);font-weight:400;color:var(--ink);line-height:1.15;margin:0 0 .45em}
h1{font-size:clamp(2rem,5.2vw,3.25rem);letter-spacing:-.01em}h2{font-size:clamp(1.5rem,3.4vw,2.1rem);margin-top:1.7em}h3{font-size:1.3rem;margin-top:1.4em}
p{margin:0 0 1.05em}ul,ol{margin:0 0 1.1em;padding-left:1.3em}li{margin:.3em 0}
.wrap{max-width:var(--w);margin:0 auto;padding:0 20px}.narrow{max-width:790px}
.skip{position:absolute;left:-999px;top:0;background:var(--ink);color:#fff;padding:10px 14px;z-index:9}.skip:focus{left:8px;top:8px}
.top{background:var(--pine-d);color:#F3EBDA;font-size:.93rem}.top .wrap{display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap;padding-top:7px;padding-bottom:7px}.top a{color:#fff;font-weight:600}
header.site{background:var(--card);border-bottom:1px solid var(--line)}header.site .wrap{display:flex;align-items:center;justify-content:space-between;gap:16px;min-height:68px;flex-wrap:wrap}
.brand{display:flex;align-items:center;gap:10px;text-decoration:none;color:var(--ink);font-family:var(--disp);font-size:1.32rem;line-height:1.05}
.brand svg{flex:none}.brand small{display:block;font-family:var(--body);font-size:.7rem;letter-spacing:.12em;text-transform:uppercase;color:var(--mute)}
#navb{display:none;background:none;border:2px solid var(--ink);border-radius:8px;padding:9px 13px;min-height:44px;font:600 .95rem var(--body);color:var(--ink);cursor:pointer}
nav.main ul{list-style:none;display:flex;flex-wrap:wrap;gap:2px;margin:0;padding:0}nav.main a{display:block;padding:12px 11px;text-decoration:none;color:var(--ink);font-weight:600;font-size:.97rem;border-radius:8px}nav.main a:hover,nav.main a[aria-current]{background:var(--sand)}
.btn{display:inline-block;background:var(--sun);color:#fff;text-decoration:none;font-weight:700;padding:13px 22px;border-radius:999px;border:0;min-height:48px;font-size:1rem;line-height:1.35;cursor:pointer;font-family:var(--body)}.btn:hover{background:var(--sun-d);color:#fff}
.btn.alt{background:transparent;color:var(--ink);box-shadow:inset 0 0 0 2px var(--ink)}.btn.alt:hover{background:var(--ink);color:#fff}
.crumbs{font-size:.9rem;color:var(--mute);padding:14px 0 0}.crumbs ol{list-style:none;display:flex;flex-wrap:wrap;gap:4px 8px;margin:0;padding:0}.crumbs li+li:before{content:"/";margin-right:8px;color:var(--line)}.crumbs a{color:var(--mute)}
.hero{padding:34px 0 10px}.hero.home{display:grid;grid-template-columns:1.15fr .85fr;gap:36px;align-items:center;padding:48px 0 24px}
.eyebrow{font-size:.8rem;letter-spacing:.14em;text-transform:uppercase;font-weight:700;color:var(--sun-d);margin:0 0 .7em}
.capsule{font-size:1.16rem;line-height:1.6;color:var(--ink);border-left:4px solid var(--sun);padding:2px 0 2px 16px;margin:0 0 1.2em}
.hero-cta{display:flex;flex-wrap:wrap;gap:12px;align-items:center;margin:1.1em 0 .4em}
.by{font-size:.9rem;color:var(--mute);margin:.2em 0 0}
main section{margin:0 0 .6em}
.grid{display:grid;gap:18px;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));margin:1.2em 0;padding:0;list-style:none}
.card{background:var(--card);border:1px solid var(--line);border-radius:var(--r);padding:18px 18px 14px;margin:0}.card h3{margin:0 0 .35em;font-size:1.2rem}.card p{margin:0 0 .5em;font-size:.98rem}.card a{font-weight:600}
.tw{overflow-x:auto;margin:1.1em 0 .4em;border:1px solid var(--line);border-radius:var(--r);background:var(--card)}
table{border-collapse:collapse;width:100%;font-size:.97rem}caption{caption-side:top;text-align:left;font-weight:700;color:var(--ink);padding:12px 14px 8px}
th,td{padding:10px 14px;text-align:left;vertical-align:top;border-top:1px solid var(--line)}thead th{background:var(--sand);color:var(--ink);font-size:.9rem;border-top:0}tbody th{font-weight:600;color:var(--ink)}
.tnote,.note{font-size:.92rem;color:var(--mute)}.note{background:var(--sand);border-radius:var(--r);padding:12px 16px}
.steps{padding-left:1.4em}.steps li{margin:.6em 0}
.faq h3{font-family:var(--body);font-weight:700;font-size:1.08rem;margin:1.3em 0 .3em;color:var(--ink)}
.cols{columns:3 220px;column-gap:28px;padding:0;list-style:none}.cols li{break-inside:avoid;margin:.25em 0}
.cta{background:var(--pine-d);color:#F4EDDD;border-radius:16px;padding:24px 26px;margin:2em 0}.cta p{margin:0 0 .6em}.cta a{color:#fff}.cta .btn{background:#F6E7C6;color:var(--ink)}.cta .btn:hover{background:#fff;color:var(--ink)}.cta-row{display:flex;flex-wrap:wrap;gap:12px 16px;align-items:center;margin:0}
.src{font-size:.92rem;color:var(--mute);border-top:1px solid var(--line);margin-top:2em;padding-top:1em}.src ul{padding-left:1.1em}.src h2{font-family:var(--body);font-size:1rem;font-weight:700;margin:0 0 .4em}
.rel{background:var(--card);border:1px solid var(--line);border-radius:var(--r);padding:16px 20px;margin:2em 0}.rel h2{font-size:1.25rem;margin:0 0 .4em}.rel ul{margin:0}
form.lead{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:22px;display:grid;gap:14px;grid-template-columns:1fr 1fr;margin:1.2em 0}
form.lead .full{grid-column:1/-1}label{display:block;font-weight:600;font-size:.93rem;color:var(--ink);margin-bottom:4px}
input,select,textarea{width:100%;font:inherit;font-size:1rem;padding:11px 12px;border:1.5px solid #8C9A92;border-radius:8px;background:#fff;color:var(--ink);min-height:46px}textarea{min-height:96px}
.ck{display:flex;gap:10px;align-items:flex-start;font-weight:400;font-size:.9rem;color:var(--text)}.ck input{width:22px;min-height:22px;height:22px;margin-top:2px;flex:none}.hp{position:absolute;left:-9999px}.ferr{color:#8A1F11;font-weight:600;margin:0}
footer.site{background:var(--ink);color:#D9D3C4;margin-top:56px;padding:40px 0 26px;font-size:.95rem}footer.site a{color:#F3EBDA}footer.site h2{font-family:var(--body);font-size:.82rem;letter-spacing:.12em;text-transform:uppercase;color:#fff;margin:0 0 .7em}
.fg{display:grid;gap:28px;grid-template-columns:repeat(auto-fit,minmax(200px,1fr))}footer.site ul{list-style:none;padding:0;margin:0}footer.site li{margin:.1em 0}footer.site li a{display:inline-block;padding:5px 0}
.legal{border-top:1px solid #33463E;margin-top:28px;padding-top:16px;font-size:.87rem;color:#B9B3A4}
.badge{text-align:center}.badge img{width:min(360px,70vw);aspect-ratio:1/1}.layers{display:block;max-width:460px;margin:1.2em auto}.layers text{font:600 11px var(--body);fill:var(--ink)}
figure.ph{margin:1.5em 0}figure.ph img{display:block;width:100%;height:auto;border-radius:var(--r);background:var(--sand)}figure.ph figcaption{font-size:.9rem;color:var(--mute);margin:.55em 0 0}
.pgrid{display:grid;gap:12px;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));list-style:none;padding:0;margin:1.2em 0}.pgrid li{margin:0}.pgrid a{display:block;border-radius:var(--r);overflow:hidden;line-height:0}.pgrid img{width:100%;height:auto;aspect-ratio:4/3;object-fit:cover;background:var(--sand);transition:transform .3s}.pgrid a:hover img{transform:scale(1.03)}
.hero-ph{position:relative;line-height:0}.hero-ph>img{width:100%;height:auto;aspect-ratio:4/3;object-fit:cover;border-radius:18px;background:var(--sand)}.hero-ph .bd{position:absolute;right:16px;bottom:16px;width:96px;height:96px;border-radius:50%;background:#fff;box-shadow:0 2px 12px rgba(0,0,0,.28)}
.gal{columns:2 320px;column-gap:24px}.gal figure.ph{break-inside:avoid;margin:0 0 24px}
@media (max-width:860px){.top span:first-child{display:none}.top .wrap{justify-content:center}.brand{font-size:1.08rem;gap:8px;min-width:0}.brand svg{width:40px;height:40px}.brand small{font-size:.62rem}header.site .wrap{gap:10px}.hero.home{grid-template-columns:1fr;padding-top:30px}#navb{display:block}nav.main{flex-basis:100%;display:none}nav.main.open{display:block}nav.main ul{flex-direction:column;padding-bottom:12px}form.lead{grid-template-columns:1fr}.hero-ph .bd{width:72px;height:72px;right:12px;bottom:12px}}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}.pgrid img{transition:none}}
@media print{header.site,footer.site,.top,.cta,form.lead{display:none}}
"""
CSS = re.sub(r"\n+", "", CSS.strip())

LOGO = re.sub(r"<svg ", '<svg width="46" height="46" aria-hidden="true" ', (ROOT / "static" / "img" / "icon.svg").read_text(encoding="utf-8"), count=1).replace(' xmlns="http://www.w3.org/2000/svg"', "")

LAYERS_SVG = '<svg class="layers" viewBox="0 0 420 330" role="img" aria-labelledby="lyT lyD"><title id="lyT">Cross-section of an artificial turf system on Central Florida sandy soil</title><desc id="lyD">From top to bottom: turf blades with infill, perforated backing, a washed crushed-rock base two to four inches deep, a weed barrier, and native fine sand graded to drain.</desc><rect width="420" height="330" rx="18" fill="#F1E7D2"/><g stroke="#1E5A47" stroke-width="3" stroke-linecap="round">' + "".join(f'<path d="M{x} 96l{(-5 if i % 2 else 5)} -{34 + (i * 7) % 16}"/>' for i, x in enumerate(range(34, 392, 11))) + '</g><rect x="24" y="92" width="372" height="16" fill="#C9B384"/><rect x="24" y="108" width="372" height="9" fill="#123A2E"/><rect x="24" y="117" width="372" height="92" fill="#B9B2A3"/><g fill="#8E8778">' + "".join(f'<circle cx="{40 + (i * 37) % 350}" cy="{128 + (i * 23) % 72}" r="{3 + i % 3}"/>' for i in range(34)) + '</g><rect x="24" y="209" width="372" height="5" fill="#3B3B3B"/><rect x="24" y="214" width="372" height="92" rx="0" fill="#E6D3A3"/><g fill="#CDB77F">' + "".join(f'<circle cx="{34 + (i * 29) % 360}" cy="{224 + (i * 17) % 74}" r="1.6"/>' for i in range(60)) + '</g><g><rect x="250" y="40" width="150" height="22" rx="11" fill="#FFFDF8"/><text x="262" y="55">Blades + infill</text><rect x="250" y="122" width="150" height="22" rx="11" fill="#FFFDF8"/><text x="262" y="137">Washed crushed rock</text><rect x="250" y="224" width="150" height="22" rx="11" fill="#FFFDF8"/><text x="262" y="239">Native fine sand</text></g></svg>'

NAV = [("/services/", "Services"), ("/artificial-turf-cost/", "Cost"), ("/areas/", "Areas"), ("/laws/", "Laws & HOA"), ("/blog/", "Blog"), ("/faq/", "FAQ"), ("/gallery/", "Photos"), ("/about/", "About"), ("/contact/", "Contact")]


def _date_h(iso):
    d = datetime.date.fromisoformat(iso)
    return d.strftime("%B %d, %Y").replace(" 0", " ")


# ---------------------------------------------------------------- photos
HERO_SIZES = "(max-width:860px) calc(100vw - 40px), 444px"
BADGE_HTML = ('<div class="badge"><img src="/static/img/logo-badge.webp" srcset="/static/img/logo-badge-320.webp 320w, /static/img/logo-badge-480.webp 480w, /static/img/logo-badge.webp 640w" '
              'sizes="(max-width:860px) 240px, 360px" width="640" height="640" alt="Kissimmee Artificial Turf logo: grass blades inside a green ring, established 2024" fetchpriority="high" decoding="async"></div>')


def _page_photo(p):
    return p.get("image") or p.get("hero_photo")


def _og_abs(p):
    pid = _page_photo(p)
    return BASE_URL + (_purl(pid, kind="og") if pid else "/static/img/og.jpg")


def _og_alt(p):
    pid = _page_photo(p) or PHOTO_ORDER[0]
    return _pinfo(pid)["alt"] + " (Kissimmee Artificial Turf)"


def image_node(pid):
    d = _pinfo(pid)
    return {"@type": "ImageObject", "@id": f"{BASE_URL}/gallery/#{pid}", "contentUrl": BASE_URL + _purl(pid), "url": BASE_URL + _purl(pid),
            "name": d["name"], "description": d["alt"], "width": d["w"], "height": d["h"], "encodingFormat": "image/webp",
            "thumbnailUrl": BASE_URL + _purl(pid, 480, thumb=True), "creator": {"@id": BASE_URL + "/#business"}, "creditText": PUBLIC_NAME,
            "copyrightNotice": f"© {datetime.date.today().year} {PUBLIC_NAME}"}


def _hero_srcset(pid):
    return ", ".join(f"{_purl(pid, w, thumb=True)} {w}w" for w in _pinfo(pid)["thumbs"])


def _hero_art(p):
    pid = p.get("hero_photo")
    if not pid:
        return BADGE_HTML
    return (f'<div class="hero-ph"><img src="{_purl(pid, 672, thumb=True)}" srcset="{_hero_srcset(pid)}" sizes="{HERO_SIZES}" width="672" height="504" '
            f'alt="{esc(_pinfo(pid)["alt"])}" fetchpriority="high" decoding="async">'
            f'<img class="bd" src="/static/img/logo-badge-192.webp" width="192" height="192" alt="" loading="lazy" decoding="async"></div>')


def _preload(p):
    pid = p.get("hero_photo")
    if not pid:
        return ""
    return f'\n<link rel="preload" as="image" imagesrcset="{_hero_srcset(pid)}" imagesizes="{HERO_SIZES}" fetchpriority="high">'


def business_node(full=False):
    n = {"@type": "HomeAndConstructionBusiness", "@id": BASE_URL + "/#business", "name": PUBLIC_NAME, "url": BASE_URL + "/", "telephone": PHONE_E164, "email": EMAIL,
         "additionalType": "https://en.wikipedia.org/wiki/Artificial_turf",
         "address": {"@type": "PostalAddress", "addressLocality": "Kissimmee", "addressRegion": "FL", "addressCountry": "US"},
         "foundingDate": "2024", "founder": {"@type": "Person", "@id": BASE_URL + "/about/#luis-austin", "name": OWNER, "jobTitle": OWNER_ROLE}}
    if full:
        n["description"] = BUSINESS["blurb"]
        n["logo"] = BASE_URL + "/static/img/logo-512.png"
        n["image"] = [BASE_URL + "/static/img/og.jpg"] + [BASE_URL + _purl(pid, kind="og") for pid in PHOTO_ORDER[1:5]]
        n["areaServed"] = [_city_node(s) for s in CITY_ORDER if CITIES[s]["tier"] == 1] + [{"@type": "AdministrativeArea", "name": COUNTIES[c]["name"] + ", Florida"} for c in COUNTY_ORDER]
        n["knowsAbout"] = ["Artificial turf", "Synthetic grass installation", "Pet turf", "Putting greens", "Playground surfacing", "Turf infill", "Florida HB 683 synthetic turf rules"]
        n["hasOfferCatalog"] = {"@type": "OfferCatalog", "name": "Artificial turf services", "itemListElement": [
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": SERVICES[k]["name"], "url": BASE_URL + SERVICES[k]["route"]}} for k in SERVICE_ORDER]}
    return n


def _city_node(slug):
    c = CITIES[slug]
    n = {"@type": "City" if c["kind"] in ("city", "town") else "Place", "name": f"{c['name']}, Florida"}
    if WIKI.get(slug):
        n["sameAs"] = WIKI[slug]
    return n


def jsonld(p):
    url = BASE_URL + p["route"]
    g = [business_node(full=(p["kind"] == "home"))]
    if p["kind"] == "home":
        g.append({"@type": "WebSite", "@id": BASE_URL + "/#website", "url": BASE_URL + "/", "name": PUBLIC_NAME, "publisher": {"@id": BASE_URL + "/#business"}, "inLanguage": "en-US"})
    wp = {"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": p["title"], "description": p["meta"], "inLanguage": "en-US",
          "isPartOf": {"@id": BASE_URL + "/#website"}, "about": {"@id": BASE_URL + "/#business"}, "dateModified": p.get("_lastmod", REVIEWED), "datePublished": p.get("published", LAUNCH_DATE)}
    if p.get("wp_type"):
        wp["@type"] = p["wp_type"]
    pid = _page_photo(p)
    if pid:
        wp["primaryImageOfPage"] = image_node(pid)
    g.append(wp)
    crumbs = [("Home", "/")] + list(p.get("crumbs") or [])
    if p["route"] != "/":
        crumbs.append((p.get("crumb") or p["h1"], p["route"]))
        g.append({"@type": "BreadcrumbList", "@id": url + "#breadcrumb", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": re.sub("<[^>]+>", "", n), "item": BASE_URL + r} for i, (n, r) in enumerate(crumbs)]})
    if p["kind"] in ("service", "cityservice") and p.get("service"):
        s = SERVICES[p["service"]]
        node = {"@type": "Service", "@id": url + "#service", "name": p["h1"], "serviceType": s["name"], "url": url, "provider": {"@id": BASE_URL + "/#business"}, "description": p["meta"]}
        if p.get("city"):
            node["areaServed"] = _city_node(p["city"])
        else:
            node["areaServed"] = [_city_node(c) for c in CITY_ORDER if CITIES[c]["tier"] == 1]
        if pid:
            node["image"] = {"@id": f"{BASE_URL}/gallery/#{pid}"}
        g.append(node)
    if p["kind"] == "post":
        g.append({"@type": "BlogPosting", "@id": url + "#article", "headline": p["h1"], "description": p["meta"], "url": url, "mainEntityOfPage": {"@id": url + "#webpage"},
                  "datePublished": p.get("published", LAUNCH_DATE), "dateModified": p.get("_lastmod", REVIEWED), "inLanguage": "en-US",
                  "author": {"@type": "Person", "@id": BASE_URL + "/about/#luis-austin", "name": OWNER, "jobTitle": OWNER_ROLE, "url": BASE_URL + "/about/"},
                  "publisher": {"@id": BASE_URL + "/#business"}, "image": _og_abs(p)})
    if p.get("faqs") and not p.get("faq_schema_off"):
        g.append({"@type": "FAQPage", "@id": url + "#faq", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"\s+", " ", re.sub("<[^>]+>", "", ans)).strip()}} for q, ans in p["faqs"]]})
    for extra in p.get("schema") or []:
        g.append(extra)
    return json.dumps({"@context": "https://schema.org", "@graph": g}, ensure_ascii=False, separators=(",", ":"))


def lead_form(p):
    svc_opts = "".join(f'<option{" selected" if p.get("service") == k else ""}>{esc(SERVICES[k]["name"])}</option>' for k in SERVICE_ORDER)
    city_opts = "".join(f'<option{" selected" if p.get("city") == s else ""}>{esc(CITIES[s]["name"])}</option>' for s in sorted(CITIES, key=lambda x: CITIES[x]["name"]))
    return f"""<form class="lead" method="post" action="https://api.web3forms.com/submit" id="quote">
<input type="hidden" name="access_key" value="{esc(WEB3FORMS_KEY)}"><input type="hidden" name="subject" value="[{esc(PUBLIC_NAME)}] Quote request"><input type="hidden" name="from_name" value="{esc(PUBLIC_NAME)} website"><input type="hidden" name="redirect" value="{BASE_URL}/thank-you/"><input type="hidden" name="page_url" value="">
<div><label for="f-name">Name</label><input id="f-name" name="name" autocomplete="name" required></div>
<div><label for="f-phone">Phone</label><input id="f-phone" name="phone" type="tel" autocomplete="tel" inputmode="tel" required></div>
<div><label for="f-email">Email</label><input id="f-email" name="email" type="email" autocomplete="email"></div>
<div><label for="f-city">City</label><select id="f-city" name="city"><option value="">Choose…</option>{city_opts}<option>Somewhere else</option></select></div>
<div><label for="f-service">What do you need?</label><select id="f-service" name="service"><option value="">Choose…</option>{svc_opts}</select></div>
<div><label for="f-size">Approximate area</label><select id="f-size" name="size"><option value="">Not sure yet</option><option>Under 300 sq ft</option><option>300–600 sq ft</option><option>600–1,000 sq ft</option><option>1,000–2,000 sq ft</option><option>Over 2,000 sq ft</option></select></div>
<div><label for="f-pets">Dogs using the yard?</label><select id="f-pets" name="pets"><option value="">Choose…</option><option>Yes</option><option>No</option></select></div>
<div><label for="f-hoa">HOA or ARC approval needed?</label><select id="f-hoa" name="hoa"><option value="">Not sure</option><option>Yes</option><option>No</option></select></div>
<div class="full"><label for="f-msg">Anything we should know?</label><textarea id="f-msg" name="message" placeholder="Sun or shade, drainage trouble, gate width, timing…"></textarea></div>
<div class="full"><label class="ck" for="f-ok"><input id="f-ok" type="checkbox" name="consent" value="yes" required><span>I agree that {esc(PUBLIC_NAME)} may call, text or email me about this request. Message and data rates may apply. Consent is not a condition of purchase. See the <a href="/privacy/">privacy policy</a>.</span></label></div>
<div class="hp" aria-hidden="true"><label for="f-hp">Leave this empty</label><input id="f-hp" type="checkbox" name="botcheck" tabindex="-1" autocomplete="off"></div>
<div class="full"><button class="btn" type="submit">Request my quote</button></div>
</form>"""


def _header(p):
    nav = "".join(f'<li><a href="{r}"{" aria-current=\"page\"" if p["route"] == r else ""}>{t}</a></li>' for r, t in NAV)
    return f"""<a class="skip" href="#main">Skip to content</a>
<div class="top"><div class="wrap"><span>Artificial turf installers serving Kissimmee &amp; Central Florida</span><span>Call or text <a href="tel:{PHONE_E164}">{PHONE_DISPLAY}</a></span></div></div>
<header class="site"><div class="wrap"><a class="brand" href="/">{LOGO}<span>{esc(PUBLIC_NAME)}<small>Est. 2024 · Kissimmee, FL</small></span></a>
<button id="navb" type="button" aria-expanded="false" aria-controls="nav">Menu</button>
<nav class="main" id="nav" aria-label="Main"><ul>{nav}</ul></nav></div></header>"""


def _footer():
    sv = "".join(f'<li><a href="{SERVICES[k]["route"]}">{esc(SERVICES[k]["name"])}</a></li>' for k in SERVICE_ORDER)
    t1 = "".join(f'<li><a href="{CITIES[s]["route"]}">{esc(CITIES[s]["name"])}</a></li>' for s in CITY_ORDER if CITIES[s]["tier"] == 1)
    co = "".join(f'<li><a href="{COUNTIES[c]["route"]}">{esc(COUNTIES[c]["name"])}</a></li>' for c in COUNTY_ORDER)
    return f"""<footer class="site"><div class="wrap"><div class="fg">
<div><h2>{esc(PUBLIC_NAME)}</h2><p>Artificial grass installation, repair and cleaning. Based in Kissimmee, Florida, working across Osceola, Orange, Polk, Lake and Seminole counties.</p><p><a href="tel:{PHONE_E164}">{PHONE_DISPLAY}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a></p></div>
<div><h2>Services</h2><ul>{sv}</ul></div>
<div><h2>Close to Kissimmee</h2><ul>{t1}</ul></div>
<div><h2>Counties</h2><ul>{co}<li><a href="/areas/">All service areas</a></li></ul><h2 style="margin-top:1.4em">Resources</h2><ul><li><a href="/artificial-turf-cost/">Turf cost guide</a></li><li><a href="/laws/">Florida turf laws &amp; HOAs</a></li><li><a href="/compare/">Comparisons</a></li><li><a href="/tools/">Calculators</a></li><li><a href="/faq/">FAQ</a></li><li><a href="/blog/">Blog</a></li><li><a href="/gallery/">Project photos</a></li></ul></div>
</div><p class="legal">© {datetime.date.today().year} {esc(PUBLIC_NAME)} · Kissimmee, FL · <a href="/privacy/">Privacy</a> · <a href="/terms/">Terms</a> · <a href="/accessibility/">Accessibility</a> · <a href="/sitemap.xml">Sitemap</a></p></div></footer>"""


def render_page(p):
    url = BASE_URL + p["route"]
    robots = "noindex,follow" if p.get("noindex") else "index,follow,max-image-preview:large,max-snippet:-1"
    crumbs_html = ""
    if p["route"] != "/" and p["kind"] != "plain":
        items = [("Home", "/")] + list(p.get("crumbs") or [])
        lis = "".join(f'<li><a href="{r}">{n}</a></li>' for n, r in items) + f'<li aria-current="page">{p.get("crumb") or p["h1"]}</li>'
        crumbs_html = f'<nav class="crumbs wrap" aria-label="Breadcrumb"><ol>{lis}</ol></nav>'
    faq_html = ""
    if p.get("faqs"):
        faq_html = '<section class="faq" id="faq"><h2>' + esc(p.get("faq_title") or "Questions people ask") + "</h2>" + "".join(f"<h3>{esc(q)}</h3><p>{ans}</p>" if not ans.lstrip().startswith("<p") else f"<h3>{esc(q)}</h3>{ans}" for q, ans in p["faqs"]) + "</section>"
    rel_html = ""
    if p.get("related"):
        rel_html = '<aside class="rel"><h2>' + esc(p.get("related_title") or "Keep reading") + "</h2><ul>" + "".join(f'<li><a href="{r}">{t}</a></li>' for r, t in p["related"]) + "</ul></aside>"
    src_html = ""
    if p.get("sources"):
        src_html = '<div class="src"><h2>Sources</h2><ul>' + "".join(f'<li><a href="{esc(SOURCES[s][1])}" rel="noopener">{esc(SOURCES[s][0])}</a></li>' if isinstance(s, str) else f'<li><a href="{esc(s[1])}" rel="noopener">{esc(s[0])}</a></li>' for s in p["sources"]) + "</ul></div>"
    by = ""
    if p["kind"] not in ("home", "plain", "page", "index") or p.get("author"):
        by = f'<p class="by">Reviewed by <a href="/about/">{esc(OWNER)}</a>, {esc(OWNER_ROLE.lower())} · Last reviewed {_date_h(p.get("_lastmod", REVIEWED))}</p>'
    form_html = ""
    if p.get("form", p["kind"] in ("home", "service", "cityservice", "city", "price")):
        form_html = f'<section id="get-quote" class="auto"><h2>{esc(p.get("form_title") or "Tell us about the yard")}</h2><p>Send the basics and we call back to set a time to measure. Prefer to talk? Call or text <a href="tel:{PHONE_E164}">{PHONE_DISPLAY}</a>.</p>{lead_form(p)}</section>'
    if p["kind"] == "home":
        hero = f'<div class="wrap"><div class="hero home"><div><p class="eyebrow">{esc(p.get("eyebrow", ""))}</p><h1>{p["h1"]}</h1>{p["lede"]}<div class="hero-cta"><a class="btn" href="#get-quote">Get a measured quote</a><a class="btn alt" href="tel:{PHONE_E164}">Call {PHONE_DISPLAY}</a></div></div>{_hero_art(p)}</div></div>'
        narrow = ""
    else:
        eb = f'<p class="eyebrow">{esc(p["eyebrow"])}</p>' if p.get("eyebrow") else ""
        hero = f'{crumbs_html}<div class="wrap narrow"><div class="hero">{eb}<h1>{p["h1"]}</h1>{p["lede"]}{by}</div></div>'
        narrow = " narrow"
    wide = "" if p.get("wide") else narrow
    main = f'<main id="main">{hero}<div class="wrap{wide}">{p["body"]}{faq_html}{form_html}{rel_html}{src_html}</div></main>'
    og_type = "article" if p["kind"] == "post" else "website"
    return f"""<!doctype html>
<html lang="en-US"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(p["title"])}</title><meta name="description" content="{esc(p["meta"])}"><meta name="robots" content="{robots}"><link rel="canonical" href="{url}">
<link rel="preload" href="/static/fonts/dm-serif-display-latin.woff2" as="font" type="font/woff2" crossorigin>{_preload(p)}
<meta property="og:type" content="{og_type}"><meta property="og:site_name" content="{esc(PUBLIC_NAME)}"><meta property="og:title" content="{esc(p["title"])}"><meta property="og:description" content="{esc(p["meta"])}"><meta property="og:url" content="{url}"><meta property="og:image" content="{_og_abs(p)}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="{esc(_og_alt(p))}"><meta property="og:locale" content="en_US"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.ico" sizes="32x32"><link rel="icon" href="/static/img/icon.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="/static/img/apple-touch-icon.png"><link rel="manifest" href="/site.webmanifest"><meta name="theme-color" content="#0B4A18">
<link rel="alternate" type="application/rss+xml" title="{esc(PUBLIC_NAME)} blog" href="/feed.xml">
<style>{CSS}</style><noscript><style>nav.main{{display:block}}#navb{{display:none}}</style></noscript>
<script type="application/ld+json">{jsonld(p)}</script>
<script src="{SITE_JS}" defer></script>
</head><body>
{_header(p)}
{main}
{_footer()}
</body></html>"""
