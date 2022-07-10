# 4:44

# ClassAtr(v Variables) & ClassMethods koriste se puno (100x) rjedje od instancnih
# Prave se bez "self" s pozivanjem uz navodjenje imena klase na pocetku

class User:
    
    active_users = 0
    
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1
        
    def logout(self):
        User.active_users -= 1
        return f"{self.first} has logged out!"
    
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
    
print(User.active_users)    #  0
user1=User("Joe", "Smith", 68)
print(User.active_users)    #  1
print(user1.logout())
print(User.active_users)    #  0
