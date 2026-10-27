"""Site-wide settings. Edit this file, then run: python3 build.py"""

DOMAIN = "archelegal.com"           # canonical domain (written to CNAME)
SITE_URL = "https://archelegal.com"  # matches CNAME (apex); GitHub Pages redirects www to it
FIRM = "Archè"
FIRM_FULL = "Archè SELARL"

EMAIL = "paris@archelegal.com"
PHONE = "+33 1 4335 8410"
PHONE_TEL = "+33143358410"
ADDRESS_LINES = ["Tour Totem", "57 Quai de Grenelle", "75015 Paris", "France"]
MAPS_URL = "https://www.openstreetmap.org/search?query=57%20Quai%20de%20Grenelle%2075015%20Paris"

LINKEDIN = "https://www.linkedin.com/company/archelegalparis"
INSTAGRAM = "https://www.instagram.com/archelegal/"

# Booking / messaging. Leave "" to hide a channel.
BOOKING_URL = ""      # e.g. a Calendly or Cal.com link: shown as the main button when set
KAKAO_URL = ""        # e.g. https://pf.kakao.com/_xxxxx
WHATSAPP_URL = ""     # e.g. https://wa.me/33143358410

# Contact form. "" = the form opens the visitor's email app. For a real form,
# create a free Formspree/Basin endpoint and paste its URL here.
FORM_ENDPOINT = ""

# Seoul / Hong Kong. Add a street address and phone when available.
SEOUL = {"address": "Humanstarville #1101, Dosandae-ro 454, Gangnam-gu, Seoul, South Korea", "phone": "", "email": "seoul@archelegal.com"}
HONGKONG = {"address": "Arche Asia Ltd., Level 1901, Cheung Kong Center, 2 Queen's Road Central, Central, Hong Kong", "phone": "", "email": "hk@archelegal.com"}

# Founder's profile links (team page; footer shows all except the firm site).
HK_LINKS = [
    ("GitHub", "https://github.com/habbine"),
    ("ORCID", "https://orcid.org/0000-0003-4990-584X"),
    ("SSRN", "https://papers.ssrn.com/sol3/cf_dev/AbsByAuth.cfm?per_id=4745485"),
    ("Instagram", "https://www.instagram.com/kim_avocat/"),
]
# Founder links kept in the footer.
FOOTER_PERSONAL = [
    ("kimavocat.com", "https://www.kimavocat.com/"),
    ("Instagram · kim_avocat", "https://www.instagram.com/kim_avocat/"),
]

PEOPLE = [
    {
        "slug": "jk",
        "initials": "JK",
        "photo": "assets/img/team-jk.webp",  # e.g. "assets/img/james-kim.jpg" once you add the file
        "name": "James Joong-ho Kim",
        "email": "james.kim@archelegal.com",
        "linkedin": "https://www.linkedin.com/in/jameskim-arche/",
    },
    {
        "slug": "hk",
        "initials": "HK",
        "photo": "assets/img/team-hk.webp",
        "name": "Habbine Estelle Kim",
        "email": "habbine.kim@archelegal.com",
        "linkedin": "https://www.linkedin.com/in/kim-avocat/",
        "links": HK_LINKS,
    },
    {
        "slug": "dk",
        "initials": "DK",
        "photo": "assets/img/team-dk.webp",
        "name": "Dabin Kevin Kim",
        "email": "dabin.kim@archelegal.com",
        "linkedin": "https://www.linkedin.com/in/dabin-kevin-kim-0082a9113/",
    },
]

# Press coverage, newest first. "title" is the original headline (shown as is, in its language).
# "outlet" and "about" are per page language; "about" may be omitted for a language (then only the title shows).
def _o(en, ko, fr=None):
    return {"en": en, "fr": fr or en, "ko": ko}

