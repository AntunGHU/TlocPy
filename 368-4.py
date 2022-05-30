def sum_pairs(ints, s):
    already_visited = set()
    for i in ints:
        difference = s - i
        if difference in already_visited:
            return [difference, i]
        already_visited.add(i)
    return []

print(sum_pairs([4,2,10,5,1], 6)) # [4,2] 
print(sum_pairs([11,20,4,2,1,5], 100)) # []
print(sum_pairs([20,80, 10], 100)) # []