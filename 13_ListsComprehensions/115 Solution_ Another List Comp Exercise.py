# For all the numbers between 1 and 100(including 100), create a variable called answer, which contains a list with all the numbers that are divisible by 12.  (12, 24, etc)
# USE A LIST COMPREHENSION.

answer = [val for val in range(1,101) if val % 12 == 0]
print(answer)

answer=[]
for val in range(1,101):
    if val%12==0:
        answer.append(val)
print(answer)
