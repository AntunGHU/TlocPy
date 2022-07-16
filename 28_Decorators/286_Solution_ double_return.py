# Write a function called double_return which accepts a function and returns another function. double_return should decorate a function by returning two copies of the inner function's return value inside of a list.

from functools import wraps


def double_return(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        val = fn(*args, **kwargs)
        return [val, val]
    return wrapper

# This wrapper function simply runs the function, and returns a list containing the result twice:


@double_return
def add(x, y):
    return x + y


print(add(1, 2))  # [3, 3]


@double_return
def greet(name):
    return "Hi, I'm " + name


print(greet("Colt"))  # ["Hi, I'm Colt", "Hi, I'm Colt"]
