Write a function called compact. This function accepts a list and returns a list of values that are truthy values, without any of the falsey values.


def compact(l):
    return [val for val in l if val]
    
compact([0,1,2,"",[], False, {}, None, "All done"]) # [1,2, "All done"]
