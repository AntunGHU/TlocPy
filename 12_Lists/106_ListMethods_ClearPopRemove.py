first_l=[1,2,3,4]
first_l.clear()
print(first_l)

first_l=[1,2,3,4]
d=first_l.pop()
print(d)
print(first_l)

first_l=[1,2,3,4]
d=first_l.pop(1)
print(d)
print(first_l)

first_l=[1,2,3,4,4,4]
first_l.remove(4)
print(first_l)
first_l.remove(5)   # ValueError: list.remove(x): x not in list
