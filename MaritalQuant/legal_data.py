# legal_data.py
# ──────────────────────────────────────────────────────────────
# FairSplit Legal Knowledge Base
# Structured data extracted from primary legal sources:
#   CN: Civil Code (Marriage & Family), Judicial Interpretations,
#       6 SPC Guiding / Typical Cases
#   UK: Matrimonial Causes Act 1973, Children Act 1989,
#       4 House of Lords / Supreme Court judgments
# ──────────────────────────────────────────────────────────────

LEGAL_KNOWLEDGE_BASE = {

    # ═══════════════════════════════════════════════════════════
    # CHINA (CN)
    # ═══════════════════════════════════════════════════════════
    "CN": {
        "Statutes": {

            # ── Community Property ──────────────────────────
            "Art_1062": {
                "title": "Joint Property (夫妻共同财产)",
                "text": (
                    "Property acquired during the marriage belongs to both "
                    "spouses jointly, including: (a) wages, bonuses, and "
                    "remuneration for labour; (b) income from production, "
                    "business operations, and investments; (c) income from "
                    "intellectual property rights; (d) inherited or gifted "
                    "property (unless Art 1063(3) applies); (e) other property "
                    "that should be jointly owned. Both spouses have equal "
                    "rights to dispose of joint property."
                ),
                "source": "Civil Code Book V, Art 1062",
                "tags": ["Community Property", "Equal Rights"],
            },

            "Art_1063": {
                "title": "Separate Property (个人财产)",
                "text": (
                    "The following are one spouse's separate property: "
                    "(a) pre-marital property; (b) compensation for personal "
                    "injury; (c) property designated to one spouse by will or "
                    "gift; (d) personal daily necessities; (e) other property "
                    "that should belong to one party."
                ),
                "source": "Civil Code Book V, Art 1063",
                "tags": ["Separate Property", "Pre-marital Assets"],
            },

            "Art_1065": {
                "title": "Marital Property Agreement (约定财产制)",
                "text": (
                    "Spouses may agree in writing that property acquired "
                    "during marriage and pre-marital property shall be owned "
                    "separately, jointly, or partly separately and partly "
                    "jointly. In the absence of agreement or where the "
                    "agreement is unclear, Arts 1062 and 1063 apply."
                ),
                "source": "Civil Code Book V, Art 1065",
                "tags": ["Property Agreement", "Written Form"],
            },

            # ── Divorce Property Division ──────────────────
            "Art_1087": {
                "title": "Division of Joint Property on Divorce (离婚财产分割)",
                "text": (
                    "Upon divorce, joint property shall be divided by "
                    "agreement between the parties. If no agreement can be "
                    "reached, the People's Court shall make a judgment based "
                    "on the specific circumstances of the property, applying "
                    "the principle of protecting the interests of children, "
                    "the wife, and the innocent party (照顾子女、女方和无过错方"
                    "权益的原则)."
                ),
                "source": "Civil Code Book V, Art 1087",
                "tags": ["Property Division", "Children's Welfare",
                         "Wife Protection", "Innocent Party"],
            },

            # ── Housework Compensation ─────────────────────
            "Art_1088": {
                "title": "Housework Compensation (家务劳动补偿)",
                "text": (
                    "Where one spouse has undertaken greater obligations "
                    "in raising children, caring for the elderly, or assisting "
                    "the other spouse's work, the spouse is entitled to request "
                    "compensation from the other party upon divorce. The "
                    "specific method shall be agreed upon by both parties; "
                    "if agreement cannot be reached, the court decides. "
                    "NOTE: In practice, compensation amounts are typically "
                    "symbolic (often ¥10,000–50,000), far below the economic "
                    "value of the labour contributed."
                ),
                "source": "Civil Code Book V, Art 1088",
                "tags": ["Housework Compensation", "Non-economic Contribution",
                         "Gender Inequality"],
            },

            # ── Financial Assistance ───────────────────────
            "Art_1090": {
                "title": "Financial Assistance for Hardship (经济帮助)",
                "text": (
                    "Upon divorce, if one party has difficulty in living, "
                    "the other party who has the ability to do so shall provide "
                    "appropriate assistance. The specific method is agreed upon "
                    "by the parties or decided by the court."
                ),
                "source": "Civil Code Book V, Art 1090",
                "tags": ["Financial Assistance", "Hardship"],
            },

            # ── Fault-Based Damages ────────────────────────
            "Art_1091": {
                "title": "Fault-Based Damage Claims (过错损害赔偿)",
                "text": (
                    "Where any of the following circumstances leads to "
                    "divorce, the innocent party has the right to claim "
                    "damages: (a) bigamy; (b) cohabitation with another "
                    "person; (c) domestic violence; (d) maltreatment or "
                    "abandonment of family members; (e) other serious faults."
                ),
                "source": "Civil Code Book V, Art 1091",
                "tags": ["Fault", "Damage Claims", "Domestic Violence",
                         "Bigamy", "Cohabitation"],
            },

            # ── Asset Concealment Penalty ──────────────────
            "Art_1092": {
                "title": "Penalty for Asset Concealment (隐匿财产处罚)",
                "text": (
                    "If one spouse conceals, transfers, sells, destroys, "
                    "or squanders joint property, or fabricates joint debts "
                    "to encroach on the other's property, the court may award "
                    "a reduced share or no share of the joint property to "
                    "that party. After divorce, the other party may sue for "
                    "re-division upon discovering such conduct."
                ),
                "source": "Civil Code Book V, Art 1092",
                "tags": ["Asset Concealment", "Penalty",
                         "Post-divorce Remedy"],
            },

            # ── Child Custody ──────────────────────────────
            "Art_1084": {
                "title": "Child Custody After Divorce (离婚后子女抚养)",
                "text": (
                    "Children under 2 shall in principle be raised by the "
                    "mother. For children 2+, if the parents cannot agree, "
                    "the court decides based on the best interests of the "
                    "child. Children 8+ shall have their own wishes respected."
                ),
                "source": "Civil Code Book V, Art 1084",
                "tags": ["Child Custody", "Best Interests"],
            },

            "Art_1085": {
                "title": "Child Support (子女抚养费)",
                "text": (
                    "The non-custodial parent shall bear part or all of the "
                    "child support costs. The amount and duration are agreed "
                    "by the parties or decided by the court."
                ),
                "source": "Civil Code Book V, Art 1085",
                "tags": ["Child Support"],
            },
        },

        "Cases": {

            # ── Guiding Case No. 66 ───────────────────────
            "Guiding_Case_66": {
                "name": "Lei v. Song (雷某某诉宋某某离婚纠纷案) — Guiding Case No. 66",
                "court": "Beijing No. 3 Intermediate People's Court",
                "year": 2015,
                "dispute": (
                    "Wife (Lei) sued for divorce and property division. "
                    "During the marriage, Lei transferred ¥195,000 of "
                    "joint savings to a third-party relative's account "
                    "without husband (Song)'s knowledge, shortly before "
                    "filing for divorce."
                ),
                "court_reasoning": (
                    "The court applied Art 47 of the former Marriage Law "
                    "(now Art 1092 of the Civil Code). Lei's transfer of "
                    "¥195,000 to a relative constituted concealment of "
                    "joint property. Although Lei initially agreed to pay "
                    "¥100,000 to Song, she later reneged. The court found "
                    "that both spouses' bank accounts should be divided, "
                    "with Lei penalised for the transfer."
                ),
                "final_split": (
                    "Each party keeps their own bank accounts. Lei was "
                    "ordered to pay Song ¥120,000 as compensation for the "
                    "concealed assets (reduced share principle applied)."
                ),
                "key_holding": (
                    "Where a spouse conceals, transfers, or dissipates "
                    "joint property before or during divorce proceedings, "
                    "the court may award a reduced or zero share of the "
                    "joint property to the offending party per Art 1092."
                ),
                "tags": ["Asset Concealment", "Fault",
                         "Reduced Share", "Guiding Case"],
            },

            # ── Fang v. Yan ───────────────────────────────
            "Fang_v_Yan": {
                "name": "Fang v. Yan (方某诉颜某离婚后财产纠纷案)",
                "court": "Supreme People's Court (Jurisdictional Ruling)",
                "year": 2022,
                "dispute": (
                    "Married 2003 in the US. In 2009, purchased a house "
                    "in Jiaxing, Zhejiang registered in husband's (Yan) "
                    "name alone. Divorced 2016 in the US but did not divide "
                    "the Jiaxing property. Wife (Fang) sued in China for "
                    "her half. During proceedings, the property was sold."
                ),
                "court_reasoning": (
                    "The SPC held that for divorced Chinese citizens both "
                    "residing abroad, disputes concerning domestic property "
                    "shall be under the jurisdiction of the court where the "
                    "main property is located (Jiaxing), as it is best "
                    "positioned to investigate the property's ownership "
                    "history and transaction records."
                ),
                "final_split": (
                    "Jurisdiction assigned to Jiaxing Nanhu District Court. "
                    "Wife claimed 50% of the property's market value."
                ),
                "key_holding": (
                    "Post-divorce property disputes involving overseas "
                    "Chinese citizens are governed by the court at the "
                    "location of the principal property in China."
                ),
                "tags": ["Jurisdiction", "Overseas Chinese",
                         "Property Location Rule"],
            },

            # ── Yang v. Yang ──────────────────────────────
            "Yang_v_Yang": {
                "name": "Yang Yi v. Yang Jia (杨某乙诉杨某甲离婚后财产纠纷案)",
                "court": "Yunnan Provincial High People's Court (Re-trial)",
                "year": 2016,
                "dispute": (
                    "Married 2003 (both remarried). Husband (Yang Jia) "
                    "sold his pre-marital house for ¥200,000 and used "
                    "the proceeds as down payment on a new home purchased "
                    "during the marriage. Additional ¥340,000 was borrowed "
                    "to pay off the mortgage. Wife (Yang Yi) sought equal "
                    "division of the home. The home appreciated significantly."
                ),
                "court_reasoning": (
                    "The Procuratorate protested the 2nd-instance ruling. "
                    "Per Judicial Interpretation (III) Art 5, personal "
                    "property income during marriage is joint property "
                    "EXCEPT for natural appreciation and fruits (孳息). "
                    "The ¥200,000 down payment traced to pre-marital "
                    "property and its natural appreciation should be "
                    "deducted as husband's separate property. The remaining "
                    "mortgage and appreciation should be divided as joint "
                    "property. Yet the total home value was assessed, and "
                    "the wife received compensation accordingly."
                ),
                "final_split": (
                    "1st instance: Home to husband, wife gets ¥2,047,500. "
                    "2nd instance: Raised to ¥3,250,000 + all debt to husband. "
                    "Re-trial: Partially reversed — pre-marital contribution "
                    "and natural appreciation deducted from the joint pool."
                ),
                "key_holding": (
                    "A home purchased during marriage using proceeds from "
                    "the sale of pre-marital property requires tracing: the "
                    "pre-marital contribution and its natural appreciation "
                    "remain separate property; only the joint mortgage "
                    "payments and corresponding appreciation are divided."
                ),
                "tags": ["Pre-marital Property Tracing", "Natural Appreciation",
                         "Joint vs Separate Property"],
            },

            # ── Liang v. Wen ─────────────────────────────
            "Liang_v_Wen": {
                "name": "Liang Moling v. Wen Moxiong (梁某玲诉温某雄离婚后财产纠纷案)",
                "court": "Guangdong Meizhou Intermediate People's Court",
                "year": 2024,
                "dispute": (
                    "After divorce by agreement in Nov 2022, husband (Wen) "
                    "refused to perform the property division terms in the "
                    "divorce agreement. Wife (Liang) sued at her own "
                    "domicile court per the agreement's jurisdiction clause. "
                    "The 1st-instance court rejected the case, ruling that "
                    "divorce agreements are personal-status agreements, not "
                    "subject to contractual jurisdiction rules."
                ),
                "court_reasoning": (
                    "The appellate court reversed, citing Civil Procedure "
                    "Law Art 35 and SPC Interpretation Art 34: after marriage "
                    "dissolution, disputes solely about property division "
                    "MAY be subject to agreed jurisdiction. The divorce "
                    "agreement's jurisdiction clause was valid because: "
                    "(1) the marriage was already dissolved; (2) the dispute "
                    "is purely about property; (3) the chosen court has an "
                    "actual connection to the dispute."
                ),
                "final_split": (
                    "Case remanded to wife's domicile court (Meizhou "
                    "Meijiang District Court) for substantive hearing."
                ),
                "key_holding": (
                    "Post-divorce property disputes can be subject to "
                    "agreed jurisdiction clauses in divorce agreements, "
                    "as they are treated as 'other property rights disputes' "
                    "under civil procedure law once the marriage is dissolved."
                ),
                "tags": ["Jurisdiction", "Agreed Jurisdiction",
                         "Divorce Agreement Enforcement"],
            },

            # ── Tu v. Feng (Cross-border) ─────────────────
            "Tu_v_Feng": {
                "name": "Tu Mocui v. Feng Mowei (涂某翠诉冯某维申请认可香港特别行政区法院离婚判决案)",
                "court": "Chongqing No. 5 Intermediate People's Court",
                "year": 2024,
                "dispute": (
                    "Both parties are HK permanent residents. They divorced "
                    "in HK District Court (2022) with a consent summons "
                    "covering property division (Chongqing apartment) and "
                    "child custody. Wife (Tu) applied to mainland China "
                    "court to recognise the HK judgment for enforcement "
                    "of the property transfer."
                ),
                "court_reasoning": (
                    "The court applied the SPC Arrangement on Mutual "
                    "Recognition and Enforcement of Matrimonial Family "
                    "Judgments between Mainland and HK. It found: (1) the "
                    "HK orders were final and effective; (2) the consent "
                    "summons content on property and custody was confirmed "
                    "by both parties; (3) no grounds for refusal existed. "
                    "The court recognised the HK orders' legal effect."
                ),
                "final_split": (
                    "HK District Court order (including property division "
                    "and child custody terms) recognised by the mainland "
                    "court with full legal effect for enforcement."
                ),
                "key_holding": (
                    "HK matrimonial judgments containing property division "
                    "and child custody orders can be recognised and enforced "
                    "in mainland China under the SPC-HK mutual recognition "
                    "arrangement, provided no statutory grounds for refusal "
                    "exist."
                ),
                "tags": ["Cross-border", "HK Judgment Recognition",
                         "Enforcement", "Property Division"],
            },

            # ── Xie v. He (Domestic Violence) ─────────────
            "Xie_v_He": {
                "name": "Xie Momei v. He Moyang (谢某梅诉贺某阳离婚纠纷案)",
                "court": "Chengdu Wuhou District People's Court",
                "year": 2024,
                "dispute": (
                    "Married May 2021, one daughter born March 2022. "
                    "Husband (He) repeatedly committed domestic violence "
                    "against wife (Xie), including pouring boiling water "
                    "on her and severe beatings resulting in: 4 counts of "
                    "serious injury (Grade II), 5 counts of minor injury "
                    "(Grade II), and disability ratings of 3×Grade VII + "
                    "2×Grade X. He was criminally prosecuted for intentional "
                    "injury and maltreatment. Wife sought divorce, custody, "
                    "¥900K material damages, and ¥100K emotional damages."
                ),
                "court_reasoning": (
                    "The court applied Art 1079(3)(ii) (DV as grounds for "
                    "divorce) and issued a PRIOR JUDGMENT (先行判决) on "
                    "divorce and custody before resolving the complex "
                    "property and damages issues (still pending in related "
                    "civil and criminal proceedings). This procedural "
                    "innovation protects the DV victim from being trapped "
                    "in the marriage while awaiting property litigation. "
                    "For custody: child goes to mother (father in criminal "
                    "detention, history of violence). For child support: "
                    "¥2,000/month paid in a lump sum to age 18, plus "
                    "60% of medical and education expenses."
                ),
                "final_split": (
                    "Divorce granted. Daughter to mother. Father pays "
                    "¥2,000/month child support (lump sum to age 18). "
                    "Father bears 60% of child's medical/education costs. "
                    "Property division and damage claims reserved for "
                    "separate proceedings."
                ),
                "key_holding": (
                    "In DV divorce cases, courts may issue a PRIOR JUDGMENT "
                    "(先行判决) to dissolve the marriage and determine custody "
                    "immediately, while deferring property division and "
                    "damage claims to later proceedings. Lump-sum child "
                    "support payments are appropriate where the obligor's "
                    "future compliance is doubtful."
                ),
                "tags": ["Domestic Violence", "Prior Judgment",
                         "Child Custody", "Lump-sum Support",
                         "Criminal Prosecution"],
            },
        },
    },

    # ═══════════════════════════════════════════════════════════
    # UNITED KINGDOM (UK)
    # ═══════════════════════════════════════════════════════════
    "UK": {
        "Statutes": {

            # ── MCA 1973 Section 25 ────────────────────────
            "MCA_Sec25": {
                "title": "Matrimonial Causes Act 1973, Section 25",
                "text": (
                    "The court must have regard to ALL circumstances of the "
                    "case, with FIRST consideration given to the welfare of "
                    "any minor child of the family. The court shall in "
                    "particular have regard to: "
                    "(a) Income, earning capacity, property and other "
                    "financial resources of each party (including foreseeable "
                    "increases); "
                    "(b) Financial needs, obligations and responsibilities "
                    "of each party; "
                    "(c) Standard of living enjoyed before the breakdown; "
                    "(d) Age of each party and duration of the marriage; "
                    "(e) Physical or mental disability of either party; "
                    "(f) Contributions (including non-financial: looking "
                    "after the home or caring for the family); "
                    "(g) Conduct, if inequitable to disregard; "
                    "(h) Value of any benefit lost by reason of the divorce "
                    "(e.g. pension rights)."
                ),
                "source": "MCA 1973, s.25(1)–(2)",
                "tags": ["Eight Factors", "Financial Provision",
                         "Child Welfare First Consideration"],
            },

            # ── MCA 1973 Section 25A ───────────────────────
            "MCA_Sec25A": {
                "title": "MCA 1973, Section 25A — Clean Break Principle",
                "text": (
                    "The court has a duty to consider whether financial "
                    "obligations between the parties can be terminated as "
                    "soon as just and reasonable after divorce. For periodical "
                    "payments, the court must consider whether to limit them "
                    "to a term sufficient for the payee to adjust to financial "
                    "independence without undue hardship."
                ),
                "source": "MCA 1973, s.25A(1)–(2)",
                "tags": ["Clean Break", "Financial Independence"],
            },

            # ── MCA 1973 Sections 23–24 ────────────────────
            "MCA_Sec23_24": {
                "title": "MCA 1973, Sections 23–24 — Financial & Property Orders",
                "text": (
                    "Section 23: Court may order periodical payments, secured "
                    "periodical payments, and lump sum payments to either "
                    "party or for benefit of children. "
                    "Section 24: Court may order property transfers, "
                    "settlements, variation of ante/post-nuptial settlements, "
                    "and sale of property (s.24A)."
                ),
                "source": "MCA 1973, ss.23–24A",
                "tags": ["Financial Orders", "Property Adjustment",
                         "Lump Sum", "Periodical Payments"],
            },

            # ── Children Act 1989 ──────────────────────────
            "Children_Act_1989": {
                "title": "Children Act 1989 — Welfare Principle",
                "text": (
                    "Section 1: The child's welfare is the court's paramount "
                    "consideration. The court must have regard to the "
                    "'welfare checklist' including: (a) ascertainable wishes "
                    "and feelings of the child; (b) physical, emotional and "
                    "educational needs; (c) likely effect of change; "
                    "(d) age, sex, background and relevant characteristics; "
                    "(e) any harm suffered or at risk; (f) capability of "
                    "each parent; (g) range of powers available."
                ),
                "source": "Children Act 1989, s.1",
                "tags": ["Paramount Consideration", "Welfare Checklist",
                         "Child's Best Interests"],
            },
        },

        "Cases": {

            # ── White v White ──────────────────────────────
            "White_v_White": {
                "name": "White v White [2000] UKHL 54",
                "court": "House of Lords",
                "year": 2000,
                "key_holding": (
                    "Rejection of the 'reasonable requirements' ceiling on "
                    "awards. Established the 'yardstick of equality': where "
                    "resources exceed needs, equality should be departed from "
                    "only if there is good reason. Non-financial contributions "
                    "(homemaking, childcare) must be valued equally to "
                    "financial contributions. Financial needs are only ONE "
                    "of the s.25 factors, not determinative."
                ),
                "quote": (
                    "There should be no bias in favour of the money-earner "
                    "and against the home-maker and the child-carer."
                ),
                "quote_attribution": "Lord Nicholls",
                "financial_outcome": (
                    "33-year farming marriage. Wife awarded ~40% of total "
                    "assets (~£1.5M of ~£4.6M). Court of Appeal's order "
                    "upheld. Father's initial cash contribution carried "
                    "little weight after 33 years."
                ),
                "ratio_decidendi": (
                    "1. 'Reasonable requirements' must not be treated as a "
                    "ceiling — it is only one of the s.25(2) factors. "
                    "2. The 'yardstick of equality' applies as a CHECK, not "
                    "a rule: equality should be departed from only for good "
                    "reason. "
                    "3. Inherited property is a relevant contribution but "
                    "carries diminishing weight over time. "
                    "4. Discrimination between breadwinner and homemaker is "
                    "the antithesis of fairness."
                ),
                "tags": ["Yardstick of Equality", "Non-discrimination",
                         "Homemaker Contribution", "Long Marriage"],
            },

            # ── Miller v Miller / McFarlane v McFarlane ───
            "Miller_v_Miller": {
                "name": "Miller v Miller; McFarlane v McFarlane [2006] UKHL 24",
                "court": "House of Lords",
                "year": 2006,
                "key_holding": (
                    "Articulated the THREE STRANDS of fairness: "
                    "(1) NEEDS — financial provision for housing and living; "
                    "(2) COMPENSATION — redressing economic disparity from "
                    "career sacrifice during the marriage; "
                    "(3) SHARING — equal division of the fruits of the "
                    "marital partnership. Distinguished 'matrimonial property' "
                    "(acquired during marriage) from 'non-matrimonial property' "
                    "(pre-marital or inherited). Short marriage: sharing of "
                    "matrimonial property still applies, but non-matrimonial "
                    "property may be excluded."
                ),
                "quote": (
                    "Each party to a marriage is entitled to a fair share of "
                    "the available property. The search is always for what "
                    "are the requirements of fairness in the particular case."
                ),
                "quote_attribution": "Lord Nicholls",
                "financial_outcome": (
                    "Miller: 2yr 9mo marriage, husband's assets ~£17.5M "
                    "(mostly pre-marital). Wife awarded £5M (~28%). "
                    "McFarlane: 16-year marriage, wife (former solicitor) "
                    "gave up career. Awarded periodical payments of £250K/yr "
                    "as COMPENSATION — not just maintenance."
                ),
                "ratio_decidendi": (
                    "1. Three strands: Needs, Compensation, Sharing. "
                    "2. Non-financial contributions discrimination prohibited. "
                    "3. Short marriage: matrimonial property still shared "
                    "equally but non-matrimonial property may be ring-fenced. "
                    "4. Periodical payments can serve a compensatory purpose, "
                    "not just maintenance. "
                    "5. Clean break principle does not override compensation "
                    "obligations."
                ),
                "tags": ["Three Strands", "Needs", "Compensation",
                         "Sharing", "Short Marriage",
                         "Matrimonial vs Non-matrimonial Property"],
            },

            # ── Radmacher v Granatino ─────────────────────
            "Radmacher": {
                "name": "Radmacher v Granatino [2010] UKSC 42",
                "court": "UK Supreme Court",
                "year": 2010,
                "key_holding": (
                    "Pre-nuptial agreements should be given decisive weight "
                    "PROVIDED they are freely entered into by each party "
                    "with a full appreciation of their implications, UNLESS "
                    "in the circumstances prevailing it would not be fair to "
                    "hold the parties to the agreement. The court retains "
                    "discretion under s.25 MCA 1973 — a pre-nup is a "
                    "relevant circumstance, not a binding contract."
                ),
                "quote": (
                    "The court should give effect to a nuptial agreement "
                    "that is freely entered into by each party with a full "
                    "appreciation of its implications unless in the "
                    "circumstances prevailing it would not be fair to hold "
                    "the parties to their agreement."
                ),
                "quote_attribution": "Majority (per Lord Phillips)",
                "financial_outcome": (
                    "German heiress married French-born husband. Pre-nuptial "
                    "agreement provided neither spouse would benefit from "
                    "other's property on divorce. Court upheld the pre-nup "
                    "but awarded husband housing and income needs for "
                    "children's benefit. Lump sum reduced from £5.56M "
                    "(Court of Appeal) to £1M."
                ),
                "ratio_decidendi": (
                    "1. Pre-nuptial agreements carry decisive weight if "
                    "entered freely and with full understanding. "
                    "2. Independent legal advice is important but not "
                    "strictly required. "
                    "3. Fairness remains the overriding criterion — the "
                    "court retains discretion. "
                    "4. Needs (especially of children) cannot be completely "
                    "contracted out of."
                ),
                "tags": ["Pre-nuptial Agreement", "Autonomy",
                         "Decisive Weight", "Fairness Override"],
            },

            # ── Stack v Dowden ────────────────────────────
            "Stack_v_Dowden": {
                "name": "Stack v Dowden [2007] UKHL 17",
                "court": "House of Lords",
                "year": 2007,
                "key_holding": (
                    "For property held in joint names (without express "
                    "declaration of trust), the starting presumption is "
                    "that beneficial ownership follows legal ownership — "
                    "i.e. equal shares. The burden falls on the party "
                    "asserting unequal shares. To displace equality, the "
                    "court examines the 'whole course of dealing' between "
                    "the parties, including: financial contributions, "
                    "the parties' intentions and expectations, who paid "
                    "the mortgage, and how they organised their finances."
                ),
                "quote": (
                    "The burden will therefore be on the person seeking to "
                    "show that the parties did intend their beneficial "
                    "interests to be different from their legal interests."
                ),
                "quote_attribution": "Baroness Hale",
                "financial_outcome": (
                    "Cohabiting couple of ~27 years, 4 children. Property "
                    "held in joint names. Despite initial presumption of "
                    "50/50, Ms Dowden's greater financial contributions "
                    "(65/35 split of purchase price/mortgage) displaced "
                    "equality. Final split: 65% Dowden / 35% Stack."
                ),
                "ratio_decidendi": (
                    "1. Joint legal ownership creates presumption of equal "
                    "beneficial ownership. "
                    "2. This can be displaced by evidence of contrary "
                    "common intention. "
                    "3. Court must look at the 'whole course of dealing' "
                    "— not just direct financial contributions. "
                    "4. Applies to cohabiting couples (not just married "
                    "couples under MCA 1973). "
                    "5. Key that parties kept finances largely separate "
                    "throughout the relationship."
                ),
                "tags": ["Cohabitation", "Joint Ownership",
                         "Beneficial Interest", "Constructive Trust",
                         "Whole Course of Dealing"],
            },
        },
    },
}


