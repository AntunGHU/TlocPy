# 9'04

# MRO ili HIJERARCKY - Stvara se u trenutku kreiranja klase i odredjuje redoslijed povlacenja metoda roditelja
# Promjenio se od Py2 na Py3 i ima vrlo iscrpan i kompleksan clanak u Py-docu
# 3 nacina ocitavanja: 1) __mro__  2) mro()  3) help(cls)-Tloc's prefered

# novi primjer s A,B,C i D:
class A:
    #4 def do_something(self):
    #4     print("Method In A")
    pass
        
class B(A):
    #2 def do_something(self):
    #2     print("Method In B")
    pass
        
class C(A):
    #3 def do_something(self):
    #3     print("Method In C")
    pass
        
class D(B,C):
    #1 def do_something(self):
    #1    print("Method In D")
    pass
        
thing = D()
thing.do_something()        #   Method In D
# Ali ako sada komamo def-ove po redu i pass-amo methodi se smjenjuju po redu u mro!
                            #1  Method In B
                            #2  Method In C
                            #3  Method In A
                            #4  AttributeError: 'D' object has no attribute 'do_something'
