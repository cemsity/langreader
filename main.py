import sys
import re



def main(arg):
    file = open_file(arg)
    words = word_array(file)
    print(get_words(words))


def word_array(string):
    return re.split(r"(\w+)", string)


def open_file(arg):
    with open(arg, 'r', encoding='utf-8') as file:
        return file.read()

def get_words(arr):
    word = re.compile(r'\w+')
    return list(filter(lambda x: word.match(x), arr ))

if __name__ == "__main__":

    main(sys.argv[1])