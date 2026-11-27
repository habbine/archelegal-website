# Archè — archelegal.com

Static, trilingual (EN / FR / KO) website of Archè, published through GitHub Pages
(`CNAME` → `archelegal.com`). **This repository is the source of truth.**

## How it works

- Text lives in `config.py`, `content.py`, `content_extra.py`, `content_services.py`,
  `experience6.py`, `press_extra.py` and `team_profiles.py`.
- `build.py` generates the pages: English at the repo root, `fr/` and `ko/` for the other
  languages, plus `404.html`, `sitemap.xml`, `robots.txt` and `CNAME`.
- Styles, scripts, fonts, logos and photos are in `assets/` (`style.css`, `site.js`,
  `fonts/`, `brand/`, `img/`, `downloads/`).
- The generated HTML is committed, because GitHub Pages serves the repo as it is.

## Rebuild the site

```bash
python3 build.py        # Python 3 standard library only, no dependencies
```

Run it after any text or style change, then commit the changed files.
`build.py` adds a version hash to the `style.css` link, so editing `assets/style.css`
without rebuilding leaves the pages pointing at the old hash.

## Restore after a problem

1. Latest published version: branch `main`.
2. Dated snapshots: tags named `backup-YYYY-MM-DD` (each is a full copy of the site and of this README).
3. Full copy outside GitHub: the `.tar.gz` (site files) and `.bundle` (all branches and history)
   kept in Habbine's own storage. Restore with:
   ```bash
   git clone archelegal-all-branches.bundle archelegal-website   # full history
   # or: tar -xzf archelegal-site-<commit>.tar.gz                # files only
   ```
4. Anyone with the files can republish: push to `main` of `habbine/archelegal-website`
   and GitHub Pages serves `archelegal.com`.

## Backup rule

Keep a current backup of the whole site and this README after every change:
update the `backup-YYYY-MM-DD` tag and refresh the `.tar.gz` and `.bundle`.

## Known gaps

- Legal notice fields `rcp` and `tva` are empty in `config.py` (the build prints a warning).

## Credit and rights

© Archè. Site content, brand marks and portraits are not open for reuse without permission.
