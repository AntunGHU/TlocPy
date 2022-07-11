# 7'01

# -Inheritance(+multiple inheritance), -method resolution order_MRO, -polymorfizam, -special methods
# I je key-osobina OOP koja omogucava definiranje nove klase kroz nasljedjivanje!

class Animal:
    def make_sound(self, sound):
        print(f"This animal says {sound}.")
    cool = True
    
class Cat(Animal):
    pass

blue = Cat()
print(blue.make_sound('MEOW'))  # This animal says MEOW.
print(blue.cool) # True
print(Cat.cool) # True
print(Animal.cool)  # True

# provjera instanci s builtin func "instance"
print(isinstance(blue, Cat))    # True
print(isinstance(blue, Animal)) # True
print(isinstance(blue, object)) # True
