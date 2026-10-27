"""Experience grouped by client need. Source: the firm's own lists of matters and clients (Oct 2026), supplied by the firm.
Client names appear as supplied by the firm. Do not add matters, figures or outcomes that are not in the firm's lists.
Indicative figures are counted from the lists below at build time (see figures())."""

FOOTNOTE = {
    "en": "Summaries of past work. Each matter depends on its own facts; past results do not guarantee future outcomes. Figures are indicative and count only the matters and clients listed on this page.",
    "fr": "Résumés de dossiers passés. Chaque affaire dépend de ses propres faits ; les résultats passés ne préjugent pas des résultats futurs. Les chiffres sont indicatifs et ne comptent que les dossiers et clients cités sur cette page.",
    "ko": "과거 업무 요약입니다. 각 사건은 고유한 사실관계에 따라 달라지며, 과거의 결과가 향후 결과를 보장하지 않습니다. 수치는 참고용이며 이 페이지에 소개된 사례와 고객만 집계한 것입니다.",
}

def T(en, fr, ko):
    return {"en": en, "fr": fr, "ko": ko}

# ---- Entering France and Europe: clients by category (firm's list) ----
ENTRY = [
    (T("Listed Korean groups", "Groupes coréens cotés", "KOSPI 상장사 및 그룹사"),
     ["Samsung Electronics", "Samsung C&T", "Samsung Electro-Mechanics", "Samsung Techwin", "Samsung Medison", "Celltrion", "Hanwha Q CELLS", "LG Chem", "LG Energy Solution", "LG Fashion", "SK Siltron", "SK Innovation", "Hyundai Innocean", "Hyundai Capital", "Naver", "Naver Webtoon", "Hyosung", "Hi-M Solutek"]),
    (T("KOSDAQ-listed and mid-sized companies", "Sociétés cotées au KOSDAQ et ETI", "코스닥 상장사 및 중견기업"),
     ["Kolmar Korea", "Vatech", "Shinhan Diamond", "Iljin Group", "Biogenics", "Seoul Semiconductor", "YG-1", "Sena Technologies", "Dasan Networks", "Booyoung", "Kokam", "IICOMBINED (Gentle Monster)"]),
    (T("Automotive, batteries, parts and tyres", "Automobile, batteries, équipements et pneumatiques", "자동차·배터리·부품·타이어"),
     ["Hyundai Motor", "Kia", "Kumho Tire", "Nexen Tire", "Hankook Tire", "Wooshin Systems"]),
    (T("Airlines and logistics", "Aérien et logistique", "항공·물류"),
     ["Korean Air", "Asiana Airlines", "T'way Air (Trinity)", "LX Pantos", "AIF", "FC Logistique"]),
    (T("Banking and finance", "Banque et finance", "금융"),
     ["Samsung Securities", "Samchully Asset Management", "Woori Investment", "Hana Bank (KEB)", "BNP Paribas", "Société Générale"]),
    (T("Broadcasting and media", "Audiovisuel et médias", "방송·미디어"),
     ["MBC", "SBS", "KBS", "KBS Media", "Iyuno Media Group"]),
    (T("Internet and content", "Internet et contenus", "IT·콘텐츠"),
     ["Delitoon", "Kidari Studio"]),
    (T("Healthcare and pharmaceuticals", "Santé et pharmacie", "의료·바이오·제약"),
     ["Osstem Implant", "Hanmi Pharm", "Hanall Biopharma"]),
    (T("Food and beverage", "Restauration et boissons", "F&B"),
     ["BLD", "LBM Corp. (London Bagel Museum)", "Red Deli (Suzie Cuisine)", "Terarosa"]),
    (T("Fashion and cosmetics", "Mode et cosmétiques", "패션·화장품"),
     ["Solid Homme & Wooyoungmi", "Songzio", "DHC Group", "Yonwoo", "LG H&H", "Amorepacific", "Newlife (China)"]),
    (T("Public bodies and institutions", "Organismes et institutions publics", "공공기관·공기업"),
     ["Nonghyup", "Suhyup", "K-water", "KEPCO", "KEPCO E&C", "KHNP", "KOCCA", "King Sejong Institute Foundation", "aT (Korea Agro-Fisheries & Food Trade Corporation)", "Korail", "Korean Register", "KOTRA", "Korean Cultural Centre", "French National Olympic Committee", "Korean Delegation to the OECD", "Embassy of Korea in France"]),
    (T("Startups", "Startups", "스타트업"),
     ["CryptoLab", "Fashion Style Map", "CLO Virtual Fashion", "Hopae"]),
]

