# Create a function running_average that returns a function. When the function returned is passed a value, the function returns the current average of all previous function calls. You will have to use closure to solve this. You should round all answers to the 2nd decimal place.

def running_average():
    running_average.accumulator = 0
    running_average.size = 0

    def inner(number):
        running_average.accumulator += number
        running_average.size += 1
        return running_average.accumulator / running_average.size

    return inner


rAvg = running_average()
print(rAvg(10))  # 10.0
print(rAvg(11))  # 10.5
print(rAvg(12))  # 11

rAvg2 = running_average()
print(rAvg2(1))  # 1
print(rAvg2(3))  # 2
