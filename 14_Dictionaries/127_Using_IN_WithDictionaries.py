instruktor={"name":"Colt", "own-dog":True, "num_courses":4, "favourite_language":"python", "is_hilarious":False, 7:"my_fav_num"}

# provjera unutar kljuceva po defu
print("name" in instruktor)
print("awesome" in instruktor)
print("name" in instruktor.keys())
print("awesome" in instruktor.keys())

# provjera unutar value-sa  se naglasava
print("Colt" in instruktor)
print("awesome" in instruktor)
print("Colt" in instruktor.values())
print("awesome" in instruktor.values())