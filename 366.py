import sqlite3
from urllib import response
import requests
from bs4 import BeautifulSoup
Urll = "http://books.toscrape.com/catalogue/category/books/history_32/index.html"
# request URL
response = requests.get(Urll)
# inialize BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")
# extract data we want
books = soup.find_all("article")
for book in books:
    title = book.find("h3").find("a")["title"]
    price = book.select(".price_color")[0].get_text()
    price = float(price.replace("£","").replace("Â",""))
    ratings = {"Zero": 0, "One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
    paragraph = book.select(".star-rating")[0]
    rating = paragraph.get_attribute_list("class")[-1]
    int_rating = ratings[rating]
# nakon ovog refactorira u 366a usput mjenjajući nazive nekih varijabli