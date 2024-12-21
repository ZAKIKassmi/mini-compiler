import json

class Translation:
    def __init__(self, english_file="./data/translation_english.json", frensh_file="./data/translation_french.json"):
        self.english_file = english_file
        self.frensh_file = frensh_file
        self.english_translations = self._load_translations(self.english_file)
        self.frensh_translations = self._load_translations(self.frensh_file)

    def _load_translations(self, file_path):
        """Load translations from a JSON file."""
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {file_path} was not found.")
        except json.JSONDecodeError:
            raise ValueError(f"The file {file_path} is not a valid JSON file.")

    def translate_english(self, bayt):
        """Translate a bayt to English."""
        translation = self.english_translations.get(bayt)
        if translation:
            return translation
        else:
            return "No English translation found."

    def translate_frensh(self, bayt):
        """Translate a bayt to French."""
        translation = self.frensh_translations.get(bayt)
        if translation:
            return translation
        else:
            return "No French translation found."