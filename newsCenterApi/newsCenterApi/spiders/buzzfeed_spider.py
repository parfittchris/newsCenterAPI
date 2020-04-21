import scrapy
import json
from datetime import datetime


class BuzzfeedSpider(scrapy.Spider):
    name = "buzzfeed"

    start_urls = [
        'https://www.buzzfeed.com'
    ]

    def parse(self, response):
        counter = 1
        time = datetime.now()

        with open('./data/Buzzfeed_articles.json', 'w') as f:
            for item in response.xpath('//article'):
                number = str(counter)
                title = item.css('a::text').get().lstrip()
                url = item.css('a::attr(href)').get()

                if title:
                    article = {
                        'number': number,
                        'title': title,
                        'url': url,
                        'site': 'Buzzfeed',
                        'time': time.strftime("%m/%d/%Y, %H:%M:%S")
                    }

                    extract = json.dumps(article)
                    f.write(extract+'\n')
                    counter += 1
