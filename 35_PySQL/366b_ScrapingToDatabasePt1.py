# dok sam u a-verziji prikazao predfunkcijski kod ovdje pokazujem reorganitzaciju tog koda u funkcije. Osnova je prilozeni fajl "366 book-scraper.py".
# Razlika tog fajla i onog sto sam ja stvorio gledajuci video je u tome sto je Ath url izdvojio u varijablu url i koristio je na kraju. Tako sam i ja u ovom zapisu.
# Takodjer razlika je i u tom sto je u videu Pt1 samo napomenuo da ce u Pt2 raditi na kodu za upis scrapanja u bazu "def save_books(all_books):" te ga ovdje samo napominje i pokazuje mu mjesto u ukupnom kodu. Ja sam to odmah ipak stavio ovdje sve.

import sqlite3
import requests
from bs4 import BeautifulSoup
url = "http://books.toscrape.com/catalogue/category/books/history_32/index.html"

# Request URl


def scrape_books(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article")
    all_books = []
    for book in books:
        book_data = (get_title(book), get_price(book), get_rating(book))
        all_books.append(book_data)
    save_books(all_books)


def save_books(all_books):
    connection = sqlite3.connect("books.db")
    c = connection.cursor()
    c.execute('''CREATE TABLE books 
		(title TEXT,price REAL,rating INTEGER)''')
    c.executemany("INSERT INTO books VALUES (?,?,?)", all_books)
    connection.commit()
    connection.close()


def get_title(book):
    return book.find("h3").find("a")["title"]


def get_price(book):
    price = book.select(".price_color")[0].get_text()
    return float(price.replace("£", "").replace("Â", ""))


def get_rating(book):
    ratings = {"Zero": 0, "One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
    paragraph = book.select(".star-rating")[0]
    word = paragraph.get_attribute_list("class")[-1]
    return ratings[word]


scrape_books(url)  # verzija iz videa sa url-varijablom
# Initialize BS
# Extract Data we Want
# Save data to database
