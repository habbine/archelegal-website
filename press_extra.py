"""Press page: dated news and events, and selected publications (firm's request, Oct 2026).

Sources: the firm's existing press-page items, and Habbine Estelle KIM's talks and publications
pages (kimavocat.com/conference.html, kimavocat.com/publication.html), checked 30 Oct 2026.
Year-only dates ("2025") are used where the source gives no exact date.
"""


def T(en, fr, ko):
    return {"en": en, "fr": fr, "ko": ko}


HK = T("Habbine Estelle KIM", "Habbine Estelle KIM", "김하빈 변호사")
JK = T("James Joong-ho KIM", "James Joong-ho KIM", "김중호 변호사")
KA_TALKS = "https://www.kimavocat.com/conference.html"

# (date, title, detail, url)
EVENTS = [
    ("2026-10-10",
     T("Salon de l'Étudiant, Korea Pavilion, Paris", "Salon de l'Étudiant, pavillon coréen, Paris", "Salon de l'Étudiant 한국관, 파리"),
     T("Habbine Estelle KIM, moderator and speaker: Korean companies in France, careers and professional opportunities. As Secretary General of the CCICF, with KOSME.",
       "Habbine Estelle KIM, modératrice et intervenante : les entreprises coréennes en France, carrières et opportunités. En qualité de secrétaire générale de la CCICF, avec la KOSME.",
       "김하빈 변호사, 사회 및 발표: 프랑스 내 한국 기업의 커리어와 기회. 한불상공회의소(CCICF) 사무총장 자격, 중소벤처기업진흥공단(KOSME)과 공동 진행."),
     KA_TALKS),
    ("2026-10-01",
     T("IAKL Annual Conference, London (30 Sep – 3 Oct 2026)", "Conférence annuelle de l'IAKL, Londres (30 sept. – 3 oct. 2026)", "IAKL 연례 컨퍼런스, 런던(2026년 9월 30일~10월 3일)"),
     T("Habbine Estelle KIM, speaker: Between Automation and Autonomy, AI, international business and legal practice.",
       "Habbine Estelle KIM, intervenante : entre automatisation et autonomie, IA, affaires internationales et pratique du droit.",
       "김하빈 변호사, 발표: 자동화와 자율 사이, AI·국제 비즈니스·법률 실무."),
     KA_TALKS),
    ("2026-01-01",
     T("Archè appointed international legal adviser to KDIC", "Archè nommé conseil juridique international de la KDIC", "아르케, 예금보험공사(KDIC) 국제 법률 자문 위촉"),
     T("Foreign asset recovery for the Korea Deposit Insurance Corporation, from 1 January 2026.",
       "Recouvrement d'actifs à l'étranger pour la Korea Deposit Insurance Corporation, à compter du 1er janvier 2026.",
       "예금보험공사의 해외 재산 환수 업무, 2026년 1월 1일부터."),
     "https://www.kimavocat.com/certification.html"),
    ("2025-11-05",
     T("Seminar at the Embassy of Korea in France", "Séminaire à l'Ambassade de Corée en France", "주프랑스 대한민국 대사관 세미나"),
     T("James Joong-ho KIM, information session on everyday law and student life, consular section.",
       "James Joong-ho KIM, séance d'information sur le droit au quotidien et la vie étudiante, section consulaire.",
       "김중호 변호사, 영사과 생활법률·유학생활 설명회."),
     ""),
    ("2025-10-17",
     T("New book: A Forgotten Promise", "Nouvel ouvrage : A Forgotten Promise", "신간 「잊혀진 약속」(A Forgotten Promise)"),
     T("James Joong-ho KIM's novel based on the Oegyujanggak restitution case.",
       "Roman de James Joong-ho KIM inspiré de l'affaire de restitution de l'Oegyujanggak.",
       "외규장각 반환 소송을 바탕으로 한 김중호 변호사의 소설."),
     "https://www.amazon.fr/dp/B0FWZS7SYM"),
    ("2025-09-19",
     T("AFEC Jeunes conference on sport and EU law, Paris", "Colloque AFEC Jeunes, sport et droit de l'Union, Paris", "AFEC 청년위원회 스포츠·EU법 컨퍼런스, 파리"),
     T("Habbine Estelle KIM, moderator of the round table on sports governance.",
       "Habbine Estelle KIM, modératrice de la table ronde sur la gouvernance du sport.",
       "김하빈 변호사, 스포츠 거버넌스 라운드테이블 사회."),
     KA_TALKS),
    ("2025-04-11",
     T("Paris Arbitration Week", "Paris Arbitration Week", "파리 중재 주간(Paris Arbitration Week)"),
     T("Habbine Estelle KIM, speaker on CAS arbitration procedures after the Paris 2024 Games (WISLaw panel).",
       "Habbine Estelle KIM, intervenante sur les procédures d'arbitrage devant le TAS après les Jeux de Paris 2024 (panel WISLaw).",
       "김하빈 변호사, 파리 2024 이후 스포츠중재재판소(CAS) 절차 발표(WISLaw 패널)."),
     KA_TALKS),
    ("2025",
     T("IAKL Annual Conference, Seoul", "Conférence annuelle de l'IAKL, Séoul", "IAKL 연례 컨퍼런스, 서울"),
     T("Habbine Estelle KIM, speaker: regulatory and trade requirements for conducting international business.",
       "Habbine Estelle KIM, intervenante : exigences réglementaires et commerciales des affaires internationales.",
       "김하빈 변호사, 발표: 국제 비즈니스를 위한 규제·통상 요건."),
     KA_TALKS),
    ("2025",
     T("IAKL European Conference, Berlin", "Conférence européenne de l'IAKL, Berlin", "IAKL 유럽 컨퍼런스, 베를린"),
     T("Habbine Estelle KIM, co-organiser and speaker: EU regulation and AI.",
       "Habbine Estelle KIM, co-organisatrice et intervenante : réglementation européenne et IA.",
       "김하빈 변호사, 공동 기획 및 발표: EU 규제와 AI."),
     KA_TALKS),
    ("2025",
     T("Station F · HEC Incubator, JETRO and IndiaAI seminar", "Station F · Incubateur HEC, séminaire JETRO et IndiaAI", "스테이션 F · HEC 인큐베이터, JETRO·IndiaAI 세미나"),
     T("Habbine Estelle KIM, speaker: navigating French incorporation, a legal guide for international startups.",
       "Habbine Estelle KIM, intervenante : créer sa société en France, guide juridique pour les startups internationales.",
       "김하빈 변호사, 발표: 해외 스타트업을 위한 프랑스 법인 설립 법률 가이드."),
     KA_TALKS),
    ("2025",
     T("K-Startup Day", "K-Startup Day", "K-스타트업 데이"),
     T("Mentoring session for Korean startups.", "Session de mentorat pour des startups coréennes.", "한국 스타트업 멘토링 세션."),
     ""),
    ("2025",
     T("KOTRA Paris webinar", "Webinaire KOTRA Paris", "KOTRA 파리 웨비나"),
     T("Webinar for Korean companies on doing business in France.", "Webinaire pour les entreprises coréennes sur les affaires en France.", "한국 기업 대상 프랑스 비즈니스 웨비나."),
     ""),
    ("2024",
     T("France-Korea Chamber of Commerce and Industry (CCICF), Paris", "Chambre de commerce et d'industrie France-Corée (CCICF), Paris", "한불상공회의소(CCICF), 파리"),
     T("Habbine Estelle KIM, speaker on French employment law: harassment.",
       "Habbine Estelle KIM, intervenante en droit du travail : le harcèlement.",
       "김하빈 변호사, 프랑스 노동법 발표: 직장 내 괴롭힘."),
     KA_TALKS),
    ("2024",
     T("IAKL European Conference, Brussels", "Conférence européenne de l'IAKL, Bruxelles", "IAKL 유럽 컨퍼런스, 브뤼셀"),
     T("Habbine Estelle KIM, speaker: professional athletes and anti-doping rules.",
       "Habbine Estelle KIM, intervenante : les athlètes professionnels et les règles antidopage.",
       "김하빈 변호사, 발표: 프로 선수와 도핑 방지 규정."),
     KA_TALKS),
    ("2024",
     T("Station F · HEC Incubator, KSC seminar", "Station F · Incubateur HEC, séminaire KSC", "스테이션 F · HEC 인큐베이터, KSC 세미나"),
     T("Habbine Estelle KIM, speaker: legal and intellectual property considerations for startups.",
       "Habbine Estelle KIM, intervenante : questions juridiques et de propriété intellectuelle pour les startups.",
       "김하빈 변호사, 발표: 스타트업의 법률·지식재산권 고려사항."),
     KA_TALKS),
    ("2023",
     T("Station F · HEC Incubator, KSC seminar", "Station F · Incubateur HEC, séminaire KSC", "스테이션 F · HEC 인큐베이터, KSC 세미나"),
     T("Habbine Estelle KIM, speaker: conducting business in France, a legal approach.",
       "Habbine Estelle KIM, intervenante : faire des affaires en France, approche juridique.",
       "김하빈 변호사, 발표: 프랑스에서의 비즈니스, 법률적 접근."),
     KA_TALKS),
    ("2023",
     T("Guest lectures, Université Paris Cité and Aix-Marseille Université", "Cours invités, Université Paris Cité et Aix-Marseille Université", "파리 시테 대학교·엑스마르세유 대학교 초빙 강의"),
     T("Habbine Estelle KIM, guest lecturer and jury member, 2023–2026.",
       "Habbine Estelle KIM, intervenante et membre du jury, 2023–2026.",
       "김하빈 변호사, 초빙 강사 및 심사위원, 2023–2026."),
     KA_TALKS),
]

