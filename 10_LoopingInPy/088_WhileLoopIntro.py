user_response = input("say magic word! ")
while user_response != "please":
    user_response = input("Ah, ha, ha, you didn't say the magic word: ")
print("Bravo, you guessed my magic word!")


msg = input("What is the secret password? \n")
while msg != "bananas":
    print("WRONG!")
    msg = input("What is the secret password? \n")
print("Bravo!")

for num in range(1, 11):
    print(num)

num = 11
while num <= 20:
    print(num)
    #num += 1
    num += 2
