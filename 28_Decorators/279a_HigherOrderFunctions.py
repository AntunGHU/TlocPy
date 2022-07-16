# 9'29

# Func as arg to other funcs

def sum(n, func):
    total = 0
    for num in range(n):
        total += func(num)
    return total


def square(x):
    return x*x


def cube(x):
    return x*x*x


print(sum(3, square))   # 5
print(sum(3, cube))     # 9


# Nested funs inside one another
