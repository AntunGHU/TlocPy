# 16'02

# urll = "http://quotes.toscrape.com"

import requests
from bs4 import BeautifulSoup
from csv import reader, writer
from time import sleep
from random import choice

base_url = "http://quotes.toscrape.com"
url = "/page/1"
all_quotes = []
while url:
    response = requests.get(f"{base_url}{url}")
    print(f"Now Scraping {base_url}{url}...")
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all(class_="quote")
    for quote in quotes:
        all_quotes.append({
            "text": quote.find(class_="text").get_text(),
            "author": quote.find(class_="author").get_text(),
            "bio-link": quote.find("a")["href"]
        })
    next_btn = soup.find(class_="next")
    url = next_btn.find("a")["href"] if next_btn else None
    sleep(2)
print(all_quotes)
print(f"Ukupno {len(all_quotes)} citata!")

# ? Slucajni izbor bilo kojeg citata, pogadjanje autora, 4 pokusaja, jos ili ne?

quote = choice(all_quotes)
remaining_guesses = 4
print("Here's a quote:...")
print(quote["text"])
print(quote['author'])      # u testne svrhe
guess = ' '
while guess.lower() != quote["author"].lower() and remaining_guesses > 0:
    guess = input(
        f"Who said this quote? Guesses remaining: {remaining_guesses} \n")
    remaining_guesses -= 1
    if guess.lower() == quote["author"].lower():
        print("YOU GOT IT RIGHT!")
        break
    if remaining_guesses == 3:
        response = requests.get(f"{base_url}{quote['bio-link']}")
        soup = BeautifulSoup(response.text, "html.parser")
        birth_date = soup.find(class_="author-born-date").get_text()
        birth_place = soup.find(class_="author-born-location").get_text()
        print(
            f"Here's hint. The author was born on {birth_date} in {birth_place}")
    elif remaining_guesses == 2:
        print(
            f"Here's hint. The author's first name starts with: {quote['author'][0]}")
    elif remaining_guesses == 1:
        last_initial = quote["author"].split(" ")[1][0]
        print(
            f"Here's hint. The author's last name starts with: {last_initial}")
    else:
        print(
            f"Sorry, you ran out of guesses! The answer was {quote['author']}")

print("After WHILE loop...")
