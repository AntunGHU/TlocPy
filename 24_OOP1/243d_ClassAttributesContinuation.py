# 12'42

# Ali kad postoji ClassAttribut onda su moguce podvale kroz nadopune sa "append" - vidi 243d

class Pet:
    
    allowed = ['cat', 'dog', 'fish', 'rat']
    
    def __init__(self, name, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} pet!")
        self.name = name
        self.species = species
        
    def set_species(self, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} pet!")
        self.species = species
    
cat1 = Pet("Blue", "cat")
print(cat1)                 # <__main__.Pet object at 0x7f3e810248b0>
print(cat1.species)         # cat            
cat1.set_species("rat")
print(cat1.species)         # rat            
#? cat1.set_species("Tiger") 
# # ValueError: You can't have a Tiger pet!

Pet.allowed.append(("Tiger"))
print(Pet.allowed)
cat1.set_species("Tiger") 
print(cat1.species)         # Tiger           
