dani = {1 : "pon", 2:"uto", 3:"sri", 4:"cet", 5:"pet", 6:"sub", 7:"ned"}

def dan(br):
    if br in dani:  # varijabla je globalna ali je func ne mjenja pa ide!
        return dani[br]
    return None
print(dan(2))
print(dan(1))
print(dan(7))
print(dan(22))


def danii(br):
    dan = {1 : "pon", 2:"uto", 3:"sri", 4:"cet", 5:"pet", 6:"sub", 7:"ned"}
    if br in dan: 
        return dan[br]
    return None
print(danii(2))
print(danii(1))
print(danii(7))
print(danii(22))