PRESS = [
    {"date": "2025-10-17", "outlet": _o("Book · Amazon", "도서 · 아마존", "Livre · Amazon"), "lang": "en",
     "url": "https://www.amazon.fr/dp/B0FWZS7SYM",
     "title": "A Forgotten Promise: The Secrets of the Royal Protocols (James J. Kim, ISBN 979-8270335410)",
     "about": {"en": "English edition of James Joong-ho Kim's novel, based on the Oegyujanggak restitution case",
               "fr": "Édition anglaise du roman de James Joong-ho Kim, inspiré de l'affaire de l'Oegyujanggak",
               "ko": "외규장각 반환 소송을 바탕으로 한 김중호 변호사 소설 「잊혀진 약속」의 영문판"},
     "quote": {"text": "Une lecture à la fois aisée et prenante.", "lang": "fr",
               "by": "Hauteclaire, Amazon.fr", "date": "2026-01-18"}},
    {"date": "2025-10-19", "outlet": _o("Legal Times", "리걸타임즈"), "lang": "ko",
     "url": "http://www.legaltimes.co.kr/news/articleView.html?idxno=89709", "cover": "assets/img/book-promise.webp",
     "title": "[신간소개] 파리에서 활동하는 김중호 변호사의 《잊혀진 약속》",
     "about": {"en": "New book: James Joong-ho Kim's novel A Forgotten Promise",
               "fr": "Parution du roman de James Joong-ho Kim, A Forgotten Promise"}},
    {"date": "2025-10-14", "outlet": _o("Book · BOOKK (YES24)", "도서 · 부크크 (YES24)", "Livre · BOOKK (YES24)"), "lang": "ko",
     "url": "https://www.yes24.com/product/goods/160462528", "cover": "assets/img/book-beopjaengi.webp",
     "title": "법쟁이 탈출기 (김중호 지음, ISBN 9791112072207)",
     "about": {"en": "Autobiographical essay by James Joong-ho Kim on 25 years of practice in France",
               "fr": "Essai autobiographique de James Joong-ho Kim sur 25 ans d'exercice en France"}},
    {"date": "2024-08-19", "outlet": _o("The Economic Times", "이코노믹 타임스"), "lang": "en",
     "url": "https://economictimes.indiatimes.com/news/sports/vinesh-phogat-cas-verdict-olympics-2024-disqualification-weight-limit-rules-same-for-all-full-list-of-reasons/articleshow/112633538.cms",
     "title": "'Weight limit rules same for all': CAS gives reasons for dismissing Vinesh Phogat's plea against olympics disqualification",
     "about": {"en": "Paris 2024: Habbine Estelle Kim named in Vinesh Phogat's pro bono legal team before the CAS",
               "fr": "Paris 2024 : Habbine Estelle Kim citée dans l'équipe pro bono de Vinesh Phogat devant le TAS",
               "ko": "파리 2024: CAS 사건에서 비네시 포갓 선수의 프로보노 변호인단에 Habbine Estelle Kim 변호사 포함"}},
    {"date": "2022-10-16", "outlet": _o("Asia Economy", "아시아경제"), "lang": "ko",
     "url": "https://view.asiae.co.kr/article/2022101600063756550",
     "title": "[인터뷰] 'K-문화에 세계 매료'…김중호 프랑스 변호사, \"한류 수출 기업, 행정·법률 정보 숙지 필수\"",
     "about": {"en": "Interview: what Korean companies need to know before entering the French market",
               "fr": "Entretien : ce que les entreprises coréennes doivent savoir avant de s'implanter en France"}},
    {"date": "2021-02-13", "outlet": _o("Segye Ilbo", "세계일보"), "lang": "ko",
     "url": "https://www.segye.com/newsView/20210210510631",
     "title": "그들만의 ‘물징계’… 뇌물·성추행 걸려도 법복 벗으면 끝 [탐사기획-법관징계 리포트]",
     "about": {"en": "Second part of the judicial-discipline investigation: comment on practice in France",
               "fr": "Deuxième volet de l'enquête sur la discipline des magistrats : commentaire sur la pratique en France"}},
    {"date": "2021-02-09", "outlet": _o("Segye Ilbo", "세계일보"), "lang": "ko",
     "url": "https://www.segye.com/newsView/20210208515023",
     "title": "수뢰판사, 美·英·佛선 ‘파면’ 가능한데… 韓은 고작 ‘정직 1년’ [탐사기획-법관징계 리포트]",
     "about": {"en": "Investigation on judicial discipline: comment on how judges are disciplined in France",
               "fr": "Enquête sur la discipline des magistrats : commentaire sur la pratique en France"}},
    {"date": "2016-02-25", "outlet": _o("Law Times", "법률신문"), "lang": "ko",
     "url": "https://www.lawtimes.co.kr/news/articleView.html?idxno=98725",
     "title": "[주목 이사람] 한국인 첫 프랑스 변호사… 세계시장 공략",
     "about": {"en": "Profile of the first Korean admitted to the French bar and the founding of Archè",
               "fr": "Portrait du premier avocat coréen au barreau français et de la création d'Archè"}},
    {"date": "2010-02-28", "outlet": _o("Kyunghyang Shinmun", "경향신문"), "lang": "ko",
     "url": "https://www.khan.co.kr/article/201002281735075",
     "title": "“프랑스의 ‘약탈’ 표현은 우리 작전의 성과”",
     "about": {"en": "Interview after the appeal: how the French State came to use the word 'pillage'",
               "fr": "Entretien après l'appel : comment l'État français en est venu à employer le mot « pillage »"}},
    {"date": "2010-02-26", "outlet": _o("Dong-A Ilbo", "동아일보"), "lang": "ko",
     "url": "https://www.donga.com/news/Culture/article/all/20100225/26453075/1",
     "title": "“외규장각 반환訴 1심 졌지만 ‘약탈’인정 성과…끝까지 투쟁”",
     "about": {"en": "After the first-instance ruling: the appeal and the French State's acknowledgement of 'pillage'",
               "fr": "Après le jugement de première instance : l'appel et la reconnaissance du « pillage » par l'État français"}},
    {"date": "2010-02-26", "outlet": _o("Seoul Shinmun", "서울신문"), "lang": "ko",
     "url": "https://www.seoul.co.kr/news/society/2010/02/26/20100226029023",
     "title": "佛행정법원에 외규장각 문서반환 항소한 김중호 변호사",
     "about": {"en": "Appeal in the Oegyujanggak royal manuscripts restitution case against the French State",
               "fr": "Appel dans l'action en restitution des manuscrits royaux de l'Oegyujanggak contre l'État français"}},
    {"date": "2010-02-25", "outlet": _o("CBS Nocut News", "CBS 노컷뉴스"), "lang": "ko",
     "url": "https://n.news.naver.com/mnews/article/079/0002133525",
     "title": "외규장각 반환소송 항소장 접수",
     "about": {"en": "Appeal filed in the Oegyujanggak restitution case: the three legal grounds",
               "fr": "Appel interjeté dans l'affaire de l'Oegyujanggak : les trois moyens soulevés"}},
    {"date": "2010-02-25", "outlet": _o("Newsis", "뉴시스"), "lang": "ko",
     "url": "https://n.news.naver.com/mnews/article/003/0003107446?sid=102",
     "title": "김중호 외규장각 반환소송 담당 변호사",
     "about": {"en": "Press conference on the appeal in the Oegyujanggak restitution case (photo)",
               "fr": "Conférence de presse sur l'appel dans l'affaire de l'Oegyujanggak (photo)"}},
    {"date": "2009-12-16", "outlet": _o("Dong-A Ilbo", "동아일보"), "lang": "ko",
     "url": "https://www.donga.com/news/article/all/20091216/24831994/1",
     "title": "佛 '약탈' 인정… 반환은 미지수",
     "about": {"en": "At the Paris hearing, the French State uses the word 'pillage' for the first time",
               "fr": "À l'audience à Paris, l'État français emploie pour la première fois le mot « pillage »"}},
    {"date": "2009-12", "outlet": _o("The Hankyoreh", "한겨레"), "lang": "ko",
     "url": "https://www.hani.co.kr/arti/politics/diplomacy/392512.html",
     "title": "프랑스 정부, 외규장각 도서 '약탈' 인정",
     "about": {"en": "The French government acknowledges the 'pillage' of the Oegyujanggak books",
               "fr": "Le gouvernement français reconnaît le « pillage » des livres de l'Oegyujanggak"}},
    {"date": "2008-09-10", "outlet": _o("Yonhap News", "연합뉴스"), "lang": "ko",
     "url": "https://www.yna.co.kr/view/AKR20080910160900005",
     "title": "<사람들> 외규장각 유물 반환소송 김중호 변호사",
     "about": {"en": "Interview on the Oegyujanggak restitution claim against the French State",
               "fr": "Entretien sur l'action en restitution de l'Oegyujanggak contre l'État français"}},
    {"date": "2008-09-10", "outlet": _o("CBS Nocut News", "CBS 노컷뉴스"), "lang": "ko",
     "url": "https://www.nocutnews.co.kr/news/494244",
     "title": "\"훔쳐간 문화재 내놔라\" 韓-佛 소송전 2라운드",
     "about": {"en": "Next stage of the Oegyujanggak restitution litigation, with an interview",
               "fr": "Nouvelle étape du contentieux de l'Oegyujanggak, avec un entretien"}},
    {"date": "2008-09-10", "outlet": _o("Yonhap News", "연합뉴스"), "lang": "ko",
     "url": "https://n.news.naver.com/mnews/article/001/0002261719?sid=103",
     "title": "佛 약탈 외규장각 유물 반환 소송 급물살",
     "about": {"en": "Press conference in front of the French Embassy in Seoul on the restitution case",
               "fr": "Conférence de presse devant l'ambassade de France à Séoul sur l'action en restitution"}},
    {"date": "2008-09-08", "outlet": _o("Yonhap News", "연합뉴스"), "lang": "ko",
     "url": "https://n.news.naver.com/mnews/article/001/0002258703?sid=103",
     "title": "프랑스 외규장각 반환 소송 '본격화'",
     "about": {"en": "The restitution case moves forward after the French government's formal reply",
               "fr": "L'action en restitution avance après la réponse officielle du gouvernement français"}},
    {"date": "2007-05-30", "outlet": _o("Seoul Shinmun", "서울신문"), "lang": "ko",
     "url": "https://www.seoul.co.kr/news/newsView.php?id=20070530014005",
     "title": "“전문화만이 살 길”… 해외 실무수습도",
     "about": {"en": "A Korean trainee lawyer's placement at Alérion in Paris, then led by James Joong-ho Kim",
               "fr": "Le stage d'un élève-avocat coréen chez Alérion à Paris, alors dirigé par James Joong-ho Kim"}},
    {"date": "2007-03-08", "outlet": _o("The Hankyoreh", "한겨레"), "lang": "ko",
     "url": "https://www.hani.co.kr/arti/society/society_general/195031.html",
     "title": "르몽드 '외규장각도서 반환촉구' 광고 실리기까지",
     "about": {"en": "Behind the Le Monde advertisement calling for the return of the Oegyujanggak books",
               "fr": "Les coulisses de l'annonce parue dans Le Monde pour le retour des livres de l'Oegyujanggak"}},
    {"date": "2007-03-08", "outlet": _o("Yonhap News", "연합뉴스"), "lang": "ko",
     "url": "https://n.news.naver.com/mnews/article/001/0001567518?sid=103",
     "title": "佛 르몽드에 외규장각도서 반환촉구 광고문 게재",
     "about": {"en": "Full-page advertisement in Le Monde calling for the return of the Oegyujanggak books",
               "fr": "Annonce pleine page dans Le Monde pour le retour des livres de l'Oegyujanggak"}},
    {"date": "2007-02-07", "outlet": _o("Seoul Shinmun", "서울신문"), "lang": "ko",
     "url": "https://www.seoul.co.kr/news/newsView.php?id=20070207009012",
     "title": "[사회플러스] “외규장각 도서 반환” 佛에 소송",
     "about": {"en": "A restitution claim to be filed at the Paris Administrative Court on 9 February",
               "fr": "Une requête en restitution déposée le 9 février devant le tribunal administratif de Paris"}},
    {"date": "2007-02-06", "outlet": _o("Yonhap News", "연합뉴스"), "lang": "ko",
     "url": "https://n.news.naver.com/mnews/article/001/0001539822?sid=103",
     "title": "<인터뷰> 외규장각 반환소송 김중호 변호사",
     "about": {"en": "Interview before filing the restitution claim at the Paris Administrative Court",
               "fr": "Entretien avant le dépôt de la requête en restitution devant le tribunal administratif de Paris"}},
    {"date": "2007-02", "outlet": _o("Yonhap News", "연합뉴스"), "lang": "ko",
     "url": "https://n.news.naver.com/mnews/article/001/0001539898?sid=102",
     "title": "<연합뉴스 이시각 헤드라인>-08:00",
     "about": {"en": "Headline: a restitution claim to be filed at the Paris Administrative Court",
               "fr": "Titre : une requête en restitution bientôt déposée devant le tribunal administratif de Paris"}},
    {"date": "2005-11-23", "outlet": _o("Chosun Ilbo", "조선일보"), "lang": "ko",
     "url": "https://www.chosun.com/site/data/html_dir/2005/11/23/2005112370512.html",
     "title": "['불탄 프랑스' 경제 대해부] <1> 복지 외치다 '실업病 30년'",
     "about": {"en": "Comment on the rigidity of French employment law",
               "fr": "Commentaire sur la rigidité du droit du travail français"}},
    {"date": "1999-03-04", "outlet": _o("Chosun Ilbo", "조선일보"), "lang": "ko",
     "url": "https://www.chosun.com/site/data/html_dir/1999/03/04/1999030470356.html",
     "title": "[사람들] 국제변호사 김중호씨…한국최초 불 변호사 자격 따내",
     "about": {"en": "The first Korean to qualify as a lawyer in France",
               "fr": "Le premier Coréen à obtenir le titre d'avocat en France"}},
]
PRESS += [
    {"date": "2017-10-12", "outlet": _o("Legal Times", "리걸타임즈"), "lang": "ko",
     "url": "https://www.legaltimes.co.kr/news/articleView.html?idxno=34302",
     "title": "프랑스서 로펌 운영하는 김중호 변호사",
     "about": {"en": "Profile: the first Korean to become a French lawyer, on running a law firm in France",
               "fr": "Portrait : le premier Coréen devenu avocat en France, à la tête d'un cabinet à Paris",
               "ko": "한국인 최초의 프랑스 변호사, 프랑스에서 로펌을 운영하는 김중호 변호사"}},
    {"date": "1998", "outlet": _o("JoongAng Ilbo", "중앙일보"), "lang": "ko",
     "url": "https://www.joongang.co.kr/article/3752927",
     "title": "김중호씨, 美·佛 변호사 자격증 동시취득",
     "about": {"en": "The first Korean national to qualify as both a US and a French lawyer",
               "fr": "Le premier ressortissant coréen à obtenir à la fois les qualifications d'avocat aux États-Unis et en France",
               "ko": "한국 국적자로는 처음으로 미국과 프랑스 변호사 자격을 동시에 취득"}},
]
PRESS.sort(key=lambda p: p["date"], reverse=True)

