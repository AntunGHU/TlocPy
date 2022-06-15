d=dict(a=1, b=2, c=3)
print(d)

# d.pop() # TypeError: pop expected at least 1 argument, got 0
# d.pop('e') # KeyError: 'e'

d.pop('a')
print(d)

d=dict(a=1, b=2, c=3, d=4, e=5)
print(d)

d.popitem() # Brise slucajni odabir
print(d)
d.popitem() # Brise slucajni odabir koji je "slucajno" uvjek zadnji?!
print(d)
d.popitem() # Brise slucajni odabir?
print(d)
d.popitem() # Brise slucajni odabir????
print(d)
d.popitem() # Brise slucajni odabir?
print(d)
# d.popitem('e') # TypeError: dict.popitem() takes no arguments (1 given)

first=dict(a=1, b=2, c=3, d=4, e=5)
print(first)
second={}
second.update(first)
print(second)

second['a']='amazing'
print(second)

first.update(second)
print(first)
first.update({})
print(first)