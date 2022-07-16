# 5'59

from itertools import count


def fib_list(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a+b
    return nums


print(fib_list(10))

# S listom da bi dosli do 10-tog fib-broja s "print(fib_list(10))" moramo ispisati sve ispred njega tj keep track. Za milion upotreba memorije ide do 500Mb.


def fib_gen(max):
    nums = []
    x, y = 0, 1
    count = 0
    while count < max:
        x, y = y, x+y
        yield x
        count += 1
    return nums


print(fib_gen(10))  # <generator object fib_gen at 0x7fa39954d7b0>
for n in fib_gen(10000):
    print(n)

# Za isto sa gen: 1. brojevi nisu u listi, 2. generiraju se samo po 1 u datom trenutku. Sa "for n in fib_gen(1000000): print(n)" uzme samo 6Mb sto je gotovo 100x manje. Brzina slicna a gen je cesto i sporiji!
