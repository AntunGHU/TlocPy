# 16'56

# Upoznajemo se sa "Scrapy"-em, framework-om za Scrapanje
# url = https://scrapy.org
# instalira se s "pip install scrapy" ili "python3 -m pip install scrapy""
# objedinjuje requests, scraping i pisanje u csv, json
# Jedini uvjet: postovati pravila imenovanja kao npr start_url isl.
# to je zapravo isto svim framsima: lakoca koristenja po cjenu manje fleksibilnosti
# dole malo koda s njihove prve stranice komentiranog
# ? $ pip install scrapy
# ? $ cat > myspider.py <<EOF
# ? import scrapy
# ?
# ? class BlogSpider(scrapy.Spider):
# ?     name = 'blogspider'
# ?     start_urls = ['https://www.zyte.com/blog/']
# ?
# ?     def parse(self, response):
# ?         for title in response.css('.oxy-post-title'):
# ?             yield {'title': title.css('::text').get()}
# ?
# ?         for next_page in response.css('a.next'):
# ?             yield response.follow(next_page, self.# parse)
# ? EOF
# ? $ scrapy runspider myspider.py
# ima vrlo dobru dokumentaciju za razliku mnogih drugih py-things
# :-( import uspjesan jedino sa 3.8
# pokretanje zahtjeva c-du: "scrapy runspider -o books.csv book_scraper.py" ja cu prvo probat iz vsc
# iz vsc automatski nije dalo rezultata pa sam k-du izveo iz terminala kao i colt uz ime mojeg pyfajla
# na zalost, uz sve isto moj csv nema nista! a krivac je vjerovatno u pogresnom nazivanju css-elementa
# dokaz tome je sljedeci item "title" koji se uredno pojavio u csv-fajlu!!!
# dodavsi next dobio sam za cas 1000 naslova knjiga!!
# za scrapanje u json fajl samo treba nastavak fajla u k-di za pokretanje promjeniti iz csv u json
# scrapy runspider -o books.json book_scraper.py


# http://books.toscrape.com/

from numpy import extract
import scrapy


class BookSpider(scrapy.Spider):
    name = 'bookspider'
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        for article in response.css('article.product_pod'):
            yield {
                'price': article.css(".price.color::text").extract_first(),
                'title': article.css("h3 > a::attr(title)").extract_first()
            }
            next = response.css('.next > a::attr(href)').extract_first()
            if next:
                yield response.follow(next, self.parse)
