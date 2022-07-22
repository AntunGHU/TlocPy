# 20'01

# Primjer koristenja py-a u dinamickom zapisivanju podataka u bazu tijekom scrapanja WebSite-a sa cijenama i rejtinzima knjiga!
# Sav kod Ath dostavlja u pratecem fajlu "366 book-scraper.py" kojeg i ja kopiram kao osnovu svojih tekst-napomena

import sqlite3
from turtle import title
import requests
from bs4 import BeautifulSoup
urll = "http://books.toscrape.com/catalogue/category/books/history_32/index.html"

# Request URl
response = requests.get(url)

# inicijalizacija BeautifulSoup-a
soup = BeautifulSoup(response.text, "html.parser")

# exctract data we want
books = soup.find_all("article")
for book in books:
    title = book.find("h3").find("a")["title"]
    price = book.select(".price_color")[0].get_text()
    price = float(price.replace("£", "").replace("Â", ""))
    ratings = {"Zero": 0, "One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
    paragraph = book.select(".star-rating")[0]
    rating = paragraph.get_attribute_list("class")[-1]
    int_rating = ratings[rating]
# Sad kad je dobio naslov, cjene i ratings ide u reorganizaciju koda u funkcije. U zapisima sam komentirao a ovdje cu jednostavno stvoriti sa SaveAs b-verziju.
