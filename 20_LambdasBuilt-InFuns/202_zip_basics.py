# zip pravi iterator kombinirajuci dane iteratore jednakih duljina
first_zip = zip([1,2,3],[4,5,6])
print(first_zip)    # <zip object at 0x7f4f6dd6ddc0>
print(list(first_zip))  # [(1, 4), (2, 5), (3, 6)]  # jednokratno
print(dict(first_zip)) # {}

first_zip = zip([1,2,3],[4,5,6])
print(first_zip)    # <zip object at 0x7f4f6dd6ddc0>
print(dict(first_zip))  # {1: 4, 2: 5, 3: 6} # jednokratno
print(list(first_zip))  # []

# poredak iteratora je bitan   
z1 = zip([1,2,3],[4,5,6])
print(list(z1))
z2 = zip([4,5,6],[1,2,3]) 
print(list(z2))

# Ako broj itema u iteratorima nije isti zip-anje staje kad se iscrpi kraci
z3 = zip([4,5,6,7],[1,2,3,4,5,6]) 
print(list(z3))

# Broj i vrsta iteratora u zip-u moze biti proizvoljno
num1 = [1,2,3,4]
num2 = [3,4,5,6,7,8,9]
words = ('hi', 'poz', 'alo', 'VOILA')
z4 = zip(num1,num2,words)
print(tuple(z4))

# uporaba * za raspakiravanje u obrnutom smjeru!
five_by_two = [(0,1), (1,2), (2,3), (3,4), (4,5)]
z5 = list(zip(*five_by_two))
print(z5)   # [(0, 1, 2, 3, 4), (1, 2, 3, 4, 5)]
five_by_three = [(0,1,'a'), (1,2,'b'), (2,3,'c'), (3,4,'d'), (4,5,'e')]
z6 = list(zip(*five_by_three))
print(z6)   # [(0, 1, 2, 3, 4), (1, 2, 3, 4, 5), ('a', 'b', 'c', 'd', 'e')]