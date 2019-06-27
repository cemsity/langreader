import sys
import re
from classes.article import Article



def main(arg):
    file = open_file(arg)
    text = Article(file)
    print(text.word_map)




def open_file(arg):
    with open(arg, 'r', encoding='utf-8') as file:
        return file.read()




if __name__ == "__main__":

    main(sys.argv[1])