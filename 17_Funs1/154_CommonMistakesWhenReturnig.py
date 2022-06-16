# uvlaka
def sum_odd_nums(nums):
    total=0
    for num in nums:
        if num % 2 != 0:
            total += num
        # return total  # 1 i staje sukladno recenom
    return total

print(sum_odd_nums([1,2,3,4,5,6,7,8,9]))

# nepotrebni "else"
def is_odd_num(num):
    if num % 2 != 0:
        return True
    else:
        return False
    
print(is_odd_num(9))

# jer moze i ovako
def is_odd_num(num):
    if num % 2 != 0:
        return True
    return False
    
print(is_odd_num(9))