# 8'40

# Kombiniramo Inheritance i dunder-redefinicije kako bi dobili GrumpyDict: "NONE OF YOUR BUSSINESS!" + pravi odgovor! Ili "Why do you always have to change things? Ugh, fine, setting "city to "SF", "THAT THING YOU WANT ISN'T HERE!".  Znaci, pravi dict + malo humora prije odrade! :-). 

class GrumpyDict(dict):
    def __repr__(self):          #? ne treba __init__ jer ga uzimamo od dict-a
        print("NONE OF YOUR BUSSINESS!") #? HUMORNI DIO
        return super().__repr__()           #? dict-dio
    
data = GrumpyDict({"first":"Tom", "animal":"cat"})
print(data) # NONE OF YOUR BUSSINESS! {'first': 'Tom', 'animal': 'cat'}

# potom dodajemo u Grampydef __missing__ i __setitem__ uz malo humora

class GrumpyDict(dict):
    def __repr__(self):          #? ne treba __init__ jer ga uzimamo od dict-a
        print("NONE OF YOUR BUSSINESS!") #? HUMORNI DIO
        return super().__repr__()           #? dict-dio
    
    def __missing__(self, key):
        print(f"YOU WANT {key}, WELL, IT ISN'T HERE!")
        
    def __setitem__(self, key, value):
        print(f"YOU WANT TO CHANGE DICTIONARY!")
        print(f"OK, FINE!")
        super().__setitem__(key, value)
        
    def __contains__(self, item):
        print("NO, IT ISN'T HERE!")
        return False
        
data = GrumpyDict({"first":"Tom", "animal":"cat"})
print(data) # NONE OF YOUR BUSSINESS! {'first': 'Tom', 'animal': 'cat'}
data['city']='Tokyo'
print(data) # YOU WANT TO CHANGE DICTIONARY!; OK, FINE!; NONE OF YOUR BUSSINESS!; {'first': 'Tom', 'animal': 'cat', 'city': 'Tokyo'}
'city' in data  # NO, IT ISN'T HERE!