# Write a function called is_palindrome. A Palindrome is a word, phrase, number, or other sequence of characters which reads the same backward or forward. This function should take in one parameter and returns True or False depending on whether it is a palindrome. As a bonus, allow your function to ignore whitespace and capitalization so that is_palindrome('a man a plan a canal Panama') returns True.


def is_palindrome(string):
    return string == string[::-1]


print(is_palindrome('testing'))  # False
print(is_palindrome('tacocat'))  # True
print(is_palindrome('hannah'))  # True
print(is_palindrome('robert'))  # False
print(is_palindrome('a man aplan a canal panama'))  # True


def is_palindrome2(string):
    striped = string.replace(" ", "")
    return striped == striped[::-1]


print(is_palindrome2('testing'))  # False
print(is_palindrome2('tacocat'))  # True
print(is_palindrome2('hannah'))  # True
print(is_palindrome2('robert'))  # False
print(is_palindrome2('a man aplan a canal panama'))  # True
