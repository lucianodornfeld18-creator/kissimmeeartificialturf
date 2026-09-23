# -*- coding: utf-8 -*-
"""Registry of the owner's project photos. Files are produced by brand/make_photos.py into site/static/img/photos/.
Keys are stable ids used by _helpers.photo() / photo_strip() and by templates for OG images and schema.
No town or neighborhood is asserted for any photo: the owner did not say where they were taken."""
import json
import pathlib

ROOT = pathlib.Path(__file__).parent
PHOTO_DIR = "/static/img/photos/"
BRAND = "kissimmee-artificial-turf"

# id -> source file in images/incoming, SEO stem, focal point (x, y in 0..1) for the 4:3 and 16:9 crops, alt, short name, services
PHOTOS = {
    "lakefront-estate": {
        "src": "p08.jpg", "stem": f"{BRAND}-lakefront-yard-pool-putting-green", "focal": (0.62, 0.5),
        "alt": "Large lakefront yard covered in artificial turf, running from an aluminum picket fence past path lights to a pool, an outdoor sofa and putting green flags",
        "name": "Lakefront yard with turf, pool and putting green", "services": ["residential", "putting", "pool"]},
    "backyard-lawn-pool-home": {
        "src": "p04.jpg", "stem": f"{BRAND}-backyard-lawn-pool-home", "focal": (0.5, 0.58),
        "alt": "Artificial grass backyard at a white single-story home, with a palm inside a gravel ring and the pool deck at the far edge",
        "name": "Backyard artificial grass at a pool home", "services": ["residential", "str"]},
    "putting-green-three-cups": {
        "src": "p03.jpg", "stem": f"{BRAND}-backyard-putting-green-three-cups", "focal": (0.5, 0.42),
        "alt": "Backyard artificial putting green with three cups and flags, a taller fringe collar and a white vinyl privacy fence",
        "name": "Three-cup backyard putting green with fringe", "services": ["putting"]},
    "putting-green-hedge": {
        "src": "p09.jpg", "stem": f"{BRAND}-putting-green-hedge-pool-deck", "focal": (0.5, 0.55),
        "alt": "Backyard putting green with three flags and practice balls beside a pool deck, framed by a tall hedge and a palm",
        "name": "Putting green beside a pool deck", "services": ["putting", "str"]},
    "turf-between-pavers": {
        "src": "p05.jpg", "stem": f"{BRAND}-between-porcelain-pavers-diagonal", "focal": (0.5, 0.5),
        "alt": "Close-up of artificial turf strips between square porcelain pavers set on the diagonal, with a block retaining wall behind",
        "name": "Turf strips between diagonal porcelain pavers", "services": ["pavers"]},
    "lakefront-backyard-palms": {
        "src": "p07.jpg", "stem": f"{BRAND}-lakefront-backyard-palms-aluminum-fence", "focal": (0.5, 0.55),
        "alt": "Lakefront backyard with artificial turf, two palms inside black ring edging, an aluminum picket fence and homes across the water",
        "name": "Fenced lakefront backyard with palms in ring edging", "services": ["residential", "pet"]},
    "rooftop-pool-deck": {
        "src": "p01.jpg", "stem": f"{BRAND}-rooftop-pool-deck-high-rise", "focal": (0.5, 0.6),
        "alt": "Artificial turf lawn on a high-rise rooftop pool deck with lounge chairs, cafe tables and drain grates set flush in the turf",
        "name": "Rooftop pool deck turf at a high-rise", "services": ["commercial", "pool"]},
    "rooftop-amenity-deck": {
        "src": "p02.jpg", "stem": f"{BRAND}-rooftop-amenity-deck-porcelain-pavers", "focal": (0.45, 0.55),
        "alt": "Rooftop amenity deck with artificial turf laid beside large-format porcelain pavers, bamboo planters and a pergola",
        "name": "Rooftop amenity deck: turf beside porcelain pavers", "services": ["commercial", "pavers", "cleaning"]},
    "turf-under-tree-lakefront": {
        "src": "p06.jpg", "stem": f"{BRAND}-seating-area-under-tree-lakefront", "focal": (0.5, 0.62),
        "alt": "Small artificial turf seating area with a bistro table around a raised stone planter under a magnolia, natural grass in front and a lake behind",
        "name": "Turf seating area around a raised tree planter", "services": ["residential"]},
}
ORDER = list(PHOTOS)

try:
    SIZES = json.loads((ROOT / "_photos_sizes.json").read_text(encoding="utf-8"))
except FileNotFoundError:
    SIZES = {}


def info(pid):
    """Merged registry + measured sizes: w, h, widths (full), thumbs (4:3 widths)."""
    d = dict(PHOTOS[pid])
    d.update(SIZES.get(pid, {}))
    d["id"] = pid
    return d


def url(pid, w=None, thumb=False, kind="webp"):
    d = info(pid)
    if kind == "og":
        return f"{PHOTO_DIR}{d['stem']}-og.jpg"
    if thumb:
        return f"{PHOTO_DIR}{d['stem']}-t{w or d['thumbs'][-1]}.webp"
    return f"{PHOTO_DIR}{d['stem']}-{w or d['widths'][-1]}.webp"
