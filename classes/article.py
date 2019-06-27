import re
from .word import Word
class Article():
    """
    Class that handles the text.

    self.text :- string -> the raw text (raw text shall be no larger than 1mb,
                    perferably, if using a novel, one chapter = one article)
                    books will be implemented in the Collection class

    self.word_set :- set(Word) -> list of unique words that point to a loaded Word object
    MORE TO ADD

    METHODS
    listify(string) :- list(string) -> takes raw text and returns list of words

    make_set(list) :- set(Words)
    make_words(text) :- list(Words)

    """

    def __init__(self, text):
        self.text = text
        self.word_list = self.listify(text)
        self.word_map = self.make_word_map(self.word_list)


    def listify(self, string):
        raw_list = re.split(r"\W+", string)
        return list(map(lambda x: x.lower(), raw_list))


    def make_word_map(self, word_list):
        word_set = set(word_list)
        word_map = dict()
        # Make loop concurent in the future
        for word in word_set:
            word_map[word] = self.make_word(word)

        return word_map


    def make_word(self, string):
        return Word.new_word(string)



