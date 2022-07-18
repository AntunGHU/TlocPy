# dodavanje 8. testa i modificirane funkcije za provjeru pojave i odrade ERROR-a

from activities import eat, is_funny, laugh, nap
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

    def test_eat_healthy_boolean(self):
        """is_healthy must be a bool"""
        with self.assertRaises(ValueError):
            eat('pizza', is_healthy="who cares?")

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

    def test_laugh(self):
        """testing laugh function"""
        self.assertIn(
            laugh(),
            ('lol', 'hahaha', 'thehehe')
        )

    # def test_for_error(self):
    #     """testing for errors"""
    #     with self.assertRaises(IndexError):
    #         l = [1, 2, 3]
    #         l[100]


if __name__ == "__main__":
    unittest.main()

# red faza

# ? test_eat_healthy (__main__.ActivitiesTests)
# ? testing eat function healthy ... ok
# ? test_eat_healthy_boolean (__main__.ActivitiesTests)
# ? is_healthy must be a bool ... FAIL
# ? test_eat_unhealthy (__main__.ActivitiesTests)
# ? testing eat function unhealthy ... ok
# ? test_is_funny_anyone_else (__main__.ActivitiesTests)
# ? testing is_funny_anyone_else function, anyone else but tim should be funny ... ok
# ? test_is_funny_tim (__main__.ActivitiesTests)
# ? testing is_funny function ... ok
# ? test_laugh (__main__.ActivitiesTests)
# ? testing laugh function ... ok
# ? test_long_nap (__main__.ActivitiesTests)
# ? testing nap function 3 hours sleep ... ok
# ? test_short_nap (__main__.ActivitiesTests)
# ? testing nap function 1 hour sleep ... ok
# ?
# ? ======================================================================
# ? FAIL: test_eat_healthy_boolean (__main__.ActivitiesTests)
# ? is_healthy must be a bool
# ? ----------------------------------------------------------------------
# ? Traceback (most recent call last):
# ?   File "/home/antun/Documents/aCod/TlocPy/29_TestingWithPy/299c_OtherTypesOfAssertions.py", line 25, in test_eat_healthy_boolean
# ?     eat('pizza', is_healthy="who cares?")
# ? AssertionError: ValueError not raised
# ?
# ? ----------------------------------------------------------------------
# ? Ran 8 tests in 0.001s
# ?
# ? FAILED (failures=1)

# green

# ? antun@ub:~/Documents/aCod/TlocPy$ /bin/python3 /home/antun/Documents/aCod/TlocPy/29_TestingWithPy/299c_OtherTypesOfAssertions.py -v
# ?
# ? test_eat_healthy (__main__.ActivitiesTests)
# ? testing eat function healthy ... ok
# ? test_eat_healthy_boolean (__main__.ActivitiesTests)
# ? is_healthy must be a bool ... ok
# ? test_eat_unhealthy (__main__.ActivitiesTests)
# ? testing eat function unhealthy ... ok
# ? test_is_funny_anyone_else (__main__.ActivitiesTests)
# ? testing is_funny_anyone_else function, anyone else but tim should be funny ... ok
# ? test_is_funny_tim (__main__.ActivitiesTests)
# ? testing is_funny function ... ok
# ? test_laugh (__main__.ActivitiesTests)
# ? testing laugh function ... ok
# ? test_long_nap (__main__.ActivitiesTests)
# ? testing nap function 3 hours sleep ... ok
# ? test_short_nap (__main__.ActivitiesTests)
# ? testing nap function 1 hour sleep ... ok
# ?
# ? ----------------------------------------------------------------------
# ? Ran 8 tests in 0.000s
# ?
# ? OK
