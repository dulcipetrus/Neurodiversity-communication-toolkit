import streamlit as st

# ======================================================
# APP CONFIG
# ======================================================
st.set_page_config(
    page_title="Neurodiversity Communication Toolkit (Japan)",
    layout="centered"
)

# ======================================================
# GLOBAL STYLES — DARK BLUE / LIGHT BLUE THEME
# ======================================================
st.markdown("""
<style>
/* Background */
body {
    background-color: #F4F8FC;
}

/* Main container */
.block-container {
    max-width: 780px;
    padding-top: 2rem;
}

/* Headings */
h1, h2, h3 {
    font-weight: 600;
    color: #0A2A4A; /* Dark Blue */
}

/* Card style */
.card {
    background-color: #FFFFFF;
    padding: 1.5rem;
    border-radius: 18px;
    border-left: 6px solid #4DA3FF; /* Light Blue Accent */
    box-shadow: 0px 2px 8px rgba(10, 42, 74, 0.08);
    margin-bottom: 1.3rem;
}

/* Subtle text */
.small {
    color: #4A657D;
    font-size: 0.85rem;
}

/* Button cards */
.button-card {
    padding: 1.4rem;
    border-radius: 16px;
    background-color: #E6F1FF;
    color: #0A2A4A;
    text-align: center;
    font-weight: 500;
    border: 1px solid #C7E0FF;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #0A2A4A;
}

section[data-testid="stSidebar"] * {
    color: #FFFFFF;
}
</style>
""", unsafe_allow_html=True)

# ======================================================
# LANGUAGE SYSTEM
# ======================================================
language = st.sidebar.radio(
    "Language / 言語",
    ["日本語", "English"],
    index=0
)

def t(jp, en):
    return jp if language == "日本語" else en

# ======================================================
# CONTENT DATA
# ======================================================
PHRASES = {
    "parents_first": {
        "label": t("保護者と初めて話す", "First conversation with parents"),
        "items": [
            {
                "category": t("強みから始める", "Opening with strengths"),
                "jp": "〇〇さんは、興味のあることに深く集中できる力があります。",
                "en": "Your child shows a strong ability to focus deeply on areas of interest."
            },
            {
                "category": t("協力への招待", "Invitation to collaborate"),
                "jp": "学校では、その力を大切にしながら、一緒に支え方を考えたいと思っています。",
                "en": "At school, we would like to think together about how to support this strength."
            }
        ]
    },
    "students": {
        "label": t("生徒に説明する", "Explaining to students"),
        "items": [
            {
                "category": t("やさしい説明", "Gentle explanation"),
                "jp": "人それぞれ、考え方や感じ方の道は少しずつ違います。",
                "en": "Everyone has slightly different paths for thinking and feeling."
            }
        ]
    }
}

VISUALS = {
    "dots": {
        "title": t("ドットの物語", "Dot Pattern Narrative"),
        "jp": "人の考えは点の集まりのようなものです。並び方が違えば、見える形も変わります。",
        "en": "Thoughts are like dots. Different arrangements create different patterns."
    },
    "waves": {
        "title": t("波の物語", "Waves Narrative"),
        "jp": "集中や疲れには波があります。波を知ることで、無理を減らせます。",
        "en": "Focus and energy come in waves. Understanding them helps reduce strain."
    },
    "paths": {
        "title": t("道の物語", "Pathways Narrative"),
        "jp": "学びへの道は一つではありません。それぞれに合った道があります。",
        "en": "There is more than one path to learning."
    }
}

SCENARIOS = [
    {
        "title": t("保護者に気になる点を伝えたい", "Talking to a parent about concerns"),
        "mind": t("関係性を守り、断定を避ける", "Protect the relationship and avoid conclusions"),
        "phrases": t("強みを起点に、協力の形で伝える", "Begin with strengths and invite collaboration"),
        "visual": t("ドットの物語", "Dot Narrative")
    },
    {
        "title": t("教室での配慮を説明したい", "Explaining classroom adjustments"),
        "mind": t("安心感と選択肢を大切にする", "Prioritize safety and choice"),
        "phrases": t("義務ではなく選択として説明する", "Explain as an option, not an obligation"),
        "visual": t("道の物語", "Pathways Narrative")
    }
]

