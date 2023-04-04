import scytale
import time
import fitness as fit

if __name__ == '__main__':
    # ee_msg = 'E rln uo u dnl acdymniaa ud heoboecrugeMa  r romna a,cneqore'
    msg =   '''\
En un lugar de la Mancha, de cuyo nombre no quiero acordarme, hola como te encuentras en este dia tan caluroso
En un lugar de la Mancha, de cuyo nombre no quiero acordarme, hola como te encuentras en este dia tan caluroso\
'''
    ee_msg = scytale.encrypt(msg, 9)
    start = time.time()
    lenght = len(ee_msg)
    guess = {}
    # valid_ps = list(filter(lambda p: lenght%p==0,range(2,len(ee_msg))))
    for perimeter in range(2,len(ee_msg)-1):
        if lenght%perimeter !=0:
            continue
        de_msg = scytale.decrypt(ee_msg, perimeter)
        guess[perimeter] = {'msg': de_msg}

    dictionary = fit.get_dict('words5T')
    fitnesses = {}
    for k, v in guess.items():
        fitnesses[k] = fit.fitness(v, dictionary)
    max_key = max(fitnesses, key=lambda k: fitnesses[k])
    print(f"The decrypted message💌: '{guess[max_key]['msg']}' key🔑={max_key}")

    end = time.time()
    print(round(end - start, 8), "seconds are needed to find the solution above")

    # guess = {}
    # for perimeter in range(2, len(e_msg) - 1):
        # de_msg = scytale.decrypt(e_msg, perimeter)
        # guess[perimeter] = de_msg

    # print(guess)
