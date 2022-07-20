# 7'41

# JSON prebacuje Py-objekte u STRING of JSON. To koliko toliko radi sa built-in clasama. Medjutim, sa custom-class to ne radi, ne valja!!!

import json

j = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
print(j)    # ["foo", {"bar": ["baz", null, 1.0, 2]}]

# Prikaz je s builtin skoro ok: None-->null, '-->", (tuple)-->[list], ostalo isto osim sto je STRING!

# Za custom-nestandardne klase imamo opciju dict-reprezenta:


class Cat():
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed


c = Cat("Blue", "Tabby")
k = json.dumps(c.__dict__)
print(k)    # {"name": "Blue", "breed": "Tabby"}

# dakle, ako zelimo picklati podatke tako da ih mozemo i pogledati (za razliku od picklanja) mozemo i sa json-om
# ruzan prikaz koji dolazi u obzir samo za jednostvne dumpove. za bolje jsonpickle!!!
# todo $ python3 -m pip install jsonpickle
# odradjeno i u 321b
