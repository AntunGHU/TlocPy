Write a function called intersection. This function should accept two lists and return a list with the values that are in both input lists.



def intersection(l1, l2):
    return [val for val in l1 if val in l2]

intersection([1,2,3], [2,3,4])    #[2,3]
intersection(['a','b','z'], ['x','y','z']) .  # ['z']
