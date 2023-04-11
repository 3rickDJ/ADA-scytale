# algoritmo de cifrado y descifrado escitala
from math import ceil
def cifrar(msg, n):
    # pad msg with * to make it a multiple of n
    msg = msg.ljust(n  * ceil(len(msg)/n), '*')
    # take slices of n chars
    chunks = [list(msg[i:i+n]) for i in range(0, len(msg), n)]
    # transpose the matrix
    t =  _transpose(chunks)
    # take each char and join them
    return ''.join([i for row in t for i in row])

def descifrar(msg, n):
    chunks = [list(msg[i:i+n]) for i in range(0, len(msg), n)]

def _transpose(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

def main():
    pass

for i in range(2,100):
    print( cifrar("hola como estas", i))
