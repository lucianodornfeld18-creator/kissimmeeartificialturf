# -*- coding: utf-8 -*-
"""QA over site/dist. Usage: python qa/qa_all.py [--only c_module_name] [--sim]
Exit code 1 when a FAIL-level check trips. Writes research/qa-report.txt and research/internal-links.csv."""
import csv
import html as htmlmod
import json
import pathlib
import re
import sys
from collections import Counter, defaultdict

ROOT = pathlib.Path(__file__).resolve().parent.parent
DIST = ROOT / "site" / "dist"
OUT = ROOT / "research"
OUT.mkdir(exist_ok=True)

BANNED = ["in today's", "whether you're", "whether you are", "look no further", "it's important to note", "it is important to note", "it's worth noting", "in conclusion", "ultimately,", "at the end of the day",
          "when it comes to", "elevate", "seamless", "unlock", "delve", "robust", "leverage", "game-changer", "game changer", "transform your", "dream yard", "dream backyard", "oasis", "paradise", "lush", "pristine",
          "we understand that", "our team of experts", "top-notch", "state-of-the-art", "cutting-edge", "meticulous", "comprehensive", "hassle-free", "peace of mind", "stand the test of time", "test of time",
          "a testament to", "nestled", "vibrant", "boasts", "tapestry", "one-stop shop", "we've got you covered", "utilize", "in order to", "let's dive in", "here's the thing", "say goodbye to", "second to none", "unparalleled"]
INTERNAL = ["lead generation", "lead-gen", "sister brand", "sister site", "partner contractor", "hub_id", "owner input", "owner-inputs", "pending:", "todo", "placeholder", "lorem", "keyword", "search volume",
            "answer engine", "tier 1", "tier 2", "tier 3", "8-gram", "similarity", "benchmark", "word count", "autocomplete", "keyword planner", "pipeline", "rank-and-rent", "seo"]
TRACK = ["most of our", "many of our", "our customers", "our clients", "we've installed", "we have installed", "we've built", "we have built", "we've done", "our jobs", "our calls", "our crews have", "years of experience", "hundreds of", "dozens of jobs", "dozens of yards", "our track record", "our portfolio", "slice of our"]
MIN_WORDS = {"home": 3800, "service": 1800, "cityservice": 900, "city": 700, "county": 1200, "price": 2000, "law": 900, "permit": 700, "post": 1200, "compare": 1000, "faq": 1000}

kinds = {}
try:
    for row in csv.DictReader(open(OUT / "titles-metas.csv", encoding="utf-8")):
        kinds[row["route"]] = row["kind"]
except FileNotFoundError:
    pass


def main_text(h):
    m = re.search(r"<main.*?</main>", h, flags=re.S)
    t = m.group(0) if m else h
    t = re.sub(r"<script.*?</script>|<style.*?</style>|<form.*?</form>|<nav.*?</nav>|<div class=\"src\">.*?</div>|<aside class=\"rel\">.*?</aside>|<section[^>]*class=\"auto\".*?</section>", " ", t, flags=re.S)
    t = re.sub(r"<[^>]+>", " ", t)
    return htmlmod.unescape(re.sub(r"\s+", " ", t)).strip()


