# Issues with doctests
# ________ Syntax is a little strange
# ________ Clutters up our function code
# ________ Lacks many features of larger testing tools
# ________ Tests can be brittle

# primjeri koji isticu neke lose osobine doctestova:

# 1) Vaznost space-a iza zareza u listi i tocnosti u prepisivanju sadrzaja pogreske iz REPL-a kad ocekujemo pad da bi test prosao!
#    """double the values in a list
#    >>> double([1,2,3,4])
#    [1,2,3,4]                              # 1.pada u Red-fazi zbog spacea iza zareza, kad ga dodamo prodje
#    >>> double([])
#    []
#    >>> double(['a','b','c'])
#    ['aa','bb','cc']                       # 2.pada u Red-fazi zbog spacea iza zareza, kad ga dodamo prodje
#    >>> double([True, None])
#    Traceback (most recent call last):     # 3. pada zbog netocnog unosa sadrazaja greske
#    ...
#    TypeError: unsupported operand type(s)for
#    """

def double(values):
    """double the values in a list
    >>> double([1,2,3,4])
    [2, 4, 6, 8]
    >>> double([])
    []
    >>> double(['a','b','c'])
    ['aa', 'bb', 'cc']
    >>> double([True, None])
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
    return [2*el for el in values]

# prvi pokusaj i REPL odgovor:

# ?...... Trying:
# ?......     double([1,2,3,4])
# ?...... Expecting:
# ?......     [2,4,6,8]
# ?...... **********************************************************************
# ?...... File "/home/antun/Documents/aCod/TlocPy/29_TestingWithPy/296c_Doctests.py", line 24, in 296c_Doctests.double
# ?...... Failed example:
# ?......     double([1,2,3,4])
# ?...... Expected:
# ?......     [2,4,6,8]
# ?...... Got:
# ?......     [2, 4, 6, 8]
# ?...... Trying:
# ?......     double([])
# ?...... Expecting:
# ?......     []
# ?...... ok
# ?...... Trying:
# ?......     double(['a','b','c'])
# ?...... Expecting:
# ?......     ['aa','bb','cc']
# ?...... **********************************************************************
# ?...... File "/home/antun/Documents/aCod/TlocPy/29_TestingWithPy/296c_Doctests.py", line 28, in 296c_Doctests.double
# ?...... Failed example:
# ?......     double(['a','b','c'])
# ?...... Expected:
# ?......     ['aa','bb','cc']
# ?...... Got:
# ?......     ['aa', 'bb', 'cc']
# ?...... Trying:
# ?......     double([True, None])
# ?...... Expecting:
# ?......     Traceback (most recent call last):
# ?......     ...
# ?......     TypeError: unsupported operand type(s)for
# ?...... **********************************************************************
# ?...... File "/home/antun/Documents/aCod/TlocPy/29_TestingWithPy/296c_Doctests.py", line 30, in 296c_Doctests.double
# ?...... Failed example:
# ?......     double([True, None])
# ?...... Expected:
# ?......     Traceback (most recent call last):
# ?......     ...
# ?......     TypeError: unsupported operand type(s)for
# ?...... Got:
# ?......     Traceback (most recent call last):
# ?......       File "/usr/lib/python3.8/doctest.py", line 1336, in __run
# ?......         exec(compile(example.source, filename, "single",
# ?......       File "<doctest 296c_Doctests.double[3]>", line 1, in <module>
# ?......         double([True, None])
# ?......       File "/home/antun/Documents/aCod/TlocPy/29_TestingWithPy/296c_Doctests.py", line 35, in double
# ?......         return [2*el for el in values]
# ?......       File "/home/antun/Documents/aCod/TlocPy/29_TestingWithPy/296c_Doctests.py", line 35, in <listcomp>
# ?......         return [2*el for el in values]
# ?......     TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
# ?...... 1 items had no tests:
# ?......     296c_Doctests
# ?...... **********************************************************************
# ?...... 1 items had failures:
# ?......    3 of   4 in 296c_Doctests.double
# ?...... 4 tests in 2 items.
# ?...... 1 passed and 3 failed.
# ?...... ***Test Failed*** 3 failures.

# nakon ispravka reda [1,2,3,4] u [1, 2, 3, 4] i ['aa','bb','cc'] u ['aa', 'bb', 'cc']

# ?...... Trying:
# ?......     double([1,2,3,4])
# ?...... Expecting:
# ?......     [2, 4, 6, 8]
# ?...... ok
# ?...... Trying:
# ?......     double([])
# ?...... Expecting:
# ?......     []
# ?...... ok
# ?...... Trying:
# ?......     double(['a','b','c'])
# ?...... Expecting:
# ?......     ['aa', 'bb', 'cc']
# ?...... ok
# ?...... Trying:
# ?......     double([True, None])
# ?...... Expecting:
# ?......     Traceback (most recent call last):
# ?......     ...
# ?......     TypeError: unsupported operand type(s)for
# ?...... **********************************************************************
# ?...... File "/home/antun/Documents/aCod/TlocPy/29_TestingWithPy/296c_Doctests.py", line 30, in 296c_Doctests.double
# ?...... Failed example:
# ?......     double([True, None])
# ?...... Expected:
# ?......     Traceback (most recent call last):
# ?......     ...
# ?......     TypeError: unsupported operand type(s)for
# ?...... Got:
# ?......     Traceback (most recent call last):
# ?......       File "/usr/lib/python3.8/doctest.py", line 1336, in __run
# ?......         exec(compile(example.source, filename, "single",
# ?......       File "<doctest 296c_Doctests.double[3]>", line 1, in <module>
# ?......         double([True, None])
# ?......       File "/home/antun/Documents/aCod/TlocPy/29_TestingWithPy/296c_Doctests.py", line 35, in double
# ?......         return [2*el for el in values]
# ?......       File "/home/antun/Documents/aCod/TlocPy/29_TestingWithPy/296c_Doctests.py", line 35, in <listcomp>
# ?......         return [2*el for el in values]
# ?......     TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
# ?...... 1 items had no tests:
# ?......     296c_Doctests
# ?...... **********************************************************************
# ?...... 1 items had failures:
# ?......    1 of   4 in 296c_Doctests.double
# ?...... 4 tests in 2 items.
# ?...... 3 passed and 1 failed.
# ?...... ***Test Failed*** 1 failures.

# i konacna verzija nakon unosa tocnog teksta ocekivane pogreske. Tekst sam namjerno ipak malo modificirao tako da su tocke na samo pocetku srednje recenice

# ?...... Trying:
# ?......     double([1,2,3,4])
# ?...... Expecting:
# ?......     [2, 4, 6, 8]
# ?...... ok
# ?...... Trying:
# ?......     double([])
# ?...... Expecting:
# ?......     []
# ?...... ok
# ?...... Trying:
# ?......     double(['a','b','c'])
# ?...... Expecting:
# ?......     ['aa', 'bb', 'cc']
# ?...... ok
# ?...... Trying:
# ?......     double([True, None])
# ?...... Expecting:
# ?......     Traceback (most recent call last):
# ?......     ...
# ?......     TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
# ?...... ok
# ?...... 1 items had no tests:
# ?......     296c_Doctests
# ?...... 1 items passed all tests:
# ?......    4 tests in 296c_Doctests.double
# ?...... 4 tests in 2 items.
# ?...... 4 passed and 0 failed.
# ?...... Test passed.
