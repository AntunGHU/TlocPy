urll = "https://www.rithmschool.com/blog"

import requests
from bs4 import BeautifulSoup
from csv import reader, writer

response = requests.get(urll)
soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("article")

with open ("blog.data.csv", "w") as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(["title", "link", "date"])
    
    for article in articles:
        a_tag = article.find("a")
        title = a_tag.get_text()
        url = a_tag['href']
        date = article.find("time")["datetime"]
        csv_writer.writerow([title, url, date])
        
with open ("blog.data.csv") as csv_file:
    csv_reader = reader(csv_file)
    ukupno = -1
    for row in csv_reader:
        print(row)
        ukupno +=1
    print(ukupno)
    
        
