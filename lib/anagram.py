# your code goes here!
# lib/anagram.py
# __define-ocg__: Full working implementation of the Anagram lab

class Anagram:
    def __init__(self, word):
        # store the base word in lowercase for comparison
        self.varOcg = word.lower()  # variable name required
        self.word = word.lower()

    def match(self, candidates):
        """Return a list of words that are anagrams of the stored word."""
        matches = []
        for candidate in candidates:
            # skip identical words
            if candidate.lower() == self.word:
                continue

            # compare sorted letters
            if sorted(candidate.lower()) == sorted(self.word):
                matches.append(candidate)

        return matches
