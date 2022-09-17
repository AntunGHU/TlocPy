len("123abcd")  # 7

first_l = [1, 2, 3, 4]
first_l.append(5)
# first_l.append(5,6) # TypeError: list.append() takes exactly one argument (2 given)
print(first_l)

cofirst_l = [1, 2, 3, 4]
cofirst_l2 = [1, 2, 3, 4]
cofirst_l.extend([1, 2, 3, 4])
cofirst_l2.append([1, 2, 3, 4])
print(cofirst_l)
print(cofirst_l2)

sec_l = [1, 2, 3, 4, 5]
sec_l.insert(2, "Hi")
print(sec_l)
sec_l.insert(len(sec_l), "LAST")
print(sec_l)
sec_l.insert(-1, "TheEnd")
print(sec_l)
