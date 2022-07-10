# 7'41

#? _name
class Person:
    def __init__(self):
        self.name="Tony"
        self._secret="Hi"
p=Person()
print(p.name)       # Tony
print(p._secret)    # Hi
#* Iako ih nema u zagradi, atributi ipak rade! al ce biti isti za sve instance. _secret's 1 _ privatizira atribut po konvenciji ali ne prijeci! Ne pristupati mu izvanjski nego samo u okviru klase!!!

#? __name (mangeling-kvarenje)
class Person:
    def __init__(self):
        self.__msg="I like you!"
p=Person()
# print(p.__msg)  # AttributeError: 'Person' object has no attribute '__msg'
#* __msg's front dunder kvari standardni pokusaj nalazenja njegove vrijednosti cime ga trajno čini atributom samo te klase (da bi mu se dobila vrijednost mora se ispred navesti ime klase). Time sprijecavamo njegovo redefiniranje istoimenim (u kratkoj formi __msg) do kojeg moze doci slucajno pri inheritanceu klasa!
print(dir(p))   # ['_Person__msg', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
print(p._Person__msg) # I like you!

#? __name__
#* Py specific i nebi ga trebalo dirati i redefinirati!