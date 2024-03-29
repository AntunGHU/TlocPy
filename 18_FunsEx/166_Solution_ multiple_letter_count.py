def multiple_letter_count(string):
    return {letter: string.count(letter) for letter in string}


# {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's': 1, 'w': 1}
print(multiple_letter_count("awesome"))
# {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's': 1, 'w': 1}
print(multiple_letter_count("multiple_letter_count"))
