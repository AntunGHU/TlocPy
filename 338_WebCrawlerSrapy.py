# Upoznajemo se sa "Scrapy"-em, framework-om za Scrapanje
# url = https://scrapy.org
# instalira se s "pip install scrapy" ili "python3 -m pip install scrapy""
# objedinjuje requests, scraping i pisanje u csv, json
# Jedini uvjet: postovati pravila imenovanja kao npr start_url isl.
# to je zapravo isto svim framsima: lakoca koristenja po cjenu manje fleksibilnosti
# dole malo koda s njihove prve stranice komentiranog

# $ pip install scrapy
# $ cat > myspider.py <<EOF
# import scrapy
# 
# class BlogSpider(scrapy.Spider):
#     name = 'blogspider'
#     start_urls = ['https://www.zyte.com/blog/']
# 
#     def parse(self, response):
#         for title in response.css('.oxy-post-title'):
#             yield {'title': title.css('::text').get()}
# 
#         for next_page in response.css('a.next'):
#             yield response.follow(next_page, self.# parse)
# EOF
# $ scrapy runspider myspider.py


# http://books.toscrape.com/

