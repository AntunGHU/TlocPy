# podsecanje na mjerenje brzine funkcije "sum" koristenjem LC i GE i "time"

from functools import wraps
from time import time


def speed_test(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = fn(*args, **kwargs)
        end_time = time()
        print(f"Executing {fn.__name__}")
        print(f"Time elapsed: {end_time-start_time}")
        return result
    return wrapper


@speed_test
def sum_num_gen():
    return sum(x for x in range(90000000))


@speed_test
def sum_num_list():
    return sum([x for x in range(90000000)])


print(sum_num_gen())   # Executing sum_num_gen
# ______________________ Time elapsed: 3.179565906524658 (kod Ath 5.94)
# ______________________ 4049999955000000
print(sum_num_list())  # Executing sum_num_list
# _______________________Time elapsed: 3.7200493812561035 (8.6)
# _______________________4049999955000000
