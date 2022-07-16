# 7.20

# GE kreiraju Generator i slice na LC s tom razlikom da koriste () a ne [].

def nums():
    for num in range(1, 10):
        yield num


g = nums()
print(g)  # <generator object nums at 0x7fec837f36d0>
print(next(g))  # 1
print(next(g))  # 2

# ili sa GE
g1 = (num for num in range(1, 10))
print(g1)  # <generator object <genexpr> at 0x7f556e6956d0>
print(next(g1))  # 1
