# 14'19

# "+" je kratica za __add__() operator-dunder koji se poziva na 1.operand. Ako je 1. operand int vrsi se zbrajanje a ako je str vrsi se konkatinacija. Ako je mix nastaje Error!
# Jos neki dunder: __len__ . Mozemo i sami (kao sto je to Ath vec jednom pokazao i dokazao) mjenjati def dundera, npr __len__

class Human:
    def __init__(self, visina):
        self.visina = visina
    def __len__(self):
        return self.visina
Antun = Human(175)
print(len(Antun))   # 175

# __repr__ dunder za ljepsi prikaz instance u obliku stringa a ne <...main
# ovi spec. methodi nalaze se pod 3.3 poglavljem Py-doc: __init__, __str__, __format__, __reversed__, __sub__, __mul__ i gomila drugih ali
# Bilo koji da bi radio za nasu klasu mora biti eksplicitno dodan!!! Ako ih (kao u sljedecim primjerima) dodamo, imamo ih na raspolaganju i mozemo ih pozivati. Komentiranja istih pri pozivanju dovode do greske.

class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
    def __len__(self):
        return self.age
    def __repr__(self):
        return f"Human named {self.first} {self.last} aged {self.age}"
j = Human("Jany", "Larsen",17)
print(len(j))   # 17
print(j)   # Human named Jany Larsen aged 17

# Ali ako blio koju def komentiramo nastaje greska
class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
    def __len__(self):
        return self.age
    # def __repr__(self):
    #     return f"Human named {self.first} {self.last} aged {self.age}"
j = Human("Jany", "Larsen",17)
print(len(j))   # 17
print(j)   # <__main__.Human object at 0x7fe5aeca2310>

# Ali ako blio koju def komentiramo nastaje greska
class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
    # def __len__(self):
    #     return self.age
    def __repr__(self):
        return f"Human named {self.first} {self.last} aged {self.age}"
j = Human("Jany", "Larsen",17)
print(j)        # Human named Jany Larsen aged 17
print(len(j))   # TypeError: object of type 'Human' has no len()