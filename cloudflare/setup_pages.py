# -*- coding: utf-8 -*-
"""Create the git-connected Cloudflare Pages project for kissimmeeartificialturf.com and attach the apex and www.
Safe to re-run. Pages serves the committed site/dist (no build command). Deploy = push to main."""
import json
import sys
import time

from cf_status import call, ZONE, ACCOUNT_ID

PROJECT = "kissimmeeartificialturf"
OWNER, REPO = "lucianodornfeld18-creator", "kissimmeeartificialturf"


def errs(r):
    return json.dumps((r or {}).get("errors"))[:300]


def main():
    base = f"/accounts/{ACCOUNT_ID}/pages/projects"
    got = call("GET", f"{base}/{PROJECT}")
    if got.get("success"):
        print("project exists:", got["result"].get("subdomain"), "source:", (got["result"].get("source") or {}).get("type"))
    else:
        body = {"name": PROJECT, "production_branch": "main",
                "build_config": {"build_command": "", "destination_dir": "site/dist", "root_dir": ""},
                "source": {"type": "github", "config": {"owner": OWNER, "repo_name": REPO, "production_branch": "main", "pr_comments_enabled": False,
                                                        "deployments_enabled": True, "production_deployments_enabled": True, "preview_deployment_setting": "none"}}}
        r = call("POST", base, body)
        if not r.get("success"):
            print("create failed:", errs(r))
            return 1
        print("created:", r["result"].get("subdomain"))
    # first production deployment from main
    d = call("POST", f"{base}/{PROJECT}/deployments", None)
    print("trigger deployment:", "ok" if (d or {}).get("success") else errs(d))
    for host in (ZONE, "www." + ZONE):
        r = call("POST", f"{base}/{PROJECT}/domains", {"name": host})
        print("attach %-32s %s" % (host, "ok" if r.get("success") else errs(r)[:160]))
    for _ in range(20):
        time.sleep(15)
        dom = call("GET", f"{base}/{PROJECT}/domains").get("result") or []
        dep = (call("GET", f"{base}/{PROJECT}/deployments?per_page=1").get("result") or [{}])[0]
        stage = (dep.get("latest_stage") or {})
        print("  domains:", " | ".join(f"{x['name']}={x.get('status')}" for x in dom), "| deploy:", stage.get("name"), stage.get("status"))
        if dom and all(x.get("status") == "active" for x in dom) and stage.get("status") == "success":
            break
    return 0


if __name__ == "__main__":
    sys.exit(main())
