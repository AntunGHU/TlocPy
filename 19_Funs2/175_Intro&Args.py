# *args - spec operator we can pass to funcs, gathers remaining arguments as tuple; parametar! but we can call it we want!!

def summ_all_nums(num1, *args):
    print(num1)
    total=0
    for num in args:
        total+=num
    return total

print(summ_all_nums(4,6,9,4,10))
print(summ_all_nums(4,6))


def ensure_correct_info(*args):
    if "Colt" in args and "Steele" in args:
        return "Welcome back, Colt!"
    return "Not sure who you are..."

print(ensure_correct_info())
print(ensure_correct_info(1, True, "Steele", "Colt"))


        
