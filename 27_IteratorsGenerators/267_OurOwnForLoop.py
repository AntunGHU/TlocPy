# 6'54

# my_for
def my_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            print("END OF ITERATOR!")
            break
my_for("Antun")

# my_for2
def my_for2(iterable, func):
    iterator = iter(iterable)
    while True:
        try:
            thing = next(iterator)
        except StopIteration:
            break
        else:
            func(thing)
            
def square(x):
    print(x*x)

my_for2("lol", print)   # Jedno ispod drugog: l o l
my_for2([1,2,3], square) # Jedno ispod drugog:  1 4 9