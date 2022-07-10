# 12'42

# primjer sa ljubimcima i konditional logic

class Pet:
    allowed = ['cat', 'dog', 'fish', 'rat']
    def __init__(self, name, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} pet!")
        self.name = name
        self.species = species
        
    
cat1 = Pet("Blue", "cat")
print(cat1)                 # <__main__.Pet object at 0x7f3e810248b0>
dog1 = Pet("Wyatt", "dog")
print(dog1)                 # <__main__.Pet object at 0x7f3e81031fa0>
tiger1 = Pet("Tony", "tiger")   # ValueError: You can't have a tiger pet!