def main():
    do_sim = "--sim" in sys.argv
    pages = {}
    for f in DIST.rglob("index.html"):
        route = "/" + str(f.parent.relative_to(DIST)).replace("\\", "/").strip(".") + "/"
        route = re.sub(r"/+", "/", route)
        pages[route] = f.read_text(encoding="utf-8")
    fails, warns = [], []
    titles, h1s, metas = defaultdict(list), defaultdict(list), defaultdict(list)
    inlinks = Counter()
    outlinks = {}
    texts = {}
    for route, h in pages.items():
        kind = kinds.get(route, "")
        t = re.search(r"<title>(.*?)</title>", h, flags=re.S).group(1)
        m = re.search(r'<meta name="description" content="(.*?)"', h, flags=re.S).group(1)
        h1 = re.findall(r"<h1[^>]*>(.*?)</h1>", h, flags=re.S)
        if len(h1) != 1:
            fails.append(f"H1 count {len(h1)}: {route}")
        titles[htmlmod.unescape(t)].append(route); metas[m].append(route)
        if h1:
            h1s[re.sub("<[^>]+>", "", h1[0])].append(route)
        tl = len(htmlmod.unescape(t))
        if tl > 65:
            warns.append(f"title {tl} chars: {route}")
        ml = len(htmlmod.unescape(m))
        if (ml < 110 or ml > 165) and "noindex" not in h[:1500]:
            warns.append(f"meta {ml} chars: {route}")
        if len(h.encode()) > 150 * 1024:
            fails.append(f"HTML {len(h.encode()) // 1024} KB > 150: {route}")
        for blob in re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, flags=re.S):
            try:
                json.loads(blob)
            except Exception as e:
                fails.append(f"JSON-LD invalid ({e}): {route}")
        txt = main_text(h)
        texts[route] = txt
        low = txt.lower()
        words = len(txt.split())
        if kind in MIN_WORDS and words < MIN_WORDS[kind]:
            warns.append(f"words {words} < {MIN_WORDS[kind]} ({kind}): {route}")
        for b in BANNED:
            if re.search(r"(?<![a-z])" + re.escape(b) + r"(?![a-z])", low):
                fails.append(f"banned phrase '{b}': {route}")
        for b in INTERNAL:
            if re.search(r"(?<![a-z])" + re.escape(b) + r"(?![a-z])", low):
                fails.append(f"internal term '{b}': {route}")
        for b in TRACK:
            if re.search(r"(?<![a-z])" + re.escape(b) + r"(?![a-z])", low):
                fails.append(f"track-record claim '{b}': {route}")
        if low.count("ensure") > 1:
            warns.append(f"'ensure' x{low.count('ensure')}: {route}")
        if "!" in re.sub(r"<[^>]+>", "", txt):
            warns.append(f"exclamation mark: {route}")
        if txt.count("—") > 2:
            warns.append(f"em dashes x{txt.count('—')}: {route}")
        nb = len(re.findall(r"\bbest\b", low))
        if nb > 3 and "best" not in route:
            warns.append(f"'best' x{nb}: {route}")
        for ph in ("artificial turf", "artificial grass"):
            c = low.count(ph)
            if words and c * 2 / words > 0.035:
                warns.append(f"density '{ph}' {c * 2 / words:.1%}: {route}")
        body = re.search(r"<main.*?</main>", h, flags=re.S).group(0)
        links = set()
        for href in re.findall(r'href="(/[^"#?]*)', h):
            if href.startswith("/static/") or re.search(r"\.(xml|txt|ico|png|svg|webmanifest|js)$", href):
                continue
            links.add(href if href.endswith("/") else href + "/")
        outlinks[route] = links
        for href in set(re.findall(r'href="(/[^"#?]*)', body)):
            href = href if href.endswith("/") else href + "/"
            if href != route and not href.startswith("/static/"):
                inlinks[href] += 1
    for route, links in outlinks.items():
        for l in links:
            if l not in pages:
                fails.append(f"broken link {l} on {route}")
    for label, d in (("title", titles), ("h1", h1s), ("meta", metas)):
        for k, v in d.items():
            if len(v) > 1:
                fails.append(f"duplicate {label} '{k[:70]}': {', '.join(v[:4])}")
    with open(OUT / "internal-links.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(["route", "kind", "inlinks_from_main", "outlinks"])
        for r in sorted(pages):
            w.writerow([r, kinds.get(r, ""), inlinks[r], len(outlinks[r])])
            if inlinks[r] < 3 and r not in ("/", "/thank-you/", "/404/") and kinds.get(r) not in ("plain",):
                warns.append(f"inlinks {inlinks[r]} < 3: {r}")
    # repeated sentences across pages
    sent_pages = defaultdict(set)
    for r, txt in texts.items():
        for s in re.split(r"(?<=[.?!])\s+", txt):
            s2 = re.sub(r"[^a-z0-9 ]", "", s.lower()).strip()
            if len(s2.split()) >= 8:
                sent_pages[s2].add(r)
    rep = sorted(((len(v), k, sorted(v)[:3]) for k, v in sent_pages.items() if len(v) > 1), reverse=True)
    for n, s, where in rep[:40]:
        warns.append(f"sentence on {n} pages: \"{s[:90]}\" e.g. {where}")
    if do_sim:
        # Two measures: (a) writer text only (bank blocks stripped) -> FAIL over 15%; (b) everything the reader sees -> WARN over 15%.
        def gramset(t):
            w = re.sub(r"[^a-z0-9 ]", "", t.lower()).split()
            return {hash(" ".join(w[i:i + 8])) for i in range(len(w) - 7)}
        own = {r: gramset(main_text(re.sub(r'<section class="bank">.*?</section>', " ", pages[r], flags=re.S))) for r in pages}
        full = {r: gramset(txt) for r, txt in texts.items()}
        rs = [r for r in full if len(full[r]) > 200]
        worst, raw = [], []
        for i, a in enumerate(rs):
            for b in rs[i + 1:]:
                inter = len(full[a] & full[b])
                if not inter:
                    continue
                o = inter / min(len(full[a]), len(full[b]))
                if o > 0.15:
                    raw.append((o, a, b))
                    io = len(own[a] & own[b]) / max(1, min(len(own[a]), len(own[b])))
                    if io > 0.15:
                        worst.append((io, a, b))
        for o, a, b in sorted(worst, reverse=True)[:60]:
            fails.append(f"8-gram overlap {o:.0%} (writer text): {a} ~ {b}")
        for o, a, b in sorted(raw, reverse=True)[:60]:
            warns.append(f"8-gram overlap {o:.0%} incl. shared bank blocks: {a} ~ {b}")
        print(f"[qa] pairs over 15% including bank blocks: {len(raw)}")
        print(f"[qa] similarity pairs over 15%: {len(worst)}")
    rep_txt = [f"pages: {len(pages)}", f"FAIL: {len(fails)}", f"WARN: {len(warns)}", ""] + ["FAIL  " + x for x in fails] + [""] + ["WARN  " + x for x in warns]
    (OUT / "qa-report.txt").write_text("\n".join(rep_txt), encoding="utf-8")
    only = None
    if "--only" in sys.argv:
        only = sys.argv[sys.argv.index("--only") + 1]
    shown = [x for x in rep_txt if (only is None or only in x or x.startswith(("pages", "FAIL:", "WARN:")))]
    print("\n".join(shown[:140]))
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
