def number_compare(a,b):
    if a > b:
        return "First is greater"
    elif b > a:
        return "Second is greater"
    return "Numbers are equal"
    
print(number_compare(1,1)) # "Numbers are equal"
print(number_compare(1,0)) # "First is greater"
print(number_compare(2,4)) # "Second is greater"
