import urllib.request,json
from .models import News,Articles


#Getting api key
apiKey = None

# Getting base url 
base_url = None
base_url_articles = None

def configure_request(app):
    global apiKey,base_url,base_url_articles
    apiKey = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    base_url_articles = app.config['ARTICLES_API_BASE_URL']
    
def get_news(lang):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(lang,apiKey)
    # print(get_news_url)
    
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        # print(get_news_response)
        
        news_sources = None
        
        if get_news_response['sources']:
            news_sources_list = get_news_response['sources']
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
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
    
        
        
        if id:
            news_object = News(id,name,description)
            news_sources.append(news_object)
            
        
    return news_sources


def  get_articles(id):
    get_articles_url = base_url_articles.format(id,apiKey)
    
    
    
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)
        
        news_articles = None
        
        if get_articles_response['articles']:
            news_articles_list =  get_articles_response['articles']
            news_articles = process_articles(news_articles_list)
        # print(news_articles_list)
    return news_articles


def process_articles(article_list):
    '''
    FUnction that processes the news results and transform them to a list of objects
    
    Args:
        news_list: A list of dictionaries that contains movie objects
        
    Returns : 
        news_results : Alist of news objects
    '''
    
    news_articles = []
    
    for article_item in article_list:
        id = article_item.get('id')
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url =article_item.get('url')
        urlToImage  = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')
        # print(urlToImage)
       
        if urlToImage:
            article_object = Articles(author,title,description,url,urlToImage,publishedAt)
            news_articles.append(article_object)
            
        
    return news_articles
