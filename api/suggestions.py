import difflib

class Suggestion:
    def __init__(self, dictionary_file=r"./data/arabic_dictionary.txt"):
        self.dictionary_file = dictionary_file
        self.bayts = self._load_bayts()
    
    def _load_bayts(self):
        """Load bayts (lines) from the dictionary file."""
        try:
            with open(self.dictionary_file, "r", encoding="utf-8") as file:
                return [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {self.dictionary_file} was not found.")
    
    def suggest(self, bayt):
        """
        Suggest the closest bayt from the dictionary and its accuracy.

        :param bayt: The input bayt (line) to compare.
        :return: A tuple of the closest bayt and its similarity score (accuracy).
        """
        if not self.bayts:
            raise ValueError("The dictionary is empty or not loaded properly.")

        closest_match = difflib.get_close_matches(bayt, self.bayts, n=1, cutoff=0)
        if closest_match:
            closest_bayt = closest_match[0]
            accuracy = difflib.SequenceMatcher(None, bayt, closest_bayt).ratio()
            return {
                "message": closest_bayt,
                "accuracy": accuracy,
                "is_found": True
            }
        else:
            return {
                "message": "no close match found",
                "accuracy": 0,
                "is_found": False
            }