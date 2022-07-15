# Prvo pokazuje kako bi ritam 1234 1234 rijesio sa funkcijom:
from typing import Counter


def current_beat():
    max = 100
    nums = (1, 2, 3, 4)
    i = 0
    result = []
    while len(result) < max:
        if i >= len(nums):
            i = 0
        result.append(nums[i])
        i += 1
    return result


print(current_beat())

# potom naglasava da to nije ono sto hoce jer liste uzimaju puno memorije a obzirom da trebamo samo 1 vrijednost u jednom trenutku rjesenje je ...> generator!


def gcurrent_beat():
    nums = (1, 2, 3, 4)
    i = 0
    while True:
        if i >= len(nums):
            i = 0
        yield nums[i]
        i += 1


counter = gcurrent_beat()
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
