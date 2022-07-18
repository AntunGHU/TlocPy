# another doctests Example
# Run these tests with comand:
# ? python3 -m doctest -v YOUR_FILE_NAME.py
# znaci prosti klik na runnera nece dostajati, njegova k-da se treba nadopuniti!!! potrebnim " -m doctest -v " djelom
# Test should fail at first - remember "Red, Green, Refactor"


def add(x, y):
    """add together x and y

    >>> add(1, 2)
    3

    >>> add(8, "hi")
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    """
    return x+y


# REPL odgovor kad ima gresku (koman return)

# ?..... Trying:
# ?.....     add(1, 2)
# ?..... Expecting:
# ?.....     3
# ?..... **********************************************************************
# ?..... File "/home/antun/Documents/aCod/TlocPy/29_TestingWithPy/296b_Doctests.py", line 11, in 296b_Doctests.add
# ?..... Failed example:
# ?.....     add(1, 2)
# ?..... Expected:
# ?.....     3
# ?..... Got nothing
# ?..... Trying:
# ?.....     add(8, "hi")
# ?..... Expecting:
# ?.....     Traceback (most recent call last):
# ?.....         ...
# ?.....     TypeError: unsupported operand type(s) for +: 'int' and 'str'
# ?..... **********************************************************************
# ?..... File "/home/antun/Documents/aCod/TlocPy/29_TestingWithPy/296b_Doctests.py", line 14, in 296b_Doctests.add
# ?..... Failed example:
# ?.....     add(8, "hi")
# ?..... Expected:
# ?.....     Traceback (most recent call last):
# ?.....         ...
# ?.....     TypeError: unsupported operand type(s) for +: 'int' and 'str'
# ?..... Got nothing
# ?..... 1 items had no tests:
# ?.....     296b_Doctests
# ?..... **********************************************************************
# ?..... 1 items had failures:
# ?.....    2 of   2 in 296b_Doctests.add
# ?..... 2 tests in 2 items.
# ?..... 0 passed and 2 failed.
# ?..... ***Test Failed*** 2 failures.

# ako ocekujemo gresku onda ju napisemo u doctest pisuci iz REPL-odgovora prvu recenicu, ... 3 tocku u drugu i vrstu greske zadnje recenice REPL-a. Tada test smatra da je dobio sto se ocekivalo i da je prolazan! Vidi gore tekst REPL-a na gornji test:

# i kad prolazi (odkoman return)

# ?...... Trying:
# ?......     add(1, 2)
# ?...... Expecting:
# ?......     3
# ?...... ok
# ?...... Trying:
# ?......     add(8, "hi")
# ?...... Expecting:
# ?......     Traceback (most recent call last):
# ?......         ...
# ?......     TypeError: unsupported operand type(s) for +: 'int' and 'str'
# ?...... ok
# ?...... 1 items had no tests:
# ?......     296b_Doctests
# ?...... 1 items passed all tests:
# ?......    2 tests in 296b_Doctests.add
# ?...... 2 tests in 2 items.
# ?...... 2 passed and 0 failed.
# ?...... Test passed.
