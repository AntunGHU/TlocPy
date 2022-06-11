def extract_full_name(l):
    return list(map(lambda val: "{} {}".format(val['first'], val['last']), l))
    
names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
extract_full_name(names) # ['Elie Schoppik', 'Colt Steele']
