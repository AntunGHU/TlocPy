from random import randint
player_wins = 0
computer_wins = 0


def display_header():
    print(f"Player Score: {player_wins} Computer Score: {computer_wins}")
    print("Rock...")
    print("Paper...")
    print("Scissors...")


def pick_computer_move():
    rand_num = randint(0, 2)
    if rand_num == 0:
        move = "rock"
    elif rand_num == 1:
        move = "paper"
    else:
        move = "scissors"
    print(f"computer plays {move}")
    return move


def calculate_winner(player, computer):
    global player_wins
    global computer_wins
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


def start_game(winning_score):
    while player_wins < winning_score and computer_wins < winning_score:
        display_header()

        player = input("Player, make your move! ").lower()
        if player == "quit" or player == "q":
            break

        computer = pick_computer_move()
        calculate_winner(player, computer)


def display_winner():
    if player_wins > computer_wins:
        print("CESTITAM, POBJEDIO SI!")
    elif player_wins == computer_wins:
        print(" IT'S A TIE")
    else:
        print("OH NE! COMPAC JE POBJEDIO! :-(")


start_game(3)
display_winner()
