# -*- coding: utf-8 -*-
"""Static site generator for Archè. Run from the repo root:  python3 build.py
Writes en pages at the repo root, fr/ and ko/ for the other languages."""
import html, json, os, re, shutil, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import config as C
from content import T
import content_extra
content_extra.apply(T)

ROOT = Path(__file__).resolve().parent
LANGS = ["en", "fr", "ko"]
LANG_LABEL = {"en": "EN", "fr": "FR", "ko": "한국어"}
NAV = ["services", "experience", "people", "insights", "contact"]
SLUG = {"home": "", "services": "services/", "experience": "experience/", "people": "team/", "insights": "insights/",
        "contact": "contact/", "legal": "legal/", "privacy": "privacy/"}
OG_LOCALE = {"en": "en_GB", "fr": "fr_FR", "ko": "ko_KR"}
e = html.escape
warnings = []


def url_path(lang, page):
    return ("" if lang == "en" else lang + "/") + SLUG[page]


def depth(lang, page):
    return url_path(lang, page).count("/")


def rel(lang, page, target_lang, target_page):
    """Relative link from (lang,page) to (target_lang,target_page)."""
    up = "../" * depth(lang, page)
    p = up + url_path(target_lang, target_page)
    return p or "./"


def abs_url(lang, page):
    return C.SITE_URL.rstrip("/") + "/" + url_path(lang, page)


def header(lang, page, t):
    up = "../" * depth(lang, page)
    nav = ""
    for key in NAV:
        cur = ' aria-current="page"' if key == page else ""
        nav += f'<a href="{rel(lang, page, lang, key)}"{cur}>{e(t["nav"][key])}</a>'
    switch = ""
    for l in LANGS:
        cur = ' aria-current="true"' if l == lang else ""
        switch += f'<a href="{rel(lang, page, l, page)}" hreflang="{l}" lang="{l}"{cur}>{LANG_LABEL[l]}</a>'
    return f'''<a class="skip" href="#main">{e(t["skip"])}</a>
<header class="site-header"><div class="wrap">
<a class="brand" href="{rel(lang, page, lang, "home")}" aria-label="{e(C.FIRM)}"><img src="{up}assets/logo-mark.png" width="43" height="48" alt=""><span class="brand-text"><span>{e(C.FIRM)}</span><small>SELARL</small></span></a>
<button class="nav-toggle" aria-expanded="false" aria-controls="primary-nav" type="button">{e(t["menu"])}</button>
<nav class="primary" id="primary-nav" aria-label="{e(t["menu"])}">{nav}<a class="btn" href="{cta_href(lang, page)}">{e(t["cta"])}</a><div class="lang" role="group" aria-label="Language">{switch}</div></nav>
</div></header>'''


def cta_href(lang, page):
    return C.BOOKING_URL or rel(lang, page, lang, "contact") + "#form"


def footer(lang, page, t):
    f = t["footer"]
    links = "".join(f'<li><a href="{rel(lang, page, lang, k)}">{e(t["nav"][k])}</a></li>' for k in NAV)
    soc = f'<li><a href="{C.LINKEDIN}" rel="noopener">LinkedIn</a></li><li><a href="{C.INSTAGRAM}" rel="noopener">Instagram</a></li>'
    return f'''<footer class="site-footer"><div class="wrap">
<div class="cols c4">
<div><h3>{e(C.FIRM_FULL)}</h3><p>{e(f["lawyers"])}</p></div>
<div><h3>{e(f["nav"])}</h3><ul>{links}</ul></div>
<div><h3>{e(t["home"]["offices_h"])}</h3><ul><li>Paris: {e(", ".join(C.ADDRESS_LINES[:2]))}</li><li>Seoul</li><li>Hong Kong</li></ul></div>
<div><h3>{e(f["follow"])}</h3><ul>{soc}</ul></div>
</div>
<div class="fine"><span>© {2026} {e(C.FIRM_FULL)}. {e(f["rights"])}</span><a href="{rel(lang, page, lang, "legal")}">{e(f["legal"])}</a><a href="{rel(lang, page, lang, "privacy")}">{e(f["privacy"])}</a></div>
</div></footer>'''


