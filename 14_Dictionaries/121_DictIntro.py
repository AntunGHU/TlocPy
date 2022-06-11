dict1 = dict(name="kitty", age=4)
print(dict1)                # {'name': 'kitty', 'age': 4}

# list1 = list(2, "kitty", "age", 4)
# print(list1)                # TypeError: list expected at most 1 argument, got 4

#! morao sam podvuci ovu nedosljednost
list2 = list((2, "kitty", "age", 4))
print(list2)      