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
        super().do_something()
        
class C(A):
    def do_something(self):
        print("Method In C")
        super().do_something()
        
class D(B,C):
    def do_something(self):
        print("Method In D")
        super().do_something()
        
thing = D()
thing.do_something()    #  Method In D

# Ako u D koristimo "super().do_something()" on ce povlaciti 1. u redu MRO-a tj B  pa cemo imati Method In D i Method In B. Ako sad taj super().do_something() dodamo u B tad  ce D printati Method In D, Method In B, Method In C i na kraju Method In D, Method In B, Method In C, Method In A

