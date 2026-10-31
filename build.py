# -*- coding: utf-8 -*-
"""Static site generator for Archè. Run from the repo root:  python3 build.py
Writes en pages at the repo root, fr/ and ko/ for the other languages."""
import html, json, os, re, shutil, sys
import hashlib
CSS_V = hashlib.md5(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets', 'style.css'), 'rb').read()).hexdigest()[:10]
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import config as C
C.PRESS.sort(key=lambda p: p["date"], reverse=True)  # newest first, whatever order config.py lists them in
from content import T
import content_extra
content_extra.apply(T)
import content_services
content_services.apply(T)

ROOT = Path(__file__).resolve().parent
LANGS = ["en", "fr", "ko"]
LANG_LABEL = {"en": "EN", "fr": "FR", "ko": "한국어"}
NAV = ["home", "services", "people", "insights", "contact"]
SLUG = {"home": "", "services": "services/", "experience": "experience/", "people": "team/", "insights": "press/",
        "contact": "contact/", "legal": "legal/", "privacy": "privacy/"}
OG_LOCALE = {"en": "en_GB", "fr": "fr_FR", "ko": "ko_KR"}
e = html.escape
warnings = []


MONTHS = {"en": "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split(),
          "fr": "janv. févr. mars avr. mai juin juil. août sept. oct. nov. déc.".split()}


def fmt_date(lang, d):
    parts = d.split("-")  # "YYYY-MM-DD", "YYYY-MM" when only the month is known, or "YYYY"
    if len(parts) == 1:
        return parts[0]
    y, m = parts[0], parts[1]
    day = parts[2] if len(parts) > 2 else None
    if lang == "ko":
        return f"{y}.{m}.{day}" if day else f"{y}.{m}"
    mon = MONTHS[lang][int(m) - 1]
    if not day:
        mon = {"en": "Jan Feb Mar Apr May June July Aug Sept Oct Nov Dec", "fr": "janvier février mars avril mai juin juillet août septembre octobre novembre décembre"}[lang].split()[int(m) - 1]
        return f"{mon} {y}"
    return f"{int(day)} {mon} {y}"


LANG_TAG = {"ko": {"en": "In Korean", "fr": "En coréen"}, "fr": {"en": "In French", "ko": "프랑스어"},
            "en": {"fr": "En anglais", "ko": "영어"}}
NEW_TAB = {"en": "opens in a new tab", "fr": "s'ouvre dans un nouvel onglet", "ko": "새 탭에서 열림"}


def press_items(lang, items, up=""):
    out = ""
    for p in items:
        cover = (f'<img class="cover" src="{up}{e(p["cover"])}" alt="" width="72" height="108" loading="lazy" decoding="async">'
                 if p.get("cover") else "")
        about = p.get("about", {}).get(lang, "")
        foreign = p["lang"] != lang
        if about and foreign and lang != "ko":
            # English/French pages: lead with the headline in the reader's language, keep the original underneath
            head = f'<strong lang="{lang}">{e(about)}</strong><span class="orig" lang="{p["lang"]}">{e(p["title"])}</span>'
        else:
            head = f'<strong lang="{p["lang"]}">{e(p["title"])}</strong>' + (f'<span class="about">{e(about)}</span>' if about else "")
        tag = LANG_TAG.get(p["lang"], {}).get(lang, "") if foreign else ""
        tag_html = f' · <span class="lang-tag">{e(tag)}</span>' if tag else ""
        out += (f'<a href="{e(p["url"])}" rel="noopener" target="_blank"{' class="has-cover"' if cover else ''}>{cover}<span class="txt">{head}'
                f'<small>{e(p["outlet"][lang])} · <time datetime="{p["date"]}">{fmt_date(lang, p["date"])}</time>{tag_html}'
                f' <span class="ext" aria-hidden="true">↗</span><span class="sr">({e(NEW_TAB[lang])})</span></small></span></a>')
    return out


PRESS_THEMES = [
    ("business", {"en": "Business and market entry", "fr": "Entreprises et implantation", "ko": "기업 및 시장 진출"}),
    ("sport", {"en": "Sport and arbitration", "fr": "Sport et arbitrage", "ko": "스포츠 및 중재"}),
    ("law", {"en": "Law and justice", "fr": "Droit et justice", "ko": "법과 사법"}),
    ("profile", {"en": "Profile and profession", "fr": "Parcours et profession", "ko": "프로필 및 법조 경력"}),
    ("heritage", {"en": "Cultural heritage", "fr": "Patrimoine culturel", "ko": "문화유산"}),
    ("books", {"en": "Books", "fr": "Livres", "ko": "도서"}),
]
# theme -> (target page, anchor, label)
PRESS_CTA = {
    "business": ("services", "advice", {"en": "Setting up in France or Korea? See how we help", "fr": "Vous vous implantez en France ou en Corée ? Nos expertises", "ko": "프랑스·한국 진출을 준비 중이신가요? 업무 분야 보기"}),
    "sport": ("services", "litigation", {"en": "Disputes and arbitration: our practice", "fr": "Contentieux et arbitrage : notre pratique", "ko": "분쟁 해결·중재 업무 보기"}),
    "profile": ("people", "", {"en": "Meet the team", "fr": "Découvrir l'équipe", "ko": "구성원 소개"}),
}
PRESS_MORE = {"en": "Show {n} more", "fr": "Voir {n} de plus", "ko": "{n}건 더 보기"}



def press_featured():
    by_url = {p["url"]: p for p in C.PRESS}
    return [by_url[u] for u in getattr(C, "PRESS_FEATURED", []) if u in by_url]

def press_by_theme(lang, up, shown=3):
    out = ""
    for key, labels in PRESS_THEMES:
        if key == "books":  # shown under Publications instead
            continue
        items = [p for p in C.PRESS if C.PRESS_THEME.get(p["url"]) == key]
        if not items:
            continue
        head, rest = items[:shown], items[shown:]
        more = (f'<details class="press-more"><summary>{e(PRESS_MORE[lang].format(n=len(rest)))}</summary>'
                f'<div class="press">{press_items(lang, rest, up)}</div></details>') if rest else ""
        cta = ""
        if key in PRESS_CTA:
            pg, anchor, lbl = PRESS_CTA[key]
            cta = f'<p class="press-cta"><a href="{rel(lang, "insights", lang, pg)}{"#" + anchor if anchor else ""}">{e(lbl[lang])} →</a></p>'
        out += (f'<div class="press-theme" id="press-{key}"><h3>{e(labels[lang])} <small>{len(items)}</small></h3>'
                f'<div class="press">{press_items(lang, head, up)}</div>{more}{cta}</div>')
    return f'<div class="press-themes">{out}</div>'


HERITAGE = {
    "en": ("The Oegyujanggak case", "Since 2007, James Joong-ho Kim has acted in the claim for the return of Korea's Oegyujanggak royal manuscripts before the Paris Administrative Court. At the December 2009 hearing, the French State used the word \u201cpillage\u201d for the first time.", "Read the press coverage"),
    "fr": ("L'affaire de l'Oegyujanggak", "Depuis 2007, James Joong-ho Kim agit dans la demande de restitution des manuscrits royaux coréens de l'Oegyujanggak devant le tribunal administratif de Paris. À l'audience de décembre 2009, l'État français a employé pour la première fois le mot \u00ab pillage \u00bb.", "Lire la presse"),
    "ko": ("외규장각 반환 소송", "김중호 변호사는 2007년부터 파리 행정법원에서 외규장각 의궤 반환 소송을 맡아 왔습니다. 2009년 12월 변론에서 프랑스 정부는 처음으로 '약탈'이라는 표현을 사용했습니다.", "언론 보도 보기"),
}


_I = {
 "globe": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18"/></svg>',
 "swap": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M4 8h15M15 4l4 4-4 4M20 16H5M9 12l-4 4 4 4"/></svg>',
 "build": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M4 21V8l6-3v16M10 21h10V11l-6-2M14 14h2M14 18h2"/></svg>',
}
# (icon, title, text, [(tag, service id)])
WHO = {
 "en": {"kicker": "Archè · International business law", "h": "Who we work with",
  "lede": "Legal counsel for businesses operating across borders, from market entry to international growth and complex commercial matters.",
  "cta_h": "Navigating a cross-border legal challenge?", "cta_p": "Let's discuss your business and how we can help.", "cta_b": "Discuss your matter",
  "cards": [
   ("globe", "International businesses coming to France and Europe", "For foreign companies establishing or expanding their presence in France and Europe.", [("Market entry", "advice"), ("Corporate structuring", "corporate"), ("Employment", "employment"), ("Commercial contracts", "corporate")]),
   ("swap", "French and European businesses going abroad", "For French and European companies entering new markets abroad, negotiating cross-border partnerships and managing legal risks across jurisdictions.", [("International expansion", "advice"), ("Partnerships", "corporate"), ("Compliance", "advice"), ("Disputes", "litigation")]),
   ("build", "Entrepreneurs, startups and growing businesses", "For founders, SMEs and independent professionals seeking practical legal support to structure, operate and grow their businesses.", [("Business formation", "corporate"), ("Contracts", "corporate"), ("Employment", "employment"), ("Restructuring", "corporate")])]},
 "fr": {"kicker": "Archè · Droit international des affaires", "h": "Qui nous accompagnons",
  "lede": "Conseil juridique pour les entreprises qui opèrent au-delà des frontières, de l'implantation à la croissance internationale et aux dossiers commerciaux complexes.",
  "cta_h": "Un enjeu juridique transfrontalier ?", "cta_p": "Parlons de votre activité et de la manière dont nous pouvons vous aider.", "cta_b": "Parlez-nous de votre dossier",
  "cards": [
   ("globe", "Entreprises internationales qui s'implantent en France et en Europe", "Pour les entreprises étrangères qui s'établissent ou se développent en France et en Europe.", [("Implantation", "advice"), ("Structuration juridique", "corporate"), ("Droit du travail", "employment"), ("Contrats commerciaux", "corporate")]),
   ("swap", "Entreprises françaises et européennes qui se développent à l'étranger", "Pour les entreprises françaises et européennes qui abordent de nouveaux marchés, négocient des partenariats transfrontaliers et maîtrisent les risques juridiques dans plusieurs juridictions.", [("Développement international", "advice"), ("Partenariats", "corporate"), ("Conformité", "advice"), ("Contentieux", "litigation")]),
   ("build", "Entrepreneurs, startups et entreprises en croissance", "Pour les fondateurs, PME et indépendants qui cherchent un appui juridique concret pour structurer, exploiter et développer leur activité.", [("Création d'entreprise", "corporate"), ("Contrats", "corporate"), ("Droit du travail", "employment"), ("Restructuration", "corporate")])]},
 "ko": {"kicker": "아르케 · 국제 비즈니스 법", "h": "이런 고객과 함께합니다",
  "lede": "국경을 넘어 사업하는 기업을 위한 법률 자문. 시장 진출에서 해외 성장, 복잡한 상사 사안까지.",
  "cta_h": "국경을 넘는 법적 과제를 안고 계신가요?", "cta_p": "귀사의 사업과 저희가 어떻게 도울 수 있는지 이야기해 보시죠.", "cta_b": "사안 상담하기",
  "cards": [
   ("globe", "프랑스·유럽에 진출하는 해외 기업", "프랑스와 유럽에 진출하거나 사업을 확장하려는 해외 기업을 위해.", [("시장 진출", "advice"), ("법인 구조 설계", "corporate"), ("노동·고용", "employment"), ("상사 계약", "corporate")]),
   ("swap", "해외로 진출하는 프랑스·유럽 기업", "새로운 해외 시장에 진출하고, 국경을 넘는 파트너십을 협상하며, 여러 관할의 법적 리스크를 관리하려는 프랑스·유럽 기업을 위해.", [("해외 확장", "advice"), ("파트너십", "corporate"), ("컴플라이언스", "advice"), ("분쟁", "litigation")]),
   ("build", "창업가, 스타트업, 성장 기업", "사업을 구조화하고 운영하고 키우는 데 실무적인 법률 지원이 필요한 창업가, 중소기업, 독립 전문가를 위해.", [("법인 설립", "corporate"), ("계약", "corporate"), ("노동·고용", "employment"), ("구조조정", "corporate")])]},
}


# Direction labels (firm's request, Oct 2026): inbound vs outbound international business.
WHO_DIR = {
 "en": {"globe": "Inbound", "swap": "Outbound", "build": "Start and grow"},
 "fr": {"globe": "Entrant", "swap": "Sortant", "build": "Créer et croître"},
 "ko": {"globe": "인바운드", "swap": "아웃바운드", "build": "창업과 성장"},
}


def who_cards(lang):
    out = ""
    for ico, title, text, tags in WHO[lang]["cards"]:
        links = "".join(f'<li><a href="{rel(lang, "home", lang, "services")}#{sid}">{e(lbl)}</a></li>' for lbl, sid in tags)
        dl = WHO_DIR[lang].get(ico, "")
        dlab = f'<p class="who-dir">{e(dl)}</p>' if dl else ""
        out += f'<div class="who-card">{dlab}<h3>{e(title)}</h3><p>{e(text)}</p><ul class="who-tags">{links}</ul></div>'
    return out


WHAT = {
 "en": {"kicker": "Archè · International business law", "learn": "Learn more", "more": "Explore our practice areas",
  "lede": "We advise businesses, founders and international groups on corporate, employment and commercial matters, combining practical legal advice with a cross-border perspective.",
  "cards": [("corporate", "Corporate, M&A and commercial contracts", "From company formation and corporate structuring to acquisitions, commercial negotiations and intellectual property, we help businesses build, operate and grow with confidence."),
            ("employment", "Employment law and workforce mobility", "We advise employers on French employment law, workplace relations and employment disputes, as well as the legal aspects of international workforce mobility, from recruitment to termination."),
            ("litigation", "Disputes, debt recovery and insolvency", "We represent businesses in litigation and arbitration, pursue debt recovery and advise on insolvency-related matters, developing a strategy tailored to each case from the outset through resolution."),
            ("advice", "International business and cross-border transactions", "We support international projects involving multiple jurisdictions, coordinate with local counsel and help businesses navigate differences in legal systems, regulatory requirements and commercial practices.")]},
 "fr": {"kicker": "Archè · Droit international des affaires", "learn": "En savoir plus", "more": "Découvrir nos expertises",
  "lede": "Nous conseillons les entreprises, les fondateurs et les groupes internationaux en droit des sociétés, droit du travail et droit commercial, en alliant conseil juridique pratique et regard transfrontalier.",
  "cards": [("corporate", "Sociétés, fusions-acquisitions et contrats commerciaux", "De la création de société et de la structuration aux acquisitions, négociations commerciales et propriété intellectuelle, nous aidons les entreprises à se construire, à opérer et à se développer en confiance."),
            ("employment", "Droit du travail et mobilité internationale", "Nous conseillons les employeurs en droit du travail français, relations de travail et contentieux, ainsi que sur les aspects juridiques de la mobilité internationale des salariés, du recrutement à la rupture."),
            ("litigation", "Contentieux, recouvrement et procédures collectives", "Nous représentons les entreprises en contentieux et en arbitrage, menons des recouvrements de créances et conseillons sur les procédures collectives, avec une stratégie adaptée à chaque dossier, de l'origine à son issue."),
            ("advice", "Affaires internationales et opérations transfrontalières", "Nous accompagnons des projets internationaux impliquant plusieurs juridictions, coordonnons avec des conseils locaux et aidons les entreprises à s'orienter entre systèmes juridiques, exigences réglementaires et pratiques commerciales.")]},
 "ko": {"kicker": "아르케 · 국제 비즈니스 법", "learn": "자세히 보기", "more": "업무분야 전체 보기",
  "lede": "기업, 창업가, 국제 그룹을 대상으로 기업법·노동법·상사 사안을 자문하며, 실무적인 법률 자문과 국경을 넘는 시각을 결합합니다.",
  "cards": [("corporate", "기업법·M&A·상사 계약", "회사 설립과 구조 설계, 인수, 상사 협상, 지식재산에 이르기까지 기업이 자신 있게 구축하고 운영하고 성장하도록 돕습니다."),
            ("employment", "노동법 및 인력 이동", "프랑스 노동법, 노사 관계, 노동 분쟁은 물론 채용부터 종료까지 국제 인력 이동의 법적 측면에 대해 사용자를 자문합니다."),
            ("litigation", "분쟁·채권 회수·도산", "소송과 중재에서 기업을 대리하고 채권 회수를 진행하며 도산 관련 사안을 자문하고, 사건마다 처음부터 종결까지 맞춤 전략을 세웁니다."),
            ("advice", "국제 비즈니스 및 국경 간 거래", "여러 관할이 얽힌 국제 프로젝트를 지원하고 현지 변호사와 협력하며, 법체계·규제 요건·상관행의 차이를 헤쳐 나가도록 돕습니다.")]},
}


SIGNATURE = {
    "en": {"kicker": "Signature", "h": "A Paris firm with Korean roots",
           "case_more": "Read about the case",
           "first_h": "One of the first Korean lawyers admitted to the French bar",
           "first_p": "Admitted to the Paris Bar in 1998, James Joong-ho Kim is one of the first Korean lawyers to practise in France.",
           "first_more": "Read the coverage", "src": "Reported by:"},
    "fr": {"kicker": "Repères", "h": "Un cabinet parisien aux racines coréennes",
           "case_more": "En savoir plus sur l'affaire",
           "first_h": "L'un des premiers avocats coréens inscrits au barreau en France",
           "first_p": "Inscrit au Barreau de Paris en 1998, James Joong-ho Kim est l'un des premiers avocats coréens à exercer en France.",
           "first_more": "Lire la presse", "src": "Selon :"},
    "ko": {"kicker": "대표 이력", "h": "한국에 뿌리를 둔 파리 로펌",
           "case_more": "사건 자세히 보기",
           "first_h": "프랑스 변호사회에 등록한 첫 한국인 변호사 중 한 명",
           "first_p": "1998년 파리 변호사회에 등록한 김중호 변호사는 프랑스에서 활동한 첫 한국인 변호사 중 한 명입니다.",
           "first_more": "보도 보기", "src": "보도:"},
}
TEAM_H = {"en": ("Who will handle your matter", "Partner-led work in French, English and Korean."),
          "fr": ("Qui suivra votre dossier", "Des dossiers suivis par les associés, en français, en anglais et en coréen."),
          "ko": ("사안을 담당할 변호사", "파트너가 직접 맡아 한국어, 프랑스어, 영어로 진행합니다.")}
NETWORK = {"en": "Through long-standing cooperation with local law firms, we also advise in other countries across Europe, Asia, Africa and the Middle East.",
           "fr": "Grâce à une coopération de longue date avec des cabinets locaux, nous intervenons aussi dans d'autres pays d'Europe, d'Asie, d'Afrique et du Moyen-Orient.",
           "ko": "현지 로펌들과의 오랜 협력 관계를 통해 유럽, 아시아, 아프리카, 중동의 다른 국가에서도 자문을 제공합니다."}
CLOSE = {"en": ("Your business. Your challenges. Our legal expertise.", "Discuss your matter", "Get in touch in English, French or Korean."),
         "fr": ("Votre activité. Vos enjeux. Notre expertise juridique.", "Parlez-nous de votre dossier", "Écrivez-nous en français, en anglais ou en coréen."),
         "ko": ("귀사의 비즈니스. 귀사의 과제. 아르케의 법률 전문성.", "사안 상담하기", "한국어, 프랑스어, 영어로 문의해 주세요.")}


def what_compact(lang):
    import content_services as CS
    svc = rel(lang, "home", lang, "services")
    return "".join(f'<li><a href="{svc}#{sid}">{e(title)}</a></li>' for sid, title, _, _ in CS.SERVICES8[lang])


def what_cards(lang):
    out = ""
    import content_services as CS
    cards = [(sid, title, " · ".join(term for term, _ in rows[:4])) for sid, title, _, rows in CS.SERVICES8[lang]]
    for sid, title, text in cards:
        href = f'{rel(lang, "home", lang, "services")}#{sid}'
        out += (f'<div class="what-card"><h3>{e(title)}</h3><p>{e(text)}</p>'
                f'<a class="what-link" href="{href}" aria-label="{e(WHAT[lang]["learn"])}: {e(title)}">{e(WHAT[lang]["learn"])} →</a></div>')
    return out


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
<a class="brand" href="{rel(lang, page, lang, "home")}" aria-label="{e(C.FIRM)}"><img class="brand-logo" src="{up}assets/logo-horizontal-dark.svg" width="491" height="132" alt=""></a>
<button class="nav-toggle" aria-expanded="false" aria-controls="primary-nav" type="button">{e(t["menu"])}</button>
<nav class="primary" id="primary-nav" aria-label="{e(t["menu"])}">{nav}<div class="lang" role="group" aria-label="Language">{switch}</div></nav>
</div></header>'''


def cta_href(lang, page):
    # The firm prefers first contact by email; a booking link, if set, takes over.
    return C.BOOKING_URL or f"mailto:{C.EMAIL}"


def footer(lang, page, t):
    f = t["footer"]
    up = "../" * depth(lang, page)
    links = "".join(f'<li><a href="{rel(lang, page, lang, k)}">{e(t["nav"][k])}</a></li>' for k in NAV)
    soc = (f'<li><a href="{C.LINKEDIN}" rel="noopener">LinkedIn</a></li><li><a href="{C.INSTAGRAM}" rel="noopener">Instagram</a></li>'
           + "".join(f'<li><a href="{e(u)}" rel="noopener">{e(l)}</a></li>' for l, u in C.FOOTER_PERSONAL))
    return f'''<footer class="site-footer"><div class="wrap">
<div class="cols c4">
<div><a href="{rel(lang, page, lang, "home")}" aria-label="{e(C.FIRM)}" class="ft-logo"><img src="{up}assets/logo-horizontal-dark.svg" width="491" height="132" alt=""></a><p class="ft-legal">{e(C.FIRM_FULL)}</p></div>
<div><h2 class="ft-h">{e(f["nav"])}</h2><ul>{links}</ul></div>
<div><h2 class="ft-h">{e(t["home"]["offices_h"])}</h2><ul><li>Paris: {e(", ".join(C.ADDRESS_LINES[:2]))}</li><li>Seoul</li><li>Hong Kong</li></ul></div>
<div><h2 class="ft-h">{e(f["follow"])}</h2><ul>{soc}</ul></div>
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
<link rel="preload" href="{up}assets/fonts/barlow-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin><link rel="stylesheet" href="{up}assets/style.css?v={CSS_V}">
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


def follow_card(lang, text):
    fl = {"en": ("Follow", "See more"), "fr": ("Suivre", "Voir plus"), "ko": ("팔로우", "더 보기")}[lang]
    head = {"en": ("Follow · Archè", "The firm: website, news and updates."),
            "fr": ("Suivre · Archè", "Le cabinet : site, actualités et mises à jour."),
            "ko": ("팔로우 · 아르케", "법인 웹사이트, 소식 및 업데이트.")}[lang]
    rows = "".join(
        f'<div class="fc-row"><span class="fc-ico" aria-hidden="true">{ico}</span><div class="fc-name"><strong>{e(name)}</strong><span>{e(handle)}</span></div>'
        f'<a class="btn ghost fc-btn" href="{e(url)}" rel="noopener">{e(lbl)} ↗</a></div>'
        for name, handle, url, lbl, ico in [
            ("LinkedIn", "archelegalparis", C.LINKEDIN, fl[0], "in"),
            ("Instagram", "@archelegal", C.INSTAGRAM, fl[0], "◎"),
            ("Website", C.SITE_URL.replace("https://", ""), C.SITE_URL, fl[1], "◍"),
        ])
    return (f'<div class="follow-card"><div class="fc-head"><img class="fc-logo" src="assets/logo-mark.png" width="38" height="48" alt="">'
            f'<div><strong>{e(head[0])}</strong><p>{e(head[1])}</p></div></div><div class="fc-list">{rows}</div></div>')


def page_home(lang, t):
    h = t["home"]
    svc = t["services"]["items"]
    svcs = "".join(f'<div class="rule-top"><h3><a href="{rel(lang, "home", lang, "services")}#{s[0]}" style="color:inherit;text-decoration:none">{e(s[1])}</a></h3><p>{e(s[2])}</p></div>' for s in svc)
    creds = "".join(f'<div class="rule-top"><h3 style="font-size:1.1rem">{e(a)}</h3><p>{e(b)}</p></div>' for a, b in h["creds"])
    inds = "".join(f'<div class="ind">{f"<h3>{e(g)}</h3>" if g else ""}<ul>' + "".join(f"<li>{e(x)}</li>" for x in items) + "</ul></div>" for g, items in h["industries"])
    def office(name, d, main=False):
        extra = ""
        if main:
            extra = f'<p>{"<br>".join(e(x) for x in C.ADDRESS_LINES)}</p><p><a href="mailto:{C.EMAIL}">{e(C.EMAIL)}</a><br><a href="tel:{C.PHONE_TEL}">{e(C.PHONE)}</a></p>'
        else:
            if d.get("address"):
                extra += f'<p>{e(d["address"])}</p>'
            if d.get("phone"):
                extra += f'<p><a href="tel:{e(d["phone"])}">{e(d["phone"])}</a></p>'
            if d.get("address") and d.get("email"):
                extra += f'<p><a href="mailto:{e(d["email"])}">{e(d["email"])}</a></p>'
            if not extra:
                extra = f'<p>{e(h["contact_office"])}: <a href="mailto:{C.EMAIL}">{e(C.EMAIL)}</a></p>'
        tag = f'<p><strong>{e(h["main_office"])}</strong></p>' if main else ""
        return f'<div class="office"><h3>{e(name)}</h3>{tag}{extra}</div>'
    offices = office(h["cities"]["paris"], {}, True) + office(h["cities"]["seoul"], C.SEOUL) + office(h["cities"]["hk"], C.HONGKONG)
    press = ""
    if C.PRESS:
        press = f'''<section><div class="wrap"><div class="section-head"><h2>{e(h["press_h"])}</h2><p class="lede">{e(h["press_p"])}</p></div>
<div class="press">''' + press_items(lang, (press_featured() or C.PRESS)[:4], "../" * depth(lang, "home")) + f'</div><p style="margin-top:20px"><a href="{rel(lang, "home", lang, "insights")}">{e(h["press_more"])}</a></p></div></section>'
    mt = ""
    if t.get("matters"):
        import experience6 as X6, content_services as CS
        area_title = {sid: title for sid, title, _, _ in CS.SERVICES8[lang]}
        svc_url = rel(lang, "home", lang, "services")
        firsts = "".join(f'<div class="rule-top"><h3 style="font-size:1.05rem"><a href="{svc_url}#{sid}" style="color:inherit;text-decoration:none">{e(area_title[sid])}</a></h3><p>{e(txt)}</p></div>' for sid, txt in X6.featured(lang))
        mt = f'''<section><div class="wrap"><div class="section-head"><h2>{e(h["matters_h"])}</h2></div>
<div class="cols c3">{firsts}</div><p style="margin-top:28px"><a href="{svc_url}">{e(h["matters_more"])}</a></p></div></section>'''
    up = "../" * depth(lang, "home")
    cov = {"en": ("International boutique law firm", "Paris · Seoul · Hong Kong", "Enter the site"), "fr": ("Cabinet d'avocats international", "Paris · Séoul · Hong Kong", "Découvrir le cabinet"), "ko": ("국제 부티크 로펌", "파리 · 서울 · 홍콩", "사이트 둘러보기")}[lang]
    hc = {"en": {"label": "Contact", "kicker": "Write to us", "cities": "Paris · Seoul · Hong Kong", "note": "Write in English, French or Korean."}, "fr": {"label": "Contact", "kicker": "Écrivez-nous", "cities": "Paris · Séoul · Hong Kong", "note": "En français, en anglais ou en coréen."}, "ko": {"label": "문의", "kicker": "문의하기", "cities": "파리 · 서울 · 홍콩", "note": "한국어, 프랑스어, 영어로 문의해 주세요."}}[lang]
    sig = SIGNATURE[lang]
    sig_html = (f'<section class="alt signature" aria-labelledby="sig-h"><div class="wrap"><div class="section-head"><p class="kicker">{e(sig["kicker"])}</p><h2 id="sig-h">{e(sig["h"])}</h2></div><div class="cols c2">'
                f'<div class="sig-card"><h3>{e(HERITAGE[lang][0])}</h3><p>{e(HERITAGE[lang][1])}</p><a class="sig-link" href="{rel(lang, "home", lang, "insights")}#oegyujanggak">{e(sig["case_more"])} →</a></div>'
                f'<div class="sig-card"><h3>{e(sig["first_h"])}</h3><p>{e(sig["first_p"])}</p><p class="sig-src">{e(sig["src"])} ' + ", ".join(f'<a href="{e(p["url"])}" rel="noopener" target="_blank">{e(p["outlet"][lang])} ({e(p["date"][:4])})</a>' for p in press_featured()[:3]) + f'</p><a class="sig-link" href="{rel(lang, "home", lang, "insights")}#press-profile">{e(sig["first_more"])} →</a></div>'
                '</div></div></section>')
    import team_profiles as TP
    team_cards = "".join(
        f'<a class="tm-card" href="{rel(lang, "home", lang, "people")}#{p["slug"]}"><img src="{up}{e(p["photo"])}" alt="" width="240" height="300" loading="lazy" decoding="async">'
        f'<span class="tm-name">{e(p["name"])}</span><span class="tm-role">{e(t["people"]["roles"][p["slug"]])}</span><span class="tm-lang">{e(TP.PROFILES[p["slug"]][lang]["lang"])}</span></a>'
        for p in C.PEOPLE if p.get("photo"))
    team_html = (f'<section aria-labelledby="tm-h"><div class="wrap"><div class="section-head"><h2 id="tm-h">{e(TEAM_H[lang][0])}</h2><p class="lede">{e(TEAM_H[lang][1])}</p></div>'
                 f'<div class="tm-grid">{team_cards}</div></div></section>')
    close = CLOSE[lang]
    close_html = (f'<section class="alt close-line"><div class="wrap"><div><h2 class="close-h">{e(close[0])}</h2><p class="close-p">{e(close[2])}</p></div>'
                  f'<a class="btn" href="{cta_href(lang, "home")}">{e(close[1])}</a></div></section>')
    primary = {"en": "Discuss your matter", "fr": "Parlez-nous de votre dossier", "ko": "사안 상담하기"}[lang]
    secondary = {"en": "Explore our expertise", "fr": "Découvrir nos expertises", "ko": "업무분야 보기"}[lang]
    strip = ('<section class="cred-strip strip-b" aria-label="' + e(h["strip"][0][0]) + '"><div class="wrap"><dl>'
             + "".join("<div><dt>" + e(a) + "</dt><dd>" + " ".join('<span class="nw">' + e(x) + ("&nbsp;·" if i < len(c.split(" · ")) - 1 else "") + "</span>" for i, x in enumerate(c.split(" · "))) + "</dd></div>" for a, c in h["strip"])
             + "</dl></div></section>")
    body = f"""<section class="landing" style="background-image:url('{up}assets/img/landing-bg.webp')" aria-hidden="true"></section>
<div id="hero-start"></div>
<section class="hero hero-b" aria-labelledby="hero-name"><div class="wrap">
<h1 class="hero-name" id="hero-name"><span class="hn-line"><span lang="fr">Archè</span> <span class="hero-name-ko" lang="ko">아르케</span></span><span class="hero-sub">{e(h["h1"])}</span></h1>
<p class="hero-cities">{e(cov[1])}</p><p class="lede">{e(h["lede"])}</p>
<div class="actions"><a class="btn" href="{cta_href(lang, "home")}">{e(primary)}</a><a class="btn ghost" href="{rel(lang, "home", lang, "services")}">{e(secondary)}</a></div>
</div></section>
{strip}
<section class="what"><div class="wrap"><div class="section-head"><p class="kicker">{e(WHAT[lang]["kicker"])}</p><h2>{e(h["services_h"])}</h2><p class="lede">{e(WHAT[lang]["lede"])}</p></div><ul class="what-compact">{what_compact(lang)}</ul>
<p class="what-more"><a href="{rel(lang, "home", lang, "services")}">{e(WHAT[lang]["more"])} →</a></p></div></section>
<section class="alt who"><div class="wrap"><div class="section-head"><h2>{e(WHO[lang]["h"])}</h2><p class="lede">{e(WHO[lang]["lede"])}</p></div><div class="cols c3">{who_cards(lang)}</div><div class="who-cta"><div><p class="who-cta-h">{e(WHO[lang]["cta_h"])}</p><p>{e(WHO[lang]["cta_p"])}</p></div><a class="btn ghost" href="{cta_href(lang, "home")}">{e(WHO[lang]["cta_b"])} ↗</a></div></div></section>
{mt}
{sig_html}
{team_html}
<section class="alt"><div class="wrap"><div class="section-head"><h2>{e(h["industries_h"])}</h2><p class="lede">{e(h["industries_p"])}</p></div><div class="industries">{inds}</div></div></section>
<section><div class="wrap"><div class="section-head"><h2>{e(h["offices_h"])}</h2><p class="lede">{e(NETWORK[lang])}</p></div><div class="offices">{offices}</div></div></section>
<section class="alt"><div class="wrap aff"><h2 class="aff-h">{AFF_H[lang]}</h2><ul class="aff-list">{"".join(f"<li>{e(x)}</li>" for x in AFFILIATIONS)}</ul></div></section>
{press}
{close_html}"""
    return body


def page_services(lang, t):
    s = t["services"]
    items = ""
    for key, title, intro, bullets in s["items"]:
        if bullets and isinstance(bullets[0], tuple):
            rows = "".join(f'<div><dt>{e(term)}</dt>' + (f'<dd>{e(desc)}</dd>' if desc else '') + '</div>' for term, desc in bullets)
            body = f'<dl class="svc-dl">{rows}</dl>'
        else:
            body = "<ul>" + "".join(f"<li>{e(b)}</li>" for b in bullets) + "</ul>"
        import experience6 as X6
        ex_html = ""
        exl = {"en": ("Key examples", "See all"), "fr": ("Exemples de dossiers", "Voir tout"), "ko": ("주요 사례", "전체 보기")}[lang]
        for kind, sub, data in X6.examples(lang).get(key, []):
            if kind == "rows":
                lis = [f'<li><strong>{e(n)}</strong> — {e(tx)}</li>' for n, tx in data]
            elif kind == "names":
                lis = [f'<li class="ex-names">{" · ".join(e(n) for n in data)}</li>']
            elif kind == "text":
                lis = [f'<li class="ex-names">{e(" · ".join(data))}</li>']
            else:
                lis = [f'<li><strong>{e(c)}</strong> — {e(" · ".join(ns))}</li>' for c, ns in data]
            head, tail = "".join(lis[:3]), "".join(lis[3:])
            more = f'<details class="ex-more"><summary>{e(exl[1])} ({len(lis)})</summary><ul class="ex-list">{tail}</ul></details>' if tail else ""
            ex_html += f'<p class="ex-sub">{e(sub)}</p><ul class="ex-list">{head}</ul>{more}'
        ex_block = f'<div class="ex"><h3 class="ex-h">{e(exl[0])}</h3>{ex_html}</div>' if ex_html else ""
        svc_cta = f'<p class="svc-cta"><a href="{cta_href(lang, "services")}">{e(t["cta"])} →</a></p>'
        items += f'<div class="service" id="{key}"><div><p class="svc-sub">{e(intro)}</p><h2>{e(title)}</h2></div>{body}{ex_block}{svc_cta}</div>'
    faq = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in s["faq"])
    ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in s["faq"]]}
    idx = ""
    services_js = """<script>(function(){var list=document.getElementById('services-list');if(!list)return;var chips=document.querySelectorAll('.practice-chip');var blocks=list.querySelectorAll('.service');function show(g){blocks.forEach(function(b){b.hidden=(g!=='all'&&b.id!==g)});chips.forEach(function(c){var on=c.getAttribute('data-group')===g;if(c.tagName==='BUTTON'){c.setAttribute('aria-pressed',String(on))}else if(on){c.setAttribute('aria-current','true')}else{c.removeAttribute('aria-current')}});}chips.forEach(function(c){c.addEventListener('click',function(ev){var g=c.getAttribute('data-group');ev.preventDefault();show(g);if(history.replaceState)history.replaceState(null,'','#'+(g==='all'?'services-list':g));list.scrollIntoView({behavior:'smooth',block:'start'});});});var h=location.hash.slice(1);if(h&&h!=='services-list'&&document.getElementById(h)&&h!=='all'){show(h);}})();</script>"""
    if s.get("index"):
        all_lbl = {"en": "All", "fr": "Tous", "ko": "전체"}[lang]
        chips = f'<button type="button" class="practice-chip" data-group="all" aria-pressed="true">{e(all_lbl)}</button>'
        chips_by_group = "".join(f'<li><a class="practice-chip" href="#{k}" data-group="{k}">{e(lbl)}</a></li>' for lbl, k in s["index"])
        idx = f'<nav class="practice-index" aria-labelledby="pi-h"><h2 id="pi-h">{e(s["index_h"])}</h2><div class="practice-all">{chips}</div><ul class="practice-chips">{chips_by_group}</ul></nav>'

    import experience6 as X6
    figs, _ = X6.figures(lang)
    fig_note = {"en": "Indicative annual figures from the firm's records.", "fr": "Chiffres annuels indicatifs issus des dossiers du cabinet.", "ko": "아르케 업무 기록에 따른 연간 참고 수치입니다."}[lang]
    fh, fl = X6.FIG_HEAD[lang]
    prof, _ = X6.client_profile(lang)
    prof_h = {"en": "Client profile", "fr": "Profil des clients", "ko": "고객 구성"}[lang]
    prof_html = f'<div class="profile"><p class="profile-h">{e(prof_h)}</p><dl>' + "".join(f'<div><dt>{e(a)}</dt><dd>{e(c)}</dd></div>' for a, c in prof) + '</dl></div>'
    fig_html = f'<div class="figs"><h2 class="figs-h">{e(fh)}</h2><p class="figs-l">{e(fl)}</p><dl>' + "".join(f'<div><dt>{e(v)}</dt><dd><span class="fig-t">{e(a)}</span><span class="fig-c">{e(c)}</span></dd></div>' for v, a, c in figs) + f'</dl>{prof_html}<p class="figs-note">{e(fig_note)}</p></div>'
    return f'''<div class="page-head"><div class="wrap"><h1>{e(s["h1"])}</h1><p class="lede">{e(s["lede"])}</p>{fig_html}{idx}</div></div>
<section style="padding-top:0"><div class="wrap" id="services-list">{items}</div><div class="wrap"><p class="xp-note">{e(X6.FOOTNOTE[lang])}</p></div></section>
{services_js}
<section class="alt"><div class="wrap"><div class="section-head"><h2>{e(s["faq_h"])}</h2></div><div class="faq" style="max-width:760px">{faq}</div></div></section>
{cta_band(lang, "services", t, s["cta_h"], s["cta_p"])}''', '<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False) + "</script>"


