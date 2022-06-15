instruktor={"name":"Colt", "own-dog":True, "num_courses":4, "favourite_language":"python", "is_hilarious":False, 7:"my_fav_num"}
print(instruktor)

#! Use .values()
print(instruktor.values())
for value in instruktor.values():
    print(value)
    
#! Use .keys()
print(instruktor.keys())
for key in instruktor.keys():
    print(key)
    
#! Use .items()
print(instruktor.items())
for key,value in instruktor.items():
    print(key,value)
    print(f"key je {key} a value je {value}")