# This exercise is a little harder than the previous make_noise  function.
# Write a function called generate_evens  that returns a list of the even numbers between 1 and 50(not including 50).
# Basically, it should return a list: [2,4,6... all the way up to 48]
# Inside the function, you can construct the list using either a loop OR list comprehension.
# You do not need to call the function in this exercise, defining it is enough.

def generate_evensLC():
    return [x for x in range(1, 50) if x % 2 == 0]


print(generate_evensLC())


# Generating evens using a loop:

def generate_evensL():
    result = []
    for x in range(1, 50):
        if x % 2 == 0:
            result.append(x)
    return result


print(generate_evensL())