AFFILIATIONS = [
    "European Law Institute (ELI)", "France Esports", "France-Korea Chamber of Commerce and Industry (CCICF)",
    "French Association for Competition Law Studies (AFEC)", "Impulse Partners",
    "Korea Creative Content Agency (KOCCA)", "Korea Deposit Insurance Corporation (KDIC)",
    "International Association of Korean Lawyers (IAKL)", "Mensa", "Paris 2024 Olympic & Paralympic Games",
    "Samsung Electronics UK", "Station F · HEC Incubator", "Korean Commercial Arbitration Board (KCAB)",
    "In-house Counsels Forum (IHCF)", "Embassy of Korea in France", "KOTRA Paris",
]
AFF_H = {"en": "Experience & affiliations", "fr": "Expériences et affiliations", "ko": "경력 및 소속"}


def page_people(lang, t):
    p = t["people"]
    out = cards = ""
    for person in C.PEOPLE:
        k = person["slug"]
        lis = "".join(f"<li>{e(x)}</li>" for x in p["bios"][k])
        up = "../" * depth(lang, "people")
        av = (f'<img src="{up}{e(person["photo"])}" alt="{e(t["people"].get("photo_alt", "{}").format(person["name"]))}" width="480" height="600" loading="lazy" decoding="async">'
              if person["photo"] else e(person["initials"]))
        btns = []  # email now sits under the lead (pf-contact); this row keeps the profile links
        if person["linkedin"]:
            btns.append(("LinkedIn", person["linkedin"], None))
        btns += [(lbl, url, None) for lbl, url in person.get("links", [])]
        links = '<ul class="person-links">' + "".join(
            f'<li><a class="pl-btn" href="{e(url)}"' + ("" if url.startswith("mailto:") else ' rel="noopener"')
            + (f' title="{e(tip)}"' if tip else "") + f'>{e(lbl)}</a></li>' for lbl, url, tip in btns) + "</ul>" if btns else ""
        import team_profiles as TP, content_services as CS
        pr, L = TP.PROFILES[k][lang], TP.LABELS[lang]
        area_title = {sid: title for sid, title, _, _ in CS.SERVICES8[lang]}
        svc = rel(lang, "people", lang, "services")
        def area(a):
            # A plain string is a Services section: same label and anchor as the Services page.
            # (None, labels) is an area with no Services section, shown as a tag without a link.
            if isinstance(a, tuple):
                return f'<li><span class="pf-area is-static">{e(a[1][lang])}</span></li>'
            return f'<li><a class="pf-area" href="{svc}#{a}">{e(area_title[a])}</a></li>'
        areas = "".join(area(a) for a in TP.PROFILES[k]["areas"])
        facts = "".join(f'<div><dt>{e(L[f])}</dt><dd>{e(pr[f])}</dd></div>' for f in ("bar", "lang"))
        def plist(key, keep=None):
            items = pr[key]
            if not items:
                return ""
            head = "".join(f"<li>{e(x)}</li>" for x in (items[:keep] if keep else items))
            rest = items[keep:] if keep else []
            tail = "".join(f"<li>{e(x)}</li>" for x in rest)
            more = (f'<details class="see-more"><summary>{e(L["more"].format(n=len(rest)))}</summary>'
                    f'<ul class="pf-list">{tail}</ul></details>') if rest else ""
            return f'<h3 class="pf-h">{e(L[key])}</h3><ul class="pf-list">{head}</ul>{more}'
        roles = plist("career") + plist("edu", 3) + plist("roles", TP.PROFILES[k].get("roles_keep", 4))
        first = person["name"].split()[0]
        dl = [(L["vcard"], up + f"assets/downloads/{k}.vcf", f"{k}.vcf")]
        for key, lbl in (("card", "card"), ("card_back", "card_back")):
            if person.get(key):
                dl.insert(0 if key == "card" else 1, (L[lbl], up + person[key], person[key].rsplit("/", 1)[1]))
        downloads = ('<ul class="person-downloads">' + "".join(
            f'<li><a class="pl-btn" href="{e(href)}" download="{e(fname)}">{e(lbl)}</a></li>' for lbl, href, fname in dl) + "</ul>")
        mail = (f'<p class="pf-contact"><a class="btn pf-mail" href="mailto:{e(person["email"])}">'
                f'{e(L["email"].format(first=first))}</a>'
                + (f' <a class="btn pf-mail pf-card" href="{up}{e(person["card"])}" download="{e(person["card"].rsplit("/", 1)[1])}">'
                   f'{e(L["card_btn"])}</a>' if person.get("card_btn") else "")
                + (f' <a class="btn pf-mail pf-card" href="{up}assets/downloads/{k}.vcf" download="{k}.vcf">'
                   f'{e(L["vcard"])}</a>' if person.get("card_btn") else "")
                + '</p>')
        out += (f'<article class="person" id="{k}"><div class="avatar" aria-hidden="{"false" if person["photo"] else "true"}">{av}</div><div class="pf">'
                f'<h2 class="pf-name">{e(person["name"])}</h2><p class="role">{e(p["roles"][k])}</p>'
                f'<p class="pf-lead">{e(pr["lead"])}</p>{mail}'
                f'<h3 class="pf-h">{e(L["areas"])}</h3><ul class="pf-areas">{areas}</ul>'
                f'<dl class="pf-facts">{facts}</dl>{roles}{links}{downloads}</div></article>')
        thumb = (f'<img src="{up}{e(person["photo"])}" alt="" width="96" height="120" loading="lazy" decoding="async">'
                 if person["photo"] else f'<span aria-hidden="true">{e(person["initials"])}</span>')
        cards += (f'<li><a class="tov-card" href="#{k}">{thumb}<span class="tov-txt"><span class="tov-name">{e(person["name"])}</span>'
                  f'<span class="tov-role">{e(p["roles"][k])}</span><span class="tov-lang">{e(pr["lang"])}</span></span></a></li>')
    import team_profiles as TP2
    people_ld = []
    for person in C.PEOPLE:
        k = person["slug"]; pr = TP2.PROFILES[k]["en"]
        same = [u for u in [person.get("linkedin")] + [u for _, u in person.get("links", [])] if u]
        people_ld.append({"@type": "Person", "name": person["name"], "jobTitle": t["people"]["roles"][k],
                          "worksFor": {"@type": "LegalService", "name": C.FIRM_FULL, "url": C.SITE_URL},
                          "email": "mailto:" + person["email"], "knowsLanguage": [x.split(" (")[0] for x in pr["lang"].split(" · ")],
                          **({"image": C.SITE_URL.rstrip("/") + "/" + person["photo"]} if person.get("photo") else {}),
                          **({"sameAs": same} if same else {})})
    ld = {"@context": "https://schema.org", "@graph": people_ld}
    import team_profiles as TP3
    W = WHO[lang]
    return f'''<div class="page-head"><div class="wrap"><h1>{e(p["h1"])}</h1><p class="lede">{e(p["lede"])}</p>
<nav class="team-ov" aria-label="{e(TP3.LABELS[lang]["jump"])}"><ul>{cards}</ul></nav></div></div>
<section style="padding-top:0"><div class="wrap">{out}</div></section>
{cta_band(lang, "people", t, W["cta_h"], W["cta_p"])}''', '<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False) + "</script>"


