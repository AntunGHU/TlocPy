# Map:  prima 2 argumenta: funkciju (obicno Lambda) i iterable
#       izvodi Lambdu nad svakim u iterble i vraca map-objekt koji je konvertibilan u druge data-oblike

from unicodedata import name


nums=[2,3,4,5,6,8,10]

doubles = map(lambda x: x*2, nums)

print(doubles)  # <map object at 0x7f0b59f34280>

for num in doubles:
    print(num)      # 4, 6, ...
    
print(list(doubles))    # []

print(doubles)      # <map object at 0x7f0b59f34280>

doubles = list(map(lambda x: x*2, nums))   

print(doubles)  # [4, 6, 8, 10, 12, 16, 20]



people=["Darcy", "Christin", "Dana", "Anabel"]
peeps = map(lambda name: name.upper(), people)
print(list(peeps))  # ['DARCY', 'CHRISTIN', 'DANA', 'ANABEL']



names = [
    {'first':'Rusty', 'last':'Steele'},
    {'first':'Colt', 'last':'Steele'},
    {'first':'Blue', 'last':'Steele'}
]
first_name = list(map(lambda x: x['first'], names))
print(first_name)   # ['Rusty', 'Colt', 'Blue']

# Moze se i klasicnom funkcijom ali tada imamo liniju koda vise - definiranje funkcije

def double(x): return x*2
doubles = map(double, nums)
print(list(doubles))    # [4, 6, 8, 10, 12, 16, 20]