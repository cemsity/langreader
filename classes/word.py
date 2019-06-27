class Word():
    """
    The template for individual words. E.G. go, goes, went will all have a
    unique entry with a reference to their Headword/Lemma (GO), to form the
    lexeme.

    Current implemtation goals state that the differntiation of Lemma based on
    parts of speech (PoS) will not noted. Thus, RUN[n] and RUN[v] will be a part
    of the same lexeme.

    self.word :- the expressed form in the text. Also the primary key for db
                look up
    self.headword :- Currently string of the Headword will be a reference to the
                Headword
    self.pos :- part of speach in the the text
    self.level :- int (currently 0-10) the level of familiarty according to
                spaced repitition(not yet implemented) also used for color
                coding. 0 = not yet learned
    MORE TO COME

    METHODS:
    ADD AS ADDED
    Class Methods
    new_word(word) : cls -> makes a new word
    """
    def __init__(self, word, headword, pos, level):
        self.word = word
        self.headword = headword
        self.pos = pos
        self.level = level


    @classmethod
    def new_word(cls, word):
        return cls(word, None, None, 0)


    def to_dict(self):
        return {
            'word': self.word,
            'headword': self.headword,
            'pos': self.pos,
            'level': self.level
        }

    def __str__(self):
        return self.to_dict()