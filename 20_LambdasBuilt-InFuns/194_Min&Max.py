from unicodedata import name


print(max(3,6,7,99))
print(max("c", "d", "a"))
print(max([3,6,701,99]))
print(max((3,6,70,9)))
print(max("awesome"))
print(max({1:"a", 3:"c", 2:"b"}))

nums = [40,32,6,5,10]
print(max(nums))
print(min(nums))

# sa stringovima nije jednostavno
names=["Arya", "Samson", "Dora", "Tim", "Olivander"]
print(max(names))   # Tim
print(min(names))   # Arya
# ni sa len ne ide!
a = min(len(name) for name in names)
print(a) # 3
# rjesenje je lambda
b = min(names, key=lambda n: len(n))
print(b) # Tim
c = max(names, key=lambda n: len(n))
print(c)  # Olivander

# Primjer sa list dict
songs = [
    {"title":"happy", "playcount":1},
    {"title":"survive", "playcount":6},
    {"title":"YMCA", "playcount":99},
    {"title":"toxic", "playcount":31}
]
d = max(songs, key=lambda s: s['playcount'])
print(d)
e = min(songs, key=lambda s: s['playcount'])
print(e)
# samo naslov
f = max(songs, key=lambda s: s['playcount'])['title']
print(f)
g = min(songs, key=lambda s: s['playcount'])['title']
print(g)

# loop-nacin
max = 0
for song in songs:
    if song['playcount']>max:
        max = song['playcount']
print(max)