# ---- M&A: selected transactions ----
TRANSACTIONS = [
    ("Naver Corporation (Korea)", T("Acquisition of a French AI R&D centre.", "Acquisition d'un centre de R&D en IA en France.", "프랑스 AI 연구개발 센터 인수")),
    ("Naver France", T("Acquisition of an internet platform in Spain and related financing of €150 million.", "Acquisition d'une plateforme internet en Espagne et financement associé de 150 millions d'euros.", "스페인 인터넷 플랫폼 인수 및 1억 5천만 유로 규모 관련 금융")),
    ("Korean Asset Management & Energy Consortium", T("Acquisition of 25 solar farms in France.", "Acquisition de 25 fermes solaires en France.", "프랑스 태양광 발전소 25개소 인수")),
    ("Korean Group D", T("Acquisition of a cosmetics manufacturing and distribution business in Provence.", "Acquisition d'une activité de fabrication et de distribution de cosmétiques en Provence.", "프로방스 지역 화장품 제조·유통 사업 인수")),
    ("KEPCO & KHNP (Korea)", T("JV share transfer with AREVA for a uranium project in Niger.", "Cession de parts de joint-venture avec AREVA pour un projet d'uranium au Niger.", "니제르 우라늄 프로젝트 관련 AREVA와의 합작사 지분 양수도")),
    ("Systra SA (France)", T("Acquisition of two Korean civil engineering companies in Korea.", "Acquisition de deux sociétés coréennes de génie civil en Corée.", "한국 토목 엔지니어링 기업 2곳 인수")),
    ("INSEEC Group (France)", T("Acquisition of a controlling stake in a Korean company.", "Prise de contrôle d'une société coréenne.", "한국 기업 경영권 인수")),
    ("Samsung Climate Control Co.", T("Equity sale to Valeo's French affiliate through share and asset transfers.", "Cession de participation à une filiale française de Valeo par transferts d'actions et d'actifs.", "주식 및 자산 이전을 통한 발레오 프랑스 계열사 대상 지분 매각")),
    ("Samsung C&T", T("Partnership with PSA for aluminium automotive wheel development and production.", "Partenariat avec PSA pour le développement et la production de jantes automobiles en aluminium.", "PSA와의 알루미늄 자동차 휠 개발·생산 파트너십")),
    ("Samsung C&T France", T("Transfer of the petrochemical business to Samsung C&T Germany.", "Transfert de l'activité pétrochimique à Samsung C&T Allemagne.", "석유화학 사업의 독일 삼성물산 이전")),
    ("Samsung Otelinox (Romania)", T("Acquisition of a controlling stake in a European stainless steel distribution business.", "Prise de contrôle d'une activité européenne de distribution d'acier inoxydable.", "유럽 스테인리스강 유통 사업 경영권 인수")),
    ("Samsung Techwin (Korea)", T("Acquisition of the digital camera business from Samsung France.", "Reprise de l'activité appareils photo numériques de Samsung France.", "삼성 프랑스로부터 디지털카메라 사업 인수")),
    ("Korean Mobile Phone Manufacturer", T("Acquisition of a French telecom baseband chip and software R&D business, including technology and personnel transfer and an R&D centre.", "Acquisition d'une activité française de R&D en puces et logiciels de bande de base, avec transfert de technologie et de personnel et centre de R&D.", "프랑스 통신 베이스밴드 칩·소프트웨어 R&D 사업 인수(기술·인력 이전 및 R&D 센터 포함)")),
    ("Singapore-based IT & Media Group", T("Acquisitions in France and Russia.", "Acquisitions en France et en Russie.", "프랑스 및 러시아 기업 인수")),
    ("SG", T("Acquisition of L Foundry production assets through judicial auction.", "Acquisition des actifs de production de L Foundry par adjudication judiciaire.", "법원 경매를 통한 L Foundry 생산 자산 인수")),
    ("AIF Group", T("Acquisition and merger of a French forwarding company, including dissolution of the target.", "Acquisition et fusion d'un transitaire français, avec dissolution de la cible.", "프랑스 운송주선 기업 인수·합병 및 대상회사 해산")),
    ("Delitoon", T("Acquisition of a controlling stake in a French company.", "Prise de contrôle d'une société française.", "프랑스 기업 경영권 인수")),
    ("KOSDAQ-listed webtoon company", T("M&A, strategic investment, convertible bonds and share transfers in France.", "Fusion-acquisition, investissement stratégique, obligations convertibles et cessions d'actions en France.", "프랑스 내 M&A, 전략적 투자, 전환사채 및 주식 양수도")),
    ("Hanall Pharma", T("Acquisition of patents and establishment of a French affiliate.", "Acquisition de brevets et création d'une filiale française.", "특허 인수 및 프랑스 법인 설립")),
    ("Modetour", T("Acquisition of shares and management rights in a French travel agency.", "Acquisition d'actions et du contrôle d'une agence de voyages française.", "프랑스 여행사 주식 및 경영권 인수")),
    ("KBS Media", T("Acquisition of a French satellite broadcasting company.", "Acquisition d'une société française de diffusion par satellite.", "프랑스 위성방송 중계사 인수")),
    ("Korean Company J", T("Tender for the acquisition of the Sonia Rykiel brand and related assets.", "Offre de reprise de la marque Sonia Rykiel et des actifs associés.", "소니아 리키엘 브랜드 및 관련 자산 인수 입찰")),
    ("Korean Consortium", T("Investment in a French EV manufacturer in liquidation, including share acquisition and Asian R&D and design centres.", "Investissement dans un constructeur français de véhicules électriques en liquidation, avec prise de participation et centres de R&D et de design en Asie.", "청산 중인 프랑스 전기차 제조사 투자(지분 인수 및 아시아 R&D·디자인 센터 포함)")),
    ("Company D", T("Asset acquisition and business transfer of consumer products from a French company.", "Acquisition d'actifs et reprise d'une activité de produits de consommation d'une société française.", "프랑스 기업의 소비재 사업 양수도 및 자산 인수")),
    ("LG Corporation", T("Corporate spin-off.", "Scission d'activité.", "기업 분할")),
]

