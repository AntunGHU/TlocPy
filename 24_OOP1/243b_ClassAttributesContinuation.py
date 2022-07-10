# 12'42

# allowed unutar inita (samo se 1x koristi pa ga je tesko opravdati kao samostalan class-atribut) cime prestaje biti ClassAtr ali ne postaje ni instance-atribut

class Pet:
    def __init__(self, name, species):
        allowed = ['cat', 'dog', 'fish', 'rat']
        if species not in allowed:
            raise ValueError(f"You can't have a {species} pet!")
        self.name = name
        self.species = species
        
    
cat1 = Pet("Blue", "cat")
print(cat1)                 # <__main__.Pet object at 0x7f3e810248b0>
dog1 = Pet("Wyatt", "dog")
print(dog1)                 # <__main__.Pet object at 0x7f3e81031fa0>
#? print(cat1.allowed)    
# # AttributeError: 'Pet' object has no attribute 'allowed'   # Vise nije instance attribut!
#? print(Pet.allowed)          
# # AttributeError: 'Pet' object has no attribute 'allowed'   # a nije ni Class attribut!
# Ali, stavivsi "allowed" u init ne mozemo sprijeciti da user nakon inicijalizacije sa kodom
dog1.species = "Tiger"  # promjeni species za dog1 instancu
print(dog1.species)     # Tiger
print(cat1.species)     # cat