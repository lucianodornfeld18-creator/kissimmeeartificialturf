# -*- coding: utf-8 -*-
"""Email Routing for kissimmeeartificialturf.com, same shape as grovelandconcrete.com / windermereconcrete.com:
hello@ -> the marketing inbox, plus an enabled catch-all so nothing addressed to the domain is dropped. Safe to re-run."""
import json
from cf_status import call, ZONE
DEST = "opusdigitalmarketingflorida@gmail.com"
ALIASES = ["hello", "info", "quotes"]

zid = call("GET", f"/zones?name={ZONE}")["result"][0]["id"]
rules = call("GET", f"/zones/{zid}/email/routing/rules?per_page=50").get("result") or []
have = {m.get("value") for r in rules for m in (r.get("matchers") or [])}
for local in ALIASES:
    addr = f"{local}@{ZONE}"
    if addr in have:
        print("rule exists:", addr); continue
    c = call("POST", f"/zones/{zid}/email/routing/rules", {"name": f"Forward {addr}", "enabled": True,
             "matchers": [{"type": "literal", "field": "to", "value": addr}], "actions": [{"type": "forward", "value": [DEST]}]})
    print("rule", addr, "->", DEST, "ok" if c.get("success") else json.dumps(c.get("errors"))[:200])
ca = call("PUT", f"/zones/{zid}/email/routing/rules/catch_all", {"name": "Forward all Kissimmee Artificial Turf email", "enabled": True,
          "matchers": [{"type": "all"}], "actions": [{"type": "forward", "value": [DEST]}]})
print("catch-all ->", DEST, "ok" if ca.get("success") else json.dumps(ca.get("errors"))[:200])
en = call("POST", f"/zones/{zid}/email/routing/enable", {})
print("enable:", "ok" if en.get("success") else json.dumps(en.get("errors"))[:300])
if not en.get("success"):
    dn = call("POST", f"/zones/{zid}/email/routing/dns", {})
    print("dns:", "ok" if dn.get("success") else json.dumps(dn.get("errors"))[:300])
s = call("GET", f"/zones/{zid}/email/routing").get("result") or {}
print("status: enabled=%s state=%s" % (s.get("enabled"), s.get("status")))
d = call("GET", f"/zones/{zid}/email/routing/dns")
for x in (d.get("result") or {}).get("record", []) if isinstance(d.get("result"), dict) else (d.get("result") or []):
    print("  needs/has:", x.get("type"), x.get("name"), (x.get("content") or "")[:60])
