# 9'46

# todo : odziv na kod copirati i pastati u ovaj fajl
# SLIDES
# Getting started with Beautiful Soup
# ? To extract data from HTML, we'll use Beautiful Soup
# ? Install it with pip: python3 -m pip install bs4
# ? Beautiful Soup lets us navigate through HTML with Python
# ? Beautiful Soup does NOT download HTML - for this, we need the requests module!

# BS navigira kroz HTML w/ Py ali ne dld-a HTML, to radi "request"-modul
# Pocinjemo sa inicijalizacijom-parsiranjem BS: #? BeautifulSoup(html_string, "htmpl-parser")
# * Kad je HTML parsiran ima vise nacina navigacije:
# .....By Tag Name
# .....Using find - returns one matching tag
# .....Using find_all - returns a list of matching tags
# * Navigati mozemo i sa CSS-selektorima:
# .....select - returns a list of elements matching a CSS selector
# .....Selector Cheatsheet
# ....._________Select by id of foo: #foo
# ....._________Select by class of bar: .bar
# ....._________Select children: div > p
# ....._________Select descendents: div p

from bs4 import BeautifulSoup
html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")
print(soup)
print(type(soup))
print(soup.body)
print(soup.body.div)
print(soup.find("div"))  # daje isto kao linija prije samo 1. dio
print(soup.find("div"))  # daje isto kao linija prije samo 1. dio
print(soup.find_all("div"))  # lista svih divova
print(soup.find_all("li"))  # lista svih li-ova
print(soup.find(id="first"))  # find_all nema smisla jer je id-samo 1!
print(soup.find_all(class_="special"))  # 2 objekta klase "special"
print(soup.find_all(attrs={"data-example": "yes"}))

d = soup.select("[data-example]")
print(d)

# find an element with an id of foo
soup.find(id="foo")
soup.select("#foo")  #

# find all elements with a class of bar
# careful! "class" is a reserved word in Python
soup.find_all(class_="bar")
soup.select(".bar")

# find all elements with a data
# attribute of "baz"
# using the general attrs kwarg
soup.find_all(attrs={"data-baz": True})
soup.select("[data-baz]")