def head(lang, page, t, extra_ld=""):
    title, desc = t["meta"][page]
    up = "../" * depth(lang, page)
    alts = "".join(f'<link rel="alternate" hreflang="{l}" href="{abs_url(l, page)}">' for l in LANGS)
    alts += f'<link rel="alternate" hreflang="x-default" href="{abs_url("en", page)}">'
    return f'''<!doctype html>
<html lang="{t["html_lang"]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{abs_url(lang, page)}">
{alts}
<meta property="og:type" content="website"><meta property="og:site_name" content="{e(C.FIRM_FULL)}">
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{abs_url(lang, page)}"><meta property="og:locale" content="{OG_LOCALE[lang]}">
<meta property="og:image" content="{C.SITE_URL.rstrip("/")}/assets/og.svg">
<meta name="twitter:card" content="summary">
<meta name="theme-color" content="#1B2B2B">
<link rel="icon" href="{up}assets/favicon.png" type="image/png"><link rel="apple-touch-icon" href="{up}assets/apple-touch-icon.png">
<link rel="stylesheet" href="{up}assets/style.css">
<script defer src="{up}assets/site.js"></script>
{extra_ld}
</head>'''


def shell(lang, page, t, body, ld=""):
    return head(lang, page, t, ld) + f'\n<body>\n{header(lang, page, t)}\n<main id="main">\n{body}\n</main>\n{footer(lang, page, t)}\n</body>\n</html>\n'


def org_ld():
    d = {
        "@context": "https://schema.org", "@type": "LegalService", "name": C.FIRM_FULL,
        "url": C.SITE_URL, "email": C.EMAIL, "telephone": C.PHONE,
        "logo": C.SITE_URL.rstrip("/") + "/assets/logo.png",
        "address": {"@type": "PostalAddress", "streetAddress": C.ADDRESS_LINES[0], "postalCode": "75015",
                    "addressLocality": "Paris", "addressCountry": "FR"},
        "areaServed": ["FR", "KR", "HK"], "knowsLanguage": ["en", "fr", "ko"],
        "sameAs": [C.LINKEDIN, C.INSTAGRAM],
    }
    return '<script type="application/ld+json">' + json.dumps(d, ensure_ascii=False) + "</script>"


def cta_band(lang, page, t, h, p, dark=True):
    return f'''<section class="{"dark" if dark else "alt"}"><div class="wrap cols c2">
<div><h2>{e(h)}</h2><p class="lede">{e(p)}</p></div>
<div style="display:flex;align-items:center;gap:14px;flex-wrap:wrap">
<a class="btn on-dark" href="{cta_href(lang, page)}">{e(t["cta"])}</a>
<a class="btn ghost" style="color:#fff;border-color:#fff" href="mailto:{C.EMAIL}">{e(C.EMAIL)}</a>
</div></div></section>'''


def bridge(lang, t):
    h = t["home"]
    rows = ""
    for key, tz in [("paris", "Europe/Paris"), ("seoul", "Asia/Seoul"), ("hk", "Asia/Hong_Kong")]:
        rows += f'''<div class="row" data-tz="{tz}"><span class="city">{e(h["cities"][key])}</span><span class="time" aria-live="off">--:--</span>
<span class="state"><span class="dot" aria-hidden="true"></span><span class="label"></span></span><div class="track" aria-hidden="true"></div></div>'''
    return f'''<aside class="bridge" id="bridge" data-open="{e(h["bridge_open"])}" data-closed="{e(h["bridge_closed"])}" aria-label="{e(h["bridge_title"])}">
<h2>{e(h["bridge_title"])}</h2>{rows}
<div class="axis" aria-hidden="true"><span>00h</span><span>06h</span><span>12h</span><span>18h</span></div>
<p class="note">{e(h["bridge_note"])}</p></aside>'''


