# import streamlit as st
# import pandas as pd
# from pathlib import Path
# from sentence_transformers import SentenceTransformer
# from sklearn.metrics.pairwise import cosine_similarity

# # PAGE CONFIGURATION

# st.set_page_config(
#     page_title="Career Discovery AI",
#     page_icon="✦",
#     layout="wide",
#     initial_sidebar_state="collapsed"
# )

# # CUSTOM DESIGN

# st.markdown(
#     """
#     <style>

#     /* -----------------------------------------------------
#        COLOR SYSTEM

#        Midnight Ink : #101827
#        Deep Slate   : #182235
#        Coral        : #FF7A66
#        Mint         : #65D6AD
#        Warm Ivory   : #F7F3EA
#        Muted Text   : #AEB8C8
#        ----------------------------------------------------- */


#     /* Main application */

#     .stApp {
#         background:
#             radial-gradient(
#                 circle at 15% 10%,
#                 rgba(101, 214, 173, 0.10),
#                 transparent 28%
#             ),
#             radial-gradient(
#                 circle at 85% 15%,
#                 rgba(255, 122, 102, 0.10),
#                 transparent 30%
#             ),
#             #101827;

#         color: #F7F3EA;
#     }


#     /* Main content width */

#     .block-container {
#         max-width: 1180px;
#         padding-top: 2.5rem;
#         padding-bottom: 4rem;
#     }


#     /* -----------------------------------------------------
#        SMALL BRAND MARK
#        ----------------------------------------------------- */

#     .brand-line {
#         display: flex;
#         align-items: center;
#         gap: 10px;

#         color: #65D6AD;

#         font-size: 0.78rem;
#         font-weight: 700;

#         letter-spacing: 0.16em;
#         text-transform: uppercase;

#         margin-bottom: 1.5rem;
#     }

#     .brand-dot {
#         width: 9px;
#         height: 9px;

#         background: #FF7A66;

#         border-radius: 50%;

#         box-shadow:
#             0 0 18px rgba(255, 122, 102, 0.8);
#     }


#     /* -----------------------------------------------------
#        HERO
#        ----------------------------------------------------- */

#     .hero-title {

#         font-size: clamp(3rem, 7vw, 6.2rem);

#         line-height: 0.96;

#         letter-spacing: -0.055em;

#         font-weight: 800;

#         color: #F7F3EA;

#         max-width: 900px;

#         margin-bottom: 1.3rem;
#     }


#     .hero-highlight {
#         color: #65D6AD;
#     }


#     .hero-description {

#         color: #AEB8C8;

#         font-size: 1.12rem;

#         line-height: 1.75;

#         max-width: 720px;

#         margin-bottom: 2rem;
#     }


#     /* -----------------------------------------------------
#        LITTLE FEATURE PILLS
#        ----------------------------------------------------- */

#     .feature-row {

#         display: flex;

#         flex-wrap: wrap;

#         gap: 10px;

#         margin-bottom: 2.8rem;
#     }


#     .feature-pill {

#         display: inline-block;

#         border: 1px solid rgba(247,243,234,0.12);

#         background: rgba(255,255,255,0.035);

#         color: #C8D0DC;

#         border-radius: 999px;

#         padding: 8px 14px;

#         font-size: 0.82rem;
#     }


#     /* -----------------------------------------------------
#        SECTION LABEL
#        ----------------------------------------------------- */

#     .section-label {

#         color: #FF7A66;

#         font-size: 0.76rem;

#         font-weight: 700;

#         letter-spacing: 0.14em;

#         text-transform: uppercase;

#         margin-bottom: 0.5rem;
#     }


#     .section-title {

#         color: #F7F3EA;

#         font-size: 2rem;

#         font-weight: 700;

#         letter-spacing: -0.03em;

#         margin-bottom: 0.4rem;
#     }


#     .section-copy {

#         color: #AEB8C8;

#         line-height: 1.65;

#         margin-bottom: 1.5rem;
#     }


#     /* -----------------------------------------------------
#        TEXT AREA
#        ----------------------------------------------------- */

#     .stTextArea textarea {

#         background: #182235 !important;

#         color: #F7F3EA !important;

#         border:

#             1px solid
#             rgba(101, 214, 173, 0.25) !important;

#         border-radius: 18px !important;

#         padding: 18px !important;

