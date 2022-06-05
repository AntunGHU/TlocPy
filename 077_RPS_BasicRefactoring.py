print("Rock...")
print("Paper...")
print("Scissors...")

#!  Rock Scissors, Scissors Paper, Paper Rock

player1 = input("Player 1, make your move! ")
player2 = input("Player 2, make your move! ")

if player1 == "rock":
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
elif player1 == player2:
    print("It's a tie!")
else:
    print("something went wrong!?")
    