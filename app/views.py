from flask import render_template
from app import app
from .request import get_news

#views 
# @app.route('/news')
# def news():
#     '''
#     View root page function that returns page and its data
#     '''
#     # Getting sources
#     politics = get_news('politics')
#     print(politics)
#     business_news = get_news('business')
#     sports_news = get_news('sports')
#     entertainment_news = get_news('entertainment')
    
    
#     title = 'Home - Welcome to best  News  Updates site '
#     return render_template('news.html', title = title,politics = politics,sports = sports_news,business = business_news, entertainment = entertainment_news)

@app.route('/sources/<id>')
def source():
    '''
    Views  news page function that returns the news details page and its data
    '''
    sourceNews = get_news('en')
    print(sourceNews)
    title = 'Home - Welcome to News  Updates site to get the latest news'  
    return render_template('source.html', title=title)

@app.route('/')
def index():
    
    language = get_news('en')
    print (language)
    title = 'Home - Welcome to News  Updates site to get the latest news'
    
    return render_template('index.html',en  = language)