def see_more(items, lang, keep=4):
    head = "".join(f"<li>{e(x)}</li>" for x in items[:keep])
    rest = items[keep:]
    if not rest:
        return f"<ul>{head}</ul>"
    tail = "".join(f"<li>{e(x)}</li>" for x in rest)
    label = {"en": "See more", "fr": "Voir plus", "ko": "더 보기"}[lang]
    return f'<ul>{head}</ul><details class="see-more"><summary>{label}</summary><ul>{tail}</ul></details>'


def page_experience(lang, t):
    m = t["matters"]
    groups = ""
    for title, items in m["groups"]:
        groups += f'<div class="service"><div><h2>{e(title)}</h2></div>{see_more(items, lang, 6)}</div>'
    return f'''<div class="page-head"><div class="wrap"><h1>{e(m["h1"])}</h1><p class="lede">{e(m["lede"])}</p></div></div>
<section style="padding-top:0"><div class="wrap">{groups}<p class="xp-note">{e(m.get("footnote", ""))}</p></div></section>
{cta_band(lang, "experience", t, m["cta_h"], m["cta_p"])}'''


BRIDGE = {"en": "An international boutique law firm headquartered in Paris, working in French, English and Korean for businesses that cross borders.",
          "fr": "Un cabinet d'avocats international de taille humaine, basé à Paris, qui accompagne en français, en anglais et en coréen les entreprises actives à l'international.",
          "ko": "파리에 본사를 둔 부티크 국제 로펌으로, 국경을 넘나드는 기업을 한국어, 프랑스어, 영어로 지원합니다."}

