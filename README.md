# kissimmeeartificialturf.com

Static site for Kissimmee Artificial Turf (Kissimmee, FL). Python generator, no dependencies beyond the standard library.

    python site/build.py        # content modules in site/content/ -> site/dist/
    python qa/qa_all.py --sim   # links, duplicates, word counts, banned phrases, JSON-LD, 8-gram similarity
    python qa/check_module.py c_home   # check one module in memory

- `site/dist/` is committed; Cloudflare Pages serves it as-is (no build command). Deploy = push to `main`.
- `docs/WRITING-GUIDE.md` is binding for every page: voice, never-invent rule, verified facts and sources.
- `twilio/` holds the call flow for (689) 202-3710; `cloudflare/` holds the Email Routing and Pages scripts.
- `docs/OWNER-INPUTS.md` lists what still needs the owner.
- Photos: originals go in `images/incoming/` (git-ignored), get registered in `site/_photos.py` (SEO name, alt, focal point, services) and processed by `python brand/make_photos.py` into `site/static/img/photos/` (responsive WebP, 4:3 thumbnails, 1200x630 JPEG for Open Graph). Pages place them with `photo(id, caption)` / `photo_strip(ids)`; `/gallery/` shows all of them.
