# 7'19

# Prosirujuci klase Animal i Cat pokazujemo da je cilj inharitance-a upravo u educiranju ponavljanja. Ako Animal ima "name" i "species" onda ne moramo iste imati u __init__ od Cat!!!

from unicodedata import name


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def __repr__(self) -> str:
        return f"{self.name} is a {self.species}"
    
class Cat(Animal):
    def __init__(self, name, breed, toy):
        super().__init__(name, species="Cat")
        self.breed = breed
        self.toy = toy
    def play(self):
        print(f"{self.name} plays with {self.toy}")
        
blue = Cat("Blue", "Scotish Fold", "Stringtoy")
print(blue) # Blue is a Cat
print(blue.species) # Cat
print(blue.breed) # Scotish Fold
print(blue.toy) # Stringtoy
blue.play() # Blue plays with Stringtoy
