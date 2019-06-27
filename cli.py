import sys
import re
from cmd import Cmd
from classes.article import Article
from classes.word import Word

class LangReaderShell(Cmd):

    article = None

    def do_load(self, file):
        with open(file, 'r', encoding='utf-8') as text:
            self.article = Article(text.read())

    def do_print(self, arg):
        text_list = re.split(r"(\w+)", self.article.text)
        out = []
        for item in text_list:
            if item:
                test = item.lower()
                if test in self.article.word_map:
                    word = self.article.word_map[test]
                    out.append(self.color_word(item, word.level))
                else:
                    out.append(item)
        print("".join(out))

    def do_learn(self, word):
        if word.lower() in self.article.word_map:
            item = self.article.word_map[word.lower()]
            item.level += 1
            print("Leveled Up!!")
        else:
            print("Word not in Article")
            


    def do_printMap(self, args):
        out = []
        for k, v in self.article.word_map.items():
            out.append(k)
        print(out)


    def do_quit(self,arg):
        print("Goodbye!")
        return True

    def do_test(self, arg):
        print(f"\033[1;32;40m {arg}!!]")


    # ======= ANCILIARY FUNCTIONS =========
    def color_word(self, word, level):
        colors = {0: "41",
                  1: "45",
                  2: "44",
                  3: "46",
                  4: "43",
                  5: "42"}
        return f"\u001b[{colors[level]};1m{word}\u001b[0m"

if __name__ == "__main__":
    prompt = LangReaderShell()
    prompt.prompt = '> '
    prompt.cmdloop("Starting Lang Reader...")
