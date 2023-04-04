import scytale
import fitness as fit

if __name__ == '__main__':
    e_msg = 'E rln uo u dnl acdymniaa ud heoboecrugeMa  r romna a,cneqore'
    msg =   'En un lugar de la Mancha, de cuyo nombre no quiero acordarme'
    # ee_msg = scytale.encrypt(msg, 10)
    ee_msg = e_msg
    print(e_msg == ee_msg)
    # print(f"{e_msg=}\n{ee_msg=}")
    print(f"{ee_msg=}")
    lenght = len(ee_msg)
    guess = {}
    for perimeter in range(2,len(ee_msg)-1):
        if lenght%perimeter !=0:
            continue
        de_msg = scytale.decrypt(ee_msg, perimeter)
        print(f"{perimeter=}:____{de_msg=}")
        guess[perimeter] = {'msg': de_msg}
    print(guess)
    print('-'*80)

    dictionary = fit.get_dict('words5T')
    fitnesses = {}
    for k, v in guess.items():
        fitnesses[k] = fit.fitness(v, dictionary)
    print( fitnesses)
    max_key = max(fitnesses, key=lambda k: fitnesses[k])
    print(f"{max_key=}___{fitnesses[max_key]=}")
    print(f"The decrypted message: '{guess[max_key]['msg']}")




    


    

    # start = time.time()
    # end = time.time()
    # print(round(end - start, 8), "seconds are needed to find the solution above")

    # guess = {}
    # for perimeter in range(2, len(e_msg) - 1):
        # de_msg = scytale.decrypt(e_msg, perimeter)
        # guess[perimeter] = de_msg

    # print(guess)
