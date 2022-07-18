# s kodom koji prolazi test! Green_Phase i activities.py promjenjen

from activities import eat, nap
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


if __name__ == "__main__":
    unittest.main()

# povrat za Gren-phase (nap(2))

# ? .... ....
# ? .... ----------------------------------------------------------------------
# ? .... Ran 4 tests in 0.000s
# ? ....
# ? .... OK

# jako sturo izvjesce zato sto nigdje nismo dodavali """ docstringove. Ath pokazuje kako se njihovim dodavanjem u test izvjesce povecava. I ja dodao i primjenio komandu za izvrsenje s prekidacem -v na kraju ((za razliku od -O u assert-testovima)

# ? .... /bin/python3 /home/antun/Documents/aCod/TlocPy/29_TestingWithPy/# ? .... 298c_IntroductionToUnittest.py -v
# ? .... test_eat_healthy (__main__.ActivitiesTests)
# ? .... testing eat function healthy ... ok
# ? .... test_eat_unhealthy (__main__.ActivitiesTests)
# ? .... testing eat function unhealthy ... ok
# ? .... test_long_nap (__main__.ActivitiesTests)
# ? .... testing nap function 3 hours sleep ... ok
# ? .... test_short_nap (__main__.ActivitiesTests)
# ? .... testing nap function 1 hour sleep ... ok

# ? .... ----------------------------------------------------------------------
# ? .... Ran 4 tests in 0.000s

# ? .... OK
