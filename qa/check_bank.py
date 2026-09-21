# -*- coding: utf-8 -*-
"""Check block-bank files: python qa/check_bank.py b_residential [b_pet ...]"""
import importlib
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "site" / "bank"))
sys.path.insert(0, str(ROOT / "qa"))
from qa_all import BANNED, INTERNAL  # noqa: E402

KEYS = ["base", "product", "process", "risks", "care"]
problems = 0
seen = {}
for name in sys.argv[1:]:
    B = importlib.import_module(name).BLOCKS
    print(f"== {name}")
    for k in KEYS:
        vs = B.get(k) or []
        if len(vs) != 5:
            print(f"FIX {k}: {len(vs)} variants (want 5)"); problems += 1
        h2s = [h for h, _ in vs]
        if len(set(h2s)) != len(h2s):
            print(f"FIX {k}: duplicate H2"); problems += 1
        for i, (h2, html) in enumerate(vs):
            txt = re.sub(r"<[^>]+>", " ", html); low = (h2 + " " + txt).lower(); n = len(txt.split()); issues = []
            if not 75 <= n <= 130:
                issues.append(f"{n} words (want 80-120)")
            if "{city}" not in html and "{city}" not in h2:
                issues.append("no {city}")
            for b in BANNED + INTERNAL:
                if re.search(r"(?<![a-z])" + re.escape(b) + r"(?![a-z])", low):
                    issues.append(f"banned '{b}'")
            if "!" in txt or "$" in txt and not re.search(r"\$\d", txt):
                issues.append("punctuation")
            for s in re.split(r"(?<=[.?])\s+", txt):
                s2 = re.sub(r"[^a-z0-9 ]", "", s.lower()).strip()
                if len(s2.split()) >= 8:
                    if s2 in seen:
                        issues.append(f"sentence repeats {seen[s2]}")
                    seen[s2] = f"{name}.{k}[{i}]"
            problems += len(issues)
            print(("OK " if not issues else "FIX"), f"{k}[{i}] {n:>3} w  {h2[:60]:<60} " + "; ".join(issues[:4]))
print(f"\n{problems} issue(s)")
sys.exit(1 if problems else 0)
