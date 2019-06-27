import sys
import re
from cmd import Cmd
from classes.article import Article
from classes.word import Word

class LangReaderShell(Cmd):

    article = None

    def do_load(self, file):
        'Load a text file to read. (utf-8)'
        with open(file, 'r', encoding='utf-8') as text:
            self.article = Article(text.read())

    def do_print(self, arg):
        'Display the current text. Text must be loaded'
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
        'Level up a word!'
        if word.lower() in self.article.word_map:
            item = self.article.word_map[word.lower()]
            item.level += 1
            print("Leveled Up!!")
        else:
            print("Word not in Article")

    def do_edit(self, args):
        'Edit a word properties'
        word, prop, value = args.split()
        if word.lower() in self.article.word_map:
            item = self.article.word_map[word.lower()]
            success = item.update((prop, value))
            if success:
                print("Word Updated!")
            else:
                print("ERROR - Property Not Availible")
        else:
            print("Word not in Article")

    def do_printWord(self, word):
        'print a words properties'
        if word.lower() in self.article.word_map:
            item = self.article.word_map[word.lower()]
            print(item)
        else:
            print("Word not in Article")

    def do_printMap(self, args):
        'print out the words in the article'
        out = []
        for k, v in self.article.word_map.items():
            out.append(k)
        print(out)


    def do_quit(self,arg):
        'Exit the program'
        print("Goodbye!")
        return True
    do_EOF = do_quit
    def do_test(self, arg):
        print(f"\033[1;32;40m {arg}!!]")

    def do_printArgs(self, args):
        print(args)

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
