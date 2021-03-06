# snimit cemo podatke scrapanja u csv-fajl tako da tjekom igre pozezemo citate iz njega. Njega cemo nadopunjavati npr jedanput tjedno
# takodjer cemo tu funkcionalnost napraviti u posebnom py-fajlu jer ne zelimo svaki put kad igramo snimati u csv-fajl.
# kopiramo sve od početka do def start_game() u taj novi py-fajl
# svaki put kad run-a updejtamo nove citate i upišemo u csv-fajl
# izmjena koja ce uciniti da run ne skrejpa svaki put - refactoring

import requests
from bs4 import BeautifulSoup
from csv import DictWriter
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
                "text": quote.find(class_="text").get_text(),
                "author": quote.find(class_="author").get_text(),
                "bio-link": quote.find("a")["href"]
            })
        next_btn = soup.find(class_="next")
        url = next_btn.find("a")["href"] if next_btn else None
        sleep(1)
    return all_quotes

# write quotes to csv-fajl


def write_quotes(quotes):
    with open("quotes.csv", "w") as file:
        headers = ["text", "author", "bio-link"]
        csv_writer = DictWriter(file, fieldnames=headers)
        csv_writer.writeheader()
        for quote in quotes:
            csv_writer.writerow(quote)


quotes = scrape_quotes()
write_quotes(quotes)