#         font-size: 1rem !important;

#         line-height: 1.6 !important;

#         min-height: 190px !important;

#         box-shadow:
#             0 18px 50px rgba(0,0,0,0.15);
#     }


#     .stTextArea textarea:focus {

#         border:
#             1px solid #65D6AD !important;

#         box-shadow:
#             0 0 0 3px
#             rgba(101,214,173,0.10) !important;
#     }


#     .stTextArea textarea::placeholder {
#         color: #768297 !important;
#     }


#     /* -----------------------------------------------------
#        BUTTON
#        ----------------------------------------------------- */

#     .stButton > button {

#         width: 100%;

#         background: #65D6AD;

#         color: #101827;

#         border: none;

#         border-radius: 14px;

#         padding: 0.85rem 1.2rem;

#         font-weight: 800;

#         font-size: 0.98rem;

#         transition: all 0.2s ease;
#     }


#     .stButton > button:hover {

#         background: #7EE2BD;

#         color: #101827;

#         transform: translateY(-2px);

#         box-shadow:
#             0 10px 30px
#             rgba(101,214,173,0.18);
#     }


#     /* -----------------------------------------------------
#        RESULT CARD
#        ----------------------------------------------------- */

#     .career-card {

#         background:
#             linear-gradient(
#                 145deg,
#                 rgba(255,255,255,0.055),
#                 rgba(255,255,255,0.025)
#             );

#         border:
#             1px solid
#             rgba(247,243,234,0.10);

#         border-radius: 22px;

#         padding: 1.4rem;

#         min-height: 215px;

#         margin-bottom: 1rem;

#         box-shadow:
#             0 20px 50px
#             rgba(0,0,0,0.15);
#     }


#     .rank-number {

#         color: #FF7A66;

#         font-size: 0.76rem;

#         font-weight: 800;

#         letter-spacing: 0.12em;

#         text-transform: uppercase;
#     }


#     .career-name {

#         color: #F7F3EA;

#         font-size: 1.55rem;

#         line-height: 1.2;

#         font-weight: 750;

#         margin-top: 0.5rem;

#         margin-bottom: 0.6rem;
#     }


#     .career-category {

#         display: inline-block;

#         color: #65D6AD;

#         background:
#             rgba(101,214,173,0.08);

#         border:
#             1px solid
#             rgba(101,214,173,0.18);

#         padding: 5px 9px;

#         border-radius: 8px;

#         font-size: 0.75rem;

#         margin-bottom: 1rem;
#     }


#     .match-score {

#         color: #F7F3EA;

#         font-size: 2rem;

#         font-weight: 800;

#         letter-spacing: -0.04em;

#         margin-top: 0.7rem;
#     }


#     .match-label {

#         color: #8995A8;

#         font-size: 0.72rem;

#         text-transform: uppercase;

#         letter-spacing: 0.10em;
#     }


#     /* -----------------------------------------------------
#        DETAIL BOX
#        ----------------------------------------------------- */

#     .detail-box {

#         background:
#             rgba(255,255,255,0.025);

#         border-left:
#             3px solid #65D6AD;

#         border-radius: 0 14px 14px 0;

#         padding: 1rem 1.2rem;

#         color: #C8D0DC;

#         line-height: 1.7;

#         margin-bottom: 0.8rem;
#     }


#     /* -----------------------------------------------------
#        DISCLAIMER
#        ----------------------------------------------------- */

#     .disclaimer {

#         margin-top: 3rem;

#         padding: 1.2rem 1.4rem;

#         border:
#             1px solid
#             rgba(255,122,102,0.20);

#         background:
#             rgba(255,122,102,0.055);

#         border-radius: 16px;

#         color: #B9C1CD;

#         font-size: 0.86rem;

#         line-height: 1.6;
#     }


#     /* Remove Streamlit header decoration */

#     header[data-testid="stHeader"] {
#         background: transparent;
#     }


#     /* Divider */

#     hr {

#         border: none;

#         border-top:
#             1px solid
#             rgba(247,243,234,0.08);

#         margin-top: 2.5rem;

#         margin-bottom: 2.5rem;
#     }

#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # PATHS

# BASE_DIR = Path(__file__).resolve().parent
# DATA_FILE = BASE_DIR / "data" / "careers_prepared.csv"


# # LOAD MODEL AND DATA

