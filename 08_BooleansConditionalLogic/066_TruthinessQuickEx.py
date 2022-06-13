x = 1
print(x is 1)   #! SyntaxWarning: "is" with a literal. Did you mean "=="?
print(x is 0)

if 0:
    print("AA")
if 1:
    print("EE")
    
animal = input("Unesi omiljenu biljku: \n")

if animal:
    print(animal + " je moja omiljena takodjer!")