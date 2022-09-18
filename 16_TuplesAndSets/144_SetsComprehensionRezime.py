# 6'21''
s = {x**2 for x in range(10)}
print(s)    # {0, 1, 64, 4, 36, 9, 16, 49, 81, 25} uvjek ovaj red!?!

s1 = {char.upper() for char in "Hello, hello!"}
print(s1)   # {' ', 'E', 'O', 'L', ',', '!', 'H'}

string1 = "hello"
print({char for char in string1 if char in "aeiou"})    # {'o', 'e'}

string2 = "sequoia"

# {'a', 'e', 'u', 'o', 'i'}
print({char for char in string2 if char in "aeiou"})

# tuples: ordered, imutable, faster, protectfaigh
# sets: unordered, unique