# @st.cache_resource # Without caching, Streamlit could repeatedly reload
# def load_model():
#     return SentenceTransformer(
#         "all-MiniLM-L6-v2"
#     )


# @st.cache_data
# def load_data():
#     return pd.read_csv(DATA_FILE)


# model = load_model()
# df = load_data()


# # CREATE CAREER EMBEDDINGS

# @st.cache_resource 
# def create_career_embeddings():

#     texts = df["match_text"].tolist()

#     return model.encode(
#         texts,
#         normalize_embeddings=True
#     )


# career_embeddings = create_career_embeddings()


# # RECOMMENDATION FUNCTION

# def recommend_careers(student_text, top_n=3):

#     student_text = student_text.strip()

#     if not student_text:
#         return pd.DataFrame()

#     student_embedding = model.encode(
#         [student_text],
#         normalize_embeddings=True
#     )

#     similarities = cosine_similarity(
#         student_embedding,
#         career_embeddings
#     )[0]

#     results = df.copy()

#     results["similarity"] = similarities

#     results = results.sort_values(
#         by="similarity",
#         ascending=False
#     )

#     return results.head(top_n)


# # HERO SECTION

# st.markdown(
#     """
#     <div class="brand-line">
#         <span class="brand-dot"></span>
#         Career Discovery AI
#     </div>

#     <div class="hero-title">
#         Your interests are clues.<br>
#         <span class="hero-highlight">
#             Follow where they lead.
#         </span>
#     </div>

#     <div class="hero-description">
#         Describe what you enjoy, what you are good at,
#         and how you like to work. Career Discovery AI
#         explores your description and finds career paths
#         with similar interests, skills, and working styles.
#     </div>

#     <div class="feature-row">

#         <span class="feature-pill">
#             ✦ Natural-language discovery
#         </span>

#         <span class="feature-pill">
#             50 career paths
#         </span>

#         <span class="feature-pill">
#             Semantic matching
#         </span>

#         <span class="feature-pill">
#             No quiz required
#         </span>

#     </div>
#     """,
#     unsafe_allow_html=True
# )


# # INPUT SECTION

# left, right = st.columns(
#     [1.55, 0.75],
#     gap="large"
# )


# with left:

#     st.markdown(
#         """
#         <div class="section-label">
#             01 / Tell us about yourself
#         </div>

#         <div class="section-title">
#             What naturally pulls your attention?
#         </div>

#         <div class="section-copy">
#             Write naturally. Mention your interests,
#             strengths, skills, subjects you enjoy,
#             problems you like solving, or the type of
#             work you imagine enjoying.
#         </div>
#         """,
#         unsafe_allow_html=True
#     )


#     student_text = st.text_area(
#         "Student profile",
#         placeholder=(
#             "For example: I enjoy mathematics and "
#             "programming. I like finding patterns in "
#             "data, solving logical problems, and "
#             "explaining useful insights to others..."
#         ),
#         label_visibility="collapsed"
#     )


#     discover_button = st.button(
#         "Discover my career paths  →",
#         use_container_width=True
#     )


# with right:

#     st.markdown(
#         """
#         <div class="section-label">
#             A better description
#         </div>

#         <div class="section-title"
#              style="font-size:1.45rem;">
#             Give the AI useful signals.
#         </div>

#         <div class="detail-box">
#             <strong style="color:#F7F3EA;">
#                 Interests
#             </strong><br>
#             What subjects or activities do you genuinely enjoy?
#         </div>

#         <div class="detail-box">
#             <strong style="color:#F7F3EA;">
#                 Strengths
#             </strong><br>
#             What kinds of problems feel natural for you to solve?
#         </div>

#         <div class="detail-box">
#             <strong style="color:#F7F3EA;">
#                 Work style
#             </strong><br>
#             Do you enjoy creating, analyzing, leading,
#             communicating, researching, or building?
#         </div>
#         """,
#         unsafe_allow_html=True
#     )


# # RECOMMENDATION RESULTS

# if discover_button:

#     if not student_text.strip():

#         st.warning(
#             "Write a little about yourself first. "
#             "A few meaningful sentences will give "
#             "you better career matches."
#         )

#     else:

#         with st.spinner(
#             "Mapping your interests across career paths..."
#         ):

#             recommendations = recommend_careers(
#                 student_text,
#                 top_n=3
#             )


