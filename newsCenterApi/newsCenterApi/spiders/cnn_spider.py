import scrapy

class CnnSpider(scrapy.Spider):
    name = "cnn"

    start_urls = [
        'https://www.cnn.com'
    ]


    def parse(self, response):

        for div in response.css('.screaming-banner-text'):
            # print('testing')
            # print(div)
            pass




