# sort() samo za liste a sorted() za sve druge iterablese
more_numbers = [6,1,8,2]
print(sorted(more_numbers)) # [1, 2, 6, 8]
print(more_numbers)     # [6, 1, 8, 2]  not in place

more_numbers.sort()
print(more_numbers)     # [1, 2, 6, 8]  in place

more_numbers = [6,1,8,2]
print(sorted(more_numbers, reverse=True)) # [8, 6, 2, 1]

print(sorted((2,1,45,26,99)))  # [1, 2, 26, 45, 99] to list od tupl


# sortanje lista sa dictima
users = [
    {"username":"samuel", "tweets":["I love", "Eva"]},
    {"username":"jeff", "tweets":[], "color":"purple"}
]
a = sorted(users, key=len)
print(a)    # [{'username': 'samuel', ...
b = sorted(users, key=lambda user:user['username'])
print(b)    # [{'username': 'jeff', ...
c = sorted(users, key=lambda user: len(user['tweets']))
print(c)    # [{'username': 'jeff', ...
d = sorted(users, key=lambda user: len(user['tweets']), reverse=True)
print(d)    # [{'username': 'samuel', ...