PRESS += [
    {"date": "2023-05", "outlet": _o("Gallery M9", "갤러리 엠나인", "Galerie M9"), "lang": "ko",
     "url": "https://gallerym9.com/somme-des-parties-m-",
     "title": "Somme des Parties: Récupération et Unité",
     "about": {"en": "K-Art exhibition in Paris hosted by the CCICF, chaired by James Joong-ho Kim, with Sisley (22 May–30 June 2023)",
               "fr": "Exposition K-Art à Paris organisée par la CCICF, présidée par James Joong-ho Kim, avec Sisley (22 mai–30 juin 2023)",
               "ko": "김중호 회장의 한불상공회의소 주최, 시슬리 그룹과 함께한 파리 K-Art 특별전(2023.5.22–6.30)"}},
    {"date": "2017", "outlet": _o("Place de Paris", "파리 광장"), "lang": "ko",
     "url": "https://placedeparis.com/community/bbs/board.php?bo_table=news_issue&wr_id=1402",
     "title": "주 프랑스 한불상공회의소 주최 제 12회 2017 취업 및 창업 세미나",
     "about": {"en": "CCICF's 12th jobs and start-up seminar: James Joong-ho Kim on company formation and administrative procedures in France",
               "fr": "12ᵉ séminaire emploi et création d'entreprise de la CCICF : James Joong-ho Kim sur la création de société et les démarches en France",
               "ko": "한불상공회의소 제12회 취업·창업 세미나: 김중호 변호사의 프랑스 법인 설립 및 행정 절차 강연"}},
    {"date": "2015-06-12", "outlet": _o("France Zone", "프랑스존"), "lang": "ko",
     "url": "https://www.francezone.com/news/articleView.html?idxno=664353",
     "title": "김중호 변호사, 프랑스 체류관련 생활법률 설명회",
     "about": {"en": "Legal information session at the Embassy of Korea for Koreans living in France: residence permits, leases and starting a business",
               "fr": "Séance d'information juridique à l'Ambassade de Corée pour les Coréens de France : titres de séjour, baux et création d'entreprise",
               "ko": "주프랑스 대한민국 대사관에서 열린 교민 대상 생활법률 설명회: 체류증, 임대차, 창업"}},
]
PRESS.sort(key=lambda p: p["date"], reverse=True)

