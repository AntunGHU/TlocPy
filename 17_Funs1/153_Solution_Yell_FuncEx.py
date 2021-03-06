def yell(phrase):
    return phrase.upper() + "!"
print(yell("Prokleto dosadno uvjezbavanje"))

# Using string concatenation:
def yell(word):
    return word.upper() + "!"
print(yell("Prokleto dosadno uvjezbavanje"))

# Using the string format() method:
def yell(word):
    return "{}!".format(word.upper())
print(yell("Prokleto dosadno uvjezbavanje"))

#Using an f-string. My personal favorite, but only works in python 3.6 or later.  Udemy exercises don't support it currently :(
def yell(word):
    return f"{word.upper()}!"
print(yell("Prokleto dosadno uvjezbavanje"))
