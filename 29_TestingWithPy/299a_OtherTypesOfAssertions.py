# 9'21

# Ath pokazuje jos neke (True, NotEqual itd) ubacujuci nove funkcije sa pass, dovrsavajuci korespondentne test-djelove a potom green-anjem koda funkcija ubacujuci kod u mjesto pass-a.
# self.assertEqual(x, y); self.assertNotEqual(x, y); self.assertTrue(x); self.assertFalse(x); self.assertIsNone(x); self.assertIsNotNone(x); self.assertIn(x, y); self.assertNotIn(x, y); ...and more!

from activities import eat, is_funny, nap
import unittest


class ActivitiesTests(unittest.TestCase):
    def test_eat_healthy(self):
        """testing eat function healthy"""
        self.assertEqual(
            eat("broccoli", is_healthy=True),
            "I'm eating broccoli because my body is a temple!"
        )

    def test_eat_unhealthy(self):
        """testing eat function unhealthy"""
        self.assertEqual(
            eat("pizza", is_healthy=False),
            "I'm eating pizza because YOLO!"
        )

    def test_short_nap(self):
        """testing nap function 1 hour sleep"""
        self.assertEqual(
            nap(1),
            "I'm feeling refreshed after my 1 hour nap!"
        )

    def test_long_nap(self):
        """testing nap function 3 hours sleep"""
        self.assertEqual(
            nap(3),
            "Ugh, I overslept. I didn't meant to sleep so long!"
        )

    def test_is_funny_tim(self):
        """testing is_funny function"""
        self.assertEqual(
            is_funny("tim"),
            False
        )

    def test_is_funny_anyone_else(self):
        """testing is_funny_anyone_else function, anyone else but tim should be funny"""
        self.assertTrue(
            is_funny("blue"),
            "blue should be funny"
        )
        self.assertTrue(
            is_funny("tammy"),
            "tammy should be funny"
        )
        self.assertTrue(
            is_funny("sven"),
            "sven should be funny"
        )


if __name__ == "__main__":
    unittest.main()

# bez green-anja funkcija test daje:

# ? .... /bin/python3 /home/antun/Documents/aCod/TlocPy/29_TestingWithPy/299_OtherTypesOfAssertions.py -v
# ? ....
# ? .... test_eat_healthy (__main__.ActivitiesTests)
# ? .... testing eat function healthy ... ok
# ? .... test_eat_unhealthy (__main__.ActivitiesTests)
# ? .... testing eat function unhealthy ... ok
# ? .... test_is_funny_anyone_else (__main__.ActivitiesTests)
# ? .... testing is_funny_anyone_else function, anyone else but tim should be funny ... ERROR
# ? .... test_is_funny_tim (__main__.ActivitiesTests)
# ? .... testing is_funny function ... ERROR
# ? .... test_long_nap (__main__.ActivitiesTests)
# ? .... testing nap function 3 hours sleep ... ok
# ? .... test_short_nap (__main__.ActivitiesTests)
# ? .... testing nap function 1 hour sleep ... ok
# ? ....
# ? .... ======================================================================
# ? .... ERROR: test_is_funny_anyone_else (__main__.ActivitiesTests)
# ? .... testing is_funny_anyone_else function, anyone else but tim should be funny
# ? .... ----------------------------------------------------------------------
# ? .... Traceback (most recent call last):
# ? ....   File "/home/antun/Documents/aCod/TlocPy/29_TestingWithPy/299_OtherTypesOfAssertions.py", line 48, in test_is_funny_anyone_else
# ? ....     is_funny("blue"),
# ? .... NameError: name 'is_funny' is not defined
# ? ....
# ? .... ======================================================================
# ? .... ERROR: test_is_funny_tim (__main__.ActivitiesTests)
# ? .... testing is_funny function
# ? .... ----------------------------------------------------------------------
# ? .... Traceback (most recent call last):
# ? ....   File "/home/antun/Documents/aCod/TlocPy/29_TestingWithPy/299_OtherTypesOfAssertions.py", line 41, in test_is_funny_tim
# ? ....     is_funny("tim"),
# ? .... NameError: name 'is_funny' is not defined
# ? ....
# ? .... ----------------------------------------------------------------------
# ? .... Ran 6 tests in 0.001s
# ? ....
# ? .... FAILED (errors=2)

# nakon green-a i dodane funkcije is_funny

# ? .... antun@ub:~/Documents/aCod/TlocPy$ /bin/python3 /home/antun/Documents/aCod/TlocPy/29_TestingWithPy/299_OtherTypesOfAssertions.py -v

# ? .... test_eat_healthy (__main__.ActivitiesTests)
# ? .... testing eat function healthy ... ok
# ? .... test_eat_unhealthy (__main__.ActivitiesTests)
# ? .... testing eat function unhealthy ... ok
# ? .... test_is_funny_anyone_else (__main__.ActivitiesTests)
# ? .... testing is_funny_anyone_else function, anyone else but tim should be funny ... ok
# ? .... test_is_funny_tim (__main__.ActivitiesTests)
# ? .... testing is_funny function ... ok
# ? .... test_long_nap (__main__.ActivitiesTests)
# ? .... testing nap function 3 hours sleep ... ok
# ? .... test_short_nap (__main__.ActivitiesTests)
# ? .... testing nap function 1 hour sleep ... ok
# ? ....
# ? .... ----------------------------------------------------------------------
# ? .... Ran 6 tests in 0.000s
# ? ....
# ? .... OK