def page_home(lang, t):
    h = t["home"]
    svc = t["services"]["items"]
    who = "".join(f'<div class="rule-top"><h3>{e(a)}</h3><p>{e(b)}</p></div>' for a, b in h["who"])
    svcs = "".join(f'<div class="rule-top"><h3><a href="{rel(lang, "home", lang, "services")}#{s[0]}" style="color:inherit;text-decoration:none">{e(s[1])}</a></h3><p>{e(s[2])}</p></div>' for s in svc)
    creds = "".join(f'<div class="rule-top"><h3 style="font-size:1.1rem">{e(a)}</h3><p>{e(b)}</p></div>' for a, b in h["creds"])
    inds = "".join(f'<span class="tag">{e(x)}</span>' for x in h["industries"])
    def office(name, d, main=False):
        extra = ""
        if main:
            extra = f'<p>{"<br>".join(e(x) for x in C.ADDRESS_LINES)}</p><p><a href="mailto:{C.EMAIL}">{e(C.EMAIL)}</a><br><a href="tel:{C.PHONE_TEL}">{e(C.PHONE)}</a></p>'
        else:
            if d.get("address"):
                extra += f'<p>{e(d["address"])}</p>'
            if d.get("phone"):
                extra += f'<p><a href="tel:{e(d["phone"])}">{e(d["phone"])}</a></p>'
            if not extra:
                extra = f'<p>{e(h["contact_office"])}: <a href="mailto:{C.EMAIL}">{e(C.EMAIL)}</a></p>'
        tag = f'<p><strong>{e(h["main_office"])}</strong></p>' if main else ""
        return f'<div class="office"><h3>{e(name)}</h3>{tag}{extra}</div>'
    offices = office(h["cities"]["paris"], {}, True) + office(h["cities"]["seoul"], C.SEOUL) + office(h["cities"]["hk"], C.HONGKONG)
    press = ""
    if C.PRESS:
        press = f'''<section class="alt"><div class="wrap"><div class="section-head"><h2>{e(h["press_h"])}</h2><p class="lede">{e(h["press_p"])}</p></div>
<div class="press">''' + "".join(f'<a href="{e(p["url"])}" rel="noopener" lang="{p["lang"]}"><strong>{e(h["press_item"])}</strong><small>{e(p["outlet"])}</small></a>' for p in C.PRESS) + "</div></div></section>"
    mt = ""
    if t.get("matters"):
        firsts = "".join(f'<div class="rule-top"><h3 style="font-size:1.05rem">{e(g[0])}</h3><p>{e(g[1][0])}</p></div>' for g in t["matters"]["groups"])
        mt = f'''<section><div class="wrap"><div class="section-head"><h2>{e(h["matters_h"])}</h2><p class="lede">{e(h["matters_intro"])}</p></div>
<div class="cols c4">{firsts}</div><p style="margin-top:28px"><a href="{rel(lang, "home", lang, "experience")}">{e(h["matters_more"])}</a></p></div></section>'''
    body = f'''<section class="hero"><div class="wrap">
<div><h1>{e(h["h1"])}</h1><p class="lede">{e(h["lede"])}</p>
<div class="actions"><a class="btn" href="{cta_href(lang, "home")}">{e(t["cta"])}</a><a class="btn ghost" href="{rel(lang, "home", lang, "services")}">{e(h["see_services"])}</a></div></div>
{bridge(lang, t)}
</div></section>
<section class="alt"><div class="wrap"><div class="section-head"><h2>{e(h["who_h"])}</h2></div><div class="cols c3">{who}</div></div></section>
<section><div class="wrap"><div class="section-head"><h2>{e(h["services_h"])}</h2></div><div class="cols c4">{svcs}</div>
<p style="margin-top:28px"><a href="{rel(lang, "home", lang, "services")}">{e(h["services_more"])}</a></p></div></section>
{mt}
<section class="alt"><div class="wrap cols c2"><div><h2>{e(h["firm_h"])}</h2><p>{e(h["firm_p"])}</p></div>
<div><h2 style="font-size:1.3rem">{e(h["industries_h"])}</h2><div>{inds}</div><p class="lead-in">{e(h["industries_p"])}</p></div></div></section>
<section><div class="wrap"><div class="section-head"><h2>{e(h["creds_h"])}</h2><p class="lede">{e(h["creds_p"])}</p></div><div class="cols c3">{creds}</div></div></section>
<section class="alt"><div class="wrap"><div class="section-head"><h2>{e(h["offices_h"])}</h2></div><div class="offices">{offices}</div></div></section>
{press}
{cta_band(lang, "home", t, h["cta_h"], h["cta_p"])}'''
    return body


