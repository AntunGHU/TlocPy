# [__for__in__]
nums = [1, 2, 3]
nums10 = [x*10 for x in nums]
print(nums10)


numz = [1, 2, 3, 4, 5]

doubled = []
for num in numz:
    # double=num*2
    doubled.append(num*2)
print(doubled)

doubled2 = [num*2 for num in numz]
print(doubled2)


name = "colt"
name_upper = [char.upper() for char in name]
print(name_upper)

friends = ["stipo", "marko", "mira"]
friends_VP = [(ime[0].upper()+ime[1:]) for ime in friends]
friends_SVP_colt = [ime[0].upper() for ime in friends]
print(friends_VP)
print(friends_SVP_colt)

num_from_range = [num*10 for num in range(1, 6)]
print(num_from_range)

bool_l = [bool(val) for val in [0, [], '', 1, "", "a", {}]]
print(bool_l)

brzastr = [1, 2, 3, 4]
brstr = [str(br) for br in brzastr]
print(brstr)

num_za_H = [1, 2, 3, 4]
brstrHELLO = [str(br) + "HELLO" for br in num_za_H]
print(brstrHELLO)
