# 8'55

# *Generatori su Iteratori *G se kreiraju s "gen-expr" ili "gen-func" *G's func yield-a
# Gen-Functions:    -Od obicnih se razlikuju u koristenju "yield"-keyworda
                  # -Obicne sve returnaju odjednom, genfunc yield-aju vise puta
                  # -Obicne returnaju "value" a genfunc yield-aju "generator"!
                  
def count_up_max(max):
    count = 1
    while count <= max:
        yield count
        count += 1
        
print(count_up_max(5))  # <generator object count_up_max at 0x0000025CFA459510>
counter = count_up_max(5)
print(counter)          # <generator object count_up_max at 0x0000025CFA459510>
print(next(counter))    # 1
print(next(counter))    # 2
print(next(counter))    # 3
print(next(counter))    # 4
print(next(counter))    # 5
# print(next(counter))    # StopIteration
#? print(counter())        # TypeError: 'generator' object is not callable
#? print(help(counter))    
#? Help on generator object:
#? 
#? count_up_max = class generator(object)
#?  |  Methods defined here:
#?  |
#?  |  __del__(...)
#?  |
#?  |  __getattribute__(self, name, /)
#?  |      Return getattr(self, name).
#?  |
#?  |  __iter__(self, /)
#?  |      Implement iter(self).
#?  |
#?  |  __next__(self, /)
#?  |      Implement next(self).
#?  |
#?  |  __repr__(self, /)
#?  |      Return repr(self).
#? -- More  --

# Kako bi istaknuli "pamcenje" generatora i nastavljanje vidi primjere dalje
counter = count_up_max(10)
for num in counter:
    print(num)              # 1,2,...9,10 jedno ispod drugog
    
# ali ako sada ovako!
counter = count_up_max(10)
next(counter)   # bez printanja ali 1
next(counter)   # bez printanja ali 2
next(counter)   # bez printanja ali 3
for num in counter: 
    print(num)  # dokaz pamcenja!!! nastavlja sa 4,5...9,10 