CASE = {
    "en": {"kicker": "Signature historical case", "src": "Timeline from press coverage and a 2017 government case study",
           "rows": [("2007", "Restitution claim brought before the Paris Administrative Court in February."),
                    ("2009", "At the December hearing, the French State uses the word “pillage” for the first time."),
                    ("2010", "Appeal filed on 24 February after the first-instance ruling. In November, the two heads of state announce the return of the manuscripts."),
                    ("2011", "Transfer of the manuscripts to Korea completed in May.")],
           "note": "Sources: press coverage listed on this page; National Human Resources Development Institute (Korea), case study on the Korea–France Oegyujanggak negotiation, September 2017.",
           "more": "See the coverage below"},
    "fr": {"kicker": "Affaire historique", "src": "Chronologie d'après la presse et une étude de cas gouvernementale (2017)",
           "rows": [("2007", "Requête en restitution déposée en février devant le tribunal administratif de Paris."),
                    ("2009", "À l'audience de décembre, l'État français emploie pour la première fois le mot « pillage »."),
                    ("2010", "Appel interjeté le 24 février après le jugement de première instance. En novembre, les deux chefs d'État annoncent le retour des manuscrits."),
                    ("2011", "Transfert des manuscrits en Corée achevé en mai.")],
           "note": "Sources : articles de presse cités sur cette page ; Institut national de développement des ressources humaines (Corée), étude de cas sur la négociation franco-coréenne relative à l'Oegyujanggak, septembre 2017.",
           "more": "Voir la couverture ci-dessous"},
    "ko": {"kicker": "대표 역사 사건", "src": "언론 보도 및 2017년 정부 사례 연구로 본 경과",
           "rows": [("2007", "2월, 파리 행정법원에 반환 청구 소송 제기."),
                    ("2009", "12월 변론에서 프랑스 정부가 처음으로 ‘약탈’이라는 표현을 사용."),
                    ("2010", "2월 24일, 1심 판결 후 항소 제기. 11월, 한불 정상이 의궤 반환을 발표."),
                    ("2011", "5월, 의궤의 한국 이관 완료.")],
           "note": "출처: 이 페이지의 언론 보도, 국가공무원인재개발원 「한-프랑스 외규장각 의궤 반환협상 사례」(2017년 9월).",
           "more": "아래 보도 보기"},
}



