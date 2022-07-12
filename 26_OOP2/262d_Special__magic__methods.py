# 14'19

#  Dorada definicije __mul__ i kao rezultat vise Humana

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
            return [self for i in range(other)]
        return "CAN'T MULTIPLY!!"
    
j = Human("Jany", "Larsen",17)
k = Human("Kevin", "Jones",34)

print(j+k)   # Human named Newborn Larsen aged 0
print(j+2)   # You cann't add that!
print(j*2)   # [Human named Jany Larsen aged 17, Human named Jany Larsen aged 17]
print(j*"2") # CAN'T MULTIPLY!!