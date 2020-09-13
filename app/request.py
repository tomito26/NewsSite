from app import  app
import urllib.request,json
from .models import news


News = news.News

#Getting api key
apiKey =app.config['NEWS_API_KEY']

# Getting base url 
base_url = app.config['NEWS_API_BASE_URL']

def get_news(searchitem):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(searchitem,apiKey)
    # print(get_news_url)
    
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        # print(get_news_response)
        
        news_sources = None
        
        if get_news_response['articles']:
            news_sources_list = get_news_response['articles']
            news_sources = process_sources(news_sources_list)
        # print(news_sources_list)
        # import pdb; pdb.set_trace()
    return news_sources





def process_sources(news_list):
    '''
    FUnction that processes the news results and transform them to a list of objects
    
    Args:
        news_list: A list of dictionaries that contains movie objects
        
    Returns : 
        news_results : Alist of news objects
    '''
    
    news_sources = []
    
    for news_item in news_list:
        author = news_item.get('author')
        headline = news_item.get('title')
        description = news_item.get('description')
        urltoimage = news_item.get('urlToImage')
        publishAt  =  news_item.get('publishedAt')
        content = news_item.get('content')
        
        
        if urltoimage:
            news_object = News(author,headline,description,urltoimage,publishAt,content)
            news_sources.append(news_object)
            
        
    return news_sources
