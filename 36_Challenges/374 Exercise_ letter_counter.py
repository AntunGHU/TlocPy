# Write a function called letter_counter which accepts a string and returns a function. When the inner function is invoked it should accept a parameter which is a letter, and the inner function should return the number of times that letter appears. This inner function should be case insensitive.

def letter_counter(s):
    letter_counter.val = s

    def inner(char):
        return len(list(c.lower() for c in letter_counter.val.lower() if c == char))
    return inner


counter = letter_counter('Amazing')
print(counter('a'))  # 2
print(counter('m'))  # 1

counter2 = letter_counter('This Is Really Fun!')
print(counter2('i'))  # 2
print(counter2('t'))  # 1

counter3 = letter_counter('This Is Really Amazing Fun!')
print(counter3('a'))  # 3
print(counter3('i'))  # 3