def page_services(lang, t):
    s = t["services"]
    items = ""
    for key, title, intro, bullets in s["items"]:
        lis = "".join(f"<li>{e(b)}</li>" for b in bullets)
        items += f'<div class="service" id="{key}"><div><h2>{e(title)}</h2><p>{e(intro)}</p></div><ul>{lis}</ul></div>'
    faq = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in s["faq"])
    ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in s["faq"]]}
    return f'''<div class="page-head"><div class="wrap"><h1>{e(s["h1"])}</h1><p class="lede">{e(s["lede"])}</p></div></div>
<section style="padding-top:0"><div class="wrap">{items}</div></section>
<section class="alt"><div class="wrap"><div class="section-head"><h2>{e(s["faq_h"])}</h2></div><div class="faq" style="max-width:760px">{faq}</div></div></section>
{cta_band(lang, "services", t, s["cta_h"], s["cta_p"])}''', '<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False) + "</script>"


def page_people(lang, t):
    p = t["people"]
    out = ""
    for person in C.PEOPLE:
        k = person["slug"]
        lis = "".join(f"<li>{e(x)}</li>" for x in p["bios"][k])
        av = f'<img src="{e(person["photo"])}" alt="{e(person["name"])}" width="120" height="120">' if person["photo"] else e(person["initials"])
        links = f'<p>{e(p["email_label"])}: <a href="mailto:{person["email"]}">{e(person["email"])}</a>'
        if person["linkedin"]:
            links += f' · <a href="{e(person["linkedin"])}" rel="noopener">{e(p["linkedin_label"])}</a>'
        links += "</p>"
        out += f'<div class="person"><div class="avatar" aria-hidden="{"false" if person["photo"] else "true"}">{av}</div><div><h2 style="font-size:1.6rem;margin-bottom:.1em">{e(person["name"])}</h2><p class="role">{e(p["roles"][k])}</p><ul>{lis}</ul>{links}</div></div>'
    return f'''<div class="page-head"><div class="wrap"><h1>{e(p["h1"])}</h1><p class="lede">{e(p["lede"])}</p></div></div>
<section style="padding-top:0"><div class="wrap">{out}</div></section>
{cta_band(lang, "people", t, t["home"]["cta_h"], t["home"]["cta_p"])}'''


def page_experience(lang, t):
    m = t["matters"]
    groups = ""
    for title, items in m["groups"]:
        lis = "".join(f"<li>{e(x)}</li>" for x in items)
        groups += f'<div class="service"><div><h2>{e(title)}</h2></div><ul>{lis}</ul></div>'
    return f'''<div class="page-head"><div class="wrap"><h1>{e(m["h1"])}</h1><p class="lede">{e(m["lede"])}</p></div></div>
<section style="padding-top:0"><div class="wrap">{groups}</div></section>
{cta_band(lang, "experience", t, m["cta_h"], m["cta_p"])}'''


