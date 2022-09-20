from random import random


def flip_coin():        # ako iza ove L negdje ponovimo "def flip_coin():" tada definiciju func flip_coin odredjuje ta druga linija -                       isto kao i sa svim drugim u dinamickom kodiranju!!!
    r = random()
    print(r)
    if r > 0.5:
        return "Heads"
    else:
        return "Tails"


print(flip_coin())
