
# urll = "http://quotes.toscrape.com"

import requests
from bs4 import BeautifulSoup
from csv import reader, writer
from time import sleep

# ? prve linije koda
# response = requests.get(urll)
# soup = BeautifulSoup(response.text, "html.parser")
# # print(soup.body)
# quotes = soup.find_all(class_="quote")
# # print(quotes)
# for quote in quotes:
#     # print(quote.find(class_="text"))
#     print(quote.find(class_="text").get_text())

# ? sad Ath reorganizira kod, dodaje iznad response-a varijablu "all_quotes"
# all_quotes = []
# response = requests.get(urll)
# soup = BeautifulSoup(response.text, "html.parser")
# ? sad u grabljenje elemenata sa DK-inspect element, osjencenje
# quotes = soup.find_all(class_="quote")
# for quote in quotes:
#     all_quotes.append({
#         "text":quote.find(class_="text").get_text(),
#         "author":quote.find(class_="author").get_text(),
#         "bio-link":quote.find("a")["href"]
#     })
# print(all_quotes)
# ?  sve potrebno je tu, ali samo s 1. stranice! Da bi dobili sve koristimo Next i DK koji vodi do <a href="/page2"... >li class="next" a ispod >a href="/page..." Sve to k refactu
# next_btn = soup.find(class_="next")
# print(next_btn.find("a")["href"])

# ? Stranica 2 je sljedeci url to scrape tako da s njom moramo nadopuniti osnovni urll kojeg preimenujemo u base_url a stranice postaju url
# base_url = "http://quotes.toscrape.com"
# url = "page/1"
# all_quotes = []
# while url:
#     response = requests.get(f"{base_url}{url}")
#     soup = BeautifulSoup(response.text, "html.parser")
#     quotes = soup.find_all(class_="quote")
#     for quote in quotes:
#         all_quotes.append({
#             "text":quote.find(class_="text").get_text(),
#             "author":quote.find(class_="author").get_text(),
#             "bio-link":quote.find("a")["href"]
#         })
#     next_btn = soup.find(class_="next")
#     url = next_btn.find("a")["href"] if next_btn else None
# print(all_quotes)

# ? Nakon ovog ubacuje ispod response-linije print(f"Now Scraping {base_url}{url}...")
# base_url = "http://quotes.toscrape.com"
# url = "page/1"
# all_quotes = []
# while url:
#     response = requests.get(f"{base_url}{url}")
#     print(f"Now Scraping {base_url}{url}...")
#     soup = BeautifulSoup(response.text, "html.parser")
#     quotes = soup.find_all(class_="quote")
#     for quote in quotes:
#         all_quotes.append({
#             "text":quote.find(class_="text").get_text(),
#             "author":quote.find(class_="author").get_text(),
#             "bio-link":quote.find("a")["href"]
#         })
#     next_btn = soup.find(class_="next")
#     url = next_btn.find("a")["href"] if next_btn else None
# print(all_quotes)

# ? Na kraju jos opreza radi pauziranje prije prelaska na next page sa modulom time i sleep tako da sve skupa na kraju:

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
