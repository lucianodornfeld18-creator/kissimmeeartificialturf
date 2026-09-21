# -*- coding: utf-8 -*-
"""Vector redraw of the owner's badge logo (dark-green double ring, grass blades, EST. 2024) and every raster derived from it."""
import asyncio, pathlib
from PIL import Image
ROOT = pathlib.Path(__file__).resolve().parent.parent
IMG = ROOT / "site" / "static" / "img"; IMG.mkdir(parents=True, exist_ok=True)
DARK, MID, LIGHT, INK = "#0B4A18", "#1C7427", "#43A83A", "#0C1F12"
# (base_x, tip_x, tip_y, half_width, bend)  bend pushes the belly of the blade sideways
BLADES = [(190, 112, 262, 19, 46), (322, 400, 262, 19, -46), (210, 140, 200, 22, 44), (302, 372, 200, 22, -44),
          (170, 118, 330, 15, 30), (342, 394, 330, 15, -30), (234, 186, 150, 24, 36), (280, 330, 124, 25, -38), (256, 250, 190, 20, 4)]

def blade(i, bx, tx, ty, w, bend, by=404):
    mx, my = (bx + tx) / 2 + bend, (by + ty) / 2
    return (f'<path fill="url(#g{i % 3})" stroke="#fff" stroke-width="3" stroke-linejoin="round" '
            f'd="M{bx - w} {by}Q{mx - w * .9:.0f} {my:.0f} {tx} {ty}Q{mx + w * 1.1:.0f} {my + 10:.0f} {bx + w} {by}Z"/>')

def grads():
    return "".join(f'<linearGradient id="g{i}" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="{a}"/><stop offset="1" stop-color="{b}"/></linearGradient>'
                   for i, (a, b) in enumerate([(DARK, MID), (DARK, LIGHT), (MID, LIGHT)]))

def badge(text=True):
    blades = "".join(blade(i, *b) for i, b in enumerate(BLADES))
    t = ""
    if text:
        t = (f'<path id="top" d="M77 256a179 179 0 0 1 358 0" fill="none"/><path id="bot" d="M43 256a213 213 0 0 0 426 0" fill="none"/>'
             f'<g font-family="Arial Black,Arial,Helvetica,sans-serif" font-weight="900" fill="{INK}" text-anchor="middle">'
             f'<text font-size="43" letter-spacing="8"><textPath href="#top" startOffset="50%">KISSIMMEE</textPath></text>'
             f'<text font-size="35" letter-spacing="6"><textPath href="#bot" startOffset="50%">ARTIFICIAL TURF</textPath></text>'
             f'<text x="73" y="268" font-size="28" letter-spacing="1">EST.</text><text x="441" y="268" font-size="28" letter-spacing="1">2024</text></g>')
        bands = (f'<g stroke="{DARK}" stroke-width="5"><path d="M20 214H118M394 214H492M20 298H118M394 298H492"/></g>'
                 f'<rect x="22" y="217" width="98" height="78" fill="#fff"/><rect x="392" y="217" width="98" height="78" fill="#fff"/>')
    else:
        bands = ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512"><defs>{grads()}<clipPath id="c"><circle cx="256" cy="256" r="140"/></clipPath></defs>'
            f'<circle cx="256" cy="256" r="246" fill="#fff" stroke="{DARK}" stroke-width="11"/><circle cx="256" cy="256" r="229" fill="none" stroke="{DARK}" stroke-width="3.5"/>'
            f'{bands}<circle cx="256" cy="256" r="146" fill="#fff" stroke="{DARK}" stroke-width="9"/><g clip-path="url(#c)">{blades}</g>{t}</svg>')

def mark():
    blades = "".join(blade(i, *b) for i, b in enumerate(BLADES))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="96 96 320 320"><defs>{grads()}<clipPath id="c"><circle cx="256" cy="256" r="140"/></clipPath></defs>'
            f'<circle cx="256" cy="256" r="150" fill="#fff" stroke="{DARK}" stroke-width="16"/><g clip-path="url(#c)">{blades}</g></svg>')

async def render():
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": 1200, "height": 630}, device_scale_factor=1)
        big_svg = badge().replace('width="512" height="512"', 'width="1024" height="1024"')
        await pg.set_content('<body style="margin:0;background:transparent"><div style="width:1024px;height:1024px">' + big_svg + '</div></body>')
        await pg.set_viewport_size({"width": 1024, "height": 1024})
        await pg.screenshot(path=str(IMG / "_badge1024.png"), omit_background=True)
        await pg.set_content(f'<body style="margin:0;background:transparent"><div style="width:512px;height:512px">{mark().replace("<svg ", "<svg width=512 height=512 ")}</div></body>')
        await pg.set_viewport_size({"width": 512, "height": 512})
        await pg.screenshot(path=str(IMG / "_mark512.png"), omit_background=True)
        await pg.set_viewport_size({"width": 1200, "height": 630})
        await pg.set_content(f'''<body style="margin:0;width:1200px;height:630px;background:#FBF7EE;display:flex;align-items:center;gap:56px;padding:0 80px;box-sizing:border-box;font-family:Georgia,serif;color:#14261F">
<div style="width:400px;height:400px;flex:none">{badge().replace('width="512" height="512"', 'width="400" height="400"')}</div>
<div><div style="font-size:64px;line-height:1.05">Kissimmee<br>Artificial Turf</div><div style="font:600 28px system-ui,Arial,sans-serif;margin-top:22px;color:#1C5A2A">Artificial grass installation · Kissimmee, FL</div><div style="font:700 34px system-ui,Arial,sans-serif;margin-top:16px;color:#B8431A">(689) 202-3710</div></div></body>''')
        await pg.screenshot(path=str(IMG / "og.png"))
        await b.close()

if __name__ == "__main__":
    (IMG / "logo.svg").write_text(badge(), encoding="utf-8")
    (IMG / "icon.svg").write_text(mark(), encoding="utf-8")
    asyncio.run(render())
    big = Image.open(IMG / "_badge1024.png").convert("RGBA")
    big.resize((512, 512), Image.LANCZOS).save(IMG / "logo-512.png", optimize=True)
    big.resize((640, 640), Image.LANCZOS).save(IMG / "logo-badge.webp", quality=84, method=6)
    big.resize((480, 480), Image.LANCZOS).save(IMG / "logo-badge-480.webp", quality=84, method=6)
    big.resize((320, 320), Image.LANCZOS).save(IMG / "logo-badge-320.webp", quality=88, method=6)
    m = Image.open(IMG / "_mark512.png").convert("RGBA")
    m.resize((192, 192), Image.LANCZOS).save(IMG / "icon-192.png", optimize=True)
    ap = Image.new("RGBA", (180, 180), "#FFFFFF"); mm = m.resize((160, 160), Image.LANCZOS); ap.paste(mm, (10, 10), mm); ap.convert("RGB").save(IMG / "apple-touch-icon.png", optimize=True)
    m.resize((64, 64), Image.LANCZOS).save(IMG / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
    og = Image.open(IMG / "og.png").convert("RGB"); og.save(IMG / "og.png", optimize=True)
    for f in ("_badge1024.png", "_mark512.png"):
        (IMG / f).unlink()
    print(sorted((f.name, f.stat().st_size) for f in IMG.iterdir()))
