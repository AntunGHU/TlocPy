# 5'43

# Kad pisemo

# ? @decorator
# ? def func(*args, **kwargs):
# ?   pass

# mi kao da zapravo pisemo

# ? func= decorator(func)

# ili kad pisemo

# ? @decorator_with_args(arg)
# ? def func(*args, **kwargs):
# ?   pass

# mi kao da zapravo pisemo

# ? func= decorator_with_args(arg)(func)

# a sve smo to i vidjeli u drugoj lekciji o dekoratorima

# * pravljenje decoratora sa argumentom!!!

from functools import wraps


def ensure_first_arg_is(val):
    def inner(fn):      # pocetak standardnog deca bez arg
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if args and args[0] != val:
                return f"First arg needs to be {val}"
            return fn(*args, **kwargs)
        return wrapper
    return inner


@ensure_first_arg_is("buritto")
def fav_food(*foods):
    return foods


print(fav_food("buritto", "ice cream"))
print(fav_food("ice cream", "buritto"))


@ensure_first_arg_is(10)
def add_to_ten(num1, num2):
    return num1+num2


print(add_to_ten(10, 12))
print(add_to_ten(12, 10))
