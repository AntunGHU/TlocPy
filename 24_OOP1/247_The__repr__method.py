# 3'02

# way to provide a nicer string representation (__str__ ili __format__). Bez __repr__ kad printamo instancu dobijemo ala <__main__User...>

class Human:
    def __init__(self, name="somebody"):
        self.name=name
    def __repr__(self):
        return self.name
    
dude = Human()
print(dude)
colt = Human(name="Colt Steele")
print(f"{colt} is totaly rad probably!") # Colt Steele is totaly rad probably!