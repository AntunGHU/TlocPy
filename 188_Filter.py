users = [
    {"username":"ante", "tweets":["I love"]},
    {"username":"antun", "tweets":[]}
]

inactive_users = list(filter(lambda u:len(u['tweets'])==0, users))
inactive_users2 = list(filter(lambda u: not u['tweets'], users))
print(inactive_users)
print(inactive_users2)

#! provjeracao i uvjerio se u tocnost Colta, ali i logicno je, iterator users se iterira i daje vani prvi osnovni element a to je dict, zato je on i rezultat!