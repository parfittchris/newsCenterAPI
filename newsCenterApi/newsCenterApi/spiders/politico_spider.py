import scrapy
import json
from datetime import datetime

class PoliticoSpider(scrapy.Spider):
    name = "politico"

    start_urls = [
        'https://www.politico.com/'
    ]

    def parse(self, response):
        counter = 1
        time = datetime.now()

        with open('./data/politico_articles.json', 'w') as f:
            for item in response.xpath('//h3[@class="headline "]'):
                number = str(counter)
                title = item.css('a::text').get()
                url = item.css('a::attr(href)').get()

                article = {
                    'number': number,
                    'title': title,
                    'url': url,
                    'site': 'Politico',
                    'time': time.strftime("%m/%d/%Y, %H:%M:%S")
                }

                extract = json.dumps(article)
                f.write(extract+'\n')
                counter += 1


