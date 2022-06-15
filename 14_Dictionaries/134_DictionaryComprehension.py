
#! {__:__for__in__}

#* Iterates over keys po def-u, za iter over k,v use .items()
nums=dict(first=1, second=2, third=3)
nums_na_kv={k:v**2 for k,v in nums.items()}
print(nums_na_kv)

str1='ABC'
str2='123'
combo={str1[i]:str2[i] for i in range(len(str1))}
print(combo)

instructor={'name':'colt', 'city':'sanfrancisco', 'color':'purple'}
yelling_instructor={k.upper():v.upper() for k,v in instructor.items()}
print(yelling_instructor)

#* Comprehension w/ ConditionalLgic
num_list=[1,2,3,4]
a={num:'even' if num%2==0 else 'odd' for num in num_list }
print(a)
yelling_instructor={k.upper() if k is 'color' else k:v.upper() for k,v in instructor.items()}
print(yelling_instructor)