PRESS += [
    {"date": "2007-02-07", "outlet": _o("France Zone", "프랑스존"), "lang": "ko",
     "url": "https://www.francezone.com/news/articleView.html?idxno=95669",
     "title": "김중호 변호사, 9일 외규장각 도서 반환 소송",
     "about": {"en": "Announcement of the Oegyujanggak restitution claim against the French State, to be filed on 9 February 2007",
               "fr": "Annonce de l'action en restitution de l'Oegyujanggak contre l'État français, déposée le 9 février 2007",
               "ko": "2007년 2월 9일 프랑스 정부 상대 외규장각 도서 반환 소송 제기 예고"}},
]
PRESS.sort(key=lambda p: p["date"], reverse=True)

# Coverage shown first on the Press page and on the home page.
PRESS_FEATURED = [
    "https://www.joongang.co.kr/article/3752927",
    "https://www.lawtimes.co.kr/news/articleView.html?idxno=98725",
    "https://www.legaltimes.co.kr/news/articleView.html?idxno=34302",
    "https://www.yna.co.kr/view/AKR20080910160900005",
    "https://www.seoul.co.kr/news/society/2010/02/26/20100226029023",
    "http://www.legaltimes.co.kr/news/articleView.html?idxno=89709",
]
PRESS_HOME = 3  # how many of the latest items the home page shows

