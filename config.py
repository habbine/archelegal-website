"""Site-wide settings. Edit this file, then run: python3 src/build.py"""

DOMAIN = "archelegal.com"           # canonical domain (written to CNAME)
SITE_URL = "https://www.archelegal.com"  # change to https://archelegal.com if you prefer the bare domain
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

PRESS = [
    {"url": "https://n.news.naver.com/article/277/0005162213", "outlet": "Naver News", "lang": "ko"},
]

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
