"""Services and sectors supplied by the firm (FR original; EN/KO translations to be reviewed)."""

# (id, title, intro, bullets)
SERVICES = {
    "en": [
        ("corporate", "Corporate, M&A, contracts and IP", "Setting up and structuring companies, acquisitions, commercial contracts and intellectual property.",
         ["Incorporating companies, subsidiaries and branches; articles of association and shareholders' agreements", "Corporate secretarial work, governance and data protection", "M&A: fundraising and exits, due diligence, takeover bids, negotiation of terms", "Commercial, distribution, subcontracting, partnership and joint-venture contracts", "Licensing, trademarks, designs and technology transfer", "Commercial leases: drafting, review and advice"]),
        ("employment", "Employment and professional immigration", "French employment law is protective and procedural. We help foreign employers get it right from the first hire.",
         ["Employment contracts (fixed-term and permanent), resignation, amicable termination, dismissal", "Harassment, discrimination and equal treatment", "Transfers of undertakings", "Litigation before the Conseil de prud'hommes", "International mobility, posted workers and assignees", "Visas and work permits"]),
        ("litigation", "Disputes, debt recovery and insolvency", "Representation in court and arbitration, with a partner following the case from start to finish.",
         ["Dispute prevention and settlement negotiation", "Asset freezing, provisional measures and judicial mortgages", "Civil, commercial, administrative and employment litigation", "National and international arbitration", "Debt recovery: formal notice, seizures, summary proceedings", "Insolvency and restructuring: assistance through the process, claims, related litigation", "Product liability and industrial risk"]),
        ("advice", "Foreign investment and international projects", "Cross-border work that involves several jurisdictions and several teams at once.",
         ["Support for foreign investment and project finance", "Partnership and joint-venture agreements; offering documents", "Structuring, implementing and exiting investments", "Regulatory compliance, data protection and cybersecurity", "Coordination with local counsel in other countries", "Projects for public institutions"]),
    ],
    "fr": [
        ("corporate", "Sociétés, fusions-acquisitions, contrats et propriété intellectuelle", "Création et structuration de sociétés, acquisitions, contrats commerciaux et propriété intellectuelle.",
         ["Création de sociétés, filiales et succursales ; statuts et pactes d'associés", "Secrétariat juridique, gouvernance et protection des données", "Fusions-acquisitions : levées de fonds et cessions, audits d'acquisition, offres publiques, négociation des conditions", "Contrats commerciaux, de distribution, de sous-traitance, de partenariat et de joint-venture", "Licences, marques, dessins et modèles, transfert de technologie", "Baux commerciaux : rédaction, revue et conseil"]),
        ("employment", "Droit du travail et immigration professionnelle", "Le droit du travail français est protecteur et formaliste. Nous aidons les employeurs étrangers à bien faire dès la première embauche.",
         ["Contrats de travail (CDD et CDI), démission, rupture conventionnelle, licenciement", "Harcèlement, discrimination et égalité de traitement", "Transferts d'entreprise", "Contentieux devant le conseil de prud'hommes", "Mobilité internationale, salariés détachés et expatriés", "Visas et autorisations de travail"]),
        ("litigation", "Contentieux, recouvrement et procédures collectives", "Représentation devant les tribunaux et en arbitrage, avec un associé qui suit le dossier du début à la fin.",
         ["Prévention des litiges et négociation transactionnelle", "Saisies conservatoires, mesures provisoires et hypothèques judiciaires", "Contentieux civil, commercial, administratif et social", "Arbitrage national et international", "Recouvrement : mise en demeure, saisies, référés", "Procédures collectives et restructuration : accompagnement, déclarations de créances, contentieux associés", "Responsabilité du fait des produits et risque industriel"]),
        ("advice", "Investissements étrangers et projets internationaux", "Un travail transfrontalier qui mobilise plusieurs juridictions et plusieurs équipes à la fois.",
         ["Accompagnement des investissements étrangers et financement de projets", "Accords de partenariat et de joint-venture ; documents d'offre", "Structuration, mise en œuvre et sortie d'investissements", "Conformité réglementaire, protection des données et cybersécurité", "Coordination avec des conseils locaux dans d'autres pays", "Projets pour des institutions publiques"]),
    ],
    "ko": [
        ("corporate", "기업법·M&A·계약·지식재산", "회사 설립과 구조 설계, 인수, 상사 계약, 지식재산.",
         ["회사·자회사·지점 설립, 정관 및 주주간 계약", "법인 사무, 지배구조 및 개인정보 보호", "M&A: 투자 유치와 엑시트, 실사, 공개매수, 거래 조건 협상", "상사·유통·하도급·파트너십·합작투자 계약", "라이선스, 상표, 디자인 및 기술 이전", "상업용 임대차: 작성, 검토 및 자문"]),
        ("employment", "노동법 및 전문직 이민", "프랑스 노동법은 보호적이고 절차 중심입니다. 외국 사용자가 첫 채용부터 올바르게 하도록 돕습니다.",
         ["근로계약(기간제·무기), 사직, 합의 해지, 해고", "괴롭힘, 차별 및 평등 대우", "사업 양도에 따른 근로관계 승계", "노동재판소(Conseil de prud'hommes) 소송", "국제 인력 이동, 파견 근로자 및 주재원", "비자 및 취업 허가"]),
        ("litigation", "분쟁·채권 회수·도산", "법원과 중재에서의 대리, 파트너가 사건을 처음부터 끝까지 담당합니다.",
         ["분쟁 예방 및 합의 협상", "자산 동결, 보전 처분 및 재판상 저당권", "민사·상사·행정·노동 소송", "국내외 중재", "채권 회수: 최고, 압류, 신속 절차", "도산 및 구조조정: 절차 지원, 채권 신고, 관련 소송", "제조물 책임 및 산업 위험"]),
        ("advice", "해외 투자 및 국제 프로젝트", "여러 관할과 여러 팀이 동시에 얽히는 국경 간 업무.",
         ["해외 투자 및 프로젝트 금융 지원", "파트너십·합작투자 계약, 투자 설명 문서", "투자의 구조 설계, 실행 및 회수", "규제 준수, 개인정보 보호 및 사이버 보안", "타국 현지 변호사와의 협업", "공공기관 프로젝트"]),
    ],
}

