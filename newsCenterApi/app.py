from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS

import os
import json

app = Flask(__name__)

CORS(app)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

ma = Marshmallow(app)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    site = db.Column(db.String(100))
    title = db.Column(db.String(500))
    url = db.Column(db.String(500))
    number = db.Column(db.Integer)

    def __init__(self, site, title, url, number):
        self.site = site
        self.title = title
        self.url = url
        self.number = number


class ArticleSchema(ma.Schema):
    class Meta:
        fields = ('id', 'site', 'title', 'url', 'number')

article_schema = ArticleSchema()
articles_schema = ArticleSchema(many=True)

def addArticles(organization):
    with open('./data/{}_articles.json'.format(organization)) as f:
        for row in f:
            row = json.loads(row)

            site = row['site']
            title = row['title']
            url = row['url']
            number = row['number']

            current = Article.query.filter(Article.number == number, Article.site == organization).first()
            
            if current:
                current.site = site
                current.title = title
                current.url = url
                current.number = number
                db.session.commit()
            else:
                new_article = Article(site, title, url, number)
                db.session.add(new_article)
                db.session.commit()

@app.route('/', methods=['GET'])
def get_articles():
    all_articles = Article.query.all()
    result = articles_schema.dump(all_articles)
    return jsonify(result)

@app.route('/article', methods=['POST'])
def add_article():
    site = request.json['site']
    title = request.json['title']
    url = request.json['url']
    number = request.json['number']

    new_article = Article(site, title, url, number)

    db.session.add(new_article)
    db.session.commit()

    return article_schema.jsonify(new_article)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

# addArticles('AP')
