# 11'30

# we can write doctests for funcs inside docstrings
# doctests-code looks like REPL >>>
# izvodi se dodavanjem prekidaca " python3 -m doctest -v ime_fajla.py" npr /bin/python3 -m doctest -v /home/antun/Documents/aCod/TlocPy/29_TestingWithPy/296_Doctests.py

def add(a, b):
    """ 
    >>> add(2,3)
    5
    >>> add(200,300)
    500
    """
    # return a*b
    return a+b

# dobio:
# ?...... Trying:
# ?......     add(2,3)
# ?...... Expecting:
# ?......     5
# ?...... **********************************************************************
# ?...... File "/home/antun/Documents/aCod/TlocPy/29_TestingWithPy/296_Doctests.py", line 8, in 296_Doctests.add
# ?...... Failed example:
# ?......     add(2,3)
# ?...... Expected:
# ?......     5
# ?...... Got:
# ?......     6
# ?...... Trying:
# ?......     add(200,300)
# ?...... Expecting:
# ?......     500
# ?...... **********************************************************************
# ?...... File "/home/antun/Documents/aCod/TlocPy/29_TestingWithPy/296_Doctests.py", line 10, in 296_Doctests.add
# ?...... Failed example:
# ?......     add(200,300)
# ?...... Expected:
# ?......     500
# ?...... Got:
# ?......     60000
# ?...... 1 items had no tests:
# ?......     296_Doctests
# ?...... **********************************************************************
# ?...... 1 items had failures:
# ?......    2 of   2 in 296_Doctests.add
# ?...... 2 tests in 2 items.
# ?...... 0 passed and 2 failed.
# ?...... ***Test Failed*** 2 failures.

# nakon ispravke koda
# ?.......Trying:
# ?.......    add(2,3)
# ?.......Expecting:
# ?.......    5
# ?.......ok
# ?.......Trying:
# ?.......    add(200,300)
# ?.......Expecting:
# ?.......    500
# ?.......ok
# ?.......1 items had no tests:
# ?.......    296_Doctests
# ?.......1 items passed all tests:
# ?.......   2 tests in 296_Doctests.add
# ?.......2 tests in 2 items.
# ?.......2 passed and 0 failed.
# ?.......Test passed.
