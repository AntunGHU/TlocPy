# treba instalati pyfiglet, ucinjeno sa 
#? pip3 install pyfiglet
# What message do you want to print? "Hello World!"
# What color? magenta

# codiranje bez func
from pyfiglet import figlet_format
from termcolor import colored

valid_colors = ("red", "green", "yellow", "black")

msg = input("What would you like to print? ")
color = input("In what color? ")

if color not in valid_colors:
    color = "blue"
    
ascii_art = figlet_format(msg)
colored_ascii = colored(ascii_art, color=color)
print(colored_ascii)
# radi ali ne boja!

# sa funkcijom
def print_art(msg, color):
    valid_colors = ("red", "green", "yellow", "black")
    if color not in valid_colors:
        color = "blue"
    ascii_art = figlet_format(msg)
    colored_ascii = colored(ascii_art, color=color)
    print(colored_ascii)
msg = input("What would you like to print? ")
color = input("In what color? ")
print_art(msg, color)

    