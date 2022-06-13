# Another Cleaner RPS Solution
# Here's another potential solution that is much shorter. Rather than individually checking for the conditions that lead to a player2 win, they're all lumped together using the else :

p1 = input("Player 1: rock, paper, or scissors ")
p2 = input("Player 2: rock, paper, or scissors ")
 
if p1 == p2:
    print("Draw")
elif p1 == "rock" and p2 == "scissors":
    print("p1 wins")
elif p1 == "paper" and p2 == "rock":
    print("p1 wins")
elif p1 == "scissors" and p2 == "paper":
    print("p1 wins")
else:
    print("p2 wins")

# The only issue with this version is that it will print "p2 wins" if either user enters an invalid move like "pizza". It doesn't have the error-checking of the previous solution detailed in the video. But as far as the pure RPS logic, this is a clean approach.
# Thanks to Jasper for sharing his version of this #solution.

