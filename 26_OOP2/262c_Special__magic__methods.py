# 14'19

#  Ath se nastavlja igrati i dodaje __mul__

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
        return "YOU ARE MULTIPLYING HUMANS!"
    
j = Human("Jany", "Larsen",17)
k = Human("Kevin", "Jones",34)

print(j+k)   # Human named Newborn Larsen aged 0
print(j+2)   # You cann't add that!
print(j*2)   # YOU ARE MULTIPLYING HUMANS!

# ali ako "other = 2" stavimo kao prvi faktor on poteze bulit-in definiciju mnozenja za int-klasu i zbog mjesanja type-ova Error

print(2*j)  # TypeError: unsupported operand type(s) for *: 'int' and 'Human'