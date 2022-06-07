def frequency(collection, searchTerm):
    return collection.count(searchTerm)
    
frequency([1,2,3,4,4,4], 4) # 3
frequency([True, False, True, True], False) # 1
frequency([1,2,3,4,], 4) # 3
frequency([True, False, True, True], True) # 1
