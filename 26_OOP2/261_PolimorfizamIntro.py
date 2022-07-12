# 6'41

# Idea: object can take many (poly) forms (morph).
# Dvije vazne prakticne primjene:
    # isti class-method radi slicno za razlicite klase:
        # Cat.speak()   # meow
        # Dog.speak()   # woof
        # Human.speak() # yo
    # isti operacija radi za razlicite vrste objekata:
        # sample_list = [1,2,3]         len(sample_list)
        # sample_tuple = [1,2,3]        len(sample_tuple)
        # sample_string = [1,2,3]       len(sample_string)
# Polymorphisam & Inheritance:
    # ista operacija radi za razlicite vrste objekata:
print(8+2)      # 10
print("8"+"2")  # 82
    # isti class-method radi slicno za razlicite klase, npr: parenth method overriden by method of subclasses - METHOD OVERRIDDING (svaka subclassa ima razlicitu implementaciju methoda!)
    
class Animal:
    def speak(self):
        raise NotImplementedError("Subclass needs to implement this method")

class Dog(Animal):
    def speak(self):
        return "woof"
    
class Cat(Animal):
    def speak(self):
        return "meuw"
    
class Fish(Animal):
    pass

d = Dog()
print(d.speak())    # woof
f = Fish()
print(f.speak())    # NotImplementedError: Subclass needs to implement this method

# Sve ovo se omagucava spesijalnim methodama ili dunderima koji daju upute Py-u kako postupati s razlicitim objektima
# Najava implementacije vlastitih verzija dundera! Vidi v.263
       