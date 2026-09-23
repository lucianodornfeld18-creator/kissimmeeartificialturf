# -*- coding: utf-8 -*-
"""Process the owner's photos from images/incoming into site/static/img/photos.
For each photo in site/_photos.py: EXIF-transpose, drop all metadata, resize to several widths (never upscale),
no sharpening (grass texture costs 20-25% more bytes when sharpened), WebP q62; 4:3 thumbnails at 480/672/1024 (q58) cropped around the focal point;
a 1200x630 JPEG with the badge for Open Graph. Also writes the site-wide og.jpg from the hero photo and
site/_photos_sizes.json. Run from the project root: python brand/make_photos.py"""
import json
import pathlib
import sys

from PIL import Image, ImageFilter, ImageOps

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "site"))
from _photos import PHOTOS, ORDER  # noqa: E402

IN = ROOT / "images" / "incoming"
OUT = ROOT / "site" / "static" / "img" / "photos"
OUT.mkdir(parents=True, exist_ok=True)
WIDTHS = (480, 800, 1200, 1600)
THUMBS = (480, 672, 1024)  # capped at 1024 so DPR-3 phones never fetch a 1280 hero
HERO = "lakefront-estate"
BADGE = ROOT / "site" / "static" / "img" / "logo-512.png"


def sharpen(im):
    return im  # sharpening kept out on purpose: see module docstring


def resize_w(im, w):
    h = round(im.height * w / im.width)
    return sharpen(im.resize((w, h), Image.LANCZOS))


def crop_ratio(im, w, h, focal):
    return sharpen(ImageOps.fit(im, (w, h), Image.LANCZOS, centering=focal))


def badge_over(im, size=150, margin=18):
    b = Image.open(BADGE).convert("RGBA").resize((size, size), Image.LANCZOS)
    out = im.convert("RGBA")
    out.alpha_composite(b, (out.width - size - margin, out.height - size - margin))
    return out.convert("RGB")


def save_webp(im, path, q=62):
    im.save(path, "WEBP", quality=q, method=6)


def save_jpg(im, path, q=78):
    im.save(path, "JPEG", quality=q, optimize=True, progressive=True)


def main():
    for old in OUT.glob("*"):
        old.unlink()
    sizes, total = {}, 0
    for pid in ORDER:
        d = PHOTOS[pid]
        im = ImageOps.exif_transpose(Image.open(IN / d["src"])).convert("RGB")
        if max(im.size) > 1600:
            im = resize_w(im, 1600) if im.width >= im.height else im.resize((round(im.width * 1600 / im.height), 1600), Image.LANCZOS)
        widths = sorted({w for w in WIDTHS if w < im.width} | {im.width})
        for w in widths:
            out = OUT / f"{d['stem']}-{w}.webp"
            save_webp(im if w == im.width else resize_w(im, w), out)
            total += out.stat().st_size
        for w in THUMBS:
            out = OUT / f"{d['stem']}-t{w}.webp"
            save_webp(crop_ratio(im, w, round(w * 3 / 4), d["focal"]), out, q=58)
            total += out.stat().st_size
        og = badge_over(crop_ratio(im, 1200, 630, d["focal"]))
        save_jpg(og, OUT / f"{d['stem']}-og.jpg")
        total += (OUT / f"{d['stem']}-og.jpg").stat().st_size
        if pid == HERO:
            save_jpg(og, ROOT / "site" / "static" / "img" / "og.jpg")
        sizes[pid] = {"w": im.width, "h": im.height, "widths": widths, "thumbs": list(THUMBS)}
        print(f"{pid:<28} {im.width}x{im.height}  widths {widths}")
    (ROOT / "site" / "_photos_sizes.json").write_text(json.dumps(sizes, indent=1), encoding="utf-8")
    print(f"\n{len(list(OUT.iterdir()))} files, {total / 1024:.0f} KB in {OUT}")


if __name__ == "__main__":
    main()
