s1=set((1,2,3,4,5,5,5,6))
print(s1)

s1.add(7)
print(s1)

s1.remove(1)
print(s1)

# s1.remove(1)    # KeyError: 1
s1.discard(1)

s2=s1.copy()
print(s2)
print(s2 is s1)

s2.clear()
print(s2)

s3={7,8,9,4,3,2}
print(s1)
print(s3)
print(s1|s3)
print(s1&s3)