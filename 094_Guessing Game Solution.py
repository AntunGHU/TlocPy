#! sam napravio!!!

from random import randint
randnum = randint(1,10)
print(randnum)

guess = int(input("Pogodi broj od 1 do 10! "))
while guess != randnum:
    if guess < randnum:
        print("Prenisko!")
    else:
        print("Previsoko!")
    guess = int(input("Probaj opet! "))
print("Bravo, pogodak! ") 
  
ponuda = input("Jos jednu partiju? (y/n) \n")
# while ponuda not in ("y", "n"):
#     ponuda = input("Jos jednu partiju? (y/n) \n")

if ponuda not in ("y", "n"):
    ponuda = input("Jos jednu partiju? (y/n) \n")
elif ponuda == "n":
    print("Hvala za igranje! Drugi put!")
else:
    guess = int(input("Pogodi broj od 1 do 10! "))
    
