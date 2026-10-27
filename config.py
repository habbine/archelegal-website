"""Site-wide settings. Edit this file, then run: python3 build.py"""

DOMAIN = "archelegal.com"           # canonical domain (written to CNAME)
SITE_URL = "https://archelegal.com"  # matches CNAME (apex); GitHub Pages redirects www to it
FIRM = "Archè"
FIRM_FULL = "Archè SELARL"

EMAIL = "paris@archelegal.com"
PHONE = "+33 1 4335 8410"
PHONE_TEL = "+33143358410"
ADDRESS_LINES = ["57 Quai de Grenelle", "75015 Paris", "France"]
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
SEOUL = {"address": "", "phone": "", "email": EMAIL}
HONGKONG = {"address": "", "phone": "", "email": EMAIL}

PEOPLE = [
    {
        "slug": "jk",
        "initials": "JK",
        "photo": "",  # e.g. "assets/img/james-kim.jpg" once you add the file
        "name": "James Joong-ho Kim",
        "email": "james.kim@archelegal.com",
        "linkedin": "",
    },
    {
        "slug": "hk",
        "initials": "HK",
        "photo": "",
        "name": "Habbine Estelle Kim",
        "email": "habbine.kim@archelegal.com",
        "linkedin": "https://www.linkedin.com/in/habbine-kim-avocat/",
    },
    {
        "slug": "dk",
        "initials": "DK",
        "photo": "",
        "name": "Dabin Kevin Kim",
        "email": "dabin.kim@archelegal.com",
        "linkedin": "",
    },
]

# Press coverage, newest first. "title" is the original headline (shown as is, in its language).
# "outlet" and "about" are per page language; "about" may be omitted for a language (then only the title shows).
def _o(en, ko, fr=None):
    return {"en": en, "fr": fr or en, "ko": ko}

PRESS = [
    {"date": "2025-10-19", "outlet": _o("Legal Times", "리걸타임즈"), "lang": "ko",
     "url": "http://www.legaltimes.co.kr/news/articleView.html?idxno=89709",
     "title": "[신간소개] 파리에서 활동하는 김중호 변호사의 《잊혀진 약속》",
     "about": {"en": "New book: James Joong-ho Kim's novel A Forgotten Promise",
               "fr": "Parution du roman de James Joong-ho Kim, A Forgotten Promise"}},
    {"date": "2025-10-14", "outlet": _o("Book · BOOKK (YES24)", "도서 · 부크크 (YES24)", "Livre · BOOKK (YES24)"), "lang": "ko",
     "url": "https://www.yes24.com/product/goods/160462528",
     "title": "법쟁이 탈출기 (김중호 지음, ISBN 9791112072207)",
     "about": {"en": "Autobiographical essay by James Joong-ho Kim on 25 years of practice in France",
               "fr": "Essai autobiographique de James Joong-ho Kim sur 25 ans d'exercice en France"}},
    {"date": "2022-10-16", "outlet": _o("Asia Economy", "아시아경제"), "lang": "ko",
     "url": "https://view.asiae.co.kr/article/2022101600063756550",
     "title": "[인터뷰] 'K-문화에 세계 매료'…김중호 프랑스 변호사, \"한류 수출 기업, 행정·법률 정보 숙지 필수\"",
     "about": {"en": "Interview: what Korean companies need to know before entering the French market",
               "fr": "Entretien : ce que les entreprises coréennes doivent savoir avant de s'implanter en France"}},
    {"date": "2016-02-25", "outlet": _o("Law Times", "법률신문"), "lang": "ko",
     "url": "https://www.lawtimes.co.kr/news/articleView.html?idxno=98725",
     "title": "[주목 이사람] 한국인 첫 프랑스 변호사… 세계시장 공략",
     "about": {"en": "Profile of the first Korean admitted to the French bar and the founding of Archè",
               "fr": "Portrait du premier avocat coréen au barreau français et de la création d'Archè"}},
    {"date": "2010-02-26", "outlet": _o("Seoul Shinmun", "서울신문"), "lang": "ko",
     "url": "http://www.seoul.co.kr/news/newsView.php?id=20100226029023",
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
    {"date": "2007-03-08", "outlet": _o("The Hankyoreh", "한겨레"), "lang": "ko",
     "url": "https://www.hani.co.kr/arti/society/society_general/195031.html",
     "title": "르몽드 '외규장각도서 반환촉구' 광고 실리기까지",
     "about": {"en": "Behind the Le Monde advertisement calling for the return of the Oegyujanggak books",
               "fr": "Les coulisses de l'annonce parue dans Le Monde pour le retour des livres de l'Oegyujanggak"}},
    {"date": "2007-02-06", "outlet": _o("Yonhap News", "연합뉴스"), "lang": "ko",
     "url": "https://n.news.naver.com/mnews/article/001/0001539822?sid=103",
     "title": "<인터뷰> 외규장각 반환소송 김중호 변호사",
     "about": {"en": "Interview before filing the restitution claim at the Paris Administrative Court",
               "fr": "Entretien avant le dépôt de la requête en restitution devant le tribunal administratif de Paris"}},
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
PRESS_HOME = 3  # how many of the latest items the home page shows

# Legal notice fields (French law requires these). Fill them in; build.py warns about blanks.
LEGAL = {
    "raison_sociale": "Archè SELARL",
    "forme": "Société d'exercice libéral à responsabilité limitée (SELARL)",
    "capital": "",
    "siege": "57 Quai de Grenelle, 75015 Paris, France",
    "rcs": "",
    "tva": "",
    "barreau": "",
    "rcp": "",
    "directeur_publication": "",
    "hebergeur": "GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, USA",
}
