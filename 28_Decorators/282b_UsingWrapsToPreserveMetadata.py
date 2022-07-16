# spasava modul "functools" koji cuva metapodatke dekorirane funcije

from functools import wraps


def my_decorator(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        # do some stuff with fn(*args, **kwargs)
        pass
    return wrapper

# za nasu funkciju to bi bilo


def log_func_data(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        """I AM WRAPPER FUNCTION
        """
        print(f"you are about to call {fn.__name__}")
        print(f"Here'e the documentation: {fn.__doc__}")
        return fn(*args, **kwargs)
    return wrapper


@log_func_data
def add(x, y):
    """Adds two numbers together.
    """
    return x+y


print(add(10, 20))  # 30 # you are about to call add
# _____________________Here'e the documentation: Adds two numbers together.

# i sada kad pokusamo istrazivati dokumentaciju "fn"-a na samostalan nacin u odgovor vise ne uskace doc od wrapper-a!!!!

print(add.__name__)  # add
print(add.__doc__)  # Adds two numbers together.
print(help(add))   # Help on function add in module __main__:
#__________________add(x, y)
# __________________    Adds two numbers together.
# __________________(END)
