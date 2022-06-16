nums=(1,2,3,4)
print(3 in nums)
print(nums[0])
b=tuple((5,6,7,8)) # samo dict prima vise argsova, tuple, list, set samo jedan
print(b)
# nums[0]="drug"  # TypeError: 'tuple' object does not support item assignment
print(type(nums))

# tuples kao keys in dict
location = {
    (35.6, 39.6):"Tokyo",
    (75.6, 68.6):"Blabla"
}
print(location)
