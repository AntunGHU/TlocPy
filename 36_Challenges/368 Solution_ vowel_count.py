# Write a function called vowel_count that accepts a string and returns a dictionary with the keys as the vowels and values as the count of times that vowel appears in the string.

def vowel_count(string):
    lower_s = string.lower()
    return {letter: lower_s.count(letter) for letter in lower_s if letter in "aeiou"}


print(vowel_count('awesome'))  # {'a': 1, 'e': 2, 'o': 1}
print(vowel_count('Elie'))  # {'e': 2, 'i': 1}
print(vowel_count('Colt'))  # {'o': 1}
