import streamlit as st

# -----------------------------
# BASIC APP CONFIG
# -----------------------------
st.set_page_config(
    page_title="Neurodiversity Communication Toolkit (Japan)",
    layout="centered"
)

# -----------------------------
# GLOBAL STYLE (CALM, LOW LOAD)
# -----------------------------
st.markdown("""
<style>
body {
    background-color: #FAFAFA;
}
.block-container {
    padding-top: 2rem;
    max-width: 720px;
}
h1, h2, h3 {
    font-weight: 600;
}
.card {
    background-color: #FFFFFF;
    padding: 1.2rem;
    border-radius: 16px;
    box-shadow: 0px 2px 6px rgba(0,0,0,0.05);
    margin-bottom: 1rem;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# LANGUAGE TOGGLE
# -----------------------------
language = st.sidebar.radio(
    "Language / 言語",
    ["日本語", "English"],
    index=0
)

# -----------------------------
# CONTENT DATA
# -----------------------------
PHRASES = {
    "parents_first": {
        "title_jp": "保護者と初めて話すとき",
        "title_en": "First conversation with parents",
        "items": [
            {
                "jp": "〇〇さんは、とても集中力が高く、興味のあることには深く取り組める力があります。",
                "en": "Your child shows strong focus and can engage deeply with areas of interest."
            },
            {
                "jp": "学校では、その力を活かしながら、より安心して学べる方法を一緒に考えたいと思っています。",
                "en": "At school, we would like to think together about ways to support learning comfortably."
            }
        ]
    },
    "students": {
        "title_jp": "生徒に説明するとき",
        "title_en": "Explaining to students",
        "items": [
            {
                "jp": "人それぞれ、考え方や感じ方の道は少しずつ違います。",
                "en": "Everyone has slightly different ways of thinking and feeling."
            }
        ]
    }
}

VISUAL_NARRATIVES = {
    "dots": {
        "title_jp": "ドットの物語",
        "text_jp": "人の考えは、点の集まりのようなものです。点の並び方が違うと、見える形も変わります。",
        "text_en": "Thoughts are like dots. When arranged differently, they form different patterns."
    },
    "waves": {
        "title_jp": "波の物語",
        "text_jp": "集中や疲れには波があります。波を理解すると、無理をしない選択ができます。",
        "text_en": "Focus and energy come in waves. Understanding them helps us choose gently."
    },
    "paths": {
        "title_jp": "道の物語",
        "text_jp": "学びへの道は一つではありません。それぞれに合った道があります。",
        "text_en": "There is more than one path to learning."
    }
}

SCENARIOS = [
    {
        "title_jp": "保護者に気になる点を伝えたい",
        "keep_in_mind": "関係性を優先し、断定を避ける",
        "phrases": "強みから話し始め、協力をお願いする形にする",
        "visual": "ドットの物語"
    },
    {
        "title_jp": "教室での配慮を説明したい",
        "keep_in_mind": "子どもの安心感を大切にする",
        "phrases": "選択肢として伝える",
        "visual": "道の物語"
    }
]

# -----------------------------
# NAVIGATION
# -----------------------------
menu = st.sidebar.radio(
    "Menu",
    [
        "Home / Today",
        "Phrases & Scripts",
        "Visual & Narrative Tools",
        "Guides for Situations",
        "About the Framework"
    ]
)

# -----------------------------
# HOME
# -----------------------------
if menu == "Home / Today":
    st.title("Neurodiversity Communication Toolkit")

    st.markdown(
        "<div class='card'>"
        "日本の教育現場で、やさしく、安心して<br>"
        "神経多様性について話すための支援ツール"
        "</div>",
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)
    col1.button("保護者と話す")
    col2.button("生徒と話す")
    col3.button("同僚と話す")

    st.markdown(
        "<div class='card'>"
        "Today’s tip: 言葉を選ぶことは、関係を守ることです。"
        "</div>",
        unsafe_allow_html=True
    )

# -----------------------------
# PHRASES
# -----------------------------
elif menu == "Phrases & Scripts":
    st.title("Phrases & Scripts")

    for section in PHRASES.values():
        st.subheader(section["title_jp"])
        for item in section["items"]:
            st.markdown(
                f"<div class='card'>{item['jp']}<br>"
                f"<small>{item['en']}</small></div>",
                unsafe_allow_html=True
            )

# -----------------------------
# VISUAL TOOLS
# -----------------------------
elif menu == "Visual & Narrative Tools":
    st.title("Visual & Narrative Tools")

    for item in VISUAL_NARRATIVES.values():
        st.subheader(item["title_jp"])
        st.markdown(
            f"<div class='card'>{item['text_jp']}<br>"
            f"<small>{item['text_en']}</small></div>",
            unsafe_allow_html=True
        )

# -----------------------------
# SCENARIOS
# -----------------------------
elif menu == "Guides for Situations":
    st.title("Guides for Situations")

    for s in SCENARIOS:
        st.markdown(
            f"<div class='card'>"
            f"<strong>{s['title_jp']}</strong><br>"
            f"大切にすること: {s['keep_in_mind']}<br>"
            f"言葉の方向性: {s['phrases']}<br>"
            f"おすすめの比喩: {s['visual']}"
            f"</div>",
            unsafe_allow_html=True
        )

# -----------------------------
# ABOUT
# -----------------------------
elif menu == "About the Framework":
    st.title("About the Framework")

    st.markdown(
        "<div class='card'>"
        "このツールは、診断や医療目的のものではありません。<br>"
        "日本の文化や教育現場に配慮した<br>"
        "コミュニケーション支援のためのものです。"
        "</div>",
        unsafe_allow_html=True
    )

    st.markdown("""
**Three Layers**
- Language Layer: 言葉のトーンと選び方  
- Visual Layer: ドット・波・道の比喩  
- Interaction Layer: 会話の流れ  
""")
