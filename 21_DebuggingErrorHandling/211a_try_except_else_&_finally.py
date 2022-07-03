def devide(a,b):
    try:
        return a/b
    except:
        print("something went wrong...")
print(devide(1,2))  # 0.5
print(devide(1,0))  # something went wrong...
                    # None - ubog pokusaja printanja

# 2v:                    
def devide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("don't devise by zero, please...")
print(devide(1,2))  # 0.5
print(devide(1,0))  # don't devise by zero, please...

# ali posto greški moze biti jos, npr da stavimo slovo 3v:
def devide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("don't devise by zero, please...")
    except TypeError:
        print("a and b must be int or floats")
print(devide(1,2))  # 0.5
print(devide(1,0))  # don't devise by zero, please...
print(devide("br",2))# a and b must be int or floats
print(devide(2,"na"))# a and b must be int or floats

# Upotreba else-a 4v:
def devide(a,b):
    try:
        result = a/b
    except ZeroDivisionError:
        print("don't devise by zero, please...")
    except TypeError:
        print("a and b must be int or floats")
    else:
        print(f"{a} divided by {b} is {result} ")
print(devide(1,2))  # 0.5
print(devide(1,0))  # don't devise by zero, please...
print(devide("a",2))# a and b must be int or floats
print(devide(2,"b"))# a and b must be int or floats

# Prihvacanje erora as "err" 5v:
def devide(a,b):
    try:
        result = a/b
    except ZeroDivisionError:
        print("don't devise by zero, please...")
    except TypeError as err:
        print("a and b must be int or floats")
        print(err)      # unsupported operand type(s) for /: 'int' and 'str'
    else:
        print(f"{a} divided by {b} is {result} ")
print(devide(1,2))  # 0.5
print(devide(1,0))  # don't devise by zero, please...
print(devide("a",2))# a and b must be int or floats
print(devide(2,"b"))# a and b must be int or floats

# Prihvacanje više vrsta erora as u tuplu 6v:
def devide(a,b):
    try:
        result = a/b
    except (ZeroDivisionError, TypeError) as err:
        print("something went wrong...")
        print(err)      # unsupported operand type(s) for /: 'int' and 'str'
    else:
        print(f"{a} divided by {b} is {result} ")
print(devide(1,2))  # 0.5
print(devide(1,0))  # don't devise by zero, please...
print(devide("a",2))# a and b must be int or floats
print(devide(2,"b"))# a and b must be int or floats