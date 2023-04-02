import numpy as np
def encrypt(msg, n):
    lenght = len(msg)
    size = lenght + (perimeter - lenght%perimeter)  if lenght%perimeter != 0 else lenght
    # Fix the length of the string by adding spaces
    # Fix the length of the string by adding spaces
    padded_string = msg.ljust(size)
    
    # Split the padded string into n-sized chunks
    chunks = [list(padded_string[i:i+n]) for i in range(0, size, n)]
    print(f"{size=}\n{chunks=}")
    return ''.join(np.transpose(chunks).flatten())

def decrypt(msg, perimeter):
    msg =  list(msg)
    num_lines = len(msg)//perimeter
    matrix = [msg[i:i+num_lines] for i in range(0,len(msg), num_lines)]
    last = ''.join(np.transpose(matrix).flatten().tolist())
    return last


# msg = "hola como estas"
if __name__ == '__main__':
    msg = 'En un lugar de la Mancha, de cuyo nombre no quiero acordarme'
    perimeter = 5
    e_msg = encrypt(msg, perimeter)
    print(f"{e_msg=}") 
    de_msg = decrypt(e_msg, perimeter)
    # print(de_msg)
    # print("it works") if de_msg == msg else print(f" {de_msg=} !=== {msg=}")
    print(f"{de_msg=}")
