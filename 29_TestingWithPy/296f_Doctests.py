# 4) sortiranje kljuceva dict-a tijekom testiranja - razlika expected i got

def make_dict(keys):
    """
    >>> make_dict(['a', 'b'])
    {'a': True, 'b': True}
    """
    return {key: True for key in keys}

# dict je unordered collection of items i poredak koji smo stavili u "expected" {'b':True, 'a':True} ne bi trebao nista zanciti ali

# ? ..... Trying:
# ? .....     make_dict(['a', 'b'])
# ? ..... Expecting:
# ? .....     {'b':True, 'a':True}
# ? ..... **********************************************************************
# ? ..... File "/home/antun/Documents/aCod/TlocPy/29_TestingWithPy/296f_Doctests.py", line 5, in 296f_Doctests.make_dict
# ? ..... Failed example:
# ? .....     make_dict(['a', 'b'])
# ? ..... Expected:
# ? .....     {'b':True, 'a':True}
# ? ..... Got:
# ? .....     {'a': True, 'b': True}
# ? ..... 1 items had no tests:
# ? .....     296f_Doctests
# ? ..... **********************************************************************
# ? ..... 1 items had failures:
# ? .....    1 of   1 in 296f_Doctests.make_dict
# ? ..... 1 tests in 2 items.
# ? ..... 0 passed and 1 failed.
# ? ..... ***Test Failed*** 1 failures.

# tek nakon ispravke expecteda sa {'b':True, 'a':True} na {'a': True, 'b': True} test prolazi i dobijam:

# ? ..... Trying:
# ? .....     make_dict(['a', 'b'])
# ? ..... Expecting:
# ? .....     {'a': True, 'b': True}
# ? ..... ok
# ? ..... 1 items had no tests:
# ? .....     296f_Doctests
# ? ..... 1 items passed all tests:
# ? .....    1 tests in 296f_Doctests.make_dict
# ? ..... 1 tests in 2 items.
# ? ..... 1 passed and 0 failed.
# ? ..... Test passed.