# ======================================================
# NAVIGATION
# ======================================================
menu = st.sidebar.radio(
    t("メニュー", "Menu"),
    [
        t("ホーム", "Home"),
        t("フレーズ & スクリプト", "Phrases & Scripts"),
        t("ビジュアルツール", "Visual Tools"),
        t("状況別ガイド", "Guides"),
        t("フレームワークについて", "About")
    ]
)

# ======================================================
# HOME
# ======================================================
if menu == t("ホーム", "Home"):
    st.title(t("やさしい対話のための支援ツール", "Support for Gentle Communication"))

    st.markdown(
        f"<div class='card'>{t('日本の教育現場で、神経多様性について安心して話すためのツールです。','A calm, culturally responsive toolkit for discussing neurodiversity in Japanese schools.')}</div>",
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)
    col1.markdown(f"<div class='button-card'>{t('保護者と話す','Talking to parents')}</div>", unsafe_allow_html=True)
    col2.markdown(f"<div class='button-card'>{t('生徒と話す','Talking to students')}</div>", unsafe_allow_html=True)
    col3.markdown(f"<div class='button-card'>{t('同僚と話す','Talking to colleagues')}</div>", unsafe_allow_html=True)

    st.markdown(
        f"<div class='card'>{t('今日のヒント：言葉は関係をつくります。','Today’s tip: Words shape relationships.')}</div>",
        unsafe_allow_html=True
    )

# ======================================================
# PHRASES
# ======================================================
elif menu == t("フレーズ & スクリプト", "Phrases & Scripts"):
    st.title(t("フレーズ & スクリプト", "Phrases & Scripts"))

    for section in PHRASES.values():
        st.subheader(section["label"])
        for item in section["items"]:
            st.markdown(
                f"<div class='card'><strong>{item['category']}</strong><br>"
                f"{item['jp'] if language == '日本語' else item['en']}"
                f"<br><span class='small'>{item['en'] if language == '日本語' else item['jp']}</span></div>",
                unsafe_allow_html=True
            )

# ======================================================
# VISUAL TOOLS
# ======================================================
elif menu == t("ビジュアルツール", "Visual Tools"):
    st.title(t("ビジュアル & ナラティブ", "Visual & Narrative Tools"))

    for v in VISUALS.values():
        st.markdown(
            f"<div class='card'><strong>{v['title']}</strong><br>"
            f"{v['jp'] if language == '日本語' else v['en']}"
            f"<br><span class='small'>{v['en'] if language == '日本語' else v['jp']}</span></div>",
            unsafe_allow_html=True
        )

# ======================================================
# GUIDES
# ======================================================
elif menu == t("状況別ガイド", "Guides"):
    st.title(t("状況別ガイド", "Guides for Situations"))

    for s in SCENARIOS:
        st.markdown(
            f"<div class='card'><strong>{s['title']}</strong><br>"
            f"{t('大切にすること','Keep in mind')}: {s['mind']}<br>"
            f"{t('言葉の方向性','Language approach')}: {s['phrases']}<br>"
            f"{t('おすすめの比喩','Suggested visual')}: {s['visual']}</div>",
            unsafe_allow_html=True
        )

# ======================================================
# ABOUT
# ======================================================
elif menu == t("フレームワークについて", "About"):
    st.title(t("フレームワークについて", "About the Framework"))

    st.markdown(
        f"<div class='card'>{t('このツールは診断や医療目的のものではありません。','This tool is not for diagnosis or medical use.')}</div>",
        unsafe_allow_html=True
    )

    st.markdown(t(
        """
**三つのレイヤー**
- 言語レイヤー：トーン、間接性、配慮  
- ビジュアルレイヤー：ドット・波・道  
- インタラクションレイヤー：対話の流れ  
""",
        """
**Three Layers**
- Language Layer: tone, phrasing, indirectness  
- Visual Layer: dots, waves, pathways  
- Interaction Layer: conversation structure  
"""
    ))
