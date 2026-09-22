# -*- coding: utf-8 -*-
"""Cross-module duplicate check: python qa/cross_check.py c_city_celebration [c_other ...]
Renders the module's pages in memory and compares them with every page already built in site/dist
that does not belong to the module. Prints shared runs of 10+ words (bank blocks excluded, since one
shared bank block per city pair is by design) and the 8-gram overlap ratio per page pair.
Exit 1 if any pair is over 12% or any run of 14+ words is shared."""
import importlib
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DIST = ROOT / "site" / "dist"
sys.path.insert(0, str(ROOT / "site"))
sys.path.insert(0, str(ROOT / "site" / "content"))
sys.path.insert(0, str(ROOT / "qa"))
from templates import render_page  # noqa: E402
from qa_all import main_text  # noqa: E402
from _data import REVIEWED  # noqa: E402


def strip_bank(h):
    h = re.sub(r'<section class="bank">.*?</section>', " ", h, flags=re.S)
    return re.sub(r'<p class="by">.*?</p>', " ", h, flags=re.S)


def words(t):
    return re.sub(r"[^a-z0-9 ]", "", t.lower()).split()


def grams(w, n=8):
    return [" ".join(w[i:i + n]) for i in range(len(w) - n + 1)]


def runs(wa, gb):
    out, cur = [], []
    for i in range(len(wa) - 7):
        g = " ".join(wa[i:i + 8])
        if g in gb:
            cur.append(i)
        elif cur:
            out.append((cur[0], cur[-1] + 8)); cur = []
    if cur:
        out.append((cur[0], cur[-1] + 8))
    return out


def main():
    mods = sys.argv[1:]
    mine, owner = {}, {}
    for name in mods:
        for p in importlib.import_module(name).get_pages():
            p.setdefault("_lastmod", REVIEWED)
            mine[p["route"]] = words(main_text(strip_bank(render_page(p))))
            owner[p["route"]] = name
    others = {}
    for f in DIST.rglob("index.html"):
        route = "/" + str(f.parent.relative_to(DIST)).replace("\\", "/").strip(".") + "/"
        route = re.sub(r"/+", "/", route)
        if route in mine:
            continue
        others[route] = words(main_text(strip_bank(f.read_text(encoding="utf-8"))))
    # pages of a different module passed in the same run are compared too (a writer given two towns must not copy between them)
    bad = 0
    for r, wa in mine.items():
        ga = grams(wa)
        pool = dict(others)
        pool.update({o: wb for o, wb in mine.items() if owner[o] != owner[r]})
        for o, wb in pool.items():
            if len(wb) < 60:
                continue
            gb = set(grams(wb))
            shared = sum(1 for g in ga if g in gb)
            if not shared:
                continue
            ratio = shared / max(1, min(len(ga), len(gb)))
            rs = [(s, e) for s, e in runs(wa, gb) if e - s >= 10]
            if ratio > 0.12 or any(e - s >= 14 for s, e in rs):
                bad += 1
                print(f"\nFIX {r}  ~  {o}   overlap {ratio:.0%}")
                for s, e in sorted(rs, key=lambda x: x[0] - x[1])[:8]:
                    print(f"   [{e - s} words] {' '.join(wa[s:s + 14])} ...")
            elif rs:
                print(f"ok  {r}  ~  {o}   overlap {ratio:.0%}, longest run {max(e - s for s, e in rs)} words")
    print(f"\n{bad} page pair(s) need rewriting" if bad else "\nno cross-module duplication found")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
