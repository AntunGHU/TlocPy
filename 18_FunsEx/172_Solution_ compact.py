# Write a function called compact. This function accepts a list and returns a list of values that are truthy values, without any of the falsey values.


def compact(l):
    return [val for val in l if val]


# [1,2, "All done"]
print(compact([0, 1, 2, "", [], False, {}, None, "All done"]))


def compact2(k):
    thruthy_vals = []
    for val in k:
        if val:
            thruthy_vals.append(val)
    return thruthy_vals


# [1,2, "All done"]
print(compact2([0, 1, 2, "", [], False, {}, None, "All done", "Samson"]))

# ljepo al ne radi!?!? Nije radilo dok sam imao pogresno upisan izraz "thruthy_vals.append[val]"
