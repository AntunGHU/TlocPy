# print("\U0001f600")
for e in range(1, 11):
    print("\U0001f600"*e)

e = 11
while e > 0:
    print("\U0001f600"*e)
    e -= 1

#! Coltov dodatak i jako mi drag jer sam ga skroz izgubio iz glave

for x in range(3):
    for num in range(1, 11):
        print("\U0001f600"*num)

for a in range(1, 21):
    count = 1
    smiles = ""
    while count <= a:
        smiles += "\U0001f600"
        count += 1
    print(smiles)

#! na kraju kaze da za simetricnu piramidu trebamo neparne brojeve i space! Sam sam rjesio!!!

e = 1
s = 10
while e < 22 and s > 0:
    print("  "*s+"\U0001f600"*e)
    e += 2
    s -= 1