CASE_SVC = {"en": "Disputes involving public bodies: our practice",
            "fr": "Contentieux impliquant des personnes publiques : notre pratique",
            "ko": "공공기관 관련 분쟁: 업무 분야 보기"}


def case_file(lang):
    c = CASE[lang]
    rows = "".join(f'<li><span class="cf-year">{y}</span><span>{e(x)}</span></li>' for y, x in c["rows"])
    return (f'<section class="case-file" id="oegyujanggak" aria-labelledby="cf-h"><div class="wrap cf-grid">'
            f'<div><p class="kicker cf-kicker">{e(c["kicker"])}</p><h2 id="cf-h">{e(HERITAGE[lang][0])}</h2><p class="lede">{e(HERITAGE[lang][1])}</p>'
            f'<p class="cf-more"><a href="#press-heritage">{e(c["more"])} ↓</a></p>'
            f'<p class="cf-more cf-svc"><a href="{rel(lang, "insights", lang, "services")}#litigation">{e(CASE_SVC[lang])} →</a></p></div>'
            f'<div class="cf-panel"><p class="cf-src">{e(c["src"])}</p><ol class="cf-timeline">{rows}</ol><p class="cf-note">{e(c.get("note", ""))}</p></div></div></section>')


PRESS_PAGE = {
 "en": {"media_btn": "Media enquiries", "latest_btn": "Latest news",
        "stat_since": "in the press since", "stat_items": "articles", "stat_outlets": "outlets", "stat_lang": "languages: Korean, English, French",
        "featured_in": "Featured in",
        "media_h": "For journalists", "media_p": "For interviews, contact the partners directly. We answer in English, French or Korean.",
        "spk_h": "Available for comment", "kit_h": "Media kit", "about_h": "About Archè",
        "about_p": "Archè (법무법인 아르케) is an international boutique law firm in Paris. It advises Asian and European businesses on corporate, employment, disputes and international projects, in English, French and Korean.",
        "logo": "Firm logo (PNG)", "photo": "Portrait of {} (WebP)", "bios": "Partner biographies", "write": "Email the press contact",
        "subject": "Press enquiry", "spk": {
            "jk": ["Korean companies entering France: company formation and administrative steps", "Restitution of cultural property: the Oegyujanggak case", "Legal practice and the judiciary in France"],
            "hk": ["Sports law and CAS arbitration (Paris 2024)", "French employment law for Korean groups' subsidiaries", "EU law, technology and regulation"]}},
 "fr": {"media_btn": "Contact presse", "latest_btn": "Dernières actualités",
        "stat_since": "dans la presse depuis", "stat_items": "articles", "stat_outlets": "médias", "stat_lang": "langues : coréen, anglais, français",
        "featured_in": "Cité par",
        "media_h": "Espace presse", "media_p": "Pour une interview, contactez directement les associés. Nous répondons en français, en anglais ou en coréen.",
        "spk_h": "Disponibles pour commenter", "kit_h": "Kit média", "about_h": "À propos d'Archè",
        "about_p": "Archè (법무법인 아르케) est un cabinet d'avocats international à Paris. Il conseille les entreprises asiatiques et européennes en droit des sociétés, droit du travail, contentieux et projets internationaux, en français, anglais et coréen.",
        "logo": "Logo du cabinet (PNG)", "photo": "Portrait de {} (WebP)", "bios": "Biographies des associés", "write": "Écrire au contact presse",
        "subject": "Demande presse", "spk": {
            "jk": ["Implantation des entreprises coréennes en France : création de société et démarches administratives", "Restitution des biens culturels : l'affaire de l'Oegyujanggak", "L'exercice du droit et la justice en France"],
            "hk": ["Droit du sport et arbitrage devant le TAS (Paris 2024)", "Droit du travail français pour les filiales de groupes coréens", "Droit de l'Union européenne, technologie et régulation"]}},
 "ko": {"media_btn": "언론 문의", "latest_btn": "최근 소식",
        "stat_since": "년부터 언론 보도", "stat_items": "건의 기사", "stat_outlets": "개 매체", "stat_lang": "개 언어: 한국어·영어·프랑스어",
        "featured_in": "보도 매체",
        "media_h": "언론 관계자용 안내", "media_p": "인터뷰는 파트너 변호사에게 직접 연락해 주십시오. 한국어, 영어, 프랑스어로 답변드립니다.",
        "spk_h": "논평 가능 분야", "kit_h": "미디어 키트", "about_h": "아르케 소개",
        "about_p": "법무법인 아르케(Archè)는 파리의 국제 부티크 로펌으로, 아시아와 유럽 기업에 기업법, 노동법, 분쟁 해결, 국제 프로젝트 자문을 한국어, 영어, 프랑스어로 제공합니다.",
        "logo": "로고 (PNG)", "photo": "{} 프로필 사진 (WebP)", "bios": "파트너 소개", "write": "언론 문의 이메일 보내기",
        "subject": "언론 문의", "spk": {
            "jk": ["한국 기업의 프랑스 진출: 법인 설립과 행정 절차", "문화재 반환: 외규장각 소송", "프랑스의 법조 실무와 사법 제도"],
            "hk": ["스포츠법과 CAS 중재(파리 2024)", "한국 기업 현지 법인을 위한 프랑스 노동법", "EU법, 기술과 규제"]}},
}