# ---- International projects, investments & partnerships ----
PROJECTS = [
    ("KEPCO E&C", T("French business expansion and the ITER project.", "Développement en France et projet ITER.", "프랑스 사업 확장 및 ITER 프로젝트")),
    ("KEPCO", T("Potential power, natural resources and infrastructure projects in Europe, Africa and Asia.", "Projets potentiels d'énergie, de ressources naturelles et d'infrastructure en Europe, en Afrique et en Asie.", "유럽·아프리카·아시아 전력, 천연자원, 인프라 사업 검토")),
    ("Samsung C&T", T("€120 million EPC solar power project in Provence.", "Projet solaire EPC de 120 millions d'euros en Provence.", "프로방스 1억 2천만 유로 규모 태양광 EPC 프로젝트")),
    ("Samsung SDI / EDF", T("Battery supply system for power stations in French overseas territories.", "Système de stockage par batteries pour des centrales des territoires d'outre-mer.", "프랑스 해외 영토 발전소용 배터리 공급 시스템")),
    ("POSCO E&C", T("Phosphate handling system construction project in Morocco.", "Projet de construction d'un système de manutention de phosphates au Maroc.", "모로코 인광석 처리 시스템 건설 프로젝트")),
    ("Korea Aerospace Industries (KAI)", T("International sale of supersonic trainers, financial structuring and related tax matters.", "Vente internationale d'avions d'entraînement supersoniques, structuration financière et fiscalité associée.", "초음속 훈련기 해외 판매, 금융 구조 설계 및 관련 조세")),
    ("Korean Air", T("Business structuring in Europe and the Middle East.", "Structuration des activités en Europe et au Moyen-Orient.", "유럽·중동 사업 구조 설계")),
    ("LG Chem", T("Investment in French electric battery projects and partnership with Renault.", "Investissement dans des projets français de batteries électriques et partenariat avec Renault.", "프랑스 배터리 프로젝트 투자 및 르노와의 파트너십")),
    ("Korean Government", T("Korean House project at the Cité Internationale Universitaire de Paris.", "Projet de Maison de la Corée à la Cité internationale universitaire de Paris.", "파리 국제대학촌 한국관 건립 프로젝트")),
    ("TUOK Group (Hong Kong)", T("Renovation and opening of the Shangri-La Paris.", "Rénovation et ouverture du Shangri-La Paris.", "샹그릴라 파리 호텔 리노베이션 및 개관")),
    ("Systra SA", T("Refinancing negotiations for the Uijeongbu light rail project.", "Négociations de refinancement du projet de métro léger d'Uijeongbu.", "의정부 경전철 프로젝트 리파이낸싱 협상")),
    ("Hanmi Pharma Group", T("Partnership negotiations for the Chinese market.", "Négociation de partenariats pour le marché chinois.", "중국 시장 파트너십 협상")),
    ("Hynix Germany", T("French business development.", "Développement commercial en France.", "프랑스 사업 개발")),
    ("Kumho Tire France", T("Business expansion in France, Italy and Spain.", "Développement en France, en Italie et en Espagne.", "프랑스, 이탈리아, 스페인 사업 확장")),
    ("Nexen Tire", T("Business development and establishment in France.", "Développement et implantation en France.", "프랑스 사업 개발 및 법인 설립")),
    ("Pantos", T("Business expansion in France and Spain.", "Développement en France et en Espagne.", "프랑스·스페인 사업 확장")),
    ("Samsung Techwin UK", T("Security camera production and installation project in Algeria.", "Projet de production et d'installation de caméras de sécurité en Algérie.", "알제리 보안 카메라 생산·설치 프로젝트")),
    ("Korean Investors Consortium", T("Financial structuring and acquisition of diamond mining rights in Guinea.", "Structuration financière et acquisition de droits miniers de diamants en Guinée.", "기니 다이아몬드 광산 채굴권 인수 및 금융 구조 설계")),
    ("Korean Investor", T("Luxury villa development in Nice and Monaco.", "Promotion de villas de luxe à Nice et Monaco.", "니스·모나코 고급 빌라 개발")),
    ("Korean Investor", T("Real estate acquisition in Île-de-France for a transnational law and business university.", "Acquisition immobilière en Île-de-France pour une université internationale de droit et de commerce.", "국제 법·경영 대학 설립을 위한 일드프랑스 부동산 인수")),
]