#         st.markdown("<hr>", unsafe_allow_html=True)


#         st.markdown(
#             """
#             <div class="section-label">
#                 02 / Your career constellation
#             </div>

#             <div class="section-title">
#                 Three paths worth exploring
#             </div>

#             <div class="section-copy">
#                 These careers have the strongest semantic
#                 match with the interests, skills, and
#                 preferences expressed in your description.
#             </div>
#             """,
#             unsafe_allow_html=True
#         )


#         result_columns = st.columns(
#             3,
#             gap="medium"
#         )


#         for index, (_, row) in enumerate(
#             recommendations.iterrows()
#         ):

#             rank = index + 1
#             score = row["similarity"] * 100


#             with result_columns[index]:

#                 st.markdown(
#                     f"""
#                     <div class="career-card">

#                         <div class="rank-number">
#                             Match 0{rank}
#                         </div>

#                         <div class="career-name">
#                             {row['career']}
#                         </div>

#                         <div class="career-category">
#                             {row['category']}
#                         </div>

#                         <div class="match-score">
#                             {score:.1f}%
#                         </div>

#                         <div class="match-label">
#                             Semantic match score
#                         </div>

#                     </div>
#                     """,
#                     unsafe_allow_html=True
#                 )


#         # DETAILED CAREER INFORMATION

#         st.markdown("<hr>", unsafe_allow_html=True)


#         st.markdown(
#             """
#             <div class="section-label">
#                 03 / Explore the paths
#             </div>

#             <div class="section-title">
#                 What could each path look like?
#             </div>
#             """,
#             unsafe_allow_html=True
#         )


#         for rank, (_, row) in enumerate(
#             recommendations.iterrows(),
#             start=1
#         ):

#             score = row["similarity"] * 100

#             with st.expander(
#                 f"{rank:02d}  ·  {row['career']}  "
#                 f"—  {score:.1f}% match"
#             ):

#                 st.markdown("#### What this career involves")

#                 st.write(
#                     row["description"]
#                 )


#                 st.markdown("#### Useful skills")

#                 st.write(
#                     row["skills"]
#                 )


#                 st.markdown("#### Interests that connect")

#                 st.write(
#                     row["interests"]
#                 )


#                 st.markdown("#### Typical work style")

#                 st.write(
#                     row["work_style"]
#                 )


#                 st.markdown("#### A simple learning roadmap")

#                 roadmap_steps = [
#                     step.strip()
#                     for step in str(
#                         row["roadmap"]
#                     ).split("→")
#                     if step.strip()
#                 ]


#                 for step_number, step in enumerate(
#                     roadmap_steps,
#                     start=1
#                 ):

#                     st.markdown(
#                         f"**{step_number}.** {step}"
#                     )


#         # DISCLAIMER

#         st.markdown(
#             """
#             <div class="disclaimer">

#                 <strong style="color:#FF9A88;">
#                     Exploration, not prediction.
#                 </strong>

#                 Career Discovery AI compares the meaning
#                 of your description with a curated career
#                 knowledge base. A higher match score means
#                 stronger semantic similarity — it does not
#                 represent the probability that you should
#                 choose or succeed in a particular career.

#                 Use these results as starting points for
#                 research, reflection, and real-world
#                 career guidance.

#             </div>
#             """,
#             unsafe_allow_html=True
#         )


import streamlit as st
import pandas as pd

from pathlib import Path
from textwrap import dedent

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# PAGE CONFIGURATION

