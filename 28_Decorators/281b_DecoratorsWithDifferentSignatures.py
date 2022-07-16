# RJESENJE!!!

def my_decorator(fn):
    def wrapper(*args, **kwargs):
        # do something w/ fn(*args, **kwargs)
        pass
    return wrapper

#  nakon modifikacije dekoratora sad rade obe funkcije


def shout(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs).upper()
    return wrapper


@shout
def greet(name):
    return f"Hi, I'm {name}"


print(greet("todd"))    # HI, I'M TODD


@shout
def order(main, side):
    return f"Hi, I'd like {main} with a side of {side}, please!"


# HI, I'D LIKE BURGER WITH A SIDE OF FRIES, PLEASE!
print(order("burger", "fries"))  # GIznad


@shout
def lol():
    return "lol"


print(lol())    # LOL


# Sa ovakvim dekoratorima (*args, **kwargs) dobijamo fleksibilnost prosljedjivanja nijednog ili puno argsova, pojedinacno ili iz tupla
# "Wrapper" moze imati i drugacije ime ali je "wrapper" postao standard!