# ---- Disputes and arbitration: selected cases ----
CASES = [
    ("Korean Company S", T("ICC international arbitration against a French defence group concerning next-generation submarines.", "Arbitrage international CCI contre un groupe français de défense au sujet de sous-marins de nouvelle génération.", "차세대 잠수함 관련 프랑스 방산 그룹 상대 ICC 국제중재")),
    ("Korean Company D", T("Consolidated ICC international arbitrations in Paris against a French defence and aerospace group concerning military satellite supply.", "Arbitrages internationaux CCI consolidés à Paris contre un groupe français de défense et d'aérospatiale au sujet de fournitures de satellites militaires.", "군사위성 공급 관련 프랑스 방산·항공우주 그룹 상대 파리 ICC 병합 국제중재")),
    ("The People of Korea", T("Litigation against the French Government concerning the restitution of the 19th-century Korean Royal Archives (Oegyujanggak).", "Contentieux contre l'État français pour la restitution des archives royales coréennes du XIXᵉ siècle (Oegyujanggak).", "19세기 조선 왕실 의궤(외규장각) 반환을 위한 프랑스 정부 상대 소송")),
    ("Company K", T("Arbitrations against Italian subcontractors concerning construction projects in the Middle East and Australia (ICC, LCIA and Milan-seated).", "Arbitrages contre des sous-traitants italiens au sujet de chantiers au Moyen-Orient et en Australie (CCI, LCIA et siège à Milan).", "중동·호주 건설 프로젝트 관련 이탈리아 하도급사 상대 중재(ICC, LCIA, 밀라노)")),
    ("Daelim Industrial", T("KCAB international arbitration against a French subcontractor concerning a Singapore underground railway project.", "Arbitrage international KCAB contre un sous-traitant français au sujet d'un projet de métro à Singapour.", "싱가포르 지하철 프로젝트 관련 프랑스 하도급사 상대 대한상사중재원 국제중재")),
    ("Daelim Industrial", T("Litigation concerning a guarantee bond issued by CIC Bank in France for a Saudi Arabian project.", "Contentieux relatif à une garantie émise par la banque CIC pour un projet en Arabie saoudite.", "사우디 프로젝트 관련 CIC 은행 발행 보증 이행 소송")),
    ("Daelim Industrial", T("Korean commercial arbitration and settlement negotiations concerning a Saudi Arabian project.", "Arbitrage commercial coréen et négociations transactionnelles au sujet d'un projet en Arabie saoudite.", "사우디 프로젝트 관련 상사중재 및 화해 협상")),
    ("Daelim Industrial", T("Claims against a French supplier in insolvency proceedings.", "Créances contre un fournisseur français en procédure collective.", "도산 절차 중인 프랑스 공급사 상대 채권 청구")),
    ("Dongbu Group", T("Multi-level litigation against Alcatel concerning defective mobile phone baseband chips; claim valued at approximately US$100 million.", "Contentieux à plusieurs degrés contre Alcatel au sujet de puces de bande de base défectueuses ; demande évaluée à environ 100 millions de dollars.", "휴대폰 베이스밴드 칩 하자 관련 알카텔 상대 다단계 소송(청구액 약 1억 달러)")),
    ("Dongbu Hitek", T("AAA international arbitration in the United States and settlement negotiations.", "Arbitrage international AAA aux États-Unis et négociations transactionnelles.", "미국 AAA 국제중재 및 화해 협상")),
    ("POSCO E&C", T("Multiple disputes and claims arising from a phosphate handling system project in Jorf Lasfar, Morocco.", "Litiges et réclamations multiples nés d'un projet de manutention de phosphates à Jorf Lasfar (Maroc).", "모로코 조르프 라스파르 인광석 처리 시스템 프로젝트 관련 다수 분쟁 및 클레임")),
    ("Korean Ministry of National Defense & Navy", T("Dispute against a French bank and contractor concerning military equipment for the Korean Navy.", "Litige contre une banque et un fournisseur français au sujet d'équipements militaires pour la marine coréenne.", "한국 해군 군사 장비 관련 프랑스 은행 및 계약업체 상대 분쟁")),
    ("Group G (Germany)", T("Singapore-seated international arbitration against a Korean company.", "Arbitrage international avec siège à Singapour contre une société coréenne.", "한국 기업 상대 싱가포르 국제중재")),
    ("Indako (Indonesia)", T("Commercial dispute and KCAB arbitration concerning a resort construction project in Indonesia.", "Litige commercial et arbitrage KCAB au sujet d'un projet de construction de complexe hôtelier en Indonésie.", "인도네시아 리조트 건설 프로젝트 관련 상사 분쟁 및 대한상사중재원 중재")),
    ("Sangji Construction", T("Multiple litigations relating to a construction project in Nice and Monaco.", "Contentieux multiples relatifs à un projet immobilier à Nice et Monaco.", "니스·모나코 건설 프로젝트 관련 다수 소송")),
    ("Samsung Electronics", T("Mobile phone design infringement litigation in France.", "Contentieux en contrefaçon de dessins de téléphones mobiles en France.", "휴대폰 디자인 침해 프랑스 소송")),
    ("Dongbu Fire Insurance", T("Product liability litigation in France and the United Kingdom.", "Contentieux de responsabilité du fait des produits en France et au Royaume-Uni.", "프랑스·영국 제조물 책임 소송")),
    ("Meritz Insurance", T("Product liability litigation in France and the United Kingdom.", "Contentieux de responsabilité du fait des produits en France et au Royaume-Uni.", "프랑스·영국 제조물 책임 소송")),
    ("Vatech", T("Contractual, tort and competition litigation with French distributors and business partners.", "Contentieux contractuel, délictuel et de concurrence avec des distributeurs et partenaires français.", "프랑스 유통사 및 사업 파트너와의 계약·불법행위·경쟁법 소송")),
    ("Hyosung Corp.", T("French litigation concerning contractual liability.", "Contentieux en France relatif à une responsabilité contractuelle.", "계약 책임 관련 프랑스 소송")),
    ("HJC Helmet", T("Business-related disputes in France.", "Litiges commerciaux en France.", "프랑스 내 사업 관련 분쟁")),
    ("Seoul National Opera", T("Litigation against French service providers.", "Contentieux contre des prestataires français.", "프랑스 용역 업체 상대 소송")),
    ("Atelier Choux", T("Unauthorised commercial resale and IP infringement.", "Revente commerciale non autorisée et contrefaçon.", "무단 상업적 재판매 및 지식재산권 침해")),
]

