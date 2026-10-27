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

# Eight practice areas supplied by the firm (EN original; FR/KO translated, to be reviewed).
SERVICES8 = {
"en": [
 ("corporate", "Corporate & Business", "General corporate", [
   ("Corporate Structuring & Incorporation", "Companies, branches and representative offices"),
   ("Corporate Management", "Articles of association, bylaws, shareholders' agreements and corporate resolutions"),
   ("Corporate Secretarial & Formalities", "Capital increases, corporate changes, filings and registrations"),
   ("Data Protection & Privacy", "GDPR and data protection compliance"),
   ("Corporate Governance & Compliance", "Governance, directors' duties and regulatory compliance"),
   ("Business Transfers & Restructuring", "Reorganisations, restructurings and related transactions")]),
 ("ma", "Corporate M&A", "Mergers & acquisitions", [
   ("M&A Structuring & Transaction Planning", "Acquisitions, disposals, mergers and strategic transactions"),
   ("Exit Strategies", "Trade sales, secondary transactions, public offers and IPO-related strategies"),
   ("Transaction Documentation", "SPA, APA, merger, investment and shareholders' agreements"),
   ("Takeover Bids & Tender Offers", "Legal assistance and transaction support"),
   ("Regulatory & Corporate Filings", "Corporate and regulatory filings with competent authorities"),
   ("Legal Due Diligence", "Corporate, commercial, employment, regulatory, IP and data protection")]),
 ("commercial", "Commercial", "Commercial contracts", [
   ("Contract Drafting & Negotiation", "Drafting, review, negotiation and amendment of commercial agreements"),
   ("Contract Risk Analysis", "Legal risk assessment and contractual risk mitigation"),
   ("Distribution & Sales", "Distribution, agency and sales agreements"),
   ("Subcontracting & Outsourcing", "Subcontracting, outsourcing and service agreements"),
   ("Independent Contractors & Service Providers", "Consultant and external service provider arrangements"),
   ("Partnerships & Joint Ventures", "Structuring and contractual arrangements"),
   ("Lease & Licensing", "Commercial leases, licences and related agreements"),
   ("Procurement & Supply", "Procurement, purchasing, supply and framework agreements"),
   ("Data Transfer & Processing", "Data transfers, data-sharing and GDPR compliance"),
   ("Commercial Disputes", "Contractual breaches, termination and enforcement")]),
 ("employment", "Employment", "Employment & social security", [
   ("Employment Contracts & Policies", "Contracts, internal policies, company agreements and HR documentation"),
   ("Employment Advisory & Compliance", "Day-to-day HR, working time, discipline, health & safety and employer obligations"),
   ("Termination & Settlement", "Dismissals, negotiated departures, resignations and settlement agreements"),
   ("Collective Labour Relations", "Works council consultation, employee representatives and collective bargaining"),
   ("Restructuring & Redundancies", "Reorganisations, closures, downsizing and collective redundancy plans"),
   ("Employment Transfers & Mobility", "Business transfers, employee transfers, secondments and posted workers"),
   ("Employment Litigation", "Labour disputes before the Conseil de prud'hommes and competent courts"),
   ("International Employment & Social Security", "Cross-border employment, mobility and social security matters"),
   ("Professional Immigration", "Visas, work permits and residence permits for executives, assignees and new hires"),
   ("Employment Compliance", "")]),
 ("litigation", "Dispute Resolution", "Litigation & arbitration", [
   ("Dispute Prevention & Risk Management", "Dispute avoidance and litigation risk assessment"),
   ("Provisional & Protective Measures", "Asset freezing, attachments, judicial mortgages and other protective measures"),
   ("Dispute Resolution Clauses", "Jurisdiction, governing law, mediation and arbitration clauses"),
   ("Settlement & Negotiation", "Settlement negotiations, mediation and alternative dispute resolution"),
   ("Litigation", "Civil, commercial, administrative and employment disputes"),
   ("Arbitration", "Domestic and international arbitration, institutional and ad hoc"),
   ("Debt Recovery", "Formal notices, seizures and summary proceedings"),
   ("Product Liability & Industrial Risk", "Defective products, warranty claims and insurer-appointed defence")]),
 ("insolvency", "Insolvency & Restructuring", "Insolvency & restructuring", [
   ("Insolvency & Restructuring Advisory", "Creditor negotiations, restructuring, safeguard and liquidation proceedings"),
   ("Insolvency Proceedings", "Advice to companies and directors throughout insolvency proceedings"),
   ("Insolvency Litigation", "Disputes involving directors, creditors and other stakeholders"),
   ("Creditor Claims", "Declaration, verification and recovery of claims")]),
 ("ip", "IP / Technology", "IP licensing & technology transfer", [
   ("IP Disputes", "Infringement, ownership and contractual disputes"),
   ("Copyright, Trademarks & Designs", "Protection and exploitation of IP rights and branding"),
   ("IP Licensing", "Drafting and negotiation of licence agreements"),
   ("Technology Transfer", "Technology, know-how transfer and commercialisation"),
   ("IP Commercialisation", "Licensing, exploitation and strategic use of IP and technology"),
   ("Supply & Distribution", "Agreements involving IP and technology rights"),
   ("IP Ownership & Rights Allocation", "Ownership, assignment and licensing of IP rights"),
   ("Brand Protection", "Trademarks, trade names, designs and other brand assets"),
   ("Confidentiality & Know-How", "Trade secrets, know-how protection and contractual safeguards")]),
 ("advice", "International Projects, Investments & Partnerships", "Foreign investment & international projects", [
   ("International Projects & Project Finance", "Cross-border projects, project finance and overseas investments"),
   ("Partnerships & Joint Ventures", "Structuring and contractual arrangements"),
   ("Regulatory Compliance", "Legal and regulatory requirements for foreign investments"),
   ("Investment Structuring & Implementation", "Structuring and execution of domestic and cross-border investments"),
   ("Investment Exit Strategies", "Disposals, transfers and other divestment strategies"),
   ("Offering & Investment Documentation", "Fundraising, investment and offering documentation")]),
],
"fr": [
 ("corporate", "Droit des sociétés et des affaires", "Droit des sociétés", [
   ("Structuration et création de sociétés", "Sociétés, succursales et bureaux de représentation"),
   ("Gestion des sociétés", "Statuts, règlements intérieurs, pactes d'associés et décisions sociales"),
   ("Secrétariat juridique et formalités", "Augmentations de capital, modifications statutaires, dépôts et immatriculations"),
   ("Protection des données", "Conformité au RGPD et à la protection des données"),
   ("Gouvernance et conformité", "Gouvernance, responsabilité des dirigeants et conformité réglementaire"),
   ("Cessions et restructurations", "Réorganisations, restructurations et opérations liées")]),
 ("ma", "Fusions-acquisitions", "Fusions et acquisitions", [
   ("Structuration des opérations", "Acquisitions, cessions, fusions et opérations stratégiques"),
   ("Stratégies de sortie", "Cessions industrielles, opérations secondaires, offres au public et introduction en bourse"),
   ("Documentation de l'opération", "Contrats de cession d'actions ou d'actifs, traités de fusion, accords d'investissement et pactes d'associés"),
   ("Offres publiques", "Assistance juridique et accompagnement de l'opération"),
   ("Formalités réglementaires et sociales", "Déclarations et dépôts auprès des autorités compétentes"),
   ("Audit juridique", "Droit des sociétés, contrats, social, réglementaire, propriété intellectuelle et données personnelles")]),
 ("commercial", "Droit commercial", "Contrats commerciaux", [
   ("Rédaction et négociation", "Rédaction, revue, négociation et avenants des contrats commerciaux"),
   ("Analyse des risques contractuels", "Évaluation et maîtrise des risques juridiques et contractuels"),
   ("Distribution et vente", "Contrats de distribution, d'agence commerciale et de vente"),
   ("Sous-traitance et externalisation", "Contrats de sous-traitance, d'externalisation et de prestation de services"),
   ("Consultants et prestataires indépendants", "Contrats avec consultants et prestataires externes"),
   ("Partenariats et joint-ventures", "Structuration et montages contractuels"),
   ("Baux et licences", "Baux commerciaux, licences et contrats associés"),
   ("Achats et approvisionnement", "Contrats d'achat, d'approvisionnement et accords-cadres"),
   ("Transferts et traitement de données", "Transferts de données, partage de données et conformité au RGPD"),
   ("Litiges commerciaux", "Inexécution, résiliation et exécution forcée des contrats")]),
 ("employment", "Droit du travail", "Droit du travail et de la sécurité sociale", [
   ("Contrats et politiques RH", "Contrats de travail, règlements intérieurs, accords d'entreprise et documentation RH"),
   ("Conseil et conformité", "Gestion RH courante, temps de travail, discipline, santé-sécurité et obligations de l'employeur"),
   ("Rupture et transaction", "Licenciements, ruptures conventionnelles, démissions et transactions"),
   ("Relations collectives", "Consultation du CSE, représentants du personnel et négociation collective"),
   ("Restructurations et licenciements économiques", "Réorganisations, fermetures, réductions d'effectifs et plans de sauvegarde de l'emploi"),
   ("Transferts et mobilité", "Transferts d'entreprise et de salariés, détachements et travailleurs détachés"),
   ("Contentieux du travail", "Litiges devant le conseil de prud'hommes et les juridictions compétentes"),
   ("Emploi international et sécurité sociale", "Emploi transfrontalier, mobilité et sécurité sociale"),
   ("Immigration professionnelle", "Visas, autorisations de travail et titres de séjour pour dirigeants, salariés détachés et recrues"),
   ("Conformité sociale", "")]),
 ("litigation", "Règlement des litiges", "Contentieux et arbitrage", [
   ("Prévention des litiges", "Prévention des différends et évaluation du risque contentieux"),
   ("Mesures conservatoires", "Saisies conservatoires, hypothèques judiciaires et autres mesures conservatoires"),
   ("Clauses de règlement des litiges", "Clauses attributives de juridiction, de loi applicable, de médiation et d'arbitrage"),
   ("Transaction et négociation", "Négociations transactionnelles, médiation et modes alternatifs de règlement"),
   ("Contentieux", "Litiges civils, commerciaux, administratifs et prud'homaux"),
   ("Arbitrage", "Arbitrage interne et international, institutionnel et ad hoc"),
   ("Recouvrement de créances", "Mises en demeure, saisies et procédures en référé"),
   ("Responsabilité du fait des produits et risque industriel", "Produits défectueux, garanties et défense à la demande des assureurs")]),
 ("insolvency", "Procédures collectives et restructuration", "Entreprises en difficulté", [
   ("Conseil en restructuration", "Négociation avec les créanciers, restructuration, sauvegarde et liquidation"),
   ("Procédures collectives", "Accompagnement des sociétés et des dirigeants tout au long de la procédure"),
   ("Contentieux des procédures collectives", "Litiges impliquant dirigeants, créanciers et autres parties prenantes"),
   ("Créances", "Déclaration, vérification et recouvrement des créances")]),
 ("ip", "Propriété intellectuelle et technologies", "Licences et transfert de technologie", [
   ("Contentieux de la propriété intellectuelle", "Contrefaçon, titularité et litiges contractuels"),
   ("Droit d'auteur, marques, dessins et modèles", "Protection et exploitation des droits et de l'image de marque"),
   ("Licences", "Rédaction et négociation des contrats de licence"),
   ("Transfert de technologie", "Transfert de technologie et de savoir-faire, valorisation"),
   ("Valorisation de la propriété intellectuelle", "Concession, exploitation et usage stratégique des droits et technologies"),
   ("Approvisionnement et distribution", "Contrats portant sur des droits de propriété intellectuelle et des technologies"),
   ("Titularité et répartition des droits", "Titularité, cession et concession des droits"),
   ("Protection de la marque", "Marques, noms commerciaux, dessins et modèles et autres actifs de marque"),
   ("Confidentialité et savoir-faire", "Secret des affaires, protection du savoir-faire et garanties contractuelles")]),
 ("advice", "Projets internationaux, investissements et partenariats", "Investissement étranger et projets internationaux", [
   ("Projets internationaux et financement de projets", "Projets transfrontaliers, financement de projets et investissements à l'étranger"),
   ("Partenariats et joint-ventures", "Structuration et montages contractuels"),
   ("Conformité réglementaire", "Exigences légales et réglementaires applicables aux investissements étrangers"),
   ("Structuration et mise en œuvre des investissements", "Structuration et réalisation d'investissements nationaux et transfrontaliers"),
   ("Stratégies de sortie", "Cessions, transferts et autres stratégies de désinvestissement"),
   ("Documentation d'investissement", "Levée de fonds, documentation d'investissement et d'offre")]),
],
"ko": [
 ("corporate", "회사법·기업 자문", "일반 기업법무", [
   ("법인 설립 및 구조 설계", "법인, 지점, 연락사무소 설립"),
   ("회사 운영", "정관, 내부 규정, 주주간 계약, 이사회·주주총회 결의"),
   ("법인 서무 및 등기", "증자, 변경 등기, 각종 신고 및 등록"),
   ("개인정보 보호", "GDPR 및 개인정보 보호 컴플라이언스"),
   ("지배구조 및 컴플라이언스", "지배구조, 이사의 의무, 규제 준수"),
   ("사업 양수도 및 구조조정", "조직 개편, 구조조정 및 관련 거래")]),
 ("ma", "인수합병(M&A)", "인수합병", [
   ("M&A 구조 설계 및 거래 기획", "인수, 매각, 합병 및 전략적 거래"),
   ("엑시트 전략", "전략적 매각, 구주 거래, 공모 및 상장 관련 전략"),
   ("거래 문서", "주식·자산 양수도 계약, 합병 계약, 투자 계약, 주주간 계약"),
   ("공개매수", "법률 지원 및 거래 실무 지원"),
   ("규제 및 회사 관련 신고", "관할 당국에 대한 회사·규제 신고"),
   ("법률 실사", "회사법, 상거래, 노동, 규제, 지식재산권, 개인정보 보호")]),
 ("commercial", "상거래", "상업 계약", [
   ("계약서 작성 및 협상", "상업 계약의 작성, 검토, 협상 및 변경"),
   ("계약 리스크 분석", "법적 리스크 평가 및 계약상 리스크 관리"),
   ("유통 및 판매", "유통, 대리점, 판매 계약"),
   ("하도급 및 아웃소싱", "하도급, 아웃소싱, 용역 계약"),
   ("독립 계약자 및 용역 제공자", "컨설턴트 및 외부 용역 제공자 계약"),
   ("파트너십 및 합작투자", "구조 설계 및 계약 체계"),
   ("임대차 및 라이선스", "상가 임대차, 라이선스 및 관련 계약"),
   ("조달 및 공급", "조달, 구매, 공급 및 기본 계약"),
   ("데이터 이전 및 처리", "데이터 이전, 데이터 공유, GDPR 준수"),
   ("상사 분쟁", "계약 위반, 해지 및 강제 이행")]),
 ("employment", "노동", "노동 및 사회보장", [
   ("근로계약 및 사내 규정", "근로계약, 내부 규정, 사내 협약, 인사 문서"),
   ("노무 자문 및 컴플라이언스", "일상 인사관리, 근로시간, 징계, 산업안전보건, 사용자 의무"),
   ("근로관계 종료 및 합의", "해고, 합의 퇴직, 사직 및 합의서"),
   ("집단적 노사관계", "직원대표위원회(CSE) 협의, 근로자 대표, 단체교섭"),
   ("구조조정 및 경영상 해고", "조직 개편, 폐쇄, 인력 감축, 집단 해고 계획"),
   ("고용 승계 및 인력 이동", "사업 이전, 고용 승계, 파견 및 해외 파견 근로자"),
   ("노동 소송", "노동법원(Conseil de prud'hommes) 및 관할 법원 소송"),
   ("국제 고용 및 사회보장", "국경 간 고용, 인력 이동, 사회보장"),
   ("취업 이민", "경영진, 주재원, 신규 채용 인력의 비자, 노동허가, 체류증"),
   ("노동법 컴플라이언스", "")]),
 ("litigation", "분쟁 해결", "소송 및 중재", [
   ("분쟁 예방 및 리스크 관리", "분쟁 회피 및 소송 리스크 평가"),
   ("보전 처분", "자산 동결, 가압류, 가처분, 법원 저당권 등 보전 조치"),
   ("분쟁 해결 조항", "관할, 준거법, 조정 및 중재 조항"),
   ("화해 및 협상", "화해 협상, 조정 및 대체적 분쟁 해결"),
   ("소송", "민사, 상사, 행정, 노동 분쟁"),
   ("중재", "국내 및 국제 중재, 기관 중재 및 임시 중재"),
   ("채권 회수", "최고, 압류, 약식 절차"),
   ("제조물 책임 및 산업 리스크", "결함 제품, 하자 담보 청구, 보험사 지정 방어")]),
 ("insolvency", "도산 및 구조조정", "도산 및 구조조정", [
   ("도산·구조조정 자문", "채권자 협상, 구조조정, 회생(sauvegarde) 및 청산 절차"),
   ("도산 절차", "도산 절차 전반에 걸친 회사 및 경영진 자문"),
   ("도산 관련 소송", "경영진, 채권자 및 기타 이해관계자 관련 분쟁"),
   ("채권 신고", "채권의 신고, 확인 및 회수")]),
 ("ip", "지식재산권·기술", "라이선스 및 기술 이전", [
   ("지식재산권 분쟁", "침해, 권리 귀속, 계약 분쟁"),
   ("저작권, 상표, 디자인", "지식재산권 및 브랜드의 보호와 활용"),
   ("라이선스", "라이선스 계약의 작성 및 협상"),
   ("기술 이전", "기술 및 노하우 이전과 사업화"),
   ("지식재산권 사업화", "지식재산권 및 기술의 라이선스, 활용, 전략적 이용"),
   ("공급 및 유통", "지식재산권 및 기술이 관련된 계약"),
   ("권리 귀속 및 배분", "지식재산권의 귀속, 양도, 라이선스"),
   ("브랜드 보호", "상표, 상호, 디자인 등 브랜드 자산"),
   ("영업비밀 및 노하우", "영업비밀, 노하우 보호, 계약상 보호 장치")]),
 ("advice", "국제 프로젝트·투자·파트너십", "해외 투자 및 국제 프로젝트", [
   ("국제 프로젝트 및 프로젝트 파이낸스", "국경 간 프로젝트, 프로젝트 파이낸스, 해외 투자"),
   ("파트너십 및 합작투자", "구조 설계 및 계약 체계"),
   ("규제 준수", "외국인 투자에 대한 법률 및 규제 요건"),
   ("투자 구조 설계 및 실행", "국내 및 국경 간 투자의 구조 설계와 실행"),
   ("투자 회수 전략", "매각, 양도 및 기타 투자 회수 전략"),
   ("투자 및 공모 문서", "자금 조달, 투자 및 공모 문서")]),
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
        t["services"]["items"] = SERVICES8[lang]
        t["services"]["index"] = [(title, sid) for sid, title, _, _ in SERVICES8[lang]]
        t["home"]["industries"] = [("", SECTORS[lang])]


HERO = {
    "en": {"kicker": "Boutique international law firm · Headquartered in Paris",
           "h1": "Cross-border law for international business.",
           "lede": "For over 25 years, we have advised companies doing business between Europe, Asia, Africa, the United States and the Middle East: company set-up, employment, disputes and international projects. In French, English and Korean.",
           "strip": [("Bar admissions", "Paris Bar · New York Bar"), ("Working languages", "French · English · Korean"), ("Experience", "EU · UK · USA · Middle East · Asia · Africa")]},
    "fr": {"kicker": "Cabinet d'avocats international de type boutique · Siège à Paris",
           "h1": "Un droit transfrontalier pour les affaires internationales.",
           "lede": "Depuis plus de 25 ans, nous conseillons les entreprises qui exercent entre l'Europe, l'Asie, l'Afrique, les États-Unis et le Moyen-Orient : création de société, droit du travail, contentieux et projets internationaux. En français, en anglais et en coréen.",
           "strip": [("Barreaux", "Barreau de Paris · Barreau de New York"), ("Langues de travail", "Français · Anglais · Coréen"), ("Expérience", "UE · Royaume-Uni · États-Unis · Moyen-Orient · Asie · Afrique")]},
    "ko": {"kicker": "부티크 국제 로펌 · 파리 본사",
           "h1": "국제 비즈니스를 위한 국경 간 법률 자문.",
           "lede": "25년 넘게 유럽, 아시아, 아프리카, 미국, 중동 사이에서 사업하는 기업을 자문해 왔습니다. 회사 설립, 노동, 분쟁, 국제 프로젝트를 한국어, 프랑스어, 영어로 지원합니다.",
           "strip": [("변호사 등록", "파리 변호사회 · 뉴욕 변호사회"), ("업무 언어", "프랑스어 · 영어 · 한국어"), ("업무 경험", "EU · 영국 · 미국 · 중동 · 아시아 · 아프리카")]},
}
_apply_old = apply


def apply(T):
    _apply_old(T)
    for lang in ("en", "fr", "ko"):
        h = T[lang]["home"]
        h["h1"], h["lede"], h["kicker"], h["strip"] = HERO[lang]["h1"], HERO[lang]["lede"], HERO[lang]["kicker"], HERO[lang]["strip"]
