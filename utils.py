import pyperclip
import streamlit as st


def copy_to_clipboard(text):
    """
    Copy text to the clipboard.
    """
    try:
        pyperclip.copy(text)
        return True
    except Exception:
        return False


def swap_languages(source, target):
    """
    Swap source and target languages.
    """
    return target, source


def clear_translation():
    """
    Clear stored text from Streamlit session.
    """
    st.session_state["input_text"] = ""
    st.session_state["translated_text"] = ""


def initialize_session():
    """
    Initialize Streamlit session variables.
    """

    defaults = {
        "input_text": "",
        "translated_text": "",
        "source_language": "Auto Detect",
        "target_language": "English"
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value