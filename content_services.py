"""Services and sectors supplied by the firm (FR original; EN/KO translations to be reviewed)."""

# (id, title, intro, bullets)
SERVICES = {
    "fr": [
        ("advice", "Conseil juridique", "Projets d'expansion internationale, d'investissement et d'implantation.",
         ["Droit des sociétés", "Contrats", "Droit réglementaire", "Gouvernance", "Restructuration", "Conformité au droit européen", "Droit du travail", "Distribution, consommation et protection des données"]),
        ("contracts", "Contrats", "Des contrats de l'activité courante aux partenariats et joint-ventures.",
         ["Contrats commerciaux", "Distribution", "Contrats sociaux", "Prestation de services", "Vente", "Partenariats", "Joint-ventures (JV)", "Baux commerciaux"]),
        ("litigation", "Contentieux", "En première instance et en appel devant les juridictions françaises.",
         ["Civil", "Commercial", "Social", "Propriété intellectuelle"]),
        ("arbitration", "Arbitrage national et international", "Procédures devant les principales institutions d'arbitrage.",
         ["CCI", "KCAB", "TAS (Tribunal arbitral du sport)"]),
        ("compliance", "Conformité", "Droit français et européen.",
         ["Droit français", "Droit européen"]),
        ("commercial", "Commercial", "Pratiques commerciales, consommation et propriété intellectuelle.",
         ["Concurrence déloyale et parasitisme", "Pratiques commerciales déloyales", "Droit de la consommation", "Responsabilité élargie du producteur (REP)", "Droit d'auteur, contrefaçon et protection des droits de PI", "Recouvrement de créances", "Rupture des relations commerciales établies", "Conditions générales de vente et d'achat"]),
        ("employment", "Droit du travail", "Contrats, restructurations et contentieux du travail.",
         ["Rédaction et négociation de contrats de travail et de services", "Restructuration", "Démission", "Prise d'acte", "Licenciement", "Harcèlement et discrimination"]),
        ("corporate", "Corporate", "Créer, gérer et faire évoluer une société.",
         ["Structuration et constitution de sociétés", "Immatriculation", "Gouvernance", "Approbation des comptes annuels", "Modification et transfert d'activités", "Restructuration", "Dissolution et liquidation"]),
    ],
    "en": [
        ("advice", "Legal advice", "International expansion, investment and set-up projects.",
         ["Company law", "Contracts", "Regulatory law", "Governance", "Restructuring", "EU law compliance", "Employment law", "Distribution, consumer and data protection law"]),
        ("contracts", "Contracts", "From everyday commercial terms to partnerships and joint ventures.",
         ["Commercial contracts", "Distribution", "Employment contracts", "Service agreements", "Sales", "Partnerships", "Joint ventures (JV)", "Commercial leases"]),
        ("litigation", "Litigation", "At first instance and on appeal before the French courts.",
         ["Civil", "Commercial", "Employment", "Intellectual property"]),
        ("arbitration", "National and international arbitration", "Proceedings before the main arbitral institutions.",
         ["ICC", "KCAB", "CAS (Court of Arbitration for Sport)"]),
        ("compliance", "Compliance", "French and European law.",
         ["French law", "European law"]),
        ("commercial", "Commercial law", "Fair trading, consumer and intellectual property issues.",
         ["Unfair competition and free-riding", "Unfair commercial practices", "Consumer law", "Extended producer responsibility (EPR)", "Copyright, counterfeiting and enforcement of IP rights", "Debt recovery", "Termination of established commercial relationships", "General terms of sale and purchase"]),
        ("employment", "Employment law", "Contracts, restructuring and employment disputes.",
         ["Drafting and negotiating employment and service contracts", "Restructuring", "Resignation", "Termination by the employee for the employer's breach (prise d'acte)", "Dismissal", "Harassment and discrimination"]),
        ("corporate", "Corporate", "Setting up, running and reshaping a company.",
         ["Structuring and incorporating companies", "Registration", "Governance", "Approval of annual accounts", "Changes to and transfers of business", "Restructuring", "Dissolution and liquidation"]),
    ],
    "ko": [
        ("advice", "법률 자문", "해외 확장, 투자 및 현지 진출 프로젝트.",
         ["회사법", "계약", "규제법", "지배구조", "구조조정", "EU법 준수", "노동법", "유통·소비자·개인정보 보호법"]),
        ("contracts", "계약", "일상적인 상거래부터 파트너십과 합작투자까지.",
         ["상사 계약", "유통", "근로 계약", "용역 계약", "매매", "파트너십", "합작투자(JV)", "상업용 임대차"]),
        ("litigation", "소송", "프랑스 법원의 1심 및 항소심.",
         ["민사", "상사", "노동", "지식재산"]),
        ("arbitration", "국내외 중재", "주요 중재기관 절차.",
         ["ICC", "KCAB", "CAS(스포츠중재재판소)"]),
        ("compliance", "컴플라이언스", "프랑스법 및 유럽법.",
         ["프랑스법", "유럽법"]),
        ("commercial", "상사법", "공정거래, 소비자 및 지식재산 문제.",
         ["부정경쟁 및 무임승차", "불공정 상관행", "소비자법", "생산자책임확대제도(EPR)", "저작권, 위조 및 지식재산권 보호", "채권 회수", "확립된 거래관계의 파기", "일반 판매·구매 약관"]),
        ("employment", "노동법", "계약, 구조조정 및 노동 분쟁.",
         ["근로·용역 계약 작성 및 협상", "구조조정", "사직", "근로자의 사용자 귀책 해지(prise d'acte)", "해고", "괴롭힘 및 차별"]),
        ("corporate", "기업법(Corporate)", "회사의 설립, 운영 및 재편.",
         ["회사 구조 설계 및 설립", "등기", "지배구조", "연간 결산 승인", "사업 변경 및 양도", "구조조정", "해산 및 청산"]),
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
