# 16'57

# Requests + Beautiful Soup Example
# ? Let's scrape data into a CSV!
# ? Goal: Grab all links from Rithm School blog
# ? Data: store URL, anchor tag text, and date

from csv import reader, writer
from bs4 import BeautifulSoup
import requests
urll = "https://www.rithmschool.com/blog"


response = requests.get(urll)
soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("article")

with open("blog.data.csv", "w") as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(["title", "link", "date"])

    for article in articles:
        a_tag = article.find("a")
        title = a_tag.get_text()
        url = a_tag['href']
        date = article.find("time")["datetime"]
        csv_writer.writerow([title, url, date])

with open("blog.data.csv") as csv_file:
    csv_reader = reader(csv_file)
    ukupno = -1
    for row in csv_reader:
        print(row)
        ukupno += 1
    print(ukupno)

# Common Issues with Web Scraping
# ? Gnarly HTML
# ? Code tightly coupled to UI
# ? Sanitizing data after grabbing it
# ? Data that isn't part of HTML, but is loaded later!

# Other Tools for Web Scraping
# ? Scrapy: https://scrapy.org/
# ? Selenium: http://www.seleniumhq.org/

# Scrapy
# ? A more streamlined way to build web crawlers, which can programmatically navigate across multiple pages
# ? Can export to many different file formats from the command line

# Selenium
# ? Allows you to open up a browser window from your code!
# ? Often used with testing
# ? Requires a driver for your browser of choice
# ? Doesn't navigate through the page until all contents have loaded

# Recap
# ? Web scraping is the process of downloading, extracting, and storing data from a web page
# ? It's helpful when there's no other way to grab data you want
# ? Be sure you're allowed to scrape before you do so
# ? BeautifulSoup + requests allow you to scrape websites in Python
# ? Building scrapers can take time up front, but should save you time in the long term
# ? Other helpful tools include Scrapy and Selenium
