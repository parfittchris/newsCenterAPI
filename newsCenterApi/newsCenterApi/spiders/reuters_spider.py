import scrapy
import json
from datetime import datetime


class ReutersSpider(scrapy.Spider):
    name = "reuters"

    start_urls = [
        'https://www.reuters.com/'
    ]

    def parse(self, response):
        counter = 1
        time = datetime.now()

        with open('./data/Reuters_articles.json', 'w') as f:
            for item in response.xpath('//a'):
                number = str(counter)
                title = item.css('h3::text').get()
                url = item.css('a::attr(href)').get()

                if title:
                    article = {
                        'number': number,
                        'title': title,
                        'url': 'https://www.reuters.com' + url,
                        'site': 'Reuters',
                        'time': time.strftime("%m/%d/%Y, %H:%M:%S")
                    }

                    extract = json.dumps(article)
                    f.write(extract+'\n')
                    counter += 1
