import re
from functools import reduce
from jellyfish import jaro_winkler_similarity as jaro
# print(punctuation)

def get_dict(name):
    with open(name) as f:
        d = list(map(lambda n: n.strip(), f.readlines()))
        return  { n:True for n in d if len(n) !=1}

def normalize(sentence):
    words = re.split(r'[\s!"#$%&\'()*+,\-./:;<=>?@\[\\\]^_`{|}~¡¿]+', sentence)
    return [w.lower() for w in words if w!='']

def jaro_dist(word, dictionary):
    max = 0
    dic = list(dictionary)
    for w in dic:
        jaro_d = jaro(word,w)
        max = jaro_d if jaro_d > max else max
    return max/len(word)

def fitness(dic, dictionary, opt=True):
    if opt:
        matchs = list(map(lambda word: 1 if dictionary.get(word, False) else 0, normalize(dic['msg'])))
    else:
        matchs = list(map(lambda word: 1 if dictionary.get(word, False) else jaro_dist(word, dictionary), normalize(dic['msg'])))
    last = reduce(lambda a,b: a+b, matchs)
    return last
