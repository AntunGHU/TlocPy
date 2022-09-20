#! ako imamo vise fn u hijerarhiji "nonlocal"
def outer():
    '''pokusaj da se vidi ishod doc-string-doca'''
    count = 0

    def inner():
        nonlocal count
        count += 1
        return count
    return inner()


print(outer())
print(outer.__doc__)  # ! zakljucak, dunder se poziva bez ()

#! RECUP
# funs izvode kod primajuci inpute i returnajuci sa return
# radi inputa kreiramo parametre koji mogu imati i def-values
# varijable defane u fun imaju scope samo u njoj!!!!
# keyword argumente mozemo dati proizvoljnim, nonparametarskim redom
# paziti da se return stavi na pravo mjesto i izbjegnu nepotrbni else-vi
