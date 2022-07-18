# 8'56

# ant
# with "assert" keyword
# assert accepts expression
# vraca "None" if expression True
# raises an "AssertionError" if expr. False
# accepts optional error msg as 2. argument
# not best solution nowdays, there are better as unit-test

# slides
# ? Assertions
# ? We can make simple assertions with the assert keyword
# ? assert accepts an expression
# ? Returns None if the expression is truthy
# ? Raises an AssertionError if the expression is falsy
# ? Accepts an optional error message as a second argument

def add_positive_numbers(x, y):
    assert x > 0 and y > 0, "Both nums must be positive!"
    return x+y


print(add_positive_numbers(1, 1))  # 2
# AssertionError: Both nums must be positive!
# print(add_positive_numbers(1, -1))  # Gore


# Malo REPL-anja
# ? >>> assert 4==4

# ? >>> assert 4==2
# ? Traceback (most recent call last):
# ?   File "<stdin>", line 1, in <module>
# ? AssertionError

# ? >>> assert 4==2, "4 should not equal 2!!!"
# ? Traceback (most recent call last):
# ?   File "<stdin>", line 1, in <module>
# ? AssertionError: 4 should not equal 2!!!

def eat_junk(food):
    assert food in ["pizza", "ice cream", "candy",
                    "fried butter"], "food must be a junk-food"
    return f"NJAM, NJAM I am eating {food}"


food = input("ENTER FOOD, PLEASE: ")
print(eat_junk(food))

# ? ENTER FOOD, PLEASE: pizza
# ? NJAM, NJAM I am eating pizza

# ? ENTER FOOD, PLEASE: apple
# ? Traceback (most recent call last):
# ?   File "/home/antun/Documents/aCod/TlocPy/29_TestingWithPy/2?    95_Assertions.py", line 40, in <module>
# ?     print(eat_junk(food))
# ?   File "/home/antun/Documents/aCod/TlocPy/29_TestingWithPy/2?95_Assertions.py", line 34, in eat_junk
# ?     assert food in ["pizza", "ice cream", "candy",
# ? AssertionError: food must be a junk-food

# Assertions Warnings:
# _____If .py file with assertion is run with -O flag, assertions will not be evaluated!! Zato ne pisati kod ala! (prekidac-veliko O se pise u komsndu za izvrsenje .py fajla npr)
# /bin/python3 - O /home/antun/Documents/aCod/TlocPy/29_TestingWithPy/295_Assertions.py


def do_something_bad(user):
    assert user.is_admin == True, "Only admins can do the bad things!"
    # destroy a bunch of stuff()    # sudo code
    return "Muu ha ha ha!"


print(do_something_bad("Antun"))

# ? Traceback (most recent call last):
# ?   File "/home/antun/Documents/aCod/TlocPy/29_TestingWithPy/295_Assertions.py", line 64, in <module>
# ?     print(do_something_bad("Antun"))
# ?   File "/home/antun/Documents/aCod/TlocPy/29_TestingWithPy/295_Assertions.py", line 59, in do_something_bad
# ?     assert user.is_admin == True, "Only admins can do the bad things!"
# ? AttributeError: 'str' object has no attribute 'is_admin'
