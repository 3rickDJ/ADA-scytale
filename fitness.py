import string
from functools import reduce
# print(punctuation)

def get_dict(name):
    with open(name) as f:
        d = list(map(lambda n: n.strip(), f.readlines()))
        d += ['hola']
        return  { n:True for n in d}

def normalize(word, punctuation):
    return "".join([char for char in word if char not in punctuation])

def fitness(dic, dictionary):
    word_list = dic['msg'].split()
    # print(word_list)
    punctuation = string.punctuation + "¡¿"
    word_list = [normalize(word, punctuation) for word in word_list]
    
    matchs = list(map(lambda word: 1 if dictionary.get(word, False) else 0, word_list))
    last = reduce(lambda a,b: a+b, matchs)
    return last