def _articles():
    return [p for p in C.PRESS if C.PRESS_THEME.get(p["url"]) != "books"]


def press_stats():
    arts = _articles()
    since = min(p["date"][:4] for p in arts)
    return since, len(arts), len({p["outlet"]["en"] for p in arts}), len({p["lang"] for p in arts})


def outlet_strip(lang, n=8):
    from collections import Counter
    cnt = Counter(p["outlet"][lang] for p in _articles())
    return " · ".join(e(o) for o, _ in cnt.most_common(n))


def press_ld(lang):
    items = []
    for i, p in enumerate(C.PRESS, 1):
        book = C.PRESS_THEME.get(p["url"]) == "books"
        it = {"@type": "Book" if book else "NewsArticle", "url": p["url"], "inLanguage": p["lang"], "datePublished": p["date"]}
        it["name" if book else "headline"] = p["title"]
        if not book:
            it["publisher"] = {"@type": "Organization", "name": p["outlet"]["en"]}
        items.append({"@type": "ListItem", "position": i, "item": it})
    d = {"@context": "https://schema.org", "@type": "CollectionPage", "name": T[lang]["meta"]["insights"][0],
         "url": abs_url(lang, "insights"), "inLanguage": lang,
         "about": {"@type": "LegalService", "name": C.FIRM_FULL, "url": C.SITE_URL},
         "mainEntity": {"@type": "ItemList", "numberOfItems": len(items), "itemListElement": items}}
    return '<script type="application/ld+json">' + json.dumps(d, ensure_ascii=False) + "</script>"


