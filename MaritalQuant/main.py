"""
FairSplit: Cross-border Asset Risk Simulator
Step 4 — Legal Tech Dashboard

Compares divorce property division outcomes:
  CN China (Statutory / Community Property)
  GB England & Wales (Discretionary / Needs-Based)

Enriched with real legal citations from the knowledge base.
"""

import streamlit as st
import plotly.graph_objects as go
from legal_data import LEGAL_KNOWLEDGE_BASE


# ===================================================
# CALCULATION ENGINE (unchanged)
# ===================================================

def calculate_china(total_assets, marriage_years, has_children,
                    wife_is_homemaker, homemaker_years,
                    home_in_husband_name, husband_has_fault):
    pool = total_assets
    base_share = pool * 0.50

    if home_in_husband_name:
        liquidity_discount = base_share * 0.20
    else:
        liquidity_discount = 0

    effective_share = base_share - liquidity_discount

    if wife_is_homemaker and homemaker_years > 0:
        compensation = homemaker_years * 5_000
    else:
        compensation = 0

    fault_adjustment = pool * 0.05 if husband_has_fault else 0
    children_adjustment = pool * 0.03 if has_children else 0
    total = effective_share + compensation + fault_adjustment + children_adjustment

    return {
        "pool": pool,
        "base_share": base_share,
        "liquidity_discount": liquidity_discount,
        "effective_share": effective_share,
        "compensation": compensation,
        "fault_adjustment": fault_adjustment,
        "children_adjustment": children_adjustment,
        "total": total,
        "enforcement_rate": 0.30,
        "housing": ("Wife LOSES home -> cash discount"
                    if home_in_husband_name else "Standard division"),
    }


def calculate_uk(total_assets, marriage_years, has_children,
                 wife_is_homemaker, homemaker_years):
    sharing_base = total_assets * 0.50

    if marriage_years > 10:
        pool = total_assets
        mingling_note = "All assets treated as matrimonial (White v White)"
    else:
        pool = total_assets
        mingling_note = "Short marriage - pre-marital assets may be ring-fenced"

    if has_children and total_assets < 10_000_000:
        needs_outcome = total_assets * 0.60
        needs_note = "Needs override: 60% to wife for children's housing security"
    else:
        needs_outcome = sharing_base
        needs_note = "Standard 50% sharing applies"

    if wife_is_homemaker and homemaker_years > 0:
        compensation = homemaker_years * 100_000
        homemaker_outcome = sharing_base + compensation
        comp_note = (f"Replacement cost: {homemaker_years} yrs x 100,000 "
                     f"= {compensation:,.0f}")
    else:
        compensation = 0
        homemaker_outcome = sharing_base
        comp_note = "No homemaker compensation"

    total = max(needs_outcome, homemaker_outcome)
    total = min(total, total_assets)

    if needs_outcome >= homemaker_outcome:
        driver = "Needs (children's housing)"
    else:
        driver = "Compensation (career sacrifice)"

    return {
        "pool": pool,
        "sharing_base": sharing_base,
        "needs_outcome": needs_outcome,
        "compensation": compensation,
        "homemaker_outcome": homemaker_outcome,
        "total": total,
        "driver": driver,
        "mingling_note": mingling_note,
        "needs_note": needs_note,
        "comp_note": comp_note,
        "enforcement_rate": 0.78,
        "housing": ("Wife KEEPS home for children"
                    if has_children else "Equitable division of housing"),
    }


def calculate_outcomes(total_assets, marriage_years, has_children,
                       wife_is_homemaker, homemaker_years,
                       home_in_husband_name, husband_has_fault):
    cn = calculate_china(
        total_assets, marriage_years, has_children,
        wife_is_homemaker, homemaker_years,
        home_in_husband_name, husband_has_fault,
    )
    uk = calculate_uk(
        total_assets, marriage_years, has_children,
        wife_is_homemaker, homemaker_years,
    )
    return cn, uk


# ===================================================
# MASTER TRANSLATOR (unchanged)
# ===================================================