def page_insights(lang, t):
    i = t["insights"]
    events = "".join(f"<li>{e(x)}</li>" for x in i["events"])
    press ="".join(f'<a href="{e(x["url"])}" rel="noopener" lang="{x["lang"]}"><strong>{e(t["home"]["press_item"])}</strong><small>{e(x["outlet"])}</small></a>' for x in C.PRESS)
    return f'''<div class="page-head"><div class="wrap"><h1>{e(i["h1"])}</h1><p class="lede">{e(i["lede"])}</p></div></div>
<section style="padding-top:0"><div class="wrap cols c2">
<div><h2>{e(i["press_h"])}</h2><div class="press">{press}</div>
<h2 style="margin-top:2em">{e(i["events_h"])}</h2><p class="lead-in">{e(i["events_p"])}</p><ul>{events}</ul></div>
<div><h2>{e(i["follow_h"])}</h2><p>{e(i["follow_p"])}</p><p><a class="btn ghost" href="{C.LINKEDIN}" rel="noopener">{e(i["follow_cta"])}</a></p>
<h2 style="margin-top:2em">{e(i["ask_h"])}</h2><p>{e(i["ask_p"])}</p><p><a href="mailto:{C.EMAIL}">{e(C.EMAIL)}</a></p></div>
</div></section>'''


def page_contact(lang, t):
    c = t["contact"]
    topics = "".join(f"<option>{e(x)}</option>" for x in c["topics"])
    msgs = ""
    if C.KAKAO_URL:
        msgs += f'<li><a href="{e(C.KAKAO_URL)}" rel="noopener">{e(c["kakao"])}</a></li>'
    if C.WHATSAPP_URL:
        msgs += f'<li><a href="{e(C.WHATSAPP_URL)}" rel="noopener">{e(c["whatsapp"])}</a></li>'
    book = f'<p><a class="btn on-dark" href="{e(C.BOOKING_URL)}" rel="noopener">{e(t["cta"])}</a></p>' if C.BOOKING_URL else ""
    endpoint = f' data-endpoint="{e(C.FORM_ENDPOINT)}"' if C.FORM_ENDPOINT else ""
    return f'''<div class="page-head"><div class="wrap"><h1>{e(c["h1"])}</h1><p class="lede">{e(c["lede"])}</p></div></div>
<section style="padding-top:0"><div class="wrap cols c2">
<div id="form"><h2>{e(c["form_h"])}</h2>
<form class="contact" data-to="{e(C.EMAIL)}"{endpoint} data-ok="{e(c["ok"])}" data-fail="{e(c["fail"])}" data-mail="{e(c["mail"])}" method="post" action="mailto:{e(C.EMAIL)}" enctype="text/plain">
<label>{e(c["f_name"])}<input name="name" required autocomplete="name"></label>
<label>{e(c["f_email"])}<input name="email" type="email" required autocomplete="email"></label>
<label>{e(c["f_company"])}<input name="company" autocomplete="organization"></label>
<label>{e(c["f_topic"])}<select name="topic">{topics}</select></label>
<label>{e(c["f_msg"])}<textarea name="message" required></textarea></label>
<label class="check"><input type="checkbox" name="consent" required><span>{e(c["f_consent"])}</span></label>
<button class="btn" type="submit">{e(c["send"])}</button>
<p class="form-status" role="status" aria-live="polite"></p>
<p class="lead-in">{e(c["confidential"])}</p>
</form></div>
<div><div class="dark" style="padding:28px"><h2 style="font-size:1.4rem">{e(c["details_h"])}</h2>
<ul class="contact-list"><li><span>{e(c["email"])}</span><a href="mailto:{C.EMAIL}">{e(C.EMAIL)}</a></li>
<li><span>{e(c["phone"])}</span><a href="tel:{C.PHONE_TEL}">{e(C.PHONE)}</a></li>
<li><span>{e(c["address"])}</span>{"<br>".join(e(x) for x in C.ADDRESS_LINES)}<br><a href="{C.MAPS_URL}" rel="noopener">{e(c["map"])}</a></li>{msgs}</ul>{book}
<h3 style="font-size:1.1rem">{e(c["other_h"])}</h3><p style="margin:0">{e(c["other_p"])}</p></div></div>
</div></section>'''


