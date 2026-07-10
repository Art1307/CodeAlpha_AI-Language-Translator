import streamlit as st
from styles import load_css

from translator import Translator
from tts import TextToSpeech
from utils import (
    copy_to_clipboard,
    swap_languages,
    clear_translation,
    initialize_session,
)

# -----------------------------
# PAGE CONFIGURATION
# -----------------------------

st.set_page_config(page_title="AI Language Translator", page_icon="🌍", layout="wide")

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

st.markdown(load_css(), unsafe_allow_html=True)

# -----------------------------
# HEADER
# -----------------------------

st.markdown(
    """
    <div class='main-title'>
        🌍 AI Language Translator
    </div>

    <div class='subtitle'>
        Translate text between 100+ languages using Artificial Intelligence
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    "<div class='subtitle'>Translate text instantly using Artificial Intelligence</div>",
    unsafe_allow_html=True,
)

st.divider()
# -----------------------------
# SIDEBAR
# -----------------------------

with st.sidebar:

    st.title("🌍 AI Language Translator")

    st.markdown("---")

    st.subheader("📌 About")

    st.write("""
Translate text instantly between multiple languages using
Google Translate AI.

This project is developed as part of the
**CodeAlpha Artificial Intelligence Internship**.
""")

    st.markdown("---")

    st.subheader("✨ Features")

    st.success("✔ AI Translation")
    st.success("✔ 100+ Languages")
    st.success("✔ Copy Translation")

    st.info("🔜 Text-to-Speech")
    st.info("🔜 Translation History")
    st.info("🔜 Swap Languages")

    st.markdown("---")

    st.subheader("👨‍💻 Developer")

    st.write("**Anurup Tiwari**")

    st.caption("CodeAlpha AI Intern")
# -----------------------------
# LANGUAGE SELECTION
# -----------------------------

col1, col2 = st.columns(2)

with col1:
    source_language = st.selectbox("Source Language", languages, index=0)

with col2:
    target_language = st.selectbox(
        "Target Language", languages, index=languages.index("English")
    )

# -----------------------------
# INPUT TEXT
# -----------------------------

input_text = st.text_area(
    "Enter Text", height=180, placeholder="Type something here..."
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
                input_text, source_language, target_language
            )

            st.session_state["translated_text"] = translated_text

            st.success("Translation completed successfully!")

            st.text_area("Translated Text", translated_text, height=180)

            if st.button("📋 Copy Translation"):

                if copy_to_clipboard(translated_text):
                    st.success("Translation copied to clipboard!")
                else:
                    st.error("Unable to copy the translation.")

        except Exception as e:
            st.error(f"Error: {e}")
