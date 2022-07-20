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

# with open("pets.pickle", "wb") as file:
#    pickle.dump(blue, file)


with open("pets.pickle", "rb") as file:
    zombie_blue = pickle.load(file)
    print(zombie_blue)
    zombie_blue.play()

# ako picklamo vise stvari odjednom tada i unpicklanje moramo raditi istim redom!

# ? with open("pets.pickle", "wb") as file:
# ?    pickle.dump((blue, rusty), file)

# ? with open("pets.pickle", "rb") as file:
# ?    zombie_blue, zombie_rusty = pickle.load(file)
# ?    print(zombie_blue)
# ?    print(zombie_rusty)
# ?    print(zombie_blue.play())

# Sto god se unpickla to se odmah izvodi pa zato treba biti vrlo oprezanmi ne unpicklati data iz nepoznatih izvora!! ili imput od usera!
