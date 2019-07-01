def make_word(word, gram_cats):
    out = {'word': word,
           'gram_cats': gram_cats}
    return out

def make_head(word, childs):
    return {'word': word, 'children': childs}

def make_hierarchy(head, order):
    for item in order:
        head['children']


