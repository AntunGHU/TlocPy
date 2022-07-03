# 10'13''
# dolazi na scenu kad iskoci greska koja nije namjerna
# importira se pdb modul

#? import pdb; pdb.set_trace() # linija koja pauzira kod, ; za vise L-koda u jednoj L

import pdb
first = "First"
second = "Second"
pdb.set_trace()     # -> result = first + second    # prikaz koda i mjesta
                    # (Pdb) 
                    # kod se izvodi sve do pdb kad staje i pokazuje u REPL-u koja je sljedeca linija koda
                    # sad mozemo koristiti k-de pdb-ea (REPL-u): l-list, n-next, p-print, c-continue i zavrsava debuging
                    # tjekom debuganja mogu pozivati varijable:
                    # (Pdb) first'First'
                    # (Pdb) second
                    # 'Second'
                    # (Pdb) third
                    # *** NameError: name 'third' is not defined
                    # (Pdb)
                    # Sa n-next pomicemo sve za jednu L i tako mozemo do kraja
                    # ako zelimo prekid mozemo sa "q" ali Colt preporuca "c" za nastaviti i zavrsiti jer "q" cesto errora.
result = first + second
third = "Third"
result += third
print(result)

# pdb unutar funkcija starta tek njenim izvršenjem!!
def add_numbers(a,b,c,d):
    import pdb; pdb.set_trace()
    return a+b+c+d
add_numbers(3,4,5,6)