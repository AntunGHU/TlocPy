# Given a list ["Elie", "Tim", "Matt"], create a variable called answer, which is a new list containing the first letter of each name in the list.  I would use a list comprehension, though you could also loop over manually.

answer = [person[0] for person in ["Elie", "Tim", "Matt"]]
print(answer)

answer=[]
for ime in ["Elie", "Tim", "Matt"]:
    answer.append(ime[0])
print(answer)

# Given a list [1,2,3,4,5,6], create a new variable called answer2, which is a new list of all the even values.  Another good candidate for a list comp.

answer2 = [val for val in [1,2,3,4,5,6] if val % 2 == 0]
print(answer2)

answer2=[]
for val in [1,2,3,4,5,6]:
    if val%2==0:
        answer2.append(val)
print(answer2)
