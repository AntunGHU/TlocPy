# 9'44

# "Crazy" zato sto to jos nitko nije pokrio prije njega! Nije cesto al pomaze razumjeti Py-strojarnicu.

class Aquatic:
    def __init__(self, name):
        print("AQUATIC INIT!!")
        self.name = name
    def swim(self):
        return f"{self.name} is swiming!"
    def greet(self):
        return f"I am {self.name} of the sea! "
    
class Ambulatory:
    def __init__(self, name):
        print("AMBULATORY INIT!!")
        self.name = name
    def walk(self):
        return f"{self.name} is walking!"
    def greet(self):
        return f"I am {self.name} of the land!"
    
class Penguin(Ambulatory, Aquatic):
    def __init__(self, name):
        print("PENGUIN INIT!!")
        super().__init__(name=name)
        
jaws = Aquatic("Jaws")
lassie = Ambulatory("Lassie")
captain_cook = Penguin("CaptainCook")

print(captain_cook.swim())      # CaptainCook is swiming!
print(captain_cook.walk())      # CaptainCook is walking!
print(captain_cook.greet())     # I am CaptainCook of the land!

# "greet()" povlači Ambulatory-method greet jer je on naveden kao prvi u Inheritanju. To dokazujemo i sa print("PENGUIN INIT") i print("AMBULATORY INIT") u sklopu init-a tijekom inicijalizacije "captain_cook-a". Nakon zamjene mjesta AQUATIC i AMBULATORY, printa se "PENGUIN INIT" i "AQUATIC INIT"
# Ako hocemo da tijekom init-a Penguin-a rade sva 3 init-a i isprintaju se sva 3 printa, moramo 2. inheritanc iz zagrade dopisati ispod super() a tada je vise stilski ako i super() promjenimo u "Ambulatory" posto je ispod njega vec imenom prisutan "Aquatic":

class Penguin(Ambulatory, Aquatic):
    def __init__(self, name):
        print("PENGUIN INIT!")
        Ambulatory.__init__(self, name=name)
        Aquatic.__init__(self, name=name)
        
captain_cook = Penguin("CaptainCook")
