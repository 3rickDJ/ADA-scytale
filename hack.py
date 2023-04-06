import scytale
import time
import fitness as fit
import argparse


def hack(e_msg,):
    dictionary = fit.get_dict('words5T')
    valid_ps = filter(lambda p: len(e_msg)%p==0,range(2,len(e_msg)))
    guess = {p:{'msg': scytale.decrypt(e_msg, p)} for p in valid_ps}
    fitness = {p:fit.fitness(v,dictionary, opt=True) for p,v in guess.items()}
    key = max(fitness, key=lambda k: fitness[k])
    msg = guess[key]['msg']
    return key, msg

def cli_tool():
    parser = argparse.ArgumentParser()
    parser.add_argument("msg", nargs='?', help="message to decrypt", type=str)
    parser.add_argument('-f', '--file', action="store_true",  help= 'read from file {msg}')
    parser.add_argument('-v', "--verbose", action="store_true",  help= 'outputs key and decrypted message')
    parser.add_argument('-k', "--key", action="store_true",  help= 'outputs only the key')
    return parser.parse_args()


if __name__ == '__main__':
    args = cli_tool()

    if args.msg:
        e_msg = open(args.msg).read() if args.file else args.msg
    else:
        e_msg = input()


    start = time.time()
    key, msg = hack(e_msg,)
    end = time.time()

    if args.verbose:
        print(f"💌 Message:'{msg}' 🔑 Key:{key}")
        print(round(end - start, 8), " 🙈 Seconds are needed to find the solution above.")
    elif args.key:
        print(f"{key}")
    else:
        print(f"{msg}")
