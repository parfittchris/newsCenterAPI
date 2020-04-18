import scrapy
import json


class APSpider(scrapy.Spider):
    name = "ap"

    start_urls = [
        'https://apnews.com/'
    ]

    def parse(self, response):
        counter = 1

        with open('../data/ap_articles.json', 'w') as f:
            for item in response.xpath('//a'):
                number = str(counter)
                title = item.css('h1::text').get()
                url = item.css('a::attr(href)').get()
                
                if title:
                    article = {
                        'number': number,
                        'title': title,
                        'url': 'https://apnews.com' + url,
                        'site': 'AP'
                    }

                    extract = json.dumps(article)
                    f.write(extract+'\n')
                    counter += 1

