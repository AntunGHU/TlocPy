# 9'46''
# Svi se mogu naći u py.org/python module Index. Ne moraju se dld-ati jer dolaze s py-instalom

import random
a=random.choice(['apple', 'banana', 'cherry', 'durion'])
print(a)
b=random.shuffle(['apple', 'banana', 'cherry', 'durion'])
print(b)    # None  cudno!!


# importanje sa "as" obicno ako je ime modula predugacko
import random as o_s_r
a=o_s_r.choice(['apple', 'banana', 'cherry', 'durion'])
print(a)
b=o_s_r.shuffle(['apple', 'banana', 'cherry', 'durion'])
print(b)    # None  cudno!!


# importanje djela modula sa "from MODULE import *" paternom
from random import choice, shuffle
a=choice(['apple', 'banana', 'cherry', 'durion'])
print(a)
b=shuffle(['apple', 'banana', 'cherry', 'durion'])
print(b)    # None  cudno!!