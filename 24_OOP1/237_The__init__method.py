# 7'28

## method koji dolazi uz gotovo (ne ide uz rijetke klase koje imaju samo methode) svaku klasu i kojeg Py automatski izvodi!

class User:
    def __init__(self):
        print("NEW USER HAS BEEN BORN!")
        
user1=User()    # NEW USER HAS BEEN BORN!
user2=User()    # NEW USER HAS BEEN BORN!
user3=User()    # NEW USER HAS BEEN BORN!

## umjesto automatskog print-a, u stvarnosti uz init ide inicijalizacija osnovnih atributa, npr prvog imena (first)

class User:
    def __init__(self, first): #self loopa atribut first instanci
        self.name=first
        
user1=User("joe")
print(user1.name)   # joe

## prosirenje i isticanje da ime atributa je ono sto stoji uz self (obicno = onom u definicijskoj zagradi!)

class User:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        
user1=User("Joe", "Smith", 68)
user2=User("Blanca", "Lopez", 41)
print(user1.first, user1.last, user1.age)   # Joe Smith 68
print(user2.first, user2.last, user2.age)   # Blanca Lopez 41