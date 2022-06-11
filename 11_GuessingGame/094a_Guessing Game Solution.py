from random import randint
randbroj = randint(1,10)
print(randbroj)

guess = None
while True:
    guess = int(input("Pogodi broj od 1 do 10! \n"))
    if guess < randbroj:
        print("Prenisko!")
    elif guess > randbroj:
        print("Previsoko!")
    else:
        print("Bravo, pogodak!")
        ponuda = input("Jos jednu partiju? (y/n) \n")
        if ponuda == "n":
            print("Hvala za igranje! Drugi put!")
            break
        else:
            randbroj = randint(1,10)
            print(randbroj)
            guess = None
    
#! Poneki moji dodaci. Takodjer Colt istice da guess ne moramo inicijalizirati prije while-loopa ako je u njemu True!!!