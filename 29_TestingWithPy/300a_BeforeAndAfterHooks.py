# 8'15

# setUp and tearDown
# ____For larger applications, you may want similar application state before running tests
# ____setUp runs before each test method
# ____tearDown runs after each test method
# ____Common use cases: adding/removing data from a test database, creating instances of a class
from robot.py import Robot
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


# Sljedi primjer koristenja hooks-a na unaprijed pripremljenom primjeru koda klase Robot (dakle obrnut redosljed od prije kad smo prvo pisali test pa fajl koji ga treba zadovoljiti).

class Robot:
    def __init__(self, name, battery=100, skills=[]):
        self.name = name
        self.battery = battery
        self.sklills = skills

    def charge(self):
        self.battery = 100
        return self

    def say_name(self):
        if self.battery > 0:
            self.battery -= 1
            return f"BEEP. I AM {self.name.upper()}."
        return "Low power. Please charge and try again."

    def learn_skill(self, new_skill, cost_to_learn):
        if self.battery >= cost_to_learn:
            self.battery -= cost_to_learn
            self.sklills.append(new_skill)
            return f"WOAH. I KNOW {new_skill.upper()}!"
        return "Insufficient battery. Please charge and try again!"

# Sad pisemo 1. verziju testova koja ce imati ponavljanja!!!


# Recap
# ____Tests help streamline development and reduce bugs
# ____You can start with tests if doing TDD / Red, Green, Refactor
# ____You can perform simple checks with assert
# ____You can test with doctests, but typically shouldn't
# ____unittest is a feature-rich, OOP style testing library in Python
# ____To reduce code duplication in tests, use before/after hooks!
