# s kodom koji ne prolazi test!

from activities import eat, nap
import unittest


class ActivitiesTests(unittest.TestCase):
    def test_eat_healthy(self):
        self.assertEqual(
            eat("broccoli", is_healthy=True),
            "I'm eating broccoli because my body is a temple!"
        )

    def test_eat_unhealthy(self):
        self.assertEqual(
            eat("pizza", is_healthy=False),
            "I'am eating pizza because YOLO!"
        )

    def test_short_nap(self):
        self.assertEqual(
            nap(1),
            "I'am feeling refreshed after my 1 hour nap!"
        )

    def test_long_nap(self):
        self.assertEqual(
            nap(3),
            "Ugh, I overslept. I didn't meant to sleep so long!"
        )


if __name__ == "__main__":
    unittest.main()

# povrat za Red-phase

# ? .... FFFF
# ? .... ======================================================================
# ? .... FAIL: test_eat_healthy (__main__.ActivitiesTests)
# ? .... ----------------------------------------------------------------------
# ? .... Traceback (most recent call last):
# ? ....   File "/home/antun/Documents/aCod/TlocPy/29_TestingWithPy/298b_IntroductionToUnittest.py", line 9, in test_eat_healthy
# ? ....     self.assertEqual(
# ? .... AssertionError: None != "I'm eating broccoli because my body is a temple!"

# ? .... ======================================================================
# ? .... FAIL: test_eat_unhealthy (__main__.ActivitiesTests)
# ? .... ----------------------------------------------------------------------
# ? .... Traceback (most recent call last):
# ? ....   File "/home/antun/Documents/aCod/TlocPy/29_TestingWithPy/298b_IntroductionToUnittest.py", line 15, in test_eat_unhealthy
# ? ....     self.assertEqual(
# ? .... AssertionError: None != "I'am eating pizza because YOLO!"

# ? .... ======================================================================
# ? .... FAIL: test_long_nap (__main__.ActivitiesTests)
# ? .... ----------------------------------------------------------------------
# ? .... Traceback (most recent call last):
# ? ....   File "/home/antun/Documents/aCod/TlocPy/29_TestingWithPy/298b_IntroductionToUnittest.py", line 27, in test_long_nap
# ? ....     self.assertEqual(
# ? .... AssertionError: None != "Ugh, I overslept. I didn't meant to sleep so long!"

# ? .... ======================================================================
# ? .... FAIL: test_short_nap (__main__.ActivitiesTests)
# ? .... ----------------------------------------------------------------------
# ? .... Traceback (most recent call last):
# ? ....   File "/home/antun/Documents/aCod/TlocPy/29_TestingWithPy/298b_IntroductionToUnittest.py", line 21, in test_short_nap
# ? ....     self.assertEqual(
# ? .... AssertionError: None != "I'am feeling refreshed after my 1 hour nap!"

# ? .... ----------------------------------------------------------------------
# ? .... Ran 4 tests in 0.000s

# ? .... FAILED (failures=4)
