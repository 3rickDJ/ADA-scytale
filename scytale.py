#!/usr/bin/env python3
import argparse
import numpy as np
def encrypt(msg, perimeter):
    lenght = len(msg)
    size = lenght + (perimeter - lenght%perimeter)  if lenght%perimeter != 0 else lenght
    # Fix the length of the string by adding spaces
    # Fix the length of the string by adding spaces
    padded_string = msg.ljust(size)
    
    # Split the padded string into n-sized chunks
    chunks = [list(padded_string[i:i+perimeter]) for i in range(0, size, perimeter)]
    # print(f"{size=}\n{chunks=}")
    return ''.join(np.transpose(chunks).flatten())

def decrypt(msg, perimeter):
    msg =  list(msg)
    num_lines = len(msg)//perimeter
    matrix = [msg[i:i+num_lines] for i in range(0,len(msg), num_lines)]
    # print(f"{matrix=}")
    last = ''.join(np.transpose(matrix).flatten().tolist())
    return last


def _main():
    parser = argparse.ArgumentParser()
    parser.add_argument("msg", nargs='?', help="message or file to read from", type=str, default='En un lugar de la Mancha, de cuyo nombre no quiero acordarme')
    parser.add_argument("key", nargs='?',help="key to decrypt/encrypt", type=int, default=5)
    parser.add_argument('-f', '--file', action="store_true", default=False, help= 'read from a file')
    parser.add_argument('-d', "--decrypt", action="store_true", default=False, help= 'encrypt or decrypt')
    parser.add_argument('-v', "--verbose", action="store_true", default=False, help= 'encrypt and decrypt. Not valid with -d option')
    parser.add_argument('-q', "--quiet", action="store_true", default=False, help= 'output quietly (as is)')
    args = parser.parse_args()
    perimeter = args.key 
    msg= args.msg
    if args.file:
        with open(args.msg)as f:
            msg = f.read()
    if (args.verbose and args.decrypt):
        print("Error: verbose only allow to encrypt, then decrypt")
        exit()

    if args.verbose:
        e_msg = encrypt(msg, perimeter)
        print(f"{e_msg=}") 
        de_msg = decrypt(e_msg, perimeter)
        print(f"{de_msg=}")
        print("it works") if de_msg == msg else print(f" {de_msg=} !=== {msg=}")
    elif args.quiet and args.decrypt:
        print(decrypt(msg, perimeter), end='')
    elif args.quiet:
        print(encrypt(msg,perimeter), end='')
    elif args.decrypt:
        print(f"Dencrypted message: '{decrypt(msg, perimeter)}'")
    else:
        print(f"Encrypted  message: '{encrypt(msg, perimeter)}'")

if __name__ == '__main__':
    _main()
