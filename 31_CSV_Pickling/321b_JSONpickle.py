import jsonpickle


class Cat():
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed


c = Cat("Blue", "Tabby")

frozen = jsonpickle.encode(c)
# {"py/object": "__main__.Cat", "name": "Blue", "breed": "Tabby"}
print(frozen)

# * Dakle, puno detaljniji zapis od obicnog pickle-a! koji osim detaljnosti omogucava i totalni povrat na mjesto odakle je encode-an (kao i obicni pickle) te moze izvesti i metode!!! sto se vidi dole ako se save-a u fajl:

with open("cat.json", "w") as file:
    frozen = jsonpickle.encode(c)
    file.write(frozen)

# * stvorio se novi fajl "cat.json" sa istim sadrzajem:
# {"py/object": "__main__.Cat", "name": "Blue", "breed": "Tabby"}
# * ali tek sad sljedi nacoolest thing. Ako ucita taj fajl sa:

with open("cat.json", "r") as file:
    content = file.read()
    unfrozen = jsonpickle.decode(content)
    print(unfrozen)  # <__main__.Cat object at 0x7f134bd45fa0>
    # prin (poceo Colt pa primjetio da nema metod)

# * I dobili smo nazad rekonstruiranu "Cat" iz json-a te da sada imamo metod mogli bi ga pozvati-izvesti. Dakle, "json" je malo limitiran glede pohrane custom klasa ali "jsonpickle" dozvoljava kao i obicni pickle sve osim sto je json.
