# Write a function called is_odd_string which returns true if sum of each character's position in the alphabet is odd. For example, "a" is in the first position, "b" is in the second position, and so on. If the sum is even, return false.  NOTE: INDEXING STARTS AT 1.  A is position 1, NOT POSITION 0.

def is_odd_string(string):
    total = sum((ord(c) - 96) for c in string.lower()) or 0
    return total % 2 == 1


print(is_odd_string('a'))  # True
print(is_odd_string('aaaa'))  # False
print(is_odd_string('amazing'))  # True
print(is_odd_string('veryfun'))  # True
print(is_odd_string('veryfunny'))  # False
