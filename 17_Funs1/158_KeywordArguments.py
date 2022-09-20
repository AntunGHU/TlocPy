def full_name(first, last):
    return f"Your name is {first} {last}"


print(full_name("Colt", "Steele"))
print(full_name(first="Colt", last="Steele"))
print(full_name(last="Steele", first="Colt"))
# print(full_name(last="Steele","Colt")) # SyntaxError: positional argument follows keyword argument
# print(full_name("Steele",first="Colt")) # TypeError: full_name() got multiple values for argument 'first'
# print(full_name(first="Colt","Steele")) # SyntaxError: positional argument follows keyword argument
print(full_name("Colt", last="Steele"))
