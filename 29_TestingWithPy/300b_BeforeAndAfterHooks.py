
# Sad pisemo 1. verziju testova koja ce imati ponavljanja!!!

import unittest
from robot import Robot     # veliko sl jer se testira klasa Robot


class RobotTests(unittest.TestCase):
    def test_charge(self):
        mega_man = Robot("Mega Man", battery=50)
        mega_man.charge()
        self.assertEqual(mega_man.battery, 100)

    def test_say_name(self):
        mega_man = Robot("Mega Man", battery=50)    # 1.ponavljanje!!!
        self.assertEqual(mega_man.say_name(), "BEEP, I AM MEGA MAN.")
        self.assertEqual(mega_man.battery, 49)


if __name__ == "__main__":
    unittest.main()

# odrada prve verzije vraca:
# ? $ C:/Users/ajerkovic/AppData/Local/Programs/Python/Python39/python.exe d:/za_PC/py/aCode/TlocPy/29_TestingWithPy/300b_BeforeAndAfterHooks.py -v

# ? test_charge (__main__.RobotTests) ... ok
# ? test_say_name (__main__.RobotTests) ... ok

# ? ----------------------------------------------------------------------
# ? Ran 2 tests in 0.001s

# ? OK

# Medjutim, nakon ovog Ath kaze da ako bi htio testirati citavu klasu Robot, ponovo bi morao pisati novi metod za funkciju "learn_skill" i novu liniju "mega_man" sto bi bilo 2. njeno ponavljanje i 3. pojavljivanje!!!
# E!!! Tu uskace SetUp! ali kao alternativu prije toga napominje mogucnost proglasavanja "mega_man"-a klasnim atributom (crveno u biljeznici). Ali, tada se javlja spomentuti (Mosh) problem globalne varijable gdje testovi-metodi koji koriste klass-atribut ili globalnu varijablu istu mjenjaju te pocetni uvjeti za metode iza njih nisu oni koji se ocekuju i trebaju. Ta verzija ispod


class RobotTests(unittest.TestCase):
    mega_man = Robot("Mega Man", battery=50)

    def test_charge(self):
        self.mega_man.charge()
        self.assertEqual(self.mega_man.battery, 100)

    def test_say_name(self):
        self.assertEqual(self.mega_man.say_name(), "BEEP, I AM MEGA MAN.")
        self.assertEqual(self.mega_man.battery, 49)


if __name__ == "__main__":
    unittest.main()

# SetUp tu prvu (crvenu) liniju rerun-a uvijek iznova cime su početni uvjeti uvjek oni potrebni. Verzija sa SetUpom ispod:


class RobotTests(unittest.TestCase):
    def setUp(self):
        self.mega_man = Robot("Mega Man", battery=50)

    def test_charge(self):
        self.mega_man.charge()
        self.assertEqual(self.mega_man.battery, 100)

    def test_say_name(self):
        self.assertEqual(self.mega_man.say_name(), "BEEP, I AM MEGA MAN.")
        self.assertEqual(self.mega_man.battery, 49)


if __name__ == "__main__":
    unittest.main()


# Recap
# ____Tests help streamline development and reduce bugs
# ____You can start with tests if doing TDD / Red, Green, Refactor
# ____You can perform simple checks with assert
# ____You can test with doctests, but typically shouldn't
# ____unittest is a feature-rich, OOP style testing library in Python
# ____To reduce code duplication in tests, use before/after hooks!