# Legal notice fields (French law requires these). Fill them in; build.py warns about blanks.
LEGAL = {
    "raison_sociale": "Archè SELARL",
    "forme": "Société d'exercice libéral à responsabilité limitée (SELARL)",
    "capital": "",
    "siege": "Tour Totem, 57 Quai de Grenelle, 75015 Paris, France",
    "rcs": "RCS Paris 812 914 018",
    "tva": "",
    "barreau": "Barreau de Paris, toque C 0281",
    "rcp": "",
    "directeur_publication": "",
    "hebergeur": "GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, USA",
}


# Photos for the "In pictures" section of the press page. Only events whose details are confirmed.
# w/h are the stored image size (used for layout, avoids page jumps).
GALLERY = [
    {"src": "assets/img/salon-2026-1.webp", "w": 568, "h": 565, "date": "2026-10-10",
     "caption": {"en": "Salon de l'Étudiant, Paris, Korea pavilion: presentations by the CCICF (Habbine Estelle Kim, Secretary General) and KOSME (Jae Yang, Director).",
                 "fr": "Salon de l'Étudiant, Paris, pavillon coréen : présentations de la CCICF (Habbine Estelle Kim, secrétaire générale) et de KOSME (Jae Yang, directrice).",
                 "ko": "Salon de l'Étudiant 파리 한국관: CCICF(Habbine Estelle Kim 사무총장)와 중소벤처기업진흥공단 KOSME(Jae Yang 소장) 발표."},
     "alt": {"en": "Two speakers seated in front of a screen showing the session programme, with French and Korean flags on the table.",
             "fr": "Deux intervenantes assises devant un écran affichant le programme, drapeaux français et coréen sur la table.",
             "ko": "세션 프로그램이 띄워진 화면 앞에 두 발표자가 앉아 있고, 탁자에 프랑스와 한국 국기가 놓여 있다."}},
    {"src": "assets/img/salon-2026-2.webp", "w": 544, "h": 561, "date": "2026-10-10",
     "caption": {"en": "Salon de l'Étudiant, Paris: KOSME presentation on support for Korean SMEs and startups.",
                 "fr": "Salon de l'Étudiant, Paris : présentation de KOSME sur l'accompagnement des PME et startups coréennes.",
                 "ko": "Salon de l'Étudiant 파리: 한국 중소기업·스타트업 지원에 관한 KOSME 발표."},
     "alt": {"en": "A speaker with a microphone beside a slide titled Overview of KOSME.",
             "fr": "Une intervenante au micro à côté d'une diapositive intitulée Overview of KOSME.",
             "ko": "Overview of KOSME 슬라이드 옆에서 마이크를 든 발표자."}},
    {"src": "assets/img/embassy-2025-poster.webp", "w": 900, "h": 1110, "date": "2025-11-05",
     "caption": {"en": "Embassy of Korea in France, consular section: 2025 information session on everyday law and student life, led by James Joong-ho Kim.",
                 "fr": "Ambassade de Corée en France, section consulaire : réunion d'information 2025 sur le droit au quotidien et la vie étudiante, animée par James Joong-ho Kim.",
                 "ko": "주프랑스 대한민국 대사관 영사부: 김중호 변호사가 강연한 2025 생활법률 & 유학생활 설명회."},
     "alt": {"en": "Event poster in Korean with a photo of James Joong-ho Kim and the date 5 November 2025, 15:00.",
             "fr": "Affiche en coréen avec une photo de James Joong-ho Kim et la date du 5 novembre 2025, 15 h.",
             "ko": "김중호 변호사 사진과 2025년 11월 5일 15시 일정이 적힌 행사 포스터."}},
    {"src": "assets/img/wislaw-2025.webp", "w": 1200, "h": 831, "date": "2025-04-11",
     "caption": {"en": "Paris Arbitration Week 2025, WISLaw panel: \"Beating the Post-Paris 2024 Olympic Blues: Experiences and Insights on CAS Arbitration Procedures\", hosted by Gaillard Banifatemi Shelbaya Disputes.",
                 "fr": "Paris Arbitration Week 2025, table ronde WISLaw : « Beating the Post-Paris 2024 Olympic Blues: Experiences and Insights on CAS Arbitration Procedures », accueillie par Gaillard Banifatemi Shelbaya Disputes.",
                 "ko": "2025 파리 중재 주간 WISLaw 패널: 「Beating the Post-Paris 2024 Olympic Blues: Experiences and Insights on CAS Arbitration Procedures」, Gaillard Banifatemi Shelbaya Disputes 주최."},
     "alt": {"en": "Four panellists seated before an audience in a Paris office, next to a screen showing the session title and the Olympic rings.",
             "fr": "Quatre intervenants devant le public dans un bureau parisien, à côté d'un écran affichant le titre de la session et les anneaux olympiques.",
             "ko": "파리 사무실에서 청중 앞에 앉은 패널 네 명과 세션 제목 및 올림픽 오륜이 표시된 화면."}},
    {"src": "assets/img/ccicf-seminar.webp", "w": 1200, "h": 900, "date": "",
     "caption": {"en": "CCI Corée France hybrid seminar \"Rencontre avec les entreprises coréennes\", with the Embassy of Korea in France.",
                 "fr": "Séminaire hybride de la CCI Corée France « Rencontre avec les entreprises coréennes », avec l'Ambassade de Corée en France.",
                 "ko": "주불한국상공회의소(CCICF)·주프랑스 대한민국 대사관 하이브리드 세미나 「한국 기업과의 만남」."},
     "alt": {"en": "Four speakers seated on a stage under a large screen showing the seminar title, a moderator speaking at a microphone.",
             "fr": "Quatre intervenants assis sur scène sous un grand écran affichant le titre du séminaire, une modératrice au micro.",
             "ko": "세미나 제목이 띄워진 대형 화면 아래 무대에 앉은 연사 네 명과 마이크 앞의 사회자."}},
    {"src": "assets/img/jk-presenting.webp", "w": 1200, "h": 900, "date": "",
     "caption": {"en": "James Joong-ho Kim presenting the main French business forms (EI, SARL/EURL, SAS/SASU).",
                 "fr": "James Joong-ho Kim présente les principales formes d'entreprise en France (EI, SARL/EURL, SAS/SASU).",
                 "ko": "프랑스의 기본 사업 형태(EI, SARL/EURL, SAS/SASU)를 설명하는 김중호 변호사."},
     "alt": {"en": "A speaker at a lectern beside a Korean flag, pointing to a slide comparing business forms.",
             "fr": "Un intervenant au pupitre à côté d'un drapeau coréen, montrant une diapositive comparant les formes d'entreprise.",
             "ko": "태극기 옆 연단에서 사업 형태 비교 슬라이드를 가리키는 발표자."}},
    {"src": "assets/img/gyeongnam-2025.webp", "w": 1000, "h": 1000, "date": "",
     "caption": {"en": "2025 Gyeongsangnam-do Investment Promotion Conference: signing of investment and cooperation agreements in aerospace and green industries.",
                 "fr": "Conférence 2025 de promotion des investissements de la province du Gyeongsangnam-do : signature d'accords d'investissement et de coopération (aéronautique et industries vertes).",
                 "ko": "2025 경상남도 투자유치 설명회: 우주항공·친환경 산업 투자 및 업무 협약 체결."},
     "alt": {"en": "Delegates holding a banner on stage in front of a screen reading 2025 Gyeongsangnam-do Investment Promotion Conference.",
             "fr": "Des délégués tenant une banderole sur scène devant un écran indiquant la conférence 2025 du Gyeongsangnam-do.",
             "ko": "2025 경상남도 투자유치 설명회 화면 앞 무대에서 현수막을 든 참석자들."}},
]