def get_legal_insight(cn_result, uk_result, wife_is_homemaker,
                      has_children, marriage_years):
    insights = []
    gap = uk_result["total"] - cn_result["total"]
    kb = LEGAL_KNOWLEDGE_BASE

    if gap > 100_000:
        art1088 = kb["CN"]["Statutes"]["Art_1088"]
        cn_comp = cn_result.get("compensation", 0)
        uk_comp = uk_result.get("compensation", 0)
        insights.append({
            "level": "warning",
            "label": "[Core Logic] CN Housework Compensation Gap",
            "body": (
                f"Your asset risk is high.  In China, despite **{art1088['title']}** "
                f"(Civil Code Art 1088), housework compensation is often "
                f"symbolic \u2014 averaging approx. \u00a530,000\u201380,000, with only a "
                f"26.92% court-approval rate.\n\n"
                f"In your scenario the CN system awards **\u00a5{cn_comp:,.0f}** "
                f"for homemaking, while the UK framework values the same "
                f"contribution at **\u00a5{uk_comp:,.0f}** \u2014 a "
                f"**\u00a5{uk_comp - cn_comp:,.0f}** compensation gap.\n\n"
                f"**[Case Precedent]** *Guiding Case No. 66 (Lei v Song)* \u2014 "
                f"even when misconduct is proven, CN courts still apply "
                f"narrow statutory caps rather than equitable redistribution."
            ),
        })

    if wife_is_homemaker:
        white = kb["UK"]["Cases"]["White_v_White"]
        insights.append({
            "level": "success",
            "label": "[Core Logic] UK Non-financial Contribution Protection",
            "body": (
                f"UK law protects your non-financial contribution.  As "
                f"established in **{white['name']}**, *\"{white['quote']}\"* "
                f"({white['quote_attribution']}).\n\n"
                f"The **Miller/McFarlane** framework further ensures that "
                f"career sacrifice is compensated through the **three strands "
                f"of fairness**: Needs, Compensation, and Sharing.\n\n"
                f"**[Case Precedent]** In *McFarlane*, a solicitor-turned-"
                f"homemaker was awarded **\u00a3250,000/year** in periodical "
                f"payments \u2014 not as maintenance, but as *compensation* "
                f"for her foregone career."
            ),
        })

    if has_children:
        mca25 = kb["UK"]["Statutes"]["MCA_Sec25"]
        children_act = kb["UK"]["Statutes"]["Children_Act_1989"]
        insights.append({
            "level": "info",
            "label": "[Core Logic] Children's Welfare & the Needs Principle",
            "body": (
                f"Both jurisdictions prioritise children \u2014 but with very "
                f"different teeth.\n\n"
                f"\U0001f1ec\U0001f1e7 **UK \u2014 MCA 1973 s.25(1):** *'{mca25['title']}'* "
                f"mandates that the **first** consideration is the welfare "
                f"of any minor child.  In practice, this often pushes the "
                f"primary carer's share to **55\u201365%** to secure housing "
                f"stability for children.  The **{children_act['title']}** "
                f"reinforces this with a statutory welfare checklist.\n\n"
                f"\U0001f1e8\U0001f1f3 **China \u2014 Art 1087:** The court shall apply "
                f"*'\u7167\u987e\u5b50\u5973\u3001\u5973\u65b9\u548c\u65e0\u8fc7\u9519\u65b9\u6743\u76ca\u7684\u539f\u5219'* (protect children, "
                f"wife, and innocent party).  However, this typically "
                f"translates to only a **2\u20135%** tilt from the 50/50 "
                f"baseline, and no mandatory housing right for the "
                f"custodial parent."
            ),
        })

    if marriage_years > 10:
        insights.append({
            "level": "info",
            "label": "[Core Logic] Long Marriage & Asset Mingling",
            "body": (
                f"After {marriage_years} years of marriage, UK law treats "
                f"virtually all assets as 'matrimonial property' subject "
                f"to equal sharing (*White v White* yardstick of equality).  "
                f"Pre-marital contributions carry diminishing weight.\n\n"
                f"In China, the statutory 50/50 community property split "
                f"(Art 1062) applies regardless of marriage duration, but "
                f"enforcement gaps and liquidity discounts erode the "
                f"wife's effective share."
            ),
        })

    if cn_result.get("fault_adjustment", 0) > 0:
        art1091 = kb["CN"]["Statutes"]["Art_1091"]
        xie_case = kb["CN"]["Cases"]["Xie_v_He"]
        insights.append({
            "level": "warning",
            "label": "[Core Logic] Fault & Domestic Violence",
            "body": (
                f"Fault is present in this scenario.  Under **{art1091['title']}** "
                f"(Art 1091), the innocent party may claim damages for "
                f"bigamy, DV, maltreatment, or abandonment \u2014 but awards "
                f"are typically **3\u20135%** of total assets.\n\n"
                f"**[Case Precedent]** In *{xie_case['name']}*, the court "
                f"used a **Prior Judgment** (\u5148\u884c\u5224\u51b3) to dissolve the "
                f"marriage immediately while DV damages were resolved "
                f"separately \u2014 protecting the victim from being trapped "
                f"in the marriage during litigation."
            ),
        })

    return insights


