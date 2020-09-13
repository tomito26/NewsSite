from flask import render_template
from app import app
from .request import get_news

#views 
@app.route('/')
def index():
    '''
    View root page function that returns page and its data
    '''
    # Getting sources
    politics = get_news('politics')
    print(politics)
    business_news = get_news('business')
    sports_news = get_news('sports')
    entertainment_news = get_news('entertainment')
    
    
    title = 'Home - Welcome to News  Updates site to get the latest news'
    return render_template('index.html', title = title,politics = politics,sports = sports_news,business = business_news, entertainment = entertainment_news)
