# algoritmo de cifrado y descifrado escitala
from math import ceil
def cifrar(msg, n, file=False):
    # convert ascii string to bytes
    if type(msg)==str:
        msg = bytes(msg, encoding='ascii')
    n = int(n)
    # length of each row
    l = int(ceil(len(msg) / float(n)))
    # padding message with ' ' to make it a multiple of n
    msg = msg.ljust(l * n, b' ')
    # take slices of l chars
    chunks = [msg[i:i+l] for i in range(0,len(msg),l)]
    transposed_codes = _transpose(chunks)
    # take each char and join them
    transposed_msg = list(map(lambda row: bytes(row), transposed_codes))
    msg =  b''.join(transposed_msg)
    # return bytes or ascii string
    if file:
        return msg
    return msg.decode(encoding='ascii')

def _transpose(matrix):
    return [bytes([row[i] for row in matrix]) for i in range(len(matrix[0]))]

def descifrar(msg, n, file=False):
    # convert ascii string to bytes
    if type(msg)==str:
        msg = bytes(msg, encoding='ascii')
    # take slices of n chars
    chunks = [msg[i:i+n] for i in range(0, len(msg), n)]
    transposed_codes = _transpose(chunks)
    # take each char and join them
    transposed_msg = list(map(lambda row: bytes(row), transposed_codes))
    msg = b''.join(transposed_msg)
    # return bytes or ascii string
    if file:
        return msg
    return msg.decode(encoding='ascii')

def main():
    msg ="hola como estas"
    for i in range(2,len(msg)):
        e_msg = cifrar(msg, i)
        d_msg = descifrar(e_msg, i)
        print("n: %d, e_msg:\n%s\n, d_msg:\n%s\n" % (i, e_msg, d_msg))

if __name__ == "__main__":
    opt = input("1. Cifrar\n2. Descifrar\n3. Salir")
    if opt == "1":
        format = input("1. Imagen\n2. Texto\n3. Archivo")
        if format == "1":
            img = input("Ingrese la ruta de la imagen")
            n = input("Ingrese el numero de filas")
            img = open(img, "rb").read()
            e_img = cifrar(img, n)
            name = img + '.cifrado'
            open(name, 'wb').write(e_img)
            print(f"Imagen cifrada en {name}")
        elif format == "2":
            msg = input("Ingrese el mensaje: ")
            n = input("Ingrese el numero de filas: ")
            e_msg = cifrar(msg, n)
            print(e_msg)
        elif format == "3":
            file = input("Ingrese la ruta del archivo")
            n = input("Ingrese el numero de filas")
            file = open(file, "r").read()
            e_file = cifrar(file, n)
            name = file + '.cifrado'
            open(name, 'wb').write(e_file)
            print(f"Archivo cifrado en {name}")
    elif opt == "2":
        format = input("1. Imagen\n2. Texto\n3. Archivo")
        if format == "1":
            img = input("Ingrese la ruta de la imagen")
            n = input("Ingrese el numero de filas")
            img = open(img, "rb").read()
            d_img = descifrar(img, n)
            name = img + '.descifrado'
            open(name, 'wb').write(d_img)
            print(f"Imagen descifrada en {name}")
        elif format == "2":
            msg = input("Ingrese el mensaje: ")
            n = input("Ingrese el numero de filas: ")
            d_msg = descifrar(msg, n)
            print(d_msg)
        elif format == "3":
            file = input("Ingrese la ruta del archivo")
            n = input("Ingrese el numero de filas")
            file = open(file, "r").read()
            d_file = descifrar(file, n)
            name = file + '.descifrado'
            open(name, 'wb').write(d_file)
            print(f"Archivo descifrado en {name}")
    print("I'm sorry Dave")
