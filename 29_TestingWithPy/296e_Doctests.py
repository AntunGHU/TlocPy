# 3) Osjetljivost na white_space: prvo sam liniju sa True namjerno napravio sa jednim space-om iza

def true_that():
    """
    >>> true_that()
    True
    """
    return True

# prije uklanjanja suvisnog spacea

# ? ...... Trying:
# ? ......     true_that()
# ? ...... Expecting:
# ? ......     True
# ? ...... **********************************************************************
# ? ...... File "/home/antun/Documents/aCod/TlocPy/29_TestingWithPy/296e_Doctests.# ? ...... py", line 5, in 296e_Doctests.true_that
# ? ...... Failed example:
# ? ......     true_that()
# ? ...... Expected:
# ? ......     True
# ? ...... Got:
# ? ......     True
# ? ...... 1 items had no tests:
# ? ......     296e_Doctests
# ? ...... **********************************************************************
# ? ...... 1 items had failures:
# ? ......    1 of   1 in 296e_Doctests.true_that
# ? ...... 1 tests in 2 items.
# ? ...... 0 passed and 1 failed.
# ? ...... ***Test Failed*** 1 failures.

 # nakon uklanjanja

# ? ...... Trying:
# ? ......     true_that()
# ? ...... Expecting:
# ? ......     True
# ? ...... ok
# ? ...... 1 items had no tests:
# ? ......     296e_Doctests
# ? ...... 1 items passed all tests:
# ? ......    1 tests in 296e_Doctests.true_that
# ? ...... 1 tests in 2 items.
# ? ...... 1 passed and 0 failed.
# ? ...... Test passed.
