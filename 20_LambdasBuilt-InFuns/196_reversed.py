# reversed vraca obrnuti svaki iter ali ne in place, dok reverse() in place list-iter

nums = [1,2,3,4]
nums.reverse()
print(nums)     # [4, 3, 2, 1]  in place

nums2 = [1,2,3,4]
a = reversed(nums2)
print(a)    # <list_reverseiterator object at 0x7f129fc2c2e0>
print(list(a))  # [4, 3, 2, 1]
print(nums2)    # [1,2,3,4]     not in place

nums3 = (1,2,3,4)
a = reversed(nums3)
print(a)    # <reversed object at 0x7f001b84ffa0>
print(list(a))  # [4, 3, 2, 1]
print(nums3)    # [1,2,3,4]     not in place


# primjenjiv i na string
b = reversed("hello")
print(b)    # <reversed object at 0x7f95047a42e0>
print(list(b))  # ['o', 'l', 'l', 'e', 'h'] # jednokratno!
c = "".join(list(reversed("hello")))
print(c)    # olleh
print("hello"[::-1])    # olleh

for char in reversed("Hello World!"):
    print(char)
    
for x in reversed(range(10)):
    print(x)