def render_legal_insights(insights):
    for insight in insights:
        label = insight["label"]
        body = insight["body"]
        if insight["level"] == "warning":
            st.warning(f"**{label}**\n\n{body}")
        elif insight["level"] == "success":
            st.success(f"**{label}**\n\n{body}")
        else:
            st.info(f"**{label}**\n\n{body}")


# ===================================================
# PLOTLY CHART BUILDER
# ===================================================

def build_comparison_chart(cn, uk):
    """Horizontal grouped bar: CN vs UK total share."""
    fig = go.Figure()

    fig.add_trace(go.Bar(
        y=["Wife's Total Share"],
        x=[cn["total"]],
        name="\U0001f1e8\U0001f1f3 China",
        orientation="h",
        marker=dict(
            color="rgba(234, 88, 12, 0.85)",
            line=dict(color="rgba(194, 65, 12, 1)", width=1.5),
        ),
        text=[f"\u00a5{cn['total']:,.0f}"],
        textposition="inside",
        textfont=dict(color="white", size=14, family="Inter, sans-serif"),
    ))

    fig.add_trace(go.Bar(
        y=["Wife's Total Share"],
        x=[uk["total"]],
        name="\U0001f1ec\U0001f1e7 United Kingdom",
        orientation="h",
        marker=dict(
            color="rgba(22, 163, 74, 0.85)",
            line=dict(color="rgba(21, 128, 61, 1)", width=1.5),
        ),
        text=[f"\u00a5{uk['total']:,.0f}"],
        textposition="inside",
        textfont=dict(color="white", size=14, family="Inter, sans-serif"),
    ))

    fig.update_layout(
        barmode="group",
        height=160,
        margin=dict(l=0, r=20, t=10, b=10),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        legend=dict(
            orientation="h", yanchor="bottom", y=1.02,
            xanchor="center", x=0.5,
            font=dict(size=13, family="Inter, sans-serif"),
        ),
        xaxis=dict(
            showgrid=True,
            gridcolor="rgba(226,232,240,0.6)",
            tickprefix="\u00a5",
            tickformat=",",
            tickfont=dict(size=11, color="#64748b"),
        ),
        yaxis=dict(showticklabels=False),
    )
    return fig


