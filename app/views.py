from flask import render_template
from app import app
from .request import get_news,get_articles

#views
@app.route('/articles/<id>')
def article(id):
    '''
    Views  article page function that returns the news details page and its data
    '''
    article = get_articles(id)
     
    print(article)
    return render_template('articles.html',article = article)

@app.route('/')
def index():
    
    language = get_news('en')
    # print (language)
    title = 'Home - Welcome to News  Updates site to get the latest news'
    
    return render_template('index.html',en  = language)