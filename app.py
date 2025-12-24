import streamlit as st

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="Neurodiversity Communication Toolkit",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------------------------
# THEME (Pastel)
# -------------------------------------------------
st.markdown(
    """
    <style>
    body {
        background-color: #fcb9a8;
    }
    .main {
        background-color: #fcb9a8;
    }
    h1, h2, h3 {
        color: #fcb9a8;
    }
    .card {
        background-color: #fcdce1;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 4px 12px rgba(11,44,74,0.08);
    }
    .primary-button > button {
        background-color: #0b2c4a;
        color: white;
        border-radius: 10px;
        padding: 0.75rem 1.5rem;
        font-size: 1rem;
        border: none;
    }
    .secondary-text {
        color: #4f6d8a;
        font-size: 0.9rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -------------------------------------------------
# LANGUAGE STATE
# -------------------------------------------------
if "lang" not in st.session_state:
    st.session_state.lang = "JP"

def t(jp, en):
    return jp if st.session_state.lang == "JP" else en

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------
with st.sidebar:
    st.markdown("### Language / 言語")
    st.session_state.lang = st.radio(
        "",
        ["JP", "EN"],
        format_func=lambda x: "日本語" if x == "JP" else "English"
    )

    st.markdown("---")
    page = st.radio(
        t("メニュー", "Menu"),
        [
            t("ホーム", "Home"),
            t("フレーズ & スクリプト", "Phrases & Scripts"),
            t("ビジュアルツール", "Visual Tools"),
            t("ガイド", "Guides"),
            t("フレームワークについて", "About the Framework")
        ]
    )

# -------------------------------------------------
# HOME
# -------------------------------------------------
if page == t("ホーム", "Home"):
    st.title(t("ニューロダイバーシティ・コミュニケーション・ツールキット",
               "Neurodiversity Communication Toolkit"))

    st.markdown(
        t(
            "日本の教育現場における、やさしく、明確で、文化的に配慮されたニューロダイバーシティの対話を支援します。",
            "Support for gentle, clear, and culturally responsive conversations about neurodiversity in Japanese educational contexts."
        )
    )

    st.markdown(
        f"""
        <div class="card">
        {t(
            "このツールキットは、文化的に尊重され、感情的に安全で、実用的に役立つ方法で、教育者が神経多様性についてコミュニケーションできるようにサポートするように設計されています。"
            "診断やラベル付けは行いません。代わりに、言語、ビジュアル、ガイダンスを提供することで、関係者全員にとって会話がより明確になり、ストレスが軽減されるよう支援します。",
            "This toolkit is designed to support educators in communicating about neurodiversity in ways that are culturally respectful, emotionally safe, and practically useful. It does not provide diagnoses or labels. Instead, it offers language, visuals, and guidance to help conversations feel clearer and less stressful for everyone involved."
        )}
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        st.button(t("保護者と話す", "I'm talking to parents"))
    with col2:
        st.button(t("児童・生徒と話す", "I'm talking to students"))
    with col3:
        st.button(t("同僚と話す", "I'm talking to colleagues"))

# -------------------------------------------------
# PHRASES & SCRIPTS
# -------------------------------------------------
elif page == t("フレーズ & スクリプト", "Phrases & Scripts"):
    st.title(t("フレーズ & スクリプト", "Phrases & Scripts"))

    sections = [
        (
            t("強みから始める", "Opening with strengths"),
            [
                ("まず、お子さんの良いところをお伝えさせてください。",
                 "First, I’d like to share some of your child’s strengths."),
                ("〇〇さんは、好奇心や創造性といった素敵な力を持っています。",
                 "○○ has many positive qualities, including curiosity and creativity.")
            ]
        ),
        (

            t("診断名を使わずに伝える", "Describing needs without labels"),
            [
                ("静かな環境だと、集中しやすいようです。",
                "○○ seems to focus better in quieter environments."),
                ("できないことではなく、サポートの工夫について考えています。",
                 "This is not about limitations, but about finding supportive conditions.")
            ]
        ),
        (
            t("協力を招く", "Inviting collaboration"),
            [
                ("一緒にどのような支援ができるか考えられたら嬉しいです。",
                 "We would like to think together about what support may help."),
                ("ご家庭でのご様子もぜひ教えてください。",
                 "Your insights as a parent are very important to us.")
            ]
        ),
        (
            t("安心して終える", "Closing safely"),
            [
                ("いつでもご相談ください。",
                 "Please feel free to share any concerns at any time."),
                ("一歩ずつ進んでいければと思います。",
                 "We can take this step by step.")
            ]
        )
    ]

    for title, items in sections:
        st.markdown(f"<div class='card'><h3>{title}</h3>", unsafe_allow_html=True)
        for jp, en in items:
            st.markdown(f"- {jp}")
            if st.session_state.lang == "EN":
                st.markdown(f"<span class='secondary-text'>{en}</span>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------------------------
# VISUAL TOOLS
# -------------------------------------------------
elif page == t("ビジュアルツール", "Visual Tools"):
    st.title(t("ビジュアル & ナラティブツール", "Visual & Narrative Tools"))

    visuals = [
        (
            t("異なるドット、異なる強み", "Different dots, different strengths"),
            t(
                "人はそれぞれ異なるドットでできています。配置が違っても、すべてが大切なパターンです。",
                "Everyone is made up of different dots. Some dots are bright, some are quiet, and some take time to appear. When dots are arranged differently, they create different patterns. Neurodiversity means that everyone's pattern is unique, and all patterns have value."
            )
        ),
        (
            t("異なる波、異なるリズム", "Different waves, different rhythms"),
            t(
                "穏やかな波のように動く人もいれば、強い波のように動く人もいます。静かな空間を必要とする波もあれば、動きを楽しむ波もあります。学習やコミュニケーションにもリズムがあります。神経多様性とは、一つのパターンを押し付けるのではなく、異なるリズムを尊重することです。",
                "Some people move like gentle waves, others like strong waves. Some waves need calm space, while others enjoy movement. Learning and communication also have rhythms. Neurodiversity means respecting different rhythms, not forcing one pattern."
            )
        ),
        (
            t("同じ目的地への異なる道", "Different paths to the same place"),
            t(
                "人は学習やコミュニケーションにおいて、それぞれ異なる道を歩みます。まっすぐな道もあれば、曲がりくねった道や途切れる道もあります。異なる道を歩むことは、迷うことを意味するわけではありません。神経多様性とは、理解に至るための異なる道を認めることです。",
                "People take different paths when they learn or communicate. Some paths are straight; others have curves or pauses. Taking a different path does not mean being lost. Neurodiversity means allowing different paths to reach understanding."
            )
        )
    ]

    for title, text in visuals:
        st.markdown(
            f"""
            <div class="card">
            <h3>{title}</h3>
            <p>{text}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

# -------------------------------------------------
# GUIDES
# -------------------------------------------------
elif page == t("ガイド", "Guides"):
    st.title(t("よくある場面のガイド", "Guides for Common Situations"))

    guides = [
        (
            t("保護者との最初の対話", "First conversation with parents"),
            t(
                "強みから始め、診断的な言葉を避け、協力関係を大切にします。",
                "Start with strengths and observations, not conclusions. Avoid technical or diagnostic language. Allow silence and reflection."
                
            )
        ),
        (
            t("児童・生徒への説明", "Talking with students"),
            t(
                "年齢に合った言葉とビジュアルを使い、違いを自然なものとして伝えます。",
                "Use age-appropriate language and visuals to normalize differences."
            )
        ),
        (
            t("同僚との共有", "Talking with colleagues"),
            t(
                "観察と実践に焦点を当て、共通の言葉を使います。",
                "Focus on observations and shared practical language."
            )
        )
    ]

    for title, text in guides:
        st.markdown(
            f"""
            <div class="card">
            <h3>{title}</h3>
            <p>{text}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

# -------------------------------------------------
# ABOUT
# -------------------------------------------------
elif page == t("フレームワークについて", "About the Framework"):
    st.title(t("このツールキットについて", "About This Toolkit"))

    st.markdown(
        t(
            "このツールキットは、日本における神経多様性に対する文化的に敏感なコミュニケーションに関する研究プロジェクトの一部です。"
            "これは、特に調和と間接的な表現が重視されるハイコンテクスト文化環境において、コミュニケーション自体がインクルージョンにおいて重要な役割を果たすという考えに基づいています。",
            "This toolkit is part of a research project on culturally responsive communication for neurodiversity in Japan. It is based on the idea that communication itself plays a key role in inclusion, especially in high-context cultural settings where harmony and indirect expression are valued."
        )
    )

    st.markdown(
        """
        <div class="card">
        <strong>Language Layer</strong><br>
        Strength-based, indirect, culturally safe tone and phrasing that reduce emotional risk <br><br>
        <strong>Visual Layer</strong><br>
        ラベルなしで理解をサポートする抽象的なメタファーとビジュアル,
        Abstract metaphors and visuals that support understanding without labels <br><br>
        <strong>Interaction Layer</strong><br>
        Conversation structures that support collaboration and trust
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        t(
            "このツールキットは診断ツールや医療ツールではありません。個人を評価、分類、または分類するものではありません。コミュニケーションと理解を支援することを目的としています。",
            "This toolkit is not a diagnostic or medical tool. It does not assess, label or classify individuals. Its purpose is to support communication and understanding."
        )
    )
