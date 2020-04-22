# News Center Backend - Webscraper and API for news articles on popular news sites



## Background and Overview
This app serves as the backend api for my News Center app (https://github.com/parfittchris/newscenter_app). It was built in Flask with the webscraping itself done using Scrapy. Note: This is Version 2 of this app, rebuilt to use Scrapy. The original version using Selenium to scrape is located here: https://github.com/parfittchris/newsCenterBackend.


## Features

### Web Scraper
Uses Scrapy to currently scrape Fox News, AP, Politico, Buzzfeed and NY Times home pages for their front page headlines and links. The results are first published as json files and then those files are parsed and their data stored in a SQLite database. Any organization prohibiting their content from being scraped was not used.

Typical scraping method:
```
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
 ```
 
 
### Flask API
Main app and api built using Flask. Article count per organization are captured and existing database articles are first replaced with new ones before new ones are added. 

```
def addArticles(organization):
    with open('./data/{}_articles.json'.format(organization)) as f:
        for row in f:
            row = json.loads(row)

            site = row['site']
            title = row['title']
            url = row['url']
            number = row['number']
            time = row['time']
            
            current = Article.query.filter(Article.number == number, Article.site == organization).first()
            
            if current:
                current.site = site
                current.title = title
                current.url = url
                current.number = number
                current.time = time
                db.session.commit()
            else:
                new_article = Article(site, title, url, number, time)
                db.session.add(new_article)
                db.session.commit()
   ```
   
   ## Future Updates
   * Add more websites and script to automatically update database.



 
