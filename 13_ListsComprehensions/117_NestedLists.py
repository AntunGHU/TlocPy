nested_list=[[1,2,3],[4,5,6],[7,8,9]]
a=nested_list[0][2]
print(a)
b=nested_list[2][2]
print(b)
c=nested_list[2][0]
print(c)

for l in nested_list:
    for val in l:
        print(val)
        
a=[[val*2 for val in l] for l in nested_list]
b=[[print(val) for val in l] for l in nested_list]
print(a)
print(b) # None... Povrsni Colt!?

board=[[num for num in range(1,4)] for val in range(1,4)]
print(board)

x0x0=[["X" if num%2 != 0 else "O" for num in range(1,4)] for val in range(1,4)]
print(x0x0)