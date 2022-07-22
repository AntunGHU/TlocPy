# 6'58

# Upis u bazu biti ce bulk. Kod ubacuje ispod funkcije "def scrape_books():". I ja dajem kompletan kod iz Pt1

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


scrape_books(url)  # verzija iz videa

# L27 koju pise u biljeznici, nakon prve izvedbe koda trebam komati, ali kad to probam sve se promjeni ispod u smedje!?! pa nisam
# nakon sveg koda u biljeznici pokaz provjera u sglite>
# > nakon runnera nista kod njega a kod mene: sqlite3.OperationalError: table books already exists - znaci moram komati onaj red gore.
# ali kako god probao kommati uvijek bi se javljala greska "TabError: inconsistent use of tabs and spaces in indentation". Tek kad sam L27 cut-ao fajl je odradio bez greske!!! Nakon toga sam isao provjeravati u sqlite>
# ? sqlite3 books.db
# ? sqlite>.tables  # books
# ? sqlite> sqlite> SELECT * FROM books; # vidi dole
# Sapiens: A Brief History of Humankind|54.23|5
# Unbound: How Eight Technologies Made Us Human, Transformed Society, and Brought Our World to the Brink|25.52|1
# The Age of Genius: The Seventeenth Century and the Birth of the Modern Mind|19.73|1
# Political Suicide: Missteps, Peccadilloes, Bad Calls, Backroom Hijinx, Sordid Pasts, Rotten Breaks, and Just Plain Dumb Mistakes in the Annals of American # Politics|36.28|2
# Thomas Jefferson and the Tripoli Pirates: The Forgotten War That Changed American History|59.64|1
# Zealot: The Life and Times of Jesus of Nazareth|24.7|3
# A Distant Mirror: The Calamitous 14th Century|14.58|3
# 1491: New Revelations of the Americas Before Columbus|21.8|3
# Brilliant Beacons: A History of the American Lighthouse|11.45|3
# "Most Blessed of the Patriarchs": Thomas Jefferson and the Empire of the Imagination|44.48|5
# A Short History of Nearly Everything|52.4|5
# The Rise and Fall of the Third Reich: A History of Nazi Germany|39.67|2
# Catherine the Great: Portrait of a Woman|58.55|4
# The Mathews Men: Seven Brothers and the War Against Hitler's U-boats|42.91|5
# The Hiding Place|55.91|4
# America's War for the Greater Middle East: A Military History|51.22|2
# The Guns of August|14.54|2
# House of Lost Worlds: Dinosaurs, Dynasties, and the Story of Life on Earth|43.7|2
# Sapiens: A Brief History of Humankind|54.23|5
# Unbound: How Eight Technologies Made Us Human, Transformed Society, and Brought Our World to the Brink|25.52|1
# The Age of Genius: The Seventeenth Century and the Birth of the Modern Mind|19.73|1
# Political Suicide: Missteps, Peccadilloes, Bad Calls, Backroom Hijinx, Sordid Pasts, Rotten Breaks, and Just Plain Dumb Mistakes in the Annals of American # Politics|36.28|2
# Thomas Jefferson and the Tripoli Pirates: The Forgotten War That Changed American History|59.64|1
# Zealot: The Life and Times of Jesus of Nazareth|24.7|3
# A Distant Mirror: The Calamitous 14th Century|14.58|3
# 1491: New Revelations of the Americas Before Columbus|21.8|3
# Brilliant Beacons: A History of the American Lighthouse|11.45|3
# "Most Blessed of the Patriarchs": Thomas Jefferson and the Empire of the Imagination|44.48|5
# A Short History of Nearly Everything|52.4|5
# The Rise and Fall of the Third Reich: A History of Nazi Germany|39.67|2
# Catherine the Great: Portrait of a Woman|58.55|4
# The Mathews Men: Seven Brothers and the War Against Hitler's U-boats|42.91|5
# The Hiding Place|55.91|4
# America's War for the Greater Middle East: A Military History|51.22|2
# The Guns of August|14.54|2
# House of Lost Worlds: Dinosaurs, Dynasties, and the Story of Life on Earth|43.7|2
