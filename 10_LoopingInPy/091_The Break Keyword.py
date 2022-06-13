while True:
    command = input("Type 'e' to exit: ")
    if command == "e":
        break
    
for x in range (1,101):
    print(x)
    if x == 55:
        break
    
times = int(input("How many times do I have to tell you?"))
for time in range(1,times+1):
    print("CLEAN UP YOUR ROOM!")
    if time >= 4:
        print("Do you even listen to me?")
        break
#! izbacuje 5 puta jer range pocinje od nule te je jednak 4 tek poslije 5. printanja: korekcija sa (1,times+1)

#! prikaz coltovog kod kojeg je smanjivao times na 3 itd
times = int(input("How many times do I have to tell you?"))
for time in range(times):
    print("CLEAN UP YOUR ROOM!")
    if time >= 4:
        print("Do you even listen to me?")
        break