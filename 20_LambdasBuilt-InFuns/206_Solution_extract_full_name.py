# Write a function called extract_full_name. This function should accept a list of dictionaries and return a new list of strings with the first and last name keys in each dictionary concatenated.
# I use map and a lambda to create a new list full of formatted strings:

def extract_full_name(l):
    return list(map(lambda val: f"{val['first']} {val['last']}", l))
    
names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
print(extract_full_name(names)) # ['Elie Schoppik', 'Colt Steele']
