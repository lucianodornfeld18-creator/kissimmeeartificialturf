# -*- coding: utf-8 -*-
"""Real-browser test of the lead form on a deployed URL. Blocks only the CRM mirror so no fake lead is created there.
Usage: python qa/form_test.py https://kissimmeeartificialturf.pages.dev"""
import asyncio
import sys

from playwright.async_api import async_playwright

BASE = sys.argv[1].rstrip("/")


async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        ctx = await b.new_context()
        mirrored = []
        await ctx.route("**/opera-portal.lucianodornfeld18.workers.dev/**", lambda r: (mirrored.append(r.request.post_data or ""), asyncio.ensure_future(r.abort()))[1])
        pg = await ctx.new_page()
        errors = []
        pg.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
        await pg.goto(BASE + "/contact/")
        await pg.fill("#f-name", "TESTE automatico do site (pode apagar)")
        await pg.fill("#f-phone", "4075550100")
        await pg.fill("#f-email", "teste@kissimmeeartificialturf.com")
        await pg.select_option("#f-city", label="Kissimmee")
        await pg.select_option("#f-service", label="Artificial Grass Installation")
        await pg.fill("#f-msg", "Teste de entrega do formulario em 2026-09-21. Pode apagar.")
        await pg.check("#f-ok")
        resp = None
        async with pg.expect_response(lambda r: "api.web3forms.com/submit" in r.url, timeout=30000) as info:
            await pg.click("form.lead button[type=submit]")
        resp = await info.value
        print("web3forms status:", resp.status, "->", resp.headers.get("location", "")[:80])
        await pg.wait_for_timeout(2500)
        print("landed on:", pg.url[:90])
        print("CRM mirror fired:", bool(mirrored), (mirrored[0][:160] if mirrored else ""))
        print("console errors:", [e[:120] for e in errors][:5])
        await b.close()

asyncio.run(main())
