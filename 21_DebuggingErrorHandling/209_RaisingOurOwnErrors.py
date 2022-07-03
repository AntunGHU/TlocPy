# raise ValueError('invalid value')     # ValueError: invalid value
# raise ValueError    # ValueError
# raise NameError("blablabla")    # NameError: blablabla

def colorize(text,color):
    if type(text) is not str:
        raise TypeError("text must be a string")
    print(f"Printed {text} in {color}")
colorize("hello", "red")
# colorize(34, "red")     # TypeError: text must be a string

def colorize(text,color):
    colors=["cyan", "yelow", "blue", "green", "magenta"]
    if type(text) is not str:
        raise TypeError("text must be a string!")
    if color not in colors:
        raise ValueError("Invalid Color!")
    print(f"Printed {text} in {color}")
colorize("hello", "blue")   # ValueError: Invalid Color!
colorize("hello", "red")

# Ako ima vise errora daje prvog na kojeg dodje. Kad to popravimo daje drugog itd