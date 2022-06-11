print("Rock...")
print("Paper...")
print("Scissors...")

#!  Rock Scissors, Scissors Paper, Paper Rock

player1 = input("Player 1, make your move! ")
print("**** NO CHEATING ***** \n\n" *50)
player2 = input("Player 2, make your move! ")

# if player2 == "rock" or player2 == "paper" or player2 == "scissors": 
#! Ali tada bi morali sve uvlaciti pa Colt odustaje!

if player1 == player2:          #! Py ide po redu i kad naidje na poklapanje staje, a ovo je najcesca mogucnost
    print("It's a tie!")
elif player1 == "rock":
    if player2 == "scissors":
        print("player1 wins!")
    elif player2 == "paper":
        print("player2 wins!")
elif player1 == "paper": 
    if player2 == "rock":
        print("player1 wins!")
    elif player2 == "scissors":
        print("player2 wins!")
elif player1 == "scissors":
    if player2 == "rock":
        print("player2 wins!")
    elif player2 == "paper":
        print("player1 wins!")
else:
    print("something went wrong!?")

#! sve radi ok osim kad samo drugi igrac unese smece - tada se nista ne desava!!!   To bi se moglo rijesiti sa jednim if iznad svega - vidi!