def build_breakdown_chart(cn, uk):
    """Stacked bar showing component breakdown for each jurisdiction."""
    categories = ["Base / Sharing", "Compensation", "Adjustments"]

    cn_values = [
        cn["effective_share"],
        cn["compensation"],
        cn["fault_adjustment"] + cn["children_adjustment"],
    ]
    uk_values = [
        uk["sharing_base"],
        uk["compensation"],
        max(0, uk["total"] - uk["sharing_base"] - uk["compensation"]),
    ]

    fig = go.Figure()

    colors_cn = ["#fb923c", "#f97316", "#ea580c"]
    colors_uk = ["#4ade80", "#22c55e", "#16a34a"]

    for i, cat in enumerate(categories):
        fig.add_trace(go.Bar(
            x=["\U0001f1e8\U0001f1f3 China"], y=[cn_values[i]],
            name=cat, marker_color=colors_cn[i],
            text=[f"\u00a5{cn_values[i]:,.0f}" if cn_values[i] > 0 else ""],
            textposition="inside",
            textfont=dict(color="white", size=11),
            showlegend=(True if i == 0 else True),
            legendgroup=cat,
        ))
        fig.add_trace(go.Bar(
            x=["\U0001f1ec\U0001f1e7 UK"], y=[uk_values[i]],
            name=cat, marker_color=colors_uk[i],
            text=[f"\u00a5{uk_values[i]:,.0f}" if uk_values[i] > 0 else ""],
            textposition="inside",
            textfont=dict(color="white", size=11),
            showlegend=False,
            legendgroup=cat,
        ))

    fig.update_layout(
        barmode="stack",
        height=340,
        margin=dict(l=0, r=10, t=10, b=40),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        legend=dict(
            orientation="h", yanchor="bottom", y=1.02,
            xanchor="center", x=0.5,
            font=dict(size=12, family="Inter, sans-serif"),
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor="rgba(226,232,240,0.5)",
            tickprefix="\u00a5",
            tickformat=",",
            tickfont=dict(size=11, color="#64748b"),
        ),
        xaxis=dict(
            tickfont=dict(size=13, family="Inter, sans-serif"),
        ),
    )
    return fig


# ===================================================
# PAGE CONFIG
# ===================================================

