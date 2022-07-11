# 10'50

# primjer koji pokazuje osjetljivost atributa (propsa):

class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        
jane = Human("Jane", "Godall", 50)
print(jane) # <__main__.Human object at 0x7fd5f70c8f40>
print(jane.age) # 50
jane.age = -100
print(jane.age) # -100

# To je to! - lako promjenimo pravu vrijednost :(. Rjesenje problema upotrebom PROPERITESA! Ali, prije toga "obilazno" rjesenje uporabom privatnog atributa "_age" i kondicionalne logike ("if"...)

class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        if age >= 0:                        # sprjecavanje negativnog broja
            self._age = age                 # uvodjenje propa _age
        else:
            self._age = 0
    def get_age(self):                      # metod ocitanja _age tj age
        return self._age
    def set_age(self, new_age):             # metod setiranja _age tj age
        if new_age >= 0:
            self._age = new_age
        else:
            self._age = 0
            
        
jane = Human("Jane", "Godall", -9)
#? print(jane.age) # AttributeError: 'Human' object has no attribute 'age'
print(jane._age) # 0 # ne bi trebali koristiti direktno, private attrib
print(jane.get_age()) # 0   # -9 postaje 0
print(jane.set_age(45)) # None
print(jane.get_age()) # 45

# koristenje "@property" za "pretvaranje" metoda u attribut pri ocitanju
class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        if age >= 0:                        # sprjecavanje negativnog broja
            self._age = age                 # uvodjenje propa _age
        else:
            self._age = 0
            
    @property                               # as getter
    def age(self):
        return self._age                    # radi "jane.age"
    
    @age.setter                             # as setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError("age cannot be negative!")
        
jane = Human("Jane", "Godall", 34)
print(jane.age) # 34
jane.age =20
print(jane.age) # 20
#? jane.age = -100 # ValueError: age cannot be negative!

# kao malo utvrdjivanje gradiva dodajemo jos par propsa:
class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        if age >= 0:                        # sprjecavanje negativnog broja
            self._age = age                 # uvodjenje propa _age
        else:
            self._age = 0
            
    @property                               # as getter
    def full_name(self):
        return f"{self.first} {self.last}" 
    
    @full_name.setter                       # as setter
    def full_name(self, name):
        self.first, self.last = name.split(" ") # pazi " " a ne "" !!!

jane = Human("Jane", "Godall", 34)      
print(jane.full_name) # Jane Godall
jane.full_name = "Tim Minchin"
print(jane.__dict__) # {'first': 'Tim', 'last': 'Minchin', '_age': 34}
print(jane.full_name) # Tim Minchin
