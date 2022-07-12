# 9'04

# MRO ili HIJERARCKY - Stvara se u trenutku kreiranja klase i odredjuje redoslijed povlacenja metoda roditelja
# Promjenio se od Py2 na Py3 i ima vrlo iscrpan i kompleksan clanak u Py-docu
# 3 nacina ocitavanja: 1) __mro__  2) mro()  3) help(cls)-Tloc's prefered

# novi primjer s A,B,C i D:
class A:
    def do_something(self):
        print("Method In A")
        
class B(A):
    def do_something(self):
        print("Method In B")
        
class C(A):
    def do_something(self):
        print("Method In C")
        
class D(B,C):
    def do_something(self):
        print("Method In D")
        
thing = D()
thing.do_something()    #  Method In D

print(D.__mro__)    # (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
print(D.mro())      # [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
help(D)             # Help on class D in module __main__:

# class D(B, C)
#  |  Method resolution order:
#  |      D
#  |      B
#  |      C
#  |      A
#  |      builtins.object
#  |  
#  |  Methods defined here:
#  |  
#  |  do_something(self)
#  |  
#  |  ----------------------------------------------------------------------
#  |  Data descriptors inherited from A:
#  |  
#  |  __dict__
#  |      dictionary for instance variables (if defined)
#  |  
#  |  __weakref__
#  |      list of weak references to the object (if defined)
# ~