def media_kit(lang, up):
    m = PRESS_PAGE[lang]
    people = {p["slug"]: p for p in C.PEOPLE}
    team = rel(lang, "insights", lang, "people")
    spk = ""
    for k in ("jk", "hk"):
        pp = people[k]
        import press_extra as PX
        tl = PX.HK_TOPICS[lang] if k == "hk" else m["spk"][k]
        topics = "".join(f"<li>{e(x)}</li>" for x in tl)
        spk += (f'<div class="spk"><h4><a href="{team}#{k}">{e(pp["name"])}</a></h4>'
                f'<p class="spk-mail"><a href="mailto:{e(pp["email"])}">{e(pp["email"])}</a></p><ul>{topics}</ul></div>')
    kit = f'<li><a href="{up}assets/logo.png" download>{e(m["logo"])}</a></li>'
    kit += "".join(f'<li><a href="{up}{e(people[k]["photo"])}" download>{e(m["photo"].format(people[k]["name"]))}</a></li>' for k in ("jk", "hk"))
    kit += f'<li><a href="{team}">{e(m["bios"])}</a></li>'
    from urllib.parse import quote
    mail = f'mailto:{C.EMAIL}?subject={quote(m["subject"])}'
    return (f'<section class="dark media" id="media" aria-labelledby="media-h"><div class="wrap">'
            f'<div class="section-head"><h2 id="media-h">{e(m["media_h"])}</h2><p class="lede">{e(m["media_p"])}</p>'
            f'<p><a class="btn on-dark" href="{e(mail)}">{e(m["write"])}</a></p>'
            f'<p class="media-contact"><a href="mailto:{C.EMAIL}">{e(C.EMAIL)}</a> · <a href="tel:{C.PHONE_TEL}">{e(C.PHONE)}</a></p></div>'
            f'<div class="media-grid"><div><h3>{e(m["spk_h"])}</h3><div class="spk-list">{spk}</div></div>'
            f'<div><h3>{e(m["kit_h"])}</h3><ul class="kit">{kit}</ul><h3>{e(m["about_h"])}</h3><p class="boiler">{e(m["about_p"])}</p></div></div>'
            f'</div></section>')


def page_insights(lang, t):
    i = t["insights"]
    m = PRESS_PAGE[lang]
    import press_extra as PX
    import content_services as CS
    svc_title = {sid: ti for sid, ti, _, _ in CS.SERVICES8[lang]}
    def ev_li(ev):
        d, title, detail, url = ev
        link = f' <a href="{e(url)}" rel="noopener">{e(PX.OPEN[lang])}<span class="sr-only"> ({e(title[lang])})</span> ↗</a>' if url else ""
        sid = PX.EVENT_SERVICE.get(d)
        if sid:
            link += (f'<a class="ev-svc" href="{rel(lang, "insights", lang, "services")}#{sid}">'
                     f'{e(PX.RELATED[lang])}{" : " if lang == "fr" else ": "}{e(svc_title[sid])} →</a>')
        return (f'<li><time datetime="{d}">{e(fmt_date(lang, d))}</time><strong>{e(title[lang])}</strong>'
                f'<span class="ev-d">{e(detail[lang])}{link}</span></li>')
    evs = sorted(PX.EVENTS, key=lambda x: x[0], reverse=True)
    events = "".join(ev_li(x) for x in evs[:PX.EVENTS_SHOWN])
    if len(evs) > PX.EVENTS_SHOWN:
        events += f'</ul><details class="ev-more"><summary>{e(PX.SHOW_ALL[lang].format(len(evs)))}</summary><ul class="events">' + "".join(ev_li(x) for x in evs[PX.EVENTS_SHOWN:]) + "</ul></details><ul class=\"events\" hidden>"
    pubs = "".join(f'<li><span class="pub-y">{y}</span><a href="{e(u)}" rel="noopener"><strong>{e(ti)}</strong></a><span class="ev-d">{e(dt[lang])}</span></li>' for y, ti, dt, u in PX.PUBS)
    up = "../" * depth(lang, "insights")
    books = [p for p in C.PRESS if C.PRESS_THEME.get(p["url"]) == "books"]
    books_lbl = dict(PRESS_THEMES)["books"][lang]
    books_html = (f'<div class="pub-books" id="press-books"><h3>{e(books_lbl)} <small>{len(books)}</small></h3>'
                  f'<div class="press">{press_items(lang, books, up)}</div></div>') if books else ""
    pubs_html = (f'<section class="alt" id="publications"><div class="wrap"><h2>{e(PX.PUBS_H[lang])}</h2><p class="lead-in">{e(PX.PUBS_P[lang])}</p>'
                 f'<ul class="pubs">{pubs}</ul><p><a class="more" href="{PX.PUBS_ALL_URL}" rel="noopener">{e(PX.PUBS_ALL[lang])} ↗</a></p>{books_html}</div></section>')
    press = press_by_theme(lang, up)
    gallery = ""
    if getattr(C, "GALLERY", None):
        def fig(g):
            when = f' <time datetime="{g["date"]}">{fmt_date(lang, g["date"])}</time>' if g.get("date") else ""
            enlarge = {"en": "Enlarge photo", "fr": "Agrandir la photo", "ko": "사진 확대"}[lang]
            return (f'<figure><button type="button" class="g-open" aria-label="{e(enlarge)}: {e(g["alt"][lang])}"><img src="{up}{e(g["src"])}" alt="{e(g["alt"][lang])}" width="{g["w"]}" height="{g["h"]}" loading="lazy" decoding="async"></button>'
                     f'<figcaption>{e(g["caption"][lang])}{when}</figcaption></figure>')
        shown = 5
        figs = "".join(fig(g) for g in C.GALLERY[:shown])
        rest = C.GALLERY[shown:]
        more_lbl = {"en": "Show {n} more photos", "fr": "Afficher {n} photos de plus", "ko": "사진 {n}장 더 보기"}[lang]
        if rest:
            figs_more = "".join(fig(g) for g in rest)
            figs_more = f'<details class="g-more"><summary>{e(more_lbl.format(n=len(rest)))}</summary><div class="gallery">{figs_more}</div></details>'
        else:
            figs_more = ""
        close = {"en": "Close", "fr": "Fermer", "ko": "닫기"}[lang]
        gallery = f'<section class="alt"><div class="wrap"><div class="section-head"><h2>{e(i["gallery_h"])}</h2></div><div class="gallery">{figs}</div>{figs_more}<dialog class="lightbox" aria-label="{e(i["gallery_h"])}"><form method="dialog"><button class="lb-close" aria-label="{close}">×</button></form><img alt=""><p></p></dialog></div></section>'
    since, n_art, n_out, n_lang = press_stats()
    stats = [(since, m["stat_since"]), (str(n_art), m["stat_items"]), (str(n_out), m["stat_outlets"])]
    if lang != "ko":  # "in the press since 1998": label before the value
        stats_html = "".join(f'<li><span>{e(l)}</span><strong>{e(v)}</strong></li>' if k == 0 else f'<li><strong>{e(v)}</strong><span>{e(l)}</span></li>'
                             for k, (v, l) in enumerate(stats))
    else:
        stats_html = "".join(f'<li><strong>{e(v)}</strong><span>{e(l)}</span></li>' for v, l in stats)
    body = (f'<div class="page-head press-head"><div class="wrap"><h1>{e(i["h1"])}</h1><p class="lede">{e(i["lede"])}</p>'
            f'<ul class="press-stats">{stats_html}</ul>'
            f'<p class="press-actions"><a class="btn on-dark" href="#media">{e(m["media_btn"])}</a> <a class="btn ghost" href="#latest">{e(m["latest_btn"])}</a></p>'
            f'<p class="outlets"><span>{e(m["featured_in"])}</span> {outlet_strip(lang)}</p></div></div>\n'
            f'<section class="alt" id="latest"><div class="wrap"><h2>{e(i["events_h"])}</h2><p class="lead-in">{e(i["events_p"])}</p><ul class="events">{events}</ul></div></section>\n'
            f'{case_file(lang)}\n'
            f'<section><div class="wrap"><h2>{e(i["press_h"])}</h2>{press}</div></section>\n'
            f'{pubs_html}\n'
            f'{gallery}\n{media_kit(lang, up)}\n'
            f'{cta_band(lang, "insights", t, WHO[lang]["cta_h"], WHO[lang]["cta_p"], dark=False)}')
    return body, press_ld(lang)


