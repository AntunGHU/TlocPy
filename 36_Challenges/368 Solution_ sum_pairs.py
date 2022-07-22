# Write a function called sum_pairs which accepts a list and a number and returns the first pair of numbers that sum to the number passed to the function.

def sum_pairs(ints, s):
    already_visited = set()
    for i in ints:
        difference = s - i
        if difference in already_visited:
            return [difference, i]
        already_visited.add(i)
    return []


print(sum_pairs([4, 2, 10, 5, 1], 6))  # [4,2]
print(sum_pairs([11, 20, 4, 2, 1, 5], 100))  # []
