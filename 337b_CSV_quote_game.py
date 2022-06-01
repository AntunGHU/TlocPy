# kako bi igrali game-logic ostaje, a dio koji skrejpa mičemo
# kako bi dobili citate iz csv-fajla importamo samo DictReader
# pravimo funkciju read_quotes()
# micemo time modul - ne treba nam

import requests
from bs4 import BeautifulSoup
from csv import DictReader
from random import choice

BASE_URL = "http://quotes.toscrape.com"


def read_quotes(filename):
    with open(filename, "r") as file:
        csv_reader = DictReader(file)
        return list(csv_reader)

def start_game(quotes):
    quote = choice(quotes)
    remaining_guesses = 4
    print("Here's a quote:...")
    print(quote["text"])
    print(quote['author'])      # u testne svrhe

    guess = ''
    while guess.lower() != quote["author"].lower() and remaining_guesses > 0:
        guess = input(f"Who said this quote? Guesses remaining:{remaining_guesses} \n")
        remaining_guesses -=1
        if guess.lower() == quote["author"].lower():
            print("YOU GOT IT RIGHT!")
            break
        if remaining_guesses == 3:
            response = requests.get(f"{BASE_URL}{quote['bio-link']}")
            soup = BeautifulSoup(response.text, "html.parser")
            birth_date = soup.find(class_="author-born-date").get_text()
            birth_place = soup.find(class_="author-born-location").get_text()
            print(f"Here's hint. The author was born on {birth_date} in {birth_place}")
        elif remaining_guesses == 2:
            print(f"Here's hint. The author's first name starts with:{quote['author'][0]}")
        elif remaining_guesses == 1:
            last_initial = quote["author"].split(" ")[1][0]
            print(f"Here's hint. The author's last name starts with:{last_initial}")
        else:
            print(f"Sorry, you ran out of guesses! The answer was {quote['author']}")
    again = ''        
    while again not in ('y', 'yes', 'n', 'no'):
        again = input("Would you like to play again? (y/n)? ")
    if again.lower() in ('yes', 'y'):
        # print("Ok, you play again!")
        return start_game(quotes)
    else:
        print("Ok, good bye! Have a nice day!")
    
quotes = read_quotes("quotes.csv")
start_game(quotes)    