# SyntaxError:
#! def first:
#           ^
#SyntaxError: invalid syntax

# NameRrror:
#! test
# NameError: name 'test' is not defined

# TypeError:
#! len(5)
# TypeError: object of type 'int' has no len()

# IndexError:
list=[1,2]
#! list[2]
# IndexError: list index out of range

# ValueError:
#! int("foo")
# ValueError: invalid literal for int() with base 10: 'foo'

# KeyError:
d={}
#! d["foo"]
# KeyError: 'foo'

# AttributeError:
#! "awesome".foo
# AttributeError: 'str' object has no attribute 'foo'
#! [1,2,3].hello()
# AttributeError: 'list' object has no attribute 'hello'