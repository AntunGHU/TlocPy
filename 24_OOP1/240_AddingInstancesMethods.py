# 12'33

class User:
    
    def __init__(self, first, last, age):
        self.first=first
        self.last=last
        self.age=age
        
    def full_name(self):
        return f"{self.first} {self.last}"
    
    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."
    
    def likes(self, thing):
        return f"{self.first} likes {thing}!"
    
user1=User("Joe", "Smith", 68)
print(user1.full_name())    # Joe Smith
print(user1.initials())     # J.S.
print(user1.likes("IceCream"))  # Joe likes IceCream!


#* Tloc dodao jos dva methoda da pokaze da se atributs-values mogu mjenjati
class User:
    
    def __init__(self, first, last, age):
        self.first=first
        self.last=last
        self.age=age
        
    def full_name(self):
        return f"{self.first} {self.last}"
    
    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."
    
    def likes(self, thing):
        return f"{self.first} likes {self.thing}!"
    
    def is_senior(self):
        return self.age > 65
    
    def birthday(self):
        self.age+=1
        return f"Happy {self.age}th birthday, {self.first}!"

#* Za kraj Tloc pokazuje posljedice ne mecanja "self"-a u zagradu uz metod

    def say_hi():
        print("Hi")   
        
user1=User("Joe", "Smith", 68)
print(user1.is_senior())    # True
print(user1.birthday())     # Happy 69th birthday, Joe!
print(user1.age)            # 69
print(user1.say_hi())       # TypeError: say_hi() takes 0 positional arguments but 1 was given
        
        