def add_and_mulpiply_numbers(a, b, c):
    return(a + b * c)
data = dict(a=1, b=2, c=3)
# data2 = dict(1="a", 2="b", 3="c") #! samo sebi dokazujem da broj ne moze biti kljuc
print(data)
print(add_and_mulpiply_numbers(**data))