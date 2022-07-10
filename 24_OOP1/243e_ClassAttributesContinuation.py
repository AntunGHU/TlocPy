# 12'42

# na kraju Tloc daje diagram ovisnosti Pet-instanci od Pet-klase u attributu "allowed". 
# Zato sto se zapravo i cat1.allowed i dog1.allowed referenciraju zapravo na isto mjesto tj na Pet.allowed, vidi kod ispod, mozemo u initu koristiti umjesto "Pet.allowed" "self.allowed" ali tada ne smijemo nista mjenjati jer bi polomili tu vezu instanci na klas-attribut

class Pet:
    
    allowed = ['cat', 'dog', 'fish', 'rat']
    
    def __init__(self, name, species):
        if species not in self.allowed:
            raise ValueError(f"You can't have a {species} pet!")
        self.name = name
        self.species = species
        
    def set_species(self, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} pet!")
        self.species = species
    
dog1 = Pet("Wyatt", "dog")
print(dog1)                 # <__main__.Pet object at 0x7f3e810248b0> 
cat1 = Pet("Blue", "cat")
print(cat1)                 # <__main__.Pet object at f3e810248b0>         

print(id(cat1.allowed))     # 140582469202816
print(id(dog1.allowed))     # 140582469202816
print(id(Pet.allowed))      # 140582469202816