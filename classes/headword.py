import re

class Headword():
    """
    The representation of the headword/lexeme. This should be inputed by the user
    as the dictionary form / lemma of the word. EG va, vais, allez et al. should be placed
    under the headword aller, which this does in contain a word
    """
    def __init__(self, lemma, lexels, pos):
        self.lemma = lemma
        self.lexels = {}
        self.part_of_speech = pos

    def add_lexel(word):
        self.lexels.append(word)
        return 0



    @classmethod
    def new_headword(cls, new_lemma, new_pos):
        return cls(new_lemma, None, new_pos)

    def __str__(self):
        return f"{self.lemma}, {self.part_of_speech}, {len(self.lexels)}"



