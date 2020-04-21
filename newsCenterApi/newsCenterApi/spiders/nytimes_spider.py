import scrapy
import json
from datetime import datetime



class FoxSpider(scrapy.Spider):
    name = "nytimes"

    start_urls = [
        'https://www.nytimes.com/'
    ]

    def parse(self, response):
        time = datetime.now()

        counter = 1
        with open('./data/nytimes_articles.json', 'w') as f:
            
            for item in response.xpath('//article'):
                number = str(counter)
                title = item.css('h2::text').get()
                url = item.css('a::attr(href)').get()


                if title and not title == ' ':
                    article = {
                        'number': number,
                        'title': title,
                        'url': url,
                        'site': 'nytimes',
                        'time': time.strftime("%m/%d/%Y, %H:%M:%S")
                    }

                    extract = json.dumps(article)
                    f.write(extract+'\n')
                    counter += 1

