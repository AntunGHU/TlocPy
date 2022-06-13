
#! Start
print(f"********Start***********")
prva=[1,2,3,4,5]
a=prva[1:]
print(a)
print(prva) # slicing ne dira objekt slicanja, not in place

b=prva[20:]
print(b)

c=prva[-3:]
print(c)

#! Kraj
print(f"********Kraj***********")
prva=[1,2,3,4,5]
a=prva[:2]
print(a)

b=prva[:4]
print(b)

c=prva[1:3]
print(c)

d=prva[:-1]
print(d)

e=prva[1:-1]
print(e)

#! Step
print(f"********Step***********")
prva=[1,2,3,4,5,6]
a=prva[1::2]
print(a)

b=prva[::2]
print(b)

c=prva[1::-1]
print(c)

d=prva[:1:-1]
print(d)

e=prva[2::-1]
print(e)

#! SlicingTricks
print(f"*******Tricks************")
strings="This is very, very fun!"
a=strings[::-1]
print(a)

#! Modifying portions of list
print(f"******Modifying portions of list")
nums=[1,2,3,4,5,]
nums[1:3]=["a","b","c","d"]
print(nums)

colors=["red", "green", "blue", "yellow"]
colors[1]=colors[1][::-1]
print(colors)

print("hellouu"[0])
print("hellouu"[:4])
print("hellouu"[::3])
