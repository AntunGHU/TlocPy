from random import randint

#! prvo poboljsanje samo sa for loopom i uvlakom koda - jos silly jer nezna ni tko pobjedjuje

for time in range(3):
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
        else:
            print("computer wins!")
    elif player == "paper": 
        if computer == "rock":
            print("player wins!")
        else:
            print("computer wins!")
    elif player == "scissors":
        if computer == "rock":
            print("computer wins!")
        else:
            print("player wins!")
    else:
        print("Please, enter valid move!")

