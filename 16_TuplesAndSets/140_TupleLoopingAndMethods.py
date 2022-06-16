nums=(1,2,3,4)
for num in nums:
    print(num)
    
months=("Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec")
i=len(months)-1
while i>=0:
    print(months[11-i])
    i-=1
    
x=(1,2,3,3,3,)
print(x.count(1))
print(x.count(3))
print(x.index(1))
print(x.index(3))
# print(x.index(5))   # ValueError: tuple.index(x): x not in tuple

nums=(1,2,3,(4,5),6,7)
print(nums[0])
print(nums[3])
print(nums[3][1])
print(nums[0:])
print(nums[0:4])
print(nums[0:4:2])