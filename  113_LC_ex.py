list1 = ["Elic", "Tim", "Mat"]
an = [ime[0] for ime in list1]
print(an)

list2 = [1,2,3,4,5,6]
an2 = [num for num in list2 if num % 2 == 0]
print(an2)

an3 = [num for num in [1,2,3,4,5] if num in [3,4,5,6,7]]
print(an3)