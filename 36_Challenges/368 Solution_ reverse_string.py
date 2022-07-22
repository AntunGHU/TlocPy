# Write a function called reverse_string which accepts a string and returns a new string with all the characters reversed.

def reverse_string(str):
    s = ''
    for i, char in enumerate(str[::-1]):
        s += char
    return s


print(reverse_string('awesome'))  # 'emosewa'
print(reverse_string('Colt'))  # 'tloC'
print(reverse_string('Elie'))  # 'eilE'
