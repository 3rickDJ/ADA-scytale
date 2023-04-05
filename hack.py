import scytale
import time
import fitness as fit

if __name__ == '__main__':
    # ee_msg = 'E rln uo u dnl acdymniaa ud heoboecrugeMa  r romna a,cneqore'
    msg =   '''\
CoMo EsT,As AmIgOS\
'''
    ee_msg = scytale.encrypt(msg, 5)
    dictionary = fit.get_dict('words5T')

    start = time.time()
    valid_ps = filter(lambda p: len(ee_msg)%p==0,range(2,len(ee_msg)))
    guess = {p:{'msg': scytale.decrypt(ee_msg, p)} for p in valid_ps}
    fitnesses = {k:{'fit': fit.fitness(v,dictionary, opt=True), 'msg': v['msg'], 'key':k }for k,v in guess.items()}
    max_key = max(fitnesses, key=lambda k: fitnesses[k]['fit'])
    end = time.time()
    for term in fitnesses.items():
        print(f"{term=}") 

    msg, key = fitnesses[max_key]['msg'], fitnesses[max_key]['key']

    print(f"The decrypted message💌: '{msg}' key🔑={key}")
    print(round(end - start, 8), "seconds are needed to find the solution above")
