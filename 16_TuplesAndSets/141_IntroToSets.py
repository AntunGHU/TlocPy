# Nemaju order, index and duplicates
s0=set([1,2,3,4,5,5,5,6])
print(s0)
s1=set((1,2,3,4,5,5,5,6))
print(s1)
s2=set({1,2,3,4,5,5,5,6})
print(s2)
s3={1,2,3,4,5,5,5,6}
print(s3)
# print(s3[0])    # TypeError: 'set' object is not subscriptable

for num in s3:
    print(num)
    
# Uporaba za ozklanjanje duplikata
cities=["LosAng", "SanFran","NewYork","Tokyo", "Bejin", "SanFran", "Tokyo", "Berlin", "SanFran"]
print(cities)
print(len(cities))
print(set(cities))
print(len(set(cities)))
print(list(set(cities)))
print(len(list(set(cities))))

