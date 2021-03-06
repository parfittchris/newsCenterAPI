import scrapy
import json
from datetime import datetime


class FoxSpider(scrapy.Spider):
    name = "fox"


    start_urls = [
        'https://www.foxnews.com'
    ]

    def parse(self, response):
        counter = 1
        time = datetime.now()

        with open('./data/fox_articles.json', 'w') as f:
            for item in response.xpath('//h2[@class="title title-color-default"]'):
                number = str(counter) 
                title = item.css('a::text').get()
                url = item.css('a::attr(href)').get()

                if 'video' in url:
                    continue

                article = {
                    'number': number,
                    'title': title,
                    'url': url,
                    'site': 'Fox',
                    'time': time.strftime("%m/%d/%Y, %H:%M:%S")
                }

                extract = json.dumps(article)
                f.write(extract+'\n')
                counter += 1



