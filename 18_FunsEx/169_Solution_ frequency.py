def frequency(collection, searchTerm):
    return collection.count(searchTerm)


print(frequency([1, 2, 3, 4, 4, 4], 4))  # 3
print(frequency([True, False, True, True], False))  # 1
print(frequency([1, 2, 3, 4, ], 4))  # 1
print(frequency([True, False, True, True], True))  # 3
print(frequency("riba ribi grize rep", " "))  # 3
