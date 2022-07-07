
# 14'47
#? touch jokes.py
import requests
from random import choice
from pyfiglet import figlet_format
from termcolor import colored  # primjer koji mi je dokazao da nemoram restrtat vsc kako bi modul nakon intala bio prepoznat!

header = figlet_format("DAD JOKE 3000!")
header = colored(header, color="magenta")
print(header)

user_input = input("What would you like to search for? \n")
url="https://icanhazdadjoke.com/search"
res = requests.get(
    url,
    headers={"Accept":"application/json"},
    params={"term":user_input}
).json()

num_jokes=res["total_jokes"] 
results =res["results"]
if num_jokes > 1:
    print(f"I found {num_jokes} jokes about {user_input}. Here's one!")
    print(choice(results)["joke"])
elif num_jokes == 1:
    print(f"I found 1 jokes about {user_input}. Here it is!")
    print(results[0]["joke"])
else:
    print(f"Sorry, couldn't found jokes about {user_input}.")

# sve radilo super!

# What would you like to search for? 
# picture
# I found 1 jokes about picture. Here it is!
# Why was the picture sent to prison? It was framed.

# What would you like to search for? 
# larb
# Sorry, couldn't found jokes about larb.

# What would you like to search for? 
# dog
# I found 12 jokes about dog. Here's one!
# It was raining cats and dogs the other day. I almost stepped in a poodle.