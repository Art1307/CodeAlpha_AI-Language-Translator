import streamlit as st

from translator import Translator
from tts import TextToSpeech
from utils import (
    copy_to_clipboard,
    swap_languages,
    clear_translation,
    initialize_session
)

# -----------------------------
# PAGE CONFIGURATION
# -----------------------------

st.set_page_config(
    page_title="AI Language Translator",
    page_icon="🌍",
    layout="wide"
)

# -----------------------------
# SESSION STATE
# -----------------------------

initialize_session()

translator = Translator()
tts = TextToSpeech()

languages = translator.get_languages()

# -----------------------------
# CUSTOM CSS
# -----------------------------

st.markdown("""
<style>

.main-title{
    text-align:center;
    font-size:42px;
    font-weight:bold;
    color:#4F8BF9;
}

.subtitle{
    text-align:center;
    font-size:18px;
    color:gray;
    margin-bottom:30px;
}

.stButton>button{
    width:100%;
    border-radius:12px;
    font-size:17px;
    font-weight:bold;
}

textarea{
    font-size:17px !important;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# HEADER
# -----------------------------

st.markdown(
    "<div class='main-title'>🌍 AI Language Translator</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Translate text instantly using Artificial Intelligence</div>",
    unsafe_allow_html=True
)

st.divider()

# -----------------------------
# LANGUAGE SELECTION
# -----------------------------

col1, col2 = st.columns(2)

with col1:
    source_language = st.selectbox(
        "Source Language",
        languages,
        index=0
    )

with col2:
    target_language = st.selectbox(
        "Target Language",
        languages,
        index=languages.index("English")
    )

# -----------------------------
# INPUT TEXT
# -----------------------------

input_text = st.text_area(
    "Enter Text",
    height=180,
    placeholder="Type something here..."
)
# -----------------------------
# TRANSLATE BUTTON
# -----------------------------

if st.button("🚀 Translate", type="primary"):

    if not input_text.strip():
        st.warning("Please enter some text to translate.")

    else:
        try:

            translated_text = translator.translate_text(
                input_text,
                source_language,
                target_language
            )

            st.success("Translation completed successfully!")

            st.text_area(
                "Translated Text",
                translated_text,
                height=180
            )

        except Exception as e:
            st.error(f"Error: {e}")