import scrapy
import json


class FoxSpider(scrapy.Spider):
    name = "nytimes"

    start_urls = [
        'https://www.nytimes.com/'
    ]

    def parse(self, response):
        counter = 1
        with open('../data/nytimes_articles.json', 'w') as f:
            for item in response.xpath('//a'):
                number = str(counter)
                title = item.css('h2::text').get()
                url = item.css('a::attr(href)').get()

                if title:
                    article = {
                        'number': number,
                        'title': title,
                        'url': url,
                        'site': 'nytimes'
                    }

                    extract = json.dumps(article)
                    f.write(extract+'\n')
                    counter += 1

