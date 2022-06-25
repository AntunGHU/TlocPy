# dok je ! u naslovu pokusaj izvodjenja coda daje "bash: !.py: event not found"

def remove_negatives(nums):
    return list(filter(lambda l: l >= 0, nums))
    
    
print(remove_negatives([-1,3,4,-99]))           #[3,4]
print(remove_negatives([-7,0,1,2,3,4,5]))       #[0, 1, 2, 3, 4, 5]
print(remove_negatives([50,60,70]))             #[50,60,70]
