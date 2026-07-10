def load_css():
    return """
<style>

/* ==========================================================
   GOOGLE FONT
========================================================== */

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

/* ==========================================================
   MAIN APP
========================================================== */

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp{
    background: linear-gradient(
        135deg,
        #0F172A 0%,
        #1E293B 45%,
        #312E81 100%
    );
    background-attachment: fixed;
}

/* ==========================================================
   MAIN CONTAINER
========================================================== */

.block-container{
    max-width:1200px;
    padding-top:2rem;
    padding-bottom:2rem;
}

/* ==========================================================
   HERO TITLE
========================================================== */

.main-title{

    font-size:58px;

    font-weight:800;

    text-align:center;

    color:white;

    letter-spacing:1px;

    margin-bottom:8px;

    text-shadow:0px 0px 30px rgba(255,255,255,.15);

}

.subtitle{

    text-align:center;

    color:#E5E7EB;

    font-size:18px;

    margin-bottom:35px;

    line-height:1.7;

}

/* ==========================================================
   GLASS CARD
========================================================== */

.glass-card{

    background:rgba(255,255,255,.08);

    backdrop-filter:blur(20px);

    -webkit-backdrop-filter:blur(20px);

    border-radius:24px;

    padding:28px;

    border:1px solid rgba(255,255,255,.15);

    box-shadow:
        0 10px 35px rgba(0,0,0,.25);

    margin-bottom:25px;

}

/* ==========================================================
   SIDEBAR
========================================================== */

section[data-testid="stSidebar"]{

    background:rgba(255,255,255,.08);

    backdrop-filter:blur(20px);

    border-right:1px solid rgba(255,255,255,.15);

}

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3{

    color:white;

}

section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] span{

    color:#E5E7EB;

}

/* ==========================================================
   BUTTONS
========================================================== */

.stButton > button{

    width:100%;

    height:50px;

    border:none;

    border-radius:14px;

    font-size:17px;

    font-weight:700;

    color:white;

    background:
        linear-gradient(
            135deg,
            #4F46E5,
            #2563EB
        );

    transition:.25s ease;

}

.stButton > button:hover{

    transform:translateY(-2px);

    box-shadow:
        0 10px 30px rgba(0,0,0,.30);

}

/* ==========================================================
   TEXT AREA
========================================================== */

textarea{

    font-size:17px !important;

}

/* ==========================================================
   INPUTS
========================================================== */

.stSelectbox{

    border-radius:14px;

}

/* ==========================================================
   METRICS
========================================================== */

[data-testid="stMetric"]{

    background:rgba(255,255,255,.08);

    border:1px solid rgba(255,255,255,.15);

    border-radius:18px;

    padding:18px;

}

/* ==========================================================
   EXPANDER
========================================================== */

.streamlit-expanderHeader{

    font-weight:600;

}

/* ==========================================================
   DIVIDER
========================================================== */

hr{

    margin-top:20px;

    margin-bottom:20px;

}

/* ==========================================================
   SCROLLBAR
========================================================== */

::-webkit-scrollbar{

    width:8px;

}

::-webkit-scrollbar-thumb{

    background:#6366F1;

    border-radius:20px;

}

::-webkit-scrollbar-track{

    background:transparent;

}

/* ==========================================================
   FOOTER
========================================================== */

.footer{

    text-align:center;

    color:#CBD5E1;

    font-size:15px;

    padding:25px;

}

</style>
"""
