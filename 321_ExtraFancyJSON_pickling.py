import json

j = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
print(j)    # ["foo", {"bar": ["baz", null, 1.0, 2]}]

#! json.dumps pretvara py-objekt u STRING of JSON. Ali to koliko toliko radi sa built-in clasama. Medjutim, sa custom-class to ne radi, ne valja!!!


class Cat():
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
           
c = Cat("Blue", "Tabby")
k = json.dumps(c.__dict__)
print(k)    # {"name": "Blue", "breed": "Tabby"}

#! ruzan prikaz koji dolazi u obzir samo za jednostvne dumpove. za bolje jsonpickle!!!
#todo $ python3 -m pip install jsonpickle


