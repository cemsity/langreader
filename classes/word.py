class Word():
    """
    Prototype
    The template for individual words. E.G. go, goes, went will all have a
    unique entry with a reference to their Headword/Lemma (GO), to form the
    lexeme.

    Current implemtation goals state that the differntiation of Lemma based on
    parts of speech (PoS) will not noted. Thus, RUN[n] and RUN[v] will be a part
    of the same lexeme.

    self.word :- the expressed form in the text. Also the primary key for db
                look upHe
    self.headword :- Currently string of the Headword will be a reference to the
                Headword
    self.pos :- part of speach in the the text
    self.level :- int (currently 0-10) the level of familiarty according to
                spaced repitition(not yet implemented) also used for color
                coding. 0 = not yet learned
    self.gram_cat :- list of grammatical categories this word
                belongs to. ( dont know how i want to implement at this time
                esp. because of syncretism ; may be list of lists?)

    METHODS:
    ADD AS ADDED
    Class Methods
    new_word(word) : cls -> makes a new word


    """
    def __init__(self, word, headword, pos, level, gram_cat):
        self.word = word
        self.headword = headword
        self.part_of_speech = pos
        self.level = level
        self.gram_cat = gram_cat


    def add_inflection(self, inflection):
        self.inflection.append(inflection)


    def remove_inflection(self, inflection):
        self.inflection.remove(inflection)


    def to_dict(self):
        return {
            'word': self.word,
            'headword': self.headword,
            'part_of_speech': self.part_of_speech,
            'level': self.level,
            'inflection': self.inflection
        }

    def update(self, tuple):
        prop = tuple[0]
        value = tuple[1]
        if prop == 'headword':
            self.headword = value
        elif prop == 'pos':
            self.pos = value
        elif prop == 'level':
            self.level = int(value)
        elif prop == 'gram_cat':
            self.gram_cat.append(value)
        else:
            return False
        return True


    def __str__(self):
        return f"{self.word}, {self.headword}, {self.pos}, {self.level}"


    @classmethod
    def new_word(cls, word):
        return cls(word, None, None, 0, [])