st.set_page_config(
    page_title="FairSplit: Divorce Asset Risk Visualiser",
    page_icon="\u2696\ufe0f",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ===================================================
# GLOBAL CSS
# ===================================================

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    /* ── Sidebar ── */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0a0f1a 0%, #111827 50%, #1e293b 100%);
    }
    [data-testid="stSidebar"] * {
        color: #cbd5e1 !important;
    }
    [data-testid="stSidebar"] .stMarkdown h2,
    [data-testid="stSidebar"] .stMarkdown h3 {
        color: #f1f5f9 !important;
        letter-spacing: -0.01em;
    }
    [data-testid="stSidebar"] .stSlider > div > div > div {
        color: #94a3b8 !important;
    }

    /* ── Header ── */
    .dashboard-header {
        background: linear-gradient(135deg, #0f172a 0%, #1e3a5f 50%, #1d4ed8 100%);
        border-radius: 16px;
        padding: 32px 40px;
        margin-bottom: 28px;
        position: relative;
        overflow: hidden;
    }
    .dashboard-header::before {
        content: '';
        position: absolute;
        top: -50%;
        right: -20%;
        width: 400px;
        height: 400px;
        background: radial-gradient(circle, rgba(59,130,246,0.15) 0%, transparent 70%);
        border-radius: 50%;
    }
    .dashboard-header::after {
        content: '';
        position: absolute;
        bottom: -60%;
        left: -10%;
        width: 300px;
        height: 300px;
        background: radial-gradient(circle, rgba(168,85,247,0.1) 0%, transparent 70%);
        border-radius: 50%;
    }
    .dashboard-title {
        color: #ffffff;
        font-size: 2.2rem;
        font-weight: 800;
        letter-spacing: -0.03em;
        margin: 0;
        position: relative;
        z-index: 1;
    }
    .dashboard-subtitle {
        color: #94a3b8;
        font-size: 1rem;
        font-weight: 400;
        margin-top: 6px;
        position: relative;
        z-index: 1;
    }
    .dashboard-badge {
        display: inline-block;
        background: rgba(59,130,246,0.2);
        border: 1px solid rgba(59,130,246,0.3);
        color: #93c5fd !important;
        font-size: 0.72rem;
        font-weight: 600;
        padding: 3px 10px;
        border-radius: 20px;
        margin-top: 10px;
        position: relative;
        z-index: 1;
        letter-spacing: 0.04em;
        text-transform: uppercase;
    }

    /* ── Metric Cards ── */
    [data-testid="stMetric"] {
        background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        padding: 20px 24px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04), 0 4px 12px rgba(0,0,0,0.03);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    [data-testid="stMetric"]:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 16px rgba(0,0,0,0.08);
    }
    [data-testid="stMetric"] label {
        font-weight: 600 !important;
        font-size: 0.8rem !important;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #64748b !important;
    }
    [data-testid="stMetric"] [data-testid="stMetricValue"] {
        font-weight: 800 !important;
        letter-spacing: -0.02em;
    }

    /* ── Gap Box ── */
    .gap-box {
        background: linear-gradient(135deg, #fef2f2 0%, #fee2e2 50%, #fecaca 100%);
        border: 2px solid #fca5a5;
        border-radius: 16px;
        padding: 28px 36px;
        text-align: center;
        margin: 8px 0;
        box-shadow: 0 4px 20px rgba(239,68,68,0.1);
    }
    .gap-title {
        color: #991b1b;
        font-size: 0.85rem;
        font-weight: 700;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        margin-bottom: 4px;
    }
    .gap-value {
        color: #dc2626;
        font-size: 2.4rem;
        font-weight: 900;
        letter-spacing: -0.02em;
    }
    .gap-sub {
        color: #b91c1c;
        font-size: 0.9rem;
        font-weight: 500;
        margin-top: 2px;
    }

    /* ── Section Headers ── */
    .section-label {
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        color: #94a3b8;
        margin-bottom: 12px;
        padding-bottom: 8px;
        border-bottom: 2px solid #e2e8f0;
    }

    /* ── Jurisdiction Headers ── */
    .china-header {
        background: linear-gradient(135deg, #c2410c, #ea580c);
        color: white !important;
        padding: 10px 20px;
        border-radius: 10px;
        text-align: center;
        font-size: 1.05rem;
        font-weight: 700;
        margin-bottom: 14px;
        letter-spacing: -0.01em;
    }
    .uk-header {
        background: linear-gradient(135deg, #1d4ed8, #2563eb);
        color: white !important;
        padding: 10px 20px;
        border-radius: 10px;
        text-align: center;
        font-size: 1.05rem;
        font-weight: 700;
        margin-bottom: 14px;
        letter-spacing: -0.01em;
    }

    /* ── Divider ── */
    .divider {
        border-top: 1px solid #e2e8f0;
        margin: 24px 0;
    }

    /* ── Footer ── */
    .footer {
        text-align: center;
        color: #94a3b8;
        font-size: 0.75rem;
        padding: 12px 0 4px;
        letter-spacing: 0.01em;
    }
    .footer a { color: #60a5fa; text-decoration: none; }

    /* ── Expander styling ── */
    .stExpander {
        border: 1px solid #e2e8f0 !important;
        border-radius: 12px !important;
        box-shadow: 0 1px 4px rgba(0,0,0,0.03) !important;
    }

    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)


# ===================================================
# SIDEBAR
# ===================================================

with st.sidebar:
    st.markdown("## \u2696\ufe0f FairSplit Settings")
    st.caption("Configure a divorce scenario to simulate")
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    # Jurisdiction
    st.markdown("### \U0001f310 Jurisdiction")
    jurisdiction_choice = st.radio(
        "Compare mode",
        options=["Compare Both", "China Only", "UK Only"],
        index=0,
        help="Choose which jurisdiction(s) to simulate.",
        label_visibility="collapsed",
    )
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    # Marriage Details
    st.markdown("### \U0001f48d Marriage Details")
    marriage_years = st.slider(
        "Marriage duration (years)", 0, 50, 10,
        help="How long the marriage lasted.",
    )
    has_children = st.checkbox("Has minor children", value=True)
    if has_children:
        num_children = st.number_input(
            "Number of children", 1, 10, 1,
        )
    else:
        num_children = 0

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    # Financial Information
    st.markdown("### \U0001f4b0 Financial Information")
    total_assets = st.number_input(
        "Total assets (\u00a5 RMB)", 0, 100_000_000, 5_000_000,
        step=100_000,
        help="Total value of all combined assets in RMB.",
    )
    wife_income = st.number_input(
        "Wife's annual income (\u00a5)", 0, 10_000_000, 0, step=10_000,
    )
    husband_income = st.number_input(
        "Husband's annual income (\u00a5)", 0, 10_000_000, 300_000, step=10_000,
    )

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    # Non-Financial Contributions
    st.markdown("### \U0001f3e0 Non-Financial Contributions")
    wife_is_homemaker = st.checkbox(
        "Wife was full-time homemaker", value=True,
        help="Whether the wife left her career to manage the household.",
    )
    if wife_is_homemaker:
        homemaker_years = st.slider(
            "Years as homemaker", 0, 50, min(8, marriage_years),
        )
        foregone_salary = st.number_input(
            "Wife's pre-homemaker salary (\u00a5/yr)",
            0, 5_000_000, 120_000, step=10_000,
        )
    else:
        homemaker_years = 0
        foregone_salary = 0

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    # Additional Factors
    st.markdown("### \u26a0\ufe0f Additional Factors")
    husband_has_fault = st.checkbox("Husband at fault (DV, affair, etc.)")
    home_in_husband_name = st.checkbox("Property registered to husband", value=True)

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    # Calculate Button in sidebar
    calculate_clicked = st.button(
        "\u26a1 Calculate Risk",
        type="primary",
        use_container_width=True,
    )


# ===================================================
# MAIN AREA
# ===================================================

# ── Professional Header ──
st.markdown("""
<div class="dashboard-header">
    <div class="dashboard-title">\u2696\ufe0f FairSplit: Divorce Asset Risk Visualiser</div>
    <div class="dashboard-subtitle">
        Bridging the gap between Statutory Law (CN) and Discretionary Fairness (UK)
    </div>
    <div class="dashboard-badge">\U0001f4d6 24 Legal Entries \u00b7 10 Statutes \u00b7 10 Cases \u00b7 2 Jurisdictions</div>
</div>
""", unsafe_allow_html=True)

# ── Quick Facts ──
st.markdown('<div class="section-label">Scenario Overview</div>',
            unsafe_allow_html=True)
qf1, qf2, qf3, qf4 = st.columns(4)
with qf1:
    st.metric("Marriage", f"{marriage_years} years")
with qf2:
    st.metric("Total Assets", f"\u00a5 {total_assets:,.0f}")
with qf3:
    st.metric("Children", str(num_children) if has_children else "None")
with qf4:
    st.metric("Homemaker", f"{homemaker_years} yrs" if wife_is_homemaker else "No")

# ── Trigger Calculation ──
if calculate_clicked:
    cn, uk = calculate_outcomes(
        total_assets, marriage_years, has_children,
        wife_is_homemaker, homemaker_years,
        home_in_husband_name, husband_has_fault,
    )
    st.session_state["cn_result"] = cn
    st.session_state["uk_result"] = uk
    st.session_state["calculated"] = True

calculated = st.session_state.get("calculated", False)
cn = st.session_state.get("cn_result")
uk = st.session_state.get("uk_result")

show_china = jurisdiction_choice in ["Compare Both", "China Only"]
show_uk = jurisdiction_choice in ["Compare Both", "UK Only"]

# ===================================================
# KEY METRICS (The Big Numbers)
# ===================================================

if calculated and cn and uk and show_china and show_uk:
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-label">Key Outcomes</div>',
                unsafe_allow_html=True)

    gap = uk["total"] - cn["total"]
    if cn["total"] > 0:
        gap_ratio = uk["total"] / cn["total"]
        ratio_text = f"UK awards {gap_ratio:.1f}x what China awards"
    else:
        ratio_text = "China awards \u00a50"

    m1, m2, m3 = st.columns(3)
    with m1:
        st.markdown('<div class="china-header">\U0001f1e8\U0001f1f3 China Outcome</div>',
                    unsafe_allow_html=True)
        st.metric(
            "Wife's Total Share",
            f"\u00a5 {cn['total']:,.0f}",
            delta=f"Enforcement: {cn['enforcement_rate']:.0%}",
            delta_color="off",
        )
    with m2:
        st.markdown('<div class="uk-header">\U0001f1ec\U0001f1e7 UK Outcome</div>',
                    unsafe_allow_html=True)
        st.metric(
            "Wife's Total Share",
            f"\u00a5 {uk['total']:,.0f}",
            delta=f"Driver: {uk['driver']}",
            delta_color="off",
        )
    with m3:
        st.markdown(f"""
        <div class="gap-box">
            <div class="gap-title">\u26a0\ufe0f PROTECTION GAP</div>
            <div class="gap-value">\u00a5 {gap:,.0f}</div>
            <div class="gap-sub">{ratio_text}</div>
        </div>
        """, unsafe_allow_html=True)

    # ── Comparison Chart ──
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-label">Visual Comparison</div>',
                unsafe_allow_html=True)

    tab_overview, tab_breakdown = st.tabs([
        "\U0001f4ca Total Comparison", "\U0001f9e9 Component Breakdown"
    ])
    with tab_overview:
        fig_compare = build_comparison_chart(cn, uk)
        st.plotly_chart(fig_compare, use_container_width=True, config={"displayModeBar": False})
    with tab_breakdown:
        fig_breakdown = build_breakdown_chart(cn, uk)
        st.plotly_chart(fig_breakdown, use_container_width=True, config={"displayModeBar": False})

    # ── Detailed Breakdown (2-col) ──
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-label">Detailed Breakdown</div>',
                unsafe_allow_html=True)

    d1, d2 = st.columns(2)
    with d1:
        st.markdown('<div class="china-header">\U0001f1e8\U0001f1f3 China Breakdown</div>',
                    unsafe_allow_html=True)
        st.markdown(f"""
| Component | Amount |
|-----------|--------|
| Matrimonial Pool | \u00a5 {cn['pool']:,.0f} |
| Base Share (50%) | \u00a5 {cn['base_share']:,.0f} |
| Liquidity Discount (\u221220%) | \u2212 \u00a5 {cn['liquidity_discount']:,.0f} |
| Effective Share | \u00a5 {cn['effective_share']:,.0f} |
| Housework Compensation | \u00a5 {cn['compensation']:,.0f} |
| Fault Adjustment | \u00a5 {cn['fault_adjustment']:,.0f} |
| Children Adjustment | \u00a5 {cn['children_adjustment']:,.0f} |
| **Total Award** | **\u00a5 {cn['total']:,.0f}** |
| \U0001f3e0 Housing | {cn['housing']} |
| \u2696\ufe0f Enforcement | {cn['enforcement_rate']:.0%} |
        """)

    with d2:
        st.markdown('<div class="uk-header">\U0001f1ec\U0001f1e7 UK Breakdown</div>',
                    unsafe_allow_html=True)
        st.markdown(f"""
| Component | Amount |
|-----------|--------|
| Divisible Pool | \u00a5 {uk['pool']:,.0f} |
| Sharing Base (50%) | \u00a5 {uk['sharing_base']:,.0f} |
| Needs Outcome (60%) | \u00a5 {uk['needs_outcome']:,.0f} |
| Homemaker Compensation | \u00a5 {uk['compensation']:,.0f} |
| Homemaker Outcome | \u00a5 {uk['homemaker_outcome']:,.0f} |
| **Total Award** | **\u00a5 {uk['total']:,.0f}** |
| \U0001f4cc Driver | {uk['driver']} |
| \U0001f3e0 Housing | {uk['housing']} |
| \u2696\ufe0f Enforcement | {uk['enforcement_rate']:.0%} |
        """)
        st.info(f"\U0001f4dd {uk['mingling_note']}")
        st.info(f"\U0001f4dd {uk['needs_note']}")
        if uk["compensation"] > 0:
            st.info(f"\U0001f4dd {uk['comp_note']}")

    # ── Gap Metrics ──
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-label">Gap Analysis</div>',
                unsafe_allow_html=True)
    g1, g2, g3 = st.columns(3)
    with g1:
        comp_gap = uk["compensation"] - cn["compensation"]
        st.metric(
            "Compensation Gap",
            f"\u00a5 {comp_gap:,.0f}",
            delta=f"UK awards \u00a5{comp_gap:,.0f} more",
            delta_color="normal",
        )
    with g2:
        st.metric(
            "Enforcement Gap",
            f"{uk['enforcement_rate'] - cn['enforcement_rate']:.0%}",
            delta=f"UK {uk['enforcement_rate']:.0%} vs CN {cn['enforcement_rate']:.0%}",
            delta_color="normal",
        )
    with g3:
        st.metric(
            "Housing Outcome",
            "Wife keeps home" if has_children else "Equitable",
            delta="UK advantage" if has_children else "Both similar",
            delta_color="normal",
        )

    # ── MASTER TRANSLATOR ──
    insights = get_legal_insight(
        cn_result=cn, uk_result=uk,
        wife_is_homemaker=wife_is_homemaker,
        has_children=has_children,
        marriage_years=marriage_years,
    )
    if insights:
        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
        st.markdown('<div class="section-label">Legal Analysis</div>',
                    unsafe_allow_html=True)
        with st.expander("\U0001f4d6 Read the Legal Logic (Why is there a gap?)",
                         expanded=True):
            st.markdown(
                "*Each insight below traces your inputs through real "
                "statutes and case law to explain **why** the numbers "
                "differ between jurisdictions.*"
            )
            render_legal_insights(insights)

