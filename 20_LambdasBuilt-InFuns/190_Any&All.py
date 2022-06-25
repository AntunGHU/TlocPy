# all vraca True ako su svi u iterable thruty ili je prazan

print(all([])) # True
print(all([0,1,2,3]))
print(all([char for char in 'eio' if char in 'aeiou']))
print(all([num for num in [4,2,10,6,8] if num%2==0]))
print(all(num%2==0 for num in [4,2,10,6,8]))
people=["Charlie", "Casey", "Cady", "Carly", "Christian"]
print(all([name[0]=="C" for name in people]))

# # all vraca True ako je bar 1 u iterable thruty, ako je prazan False
print(any([]))
print(any(num%2==1 for num in [4,2,10,6,8]))
print(any(num%2==1 for num in [4,2,10,6,8,7]))

