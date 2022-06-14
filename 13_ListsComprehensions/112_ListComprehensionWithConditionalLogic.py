# [__for__in__]
nums=[1,2,3,4,5,6,7,8]
parninums = [x for x in nums if x%2==0]
print(parninums)


numz=[1,2,3,4,5]
doubled2=[num*2 if num%2==0 else num/2 for num in numz]
print(doubled2)


izjava="Ovo je tako zabavno!"
aeiou=''.join(char for char in izjava if char not in "aeiou")
aeiouL=[char for char in izjava if char not in "aeiou"]
print(aeiou)
print(aeiouL)

