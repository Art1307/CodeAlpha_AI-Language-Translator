from deep_translator import GoogleTranslator


class Translator:
    def __init__(self):
        self.languages = GoogleTranslator().get_supported_languages(as_dict=True)

    def get_languages(self):
        language_list = ["Auto Detect"]
        language_list.extend(
            sorted([language.title() for language in self.languages.keys()])
        )
        return language_list

    def translate_text(self, text, source_language, target_language):
        if not text.strip():
            raise ValueError("Please enter some text to translate.")

        if source_language == target_language:
            raise ValueError("Source and Target languages cannot be the same.")

        source = (
            "auto"
            if source_language == "Auto Detect"
            else self.languages[source_language.lower()]
        )
        target = self.languages[target_language.lower()]

        translator = GoogleTranslator(source=source, target=target)

        translated_text = translator.translate(text)

        return translated_text
