# 2) primjer osjetljivosti na 'single'-"double" quotas. Primjer dole izgleda ok i trebao bi proci test ali ne prolazi jer je

def say_hi():
    """
    >>> say_hi()
    'hi'
    """
    return "hi"

# prije ispravka sa "hi" na 'hi'

# ? ...... Trying:
# ? ......     say_hi()
# ? ...... Expecting:
# ? ......     "hi"
# ? ...... **********************************************************************
# ? ...... File "/home/antun/Documents/aCod/TlocPy/29_TestingWithPy/296d_Doctests.# ? ...... py", line 5, in 296d_Doctests.say_hi
# ? ...... Failed example:
# ? ......     say_hi()
# ? ...... Expected:
# ? ......     "hi"
# ? ...... Got:
# ? ......     'hi'
# ? ...... 1 items had no tests:
# ? ......     296d_Doctests
# ? ...... **********************************************************************
# ? ...... 1 items had failures:
# ? ......    1 of   1 in 296d_Doctests.say_hi
# ? ...... 1 tests in 2 items.
# ? ...... 0 passed and 1 failed.
# ? ...... ***Test Failed*** 1 failures.

# nakon ispravka sa "hi" na 'hi'

# ? ...... Trying:
# ? ......     say_hi()
# ? ...... Expecting:
# ? ......     'hi'
# ? ...... ok
# ? ...... 1 items had no tests:
# ? ......     296d_Doctests
# ? ...... 1 items passed all tests:
# ? ......    1 tests in 296d_Doctests.say_hi
# ? ...... 1 tests in 2 items.
# ? ...... 1 passed and 0 failed.
# ? ...... Test passed.