# ---- Employment ----
RESTRUCTURING = [
    ("LG Electronics France", T("Downsizing and collective redundancy proceedings, including works council consultation.", "Réduction d'effectifs et licenciement économique collectif, avec consultation du CSE.", "인력 감축 및 집단 해고 절차, 직원대표위원회 협의 포함")),
    ("LG Mobile R&D France", T("Closure and economic redundancy plan, including works council consultation.", "Fermeture et plan de licenciement économique, avec consultation du CSE.", "폐쇄 및 경영상 해고 계획, 직원대표위원회 협의 포함")),
    ("Samsung C&T France", T("Collective redundancy, business transfer and related employment matters.", "Licenciement collectif, transfert d'activité et questions sociales liées.", "집단 해고, 사업 이전 및 관련 노동 사안")),
    ("Samsung CP Inox France", T("Factory closure, collective redundancy and settlement negotiations.", "Fermeture d'usine, licenciement collectif et négociations transactionnelles.", "공장 폐쇄, 집단 해고 및 합의 협상")),
    ("Samsung Electro-Mechanics France", T("Collective redundancy proceedings.", "Procédure de licenciement collectif.", "집단 해고 절차")),
    ("Samsung Electronics France", T("Restructuring and employment law matters.", "Restructuration et droit du travail.", "구조조정 및 노동법 사안")),
    ("Samsung Techwin France", T("Employment transfer and labour law matters arising from the acquisition of a digital camera business.", "Transfert des contrats de travail et droit du travail liés à la reprise d'une activité d'appareils photo numériques.", "디지털카메라 사업 인수에 따른 고용 승계 및 노동법 사안")),
    ("Samsung Otelinox Romania", T("Employment matters arising from the acquisition of a French distribution network.", "Questions sociales liées à l'acquisition d'un réseau de distribution français.", "프랑스 유통망 인수에 따른 노동 사안")),
    ("Korean Air France", T("Reorganisation, restructuring, redundancies and settlement negotiations.", "Réorganisation, restructuration, licenciements et négociations transactionnelles.", "조직 개편, 구조조정, 해고 및 합의 협상")),
    ("Naver Labs Europe", T("Restructuring and employment law matters.", "Restructuration et droit du travail.", "구조조정 및 노동법 사안")),
    ("Louis Quatorze France", T("Restructuring and employment matters.", "Restructuration et questions sociales.", "구조조정 및 노동 사안")),
]
EMP_LITIGATION = ["Osstem Implant", "Celltrion Healthcare", "CJ Europe", "Hopae France", "Kumho Tire France", "POSCO International GmbH", "Samsung Electro-Mechanics Germany", "SK Hynix Germany", "SK Siltron", "YG-1 Europe"]
EMP_ADVISORY = ["Korean Air", "Asiana Airlines", "T'way Air (Trinity)", "Naver France", "CLO Virtual Fashion", "Hyosung TNC", "Hyundai Motor France", "IICOMBINED Europe (Gentle Monster)", "Innocean Worldwide France (Hyundai Motor Group)", "Songzio Paris", "Yonwoo"]
EMP_CONTRACTS = ["CLO Virtual Fashion", "Hyosung TNC", "IICOMBINED Europe", "Kumho Tire France", "Nexen Tire"]