def page_legal(lang, t):
    L = t["legal_page"]
    rows = ""
    for label, key in L["rows"]:
        v = C.LEGAL.get(key, "")
        if not v:
            warnings.append(f"legal notice: '{key}' is empty (shown highlighted on the page)")
            cell = '<span class="todo">[…]</span>'
        else:
            cell = e(v)
        rows += f"<tr><th scope='row'>{e(label)}</th><td>{cell}</td></tr>"
    return f'''<div class="page-head"><div class="wrap"><h1>{e(L["h1"])}</h1></div></div>
<section style="padding-top:0"><div class="wrap prose"><p>{e(L["intro"])}</p><table>{rows}</table>{L["extra"]}</div></section>'''


def page_privacy(lang, t):
    P = t["privacy"]
    return f'''<div class="page-head"><div class="wrap"><h1>{e(P["h1"])}</h1></div></div>
<section style="padding-top:0"><div class="wrap prose">{P["body"]}</div></section>'''


def write(path, text):
    path = ROOT / path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main():
    # clean generated output only
    for d in ["fr", "ko", "services", "experience", "team", "insights", "contact", "legal", "privacy"]:
        shutil.rmtree(ROOT / d, ignore_errors=True)
    for f in ["index.html", "404.html", "sitemap.xml", "robots.txt", "CNAME", ".nojekyll"]:
        (ROOT / f).unlink(missing_ok=True)

    builders = {"home": page_home, "services": page_services, "experience": page_experience, "people": page_people,
                "insights": page_insights, "contact": page_contact, "legal": page_legal, "privacy": page_privacy}
    urls = []
    for lang in LANGS:
        t = T[lang]
        for page, fn in builders.items():
            res = fn(lang, t)
            ld = ""
            if isinstance(res, tuple):
                body, ld = res
            else:
                body = res
            if page == "home":
                ld = org_ld()
            out = shell(lang, page, t, body, ld)
            write(url_path(lang, page) + "index.html", out)
            urls.append((lang, page))

    # 404 (absolute asset paths so it works at any depth)
    t = T["en"]
    base = C.SITE_URL.rstrip("/") + "/"
    nf = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(t["meta"]["404"][0])}</title><meta name="robots" content="noindex"><link rel="icon" href="{base}assets/favicon.png" type="image/png"><link rel="stylesheet" href="{base}assets/style.css">
</head><body><main id="main"><section><div class="wrap"><h1>{e(t["nf"]["h1"])}</h1><p class="lede">{e(t["nf"]["p"])}</p><p><a class="btn" href="{base}">{e(t["nf"]["back"])}</a></p></div></section></main></body></html>'''
    write("404.html", nf)

    # sitemap with hreflang alternates
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for page in builders:
        for lang in LANGS:
            sm.append(f"<url><loc>{abs_url(lang, page)}</loc>")
            for l in LANGS:
                sm.append(f'<xhtml:link rel="alternate" hreflang="{l}" href="{abs_url(l, page)}"/>')
            sm.append("</url>")
    sm.append("</urlset>")
    write("sitemap.xml", "\n".join(sm) + "\n")
    write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {C.SITE_URL.rstrip('/')}/sitemap.xml\n")
    write("CNAME", C.DOMAIN + "\n")
    write(".nojekyll", "")

    for w in sorted(set(warnings)):
        print("WARNING:", w)
    print(f"Built {len(urls)} pages + 404, sitemap, robots, CNAME.")


if __name__ == "__main__":
    main()
