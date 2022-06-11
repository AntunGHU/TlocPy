from random import randint

#! drugo s uvodjenjem broja pobjeda i while loopa te rezultata na pocetku i final scorea na kraju
player_wins = 0
computer_wins = 0

while player_wins < 2 and computer_wins <2:
    print(f"Player Score: {player_wins} Computer Score: {computer_wins}")
    print("Rock...")
    print("Paper...")
    print("Scissors...")

    player = input("Player, make your move! ").lower()
    rand_num = randint(0,2)
    if rand_num == 0:
        computer = "rock"
    elif rand_num == 1:
        computer = "paper"
    else:
        computer = "scissors"
    print(f"computer plays {computer}")

    if player == computer:       
        print("It's a tie!")
    elif player == "rock":
        if computer == "scissors":
            print("player wins!")
            player_wins += 1    
        else:
            computer_wins += 1   
            print("computer wins!  :-(")
    elif player == "paper": 
        if computer == "rock":
            player_wins += 1    
            print("player wins!")
        else:
            computer_wins += 1   
            print("computer wins!  :-(")
    elif player == "scissors":
        if computer == "rock":
            computer_wins += 1   
            print("computer wins!  :-(")
        else:
            player_wins += 1    
            print("player wins!")
    else:
        print("Please, enter valid move!")
print(f"Final Scores...Player Score: {player_wins} Computer Score: {computer_wins}")

