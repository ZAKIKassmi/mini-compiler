import random
import json

class PoemGenerator:
    def __init__(self):
        """Initialize the PoemGenerator with poems data."""
        try:
            # Load poems data from the JSON file
            with open(r"./data/poems.json", "r", encoding="utf-8") as file:
                self.poems = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError("The file 'data/poems.json' was not found. Please verify the path.")
        except json.JSONDecodeError:
            raise ValueError("The file 'data/poems.json' is not a valid JSON file.")

    def generate_poem(self, theme):
        """Generate a poem based on the given theme."""
        if theme in self.poems:
            # Randomly select a poem under the given theme
            return random.choice(self.poems[theme])
        else:
            return "Désolé, aucun poème trouvé pour ce thème."