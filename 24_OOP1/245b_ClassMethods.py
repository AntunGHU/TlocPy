
# mala varijacija od print na return

class User:
    
    active_users=0
    
    @classmethod
    def display_active_users(cls):
        return f"There are currently {cls.active_users} active users."
        
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
    
user1=User("Joe", "Smith", 68)
user2=User("Blanca", "Lopez", 41)
print(User.active_users)    # 2
print(User.display_active_users()) # There are currently 2 active users.
user1=User("Joe", "Smith", 68)
user2=User("Blanca", "Lopez", 41)
print(User.active_users)    # 4
print(User.display_active_users()) # There are currently 4 active users.