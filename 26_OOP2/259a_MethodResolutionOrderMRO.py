# 9'04

# MRO ili HIJERARCKY - Stvara se u trenutku kreiranja klase i odredjuje redoslijed povlacenja metoda roditelja
# Promjenio se od Py2 na Py3 i ima vrlo iscrpan i kompleksan clanak u Py-docu
# 3 nacina ocitavanja: 1) __mro__  2) mro()  3) help(cls)-Tloc's prefered
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

print(Penguin.__mro__)  # (<class '__main__.Penguin'>, <class '__main__.Ambulatory'>, <class '__main__.Aquatic'>, <class 'object'>)
print(Penguin.mro())    # [<class '__main__.Penguin'>, <class '__main__.Ambulatory'>, <class '__main__.Aquatic'>, <class 'object'>]
print(help(Penguin)) #
# Help on class Penguin in module __main__:
# 
# class Penguin(Ambulatory, Aquatic)
#  |  Penguin(name)
#  |  
#  |  Method resolution order:
#  |      Penguin
#  |      Ambulatory
#  |      Aquatic
#  |      builtins.object
#  |  
#  |  Methods defined here:
#  |  
#  |  __init__(self, name)
#  |      Initialize self.  See help(type(self)) for accurate signature.
#  |  
#  |  ----------------------------------------------------------------------
#  |  Methods inherited from Ambulatory:
#  |  
#  |  greet(self)
#  |  
#  |  walk(self)
#  |  
#  |  ----------------------------------------------------------------------
#  |  Data descriptors inherited from Ambulatory:
#  |  
#  |  __dict__
#  |      dictionary for instance variables (if defined)
#  |  
#  |  __weakref__
#  |      list of weak references to the object (if defined)
#  |  
#  |  ----------------------------------------------------------------------
#  |  Methods inherited from Aquatic:
#  |  
#  |  swim(self)
# (END)
# novi primjer s A,B,C i D:
