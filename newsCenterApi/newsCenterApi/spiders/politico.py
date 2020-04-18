import scrapy
import json


class PoliticoSpider(scrapy.Spider):
    name = "politico"

    start_urls = [
        'https://www.politico.com/'
    ]

    def parse(self, response):
        counter = 1
        with open('../data/politico_articles.json', 'w') as f:
            for item in response.xpath('//h3[@class="headline "]'):
                num = str(counter)
                title = item.css('a::text').get()
                link = item.css('a::attr(href)').get()

                article = {
                    'num': num,
                    'title': title,
                    'link': link,
                    'site': 'Politico'
                }

                extract = json.dumps(article)
                f.write(extract+'\n')
                counter += 1


