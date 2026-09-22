# -*- coding: utf-8 -*-
"""Check one content module in memory (safe to run while other modules are being written).
Usage: python qa/check_module.py c_services_a [c_other ...]"""
import html as htmlmod
import importlib
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "site"))
sys.path.insert(0, str(ROOT / "site" / "content"))
sys.path.insert(0, str(ROOT / "qa"))
from templates import render_page  # noqa: E402
from qa_all import BANNED, INTERNAL, TRACK, MIN_WORDS, main_text  # noqa: E402
from _data import REVIEWED  # noqa: E402

problems = 0
for name in sys.argv[1:]:
    mod = importlib.import_module(name)
    pages = mod.get_pages()
    print(f"== {name}: {len(pages)} page(s)")
    seen_sent = {}
    for p in pages:
        p.setdefault("_lastmod", REVIEWED)
        h = render_page(p)
        txt = main_text(h)
        low = txt.lower()
        words = len(txt.split())
        issues = []
        if len(p["title"]) > 65:
            issues.append(f"title {len(p['title'])} chars")
        if not 110 <= len(p["meta"]) <= 165 and not p.get("noindex"):
            issues.append(f"meta {len(p['meta'])} chars")
        if p["title"].strip().lower() == re.sub('<[^>]+>', '', p["h1"]).strip().lower():
            issues.append("H1 equals title")
        need = MIN_WORDS.get(p["kind"])
        if need and words < need:
            issues.append(f"words {words} < {need}")
        lede_words = len(re.sub("<[^>]+>", " ", p["lede"]).split())
        if p["kind"] not in ("page", "plain", "index") and not 35 <= lede_words <= 80:
            issues.append(f"capsule {lede_words} words (want 40-70)")
        for b in BANNED + INTERNAL + TRACK:
            if re.search(r"(?<![a-z])" + re.escape(b) + r"(?![a-z])", low):
                issues.append(f"banned '{b}'")
        if low.count("ensure") > 1:
            issues.append(f"'ensure' x{low.count('ensure')}")
        if re.search(r"\{(svc|city|county|cs|post|a|ext|src|price|tel)\(", txt):
            issues.append("unrendered helper call")
        if "!" in txt:
            issues.append("exclamation mark")
        if txt.count("—") > 2:
            issues.append(f"em dashes x{txt.count('—')}")
        nb = len(re.findall(r"\bbest\b", low))
        if nb > 3 and "best" not in p["route"]:
            issues.append(f"'best' x{nb}")
        internal = set(re.findall(r'href="(/[^"#?]*)', re.search(r"<main.*?</main>", h, flags=re.S).group(0)))
        if len(internal) < 5 and p["kind"] not in ("plain", "page", "index"):
            issues.append(f"only {len(internal)} internal links in main")
        for blob in re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, flags=re.S):
            json.loads(blob)
        for s in re.split(r"(?<=[.?])\s+", txt):
            s2 = re.sub(r"[^a-z0-9 ]", "", s.lower()).strip()
            if len(s2.split()) >= 8:
                if s2 in seen_sent and seen_sent[s2] != p["route"]:
                    issues.append(f"sentence repeated from {seen_sent[s2]}: \"{s2[:60]}\"")
                seen_sent.setdefault(s2, p["route"])
        kb = len(h.encode()) / 1024
        flag = "OK " if not issues else "FIX"
        problems += len(issues)
        print(f"{flag} {p['route']:<62} {words:>5} w {kb:>5.0f} KB  " + "; ".join(issues[:6]))
print(f"\n{problems} issue(s)")
sys.exit(1 if problems else 0)
