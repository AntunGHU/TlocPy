# The most straight forward solution is to use a large if-elif-else statement:
def speak(animal="dog"):
    if animal == "pig":
        return "oink"
    elif animal == "duck":
        return "quack"
    elif animal == "cat":
        return "meow"
    elif animal == "dog":
        return "woof"
    else:
        return "?"


print(speak())  # "woof"
print(speak("pig"))  # "oink"
print(speak("duck"))  # "quack"
print(speak("cat"))  # "meow"
print(speak("dog"))  # "woof"
print(speak("banana"))  # "?"

# Another shorter solution involves using a dictionary that maps animal names to noises.
# ? noises = {"dog": "woof", "pig": "oink", "duck": "quack", "cat": "meow"}
# Then, we just use the dictionary.get() method to retrieve the correct animal noise and save it to a variable called noise . get() will return None  if the animal is not in the dictionary.  Then we just check to see if noise  exists.  If it does, return noise .  Otherwise, return "?"


def speak2(animal="dog"):
    noises = {"dog": "woof", "pig": "oink", "duck": "quack", "cat": "meow"}
    noise = noises.get(animal)
    if noise:
        return noise
    return "?"


print(speak2())  # "woof"
print(speak2("pig"))  # "oink"
print(speak2("duck"))  # "quack"
print(speak2("cat"))  # "meow"
print(speak2("dog"))  # "woof"
print(speak2("banana"))  # "?"

# Thanks to Todd for sharing his even more compact solution which passes in a default value to get()


def speak3(animal='dog'):
    noises = {'pig': 'oink', 'duck': 'quack', 'cat': 'meow', 'dog': 'woof'}
    return noises.get(animal, '?')


print(speak3())  # "woof"
print(speak3("pig"))  # "oink"
print(speak3("duck"))  # "quack"
print(speak3("cat"))  # "meow"
print(speak3("dog"))  # "woof"
print(speak3("banana"))  # "?"
