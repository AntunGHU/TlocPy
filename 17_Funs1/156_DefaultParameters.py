def exponent(num,power):
    return num**power

print(exponent(2,3))
print(exponent(3,2))
# print(exponent(2))  # TypeError: exponent() missing 1 required positional argument: 'power'

# ali ovako moze 
def exponent(num,power=4):
    return num**power

print(exponent(2,3))
print(exponent(2))
print(exponent(4))

def add(a=5, b=10):
    return a+b

print(add(10,20))
print(add(10)) # a=10 prvi argument prvi uzima ako se dalo
print(add())

# Uvjezbavamo s Coltom
def show_info(first_name="Colt", is_instructor=False):
    if first_name=="Colt" and is_instructor:
        return "Welcome back instructor Colt!"
    elif first_name == "Colt":
        return "I really tought you were an instructor..."
    return f"Hello {first_name}!"
print(show_info())
print(show_info(is_instructor=True))
print(show_info("Molly"))

# def parametar moze biti bilo sto: broj, string, funkcija cak!
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def math(a,b,fun=add):      # namjerno stavio fun zbog nedorazumjena fn-a ranije
    return fun(a,b)

print(math(2,20))
print(math(2,20,sub))

#! brisanje terminala i s njime alociranih varijabli jako bitno! inace pokaze gresku koje nema!!!

