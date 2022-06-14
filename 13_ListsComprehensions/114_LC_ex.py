an1 = [num for num in [1,2,3,4,5] if num in [3,4,5,6,7]]
print(an1)

an1 = []
for x in [1,2,3,4,5]:
    if x in [3,4,5,6,7]:
        an1.append(x)
print(an1)

list1 = ["Elic", "Tim", "Mat"]

answer1 = [item[::-1].lower() for item in list1 ]
print(answer1)

answer1 = []
for name in list1:
    answer1.append(name[::-1].lower())
print(answer1)