# ──────────────────────────────────────────────────────────────
# Convenience lookup helpers
# ──────────────────────────────────────────────────────────────

def get_statute(jurisdiction: str, article_key: str) -> dict | None:
    """Return a statute entry by jurisdiction and key."""
    return LEGAL_KNOWLEDGE_BASE.get(jurisdiction, {}).get(
        "Statutes", {}
    ).get(article_key)


def get_case(jurisdiction: str, case_key: str) -> dict | None:
    """Return a case entry by jurisdiction and key."""
    return LEGAL_KNOWLEDGE_BASE.get(jurisdiction, {}).get(
        "Cases", {}
    ).get(case_key)


def search_by_tag(tag: str) -> list[dict]:
    """Return all entries (statutes + cases) matching a tag."""
    results = []
    for jur, sections in LEGAL_KNOWLEDGE_BASE.items():
        for section_name, entries in sections.items():
            for key, entry in entries.items():
                if tag.lower() in [t.lower() for t in entry.get("tags", [])]:
                    results.append({
                        "jurisdiction": jur,
                        "section": section_name,
                        "key": key,
                        **entry,
                    })
    return results


def list_all_keys() -> dict:
    """Return a dictionary of all keys organised by jurisdiction/section."""
    result = {}
    for jur, sections in LEGAL_KNOWLEDGE_BASE.items():
        result[jur] = {}
        for section_name, entries in sections.items():
            result[jur][section_name] = list(entries.keys())
    return result
