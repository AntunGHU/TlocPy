# vraca filter objekt konvertibilan u druge data-oblike i koji se sastojim samo od iterable-items-a koji zadovoljavaju lambda-kriterij

l = [1,2,3,4]
evens = list(filter(lambda x: x % 2 == 0, l))
print(evens)    # [2, 4]


names = ["austin", "penny", "anthony", "angel", "billy"]
a_names = list(filter(lambda n: n[0]=='a', names))
print(a_names)  # ['austin', 'anthony', 'angel']


users = [
    {"username":"ante", "tweets":["I love"]},
    {"username":"antun", "tweets":[]}
]

inactive_users = list(filter(lambda u:len(u['tweets'])==0, users))
inactive_users2 = list(filter(lambda u: not u['tweets'], users))
print(inactive_users)   # [{'username': 'antun', 'tweets': []}]
print(inactive_users2)  # [{'username': 'antun', 'tweets': []}]

#! provjeracao i uvjerio se u tocnost Colta, ali i logicno je, iterator users se iterira i daje vani prvi osnovni element a to je dict, zato je on i rezultat!


#* Combining filter and map
names2 = ["Lassie", "Colt", "Rusty"]
instr = list(map(lambda name: f"Your instructor is {name}", filter(lambda value: len(value)<5, names2)))
instr2 = map(lambda name: f"Your instructor is {name}", filter(lambda value: len(value)<5, names2))
print(instr)    # ['Your instructor is Colt']
print(instr2)   # <map object at 0x7f385feebdf0>

#* What about ListComprehension
a = [f"Your instructor is {name}" for name in names2 if len(name)<5]
print(a)    # ['Your instructor is Colt']
b = [user for user in users if not user["tweets"]]
print(b)    # [{'username': 'antun', 'tweets': []}]
c = [user["username"].upper() for user in users if not user["tweets"]]
print(c)    # ['ANTUN']