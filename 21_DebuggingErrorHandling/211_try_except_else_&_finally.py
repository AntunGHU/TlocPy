# 11'18''
# ako run-a except ne run-a else i obrnuto. Finally ide sa oba!

try:
    num = int(input("please, enter a number: "))
except:
    print("That's not a number!")
else:
    print("I AM IN THE ELSE!")
finally:
    print("RUNS NO MATTER WHAT!")

# Kako bi imalo vise smisla malo izmjena:

while True:
    try:
        num=int(input("please enter a number: "))
    except ValueError:
        print("That's not a number!")
    else:
        print("Good job! you entered a number!")
        break
    finally:
        print("RUNS NO MATTER WHAT!")
print("REST OF THE GAME'S LOGIC5")