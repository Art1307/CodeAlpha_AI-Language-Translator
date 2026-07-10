from gtts import gTTS
import tempfile
import os


class TextToSpeech:

    def __init__(self):
        self.language_map = {
            "English": "en",
            "Hindi": "hi",
            "French": "fr",
            "German": "de",
            "Spanish": "es",
            "Italian": "it",
            "Japanese": "ja",
            "Korean": "ko",
            "Chinese (Simplified)": "zh-CN",
            "Arabic": "ar",
            "Russian": "ru",
            "Portuguese": "pt",
            "Bengali": "bn",
            "Gujarati": "gu",
            "Tamil": "ta",
            "Telugu": "te",
            "Marathi": "mr",
            "Punjabi": "pa",
            "Urdu": "ur",
        }

    def generate_audio(self, text, language):

        if not text.strip():
            raise ValueError("No text available for speech.")

        lang = self.language_map.get(language, "en")

        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
            tts = gTTS(text=text, lang=lang, slow=False)
            tts.save(temp_file.name)

            return temp_file.name

    def delete_audio(self, filepath):

        if filepath and os.path.exists(filepath):
            os.remove(filepath)