# ---- Professional immigration ----
IMMIGRATION_SERVICES = [
    (T("Visas and work permits", "Visas et autorisations de travail", "비자 및 노동허가"), T("Visa, residence permit and work authorisation applications.", "Demandes de visa, de titre de séjour et d'autorisation de travail.", "비자, 체류증, 노동허가 신청")),
    (T("International mobility", "Mobilité internationale", "국제 인력 이동"), T("Cross-border mobility of employees, executives and professionals.", "Mobilité internationale des salariés, dirigeants et professionnels.", "임직원 및 전문 인력의 국경 간 이동")),
    (T("Intra-group transfers", "Mobilités intragroupe", "그룹 내 전보"), T("International assignments and intra-group mobility arrangements.", "Missions internationales et mobilités intragroupe.", "해외 파견 및 그룹 내 이동")),
    (T("Secondment and staff assignment", "Détachement et mise à disposition", "파견 및 인력 배치"), T("Secondment and cross-border employment arrangements.", "Détachements et montages d'emploi transfrontalier.", "파견 및 국경 간 고용 구조")),
    (T("Posted workers", "Travailleurs détachés", "파견 근로자"), T("Posting of employees to France for projects, contracts and assignments.", "Détachement de salariés en France pour des projets, contrats et missions.", "프로젝트·계약 수행을 위한 프랑스 파견")),
    (T("Executive and professional mobility", "Mobilité des dirigeants et professionnels", "경영진·전문 인력 이동"), T("Immigration and employment aspects of relocation to France.", "Aspects immigration et droit du travail de l'installation en France.", "프랑스 부임에 따른 이민 및 고용 측면")),
    (T("Immigration compliance", "Conformité en immigration", "이민 컴플라이언스"), T("Ongoing immigration and employment compliance for foreign employees.", "Conformité continue en immigration et droit du travail pour les salariés étrangers.", "외국인 임직원의 이민·고용 컴플라이언스 상시 관리")),
]
IMMIGRATION_CLIENTS = ["Celltrion Healthcare", "CJ Europe", "Asiana Airlines", "Biogenics", "Booyoung Corp.", "KBS", "SBS", "MBC", "Dasan Networks", "Vatech & Dentalvia", "DHC (Japan)", "Dorco France", "GIBA", "Hyosung TNC", "IICOMBINED Europe", "Iljin Bearing", "Innocean Worldwide (Hyundai Motor Group)", "King Sejong Institute Foundation", "Korea Agro-Fisheries & Food Trade Corporation", "Korea Creative Content Agency", "Korea Water Resources Corporation", "LG Fashion", "Logos Biosystems", "Naver France", "Nonghyup", "Olivia K Global Partners", "Sena Technologies", "Seoul Semiconductor", "Shinhan Diamond", "Solid Homme / Wooyoungmi", "Songzio Paris", "Suhyup", "Suprema Europe", "Wooshin Systems", "YG-1 Europe", "Yonwoo"]


