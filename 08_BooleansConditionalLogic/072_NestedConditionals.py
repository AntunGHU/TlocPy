# ask for age
# 18-21 narukvica
# 21 pice i normalan ulaz
# > 18, premlad, nema ulaza

age = int(input("Kolko si star? \n"))

if age < 18:
    print("premlad, nema ulaza")
elif 18 <= age <= 21:
    print("narukvica")
else:
    print("pice i normalan ulaz")
