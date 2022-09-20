def devide(a,b):
    try:
        total = a / b
    except TypeError:
        return "Please provide two integers or floats"
    except ZeroDivisionError:
        return "Please do not divide by zero"
    return total

# Write a function called divide, which accepts two parameters (you can call them num1 and num2). The function should return the result of num1 divided by num2. If you do not pass the correct amount of arguments to the function, it should return the string "Please provide two arguments". If you pass as the second argument a 0, Python will raise a ZeroDivisionError, so if this function is invoked with a 0 as the value of num2, return the string "Please do not divide by zero"

    # Examples
    
# print(devide(4,2))  # 2
print(devide(1,2,3)) # "Please provide two integers or floats"
                     # "TypeError: devide() takes 2 positional arguments but 3 were given"
# print(devide(1,0)) # "Please do not divide by zero"
