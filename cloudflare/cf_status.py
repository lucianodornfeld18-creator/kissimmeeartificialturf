# -*- coding: utf-8 -*-
"""Read-only Cloudflare status for kissimmeeartificialturf.com (zone, DNS, Email Routing, Pages)."""
import json, os, pathlib, urllib.request
ZONE = "kissimmeeartificialturf.com"
ACCOUNT_ID = "21cabe20549f2f63baa4d3fd781abe74"
API = "https://api.cloudflare.com/client/v4"

def _wrangler_token():
    cfg = pathlib.Path(os.path.expanduser("~/.wrangler/config/default.toml"))
    if cfg.exists():
        for line in cfg.read_text(encoding="utf-8").splitlines():
            if line.strip().startswith("oauth_token"):
                return line.split("=", 1)[1].strip().strip('"')
TOKENS = [t for t in (os.environ.get("CF_API_TOKEN"), _wrangler_token()) if t]

def call(method, path, body=None):
    last = None
    for tok in TOKENS:
        r = urllib.request.Request(API + path, data=json.dumps(body).encode() if body is not None else None, method=method,
                                   headers={"Authorization": "Bearer " + tok, "Content-Type": "application/json"})
        try:
            return json.loads(urllib.request.urlopen(r, timeout=60).read())
        except urllib.error.HTTPError as e:
            raw = e.read().decode()
            try: last = json.loads(raw or "{}")
            except Exception: last = {"success": False, "errors": [{"code": e.code, "message": raw[:200]}]}
            if not ({"10000", "9109", "1000"} & {str(x.get("code")) for x in (last.get("errors") or [])}):
                return last
    return last

if __name__ == "__main__":
    print("tokens:", len(TOKENS))
    z = call("GET", f"/zones?name={ZONE}")
    res = z.get("result") or []
    if not res:
        print("zone not visible:", json.dumps(z.get("errors"))[:300]); raise SystemExit(1)
    zid = res[0]["id"]
    print("zone", zid, "status", res[0]["status"], "ns", res[0].get("name_servers"))
    d = call("GET", f"/zones/{zid}/dns_records?per_page=200")
    if d.get("success"):
        for x in d["result"]:
            print("  DNS %-6s %-40s %s %s" % (x["type"], x["name"], (x.get("content") or "")[:60], "proxied" if x.get("proxied") else ""))
    else:
        print("  DNS read:", json.dumps(d.get("errors"))[:200])
    e = call("GET", f"/zones/{zid}/email/routing")
    print("email routing:", json.dumps({k: (e.get("result") or {}).get(k) for k in ("enabled", "status", "name")}) if e.get("success") else json.dumps(e.get("errors"))[:200])
    r = call("GET", f"/zones/{zid}/email/routing/rules?per_page=50")
    for x in (r.get("result") or []):
        print("  rule", x.get("name"), x.get("enabled"), [m.get("value", m.get("type")) for m in x.get("matchers", [])], [a.get("value") for a in x.get("actions", [])])
    a = call("GET", f"/accounts/{ACCOUNT_ID}/email/routing/addresses")
    for x in (a.get("result") or []):
        print("  dest", x.get("email"), "verified" if x.get("verified") else "NOT verified")
    p = call("GET", f"/accounts/{ACCOUNT_ID}/pages/projects?per_page=50")
    names = [(x["name"], (x.get("source") or {}).get("type"), x.get("domains")) for x in (p.get("result") or [])]
    print("pages projects:", len(names))
    for n in names:
        if "turf" in n[0] or "kissimmee" in n[0]:
            print("  ", n)
