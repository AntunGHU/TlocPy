# dodajemo "Play again?" mogućnost na mjesto L:print("AFTER LOOPING")
# refaktoramo u funkciju def start_game(): dio igra a ne i scrap-dio
# pokrecemo funkciju start_game() na samom kraju kao i iz if-a stavljajuci njen poziv na mjesto  komprinta
# stavlja scrape-dio u funciju dcrape_quotes() i identa, prebacuje all_quotes = [] iznad while url (treba mu biti dohvatljiv), a umjesto print(all_quotes) stavlja return(all_quotes). Mičem  print(f"Ukupno {len(all_quotes)} citata!") jer je jasno da je 100!. Iznad poziva "start_game()" stavlja poziv "scrape_quotes()"", snima ga u varijablu "quotes" i nju  stavlja kao argument od "start_game()" ali i kao parametar u def start-game(quotes) i u return start_game(quotes) te mjanja choice(all_qoutes) u choice(quotes)
# mjenja base_url u BASE_URL cisto da naglasi da je on konstanta i ne mjenja se!
# na kraju nakon greske pri kontroli još prebacuje url = "/page/1 u funkciju ispod all_quotes

import requests
from bs4 import BeautifulSoup
from csv import reader, writer
from time import sleep
from random import choice

BASE_URL = "http://quotes.toscrape.com"


def scrape_quotes():
    all_quotes = []
    url = "/page/1"
    while url:
        response = requests.get(f"{BASE_URL}{url}")
        print(f"Now Scraping {BASE_URL}{url}...")
        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.find_all(class_="quote")
        for quote in quotes:
            all_quotes.append({
                "text":quote.find(class_="text").get_text(),
                "author":quote.find(class_="author").get_text(),
                "bio-link":quote.find("a")["href"]      
            })
        next_btn = soup.find(class_="next")
        url = next_btn.find("a")["href"] if next_btn else None
        #  sleep(2)
    return all_quotes

def start_game(quotes):
    quote = choice(quotes)
    remaining_guesses = 4
    print("Here's a quote:...")
    print(quote["text"])
    print(quote['author'])      # u testne svrhe

    guess = ''
    while guess.lower() != quote["author"].lower() and remaining_guesses > 0:
        guess = input(f"Who said this quote? Guesses remaining:     {remaining_guesses} \n")
        remaining_guesses -=1
        if guess.lower() == quote["author"].lower():
            print("YOU GOT IT RIGHT!")
            break
        if remaining_guesses == 3:
            response = requests.get(f"{BASE_URL}{quote['bio-link']}")
            soup = BeautifulSoup(response.text, "html.parser")
            birth_date = soup.find(class_="author-born-date").get_text()
            birth_place = soup.find(class_="author-born-location").get_text()
            print(f"Here's hint. The author was born on {birth_date} in     {birth_place}")
        elif remaining_guesses == 2:
            print(f"Here's hint. The author's first name starts with: {quote    ['author'][0]}")
        elif remaining_guesses == 1:
            last_initial = quote["author"].split(" ")[1][0]
            print(f"Here's hint. The author's last name starts with:    {last_initial}")
        else:
            print(f"Sorry, you ran out of guesses! The answer was {quote    ['author']}")
    again = ''        
    while again not in ('y', 'yes', 'n', 'no'):
        again = input("Would you like to play again? (y/n)? ")
    if again.lower() in ('yes', 'y'):
        # print("Ok, you play again!")
        return start_game(quotes)
    else:
        print("Ok, good bye! Have a nice day!")
    
quotes = scrape_quotes()
start_game(quotes)    