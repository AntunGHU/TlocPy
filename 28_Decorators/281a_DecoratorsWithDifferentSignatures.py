# 4'27

def shout(fn):
    def wrapper(name):
        return fn(name).upper()
    return wrapper


@shout
def greet(name):
    return f"Hi, I'm {name}"


print(greet("todd"))    # HI, I'M TODD

# u gornjem primjeru greet fn ima jedan parametar i wrapper  koji treba dekorirati fn prima takodjer jedan tako da u tjeku dekoracije nema problema, wrapper ocekivao 1 i dobio jedan. ALI!
# ako funkcija koju zelimo dekorirati ima 2 parametra?


@shout
def order(main, side):
    return f"Hi, I'd like {main} with a side of {side}, please!"


# TypeError: wrapper() takes 1 positional argument but 2 were given
print(order("burger", "fries"))  # GIznad


# RJESENJE!!!

def my_decorator(fn):
    def wrapper(*args, **kwargs):
        # do something w/ fn(*args, **kwargs)
        pass
    return wrapper
