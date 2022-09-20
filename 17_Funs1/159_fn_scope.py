# global scope

instructor = "Colt"


def say_hello():
    return f"Hello {instructor}"


print(instructor)
print(say_hello())


# local scope

def say_hello():
    instructorb = "Coltb"
    return f"Hello {instructorb}"


# print(instructorb)  # NameError: name 'instructorb' is not defined. Did you mean: 'instructor'?
print(say_hello())


# global uz promjenu unutar func

total = 0


def increment():
    global total    # samo zbog ovog radi!
    total += 1
    return total


print(increment())


name = "Rustty"


def greet():
    global name     # samo zbog ovog radi!
    name += "Steele"
    return name


print(greet())

# ali ako se ne mjenja predstavljanje netreba
name = "Rustty"


def greet():
    return name


print(greet())

#! ako imamo vise fn u hijerarhiji "nonlocal"


def outer():
    '''pokusaj da se vidi ishod doc-string-doca'''
    count = 0

    def inner():
        nonlocal count
        count += 1
        return count
    return inner()


print(outer())
print(outer.__doc__)  # ! zakljucak, dunder se poziva bez ()
