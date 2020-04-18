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
                num = str(counter)
                title = item.css('h1::text').get()
                link = item.css('a::attr(href)').get()
                
                if title:
                    article = {
                        'num': num,
                        'title': title,
                        'link': 'https://apnews.com' + link,
                        'site': 'AP'
                    }

                    extract = json.dumps(article)
                    f.write(extract+'\n')
                    counter += 1