def _rows(rows, lang):
    return [(n, d[lang]) for n, d in rows]


def _take(rows, names_texts):
    """Split rows: (picked, rest) where picked match (name, english text prefix)."""
    picked, rest = [], []
    for r in rows:
        (picked if any(r[0] == n and r[1]["en"].startswith(t) for n, t in names_texts) else rest).append(r)
    return picked, rest


# Re-file matters under the eight practice areas of the Services page.
_INSOLV_DEALS, _DEALS = _take(TRANSACTIONS, [("SG", "Acquisition of L Foundry"), ("Korean Company J", "Tender"), ("Korean Consortium", "Investment in a French EV")])
_IP_DEALS, _DEALS = _take(_DEALS, [("Hanall Pharma", "Acquisition of patents")])
_COMM_DEALS, _DEALS = _take(_DEALS, [("Samsung C&T", "Partnership with PSA")])
_COMM_PROJ, _PROJ = _take(PROJECTS, [("Hanmi Pharma Group", "Partnership"), ("LG Chem", "Investment in French electric battery")])
_INSOLV_CASES, _CASES = _take(CASES, [("Daelim Industrial", "Claims against a French supplier in insolvency")])
_IP_CASES, _CASES = _take(_CASES, [("Samsung Electronics", "Mobile phone design"), ("Atelier Choux", "Unauthorised")])
_COMM_CASES, _CASES = _take(_CASES, [("Vatech", "Contractual"), ("Hyosung Corp.", "French litigation"), ("HJC Helmet", "Business-related"), ("Seoul National Opera", "Litigation against French service")])