st.set_page_config(
    page_title="Career Discovery AI",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# HELPER FOR CLEAN HTML

def html(content):
    """
    Removes unwanted indentation from multiline HTML
    before sending it to Streamlit.
    """
    st.html(dedent(content))


# GLOBAL DESIGN

html("""
<style>

:root {
    --bg: #0D1726;
    --surface: #142033;
    --surface-soft: #18263B;

    --ivory: #F5F0E6;
    --muted: #AAB6C8;

    --mint: #64D9B1;
    --coral: #FF7967;
    --violet: #A99AF4;

    --border: rgba(245, 240, 230, 0.10);
}


/* ---------------------------------------------------------
   APP BACKGROUND
   --------------------------------------------------------- */

.stApp {
    background:
        radial-gradient(
            circle at 8% 12%,
            rgba(100, 217, 177, 0.10),
            transparent 27%
        ),
        radial-gradient(
            circle at 92% 20%,
            rgba(169, 154, 244, 0.08),
            transparent 28%
        ),
        radial-gradient(
            circle at 75% 85%,
            rgba(255, 121, 103, 0.06),
            transparent 26%
        ),
        var(--bg);

    color: var(--ivory);
}


/* ---------------------------------------------------------
   PAGE WIDTH
   --------------------------------------------------------- */

.block-container {
    max-width: 1220px;
    padding-top: 2.4rem;
    padding-bottom: 5rem;
}


/* ---------------------------------------------------------
   STREAMLIT HEADER
   --------------------------------------------------------- */

header[data-testid="stHeader"] {
    background: transparent;
}


/* ---------------------------------------------------------
   BRAND
   --------------------------------------------------------- */

.brand {
    display: flex;
    align-items: center;
    gap: 11px;

    font-size: 0.76rem;
    font-weight: 750;

    letter-spacing: 0.16em;
    text-transform: uppercase;

    color: var(--mint);

    margin-bottom: 2.3rem;
}

.brand-symbol {
    width: 11px;
    height: 11px;

    border-radius: 50%;

    background: var(--coral);

    box-shadow:
        0 0 0 5px rgba(255,121,103,0.08),
        0 0 20px rgba(255,121,103,0.50);
}


/* ---------------------------------------------------------
   HERO
   --------------------------------------------------------- */

.hero {
    max-width: 940px;
    padding-top: 0.5rem;
}

.hero-kicker {
    color: var(--coral);

    font-size: 0.78rem;
    font-weight: 750;

    letter-spacing: 0.16em;
    text-transform: uppercase;

    margin-bottom: 1rem;
}

.hero-title {
    color: var(--ivory);

    font-size: clamp(3.2rem, 6vw, 5.5rem);

    line-height: 0.98;
    letter-spacing: -0.055em;

    font-weight: 800;

    margin: 0;
}

.hero-title .accent {
    color: var(--mint);
}

.hero-text {
    max-width: 760px;

    color: var(--muted);

    font-size: 1.08rem;
    line-height: 1.75;

    margin-top: 1.7rem;
}


/* ---------------------------------------------------------
   SIGNAL PILLS
   --------------------------------------------------------- */

.signal-row {
    display: flex;
    flex-wrap: wrap;

    gap: 10px;

    margin-top: 1.8rem;
    margin-bottom: 4.2rem;
}

.signal-pill {
    display: inline-flex;
    align-items: center;

    padding: 9px 14px;

    border: 1px solid var(--border);
    border-radius: 999px;

    background: rgba(255,255,255,0.035);

    color: #C8D1DF;

    font-size: 0.80rem;
}

.signal-dot {
    width: 6px;
    height: 6px;

    margin-right: 8px;

    border-radius: 50%;

    background: var(--mint);
}


/* ---------------------------------------------------------
   SECTION HEADERS
   --------------------------------------------------------- */

.section-number {
    color: var(--coral);

    font-size: 0.76rem;
    font-weight: 780;

    letter-spacing: 0.15em;
    text-transform: uppercase;

    margin-bottom: 0.6rem;
}

.section-title {
    color: var(--ivory);

    font-size: 2.05rem;
    font-weight: 760;

    line-height: 1.15;
    letter-spacing: -0.035em;

    margin-bottom: 0.75rem;
}

.section-description {
    color: var(--muted);

    font-size: 0.98rem;
    line-height: 1.7;

    max-width: 760px;

    margin-bottom: 1.5rem;
}


/* ---------------------------------------------------------
   INPUT
   --------------------------------------------------------- */

.stTextArea textarea {
    min-height: 205px !important;

    background: rgba(20, 32, 51, 0.88) !important;

    color: var(--ivory) !important;

    border:
        1px solid
        rgba(100, 217, 177, 0.20) !important;

    border-radius: 20px !important;

    padding: 20px !important;

    font-size: 1rem !important;
    line-height: 1.65 !important;

    box-shadow:
        inset 0 1px 0 rgba(255,255,255,0.025),
        0 18px 45px rgba(0,0,0,0.12);
}

.stTextArea textarea:focus {
    border:
        1px solid
        rgba(100,217,177,0.75) !important;

    box-shadow:
        0 0 0 4px
        rgba(100,217,177,0.08) !important;
}

.stTextArea textarea::placeholder {
    color: #718095 !important;
}


/* ---------------------------------------------------------
   BUTTON
   --------------------------------------------------------- */

.stButton > button {
    min-height: 3.2rem;

    width: 100%;

    border: 0;

    border-radius: 14px;

    background:
        linear-gradient(
            110deg,
            #64D9B1,
            #7BE2BD
        );

    color: #08141F;

    font-weight: 800;

    transition:
        transform 0.18s ease,
        box-shadow 0.18s ease;
}

.stButton > button:hover {
    transform: translateY(-2px);

    box-shadow:
        0 12px 30px
        rgba(100,217,177,0.18);

    color: #08141F;
}


/* ---------------------------------------------------------
   GUIDANCE PANEL
   --------------------------------------------------------- */

.guide-panel {
    padding: 1.35rem;

    border:
        1px solid
        rgba(169,154,244,0.13);

    border-radius: 22px;

    background:
        linear-gradient(
            145deg,
            rgba(169,154,244,0.06),
            rgba(255,255,255,0.02)
        );
}

.guide-title {
    color: var(--ivory);

    font-size: 1.3rem;
    font-weight: 720;

    margin-bottom: 1.1rem;
}

.guide-item {
    padding: 0.9rem 0;

    border-bottom:
        1px solid
        rgba(245,240,230,0.075);
}

.guide-item:last-child {
    border-bottom: 0;
}

.guide-label {
    color: var(--mint);

    font-size: 0.8rem;
    font-weight: 720;

    margin-bottom: 0.3rem;
}

.guide-copy {
    color: var(--muted);

    font-size: 0.88rem;
    line-height: 1.55;
}


/* ---------------------------------------------------------
   DIVIDER
   --------------------------------------------------------- */

.soft-divider {
    height: 1px;

    margin: 3.5rem 0;

    background:
        linear-gradient(
            to right,
            transparent,
            rgba(245,240,230,0.10),
            transparent
        );
}


/* ---------------------------------------------------------
   RESULT CARDS
   --------------------------------------------------------- */

.career-card {
    position: relative;

    min-height: 250px;

    overflow: hidden;

    padding: 1.5rem;

    border:
        1px solid
        rgba(245,240,230,0.11);

    border-radius: 24px;

    background:
        linear-gradient(
            150deg,
            rgba(255,255,255,0.052),
            rgba(255,255,255,0.018)
        );

    box-shadow:
        0 20px 45px
        rgba(0,0,0,0.14);
}

.career-card::after {
    content: "";

    position: absolute;

    width: 110px;
    height: 110px;

    top: -50px;
    right: -45px;

    border-radius: 50%;

    background:
        rgba(100,217,177,0.07);
}

.career-rank {
    color: var(--coral);

    font-size: 0.72rem;
    font-weight: 800;

    letter-spacing: 0.13em;
    text-transform: uppercase;
}

.career-title {
    color: var(--ivory);

    font-size: 1.55rem;
    font-weight: 760;

    line-height: 1.15;

    margin-top: 0.8rem;
    margin-bottom: 0.8rem;
}

.career-tag {
    display: inline-block;

    color: var(--mint);

    font-size: 0.73rem;
    font-weight: 650;

    padding: 6px 9px;

    border-radius: 8px;

    background:
        rgba(100,217,177,0.075);

    border:
        1px solid
        rgba(100,217,177,0.12);
}

.score-wrap {
    margin-top: 2rem;
}

.score-number {
    color: var(--ivory);

    font-size: 2.25rem;
    font-weight: 820;

    letter-spacing: -0.045em;
}

.score-label {
    color: #8390A3;

    font-size: 0.68rem;
    font-weight: 650;

    letter-spacing: 0.11em;
    text-transform: uppercase;
}


/* ---------------------------------------------------------
   DISCLAIMER
   --------------------------------------------------------- */

.disclaimer {
    margin-top: 3rem;

    padding: 1.35rem 1.5rem;

    border:
        1px solid
        rgba(255,121,103,0.20);

    border-radius: 18px;

    background:
        linear-gradient(
            120deg,
            rgba(255,121,103,0.055),
            rgba(169,154,244,0.025)
        );
}

.disclaimer-title {
    color: #FF9C8C;

    font-size: 0.83rem;
    font-weight: 800;

    letter-spacing: 0.05em;

    margin-bottom: 0.5rem;
}

.disclaimer-copy {
    color: var(--muted);

    line-height: 1.65;

    font-size: 0.87rem;
}


/* ---------------------------------------------------------
   ROADMAP STYLING
   --------------------------------------------------------- */

.road-step {
    display: flex;

    gap: 12px;

    margin-bottom: 0.7rem;

    align-items: flex-start;
}

.road-number {
    min-width: 28px;
    height: 28px;

    display: flex;
    align-items: center;
    justify-content: center;

    border-radius: 50%;

    color: #0D1726;

    background: var(--mint);

    font-size: 0.72rem;
    font-weight: 800;
}

.road-copy {
    padding-top: 3px;

    color: #D3D9E2;

    line-height: 1.5;
}


/* ---------------------------------------------------------
   MOBILE
   --------------------------------------------------------- */

@media (max-width: 800px) {

    .block-container {
        padding-top: 1.4rem;
    }

    .hero-title {
        font-size: 3.3rem;
    }

    .hero-text {
        font-size: 1rem;
    }

    .signal-row {
        margin-bottom: 3rem;
    }

}

</style>
""")


# PATHS

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "careers_prepared.csv"


# LOAD DATA + MODEL

@st.cache_data
def load_data():
    return pd.read_csv(DATA_FILE)


@st.cache_resource
def load_model():
    return SentenceTransformer(
        "all-MiniLM-L6-v2"
    )


df = load_data()
model = load_model()


# CAREER EMBEDDINGS

@st.cache_resource
def create_career_embeddings():

    match_texts = df["match_text"].tolist()

    return model.encode(
        match_texts,
        normalize_embeddings=True
    )


career_embeddings = create_career_embeddings()


# RECOMMENDER

def recommend_careers(student_text, top_n=3):

    student_text = student_text.strip()

    if not student_text:
        return pd.DataFrame()

    student_embedding = model.encode(
        [student_text],
        normalize_embeddings=True
    )

    similarities = cosine_similarity(
        student_embedding,
        career_embeddings
    )[0]

    results = df.copy()

    results["similarity"] = similarities

    results = results.sort_values(
        "similarity",
        ascending=False
    )

    return results.head(top_n)


# HERO

html("""
<div class="brand">
    <span class="brand-symbol"></span>
    Career Discovery AI
</div>

<div class="hero">

    <div class="hero-kicker">
        Explore possibilities, not labels
    </div>

    <h1 class="hero-title">
        Turn what you enjoy into
        <span class="accent">directions worth exploring.</span>
    </h1>

    <div class="hero-text">
        Tell us what interests you, what kinds of problems
        you enjoy solving, and how you like to work.
        Your description is compared with a curated map of
        career profiles to surface paths that share similar signals.
    </div>

</div>

<div class="signal-row">

    <span class="signal-pill">
        <span class="signal-dot"></span>
        Natural-language input
    </span>

    <span class="signal-pill">
        <span class="signal-dot"></span>
        50 career paths
    </span>

    <span class="signal-pill">
        <span class="signal-dot"></span>
        Semantic similarity
    </span>

    <span class="signal-pill">
        <span class="signal-dot"></span>
        Exploration first
    </span>

</div>
""")


# INPUT SECTION

left, right = st.columns(
    [1.5, 0.72],
    gap="large"
)


with left:

    html("""
    <div class="section-number">
        01 / Your signals
    </div>

    <div class="section-title">
        Describe yourself without choosing from boxes.
    </div>

    <div class="section-description">
        Write naturally. You can mention subjects you enjoy,
        strengths, hobbies, skills, problems you like solving,
        or the type of environment in which you imagine doing
        your best work.
    </div>
    """)

    student_text = st.text_area(
        "Student profile",
        placeholder=(
            "Example: I enjoy mathematics and programming. "
            "I like finding patterns in data, solving logical "
            "problems, and explaining useful insights to people..."
        ),
        label_visibility="collapsed"
    )

    discover_button = st.button(
        "Map my possible directions  →",
        use_container_width=True
    )


with right:

    html("""
    <div class="section-number">
        Better input → better exploration
    </div>

    <div class="guide-panel">

        <div class="guide-title">
            What could you mention?
        </div>

        <div class="guide-item">
            <div class="guide-label">
                01 · Interests
            </div>

            <div class="guide-copy">
                Subjects, activities, topics, or problems
                that naturally hold your attention.
            </div>
        </div>

        <div class="guide-item">
            <div class="guide-label">
                02 · Strengths
            </div>

            <div class="guide-copy">
                Things you are good at or skills you
                would genuinely like to improve.
            </div>
        </div>

        <div class="guide-item">
            <div class="guide-label">
                03 · Work style
            </div>

            <div class="guide-copy">
                Creating, analyzing, leading, building,
                researching, communicating, or helping.
            </div>
        </div>

    </div>
    """)


# RESULTS

if discover_button:

    if not student_text.strip():

        st.warning(
            "Please describe yourself in a few sentences "
            "before exploring career paths."
        )

    else:

        with st.spinner(
            "Mapping your description across career profiles..."
        ):

            recommendations = recommend_careers(
                student_text,
                top_n=3
            )


        html("""
        <div class="soft-divider"></div>

        <div class="section-number">
            02 / Career constellation
        </div>

        <div class="section-title">
            Three directions with the strongest signal.
        </div>

        <div class="section-description">
            These are not predictions. They are the career
            profiles whose meaning is most similar to the
            interests and preferences expressed in your description.
        </div>
        """)


        result_columns = st.columns(
            3,
            gap="medium"
        )


        for index, (_, row) in enumerate(
            recommendations.iterrows()
        ):

            rank = index + 1
            score = row["similarity"] * 100

            card_html = f"""
            <div class="career-card">

                <div class="career-rank">
                    Direction {rank:02d}
                </div>

                <div class="career-title">
                    {row['career']}
                </div>

                <div class="career-tag">
                    {row['category']}
                </div>

                <div class="score-wrap">

                    <div class="score-number">
                        {score:.1f}%
                    </div>

                    <div class="score-label">
                        Semantic match score
                    </div>

                </div>

            </div>
            """

            with result_columns[index]:
                html(card_html)


        
        # DETAILS

        html("""
        <div class="soft-divider"></div>

        <div class="section-number">
            03 / Explore the paths
        </div>

        <div class="section-title">
            Look beyond the career title.
        </div>

        <div class="section-description">
            Open each path to see what the career involves,
            relevant skills and interests, working style,
            and a simple learning direction.
        </div>
        """)


        for rank, (_, row) in enumerate(
            recommendations.iterrows(),
            start=1
        ):

            score = row["similarity"] * 100

            expander_title = (
                f"{rank:02d} · {row['career']} "
                f"— {score:.1f}% match"
            )

            with st.expander(expander_title):

                st.markdown(
                    "#### What this career involves"
                )

                st.write(
                    row["description"]
                )


                st.markdown(
                    "#### Skills you may build"
                )

                skills = [
                    skill.strip()
                    for skill in str(
                        row["skills"]
                    ).split(";")
                    if skill.strip()
                ]

                st.write(
                    " · ".join(skills)
                )


                st.markdown(
                    "#### Interests that connect"
                )

                interests = [
                    item.strip()
                    for item in str(
                        row["interests"]
                    ).split(";")
                    if item.strip()
                ]

                st.write(
                    " · ".join(interests)
                )


                st.markdown(
                    "#### Typical work style"
                )

                st.write(
                    row["work_style"]
                )


                st.markdown(
                    "#### Starter learning path"
                )

                roadmap_steps = [
                    item.strip()
                    for item in str(
                        row["roadmap"]
                    ).split("→")
                    if item.strip()
                ]


                for number, step in enumerate(
                    roadmap_steps,
                    start=1
                ):

                    html(
                        f"""
                        <div class="road-step">

                            <div class="road-number">
                                {number}
                            </div>

                            <div class="road-copy">
                                {step}
                            </div>

                        </div>
                        """
                    )


        # DISCLAIMER

        html("""
        <div class="disclaimer">

            <div class="disclaimer-title">
                Exploration, not prediction.
            </div>

            <div class="disclaimer-copy">
                Career Discovery AI compares the semantic meaning
                of your description with a curated career knowledge
                base. The displayed percentage is a similarity score,
                not the probability that you should choose or succeed
                in a particular career.
                <br><br>
                Treat the results as starting points for research,
                reflection, conversations, and real-world career guidance.
            </div>

        </div>
        """)