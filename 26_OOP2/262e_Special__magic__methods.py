# 14'19

#  Za kraj Ath skrece paznju na jednu osobinu. Da bi je pokazao prvo (j*3) i snima je u varijablu "triplets". Potom pokusava primjenom "triplets[1].first='Jessica'" promjeniti ime 2. clana. Medjutim, pokazuje se da ce to dovesti do promjene imena sva 3 itema! iako je triplets list.

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

print(j*3)   # [Human named Jany Larsen aged 17, Human named Jany Larsen aged 17, Human named Jany Larsen aged 17]
triplets = j*3
print(triplets) # [Human named Jany Larsen aged 17, Human named Jany Larsen aged 17, Human named Jany Larsen aged 17]
triplets[1].first='Jessica'
print(triplets) # [Human named Jessica Larsen aged 17, Human named Jessica Larsen aged 17, Human named Jessica Larsen aged 17]

# Razlog je kao to sto je objekt na kom se vrsi promjena isti, onaj prvi operand mnozenja a mnozenje dolazi nakon promjene!
# Za dobiti stvarno 3 neovisne kopije moramo prvo importati "copy" i primjeniti ga u def-u __mul__a