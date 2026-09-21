import asyncio, sys, pathlib, http.server, threading, functools
from playwright.async_api import async_playwright
DIST = pathlib.Path(__file__).resolve().parent.parent / "site" / "dist"
OUT = pathlib.Path(sys.argv[1]); route = sys.argv[2] if len(sys.argv) > 2 else "/"
h = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(DIST))
srv = http.server.ThreadingHTTPServer(("127.0.0.1", 8765), h); threading.Thread(target=srv.serve_forever, daemon=True).start()
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for name, w, hgt in (("desktop", 1280, 900), ("mobile", 390, 844)):
            pg = await b.new_page(viewport={"width": w, "height": hgt})
            await pg.goto("http://127.0.0.1:8765" + route); await pg.wait_for_timeout(400)
            await pg.screenshot(path=str(OUT / f"{name}.png"), full_page=False)
        await b.close()
asyncio.run(main())
