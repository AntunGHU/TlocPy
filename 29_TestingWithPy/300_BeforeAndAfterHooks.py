# 8'15

# setUp and tearDown
# ____For larger applications, you may want similar application state before running tests
# ____setUp runs before each test method
# ____tearDown runs after each test method
# ____Common use cases: adding/removing data from a test database, creating instances of a class
import unittest


class SomeTests(unittest.TestCase):

    def setUp(self):
        # do setup here
        pass

    def test_first(self):
        # setUp runs before
        # tearDown runs after
        pass

    def test_second(self):
        # setUp runs before
        # tearDown runs after
        pass

    def tearDown(self):
        # do teardown here
        pass

# Sljedi primjer koristenja hooks-a na unaprijed pripremljenom primjeru klase Robot:


class Robot:
    pass

    # Recap
    # ____Tests help streamline development and reduce bugs
    # ____You can start with tests if doing TDD / Red, Green, Refactor
    # ____You can perform simple checks with assert
    # ____You can test with doctests, but typically shouldn't
    # ____unittest is a feature-rich, OOP style testing library in Python
    # ____To reduce code duplication in tests, use before/after hooks!
