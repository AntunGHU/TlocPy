instruktor={"name":"Colt", "own-dog":True, "num_courses":4, "favourite_language":"python", "is_hilarious":False, 7:"my_fav_num"}

instruktor.clear()
print(instruktor)

instruktor={"name":"Colt", "own-dog":True, "num_courses":4, "favourite_language":"python", "is_hilarious":False, 7:"my_fav_num"}
d=instruktor.copy()
print(d)
print(d is instruktor)
print(d == instruktor)

c={}.fromkeys("a","b")
print(c)
c={}.fromkeys(["email"],"unknown")
print(c)
c={}.fromkeys("a",[1,2,3])
print(c)

new_user={}.fromkeys(['name', 'score', 'email'], 'unknown')
print(new_user)
new_user.fromkeys(['phone'], 'unknown') # vise ne modificira nego stvara novi zasebni dict
print(new_user.fromkeys(['phone'], 'unknown')) # dokaz novog posebnog
print(new_user) # dokaz ne promjenjenosti starog

new_user={}.fromkeys('name', 'unknown')
print(new_user)
new_user={}.fromkeys(range(10), 'unknown')
print(new_user)

instruktor={"name":"Colt", "own-dog":True, "num_courses":4, "favourite_language":"python", "is_hilarious":False, 7:"my_fav_num"}
print(instruktor['name'])
print(instruktor.get('name'))
print(instruktor['own-dog'])
print(instruktor.get('own-dog'))

print(instruktor.get('no-key'))
print(instruktor['no-key'])