L = {
    "entry": T("Companies and institutions supported in setting up and operating in France", "Entreprises et institutions accompagnées dans leur implantation et leurs activités en France", "프랑스 진출 및 운영을 지원한 기업·기관"),
    "deals": T("Selected transactions", "Opérations choisies", "주요 거래"),
    "proj": T("Selected projects", "Projets choisis", "주요 프로젝트"),
    "cases": T("Selected cases", "Dossiers choisis", "주요 사례"),
    "partners": T("Partnerships", "Partenariats", "파트너십"),
    "cdisp": T("Commercial disputes", "Litiges commerciaux", "상사 분쟁"),
    "emp_r": T("Restructuring, reorganisation and redundancy", "Restructurations, réorganisations et licenciements", "구조조정·조직 개편·해고"),
    "emp_l": T("Employment litigation", "Contentieux du travail", "노동 소송"),
    "emp_a": T("Employment advisory (day-to-day HR)", "Conseil en droit du travail (gestion RH courante)", "노무 자문(일상 인사 업무)"),
    "emp_c": T("Employment contracts and labour relations", "Contrats de travail et relations sociales", "근로계약 및 노사 관계"),
    "imm_c": T("Professional immigration: clients supported", "Immigration professionnelle : clients accompagnés", "취업 이민 지원 고객"),
    "ins": T("Insolvency-related matters", "Dossiers liés aux procédures collectives", "도산 관련 사안"),
    "ip": T("IP and technology matters", "Dossiers de propriété intellectuelle et de technologie", "지식재산권·기술 사안"),
}


def examples(lang):
    """Key examples per practice area id (content_services.SERVICES8). Blocks: ("cats"|"rows"|"names", subtitle, data)."""
    g = lambda k: L[k][lang]
    return {
        "corporate": [("cats", g("entry"), [(c[lang], names) for c, names in ENTRY])],
        "ma": [("rows", g("deals"), _rows(_DEALS, lang))],
        "commercial": [("rows", g("partners"), _rows(_COMM_DEALS + _COMM_PROJ, lang)), ("rows", g("cdisp"), _rows(_COMM_CASES, lang))],
        "employment": [("rows", g("emp_r"), _rows(RESTRUCTURING, lang)), ("names", g("emp_l"), EMP_LITIGATION),
                       ("names", g("emp_a"), EMP_ADVISORY), ("names", g("emp_c"), EMP_CONTRACTS),
                       ("names", g("imm_c"), IMMIGRATION_CLIENTS)],
        "litigation": [("rows", g("cases"), _rows(_CASES, lang))],
        "insolvency": [("rows", g("ins"), _rows(_INSOLV_CASES + _INSOLV_DEALS, lang))],
        "ip": [("rows", g("ip"), _rows(_IP_CASES + _IP_DEALS, lang))],
        "advice": [("rows", g("proj"), _rows(_PROJ, lang))],
    }


def figures(lang):
    """Indicative figures counted from the lists above (rounded down to the nearest 5, shown with '+')."""
    def plus(n):
        return f"{(n // 5) * 5}+" if n >= 10 else str(n)
    entry = len({n for _, names in ENTRY for n in names})
    deals = len(TRANSACTIONS) + len(PROJECTS)
    cases = len(CASES)
    emp = len({n for n, _ in RESTRUCTURING} | set(EMP_LITIGATION) | set(EMP_ADVISORY) | set(EMP_CONTRACTS))
    imm = len(set(IMMIGRATION_CLIENTS))
    labels = {
        "en": ["years of practice", "companies and institutions supported in France", "transactions and international projects", "disputes and arbitrations", "employers advised on employment law", "clients supported on immigration"],
        "fr": ["ans d'exercice", "entreprises et institutions accompagnées en France", "opérations et projets internationaux", "litiges et arbitrages", "employeurs conseillés en droit du travail", "clients accompagnés en immigration"],
        "ko": ["년 이상의 경력", "프랑스 진출 지원 기업·기관", "거래 및 국제 프로젝트", "분쟁·중재 사건", "노동 자문 고객", "취업 이민 지원 고객"],
    }[lang]
    vals = ["25+", plus(entry), plus(deals), plus(cases), plus(emp), plus(imm)]
    return list(zip(vals, labels)), {"entry": entry, "deals": deals, "cases": cases, "emp": emp, "imm": imm}


def featured(lang):
    """Six highlights for the home page: (practice area id, text)."""
    ex = examples(lang)
    first = lambda sid, k=0: "{}: {}".format(*[b for b in ex[sid] if b[0] == "rows"][0][2][k])
    return [("ma", first("ma")), ("advice", first("advice")), ("litigation", first("litigation")),
            ("litigation", first("litigation", 1)), ("employment", first("employment")), ("ma", first("ma", 2))]