# date -> Services section it demonstrates (shown as a small link on the entry)
EVENT_SERVICE = {"2026-10-10": "advice", "2026-01-01": "litigation"}
RELATED = T("Related practice", "Expertise liée", "관련 업무")
EVENTS_SHOWN = 6  # the rest go under "Show all"

PUBS_H = T("Publications and institutional work", "Publications et travaux institutionnels", "논문 및 기관 활동")
PUBS_P = T("Selected research and contributions by Habbine Estelle KIM.",
           "Sélection de travaux de recherche et de contributions de Habbine Estelle KIM.",
           "김하빈 변호사의 주요 연구와 기관 기여.")
PUBS_ALL = T("All publications on kimavocat.com", "Toutes les publications sur kimavocat.com", "kimavocat.com에서 전체 논문 보기")
PUBS_ALL_URL = "https://www.kimavocat.com/publication.html"

# (year, title as published, detail, url)
PUBS = [
    ("2025", "ELI Principles and Guidance for Enforcement Against Digital Assets",
     T("European Law Institute. Member of the Consultative Committee.", "European Law Institute. Membre du comité consultatif.", "유럽법연구소(ELI). 자문위원회 위원."),
     "https://www.europeanlawinstitute.eu/projects-publications/current-projects/current-projects/eli-enforcement-against-digital-assets/"),
    ("2025", "ELI Guiding Principles and Model Rules on Digital Assistants for Consumer Contracts",
     T("European Law Institute. Member of the Consultative Committee.", "European Law Institute. Membre du comité consultatif.", "유럽법연구소(ELI). 자문위원회 위원."),
     "https://www.europeanlawinstitute.eu/fileadmin/user_upload/p_eli/Projects/Algorithmic_Contracts/Guiding_Principles_and_Model_Rules_on_Digital_Assistants_for_Consumer_Contracts.pdf"),
    ("2025", "Observations de l'AFEC sur la contribution du droit de la concurrence à la promotion du développement durable",
     T("French Association for Competition Law Studies (AFEC). Coordinator, AFEC Jeunes. In French.",
       "Association française d'étude de la concurrence (AFEC). Coordinatrice, AFEC Jeunes.",
       "프랑스 경쟁법연구회(AFEC). AFEC 청년위원회 코디네이터. 프랑스어."),
     "https://afec.asso.fr/observations-de-lafec-sur-la-contribution-du-droit-de-la-concurrence-a-la-promotion-du-developpement-durable/"),
    ("2024", "ELI Guiding Principles and Model Rules on Algorithmic Contracts",
     T("European Law Institute project. Member of the Consultative Committee.", "Projet de l'European Law Institute. Membre du comité consultatif.", "유럽법연구소(ELI) 프로젝트. 자문위원회 위원."),
     "https://www.europeanlawinstitute.eu/projects-publications/current-projects/current-projects/eli-guiding-principles-and-model-rules-on-algorithmic-contracts/"),
    ("2023", "Greening Consumer Welfare: Towards a New Perspective on Consumer Protection",
     T("InDret 2.23, Universitat Pompeu Fabra. Shortlisted for the UPF international conference 2022.",
       "InDret 2.23, Universitat Pompeu Fabra. Sélectionné pour la conférence internationale de l'UPF 2022.",
       "InDret 2.23, 폼페우 파브라 대학교. 2022 UPF 국제 컨퍼런스 발표 선정."),
     "https://indret.com/greening-consumer-welfare-towards-a-new-perspective-on-consumer-protection/?edicion=2.23"),
    ("2022", "Decentralisation and Digital Transformation: User e-Consciousness and Accountability of Intermediators",
     T("With Maciej Bernard Plotka. Shortlisted for the ELI Young Lawyers Award 2022.",
       "Avec Maciej Bernard Plotka. Présélectionné pour le ELI Young Lawyers Award 2022.",
       "Maciej Bernard Plotka 공저. 2022 ELI 청년 법률가상 최종 후보."),
     "https://ssrn.com/abstract=4256243"),
    ("2022", "Where Esport Law Does Not Exist · Quand la loi de l'esport n'existe pas",
     T("Comparative study of French and European esport law. In English and French.",
       "Étude comparée du droit français et européen de l'esport. En anglais et en français.",
       "프랑스·유럽 e스포츠법 비교 연구. 영어·프랑스어."),
     "https://ssrn.com/abstract=4047288"),
]

HK_TOPICS = T(
    ["Setting up companies and doing business between Korea and France (inbound and outbound)", "French employment law for Korean groups' subsidiaries",
     "Sports law and CAS arbitration (Paris 2024)", "AI, EU law and digital regulation"],
    ["Implantation et affaires entre la Corée et la France, dans les deux sens", "Droit du travail français pour les filiales de groupes coréens",
     "Droit du sport et arbitrage devant le TAS (Paris 2024)", "IA, droit de l'Union et régulation du numérique"],
    ["한국·프랑스 간 법인 설립과 비즈니스(진출 및 유치)", "한국 기업 현지 법인을 위한 프랑스 노동법",
     "스포츠법과 CAS 중재(파리 2024)", "AI, EU법과 디지털 규제"],
)

SHOW_ALL = T("Show all {} events", "Voir les {} événements", "행사 {}건 모두 보기")
OPEN = T("Details", "Détails", "자세히")
