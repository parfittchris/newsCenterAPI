import scrapy
from ..items import NewscenterapiItem

class CnnSpider(scrapy.Spider):
    name = "fox"

    start_urls = [
        'https://www.foxnews.com'
    ]

    def parse(self, response):
        articles = NewscenterapiItem()

        counter = 1
        for item in response.xpath('//h2[@class="title title-color-default"]'):
            num = str(counter) 
            title = item.css('a::text').get()
            link = item.css('a::attr(href)').get()

            if 'video' in link:
                continue

            articles['num'] = num
            articles['title'] = title
            articles['link'] = link
            articles['site'] = 'Fox'

            yield articles
            counter += 1


        # for item in response.xpath('//li[@class="related-item related-item-color-default"]'):
        #     num = str(counter)
        #     title = item.css('a::text').get()
        #     link = item.css('a::attr(href)').get()
            
        #     article = {
        #         'num': num,
        #         'site': 'Fox',
        #         'title': title,
        #         'link': link
        #     }

        #     yield(article)
        #     counter += 1


