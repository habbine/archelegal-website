# Archè website

Static website for Archè SELARL (English, French, Korean). No framework, no external requests, no cookies.
Hosted on GitHub Pages in **its own repository**, separate from `habbine.github.io`.

## Edit the site

- Text: `content.py` (EN / FR / KO)
- Contact details, booking link, KakaoTalk, legal notice fields, team photos: `config.py`
- Look: `assets/style.css`

Upload or push the whole folder **with its subfolders** (`assets/`, `fr/`, `ko/`, `services/` and so on). Uploading files one by one through the GitHub web page flattens the folders and breaks the site.

After any change:

```bash
python3 build.py
git add -A && git commit -m "Update site" && git push
```

## Publish on GitHub Pages

1. Create a new **public** repo, e.g. `habbine/archelegal-website` (not `habbine.github.io`).
2. Push this folder to the `main` branch.
3. Repo **Settings → Pages → Build and deployment**: Source = *Deploy from a branch*, Branch = `main`, folder = `/ (root)`.
4. Preview at `https://habbine.github.io/archelegal-website/` (links are relative, so it works there too).

## Point archelegal.com to it (when ready)

The repo contains a `CNAME` file for `archelegal.com`. DNS is managed in Wix (Settings → Domains → Manage DNS records).
**Changing the A records takes the Wix site offline for archelegal.com**, so do this only after the new site is approved.

**Change these (web):**

| Type | Host | Now | Replace with |
|---|---|---|---|
| A | archelegal.com | 185.230.63.107 | 185.199.108.153 |
| A | archelegal.com | 185.230.63.186 | 185.199.109.153 |
| A | archelegal.com | 185.230.63.171 | 185.199.110.153 |
| A | archelegal.com | (new record) | 185.199.111.153 |
| CNAME | www | cdn3.wixdns.net | habbine.github.io |

(Use the account or organisation name that owns the new repo in place of `habbine` if different.)

**Do not touch (email):** the MX record, the TXT record starting `v=spf1`, `mail` (CNAME to ex01.directcloud.co.kr),
`autodiscover` (CNAME to autodiscover.outlook.com), and any other TXT/MX records below the part that was visible.

Then in the new repo: Settings → Pages → Custom domain = `archelegal.com`, wait for the DNS check, tick **Enforce HTTPS**.
Optional but recommended: Settings (account) → Pages → *Add a domain* to verify archelegal.com, which stops anyone else claiming it.

Rollback: put the three Wix A records and the `cdn3.wixdns.net` CNAME back. DNS TTL is 1 hour.

`archelegal.net` (the old Wix address) is a separate domain and is not affected. Redirect it later if you want.

Redirects: set `SITE_URL` in `config.py` to the version you want as canonical (`www` or bare) and rebuild.

## Before launch checklist

- [ ] Fill the legal notice fields in `config.py` (`LEGAL`): RCS, capital, VAT, bar, insurance, publication director. Blank ones show highlighted on the page.
- [ ] Have a native speaker proofread the French and Korean text in `content.py`.
- [ ] Confirm the claims in the credentials section with each partner (roles and dates change, e.g. the CCICF presidency).
- [ ] Add a booking link (`BOOKING_URL`), a form endpoint (`FORM_ENDPOINT`, e.g. Formspree) and KakaoTalk if used.
- [ ] Add real photos: put files in `assets/img/` and set `photo` for each person in `config.py`.
- [ ] Add Seoul and Hong Kong addresses if the offices have them.
- [ ] Selected matters (Experience page) are anonymised summaries from the old Competence page. Brand and client names that appeared there (e.g. carmakers, luxury houses, a coffee chain) were left out. Add them back only with client consent, and check bar advertising rules.
- [ ] CCICF presidency dates differ on the old site (home page: 2019–2026; profile slide: since 2018). Confirm and fix in `content.py` and `content_extra.py`.
- [ ] Replace `assets/logo.svg` with the firm's real logo file (keep the name, or edit `build.py`).
- [ ] Personal mobile numbers shown on the old profile slides were intentionally not copied.
