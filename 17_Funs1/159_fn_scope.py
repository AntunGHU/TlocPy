from functools import total_ordering

total = 0
def increment():
    global total
    total += 1
    return total

print(increment())

name = "Rustty"
def greet():
    global name
    name += "Steele"
    print(name)
    
greet()

#! dakle, da bi varijabla definirana van funkcije mogla biti mjenjana, mora se ipak predstaviti i u funkciji sa posebnim predstavljanjem "global"

#! ali ako se ne mjenja predstavljanje netreba

name = "Rustty"
def greet():
    print(name)
    
greet()

#! ako imamo vise fn u hijerarhiji "nonlocal"

def outer():
    '''pokusaj da se vidi ishod doc-string-doca'''
    count = 0
    def inner():
        nonlocal count
        count +=1
        return count
    return inner()

print(outer())
print(outer.__doc__)    #! zakljucak, dunder se poziva bez ()