# Press theme per article (used to group the Press page); keyed by URL
PRESS_THEME = {
    'https://www.francezone.com/news/articleView.html?idxno=95669': 'heritage',
    'https://gallerym9.com/somme-des-parties-m-': 'business',
    'https://placedeparis.com/community/bbs/board.php?bo_table=news_issue&wr_id=1402': 'business',
    'https://www.francezone.com/news/articleView.html?idxno=664353': 'law',
    'https://www.legaltimes.co.kr/news/articleView.html?idxno=34302': 'profile',
    'https://www.joongang.co.kr/article/3752927': 'profile',
    'https://www.khan.co.kr/article/201002281735075': 'heritage',
    'https://www.donga.com/news/Culture/article/all/20100225/26453075/1': 'heritage',
    'https://www.seoul.co.kr/news/society/2010/02/26/20100226029023': 'heritage',
    'https://n.news.naver.com/mnews/article/079/0002133525': 'heritage',
    'https://n.news.naver.com/mnews/article/003/0003107446?sid=102': 'heritage',
    'https://www.donga.com/news/article/all/20091216/24831994/1': 'heritage',
    'https://www.hani.co.kr/arti/politics/diplomacy/392512.html': 'heritage',
    'https://www.yna.co.kr/view/AKR20080910160900005': 'heritage',
    'https://www.nocutnews.co.kr/news/494244': 'heritage',
    'https://n.news.naver.com/mnews/article/001/0002261719?sid=103': 'heritage',
    'https://n.news.naver.com/mnews/article/001/0002258703?sid=103': 'heritage',
    'https://www.hani.co.kr/arti/society/society_general/195031.html': 'heritage',
    'https://n.news.naver.com/mnews/article/001/0001567518?sid=103': 'heritage',
    'https://www.seoul.co.kr/news/newsView.php?id=20070207009012': 'heritage',
    'https://n.news.naver.com/mnews/article/001/0001539822?sid=103': 'heritage',
    'https://n.news.naver.com/mnews/article/001/0001539898?sid=102': 'heritage',
    'http://www.legaltimes.co.kr/news/articleView.html?idxno=89709': 'books',
    'https://www.amazon.fr/dp/B0FWZS7SYM': 'books',
    'https://www.yes24.com/product/goods/160462528': 'books',
    'https://economictimes.indiatimes.com/news/sports/vinesh-phogat-cas-verdict-olympics-2024-disqualification-weight-limit-rules-same-for-all-full-list-of-reasons/articleshow/112633538.cms': 'sport',
    'https://view.asiae.co.kr/article/2022101600063756550': 'business',
    'https://www.chosun.com/site/data/html_dir/2005/11/23/2005112370512.html': 'business',
    'https://www.segye.com/newsView/20210210510631': 'law',
    'https://www.segye.com/newsView/20210208515023': 'law',
    'https://www.lawtimes.co.kr/news/articleView.html?idxno=98725': 'profile',
    'https://www.seoul.co.kr/news/newsView.php?id=20070530014005': 'profile',
    'https://www.chosun.com/site/data/html_dir/1999/03/04/1999030470356.html': 'profile',
}
