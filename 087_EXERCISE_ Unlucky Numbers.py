for num in range(1,21):
    if num == 4 or num == 13:
        print(f"Broj {num} je nesretan!")
    elif num % 2 != 0:
        print(f"Broj {num} je neparan!")
    else:
        print(f"Broj {num} je paran!")
        

#! Coltov dodatak

for num in range(1,21):
    if num == 4 or num == 13:
        state = "nesretan!"
    elif num % 2 != 0:
        state = "neparan!"
    else:
        state = "paran"
    print(f"Broj {num} je {state}!")
        
        