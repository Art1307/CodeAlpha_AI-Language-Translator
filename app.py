import streamlit as st

from constants import (
    APP_TITLE,
    APP_ICON,
    APP_SUBTITLE,
    ABOUT_TEXT,
    FEATURES,
    DEFAULT_SOURCE_LANGUAGE,
    DEFAULT_TARGET_LANGUAGE,
)

from styles import load_css
from translator import Translator
from tts import TextToSpeech
from utils import (
    copy_to_clipboard,
    swap_languages,
    initialize_session,
)

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title=APP_TITLE,
    page_icon=APP_ICON,
    layout="wide",
)

# ==========================================================
# INITIALIZE
# ==========================================================

initialize_session()

translator = Translator()
tts = TextToSpeech()

languages = translator.get_languages()

# ==========================================================
# LOAD CSS
# ==========================================================

st.markdown(load_css(), unsafe_allow_html=True)

# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.title(f"{APP_ICON} {APP_TITLE}")

    st.divider()

    st.subheader("📌 About")

    st.write(ABOUT_TEXT)

    st.divider()

    st.subheader("✨ Features")

    for feature in FEATURES:
        st.success(f"✔ {feature}")

    st.divider()

    st.subheader("📊 Session")

    total = len(st.session_state["history"])

    st.metric("Translations", total)

    st.divider()

    st.subheader("👨‍💻 Developer")

    st.write("**Anurup Tiwari**")

    st.caption("CodeAlpha AI Internship")

# ==========================================================
# HEADER
# ==========================================================

st.markdown(
    f"""
<div class="main-title">
{APP_ICON} {APP_TITLE}
</div>

<div class="subtitle">
{APP_SUBTITLE}
</div>
""",
    unsafe_allow_html=True,
)

st.divider()

# ==========================================================
# LANGUAGE SELECTION
# ==========================================================

left, middle, right = st.columns([5, 1, 5])

with left:

    source_language = st.selectbox(
        "🌐 Source Language",
        languages,
        index=languages.index(st.session_state["source_language"]),
    )

with middle:

    st.write("")

    st.write("")

    if st.button("🔄"):

        if source_language != DEFAULT_SOURCE_LANGUAGE:

            source_language, target_language = swap_languages(
                source_language,
                st.session_state["target_language"],
            )

            st.session_state["source_language"] = source_language
            st.session_state["target_language"] = target_language

            st.rerun()

with right:

    target_language = st.selectbox(
        "🎯 Target Language",
        languages,
        index=languages.index(st.session_state["target_language"]),
    )

# ==========================================================
# INPUT
# ==========================================================

input_text = st.text_area(
    "📝 Enter Text",
    value=st.session_state["input_text"],
    height=220,
    placeholder="Type something to translate...",
)

st.divider()
# ==========================================================
# TRANSLATION
# ==========================================================

translate_col1, translate_col2, translate_col3 = st.columns([2, 4, 2])

with translate_col2:

    translate_clicked = st.button(
        "🚀 Translate",
        type="primary",
        use_container_width=True,
    )

if translate_clicked:

    if not input_text.strip():

        st.warning("Please enter some text.")

    else:

        try:

            with st.spinner("Translating..."):

                translated_text = translator.translate_text(
                    input_text,
                    source_language,
                    target_language,
                )

            # --------------------------
            # Save session
            # --------------------------

            st.session_state["input_text"] = input_text

            st.session_state["translated_text"] = translated_text

            st.session_state["source_language"] = source_language

            st.session_state["target_language"] = target_language

            # --------------------------
            # Save history
            # --------------------------

            st.session_state["history"].append(
                {
                    "source": source_language,
                    "target": target_language,
                    "input": input_text,
                    "output": translated_text,
                }
            )

        except Exception as e:

            st.error(str(e))

# ==========================================================
# OUTPUT
# ==========================================================

if st.session_state["translated_text"]:

    st.success("Translation completed successfully.")

    st.text_area(
        "📄 Translated Text",
        value=st.session_state["translated_text"],
        height=220,
    )
# ==========================================================
# TOOLS
# ==========================================================

st.write("")

tool_col1, tool_col2, tool_col3 = st.columns(3)

# ----------------------------------------------------------
# COPY
# ----------------------------------------------------------

with tool_col1:

    if st.button(
        "📋 Copy",
        use_container_width=True,
        disabled=not st.session_state["translated_text"],
    ):

        if copy_to_clipboard(st.session_state["translated_text"]):

            st.success("Copied to clipboard!")

        else:

            st.error("Unable to copy.")

# ----------------------------------------------------------
# TEXT TO SPEECH
# ----------------------------------------------------------

with tool_col2:

    if st.button(
        "🔊 Listen",
        use_container_width=True,
        disabled=not st.session_state["translated_text"],
    ):

        try:

            with st.spinner("Generating audio..."):

                audio_path = tts.generate_audio(
                    st.session_state["translated_text"],
                    st.session_state["target_language"],
                )

                with open(audio_path, "rb") as audio_file:

                    audio_bytes = audio_file.read()

                st.audio(audio_bytes)

                tts.delete_audio(audio_path)

        except Exception as e:

            st.error(f"Audio Error: {e}")

# ----------------------------------------------------------
# DOWNLOAD
# ----------------------------------------------------------

with tool_col3:

    st.download_button(
        "📥 Download",
        st.session_state["translated_text"],
        file_name="translation.txt",
        mime="text/plain",
        use_container_width=True,
        disabled=not st.session_state["translated_text"],
    )
