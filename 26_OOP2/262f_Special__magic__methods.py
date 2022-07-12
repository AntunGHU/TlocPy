# 14'19

#  importamo "copy" i mjenjamo def __mul__

from copy import copy

class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
    def __len__(self):
        return self.age
    def __repr__(self):
        return f"Human named {self.first} {self.last} aged {self.age}"
    def __add__(self, other):
        if isinstance(other, Human):
            return Human(first="Newborn", last=self.last, age=0)
        return "You cann't add that!"   # ili raise TypeError kod pravog koda
    def __mul__(self, other):
        if isinstance(other, int):
            return [copy(self) for i in range(other)]
        return "CAN'T MULTIPLY!!"
    
j = Human("Jany", "Larsen",17)
k = Human("Kevin", "Jones",34)

print(j*3)   # [Human named Jany Larsen aged 17, Human named Jany Larsen aged 17, Human named Jany Larsen aged 17]
triplets = j*3
print(triplets) # [Human named Jany Larsen aged 17, Human named Jany Larsen aged 17, Human named Jany Larsen aged 17]
triplets[1].first='Jessica'
print(triplets) # [Human named Jany Larsen aged 17, Human named Jessica Larsen aged 17, Human named Jany Larsen aged 17]

# jos mala varijacija za kraj
triplets = (k+j)*3
print(triplets) # [Human named Newborn Jones aged 0, Human named Newborn Jones aged 0, Human named Newborn Jones aged 0]