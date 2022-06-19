# Using * as an Argument ili ArgumentUnpacking: "unpacks values"

def sum_all_values(*args):
    print(args)
    total=0
    for num in args:
        total+=num
    print(total)
    
sum_all_values(1,30,2,5,6) # 44

# ali!! ako imamo tuple ili listu brojeva npr a=(1,2,3,4,5,6) ili b=[1,2,3,4,5,6] i pokusamo: 
# sum_all_values(a)  ili  sum_all_values(b) dobijemo grešku!!!  I tu u pomoc stize *
a=(1,2,3,4,5,6)
b=[1,2,3,4,5,6]
sum_all_values(*a) # 21
sum_all_values(*b) # 21
# sum_all_values(a) # 21 TypeError: unsupported operand type(s) for +=: 'int' and 'tuple'
# sum_all_values(b) # 21 TypeError: unsupported operand type(s) for +=: 'int' and 'tuple'