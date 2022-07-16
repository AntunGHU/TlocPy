# 3'26

# zelimo enforce-ati certain restrictions on arguments, npr da nema keywords-a ili brojnih argumenata

from functools import wraps


def ensure_no_kwargs(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs:
            raise ValueError("No kwargs allowed, sorry!")
        return fn(*args, **kwargs)
    return wrapper


@ensure_no_kwargs
def greet(name):
    print(f"Hi there {name}")


greet("Tony")       # Hi there Tony
greet(name="Tony")      # ValueError: No kwargs allowed, sorry!
