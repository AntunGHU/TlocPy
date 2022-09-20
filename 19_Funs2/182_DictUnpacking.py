names = {"first": "Colt", "second": "rusty"}


def display_names(first, second):
    return f"{first} says hello to {second}"


# display_names(names)    # TypeError: display_names() missing 1 required positional argument: 'second'
print(display_names(*names))  # first says hello to second
print(display_names(**names))  # Colt says hello to rusty


# data2 = dict(1="a", 2="b", 3="c") #! samo sebi dokazujem da broj ne moze biti kljuc

def add_and_mulpiply_numbers(a, b, c):
    return(a + b * c)


data = dict(a=1, b=2, c=3)

print(data)
print(add_and_mulpiply_numbers(**data))


dataj = dict(a=1, b=2, c=3, d=55, name="Tony")


def add_and_multiply_nums(a, b, c, **kwargs):
    print(a+b*c)
    print("OTHER STUFF")
    print(kwargs)


print(dataj)    # {'a': 1, 'b': 2, 'c': 3, 'd': 55, 'name': 'Tony'}
add_and_multiply_nums(**dataj, cat="blue")
# ? 7
# ? OTHER STUFF
# ? {'d': 55, 'name': 'Tony', 'cat': 'blue'}
