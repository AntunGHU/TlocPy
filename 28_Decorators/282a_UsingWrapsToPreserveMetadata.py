# 4'34
def log_func_data(fn):
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

# za sada sve super, ali kad pokusamo istrazivati dokumentaciju "fn"-a na samostalan nacin u odgovor uskace doc od wrapper-a!?!?
print(add.__name__)  # wrapper
print(add.__doc__)  # I AM WRAPPER FUNCTION
print(help(add))   # help on function wrapper in module __main__:
#____________________wrapper(*args, **kwargs)
# ___________________    I AM WRAPPER FUNCTION
# ___________________(END)

# spasava modul "functools" koji cuva metapodatke dekorirane funcije
