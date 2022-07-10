# 6'43

#* @classmethod

# ala konvencija za polozaj unutar koda klase ne postoji (kao npr za __init__ za kog je normalno odmah na vrhu) ali ath edukativno bira staviti ih na vrh. Pošto je istakao kako se rijetko koriste, mislim da onda zasluzuju da se i oni stavljaju na vrh vrhova!

class User:
    
    active_users=0
    
    @classmethod
    def display_active_users(cls):
        print(cls)
        
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

print(User.display_active_users())  # None # jasnije da se poziva class-metod
user1.display_active_users()    # <class '__main__.User'>