SECTORS = {
    "fr": ["Construction", "Agroalimentaire & Boissons", "Distribution & Retail", "Automobile", "Technologie & IA", "E-commerce & Digital", "Art", "Mode & Luxe", "Beauté & Cosmétique", "Santé & Sciences de la vie", "Dispositifs médicaux"],
    "en": ["Construction", "Agrifood & Beverage", "Distribution & Retail", "Automotive", "Technology & AI", "E-commerce & Digital", "Art", "Fashion & Luxury", "Beauty & Cosmetics", "Health & Life Sciences", "Medical Devices"],
    "ko": ["건설", "식품·음료", "유통·리테일", "자동차", "기술·AI", "이커머스·디지털", "예술", "패션·럭셔리", "뷰티·화장품", "헬스케어·생명과학", "의료기기"],
}


def apply(T):
    for lang in ("en", "fr", "ko"):
        t = T[lang]
        t["services"]["items"] = SERVICES[lang]
        t["services"]["index"] = [(title, sid) for sid, title, _, _ in SERVICES[lang]]
        t["home"]["industries"] = [("", SECTORS[lang])]


HERO = {
    "en": {"kicker": "Boutique international law firm · Headquartered in Paris",
           "h1": "Cross-border law for international business.",
           "lede": "For over 25 years, we have advised companies doing business between Europe, Asia, Africa, the United States and the Middle East: company set-up, employment, disputes and international projects. In French, English and Korean.",
           "strip": [("Bar admissions", "Paris Bar · New York Bar"), ("Working languages", "French · English · Korean"), ("Affiliations", "ELI · KOCCA · CCICF · Station F, HEC Incubator · IAKL")]},
    "fr": {"kicker": "Cabinet d'avocats international de type boutique · Siège à Paris",
           "h1": "Un droit transfrontalier pour les affaires internationales.",
           "lede": "Depuis plus de 25 ans, nous conseillons les entreprises qui exercent entre l'Europe, l'Asie, l'Afrique, les États-Unis et le Moyen-Orient : création de société, droit du travail, contentieux et projets internationaux. En français, en anglais et en coréen.",
           "strip": [("Barreaux", "Barreau de Paris · Barreau de New York"), ("Langues de travail", "Français · Anglais · Coréen"), ("Affiliations", "ELI · KOCCA · CCICF · Station F, Incubateur HEC · IAKL")]},
    "ko": {"kicker": "부티크 국제 로펌 · 파리 본사",
           "h1": "국제 비즈니스를 위한 국경 간 법률 자문.",
           "lede": "25년 넘게 유럽, 아시아, 아프리카, 미국, 중동 사이에서 사업하는 기업을 자문해 왔습니다. 회사 설립, 노동, 분쟁, 국제 프로젝트를 한국어, 프랑스어, 영어로 지원합니다.",
           "strip": [("변호사 등록", "파리 변호사회 · 뉴욕 변호사회"), ("업무 언어", "프랑스어 · 영어 · 한국어"), ("소속 단체", "ELI · KOCCA · CCICF · 스테이션 F HEC 인큐베이터 · IAKL")]},
}
_apply_old = apply


def apply(T):
    _apply_old(T)
    for lang in ("en", "fr", "ko"):
        h = T[lang]["home"]
        h["h1"], h["lede"], h["kicker"], h["strip"] = HERO[lang]["h1"], HERO[lang]["lede"], HERO[lang]["kicker"], HERO[lang]["strip"]