# What happens after a message. Each line restates something the site already says
# (Services call to action, fees FAQ); no response time is promised.
NEXT_STEPS = {
    "en": ("What happens next", [
        ("1. Describe your matter", "In English, French or Korean, by email or with the form below."),
        ("2. We reply with a first view", "What your matter involves and what to prepare."),
        ("3. Fees agreed in advance", "Fixed fees for clearly defined assignments; otherwise hourly or tailored, agreed before work starts.")]),
    "fr": ("Comment cela se passe", [
        ("1. Décrivez votre situation", "En français, en anglais ou en coréen, par courriel ou avec le formulaire ci-dessous."),
        ("2. Nous vous répondons", "Ce que votre dossier implique et ce qu'il faut préparer."),
        ("3. Des honoraires convenus à l'avance", "Forfait pour les missions clairement définies ; sinon au temps passé ou sur mesure, convenus avant le début de la mission.")]),
    "ko": ("상담 진행 방식", [
        ("1. 사안 설명", "한국어, 프랑스어, 영어로 이메일 또는 아래 양식을 통해 보내 주세요."),
        ("2. 1차 답변", "사안에 필요한 절차와 준비 사항을 안내해 드립니다."),
        ("3. 사전 보수 합의", "업무 범위가 명확한 사안은 정액 보수, 그 밖에는 시간제 또는 맞춤형 보수를 업무 시작 전에 합의합니다.")]),
}


def page_contact(lang, t):
    c = t["contact"]
    topics = "".join(f"<option>{e(x)}</option>" for x in c["topics"])
    msgs = ""
    if C.KAKAO_URL:
        msgs += f'<li><a href="{e(C.KAKAO_URL)}" rel="noopener">{e(c["kakao"])}</a></li>'
    if C.WHATSAPP_URL:
        msgs += f'<li><a href="{e(C.WHATSAPP_URL)}" rel="noopener">{e(c["whatsapp"])}</a></li>'
    book = f'<p><a class="btn on-dark" href="{e(C.BOOKING_URL)}" rel="noopener">{e(t["cta"])}</a></p>' if C.BOOKING_URL else ""
    nx = NEXT_STEPS[lang]
    steps = "".join(f'<li><strong>{e(h)}</strong><span>{e(x)}</span></li>' for h, x in nx[1])
    return f'''<div class="page-head"><div class="wrap"><h1>{e(c["h1"])}</h1><p class="lede">{e(c["lede"])}</p>
<h2 class="next-h">{e(nx[0])}</h2><ol class="next-steps">{steps}</ol></div></div>
<section style="padding-top:0"><div class="wrap cols c2">
<div id="form"><h2>{e(c["form_h"])}</h2>
<form class="contact" data-to="{e(C.EMAIL)}" data-subject="{e(c["subject"])}" data-sep="{" : " if lang == "fr" else ": "}" data-mail="{e(c["mail"])}" data-fallback="{e(c["fallback"])}" data-copy="{e(c["copy"])}" data-copied="{e(c["copied"])}" data-intro="{e(json.dumps([c["f_name"], c["f_position"], c["f_company"]], ensure_ascii=False))}" method="post" action="mailto:{e(C.EMAIL)}" enctype="text/plain">
<label>{e(c["f_topic"])}<select name="topic" required>{topics}</select></label>
<label>{e(c["f_object"])}<textarea name="object" required></textarea></label>
<label class="check"><input type="checkbox" name="consent" required><span>{e(c["f_consent"])}</span></label>
<button class="btn" type="submit">{e(c["send"])}</button>
<p class="form-status" role="status" aria-live="polite"></p>
<p class="lead-in">{e(c["confidential"])}</p>
</form></div>
<div><div class="dark" style="border-radius:14px;padding:28px"><h2 style="font-size:1.4rem">{e(c["details_h"])}</h2>
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


def vcard(person, role):
    # Only data already on the site and in config.py; no new facts.
    parts = person["name"].split()
    def esc(v):
        return v.replace("\\", "\\\\").replace(",", "\\,").replace(";", "\\;")
    lines = ["BEGIN:VCARD", "VERSION:3.0",
             f"N:{esc(parts[-1])};{esc(' '.join(parts[:-1]))};;;",
             f"FN:{esc(person['name'])}",
             f"ORG:{esc(C.FIRM_FULL)}",
             f"TITLE:{esc(role)}",
             f"EMAIL;TYPE=WORK:{person['email']}",
             f"TEL;TYPE=WORK,VOICE:{C.PHONE_TEL}",
             *[f"TEL;TYPE=CELL,VOICE:{n}" for n in person.get("tel", [])],
             f"ADR;TYPE=WORK:;;57 Quai de Grenelle;Paris;;75015;France",
             f"URL:{C.SITE_URL}",
             "END:VCARD"]
    return "\r\n".join(lines) + "\r\n"


def write(path, text):
    path = ROOT / path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main():
    # clean generated output only
    for d in ["fr", "ko", "services", "experience", "team", "insights", "press", "contact", "legal", "privacy"]:
        shutil.rmtree(ROOT / d, ignore_errors=True)
    for f in ["index.html", "404.html", "sitemap.xml", "robots.txt", "CNAME", ".nojekyll"]:
        (ROOT / f).unlink(missing_ok=True)

    builders = {"home": page_home, "services": page_services, "people": page_people,
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

    # Former Experience page: redirect to Services (content now lives there as key examples)
    for lang in LANGS:
        target = abs_url(lang, "services")
        write(url_path(lang, "experience") + "index.html",
              f'<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><title>Archè</title>'
              f'<meta name="robots" content="noindex"><link rel="canonical" href="{target}">'
              f'<meta http-equiv="refresh" content="0; url={target}"></head>'
              f'<body><p><a href="{target}">{e(T[lang]["nav"]["services"])}</a></p></body></html>')

    # Former /insights/ URL: redirect to the Press page (nav label and URL now match)
    for lang in LANGS:
        target = abs_url(lang, "insights")
        write(("" if lang == "en" else lang + "/") + "insights/index.html",
              f'<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><title>Archè</title>'
              f'<meta name="robots" content="noindex"><link rel="canonical" href="{target}">'
              f'<meta http-equiv="refresh" content="0; url={target}"></head>'
              f'<body><p><a href="{target}">{e(T[lang]["nav"]["insights"])}</a></p></body></html>')

    # 404 (absolute asset paths so it works at any depth)
    t = T["en"]
    base = C.SITE_URL.rstrip("/") + "/"
    nf = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(t["meta"]["404"][0])}</title><meta name="robots" content="noindex"><link rel="icon" href="{base}assets/favicon.png" type="image/png"><link rel="stylesheet" href="{base}assets/style.css?v={CSS_V}">
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
    for person in C.PEOPLE:
        write(f"assets/downloads/{person['slug']}.vcf", vcard(person, T["en"]["people"]["roles"][person["slug"]]))

    for w in sorted(set(warnings)):
        print("WARNING:", w)
    print(f"Built {len(urls)} pages + 404, sitemap, robots, CNAME.")


if __name__ == "__main__":
    main()
