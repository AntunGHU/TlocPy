# 7'14

# Pickling (kiseljenje): privremeno bup-anje .py-fajlova u binarni oblik;
# Unpickling: vracanje u kod

# Primjer pohrane jedne instance "blue" u fajl "pets-pickle" s kodom ispod instance

import pickle


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __repr__(self):
        return f"{self.name} is a {self.species}"

    def make_sound(self, sound):
        print(f"this animal says {sound}")


class Cat(Animal):
    def __init__(self, name, breed, toy):
        super().__init__(name, species="Cat")
        self.breed = breed
        self.toy = toy

    def play(self):
        print(f"{self.name} plays with {self.toy}")


blue = Cat("Blue", "Scottish Fold", "String")

# ! npr da nije instanca klase Cat nego deck pokera kojeg bi zelio snimiti u pauzi izmedju dva onoff-a. Mogao bih mozda CSV ali bi morao dobro misliti kako? Cak ni 1 red od "blue" ne treba csv, jedan je red samo! Tu dolazi pickling!!

with open("pets.pickle", "wb") as file:
    pickle.dump(blue, file)

# ! ali ako zelimo citati i koristi fajl dok je u #pickl-formi nece moci - nije citak-binaran
