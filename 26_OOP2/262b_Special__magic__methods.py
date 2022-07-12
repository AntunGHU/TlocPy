# 14'19

#  nastavku Ath pokazuje kako mozemo svojoj klasi Human dodati svoju verziju __add__ koja ce sa drugom instancom Human-klase dati rodjenje nove instance Human klase sa age=0. Kako bi to mogao dodaje jos jednu instancu "k"
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
j = Human("Jany", "Larsen",17)
k = Human("Kevin", "Jones",34)

print(j+k)   # Human named Newborn Larsen aged 0
print(j+2)   # You cann't add that!