elif calculated:
    # Single-jurisdiction mode
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    if show_china and cn:
        st.markdown('<div class="section-label">\U0001f1e8\U0001f1f3 China Outcome</div>',
                    unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric("Wife's Total Share", f"\u00a5 {cn['total']:,.0f}")
        with c2:
            st.metric("Housework Compensation", f"\u00a5 {cn['compensation']:,.0f}")
        with c3:
            st.metric("Enforcement Rate", f"{cn['enforcement_rate']:.0%}")

    if show_uk and uk:
        st.markdown('<div class="section-label">\U0001f1ec\U0001f1e7 UK Outcome</div>',
                    unsafe_allow_html=True)
        u1, u2, u3 = st.columns(3)
        with u1:
            st.metric("Wife's Total Share", f"\u00a5 {uk['total']:,.0f}")
        with u2:
            st.metric("Compensation (Career Loss)", f"\u00a5 {uk['compensation']:,.0f}")
        with u3:
            st.metric("Key Driver", uk["driver"])

    st.info("\U0001f4a1 Select **Compare Both** in the sidebar to see the full gap analysis, "
            "charts, and legal insights.")

    # Single-jurisdiction insights
    if cn and show_china and not show_uk:
        dummy_uk = calculate_uk(total_assets, marriage_years, has_children,
                                wife_is_homemaker, homemaker_years)
        insights = get_legal_insight(cn_result=cn, uk_result=dummy_uk,
                                     wife_is_homemaker=wife_is_homemaker,
                                     has_children=has_children,
                                     marriage_years=marriage_years)
        cn_insights = [i for i in insights
                       if "CN" in i["label"] or "Children" in i["label"]
                       or "Fault" in i["label"]]
        if cn_insights:
            with st.expander("\U0001f4d6 Legal Insights for Your Scenario"):
                render_legal_insights(cn_insights)

    elif uk and show_uk and not show_china:
        dummy_cn = calculate_china(total_assets, marriage_years, has_children,
                                    wife_is_homemaker, homemaker_years,
                                    home_in_husband_name, husband_has_fault)
        insights = get_legal_insight(cn_result=dummy_cn, uk_result=uk,
                                     wife_is_homemaker=wife_is_homemaker,
                                     has_children=has_children,
                                     marriage_years=marriage_years)
        uk_insights = [i for i in insights
                       if "UK" in i["label"] or "Children" in i["label"]
                       or "Long Marriage" in i["label"]]
        if uk_insights:
            with st.expander("\U0001f4d6 Legal Insights for Your Scenario"):
                render_legal_insights(uk_insights)

else:
    # No calculation yet
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align:center; padding: 60px 20px; color: #94a3b8;">
        <div style="font-size: 3rem; margin-bottom: 12px;">\U0001f4ca</div>
        <div style="font-size: 1.1rem; font-weight: 600; color: #64748b;">
            Configure your scenario in the sidebar
        </div>
        <div style="font-size: 0.9rem; margin-top: 6px;">
            Then click <strong>\u26a1 Calculate Risk</strong> to see results
        </div>
    </div>
    """, unsafe_allow_html=True)


# ── Footer ──
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="footer">
    FairSplit v0.4 \u00b7 Legal Tech Dashboard \u00b7
    Based on thesis: "The Impact of Chinese and British Marital Property Division
    Mechanism on Chinese Women's Post-divorce Economic Security" \u00b7
    Lingnan University 2025 \u00b7
    24 legal entries across 2 jurisdictions
</div>
""", unsafe_allow_html=True)
